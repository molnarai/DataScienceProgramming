---
date: 2026-11-04
classdates: '2026-11-04'
draft: false
title: 'Robustness, Drift & Monitoring'
theoretical: "Robustness to noise, outliers, and missing data in large logs. Covariate shift and concept drift; what to monitor (distributions, metrics) over time with limited compute."
technical: "Testing, CI/CD, and reliability: schema and data checks, ML sanity tests, simple CI flows. Teams add tests and document a CI/CD-style deployment and monitoring plan."
weight: 110
numsession: 11
---
## Theory
Discuss robustness and uncertainty in large-scale systems: impact of noisy labels, missing data, and outliers when logs are huge but not perfectly clean. Introduce covariate shift and concept drift with examples from retail (seasonality, changing customer behavior, product additions). Cover monitoring concepts from a theoretical perspective: what to track (distributional changes, performance on holdout slices), how to construct 'cheap checks' (schema checks, basic distribution checks) versus more detailed periodic evaluations. Emphasize that even with big data, computational limits constrain how often and how deeply models can be monitored.

## Technical
Technical focus on testing, CI/CD, and reliability practices for data and ML pipelines. Show examples of basic tests for ETL (schema validation, row-count expectations, null checks) and for ML (sanity checks on metrics, simple invariants). Demonstrate how to integrate tests into a simple CI pipeline (e.g., running checks on every commit, or nightly). In-class: teams add tests or validation steps to their projects, plan a CI/CD-style workflow, and document how their system would behave in a production-like environment (including monitoring and retraining triggers).

