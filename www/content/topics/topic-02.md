---
date: 2026-09-02
classdates: '2026-09-02'
draft: false
title: 'Types, Strings, and Conditionals'
concept: "Core scalar types (int, float, str, bool) and what a value's type implies. Comparison operators, truth values, and branching logic as a decision structure."
practice: "String methods and f-string formatting; explicit type conversion; `if`, `elif`, `else`. In-class: classify simple values and transform short text inputs."
weight: 20
numsession: 2
---


This session introduces Python as a language with its own syntax and conventions, establishing the habits of readable, consistent code before any complexity is added.
<!--more-->
 It then turns to variables and objects: a name refers to an object, every object has a type, and that type determines which operations are meaningful. Working through the core scalar types, students see why some combinations of values work and others raise errors, why explicit conversion is preferable to relying on implicit behavior, and where the common early pitfalls lie in numeric precision and in values that only appear to be what they seem. Comparison and boolean logic follow as the means of expressing a decision, leading to branching as a control structure in which exactly one path runs and ordering carries meaning.

The practical half builds outward from small, self-contained tasks toward larger programs assembled from reusable pieces. Students work with text and numeric data, format output for readability, and treat errors and tracebacks as information to be read rather than failures to be avoided. Conditional logic is developed incrementally, tracing how a given input moves through a program, and short working fragments are then combined so that composition becomes visible early. The session closes with a hands-on exercise in which students apply each of these aspects together on simple inputs, including cases that are empty or malformed.

{{<figure src="imgs/Core_Programming_Tools_for_Data.png" 
    alt="Figure: Infrographic that summarizes the content of this session" >}}

## Listen

{{< podcast src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/podcast/python_programming_blueprints_for_graduate_researchers.m4a" title="Python Programming Blueprints" >}}


## Read
- [Wes McKinney: Python for Data Analysis: Chapter 2](https://wesmckinney.com/book/python-basics)
- [Wes McKinney: Python for Data Analysis: Chapter 3](https://wesmckinney.com/book/python-builtin)

## Hands-on
Notebooks in [02-Types-Strings-Conditionals](https://github.com/molnarai/DataScienceProgramming/tree/main/02-Types-Strings-Conditionals)


## References
- [The Python Language Reference](https://docs.python.org/3.12/reference/index.html)
- [The Python Standard Library](https://docs.python.org/3.12/library/index.html#library-index)
- [Built-in Functions](https://docs.python.org/3.12/library/functions.html)
- [Built-in Types](https://docs.python.org/3.12/library/stdtypes.html)
- [Common string operations](https://docs.python.org/3.12/library/string.html)
- [File and Directory Access](https://docs.python.org/3.12/library/filesys.html)
