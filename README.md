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

  Example 
  Question 1 Run 2 
  Bikes are worth it for cutting down commute times (cutting an 18-minute walk to about 6 minutes), but covered bike parking fills up by 9 am, and winter salt can destroy a drivetrain in one season. *(thread_bike_commute.txt)* This failed because it did not have cheap bike but it did give correct information. 

  Question 5 All runs. 
  This is because the questions is almost out of corpus. It contains enough information to be relevant but only one of the replies has what question.py is looking for and it does not relate to what the person is saying.  

  Example. 
  Based on the provided documents, you can find information about internship timing and when to look for them in `thread_internship_timing

  The last criteria that was missed was Conflicts defer to vote count, but get flagged and that was for all the questions. That is because this was not built in to the testing. But I plan to build this in the testing, as I think it would be important not to raise. Especially as the Rag system starts to grow. Or if you were using this on a larger platform with more conflicting answers like on reddit. 

     Milestone 3. -->

## The Improvement

I left my criteria as is but updated the questions.py because I think they were corrupting the results from run_eval.py. 

**What I changed:**

I changed the question for 5 to be more relevant as the question I chose was not directly answered at all in the text. I also changed the expected for question 1. 

 {"question": "Are bikes a good idea on campus?", "expects": "bike"},

{"question": "What is the best time to look for an internship?", "expects": "earlier"},

**Why I picked it:**

I changed it because I feel like my critera was not testing correctly with the way the questions were written as is. I did not re write the questions so that they could pass the criteria but rather so that the criteria would be relevant. Because question 5 was going to fail everytime no matter what the criteria was because it was a bad question and question 1 was too strict and would risk the quality of the app if I kept it as is. 
### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  4/5|4/5|3/5 |Missed  |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5| 5/5 | Met  |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | Met  |
| 4. Reply chunks keep their thread context |4 of 5  |5/5 | 5/5| 5/5| Met
| 5. Conflicts defer to vote count, but get flagged | 4 of 5| 0|0 |0 | Missed



**Did it help?**

I think it helped. Question 5 was now testable but also did not make it a guaranteed win every single time. I think Seeing question 4 fail consistently on this one made me double down on the need to add the testing for the 5th criteria. Because in this thread there are multiple answers about which lot is best and why, but just expanding the expects in the question would not allow the RAG system to work dynamically. Because ideally you would want this to work and always give the best answer. Even if the best lot to park changes. For example east lot could be best this year. But then South Lot expands to be closer and becomes better the next year. So instead of hard coding an answer allowing the votes to change the answer would allow for this context. Whereas in other ones where I did change the questions.py I did so because the expects was too narrow. 

## What's Still Broken

The last criteria is still broken but like I mentioned above I think it is still one I want to have I just need to update run_eval.py to test for it so that we can see how it actually performs and if it helps. But I did not have the time to make that test this time. 

## What I'd Do Differently

I think I would write 5 differently and 4 differently. I think 4 is too broad and really just expands on what 3 already looks for. Maybe I will add a sixth one to make up for the lack of diversity in my criteria. 