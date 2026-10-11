+++
date = '2026-10-07'
due_date = '2026-10-21T23:59:00'
draft = false
title = 'Homework 6: Northwind, Audited and Joined'
weight = 60
status = 'Posted'
+++

Somebody hands you four CSV files from Northwind, the small food importer from Session 7, and asks which product category earns the most. The answer is one `groupby` away; this assignment is about everything that has to be true before that `groupby` can be trusted. Across seven test-driven phases you will write a single pandas program that audits the tables, splits a file stored at the wrong grain into the two tables it really is, finds rows whose foreign key points at nothing, joins four tables into one view without dropping or repeating a row, and then groups, counts, and ranks to produce a report. Along the way you will meet four things wrong with the data: freight repeated on every order line, rows with no partner, a `unitprice` column that exists twice and means two different things, and lines with no category whose revenue disappears without an error if you group carelessly.

<!-- more -->


Related session: [Session 7 — Data Tables](../../topics/topic-07/)

### The Phases

| | |
|---|---|
| **1** | What is in this table? — rows, a unique key, and what is missing |
| **2** | One file, two grains — splitting `orders.csv` into orders and order lines |
| **3** | Rows with no partner — orphans, and customers who never ordered |
| **4** | The view — one row per order line, joined from four tables |
| **5** | Group and total — so that nothing disappears |
| **6** | Count the right thing — orders, not rows |
| **7** | Rank within a group, and the report |

Each phase meets one way a table quietly gives the wrong answer. Summing
freight over order lines counts it once per line; an inner join drops the line
for an unknown product; a repeated key in a parent table repeats every line
that points at it; and `groupby` drops rows whose key is missing. None of these
raises an error — the report is simply wrong, and it looks fine.

### Topics Covered

- Describing a table: its grain, its key, and its missing values
- Reading CSV and JSON into the same table
- Grain: recognising a denormalized file and splitting it
- Foreign keys, orphans, and the difference between "points at nothing" and "unknown"
- Left joins, many-to-one validation, and columns with the same name in two tables
- Group and total with missing group names (`dropna=False`)
- Counting distinct values versus counting rows; filtering groups after grouping
- Ranking within a group

### Instructions

The full instructions, the starter file, and the per-phase tests are released
through the course template. On the course server run `ifi8410-update`, then
read `Assignments/HW06/instructions/homework06_instructions.md` and work in
`Assignments/HW06/submission/`.

The real dataset is already on the cluster under `/data/public/northwind/`
(830 orders, 2,155 order lines) — do not copy it. A tiny copy with 7 orders and
14 order lines is in `test/fixtures/northwind/`; work with that one, since you
can check every answer by hand. Use pandas, which is already in the course
environment. Hand in with `ifi8410-test` and `ifi8410-submit`.
