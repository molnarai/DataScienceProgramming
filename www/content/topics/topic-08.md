---
date: 2026-10-14
classdates: '2026-10-14'
draft: false
title: 'Python for Data Analysis'
theoretical: "Tabular data as a first-class structure. Vectorized thinking versus loops. Split-apply-combine as a model for grouped computation; missing data as a modeling decision."
technical: "NumPy arrays and Pandas DataFrames; loading and inspecting data; selecting, filtering, grouping, aggregating; handling missing values. In-class: explore a small real-world dataset."
weight: 80
numsession: 8
---
## Theory
Introduce the table — rows as observations, columns as variables — as the central data structure of analytics, and contrast it with the lists and dictionaries students have been assembling by hand. Explain vectorized thinking: expressing an operation over a whole column at once instead of looping over elements, which is both more readable and dramatically faster because the work happens in compiled code. Present split-apply-combine as the conceptual model behind grouped computation: partition rows by a key, compute a summary per group, and reassemble the results. Treat missing data as a substantive question rather than a technical nuisance — a blank cell may mean zero, unknown, or not applicable, and dropping versus filling changes what the resulting numbers mean. Close on the habit of inspecting a dataset (shape, types, ranges, missingness) before drawing any conclusion from it.

## Technical
Introduce NumPy arrays and elementwise operations, then move to Pandas as the practical workhorse. Load a CSV into a DataFrame and inspect it with `head`, `shape`, `dtypes`, `info`, and `describe`, diagnosing columns that were read with the wrong type. Select columns and rows, filter with boolean masks and combined conditions, and create derived columns. Group with `groupby` and aggregate with counts, means, and multiple aggregations at once, then sort the result. Detect missing values with `isna` and compare `dropna` and `fillna` on the same question to show that the choice affects the answer. In-class activity: students explore a small real-world dataset and report several grouped summaries. Homework: conduct a basic exploratory data analysis in Python.

