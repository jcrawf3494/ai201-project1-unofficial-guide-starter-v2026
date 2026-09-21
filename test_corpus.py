#!/usr/bin/env python3
"""
Milestone 4 — where does the relevance cutoff belong?

Runs the five questions in questions.py QUESTIONS (the ones your corpus covers)
and the five in OUT_OF_SCOPE (the ones it clearly doesn't) through retrieval
only, records the best distance for each, and prints the ten-row markdown table
the README asks for, plus the gap between the two groups.

No model calls — this is retrieval and the gate, nothing more, so it costs no
API quota and you can run it as often as you like.

    python test_corpus.py                  the current corpus, from config.py
    python test_corpus.py --corpus city_guides
    python test_corpus.py --top-k 5 --variant v2
    python test_corpus.py --detail         also show the closest chunk per question

Copy the table under "Relevance cutoff" in README.md.
"""

import argparse
import sys

import config
from store import search


def best_distance(question: str, corpus: str, variant: str, top_k: int):
    """Retrieve for one question and hand back the nearest chunk.

    Chroma returns results nearest-first, but `min` is used anyway so the
    number is right regardless of ordering.
    """
    results = search(question, top_k=top_k, corpus=corpus, variant=variant)
    if not results:
        return None, None
    closest = min(results, key=lambda r: r.distance)
    return closest.distance, closest


def collect(corpus: str, variant: str, top_k: int) -> list[dict]:
    """Every question, in-corpus first, with its best distance."""
    from questions import OUT_OF_SCOPE, answered

    rows = []

    for item in answered():
        question = item["question"]
        distance, closest = best_distance(question, corpus, variant, top_k)
        rows.append(
            {
                "question": question,
                "in_corpus": True,
                "distance": distance,
                "closest": closest,
            }
        )

    for question in OUT_OF_SCOPE:
        distance, closest = best_distance(question, corpus, variant, top_k)
        rows.append(
            {
                "question": question,
                "in_corpus": False,
                "distance": distance,
                "closest": closest,
            }
        )

    return rows


def print_table(rows: list[dict]):
    """The three columns the README wants, as markdown you can paste."""
    print("| Question | In corpus? | Best distance |")
    print("|---|---|---|")
    for row in rows:
        distance = "—" if row["distance"] is None else f"{row['distance']:.3f}"
        in_corpus = "Yes" if row["in_corpus"] else "No"
        # A pipe inside a question would break the table.
        question = row["question"].replace("|", "\\|")
        print(f"| {question} | {in_corpus} | {distance} |")


def print_detail(rows: list[dict]):
    """Which chunk each question actually landed on, for the write-up."""
    print("Closest chunk per question")
    print("-" * 70)
    for row in rows:
        group = "in corpus" if row["in_corpus"] else "out of scope"
        print(f"\n{row['question']}  ({group})")
        if row["closest"] is None:
            print("  nothing retrieved")
            continue
        preview = row["closest"].text[:100].replace("\n", " ")
        print(f"  distance {row['distance']:.3f}  |  {row['closest'].label}")
        print(f"  {preview}...")
    print()


def print_gap(rows: list[dict], threshold: float):
    """The two groups, the space between them, and where the cutoff sits."""
    inside = [r["distance"] for r in rows if r["in_corpus"] and r["distance"] is not None]
    outside = [r["distance"] for r in rows if not r["in_corpus"] and r["distance"] is not None]

    if not inside or not outside:
        print("Not enough distances to compare the two groups.")
        return

    worst_in = max(inside)
    best_out = min(outside)

    print("Where the two groups landed")
    print("-" * 70)
    print(
        f"  in corpus     {min(inside):.3f} – {worst_in:.3f}"
        f"   (mean {sum(inside) / len(inside):.3f}, n={len(inside)})"
    )
    print(
        f"  out of scope  {best_out:.3f} – {max(outside):.3f}"
        f"   (mean {sum(outside) / len(outside):.3f}, n={len(outside)})"
    )

    gap = best_out - worst_in
    print()
    if gap > 0:
        midpoint = worst_in + gap / 2
        print(f"  Gap: {worst_in:.3f} → {best_out:.3f}  (width {gap:.3f})")
        print(f"  Midpoint of the gap: {midpoint:.3f}")
    else:
        print(
            f"  No gap — the groups overlap by {abs(gap):.3f}: "
            f"the worst in-corpus question ({worst_in:.3f}) is further away "
            f"than the closest out-of-scope one ({best_out:.3f})."
        )
        print("  No single cutoff separates them cleanly. Say so in the README,")
        print("  pick the cutoff that costs you least, and name what it costs.")

    # What the cutoff you have now would actually do to these ten questions.
    wrongly_refused = [r for r in rows if r["in_corpus"] and r["distance"] is not None and r["distance"] >= threshold]
    wrongly_answered = [r for r in rows if not r["in_corpus"] and r["distance"] is not None and r["distance"] < threshold]

    print()
    print(f"  Current cutoff (config.THRESHOLD): {threshold}")
    print(
        f"    answers {len(inside) - len(wrongly_refused)} of {len(inside)} in-corpus, "
        f"refuses {len(outside) - len(wrongly_answered)} of {len(outside)} out-of-scope"
    )
    for row in wrongly_refused:
        print(f"    refuses (shouldn't): {row['question']}  [{row['distance']:.3f}]")
    for row in wrongly_answered:
        print(f"    answers (shouldn't): {row['question']}  [{row['distance']:.3f}]")
    print()


def main():
    parser = argparse.ArgumentParser(
        prog="test_corpus.py",
        description="Milestone 4: best distance for all ten questions, as a markdown table.",
    )
    parser.add_argument("--corpus", help="corpus folder name (default: config.CORPUS)")
    parser.add_argument("--variant", default="default", help="index variant")
    parser.add_argument("--top-k", type=int, help=f"chunks per question (default: {config.TOP_K})")
    parser.add_argument(
        "--threshold",
        type=float,
        help=f"cutoff to judge against (default: config.THRESHOLD, {config.THRESHOLD})",
    )
    parser.add_argument(
        "--detail",
        action="store_true",
        help="also print the closest chunk behind each distance",
    )
    args = parser.parse_args()

    corpus = args.corpus or config.CORPUS
    top_k = args.top_k or config.TOP_K
    threshold = config.THRESHOLD if args.threshold is None else args.threshold

    print(f"Corpus: {corpus}   variant: {args.variant}   top_k: {top_k}")
    print("Retrieval only — no model calls.\n")

    try:
        rows = collect(corpus, args.variant, top_k)
    except Exception as exc:  # noqa: BLE001 — a readable message beats a traceback
        print(f"\n{type(exc).__name__}: {exc}\n", file=sys.stderr)
        return 1

    if args.detail:
        print_detail(rows)

    print_gap(rows, threshold)

    print("Paste this into README.md under the relevance cutoff section:\n")
    print_table(rows)
    print()
    print("Lower is better. 0.3 is a close match, 0.9 is unrelated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
