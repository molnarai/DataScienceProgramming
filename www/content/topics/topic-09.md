---
date: 2026-10-21
classdates: '2026-10-21'
draft: false
title: 'Model Selection & Large-Scale Experiments'
theoretical: "Bias-variance and model capacity under compute limits. Hyperparameter tuning (grid, random, simple adaptive methods) and overfitting to validation sets with many experiments."
technical: "Implement improved methods per track (ALS or advanced recsys, graph-based segmentation, richer forecasting models). Collect side-by-side metrics vs baselines and log experiments."
weight: 90
numsession: 9
---
## Theory
Revisit bias variance and model capacity, now constrained by computational budgets. Discuss hyperparameter tuning strategies (grid search, random search, simple adaptive methods) and why exhaustive hyperparameter sweeps may be impossible at scale. Cover the risk of “metric hacking” when repeatedly probing the same validation set across many runs, even with large data. Emphasize strategies for responsible model selection: limited sweeps, early stopping, and pre-defined evaluation protocols. Use examples from recommenders, segmentation, and forecasting where small hyperparameter tweaks may or may not justify heavy compute.

## Technical
Technical focus on implementing improved models per project track. For recommenders: implementing ALS or more sophisticated models in Spark ML; for graphs: implementing a community-detection or graph-based segmentation pipeline; for forecasting: building richer models or engineered feature sets in Spark ML. In-class: teams work on their improved approaches, run them on a subset of data, and start collecting side-by-side metrics versus baselines (both technical and quality). Emphasis on logging experiments in MLflow so results are reproducible and comparable.

