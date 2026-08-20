---
date: 2026-11-04
classdates: '2026-11-04'
draft: false
title: 'Search and Hashing'
concept: "Search as a fundamental operation. Linear versus binary search and the assumptions each requires. Hashing intuition and why dictionary lookup is fast; introductory efficiency tradeoffs."
practice: "Implement linear and binary search; time lookups on lists versus dictionaries and sets; compare approaches empirically. In-class: compare lookup methods on structured data."
weight: 110
numsession: 11
---
## Concept
Use search as the entry point to algorithmic thinking: the same question — is this item present, and where — admits strategies with very different costs. Develop linear search as the general method that always works, then binary search as a much faster method that buys its speed with an assumption (the data must be sorted) and works by halving the remaining range. Introduce the intuition behind hashing: a hash function maps a key to a location, so a dictionary can go more or less directly to the value instead of scanning, which is why lookup cost barely grows with size. Present efficiency informally but honestly, in terms of how the work scales as data grows rather than formal notation, and name the tradeoffs: sorting has an upfront cost, dictionaries and sets use extra memory, and the fastest approach depends on how many lookups you will perform.

## Practice
Implement linear search over a list, returning an index or a sentinel for absent items, and test it against edge cases: empty input, first element, last element, and duplicates. Implement binary search with explicit low and high bounds, tracing the shrinking interval by hand before coding it, and confirm what happens if the input is unsorted. Time all three approaches — list scan, binary search on a sorted list, dictionary or set lookup — at several input sizes and tabulate the results so the scaling difference is visible rather than asserted. Revisit `in` on a list versus a set with this cost model in mind. In-class activity: students compare lookup methods on structured data and report timings. Homework: write search-related functions and compare their behavior on test inputs.

