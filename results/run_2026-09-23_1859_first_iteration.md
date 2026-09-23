# Run log — first_iteration

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.625
- Runs per question: 3, caching off
- When: 2026-09-23 18:59

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Are bikes a good idea on campus? | fail | fail | fail |
| Can I submit work late? | pass | pass | pass |
| Best quiet place to study? | pass | pass | pass |
| What is the best parking spot or area? | fail | pass | pass |
| Where can I find information about internships? | fail | fail | fail |

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
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes can be both a good and bad idea depending on the circumstances. They cut an 18-minute walk to about 6 minutes and can be registered for free on campus (thread_bike_commute.txt). However, covered bike parking fills up by 9 am, salt from winter paths can destroy a drivetrain in one season, and they are susceptible to being stolen (thread_bike_commute.txt).
```

### Are bikes a good idea on campus? — run 2

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes have mixed reviews. They can cut an 18-minute walk down to about 6 minutes, but covered bike parking fills up by 9 am, and winter paths can be icy or salted, which destroys drivetrains (thread_bike_commute.txt).
```

### Are bikes a good idea on campus? — run 3

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes can be a good idea because they cut commute times significantly, but they also have drawbacks. Storage can be an issue since covered bike parking fills up by 9 am, and winter conditions like ice and salt can damage a drivetrain in a single season (thread_bike_commute.txt).
```

### Can I submit work late? — run 1

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Whether you can submit work late is entirely instructor-dependent, and you should follow what is stated in your syllabus (thread_late_work.txt). Additionally, the universal rule is to ask before the deadline rather than after (thread_late_work.txt).
```

### Can I submit work late? — run 2

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Yes, submitting work late is entirely instructor-dependent, and the policy stated in the syllabus is accurate (e.g., if it says 10% off a day, it is 10% a day) (*thread_late_work.txt*). Additionally, you should ask before the deadline rather than after, as almost everyone will grant an extension if you ask ahead of time (*thread_late_work.txt*).
```

### Can I submit work late? — run 3

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
What happens when you hand something in late is entirely instructor-dependent and follows what is written in the syllabus (thread_late_work.txt). Additionally, the universal rule for late work is to ask before the deadline rather than after (thread_late_work.txt).
```

### Best quiet place to study? — run 1

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Depending on what you need, the third floor of the library is the only place that reliably delivers silence (thread_study_spots.txt). Alternatively, Ridgeway Café before 10am is empty and quiet (thread_study_spots.txt).
```

### Best quiet place to study? — run 2

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to thread_study_spots.txt, Ridgeway Café before 10am is empty and quiet, and the third floor of the library is the only place that reliably delivers silence if you need it.
```

### Best quiet place to study? — run 3

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, the third floor of the library is noted as the only place that reliably delivers silence (thread_study_spots.txt). Additionally, Ridgeway Café before 10am is described as empty and quiet (thread_study_spots.txt).
```

### What is the best parking spot or area? — run 1

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to `thread_parking.txt`, the west permit is worth getting if you commute daily, though the west lots sell out in about three days in August. Street parking on Verrill is also noted as legal, free, and unmarked, which is why half the upper years use it.
```

### What is the best parking spot or area? — run 2

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to `thread_parking.txt`, the west permit is worth getting if you are commuting daily. If you are not commuting daily, the documents state not to bother getting one, and that the east lot is a 12-minute walk while street parking on Verrill is legal, free, and unmarked.
```

### What is the best parking spot or area? — run 3

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to `thread_parking.txt`, the best parking choice depends on your needs: the west permit is worth getting if you are commuting daily, while street parking on Verrill is popular because it is legal, free, and unmarked. The east lot never sells out, though it is a 12-minute walk.
```

### Where can I find information about internships? — run 1

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to thread_internship_timing.txt, large employers close applications in October and November, while smaller and local places hire in February and March. Additionally, the careers office reviews CVs on a drop-in basis.
```

### Where can I find information about internships? — run 2

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_internship_timing.txt`, you can learn about internship application timelines and employer hiring schedules (with large employers closing applications in October/November, and smaller places hiring in February/March). Additionally, the document mentions that the careers office reviews CVs on a drop-in basis.
```

### Where can I find information about internships? — run 3

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, information about internship timing and when to start looking for them can be found in `thread_internship_timing.txt`.
```
