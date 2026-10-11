# Session 7: Data Tables

Until now your data lived in lists and dictionaries, and every question was a
loop. This session introduces the two libraries that the rest of the course
is built on: **NumPy**, for arrays of numbers, and **pandas**, for tables with
named columns. It also introduces the way of thinking that goes with them:

1. **Functions and methods.** Why it is `len(word)` and `word.upper()`. NumPy
   and pandas use both styles constantly, and you need to read both.
2. **Arrays.** Many numbers of one kind, handled all at once: shape, axes,
   slicing, arithmetic on whole arrays, conditions.
3. **Tables.** Rows are observations, columns are variables. Choosing rows and
   columns, sorting, missing values, adding a column.
4. **Grain.** What does one row mean? The first question to ask of any table.
5. **Joining and grouping.** Combining tables through keys, and summarising
   per group.
6. **Position, label, or key.** Every operation pairs values up in one of
   these three ways, and mixing them up is where the surprises come from.

> **Run these on ARC, with the kernel set to Conda Python 3.12.** Notebook 02
> reads CSV files under `/data/public/northwind/` and connects to a database
> server, both of which are reachable only from there.

The reading *Tabular Data* on the course website introduces the table
operations on a four-row example. These notebooks apply them.

## Notebooks

Rename a notebook before you edit it, so that the next course release does not
overwrite your work.

### `01_Intro_Numpy_Pandas.ipynb` — from lists to arrays and tables

Start here. Three parts, each ending in an exercise.

**Functions and methods** explains the dot: methods, attributes, modules, how
to find out what a value can do, and whether a method changes the value or
returns a new one. **NumPy** builds a first array and compares it with a list,
then covers indexing and slicing, summaries, picking values with a condition,
and arrays of two and more dimensions. **pandas** introduces the Series and
the DataFrame: a first look at a table, choosing columns and rows, missing
values, sorting, adding a column, a first taste of grouping, and reading a
table from a CSV file.

### `02_Northwind_SQL_Pandas.ipynb` — one business database, queried two ways

A worked example on Northwind, the sample database of a small food
importer: customers, orders, order lines, products, categories,
employees. Every operation is shown twice, as a **SQL** query sent to a
PostgreSQL database and as the **pandas** version on the CSV files, followed
by a check that both give the same answer.

It covers grain, and why the exported orders file has to be split back into
orders and order lines; selecting, filtering and sorting; joins, including the
same column name in two tables, a left join to find customers who never
ordered, and a self-join; grouping, keeping only the large groups, and
join-then-group; and window calculations such as a rank within each category
and a running total. Four exercises.

The database asks for your ARC user name and password. The notebook shows how
to enter the password without it ending up in the file.

### `03_Array_DataFrame_Operations.ipynb` — a detailed guide to the operations

A slower, closer look at the operations themselves, on a small made-up coffee
company whose numbers you can check in your head. It asks the same four
questions of every operation: what one element or row represents, what the
input shape or grain is, what the output will be, and whether values are
paired by position, by label, or by a join key. You are asked to predict the
shape of a result before running each cell.

**NumPy:** shape and axes, indexing, elementwise arithmetic, broadcasting,
reductions along an axis, reshaping, masks and `np.where`, views and copies.
**pandas:** `.loc` against `.iloc`, automatic alignment on labels and how it
bites, reshaping between wide and long with `melt` and `pivot`, dates with
`shift`, resampling and rolling averages, and categorical and missing values.
Two sets of exercises.

## Homework

[Homework 6](../../Assignments/HW06/instructions/homework06_instructions.md)
audits the Northwind tables and joins them into one view, with pandas on CSV
and JSON files. It uses the pandas half of notebook 02: grain, keys, joins,
join-then-group and ranking within a group. The SQL half is not needed for
it. Two things the homework needs that these notebooks do not spell out,
reading a table from a JSON file and finding rows whose key points at nothing,
are covered in the homework's own guided notebook.

## What comes next

[Session 8](../08-Python-Data-Analysis/) builds on these tools without
repeating them: inspecting and cleaning a real file, whole-column thinking,
split-apply-combine, and what a missing value means.
