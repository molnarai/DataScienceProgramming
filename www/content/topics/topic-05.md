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
## Concept
Motivate persistence: a notebook loses its state, but a file outlives the session, which is what allows one program's output to become another's input. Develop a precise model of file paths — absolute versus relative, and the working directory that relative paths resolve against — since "file not found" is the most common error at this stage and is almost always a path problem rather than a code problem. Introduce text files as sequences of lines and CSV as a text convention with delimiters and a header row, along with the ambiguities that convention leaves open (quoting, embedded commas, encodings, missing fields). Explain modules and namespaces: importing binds names from another file, which is how code becomes reusable across programs. Close on the distinction between a file that is imported and a file that is run, and why a program needs a defined entry point.

## Practice
Read and write text files using `with open(...)` blocks, and explain why the context manager is preferable to manual `close`. Process a file line by line, strip newlines, and handle a header row; then do the same work with the `csv` module and compare. Write output files and verify results by reading them back. Demonstrate importing from the standard library and from a local helper module in the same directory. Introduce the `if __name__ == "__main__"` guard and run the resulting program from the terminal with `python script.py`, previewing the command-line work of the next session. In-class activity: students convert working notebook logic into a self-contained script with functions and a main block. Homework: a file-processing assignment that reads input, produces output, and reports basic results.

