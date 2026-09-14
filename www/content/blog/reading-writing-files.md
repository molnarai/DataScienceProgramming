---
draft: false
title: 'Reading and Writing Files: Text, CSV, JSON, and JSONL'
weight: 45
description: >-
  Paths and the working directory, safe file handling with `with open(...)`,
  and choosing among CSV, JSON, and JSON Lines for tabular and record-shaped data.
date: 2026-09-23
lastmod: 2026-09-23
---

A notebook loses its state when the kernel restarts; a file outlives the session that
created it. That is what allows one program's output to become another's input, and it is
why almost every data-science workflow begins and ends with a file.
<!--more-->
This post covers the mechanics: how paths and the working directory decide where a program
looks, how to open, read, and write files safely with `with open(...)`, and how to choose
among the three text formats that carry most tabular and record-shaped data — CSV, JSON,
and JSON Lines. It closes with a complete program that reads JSONL, validates it, and
writes a CSV summary.

Its companion post, [Python Modules and Self-Standing Scripts](../python-modules-scripts/),
covers packaging this work into a program that can be rerun.

## Why files matter

A notebook is useful for learning, exploration, visualization, and experimentation. However, notebook state is temporary and can be difficult to reproduce precisely.

A notebook may have hidden dependencies:

- Variables disappear when the kernel restarts.
- Cells may be run out of order.
- Earlier cells may have changed data or configuration in ways that later cells assume.
- The exact input file and output files may not be obvious.
- Another person may be unable to recreate the result from a clean environment.

A file outlives a Python session. Files make it possible for one program's output to become another program's input.

A basic data workflow can be described as:

\[
\text{Input files} \rightarrow \text{Processing program} \rightarrow \text{Output files}
\]

For example:

\[
\texttt{survey.csv} \rightarrow \texttt{clean\_survey.py} \rightarrow \texttt{survey\_summary.csv}
\]

The program is not simply "some Python code." It is a defined transformation with documented inputs, processing logic, outputs, and expectations.

### Why this matters for data science

Files allow a workflow to be:

- Re-run next week, next semester, or by another team member.
- Reviewed and tested outside of a notebook.
- Archived with its inputs and outputs.
- Automated later through scheduled jobs, CI/CD, containers, or workflow tools.
- Shared with stakeholders who may use the outputs but not write code.

### Project-management perspective

Many data-science graduates will manage projects, collaborate with analysts and engineers, or evaluate technical workflows rather than write every component themselves. They should be able to ask:

- What files are inputs to the process?
- Who provides or creates those files?
- What format, columns, units, dates, identifiers, and encodings are expected?
- Where are input files stored?
- What happens when an input file is missing or malformed?
- What output files are produced?
- How are outputs checked for completeness and reasonableness?
- Can another person rerun the workflow without relying on a particular person's notebook or laptop?

This is the beginning of **reproducible data science**.

---

## Files, folders, and paths

A **file path** tells the operating system where a file is located.

Examples:

```text
data/survey.csv
output/summary.txt
/home/student/project/data/survey.csv
C:\Users\Student\project\data\survey.csv
```

The exact path syntax differs by operating system, but the underlying idea is the same.

### Absolute paths

An **absolute path** gives the complete location of a file beginning from the root of a file system.

macOS and Linux example:

```text
/home/peter/projects/ifi8410/data/survey.csv
```

Windows example:

```text
C:\Users\Peter\projects\ifi8410\data\survey.csv
```

Absolute paths are unambiguous on one particular computer. They are generally a poor choice to hard-code into a shared project because other users have different usernames and directory structures.

Avoid this in shared code:

```python
with open("/Users/peter/Desktop/IFI8410/data/survey.csv") as file:
    ...
```

That script likely works only on the original author's computer.

### Relative paths

A **relative path** is interpreted relative to the current working directory.

```python
with open("data/survey.csv") as file:
    ...
```

This says: starting in the current working directory, locate a folder named `data`, then open `survey.csv` inside it.

A relative path works well when projects use a predictable directory structure:

```text
project/
├── data/
│   └── survey.csv
├── output/
├── src/
│   └── analyze_survey.py
└── README.md
```

If Python runs from `project/`, this relative path works:

```python
"data/survey.csv"
```

### The current working directory

The **current working directory** is the folder from which Python resolves relative file paths.

Inspect it with `Path.cwd()`:

```python
from pathlib import Path

print(Path.cwd())
```

Possible output:

```text
/home/student/ifi8410-project
```

List its immediate contents:

```python
from pathlib import Path

for item in Path.cwd().iterdir():
    print(item)
```

### The common `FileNotFoundError`

At this stage, a `FileNotFoundError` is usually a path problem rather than a programming-logic problem.

```python
with open("data/survey.csv", encoding="utf-8") as file:
    contents = file.read()
```

If Python reports:

```text
FileNotFoundError: [Errno 2] No such file or directory: 'data/survey.csv'
```

check systematically:

1. Is the filename spelled exactly correctly?
2. Does capitalization match? On many systems, `Survey.csv` and `survey.csv` are different files.
3. Is the extension correct, such as `.csv` versus `.CSV` or `.txt`?
4. Does the `data` directory exist in the working directory?
5. Is Python running from the directory you expected?
6. Is a notebook using a different working directory than the terminal?
7. Is the file actually in Downloads, Desktop, or another folder rather than in the project?

### Use `pathlib` for paths

Python's `pathlib` module provides readable and portable path handling.

```python
from pathlib import Path

input_path = Path("data") / "survey.csv"
output_path = Path("output") / "summary.txt"

print(input_path)
```

The `/` operator constructs a path in an operating-system-appropriate way.

A more robust input check:

```python
from pathlib import Path

input_path = Path("data") / "survey.csv"

if not input_path.exists():
    raise FileNotFoundError(f"Input file not found: {input_path.resolve()}")

print(f"Reading from: {input_path.resolve()}")
```

A good error message should tell the user what failed and where Python looked.

---

## Reading and writing text files

A plain-text file is a sequence of characters, typically organized into lines. Examples include:

- `.txt`
- `.csv`
- `.json`
- `.jsonl`
- `.log`
- `.md`
- `.py`

### Opening text files safely

Use a context manager:

```python
with open("data/notes.txt", mode="r", encoding="utf-8") as file:
    contents = file.read()

print(contents)
```

The standard pattern is:

```python
with open(path, mode, encoding) as file:
    # Work with the file here.
```

The `with` block closes the file automatically after the block exits, including if an error occurs.

### Why not close files manually?

Manual closing can work:

```python
file = open("data/notes.txt", mode="r", encoding="utf-8")
contents = file.read()
file.close()
```

But it is fragile. If an error occurs before `file.close()`, Python never reaches the closing operation.

```python
file = open("data/notes.txt", mode="r", encoding="utf-8")
contents = file.read()

result = 10 / 0

file.close()
```

In contrast, this safely closes the file even though the calculation fails:

```python
with open("data/notes.txt", mode="r", encoding="utf-8") as file:
    contents = file.read()
    result = 10 / 0
```

### Common file modes

| Mode | Meaning | Typical use |
|---|---|---|
| `"r"` | Read an existing file | Reading input data |
| `"w"` | Write a file, replacing existing contents | Creating a fresh output file |
| `"a"` | Append to the end of an existing file | Adding logs or records |
| `"x"` | Create a file, failing if it already exists | Preventing accidental overwrite |
| `"rb"` | Read binary data | Images, PDFs, serialized data |
| `"wb"` | Write binary data | Images, PDFs, serialized data |

For introductory text processing, the most important modes are `"r"` and `"w"`.

### Use explicit UTF-8 encoding

Use `encoding="utf-8"` for text unless a project specifies another encoding.

```python
with open("data/comments.txt", mode="r", encoding="utf-8") as file:
    contents = file.read()
```

UTF-8 supports standard English text, accented names, and many non-English writing systems. Specifying an encoding helps code behave consistently across machines.

### Process a file line by line

For small files, `file.read()` is convenient. For large files, or when records should be handled independently, iterate through the file.

```python
with open("data/notes.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        print(line)
```

Each line generally ends with a newline character, `"\n"`. Since `print()` also adds a newline, this may display blank lines.

Remove trailing whitespace and newline characters with `rstrip()`:

```python
with open("data/notes.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.rstrip()
        print(clean_line)
```

Use `strip()` only when removing whitespace from both ends is appropriate:

```python
clean_line = line.strip()
```

Be deliberate:

- `rstrip()` removes trailing whitespace, including line endings.
- `strip()` removes both leading and trailing whitespace.
- Neither operation is universally correct data cleaning; it is a specific transformation that must match project requirements.

### Example: count non-empty lines

```python
from pathlib import Path

input_path = Path("data") / "notes.txt"
nonempty_line_count = 0

with open(input_path, mode="r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            nonempty_line_count += 1

print(f"Non-empty lines: {nonempty_line_count}")
```

This follows a useful general pattern:

1. Define an input path.
2. Open the file safely.
3. Process records one at a time.
4. Accumulate a result.
5. Report a clear summary.

### Handle a header row

A structured text file often has a header line that labels columns.

Example `students.txt`:

```text
student_id,name,program
1001,Amina Patel,MS Data Science
1002,Jordan Lee,MS Analytics
1003,Carlos Rivera,MS Data Science
```

If processing as generic text, explicitly consume the first line:

```python
with open("data/students.txt", mode="r", encoding="utf-8") as file:
    header = next(file).rstrip()
    print(f"Header: {header}")

    for line in file:
        record = line.rstrip()
        print(record)
```

The expression `next(file)` retrieves the next line from the file iterator.

For a more robust approach that handles an empty file:

```python
with open("data/students.txt", mode="r", encoding="utf-8") as file:
    header = next(file, None)

    if header is None:
        print("The input file is empty.")
    else:
        print(f"Header: {header.rstrip()}")

        for line in file:
            print(line.rstrip())
```

### Write a text file

```python
from pathlib import Path

output_path = Path("output") / "summary.txt"
output_path.parent.mkdir(exist_ok=True)

with open(output_path, mode="w", encoding="utf-8") as file:
    file.write("Survey Summary\n")
    file.write("==============\n")
    file.write("Records processed: 125\n")
    file.write("Records retained: 119\n")
```

The line:

```python
output_path.parent.mkdir(exist_ok=True)
```

creates the output directory if it does not already exist.

#### Important behavior of `"w"`

Opening a file in `"w"` mode creates it if it does not exist. If it does exist, `"w"` replaces its existing contents.

Use append mode when you need to preserve existing content:

```python
with open("output/run_log.txt", mode="a", encoding="utf-8") as file:
    file.write("Processed survey.csv successfully.\n")
```

### Verify outputs by reading them back

Do not assume a successful write means that the output is correct.

```python
from pathlib import Path

output_path = Path("output") / "summary.txt"

with open(output_path, mode="r", encoding="utf-8") as file:
    print(file.read())
```

A basic professional habit is:

\[
\text{Write output} \rightarrow \text{Inspect output} \rightarrow \text{Validate against expectations}
\]

Verification can include:

- Confirming that the output file exists.
- Checking the expected number of records.
- Checking headers and column names.
- Reviewing a small sample of rows.
- Checking that summary values are plausible.
- Comparing a test output with an expected result.

---

## CSV data files

CSV stands for **comma-separated values**. It is a common text convention for storing tabular data.

Example:

```csv
student_id,name,program,gpa
1001,Amina Patel,MS Data Science,3.8
1002,Jordan Lee,MS Analytics,3.6
1003,Carlos Rivera,MS Data Science,3.9
```

A CSV file typically has:

- One row per record.
- One field per column.
- A delimiter, commonly a comma.
- Often a header row that names the columns.

### CSV is a convention, not a complete data model

CSV is simple and widely supported, but it leaves important details open. Data can include:

- Quoted values.
- Commas embedded inside a field.
- Newlines embedded inside quoted values.
- Empty or missing fields.
- Semicolon, tab, or other delimiters.
- Different encodings.
- Inconsistent column counts.
- Dates and numeric values represented as text.

For example:

```csv
student_id,name,city
1001,"Patel, Amina",Atlanta
```

This is why manually splitting on commas is unsafe:

```python
fields = line.split(",")
```

The comma within `"Patel, Amina"` is data, not a column boundary.

Use Python's built-in `csv` module for actual CSV processing.

### Read CSV with `csv.reader`

```python
import csv

with open("data/students.csv", mode="r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Each row is a list of strings:

```python
['student_id', 'name', 'program', 'gpa']
['1001', 'Amina Patel', 'MS Data Science', '3.8']
['1002', 'Jordan Lee', 'MS Analytics', '3.6']
```

Use `newline=""` when working with the `csv` module so it can handle platform-specific line endings correctly.

#### Handle a CSV header

```python
import csv

with open("data/students.csv", mode="r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)

    header = next(reader)
    print(f"Columns: {header}")

    for row in reader:
        print(row)
```

With `csv.reader`, column values are accessed by position:

```python
student_id = row[0]
name = row[1]
program = row[2]
gpa = float(row[3])
```

This works, but becomes difficult to read and brittle if column order changes.

### Prefer `csv.DictReader`

`csv.DictReader` reads rows as dictionaries using the header values as keys.

```python
import csv

with open("data/students.csv", mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["program"])
```

Possible output:

```text
Amina Patel MS Data Science
Jordan Lee MS Analytics
Carlos Rivera MS Data Science
```

This is clearer than numeric indexing:

```python
gpa = float(row["gpa"])
```

rather than:

```python
gpa = float(row[3])
```

### Validate required columns

A program should check whether required columns are present before processing records.

```python
import csv

required_columns = {"student_id", "name", "program", "gpa"}

with open("data/students.csv", mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    actual_columns = set(reader.fieldnames or [])

    missing_columns = required_columns - actual_columns

    if missing_columns:
        raise ValueError(
            f"Input file is missing required columns: {sorted(missing_columns)}"
        )

    for row in reader:
        print(row["student_id"], row["name"])
```

This is an example of a **data contract**: the program explicitly defines the structure it requires from input data.

### Write CSV with `csv.DictWriter`

```python
import csv
from pathlib import Path

output_path = Path("output") / "program_counts.csv"
output_path.parent.mkdir(exist_ok=True)

fieldnames = ["program", "student_count"]

rows = [
    {"program": "MS Analytics", "student_count": 18},
    {"program": "MS Data Science", "student_count": 27},
]

with open(output_path, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)
```

The resulting file:

```csv
program,student_count
MS Analytics,18
MS Data Science,27
```

The `fieldnames` list is the output schema. It documents expected columns and gives their output order.

### Verify a generated CSV

```python
import csv

with open("output/program_counts.csv", mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

Possible output:

```python
{'program': 'MS Analytics', 'student_count': '18'}
{'program': 'MS Data Science', 'student_count': '27'}
```

CSV values are read as strings by default. Convert values explicitly when appropriate:

```python
count = int(row["student_count"])
```

---

## JSON data files

JSON stands for **JavaScript Object Notation**. Despite its name, it is language-independent and widely used for APIs, configuration files, experiment metadata, web services, event data, machine-learning datasets, and data exchange.

Python's built-in `json` package converts between JSON and Python values.

```python
import json
```

### JSON values and Python equivalents

| JSON value | Python equivalent | Example |
|---|---|---|
| Object | `dict` | `{"name": "Amina", "gpa": 3.8}` |
| Array | `list` | `["Python", "SQL", "R"]` |
| String | `str` | `"MS Data Science"` |
| Number | `int` or `float` | `1001`, `3.8` |
| Boolean | `True` or `False` | `true` becomes `True` |
| Null | `None` | `null` becomes `None` |

JSON requires lowercase keywords:

```json
true
false
null
```

Python uses:

```python
True
False
None
```

This distinction is important when manually creating or editing JSON files.

### Example JSON file

Suppose `data/students.json` contains one complete JSON value: an array of student records.

```json
[
  {
    "student_id": "1001",
    "name": "Amina Patel",
    "program": "MS Data Science",
    "gpa": 3.8,
    "courses": ["Python Programming", "Data Management"],
    "international": false
  },
  {
    "student_id": "1002",
    "name": "Jordan Lee",
    "program": "MS Analytics",
    "gpa": 3.6,
    "courses": ["Statistical Modeling"],
    "international": true
  }
]
```

Each student is an object. The whole file is an array containing objects.

Unlike a flat CSV row, a JSON object can include nested structures naturally:

```json
{
  "student_id": "1001",
  "name": "Amina Patel",
  "contact": {
    "email": "amina@example.edu",
    "city": "Atlanta"
  },
  "courses": ["Python Programming", "Data Management"]
}
```

Here:

- `contact` is a nested object.
- `courses` is an array.
- The data can represent structures that would be awkward to store in a single flat CSV row.

### Read JSON with `json.load()`

Use `json.load()` to read JSON from an open file.

```python
import json
from pathlib import Path

input_path = Path("data") / "students.json"

with open(input_path, mode="r", encoding="utf-8") as file:
    students = json.load(file)

print(students)
```

After loading, `students` is an ordinary Python list containing dictionaries.

```python
print(type(students))
print(type(students[0]))
```

Expected output:

```text
<class 'list'>
<class 'dict'>
```

Access values as ordinary dictionary and list values:

```python
for student in students:
    print(student["name"], student["program"])
```

### Read nested JSON values

```python
student = {
    "student_id": "1001",
    "name": "Amina Patel",
    "contact": {
        "email": "amina@example.edu",
        "city": "Atlanta",
    },
    "courses": ["Python Programming", "Data Management"],
}

print(student["contact"]["email"])
print(student["courses"][0])
```

Expected output:

```text
amina@example.edu
Python Programming
```

### Validate JSON structure

A program should not assume that every JSON file contains the expected kind of object or list.

```python
import json

with open("data/students.json", mode="r", encoding="utf-8") as file:
    students = json.load(file)

if not isinstance(students, list):
    raise ValueError("Expected the JSON file to contain a list of student records.")

for student in students:
    if not isinstance(student, dict):
        raise ValueError("Each student record must be a JSON object.")

    required_fields = {"student_id", "name", "program"}
    missing_fields = required_fields - set(student)

    if missing_fields:
        raise ValueError(
            f"Student record is missing fields: {sorted(missing_fields)}"
        )
```

### Write JSON with `json.dump()`

Use `json.dump()` to write a Python object to a JSON file.

```python
import json
from pathlib import Path

students = [
    {
        "student_id": "1001",
        "name": "Amina Patel",
        "program": "MS Data Science",
        "gpa": 3.8,
    },
    {
        "student_id": "1002",
        "name": "Jordan Lee",
        "program": "MS Analytics",
        "gpa": 3.6,
    },
]

output_path = Path("output") / "students_copy.json"
output_path.parent.mkdir(exist_ok=True)

with open(output_path, mode="w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)
```

The argument `indent=2` makes the output readable for debugging, review, small datasets, and configuration files.

Use `ensure_ascii=False` when you want readable non-ASCII names and text:

```python
with open(output_path, mode="w", encoding="utf-8") as file:
    json.dump(students, file, indent=2, ensure_ascii=False)
```

### Verify JSON output

```python
import json

with open("output/students_copy.json", mode="r", encoding="utf-8") as file:
    saved_students = json.load(file)

if saved_students == students:
    print("Verification successful: saved JSON matches the original data.")
else:
    print("Verification failed: saved JSON differs from the original data.")
```

### `load()` / `loads()` and `dump()` / `dumps()`

| Function | Input | Result |
|---|---|---|
| `json.load(file)` | Open file object | Reads JSON into a Python object |
| `json.loads(text)` | JSON-formatted string | Converts a string into a Python object |
| `json.dump(data, file)` | Python object and open file | Writes JSON to the file |
| `json.dumps(data)` | Python object | Returns JSON-formatted text as a string |

The final `s` in `loads()` and `dumps()` refers to a **string**.

Example JSON text in a Python string:

```python
import json

json_text = """
{
  "student_id": "1001",
  "name": "Amina Patel",
  "gpa": 3.8
}
"""

student = json.loads(json_text)

print(student["name"])
```

Example of creating JSON text:

```python
import json

student = {
    "student_id": "1001",
    "name": "Amina Patel",
    "gpa": 3.8,
}

json_text = json.dumps(student, indent=2)

print(json_text)
```

Use `load()` and `dump()` for files. Use `loads()` and `dumps()` for strings.

---

## JSON Lines / JSONL files

**JSON Lines**, commonly called **JSONL**, stores one complete JSON value per line. It is also called newline-delimited JSON or NDJSON.

Typical filenames include:

```text
students.jsonl
events.jsonl
model_outputs.ndjson
application.log.jsonl
```

Example `data/students.jsonl`:

```json
{"student_id": "1001", "name": "Amina Patel", "program": "MS Data Science", "gpa": 3.8}
{"student_id": "1002", "name": "Jordan Lee", "program": "MS Analytics", "gpa": 3.6}
{"student_id": "1003", "name": "Carlos Rivera", "program": "MS Data Science", "gpa": 3.9}
```

Every non-empty line is valid JSON by itself. The entire file is not one JSON array, so this will not work:

```python
json.load(file)
```

A JSONL file contains multiple top-level JSON objects rather than one complete top-level JSON object or array.

### Why JSONL exists

JSONL is useful when data consists of many independent records.

Benefits include:

- Process one record at a time without loading a large dataset into memory.
- Append a new record easily.
- Stream records from logs, APIs, event systems, or model pipelines.
- Divide large datasets across files or partitions.
- Isolate malformed data to a specific line more easily.
- Support common machine-learning, LLM evaluation, and data-engineering workflows.

For example, an LLM evaluation process might write one record per prompt containing the prompt ID, model name, response, score, timing, and metadata. JSONL lets the workflow save records incrementally as they are generated.

### Read JSONL files

Read a JSONL file line by line and parse each non-empty line with `json.loads()`.

```python
import json
from pathlib import Path

input_path = Path("data") / "students.jsonl"
students = []

with open(input_path, mode="r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        student = json.loads(line)
        students.append(student)

print(f"Read {len(students)} student records.")
```

For a large input file, process each record immediately rather than loading every record into a list.

```python
import json

with open("data/students.jsonl", mode="r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()

        if not line:
            continue

        student = json.loads(line)
        print(student["student_id"], student["name"])
```

### Report JSONL parsing errors clearly

```python
import json

with open("data/students.jsonl", mode="r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()

        if not line:
            continue

        try:
            student = json.loads(line)
        except json.JSONDecodeError as error:
            raise ValueError(
                f"Invalid JSON on line {line_number}: {error.msg}"
            ) from error

        print(student)
```

A message such as "Invalid JSON on line 8423" is much more useful than a generic parsing failure.

### Write JSONL files

Write one compact JSON value per line.

```python
import json
from pathlib import Path

students = [
    {
        "student_id": "1001",
        "name": "Amina Patel",
        "program": "MS Data Science",
        "gpa": 3.8,
    },
    {
        "student_id": "1002",
        "name": "Jordan Lee",
        "program": "MS Analytics",
        "gpa": 3.6,
    },
]

output_path = Path("output") / "students.jsonl"
output_path.parent.mkdir(exist_ok=True)

with open(output_path, mode="w", encoding="utf-8") as file:
    for student in students:
        json_line = json.dumps(student, ensure_ascii=False)
        file.write(json_line + "\n")
```

The output contains one JSON record per line:

```json
{"student_id": "1001", "name": "Amina Patel", "program": "MS Data Science", "gpa": 3.8}
{"student_id": "1002", "name": "Jordan Lee", "program": "MS Analytics", "gpa": 3.6}
```

### Append to JSONL

JSONL supports append mode naturally.

```python
import json

new_student = {
    "student_id": "1003",
    "name": "Carlos Rivera",
    "program": "MS Data Science",
    "gpa": 3.9,
}

with open("output/students.jsonl", mode="a", encoding="utf-8") as file:
    file.write(json.dumps(new_student, ensure_ascii=False) + "\n")
```

Appending to a conventional JSON array is more complicated because the program must preserve valid commas and closing brackets. JSONL avoids this issue because each record is independent.

### JSON versus JSONL

| Feature | JSON | JSONL / NDJSON |
|---|---|---|
| Basic structure | One complete JSON value in the entire file | One JSON value per line |
| Common top-level structure | Object or array | Usually one object per line |
| Reading | `json.load(file)` | Loop through lines with `json.loads(line)` |
| Writing | `json.dump(data, file)` | Loop through records with `json.dumps(record)` |
| Typical use | Configuration, metadata, nested documents | Logs, events, large datasets, model records |
| Appending records | Awkward if the root is an array | Simple using append mode |
| Large-file processing | May require loading one large object or array | Naturally supports record-by-record streaming |
| Error isolation | One error can invalidate the entire document | Errors can often be located to a line number |
| Best fit | One coherent structured document | Many repeated, independent observations |

A regular JSON file answers:

> What is this complete structured document?

A JSONL file answers:

> What are the many individual records in this stream or collection?

The file extension is only a convention. Programs should validate actual content rather than assume that a `.json` or `.jsonl` extension guarantees a valid structure.

---

## Choosing CSV, JSON, or JSONL

CSV, JSON, and JSONL serve different project needs.

| Feature | CSV | JSON | JSONL |
|---|---|---|---|
| Primary structure | Flat rows and columns | Objects, arrays, nested values | One JSON object or value per line |
| Best for | Spreadsheet-style tables | Structured documents and nested metadata | Streams or collections of independent records |
| Nested data | Awkward; generally requires flattening | Natural | Natural within each record |
| Typical reader | `csv.DictReader` | `json.load()` | `json.loads()` per line |
| Spreadsheet compatibility | Excellent | Limited | Limited |
| Large-file streaming | Possible row by row | Less convenient for a giant array | Natural and efficient |
| Appending records | Possible but schema-sensitive | Awkward for arrays | Simple |
| Typical use | Reports, exports, simple datasets | APIs, configuration, experiment metadata | Logs, event data, LLM records, large pipelines |

### When CSV is a good fit

A simple daily measurement table:

```csv
date,station_id,temperature_c,precipitation_mm
2026-09-01,ATL-01,29.4,0.0
2026-09-02,ATL-01,28.9,4.2
```

CSV is useful when every record has the same fixed fields and users need compatibility with spreadsheet tools.

### When JSON is a good fit

A research experiment with nested settings and results:

```json
{
  "experiment_id": "exp-2026-001",
  "researcher": {
    "name": "Amina Patel",
    "department": "Information Systems"
  },
  "parameters": {
    "model": "random_forest",
    "trees": 500,
    "random_seed": 42
  },
  "metrics": {
    "accuracy": 0.91,
    "f1_score": 0.88
  },
  "artifacts": [
    "output/model.pkl",
    "output/evaluation.csv"
  ]
}
```

Representing this faithfully in one CSV would require awkward conventions or multiple related files.

### When JSONL is a good fit

A collection of independent model-evaluation records:

```json
{"prompt_id": "p001", "model": "model-a", "score": 0.92, "duration_seconds": 1.8}
{"prompt_id": "p002", "model": "model-a", "score": 0.87, "duration_seconds": 2.1}
{"prompt_id": "p003", "model": "model-a", "score": 0.95, "duration_seconds": 1.6}
```

Each evaluation can be read, processed, written, retried, or appended independently.

---

## JSON data-quality concerns

JSON avoids some CSV-specific problems, but it introduces other issues that require explicit decisions.

### Schema inconsistency

Records may have different keys:

```json
{"student_id": "1001", "name": "Amina Patel", "gpa": 3.8}
{"student_id": "1002", "name": "Jordan Lee"}
```

The second record does not contain `gpa`.

Use `.get()` when a value is optional:

```python
gpa = student.get("gpa")
```

Or reject incomplete records when the field is required:

```python
if "gpa" not in student:
    raise ValueError("Student record is missing a required gpa field.")
```

### Type inconsistency

These values appear related but have different types and meanings:

```json
{"gpa": 3.8}
{"gpa": "3.8"}
{"gpa": null}
{"gpa": "not available"}
```

A robust program must define acceptable types and define what happens when values are missing or invalid.

### Nested data

Nested JSON can accurately represent complex real-world information. It can also make analysis more difficult. Teams should decide whether nested fields should be:

- Retained as metadata.
- Flattened into columns.
- Normalized into separate related tables or files.
- Converted to another format for a particular analysis tool.

### Large JSON arrays

A JSON file with one huge array can be inconvenient because `json.load()` commonly loads the entire array into memory. When records are independent and input is large, JSONL is often a better operational format.

---

## Complete example: JSONL input to CSV output

The following program reads event records from JSONL, validates them, counts events by type, and writes a CSV summary.

The conceptual pipeline is:

```text
JSONL input ──▶ Python processing ──▶ CSV summary
```

Example input file, `data/events.jsonl`:

```json
{"event_id": "e001", "user_id": "u101", "event_type": "login"}
{"event_id": "e002", "user_id": "u101", "event_type": "view_report"}
{"event_id": "e003", "user_id": "u102", "event_type": "login"}
{"event_id": "e004", "user_id": "u101", "event_type": "login"}
```

Program:

```python
from collections import Counter
from pathlib import Path
import csv
import json

def read_events(input_path):
    """Read event records from a JSONL file."""
    events = []

    with open(input_path, mode="r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                event = json.loads(line)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid JSON on line {line_number}: {error.msg}"
                ) from error

            if "event_type" not in event:
                raise ValueError(
                    f"Missing event_type on line {line_number}."
                )

            events.append(event)

    return events

def count_event_types(events):
    """Count events by event type."""
    return Counter(event["event_type"] for event in events)

def write_event_summary(event_counts, output_path):
    """Write event counts as a CSV file."""
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = ["event_type", "event_count"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for event_type, count in sorted(event_counts.items()):
            writer.writerow(
                {
                    "event_type": event_type,
                    "event_count": count,
                }
            )

def main():
    input_path = Path("data") / "events.jsonl"
    output_path = Path("output") / "event_summary.csv"

    if not input_path.exists():
        raise FileNotFoundError(
            f"Input file not found: {input_path.resolve()}"
        )

    events = read_events(input_path)
    event_counts = count_event_types(events)
    write_event_summary(event_counts, output_path)

    print(f"Read {len(events)} events.")
    print(f"Wrote summary to: {output_path.resolve()}")

    for event_type, count in sorted(event_counts.items()):
        print(f"{event_type}: {count}")

if __name__ == "__main__":
    main()
```

Potential output file, `output/event_summary.csv`:

```csv
event_type,event_count
login,3
view_report,1
```

This example illustrates:

- Explicit input and output locations.
- Record-by-record processing of JSONL input.
- Early validation and useful error messages.
- Separation of file handling, analysis, and writing responsibilities.
- A clear summary for a user or operator.
- A script that can be rerun from a terminal.

## Key takeaways

- Files provide persistence: they allow data and results to outlive a notebook or Python session.
- Relative paths make projects portable, but they resolve against the current working directory.
- Many early `FileNotFoundError` problems are path problems.
- Use `with open(...)` to close files safely and clearly.
- Text files are sequences of lines; process them line by line when appropriate.
- Use CSV for flat, spreadsheet-like tables, and use the `csv` module rather than splitting lines on commas manually.
- Use JSON for structured documents, nested metadata, APIs, and configurations: `json.load()` and `json.dump()` for files, `json.loads()` and `json.dumps()` for strings.
- Use JSONL for large collections of independent records, logs, streams, event data, and incremental outputs; read it record by record and parse each line with `json.loads()`.
- Validate input file existence, expected columns, expected JSON fields, and data types before analysis.
- Keep raw inputs separate from generated outputs, and read output files back after writing them as a basic verification practice.
