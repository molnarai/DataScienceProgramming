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
Some questions cannot be answered by looking something up, because the answer depends on things that have not happened yet and that vary by chance: how many pastries to bake when the number of customers changes from day to day, or whether one person at a service desk is enough when people arrive in bursts. For a few such questions there is a formula; for most there is not. A **simulation** works regardless: build a small model of the situation, let the computer live through it thousands of times, and count what happens. A computer cannot produce chance, so its random numbers are **pseudorandom** — a sequence fixed entirely by its **seed** — and that is a feature, because a result that cannot be repeated cannot be checked or debugged. The discipline is one generator, made once from a seed and passed to every function that draws; a generator created inside the loop restarts the sequence, and every trial becomes the same trial.
<!--more-->
Simulation also brings a difficulty nothing earlier in the course had: run the program again and the answer changes. A simulated number is an estimate, so it comes with a **standard error** and an interval, both computable from a single run. The error shrinks with the square root of the number of trials — a hundred times the work buys one more decimal place — which gives "how many trials?" an answer: enough that the interval is narrower than the difference you care about. To compare options fairly, give each exactly the same random draws, so the luck is in both results and cancels out of the difference. The same machinery, pointed at real data, is the **bootstrap**: resample the sample, with replacement, to see how far its mean or median would move. Report the estimate with its interval, its number of trials, its seed, and its assumptions; the simulation answers the model, not the world.

TODO: marquee image

## Listen

TODO: podcast

## Presentation

TODO: presentation

## Read

- [Simulation and Randomness](../../blog/simulation-randomness/) (lecture notes)

## Hands-on

Notebooks in [10-Simulation-Randomness](https://github.com/molnarai/DataScienceProgramming/tree/main/10-Simulation-Randomness)

## Homework

- [Homework 9: An Answer with Error Bars](../../assignments/assignment-09/) — due Wednesday, November 11, 2026
