---
date: 2026-11-18
classdates: '2026-11-18'
draft: false
title: 'Introductory Machine Learning'
concept: "Supervised learning as learning a mapping from features to labels. Classification versus regression; why held-out data is necessary; accuracy, error, and overfitting intuition."
practice: "scikit-learn workflow: prepare features and labels, train/test split, fit, predict, evaluate against a baseline. In-class: train and evaluate a simple model on a toy dataset."
weight: 130
numsession: 13
---
Every program earlier in this course followed a rule that a person wrote. Some rules nobody can write down: which customers are about to cancel, which transactions are fraudulent, which restaurants will have closed by next year. What usually does exist is a record of past cases with their outcomes, and **machine learning** is the idea of handing those examples to a program and letting it find the rule. The table is cut into **features**, what the model may look at, and a **target**, what it should predict. Producing predictions takes three lines of scikit-learn; the problem is everything around them. A model that is wrong raises no error. It prints a number, and the number looks fine. So the most important habit in the subject comes before any learning: put some rows aside as a **test set**, let nothing that is learned or chosen use them, and measure on them once, at the end. Before any model, compute the **baseline** — always answering with the more common class — because "70 % accurate" means little if always saying "no" scores 67 %.
<!--more-->
A **decision tree** predicts by asking yes/no questions about the features, one after another, and a small one can be read and checked against common sense. Let it grow without limit and it gives nearly every training example a verdict of its own: training accuracy only rises, while accuracy on unseen rows rises, stalls, and falls, sometimes below the baseline. That widening gap is **overfitting**, and the depth is chosen on a validation set taken from the training rows, never on the test set. Accuracy also counts mistakes without saying which. The confusion matrix separates false alarms from misses, **precision** and **recall** put numbers on each, and which matters more is a business decision; when the interesting class is rare, accuracy alone is the wrong score. Finally, a model will use any column that helps, including one that would not exist on the day a real prediction is needed. That is **leakage**, and its symptom is a score too good to be true. A model finds what goes together, not what causes what, and it knows only the world it was shown.

TODO: marquee image

## Listen

TODO: podcast

## Presentation

- [Introductory Machine Learning](../../slides/slide-13-intro-machine-learning/)

## Read

- [Introductory Machine Learning](../../blog/intro-machine-learning/) (lecture notes)
- Kelleher, Mac Namee, *D'Arcy Fundamentals of Machine Learning for Predictive Data Analytics*, 2nd Edition, MIT Press, 2020, ISBN-13 978-0262044691. Electronic version available at the [GSU Library](https://library.gsu.edu).

## Hands-on

Notebooks in [13-Intro-Machine-Learning](https://github.com/molnarai/DataScienceProgramming/tree/main/13-Intro-Machine-Learning)

## Homework

- [Homework 12: Does It Beat Guessing?](../../assignments/assignment-12/) — due Wednesday, December 2, 2026
