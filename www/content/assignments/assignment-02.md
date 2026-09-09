+++
date = '2026-09-09'
due_date = '2026-09-22'
draft = false
title = 'Homework 2: Bike-Share Trip Analysis'
weight = 20
status = 'Scheduled'
+++

Analyze a month of campus bike-share trips using nothing but core Python — no pandas, no NumPy, no file reading, just a list of dictionaries and the loop patterns from 

Session 3. Across eight test-driven phases you will count records by any field, collect distinct values into a set, accumulate totals and averages, filter records without modifying the originals, find a maximum with a tie-break that makes the answer reproducible, group and sum riding time by rider type, and use membership tests to catch a station that does not belong — then assemble every result into one summary and print an exactly formatted report. Each phase ships with its own tests, so you find out whether the piece you just wrote works before you build the next one on top of it.

<!-- more -->


**Posted:** September 9, 2026 &nbsp;&nbsp;|&nbsp;&nbsp; **Due:** Tuesday, September 22, 2026 at 23:59

Related session: [Session 3 — Loops and Core Data Structures](../../topics/topic-03/)


## Learning objectives

Session 3 gave you four containers, two kinds of loop, and four loop patterns.
This assignment applies all of them to a second dataset in the same shape as the
coffee-cart data — a month of campus bike-share trips — using **core Python
only**.

Your program will:

1. Count records by any field, using a dictionary whose keys come from the data.
2. Collect the distinct values of a field into a set.
3. Accumulate a numeric total and an average.
4. Filter records into new lists without modifying the originals.
5. Find the largest value in a counts dictionary, with a defined tie-break.
6. Group and sum — total riding time per rider type.
7. Check data quality with membership tests.
8. Assemble everything into one summary and print a formatted report.

No pandas, no numpy, no file reading. The dataset is a list of dictionaries
defined in the starter file. Every function is a loop over that list.

You may use `sorted()`, `round()`, `len()`, and `collections.Counter`, but the
first phase deliberately asks you to write the counting idiom yourself — that is
the point of the session, and later phases build on it.

## How to work on this assignment

**Do not write the whole program and then run it.** The assignment is split into
eight phases. Each phase adds one or two functions and has its own test file.
Work in this order:

1. Read the phase description.
2. Implement only the functions in that phase.
3. Run that phase's tests: `./run_tests.sh 2` for Phase 2.
4. Fix your code until every test in that phase passes.
5. Only then move to the next phase.

Later phases call the functions you wrote in earlier ones — Phase 7 calls almost
everything — so a bug you leave behind in Phase 1 will produce confusing
failures in Phase 7. Catching it in Phase 1 costs a minute.

You test in two places, and they do different jobs:

| | Where | When | What it is for |
|---|---|---|---|
| **Locally** | on the cluster, `./run_tests.sh N` | constantly, while you work | Fast feedback on the phase you are writing |
| **Pipeline** | GitLab, on merge into `testing` | once a phase is done | The record of what passed; this is what counts |

The test suite is not hidden. It lives in [`../test/`](../test/) and you are
expected to read it. Editing your copy achieves nothing: the pipeline runs the
course's copy, plus additional tests you do not have.

## Setup

Work on the `work` branch of your course repository:

```bash
git checkout work
cd Assignments/HW02
mkdir -p submission
cp starter/bikeshare.py submission/bikeshare.py
cp starter/JOURNAL.md submission/JOURNAL.md
```

### The notebook

There is a guided notebook for this assignment:

```text
Assignments/HW02/starter/Instructions_orig.ipynb
```

Rename it to drop the `_orig` before you run anything, then work through it. It
walks the eight phases in the same order as this handout, gives you a cell to
experiment in, and checks each function as you write it. This handout stays the
authority on every rule; the notebook is the guided path through it. Either way,
the file you submit is `submission/bikeshare.py`.

Your directory should then look like this:

```text
Assignments/HW02/
├── instructions/
│   └── homework02_instructions.md
├── starter/
│   ├── Instructions_orig.ipynb  <- rename it, then work in it
│   ├── bikeshare.py         <- the untouched template; leave it alone
│   └── JOURNAL.md
├── submission/              <- everything you write goes here
│   ├── bikeshare.py         <- the file you edit
│   └── JOURNAL.md           <- required, not graded
└── test/                    <- the test suite; read it, do not edit it
```

**Do not edit anything in `starter/`, `test/`, or `instructions/`.** Only files
under `submission/` are read as your solution, and the file must be named
`bikeshare.py`. A later release replaces the other folders and your edits there
would be lost.

Check that the tests can find your file:

```bash
cd test
./run_tests.sh
```

You should see a long list of failures. That is correct — you have not written
anything yet. If instead you see `Could not find bikeshare.py`, your file is in
the wrong place; re-read the tree above.

Every `./run_tests.sh` command below is run from that `test/` directory.

```bash
./run_tests.sh 2      # just Phase 2's tests
./run_tests.sh        # all of them
./run_tests.sh 3 -x   # Phase 3, stopping at the first failure
```

## The dataset

`TRIPS` is defined near the top of the starter file: a list of dictionaries,
one per bike-share trip.

```python
{
    "trip_id": 1001,
    "start_station": "Library North",
    "end_station": "Student Center",
    "day": "Mon",
    "hour": 8,
    "minutes": 11,
    "rider_type": "member",
    "bike_type": "classic",
}
```

| Field | Type | Notes |
|---|---|---|
| `trip_id` | `int` | unique |
| `start_station` | `str` | where the bike was taken |
| `end_station` | `str` | where it was returned; may equal the start |
| `day` | `str` | `"Mon"` … `"Sun"` |
| `hour` | `int` | 0–23, the hour the trip started |
| `minutes` | `int` | trip duration |
| `rider_type` | `str` | `"member"` or `"casual"` |
| `bike_type` | `str` | `"classic"` or `"electric"` |

Two constants sit beside it:

```python
KNOWN_STATIONS = ("Library North", "Student Center", ...)   # the official station list
DAY_ORDER = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
```

Both are **tuples**, because both are fixed reference data that no part of your
program should modify. `DAY_ORDER` exists because alphabetical order puts Friday
before Monday, which is not how anyone reads a weekly report.

`TRIPS` contains at least one trip touching a station that is **not** in
`KNOWN_STATIONS`. That is deliberate, and Phase 6 is what finds it.

## Rules that apply to every function

These are checked by the tests, so read them once now.

- **Never modify the argument.** Your functions read `records`; they do not
  append to it, sort it in place, or change the dictionaries inside it. Build
  and return something new.
- **Do not read the global `TRIPS`** inside any function except `main()`. Every
  function takes the records it works on as a parameter — that is what lets the
  tests call it with their own small fixtures.
- **Handle the empty case.** An empty list of records is not an error. Each
  phase says what to return for it.
- **Return the type asked for**, exactly. A `dict` is not a `Counter`, and a
  `list` is not a `set`. The tests check with `type(...)`.
- **No `input()`**, and no printing anywhere except in `format_report`'s caller
  and `main`. A function that prints instead of returning fails its tests.

## Required functions

Keep these names and parameter lists **exactly** as shown. You may add helper
functions, but do not remove, rename, or re-order the required ones — the tests
call them directly.

| Phase | Function | Purpose |
|---:|---|---|
| 1 | `count_by(records, field)` | Count records per distinct value of a field |
| 1 | `unique_values(records, field)` | The distinct values of a field, as a set |
| 2 | `total_of(records, field)` | Sum a numeric field |
| 2 | `average_of(records, field)` | Mean of a numeric field |
| 3 | `select_where(records, field, value)` | Records whose field equals a value |
| 3 | `select_longer_than(records, minutes)` | Trips strictly longer than a duration |
| 4 | `most_common(counts)` | The `(key, count)` pair with the largest count |
| 5 | `busiest_hour(records)` | The hour with the most trips |
| 5 | `total_by(records, group_field, value_field)` | Group-by-and-sum |
| 6 | `unknown_stations(records, known_stations)` | Stations not in the official list |
| 7 | `summarize(records, known_stations)` | Assemble every result into one dictionary |
| 8 | `format_report(summary)` | Return the whole report as one string |
| 8 | `main()` | Analyze `TRIPS` and print the report |

---

# The phases

## Phase 1 — Counting and distinct values

Implement `count_by(records, field)` and `unique_values(records, field)`.

### `count_by(records, field)`

Return a dictionary mapping each distinct value of `records[i][field]` to the
number of records having it.

```python
count_by(TRIPS, "rider_type")   # {"member": 13, "casual": 9}
count_by(TRIPS, "hour")         # {8: 6, 9: 3, 12: 3, ...}
```

- The keys come from the data. Do not hard-code `"member"` and `"casual"` — the
  same function must work for `"day"`, `"hour"`, and `"bike_type"`.
- Values are integers.
- Empty records produce an empty dictionary `{}`.
- Return a **plain `dict`**. A `Counter` is a dict subclass and would compare
  equal, but the tests check `type(result) is dict`. The point of this phase is
  that you can build it yourself; if you use `Counter`, convert with `dict(...)`
  and know what you skipped.

This is Section 13 of the session notebook. Either spelling works — the explicit
`if field_value not in counts:` check, or the `counts.get(value, 0) + 1`
shorthand.

### `unique_values(records, field)`

Return a **set** of the distinct values of that field. Empty records produce an
empty set — which you create with `set()`, not `{}`.

```bash
./run_tests.sh 1
```

**Do not continue until every test in Phase 1 passes.**

## Phase 2 — Totals and averages

Implement `total_of(records, field)` and `average_of(records, field)`.

`total_of` returns the sum of `records[i][field]` over every record. Start the
accumulator at `0`. An empty list totals `0`.

`average_of` returns the mean as a **float**: the total divided by the number of
records. An empty list averages `0.0` — divide first and you get
`ZeroDivisionError`, so check the length before you divide.

Do **not** round inside `average_of`. Rounding is a display decision and belongs
in `format_report`; a function that rounds early throws away precision its
callers may need.

```bash
./run_tests.sh 2
```

## Phase 3 — Filtering

Implement `select_where(records, field, value)` and
`select_longer_than(records, minutes)`.

Both return a **new list** containing the records that match, **in their
original order**. Both return `[]` when nothing matches.

- `select_where` matches with `==` on `records[i][field]`. It must work for
  string fields and integer fields alike: `select_where(TRIPS, "hour", 8)` is a
  valid call.
- `select_longer_than` keeps trips whose `minutes` is **strictly greater than**
  the argument. A 15-minute trip is not longer than 15.

The returned list holds the *same dictionary objects* as the input — that is
expected and correct. What must not happen is a change to the input list itself.

```bash
./run_tests.sh 3
```

## Phase 4 — The maximum, with a tie-break

Implement `most_common(counts)`.

The argument is a counts dictionary of the kind Phase 1 produces. Return a
**tuple** `(key, count)` for the key with the largest count.

- **Ties go to the smaller key.** If `"Tue"` and `"Wed"` both have 4 trips,
  return `("Tue", 4)` — `"Mon" < "Wed"` as strings. If hours 8 and 17 tie,
  return `(8, ...)`. Without this rule the answer would depend on dictionary
  insertion order, and the same program would give different answers on
  different data orderings.
- An empty dictionary returns `(None, 0)`.

The scan is the maximum pattern from Section 14 of the notebook, with one extra
clause in the condition: replace the best-so-far when the count is larger, **or**
when the count is equal and the key is smaller.

```bash
./run_tests.sh 4
```

## Phase 5 — Busiest hour and group-by-and-sum

Implement `busiest_hour(records)` and `total_by(records, group_field, value_field)`.

### `busiest_hour(records)`

Return the `(hour, count)` tuple for the hour with the most trips. Ties go to the
**earlier** hour. Empty records return `(None, 0)`.

Write this by calling the two functions you already have. If `count_by` and
`most_common` are correct, this is one line — and the tie-break you specified in
Phase 4 is exactly the "earlier hour" rule. Re-implementing the scan here is a
missed opportunity to see why the tie-break was defined that way.

### `total_by(records, group_field, value_field)`

Return a dictionary mapping each distinct value of `group_field` to the **sum**
of `value_field` over the records in that group.

```python
total_by(TRIPS, "rider_type", "minutes")   # {"member": 141, "casual": 186}
```

This is counting with one change: instead of adding `1` per record, add
`record[value_field]`. It is a group-by-and-sum written by hand — the same
operation as pandas' `df.groupby("rider_type").minutes.sum()`, which you will
meet in Session 8.

Empty records produce `{}`. Return a plain `dict`.

```bash
./run_tests.sh 5
```

## Phase 6 — Data quality

Implement `unknown_stations(records, known_stations)`.

Return a **sorted list** of the distinct station names that appear in the data
but are **not** in `known_stations`. Check **both** `start_station` and
`end_station` — a bike can be returned to a station it was never taken from.

- Each unknown name appears once, however many trips touched it.
- The list is sorted alphabetically, so the report is reproducible.
- When every station is known, return `[]`.
- `known_stations` may be a tuple, a list, or a set. Do not assume which.

This is the membership test from Section 17: build a set of the offenders while
you loop, then `sorted()` it on the way out. A set collects the distinct names;
the sorted list makes the output deterministic.

```bash
./run_tests.sh 6
```

## Phase 7 — The summary

Implement `summarize(records, known_stations)`.

Return one dictionary with **exactly** these keys, built by calling the functions
from the earlier phases:

| Key | Type | Value |
|---|---|---|
| `"trip_count"` | `int` | number of records |
| `"station_count"` | `int` | how many distinct stations appear, start and end together |
| `"total_minutes"` | `int` | total riding time |
| `"average_minutes"` | `float` | mean trip duration, unrounded |
| `"trips_by_day"` | `dict` | day → trip count |
| `"trips_by_rider"` | `dict` | rider type → trip count |
| `"trips_by_bike"` | `dict` | bike type → trip count |
| `"minutes_by_rider"` | `dict` | rider type → total minutes |
| `"busiest_hour"` | `tuple` | `(hour, count)` |
| `"top_start_station"` | `tuple` | `(station, count)`, the most frequent start |
| `"unknown_stations"` | `list` | sorted, from Phase 6 |

Two of these need a moment's thought.

`station_count` counts start and end stations **together as one pool**: a station
used only as a destination still counts. `unique_values` handles one field at a
time, so take the union of two sets — with `|`, or `.update()`, or two loops.

`top_start_station` is `most_common(count_by(records, "start_station"))`.

For empty records, every count is `0`, every dictionary is `{}`, every tuple is
`(None, 0)`, `average_minutes` is `0.0`, and `unknown_stations` is `[]`. Written
with your earlier functions, this falls out for free — which is the argument for
having handled the empty case in each of them.

```bash
./run_tests.sh 7
```

## Phase 8 — The report

Implement `format_report(summary)` and `main()`.

### `format_report(summary)`

Return the entire report as **one string**. Do not print anything, and do not end
the string with a newline — `print()` adds that.

The exact expected output for the starter dataset:

```text
BIKE-SHARE TRIP REPORT
======================

Trips analyzed: 22
Distinct stations: 6
Total riding time: 327 minutes
Average trip: 14.9 minutes

Trips by day
  Mon             5
  Tue             4
  Wed             4
  Thu             3
  Fri             3
  Sat             2
  Sun             1

Trips by rider type
  casual          9
  member         13

Trips by bike type
  classic        13
  electric        9

Riding time by rider type
  casual        186 minutes
  member        141 minutes

Busiest hour: 8:00 (6 trips)
Most common start station: Library North (6 trips)

Unknown stations: Riverside Annex
```

The formatting rules, precisely:

- Section titles are on their own line, with **no** blank line between a title
  and its first row. One blank line separates sections.
- Every data row begins with **two spaces**. The label is left-aligned in a
  field **14** characters wide and the number right-aligned in a field **3**
  wide: `f"  {label:<14}{value:>3}"`. Rows in the riding-time section end with
  `" minutes"`.
- `Trips by day` is ordered by `DAY_ORDER`, **not** alphabetically, and days with
  no trips are omitted. The other three count sections are sorted
  **alphabetically by key**.
- `Average trip` is rounded to **one** decimal place with `:.1f`. This is the
  only place rounding happens.
- The hour is written `8:00`, with no leading zero — `f"{hour}:00"`.
- The last line is `Unknown stations: ` followed by the names joined with
  `", "`. When there are none, the line reads exactly
  `Unknown stations: none`.
- A section whose dictionary is empty prints its title and no rows.

Build the report as a **list of lines** and `"\n".join(lines)` at the end.
Concatenating onto a string with `+=` in a loop works but is harder to read and
harder to fix when one line is wrong.

If a test fails here, read the diff pytest prints character by character. Almost
every failure in this phase is one space, one missing blank line, or a `:>3`
written as `:<3`.

### `main()`

Analyze the module-level `TRIPS` with `KNOWN_STATIONS`, and print the report:

```python
def main():
    summary = summarize(TRIPS, KNOWN_STATIONS)
    print(format_report(summary))
```

This is the one function that may use the global `TRIPS`. Run the program the
way any script is run:

```bash
cd ../submission
python3 bikeshare.py
```

```bash
./run_tests.sh 8
./run_tests.sh        # everything, one last time
```

---

## The journal

`submission/JOURNAL.md` is **required** and **not graded**. Nothing you write in
it can lower your mark; the automatic check only confirms that you wrote roughly
forty words of your own. Be honest about dead ends, about help from peers or the
instructor, and about AI tools — which one, what you asked, and whether you used,
adapted, or rejected the answer. Recording help never costs you marks.

See [`../../../Shared/ASSIGNMENT-JOURNAL.md`](../../../Shared/ASSIGNMENT-JOURNAL.md).

## In your journal, answer this

One question is worth thinking about while you work, and it is the reason the
assignment is shaped this way:

> `count_by` and `total_by` are nearly the same function — one adds `1` per
> record, the other adds a field's value. Could one function do both jobs? What
> would its signature look like, and would the result be easier or harder to
> read at the call site?

There is no required answer. Session 4 is about exactly this question.

## Submitting

```bash
git add Assignments/HW02/submission
git commit -m "HW02: phase 3 complete"
git push origin work
```

Then open a merge request from `work` into `testing`. The `hw02` job runs your
submission against the course's copy of the tests plus additional hidden ones.
Until the last phase is done most of the pipeline will be red — that is expected.
Look for the phase you just finished and ignore the rest.
