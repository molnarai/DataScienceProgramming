---
date: 2026-10-14
classdates: '2026-10-14'
draft: false
title: 'Parallel ETL & Distributed Patterns'
theoretical: "Map-shuffle-reduce patterns; communication vs computation costs; partitioning strategies and skew. Algorithmic thinking for scalable ETL and aggregations."
technical: "Spark performance tuning: Spark UI, stages/shuffles, partitioning, caching, broadcast joins, skew mitigation. In-class: profile ETL/baseline pipelines, apply at least one optimization, and record before/after performance."
weight: 80
numsession: 8
---
## Theory
Explore algorithmic patterns behind ETL and large-scale analytics: map, shuffle, reduce, join, and dataflow graphs. Discuss complexity at the distributed level: computation cost vs communication cost, with shuffles as a key source of overhead. Analyze how different partitioning strategies (hash, range, custom keys) affect load balance and skew, especially in retail logs with heavy-tailed popularity distributions. Show how naive implementations of aggregations and joins become bottlenecks, and how to reason about more efficient algorithms. Include exercises where students choose partition keys and sketch map reduce decompositions for concrete ETL tasks.

## Technical
Technical deep dive into Spark performance and debugging on the ARC cluster. Walk through Spark UI: stages, tasks, shuffles, storage levels, and common performance anti-patterns. Demonstrate tuning options: partitioning, caching, broadcast joins, and skew mitigation techniques. In-class: teams profile their baseline pipelines on a moderate subset of data, identify bottlenecks, and apply at least one optimization (e.g., better partitioning strategy or caching). They record before/after performance numbers in preparation for discussing technical improvements alongside model improvements.

