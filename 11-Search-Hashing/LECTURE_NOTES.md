# Lecture Notes — Session 11: Search and Hashing

## 1. The problem

Almost every program looks things up. Is this customer already in the list?
Which product has this id? Have I seen this order before? Which of these
records have no match in the other file?

On a hundred records, any way of answering is instant. On a million, the way
you answer decides whether the program finishes in a second or is still
running when you come back from lunch, and **the two programs look almost
identical.** Both say `if x in collection`. One of them looks at up to a
million items every time; the other looks at one.

So the problem of this session is not "how do I find something". It is:

- **What does a lookup cost**, and how does that cost grow as the data grows?
- **How should the data be organised** so that the lookups I need are cheap?
- **Which organisation fits which question?** Finding one exact key, finding
  everything between two values, and finding what is missing are different
  questions, and the best structure for one is useless for another.

The underlying skill is reasoning about cost *before* running the program,
which matters more the larger the data gets, and matters to everyone who
writes a loop over a table.

## 2. Core concepts, and how Python realizes them

### The tools

Nothing here needs installing: it is all in Python itself.

| Tool | Purpose | What it gives you |
|---|---|---|
| **`list`** | an ordered sequence | `x in items`, `items.index(x)`, `items.count(x)`: all of them scan |
| **`sorted`, `list.sort`** | ordering | a sorted copy or an in-place sort, by any key |
| **`bisect`** (standard library) | searching sorted lists | `bisect_left`, `bisect_right`: where a value is, or would go, in about log₂(n) steps |
| **`dict`** | lookup by key | a value stored under a key, found in about one step |
| **`set`** | membership | "is it there?" in about one step; unions, intersections, differences |
| **`collections.Counter`, `defaultdict`** | tallies and groups | counting and grouping, built on `dict` |

pandas uses the same ideas internally: `merge`, `isin`, `groupby`,
`value_counts` and `drop_duplicates` are built on hash tables, and
`searchsorted` is a binary search.

### Concept 1 — Count the work, do not time it

Time the same line five times and you get five slightly different answers; on
a shared machine, very different ones. A time depends on the hardware and on
what else is running.

A steadier measure is to **count the steps**, here the comparisons between an
item and the target. A count is the same on every machine, and it answers the
question a time cannot: *what happens when the data is ten times larger?*

```python
def linear_search(items, target):
    comparisons = 0
    for index in range(len(items)):
        comparisons += 1
        if items[index] == target:
            return (index, comparisons)
    return (-1, comparisons)
```

### Concept 2 — Linear search

Look at each item in turn until one matches. It needs nothing from the data:
any order, any contents.

| Case | Comparisons, for n items |
|---|---|
| the target is first | 1 |
| the target is there, on average | about n / 2 |
| **the target is not there** | **n, every time** |

Ten times the list, ten times the work: the cost is **linear**. The last row
is the one that hurts, because "is this new?" and "which are missing?" are
questions about things that are not there.

`in`, `.index()` and `.count()` on a list are linear searches. The pattern to
watch for is a linear search **inside a loop**:

```python
for order in orders:                        # a million orders
    if order["customer"] in customer_list:  # a scan of 100,000, every time
        ...
```

That is up to a hundred billion comparisons. Work that grows with the product
of two sizes is called **quadratic**, and it is the usual reason a program
that worked on a sample never finishes on the full file.

### Concept 3 — Binary search

Guess a number from 1 to 100 with "higher" or "lower" as the only feedback.
Nobody starts at 1. You say 50, then 75 or 25: every answer halves what is
left. That works because the numbers are in order, and a **sorted** list
allows the same thing.

```python
def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            low = middle + 1          # the target can only be to the right
        else:
            high = middle - 1         # ... or only to the left
    return -1
```

`low` and `high` fence in the part where the target can still be. Each round
looks at the middle and moves one fence past it. The loop keeps one promise:
*if the target is in the list, it is between `low` and `high`.*

A million items are down to one after twenty halvings, since 2²⁰ is about a
million. The number of halvings is the **logarithm to base 2** of the size,
and work that grows this way is **logarithmic**.

| Items | Linear, on average | Binary |
|---:|---:|---:|
| 1,000 | 500 | 10 |
| 1,000,000 | 500,000 | 20 |
| 1,000,000,000 | 500,000,000 | 30 |

Two things to know.

**It needs sorted data, and fails silently without it.** On an unsorted list
a binary search throws away the half that holds the target and reports "not
there", with no error.

**Sorting has a price**, about n × log₂(n) comparisons, paid once. Whether it
is worth paying depends on how many lookups follow. For one lookup, sorting
is a waste; for a few dozen it has already paid for itself.

In practice you use the library:

```python
import bisect

position = bisect.bisect_left(sorted_items, target)       # where it is, or would go
found = position < len(sorted_items) and sorted_items[position] == target
```

`bisect_left` returns the **insertion point**: the first position whose item
is not below the target. That is more useful than "found or not", because two
insertion points fence in a range without looking inside it:

```python
count = bisect.bisect_left(dates, "2020-01-01") - bisect.bisect_left(dates, "2019-01-01")
```

### Concept 4 — Hashing

Binary search rules things out quickly. Hashing is more radical: **do not
search at all; compute where the key must be.**

A cloakroom with numbered hooks: take the ticket number, and its last two
digits are the hook. To fetch the coat, compute the hook and reach for it.

A **hash function** turns a key into a number, the same one every time:

```python
def hash_key(key):
    value = 0
    for character in key:
        value = (value * 31 + ord(character)) % 1_000_000_007
    return value
```

That number, folded onto the size of the table (`hash_key(key) % buckets`),
says which **bucket** the key belongs in. Two different keys will sometimes
land in the same bucket, a **collision**, so each bucket holds a short list.
A lookup computes the bucket and searches only that short list.

The method is fast as long as the buckets stay short, which depends on the
**load factor**: keys divided by buckets. A real hash table watches it and,
when it passes a limit, doubles its buckets and re-places every key.

The result: a lookup takes about **one step, whatever the size**. Work that
does not grow is called **constant**.

**Python's `dict` and `set` are hash tables.** That is the difference between
these two lines, which look the same:

```python
999_999 in a_list_of_a_million      # scans
999_999 in a_set_of_a_million       # one step: thousands of times faster
```

The fix for the slow loop above is one line before it:
`customers = set(customer_list)`.

Two rules you have met without their reasons follow from how hashing works.

- **A key must not change.** Its bucket is computed from its contents; change
  the contents and it sits in the wrong bucket, never to be found. So only
  immutable values (numbers, strings, tuples) can be dictionary keys, and a
  list cannot.
- **A hash table has no order.** The hash scatters keys on purpose. A
  dictionary can tell you whether exactly this key is present, and nothing
  about which keys come next, lie between two values, or start with the same
  letters.

### Concept 5 — Choosing

| Operation | Unsorted list | Sorted list | `dict` / `set` |
|---|---|---|---|
| is this key here? | n | log n | 1 |
| add an item | 1 | n | 1 |
| everything between a and b | n | log n | n |
| the smallest; the next larger | n | 1; log n | n |
| needs | nothing | sorting; comparable items | immutable keys; more memory |

1. **Many lookups by exact key:** a `dict` or a `set`. This is the usual case
   and the usual fix.
2. **Questions about order or ranges:** sort once, then `bisect`.
3. **A handful of items, or a single lookup:** a list and `in` are fine.

Counting and grouping are lookups too: a tally per key means finding that
key's running total for every record, so tallies live in a dictionary. That
is why the loop-and-dictionary pattern is fast, and what `Counter`,
`groupby` and `value_counts` do underneath.

## 3. Business use cases

**Matching two files.** A review site has 900,000 short customer tips, each
carrying the id of a business, and a separate file of 150,000 businesses. To
say anything about a tip, its business has to be found. Scanning the list of
businesses for each tip takes about a quarter of an hour. Sorting the ids
once and using binary search takes under a second. Building a dictionary from
id to business takes a quarter of a second. The step from the first to the
second is the difference between unusable and instant; the step from the
second to the third hardly matters. This is the join that database systems
and pandas perform, and it is why they are fast.

**Finding what is missing.** Which businesses never received a tip? Which
tips refer to a business that is not in the file? Both are questions about
absence, the worst case for a scan. With a set they are one pass:
`[b for b in businesses if b["id"] not in tipped_ids]`. The second question,
orphan records, is a routine data-quality check before trusting any join, and
with a set it is cheap enough to run every time.

**Counting distinct customers.** How many different users wrote those tips?
`len(set(user_ids))`. A set keeps each value once, which is exactly the
question.

**Search by prefix and by date range.** How many business names start with
"Star"? How many tips were written in 2019? These are order questions. With
the names or the dates sorted, each is two binary searches and a subtraction,
without looking at the hundreds or thousands of items in between. A
dictionary cannot answer either: it can only be asked for one exact key at a
time. This is why databases keep sorted indexes as well as hash indexes.

**The busiest businesses.** Which business has the most tips? A tally per
business id in a dictionary, one pass over the tips, then a sort of the
tallies. The same pattern counts page views per user, sales per product,
errors per server.

**A slow report, diagnosed.** A monthly report that used to take seconds now
takes an hour, because the customer file grew from five thousand to five
hundred thousand rows. Somewhere inside a loop over orders there is an `in`
against a list. Changing the list to a set, one line, restores the seconds.
Recognising that pattern is the most practically useful thing in this
session.

## Key points

- Ask how the work grows, not how long it took today.
- A linear search is harmless once and ruinous inside a loop.
- Binary search needs sorted data and is silently wrong without it.
- A hash table finds an exact key in about one step; `dict` and `set` are
  hash tables.
- Sorted data answers "between", "next" and "starts with". A hash table does
  not.
- Before optimising anything else, look for a scan inside a loop.
