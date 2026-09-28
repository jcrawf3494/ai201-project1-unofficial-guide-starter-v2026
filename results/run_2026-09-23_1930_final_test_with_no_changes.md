# Run log — final_test_with_no_changes

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.625
- Runs per question: 3, caching off
- When: 2026-09-23 19:30

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Are bikes a good idea on campus? | pass | fail | fail |
| Can I submit work late? | pass | pass | pass |
| Best quiet place to study? | pass | pass | pass |
| What is the best parking spot or area? | fail | pass | fail |
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
Whether a bike is a good idea depends on the season and storage availability. Covered bike parking fills up by 9 am, salt in the winter destroys drivetrains, and paths can be icy between November and March, though some students use a cheap bike for autumn and walk the rest of the year (*thread_bike_commute.txt*).
```

### Are bikes a good idea on campus? — run 2

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes are worth it for cutting down commute times (cutting an 18-minute walk to about 6 minutes), but covered bike parking fills up by 9 am, and winter salt can destroy a drivetrain in one season. 

Source: `thread_bike_commute.txt`
```

### Are bikes a good idea on campus? — run 3

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes are worth it for cutting down commute times, but there are downsides: covered bike parking fills up by 9 AM, winter salt can destroy a drivetrain in one season, and they can be stolen (though free registration helps recover them). 

Source: thread_bike_commute.txt
```

### Can I submit work late? — run 1

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
According to `thread_late_work.txt`, what happens when you hand work in late is entirely instructor-dependent, and the syllabus is accurate (e.g., if it says 10% a day, it is 10% a day). Additionally, the universal rule is to ask before the deadline rather than after, as almost everyone will give you two days if you ask beforehand (`thread_late_work.txt`). Documented illness also goes through the dean of students rather than the instructor, and that route works (`thread_late_work.txt`).
```

### Can I submit work late? — run 2

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
According to `thread_late_work.txt`, whether you can submit work late is entirely instructor-dependent, and the policy stated in your syllabus is accurate (e.g., if it says 10% off per day, that is the rule). The universal rule is to ask before the deadline rather than after, as almost everyone will grant an extension if you ask beforehand. Additionally, documented illnesses should go through the dean of students rather than the instructor.
```

### Can I submit work late? — run 3

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
What happens if you hand work in late is entirely instructor-dependent, and you should follow what the syllabus states (e.g., if it says 10% off a day, then it is 10% a day). Additionally, a universal rule is to ask for an extension before the deadline rather than after. 

Source: `thread_late_work.txt`
```

### Best quiet place to study? — run 1

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, the library third floor is the only place that reliably delivers silence (*thread_study_spots.txt*). Additionally, Ridgeway Café before 10am is noted as being empty and quiet (*thread_study_spots.txt*).
```

### Best quiet place to study? — run 2

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to *thread_study_spots.txt*, the library third floor is the only place that reliably delivers silence if that is what you need. Additionally, the science building has open lounges on floors 2 through 5 that are unlocked and almost always empty, and Ridgeway Café before 10am is empty and quiet.
```

### Best quiet place to study? — run 3

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_study_spots.txt`, the library's third floor is the only place that reliably delivers silence if that is what you need. Additionally, the science building has open lounges on floors 2 through 5 that are unlocked and almost always empty, and Ridgeway Café before 10am is noted as empty and quiet.
```

### What is the best parking spot or area? — run 1

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to thread_parking.txt, if you are commuting daily, the west permit is worth getting, though the west lots sell out in about three days in August. Alternatively, street parking on Verrill is legal, free, and unmarked.
```

### What is the best parking spot or area? — run 2

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to **thread_parking.txt**, the best parking spot depends on your needs: the west permit is worth getting if you commute daily, while street parking on Verrill is popular because it is legal, free, and unmarked. The east lot never sells out, but it is a 12-minute walk.
```

### What is the best parking spot or area? — run 3

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to `thread_parking.txt`, the west permit is worth getting if you commute daily, though west lots sell out in about three days in August. Half the upper years park on Verrill Street because it is legal, free, and unmarked.
```

### Where can I find information about internships? — run 1

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_internship_timing.txt`, information about summer internships indicates that large employers close applications in October and November, while smaller and local places hire in February and March. Additionally, the careers office reviews CVs on a drop-in basis.
```

### Where can I find information about internships? — run 2

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to thread_internship_timing.txt, large employers close applications in October and November for the following summer, while smaller and local places hire in February and March. Additionally, the careers office reviews CVs on a drop-in basis.
```

### Where can I find information about internships? — run 3

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, information about summer internships and application timelines is discussed in `thread_internship_timing.txt`. Large employers close applications in October and November, while smaller and local places hire in February and March (`thread_internship_timing.txt`). Additionally, the careers office reviews CVs on a drop-in basis (`thread_internship_timing.txt`).
```
