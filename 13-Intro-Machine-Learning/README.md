# Session 13: Introductory Machine Learning

Every program so far followed rules that you wrote. This session is about
programs that are given examples and find a rule themselves. Getting such a
program to produce predictions takes three lines. The work, and this session,
is in the question that comes after: are the predictions any good, and how
would you know?

1. **Features and target.** A model learns to predict one column from the
   others.
2. **Train and test.** A model is measured on examples it has not seen, or not
   at all.
3. **The baseline.** Before any model: how good is the simplest possible
   guess?
4. **A decision tree.** A model that asks yes/no questions, chosen from the
   training examples.
5. **Overfitting.** A model can learn its examples by heart and get worse at
   everything else.
6. **Beyond accuracy.** Which mistakes it makes matters as much as how many.

> **Run these on ARC, with the kernel set to Conda Python 3.12.** Notebook 02
> reads a file under `/data/public/ConsumerComplaintDatabase/` that exists
> only there.

Nothing here repeats earlier sessions. Tables and missing values are Session
8, plots Session 9, and seeds and run-to-run variation Session 10; all three
are used throughout.

## Notebooks

Rename a notebook before you edit it, so that the next course release does not
overwrite your work.

### `01_Learning_from_Examples.ipynb` — the ideas

An overview of the six ideas on a year of made-up coffee-cart days: will
tomorrow be busy? A tree scored on the days it learned from looks nearly
perfect, and on days put aside it is right two times in three; that gap is the
reason for a test set. Always answering "quiet" is right 57 % of the time,
which is the number every model has to beat. A tree with one question is found
by trying every threshold by hand, then scikit-learn does the same search, and
the tree is printed and read. Drawn on the plane, a small tree shades one
broad region and an unlimited one a bar code, which is what overfitting looks
like. The depth is chosen on a validation set, not on the test set. A
confusion matrix then shows which mistakes the model makes, and the notebook
ends with three things a model is not.

Four exercises, and a table mapping each idea to a phase of Homework 12.

### `02_Late_Answers_Example.ipynb` — one problem, start to finish

A worked example on the 1,282,355 consumer complaints of Session 9: which ones
will the company answer late? One in forty is, so always saying "on time" is
97.5 % accurate. The first tree is 97.5 % accurate too, and finds none of the
late ones. A second scores perfect precision by reading a column that is
written after the outcome, and has to be thrown away. A feature built with
care, each company's past share of late answers taken from the training rows
only, turns a model that does nothing into one that finds three late answers
in ten with seven alarms in ten real, while the accuracy moves by half a
point. Tested on the two years after its training data, its precision drops.
Six traps, none of which raised an error.

Five exercises on the same data.

### `03_Machine_Learning_Reference.ipynb` — a lookup guide

Meant to be searched, not read through, and to stay open during Homework 12.
Twelve sections with runnable examples on 500 made-up restaurants: the
vocabulary; features and target; turning missing values, True/False and
categories into numbers; splitting by hand, with scikit-learn, stratified and
by time; the baseline; the four steps every model shares; decision trees and
how to read one; the confusion matrix with accuracy, precision and recall, and
scikit-learn's layout of it; overfitting, validation and cross-validation; a
leakage checklist; what to report; and a table of error messages and scores
that look wrong.

## Homework

[Homework 12](../../Assignments/HW12/instructions/homework12_instructions.md)
predicts which Yelp restaurants have closed. A third have, so the baseline is
67 %; a tree of depth 6 reaches 72 % on restaurants it has not seen; and a
tree of depth 30 scores 99 % on its training restaurants and 65 % on new ones,
below the baseline. You write the split, the baseline and the scores yourself
and use scikit-learn for the tree. The overlap with these notebooks is
deliberate.
