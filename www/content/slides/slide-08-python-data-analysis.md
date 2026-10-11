+++
title = "Python for Data Analysis"
description = "Tables, vectorized thinking, split-apply-combine, and missing values: what has to be true before a line of pandas can be trusted"
weight = 80
outputs = ["Reveal"]
math = false
thumbnail = "../imgs/slides/pandas-origami.png"


[reveal_hugo]
custom_theme = "css/reveal-robinson.css"
slide_number = true
transition = "none"

+++

<style>
  .reveal .slides section { box-sizing: border-box; }
  .reveal .dc-sub { color: #666; font-size: 0.9em; }
  .reveal .dc-kicker { color: #CC0000; font-size: 0.55em; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin: 0 0 4px 0; }
  .reveal .dc-small { font-size: 0.75em; }
  .reveal .dc-muted { color: #666; }
  .reveal .dc-quote { font-size: 0.85em; border-left: 5px solid #CC0000; background: #f4f6f9; padding: 12px 18px; text-align: left; margin: 18px 0; }

  /* Cards */
  .reveal .dc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px; }
  .reveal .dc-grid.three { grid-template-columns: 1fr 1fr 1fr; }
  .reveal .dc-card { background: #f4f6f9; border-left: 5px solid #003478; padding: 10px 14px; border-radius: 4px; }
  .reveal .dc-card h3 { margin: 0 0 4px 0; font-size: 0.85em; }
  .reveal .dc-card p { margin: 0; font-size: 0.62em; }
  .reveal .dc-card .dc-from { color: #666; font-size: 0.58em; margin-bottom: 6px; }
  .reveal .dc-card.red { border-left-color: #CC0000; }
  .reveal .dc-card.red h3 { color: #CC0000; }
  .reveal .dc-card.green { border-left-color: #2e7d32; }
  .reveal .dc-card.green h3 { color: #2e7d32; }

  /* Flow */
  .reveal .dc-flow { display: flex; align-items: center; justify-content: center; gap: 8px; margin: 20px 0; }
  .reveal .dc-node { background: #f4f6f9; border: 2px solid #003478; border-radius: 6px; padding: 10px 14px; font-size: 0.62em; text-align: center; }
  .reveal .dc-node.dark { background: #003478; color: #fff; }
  .reveal .dc-node .dc-owner { margin-top: 4px; font-size: 0.85em; font-style: italic; color: #CC0000; }
  .reveal .dc-node.dark .dc-owner { color: #cfd8e8; }
  .reveal .dc-arrow { color: #003478; font-size: 0.9em; font-weight: 700; }

  /* Two columns */
  .reveal .dc-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }
  .reveal .dc-cols h4 { font-size: 0.65em; margin: 6px 0 0 0; }
  .reveal .dc-cols h4.bad { color: #CC0000; }
  .reveal .dc-cols h4.good { color: #2e7d32; }

  /* Code */
  .reveal .highlight pre, .reveal pre { width: 100%; font-size: 0.5em; margin: 8px 0; }
  .reveal .dc-code-lg pre { font-size: 0.58em; }

  /* Bullets */
  .reveal .dc-points { margin-top: 8px; }
  .reveal .dc-points li { font-size: 0.72em; margin-bottom: 0.4em; }

  .reveal .dc-table { font-size: 0.58em; width: 100%; margin-top: 10px; }
  .reveal .dc-table td { vertical-align: top; }

  .reveal .dc-nb { font-size: 0.6em; }
  .reveal .dc-nb .num { display: inline-block; width: 1.6em; height: 1.6em; line-height: 1.6em; text-align: center; border-radius: 50%; background: #003478; color: #fff; font-weight: 700; margin-right: 6px; }
</style>

<p class="dc-kicker">IFI 8410 — Session 8: Python for Data Analysis</p>
<h1>Python for Data Analysis</h1>
<p class="dc-sub">A line of pandas always returns a number</p>

{{% note %}}
Session 7 was about the shape of tables and the operations on them. Today is pandas in practice, and the theme is not syntax: it is everything that has to be true before the one computing line can be trusted.
{{% /note %}}

***

<p class="dc-kicker">The problem</p>

## One line, and it always answers

<div class="dc-code-lg">
{{< highlight python >}}
restaurants.groupby("price")["stars"].mean()
{{< /highlight >}}
</div>

<p class="dc-small">It does not know about blank cells, a price stored as the word <code>"None"</code>, a placeholder date of 1900-01-01, or a group with half its records missing. <b>It computes anyway.</b></p>

<div class="dc-grid">
  <div class="dc-card"><h3>What is in this table?</h3><p>What one row stands for, the column types, what is missing.</p></div>
  <div class="dc-card"><h3>Is it fit to compute on?</h3><p>Which values are wrong, disguised, or impossible.</p></div>
  <div class="dc-card red"><h3>What does a blank mean?</h3><p>Zero, unknown, or not applicable.</p></div>
  <div class="dc-card red"><h3>What does the result leave out?</h3><p>How many rows it used, and which it dropped.</p></div>
</div>

{{% note %}}
A wrong answer looks exactly like a right one: same format, same number of decimals, no error message. So the work is in the four questions, not in the line.
{{% /note %}}

***

<p class="dc-kicker">The tools</p>

## Two packages

<div class="dc-grid">
  <div class="dc-card"><h3>pandas <code>pd</code></h3><p class="dc-from">tables</p><p>The <code>DataFrame</code> (a table with named columns) and the <code>Series</code> (one column). Reading and writing CSV and JSON; selecting, joining, grouping; dates and text.</p></div>
  <div class="dc-card"><h3>NumPy <code>np</code></h3><p class="dc-from">arrays of numbers</p><p>Fast arithmetic on whole arrays, and the engine underneath pandas. <code>np.where</code> and <code>np.select</code> choose values by a condition.</p></div>
</div>

<p class="dc-small" style="margin-top: 22px;"><code>import pandas as pd</code> and <code>import numpy as np</code> — a convention so universal that code without it looks wrong.</p>

***

<p class="dc-kicker">Concept 1</p>

## The table is the central structure

<div class="dc-cols">
<div>
<h4 class="bad">Core Python: a loop and a dictionary</h4>
{{< highlight python >}}
totals = {}
for row in records:
    name = row["customer"]
    if name not in totals:
        totals[name] = 0
    totals[name] += row["amount"]
{{< /highlight >}}
</div>
<div>
<h4 class="good">pandas: the loop disappears</h4>
{{< highlight python >}}
deliveries = pd.DataFrame(records)

deliveries.groupby("customer")["amount"].sum()
{{< /highlight >}}
</div>
</div>

<ul class="dc-points">
  <li>Rows are <b>observations</b>, columns are <b>variables</b>.</li>
  <li>First question of any table, its <b>grain</b>: what does one row stand for? One order, or one line of an order?</li>
  <li>Every count and every average depends on the answer.</li>
</ul>

{{% note %}}
The left side is what students wrote in HW04. What the table lets you stop thinking about is the bookkeeping: creating the totals dictionary, checking whether a key is there, keeping the loop variable straight.
{{% /note %}}

***

<p class="dc-kicker">Concept 2</p>

## Vectorized thinking

<p><b>Say what happens to a whole column, not what happens to each row.</b></p>

<div class="dc-code-lg">
{{< highlight python >}}
deliveries["amount"] = deliveries["boxes"] * deliveries["price_per_box"]
deliveries["large"]  = deliveries["boxes"] >= 4

deliveries["discounted"] = np.where(deliveries["boxes"] >= 4,
                                    deliveries["amount"] * 0.9,
                                    deliveries["amount"])
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>No loop in sight: the work happens in compiled code, hundreds of times faster on a million rows.</li>
  <li>Speed is the smaller benefit. The code reads like the sentence: <i>amount is boxes times price</i>.</li>
  <li><code>.where(cond)</code> keeps values where the condition holds and blanks the rest; <code>.mask(cond)</code> is the reverse.</li>
</ul>

{{% note %}}
The habit to build: when you catch yourself writing for over the rows of a table, stop and ask what the column-level sentence is. Also worth showing from the notebook: the mean of a True/False column is a share.
{{% /note %}}

***

<p class="dc-kicker">Concept 3</p>

## Split, apply, combine

<p class="dc-small">Every question with the word <b>per</b> in it has the same three steps.</p>

<div class="dc-flow">
  <div class="dc-node">Split<div class="dc-owner">rows into groups</div></div>
  <div class="dc-arrow">→</div>
  <div class="dc-node dark">Apply<div class="dc-owner">a calculation to each</div></div>
  <div class="dc-arrow">→</div>
  <div class="dc-node">Combine<div class="dc-owner">the results</div></div>
</div>

<table class="dc-table">
  <thead><tr><th>Kind</th><th>Result</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td><b>aggregate</b></td><td>one row per group</td><td>total sales per customer</td></tr>
    <tr><td><b>transform</b></td><td>one value per original row</td><td>each delivery's share of its day's total</td></tr>
    <tr><td><b>filter</b></td><td>the original rows of some groups</td><td>only customers with at least five orders</td></tr>
  </tbody>
</table>

{{% note %}}
pandas does all three steps with groupby. Choosing which of the three kinds of calculation you need is most of the skill.
{{% /note %}}

***

<p class="dc-kicker">Concept 3 in code</p>

## `agg` shrinks the table, `transform` keeps its shape

<div class="dc-code-lg">
{{< highlight python >}}
# aggregate: one row per customer
summary = deliveries.groupby("customer", as_index=False).agg(
    orders=("amount", "size"),
    total=("amount", "sum"),
    products=("product", "nunique"),
)

# transform: every row gets its group's value
day_total = deliveries.groupby("date")["amount"].transform("sum")
deliveries["share_of_day"] = deliveries["amount"] / day_total
{{< /highlight >}}
</div>

<p class="dc-quote">Before writing code, ask: <b>how many rows should the answer have?</b> One per group means aggregate. As many as the table means transform.</p>

***

<p class="dc-kicker">Concept 4</p>

## A missing value is a question

<table class="dc-table">
  <thead><tr><th>The blank means</th><th>Treat it as</th><th>The average…</th></tr></thead>
  <tbody>
    <tr><td>"nothing happened" — no tip was given</td><td>zero</td><td>counts the row, with 0</td></tr>
    <tr><td>"we do not know" — nobody wrote it down</td><td>missing</td><td>leaves the row out</td></tr>
    <tr><td>"does not apply" — a price level for a business with no prices</td><td>missing, perhaps a separate group</td><td>leaves the row out</td></tr>
  </tbody>
</table>

<div class="dc-code-lg">
{{< highlight python >}}
tips.mean()             # 3.00   blanks left out
tips.fillna(0).mean()   # 1.50   blanks counted as zero
tips.isna().sum()       # 4      of 8: always report this
{{< /highlight >}}
</div>

<p class="dc-small">pandas <b>skips</b> missing values in sums and averages. That default is a decision somebody made on your behalf.</p>

{{% note %}}
The farm example from the first notebook: the driver fills the tip column in when they remember, and four of eight cells are blank. Same column, a factor of two apart. Which is right depends on what the blank means, and that is not a pandas question.
{{% /note %}}

***

<p class="dc-kicker">Concept 4, continued</p>

## How missing values behave

<div class="dc-grid">
  <div class="dc-card"><h3>Arithmetic</h3><p>Anything computed with a missing value is missing.</p></div>
  <div class="dc-card red"><h3>Comparisons</h3><p>A comparison with a missing value is <code>False</code>. Split tips into "above $2" and "$2 or less" and the blank rows are in <b>neither</b> half.</p></div>
  <div class="dc-card red"><h3>Groups</h3><p><code>groupby</code> drops rows whose key is missing, unless told <code>dropna=False</code>.</p></div>
  <div class="dc-card"><h3>Counting</h3><p><code>count</code> counts values; <code>size</code> counts rows.</p></div>
</div>

<p class="dc-small" style="margin-top: 18px;"><b>The worst ones are disguised</b>, and <code>isna()</code> cannot see them: an empty string, the word <code>"Unknown"</code> or <code>"None"</code>, a zero that means "not measured", a date of 1900-01-01.</p>

***

<p class="dc-kicker">Concept 5</p>

## Inspect before you conclude

<div class="dc-cols">
<div>
<h4>Five lines of looking</h4>
{{< highlight python >}}
table.shape          # rows and columns
table.dtypes         # number, or text?
table.head()         # what is a row?
table.isna().sum()   # where are blanks?
table.describe()     # anything impossible?

table["state"].value_counts(dropna=False)
{{< /highlight >}}
</div>
<div>
<h4>Cleaning: explicit rules</h4>
{{< highlight python >}}
dates = pd.to_datetime(table["date"],
                       errors="coerce")
table["cover"] = table["cover"].where(
    table["cover"].between(0, 100))
words = table["kind"].str.strip().str.lower()
table["kind"] = table["kind"].mask(
    words.isin(["unknown", ""]))
{{< /highlight >}}
</div>
</div>

<ul class="dc-points">
  <li>Each rule makes a value <b>missing</b> or corrects its type. None deletes a row silently.</li>
  <li><b>Count what each rule changed</b>, and report it with the result.</li>
</ul>

{{% note %}}
value_counts with dropna=False is where disguised blanks, misspellings and groups of three rows become visible.
{{% /note %}}

***

<p class="dc-kicker">Worked example — notebook 2</p>

## Do more expensive restaurants get better ratings?

<p class="dc-small">150,000 Yelp business records. The question seems to need one line: average stars per price level. On the way to an answer worth giving:</p>

<ul class="dc-points">
  <li>the price level is text inside a nested dictionary, with the word <code>'None'</code> for some blanks;</li>
  <li>some text fields are empty strings, which <code>isna()</code> does not report;</li>
  <li>a few states have four businesses in them, and their averages mean nothing;</li>
  <li>restaurants with no listed price are rated differently from the rest, so dropping them changes the comparison;</li>
  <li>restaurants with a handful of reviews have extreme averages; set them aside and the pattern changes.</li>
</ul>

{{% note %}}
Walk through the seven steps of the notebook: load, inspect, clean, whole-column work, split-apply-combine, what do the blanks mean, conclude. Nested JSON: column.str.get("key") pulls one entry out of each dictionary.
{{% /note %}}

***

<p class="dc-kicker">Worked example — the result</p>

## An answer with its conditions attached

<p class="dc-quote"><i>Among restaurants with at least so many reviews and a listed price, the average rating rises by so much per price level; so many records had no price and were left out.</i></p>

<ul class="dc-points">
  <li>The number, <b>and how many rows it came from</b>.</li>
  <li>What was left out, and why.</li>
  <li>Which meaning of a blank was chosen.</li>
</ul>

<p class="dc-small">The same applies to the monthly sales-by-region report: a grain error counts freight once per order line, and a region with three orders sits next to one with three thousand as if the averages were equally solid.</p>

***

<p class="dc-kicker">To take away</p>

## Key points

<ul class="dc-points">
  <li>A line of pandas always returns a number. Whether it means anything is decided before the line is written.</li>
  <li>Know the grain: what one row stands for.</li>
  <li>Describe the column, not the row.</li>
  <li>"Per" means split, apply, combine. Ask how many rows the answer should have.</li>
  <li>A blank is zero, unknown, or not applicable. Decide, and say so.</li>
  <li>Inspect first: shape, types, a few rows, blanks, ranges, distinct values.</li>
  <li>Report what was left out, with counts.</li>
</ul>

***

<p class="dc-kicker">Now: hands-on</p>

## Over to the notebooks

<p class="dc-small">Folder <a href="https://github.com/molnarai/DataScienceProgramming/tree/main/08-Python-Data-Analysis"><code>08-Python-Data-Analysis</code></a> — work them in this order:</p>

<div class="dc-grid three">
  <div class="dc-card green"><h3><span class="dc-nb"><span class="num">1</span></span>Thinking in Tables</h3><p class="dc-from">Concepts</p><p>The farm's delivery book: tables, vectorized columns, <code>groupby</code>, and tips that are half empty. Four exercises.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">2</span></span>Yelp Businesses</h3><p class="dc-from">Worked example</p><p>One question, seven steps, on 150,000 real records. Run it on ARC.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">3</span></span>Reference</h3><p class="dc-from">Look things up</p><p>pandas and NumPy operations to keep open while you work.</p></div>
</div>

<p class="dc-small" style="margin-top: 20px;">As you work, ask of every result: <b>how many rows did it use, and which did it leave out?</b><br>Homework: <a href="../../assignments/assignment-07/">Homework 7: Invasive Plants, from Raw File to Report</a></p>
