---
date: 2026-09-23
classdates: '2026-09-23'
draft: false
title: 'Files, Modules, and Scripts'
concept: "Persistence: why programs read and write files. Paths and the working directory. Modules and namespaces; what makes a program runnable as a script."
practice: "Reading and writing text and CSV files; `with` blocks; imports; `if __name__ == \"__main__\"`. In-class: convert notebook logic into a self-contained script."
weight: 50
numsession: 5
---
A file outlives the session that created it, which is what allows one program's output to become another's input. Safe file handling rests on a few habits: a `with` block that closes the file whatever happens, an explicit UTF-8 encoding, input and output locations that are named rather than assumed, and a read-back of anything written. Which format to write in depends on the shape of the data. CSV suits simple rectangular tables and moves easily between spreadsheets and programs, at the cost of careful handling of headers, quoting, embedded commas, missing fields, and the conversion of every value from text. JSON carries structured documents — nested objects and lists, numbers, booleans, and null — which makes it a fit for configuration, metadata, API payloads, and records that are not flat. JSONL puts one complete JSON record on each line, so large collections of independent records such as logs, events, and model outputs can be appended and processed one record at a time.
<!--more-->
Code becomes reusable once it is divided along its responsibilities — reading, validating, transforming, analyzing, writing — and those functions are gathered into modules that other programs import. A script needs one explicit entry point: a `main()` function behind an `if __name__ == "__main__":` guard, so the same file can be imported without side effects or run directly from the terminal. What these conventions share is that they make a program's inputs, assumptions, transformations, outputs, and execution steps visible rather than implicit, which is what allows an analysis to be repeated and checked by someone other than its author.

{{<figure src="imgs/Programming_File_Handling_Guide.png"  alt="Figure: Infographic about Files and Modules" >}}

## Listen

{{< podcast src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/podcast/from_notebooks_to_reproducible_python_scripts.m4a" title="Overview" >}}

{{< podcast src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/podcast/from_jupyter_notebooks_to_production_python.m4a"
title="Deep Dive" >}}




## Read

- [Reading and Writing Files](../../blog/reading-writing-files/) (source document for podcast )
- [Python Modules and Self-Standing Scripts](../../blog/python-modules-scripts/) (source document for podcast )
- [Wes McKinney: Python for Data Analysis: Chapter 3](https://wesmckinney.com/book/python-builtin)

## Hands-on

Notebooks in [05-Files-Modules-Scripts](https://github.com/molnarai/DataScienceProgramming/tree/main/05-Files-Modules-Scripts)


