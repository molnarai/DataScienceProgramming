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


## The problem

The Yelp academic dataset is on the cluster in `/data/public/yelp`. Two of its
files matter here:

| File | Records | Size |
|---|---:|---:|
| `yelp_academic_dataset_business.json` | 150,346 businesses | 119 MB |
| `yelp_academic_dataset_review.json` | 6,990,280 reviews | 5.3 GB |

The question this assignment answers:

> **In 2018 and 2019, which restaurants did Yelp reviewers disagree about the
> most?**

A restaurant where every review gives four stars has no disagreement at all. A
restaurant where half the reviews give one star and half give five is as
divided as a five-star scale allows. The **standard deviation** of a
restaurant's star ratings measures exactly that: 0.0 for perfect agreement, 2.0
for a perfect split. You will compute it for every restaurant with at least 50
reviews in those two years, and rank them.

The analysis is not the hard part. The hard part is that the review file is
5.3 GB of text, and loaded into Python as a list of dictionaries it would need
several times that in memory — far more than your session on the server has.
Session 5 showed you how to read a JSON Lines file one record at a time. This
assignment builds a whole program on that idea: a **pipeline** of stages, each
reading the file the stage before it wrote, none of them ever holding the big
file in memory.

```text
  business.json ──filter──▶ 1_businesses.jsonl ───┐
     119 MB                   52,268 · 6 MB       │
                                                  ├──join──▶ 3_joined.jsonl
  review.json ────filter──▶ 2_reviews.jsonl ──────┘         1,218,962 · 180 MB
     5.3 GB                1,813,646 · 125 MB                     │
                                                                group
                                                                  │
                      5_sorted.jsonl ◀──sort── 4_groups.jsonl ◀──┘
                         6,571 · 1.6 MB           6,571 · 1.6 MB
                               │
                             report
```

Those counts and sizes are what the finished program produces on the real data.

## Learning objectives

Your program will:

1. Read a multi-gigabyte JSON Lines file one record at a time, and write its
   results as it goes.
2. **Filter** records, and keep only the fields the later stages need.
3. **Join** a large file against a small table held in a dictionary.
4. **Group and aggregate**: count, sum, minimum, maximum, mean and standard
   deviation for thousands of groups, without ever storing the values.
5. **Sort** a file by reusing HW03's merge sort on files, and handing pieces
   smaller than 1,000 records to Python's `sorted()`.
6. Connect the stages so that each one reads the file the previous one wrote,
   and run the whole pipeline from the command line.
7. Explain where the program's memory goes, and why it does not grow with the
   size of the input.

Everything is core Python: `json`, `pathlib`, `sys`. No pandas, no numpy.

## Constraints

These are graded, and several are checked by tests you cannot see.

- **Read files one record at a time.** In `select_businesses`,
  `filter_reviews`, `join_reviews`, `group_reviews`, `count_records`,
  `split_file`, `merge_files`, `sort_file` and `format_report`, do not use
  `.read()`, `.readlines()`, `read_text()`, `read_bytes()` or `json.load()`, and
  do not collect a file's records in a list. The tests measure how much memory
  these functions hold.
- **`sorted()` and `.sort()` only in `sort_small_file`**, and only for files of
  fewer than `chunk_size` records. Everywhere else, the order is built by the
  functions you write.
- **Use the functions you wrote in earlier phases.** `select_businesses` calls
  `has_category` and `price_level`; `group_reviews` calls the Phase 4
  accumulator functions; `merge_files` compares with `sort_key`; `sort_file`
  calls `split_file`, `merge_files` and itself.
- **Never modify an input.** No function changes a file it reads, or the lookup
  dictionary it is given. The one exception is `update_stats`, whose whole job
  is to update its accumulator.
- **Nothing prints except `main()`.**
- **Every function keeps its docstring.**
- **Never write pipeline output into the repository.** The stage files for the
  real data take about 300 MB. They go in a folder in your home directory, such
  as `~/hw04_work`, never under `submission/`.

## How to work on this assignment

**Do not write the whole program and then run it on 5 GB.** The assignment is
split into nine phases. Each phase adds one to three functions and has its own
test files. Work in this order:

1. Read the phase description.
2. Implement only the functions in that phase.
3. Run that phase's tests: `./run_tests.sh 2` for Phase 2.
4. Fix your code until every test in that phase passes.
5. Only then move to the next phase.

Every phase is tested on a **sample** of the dataset that ships with the
assignment, in `test/fixtures/yelp_sample/`: twelve businesses and 629 reviews,
in exactly the real files' format. The whole test suite runs in about ten
seconds. You run on the real data **once**, at the end of Phase 9, when every
test passes.

You test in two places, and they do different jobs:

| | Where | When | What it is for |
|---|---|---|---|
| **Locally** | on the cluster, `./run_tests.sh N` | constantly, while you work | Fast feedback on the phase you are writing |
| **Pipeline** | GitLab, on merge into `testing` | once a phase is done | The record of what passed; this is what counts |

The test suite is not hidden. It lives in [`../test/`](../test/) and you are
expected to read it. Editing your copy achieves nothing: the pipeline runs the
course's copy, plus additional tests you do not have. The pipeline cannot see
`/data/public/yelp` either — it tests only on the sample.

## Setup

Start the way you start every session, then collect the assignment:

```bash
ifi8410-status --auto
ifi8410-update
cd Assignments/HW04
mkdir -p submission
cp starter/yelp_pipeline.py submission/yelp_pipeline.py
cp starter/JOURNAL.md submission/JOURNAL.md
```

### The notebook

There is a guided notebook for this assignment:

```text
Assignments/HW04/starter/Instructions_orig.ipynb
```

Rename it to drop the `_orig` before you run anything, then work through it. It
walks the nine phases in the same order as this handout, gives you cells to
experiment in — including a few that peek at the real data without loading it —
and checks each function as you write it. This handout stays the authority on
every rule; the notebook is the guided path through it. Either way, the file you
submit is `submission/yelp_pipeline.py`.

Your directory should then look like this:

```text
Assignments/HW04/
├── instructions/
│   ├── homework04_instructions.md
│   ├── SCHEMA.md                  <- every field of every Yelp file
│   └── JSON_SAMPLES.txt           <- one real record from each file
├── starter/
│   ├── Instructions_orig.ipynb    <- rename it, then work in it
│   ├── yelp_pipeline.py           <- the untouched template; leave it alone
│   └── JOURNAL.md
├── submission/                    <- everything you write goes here
│   ├── yelp_pipeline.py           <- the file you edit
│   └── JOURNAL.md                 <- required, not graded
└── test/                          <- the test suite; read it, do not edit it
    └── fixtures/
        └── yelp_sample/           <- the sample the tests run on
```

**Do not edit anything in `starter/`, `test/`, or `instructions/`.** Only files
under `submission/` are read as your solution, and the file must be named
`yelp_pipeline.py`. A later release replaces the other folders and your edits
there would be lost.

Check that the tests can find your file:

```bash
cd test
./run_tests.sh
```

You should see a long list of failures. That is correct — you have not written
anything yet. If instead you see `Could not find yelp_pipeline.py`, your file is
in the wrong place; re-read the tree above.

Every `./run_tests.sh` command below is run from that `test/` directory.

## The dataset

Both files are **JSON Lines**: one complete JSON object per line, exactly the
format of Session 5, Section 6. [`SCHEMA.md`](SCHEMA.md) lists every field of
every Yelp file, and [`JSON_SAMPLES.txt`](JSON_SAMPLES.txt) shows one real
record from each. The dataset is already on the cluster. **Do not copy or
download it.**

Look before you load. From a terminal, this prints the first review — one line
of a 5.3 GB file — and returns immediately:

```bash
head -n 1 /data/public/yelp/yelp_academic_dataset_review.json
```

### A business

The fields this assignment uses:

```json
{
  "business_id": "Pns2l4eNsfO8kk83dixA6A",
  "name": "Abby Rappoport, LAC, CMQ",
  "city": "Santa Barbara",
  "state": "CA",
  "attributes": {"ByAppointmentOnly": "True"},
  "categories": "Doctors, Traditional Chinese Medicine, Naturopathic/Holistic, Acupuncture, Health & Medical, Nutritionists"
}
```

| Field | Type | Notes |
|---|---|---|
| `business_id` | `str` | 22 characters; unique |
| `name`, `city`, `state` | `str` | not cleaned: `Philadephia` and `St Louis` both occur |
| `attributes` | `dict` or `None` | every value is a **string**; `RestaurantsPriceRange2` is the price level |
| `categories` | `str` or `None` | **one** string of comma-separated names |

### A review

```json
{
  "review_id": "KU_O5udG6zpxOg-VcAEodg",
  "user_id": "mh_-eMZ6K5RLWhZyISBhwA",
  "business_id": "XQfwVwDr-v0ZS3_CbbE5Xw",
  "stars": 3.0,
  "useful": 0,
  "funny": 0,
  "cool": 0,
  "text": "If you decide to eat here, just be aware it is going to take about 2 hours ...",
  "date": "2018-07-07 22:09:11"
}
```

| Field | Type | Notes |
|---|---|---|
| `business_id` | `str` | the business reviewed |
| `stars` | `float` | `1.0` to `5.0`, whole stars only |
| `useful` | `int` | how many readers marked the review useful |
| `date` | `str` | `"YYYY-MM-DD HH:MM:SS"` |
| `text` | `str` | the review itself — most of the file's 5.3 GB, and not needed here |

### The parameters

The top of `yelp_pipeline.py` holds the assignment's settings. Your functions
receive them as arguments; only `run_pipeline` and `main` read them directly.

| Constant | Value | Meaning |
|---|---|---|
| `CATEGORY` | `"Restaurants"` | the businesses selected |
| `FIRST_YEAR`, `LAST_YEAR` | `2018`, `2019` | the review window, inclusive — the last two years before the pandemic, and the two with the most reviews |
| `MIN_REVIEWS` | `50` | fewer reviews than this, and a standard deviation says little |
| `CHUNK_SIZE` | `1000` | a file with fewer records than this is sorted with `sorted()` |
| `TOP_N` | `20` | rows in the report |
| `BUSINESSES_OUT` … `SORTED_OUT` | `"1_businesses.jsonl"` … `"5_sorted.jsonl"` | the stage files |

## Required functions

Keep these names and parameter lists **exactly** as shown. You may add helper
functions, but do not remove, rename, or re-order the required ones — the tests
call them directly.

| Phase | Stage | Function | Purpose |
|---:|---|---|---|
| 1 | filter | `has_category(business, category)` | Is the category one of the business's categories? |
| 1 | filter | `price_level(business)` | The price level, 1–4, or `None` |
| 1 | filter | `select_businesses(business_path, output_path, category)` | Write the small table |
| 2 | filter | `filter_reviews(review_path, output_path, first_year, last_year)` | Write the reviews in the window, three fields each |
| 3 | join | `load_lookup(businesses_path)` | The small table as a dictionary |
| 3 | join | `join_reviews(reviews_path, lookup, output_path)` | Attach each review to its business |
| 4 | aggregate | `new_stats()` | An empty accumulator |
| 4 | aggregate | `update_stats(stats, stars, useful)` | Add one review to an accumulator |
| 4 | aggregate | `finish_stats(stats)` | Count, mean, standard deviation, min, max, total |
| 5 | group | `group_reviews(joined_path, output_path, min_reviews)` | One summary line per business |
| 6 | sort | `sort_key(record)` | The value that decides the order |
| 6 | sort | `sort_small_file(input_path, output_path)` | Sort a small file with `sorted()` |
| 7 | sort | `count_records(path)` | Lines in a file |
| 7 | sort | `split_file(input_path, front_path, back_path)` | One file into two halves |
| 7 | sort | `merge_files(left_path, right_path, output_path)` | Two sorted files into one |
| 8 | sort | `sort_file(input_path, output_path, work_dir, chunk_size)` | Sort a file of any size |
| 9 | report | `format_report(sorted_path, top_n)` | The report, as one string |
| 9 | — | `run_pipeline(data_dir, work_dir, ...)` | Every stage, in order |
| 9 | — | `main()` | The command line |

### Two rules about lines

- **Files you did not write** — the two Yelp files — may contain blank lines.
  Skip a line when `line.strip()` is empty. `select_businesses` and
  `filter_reviews` must do this.
- **Files your pipeline writes** hold exactly one record per line and nothing
  else: `json.dumps(record) + "\n"`. The later stages may rely on that.

Every path argument may be a `str` or a `pathlib.Path`; `open()` accepts both.
Every function that writes a file **replaces** it if it already exists — mode
`"w"`.

---

# The phases

## Phase 1 — Filter the small table

Implement `has_category`, `price_level`, and `select_businesses`.

### `has_category(business, category)`

Return `True` when `category` is **one of the names** in
`business["categories"]`, and `False` otherwise — a real Boolean.

`categories` is one string, not a list:

```python
"Pizza, Restaurants"
"Restaurants, Sushi Bars, Japanese"
"Pop-Up Restaurants, Food"
None
```

`"Restaurants" in "Pop-Up Restaurants, Food"` is `True` — the letters are
there — but a pop-up restaurant is not what the question means. Split the string
on `","`, `strip()` each name, and compare whole names with `==`. `None`, an
empty string, and a business with no `categories` key at all all give `False`;
`business.get("categories")` covers all three.

### `price_level(business)`

Yelp stores the price level as a string inside `attributes`, and records a
missing price in several different ways. This function turns every one of them
into one of five answers:

| `business["attributes"]` | Result |
|---|---|
| `{"RestaurantsPriceRange2": "2", ...}` | `2` — an `int` |
| `{"RestaurantsPriceRange2": "None"}` | `None` — the *text* `"None"` |
| `{"RestaurantsPriceRange2": None}` | `None` |
| `{"WiFi": "u'free'"}` — no price key | `None` |
| `None` — no attributes at all | `None` |
| any value but `"1"`, `"2"`, `"3"`, `"4"` | `None` |

Of the 52,268 restaurants in the real file, 7,203 have the value `None`, 565 have
no attributes, and 16 have the string `"None"`. All three mean the same thing,
and a program should say so in one place.

### `select_businesses(business_path, output_path, category)`

Read the business file **one line at a time**. Skip blank lines. For each
business that `has_category`, write one line holding only these five fields, and
return how many businesses were written:

```json
{"business_id": "rest-divided-pizza-001", "name": "Pizza Palace", "city": "Tampa", "state": "FL", "price": 1}
```

`price` comes from `price_level`. Every other field of the business — address,
hours, the rest of the attributes — is left behind: later stages never need it,
so it is never written.

Reading one file while writing another needs two open files at once. One `with`
statement can open both:

```python
with open(business_path, encoding="utf-8") as source, \
        open(output_path, "w", encoding="utf-8") as target:
    for line in source:
        ...
        target.write(json.dumps(record) + "\n")
```

On the sample, 9 of the 12 businesses are restaurants.
[`../test/fixtures/README.md`](../test/fixtures/README.md) says what each
sample business is there to catch.

```bash
./run_tests.sh 1
```

**Do not continue until every test in Phase 1 passes.**

## Phase 2 — Filter the big table

Implement `filter_reviews(review_path, output_path, first_year, last_year)`.

Read the review file one line at a time, and skip blank lines. Keep a review
when the year of its date is between `first_year` and `last_year`,
**inclusive**. The year is the first four characters of the date:

```python
int("2018-07-07 22:09:11"[:4])      # 2018
```

For every kept review, write one line of **three** fields:

```json
{"business_id": "XQfwVwDr-v0ZS3_CbbE5Xw", "stars": 3.0, "useful": 0}
```

Return the tuple `(reviews_read, reviews_kept)`. Blank lines are not reviews and
are not counted.

### Why three fields

Choosing the fields to keep is called **projection**, and on this file it is
worth more than the filter. A review line averages 760 bytes, almost all of it
`text`. The three fields above take about 70. Dropping the other fields as early
as possible means every later stage reads a file 10 times smaller.

### What "one at a time" means

This works on 5.3 GB:

```python
for line in source:                   # one line in memory
    review = json.loads(line)         # one review in memory
    ...
    target.write(json.dumps(record) + "\n")   # and it is gone
```

Each of these holds the whole file, or all of the kept reviews, and runs out of
memory on the real data:

```python
lines = source.readlines()            # 5.3 GB of strings
text = source.read()                  # the same
kept = []                             # 1.8 million dictionaries...
for line in source:
    ...
    kept.append(record)               # ...written only at the end
```

The Phase 2 tests include one that hands `filter_reviews` a 26 MB file and
measures the most memory it holds at once. Reading one review at a time needs
far less than 1 MB; the test allows 5.

```bash
./run_tests.sh 2
```

**Do not continue until every test in Phase 2 passes.**

## Phase 3 — Join

Implement `load_lookup` and `join_reviews`.

The filtered reviews know a `business_id`. The report needs a name, a city, and
a price. Those are in the other file, and bringing them together is a **join**.

### The small table goes in memory; the big table is streamed

There are 52,268 selected businesses and 1,813,646 filtered reviews. The
businesses fit comfortably in memory — about 6 MB of text. So:

- **`load_lookup(businesses_path)`** reads the selected businesses into a
  dictionary keyed by `business_id`, and returns it. Each value is the record
  exactly as read.

  ```python
  {"rest-divided-pizza-001": {"business_id": "rest-divided-pizza-001", "name": "Pizza Palace", ...},
   ...}
  ```

- **`join_reviews(reviews_path, lookup, output_path)`** reads the reviews one at
  a time, looks each review's business up, and writes the business's fields
  followed by the review's `stars` and `useful`:

  ```json
  {"business_id": "rest-divided-pizza-001", "name": "Pizza Palace", "city": "Tampa", "state": "FL", "price": 1, "stars": 5.0, "useful": 2}
  ```

  A review whose business is not in the lookup — a business that is not a
  restaurant — is dropped. Return `(reviews_read, reviews_joined)`.

### Why a dictionary

`lookup.get(business_id)` finds a business in one step, however many there are.
Searching a *list* of 52,268 businesses for each of 1.8 million reviews would
take up to 95 billion comparisons. The dictionary is what makes the join take
seconds.

### Build a new dictionary for every joined record

Session 5 showed `{**row, "price": ...}`: copy every key of one dictionary into a
new one, then add more. That is exactly the joined record:

```python
record = {**business, "stars": review["stars"], "useful": review["useful"]}
```

Do **not** add the fields to the business itself:

```python
business["stars"] = review["stars"]       # changes the record INSIDE lookup
```

That line corrupts the lookup: the business now carries the stars of whichever
review touched it last. The tests check that `lookup` is unchanged.

```bash
./run_tests.sh 3
```

## Phase 4 — Aggregates, one value at a time

Implement `new_stats`, `update_stats`, and `finish_stats`.

A restaurant can have hundreds of reviews in the window, and there are 38,402
restaurants with at least one. Keeping every restaurant's star ratings in a list
would mean holding all 1.2 million of them. You do not need them. Every number
the report shows can be computed from **six running values** per restaurant,
updated as each review goes past:

```python
def new_stats():
    return {
        "count": 0,             # how many reviews
        "stars_sum": 0.0,       # the sum of the stars
        "stars_squares": 0.0,   # the sum of each star rating squared
        "stars_min": None,      # the lowest rating so far
        "stars_max": None,      # the highest rating so far
        "useful_total": 0,      # the sum of the useful votes
    }
```

A structure like this is an **accumulator**: the Session 3 counting pattern,
with more than one thing being counted.

### `update_stats(stats, stars, useful)`

Add one review to the accumulator, **in place**, and return `None`. This is the
one function in the assignment that is meant to change its argument.

- `count` goes up by 1, `stars_sum` by `stars`, `stars_squares` by
  `stars * stars`, `useful_total` by `useful`.
- `stars_min` and `stars_max` start as `None`, which means "no value yet". The
  first review replaces both; after that, a smaller rating replaces `stars_min`
  and a larger one replaces `stars_max`.

### `finish_stats(stats)`

Turn an accumulator into a **new** dictionary of six fields:

```python
{"review_count": 4, "stars_mean": 3.0, "stars_std": 2.0,
 "stars_min": 1.0, "stars_max": 5.0, "useful_total": 9}
```

The mean is the sum divided by the count. The standard deviation needs no list
either, because the variance is *the mean of the squares minus the square of the
mean*:

```text
mean     = stars_sum / count
variance = stars_squares / count - mean ** 2
std      = variance ** 0.5
```

Check it by hand on four reviews, 1★ 5★ 1★ 5★:

```text
count = 4    stars_sum = 12    stars_squares = 1 + 25 + 1 + 25 = 52
mean = 12 / 4 = 3.0
variance = 52 / 4 - 3.0 ** 2 = 13.0 - 9.0 = 4.0
std = 4.0 ** 0.5 = 2.0
```

The rules:

- This is the **population** standard deviation, dividing by `count` — what
  `statistics.pstdev` computes. (The *sample* standard deviation divides by
  `count - 1`; the course returns to the difference with descriptive
  statistics.)
- Round `stars_mean` and `stars_std` to **3** decimal places with `round(x, 3)`.
  Round only at the end: compute the variance from the unrounded mean.
- An accumulator that has seen no reviews raises `ValueError`. There is no mean
  of nothing, and such a group should never reach this function.
- **A variance just below zero counts as zero.** Floating-point arithmetic is
  not exact. For three reviews that are all equal, the two terms of the variance
  are the same number and should cancel to 0 — but rounding in the last binary
  digit can leave something like `-1.7e-18`. In Python, a negative number
  `** 0.5` is a *complex* number, and `math.sqrt` of one raises `ValueError`.
  Add `if variance < 0: variance = 0.0` before taking the root. The tests include
  a case that needs it.
- `stats` itself is unchanged.

```bash
./run_tests.sh 4
```

## Phase 5 — Group

Implement `group_reviews(joined_path, output_path, min_reviews)`.

Read the joined reviews one at a time, keeping a dictionary with one entry per
business:

```python
groups = {
    "rest-divided-pizza-001": {
        "business": {"business_id": ..., "name": ..., "city": ..., "state": ..., "price": ...},
        "stats": {"count": 52, "stars_sum": 156.0, ...},
    },
    ...
}
```

The first time a `business_id` appears, add its entry, with an accumulator from
`new_stats()`. Every time — including the first — add the review with
`update_stats`.

**The dictionary grows with the number of businesses, not the number of
reviews.** On the real data that is 38,402 entries, holding six numbers and five
fields each, while 1.2 million reviews stream past.

After the last review, write one line per business that has **at least**
`min_reviews` reviews. The line holds the five business fields followed by the
six from `finish_stats`:

```json
{"business_id": "rest-divided-pizza-001", "name": "Pizza Palace", "city": "Tampa", "state": "FL", "price": 1, "review_count": 52, "stars_mean": 3.0, "stars_std": 2.0, "stars_min": 1.0, "stars_max": 5.0, "useful_total": 78}
```

`{**group["business"], **finish_stats(group["stats"])}` builds it in one step.

- Write the groups **in the order each business first appeared** — the order a
  dictionary keeps. Do not sort them; that is stage 4's job.
- `min_reviews` can only be applied after reading everything: while the file is
  still being read, no business knows its final count.
- Return `(groups_found, groups_written)`. On the sample that is `(9, 7)`: Tiny
  Tacos has 49 reviews in the window, and Old Favorite Grill has 30.

```bash
./run_tests.sh 5
```

**Do not continue until every test in Phase 5 passes.** Stages 1 to 3 are now
complete and tested. The rest of the assignment is the sort.

## Phase 6 — Sorting with `sorted()`

Implement `sort_key` and `sort_small_file`.

In HW03 you built merge sort precisely *without* Python's sorting tools. This
assignment uses one of them, `sorted()`, for the small pieces of a large sort.
It has not been covered in class yet, so this phase explains it properly before
you use it.

### What `sorted()` does

`sorted(something)` takes any collection and returns a **new list** of its items
in ascending order. The original is not changed.

```python
scores = [87, 72, 91, 84]
ordered = sorted(scores)

print(ordered)       # [72, 84, 87, 91]
print(scores)        # [87, 72, 91, 84]  -- unchanged
```

Lists also have a `.sort()` method, which reorders the list **in place** and
returns `None`. That makes this a classic bug:

```python
ordered = scores.sort()
print(ordered)       # None
```

This assignment uses only `sorted()`, which never changes its input — the same
rule every function in HW03 followed.

`sorted()` compares items with `<`. Numbers compare by value and strings
character by character — which is why, in Session 5, `sorted(["10", "8", "9"])`
gave `["10", "8", "9"]`: `"1"` comes before `"8"`.

### Sorting dictionaries needs a key

Dictionaries cannot be compared with `<`:

```python
records = [{"name": "Tacos", "stars_std": 0.5}, {"name": "Sushi", "stars_std": 2.0}]
sorted(records)
# TypeError: '<' not supported between instances of 'dict' and 'dict'
```

`sorted()` has to be told *what about* each dictionary to compare. That is the
`key` argument: a **function** that takes one item and returns the value to
compare it by.

```python
def by_std(record):
    return record["stars_std"]

sorted(records, key=by_std)
# [{'name': 'Tacos', 'stars_std': 0.5}, {'name': 'Sushi', 'stars_std': 2.0}]
```

What happens inside:

1. `sorted()` calls `by_std` **once for each item**, and remembers the results:
   `0.5` for Tacos, `2.0` for Sushi.
2. It orders the items by comparing those results with `<`.
3. It returns the **original items** — the whole dictionaries — in that order.
   The key only decides the order; it is not what comes back.

Notice `key=by_std`, **without parentheses**. That passes the function itself,
for `sorted()` to call. `key=by_std()` would call it immediately, with no
argument, and fail. Session 4 passed functions as values in exactly this way,
and used `key=lambda row: row["price"]`; a `lambda` is only a function without a
name, and here the function deserves a name and a docstring.

### Several columns: return a tuple

Tuples compare **item by item**, left to right, and the first difference decides:

```python
(2.0, 50) < (2.0, 52)      # True:  first items equal, so 50 < 52 decides
(1.5, 99) < (2.0, 1)       # True:  1.5 < 2.0 decides; the rest is never looked at
```

So a key function that returns a tuple sorts by the first column, breaks ties
with the second, and breaks remaining ties with the third.

### Largest first: negate

`sorted()` always puts the smallest key first. To put the **largest** standard
deviation first, make the key its negative: a standard deviation of 2.0 becomes
−2.0, which is smaller than −0.5, so it comes first.

`sorted()` also accepts `reverse=True`, but that reverses the *whole* key,
including the tie-breaker. Here the standard deviation and the review count must
be descending while `business_id` stays in alphabetical order, so negate the two
numbers and leave the string alone.

### Ties keep their order

When two items have **equal** keys, `sorted()` keeps them in the order they had
in the input. This is called **stability** — the property your HW03 merge sort
had because `comes_before_or_equal` answered `True` on a tie. Python's `sorted()`
is, in fact, a merge sort too: an algorithm called Timsort, which finds runs that
are already in order, sorts short runs with a simpler method, and merges them.

### Why only for small files

`sorted()` needs every item in a list in memory at once. For a thousand records
that is nothing. For a file of any size it is the problem this whole assignment
avoids. So the rule is: **`sorted()` only ever sees fewer than `chunk_size`
records**, and Phases 7 and 8 make sure nothing bigger reaches it.

### `sort_key(record)`

Return the tuple that puts a group record where it belongs in the ranking:

```python
(-record["stars_std"], -record["review_count"], record["business_id"])
```

1. The **highest** standard deviation first — the most divisive restaurant.
2. On an equal standard deviation, the **most** reviews first: a split across
   150 reviews says more than a split across 50.
3. On equal reviews too, `business_id` in **alphabetical** order.

No two businesses share a `business_id`, so no two records ever have equal keys.
That makes the ranking the same whichever way it is computed — which is what
lets the tests check it exactly. And ties on the first two are common: among the
6,571 real restaurants there are only 1,163 distinct standard deviations.

### `sort_small_file(input_path, output_path)`

Read every record of `input_path` into a list, order it with
`sorted(records, key=sort_key)`, write the ordered records to `output_path`, one
per line, and return how many there were. This is the one function that may read
a whole file — and it is only ever given small ones.

```bash
./run_tests.sh 6
```

## Phase 7 — Divide a file, and combine two sorted files

Implement `count_records`, `split_file`, and `merge_files`.

These are HW03's `split_in_half` and `combine_ordered_groups`, working on files
instead of lists.

### `count_records(path)`

Return the number of lines in a file the pipeline wrote, reading it one line at
a time.

### `split_file(input_path, front_path, back_path)`

Write the first `total // 2` records to `front_path` and the rest to
`back_path`, and return `(front_count, back_count)`. With an odd count the extra
record goes to the **back** — the HW03 convention:

```text
5 records  ->  front: 2    back: 3
1 record   ->  front: 0    back: 1       (front is an empty file)
0 records  ->  front: 0    back: 0       (both files exist, both empty)
```

Count first with `count_records`, then read the input again, sending each line
to front or back by its position; `enumerate` gives you the position. The lines
can be copied as they are, without parsing them. Reading the file twice is
deliberate: it costs a second pass over the disk, and saves holding the file in
memory.

### `merge_files(left_path, right_path, output_path)`

Both inputs are already in `sort_key` order. Write every record from both, in
`sort_key` order, and return how many were written. This is HW03's Phase 2, and
the picture is the same — except that each "group" is now a file, and the marker
is simply *the record you have read from it and not yet written*:

```text
left file:    [2.000  1.562  0.816 ...]
               ^ current left record
right file:   [2.000  0.816  0.500 ...]
               ^ current right record

Compare the two current records with sort_key.
Write the one that comes first.
Read the next record ONLY from the file it came from.
When one file runs out, write every record left in the other.
```

To read "the next record" from an open file, use `next(file, None)`, from
Session 5: it returns the next line, or `None` when the file has no more.

```python
left_line = next(left, None)
left_record = json.loads(left_line) if left_line is not None else None
```

- On equal keys, write the **left** record first:
  `sort_key(left_record) <= sort_key(right_record)`. Your HW03 tie rule, again.
- Hold **one** record from each file, never more. Loading both files into lists
  and merging those would pass the ordering tests — and fail the memory test,
  which merges two files of 20,000 records each.
- The three HW03 mistakes are all still possible, and all still tested: dropping
  the leftovers, advancing both files at once, and changing an input.

```bash
./run_tests.sh 7
```

**Do not continue until every test in Phase 7 passes.**

## Phase 8 — Sort a file of any size

Implement `sort_file(input_path, output_path, work_dir, chunk_size=CHUNK_SIZE)`.

This is HW03's `order_applications`, for files:

```text
                  input file
                      │
          fewer than chunk_size records?
                      │
              ┌───────┴──────────┐
             yes                 no
              │                  │
     sort_small_file     split_file into front and back     ← Phase 7
                                 │
                  ┌──────────────┴──────────────┐
                  │                             │
          sort_file(front)              sort_file(back)     ← this function, again
                  │                             │
                  └──────────────┬──────────────┘
                                 │
                  merge_files into output_path              ← Phase 7
```

There is one difference from HW03. HW03 divided until a group had fewer than
two items. This function stops dividing much earlier, at **fewer than
`chunk_size` records**, because a list of a few hundred records is tiny, and
`sorted()` orders it far faster than splitting and merging files could. On the
real data the division stops after three levels:

```text
6,571
├── 3,285
│   ├── 1,642 ──▶ 821 + 821    each sorted with sorted()
│   └── 1,643 ──▶ 821 + 822
└── 3,286
    ├── 1,643 ──▶ 821 + 822
    └── 1,643 ──▶ 821 + 822
```

Eight calls to `sort_small_file` of about 820 records each, and seven merges.
No more than 822 records are ever in memory at once.

The rules:

- **`chunk_size` below 2 raises `ValueError`.** With `chunk_size=1`, a file of
  one record is not "fewer than 1", so it would be split — into an empty front
  and a one-record back, which would be split again, for ever.
- **Temporary files go in `work_dir`** and are **deleted** once used, with
  `Path.unlink()`. When `sort_file` returns, `work_dir` holds nothing it created.
  Name them after `output_path`, so that no two levels of the recursion can
  pick the same name. This scheme works:

  ```python
  front_path   = work_dir / (output_path.stem + ".front.jsonl")    # unsorted halves
  back_path    = work_dir / (output_path.stem + ".back.jsonl")
  front_sorted = work_dir / (output_path.stem + "_0.jsonl")        # sorted halves
  back_sorted  = work_dir / (output_path.stem + "_1.jsonl")
  ```

  `Path.stem` is the file name without its extension (Session 5, Section 2), so
  the halves of `5_sorted.jsonl` sort into `5_sorted_0.jsonl` and
  `5_sorted_1.jsonl`, and *their* halves into `5_sorted_0_0.jsonl` and so on.
  Turn the three arguments into `Path` objects first: `Path(input_path)`.
- The input file is unchanged, and `output_path` may be in any folder.
- Return the number of records written.
- Records with equal keys keep their input order. You write nothing for this:
  it follows from the front staying in front in `split_file`, the left winning
  ties in `merge_files`, and `sorted()` being stable.

A test spies on `sort_small_file` and fails if it is ever given `chunk_size`
records or more. Another sorts 10,000 records with `chunk_size=100` and measures
the memory.

If you get `RecursionError`, the stopping condition is never reached: check that
the comparison is `< chunk_size` on the count, and that the halves really are
smaller.

```bash
./run_tests.sh 8
```

## Phase 9 — The report, and the whole pipeline

Implement `format_report`, `run_pipeline`, and `main`.

### `format_report(sorted_path, top_n)`

Return the report as **one string**, with no trailing newline. The exact report
for the sample, from `format_report("../test/fixtures/sample_sorted.jsonl", 20)`:

```text
MOST DIVISIVE RESTAURANTS
=========================

Restaurants ranked: 7
Showing: top 7

Rank  Std    Mean   Min  Max  Reviews  Useful  Price  Restaurant
   1  2.000  3.000  1.0  5.0       52      78  $      Pizza Palace (Tampa, FL)
   2  2.000  3.000  1.0  5.0       50      73  $$     Sushi Split (Reno, NV)
   3  1.562  3.600  1.0  5.0       50      77  $$$$   Prime Cut Steakhouse (Nashville, TN)
   4  0.816  3.000  2.0  4.0       60      90  $$     Twin Diner (Philadelphia, PA)
   5  0.816  3.000  2.0  4.0       60      90  $$     Twin Diner (Philadelphia, PA)
   6  0.500  4.500  4.0  5.0       60      90  -      Café Zoë (New Orleans, LA)
   7  0.000  4.000  4.0  4.0       55      82  -      Noodle Bar (Boise, ID)
```

The rules, precisely:

- The title, a line of `=` exactly as long as the title, and a blank line.
- `Restaurants ranked: N`, where N is every record in the file — count them
  with `count_records`.
- `Showing: top K`, where K is `top_n`, or N if the file has fewer. Then a blank
  line, then the header line exactly as shown.
- One row per record, for the first K records only:

  ```python
  f"{rank:>4}  {std:.3f}  {mean:.3f}  {low:.1f}  {high:.1f}  {count:>7}  {useful:>6}  {price:<5}  {name} ({city}, {state})"
  ```

  where `rank` counts from 1 and `price` is `"$" * price`, or `"-"` when the
  price is `None`. Two spaces separate every column.
- **Read only the first `top_n` records.** The file is already sorted, so
  nothing after them can appear in the report. Loop with
  `enumerate(file, start=1)` and `break` once the rank passes `top_n`.
- An **empty** file gives the title, its underline, a blank line,
  `Restaurants ranked: 0`, a blank line, and `No restaurants to rank.` — no
  `Showing` line, no header.
- `top_n` below 1 raises `ValueError`.

Build the report as a **list of lines** and `"\n".join(lines)` at the end. If a
test fails here, read the difference pytest prints character by character:
almost every failure in this phase is one space.

### `run_pipeline(data_dir, work_dir, first_year=FIRST_YEAR, last_year=LAST_YEAR, min_reviews=MIN_REVIEWS, chunk_size=CHUNK_SIZE)`

Run every stage in order and return a dictionary of seven counts:

```python
{"businesses_selected": 9, "reviews_read": 629, "reviews_kept": 589,
 "reviews_joined": 466, "groups_found": 9, "groups_written": 7, "records_sorted": 7}
```

1. Build the two input paths, `data_dir / BUSINESS_FILE` and
   `data_dir / REVIEW_FILE`. If either does not exist, raise
   `FileNotFoundError` — **before** creating `work_dir` or writing anything.
   Session 5's rule: a bad input produces no output, not half of one.
2. Create `work_dir` with `mkdir(parents=True, exist_ok=True)`.
3. **Filter**: `select_businesses` into `work_dir / BUSINESSES_OUT` with
   `CATEGORY`, then `filter_reviews` into `work_dir / REVIEWS_OUT`.
4. **Join**: `load_lookup` from the businesses file, then `join_reviews` into
   `work_dir / JOINED_OUT`.
5. **Group**: `group_reviews` into `work_dir / GROUPS_OUT`.
6. **Sort**: create the folder `work_dir / SORT_TEMP_DIR`, `sort_file` the groups
   into `work_dir / SORTED_OUT` using it, then remove the now-empty folder with
   `rmdir()`.

Afterwards `work_dir` holds exactly the five stage files. Each one is the input
to the next, which is also what makes the pipeline easy to debug: when a number
looks wrong, open the stage files in order and find the first one that is wrong.

The sample's counts are in the dictionary above;
[`../test/fixtures/README.md`](../test/fixtures/README.md) explains every one.

### `main()`

The command line:

```bash
python3 yelp_pipeline.py DATA_DIR WORK_DIR
```

- With anything other than exactly two arguments, print
  `Usage: python3 yelp_pipeline.py DATA_DIR WORK_DIR` to `sys.stderr` and return
  `1`.
- Call `run_pipeline(DATA_DIR, WORK_DIR)`. If it raises `FileNotFoundError`,
  print the error to `sys.stderr` and return `1`. (`Path(...).expanduser()`
  turns a `~` that reached the program unexpanded into your home directory.)
- Print the seven counts, a blank line, and `format_report(... SORTED_OUT, TOP_N)`.
  Then return `0`. The layout of the count lines is up to you; the tests only
  check that every count appears above the report. This layout is a good one:

  ```text
  Pipeline: ../test/fixtures/yelp_sample -> /home/you/hw04_work/sample
    filter  businesses selected           9  -> 1_businesses.jsonl
    filter  reviews read                629
    filter  reviews kept                589  -> 2_reviews.jsonl
    join    reviews joined              466  -> 3_joined.jsonl
    group   groups found                  9
    group   groups written                7  -> 4_groups.jsonl
    sort    records sorted                7  -> 5_sorted.jsonl
  ```

  `f"{count:>10,}"` right-aligns a number in 10 characters with thousands
  separators.

The last line of the starter file is `sys.exit(main())`, which hands `main`'s
return value to the terminal as the program's exit status.

```bash
./run_tests.sh 9
./run_tests.sh          # everything, one last time
```

### Run it on the sample, then on the real data

From `submission/`, on the sample first:

```bash
cd ../submission
python3 yelp_pipeline.py ../test/fixtures/yelp_sample ~/hw04_work/sample
```

Then, when that prints the report above, on the real dataset:

```bash
python3 yelp_pipeline.py /data/public/yelp ~/hw04_work
```

This reads all 5.3 GB. On the course cluster it takes about a minute when the
machine is quiet, and longer when the class is running it at once. The counts
should be exactly these:

```text
  filter  businesses selected      52,268  -> 1_businesses.jsonl
  filter  reviews read          6,990,280
  filter  reviews kept          1,813,646  -> 2_reviews.jsonl
  join    reviews joined        1,218,962  -> 3_joined.jsonl
  group   groups found             38,402
  group   groups written            6,571  -> 4_groups.jsonl
  sort    records sorted            6,571  -> 5_sorted.jsonl
```

and the report should begin:

```text
Restaurants ranked: 6571
Showing: top 20

Rank  Std    Mean   Min  Max  Reviews  Useful  Price  Restaurant
   1  1.856  2.906  1.0  5.0       53      82  $$     Joe Gambino's Bakery (Metairie, LA)
   2  1.851  2.839  1.0  5.0       62      33  $      Mangia Bene Pizzeria (Tampa, FL)
   3  1.811  3.079  1.0  5.0       63     217  -      Bacio (erdenheim, PA)
```

Look at the stage files with `ls -lh ~/hw04_work`: five files, from 120 MB down
to 1.5 MB. Keep them until your journal is written, then delete the folder —
`rm -r ~/hw04_work` — since together they take about 300 MB of your space.

---

## The journal

`submission/JOURNAL.md` is **required** and **not graded**. Nothing you write in
it can lower your mark; the automatic check only confirms that you wrote roughly
forty words of your own. Be honest about dead ends, about help from peers or the
instructor, and about AI tools — which one, what you asked, and whether you used,
adapted, or rejected the answer. Recording help never costs you marks.

See [`../../../Shared/ASSIGNMENT-JOURNAL.md`](../../../Shared/ASSIGNMENT-JOURNAL.md).

## In your journal, answer these

Answer them after your program has run on the real data. A few sentences each.

1. **Where did the memory go?** At its peak, your program holds three things
   that are bigger than one record: the lookup, the groups, and one small sort.
   Roughly how many entries does each hold on the real data? Which one would
   become a problem if the question were about Yelp's 1,987,897 *users* instead
   of its restaurants — and why would the review file's size still not be the
   problem?
2. **What does the ranking say?** Look at the top of your report, then at the
   bottom of the sorted file: `tail -n 5 ~/hw04_work/5_sorted.jsonl`. What mean
   ratings do the most and the least divisive restaurants have? Why can a
   restaurant averaging 4.9 stars never have a standard deviation of 1.8?
3. **What does `chunk_size` cost?** In a notebook cell, time `sort_file` on your
   real `4_groups.jsonl` with `chunk_size` set to 2, to 1000, and to 10000. What
   changes, and what is the trade-off? (The notebook has a cell for this.)

---

## Only after you have finished

<details>
<summary><b>What you have built</b> — open this once your program has run on the real data.</summary>

Each stage of your pipeline has a name, and so does the pipeline as a whole.

- **Stage 4 is an external merge sort** — "external" because the data lives
  outside memory, on disk. It is how every database sorts a table larger than
  its memory, and how the Unix `sort` command sorts files of any size. Real
  implementations usually split the input into memory-sized chunks in one pass,
  sort each chunk in memory, and merge many sorted files at once rather than two
  — but the idea is exactly yours.
- **Stage 2's join is a hash join**: the small table goes into a hash table —
  a Python dictionary is one — and the big table is streamed past it. **Stage
  3's grouping is hash aggregation**, and your accumulator is what databases call
  an *aggregate function*: state that can be updated one value at a time.
- If you have used SQL, you have written this whole program as one query:

  ```sql
  SELECT   b.business_id, b.name, b.city, b.state, b.price,
           COUNT(*), AVG(r.stars), STDDEV_POP(r.stars), MIN(r.stars), MAX(r.stars),
           SUM(r.useful)
  FROM     review r JOIN business b ON r.business_id = b.business_id
  WHERE    b.categories LIKE '%Restaurants%' AND YEAR(r.date) BETWEEN 2018 AND 2019
  GROUP BY b.business_id
  HAVING   COUNT(*) >= 50
  ORDER BY STDDEV_POP(r.stars) DESC, COUNT(*) DESC, b.business_id;
  ```

  `WHERE` is your filter, `JOIN` your join, `GROUP BY` and `HAVING` your
  grouping, and `ORDER BY` your sort. A database runs that query with the same
  four stages you wrote. (Its `LIKE '%Restaurants%'` would even make the
  pop-up-restaurant mistake that Phase 1 avoids.)
- Streaming records through stages that each keep only a small amount of state
  is also the idea behind MapReduce and Spark, which run the same stages across
  many machines at once.

</details>

## Submitting

```bash
ifi8410-test -m "HW04: phase 3 complete"
ifi8410-submit
```

`ifi8410-test` saves your work, sends it to GitLab and merges it into
`testing`, which is what starts the pipeline. The `hw04` job runs your
submission against the course's copy of the tests plus additional hidden ones.
Until the last phase is done most of the pipeline will be red — that is
expected. Look for the phase you just finished and ignore the rest.

`ifi8410-test` runs the tests; `ifi8410-submit` is what hands in your work. Run
both.

Only `submission/` is submitted. Your stage files in `~/hw04_work` are not part
of the repository, and must not be: never copy them into `submission/`.
