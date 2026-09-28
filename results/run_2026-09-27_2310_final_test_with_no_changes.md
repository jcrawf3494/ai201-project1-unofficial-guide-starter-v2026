# Run log — final_test_with_no_changes

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.625
- Runs per question: 3, caching off
- When: 2026-09-27 23:10

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Are bikes a good idea on campus? | pass | fail | pass |
| Can I submit work late? | pass | pass | pass |
| Best quiet place to study? | pass | pass | pass |
| What is the best parking spot or area? | pass | pass | pass |
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
Bikes are useful because they can cut an 18-minute walk down to about 6 minutes, but they also have downsides, such as full covered parking by 9 AM and drivetrains being destroyed by salt between November and March (thread_bike_commute.txt). One person notes they keep a cheap bike for autumn and walk the rest of the year, while another sold theirs due to icy or salted paths (thread_bike_commute.txt).
```

### Are bikes a good idea on campus? — run 2

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes are worth it for cutting down commute times (cutting an 18-minute walk to about 6 minutes), but covered bike parking fills up by 9 am, and winter salt can destroy a drivetrain in one season. *(thread_bike_commute.txt)*
```

### Are bikes a good idea on campus? — run 3

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes can cut a walk significantly, but there are downsides like full covered parking by 9 am and salt destroying the drivetrain between November and March (`thread_bike_commute.txt`). Some students manage this by using a cheap bike only from September to November and walking the rest of the year (`thread_bike_commute.txt`).
```

### Can I submit work late? — run 1

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Whether you can submit work late depends entirely on the instructor, and you should check the syllabus as it is accurate (thread_late_work.txt). The universal rule is to ask before the deadline rather than after, as instructors are much more likely to grant an extension beforehand (thread_late_work.txt).
```

### Can I submit work late? — run 2

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
What happens when you hand something in late is entirely instructor-dependent, and you should follow what is stated in the syllabus (source: thread_late_work.txt). Additionally, the universal rule is to ask before the deadline rather than after, as almost everyone will grant an extension if asked beforehand (source: thread_late_work.txt).
```

### Can I submit work late? — run 3

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Whether you can submit work late is entirely instructor-dependent, and the policy stated in the syllabus is accurate (e.g., if it says 10% off per day, that is the rule). The universal rule is to ask before the deadline rather than after. 

Source: `thread_late_work.txt`
```

### Best quiet place to study? — run 1

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Depending on what you need, the third floor of the library is the only place that reliably delivers silence (thread_study_spots.txt). Alternatively, Ridgeway Café before 10am is empty and quiet, and open lounges on floors 2 through 5 of the science building are almost always empty (thread_study_spots.txt).
```

### Best quiet place to study? — run 2

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_study_spots.txt`, the library's third floor is the only place that reliably delivers silence if that is what you need. Additionally, the science building has open lounges on floors 2 through 5 that are unlocked and almost always empty, and the Ridgeway Café before 10am is empty and quiet.
```

### Best quiet place to study? — run 3

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_study_spots.txt`, if you need silence, the third floor of the library is the only place that reliably delivers it. Alternatively, Ridgeway Café before 10am is empty and quiet, and the science building has open lounges on floors 2 through 5 that are almost always empty.
```

### What is the best parking spot or area? — run 1

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to `thread_parking.txt`, the west permit is worth getting if you commute daily, though west lots sell out in about three days in August. The east lot never sells out, but it is a 12-minute walk. Alternatively, street parking on Verrill is legal, free, and unmarked.
```

### What is the best parking spot or area? — run 2

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to **thread_parking.txt**, the best parking choice depends on your needs: the west permit is worth getting if you are commuting daily, while the east lot never sells out (though it's a 12-minute walk). Additionally, half the upper years use Verrill for street parking because it is legal, free, and unmarked.
```

### What is the best parking spot or area? — run 3

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to *thread_parking.txt*, the best parking option depends on your situation: west lots are worth getting if you are commuting daily, while street parking on Verrill is popular because it is legal, free, and unmarked. The east lot never sells out, but it is a 12-minute walk.
```

### Where can I find information about internships? — run 1

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, information regarding summer internships can be found in the discussion about when to start looking, which notes that large employers close applications in October and November while smaller and local places hire in February and March (*thread_internship_timing.txt*). Additionally, the careers office reviews CVs on a drop-in basis (*thread_internship_timing.txt*).
```

### Where can I find information about internships? — run 2

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_internship_timing.txt`, large employers close applications in October and November for the following summer, while smaller and local places hire in February and March. Additionally, the careers office reviews CVs on a drop-in basis.
```

### Where can I find information about internships? — run 3

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, you can find information about internship timing and when to look for them in `thread_internship_timing.txt`.
```
