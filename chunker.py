"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document

# --- advice_threads format --------------------------------------------------
# Documents in this corpus look like:
#
#   THREAD: How many clubs is too many?
#
#   --- reply 1 (31 votes) ---
#   Two you actually turn up to beats six you signed up for at the fair.
#
#   --- reply 2 (24 votes) ---
#   The club fair collects about four hundred email addresses per society [...]
#
# One reply is one answer to the thread's question, so one reply is one chunk.

MIN_CHUNK_CHARS = 50

_THREAD_TITLE_RE = re.compile(r"^[ \t]*THREAD[ \t]*:[ \t]*(.*?)[ \t]*$", re.IGNORECASE)

# Matches "--- reply 1 (31 votes) ---" and the sloppier variants of it:
# any run of dashes, optional "#", any number of votes (including 0 or a
# signed count), "vote" or "votes", and whatever spacing crept in.
_REPLY_HEADER_RE = re.compile(
    r"""^[ \t]*-{2,}[ \t]*                      # opening dashes
        reply[ \t]*\#?[ \t]*(\d+)[ \t]*         # "reply 1", "reply #1"
        \([ \t]*([+-]?\d+)[ \t]*votes?[ \t]*\)  # "(31 votes)"
        [ \t]*-{2,}[ \t]*$                      # closing dashes
    """,
    re.IGNORECASE | re.MULTILINE | re.VERBOSE,
)


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


def _parse_preamble(preamble: str) -> tuple[str, str]:
    """
    Pull the thread title out of everything before the first reply.

    Returns (title, opening_text). `opening_text` is whatever else sat above
    the first reply — usually nothing, occasionally the original poster's
    question spelled out over a few lines.
    """
    title = ""
    rest: list[str] = []

    for line in preamble.splitlines():
        match = _THREAD_TITLE_RE.match(line)
        if match and not title:
            title = match.group(1).strip()
        else:
            rest.append(line)

    return title, "\n".join(rest).strip()


def _format_chunk(title: str, number: str | None, votes: str | None, body: str) -> str:
    """
    One reply, carrying the context it needs to make sense on its own.

    A reply retrieved without its thread title is close to useless — "two you
    actually turn up to" only answers a question if the question travels with
    it. The vote count rides along as a rough quality signal.
    """
    header: list[str] = []
    if title:
        header.append(f"Thread: {title}")
    if number is not None:
        header.append(f"Reply {number} ({votes} votes)")

    return "\n".join([*header, body]) if header else body


def _thread_chunks(text: str) -> list[str]:
    """Split one advice_threads document into reply-sized chunk texts."""
    # split() with two capture groups gives:
    #   [preamble, number, votes, body, number, votes, body, ...]
    parts = _REPLY_HEADER_RE.split(text)
    title, opening = _parse_preamble(parts[0])

    pieces: list[str] = []

    # The original post, when the thread has one above the first reply.
    if len(opening) >= MIN_CHUNK_CHARS:
        pieces.append(_format_chunk(title, None, None, opening))

    for number, votes, body in zip(parts[1::3], parts[2::3], parts[3::3]):
        body = body.strip()
        # Drop the stubs — "^", "ditto", a stray bullet. They retrieve noise.
        if len(body) < MIN_CHUNK_CHARS:
            continue
        pieces.append(_format_chunk(title, number, votes, body))

    return pieces


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split advice_threads documents on their reply delimiters.

    Milestone 3 strategy: these documents are not prose, they are threads. Each
    "--- reply N (V votes) ---" block is one person answering one question, so
    the delimiter is the natural chunk boundary — no character window gets it
    this right, and a fixed window either leaves whole threads unsplit or cuts
    replies in half.

    Each chunk gets the thread title and vote count prepended, so a retrieved
    reply still carries the question it was answering. Replies shorter than
    MIN_CHUNK_CHARS are discarded rather than indexed.

    This never calls `fallback_split` — a document with no reply delimiters is
    kept whole (still subject to the length check) instead of silently
    dropping back to fixed-size windows.
    """
    chunks: list[Chunk] = []

    for doc in documents:
        for index, text in enumerate(_thread_chunks(doc.text)):
            chunks.append(
                Chunk(
                    text=text,
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
