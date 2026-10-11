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
Almost every program looks things up: is this customer already in the list, which product has this id, which records have no match in the other file? On a hundred records any way of answering is instant. On a million, the way you answer decides whether the program finishes in a second or is still running after lunch, and the two programs look almost identical — both say `if x in collection`. So the question is what a lookup costs and how that cost grows with the data, and the steady way to measure it is to count comparisons rather than time them. **Linear search** looks at each item in turn, needs nothing from the data, and costs about n/2 comparisons for a key that is there and all n for one that is not. Once is harmless; inside a loop over another large collection it is quadratic, the usual reason a program that worked on a sample never finishes on the full file.
<!--more-->
Two ways of organising the data change that cost. **Binary search** halves a sorted list each round, so a million items take twenty steps; it needs sorted data, fails silently without it, and the sorting has a price that only repeated lookups repay. **Hashing** does not search at all: a hash function computes which bucket a key must be in, and a lookup takes about one step whatever the size. Python's `dict` and `set` are hash tables, which explains two rules met earlier without their reasons — a key must be immutable, and a dictionary has no order. That last point decides which structure to use: a hash table answers "is exactly this key here?", while sorted data also answers "between", "next", and "starts with". Before optimising anything else, look for a scan inside a loop; changing one list to a set is often the whole fix.

TODO: marquee image

## Listen

TODO: podcast

## Presentation

- [Search and Hashing](../../slides/slide-11-search-hashing/)

## Read

- [Search and Hashing](../../blog/search-hashing/) (lecture notes)

## Hands-on

Notebooks in [11-Search-Hashing](https://github.com/molnarai/DataScienceProgramming/tree/main/11-Search-Hashing)

## Homework

- [Homework 10: Three Ways to Find It](../../assignments/assignment-10/) — due Wednesday, November 18, 2026
