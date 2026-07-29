---
date: 2026-12-02
classdates: '2026-12-02'
draft: false
title: 'Integration and Review'
theoretical: "Review of core Python ideas as a connected whole. Debugging as a systematic process rather than guesswork. Reproducibility and readiness for follow-on coursework."
technical: "Reading tracebacks, isolating failures, and testing; reproducible file and repository organization. In-class: an integrative coding and interpretation exercise."
weight: 140
numsession: 14
---
## Theory
Revisit the course as a connected whole rather than a list of topics: values and types, control flow, functions, files, tabular data, and algorithmic ideas are the layers of a single toolkit, and a realistic task uses several at once. Treat debugging explicitly as a systematic method — reproduce the failure, read the error, form a hypothesis, shrink the input, test one change at a time — and contrast it with guess-and-rerun, which is where beginners lose the most time. Consolidate reproducibility as the through-line of the second half of the course: clear file organization, code that runs from the command line, fixed random seeds, and a commit history that records how the work developed. Close by connecting these skills to what comes next, including where each idea reappears in later statistics, analytics, and machine learning coursework.

## Technical
Work through a review of the recurring constructs and the errors they produce, reading real tracebacks and identifying the failing line and cause. Practice isolating a bug in a multi-function program by testing components separately and adding assertions, and demonstrate why a function with a clear contract is easier to debug than a long block of inline code. Lay out a small project properly: a script with a main entry point, helper functions, input and output directories, a README, and a `.gitignore`, then run it from a clean shell to confirm it works outside the notebook. In-class activity: students complete an integrative exercise that reads data, computes a result with their own functions, produces a figure, and explains the finding. Homework: a cumulative assignment combining functions, files, analysis, and one algorithmic component.

