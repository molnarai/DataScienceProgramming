# Lecture Notes — Session 9: Visualization and Descriptive Statistics

## 1. The problem

You have a clean table with ten thousand rows. Nobody can read ten thousand
rows. To tell anyone what is in it, you have to **reduce** it, and there are
two ways to do that:

- **a few numbers**: an average, a spread, a correlation;
- **a picture**: a histogram, a bar chart, a scatter plot, a line.

Each loses information, and they lose different information. A summary number
is exact and fits in a sentence, and it hides the shape of the data: two very
different columns can have the same mean. A picture shows the shape, and it
cannot be quoted, and it can mislead through nothing more than the choice of
an axis.

The problem this session addresses is **describing data honestly**: choosing
the number that answers the question actually asked, choosing the chart that
suits the kind of question, and drawing it so that the reader's eye gets the
right impression. "Descriptive" is the important word. Nothing here predicts
or tests anything. It says what is there, which has to come first.

Three failures recur in practice, and the session is organised around
avoiding them:

1. reporting a mean for data where the mean describes almost no one;
2. deleting unusual values because they are unusual;
3. a chart that is technically correct and gives a false impression.

## 2. Core concepts, and how Python realizes them

### The packages

| Package | Purpose | What it gives you |
|---|---|---|
| **pandas** | tables | summary methods on columns (`mean`, `median`, `std`, `quantile`, `describe`, `corr`), and per-group summaries with `groupby` |
| **NumPy** | arrays | the same reductions on arrays; `np.quantile`; `np.geomspace` for logarithmic bins |
| **matplotlib** | drawing | figures and axes; histograms, bars, scatter plots, lines, box plots; full control of labels, scales and layout; saving to PNG, PDF, SVG |

matplotlib is the foundation of plotting in Python. Other libraries (seaborn,
the `.plot` methods of pandas) are conveniences built on top of it, so what
you learn about its figures and axes applies to them as well.

### Concept 1 — Centre: mean and median

Two numbers both called "the average":

- the **mean** is the sum divided by the count;
- the **median** is the middle value once the data is sorted.

```python
salaries.mean()
salaries.median()
```

Nine employees earning between 38 and 60 thousand have a mean of 47.8 and a
median of 47. Add the owner at 400 and the mean jumps to 83, while the median
moves to 48.5. Nine of the ten people now earn less than "the average".

Neither is wrong. They answer different questions:

| Question | Use | Because |
|---|---|---|
| what does a typical one look like? | median | half are below, half above, whatever the extremes do |
| what is the total, spread evenly? | mean | mean × count is the total |

Data with a long tail on one side is **skewed**. Incomes, prices, company
sizes, review counts and waiting times are skewed to the right. Under skew the
mean is pulled toward the tail. A large gap between mean and median is itself
a finding: it tells you the data is skewed before you draw anything.

### Concept 2 — Spread

How far do the values lie from the centre? Two cafés can both have an average
wait of five minutes, one with every customer waiting four to six minutes and
the other with waits from one to ten.

- The **variance** is the typical *squared* distance from the mean.
- The **standard deviation** is its square root, back in the units of the
  data.

```python
waits.var()       # variance
waits.std()       # standard deviation
```

A trap worth knowing by heart: **pandas and NumPy disagree on the default.**
pandas divides by count − 1 (the *sample* variance, appropriate when the data
is a sample of something larger); NumPy divides by count (the *population*
variance). `np.var(x, ddof=1)` makes NumPy agree with pandas. Same data, same
function name, two answers, no warning.

The standard deviation shares the mean's weakness: one extreme value inflates
it. The median has a partner without that weakness. **Quartiles** cut the
sorted data into four equal parts, and the **interquartile range** (IQR) is
the width of the middle half:

```python
q1, q3 = values.quantile(0.25), values.quantile(0.75)
iqr = q3 - q1
values.describe()     # count, mean, std, min, quartiles, max in one call
```

| | Centre | Spread | One extreme value |
|---|---|---|---|
| built on sums | mean | variance, standard deviation | moves both |
| built on order | median | quartiles, IQR | moves neither much |

### Concept 3 — Outliers are questions

A common rule of thumb draws two **fences**, 1.5 interquartile ranges outside
the quartiles, and flags what lies beyond:

```python
outside = (values < q1 - 1.5 * iqr) | (values > q3 + 1.5 * iqr)
```

The result is a column of True and False. Nothing is removed. A flagged value
can be at least three different things:

| It is | Example | Do |
|---|---|---|
| a mistake | a salary typed with an extra zero | correct it or make it missing, and say so |
| a different kind of thing | the owner among the employees | decide whether it belongs to the question |
| the most important row | the customer who brings half the revenue | keep it and report it |

Deleting outliers because they are outliers removes the third kind along with
the first. On skewed data the rule flags a great deal, and the flagged rows
are frequently the subject of the analysis.

### Concept 4 — Two columns: correlation

The **correlation** r measures how closely two columns follow a straight
line: 1 for a perfect rising line, −1 for a falling one, about 0 when a line
says nothing.

```python
table["temperature"].corr(table["cups"])
```

Two cautions. r measures *straight-line* association only: a clear curve can
have r near 0. And it says nothing about cause.

The classic demonstration is **Anscombe's quartet**: four small datasets with
the same means, the same standard deviations and the same correlation (0.82),
which look nothing alike when drawn: a loose cloud, a curve, a line with one
point off it, and a vertical stack with one point that creates the whole
correlation. Sums cannot tell shapes apart. **Always draw the data.**

### Concept 5 — A figure is an object

matplotlib has two things to know:

- a **Figure** is the whole picture: what is shown, and what is saved;
- an **Axes** is one plot inside it, with an x axis and a y axis.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(waits, bins=20)
ax.axvline(waits.mean(), linestyle="--", label="mean")
ax.axvline(waits.median(), linestyle=":", label="median")
ax.set_xlabel("waiting time (minutes)")
ax.set_ylabel("customers")
ax.set_title("A typical wait is four minutes; a few customers wait three times as long")
ax.legend()
fig.savefig("waits.png", dpi=150, bbox_inches="tight")
```

Everything is done by calling methods of the Axes. This is the **object
interface**. Code that calls `plt.hist(...)`, `plt.xlabel(...)` directly uses
a hidden "current Axes", which is fine for one quick plot and breaks down
with two plots or inside a function. The robust pattern is a function that
takes an Axes and draws on it, which can then be placed anywhere:

```python
fig, (left, right) = plt.subplots(1, 2, sharex=True, sharey=True)
draw_waits(left, january)
draw_waits(right, july)
```

`sharex` and `sharey` give panels the same range, which is what makes them
comparable by eye.

In a notebook a figure appears when its cell finishes. In a program there is
no screen: save the figure with `fig.savefig` and release it with
`plt.close(fig)`.

### Concept 6 — The chart follows the question

Decide which kind of question you have before choosing a chart.

| Question | Kind | Chart | Method | Summary number |
|---|---|---|---|---|
| how are the values spread out? | distribution | histogram, box plot | `ax.hist`, `ax.boxplot` | median, quartiles |
| which group has more? | comparison | bars | `ax.bar`, `ax.barh` | one number per group |
| do two things go together? | relationship | scatter plot | `ax.scatter` | correlation |
| how did it change over time? | trend | line | `ax.plot` | change from start to end |

Most bad charts are a good answer to a question nobody asked.

### Concept 7 — Honest pictures

> A figure without axis labels and units is not yet a result.

A chart turns numbers into lengths, positions and slopes, and the reader's
eye turns them back. It is honest when the eye gets the right numbers.

- **Bars start at zero.** A bar shows a number by its length. Cut the axis at
  5,100 and a 7 % difference looks like a factor of four.
- **A line may start anywhere**, because it shows change by its slope. But the
  shape of the frame can make the same rise look gentle or dramatic, so state
  the size of the change in words.
- **Skewed data needs a logarithmic axis**, where each step multiplies by
  ten. The bins must then be evenly spaced on that scale
  (`np.geomspace(low, high, bins + 1)` with `ax.set_xscale("log")`), and the
  label must say the scale is logarithmic.
- **Labels name the quantity and the unit**: "area of the infestation
  (acres)", not "area".
- **A title says what to see**: "Weekends sell a third more", not "Cups by
  weekday".
- **Periods must be complete** in a trend: a last month with ten days of data
  looks like a collapse.
- **Categories must mean the same thing throughout**: a renamed category
  splits one bar into two smaller ones.

## 3. Business use cases

**What does this company pay?** A firm of ten reports an average salary of
83 thousand. Nine of the ten earn under 60. For a job applicant the median is
the honest number; for the payroll budget the mean is. The same data, two
correct answers, and the report should say which question it is answering.

**How long do customers wait?** A café measures 200 waiting times. The
histogram shows most customers served within five minutes and a tail out to
fifteen. The mean sits to the right of the median, pulled by the tail. For
staffing, the tail is the interesting part: it is where complaints come from,
and an average hides it.

**A coffee cart's summer.** Eighty-four days of records: date, temperature,
cups sold. One table answers four kinds of question, each with its chart: how
many cups on a usual day (a histogram), which weekday sells most (bars, in
weekday order), whether cold days sell more (a scatter plot with r), and
whether sales grew over the summer (a line, with a seven-day rolling mean to
see through the weekly zigzag).

**Who gets complained about?** A financial regulator publishes 1.3 million
consumer complaints against 5,275 companies. The mean number of complaints
per company is 243 and the median is 6: the typical company received six
complaints in seven years, and ten companies received half of all complaints.
A histogram with equal bins shows a single bar; on a logarithmic axis the
shape appears. The outlier rule flags 778 companies, which together account
for 96 % of the complaints: they are not errors, they are the subject.

The same data sets several traps, none of which raises an error:

- a bar chart ranks mortgages as the most complained-about product, because
  the "credit reporting" category was renamed partway through and its
  complaints are split across two bars;
- a trend line collapses in the final month, because the file ends on the
  tenth of that month;
- a spike in one month turns out to follow a major data breach at a credit
  bureau: an outlier that is the most informative point on the chart;
- a scatter plot of company size against the share of complaints answered on
  time has a correlation near zero, and a clear pattern all the same: the
  companies that answer late are small ones.

**Field data for a public agency.** Areas of plant infestations range from a
fraction of an acre to thousands of acres. The mean area is eighty times the
median. Reporting "the average infestation is nine acres" would describe
almost none of them; "half are smaller than about a tenth of an acre, and the
largest fifth hold nearly all of the infested land" describes the situation
and tells a manager where to look.

## Key points

- Mean and median answer different questions. Compute both; if they differ,
  say why.
- Know which variance you have: count − 1 in pandas, count in NumPy.
- An outlier is flagged, looked at, and then decided on. Never deleted on
  sight.
- The same summary numbers can come from very different data. Draw it.
- Name the kind of question, then choose the chart.
- Bars from zero; logarithmic axes announced; labels with units; a title that
  says what to see.
