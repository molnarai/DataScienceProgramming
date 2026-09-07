---
draft: false
title: IFI-8410 Course Tools
weight: 20
description: Command Line (CLI) tools for manage class content and submissions.
date: 2026-09-07
lastmod: 2026-09-07
---
# IFI8410 — Using the course commands
Command Line (CLI) tools for manage class content and submissions.
<!--more-->

*A guide for students. No prior experience with Git or the command line is
assumed. Everything here is typed into a terminal on the course server.*

You have four commands. They all start with the course number, so you never
have to remember which course you are in:

| Command | What it does |
|---|---|
| `ifi8410-status` | Checks everything and tells you where you stand. Start here. |
| `ifi8410-update` | Brings in new files from your instructor. |
| `ifi8410-test` | Saves your work and runs the automatic tests on it. |
| `ifi8410-submit` | Says "this is the version I want graded". |

Add `--help` to any of them to see its options.

---

## 1. Getting a terminal

A **terminal** is a window where you type commands. There are two ways to get
one, and they are equally good — the commands are identical in both.

### In JupyterLab

1. Open JupyterLab in your browser and log in.
2. **File → New → Terminal** (or click the **Terminal** tile in the Launcher).
3. A black window opens with a prompt that ends in `$`. Type there.

### Over SSH

From the Terminal app on a Mac, or Windows Terminal / PowerShell on Windows:

```
ssh yourid@<the server name your instructor gave you>
```

Type your password when asked. Nothing appears while you type it — that is
normal.

> **A notebook cell is not a terminal.** You *can* run these commands in a
> notebook with `%%sh`, and section 9 shows how, but a notebook cannot move you
> into a folder or turn on your Python environment. Use a terminal for those.

---

## 2. Your first command, every day

```
ifi8410-status
```

Run it the moment you sit down. It looks at everything, prints one line per
check, and then tells you what to do next. It never changes your files without
asking.

```
Course: IFI8410 - Programming for Business

⚠️  Course directory       you are in ~
✅  SSH key                ~/.ssh/id_ed25519
❌  Conda environment      none active (expected conda-python3.12)

What to do next
  The conda-python3.12 environment is not active, so your Python packages are missing.
      source conda-env conda-python3.12

Your project is not in this directory. You can work in:

  1) go to ~/IFI8410FALL2026/ifi8410-abc123 and activate conda-python3.12
  2) go to ~/IFI8410FALL2026/ifi8410-abc123
  3) activate conda-python3.12 here, without moving

Which one? [1-3, or Enter to stay here]
```

Type `1` and press Enter. You are now in your project folder with Python ready,
and you can start work. Press Enter on its own and nothing happens.

### The one-key version

```
ifi8410-status --auto
```

or `ifi8410-status -a` for short. It does the same three things — takes you to
your project, puts you on the `work` branch, turns on the Python environment —
without asking any questions. This is the fastest way to start.

---

## 3. Reading the report

| Symbol | Meaning |
|---|---|
| ✅ | Fine, nothing to do |
| ⚡ | Ordinary work waiting for you — not a problem |
| ⚠️ | Worth knowing |
| ❌ | Something is broken and needs fixing |
| ➖ | Not checked (usually because something above it failed) |

The nine rows, in the order they appear:

| Row | What it is telling you |
|---|---|
| **Course directory** | Whether you are standing in your project folder |
| **SSH key** | The ID card your account uses to talk to GitLab |
| **GitLab connection** | Whether the server answered |
| **Branch** | You should be on `work`; that is where your work belongs |
| **Your changes** | Files you have edited but not saved into Git yet, or saved but not sent |
| **Instructor updates** | New files waiting for you |
| **Submitted for grading** | Which version of your work would be graded right now |
| **Feedback** | Appears once your marked work comes back |
| **Conda environment** | Whether your Python packages are switched on |

Under the rows is **What to do next** — one line per thing that needs
attention, with the exact command underneath it. You can always copy that
command and run it.

---

## 4. The routine

```
ifi8410-status -a      →  start the day
ifi8410-update         →  get the new material
   ... do your work, in JupyterLab or an editor ...
ifi8410-test           →  save it and run the tests
   ... fix what the tests found, run ifi8410-test again ...
ifi8410-submit         →  hand it in
```

You can run any of them as many times as you like. None of them ever throws
work away.

---

## 5. `ifi8410-update` — get your instructor's new files

```
ifi8410-update
```

Run it at the start of every session and whenever `ifi8410-status` shows
`⚡ Instructor updates`.

```
Updated.
New files from your instructor are now in your repository.
Now at: 8f2c1a4 Week 3 notebook and data
```

Two things it needs first, and it will tell you if they are missing:

- you must be on the `work` branch (`ifi8410-status` offers to put you there);
- your own changes must be saved into Git first — run `ifi8410-test`, which
  saves them.

### When you and your instructor changed the same file

This is normal and nothing is lost. You will see:

```
You and your instructor have both changed things since your last update.

Nothing is lost either way: where you both changed the same file, one
version keeps the file name and the other is saved next to it.

  1) Keep my instructor's version; save mine beside it   (recommended)
  2) Keep my version; save my instructor's beside it
  3) Do nothing for now

Which one? [1]
```

Press Enter to take the recommendation. **Both versions of every file survive**
— one keeps its name, the other is saved next to it with a longer name, so you
can open them side by side and copy across anything you need.

---

## 6. `ifi8410-test` — save your work and run the tests

```
ifi8410-test
```

It shows you what it is about to save, asks once, then saves it, sends it to
GitLab, and starts the automatic tests.

```
These changes will be committed:
  - unstaged: HW01/exercise1.py
  - untracked: HW01/notes.md

Commit these changes and start testing? [y/N] y
Committed: 3d9f0aa course-test: 2026-09-07 10:15

Testing started.

Tested commit: 3d9f0aa course-test: 2026-09-07 10:15
Pushed:        work
Merged into:   testing

The pipeline is running now on testing.
A failing test changes nothing: fix the problem and run course-test again.
```

Add a note about what you did with `-m`:

```
ifi8410-test -m "finished exercise 1"
```

The tests run on the server and take a little while. You can keep working
while they do. A failing test is information, not a punishment — fix it and run
`ifi8410-test` again, as often as you like.

---

## 7. `ifi8410-submit` — hand work in for grading

```
ifi8410-submit
```

This marks the version you want graded.

```
You are about to submit:
Course: IFI8410 - Programming for Business
Branch: work  ->  grading
Current time: 2026-09-07 10:22 EDT

Submission recorded.

Submitted commit: 3d9f0aa finished exercise 1
Recorded on:      grading
Time:             2026-09-07 10:22 EDT

This is the version that will be graded.
```

Things worth knowing:

- **Submit early, submit often.** You can run it as many times as you like
  before the deadline. The newest submission is the one that counts.
- **Nothing is deleted.** Every submission stays in the history; a new one just
  moves the marker.
- `ifi8410-status` always shows you what is currently up for grading:
  `✅ Submitted for grading  this commit (3d9f0aa)` means the version on the
  server is exactly what you have now. `⚡ ... 4 newer commits not submitted`
  means you have done work since you last submitted — run `ifi8410-submit`
  again if you want it graded.
- Name the assignment if your instructor asks you to:
  `ifi8410-submit --assignment HW01`

---

## 8. Feedback

When your work has been marked, a new row appears:

```
✅  Feedback               graded-HW01-Sept-16-2026
```

and below the report:

```
Read your feedback with: git show origin/graded-HW01-Sept-16-2026 --stat
```

Copy that line and run it. Your own work is untouched by feedback.

---

## 9. The Python environment

Your course packages live in an environment called **conda-python3.12**. To
turn it on:

```
source conda-env conda-python3.12
```

To have it on automatically in every terminal from now on — do this once:

```
source conda-env --set-profile conda-python3.12
```

> **Type `source conda-env ...`, not `conda activate ...`.** On this server
> `conda` on its own is not set up in a fresh terminal; the `conda-env` helper
> does the setup for you. The word `source` matters: it lets the command change
> *your* terminal rather than a copy of it.

---

## 10. Using the commands in a notebook

You can run them from a notebook cell with `%%sh`, and this works well for
*looking*:

```
%%sh
ifi8410-status --auto
```

`--auto` is the right form in a notebook: it never reports an error to Python,
so your cell will not turn red. For just the table of rows:

```
%%sh
ifi8410-status --quiet
```

Two limits, and they are not bugs:

- **A cell cannot move you into a folder or turn on the environment.** It runs
  in a throwaway shell that disappears when the cell finishes. The commands
  know this: instead of a menu they print the two lines for you to run in a
  terminal.
- **A cell cannot ask you a question**, so no menus appear there. `ifi8410-test`
  and `ifi8410-submit` from a cell need `--yes` to answer their one question in
  advance:

  ```
  %%sh
  ifi8410-test --yes -m "week 3 exercises"
  ```

If a plain `%%sh ifi8410-status` cell ends in a red `CalledProcessError`, that
only means a ❌ row was found — the report above the traceback is the real
message. Use `--auto`, or start the cell with `%%sh --no-raise-error`.

---

## 11. When something goes wrong

Work down the report from the top: the first ❌ is usually the cause of
everything under it.

### `❌ SSH key — no ~/.ssh/id_ed25519`

You have no ID card for GitLab yet. Run the line the report gives you:

```
mkdir -p ~/.ssh && chmod 0700 ~/.ssh && ssh-keygen -t ed25519 -N '' -C 'yourid@ifi8410' -f ~/.ssh/id_ed25519
```

Then show the public half and copy the whole line it prints:

```
cat ~/.ssh/id_ed25519.pub
```

Paste it into GitLab at **https://git.insight.gsu.edu/-/user_settings/ssh_keys**
(*Add new key* → paste → *Add key*). Run `ifi8410-status` again.

### `❌ GitLab connection — cannot reach ...`

Read the sentence under it; the advice depends on the cause. Most often you are
off the university network or VPN — connect and try again. If it mentions the
host key, run the `ssh-keyscan` line it prints; that is a one-time step.

### `❌ Branch — main (your work belongs on work)`

Answer `y` when it offers to switch, or use `ifi8410-status --auto`. Your work
belongs on `work`; the other branches are managed for you.

### "Your project is not in this directory"

You are somewhere else in the file system. Pick a number from the menu, or run
`ifi8410-status --auto`.

### "You have more than one ifi8410 project on this computer"

You have cloned more than one project. Pick the one you mean from the list, or
`cd` into it first. `--auto` will not guess for you.

### "Your work is not ready to update"

`ifi8410-update` needs your changes saved into Git first. Run `ifi8410-test`,
which saves them, then update.

### You answered the menu but your terminal did not move

Your terminal session started before the tools were installed or updated. Fix
it for this session:

```
source /etc/profile.d/course-tools.sh
```

Every new login does this for you automatically.

---

## 12. Quick reference

```
ifi8410-status              check everything, then offer to fix where you stand
ifi8410-status --auto       go to the project, switch to work, activate Python
ifi8410-status --quiet      just the table of rows
ifi8410-status --offline    skip the checks that need GitLab
ifi8410-status --path       print the folder your project is in

ifi8410-update              bring in new instructor files
ifi8410-test                save your work and run the tests
ifi8410-test -m "note"      ... with a note about what you did
ifi8410-submit              hand in the version to be graded
ifi8410-submit --assignment HW01

source conda-env conda-python3.12               turn Python on now
source conda-env --set-profile conda-python3.12 turn it on in every terminal
```

Useful facts:

- Your course folder is `~/IFI8410FALL2026`.
- Your project is inside it, named by GitLab — something like `ifi8410-abc123`.
- Your work belongs on the branch called `work`.
- `~` means your home folder; `cd ~/IFI8410FALL2026/ifi8410-abc123` moves you
  into your project by hand.

---

## 13. Getting help

Run `ifi8410-status` and copy **the whole report**, including the lines under
*What to do next*, into your message to course staff. That report tells us in
one glance what your set-up looks like, and it is much faster than a
description.

None of these commands deletes your work, rewrites your history, or discards a
file you have edited. If something looks alarming, stop and ask — nothing is
lost.
