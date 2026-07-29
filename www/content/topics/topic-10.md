---
date: 2026-10-28
classdates: '2026-10-28'
draft: false
title: 'Optimization & Iterative Algorithms'
theoretical: "Conceptual overview of gradient descent, SGD, mini-batching, and scalability. Data vs model parallelism; how optimization choices interact with distributed systems and iterative algorithms (e.g., ALS, PageRank)."
technical: "Workflow orchestration: DAGs, scheduling, retries, logging. In-class: design and, where feasible, implement DAGs that run ETL and modeling pipelines on a schedule."
weight: 100
numsession: 10
---
## Theory
Provide a conceptual overview of gradient-based optimization: gradient descent, stochastic gradient descent, and mini-batching. Explain why full-batch methods become impractical with very large datasets, and how stochastic/mini-batch approaches trade variance for speed. Introduce data parallelism vs model parallelism and the idea of parameter servers/asynchronous updates (conceptually, not implementation-level). Connect these ideas back to specific algorithms used in the course (e.g., ALS vs SGD for factorization, iterative graph algorithms like PageRank). Emphasize that in practice, “good enough, fast” often wins over theoretically optimal but slow solutions.

## Technical
Technical introduction to orchestration and automation with Airflow (or similar tooling). Explain DAG concepts, scheduling, retries, and logging. Show how to wrap Spark ETL and model-training steps into a workflow graph that can be triggered regularly. In-class: teams draft and, where possible, implement a simple DAG that runs at least their ETL and baseline or improved model pipelines. They think through what a daily or weekly production run would look like, including data refresh and model retraining steps.

