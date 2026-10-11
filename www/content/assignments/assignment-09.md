+++
date = '2026-10-28'
due_date = '2026-11-11T23:59:00'
draft = false
title = 'Homework 9: An Answer with Error Bars'
weight = 90
status = 'Posted'
+++

A coffee cart sells pastries that cost $1 to bake and sell for $3, and whatever is left in the evening is thrown away. About forty customers a day want one. How many should the cart bake each morning? There is no column to look this up in; the way to get the answer is to let the computer live through ten thousand mornings and count. That is a simulation, and its result has a property no result in this course has had so far: run it again and it changes — one seed says 42, another says 43. Across seven test-driven phases you will check a simulation against a problem with a known answer, run many trials from one seeded generator, attach a standard error and an interval to every estimate, build a model of the cart, compare batch sizes on the same random days, and apply the same idea to real data with the bootstrap.

<!-- more -->


Related session: [Session 10 — Simulation and Randomness](../../topics/topic-10/)

### The Phases

| | |
|---|---|
| **1** | A problem with a known answer — the birthday problem, exact and as one trial |
| **2** | Many trials from one generator |
| **3** | How sure? — standard error and interval |
| **4** | More trials, less noise — and how slowly |
| **5** | A model of the coffee cart |
| **6** | Which option is best, and how sure is that? |
| **7** | Real data with the bootstrap, and the report |

A simulated number is an estimate, and an estimate with no statement of how
far it can be trusted is half an answer. The error shrinks with the square
root of the number of trials: to halve it you need four times the work, and to
gain a digit, a hundred times. Your numbers will not match the handout's or
your neighbour's, and the tests do not expect them to.

### Topics Covered

- Checking a simulation against an exact answer before trusting it
- Pseudorandom generators and seeds; passing one generator through a program
- Estimates, the standard error, and a 95 % interval
- Convergence: how the error depends on the number of trials
- Modelling a decision whose outcome depends on chance
- Comparing options on the same random numbers, and the interval of a difference
- The bootstrap: an interval for a statistic of real data
- Reporting a simulated result with its seed, its trials, and its interval

### Instructions

The full instructions, the starter file, and the per-phase tests are released
through the course template. On the course server run `ifi8410-update`, then
read `Assignments/HW09/instructions/homework09_instructions.md` and work in
`Assignments/HW09/submission/`.

Use numpy and pandas, which are already in the course environment. Every
random number comes from a generator that is passed in; the global generators
(`np.random.seed`, `random.random()`) are not allowed, and the tests check
that a result follows from its seed. The last part of the report uses the
cleaned invasive-plants file, so it runs only on the cluster. Hand in with
`ifi8410-test` and `ifi8410-submit`.
