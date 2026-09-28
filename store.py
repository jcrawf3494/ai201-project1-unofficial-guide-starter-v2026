"""
Stages 3 and 4 of the pipeline: embedding chunks and retrieving them.

Three things in here are worth knowing about, because they'd quietly break the
rest of the project if they were wrong:

1. The Chroma collection is created with cosine distance, explicitly. Chroma
   defaults to squared L2, and the 0.6 threshold the course uses is calibrated
   against cosine. Getting this wrong makes every distance number meaningless.

2. `search` returns the distance alongside each chunk. Milestone 4 has you
   compare distances, so they have to be visible.

3. The embedding model is the one Chroma bundles, not one loaded through
   `sentence-transformers`. It is the same model — `all-MiniLM-L6-v2`, 384
   dimensions — but it arrives as an ONNX build from Chroma's own CDN, so the
   install needs neither PyTorch nor a reachable Hugging Face. See `_embedder`.
"""

import math
import os
import re
import shutil
from dataclasses import dataclass

# Must be set BEFORE chromadb is imported. Without it, some Chroma versions
# print "Failed to send telemetry event ..." on every single call — which looks
# exactly like a real error, isn't one, and cost a previous cohort a lot of
# confused help-channel messages.
os.environ.setdefault("ANONYMIZED_TELEMETRY", "False")

import chromadb  # noqa: E402
from rank_bm25 import BM25Okapi  # noqa: E402

import config
from chunker import Chunk


@dataclass
class Result:
    """One retrieved chunk and how far it was from the question."""

    text: str
    source: str
    label: str
    distance: float   # LOWER IS BETTER. 0.3 is close, 0.9 is unrelated.
    produced_by: str
    matched_by: str = ""   # "embedding", "bm25", or "both" — set by search()


_model = None

# The model Chroma bundles. Anything else in config.EMBEDDING_MODEL means
# "fetch that one from Hugging Face instead" — see `_embedder`.
BUNDLED_MODEL = "all-MiniLM-L6-v2"


class _OnnxEmbedder:
    """
    Chroma's built-in embedder, wrapped to look like the other two.

    Chroma's embedding functions are called directly and hand back numpy
    arrays. The rest of this file wants `.encode(texts)`, so the adapter lives
    here rather than making every caller care which embedder it got.
    """

    def __init__(self):
        from chromadb.utils.embedding_functions import ONNXMiniLM_L6_V2

        self._ef = ONNXMiniLM_L6_V2()

    def encode(self, texts, show_progress_bar: bool = False):
        return [vector.tolist() for vector in self._ef(list(texts))]


def _sentence_transformer(name: str):
    """
    The escape hatch: any model that isn't the bundled one.

    Unit 2's "try a second embedding model" stretch option comes through here,
    and so does anything you set `EMBEDDING_MODEL` to. This path *does* need
    `sentence-transformers` and a reachable Hugging Face, neither of which the
    default install has — which is the whole point of the default install.
    """
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise RuntimeError(
            f"config.EMBEDDING_MODEL is set to {name!r}, which isn't the model "
            f"Chroma bundles ({BUNDLED_MODEL!r}), so it has to be downloaded "
            f"from Hugging Face.\n"
            f"Install the optional dependency first:\n"
            f"    pip install 'sentence-transformers>=3.4,<3.5'\n"
            f"Or set EMBEDDING_MODEL back to {BUNDLED_MODEL!r}."
        ) from exc

    return SentenceTransformer(name)


def _embedder():
    """
    Load the embedding model once and keep it.

    First call is slow — it downloads about 80 MB. That's why setup happens
    before class.
    """
    global _model

    if _model is not None:
        return _model

    # Used only by this repo's own smoke test, which runs where no model can be
    # downloaded at all. Never set this yourself.
    if os.getenv("AI201_FAKE_EMBEDDINGS") == "1":
        from _smoke_embedder import FakeEmbedder

        _model = FakeEmbedder()
    elif config.EMBEDDING_MODEL == BUNDLED_MODEL:
        _model = _OnnxEmbedder()
    else:
        _model = _sentence_transformer(config.EMBEDDING_MODEL)

    return _model


def embed(texts: list[str]) -> list[list[float]]:
    """Turn text into vectors. Runs on your machine, costs no API quota."""
    vectors = _embedder().encode(texts, show_progress_bar=False)
    # sentence-transformers and the smoke stand-in return something with a
    # .tolist(); _OnnxEmbedder has already done that conversion itself.
    return vectors.tolist() if hasattr(vectors, "tolist") else vectors


def _client():
    return chromadb.PersistentClient(
        path=str(config.CHROMA_DIR),
        settings=chromadb.config.Settings(anonymized_telemetry=False),
    )


def _tokenize(text: str) -> list[str]:
    """Lowercase word tokens. Good enough for BM25 — no stemming, no stopwords."""
    return re.findall(r"\w+", text.lower())


# Keyed by collection name. Each entry is (BM25Okapi, ids, docs, metadatas),
# with the three lists index-aligned with each other and with the corpus the
# BM25Okapi instance was built from.
_bm25_cache: dict[str, tuple] = {}


def _bm25_index(collection):
    """Get or build the BM25 index for a collection, from its own documents.

    Built lazily from whatever is already in Chroma, so it always matches
    what `build_index` last stored — nothing new to keep in sync by hand.
    """
    name = collection.name
    if name in _bm25_cache:
        return _bm25_cache[name]

    stored = collection.get(include=["documents", "metadatas"])
    ids = stored["ids"]
    docs = stored["documents"]
    metadatas = stored["metadatas"]
    bm25 = BM25Okapi([_tokenize(doc) for doc in docs])

    entry = (bm25, ids, docs, metadatas)
    _bm25_cache[name] = entry
    return entry


def _cosine_distance(a: list[float], b: list[float]) -> float:
    """1 - cosine similarity, matching Chroma's `hnsw:space: cosine` collections."""
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 1.0
    return 1.0 - dot / (norm_a * norm_b)


def build_index(
    chunks: list[Chunk],
    corpus: str | None = None,
    variant: str = "default",
) -> int:
    """
    Embed every chunk and store it.

    `variant` lets you keep more than one index of the same corpus at the same
    time. In unit 2, when you compare two chunking strategies, index the second
    one as variant="v2" and you can query both instead of deleting the first
    and starting over.
    """
    name = config.collection_name(corpus, variant)
    client = _client()

    try:
        client.delete_collection(name)
    except Exception:
        pass

    _bm25_cache.pop(name, None)

    collection = client.create_collection(
        name=name,
        # ⚠️ Do not remove. Chroma defaults to squared L2, and every distance
        # number in this course assumes cosine.
        metadata={"hnsw:space": "cosine"},
    )

    batch = 256
    for start in range(0, len(chunks), batch):
        window = chunks[start : start + batch]
        collection.add(
            ids=[f"{c.source}#{c.index}" for c in window],
            documents=[c.text for c in window],
            embeddings=embed([c.text for c in window]),
            metadatas=[
                {"source": c.source, "index": c.index, "produced_by": c.produced_by}
                for c in window
            ],
        )

    return len(chunks)


def search(
    question: str,
    top_k: int | None = None,
    corpus: str | None = None,
    variant: str = "default",
) -> list[Result]:
    """
    Retrieve the chunks closest to a question by meaning (embeddings) and by
    keyword (BM25), then combine the two with Reciprocal Rank Fusion.

    RRF combines by *rank*, not raw score, so it needs no rescaling between
    cosine distance (lower is better) and BM25 score (higher is better, no
    fixed range). Each method contributes up to `config.HYBRID_CANDIDATES`
    candidates; a chunk's fused score is the sum of `1 / (RRF_K + rank)`
    across whichever method(s) surfaced it.

    Every returned `Result.distance` is still a real cosine distance (see the
    module docstring) — for a chunk that only came in via BM25, it's computed
    on the spot against its stored embedding — so `gate.py`'s threshold keeps
    meaning exactly what it always has.

    Returns the fused top `top_k`, best first.
    """
    top_k = top_k or config.TOP_K
    name = config.collection_name(corpus, variant)

    try:
        collection = _client().get_collection(name)
    except Exception as exc:
        raise RuntimeError(
            f"No index called '{name}'. Run `python app.py index` first."
        ) from exc

    count = collection.count()
    if count == 0:
        return []

    candidate_k = min(max(top_k, config.HYBRID_CANDIDATES), count)

    query_embedding = embed([question])[0]
    raw = collection.query(
        query_embeddings=[query_embedding],
        n_results=candidate_k,
    )
    embed_ids = raw["ids"][0]
    embed_rank = {cid: i + 1 for i, cid in enumerate(embed_ids)}
    embed_distance = dict(zip(embed_ids, raw["distances"][0]))

    bm25, all_ids, all_docs, all_metas = _bm25_index(collection)
    doc_by_id = dict(zip(all_ids, all_docs))
    meta_by_id = dict(zip(all_ids, all_metas))

    scores = bm25.get_scores(_tokenize(question))
    bm25_ranked = sorted(zip(all_ids, scores), key=lambda pair: pair[1], reverse=True)
    bm25_candidates = [cid for cid, score in bm25_ranked if score > 0][:candidate_k]
    bm25_rank = {cid: i + 1 for i, cid in enumerate(bm25_candidates)}

    fused: dict[str, float] = {}
    for cid in set(embed_rank) | set(bm25_rank):
        score = 0.0
        if cid in embed_rank:
            score += 1.0 / (config.RRF_K + embed_rank[cid])
        if cid in bm25_rank:
            score += 1.0 / (config.RRF_K + bm25_rank[cid])
        fused[cid] = score

    final_ids = sorted(fused, key=lambda cid: fused[cid], reverse=True)[:top_k]

    # Gate safety net: keep the single nearest-embedding chunk in the final
    # set even if BM25 pushed it out of the fused top_k, so the relevance
    # gate's "how close is the closest chunk" check never gets worse than it
    # is with embeddings alone.
    if embed_ids and embed_ids[0] not in final_ids and final_ids:
        final_ids[-1] = embed_ids[0]

    missing_embeddings = [cid for cid in final_ids if cid not in embed_distance]
    fetched_embeddings = {}
    if missing_embeddings:
        fetched = collection.get(ids=missing_embeddings, include=["embeddings"])
        fetched_embeddings = dict(zip(fetched["ids"], fetched["embeddings"]))

    results: list[Result] = []
    for cid in final_ids:
        if cid in embed_distance:
            distance = float(embed_distance[cid])
        else:
            distance = _cosine_distance(query_embedding, fetched_embeddings[cid])

        in_embed = cid in embed_rank
        in_bm25 = cid in bm25_rank
        matched_by = "both" if in_embed and in_bm25 else ("embedding" if in_embed else "bm25")

        meta = meta_by_id.get(cid, {})
        results.append(
            Result(
                text=doc_by_id.get(cid, ""),
                source=str(meta.get("source", "unknown")),
                label=f"{meta.get('source', 'unknown')}#{meta.get('index', 0)}",
                distance=distance,
                produced_by=str(meta.get("produced_by", "unknown")),
                matched_by=matched_by,
            )
        )
    return results


def index_exists(corpus: str | None = None, variant: str = "default") -> bool:
    """Is there an index here to search, without searching it?

    `serve.py`'s health check asks this. It deliberately does not embed
    anything: loading the embedding model takes 80 MB and a few seconds, and a
    health check that heavy is a health check nobody can afford to call.
    """
    try:
        collection = _client().get_collection(config.collection_name(corpus, variant))
        return collection.count() > 0
    except Exception:
        return False


def reset():
    """Delete every index. Occasionally the fastest way out of a mess."""
    if config.CHROMA_DIR.exists():
        shutil.rmtree(config.CHROMA_DIR)
