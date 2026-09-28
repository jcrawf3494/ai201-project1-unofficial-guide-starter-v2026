# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
 This gives the ai a keyword to look for which helps add some determinism in the response and prevents the ai from hallucinating and answer. And setting a testing boundary is what is important. So 4/5 but you could also change it to a more stict like 5/5 for where accuracy is more important. Like in a medical situation where doctors are looking up information about a disease. 

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
Same as above allows the user to verify the answer and prevents the AI from hallucinating and answer. 

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

-->

**Why this target:**
This is so there is no hallucination 

---

## 4. Reply chunks keep their thread context

For a sample of at least 5 chunks that are replies (not original posts), at
least 4 of 5 include the original message/question they are replying to —
either appended into the chunk text or stored as chunk metadata I can check
by hand.

**Why this target:**
If a reply chunk is stored without the message it's replying to, the model
loses the context that disambiguates it — e.g. "late" could mean late work or
late registration, and both would retrieve on the same keyword. 9/10 leaves
room for one edge case (like a root post with no parent) without failing the
criterion outright.


---

## 5. Conflicts defer to vote count, but get flagged

For at least 4 of 5 test questions where my corpus has two conflicting
answers (e.g., one post says late work is okay, another says it isn't), the
system's answer (a) matches the source with the higher vote count, and (b)
explicitly states that a conflicting, lower-voted answer exists.
**Why this target:**
These answers are student-submitted, and votes are the best proxy I have for
which one the class actually trusts, so the higher-voted answer should win by
default. Still mentioning the lower-voted one matters because vote count
isn't the same as correctness — 4/5 matches the same tolerance I used for the
other criteria.


**NOTES FOR REVISION** This criteria failed not because it is invalid but because there is not testing in place for it. So I will add this later on and then retest. But I still want this to be a criteria because I believe that it will be important to measure. Plus, technically because there is no way to test for it or to do this all of the questions would pass right now. But Like i mentioned I want to add this feature. 


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
