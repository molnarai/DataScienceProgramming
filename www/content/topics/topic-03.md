---
date: 2026-09-09
classdates: '2026-09-09'
draft: false
title: 'Loops and Core Data Structures'
concept: "Iteration as a way to express repeated work. Lists, tuples, sets, and dictionaries: what each is for and what its structure guarantees. Counting and accumulation patterns."
practice: "`for` and `while` loops; indexing and slicing; membership tests; dictionary-based counting. In-class: compute category counts from a small dataset."
weight: 30
numsession: 3
---
This session covers fundamental Python data structures, iteration techniques, and practical loop patterns, using a campus coffee cart sales dataset as a practical working example.
<!--more-->

It begins by introducing Python's four built-in containers, contrasting how ordered lists allow duplicates and in-place modifications, tuples store fixed records that cannot be changed, sets keep only distinct values for membership testing with `in` and `not in`, and dictionaries map unique keys to values. The material covers essential methods including indexing, slicing, list comprehensions, tuple unpacking, and using `.get()` to prevent lookup errors.

The session also explores looping mechanisms, examining `for` loops over sequences, ranges, and enumerated items, alongside condition- and sentinel-controlled `while` loops. Finally, it establishes four fundamental loop patterns—counting matches, accumulating running totals, filtering items into new lists, and finding maximum or minimum values—as well as techniques for counting item popularity using dictionaries and `collections.Counter`.

{{<figure src="imgs/loops-containers.png" 
    alt="Figure: Abstract image representing loops and containers" >}}

## Listen 

{{< podcast src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/podcast/python_containers_and_four_loop_patterns.m4a" title="Python Programming Blueprints" >}}

## Read
- [Wes McKinney: Python for Data Analysis: Chapter 2](https://wesmckinney.com/book/python-basics)
- [Wes McKinney: Python for Data Analysis: Chapter 3](https://wesmckinney.com/book/python-builtin)


## Hands-on
Notebooks in [03-Loops-Data-Structures](https://github.com/molnarai/DataScienceProgramming/tree/main/03-Loops-Data-Structures)


## Special CLI Commands

Use the following CLI commands on the Analytics Research Cluster

| Command | What it does |
|---|---|
| `ifi8410-status` | Checks everything and tells you where you stand. Start here. |
| `ifi8410-update` | Brings in new files from your instructor. |
| `ifi8410-test` | Saves your work and runs the automatic tests on it. |
| `ifi8410-submit` | Says "this is the version I want graded". |

Read the document [IFI-8410 Course Tools](../blog/ifi8410-course-tools.md)




## References
- [The Python Language Reference](https://docs.python.org/3.12/reference/index.html)
- [The Python Standard Library](https://docs.python.org/3.12/library/index.html#library-index)
- [Built-in Functions](https://docs.python.org/3.12/library/functions.html)
- [Built-in Types](https://docs.python.org/3.12/library/stdtypes.html)
- [Common string operations](https://docs.python.org/3.12/library/string.html)
- [File and Directory Access](https://docs.python.org/3.12/library/filesys.html)