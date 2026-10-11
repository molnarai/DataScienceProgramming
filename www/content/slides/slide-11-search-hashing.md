+++
title = "Search and Hashing"
description = "What a lookup costs and how that cost grows: linear search, binary search, hash tables, and choosing the structure that fits the question"
weight = 110
outputs = ["Reveal"]
math = false
thumbnail = "../imgs/slides/.png"

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

<p class="dc-kicker">IFI 8410 — Session 11: Search and Hashing</p>
<h1>Finding Things</h1>
<p class="dc-sub">What a lookup costs, and how that cost grows</p>

{{% note %}}
A change of register: the last three sessions were about data and what it means. This one and the next are about how programs do their work, and what it costs.
{{% /note %}}

***

<p class="dc-kicker">The problem</p>

## Two programs that look almost identical

<div class="dc-code-lg">
{{< highlight python >}}
if x in collection:
    ...
{{< /highlight >}}
</div>

<p class="dc-small">On a hundred records, any way of answering is instant. On a million, one version looks at <b>up to a million items every time</b>; the other looks at <b>one</b>.</p>

<div class="dc-grid three">
  <div class="dc-card"><h3>What does a lookup cost?</h3><p>And how does that cost grow as the data grows?</p></div>
  <div class="dc-card"><h3>How should the data be organised?</h3><p>So that the lookups I need are cheap.</p></div>
  <div class="dc-card"><h3>Which organisation fits which question?</h3><p>One exact key, everything between two values, and what is missing are different questions.</p></div>
</div>

{{% note %}}
The underlying skill is reasoning about cost before running the program. It matters more the larger the data gets, and it matters to everyone who writes a loop over a table.
{{% /note %}}

***

<p class="dc-kicker">The tools</p>

## All of it is in Python itself

<table class="dc-table">
  <thead><tr><th>Tool</th><th>Purpose</th><th>What it gives you</th></tr></thead>
  <tbody>
    <tr><td><code>list</code></td><td>an ordered sequence</td><td><code>x in items</code>, <code>.index(x)</code>, <code>.count(x)</code>: all of them <b>scan</b></td></tr>
    <tr><td><code>sorted</code>, <code>.sort</code></td><td>ordering</td><td>a sorted copy or an in-place sort, by any key</td></tr>
    <tr><td><code>bisect</code></td><td>searching sorted lists</td><td>where a value is, or would go, in about log₂(n) steps</td></tr>
    <tr><td><code>dict</code></td><td>lookup by key</td><td>a value stored under a key, found in about one step</td></tr>
    <tr><td><code>set</code></td><td>membership</td><td>"is it there?" in about one step; unions, intersections, differences</td></tr>
    <tr><td><code>Counter</code>, <code>defaultdict</code></td><td>tallies and groups</td><td>counting and grouping, built on <code>dict</code></td></tr>
  </tbody>
</table>

<p class="dc-small">pandas uses the same ideas: <code>merge</code>, <code>isin</code>, <code>groupby</code>, <code>value_counts</code> are built on hash tables; <code>searchsorted</code> is a binary search.</p>

***

<p class="dc-kicker">Concept 1</p>

## Count the work, do not time it

<div class="dc-code-lg">
{{< highlight python >}}
def linear_search(items, target):
    comparisons = 0
    for index in range(len(items)):
        comparisons += 1
        if items[index] == target:
            return (index, comparisons)
    return (-1, comparisons)
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>Time the same line five times and you get five answers; on a shared machine, very different ones.</li>
  <li>A <b>count</b> of comparisons is the same on every machine.</li>
  <li>It answers what a time cannot: <b>what happens when the data is ten times larger?</b></li>
</ul>

***

<p class="dc-kicker">Concept 2</p>

## Linear search

<div class="dc-cols">
<div>
<h4>One search</h4>
<table class="dc-table">
  <thead><tr><th>Case</th><th>Comparisons, n items</th></tr></thead>
  <tbody>
    <tr><td>the target is first</td><td>1</td></tr>
    <tr><td>it is there, on average</td><td>about n / 2</td></tr>
    <tr><td><b>it is not there</b></td><td><b>n, every time</b></td></tr>
  </tbody>
</table>
<p class="dc-small">Ten times the list, ten times the work: <b>linear</b>. It needs nothing from the data.</p>
</div>
<div>
<h4 class="bad">A search inside a loop</h4>
{{< highlight python >}}
for order in orders:              # a million
    if order["customer"] in customer_list:
        ...                       # scans 100,000
{{< /highlight >}}
<p class="dc-small">Up to a hundred billion comparisons. Work that grows with the product of two sizes is <b>quadratic</b>.</p>
</div>
</div>

<p class="dc-small">"Is this new?" and "which are missing?" are questions about things that are <b>not there</b>: the worst case, every time.</p>

{{% note %}}
in, .index() and .count() on a list are linear searches. The scan inside a loop is the usual reason a program that worked on a sample never finishes on the full file.
{{% /note %}}

***

<p class="dc-kicker">Concept 3</p>

## Binary search

<div class="dc-cols">
<div>
{{< highlight python >}}
def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
            return middle
        if items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
{{< /highlight >}}
</div>
<div>
<ul class="dc-points">
  <li>Guess a number from 1 to 100: nobody starts at 1. Every answer <b>halves</b> what is left.</li>
  <li>The promise the loop keeps: <i>if the target is in the list, it is between <code>low</code> and <code>high</code>.</i></li>
</ul>
<table class="dc-table">
  <thead><tr><th>Items</th><th>Linear</th><th>Binary</th></tr></thead>
  <tbody>
    <tr><td>1,000</td><td>500</td><td>10</td></tr>
    <tr><td>1,000,000</td><td>500,000</td><td>20</td></tr>
    <tr><td>1,000,000,000</td><td>500,000,000</td><td>30</td></tr>
  </tbody>
</table>
</div>
</div>

<p class="dc-small">2²⁰ is about a million. The number of halvings is the <b>logarithm to base 2</b> of the size: <b>logarithmic</b> work.</p>

{{% note %}}
Trace it by hand on a list of eight before running it. The classic bug: low = middle, without the + 1, never ends once low and high are neighbours.
{{% /note %}}

***

<p class="dc-kicker">Concept 3, two things to know</p>

## The price of binary search

<div class="dc-grid">
  <div class="dc-card red"><h3>It needs sorted data, and fails silently</h3><p>On an unsorted list it throws away the half that holds the target and reports "not there". No error.</p></div>
  <div class="dc-card"><h3>Sorting has a price</h3><p>About n × log₂(n) comparisons, paid once. For one lookup it is a waste; for a few dozen it has already paid for itself.</p></div>
</div>

<div class="dc-code-lg">
{{< highlight python >}}
import bisect

position = bisect.bisect_left(sorted_items, target)       # where it is, or would go
found = position < len(sorted_items) and sorted_items[position] == target

count = bisect.bisect_left(dates, "2020-01-01") - bisect.bisect_left(dates, "2019-01-01")
{{< /highlight >}}
</div>

<p class="dc-small">The <b>insertion point</b> is more useful than "found or not": two of them fence in a range without looking inside it.</p>

***

<p class="dc-kicker">Concept 4</p>

## Hashing: do not search, compute where it must be

<div class="dc-cols">
<div>
{{< highlight python >}}
def hash_key(key):
    value = 0
    for character in key:
        value = (value * 31
                 + ord(character)) % 1_000_000_007
    return value

bucket = hash_key(key) % buckets
{{< /highlight >}}
</div>
<div>
<ul class="dc-points">
  <li>A cloakroom: the last two digits of the ticket are the hook.</li>
  <li>A <b>hash function</b> turns a key into a number, the same one every time.</li>
  <li>Two keys in one <b>bucket</b> is a <b>collision</b>, so each bucket holds a short list.</li>
  <li>The <b>load factor</b> is keys ÷ buckets. Past a limit, the table doubles and re-places every key.</li>
</ul>
</div>
</div>

<p class="dc-quote">A lookup takes about <b>one step, whatever the size</b>. Work that does not grow is <b>constant</b>.</p>

***

<p class="dc-kicker">Concept 4, continued</p>

## `dict` and `set` are hash tables

<div class="dc-code-lg">
{{< highlight python >}}
999_999 in a_list_of_a_million      # scans
999_999 in a_set_of_a_million       # one step: thousands of times faster

customers = set(customer_list)      # the one-line fix for the slow loop
{{< /highlight >}}
</div>

<div class="dc-grid">
  <div class="dc-card"><h3>A key must not change</h3><p>Its bucket is computed from its contents. Change them and it sits in the wrong bucket, never to be found. So keys are immutable: numbers, strings, tuples. Not lists.</p></div>
  <div class="dc-card red"><h3>A hash table has no order</h3><p>The hash scatters keys on purpose. It can say whether exactly this key is present, and nothing about what comes next, lies between, or starts with the same letters.</p></div>
</div>

{{% note %}}
Two rules students have met without their reasons. Both follow from how hashing works.
{{% /note %}}

***

<p class="dc-kicker">Concept 5</p>

## Choosing

<table class="dc-table">
  <thead><tr><th>Operation</th><th>Unsorted list</th><th>Sorted list</th><th><code>dict</code> / <code>set</code></th></tr></thead>
  <tbody>
    <tr><td>is this key here?</td><td>n</td><td>log n</td><td><b>1</b></td></tr>
    <tr><td>add an item</td><td>1</td><td>n</td><td>1</td></tr>
    <tr><td>everything between a and b</td><td>n</td><td><b>log n</b></td><td>n</td></tr>
    <tr><td>the smallest; the next larger</td><td>n</td><td><b>1; log n</b></td><td>n</td></tr>
    <tr><td>needs</td><td>nothing</td><td>sorting; comparable items</td><td>immutable keys; more memory</td></tr>
  </tbody>
</table>

<ol class="dc-points">
  <li><b>Many lookups by exact key:</b> a <code>dict</code> or a <code>set</code>. The usual case and the usual fix.</li>
  <li><b>Questions about order or ranges:</b> sort once, then <code>bisect</code>.</li>
  <li><b>A handful of items, or a single lookup:</b> a list and <code>in</code> are fine.</li>
</ol>

***

<p class="dc-kicker">Worked example — notebook 2</p>

## 900,000 tips and their businesses

<p class="dc-small">Each tip carries the id of a business; a separate file holds 150,000 businesses. To say anything about a tip, its business has to be found.</p>

<div class="dc-grid three">
  <div class="dc-card red"><h3>Scan the list for each tip</h3><p class="dc-from">linear</p><p>About a <b>quarter of an hour</b>.</p></div>
  <div class="dc-card"><h3>Sort the ids once, then halve</h3><p class="dc-from">binary</p><p><b>Under a second.</b></p></div>
  <div class="dc-card green"><h3>A dictionary from id to business</h3><p class="dc-from">hash</p><p>A <b>quarter of a second.</b></p></div>
</div>

<ul class="dc-points">
  <li>The step from the first to the second is the difference between unusable and instant.</li>
  <li>The step from the second to the third hardly matters.</li>
  <li>This is the <b>join</b> that databases and pandas perform, and it is why they are fast.</li>
</ul>

{{% note %}}
Run the notebook on ARC. The obvious way is run on a sample and extrapolated, not run to the end.
{{% /note %}}

***

<p class="dc-kicker">Worked example — notebook 2</p>

## What each structure was good for

<div class="dc-grid three">
  <div class="dc-card"><h3>A set: membership</h3><p>Which businesses have no tip at all? Does every tip refer to a business we have? How many different people wrote tips? <code>len(set(user_ids))</code></p></div>
  <div class="dc-card"><h3>Sorted data: ranges and prefixes</h3><p>How many names start with "Star"? How many tips were written in 2019? Two binary searches and a subtraction.</p></div>
  <div class="dc-card"><h3>A dictionary: tallies</h3><p>Which businesses get the most tips? One pass, one running total per key. What <code>Counter</code>, <code>groupby</code> and <code>value_counts</code> do underneath.</p></div>
</div>

<p class="dc-small" style="margin-top: 18px;">Orphan records are a routine data-quality check before trusting any join. With a set it is cheap enough to run every time.</p>

{{% note %}}
A dictionary cannot answer the prefix or the date-range question: it can only be asked for one exact key at a time. This is why databases keep sorted indexes as well as hash indexes.
{{% /note %}}

***

<p class="dc-kicker">In practice</p>

## A slow report, diagnosed

<p class="dc-small">A monthly report that used to take seconds now takes an hour. The customer file grew from five thousand to five hundred thousand rows.</p>

<div class="dc-cols">
<div>
<h4 class="bad">An <code>in</code> against a list, inside a loop</h4>
{{< highlight python >}}
for order in orders:
    if order["customer"] in customer_list:
        ...
{{< /highlight >}}
</div>
<div>
<h4 class="good">One line restores the seconds</h4>
{{< highlight python >}}
customers = set(customer_list)
for order in orders:
    if order["customer"] in customers:
        ...
{{< /highlight >}}
</div>
</div>

<p class="dc-quote">Recognising that pattern is the most practically useful thing in this session.</p>

***

<p class="dc-kicker">To take away</p>

## Key points

<ul class="dc-points">
  <li>Ask how the work grows, not how long it took today.</li>
  <li>A linear search is harmless once and ruinous inside a loop.</li>
  <li>Binary search needs sorted data and is silently wrong without it.</li>
  <li>A hash table finds an exact key in about one step; <code>dict</code> and <code>set</code> are hash tables.</li>
  <li>Sorted data answers "between", "next" and "starts with". A hash table does not.</li>
  <li>Before optimising anything else, look for a scan inside a loop.</li>
</ul>

{{% note %}}
The names for later: linear is O(n), logarithmic is O(log n), constant is O(1).
{{% /note %}}

***

<p class="dc-kicker">Now: hands-on</p>

## Over to the notebooks

<p class="dc-small">Folder <a href="https://github.com/molnarai/DataScienceProgramming/tree/main/11-Search-Hashing"><code>11-Search-Hashing</code></a> — work them in this order:</p>

<div class="dc-grid three">
  <div class="dc-card green"><h3><span class="dc-nb"><span class="num">1</span></span>Finding Things</h3><p class="dc-from">Concepts</p><p>Counting comparisons, linear and binary search, a hash table from scratch, and choosing. Four exercises.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">2</span></span>Yelp Tips</h3><p class="dc-from">Worked example</p><p>900,000 tips matched to their businesses three ways, in seven steps. Run it on ARC.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">3</span></span>Reference</h3><p class="dc-from">Look things up</p><p>Lists, <code>bisect</code>, dictionaries and sets to keep open while you work.</p></div>
</div>

<p class="dc-small" style="margin-top: 20px;">As you work, ask of every lookup: <b>what happens when the data is ten times larger?</b><br>Homework: <a href="../../assignments/assignment-10/">Homework 10: Three Ways to Find It</a></p>
