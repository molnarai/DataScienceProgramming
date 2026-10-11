# Session 8: Python for Data Analysis

Session 7 handed over the tools: NumPy arrays, pandas tables, joins and groups.
This session is about the habits that make those tools give answers you can
trust. A line of pandas always returns a number. Whether the number means
anything is decided before the line is written, by five ideas:

1. **The table is the central structure.** Rows are observations, columns are
   variables.
2. **Vectorized thinking.** Say what happens to a whole column, not to each
   row.
3. **Split, apply, combine.** Every "per something" question has the same three
   steps.
4. **A missing value is a question.** A blank can mean zero, unknown, or not
   applicable, and the three give different numbers.
5. **Inspect before you conclude.** Shape, types, ranges and missingness first.

> **Run these on ARC, with the kernel set to Conda Python 3.12.** Notebook 02
> reads a file under `/data/public/yelp/` that exists only there.

Nothing here repeats Session 7. Choosing rows and columns, joins, reshaping,
dates and ranking within a group are in `../07-Data-Tables/`, and these
notebooks point back to them where they are needed.

## Notebooks

Rename a notebook before you edit it, so that the next course release does not
overwrite your work.

### `01_Thinking_in_Tables.ipynb` — the ideas

An overview of the five ideas on tables small enough to read. A week of farm
deliveries is totalled first with the loop-and-dictionary pattern from Session
3, then as a table, to show what the table lets you stop thinking about. A
million-row timing shows what vectorized code buys. Split, apply, combine is
done by hand once and then with `groupby`, in its three kinds: aggregate,
transform and filter. A tips column that is half empty gives two different
averages, which opens the question of what a blank means and how missing values
behave in sums, comparisons and groups. A last table has four things wrong with
it, all of which five lines of inspection find.

Four exercises, and a table mapping each idea to a phase of Homework 7.

### `02_Yelp_Businesses_Example.ipynb` — one analysis, start to finish

A worked example on 150,346 real records: *do more expensive restaurants get
better ratings?* Seven steps — load a JSON Lines file, inspect it, clean it,
build whole columns, group, look at the blanks, conclude. Along the way the
file turns out to hold empty text where `isna()` sees nothing, a price stored
as text inside a nested dictionary with the word `'None'` for some blanks,
states with four businesses in them, and restaurants whose missing opening
hours predict that they have closed. The first answer changes once thinly
reviewed restaurants are set aside, and the notebook ends with what an honest
statement of the result has to include.

Five exercises on the same data.

### `03_Data_Analysis_Reference.ipynb` — a lookup guide

Meant to be searched, not read through, and to stay open during Homework 7.
Nine sections, each a set of "you want / write this" tables with runnable
examples on one small table: inspecting; types and conversion; missing values
(finding, behaviour, removing, filling, creating, choosing a policy);
whole-column operations; text and date columns; split, apply, combine;
reading and writing CSV and JSON; working style and the warnings you will
meet; and a table translating the loop patterns of Sessions 3 and 4 into
pandas.

## Homework

[Homework 7](../../Assignments/HW07/instructions/homework07_instructions.md)
walks the seven steps of notebook 02 through a different file: the Forest
Service invasive-plants records from Homework 5. The overlap is deliberate.
Each phase uses an idea from notebook 01 and methods listed in notebook 03.
