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
## Concept
Introduce the function as a named unit of behavior with an explicit contract: what it takes in, what it gives back, and the one job it is responsible for. Distinguish returning a value from printing one — a distinction beginners routinely conflate and which matters the moment code is tested automatically. Cover scope: names created inside a function are local and disappear when it returns, which is what makes a function safe to reuse; reliance on global state is what makes it fragile. Frame decomposition as a design activity rather than a cleanup step: given a larger task, identify the sub-steps that can be named, tested, and reasoned about separately. Discuss what makes a function good — a descriptive name, few parameters, no hidden side effects — and how a docstring records the contract for the next reader, including the author a week later.

## Practice
Define functions with positional and default parameters, return single and multiple values, and write docstrings that state purpose, parameters, and return value. Trace what happens to local variables across calls and demonstrate the classic surprises: shadowing a global name, mutating a list passed as an argument, and forgetting a `return` so the function yields `None`. Introduce simple testing with `assert` and a handful of representative cases including an edge case, connecting directly to how the autograder will evaluate submissions. In-class activity: students take a block of repetitive code from an earlier session and refactor it into functions, verifying the behavior is unchanged. Homework: implement several small functions and pass an autograder test suite.

