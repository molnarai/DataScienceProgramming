---
date: 2026-11-18
classdates: '2026-11-18'
draft: false
title: 'Introductory Machine Learning'
theoretical: "Supervised learning as learning a mapping from features to labels. Classification versus regression; why held-out data is necessary; accuracy, error, and overfitting intuition."
technical: "scikit-learn workflow: prepare features and labels, train/test split, fit, predict, evaluate against a baseline. In-class: train and evaluate a simple model on a toy dataset."
weight: 130
numsession: 13
---
## Theory
Frame supervised learning as fitting a mapping from features to a label using examples where the label is known, and connect it to the tabular data students already handle: columns become features, one column becomes the target. Distinguish classification (a categorical label, scored by accuracy and error rates) from regression (a numeric label, scored by error magnitude). Make the case for held-out data carefully, because it is the central idea of the session: a model evaluated on the data it was trained on can memorize rather than generalize, so its score is not evidence that it works. Develop overfitting intuition through model flexibility — a model complex enough to fit noise will do so — and introduce the train/test split as the minimal defense. Close on interpretation: accuracy is meaningless without a baseline, class imbalance can make a high score worthless, and a model that predicts well still explains nothing about cause.

## Technical
Walk through the scikit-learn workflow end to end on a small dataset: build a feature matrix and a label vector from a DataFrame, split with `train_test_split` using a fixed `random_state`, fit an estimator, predict on the test set, and score the result. Use one classifier and one regressor so both metric families appear, and compare each against a trivial baseline (predict the majority class, predict the mean). Demonstrate the failure directly by scoring on the training set and on the test set and comparing the two numbers. Inspect a confusion matrix to see which cases the classifier actually gets wrong. In-class activity: students train and evaluate a simple model on a toy dataset and report both scores. Homework: fit a basic model, report results, and discuss limitations.

