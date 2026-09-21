---
draft: false
title: "UNIX File System and Command Line Interface (CLI)"
weight: 32
description: >-
  Working in the shell: the file tree and the working directory, absolute and
  relative paths, navigating and organizing files, text streams with redirection
  and pipes, permissions, and the `os`, `pathlib`, and `sys` equivalents in Python.
date: 2026-09-21
lastmod: 2026-09-21
---


Three posts cover Unix for [Session 6](../../topics/topic-06/), and they are meant to be read together:

- [UNIX Overview: Why the Command Line Still Matters](../unix-core-idea/) — where Unix came from, how Linux, the BSDs, and macOS are related, and the ideas behind the tools.
- **UNIX File System and Command Line Interface (CLI)** (this post) — the commands themselves: paths, navigation, redirection, pipes, permissions, and the Python equivalents.
- [UNIX Reference](../unix-reference/) — tutorials, courses, and official documentation for going further.

> **Safety principle:** The command line is powerful because it acts directly. In particular, `rm` normally has no undo. Read commands before pressing Enter, and verify where you are before deleting or moving files.

---

## 1. The shell: a text-based interface to the operating system

A **terminal** is an application that presents a text interface. A **shell** is the program running inside the terminal that reads commands, starts programs, and connects programs to files or to each other.

Common Unix shells include:

- `bash` — Bourne Again Shell; common on Linux and older macOS installations.
- `zsh` — common as the default shell on modern macOS.
- `fish` — an interactive shell with different syntax in some cases.

This course uses command syntax that works in typical `bash` and `zsh` environments.

A command often has this form:

```text
command [options] [arguments]
```

For example:

```bash
ls -la projects
```

- `ls` is the command.
- `-la` contains options (also called flags).
- `projects` is an argument: the directory to list.

The shell reads the line, interprets shell syntax such as quotes, wildcards, pipes, and redirection, then launches the requested program.

### Why use a command line?

A graphical file manager is useful for browsing and occasional file operations. The command line becomes especially valuable when you need to:

- Work remotely over SSH.
- Repeat the same operation reliably.
- Process many files.
- Combine tools in a pipeline.
- Record an analysis workflow in a script.
- Integrate file operations with Python, version control, containers, schedulers, or CI/CD.

The terminal is not an alternative to programming. It is one of the environments in which programming workflows are built.

---

## 2. The Unix file system as a tree

Unix organizes files and directories as one hierarchical tree. The tree has exactly one top-level directory, named the **root directory**:

```text
/
```

Every file and directory exists somewhere beneath `/`.

A simplified Unix-like file system might look like this:

```text
/
├── bin
├── etc
├── home
│   ├── alice
│   └── peter
│       ├── Documents
│       ├── Downloads
│       └── projects
├── tmp
├── usr
└── var
```

The exact layout differs across Linux distributions, macOS, servers, and containers, but the tree model is consistent.

### Directories and files

- A **file** stores data: text, Python source code, CSV data, an image, an executable program, and so on.
- A **directory** stores references to files and other directories. It is a container that helps organize the tree.

A directory can contain other directories, which is why the structure is hierarchical.

### Root is not the home directory

Do not confuse `/` with your home directory.

- `/` is the root of the entire file system.
- `~` is shorthand for your own home directory.
- On many Linux systems, a user home directory is under `/home/username`.
- On macOS, it is usually under `/Users/username`.

For example, if your username is `student`, these could refer to different locations:

```text
/                       the root of the file system
/home/student           a typical Linux home directory
/Users/student          a typical macOS home directory
~                       shorthand expanded by the shell to the current user's home directory
```

---

## 3. Paths: naming locations in the tree

A **path** describes how to reach a file or directory in the file-system tree.

### Absolute paths

An **absolute path** begins at the root directory, `/`. It gives a location independently of the current working directory.

```bash
/home/student/ifi8410/week02/example.py
```

or, on a typical macOS system:

```bash
/Users/student/ifi8410/week02/example.py
```

Absolute paths always start with `/`.

### Relative paths

A **relative path** is interpreted relative to the current working directory. It does not begin with `/`.

```bash
week02/example.py
```

If the current working directory is:

```text
/home/student/ifi8410
```

then the relative path `week02/example.py` refers to:

```text
/home/student/ifi8410/week02/example.py
```

### The working directory

Every shell session has a **current working directory** (often abbreviated CWD). It is the directory from which relative paths are interpreted.

Use `pwd` to display it:

```bash
pwd
```

Example output:

```text
/home/student/ifi8410/week02
```

`pwd` means **print working directory**.

### Special path components

Unix provides several useful shorthand path forms:

| Notation | Meaning |
|---|---|
| `/` | Root directory |
| `~` | Your home directory (shell expansion) |
| `.` | The current directory |
| `..` | The parent of the current directory |
| `-` | In `cd -`, the previous working directory |

Examples:

```bash
cd ~              # Go to the home directory.
cd .              # Stay in the current directory.
cd ..             # Move one level upward.
cd ../data        # Move to a sibling directory named data.
cd -              # Return to the directory used immediately before this one.
```

Suppose you are in:

```text
/home/student/ifi8410/week02/scripts
```

Then:

```text
.                 means /home/student/ifi8410/week02/scripts
..                means /home/student/ifi8410/week02
../data           means /home/student/ifi8410/week02/data
../../            means /home/student/ifi8410
```

### A path-navigation example

Assume this tree:

```text
/home/student/ifi8410/
├── week01/
│   └── hello.py
└── week02/
    ├── data/
    │   └── observations.txt
    └── scripts/
        └── analyze.py
```

If your working directory is `week02/scripts`, then all of these can name the same script:

```bash
./analyze.py
/home/student/ifi8410/week02/scripts/analyze.py
```

To refer to the observation data from `scripts`, use:

```bash
../data/observations.txt
```

To run the prior week's script, use:

```bash
python ../../week01/hello.py
```

---

## 4. Navigating and inspecting directories

### `pwd`: show the current location

```bash
pwd
```

Use `pwd` whenever you are uncertain about where you are, especially before a destructive command such as `rm`.

### `ls`: list directory contents

```bash
ls
```

With no argument, `ls` lists the current directory.

```bash
ls data
```

lists the contents of `data` relative to the working directory.

Useful options:

```bash
ls -l
```

Long format. It shows permissions, link count, owner, group, size, modification time, and name.

```bash
ls -a
```

Includes entries whose names start with `.`. These are conventionally hidden configuration files and directories.

```bash
ls -h
```

Uses human-readable file sizes when combined with `-l`.

```bash
ls -la
ls -lah
```

Common combinations: long format, including hidden files, and optionally human-readable sizes.

Example:

```bash
ls -lah
```

Possible output:

```text
drwxr-xr-x  6 student staff  192 Sep 21 13:40 .
drwxr-xr-x 12 student staff  384 Sep 21 12:15 ..
-rw-r--r--  1 student staff  152 Sep 21 13:38 README.md
drwxr-xr-x  3 student staff   96 Sep 21 13:39 data
-rw-r--r--  1 student staff  841 Sep 21 13:40 analyze.py
```

The first character indicates the object type:

- `-` means a regular file.
- `d` means a directory.
- `l` means a symbolic link.

The remaining characters encode permissions, discussed later.

### `cd`: change directory

```bash
cd directory_name
```

Examples:

```bash
cd data
cd ..
cd ~/ifi8410
cd /tmp
cd
```

With no argument, `cd` typically takes you to your home directory.

A useful habit is to combine navigation with verification:

```bash
cd ~/ifi8410/week02
pwd
ls
```

---

## 5. Creating and organizing files and directories

### `mkdir`: make a directory

Create one directory:

```bash
mkdir notes
```

Create nested directories with `-p`:

```bash
mkdir -p project/{data,src,results}
```

This shell command creates:

```text
project/
├── data/
├── results/
└── src/
```

The `-p` option means “create parent directories as needed” and avoids an error if a requested directory already exists.

Without shell brace expansion, the equivalent is:

```bash
mkdir -p project/data project/src project/results
```

### `cp`: copy files and directories

Copy a file:

```bash
cp original.txt backup.txt
```

Copy into a directory:

```bash
cp observations.csv data/
```

Copy a directory recursively:

```bash
cp -r source_directory backup_directory
```

The `-r` option is required because a directory may contain additional files and directories.

### `mv`: move or rename

Move a file into a directory:

```bash
mv draft.txt notes/
```

Rename a file:

```bash
mv draft.txt final_report.txt
```

`mv` uses the same syntax for moving and renaming. The result depends on whether the final argument already names a directory.

### `rm`: remove files

Remove one file:

```bash
rm temporary.txt
```

Ask for confirmation before each removal:

```bash
rm -i temporary.txt
```

Remove an empty directory:

```bash
rmdir empty_directory
```

Remove a directory and all of its contents:

```bash
rm -r old_results
```

Use the interactive form while learning:

```bash
rm -ri old_results
```

> **Critical warning:** `rm` does not ordinarily move items to a recycle bin or trash. A command such as `rm -r` can permanently remove a directory tree. Never run a destructive command unless you have verified the target with `pwd`, `ls`, and careful reading of the full command.

Avoid dangerous habits such as using `rm -rf` automatically. The `-f` option suppresses many warnings, while `-r` recursively traverses directories. Those options can be appropriate in carefully designed scripts, but they are not a default for interactive work.

### Build and inspect a directory tree

From an empty practice directory, run:

```bash
mkdir -p unix-practice/{data/raw,data/processed,scripts,results}
cd unix-practice
pwd
ls -la
```

Create two small files:

```bash
printf 'id,value\n1,17\n2,24\n' > data/raw/measurements.csv
printf 'Hello from IFI8410\n' > scripts/greeting.txt
```

Move and copy them:

```bash
mv scripts/greeting.txt results/greeting.txt
cp data/raw/measurements.csv data/processed/measurements_copy.csv
```

Verify the result:

```bash
find . -maxdepth 3 -type f | sort
```

Expected file paths:

```text
./data/processed/measurements_copy.csv
./data/raw/measurements.csv
./results/greeting.txt
```

`find` is introduced here as a useful inspection tool. We will return to it later in the course.

---

## 6. Reading and inspecting text files

Unix tools treat text as a common interchange format. A text file can be inspected with several focused programs.

### `cat`: print a file to standard output

```bash
cat README.md
```

`cat` is convenient for short files. It prints the entire file immediately.

Avoid using `cat` for large files: the output may scroll past quickly.

### `less`: page through a file

```bash
less large_log.txt
```

Within `less`:

- Press `Space` to move forward one page.
- Press `b` to move backward one page.
- Type `/word` to search for `word`.
- Press `n` for the next search match.
- Press `q` to quit.

`less` is usually a better default for large files, logs, source files, and structured output.

### `head`: show the beginning

```bash
head data/raw/measurements.csv
```

Show a specific number of lines:

```bash
head -n 3 data/raw/measurements.csv
```

This is especially useful for checking headers and basic structure in CSV or TSV files.

### `tail`: show the end

```bash
tail application.log
```

Show the last 20 lines:

```bash
tail -n 20 application.log
```

Follow a file as new content is appended:

```bash
tail -f application.log
```

Stop a running `tail -f` with `Ctrl-C`.

### `wc`: count lines, words, and bytes

```bash
wc report.txt
```

Typical output contains line count, word count, byte count, and file name.

Common forms:

```bash
wc -l report.txt      # Number of lines
wc -w report.txt      # Number of words
wc -c report.txt      # Number of bytes
```

For CSV-style data, `wc -l` gives the number of newline-terminated records, which commonly includes a header row if one is present.

---

## 7. Unix philosophy: small programs and text streams

A central Unix design idea is often summarized as:

> Build small programs that do one thing well, and connect them.

The wording varies, and real programs may be complex, but the practical lesson is important: instead of searching for one enormous program that performs every task, combine specialized tools.

Examples:

- `grep` finds lines matching a pattern.
- `sort` orders lines.
- `uniq` collapses adjacent duplicates.
- `wc -l` counts lines.
- `head` selects an initial portion.
- `tail` selects a final portion.

Each command can read text and write text. That common interface makes them composable.

### The three standard streams

When a program runs from the shell, it conventionally has three streams:

| Stream | File descriptor | Purpose |
|---|---:|---|
| Standard input | `0` | Data sent into a program |
| Standard output | `1` | Normal results produced by a program |
| Standard error | `2` | Diagnostics, warnings, and errors |

Their conventional short names are:

```text
stdin   stdout   stderr
```

By default:

- `stdin` comes from the keyboard.
- `stdout` appears in the terminal.
- `stderr` also appears in the terminal.

Keeping normal output separate from errors matters. A data-processing command can send machine-readable results to `stdout` while sending a useful warning or traceback to `stderr`. You can save the results without accidentally mixing diagnostics into a data file.

---

## 8. Redirection: reconnecting streams to files

**Redirection** changes where a command reads input from or writes output to.

### Redirect standard output with `>`

```bash
ls -la > directory_listing.txt
```

This writes the normal output of `ls -la` into `directory_listing.txt` instead of displaying it in the terminal.

> `>` overwrites the destination file if it already exists.

### Append standard output with `>>`

```bash
date >> activity.log
```

This adds output to the end of `activity.log`, preserving existing contents.

Example:

```bash
printf 'first line\n' > notes.txt
printf 'second line\n' >> notes.txt
cat notes.txt
```

Output:

```text
first line
second line
```

### Redirect standard input with `<`

```bash
wc -l < data/raw/measurements.csv
```

This sends the file contents into `wc -l` as standard input. The output does not include the filename because `wc` was given a stream rather than a named file argument.

Many commands can accept either a filename argument or data via standard input. Both styles are useful.

### Redirect errors with `2>`

```bash
python missing_script.py 2> errors.txt
```

Normal output still appears in the terminal, while error output is written to `errors.txt`.

Redirect normal output and errors separately:

```bash
python analyze.py input.csv > results.txt 2> errors.txt
```

Redirect both streams to the same file in common shell syntax:

```bash
python analyze.py input.csv > run.log 2>&1
```

Read `2>&1` as “send stream 2 (standard error) to wherever stream 1 (standard output) is currently going.” Order matters, so write this form exactly in this order when you want both in `run.log`.

### Saving a script's output

Suppose `summary.py` prints results to standard output:

```bash
python summary.py data/raw/measurements.csv > results/summary.txt
```

Then inspect the saved result:

```bash
less results/summary.txt
```

This is useful for reproducibility: the command documents which program ran, what input it received, and where its output was stored.

---

## 9. Pipes: connecting one program to another

A **pipe**, written as `|`, sends the standard output of the command on the left to the standard input of the command on the right.

General form:

```bash
producer | consumer
```

Example:

```bash
ls -la | less
```

Here, `ls -la` produces a directory listing; `less` receives that listing and lets you page through it.

### `grep`: select matching lines

`grep` prints lines that match a text pattern.

```bash
grep 'ERROR' application.log
```

Ignore case:

```bash
grep -i 'error' application.log
```

Count matching lines directly:

```bash
grep -c 'ERROR' application.log
```

### Example: count matching lines with `grep` and `wc -l`

```bash
grep 'ERROR' application.log | wc -l
```

Step by step:

1. `grep 'ERROR' application.log` emits every line containing `ERROR`.
2. `|` connects that output to the next command.
3. `wc -l` counts the received lines.

This is a small workflow assembled from two independent tools.

### Example: find the most common values

Suppose `events.txt` contains one event label per line:

```bash
sort events.txt | uniq -c | sort -nr
```

Interpretation:

1. `sort events.txt` places identical lines next to one another.
2. `uniq -c` collapses adjacent identical lines and prefixes each with a count.
3. `sort -nr` sorts numerically (`-n`) in reverse order (`-r`), placing the largest counts first.

This pattern illustrates why Unix composition is powerful: no single tool needs to know the entire task.

### Pipes and temporary files

You could implement a multi-step process using intermediate files:

```bash
grep 'ERROR' application.log > errors_only.txt
wc -l errors_only.txt
```

That can be appropriate when the intermediate result is meaningful and should be retained. But when it is only a temporary connection, a pipe is shorter and avoids clutter:

```bash
grep 'ERROR' application.log | wc -l
```

---

## 10. Everyday shell efficiency

### Tab completion

Press the `Tab` key while typing a path, command, or filename.

For example, after creating `data/processed/measurements_copy.csv`, type:

```bash
cat data/pro<Tab>
```

The shell may complete it to:

```bash
cat data/processed/
```

Then continue:

```bash
cat data/processed/mea<Tab>
```

If there are multiple possible completions, pressing `Tab` again often displays choices.

Tab completion reduces typing and avoids many spelling mistakes. Use it constantly.

### Command history

The shell remembers previously executed commands.

- Press the up arrow to recall earlier commands.
- Press the down arrow to move forward through history.
- Type `history` to display a numbered list of commands.
- In many shells, press `Ctrl-R` and type part of a previous command to search history interactively.

Example:

```bash
history | tail
```

This displays the most recent entries in history.

Reviewing and editing a previous command is usually safer than retyping a long command manually.

### Wildcards (globbing)

The shell expands wildcard patterns into matching pathnames before a command runs.

| Pattern | Meaning |
|---|---|
| `*` | Any sequence of characters, including none |
| `?` | Exactly one character |
| `[abc]` | Exactly one character: `a`, `b`, or `c` |
| `[0-9]` | Exactly one digit in the range 0–9 |

Examples:

```bash
ls *.py
```

Lists all filenames ending in `.py` in the current directory.

```bash
cp data/raw/*.csv data/processed/
```

Copies all CSV files from `data/raw` to `data/processed`.

```bash
ls report?.txt
```

Matches `report1.txt` and `reportA.txt`, but not `report10.txt`.

> **Wildcard safety:** Always inspect what a pattern matches before using it with `rm`, `mv`, or another modifying command. First run a non-destructive command such as `printf '%s\n' pattern` or `ls pattern`.

For example:

```bash
printf '%s\n' results/*.txt
```

Only after verifying the list should you consider a modifying operation.

### Quotes and spaces in filenames

Unix permits spaces in filenames, but they create additional quoting requirements. Prefer descriptive names without spaces, often using underscores or hyphens:

```text
analysis_results.csv
analysis-results.csv
```

If a filename has spaces, quote it:

```bash
cat "my notes.txt"
```

The shell otherwise interprets spaces as separators between arguments.

---

## 11. Running Python from the shell

The shell starts Python programs just as it starts other programs.

### Run a script

```bash
python hello.py
```

On some systems, the command is `python3`:

```bash
python3 hello.py
```

Use the command configured for the course environment. In a virtual environment, activate the environment first when instructed, then run `python`.

Suppose `hello.py` contains:

```python
print("Hello, IFI8410!")
```

Run it from the directory that contains it:

```bash
python hello.py
```

Or use a relative path from elsewhere:

```bash
python scripts/hello.py
```

### Pass a filename as an argument

Suppose `line_count.py` contains:

```python
import sys

filename = sys.argv[1]

with open(filename, encoding="utf-8") as input_file:
    count = sum(1 for _ in input_file)

print(f"{filename}: {count} lines")
```

Run it with a filename argument:

```bash
python line_count.py data/raw/measurements.csv
```

The shell splits the command line into arguments and gives them to Python. Python makes them available through `sys.argv`.

For the command:

```bash
python line_count.py data/raw/measurements.csv
```

the list is conceptually:

```python
sys.argv == ["line_count.py", "data/raw/measurements.csv"]
```

The first element is the script name; later elements are command-line arguments.

### Save a Python program's output

```bash
python line_count.py data/raw/measurements.csv > results/line_count.txt
```

Inspect it:

```bash
cat results/line_count.txt
```

### Arguments versus input streams

A filename argument tells a program which named file to open:

```bash
python line_count.py data/raw/measurements.csv
```

Standard input sends data itself into the program:

```bash
cat data/raw/measurements.csv | python process_stdin.py
```

Both patterns are common. Command-line programs should make clear which interface they expect.

---

## 12. Python parallels: `os`, `pathlib`, and `sys`

The command line and Python do not compete. Python programs use operating-system services, and the same core ideas appear in Python APIs.

For modern file-path work in Python, `pathlib` is often the clearest interface. The `os` package remains important and is widely used, especially for environment variables, process-related tasks, and lower-level file-system operations.

### Conceptual mapping

| Unix concept or command | Python parallel | Notes |
|---|---|---|
| Working directory: `pwd` | `os.getcwd()` or `Path.cwd()` | Returns the current working directory |
| Change directory: `cd path` | `os.chdir(path)` | Changes the process working directory |
| Home directory: `~` | `Path.home()` or `os.path.expanduser("~")` | Finds or expands the user's home directory |
| Current directory: `.` | `Path(".")` | A relative path from the current directory |
| Parent directory: `..` | `Path("..").resolve()` or `Path.cwd().parent` | Represents or obtains a parent location |
| List directory: `ls` | `os.listdir(path)` or `Path.iterdir()` | Enumerates directory contents |
| Create directory: `mkdir -p` | `Path.mkdir(parents=True, exist_ok=True)` | Creates parent directories if necessary |
| Copy: `cp` | `shutil.copy()` / `shutil.copy2()` | `shutil` provides higher-level operations |
| Move/rename: `mv` | `shutil.move()` or `Path.rename()` | Choose based on intended behavior |
| Remove file: `rm` | `Path.unlink()` or `os.remove()` | Destructive; no automatic undo |
| Remove directory tree: `rm -r` | `shutil.rmtree()` | Highly destructive; use carefully |
| Permissions: `chmod` | `os.chmod()` or `Path.chmod()` | Uses numeric mode bits or constants |
| Command arguments | `sys.argv` | A list of command-line tokens |
| Standard input | `sys.stdin` | Text stream supplied to the process |
| Standard output | `sys.stdout` | Normal output stream |
| Standard error | `sys.stderr` | Diagnostic/error stream |
| Shell output redirection | `print(..., file=...)`, `open(...)`, `subprocess` | Python can direct output programmatically |
| Shell pipeline | `subprocess` pipes or Python iterators | Choose the clearest level of abstraction |

### Working directory in Python

```python
from pathlib import Path

print(Path.cwd())
```

Equivalent `os` version:

```python
import os

print(os.getcwd())
```

These correspond conceptually to:

```bash
pwd
```

### Listing files in Python

Shell:

```bash
ls data
```

Python with `pathlib`:

```python
from pathlib import Path

for item in Path("data").iterdir():
    print(item)
```

Python with `os`:

```python
import os

for name in os.listdir("data"):
    print(name)
```

### Creating a nested directory in Python

Shell:

```bash
mkdir -p results/2026/week02
```

Python:

```python
from pathlib import Path

Path("results/2026/week02").mkdir(parents=True, exist_ok=True)
```

### Paths should not be built by string concatenation

Avoid code such as:

```python
filename = "data/" + user_input + ".csv"
```

Prefer `Path` joining:

```python
from pathlib import Path

filename = Path("data") / f"{user_input}.csv"
```

`Path` handles platform-appropriate path separators and makes code clearer.

### Command-line arguments with `sys.argv`

```python
import sys

print(sys.argv)
```

Run:

```bash
python show_args.py alpha beta
```

Conceptual output:

```python
["show_args.py", "alpha", "beta"]
```

For robust scripts with options, defaults, help text, and validation, use `argparse` rather than manually indexing `sys.argv`.

```python
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser(description="Count lines in a text file.")
parser.add_argument("filename", type=Path)
args = parser.parse_args()

with args.filename.open(encoding="utf-8") as input_file:
    print(sum(1 for _ in input_file))
```

Then run:

```bash
python line_count.py data/raw/measurements.csv
```

### Standard streams in Python

Python's `print()` writes to standard output by default:

```python
print("Analysis complete")
```

Send a diagnostic message to standard error:

```python
import sys

print("Warning: missing values detected", file=sys.stderr)
```

Read all standard input:

```python
import sys

for line in sys.stdin:
    print(line.rstrip().upper())
```

This program can participate in a shell pipeline:

```bash
cat names.txt | python uppercase.py
```

The shell and Python are using the same stream model.

---

## 13. Permissions: who may do what?

Unix permissions regulate access to files and directories. The basic model defines permissions for three categories:

- **User** (`u`): the owner of the file.
- **Group** (`g`): users associated with the file's group.
- **Others** (`o`): everyone else.

For each category, the basic permissions are:

- **Read** (`r`)
- **Write** (`w`)
- **Execute** (`x`)

### Reading permission strings

Consider this `ls -l` output:

```text
-rwxr-xr-- 1 student staff 841 Sep 21 13:40 analyze.py
```

Break down the first field:

```text
- rwx r-x r--
| |   |   |
| |   |   +-- others: read
| |   +------ group: read and execute
| +---------- user: read, write, and execute
+------------ regular file
```

The three permission triplets are, in order:

```text
user   group   others
rwx    r-x     r--
```

### Meaning for files

For a regular file:

- `r` generally permits reading the file contents.
- `w` generally permits modifying the file contents.
- `x` permits executing it as a program or script, subject to other system constraints.

### Meaning for directories

For directories, permissions have related but distinct effects:

- `r` permits listing the names in the directory.
- `w` permits creating, deleting, or renaming entries in the directory, subject to other rules.
- `x` permits traversing/searching the directory: accessing items inside it when their names are known.

Directory permissions are often initially unintuitive. A directory is not merely a file that contains other files; it participates in path traversal.

### `chmod`: change mode (permissions)

Symbolic form:

```bash
chmod u+x analyze.py
```

Adds execute permission for the owner.

Other examples:

```bash
chmod g-w shared.txt    # Remove write permission for the group.
chmod o-r private.txt   # Remove read permission for others.
chmod u=rw,g=r,o= report.txt
```

Numeric form uses a sum of permission values:

```text
r = 4
w = 2
x = 1
```

Examples:

| Mode | Meaning |
|---:|---|
| `644` | User read/write; group read; others read |
| `600` | User read/write; no group or other access |
| `755` | User read/write/execute; group and others read/execute |
| `700` | User read/write/execute only |
|
Thus:

```bash
chmod 755 analyze.py
```

sets `rwxr-xr-x`.

### Executable scripts

A Python file can be started with the Python interpreter even when it is not marked executable:

```bash
python analyze.py
```

To run it directly as a program, it needs:

1. A **shebang** on the first line that identifies the interpreter.
2. Execute permission.

Example `analyze.py`:

```python
#!/usr/bin/env python3

print("Running analysis")
```

Then:

```bash
chmod u+x analyze.py
./analyze.py
```

Why `./analyze.py` rather than simply `analyze.py`? The `./` explicitly names the file in the current directory. For security reasons, the current directory is commonly not included in the shell's command search path.

### Permissions are not the whole security model

The basic `rwx` permission model is foundational, but modern systems may also use access control lists, capabilities, mandatory access controls, mount options, container isolation, or centralized identity systems. For everyday command-line work, start by understanding the standard owner/group/others model.

---

## 14. Guided terminal workflow activity

This activity begins in an empty directory and ends with an organized project, a runnable Python script, saved output, and a verified directory structure.

### Goal

Create this project layout:

```text
terminal-workflow/
├── data/
│   └── raw/
│       └── scores.txt
├── results/
│   └── summary.txt
└── scripts/
    └── count_passing.py
```

The script should read a filename passed on the command line and count scores of at least 70.

### Step 1: Create and enter a safe practice directory

```bash
mkdir -p ~/ifi8410-practice
cd ~/ifi8410-practice
pwd
```

Confirm that the output is a location inside your own home directory.

### Step 2: Create the project tree

```bash
mkdir -p terminal-workflow/{data/raw,scripts,results}
cd terminal-workflow
ls -la
```

### Step 3: Create a small data file

```bash
printf '82\n67\n91\n70\n58\n76\n' > data/raw/scores.txt
cat data/raw/scores.txt
```

### Step 4: Inspect the data

```bash
wc -l data/raw/scores.txt
head -n 3 data/raw/scores.txt
tail -n 2 data/raw/scores.txt
```

### Step 5: Create the Python script

Use a text editor to create `scripts/count_passing.py` with the following content:

```python
#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Usage: count_passing.py FILENAME", file=sys.stderr)
    raise SystemExit(2)

filename = sys.argv[1]

with open(filename, encoding="utf-8") as input_file:
    scores = [int(line.strip()) for line in input_file if line.strip()]

passing = [score for score in scores if score >= 70]
print(f"Total scores: {len(scores)}")
print(f"Passing scores: {len(passing)}")
```

Verify that it exists:

```bash
ls -l scripts/count_passing.py
```

### Step 6: Run the script through Python

```bash
python scripts/count_passing.py data/raw/scores.txt
```

Expected output:

```text
Total scores: 6
Passing scores: 4
```

### Step 7: Redirect results to a file

```bash
python scripts/count_passing.py data/raw/scores.txt > results/summary.txt
cat results/summary.txt
```

### Step 8: Make the script executable

```bash
chmod u+x scripts/count_passing.py
ls -l scripts/count_passing.py
./scripts/count_passing.py data/raw/scores.txt
```

### Step 9: Use a pipe for a related query

Count scores beginning with `7`, `8`, or `9` directly from the raw file:

```bash
grep '^[789]' data/raw/scores.txt | wc -l
```

Here, `^` means “beginning of the line,” and `[789]` matches one character that is `7`, `8`, or `9`.

### Step 10: Verify the final result

```bash
find . -maxdepth 3 -type f | sort
```

Also inspect the project recursively, if the `tree` command is available:

```bash
tree
```

If `tree` is unavailable, use:

```bash
find . -print | sort
```

### Reflection questions

- Which paths in the activity were relative? What would their absolute equivalents be on your machine?
- What changed when `>` was added to the Python command?
- Which program consumed the output of `grep` in the pipeline?
- Why did `./scripts/count_passing.py` require execute permission while `python scripts/count_passing.py` did not?
- How does the script know which input file to process?

---

## 15. Common errors and how to diagnose them

### “No such file or directory”

Example:

```text
cat: data/raw/scroes.txt: No such file or directory
```

Likely causes:

- A filename is misspelled.
- You are in a different working directory than expected.
- The path is relative when you intended an absolute path.
- Uppercase and lowercase letters differ. Unix paths are generally case-sensitive.

Diagnose with:

```bash
pwd
ls
ls data/raw
```

Use tab completion rather than manually retyping long names.

### “Permission denied”

Example:

```text
zsh: permission denied: ./scripts/count_passing.py
```

Likely causes:

- The file lacks execute permission.
- The file system or directory has an additional restriction.

Check permissions:

```bash
ls -l scripts/count_passing.py
```

Add owner execute permission if appropriate:

```bash
chmod u+x scripts/count_passing.py
```

Alternatively, run it through Python:

```bash
python scripts/count_passing.py data/raw/scores.txt
```

### “Command not found”

Example:

```text
zsh: command not found: analyze.py
```

Typing `analyze.py` asks the shell to search the directories listed in `PATH`. The current directory is often not searched.

Use:

```bash
./analyze.py
```

if the script is executable and in the current directory, or:

```bash
python analyze.py
```

### Accidentally overwriting a file with `>`

If `>` replaced a file you meant to preserve, recovery may be difficult. Prevent this by:

- Choosing new output filenames deliberately.
- Inspecting existing files with `ls` before redirecting.
- Using `>>` only when appending is genuinely intended.
- Keeping important work in version control or backed up.

### Treating a wildcard as a literal filename

If a wildcard matches nothing, shells may behave differently depending on configuration. Before a destructive command, preview expansion:

```bash
printf '%s\n' data/raw/*.csv
```

Do not assume a wildcard matches the files you intended.

---

## 16. Command reference

| Command | Purpose | Example |
|---|---|---|
| `pwd` | Print working directory | `pwd` |
| `ls` | List contents | `ls -lah` |
| `cd` | Change directory | `cd ../data` |
| `mkdir` | Create directory | `mkdir -p project/data/raw` |
| `cp` | Copy file or directory | `cp source.txt backup.txt` |
| `mv` | Move or rename | `mv draft.txt final.txt` |
| `rm` | Remove file | `rm -i temporary.txt` |
| `rmdir` | Remove empty directory | `rmdir empty_dir` |
| `cat` | Print file contents | `cat README.md` |
| `less` | View text interactively | `less large.txt` |
| `head` | Show first lines | `head -n 10 data.csv` |
| `tail` | Show final lines | `tail -n 20 log.txt` |
| `wc` | Count lines, words, bytes | `wc -l data.csv` |
| `grep` | Select matching lines | `grep -i 'error' log.txt` |
| `chmod` | Change permissions | `chmod u+x script.py` |
| `find` | Search/list tree contents | `find . -type f` |

### Shell operators reference

| Operator | Meaning | Example |
|---|---|---|
| `>` | Redirect stdout; overwrite file | `python script.py > output.txt` |
| `>>` | Redirect stdout; append to file | `date >> log.txt` |
| `<` | Send file to stdin | `wc -l < data.csv` |
| `2>` | Redirect stderr | `python bad.py 2> errors.txt` |
| `2>&1` | Send stderr to stdout's destination | `python script.py > run.log 2>&1` |
| `|` | Pipe stdout to next command's stdin | `grep ERROR log.txt | wc -l` |
| `*` | Wildcard for any characters | `ls *.py` |
| `?` | Wildcard for one character | `ls file?.txt` |

---

## 17. Homework: command-line file workflow

### Objective

Demonstrate that you can organize a small project, inspect files, run a Python script from the shell, pass a filename argument, use redirection or a pipeline, and explain the command-line choices you made.

### Required tasks

1. Create a directory named `ifi8410-unix-homework` in an appropriate location inside your home directory.
2. Create this structure:

```text
ifi8410-unix-homework/
├── data/
├── scripts/
├── results/
└── README.md
```

3. Place at least one text or CSV data file in `data/`.
4. Write a Python script in `scripts/` that accepts the input filename as a command-line argument. The script should produce a small, meaningful summary of the file.
5. Run the script from the shell using a relative path and redirect its standard output to a file in `results/`.
6. Use at least one pipeline involving `grep`, `wc`, `sort`, `head`, `tail`, or another standard text-processing command.
7. Make the Python script executable with `chmod` and demonstrate running it as `./scripts/your_script.py ...`.
8. In `README.md`, include:

```text
- The command used to run your script.
- The command used to save output to results/.
- The pipeline you used and what it computes.
- One absolute path and one relative path that refer to a location in your project.
- A short explanation of the difference between standard output and standard error.
```

### Suggested verification commands

```bash
cd ~/ifi8410-unix-homework
pwd
ls -lah
find . -maxdepth 2 -type f | sort
cat README.md
```

### Submission checklist

- The project structure is organized and readable.
- Paths in commands are correct.
- The script runs successfully from the shell.
- The script accepts a filename argument rather than hard-coding the input path.
- A result file was created using redirection.
- The README explains the required command-line concepts accurately.
- No large, unnecessary generated files are included.

---

## 18. Key takeaways

- Unix presents storage as a single tree rooted at `/`.
- Your working directory determines how relative paths are interpreted.
- `.` means the current directory; `..` means its parent; `~` expands to your home directory.
- `pwd`, `ls`, and `cd` are the core navigation tools.
- `mkdir`, `cp`, `mv`, and `rm` organize file-system objects; use `rm` cautiously because it normally has no undo.
- Text streams—`stdin`, `stdout`, and `stderr`—are the interfaces that let command-line programs compose.
- `>` and `>>` redirect output to files; `|` sends output from one program into another.
- Unix permissions specify read, write, and execute access for the owner, group, and others.
- A Python program launched from the shell receives command-line arguments through `sys.argv` and can use standard streams through `sys.stdin`, `sys.stdout`, and `sys.stderr`.
- Shell commands and Python modules such as `os`, `pathlib`, `shutil`, and `sys` express the same underlying operating-system concepts at different levels of abstraction.
- Use tab completion, command history, and carefully checked wildcards to work faster and more safely.
