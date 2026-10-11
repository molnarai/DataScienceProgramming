+++
title = "Visualization and Descriptive Statistics"
description = "Mean and median, spread, outliers, correlation, and charts with matplotlib: describing data honestly in numbers and in pictures"
weight = 90
outputs = ["Reveal"]
math = true
thumbnail = "../imgs/slides/data-analysis-with-pythons.png"

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

<p class="dc-kicker">IFI 8410 — Session 9: Visualization and Descriptive Statistics</p>
<h1>Numbers and Pictures</h1>
<p class="dc-sub">Describing data honestly</p>

{{% note %}}
Last week the table was cleaned and summarised per group. Today: how to tell someone what is in it. Nothing here predicts or tests anything. It says what is there, which has to come first.
{{% /note %}}

***

<p class="dc-kicker">The problem</p>

## Nobody can read ten thousand rows

<div class="dc-grid">
  <div class="dc-card"><h3>A few numbers</h3><p>An average, a spread, a correlation. Exact, and fits in a sentence. <b>Hides the shape</b>: two very different columns can have the same mean.</p></div>
  <div class="dc-card"><h3>A picture</h3><p>A histogram, bars, a scatter plot, a line. Shows the shape. <b>Cannot be quoted</b>, and can mislead through the choice of an axis.</p></div>
</div>

<p class="dc-small" style="margin-top: 22px;">Three failures this session is organised around:</p>

<ol class="dc-points">
  <li>reporting a mean for data where the mean describes almost no one;</li>
  <li>deleting unusual values because they are unusual;</li>
  <li>a chart that is technically correct and gives a false impression.</li>
</ol>

***

<p class="dc-kicker">The tools</p>

## Three packages

<div class="dc-grid three">
  <div class="dc-card"><h3>pandas</h3><p class="dc-from">tables</p><p><code>mean</code>, <code>median</code>, <code>std</code>, <code>quantile</code>, <code>describe</code>, <code>corr</code>, and per-group summaries.</p></div>
  <div class="dc-card"><h3>NumPy</h3><p class="dc-from">arrays</p><p>The same reductions on arrays; <code>np.quantile</code>; <code>np.geomspace</code> for logarithmic bins.</p></div>
  <div class="dc-card"><h3>matplotlib</h3><p class="dc-from">drawing</p><p>Figures and axes; histograms, bars, scatter plots, lines; labels, scales, layout; saving to PNG, PDF, SVG.</p></div>
</div>

<p class="dc-small" style="margin-top: 22px;">seaborn and the <code>.plot</code> methods of pandas are conveniences built on matplotlib. What you learn about figures and axes applies to them too.</p>

***

<p class="dc-kicker">Concept 1</p>

## Centre: mean and median

<div class="dc-code-lg">
{{< highlight python >}}
salaries.mean()      # 47.8   nine employees, 38 to 60 thousand
salaries.median()    # 47.0

# add the owner, at 400
salaries.mean()      # 83.0   nine of ten now earn less than "the average"
salaries.median()    # 48.5
{{< /highlight >}}
</div>

<table class="dc-table">
  <thead><tr><th>Question</th><th>Use</th><th>Because</th></tr></thead>
  <tbody>
    <tr><td>what does a typical one look like?</td><td><b>median</b></td><td>half are below, half above, whatever the extremes do</td></tr>
    <tr><td>what is the total, spread evenly?</td><td><b>mean</b></td><td>mean × count is the total</td></tr>
  </tbody>
</table>

<p class="dc-small">Incomes, prices, review counts and waiting times are <b>skewed</b> to the right. A large gap between mean and median is itself a finding.</p>

{{% note %}}
Neither number is wrong. For a job applicant the median is the honest number; for the payroll budget the mean is. The report should say which question it is answering.
{{% /note %}}

***

<p class="dc-kicker">Concept 2</p>

## Spread, and a trap

<div class="dc-cols">
<div>
<h4>Variance and standard deviation</h4>
{{< highlight python >}}
waits.var()    # variance
waits.std()    # standard deviation
{{< /highlight >}}
<table class="dc-table">
  <thead><tr><th></th><th>divides by</th></tr></thead>
  <tbody>
    <tr><td><code>x.var()</code> in pandas</td><td>count − 1</td></tr>
    <tr><td><code>np.var(x)</code> in NumPy</td><td><b>count</b></td></tr>
    <tr><td><code>np.var(x, ddof=1)</code></td><td>count − 1</td></tr>
  </tbody>
</table>
</div>
<div>
<h4>Quartiles and the IQR</h4>
{{< highlight python >}}
q1 = values.quantile(0.25)
q3 = values.quantile(0.75)
iqr = q3 - q1
values.describe()
{{< /highlight >}}
<table class="dc-table">
  <thead><tr><th></th><th>Centre</th><th>Spread</th></tr></thead>
  <tbody>
    <tr><td>built on sums</td><td>mean</td><td>variance, std</td></tr>
    <tr><td>built on order</td><td>median</td><td>quartiles, IQR</td></tr>
  </tbody>
</table>
</div>
</div>

<p class="dc-small"><b>Same data, same function name, two answers, no warning.</b> One extreme value moves everything built on sums and hardly touches what is built on order.</p>

{{% note %}}
Two cafes with the same average wait of five minutes: one where everyone waits four to six, one with waits from one to ten. The variance is the typical squared distance from the mean; the standard deviation brings it back to the units of the data.
{{% /note %}}

***

<p class="dc-kicker">Concept 3</p>

## Outliers are questions

<div class="dc-code-lg">
{{< highlight python >}}
outside = (values < q1 - 1.5 * iqr) | (values > q3 + 1.5 * iqr)
{{< /highlight >}}
</div>

<p class="dc-small">A column of True and False. <b>Nothing is removed.</b> A flagged value can be three different things:</p>

<table class="dc-table">
  <thead><tr><th>It is</th><th>Example</th><th>Do</th></tr></thead>
  <tbody>
    <tr><td>a mistake</td><td>a salary typed with an extra zero</td><td>correct it or make it missing, and say so</td></tr>
    <tr><td>a different kind of thing</td><td>the owner among the employees</td><td>decide whether it belongs to the question</td></tr>
    <tr><td><b>the most important row</b></td><td>the customer who brings half the revenue</td><td>keep it and report it</td></tr>
  </tbody>
</table>

{{% note %}}
Deleting outliers because they are outliers removes the third kind along with the first. On skewed data the rule flags a great deal, and the flagged rows are frequently the subject of the analysis.
{{% /note %}}

***

<p class="dc-kicker">Concept 4</p>

## Two columns: correlation

<div class="dc-code-lg">
{{< highlight python >}}
table["temperature"].corr(table["cups"])    # r, from -1 to 1
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>r measures <b>straight-line</b> association only: a clear curve can have r near 0.</li>
  <li>It says nothing about cause.</li>
</ul>

<div class="dc-grid">
  <div class="dc-card"><h3>Anscombe's quartet</h3><p>Four small datasets with the same means, the same standard deviations, and the same correlation, 0.82.</p></div>
  <div class="dc-card red"><h3>Drawn, they are…</h3><p>a loose cloud, a curve, a line with one point off it, and a vertical stack with one point that creates the whole correlation.</p></div>
</div>

<p class="dc-quote">Sums cannot tell shapes apart. <b>Always draw the data.</b></p>

***

<p class="dc-kicker">Concept 5</p>

## A figure is an object

<div class="dc-code-lg">
{{< highlight python >}}
fig, ax = plt.subplots(figsize=(7, 4))          # a Figure, with one Axes
ax.hist(waits, bins=20)
ax.axvline(waits.mean(), linestyle="--", label="mean")
ax.axvline(waits.median(), linestyle=":", label="median")
ax.set_xlabel("waiting time (minutes)")
ax.set_ylabel("customers")
ax.set_title("A typical wait is four minutes; a few wait three times as long")
ax.legend()
fig.savefig("waits.png", dpi=150, bbox_inches="tight")
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>A <b>Figure</b> is the whole picture; an <b>Axes</b> is one plot inside it.</li>
  <li>Everything is done by calling methods of the Axes: the <b>object interface</b>.</li>
</ul>

{{% note %}}
plt.hist, plt.xlabel and friends draw on a hidden current Axes. Fine for one quick plot; breaks down with two plots or inside a function. This course uses the object interface throughout.
{{% /note %}}

***

<p class="dc-kicker">Concept 5, continued</p>

## Functions that draw on an Axes

<div class="dc-code-lg">
{{< highlight python >}}
def draw_waits(ax, waits):
    ax.hist(waits, bins=20)
    ax.set_xlabel("waiting time (minutes)")
    return ax

fig, (left, right) = plt.subplots(1, 2, sharex=True, sharey=True)
draw_waits(left, january)
draw_waits(right, july)

fig.savefig("waits.png")
plt.close(fig)
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li><code>sharex</code> and <code>sharey</code> give the panels the same range, which makes them comparable by eye.</li>
  <li>In a program there is no screen: <b>save</b> the figure, then <b>close</b> it. Nothing calls <code>show()</code>.</li>
</ul>

***

<p class="dc-kicker">Concept 6</p>

## The chart follows the question

<table class="dc-table">
  <thead><tr><th>Question</th><th>Kind</th><th>Chart</th><th>Method</th><th>Summary number</th></tr></thead>
  <tbody>
    <tr><td>how are the values spread out?</td><td>distribution</td><td>histogram, box plot</td><td><code>ax.hist</code>, <code>ax.boxplot</code></td><td>median, quartiles</td></tr>
    <tr><td>which group has more?</td><td>comparison</td><td>bars</td><td><code>ax.bar</code>, <code>ax.barh</code></td><td>one number per group</td></tr>
    <tr><td>do two things go together?</td><td>relationship</td><td>scatter plot</td><td><code>ax.scatter</code></td><td>correlation</td></tr>
    <tr><td>how did it change over time?</td><td>trend</td><td>line</td><td><code>ax.plot</code></td><td>change from start to end</td></tr>
  </tbody>
</table>

<p class="dc-quote">Most bad charts are a good answer to a question nobody asked.</p>

{{% note %}}
The coffee cart's summer from notebook 1: one table of 84 days answers all four kinds of question, each with its own chart. For the trend, a seven-day rolling mean sees through the weekly zigzag.
{{% /note %}}

***

<p class="dc-kicker">Concept 7</p>

## Honest pictures

<p class="dc-quote">A figure without axis labels and units is not yet a result.</p>

<ul class="dc-points">
  <li><b>Bars start at zero.</b> Cut the axis at 5,100 and a 7 % difference looks like a factor of four.</li>
  <li><b>A line may start anywhere</b>: it shows change by its slope. State the size of the change in words.</li>
  <li><b>Skewed data needs a logarithmic axis</b>, with bins from <code>np.geomspace</code>, and a label that says so.</li>
  <li><b>Labels name the quantity and the unit</b>: "area of the infestation (acres)", not "area".</li>
  <li><b>A title says what to see</b>: "Weekends sell a third more", not "Cups by weekday".</li>
</ul>

{{% note %}}
A chart turns numbers into lengths, positions and slopes, and the eye turns them back. It is honest when the eye gets the right numbers.
{{% /note %}}

***

<p class="dc-kicker">Worked example — notebook 2</p>

## 1.3 million consumer complaints

<div class="dc-grid">
  <div class="dc-card"><h3>Mean 243, median 6</h3><p>Complaints per company, 5,275 companies. The typical company received six complaints in seven years.</p></div>
  <div class="dc-card"><h3>Ten companies</h3><p>received half of all complaints.</p></div>
  <div class="dc-card"><h3>Equal bins: one bar</h3><p>The histogram shows nothing until the axis is logarithmic. Then the shape appears.</p></div>
  <div class="dc-card red"><h3>778 "outliers"</h3><p>hold 96 % of the complaints. They are not errors. <b>They are the subject.</b></p></div>
</div>

{{% note %}}
Published by a financial regulator. Run the notebook on ARC. The fences flag 778 companies; deleting them would delete the analysis.
{{% /note %}}

***

<p class="dc-kicker">Worked example — notebook 2</p>

## Four traps, none of which raises an error

<div class="dc-grid">
  <div class="dc-card red"><h3>1. The axis that hides the data</h3><p>Equal-width bins on heavily skewed counts put nearly everything in the first bar.</p></div>
  <div class="dc-card red"><h3>2. The categories changed</h3><p>"Credit reporting" was renamed partway through. Its complaints are split across two bars, and mortgages look like the top product.</p></div>
  <div class="dc-card red"><h3>3. The incomplete last period</h3><p>The trend line collapses in the final month. The file ends on the tenth.</p></div>
  <div class="dc-card red"><h3>4. Deleting what you have not understood</h3><p>7,052 complaints were forwarded "one day early". Not 7,052 typing mistakes: one cause, such as two systems in different time zones. Decide, and write the count next to the result.</p></div>
</div>

<p class="dc-small" style="margin-top: 16px;">Also in the data: a spike that follows a data breach at a credit bureau, an outlier that is the most informative point on the chart; and a correlation near zero with a clear pattern all the same, since the companies that answer late are small ones.</p>

***

<p class="dc-kicker">To take away</p>

## Key points

<ul class="dc-points">
  <li>Mean and median answer different questions. Compute both; if they differ, say why.</li>
  <li>Know which variance you have: count − 1 in pandas, count in NumPy.</li>
  <li>An outlier is flagged, looked at, and then decided on. Never deleted on sight.</li>
  <li>The same summary numbers can come from very different data. Draw it.</li>
  <li>Name the kind of question, then choose the chart.</li>
  <li>Bars from zero; logarithmic axes announced; labels with units; a title that says what to see.</li>
</ul>

***

<p class="dc-kicker">Now: hands-on</p>

## Over to the notebooks

<p class="dc-small">Folder <a href="https://github.com/molnarai/DataScienceProgramming/tree/main/09-Visualization-Descriptive-Statistics"><code>09-Visualization-Descriptive-Statistics</code></a> — work them in this order:</p>

<div class="dc-grid three">
  <div class="dc-card green"><h3><span class="dc-nb"><span class="num">1</span></span>Numbers and Pictures</h3><p class="dc-from">Concepts</p><p>Centre, spread, outliers, your first figure, and the coffee cart's summer in four charts. Four exercises.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">2</span></span>Consumer Complaints</h3><p class="dc-from">Worked example</p><p>1.3 million records, seven steps, four traps. Run it on ARC.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">3</span></span>Reference</h3><p class="dc-from">Look things up</p><p>Statistics and plotting calls to keep open while you work.</p></div>
</div>

<p class="dc-small" style="margin-top: 20px;">As you work, ask of every figure: <b>would a reader get the right numbers from it?</b><br>Homework: <a href="../../assignments/assignment-08/">Homework 8: Same Numbers, Different Pictures</a></p>
