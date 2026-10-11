---
date: 2026-10-14
classdates: '2026-10-14'
draft: false
title: 'Python for Data Analysis'
concept: "Tabular data as a first-class structure. Vectorized thinking versus loops. Split-apply-combine as a model for grouped computation; missing data as a modeling decision."
practice: "NumPy arrays and Pandas DataFrames; loading and inspecting data; selecting, filtering, grouping, aggregating; handling missing values. In-class: explore a small real-world dataset."
weight: 80
numsession: 8
---
With pandas, most questions about a table are one line of code, and that line **always returns a number**. It does not know whether the file had blank cells, whether a price was stored as the word `"None"`, whether a date of 1 January 1900 was real or a placeholder, or whether half of one group's records were missing. It computes anyway, and a wrong answer looks exactly like a right one. So data analysis is less about the computing line than about what comes before it: what one row stands for (the **grain**), what types the columns have, which values are wrong, disguised, or impossible, and what a blank means — zero, unknown, or not applicable. Those three readings can put an average a factor of two apart, and no error message raises the question for you.
<!--more-->
Two ideas then carry the computing itself. **Vectorized thinking** says what happens to a whole column, not to each row: `amount = boxes * price` applies to every row at once, in compiled code, and reads like the sentence it implements. **Split, apply, combine** is the shape of every question with the word *per* in it, and `groupby` does all three steps; the skill is choosing between an aggregate, which shrinks the table to one row per group, and a transform, which keeps every row and puts the group's value beside it. Around both sits the habit the session is built on: inspect first — shape, types, a few rows, blanks, ranges, distinct values — clean with a short list of explicit rules that make a value missing but never delete a row silently, and report what was left out, with counts.

TODO: marquee image

## Listen

TODO: podcast

## Presentation

- [Python for Data Analysis](../../slides/slide-08-python-data-analysis/)

## Read

- [Python for Data Analysis](../../blog/python-data-analysis/) (lecture notes)

## Hands-on

Notebooks in [08-Python-Data-Analysis](https://github.com/molnarai/DataScienceProgramming/tree/main/08-Python-Data-Analysis)

## Homework

- [Homework 7: Invasive Plants, from Raw File to Report](../../assignments/assignment-07/) — due Wednesday, October 28, 2026
