# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does
I chose advice_threads because I believe it has some very real world applications. Especially when training new models for AI. While that is out of scope of this class I think it would be interesting to learn how to decide which response is better than others. So the end goal of this app will be able to get a working rag system that stays within scope of the answer but also gives the most correct answer that is available. 

## Chunking Strategy

**Chunk size:**
**Overlap:**

I spent some time working with Gemini in a separate chat to determine the best chunk size and it really came down to most of the answers are not super long but it does require the context of the "thread" to answer correctly. For example if there was a question about being late for class or being late for registration the answers would be different but if we didnt keep that context alive with the thread headers then it could get lost and the model could give a "correct" answer via chunk logic but it would be incorrect logically. So this helps provide a more deterministic outcome. 

## Sample Chunks


Paste these into your README under Sample Chunks. The rubric asks
for the source file and the function that produced them — both are
printed for you below.

======================================================================
Chunk 1  |  source: thread_bike_commute.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Thread: Is a bike worth it for a 20 minute walk commute?
Reply 1 (14 votes)
Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9am at all three.

======================================================================
Chunk 2  |  source: thread_first_gen.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Thread: Anything specific for first-generation students?
Reply 2 (41 votes)
The thing I'd say: the unwritten rules are the hard part, not the coursework. Ask about the unwritten rules explicitly. People are happy to explain them and nobody volunteers them.

======================================================================
Chunk 3  |  source: thread_laptop_specs.txt#2  |  produced by: chunker.py::split_documents
======================================================================
Thread: How much laptop do I actually need for CS courses?
Reply 3 (12 votes)
I did two years on an 8GB machine and it was fine until the last project, at which point it very much wasn't. 16 isthe answer.

======================================================================
Chunk 4  |  source: thread_parking.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Thread: Worth getting a parking permit?
Reply 2 (21 votes)
Street parking on Verrill is legal and free and unmarked, which is why half the upper years do it.

======================================================================
Chunk 5  |  source: thread_sleep_schedule.txt#1  |  produced by: chunker.py::split_documents
======================================================================
Thread: Everyone says fix your sleep. Does it actually matter?
Reply 2 (37 votes)
The library being open until 2am is a trap. It's a resource, not a schedule.
```
```

## Sample Answer



**Question:**

"Are bikes good for campus?"
  (best distance 0.398, cutoff 0.6)

Bikes can cut an 18-minute walk down to about 6 minutes, but storage is an issue because covered bike parking fills up by 9:00 AM, and salt from winter paths can destroy a drivetrain in a single season. (Source: thread_bike_commute.txt)

Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

.625 seems to be a good cutoff it is a little long for most but it covers even for the responses that are long. 


| Question | In corpus? | Best distance |
|---|---|---|
| Are bikes a good idea on campus? | Yes | 0.386 |
| Can I submit work late? | Yes | 0.585 |
| Best quiet place to study? | Yes | 0.371 |
| What is the best parking spot or area? | Yes | 0.511 |
| Where can I find information about internships? | Yes | 0.537 |
| What is the capital of Mongolia? | No | 0.890 |
| How do I change the oil in a diesel engine? | No | 0.930 |
| Who won the 1994 World Cup? | No | 0.787 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.828 |
| How do I write a for loop in Rust? | No | 0.871 |


## How I Used AI


**1.**
I used Ai to help create a test for in corpus and out of corpus questions. This was needed so I did not have to type and format with 10 different questions. I liked the way it worked so I left it. 

**2.**
I also used AI to help create the chunking pattern I planned with it and gave it some context and the rules that I wanted to keep and then it gave me a prompt to give to claude to be able to build a more effective chunker.py. It took a few prompts to create a final prompt I was happy with .

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->
Stretch Features
1. I added an additional testing file. testing_corpus.py that can be updated and ran to test the corpus without having to do it all more than once. 
---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4/5 | 3/5 | 4/5 | MISSED |
| 2. Every answer names a source | 5/5 | 5/5 | 5/5 |  MET |
| 3. Gate stops out-of-corpus questions | 5/5 | 5/5 | 5/5 |  MET |




<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### Are bikes a good idea on campus? — run 1
produced by run_eval.py [text](results/run_2026-09-27_2310_final_test_with_no_changes.md)

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes are useful because they can cut an 18-minute walk down to about 6 minutes, but they also have downsides, such as full covered parking by 9 AM and drivetrains being destroyed by salt between November and March (thread_bike_commute.txt). One person notes they keep a cheap bike for autumn and walk the rest of the year, while another sold theirs due to icy or salted paths (thread_bike_commute.txt).

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4/5 | 3/5 | 4/5 | MISSED | The ones that failed did not have a chunk that contained the corrected answer
| 2. Every answer names a source | 5/5 | 5/5 | 5/5 |  MET | Event if the answer was incorrect it named a source
| 3. Gate stops out-of-corpus questions | 5/5 | 5/5 | 5/5 |  MET | None of the out of corpus questions passed. 
| 4. Reply chunks keep their thread context| 5/5 |5/5|5/5|  MET |Because even if the answer was incorrect they still pulled from the same thread
| 5. Conflicts defer to vote count, but get flagged | 0/5 |0/5  |0/5 |Missed| Not a way to judge this right now. They technically could have passed as well because there were no issues with this but I wanted to keep this as fail so this could be built in later to flag for this as I think it will be a really useful diagnosis tool 

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
  Most of my misses were from criteria Retrieved chunks contain the answer
  Specifically for question 1 and 5. These failures did not come because the answers were necessarily incorrect but rather because I was too general in the expects portion of the questions.py. If that was updated the answers to these questions would be a pass as they did give relevant answers based on the provided text

  The last criteria that was missed was Conflicts defer to vote count, but get flagged and that was for all the questions. That is because this was not built in to the testing. But I plan to build this in the testing, as I think it would be important not to raise. Especially as the Rag system starts to grow. Or if you were using this on a larger platform with more conflicting answers like on reddit. 

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
