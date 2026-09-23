+++
date = '2026-09-23'
due_date = '2026-10-07T23:59:00'
draft = false
title = 'Homework 4: A Pipeline Through Five Gigabytes of Reviews'
weight = 40
status = 'Scheduled'
+++

Find the restaurants Yelp reviewers disagreed about most in 2018 and 2019, working from the 5.3 GB review file on the cluster, which is far too large to load into memory. Across nine test-driven phases you will build a pipeline of stages in core Python, each reading the file the stage before it wrote, one record at a time. You will filter the business and review files, join reviews to a small lookup table, compute count, mean, and standard deviation for thousands of restaurants without storing the values, and sort a file of any size by reusing your HW03 merge sort on files. Finally you will run the whole pipeline from the command line and print a ranked report. Every phase is tested on a small sample of the dataset before you run it on the real thing.

<!-- more -->


Related session: [Session 5 — Files, Modules, and Scripts](../../topics/topic-05/)

### The Phases

| | |
|---|---|
| **1** | Filter the small table — 150,346 businesses down to restaurants |
| **2** | Filter the big table — 6,990,280 reviews down to 2018–2019 |
| **3** | Join the reviews to the businesses |
| **4** | Aggregates one value at a time: count, mean, standard deviation |
| **5** | Group the joined records |
| **6** | Sorting with `sorted()`, and where it stops working |
| **7** | Divide a file, and combine two sorted files |
| **8** | Sort a file of any size |
| **9** | The report, and the whole pipeline from the command line |

Each stage writes a file the next stage reads, so nothing ever holds the big
file in memory. The measurable result is that the program's memory does not grow
with the size of its input — and the tests check it.

### Topics Covered

- Streaming a multi-gigabyte JSON Lines file one record at a time
- Filtering and projecting; keeping only the fields later stages need
- Joining a large file against a small lookup dictionary
- Running aggregates — count, sum, min, max, mean, standard deviation — without
  storing the values
- External merge sort: splitting a file, merging sorted files, recursion
- Composing stages into a pipeline and running it from the shell
- Reasoning about where a program's memory goes

### Instructions

The full instructions, the starter file, and the per-phase tests are released
through the course template. On the course server run `ifi8410-update`, then
read `Assignments/HW04/instructions/homework04_instructions.md` and work in
`Assignments/HW04/submission/`.

The dataset is already on the cluster in `/data/public/yelp` — do not copy it.
Everything is core Python (`json`, `pathlib`, `sys`); no pandas, no numpy. Hand
in with `ifi8410-test` and `ifi8410-submit`.
