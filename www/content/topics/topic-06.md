---
date: 2026-09-30
classdates: '2026-09-30'
draft: false
title: 'Unix File System and Command Line'
concept: "The file system as a tree. Absolute and relative paths, the working directory, and the home directory. The Unix philosophy of small composable tools; permissions as a model of access."
practice: "`pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`; redirection and pipes; running scripts from the shell; basic permissions. In-class: guided terminal workflow exercise."
weight: 60
numsession: 6
---
## Concept
Build a clear model of the file system as a hierarchical tree with a single root, and locate the concepts students have been using implicitly: the working directory, the home directory, `.` and `..`, and how an absolute path differs from a relative one. Introduce the Unix design philosophy — many small programs that each do one thing and communicate through text streams — and present standard input, standard output, and standard error as the channels that make composition possible. Explain redirection and pipes as ways to reconnect those channels, which is what turns individual commands into a workflow. Cover the permission model (read, write, execute for user, group, and others) as an answer to who may do what with a file, and note that `rm` has no undo, so command-line power comes with a corresponding need for care.

## Practice
Practice the core commands: `pwd`, `ls` with useful flags, `cd`, `mkdir -p`, `cp`, `mv`, `rm`, plus `cat`, `less`, `head`, `tail`, and `wc` for inspecting files. Build a directory tree, move files into it, and verify the result. Use redirection (`>`, `>>`) and pipes to chain commands, for example counting matching lines with `grep` and `wc -l`, and saving a script's output to a file. Run last session's Python script from the shell, including passing a filename as an argument. Show `chmod` and an executable script, and demonstrate tab completion, command history, and wildcards as everyday efficiency. In-class activity: a guided terminal workflow exercise from an empty directory to an organized, runnable result. Homework: organize files, run scripts from the shell, and demonstrate correct command-line usage.

