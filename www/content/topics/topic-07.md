---
date: 2026-10-07
classdates: '2026-10-07'
draft: false
title: 'Data Tables'
concept: "Why business applications store data in related tables rather than one giant table. The grain of a table, primary and foreign keys, and column types; null as unknown, not zero. SQL's declarative, set-oriented philosophy and its roots in Codd's relational model."
practice: "Selection, filtering, sorting, grouping, aggregation, and window calculations side by side in SQL and pandas; inner, left, right, full outer, and cross joins; validating joins against expected cardinality. In-class: answer the same business question in SQL and in pandas and check that the results agree."
weight: 70
numsession: 7
---
Business applications rarely keep their data in one giant table. Customers, orders, order lines, and products each describe a different thing at a different **grain**, so each gets its own table, linked to the others by primary and foreign keys. That design, which Microsoft's Northwind sample database illustrates, avoids repeated and inconsistent copies, and it gives a report its shape: joins build the view a question needs. Reading a table well starts with three questions: what does one row represent, which columns identify it, and what type is each column? Add a fourth: which values are missing? A null means *unknown*, not zero, and SQL and pandas each have their own rules for how nulls behave in filters, counts, and sums.
<!--more-->
With that foundation, the same table operations appear in both SQL and pandas: choosing columns, filtering rows, sorting, grouping and aggregating, and window calculations that compute across related rows while keeping every row visible. Joins get the most attention, because choosing the wrong join type, duplicated or incomplete keys, or a filter placed after a left join can silently drop rows or inflate totals. The habit to build is to predict the row count before running the query and to check it afterwards. The session closes with why SQL looks the way it does: a declarative language, descended from Codd's 1970 relational model, where you describe the result you want and the database decides how to produce it.

{{<figure src="imgs/victorian-database.png" alt="Figure: A Victorian-style illustration of a database" >}}

## Listen

TODO: podcast based on the Tabular Data blog post
{{< podcast src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/podcast/relational_architecture_in_sql_and_pandas.m4a" title="Relational Architecture in SQL and Pandas" >}}


## Presentation

- [Tabular Data](../../slides/slide-07-tabular-data/)

## Read

- [Tabular Data](../../blog/tabular-data/) (source document for podcast)

## Hands-on

Notebooks in [07-Data-Tables](https://github.com/molnarai/DataScienceProgramming/tree/main/07-Data-Tables)

## Homework

- [Homework 6: Data Tables](../../assignments/assignment-06/)
