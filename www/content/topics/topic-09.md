---
date: 2026-10-21
classdates: '2026-10-21'
draft: false
title: 'Visualization and Descriptive Statistics'
theoretical: "Summary statistics and what each one hides. Distribution shape, spread, skew, and outliers. Matching a chart type to a question; honest visual encoding."
technical: "Histograms, bar charts, scatter plots, line plots; mean, median, variance, standard deviation; labeling and saving figures. In-class: compare two variables visually and numerically."
weight: 90
numsession: 9
---
## Theory
Develop summary statistics and visualization as two views of the same question, each covering the other's blind spots. Define mean, median, variance, and standard deviation, and show why the mean and median diverge under skew and why a single number can describe very different distributions identically. Introduce distribution shape, spread, and outliers, and treat an outlier as something to investigate rather than automatically discard. Connect chart type to question type: distribution of one variable, comparison across categories, relationship between two variables, change over time. Discuss honest encoding — truncated axes, misleading aspect ratios, missing labels, and reading correlation in a scatter plot as if it were causation — and establish that a figure without axis labels and units is not yet a result.

## Technical
Produce the four workhorse chart types from Pandas and Matplotlib: histograms for distributions, bar charts for category comparisons, scatter plots for relationships, and line plots for ordered or time-indexed data. Control bin counts and observe how binning changes the apparent shape. Add titles, axis labels, and units on every figure, and save figures to files so they can be committed with an assignment. Compute the same summaries with Pandas (`mean`, `median`, `std`, `quantile`, `describe`) and compare group summaries against the corresponding plot. Show a case where the numbers and the picture disagree and work out why. In-class activity: students compare two variables both visually and numerically and write down what each view adds. Homework: produce plots and descriptive statistics and answer short interpretation prompts.

