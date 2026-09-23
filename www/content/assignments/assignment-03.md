+++
date = '2026-09-16'
due_date = '2026-09-30T23:59:00'
draft = false
title = 'Homework 3: Ranking Scholarship Applications'
weight = 30
status = 'Posted'
+++

Order a list of scholarship applications from the lowest review score to the highest, without `sorted()`, `.sort()`, `min()`, or `max()`. Across seven test-driven phases you will build the solution out of small functions with clear contracts: one comparison rule that settles what a tie means, a function that combines two ordered groups, a function that splits a group in two, a function that orders the groups too small to split, and a function that uses all of them to order a group of any size. Then you will add a policy for applications with missing or unusable scores and print an exactly formatted ranking report. Each phase ships with its own tests, and only at the end are you asked to name the method you have built.

<!-- more -->


Related session: [Session 4 — Functions and Decomposition](../../topics/topic-04/)

### The Phases

| | |
|---|---|
| **1** | One comparison rule, and what a tie means |
| **2** | Combine two already-ordered groups |
| **3** | Divide a group in two |
| **4** | Order the groups too small to divide |
| **5** | Order a group of any size, using Phases 1–4 |
| **6** | A policy for missing or unusable scores |
| **7** | The formatted ranking report |

The point is not "produce ordered output". It is to write focused functions with
clear inputs, outputs and responsibilities, test each one on its own, combine
them into a larger solution, and revise the design when hidden cases surface.

### Topics Covered

- Functions as contracts: name, parameters, return value, documented edge cases
- Decomposition — building one behavior out of several smaller ones
- Recursion, and the base case that stops it
- Returning new data instead of modifying the input
- Deciding a policy for missing and unusable values
- Test-driven work, one phase at a time
- String formatting for an exactly specified report

### Instructions

The full instructions, the starter file, and the per-phase tests are released
through the course template. On the course server run `ifi8410-update`, then
read `Assignments/HW03/instructions/homework03_instructions.md` and work in
`Assignments/HW03/submission/`.

No pandas, no numpy, no file reading — the dataset is a list of dictionaries
defined in the starter file. Hand in with `ifi8410-test` and `ifi8410-submit`.
