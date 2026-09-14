# Session 5: Files, Modules, and Scripts

The step from code that worked once in a notebook to a program someone else can
rerun. Files let data and results outlive a kernel session; modules let code be
written once and imported everywhere; a script with a single entry point runs
the whole workflow from a terminal, from a clean start, the same way every time.

Both notebooks keep using the campus coffee-cart table from Sessions 3 and 4,
and the Session 4 functions `parse_price`, `group_by`, `summarize`, and
`validate_row` — now read from and written to files, then moved into modules.

## Notebooks

### 1. `Reading_and_Writing_Files_orig.ipynb`

Start here. Paths and the working directory, and why most `FileNotFoundError`s
are really working-directory problems. Reading and writing text safely with
`with open(...)`, file modes, and UTF-8. The coffee-cart table written out and
read back as CSV (and what the round trip loses), as JSON (nesting and types,
and the `int`-key surprise), and as JSON Lines (streaming, appending, and
reporting bad lines by number). It closes with validation of a messy real-world
export and a complete JSONL-to-CSV program.

### 2. `Python_Modules_and_Scripts_orig.ipynb`

Modules, imports, and namespaces; why `from x import *` and a file called
`statistics.py` both cause trouble; why importing a file runs it, and how
`if __name__ == "__main__":` prevents that. The notebook then builds a small
project — a helper module, a script with `main()`, a README, and a pytest
file — out of the coffee-cart analysis, and runs it from a terminal.

Each notebook writes only into its own workspace folder (`files_workspace/` or
`modules_workspace/`) and recreates it when re-run. Keep your own work in
`Student-Notes/`, not there.

## Objectives

- Explain how the current working directory determines where a relative path
  points, and build paths with `pathlib`.
- Read and write text files with `with open(...)`, choosing a file mode and an
  encoding deliberately.
- Read and write CSV with `csv.DictReader` and `csv.DictWriter`, and convert
  types explicitly after reading.
- Read and write JSON and JSON Lines, and choose among CSV, JSON, and JSONL for
  a given dataset.
- Validate an input file before computing from it, and verify an output by
  reading it back.
- Explain what `import` does, where Python looks for modules, and how
  namespaces prevent name collisions.
- Write a script with a `main()` function and a `__main__` guard, so it can be
  both imported and run.
- Organize a small project so raw data, outputs, code, and tests are kept apart,
  and run it from the terminal.

## Topics

- Absolute and relative paths; `Path.cwd()`, `/`, `.resolve()`, `.exists()`.
- `with open(path, mode, encoding=...)`; modes `r`, `w`, `a`, `x`; UTF-8.
- Line-by-line reading, `strip` versus `rstrip`, header lines with `next()`.
- CSV quoting, `newline=""`, `DictReader`/`DictWriter`, required columns.
- JSON types, `load`/`loads`/`dump`/`dumps`, `indent`, `ensure_ascii`.
- JSON Lines: streaming, appending, stop-or-skip policies for bad lines.
- Schema and type inconsistency; flattening nested data.
- Modules, `sys.path`, `sys.modules`, `importlib.reload`, shadowing.
- `__name__`, `main()`, and the `__main__` guard.
- Project layout, `Path(__file__)`, exit codes, a README, and a test file.
- Coding principles and a project-management checklist for data workflows.

## Call to Action

1. Work through `Reading_and_Writing_Files_orig.ipynb` (rename it first to drop
   the `_orig`). Run every cell in order and attempt each *Try it* cell.
2. Work through `Python_Modules_and_Scripts_orig.ipynb` the same way. In
   Section 8, open a real terminal (*File → New → Terminal*) and run the script
   there too.
3. Do the in-class activity at the end of each notebook.
