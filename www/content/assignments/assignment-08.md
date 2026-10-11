+++
date = '2026-10-21'
due_date = '2026-11-04T23:59:00'
draft = false
title = 'Homework 8: Same Numbers, Different Pictures'
weight = 80
status = 'Posted'
+++

Describe the Forest Service file of invasive plants first in a handful of numbers, then in pictures, and find out that each hides things the other shows. The mean size of an infestation is 9.12 acres and the median is 0.114 — both are "the average", and one is 80 times the other. Meanwhile four small datasets share the same means, the same standard deviation, and the same correlation, and look nothing alike once drawn. Across seven test-driven phases you will compute centre and spread from their definitions, find quartiles and flag outliers without removing them, measure correlation, and then draw a histogram, a bar chart, a line, and a scatter plot with matplotlib. You will also write a function that audits any figure for what a reader needs — labels, a title, and bars that start at zero — and save a set of figures from the real data.

<!-- more -->


Related session: [Session 9 — Visualization and Descriptive Statistics](../../topics/topic-09/)

### The Phases

| | |
|---|---|
| **1** | A column in seven numbers — mean, median, variance, standard deviation |
| **2** | Quartiles, fences, and flagging outliers |
| **3** | Two columns and many groups — correlation, and a summary per group |
| **4** | A distribution — a histogram, and when its axis must be logarithmic |
| **5** | A comparison, a trend, a relationship — bars, a line, a scatter plot |
| **6** | A whole figure — small multiples, and an audit of any figure |
| **7** | The set of figures, saved as PNG files |

The chart follows from the question: how the values are spread out, which
group has more, how it changed over time, whether two things go together. And
a rule of thumb marks values for a person to look at; it does not decide what
they are. On the plants file 19 % of the records lie beyond the upper fence,
and they hold 97 % of all the infested acres.

### Topics Covered

- Centre and spread: mean, median, sample variance, standard deviation — and where pandas and numpy disagree on the default
- Quartiles, the interquartile range, and outliers as flags rather than deletions
- Correlation, and what it says nothing about
- Matching a chart type to a question: histogram, bars, line, scatter plot
- Logarithmic axes for skewed data
- Drawing on a matplotlib `Axes`; figures with several Axes and shared ranges
- Honest encoding: labels with units, titles, bars that start at zero
- Saving and closing figures

### Instructions

The full instructions, the starter file, and the per-phase tests are released
through the course template. On the course server run `ifi8410-update`, then
read `Assignments/HW08/instructions/homework08_instructions.md` and work in
`Assignments/HW08/submission/`.

The cleaned plants file is already on the cluster under
`/data/public/usda/us-forest-service/current-invasive-plants/` — do not copy
it — and you do not need to have finished HW07 to use it. The four look-alike
datasets come with the assignment in `data/lookalike.csv`, and a 20-record
copy of the plants file is in `test/fixtures/`. Use pandas, numpy, and
matplotlib, which are already in the course environment. Draw on the `Axes`
you are given and do not call `plt.show()`. Hand in with `ifi8410-test` and
`ifi8410-submit`.
