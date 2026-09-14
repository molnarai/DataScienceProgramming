---
draft: false
title: 'Python Modules and Self-Standing Scripts'
weight: 46
description: >-
  Modules, imports, and namespaces; what separates an imported file from an
  executed one; and using `main()` with `if __name__ == "__main__":` to turn notebook
  logic into a reproducible program.
date: 2026-09-23
lastmod: 2026-09-23
---

Code that works once, in one notebook, is not yet a program. Turning it into one means
dividing it along its responsibilities, putting those pieces in files other code can
import, and giving the result a single, explicit place to start.
<!--more-->
This post covers modules and imports, the namespaces they create, what separates a file
that is imported from one that is run, and the `if __name__ == "__main__":` guard that
lets the same file do both. It then applies all of it: a small project layout, a worked
conversion of notebook cells into a script, running that script from the terminal, and the
coding principles that keep a workflow reproducible.

Its companion post, [Reading and Writing Files: Text, CSV, JSON, and JSONL](../reading-writing-files/),
covers the file handling these programs are built around.

## Modules and imports

A **module** is a Python file containing reusable code.

For example:

```text
analysis_helpers.py
```

is a Python module named:

```python
analysis_helpers
```

Modules support decomposition. Instead of putting every function into a single notebook or script, code can be divided into files with coherent responsibilities.

### Import from the standard library

Python includes many standard-library modules.

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

In this example:

- `math` is a module.
- `sqrt` is a name defined in that module.
- `math.sqrt` is the fully qualified name.

Another example:

```python
from pathlib import Path

project_path = Path("data") / "students.csv"
print(project_path)
```

### Namespaces

A **namespace** is a mapping between names and objects. It helps Python determine what a name refers to.

```python
import math

result = math.sqrt(16)
```

The name `sqrt` belongs to the `math` namespace, so we write `math.sqrt(16)`.

Namespaces prevent collisions. Different modules may define names such as `mean`, `load`, `read`, or `process`. The module prefix makes it clear which one is intended.

### Common import styles

```python
import math
```

Use:

```python
math.sqrt(9)
```

```python
from math import sqrt
```

Use:

```python
sqrt(9)
```

```python
import math as m
```

Use:

```python
m.sqrt(9)
```

For beginner-friendly and shared code, explicit imports are often clearest:

```python
import csv
import json
import math
from pathlib import Path
```

### Avoid wildcard imports

Avoid:

```python
from math import *
```

This imports many names into the current namespace. It becomes difficult to identify where functions came from and can create confusing name conflicts.

### Local helper modules

Suppose a project is organized this way:

```text
student-project/
├── data/
│   └── students.csv
├── output/
├── analysis_helpers.py
└── summarize_students.py
```

The helper module can define reusable analysis functions.

`analysis_helpers.py`:

```python
from collections import Counter

def count_by_program(students):
    return Counter(student["program"] for student in students)

def average_gpa(students):
    gpas = [float(student["gpa"]) for student in students if student["gpa"]]
    return sum(gpas) / len(gpas)
```

`summarize_students.py`:

```python
from analysis_helpers import average_gpa, count_by_program

students = [
    {
        "student_id": "1001",
        "name": "Amina Patel",
        "program": "MS Data Science",
        "gpa": "3.8",
    },
    {
        "student_id": "1002",
        "name": "Jordan Lee",
        "program": "MS Analytics",
        "gpa": "3.6",
    },
]

print(count_by_program(students))
print(average_gpa(students))
```

### Why helper modules matter

A project can separate responsibilities:

- One file manages inputs and outputs.
- One file contains cleaning or validation functions.
- One file contains analysis functions.
- One file runs the workflow.
- One file contains tests.

This structure is easier to review, test, reuse, and maintain than one large script.

### Do not shadow standard-library modules

Avoid local filenames such as:

```text
csv.py
json.py
math.py
pathlib.py
random.py
statistics.py
```

If a project includes `csv.py`, then this statement:

```python
import csv
```

may import the local file instead of the intended standard-library module. This produces confusing errors.

---

## Imported files versus executed scripts

A Python file can be used in two related ways:

1. It can be run directly as a program.
2. It can be imported by another Python file.

Consider `greetings.py`:

```python
def greet(name):
    return f"Hello, {name}!"

print("greetings.py is running")
```

Run directly:

```bash
python greetings.py
```

Output:

```text
greetings.py is running
```

Now import it from another program:

```python
import greetings

print(greetings.greet("Amina"))
```

Output:

```text
greetings.py is running
Hello, Amina!
```

Why does it print the first message during import? Importing a module executes its top-level code. This can be undesirable when that code launches processing, writes files, or performs other work that should occur only when a program is intentionally executed.

---

## The `__main__` guard and program entry points

Python gives every module a special variable named `__name__`.

- When a file is run directly, `__name__` is `"__main__"`.
- When a file is imported, `__name__` is the module's name.

The standard pattern is:

```python
if __name__ == "__main__":
    main()
```

Example:

```python
def greet(name):
    return f"Hello, {name}!"

def main():
    print(greet("Amina"))

if __name__ == "__main__":
    main()
```

When run directly:

```bash
python greetings.py
```

Output:

```text
Hello, Amina!
```

When imported:

```python
from greetings import greet

print(greet("Jordan"))
```

Output:

```text
Hello, Jordan!
```

The imported module's `main()` function does not automatically run.

### Why an entry point matters

The main guard lets the same file be both:

- A reusable module that defines functions.
- A standalone executable script that coordinates a workflow.

This supports testing, reuse in notebooks, and use in larger pipelines without accidentally running a complete file-processing job upon import.

---

## Recommended small-project structure

A simple introductory project can use this structure:

```text
project-name/
├── README.md
├── data/
│   ├── raw/
│   │   └── source_data.csv
│   └── processed/
├── output/
│   ├── tables/
│   └── reports/
├── src/
│   ├── helpers.py
│   └── process_data.py
└── tests/
```

A smaller version is suitable for early assignments:

```text
project-name/
├── data/
│   └── input.csv
├── output/
├── helpers.py
└── main.py
```

### Folder and file responsibilities

| Folder or file | Purpose |
|---|---|
| `data/` | Input data and, when appropriate, processed data |
| `data/raw/` | Original source data that should generally not be changed |
| `data/processed/` | Cleaned, transformed, or derived datasets |
| `output/` | Generated reports, summary tables, charts, and results |
| `src/` | Source code for the project |
| `tests/` | Automated checks for important functions |
| `README.md` | Setup, inputs, execution instructions, outputs, and assumptions |
| `main.py` or `process_data.py` | Main executable workflow |

### Why separation matters

Do not mix raw inputs and generated outputs in the same folder without a clear convention. Separation helps answer:

- Which files came from an external source?
- Which files were created by the analysis?
- Which files can be overwritten safely?
- Which code created a particular output?
- Which outputs should be shared with stakeholders?

This supports provenance, auditability, maintenance, and accidental-overwrite prevention.

---

## Convert notebook work into a script

Notebooks are good for exploration. The goal is not to eliminate them. The goal is to distinguish between exploratory work and a repeatable operational workflow.

### Typical notebook pattern

```python
# Cell 1
import csv

# Cell 2
with open("students.csv") as file:
    ...

# Cell 3
# Clean data

# Cell 4
# Analyze data

# Cell 5
# Write result
```

Potential issues:

- Cells may run in a different order than they appear.
- Variables may remain in memory from earlier work.
- Paths and assumptions may be scattered across cells.
- The notebook may work only because of hidden state.
- A collaborator may not know how to reproduce the output from scratch.

### Script-oriented design

Move work into named functions:

```python
def read_data(input_path):
    ...

def clean_data(records):
    ...

def analyze_data(records):
    ...

def write_results(results, output_path):
    ...

def main():
    input_path = ...
    output_path = ...

    records = read_data(input_path)
    clean_records = clean_data(records)
    results = analyze_data(clean_records)
    write_results(results, output_path)

if __name__ == "__main__":
    main()
```

This expresses a visible pipeline:

\[
\text{Read} \rightarrow \text{Clean} \rightarrow \text{Analyze} \rightarrow \text{Write}
\]

### Benefits

- Each function has a specific responsibility.
- Functions can be tested independently.
- Inputs and outputs are explicit.
- The workflow can run from a terminal.
- The code is easier to review and maintain.
- A project can be handed off to another person.
- A notebook can still import and use the same functions for exploration.

---

## Run scripts from the terminal

Suppose the project looks like this:

```text
student-project/
├── data/
│   └── students.csv
├── output/
└── summarize_students.py
```

Open a terminal and change to the project directory:

```bash
cd path/to/student-project
```

Run the script:

```bash
python summarize_students.py
```

On some systems, Python 3 may be invoked as:

```bash
python3 summarize_students.py
```

### Why terminal execution matters

Terminal execution begins the transition toward automation:

- A program can run without manually opening a notebook.
- The exact command can be documented in the README.
- A workflow can later be scheduled or integrated into CI/CD.
- The same script can run in a container, server, cluster job, or automated pipeline.
- Future sessions can add command-line arguments instead of fixed file paths.

At this stage, the central goal is simple: the program should run reliably from a clean starting state.

---

## Coding principles for data-science projects

Beyond syntax, a few habits are what make a project maintainable.

### Make inputs and outputs explicit

A reader should be able to identify:

- Input file locations.
- Output file locations.
- Expected input columns or JSON fields.
- Transformations performed.
- Summary statistics or deliverables produced.

Avoid hidden dependencies and unexplained state.

### Use meaningful names

Prefer:

```python
student_records
average_gpa
input_path
output_path
program_counts
```

over:

```python
x
data2
temp
thing
result1
```

Good names reduce the effort required to read, review, manage, and maintain a program.

### Keep functions focused

Prefer separate functions with coherent responsibilities:

```python
def read_students(input_path):
    ...

def validate_students(students):
    ...

def calculate_average_gpa(students):
    ...

def write_summary(summary, output_path):
    ...
```

Avoid a single function that reads input, cleans data, analyzes it, writes results, and performs unrelated actions.

### Preserve raw data

Treat source data as read-only whenever possible.

Instead of overwriting:

```text
data/survey.csv
```

write a derived file:

```text
data/processed/survey_cleaned.csv
```

This preserves provenance: the team can inspect the original input and understand what transformations created the derived data.

### Validate early

Check assumptions near the beginning of a workflow:

- Does the input file exist?
- Is it empty?
- Does it have required CSV columns or JSON fields?
- Are identifiers unique when they should be?
- Are numeric fields actually numeric?
- Are dates parseable?
- Are values within plausible ranges?
- Are required fields missing?

Early validation prevents bad data from silently creating misleading results.

### Report what happened

A script should summarize its work.

```text
Input file: data/input.csv
Rows read: 850
Rows skipped: 12
Rows analyzed: 838
Output file: output/category_summary.csv
Categories found: 6
```

This supports quality assurance, troubleshooting, operational transparency, and stakeholder communication.

---

## Project-management checklist

A project manager need not write every Python function, but should be able to determine whether a workflow is sufficiently specified, reproducible, and trustworthy.

### Inputs

- What person, system, or process provides the input data?
- What file format is expected: text, CSV, JSON, JSONL, or another format?
- Which CSV columns or JSON fields are required?
- What do missing values mean?
- Which date, time-zone, unit, category, and identifier conventions apply?
- How often is the input refreshed?
- Does the process preserve the original data?

### Processing

- Which transformations occur?
- Are those transformations documented?
- How does the workflow handle invalid or incomplete records?
- Does it report input, skipped, and output record counts?
- Can it be rerun from scratch?
- Are intermediate datasets retained when auditability requires them?

### Outputs

- What reports, tables, files, or derived datasets are produced?
- What fields and definitions do they contain?
- Who uses the output?
- How is output quality verified?
- Where are outputs stored?
- Are outputs dated, versioned, or otherwise traceable?

### Operational readiness

- Can another person run the project from documented instructions?
- Does it use portable project-relative paths instead of personal desktop paths?
- Does it provide understandable errors?
- Are dependencies and versions documented?
- Is there a clear entry point such as `python src/process_data.py`?

## Key takeaways

- Modules support code reuse and separation of responsibilities.
- Imports create namespaces; use clear imports and avoid ambiguous local module names.
- `if __name__ == "__main__":` distinguishes reusable code from code that should run as a program.
- A script needs one explicit entry point, so the same file can be imported without side effects or run directly from the terminal.
- Keep functions focused, name things meaningfully, validate early, and report what happened.
- A maintainable data-science project makes its inputs, transformations, outputs, assumptions, and execution steps visible.
