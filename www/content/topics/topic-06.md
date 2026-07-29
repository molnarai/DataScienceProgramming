---
date: 2026-09-30
classdates: '2026-09-30'
draft: false
title: 'Factorization & Sequential Patterns'
theoretical: "Matrix factorization for recommenders (ALS-style objectives, regularization, implicit feedback) and why ALS is attractive at scale. Sequential pattern mining (PrefixSpan) and its use for session/sequence behavior on large logs."
technical: "Implement and evaluate baselines for each project (simple recsys, basic graph segmentation, naive forecasts). Compute quality metrics and record initial technical metrics."
weight: 60
numsession: 6
---
## Theory
Present low-rank matrix factorization for recommenders: representing user item interaction matrices as products of user and item latent factor matrices. Explain ALS-style objectives for implicit and explicit feedback, regularization, and how alternating optimization lends itself to distributed implementations (solving for user factors given item factors and vice versa). Discuss trade-offs between ALS and SGD at scale (synchronization, convergence, fault tolerance). Introduce sequential pattern mining via PrefixSpan: frequent subsequences, prefix-projected databases, and why PrefixSpan reduces database scans compared to older methods. Emphasize scaling issues: pattern explosion and the need for minimum support, maximum pattern length, and parallel prefix projections. Show how sequential patterns can inform next-item recommendation and session-level behavior modeling.

## Technical
Technical work on baselines and evaluation metrics. Walk through coding of simple baselines for each project type in Spark (popularity or simple co-occurrence for recommenders, basic clustering or heuristics for graphs, naive or moving-average forecasts). Demonstrate how to compute quality metrics at scale (precision@k, modularity proxies, RMSE/MAPE) and how to efficiently compute them without repeated full-table scans. In-class: teams implement or refine their baseline models, compute first quality metrics on held-out data, and start systematically recording simple technical metrics such as runtimes and dataset sizes.

