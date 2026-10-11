---
date: 2026-10-21
classdates: '2026-10-21'
draft: false
title: 'Visualization and Descriptive Statistics'
concept: "Summary statistics and what each one hides. Distribution shape, spread, skew, and outliers. Matching a chart type to a question; honest visual encoding."
practice: "Histograms, bar charts, scatter plots, line plots; mean, median, variance, standard deviation; labeling and saving figures. In-class: compare two variables visually and numerically."
weight: 90
numsession: 9
---
Nobody can read ten thousand rows. To tell anyone what is in a table you have to reduce it, either to a few numbers or to a picture, and each loses different information. A summary number is exact and fits in a sentence, and it hides the shape of the data: the **mean** and the **median** are both called "the average", and under skew — incomes, prices, review counts, waiting times — they can be far apart, because one extreme value moves the mean and leaves the median where it was. The same split runs through spread: variance and standard deviation are built on sums and inflated by extremes, quartiles and the interquartile range are built on order and are not. An **outlier** is a question, not an error. It may be a mistake, a different kind of thing, or the most important row in the table, so it is flagged, looked at, and then decided on — never deleted on sight.
<!--more-->
A picture shows what the numbers cannot. Anscombe's quartet is four small datasets with the same means, the same standard deviations, and the same correlation that look nothing alike when drawn, which is why you always draw the data. The chart follows from the kind of question: a histogram for how values are spread out, bars for which group has more, a scatter plot for whether two things go together, a line for how something changed over time. In matplotlib a Figure is the whole picture and an Axes is one plot inside it, and functions that draw on an Axes they are given can be placed anywhere. A chart is honest when the eye gets the right numbers: bars start at zero, a logarithmic axis is announced, labels name the quantity and its unit, periods in a trend are complete, and the title says what to see. A figure without axis labels and units is not yet a result.

{{<figure src="imgs/Describing_Data_Honestly_Guide.png" alt="Figure: Infographic depicting analysis and visualization techniques" >}}

## Listen

{{< podcast src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/podcast/how_summary_statistics_misrepresent_data.m4a" title="Visualizing Data and Descriptive Statistics" >}}


## Presentation

- [Visualization and Descriptive Statistics](../../slides/slide-09-visualization-descriptive-statistics/)

## Read

- [Visualization and Descriptive Statistics](../../blog/visualization-descriptive-statistics/) (lecture notes)

## Hands-on

Notebooks in [09-Visualization-Descriptive-Statistics](https://github.com/molnarai/DataScienceProgramming/tree/main/09-Visualization-Descriptive-Statistics)

## Homework

- [Homework 8: Same Numbers, Different Pictures](../../assignments/assignment-08/) — due Wednesday, November 4, 2026
