---
date: 2026-11-11
classdates: '2026-11-11'
draft: false
title: 'Algorithm-System Trade-offs & Cases'
theoretical: "Cross-cutting trade-offs: accuracy vs latency vs cost vs interpretability across recommenders, graphs, and forecasting. Simple Pareto-style reasoning and brief real-world case vignettes."
technical: "Integrative workshop: short end-to-end demo, then supervised project work. Design reviews of ETL, models, metrics, and system decisions."
weight: 120
numsession: 12
---
## Theory
Synthesize algorithmic trade-offs across the three domains: for each project type, compare simple baselines vs more complex models under constraints of latency, memory, cost, and interpretability. Introduce the idea of Pareto frontiers (no formal math required) to reason about accuracy vs efficiency trade-offs. Present short case-study vignettes from industry-scale systems (e.g., simpler models in high-traffic settings, approximate algorithms for triangle counting or PageRank). Encourage students to map their project choices onto this framework: where does their baseline sit, where does their improved model sit, and is there a 'sweet spot' in between?

## Technical
Technical session used primarily as a supervised project workshop. Begin with a short integrative demo showing an end-to-end retail analytic pipeline (ETL -> model -> deployment -> monitoring). Then dedicate most of the time to team work: refactoring code, solidifying ETL and workflows, refining improved models, and cleaning up metrics and logging. Instructor and TAs run short design reviews with each team, probing their reasoning about algorithm system trade-offs and robustness.

