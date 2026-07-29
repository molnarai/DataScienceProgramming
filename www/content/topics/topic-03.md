---
date: 2026-09-09
classdates: '2026-09-09'
draft: false
title: 'Loops and Core Data Structures'
theoretical: "Iteration as a way to express repeated work. Lists, tuples, sets, and dictionaries: what each is for and what its structure guarantees. Counting and accumulation patterns."
technical: "`for` and `while` loops; indexing and slicing; membership tests; dictionary-based counting. In-class: compute category counts from a small dataset."
weight: 30
numsession: 3
---
## Theory
Present iteration as the tool for expressing repeated work over a collection, and distinguish a `for` loop (a known set of items) from a `while` loop (an unknown number of repetitions governed by a condition, with the corresponding risk of never terminating). Introduce the four core containers and the reason each exists: lists for ordered, mutable sequences; tuples for fixed records; sets for uniqueness and fast membership; dictionaries for key-to-value lookup. Emphasize the structural consequences — that a set has no order and no duplicates, that a dictionary key must be unique — because these properties are the reason to choose one container over another. Name the recurring loop patterns explicitly: counting, accumulating a total, filtering into a new collection, and finding a maximum. Recognizing a pattern by name is what lets students reuse it later.

## Technical
Write loops over lists, strings, and dictionaries, including `range`, `enumerate`, and iteration over `.items()`. Practice indexing and slicing, and confront off-by-one errors and the difference between mutating a list in place and building a new one. Demonstrate membership tests with `in` and contrast scanning a list against looking up a key in a dictionary. Build the counting idiom carefully — initialize, check for the key, increment — before showing `dict.get` and `collections.Counter` as shorthands for the same logic. In-class activity: students compute category counts from a small dataset and report the most frequent categories. Homework: use loops and dictionaries to summarize structured input data.

