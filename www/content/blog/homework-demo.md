---
draft: false
title: Homework Demo
weight: 10
description: Videos to demonstrate solving, testing and submitting a homework assignment
date: 2026-09-07
lastmod: 2026-09-07
---

These two screencasts walk through **HW00 — Word Frequencies in the Works of Shakespeare**
(`Assignments/HW00`) from start to finish. HW00 carries no points and is not handed in;
it exists so you can practice the workflow once while nothing is at stake. Every graded
assignment after it looks the same and uses the same four commands.

Follow along in your own JupyterLab session on the Analytics Research Cluster — see
[Getting started]({{< ref "getting_started.md" >}}) if you have not logged in yet.

## Part 1: Setup and Work on Solution

Starting a session with `ifi8410-status --auto`, collecting the assignment with
`ifi8410-update`, and finding your way around the `HW00` folder — `instructions/`,
`starter/`, `test/`, and the `submission/` folder where everything you write goes.
The demo then opens `starter/Instructions_orig.ipynb`, renames it (the next course
release overwrites the files it delivered, answers and all), and works through the
step-by-step notebook: try the idea out, write the function, save it into
`submission/steps/` with `%%writefile`, and let the step's test cell check the saved
file.

{{< video src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/vido/hw00-demo-part-1.mp4" title="Homework Demo: Setup and Work" >}}

## Part 2: Testing and Submission

Assembling the nine step files into `submission/wordfrequency.py` — the one file that is
graded — then running the test suite locally from a terminal (`./run_tests.sh`, or
`./run_tests.sh 6` for a single step), reading a failing test to work out what it expects,
and finally `ifi8410-test` to save your work and run the suite on the server, followed by
`ifi8410-submit` to hand it in. Note the required `JOURNAL.md`, and keep the downloaded
book out of Git.

_TBD_
