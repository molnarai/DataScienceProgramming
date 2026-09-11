---
date: 2026-09-16
classdates: '2026-09-16'
draft: false
title: 'Functions and Decomposition'
concept: "Functions as named, reusable units with a contract: inputs, a return value, and a single responsibility. Scope and local versus global names. Decomposition as a design activity."
practice: "Function definitions, parameters and defaults, return values, docstrings, and simple tests with `assert`. In-class: refactor repetitive code into functions."
weight: 40
numsession: 4
---
Decomposition is how a problem too large to hold in your head becomes a handful of steps you can name, write, and check one at a time. In Python those steps are functions: each one a contract with a single responsibility and clear expectations about its inputs, its return value, and its edge cases.
<!--more-->
The same discipline is what lets the pieces fit back together. Returning a value instead of printing keeps a function usable by a test or by the next stage of a pipeline; local names and no shared global state keep one piece from quietly breaking another. Docstrings, type hints, and a little input validation record what each unit promises — so a program assembled from small, isolated parts stays something you can read, test, and change.

{{<figure src="imgs/Programming_Function_Coding_Contract.png"  alt="Figure: Infographic about Functions" >}}

## Listen

{{< podcast src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/podcast/predictable_python_function_design_for_data.m4a" title="Overview of Session" >}}


{{< podcast src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/podcast/how_decomposition_cures_project_paralysis.m4a" title="How Decomposition Cures Project Paralysis" >}}


{{< podcast src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/podcast/python_functions_as_legally_binding_contracts.m4a" title="Python Functions as Legally Binding Contracts" >}}

## Read

- [Decomposition: Breaking a Large Problem into Smaller Pieces](../blog/decomposition/) (source document for podcast )
- [Wes McKinney: Python for Data Analysis: Chapter 2](https://wesmckinney.com/book/python-basics)
- [Wes McKinney: Python for Data Analysis: Chapter 3](https://wesmckinney.com/book/python-builtin)

## Hands-on

Notebooks in [04-Functions-Decomposition](https://github.com/molnarai/DataScienceProgramming/tree/main/04-Functions-Decomposition)


