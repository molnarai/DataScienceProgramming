---
date: 2026-10-07
classdates: '2026-10-07'
draft: false
title: 'Git and Reproducible Workflow'
concept: "Why version control exists: history, recovery, and accountable authorship. Commits as snapshots; the working tree, staging area, and repository. Local versus remote."
practice: "`git status`, `git add`, `git commit`, `git log`, `git diff`; `.gitignore`; remotes, push and pull; meaningful commit messages. In-class: create a repository and inspect its history."
weight: 70
numsession: 7
---
## Concept
Motivate version control from problems students already have: files named `final_v3_actually_final`, a change that broke working code with no way back, and no record of what was done when. Present a commit as a snapshot of the project with an author, a timestamp, and a message, and the repository as the sequence of those snapshots. Develop the three-area model — working tree, staging area, repository — because most beginner confusion with Git comes from not knowing which area a command acts on. Distinguish local history from a remote copy, and explain what pushing and pulling actually move. Frame commit messages as documentation written for a future reader, and connect version control to reproducibility more broadly: a project is reproducible when the code, the data references, and the sequence of changes are all recoverable, which is also what makes authorship verifiable.

## Practice
Initialize a repository and work through the everyday cycle: `git status` to see state, `git diff` to see uncommitted changes, `git add` to stage, `git commit -m` to record, and `git log` to review. Show what `.gitignore` is for and why generated files, data dumps, and notebook checkpoints usually do not belong in a repository. Connect to a remote, then push and pull, and walk through recovering a previous version of a file. Discuss commit granularity: several small, meaningful commits rather than one large drop at the deadline, which is also what the course expects in submissions. In-class activity: students create a repository, make a series of edits with separate commits, and inspect the resulting history. Homework: submit a small assignment through the Git-based workflow with multiple commits.

