# Lecture Notes — Session 8: Python for Data Analysis

## 1. The problem

A company's data arrives as files: exports from a sales system, records typed
in by staff, downloads from a public agency. Someone asks a question of it.
*Which product earns the most? Do expensive restaurants get better ratings?
How much did each region sell?*

With the right library, each of those questions is one line of code, and that
line **always returns a number**. This is the problem. The line does not know
whether the file had blank cells, whether a price was stored as the word
`"None"`, whether a date of 1 January 1900 was a real date or a placeholder,
or whether half of one group's records were missing. It computes anyway. A
wrong answer looks exactly like a right one: same format, same number of
decimals, no error message.

So data analysis is less about the computing line than about what happens
before it:

- **What is in this table?** What does one row stand for, what types are the
  columns, what is missing?
- **Is it fit to compute on?** Which values are wrong, disguised, or
  impossible?
- **What does a blank mean?** Zero, unknown, or not applicable?
- **What does the result leave out?** How many rows did it use, and which did
  it drop?

The question space this session covers is the everyday one: *summarise a
table, per group, after making sure the table can be trusted.* It is the
largest single share of practical data work, and it comes before any
statistics, chart or model.

## 2. Core concepts, and how Python realizes them

### The packages

| Package | Purpose | What it gives you |
|---|---|---|
| **pandas** | tables | the `DataFrame` (a table with named columns) and the `Series` (one column); reading and writing CSV, JSON and Excel; selecting, joining, grouping, reshaping; dates and text |
| **NumPy** | arrays of numbers | fast arithmetic on whole arrays; the engine underneath pandas; functions such as `np.where` and `np.select` for choosing values by a condition |

pandas is imported as `pd` and NumPy as `np`, by a convention so universal
that code without it looks wrong.

### Concept 1 — The table is the central structure

A table has **rows that are observations** and **columns that are
variables**. One row of a deliveries table is one delivery; its columns are
the date, the customer, the product, the number of boxes, the amount.

The first question to ask of any table is its **grain**: *what does one row
stand for?* One order, or one line of an order? One customer, or one visit?
Every count and every average depends on the answer.

In plain Python a table is a list of dictionaries, and every question is a
loop with a dictionary of running totals. In pandas the same data is a
`DataFrame`, and the loop disappears:

```python
import pandas as pd

deliveries = pd.DataFrame(records)              # from a list of dictionaries
deliveries = pd.read_csv("deliveries.csv")      # or from a file

deliveries.groupby("customer")["amount"].sum()  # total per customer
```

What the table lets you stop thinking about is the bookkeeping: creating the
totals dictionary, checking whether a key is already there, keeping the loop
variable straight.

### Concept 2 — Vectorized thinking

**Say what happens to a whole column, not what happens to each row.**

```python
deliveries["amount"] = deliveries["boxes"] * deliveries["price_per_box"]
deliveries["large"] = deliveries["boxes"] >= 4
```

There is no loop in sight. The multiplication applies to every row at once,
inside compiled code, and on a million rows it is hundreds of times faster
than a Python loop. Speed is the smaller benefit. The larger one is that the
code reads like the sentence it implements: *amount is boxes times price*.

Choosing a value by a condition is also a column operation:

```python
import numpy as np

deliveries["discounted"] = np.where(deliveries["boxes"] >= 4,
                                    deliveries["amount"] * 0.9,
                                    deliveries["amount"])
```

`Series.where(condition)` keeps values where the condition holds and blanks
the rest; `Series.mask(condition)` does the reverse. They are the tools for
"make this value missing when it cannot be true".

The habit to build: when you catch yourself writing `for` over the rows of a
table, stop and ask what the column-level sentence is.

### Concept 3 — Split, apply, combine

Every question with the word **per** in it has the same three steps:

1. **Split** the rows into groups (per customer, per month, per store).
2. **Apply** a calculation to each group.
3. **Combine** the results.

pandas does all three with `groupby`. The calculation comes in three kinds,
and choosing the right one is most of the skill:

| Kind | Result | Example |
|---|---|---|
| **aggregate** | one row per group | total sales per customer |
| **transform** | one value per original row | each delivery's share of its day's total |
| **filter** | the original rows of some groups | only customers with at least five orders |

```python
# aggregate: the table shrinks to one row per customer
summary = deliveries.groupby("customer", as_index=False).agg(
    orders=("amount", "size"),
    total=("amount", "sum"),
    products=("product", "nunique"),
)

# transform: the table keeps its shape; every row gets its group's value
day_total = deliveries.groupby("date")["amount"].transform("sum")
deliveries["share_of_day"] = deliveries["amount"] / day_total
```

A way to tell which you need before writing code: *how many rows should the
answer have?* One per group means aggregate. As many as the table means
transform.

### Concept 4 — A missing value is a question

A blank cell can mean three different things:

| The blank means | Treat it as | The average... |
|---|---|---|
| "nothing happened" (no tip was given) | zero | counts the row, with 0 |
| "we do not know" (nobody wrote it down) | missing | leaves the row out |
| "does not apply" (a price level for a business with no prices) | missing, and perhaps a separate group | leaves the row out |

These give different numbers, sometimes by a factor of two, and no error
message will raise the question for you. pandas has a default: it **skips**
missing values in sums and averages. That default is a decision somebody made
on your behalf.

```python
tips.mean()                 # blanks left out
tips.fillna(0).mean()       # blanks counted as zero
tips.isna().sum()           # how many blanks there are: always report this
```

How missing values behave, in brief: arithmetic with a missing value gives a
missing value; a comparison with one gives `False`; `groupby` drops rows whose
group is missing unless told `dropna=False`; and `count` counts values while
`size` counts rows.

The worst missing values are the **disguised** ones, which `isna()` cannot
see: an empty string, the word `"Unknown"` or `"None"`, a zero that means "not
measured", a date of 1900-01-01. Finding them takes a look at the actual
values of each column.

### Concept 5 — Inspect before you conclude

Five lines of looking, before the one line of computing:

```python
table.shape                 # how many rows and columns
table.dtypes                # is the price a number, or text?
table.head()                # what does a row look like?
table.isna().sum()          # where are the blanks?
table.describe()            # ranges: is anything impossible?
```

For a text column, `table["state"].value_counts(dropna=False)` shows every
distinct value with its count, which is where disguised blanks, misspellings
and groups of three rows become visible.

**Cleaning** is then a short list of explicit rules, each of which makes a
value missing or corrects its type, and none of which deletes a row silently:

```python
dates = pd.to_datetime(table["date"], errors="coerce")       # not a date -> missing
table["cover"] = table["cover"].where(table["cover"].between(0, 100))
words = table["kind"].str.strip().str.lower()
table["kind"] = table["kind"].mask(words.isin(["unknown", ""]))
```

Count what each rule changed, and report it with the result.

### Reading and writing

| Format | Read | Write |
|---|---|---|
| CSV | `pd.read_csv(path)` | `table.to_csv(path, index=False)` |
| JSON, a list of records | `pd.read_json(path)` | `table.to_json(path, orient="records")` |
| JSON Lines, one record per line | `pd.read_json(path, lines=True)` | `table.to_json(path, orient="records", lines=True)` |

Real JSON often nests data: a restaurant's attributes arrive as a dictionary
inside one cell. `column.str.get("key")` pulls one entry out of each.

## 3. Business use cases

**A farm's delivery book.** A small farm delivers boxes of produce to four
restaurants. The owner wants the total per customer and per product. Done
with a loop and a dictionary it is fifteen lines and easy to get subtly
wrong; as a table it is one `groupby`. The follow-up questions arrive at once
(which customer bought the most *different* products? what share of each
day's revenue was each delivery?) and each is one more line, where the loop
version would need rewriting.

**Tips that are half empty.** The farm starts recording the tip on each
delivery. The driver fills the column in when they remember, and four of
eight cells are blank. Leave the blanks out and the average tip is $3.00;
count them as zero and it is $1.50. Which is right depends on whether a blank
means "no tip was given", "the driver forgot to write it down", or "this
customer pays by invoice and never tips". The analyst's job is to find out,
choose, and say which was chosen. There is a second trap in the same column:
split the deliveries into "tip above $2" and "tip of $2 or less" and the four
blank rows are in neither half, because every comparison with a missing value
is False.

**Do more expensive restaurants get better ratings?** A review site publishes
150,000 business records. The question seems to need one line: average stars
per price level. On the way to an answer worth giving:

- the price level is stored as text inside a nested dictionary, with the word
  `'None'` for some blanks;
- some text fields are empty strings, which `isna()` does not report;
- a few states have four businesses in them, and their averages mean nothing;
- restaurants with no listed price turn out to be rated differently from the
  rest, so dropping them changes the comparison;
- restaurants with a handful of reviews have extreme averages, and once they
  are set aside the pattern changes.

The honest result is a sentence with its conditions attached: *among
restaurants with at least so many reviews and a listed price, the average
rating rises by so much per price level; so many records had no price and
were left out.*

**A public agency's field records.** Surveyors record infestations of
invasive plants: the area, the share of ground covered, the date. Half the
records have no cover percentage. Some dates are placeholders a century off.
Some percentages are above 100. Before anyone reports "average cover by
forest", the table needs the four cleaning rules above, and the report needs
to state how many values each rule removed.

**Sales by region for a monthly report.** The most common request in any
business. The risks are the ones this session names: joining order lines to
orders and counting freight once per line (a grain error), averaging a column
with blanks without knowing what they mean, and presenting a region with
three orders next to one with three thousand as if the averages were equally
solid.

## Key points

- A line of pandas always returns a number. Whether the number means anything
  is decided before the line is written.
- Know the grain: what one row stands for.
- Describe the column, not the row.
- "Per" means split, apply, combine. Ask how many rows the answer should
  have.
- A blank is zero, unknown, or not applicable. Decide, and say so.
- Inspect first: shape, types, a few rows, blanks, ranges, distinct values.
- Report what was left out, with counts.
