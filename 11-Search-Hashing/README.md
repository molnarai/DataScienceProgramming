# Session 11: Search and Hashing

Nearly every program looks something up, and you have written `in` and
`records[key]` all term without asking what they cost. This session asks,
because the answer decides whether a program finishes in a second or is still
running at lunch.

1. **Count the work, do not time it.** The number of comparisons is exact and
   shows how the work grows with the size of the data.
2. **Linear search.** Look at every item: the work grows with the list.
3. **Binary search.** Halve a sorted list: a million items in twenty steps.
4. **Hashing.** Compute where the key must be and look only there.
5. **Choosing.** Each structure answers some questions quickly and others
   slowly or not at all.

> **Run these on ARC, with the kernel set to Conda Python 3.12.** Notebook 02
> reads two files under `/data/public/yelp/` that exist only there.

Nothing here repeats earlier sessions. Lists, dictionaries and sets as you use
them are Sessions 3 and 4; joins are Sessions 7 and 8. This session is about
what happens inside them.

## Notebooks

Rename a notebook before you edit it, so that the next course release does not
overwrite your work.

### `01_Finding_Things.ipynb` — the ideas

An overview of the five ideas on lists small enough to follow by hand. The
same line is timed five times and gives five answers, which is the case for
counting comparisons. A linear search that returns its own count shows work
growing in step with the list. The number-guessing game becomes binary search,
followed round by round, and a million items take twenty comparisons; on an
unsorted list the same search is silently wrong. A cloakroom with numbered
hooks introduces hashing: a hash function, buckets, collisions and the load
factor, in thirty lines. Python's `set` then beats a list by a factor of
several thousand on the same `in`, and two rules get their reasons: why a
dictionary key must be immutable, and why a hash table cannot answer "which
ones are between".

Four exercises, and a table mapping each idea to a phase of Homework 10.

### `02_Yelp_Tips_Example.ipynb` — one task, three ways

A worked example on real data: 908,915 Yelp tips, each to be matched to one of
150,346 businesses. Scanning the list would take a quarter of an hour;
sorting once and halving takes under a second; a dictionary takes a quarter of
a second. The notebook then asks what each structure is *for*: a set finds
the 44,153 businesses nobody tipped and confirms that no tip is an orphan;
sorted names and dates answer "starts with" and "in 2019" with two short
searches each, which a hash table cannot do; and a dictionary of tallies finds
the café with 2,571 tips.

Five exercises on the same data.

### `03_Search_and_Hashing_Reference.ipynb` — a lookup guide

Meant to be searched, not read through, and to stay open during Homework 10.
Twelve sections of "you want / write this" tables with runnable examples: what
each operation costs in a list, a sorted list and a hash table; searching a
list; a linear search with a counter; binary search line by line, with its
promise and its classic bugs; insertion points, ranges and prefixes with
`bisect`; sorting; hash functions and what can be a key; a hash table by hand;
`dict` and `set`; counting and grouping; the same ideas in pandas; and a table
of symptoms and causes.

## Homework

[Homework 10](../../Assignments/HW10/instructions/homework10_instructions.md)
has you build what notebook 01 shows: a linear search, a binary search, and a
hash table as a list of buckets, each returning the number of comparisons it
made, and then compare them on the business ids of notebook 02. The overlap is
deliberate. In Phases 1 to 6 you write these tools yourself; the built-in
versions in notebook 03 are there so that you recognise what you built.
