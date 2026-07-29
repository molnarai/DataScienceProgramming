---
date: 2026-09-23
classdates: '2026-09-23'
draft: false
title: 'Time Series & Many-Series Forecasting'
theoretical: "Time-series fundamentals: trend, seasonality, baselines (naïve, moving averages), and error metrics. Many-series forecasting and why simple single-series methods don't scale."
technical: "EDA and feature engineering with Spark: sampling, grouped stats, and task-specific features for each track. Teams extend ETL to feature-ready tables and perform basic EDA."
weight: 50
numsession: 5
---
## Theory
Cover time-series fundamentals: trend, seasonality, residuals, stationarity. Discuss classical baseline models (na√Øve last-value, moving averages, simple exponential smoothing) and appropriate error metrics (RMSE, MAE, MAPE). Emphasize the “many-series” setting in retail (thousands of product √ó store series) and what breaks from single-series methods: memory/compute constraints, the need for shared models or hierarchical structures, and proper time-based evaluation (rolling or expanding windows). Highlight how naive random splits cause leakage in time-series and why backtesting protocols are needed at scale. Include quick exercises computing simple baselines and errors on short synthetic series.

## Technical
Technical focus on exploratory data analysis (EDA) and feature engineering with Spark. Show patterns for EDA at scale: stratified sampling, approximate quantiles, grouped statistics, and visualization via sampled extracts. For each project type, demonstrate typical feature engineering: interaction counts and recency for recommenders, degree distributions and edge weights for graphs, lagged values and calendar features for forecasting. In-class: teams extend their ETL to produce initial feature-ready tables and perform basic EDA relevant to their project (e.g., item popularity histograms, graph degree histograms, seasonality plots from aggregated sales).

