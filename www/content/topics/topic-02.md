---
date: 2026-09-02
classdates: '2026-09-02'
draft: false
title: 'Types, Strings, and Conditionals'
theoretical: "Core scalar types (int, float, str, bool) and what a value's type implies. Comparison operators, truth values, and branching logic as a decision structure."
technical: "String methods and f-string formatting; explicit type conversion; `if`, `elif`, `else`. In-class: classify simple values and transform short text inputs."
weight: 20
numsession: 2
---
## Theory
Introduce Python's core scalar types (integers, floats, strings, booleans) and the idea that a value's type determines which operations are meaningful. Discuss why `"5" + 5` fails while `5 + 5.0` succeeds, and use that to motivate explicit conversion over implicit coercion. Cover the pitfalls beginners meet first: floating-point values that do not compare exactly, integer division versus true division, and strings that look numeric but are not. Present comparison operators and boolean logic as the machinery for expressing a decision, then introduce branching as a control structure: exactly one path of an `if`/`elif`/`else` chain runs, order matters, and an unreachable branch is a logic error even when the code is syntactically valid.

## Technical
Work through string operations in depth: indexing, slicing, concatenation, and the common methods (`lower`, `upper`, `strip`, `split`, `replace`, `startswith`, `find`) that do most of the practical work in text handling. Demonstrate f-strings for readable output formatting. Show `int()`, `float()`, `str()`, and `bool()` conversions along with the errors raised when a conversion is impossible, and read those tracebacks aloud as a debugging skill. Write conditional logic step by step, tracing which branch executes for a given input. In-class activity: students classify simple values by type and write short transformations of text input, using conditionals to handle empty or malformed cases. Homework: a small text-processing task using strings and conditionals.

