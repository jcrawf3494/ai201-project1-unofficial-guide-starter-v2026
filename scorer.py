"""
The judgment call unit 2 asks you to build.

`run_eval.py` looks for a function called `judge(question, expects, answer,
results) -> bool` in this file. Once it exists, the Run columns in the run log
carry real verdicts instead of blanks.

What "pass" means here, and why:

A run passes when the answer does two things:

  1. Contains what Milestone 2 said a correct answer should contain — the
     `expects` word or phrase from questions.py. That target was written
     before any results existed, so scoring against it isn't scoring
     against whatever happened to come back.
  2. Names one of the sources retrieval actually returned for that
     question. This is criterion 2 in criteria.md ("every answer names a
     source"): an answer that says the right thing but cites nothing, or
     cites something that was never retrieved, isn't the grounded answer
     this system is supposed to produce.

A refusal (`gate.REFUSAL`) never passes. The questions this function is
called on come from `questions.answered()`, not `OUT_OF_SCOPE` — they're
questions the corpus is supposed to cover, so a refusal here means
retrieval or the gate missed, not that the system correctly recognized an
unanswerable question.

Matching `expects` is deliberately loose: lowercased, and split into
significant words that each have to show up *somewhere* in the answer, as
a word-start match (so "career" also matches "careers"). That tolerates
rewording ("ask before the deadline" for an expects of "ask before
deadline") without tolerating a word that's simply missing — which is
exactly the kind of miss criterion 1 exists to catch. It's a blunt
instrument on purpose: this file is meant to save you from re-reading
every transcript by hand, not to replace your own read of the output in
results/. If a verdict here looks wrong for a specific question, trust
your own reading of the transcript over this function.
"""

import re

import gate

_WORD_RE = re.compile(r"[a-z0-9]+")
_STOPWORDS = {"a", "an", "the", "of", "to", "in", "on", "for", "is", "are", "or", "and"}


def _significant_words(text: str) -> list[str]:
    return [w for w in _WORD_RE.findall(text.lower()) if w not in _STOPWORDS]


def _mentions_expected(answer: str, expects: str) -> bool:
    """Does the answer contain every significant word of `expects`?

    Word-start matching ("career" matches "careers") rather than plain
    substring matching, so a short word like "east" doesn't accidentally
    match inside an unrelated word like "least".
    """
    words = _significant_words(expects)
    if not words:
        return True

    answer_lower = answer.lower()
    return all(
        re.search(rf"\b{re.escape(word)}\w*", answer_lower) for word in words
    )


def _names_a_source(answer: str, results) -> bool:
    """Does the answer cite at least one of the sources actually retrieved?"""
    if not results:
        return False
    answer_lower = answer.lower()
    return any(r.source.lower() in answer_lower for r in results)


def judge(question: str, expects: str, answer: str, results) -> bool:
    """One run's pass/fail verdict. See the module docstring for the rule."""
    if not answer or answer.strip() == gate.REFUSAL:
        return False
    return _mentions_expected(answer, expects) and _names_a_source(answer, results)
