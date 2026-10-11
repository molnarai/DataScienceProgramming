+++
date = '2026-11-04'
due_date = '2026-11-18T23:59:00'
draft = false
title = 'Homework 10: Three Ways to Find It'
weight = 100
status = 'Posted'
+++

Almost every program you have written this term looks something up: `if word in words`, `businesses[business_id]`. This week you build what is inside, three times, and count the work each way takes. On 100,000 Yelp business ids, looking at every item costs about 50,000 comparisons per lookup, halving a sorted list costs 16, and a hash table costs about one — a difference that does not depend on how fast the computer is. Across seven test-driven phases you will write linear search, binary search, and a search for where a value belongs in a sorted list; a hash function for strings; and a hash table of buckets that grows as it fills. Then you will compare the three by counting comparisons, and work out when sorting pays for itself.

<!-- more -->


Related session: [Session 11 — Search and Hashing](../../topics/topic-11/)

### The Phases

| | |
|---|---|
| **1** | Look at every item — linear search |
| **2** | Halve a sorted list — binary search |
| **3** | Where would it go? — the leftmost position, and counting a range |
| **4** | A number for every key — a hash function |
| **5** | A table of buckets — put and get |
| **6** | A table that grows — load factor and resizing |
| **7** | What does a lookup cost? — the comparison, and the break-even point |

Every search returns its answer and the number of comparisons it made. A time
depends on the machine and on luck; a count is exact, the same everywhere, and
shows directly how the work grows with the size of the list. Each method buys
its speed with a requirement: binary search needs sorted data, and a hash
table can say whether exactly this key is here but not which keys lie between
two others.

### Topics Covered

- Linear search and its cost, especially for a key that is not there
- Binary search: the invariant, the off-by-one traps, and the need for sorted data
- Insertion positions and range counts on sorted data
- Hash functions: same key, same number; why order of characters must matter
- Hash tables with buckets, collisions, load factor, and resizing
- Counting comparisons rather than timing
- Linear, logarithmic, and constant growth
- When sorting first is worth it

### Instructions

The full instructions, the starter file, and the per-phase tests are released
through the course template. On the course server run `ifi8410-update`, then
read `Assignments/HW10/instructions/homework10_instructions.md` and work in
`Assignments/HW10/submission/`.

Use only the standard library — no numpy, no pandas. In Phases 1 to 6 do not
use `in`, `.index()`, `bisect`, `dict`, `set`, or the built-in `hash()` to do
the searching or the storing; the tests measure the comparisons your code
makes. The report uses the Yelp business ids on the cluster. Hand in with
`ifi8410-test` and `ifi8410-submit`.
