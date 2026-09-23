+++
date = '2026-09-30'
due_date = '2026-10-14T23:59:00'
draft = false
title = 'Homework 5: A Query Engine Made of Pipes'
weight = 50
status = 'Scheduled'
+++

Answer one question about 863,077 US Forest Service records of invasive plants — which ones cover the most ground, and where — by building the machine that runs the SQL rather than writing the SQL. Across eight test-driven phases you will write a single Python file that becomes seven command-line tools, each reading CSV on stdin and writing CSV on stdout, then compose them into a pipeline with Unix pipes: filter, select, group-by, aggregate, order-by, head. Along the way you will parse CSV correctly including quoted fields with embedded commas and newlines, decide what a text field actually means and handle nulls the way SQL does, stream rows so memory does not grow with the file, sort by several keys in either direction, and compute count, sum, avg, min, and max for a group without ever holding the group's rows.

<!-- more -->


Related session: [Session 6 — Unix File System and Command Line](../../topics/topic-06/)

### The Phases

| | |
|---|---|
| **1** | What a field means — number, date, word, or nothing at all |
| **2** | `select` — choosing columns |
| **3** | `filter` — keeping rows, and why null does not compare |
| **4** | `schema` — what is in this file? |
| **5** | `order-by` — several keys, either direction, mixed types |
| **6** | `group-by` — making equal keys neighbours |
| **7** | The parts of an aggregate: a group is five running numbers |
| **8** | `aggregate` — one pass over grouped rows |

Building the stages separately makes visible the three rules an SQL engine
hides: filtering and projecting are cheap, sorting is expensive because it
cannot emit its first row until it has read its last, and grouped aggregation
requires equal keys to be neighbours. Only `order-by` and `group-by` may hold
the whole stream; the tests measure the rest.

### Topics Covered

- Reading and writing CSV correctly, including quoted and multi-line fields
- Type inference on text fields, and SQL's treatment of nulls
- Streaming: handle a row, emit it, forget it
- Sorting on several keys, ascending and descending, in a mixed-type column
- Running aggregates over a group without storing its rows
- Programs as filters: stdin, stdout, exit status, and composition with pipes
- One file with several names, and how a program knows which it was called by
- Why the order of pipeline stages is a query plan

### Instructions

The full instructions, the starter file, and the per-phase tests are released
through the course template. On the course server run `ifi8410-update`, then
read `Assignments/HW05/instructions/homework05_instructions.md` and work in
`Assignments/HW05/submission/`.

The dataset is already on the cluster under
`/data/public/usda/us-forest-service/` — do not copy it. No pandas, numpy,
`sqlite3`, or any other dataframe or database library. Hand in with
`ifi8410-test` and `ifi8410-submit`.
