---
date: 2026-09-09
classdates: '2026-09-09'
draft: false
title: 'Recommenders & Frequent Patterns'
theoretical: "Large, sparse user-item matrices; non-personalized recommenders; co-occurrence similarity. Frequent itemset mining (FP-growth), association rules, and scaling issues on massive transaction logs."
technical: "Spark fundamentals on ARC: DataFrames, basic transforms, job submission. In-class: set up repos, connect to cluster, and load project data with simple counts and aggregates."
weight: 30
numsession: 3
---
## Theory
Introduce recommender systems as large, sparse matrix problems. Cover non-personalized methods (global popularity, item popularity within segments) and simple item item similarity from co-occurrence. Explain frequent itemset mining for market-basket analysis: definition of support, confidence, and association rules. Present FP-growth: how FP-trees compress transaction databases and avoid candidate explosion, and why it scales better than Apriori. Discuss scaling issues: building FP-trees per partition, memory limits, pruning by minimum support, and how these patterns can be used to derive item item edges or candidate sets in large retail systems. Include quick exercises on computing supports and small FP-trees.

## Technical
Technical introduction to Spark on the ARC cluster. Show how to submit simple Spark jobs via Slurm, how to inspect logs, and how to access data on CubeFS. Hands-on demo: load one of the course datasets with Spark DataFrames, perform simple filters, projections, and aggregations. Teams set up project repositories, connect to the cluster, and implement a minimal Spark script/notebook that reads their chosen dataset and prints basic statistics (row counts, distinct users/items, time spans).

