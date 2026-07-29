---
date: 2026-10-07
classdates: '2026-10-07'
draft: false
title: 'Communities, Triangles & Structure'
theoretical: "Community detection objectives (modularity, conductance) and heuristic algorithms (e.g., Louvain). Triangle counting and clustering coefficients as measures of local graph structure at scale."
technical: "Experiment tracking and ML lifecycle: integrate run tracking (e.g., MLflow-like tooling) into pipelines. In-class: log baseline runs, metrics, and configurations in preparation for improved models."
weight: 70
numsession: 7
---
## Theory
Dive deeper into graph algorithms for segmentation. Introduce community detection objectives (modularity, conductance) and explain heuristic algorithms like Louvain/Leiden that optimize modularity in a multi-level fashion. Provide an intuitive overview of spectral clustering and the graph Laplacian (no heavy proofs, but clear conceptual links to partitioning). Introduce triangle counting and clustering coefficients as measures of local transitivity and “tight-knit” neighborhoods. Discuss how these metrics help characterize communities in product or customer graphs, and the challenges of counting triangles in large, skewed graphs (approximate methods, wedge sampling, special handling of high-degree nodes).

## Technical
Technical introduction to experiment tracking and the ML lifecycle. Show how to integrate MLflow (or similar tooling) into Spark workflows to log parameters, metrics, and artifacts for each run. Demonstrate how to compare baseline runs, track configurations, and manage results across the cluster. In-class: teams add run tracking to their baseline pipelines and set up a basic experiment structure (run naming, tags, logging of both quality and technical metrics). They prepare the scaffolding needed for comparing improved models later.

