---
date: 2026-09-16
classdates: '2026-09-16'
draft: false
title: 'Graph Basics & Connectivity'
theoretical: "Graphs in retail (product co-purchase, user-item graphs); degree, neighborhoods, connected components. Challenges of storing and processing large graphs in distributed environments."
technical: "Data modeling and ETL design: profiling, cleaning, layered tables (raw/clean/feature). In-class: design schema and implement first Spark ETL that produces cleaned data."
weight: 40
numsession: 4
---
## Theory
Define graphs formally (nodes, edges, weighted/unweighted, directed/undirected) with examples from retail: product co-purchase graphs, user item bipartite graphs. Introduce degree, paths, and neighborhoods (ego-nets) as a way to analyze local structure. Cover connected components (weak/strong) and their interpretation in co-purchase or social graphs (e.g., isolated subgraphs vs a giant component). Discuss the computational challenges of processing large graphs: storing adjacency information across partitions, iteratively propagating labels (for components), and the difference between small networkx-style analyses and cluster-scale graph processing. Use small toy graphs for cut/degree/component quizzes.

## Technical
Technical deep dive into data modeling and ETL design in Spark. Cover practical data profiling and quality checks (missing values, outliers, inconsistent keys) on large tables. Introduce layered data architecture (raw/staging *cleaned* feature tables) and idempotent ETL design. In-class lab: teams explore schemas, identify key tables for their project, and sketch a target data model (tables/views needed for training and evaluation). Begin implementing a first ETL pipeline in Spark that reads raw data and writes a cleaned/normalized version to a curated location.


