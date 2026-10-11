+++
date = '2026-11-18'
due_date = '2026-12-02T23:59:00'
draft = false
title = 'Homework 12: Does It Beat Guessing?'
weight = 120
status = 'Scheduled'
+++

A third of the restaurants in the Yelp data have closed. From what is known about a restaurant — its rating, its number of reviews, its price level, whether it lists opening hours — can a program learn to tell the ones that close from the ones that stay open? Getting a model to produce predictions takes three lines; this assignment is about the question that matters afterwards: are the predictions any good, and compared with what? Across six test-driven phases you will turn a table into features and a target, put a share of the rows aside for testing, compute the baseline that any model has to beat, count the four kinds of right and wrong prediction, and train decision trees of increasing depth with scikit-learn. A tree allowed 30 questions is right on 98.9 % of the restaurants it studied and on 64.9 % of the ones it has not seen — worse than always saying "open".

<!-- more -->


Related session: [Session 13 — Introductory Machine Learning](../../topics/topic-13/)

### The Phases

| | |
|---|---|
| **1** | Features and target — numbers a model can use |
| **2** | Put some rows aside — the train/test split |
| **3** | The guess to beat — the baseline |
| **4** | Right and wrong, in four kinds — accuracy, precision, recall |
| **5** | A tree, and how deep to grow it |
| **6** | Choosing honestly, and the report |

The test part is looked at once. Nothing that is learned or chosen — the
majority class, the tree, the depth of the tree — may use the test rows,
because a measurement you have tuned towards is no longer a measurement. So
the depth is chosen on a validation part taken from the training rows, and the
tests check that the test rows stayed out of it.

### Topics Covered

- Supervised learning: features, a target, and learning from examples
- Encoding missing values and categories as numbers; one-hot encoding
- Leakage: the answer hiding among the features
- Training and test parts, and why the split is shuffled and seeded
- The majority-class baseline
- The confusion matrix; accuracy, precision, and recall
- Decision trees with scikit-learn, and overfitting as depth grows
- Choosing a model on validation rows, not on test rows

### Instructions

The full instructions, the starter file, and the per-phase tests are released
through the course template after the November 18 session. Once they are
out, run `ifi8410-update` on the course server, then read
`Assignments/HW12/instructions/homework12_instructions.md` and work in
`Assignments/HW12/submission/`.

The Yelp business file is already on the cluster; the 600 made-up restaurants
in `test/fixtures/restaurants.csv` have the same columns, and every phase is
tested on them. Use pandas, numpy, and scikit-learn, which are already in the
course environment — but write the split and the scores yourself, and take
only `DecisionTreeClassifier` from scikit-learn. Hand in with `ifi8410-test`
and `ifi8410-submit`.
