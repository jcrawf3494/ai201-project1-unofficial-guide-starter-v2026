# Run — 2026-09-23 19:20

# Run log

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.625
- Runs per question: 3, caching off
- When: 2026-09-23 19:20

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Are bikes a good idea on campus? | pass | fail | pass |
| Can I submit work late? | pass | pass | pass |
| Best quiet place to study? | pass | pass | pass |
| What is the best parking spot or area? | pass | pass | fail |
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
Bikes have both drawbacks and benefits. They cut an 18-minute walk down to about 6 minutes, but covered bike parking fills up by 9 am, and winter salt can destroy a drivetrain in a single season (thread_bike_commute.txt). One student recommends getting a cheap bike for the autumn months and walking the rest of the year (thread_bike_commute.txt).
```

### Are bikes a good idea on campus? — run 2

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes can be both a good and bad idea depending on the conditions. They cut an 18-minute walk down to about 6 minutes, but covered bike parking fills up by 9 AM, and road salt between November and March can destroy a drivetrain in one season (thread_bike_commute.txt).
```

### Are bikes a good idea on campus? — run 3

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Whether bikes are a good idea depends on the season and storage availability. Covered bike parking fills up by 9 am, salt can destroy a drivetrain between November and March, and paths can be icy (thread_bike_commute.txt). However, they can significantly cut down commute times, and students sometimes manage this by using a cheap bike for specific months and walking the rest of the year (thread_bike_commute.txt).
```

### Can I submit work late? — run 1

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Yes, you can, but what actually happens is entirely instructor-dependent and the syllabus is accurate (thread_late_work.txt). Additionally, the universal rule is to ask before the deadline rather than after, as almost everyone will give you two days if you ask beforehand (thread_late_work.txt).
```

### Can I submit work late? — run 2

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Whether you can submit work late depends entirely on the instructor, and you should check the syllabus, as policies like a 10% deduction per day are accurate if stated there (thread_late_work.txt). Additionally, the universal rule is to ask before the deadline rather than after, as instructors are much more likely to grant an extension if you ask beforehand (thread_late_work.txt). Documented illness should go through the dean of students rather than the instructor (thread_late_work.txt).
```

### Can I submit work late? — run 3

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Yes, but what actually happens is entirely instructor-dependent and the syllabus is accurate (thread_late_work.txt). Additionally, you should ask before the deadline; almost everyone will give you extra time if you ask ahead, but almost nobody will on the following Monday (thread_late_work.txt). Documented illness should go through the dean of students rather than the instructor (thread_late_work.txt).
```

### Best quiet place to study? — run 1

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_study_spots.txt`, if you need silence, the library third floor is the only place that reliably delivers it. Alternatively, the Ridgeway Café before 10am is noted as being empty and quiet, and the science building has open lounges on floors 2 through 5 that are almost always empty.
```

### Best quiet place to study? — run 2

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_study_spots.txt`, if you need silence, the library third floor is the only place that reliably delivers it. Alternatively, Ridgeway Café before 10am is empty and quiet, and the science building has open lounges on floors 2 through 5 that are almost always empty.
```

### Best quiet place to study? — run 3

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, the best study spots depend on your needs:
- Ridgeway Café before 10am is empty, quiet, and has good coffee (thread_study_spots.txt).
- The science building has open lounges on floors 2 through 5 that are unlocked and almost always empty (thread_study_spots.txt).
- The library third floor is the only place that reliably delivers silence, if you need it (thread_study_spots.txt).

Source: thread_study_spots.txt
```

### What is the best parking spot or area? — run 1

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
Based on the provided documents, whether a parking spot is "best" depends on your needs:

* **West lots:** Worth getting if you are commuting daily, though they sell out in about three days in August (*thread_parking.txt*).
* **East lot:** Never sells out, but it's a 12-minute walk (*thread_parking.txt*).
* **Verrill Street:** Half the upper years park here because the street parking is legal, free, and unmarked (*thread_parking.txt*). 

Source: *thread_parking.txt*
```

### What is the best parking spot or area? — run 2

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
Based on the documents provided:

- **West lots** are worth getting if you are commuting daily, though they sell out in about three days in August (*thread_parking.txt*). 
- **Street parking on Verrill** is legal, free, and unmarked, which is why half the upper years use it (*thread_parking.txt*).
- **East lot** never sells out, but it is a 12-minute walk (*thread_parking.txt*). 

Source: thread_parking.txt
```

### What is the best parking spot or area? — run 3

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to the documents, west lots are worth the August scramble if you are commuting daily, though they sell out in about three days in August. Alternatively, street parking on Verrill is legal, free, and unmarked. 

Source: thread_parking.txt
```

### Where can I find information about internships? — run 1

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_internship_timing.txt`, you can learn about internship application timelines and employer hiring schedules (with large employers closing applications in October/November and smaller places hiring in February/March), as well as have your CV reviewed on a drop-in basis at the careers office.
```

### Where can I find information about internships? — run 2

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, information about summer internships and the timing of applications can be found in `thread_internship_timing.txt`.
```

### Where can I find information about internships? — run 3

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to `thread_internship_timing.txt`, large employers close applications in October and November for the following summer, while smaller and local places hire in February and March. Additionally, the careers office reviews CVs on a drop-in basis.
```


---

# Run — 2026-09-23 19:26

# Run log

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.625
- Runs per question: 3, caching off
- When: 2026-09-23 19:26

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Are bikes a good idea on campus? | fail | pass | pass |
| Can I submit work late? | pass | fail | pass |
| Best quiet place to study? | pass | pass | pass |
| What is the best parking spot or area? | fail | fail | fail |
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
Bikes can be both good and bad. They cut an 18-minute walk down to about 6 minutes, but covered bike parking fills up by 9 am, and winter salt can destroy a drivetrain in a single season (thread_bike_commute.txt).
```

### Are bikes a good idea on campus? — run 2

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes are good for cutting down commute times (for example, turning an 18-minute walk into a 6-minute ride), but they have drawbacks like full covered parking by 9 am and salt destroying the drivetrain between November and March (thread_bike_commute.txt). To manage this, one person uses a cheap bike from September to November and walks the rest of the year (thread_bike_commute.txt).
```

### Are bikes a good idea on campus? — run 3

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Whether bikes are a good idea depends on the season and storage availability. Covered bike parking fills up by 9 am, salt in the winter destroys drivetrains, and paths can be icy between November and March, though some students use cheap bikes for part of the year or cut their commute times down significantly. *(thread_bike_commute.txt)*
```

### Can I submit work late? — run 1

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Yes, what happens when you hand something in late is entirely instructor-dependent and follows what is in the syllabus (thread_late_work.txt). Additionally, the universal rule is to ask before the deadline rather than after, as almost everyone will grant an extension if you ask ahead of time (thread_late_work.txt). Finally, documented illness goes through the dean of students rather than the instructor (thread_late_work.txt).
```

### Can I submit work late? — run 2

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
What happens when you hand something in late is entirely dependent on the instructor, and the syllabus is accurate (e.g., if it says 10% off a day, it is 10% a day) (*thread_late_work.txt*).
```

### Can I submit work late? — run 3

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Whether you can submit work late depends entirely on the instructor, and the syllabus is accurate (thread_late_work.txt). If the syllabus states a penalty of 10% a day, that is what happens (thread_late_work.txt). A universal rule is to ask before the deadline rather than after, as almost everyone will grant an extension if you ask beforehand (thread_late_work.txt).
```

### Best quiet place to study? — run 1

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, the best study spots depend on your needs:
- Ridgeway Café before 10am is empty, quiet, and has good coffee (thread_study_spots.txt).
- The science building has open lounges on floors 2 through 5 that are unlocked and almost always empty (thread_study_spots.txt).
- The library third floor is the only place that reliably delivers silence, if you need complete silence (thread_study_spots.txt).

Source: thread_study_spots.txt
```

### Best quiet place to study? — run 2

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on thread_study_spots.txt, the library third floor is the only place that reliably delivers silence. Additionally, the science building has open lounges on floors 2 through 5 that are unlocked and almost always empty, and Ridgeway Café before 10am is empty and quiet. 

Source: thread_study_spots.txt
```

### Best quiet place to study? — run 3

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to **thread_study_spots.txt**, if you need silence, the library third floor is the only place that reliably delivers it. Alternatively, Ridgeway Café before 10am is empty and quiet, and the science building has open lounges on floors 2 through 5 that are unlocked and almost always empty.
```

### What is the best parking spot or area? — run 1

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to `thread_parking.txt`, the west permit is worth getting if you commute daily, though west lots sell out in about three days in August. Half the upper years park on Verrill because street parking there is legal, free, and unmarked.
```

### What is the best parking spot or area? — run 2

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to **thread_parking.txt**, the west permit is worth getting if you are commuting daily. Alternatively, street parking on Verrill is legal, free, and unmarked.
```

### What is the best parking spot or area? — run 3

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
Based on the documents, the best parking spot depends on your situation: 

- A west permit is worth getting if you are commuting daily (*thread_parking.txt*). 
- Street parking on Verrill is legal, free, and unmarked, which is why half the upper years use it (*thread_parking.txt*). 

Source: thread_parking.txt
```

### Where can I find information about internships? — run 1

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, you can find information about when to start looking for summer internships in **thread_internship_timing.txt**, which notes that large employers close applications in October and November and smaller places hire in February and March. Additionally, **thread_internship_timing.txt** mentions that the careers office reviews CVs on a drop-in basis.
```

### Where can I find information about internships? — run 2

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, large employers close applications in October and November, while smaller and local places hire in February and March (*thread_internship_timing.txt*). Additionally, the careers office reviews CVs on a drop-in basis (*thread_internship_timing.txt*).
```

### Where can I find information about internships? — run 3

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, large employers close applications for summer internships in October and November, while smaller and local places hire in February and March. Additionally, the careers office reviews CVs on a drop-in basis. 

Source: thread_internship_timing.txt
```


---

# Run — 2026-09-23 19:29 (test)

# Run log — test

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.625
- Runs per question: 3, caching off
- When: 2026-09-23 19:29

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Are bikes a good idea on campus? | fail | fail | pass |
| Can I submit work late? | fail | pass | fail |
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
Bikes are a mixed idea. They can cut an 18-minute walk down to about 6 minutes, but covered bike parking fills up by 9 am, and winter salt can destroy a drivetrain in a single season. 

Source: `thread_bike_commute.txt`
```

### Are bikes a good idea on campus? — run 2

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Based on the documents, bikes can be worth it because they significantly shorten commute times (cutting an 18-minute walk to about 6 minutes), but they also have drawbacks such as covered bike parking filling up by 9am, winter salt destroying drivetrains, and the risk of theft. 

Source: `thread_bike_commute.txt`
```

### Are bikes a good idea on campus? — run 3

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Bikes can be a good idea, as they can cut an 18-minute walk down to about 6 minutes, but there are drawbacks like full covered bike parking by 9 AM and drivetrain damage from ice or salt between November and March (thread_bike_commute.txt). One user manages this by keeping a cheap bike for September to November and walking the rest of the year (thread_bike_commute.txt).
```

### Can I submit work late? — run 1

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
What happens if you hand work in late is entirely instructor-dependent and follows what is written in the syllabus (Source: `thread_late_work.txt`).
```

### Can I submit work late? — run 2

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Whether you can submit work late depends entirely on the instructor, and you should check the syllabus because its policy is accurate (thread_late_work.txt). Additionally, the universal rule is to ask before the deadline rather than after, as almost everyone will grant an extension if you ask ahead of time, but almost nobody will after the deadline has passed (thread_late_work.txt). Documented illness goes through the dean of students rather than the instructor (thread_late_work.txt).
```

### Can I submit work late? — run 3

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
What happens when you hand something in late is entirely instructor-dependent, and the syllabus is accurate (if it says 10% a day, it is 10% a day). *(thread_late_work.txt)*
```

### Best quiet place to study? — run 1

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, the best study spots depend on your needs:
* **Ridgeway Café** (before 10am) is recommended as empty and quiet (thread_study_spots.txt).
* **The science building** has open lounges on floors 2 through 5 that are unlocked and almost always empty (thread_study_spots.txt).
* **The library third floor** is recommended if you specifically need silence (thread_study_spots.txt).

Source: thread_study_spots.txt
```

### Best quiet place to study? — run 2

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Depending on what you need, the library third floor is the only place that reliably delivers silence (*thread_study_spots.txt*). Additionally, Ridgeway Café before 10am is described as empty and quiet (*thread_study_spots.txt*).
```

### Best quiet place to study? — run 3

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Based on the provided documents, the best study spots depend on your needs:
- Ridgeway Café before 10am is empty, quiet, and has good coffee (thread_study_spots.txt).
- The science building has open lounges on floors 2 through 5 that are unlocked and almost always empty (thread_study_spots.txt).
- If you need silence, the library third floor is the only place that reliably delivers it (thread_study_spots.txt).

Source: thread_study_spots.txt
```

### What is the best parking spot or area? — run 1

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to `thread_parking.txt`, the west permit is worth getting if you are commuting daily. Alternatively, street parking on Verrill is legal, free, and unmarked, which is why half the upper years use it.
```

### What is the best parking spot or area? — run 2

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to the documents, west lots are worth getting if you are commuting daily, though they sell out in about three days in August, while the east lot never sells out (thread_parking.txt). Additionally, street parking on Verrill is noted as legal, free, and unmarked (thread_parking.txt). 

Source: thread_parking.txt
```

### What is the best parking spot or area? — run 3

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to `thread_parking.txt`, the west permit is worth getting if you are commuting daily. If you are not commuting daily, the documents state that street parking on Verrill is legal, free, and unmarked.
```

### Where can I find information about internships? — run 1

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to the documents, you can find information about when to start looking for summer internships in **thread_internship_timing.txt**, which notes that large employers close applications in October and November, while smaller and local places hire in February and March. Additionally, **thread_internship_timing.txt** mentions that the careers office reviews CVs on a drop-in basis.
```

### Where can I find information about internships? — run 2

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
You can find information about internships by looking at the thread about internship timing, which notes that large employers close applications in October and November and smaller, local places hire in February and March (`thread_internship_timing.txt`). Additionally, the careers office reviews CVs on a drop-in basis (`thread_internship_timing.txt`).
```

### Where can I find information about internships? — run 3

- Best distance: 0.5371 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_internship_timing.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to *thread_internship_timing.txt*, large employers close applications for summer internships in October and November, while smaller and local places hire in February and March.
```


---

# Run — 2026-09-23 19:30 (final_test_with_no_changes)

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


---

# Run — 2026-09-27 23:10 (final_test_with_no_changes)

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


---

# Run — 2026-09-27 23:58 (after)

# Run log — after

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `advice_threads` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.625
- Runs per question: 3, caching off
- When: 2026-09-27 23:58

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Are bikes a good idea on campus? | pass | pass | pass |
| Can I submit work late? | pass | pass | pass |
| Best quiet place to study? | pass | pass | pass |
| What is the best parking spot or area? | fail | fail | fail |
| What is the best time to look for an internship? | pass | pass | fail |

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
Bikes can be a good idea, as they can cut an 18-minute walk to about 6 minutes, but there are drawbacks like full covered bike parking by 9 am and salt from winter paths destroying drivetrains in one season (*thread_bike_commute.txt*). To handle this, one person suggests keeping a cheap bike for September to November and walking the rest of the year (*thread_bike_commute.txt*).
```

### Are bikes a good idea on campus? — run 2

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Whether bikes are a good idea depends on the season and storage availability. Covered bike parking fills up by 9 am, salt in the winter can destroy a drivetrain in one season, and paths are icy or salted between November and March, though some students use a cheap bike for autumn and walk the rest of the year. 

Source: thread_bike_commute.txt
```

### Are bikes a good idea on campus? — run 3

- Best distance: 0.3857 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_commuting.txt, thread_first_gen.txt, thread_laptop_specs.txt, thread_study_spots.txt

```
Based on the provided documents, bikes can be worth it because they shorten commute times (cutting an 18-minute walk to about 6 minutes), but they also have drawbacks such as full covered parking by 9 am, and winter salt that can destroy a drivetrain in one season. Some students address this by using a cheap bike for part of the year and walking the rest. 

Source: `thread_bike_commute.txt`
```

### Can I submit work late? — run 1

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Yes, submitting work late is entirely instructor-dependent, and the policy stated in the syllabus is accurate (e.g., if it says 10% off per day, that is the rule). However, a universal rule is to ask before the deadline rather than after. (Source: thread_late_work.txt)
```

### Can I submit work late? — run 2

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
Yes, what happens when you hand something in late is entirely dependent on the instructor, and the syllabus is accurate (e.g., if it says 10% a day, it is 10% a day). Additionally, the universal rule is to ask before the deadline rather than after, as almost everyone will give you two days if you ask ahead of time, but almost nobody will on the following Monday. (Source: thread_late_work.txt)
```

### Can I submit work late? — run 3

- Best distance: 0.5854 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_group_project.txt, thread_late_work.txt, thread_professor_email.txt

```
What happens when you hand something in late is entirely instructor-dependent, and the syllabus is accurate (e.g., if it says 10% a day, it's 10% a day) (*thread_late_work.txt*). However, the universal rule is to ask before the deadline rather than after (*thread_late_work.txt*). Documented illness goes through the dean of students rather than the instructor, and that route works (*thread_late_work.txt*).
```

### Best quiet place to study? — run 1

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to thread_study_spots.txt, the library third floor is the only place that reliably delivers silence if you need it. Alternatively, Ridgeway Café before 10am is empty and quiet, and the science building has open lounges on floors 2 through 5 that are almost always empty.
```

### Best quiet place to study? — run 2

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
Depending on what you need, the third floor of the library is the only place that reliably delivers silence (from thread_study_spots.txt). Alternatively, Ridgeway Café before 10am is empty and quiet (from thread_study_spots.txt).
```

### Best quiet place to study? — run 3

- Best distance: 0.3706 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_first_gen.txt, thread_office_hours_etiquette.txt, thread_sleep_schedule.txt, thread_study_spots.txt

```
According to the documents, if you need silence, the third floor of the library is the only place that reliably delivers it (thread_study_spots.txt). Alternatively, Ridgeway Café before 10am is noted as being empty and quiet (thread_study_spots.txt).
```

### What is the best parking spot or area? — run 1

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to `thread_parking.txt`, the west permit is worth getting if you are commuting daily. Alternatively, street parking on Verrill is legal, free, and unmarked, which is why half the upper years use it.
```

### What is the best parking spot or area? — run 2

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to *thread_parking.txt*, the west permit is worth getting if you are commuting daily. Otherwise, street parking on Verrill is legal, free, and unmarked, which is why half the upper years use it.
```

### What is the best parking spot or area? — run 3

- Best distance: 0.5111 (passed the gate)
- Sources retrieved: thread_bike_commute.txt, thread_internship_timing.txt, thread_parking.txt, thread_study_spots.txt, thread_winter_advice.txt

```
According to `thread_parking.txt`, the west permit is worth getting if you commute daily, though west lots sell out in about three days in August. Half the upper years park on Verrill because street parking there is legal, free, and unmarked.
```

### What is the best time to look for an internship? — run 1

- Best distance: 0.3742 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_internship_timing.txt, thread_late_work.txt, thread_professor_email.txt, thread_sleep_schedule.txt

```
You should start looking earlier than feels reasonable, as large employers close applications in October and November for the following summer. Smaller and local places hire in February and March. 

Source: `thread_internship_timing.txt`
```

### What is the best time to look for an internship? — run 2

- Best distance: 0.3742 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_internship_timing.txt, thread_late_work.txt, thread_professor_email.txt, thread_sleep_schedule.txt

```
You should look earlier than feels reasonable, as large employers close applications in October and November for the following summer. Smaller and local places hire in February and March. 

Source: thread_internship_timing.txt
```

### What is the best time to look for an internship? — run 3

- Best distance: 0.3742 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_internship_timing.txt, thread_late_work.txt, thread_professor_email.txt, thread_sleep_schedule.txt

```
Large employers close their applications in October and November for the following summer, while smaller and local places hire in February and March. 

Source: `thread_internship_timing.txt`
```


---

# Run — 2026-09-28 00:49 (stretch_feature)

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

