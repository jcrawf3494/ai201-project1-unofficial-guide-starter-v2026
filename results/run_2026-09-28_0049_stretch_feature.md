# Run log — stretch_feature

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.625
- Runs per question: 3, caching off
- When: 2026-09-28 00:49

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Are bikes a good idea on campus? | pass | pass | pass |
| Can I submit work late? | pass | pass | pass |
| Best quiet place to study? | pass | pass | pass |
| What is the best parking spot or area? | pass | pass | pass |
| What is the best time to look for an internship? | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.625. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.890 | refused |
| How do I change the oil in a diesel engine? | 0.930 | refused |
| Who won the 1994 World Cup? | 0.787 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.828 | refused |
| How do I write a for loop in Rust? | 0.871 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### Are bikes a good idea on campus? — run 1

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_first_gen.txt, thread_meal_plan_tier.txt, thread_parking.txt, thread_study_spots.txt

```
Bikes can cut a walk time significantly, but there are downsides like full covered bike parking by 9 am (thread_bike_commute.txt). Additionally, paths can be icy or salted between November and March, which can destroy a drivetrain in one season, though some students use a cheap bike for autumn and walk the rest of the year (thread_bike_commute.txt).
```

### Are bikes a good idea on campus? — run 2

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_first_gen.txt, thread_meal_plan_tier.txt, thread_parking.txt, thread_study_spots.txt

```
Bikes can cut a walk significantly, but there are issues with storage (covered parking fills up by 9 am) and winter weather (salt destroys drivetrains between November and March, or paths are icy). (Source: thread_bike_commute.txt)
```

### Are bikes a good idea on campus? — run 3

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_first_gen.txt, thread_meal_plan_tier.txt, thread_parking.txt, thread_study_spots.txt

```
Bikes can reduce commute times, but there are drawbacks like full covered parking by 9 AM (thread_bike_commute.txt, reply 1), salt destroying drivetrains between November and March (thread_bike_commute.txt, reply 2), and the risk of theft (thread_bike_commute.txt, reply 4). Some students handle this by using a cheap bike for part of the year and walking the rest (thread_bike_commute.txt, reply 3). 

Source: thread_bike_commute.txt
```

### Can I submit work late? — run 1

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_pass_fail.txt

```
Whether you can submit work late is entirely dependent on the instructor and what the syllabus states (thread_late_work.txt). However, you should ask before the deadline rather than after, as almost everyone will grant an extension if you ask beforehand, but almost nobody will after the deadline has passed (thread_late_work.txt). Additionally, documented illness goes through the dean of students rather than the instructor (thread_late_work.txt).
```

### Can I submit work late? — run 2

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_pass_fail.txt

```
Yes, you can submit work late, but the consequences are entirely dependent on the instructor and what the syllabus states (e.g., if it says 10% off a day, it is 10% a day). The universal rule is to ask before the deadline rather than after, as almost everyone will give you extra time if you ask ahead of time. Additionally, documented illness goes through the dean of students rather than the instructor. 

Source: `thread_late_work.txt`
```

### Can I submit work late? — run 3

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_pass_fail.txt

```
Whether you can submit work late depends entirely on the instructor and what the syllabus states (thread_late_work.txt). However, you should ask before the deadline rather than after, as instructors are much more likely to grant an extension beforehand (thread_late_work.txt). Additionally, documented illness goes through the dean of students rather than the instructor (thread_late_work.txt).
```

### Best quiet place to study? — run 1

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, if you need silence, the third floor of the library is the only place that reliably delivers it (thread_study_spots.txt).
```

### Best quiet place to study? — run 2

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
If you need silence, the third floor of the library is the only place that reliably delivers it (thread_study_spots.txt).
```

### Best quiet place to study? — run 3

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to thread_study_spots.txt, the library third floor is the only place that reliably delivers silence if you need it.
```

### What is the best parking spot or area? — run 1

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_laundry_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
Based on the provided documents, the best parking options depend on your needs:

* **West lots:** Worth getting a permit for if you are commuting daily, though they sell out in about three days in August (*thread_parking.txt*).
* **Street parking on Verrill:** Described as legal, free, and unmarked, which is why half the upper years use it (*thread_parking.txt*).
* **East lot:** Never sells out, but it is a 12-minute walk (*thread_parking.txt*).
```

### What is the best parking spot or area? — run 2

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_laundry_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
Based on the provided documents, there are a few parking options discussed, but whether one is "best" depends on your needs:

* **West lots:** Worth getting the permit if you are commuting daily, though they sell out in about three days in August (*thread_parking.txt*).
* **Street parking on Verrill:** Legal, free, and unmarked, which is why half the upper years use it (*thread_parking.txt*). 
* **East lot:** Never sells out, but it is a 12-minute walk (*thread_parking.txt*).

Source: *thread_parking.txt*
```

### What is the best parking spot or area? — run 3

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_laundry_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
Based on the provided documents, whether a parking spot is "best" depends on your situation:
- The west permit is worth getting if you commute daily, though west lots sell out in about three days in August (*thread_parking.txt*).
- The East lot never sells out, but it requires a 12-minute walk (*thread_parking.txt*).
- Street parking on Verrill is legal, free, and unmarked, which is why half the upper years use it (*thread_parking.txt*). 

Source: thread_parking.txt
```

### What is the best time to look for an internship? — run 1

- Best distance: 0.3742 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_internship_timing.txt, thread_late_work.txt, thread_pass_fail.txt, thread_study_spots.txt

```
You should start looking earlier than feels reasonable, as large employers close their applications in October and November for the following summer. Smaller and local places hire in February and March if you miss the autumn window. 

*(Source: thread_internship_timing.txt)*
```

### What is the best time to look for an internship? — run 2

- Best distance: 0.3742 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_internship_timing.txt, thread_late_work.txt, thread_pass_fail.txt, thread_study_spots.txt

```
You should start looking earlier than feels reasonable, as large employers close applications in October and November for the following summer. Smaller and local places hire later, in February and March. 

Source: `thread_internship_timing.txt`
```

### What is the best time to look for an internship? — run 3

- Best distance: 0.3742 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_internship_timing.txt, thread_late_work.txt, thread_pass_fail.txt, thread_study_spots.txt

```
You should start looking earlier than feels reasonable, as large employers close applications in October and November for the following summer. Smaller and local places hire in February and March. 

Source: `thread_internship_timing.txt`
```
