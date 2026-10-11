# Session 9: Visualization and Descriptive Statistics

Session 8 ended with a clean table. This session describes one: in a few
numbers, and in a picture. They are two views of the same question, and each
covers the other's blind spots. A summary number hides the shape of the data;
a picture shows the shape and cannot be put in a sentence.

1. **Centre.** The mean and the median answer different questions, and under
   skew they give different answers.
2. **Spread.** Variance, standard deviation and the interquartile range.
3. **Outliers.** A value far from the rest is something to investigate, not a
   row to delete.
4. **The figure as an object.** A Figure holds Axes, and you draw by calling
   methods of the Axes.
5. **The chart follows the question.** Distribution, comparison,
   relationship, trend.
6. **Honest pictures.** A figure without axis labels and units is not yet a
   result, and an axis can mislead.

> **Run these on ARC, with the kernel set to Conda Python 3.12.** Notebook 02
> reads a file under `/data/public/ConsumerComplaintDatabase/` that exists
> only there.

Nothing here repeats Sessions 7 and 8. Loading, cleaning, missing values and
`groupby` are in `../08-Python-Data-Analysis/`; selecting, joining and dates
are in `../07-Data-Tables/`. These notebooks use them and point back.

## Notebooks

Rename a notebook before you edit it, so that the next course release does not
overwrite your work.

### `01_Numbers_and_Pictures.ipynb` — the ideas

An overview of the six ideas on data small enough to read. Ten salaries show
what one large value does to the mean and what it does not do to the median.
Two cafés with the same average wait introduce spread, the variance is worked
out by hand, and pandas and numpy turn out to disagree about it. Fences flag a
value without removing it. The first figure is built up from a bare histogram
to a labelled result, with matplotlib's object interface (`fig, ax =
plt.subplots()`) and a function that takes an Axes. One table of a coffee
cart's summer answers four kinds of question with four charts. Anscombe's four
datasets have the same means, standard deviations and correlation, and look
nothing alike. The last part draws the same numbers honestly and dishonestly.

Four exercises, and a table mapping each idea to a phase of Homework 8.

### `02_Consumer_Complaints_Example.ipynb` — one dataset, start to finish

A worked example on 1,282,355 real records: the complaints about financial
products published by the U.S. Consumer Financial Protection Bureau from 2011
to 2019. *Who gets complained about, about what, and is it getting worse?*
The median company received 6 complaints and the mean is 243. Along the way
four charts look fine and say something false: a histogram with one bar, a
bar chart that ranks mortgages first because a category was renamed in 2017, a
trend line that collapses in a month the file only half covers, and 7,052
complaints forwarded the day before they arrived. A spike in September 2017
turns out to be the most interesting point in the data. The notebook ends with
one figure of four Axes and what an honest statement of the result includes.

Five exercises on the same data.

### `03_Statistics_and_Plotting_Reference.ipynb` — a lookup guide

Meant to be searched, not read through, and to stay open during Homework 8.
Thirteen sections of "you want / write this" tables with runnable examples on
one small table: summary numbers (and which variance each library computes);
quantiles, fences and flags; summaries per group; correlation and the index
trap; making a figure; one chart per kind of question (histogram, bars,
scatter, line, box plot); labels, legends and text; scales, limits and ticks;
colours and markers; saving and closing; asking an Axes what is drawn on it;
the pandas `.plot` shortcut; and a checklist with the error messages you will
meet and a table translating `plt.` code into the object interface.

## Homework

[Homework 8](../../Assignments/HW08/instructions/homework08_instructions.md)
asks the four kinds of question of the invasive-plants data from Homework 7,
and has you draw Anscombe's four datasets with your own functions. The overlap
with these notebooks is deliberate. Each phase uses an idea from notebook 01
and methods listed in notebook 03.
