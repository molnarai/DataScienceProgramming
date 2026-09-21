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
Unix presents every disk, every home directory, and every data file as one tree rooted at `/`, and gives you a text interface for moving through it. Learn where you are (`pwd`), what is there (`ls`), and how to get elsewhere (`cd`), and the rest — absolute versus relative paths, `.` and `..`, `~` — stops being syntax to memorize and becomes a map you can read.
<!--more-->
The second idea is composition. Unix tools are small programs that each do one thing and speak in text streams, so redirection (`>`, `>>`) and pipes (`|`) can reconnect their input and output into a workflow no single command provides. Around that sit the practical concerns: permissions, which decide who may read, write, or execute a file; running your own Python scripts from the shell with arguments; and the care the command line demands, since `rm` has no undo.

{{<figure src="imgs/unix-creators.jpg" alt="Figure: Ken Thompson and Dennis Ritchie at a PDP-11, the machine on which Unix was developed" >}}

## Listen

{{< podcast src="https://insight-gsu-edu-msa8700-public-files-us-east-1.s3.us-east-1.amazonaws.com/podcast/why_modern_ai_still_runs_on_unix.m4a" title="Why Modern AI Still Runs on Unix" >}}

## Presentation

- [Unix File System and Command Line](../../slides/slide-06-unix/) — the blueprint of modern computing: one tree, small tools, and text flowing between them

## Read
- [The Core Ideas Behind UNIX](../../blog/unix-core-idea/) (source document for podcast)
- [UNIX File System and Command Line Interface](../../blog/unix-file-system-command-line/) 
- [UNIX References and Tutorials](../../blog/unix-reference/)

## Hands-on

Notebooks in [06-Unix-Command-Line](https://github.com/molnarai/DataScienceProgramming/tree/main/06-Unix-Command-Line)

## Homework

- [Homework 5: Unix File System and Command Line](../../assignments/assignment-05/) — due Wednesday, October 14, 2026
