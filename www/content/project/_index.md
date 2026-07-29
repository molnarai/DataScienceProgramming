---
title: Project
description: "The course projects comprise a curated set of retail analytics problems designed with consistent scope, data scale, and technical rigor, forming the primary analytical work of the course. Each project follows a structured sequence of milestones that guide the development of an end‑to‑end scalable data analytics system, beginning with data understanding and ETL/ELT pipeline construction and progressing through baseline and improved modeling, systematic evaluation of analytical quality and system performance, and comprehensive reporting. Projects are developed and versioned using the internal GitLab repository and executed on the ARC to ensure reproducibility in a realistic computing environment. The milestone sequence culminates in a final report and presentation, producing a polished technical artifact suitable for inclusion in a professional portfolio."
layout: "project"
---
<!-- **[Guidelines for Final Project Presentation](project-final-presentation/)** -->

<!-- **Project Assignment: Building an AI-Powered Business Solution** -->

Choose one of three project options: a retail recommender system, graph-based retail segmentation, or retail demand forecasting.
Each project must include a reproducible ETL or ELT pipeline, run on the course Spark environment, and include quantitative evaluations of both technical performance and output quality.

All teams should start by building a clear baseline system, then improve on it and report measured changes in system performance and solution quality. Technical metrics may include runtime, memory usage, storage footprint, and other Spark execution characteristics. Quality metrics depend on the project type and should be clearly justified in the final report.

Teams may have one to three students. The same guidelines and deliverables apply to all teams. Smaller teams can narrow the scope of their experiments, but they must still complete the full ETL, baseline, improvement, and evaluation process.

## Project 1: Retail recommender system

### Goal

Build a Spark-based retail recommender system using the course-provided interaction and product data. The project should model how a retailer can recommend products to users or predict useful item-to-item suggestions using a reproducible data pipeline.

### Data

The provided dataset will include user interaction or transaction records plus product metadata such as item identifiers, categories, and attributes. Similar public recommender datasets often combine event logs with catalog information so students can build both simple and personalized recommendation pipelines.

### Required work

- Create an ETL pipeline that cleans raw data, resolves missing or inconsistent fields, joins events to item metadata, and produces training, validation, and test datasets.
- Implement a baseline recommender, such as popularity ranking, co-occurrence, or another simple non-personalized method.
- Implement an improved recommender, such as collaborative filtering with Spark ALS, improved candidate generation, or stronger feature engineering.
- Track and compare technical metrics for the baseline and improved systems, including end-to-end runtime and resource use.
- Track and compare quality metrics such as `precision@k`, `recall@k`, `hit rate`, or `NDCG` on held-out data.

### Deliverables

The final submission must include ETL workflow artifacts, code, experiment logs, a written report, and a short presentation. The final analysis must explain whether the improved recommender achieved better recommendation quality, what technical cost that improvement required, and whether the trade-off is justified for a retail setting.

## Project 2: Graph-based retail segmentation

### Goal

Build a Spark-based graph analytics pipeline for retail segmentation using the course-provided data. The project should convert retail interactions into a graph structure and use graph algorithms or graph-informed methods to discover meaningful product groups or customer segments.

### Data

The provided dataset will support graph construction from retail behavior, such as co-purchase links between products or interaction-based relationships among customers and products. Public co-purchase and recommender datasets commonly support this kind of graph derivation because transactions naturally induce item-item and user-item networks.

### Required work

- Create an ETL pipeline that transforms the raw retail data into a clean graph representation, such as an edge list and node attributes.
- Implement a baseline segmentation approach, such as feature-based clustering or a simple threshold-based grouping method.
- Implement an improved graph-based approach, such as community detection, label propagation, spectral methods, or another justified graph segmentation technique.
- Measure technical performance, including runtime, memory use, storage footprint, and any graph-processing bottlenecks.
- Measure segmentation quality using metrics such as modularity, cohesion/separation, cluster interpretability, or a justified downstream business metric.

### Deliverables

The final submission must include the graph-building ETL workflow, code, experiment tracking, a written report, and a short presentation. The report must compare the baseline and improved segmentation methods and explain how graph structure changed both technical performance and segmentation quality.



## Project 3: Retail demand forecasting

### Goal

Build a Spark-based retail demand forecasting pipeline using the course-provided time-series sales data. The project should represent a realistic analytics workflow in which a retailer prepares operational data and predicts future demand for products, stores, or product-store combinations.

### Data

The provided dataset will include historical retail sales over time, and may also include calendar, promotion, holiday, or product attributes. Public retail forecasting datasets typically combine transactional or aggregated sales with contextual information so students can compare simple baselines with richer predictive models.

### Required work

- Create an ETL pipeline that cleans raw sales data and produces analysis-ready time-series tables for modeling.
- Implement a baseline forecaster, such as a last-value, moving-average, or simple regression approach.
- Implement an improved forecasting system using stronger feature engineering, Spark ML methods, or another justified predictive approach.
- Measure technical performance for both systems, including runtime, memory use, and storage footprint.
- Measure forecast quality using justified metrics such as `RMSE`, `MAE`, or `MAPE` on a held-out test period.

### Deliverables

The final submission must include ETL workflow artifacts, code, experiment logs, a written report, and a short presentation. The report must show whether the improved forecasting system produced meaningfully better predictive accuracy, what computational costs were introduced, and which design would be preferable in a real retail environment.

## Shared submission expectations

Each team must submit a reproducible codebase, workflow definition, experiment record, report, and presentation. Projects should reflect sound data-engineering practice, including pipeline structure and automation principles commonly associated with ETL orchestration tools and production data workflows.

Each final presentation should clearly cover the business problem, dataset, ETL design, baseline system, improved system, technical metrics, quality metrics, and the evidence for improvement. The strongest projects will not only report better numbers but also explain the trade-offs between speed, resource usage, and analytical quality.




