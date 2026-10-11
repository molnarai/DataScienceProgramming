+++
date = '2026-10-14'
due_date = '2026-10-28T23:59:00'
draft = false
title = 'Homework 7: Invasive Plants, from Raw File to Report'
weight = 70
status = 'Posted'
+++

In HW05 you built a query engine for the Forest Service file of invasive plants, one row at a time. This week you meet the same 863,069 records again with pandas, where a question that took a pipeline takes a line — and a line of pandas will always give you a number, whether or not the number means anything. Across seven test-driven phases you will write a single program that inspects the raw table, cleans it (text into dates, missing values disguised as the word `Unknown`, values that cannot be true), computes whole columns at once with no loop, and summarises the records by forest, by species, and by year. The assignment turns on one column: half of the records have no `cover_pct`, and the average cover is 17.1 %, 8.5 %, or 18.4 % depending on what you decide a blank means.

<!-- more -->


Related session: [Session 8 — Python for Data Analysis](../../topics/topic-08/)

### The Phases

| | |
|---|---|
| **1** | Look before you compute — types, missing values, distinct values |
| **2** | Clean — dates, disguised blanks, impossible values |
| **3** | Whole columns at once — arithmetic and labels with no loop |
| **4** | What does a blank mean? — three policies, three averages |
| **5** | Split, apply, combine — one row per forest |
| **6** | A group's total on every row — `transform` against `agg` |
| **7** | Over time, a JSON file, and the report |

"We do not know", "nothing was there", and "about what is usual in that forest"
are three defensible readings of an empty cell, and they put the average a
factor of two apart. Which one is right is not a pandas question, and no error
message will raise it for you. So the program reports all three, with the
number of rows each average was taken over.

### Topics Covered

- Inspecting a table before computing from it
- Cleaning: parsing dates, finding missing values written as words, making impossible values missing without deleting the row
- Vectorized computation: `where`, `mask`, `np.select`, and why not to loop over rows
- Missing data as a decision: drop, fill with zero, fill with a group median
- Split-apply-combine with named aggregation
- `transform` versus `agg`: keeping the table's shape or shrinking it
- Summaries over time, and writing a table to JSON

### Instructions

The full instructions, the starter file, and the per-phase tests are released
through the course template. On the course server run `ifi8410-update`, then
read `Assignments/HW07/instructions/homework07_instructions.md` and work in
`Assignments/HW07/submission/`.

The real file is already on the cluster under
`/data/public/usda/us-forest-service/current-invasive-plants/` — do not copy
it. A 16-record copy is in `test/fixtures/plants/`; work with that one, since
you can check every answer by hand. Use pandas and numpy, which are already in
the course environment. Phase 3 allows no `for`, `while`, comprehension,
`.apply`, or `.iterrows`, and the tests check it. Hand in with `ifi8410-test`
and `ifi8410-submit`.
