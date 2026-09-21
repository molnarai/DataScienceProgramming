---
draft: false
title: "UNIX Reference"
weight: 33
description: >-
  Curated references for Session 6: open tutorials, LinkedIn Learning and
  O'Reilly titles available through the university, official shell and Python
  standard-library documentation, and how to read your system's own man pages.
date: 2026-09-21
lastmod: 2026-09-21
---

This reference list supports [Session 6](../../topics/topic-06/) on Unix file systems, command-line workflows, standard streams, redirection, pipes, permissions, executable scripts, and the connections between shell operations and Python's standard-library interfaces.

Three posts cover this material, and they are meant to be read together:

- [UNIX Overview: Why the Command Line Still Matters](../unix-core-idea/) — where Unix came from, how Linux, the BSDs, and macOS are related, and the ideas behind the tools.
- [UNIX File System and Command Line Interface (CLI)](../unix-file-system-command-line/) — the commands themselves: paths, navigation, redirection, pipes, permissions, and the Python equivalents.
- **UNIX Reference** (this post) — tutorials, courses, and official documentation for going further.

> **Platform note:** The GNU Coreutils documentation is the authoritative reference for common GNU/Linux command implementations. macOS and other Unix-like systems may provide BSD variants with some option differences. Students should use `man command` on their own system to consult the locally installed manual page.

## 1. Tutorials and instructional resources

The following resources are intended for learning, guided practice, and reinforcement. LinkedIn Learning and O'Reilly titles are especially appropriate for IFI8410 students because institutional access is available.

### Open educational tutorials and practice resources

- Software Carpentry. **[The Unix Shell](https://swcarpentry.github.io/shell-novice/)**. A respected, openly available, hands-on lesson series widely used in research and data-science education. It teaches navigation, files and directories, pipes and filters, loops, shell scripts, and finding things. This is particularly suitable for practice-oriented reinforcement.

- MIT Missing Semester. **[The Shell](https://missing.csail.mit.edu/2020/course-shell/)**. A rigorous, concise tutorial on shell fundamentals, including shell syntax, piping, redirection, searching, and programmatic use of the command line.

- The Linux Foundation. **[Introduction to Linux](https://training.linuxfoundation.org/training/introduction-to-linux/)**. A reputable foundational Linux learning resource. Students should use the course catalog and their available access routes to identify the current offering and modules most relevant to command-line fundamentals.

- Python Software Foundation. **[Python Tutorial](https://docs.python.org/3/tutorial/)**. The official guided introduction to Python. For this session, students should focus on the sections most relevant to scripts, modules, file input/output, errors, and command-line execution.

- W3Schools. **[Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)**. A short, beginner-friendly practice resource for opening, reading, writing, and closing files in Python. It should supplement—not replace—the official Python documentation.

- W3Schools. **[Python `os` Module](https://www.w3schools.com/python/module_os.asp)**. A quick reference and interactive-style introduction to common `os` functionality. Students should cross-check important details with the official Python `os` documentation.

- W3Schools. **[Python `sys` Module](https://www.w3schools.com/python/module_sys.asp)**. A brief reference for selected `sys` facilities; use it alongside the official `sys` documentation for `argv` and standard streams.


### LinkedIn Learning

- LinkedIn Learning. **[Unix Essential Training](https://www.linkedin.com/learning/unix-essential-training)**. A structured introductory Unix course covering command-line basics, navigating files and directories, moving/renaming/copying/deleting files, permissions, and common Unix workflows. 

- LinkedIn Learning. **[Command Basics — Unix Essential Training](https://www.linkedin.com/learning/unix-essential-training/command-basics)**. A focused lesson introducing Unix commands as small programs and directing learners to command documentation through manual pages. 

- LinkedIn Learning. **[Learning Linux Command Line](https://www.linkedin.com/learning/learning-linux-command-line)**. A practical course on Bash-based command-line work, including file-system navigation, text editing, permissions, `grep`, output redirection, and `PATH`. The associated public course-exercise repository confirms these topic areas. 

- LinkedIn Learning. **[Unix Learning Paths and Courses](https://www.linkedin.com/learning/topics/unix)**. A catalog page useful for finding additional Unix, shell, command-line data analysis, and related courses available through institutional access. 

### O'Reilly Learning

- O'Reilly Media. **[Learning the Unix Operating System, 5th Edition](https://www.oreilly.com/library/view/learning-the-unix/0596002610/ch01.html)**. A beginner-oriented introduction to Unix accounts, terminals, shells, command entry, and common problems. 

- O'Reilly Media. **[Learning Unix for Mac OS X: Syntax of a Unix Command Line](https://www.oreilly.com/library/view/learning-unix-for/0596006179/ch02s02.html)**. A concise tutorial on command structure, options, filename arguments, and wildcards. Although written for Mac OS X, its command-line concepts apply broadly to Unix-like environments. 

- O'Reilly Media. **[Unix: Visual QuickStart Guide — Working with Your Shell](https://www.oreilly.com/library/view/unix-visual-quickstart/0201353954/0201353954_ch03.html)**. An accessible reference/tutorial chapter on shells and interactive shell behavior. 

- O'Reilly Media. **[Unix: Visual QuickStart Guide — Command Completion](https://www.oreilly.com/library/view/unix-visual-quickstart/0201353954/0201353954_ch03lev1sec5.html)**. A focused explanation of Bash command completion and why it improves interactive work. 

- O'Reilly Media. **[A Practical Guide to Linux Commands, Editors, and Shell Programming](https://www.oreilly.com/library/view/a-practical-guide/0131478230/)**. A broad, detailed book for students who want a continuing reference beyond the introductory session, covering command-line utilities and shell programming. 

- O'Reilly Media. **[Unix Shell Programming, Third Edition](https://www.oreilly.com/library/view/unix-shell-programming/0672324903/)**. A more advanced tutorial/reference for shell use and shell programming; it covers command files, parameters, text filters, regular expressions, processes, and debugging. 



---
## 2. Official documentation and technical references

### Unix shell and command-line commands

- GNU Project. **[GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/)**. Official reference manual for the GNU core utilities, including `cat`, `chmod`, `cp`, `head`, `ls`, `mkdir`, `mv`, `pwd`, `rm`, `tail`, and `wc`. Use the navigation or in-page search to locate a command by name. 

- GNU Project. **[Coreutils: Directory Listing (`ls`)](https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html)**. Detailed command syntax and options for listing directory contents.

- GNU Project. **[Coreutils: Working Context (`pwd`)](https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html)**. Reference for displaying the current working directory.

- GNU Project. **[Coreutils: Creating Directories (`mkdir`)](https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html)**. Documentation for directory creation, including parent-directory creation with `-p`.

- GNU Project. **[Coreutils: Copying Files (`cp`)](https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html)**. Reference for file and recursive directory copying.

- GNU Project. **[Coreutils: Moving Files (`mv`)](https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html)**. Reference for moving and renaming files and directories.

- GNU Project. **[Coreutils: Removing Files (`rm`)](https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html)**. Reference for removal behavior and options. Read carefully before using recursive removal. The GNU manual documents `cp`, `mv`, and `rm` as core file-manipulation tools. 

- GNU Project. **[Coreutils: Concatenating Files (`cat`)](https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html)**. Documentation for printing and combining file contents.

- GNU Project. **[Coreutils: Output First Lines (`head`)](https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html)**. Reference for viewing initial lines of a file.

- GNU Project. **[Coreutils: Output Last Lines (`tail`)](https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html)**. Reference for viewing final lines and following files.

- GNU Project. **[Coreutils: Printing Byte, Word, and Line Counts (`wc`)](https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html)**. Reference for `wc`, including `wc -l` for line counts.

- GNU Project. **[Coreutils: Changing File Permissions (`chmod`)](https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html)**. Detailed reference for symbolic and numeric permission modes.

- GNU Project. **[Coreutils: Sorting Text Files (`sort`)](https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html)**. Reference for sorting text and standard-input behavior. 

- GNU Project. **[Coreutils: Modifying I/O Stream Buffering (`stdbuf`)](https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html)**. Advanced reference that explicitly discusses the standard input, output, and error streams. 

- GNU Project. **[Bash Reference Manual](https://www.gnu.org/software/bash/manual/)**. Official documentation for Bash syntax and features, including shell expansions, quoting, redirection, pipelines, command history, completion, and shell parameters.

- The Open Group. **[POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)**. The portable standard specification for shell command language concepts, including redirection, pipelines, quoting, and command execution.

- The Open Group. **[POSIX `cd` Utility](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/cd.html)**. Formal specification for the `cd` shell utility.

- The Open Group. **[POSIX `grep` Utility](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/grep.html)**. Formal specification for searching text with `grep`.

- GNU Project. **[GNU Grep Manual](https://www.gnu.org/software/grep/manual/grep.html)**. Official manual for GNU `grep`, including basic and extended regular expressions.

- GNU Project. **[GNU Readline Library](https://www.gnu.org/software/readline/)**. Documentation for the interactive line-editing facilities used by Bash, including command history and completion behavior.

- ArchWiki. **[Core Utilities](https://wiki.archlinux.org/title/Core_utilities)**. A well-maintained technical index connecting common core utilities such as `cd`, `ls`, `mkdir`, `rm`, `cp`, and `mv` to their documentation and alternatives. 

### Python standard-library documentation

- Python Software Foundation. **[`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)**. Official documentation for operating-system interfaces, including the current working directory, directory manipulation, environment variables, permissions, and process-related facilities. 

- Python Software Foundation. **[`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)**. Official documentation for interpreter-level facilities, including `sys.argv`, `sys.stdin`, `sys.stdout`, and `sys.stderr`. 

- Python Software Foundation. **[`pathlib` — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)**. Official documentation for `Path` objects, directory traversal, path construction, home/current directories, file inspection, and directory creation. It includes a comparison table between `os`/`os.path` operations and `pathlib` equivalents. 

- Python Software Foundation. **[`shutil` — High-level file operations](https://docs.python.org/3/library/shutil.html)**. Official documentation for higher-level copying, moving, archiving, and deletion operations such as `shutil.copy()`, `shutil.move()`, and `shutil.rmtree()`. 

- Python Software Foundation. **[`argparse` — Parser for command-line options, arguments and sub-commands](https://docs.python.org/3/library/argparse.html)**. Official documentation for creating robust command-line interfaces in Python, including required positional filename arguments, options, usage messages, and help output.

- Python Software Foundation. **[`subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html)**. Official documentation for starting external commands from Python and connecting their standard input, output, and error streams.

- Python Software Foundation. **[Python Standard Library](https://docs.python.org/3/library/)**. The central reference index for the modules bundled with Python, including file I/O and system interfaces. 

### Local documentation students should use

- **Manual pages:** Run `man command` in a terminal, for example:

  ```bash
  man ls
  man chmod
  man grep
  man python
  ```

  Local manual pages document the actual command version installed on the system students are using.

- **Shell help for built-ins:** `cd` is usually a shell built-in, so use:

  ```bash
  help cd       # Bash
  man zshbuiltins  # Commonly useful in zsh environments
  ```

- **Short option summary:** Many commands provide usage information through:

  ```bash
  command --help
  ```

  For example, `ls --help` is common on GNU/Linux systems, although this convention is not universal across all Unix variants.

---


<!-- 
---

## Recommended use sequence

1. Begin with the course lecture notes and complete the guided terminal workflow.
2. When unsure about a command on the local machine, check `man command` first.
3. Use the GNU Coreutils or Bash manuals to understand option behavior in GNU/Linux environments.
4. Use the official Python documentation for `os`, `sys`, `pathlib`, `shutil`, and `argparse` when writing Python scripts.
5. Use LinkedIn Learning or O'Reilly for structured review and deeper practice.
6. Use Software Carpentry or Missing Semester for hands-on command-line practice.
7. Treat short-form tutorial sites and Medium articles as supplementary explanations; confirm any consequential command, permission, or deletion behavior against primary documentation. -->
