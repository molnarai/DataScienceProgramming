---
date: 2026-10-28
classdates: '2026-10-28'
draft: false
title: 'Simulation and Randomness'
concept: "Estimating an answer by repeated trials. Pseudorandomness and why seeds make randomness reproducible. Monte Carlo intuition; variability of an estimate across runs."
practice: "The `random` module and NumPy random generators; seeding; sampling and repeated experiments; summarizing simulated outcomes. In-class: simulate a random process and compare runs."
weight: 100
numsession: 10
---
## Concept
Introduce simulation as a way to answer a question by running an experiment many times instead of solving it analytically, which makes problems accessible long before the corresponding mathematics is. Explain pseudorandomness: the generator is deterministic given its seed, so results are reproducible on demand — a property that is essential for grading, debugging, and scientific reporting, not a limitation. Build Monte Carlo intuition through the estimate-as-average idea, and emphasize the point beginners most often miss: a simulated result is itself uncertain, it varies from run to run, and more trials shrink that variability in a predictable way. Discuss how to report a simulation honestly by stating the number of trials and the seed, and how the same machinery underlies resampling, sensitivity analysis, and probabilistic reasoning about real data.

## Practice
Use Python's `random` module and NumPy's random generators for uniform draws, integer draws, sampling with and without replacement, and shuffling. Set a seed and demonstrate that two seeded runs match exactly while two unseeded runs do not. Build a simulation as a function of the number of trials, so the same code can be run at different scales, and structure it with a loop that records each trial's outcome for later summary. Estimate a probability as a proportion of trials, then rerun at increasing trial counts and observe the estimate stabilizing. Summarize outcomes with the statistics and plots from the previous session, including a histogram of simulated results. In-class activity: students simulate a simple random process and compare outcomes across runs and seeds. Homework: implement a simulation study and explain the results.

