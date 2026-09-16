+++
date = '2026-09-16'
due_date = '2026-09-29T23:59:00'
draft = false
title = 'Homework 3: Ranking Scholarship Applications'
weight = 30
status = 'Posted'
+++

Order a list of scholarship applications from the lowest review score to the highest, without `sorted()`, `.sort()`, `min()`, or `max()`. Across seven test-driven phases you will build the solution out of small functions with clear contracts: one comparison rule that settles what a tie means, a function that combines two ordered groups, a function that splits a group in two, a function that orders the groups too small to split, and a function that uses all of them to order a group of any size. Then you will add a policy for applications with missing or unusable scores and print an exactly formatted ranking report. Each phase ships with its own tests, and only at the end are you asked to name the method you have built.

<!-- more -->


Related session: [Session 4 — Functions and Decomposition](../../topics/topic-04/)


## The problem

A department has a collection of scholarship applications. Each application has
an applicant name, an application ID, and a review score.

> **Produce a new list ordered from the lowest score to the highest score,
> without using Python's built-in sorting tools.**

Python can already do this in one line. That line is banned here, and the ban is
the point: Session 4 was about **decomposition** — breaking a task into small
named functions with clear contracts — and this assignment is a task that
genuinely needs it. You will not be told the name of the method you are
building. You will build it out of five small functions, each one testable on
its own, and only at the end will you be asked what you have made.

## Learning objectives

Your program will:

1. Define one comparison rule as a function, and decide what a tie means.
2. Combine two already-ordered groups into one ordered group.
3. Divide a group into two smaller groups, and handle an odd count.
4. Order the cases too small to divide.
5. Apply the same process to smaller and smaller groups until the whole
   collection is ordered.
6. Decide and enforce a policy for applications with missing or unusable scores.
7. Print a ranking report.

The objective is not merely "produce ordered output." It is to write several
focused functions with clear inputs, outputs and responsibilities, combine them
into a larger solution, test each part independently, and revise the design when
hidden cases surface.

No pandas, no numpy, no file reading. The dataset is a list of dictionaries
defined in the starter file.

## Constraints

These are graded, and two of them are checked by tests you cannot see.

- **Do not use `sorted()`, `.sort()`, `min()`, or `max()`** anywhere in the five
  ordering functions. Building the order yourself is the assignment.
- **Do not reduce applications to a list of scores.** The result must contain
  the application dictionaries themselves, not their scores.
- **Do not modify the input.** No function changes the list it is given or the
  dictionaries inside it. Build and return something new.
- **Do not solve Phase 5 in one long block.** It must call the functions you
  wrote in Phases 1–4.
- **Every function keeps its docstring**, stating what it returns and whether it
  changes its inputs.
- **Nothing prints except `main()`.**

## How to work on this assignment

**Do not write the whole program and then run it.** The assignment is split into
seven phases. Each phase adds one function and has its own test file. Work in
this order:

1. Read the phase description.
2. Implement only the function in that phase.
3. Run that phase's tests: `./run_tests.sh 2` for Phase 2.
4. Fix your code until every test in that phase passes.
5. Only then move to the next phase.

Phase 5 calls Phases 1–4, and Phase 7 calls everything. A bug you leave behind in
Phase 2 will produce a baffling failure in Phase 5. Catching it in Phase 2 costs
a minute.

You test in two places, and they do different jobs:

| | Where | When | What it is for |
|---|---|---|---|
| **Locally** | on the cluster, `./run_tests.sh N` | constantly, while you work | Fast feedback on the phase you are writing |
| **Pipeline** | GitLab, on merge into `testing` | once a phase is done | The record of what passed; this is what counts |

The test suite is not hidden. It lives in [`../test/`](../test/) and you are
expected to read it. Editing your copy achieves nothing: the pipeline runs the
course's copy, plus additional tests you do not have.

## Setup

Start the way you start every session, then collect the assignment:

```bash
ifi8410-status --auto
ifi8410-update
cd Assignments/HW03
mkdir -p submission
cp starter/applications.py submission/applications.py
cp starter/JOURNAL.md submission/JOURNAL.md
```

### The notebook

There is a guided notebook for this assignment:

```text
Assignments/HW03/starter/Instructions_orig.ipynb
```

Rename it to drop the `_orig` before you run anything, then work through it. It
walks the seven phases in the same order as this handout, gives you cells to
experiment in, and checks each function as you write it. This handout stays the
authority on every rule; the notebook is the guided path through it. Either way,
the file you submit is `submission/applications.py`.

Your directory should then look like this:

```text
Assignments/HW03/
├── instructions/
│   └── homework03_instructions.md
├── starter/
│   ├── Instructions_orig.ipynb  <- rename it, then work in it
│   ├── applications.py          <- the untouched template; leave it alone
│   └── JOURNAL.md
├── submission/              <- everything you write goes here
│   ├── applications.py      <- the file you edit
│   └── JOURNAL.md           <- required, not graded
└── test/                    <- the test suite; read it, do not edit it
```

**Do not edit anything in `starter/`, `test/`, or `instructions/`.** Only files
under `submission/` are read as your solution, and the file must be named
`applications.py`. A later release replaces the other folders and your edits
there would be lost.

Check that the tests can find your file:

```bash
cd test
./run_tests.sh
```

You should see a long list of failures. That is correct — you have not written
anything yet. If instead you see `Could not find applications.py`, your file is
in the wrong place; re-read the tree above.

Every `./run_tests.sh` command below is run from that `test/` directory.

```bash
./run_tests.sh 2      # just Phase 2's tests
./run_tests.sh        # all of them
./run_tests.sh 3 -x   # Phase 3, stopping at the first failure
```

## The dataset

`APPLICATIONS` is defined near the top of the starter file: a list of
dictionaries, one per application, **in the order the applications arrived**.

```python
{
    "id": "A104",
    "name": "Jordan Lee",
    "score": 87,
}
```

| Field | Type | Notes |
|---|---|---|
| `id` | `str` | the application ID |
| `name` | `str` | the applicant's name |
| `score` | `int` | the review score |

Eleven applications, and the arrival order is not the score order:

```text
87  72  91  84  96  84  75  68  91  79  84
```

Two things about that list are deliberate. It has an **odd** length, so every
split is uneven. And **three applications share the score 84** while two share
91 — which forces the question Phase 1 asks you to answer.

## Required functions

Keep these names and parameter lists **exactly** as shown. You may add helper
functions, but do not remove, rename, or re-order the required ones — the tests
call them directly.

| Phase | Function | Purpose |
|---:|---|---|
| 1 | `comes_before_or_equal(first, second)` | The one comparison rule |
| 2 | `combine_ordered_groups(left, right)` | Merge two ordered groups into one |
| 3 | `split_in_half(applications)` | Divide one group into two |
| 4 | `order_small_group(applications)` | Order a group of at most two |
| 5 | `order_applications(applications)` | Order a group of any size |
| 6 | `score_of(application)` | Read a score, with a validation policy |
| 7 | `format_ranking(applications)` | Return the whole report as one string |
| 7 | `main()` | Rank `APPLICATIONS` and print the report |

---

# The phases

## Phase 1 — One comparison rule

Implement `comes_before_or_equal(first, second)`.

Both arguments are application dictionaries. Answer one question:

> Given two applications, should the first appear before or at the same position
> as the second when ordered by score?

Return `True` or `False` — a real Boolean, not a number and not a string.

Only the **score** decides. Names and IDs must not influence the answer, however
tempting alphabetical order looks.

### The decision this phase forces

What should happen when the scores are **equal**?

Your options are genuinely different, and the tests require the second one:

- Equal scores may come out in either order. Simple, but the same input can
  produce different output, which makes a ranking report impossible to check.
- **Equal scores keep the order the applications arrived in.** Dana applied
  before Ivy, so with the same score Dana is listed first. This is the rule your
  function must implement, and it is why the function is named
  `comes_before_or_equal` rather than `comes_before`: on a tie it answers
  `True`, so the first argument is taken first.

That single choice is what will make your final output reproducible. Phase 2 is
where it does its work.

```bash
./run_tests.sh 1
```

**Do not continue until every test in Phase 1 passes.**

## Phase 2 — Combine two ordered groups

Implement `combine_ordered_groups(left, right)`.

You are given two lists of applications that are **already ordered** by score:

```text
Left group:   72  84  91
Right group:  75  84  96
```

Return **one** list holding all of them, in order:

```text
Result:       72  75  84  84  91  96
```

This is the central task of the assignment. Read the constraints, not a recipe:

- Both input groups are already in nondecreasing score order.
- The result contains every application from both groups **exactly once**.
- The result is in nondecreasing score order.
- **Neither input group is changed.**
- When scores are equal, the application from `left` is taken first.

### Working it out

You are not being asked to re-order anything here. Both groups are already
ordered, which means the smallest item still unused is always at the front of one
group or the other. You only have to keep asking which of those two it is.

```text
Left:   [72, 84, 91]
          ^
Right:  [75, 84, 96]
          ^

Compare the two marked applications.
Move the earlier one into the result.
Advance the marker ONLY in the group that supplied it.
Continue until one group is exhausted.
Then take everything remaining in the other group.
```

Use `comes_before_or_equal` for the comparison. Do not write the score
comparison again by hand — Phase 1 exists so that the tie rule lives in exactly
one place.

Three things go wrong here for almost everybody, and the tests check all three:

- **The leftovers are dropped.** When one group runs out, the other still has
  applications in it. They must all arrive.
- **Both markers advance at once.** Only the group that supplied the item moves.
- **`left` or `right` gets modified.** Building the result by removing items from
  the inputs destroys the caller's data. Track positions instead.

```bash
./run_tests.sh 2
```

## Phase 3 — Divide a group in two

Implement `split_in_half(applications)`.

Return a **tuple** `(front, back)` of two new lists.

For an even count this is obvious. For an odd count you must decide which group
gets the extra application. The convention this assignment uses, which the tests
check:

```text
[A, B, C, D, E]
      │
      ├── front: [A, B]
      └── back:  [C, D, E]
```

The extra one goes to **`back`**. `len(applications) // 2` gives you the split
point: `//` divides and discards the remainder, so five applications give a
middle of 2.

- Five applications split 2 and 3.
- One application splits 0 and 1 — `front` is empty, and that is correct.
- No applications split into two empty lists.
- The input is unchanged. Slicing gives you new lists for free.

The exact convention matters less than applying it consistently, but an
inconsistent one loses an application somewhere in Phase 5, in a way that is
very hard to find.

```bash
./run_tests.sh 3
```

## Phase 4 — The cases too small to divide

Implement `order_small_group(applications)`.

This function handles **at most two** applications:

- Zero applications: return a new empty list.
- One application: return a new list containing it.
- Two applications: return them in score order, using `comes_before_or_equal`.
- More than two: raise `ValueError`. This function's contract does not cover
  them, and saying so is better than guessing.

### The observation

Writing this should make something obvious:

> A group of zero or one application is **already ordered**. There is nothing to
> do.

Say that out loud, because it is the answer to a question Phase 5 is about to
ask: *when do we stop dividing?* Write it in your journal now, in your own words,
before you read Phase 5.

```bash
./run_tests.sh 4
```

## Phase 5 — Order a group of any size

Implement `order_applications(applications)`.

> Return a new list of applications of **any length**, ordered by score from low
> to high. The original list must remain unchanged.

You have already written every piece you need. The task is to see how they fit
together:

```text
        An unordered collection
                  │
                  ▼
    Divide it into two smaller collections      ← Phase 3
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
   Order the left      Order the right          ← ??
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
      Combine the two ordered collections       ← Phase 2
                  │
                  ▼
         One ordered collection
```

The two boxes marked `??` are the interesting ones. Ordering a smaller group is
**the same job** this function already does — so it can call itself. A function
that calls itself needs a case where it stops, and Phase 4 gave you one: a group
of fewer than two applications is already ordered, so return a copy of it and
stop dividing.

That is the whole function: four or five lines.

- If the group is too small to divide, return a copy of it.
- Otherwise split it, order each half **with this same function**, and combine
  the two ordered halves.

Equal scores must still come out in arrival order. If Phase 1 and Phase 2 are
right, this happens on its own — you do not write anything extra here.

If you get `RecursionError`, your stopping case is never reached: check that the
groups really do get smaller, and that a one-application group returns instead of
dividing again.

```bash
./run_tests.sh 5
```

## Phase 6 — Deciding what bad data means

Implement `score_of(application)`, then **revise Phase 1 to use it**.

So far every application has been a dictionary with a numeric `score`. Real data
is not so obliging. Try this in a notebook cell and watch what happens:

```python
order_applications([
    {"id": "A1", "name": "Ada", "score": 84},
    {"id": "A2", "name": "Bo"},                  # no score at all
])
```

You will get a `KeyError` from somewhere deep inside your comparison — a message
about `'score'` that says nothing about *which* application was broken or what
the program expected. That is the failure this phase repairs.

`score_of(application)` returns the numeric score, and defines the policy:

| Input | Result |
|---|---|
| `{"score": 84}` | returns `84` |
| `{"score": 84.5}` | returns `84.5` |
| `{"score": 0}` | returns `0` — zero is a real score |
| `{"score": -5}` | returns `-5` — this function checks the type, not the range |
| `{"name": "Bo"}` | raises `ValueError` |
| `{"score": "87"}` | raises `TypeError` |
| `{"score": None}` | raises `TypeError` |
| `{"score": True}` | raises `TypeError` |
| `"not a dict"` | raises `TypeError` |

The two exceptions mean different things, and choosing correctly is most of this
phase:

- **`TypeError`** — the wrong **kind** of object. A string where a number
  belongs. Usually a bug in the calling code.
- **`ValueError`** — the right kind of object, an unusable **value**. A
  dictionary that simply has no score. Usually bad data.

One trap: in Python `isinstance(True, int)` is `True`, because `bool` is a
subclass of `int`. Check for `bool` **first**, or a score of `True` will quietly
be treated as `1`.

Then change `comes_before_or_equal` to call `score_of` instead of reading
`first["score"]` directly. Every ordering function goes through it, so the whole
program now reports bad data in one clear place — which is the argument for
having one accessor rather than nine dictionary lookups.

Re-run the earlier phases after you change Phase 1. They must all still pass.

```bash
./run_tests.sh 6
./run_tests.sh          # everything so far
```

## Phase 7 — The report

Implement `format_ranking(applications)` and `main()`.

### `format_ranking(applications)`

Return the entire report as **one string**. Do not print anything, and do not end
the string with a newline — `print()` adds that.

It receives applications in **any** order and orders them itself, by calling
`order_applications`.

The exact expected output for the starter dataset:

```text
SCHOLARSHIP APPLICATION RANKING
===============================

Applications ranked: 11

  1.  68  Ellis Barnes (A123)
  2.  72  Priya Raman (A118)
  3.  75  Noor Haddad (A115)
  4.  79  Ruth Adeyemi (A112)
  5.  84  Dana Whitfield (A127)
  6.  84  Ivy Chen (A131)
  7.  84  Kai Brennan (A140)
  8.  87  Jordan Lee (A104)
  9.  91  Sam Okafor (A102)
 10.  91  Tomas Novak (A136)
 11.  96  Mateo Alvarez (A109)

Lowest score: 68 (Ellis Barnes)
Highest score: 96 (Mateo Alvarez)
Applications sharing a score: 5
```

The formatting rules, precisely:

- The title is followed by a line of `=` **exactly as long as the title**, then
  one blank line.
- `Applications ranked: N`, then one blank line.
- One row per application:
  `f"{position:>3}. {score:>3}  {name} ({app_id})"` — the position
  right-aligned in a field **3** wide, a full stop, one space, the score
  right-aligned in a field **3** wide, **two** spaces, the name, then the ID in
  parentheses. Positions start at **1**, not 0.
- One blank line, then the three summary lines exactly as shown.
- `Applications sharing a score` counts every application whose score is held by
  more than one application. Here that is three 84s plus two 91s, so **5**.
- For an **empty** list: the title, `Applications ranked: 0`, a blank line, and
  the single line `No applications to rank.` — no rows and no summary.

Build the report as a **list of lines** and `"\n".join(lines)` at the end.
`enumerate(ordered, start=1)` gives you the position and the application together.

If a test fails here, read the diff pytest prints character by character. Almost
every failure in this phase is one space or one missing blank line.

### `main()`

Rank the module-level `APPLICATIONS` and print the report:

```python
def main():
    print(format_ranking(APPLICATIONS))
```

This is the one function that may use the global `APPLICATIONS`, and the only one
that prints. Run the program the way any script is run:

```bash
cd ../submission
python3 applications.py
```

```bash
./run_tests.sh 7
./run_tests.sh        # everything, one last time
```

---

## The journal

`submission/JOURNAL.md` is **required** and **not graded**. Nothing you write in
it can lower your mark; the automatic check only confirms that you wrote roughly
forty words of your own. Be honest about dead ends, about help from peers or the
instructor, and about AI tools — which one, what you asked, and whether you used,
adapted, or rejected the answer. Recording help never costs you marks.

See [`../../../Shared/ASSIGNMENT-JOURNAL.md`](../../../Shared/ASSIGNMENT-JOURNAL.md).

## In your journal, answer this

Answer these **after** Phase 5 works, and before you read the last section of
this handout:

> Look at the structure of your finished solution.
>
> - What happens to a large collection before any of it is ordered?
> - What condition makes a collection simple enough to stop dividing?
> - How are two already-ordered collections turned into one ordered collection?
> - What name would you give this repeated divide-and-combine strategy?

Then add a short note on Phase 6: which bad-data case did you try first, what did
the program do before you wrote `score_of`, and what does it do now? Three or
four sentences is plenty.

---

## Only after you have finished

<details>
<summary><b>What you have built</b> — do not open this until Phase 5 passes.</summary>

You have constructed **merge sort**.

Its central idea is exactly the one you assembled: split a large ordering task
into smaller ordering tasks, treat a collection of zero or one item as already
ordered, and combine ordered collections into a larger ordered collection. It is
the standard example of a **divide-and-conquer** algorithm, and
`combine_ordered_groups` — your Phase 2 — is the *merge* that gives it its name.

Two details you chose on purpose are worth knowing by their real names:

- Because `comes_before_or_equal` answers `True` on a tie, your sort is
  **stable**: equal items keep their original order. Python's own `sorted()` is
  stable for the same reason, and it matters whenever you sort by one column and
  want an earlier sort to survive.
- Halving the group each time is what makes the method fast. Eleven applications
  took four levels of splitting; a thousand would take ten.

You did not memorize a named procedure and then implement it. You built it from
smaller responsibilities, tested each one's claims, found the assumptions that
were incomplete, and repaired them. That is the same process used on work far
larger than this.

</details>

## Submitting

```bash
ifi8410-test -m "HW03: phase 3 complete"
ifi8410-submit
```

`ifi8410-test` saves your work, sends it to GitLab and merges it into
`testing`, which is what starts the pipeline. The `hw03` job runs your
submission against the course's copy of the tests plus additional hidden ones.
Until the last phase is done most of the pipeline will be red — that is expected.
Look for the phase you just finished and ignore the rest.
