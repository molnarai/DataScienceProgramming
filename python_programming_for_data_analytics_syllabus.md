# Python Programming for Data Analytics

## Course overview

This course introduces Python programming for students in data analytics and data science who have little or no prior programming experience. It starts with Jupyter notebooks for interactive exploration, then moves deliberately toward writing functions, building self-contained scripts, using the Unix command line, navigating the Unix file system, and managing code with Git. Students also encounter foundational ideas from statistics, simulation, machine learning, and algorithmic thinking through carefully scaffolded coding examples and assignments.

The course is organized around repeated practice rather than exams. Students learn by writing code every week, receiving automated feedback, revising submissions, and explaining their work in plain language. This structure supports beginners while still building habits needed for later data science, analytics, and computational coursework.

## Learning objectives

By the end of the course, students should be able to:

- Write, run, and debug Python code in Jupyter notebooks and in standalone `.py` programs.
- Use variables, expressions, strings, conditionals, loops, and core Python data structures.
- Write reusable Python functions with parameters, return values, and basic documentation.
- Read from and write to text files and CSV files.
- Navigate directories and files using the Unix command line.
- Use Git to track changes, submit work, and maintain a reproducible coding workflow.
- Apply Python to simple descriptive statistics, visualization, simulation, and introductory machine learning tasks.
- Implement and reason about simple computational ideas such as search, hashing, shortest path, and basic data structures.
- Interpret coding results clearly in short written explanations.
- Use AI tools responsibly as learning aids while maintaining authorship, understanding, and academic integrity.

## Prerequisites

No prior programming experience is required. Students should be comfortable with basic computer use, file management, and routine mathematical reasoning at the level expected in an introductory data analytics program.

## Required tools

Students will need regular access to a laptop capable of running Python, Jupyter notebooks, Git, and a Unix-like command line environment. A course-supported setup may use local installation, a managed lab image, or a hosted environment such as JupyterHub, but students are still expected to understand files, directories, and command-line execution regardless of platform.

## Course format

The course meets for 14 sessions. Each session combines brief lecture, live coding, guided practice, and interactive class work. The first part of the course emphasizes interactive exploration and immediate feedback in notebooks; the middle and later parts emphasize writing functions, scripts, command-line workflows, and reproducible project structure.

Students complete individual assignments only. There are no group projects and no exams. Learning is assessed through in-class activities, short quizzes, and coding homework assignments.

## Grading policy

The course grade is based on two components:

- **Interactive class activities and quizzes:** 20%
- **Coding homework assignments:** 80%

This grading policy is intentional. Since the central goal of the course is to help students learn programming by doing it, most of the grade comes from regular coding practice rather than one-time exams. Students will see many small opportunities to improve, revise, and strengthen their work over time.

### In-class activities and quizzes (20%)

Interactive class activities are short exercises completed during class, sometimes individually and sometimes as guided whole-class work. These activities are designed to reinforce the day’s topic, surface misconceptions early, and give students immediate practice with the tools and concepts introduced in class.

Some class meetings will include short quizzes. These quizzes are low stakes and are meant to check understanding of key concepts such as Python syntax, tracing code, interpreting output, Git workflow, Unix commands, and reasoning about simple data analysis results.

In-class work is graded primarily for participation, reasonable completion, and evidence of engagement with the material. Because these activities are part of the learning process, they are not intended to function like high-pressure exams.

### Coding homework (80%)

Coding homework is the main assessed component of the course. Assignments are individual and will be submitted electronically through the course repository or submission pipeline. Most assignments require students to write code that can be tested automatically, and many will also ask for short written explanations or interpretations.

Homework assignments are designed to build progressively:

- early assignments focus on syntax, logic, and confidence,
- middle assignments emphasize functions, files, scripts, Unix, and Git,
- later assignments introduce data analysis, simulation, algorithms, and machine learning in beginner-friendly ways.

### Homework rubric

A typical homework assignment may be evaluated using the following structure:

- **Correctness and robustness:** 50%
- **Code organization and readability:** 15%
- **Explanation, interpretation, or reflection:** 15%
- **Workflow and reproducibility requirements:** 20%

Correctness and robustness refer to whether the program produces the required output, handles expected cases, and passes the automated tests. Code organization and readability include meaningful names, clear decomposition into functions, formatting, and avoiding unnecessary complexity. Explanation and reflection may include short prompts asking students to describe how their code works, interpret a result, or explain a design decision. Workflow and reproducibility may include required filenames, directory structure, Git commit history, script entry points, or other assignment-specific expectations.

### Automated grading and resubmission policy

Homework assignments are graded automatically through a CI/CD pipeline. Students may submit or resubmit their assignments multiple times before the deadline. The last submission before the deadline is treated as the final submission for grading purposes.

This model is intended to encourage iteration and learning. Students should use the automated feedback to identify errors, improve their code, and test their understanding. The ability to resubmit is a learning support, not a shortcut; students are expected to study the feedback and make purposeful revisions.

Automated grading may include:

- visible tests that check core functionality,
- hidden tests that check edge cases or robustness,
- checks for required files or outputs,
- light style or structure checks,
- validation of command-line behavior when scripts are required.

Passing visible tests does not guarantee full credit if other requirements are not met. Students should read each assignment carefully and verify that their code satisfies the full specification.

### Late work policy

A clear late policy should be stated in the course site and applied consistently. A recommended policy is:

- assignments submitted after the deadline incur a fixed penalty per day,
- assignments more than a specified number of days late are not accepted unless prior arrangements were approved,
- documented emergencies are handled individually according to university policy.

Because students can already submit multiple times before the deadline, they are expected to start early and use the feedback cycle effectively.

## AI usage policy

AI tools are now part of the professional computing landscape, and students in a data analytics or data science program should learn how to use them responsibly. In this course, AI use is neither ignored nor treated as automatically prohibited. Instead, the course adopts a guided-use policy: AI may support learning, but it may not replace the student’s own reasoning, authorship, or accountability.

### Core principle

Students may use AI tools to support their learning, but every submitted assignment must represent work that the student understands and can explain. Submitting code that a student cannot explain, debug, adapt, or justify is not acceptable, even if the code appears to run correctly.

### Permitted uses of AI

Unless an assignment explicitly states otherwise, students may use AI tools for limited support such as:

- asking for explanations of Python syntax or error messages,
- requesting conceptual clarification about loops, functions, lists, files, or libraries,
- getting hints about how to approach a problem,
- asking for debugging suggestions,
- requesting feedback on code readability or organization,
- checking understanding of Git, command-line, or programming terminology.

These uses are acceptable when they help the student learn and when the student independently verifies the resulting code or advice.

### Prohibited uses of AI

Unless an assignment explicitly states otherwise, students may not:

- submit AI-generated code as their own original solution without disclosure,
- ask an AI tool to produce a complete homework solution and then turn it in,
- use AI to bypass the intended learning objective of the assignment,
- use AI-generated explanations or reflections that the student did not write and cannot defend,
- fabricate outputs, results, screenshots, command history, or commit history.

In short, AI may assist the learning process, but it may not replace the student’s authorship of the submitted work.

### Required disclosure

Every homework submission must include a short AI-use statement. A simple format is sufficient:

- “No AI tools used.”
- “Used ChatGPT to explain a Python error and suggest debugging steps; final code written and verified independently.”
- “Used Claude to clarify Pandas grouping syntax and compare two plotting options; all submitted code was revised and tested independently.”

The goal of disclosure is transparency, not punishment. Honest disclosure of limited, appropriate AI use is preferable to hidden misuse.

### Verification of understanding

Because this course values learning over mere output, students may occasionally be asked to do one or more of the following:

- explain part of their code in class,
- answer a short follow-up question about a homework solution,
- modify a small part of a previous solution,
- complete a brief quiz related to a recently submitted assignment.

If a student submits work that they cannot explain at a basic level, the instructor may treat that as evidence that the work does not represent the student’s own understanding.

### Why this policy exists

The purpose of the AI policy is not simply to police misconduct. It is to protect the learning goals of the course. In an introductory programming course, students need repeated practice translating ideas into code, debugging errors, and building fluency through effort. If AI tools remove all productive struggle, students may complete assignments without developing the skills needed for later coursework.

At the same time, responsible AI use is a practical professional skill. This course therefore aims to teach students how to use AI as a tutor, assistant, or reviewer rather than as a substitute for thinking.

## Academic integrity

All submitted work must be completed individually unless an activity explicitly allows collaboration. Students may discuss general ideas with classmates, but they may not share solution code, copy another student’s work, reuse unauthorized solution material, or collaborate in ways that blur authorship.

Improper use of AI tools falls under the same academic integrity framework as any other unauthorized assistance. The key question is whether the submitted work honestly represents the student’s own understanding and effort.

## Course schedule

## Session 1: Introduction to Python and the course environment

### Objectives

- Understand course expectations, tools, and workflow.
- Open and use a Jupyter notebook.
- Run simple Python statements and evaluate expressions.
- Distinguish notebooks from scripts.

### Topics

- What Python is and why it is used in analytics and data science.
- Jupyter notebook basics.
- Code cells and markdown cells.
- Variables, expressions, and basic output.
- Saving work and naming files clearly.

### In-class activity

Students complete a guided notebook exercise that includes arithmetic, strings, and variable assignment.

### Homework

Notebook setup and basic Python expressions.

## Session 2: Types, strings, and conditionals

### Objectives

- Recognize common Python data types.
- Convert between types when appropriate.
- Write simple branching logic.

### Topics

- Integers, floats, strings, booleans.
- String operations and common methods.
- Comparisons.
- `if`, `elif`, and `else`.

### In-class activity

Students classify simple values and transform short text inputs.

### Homework

A small text-processing task using strings and conditionals.

## Session 3: Loops and core data structures

### Objectives

- Use `for` and `while` loops appropriately.
- Work with lists, tuples, sets, and dictionaries.
- Recognize patterns such as counting and accumulation.

### Topics

- Iteration.
- Indexing and slicing.
- Membership tests.
- Dictionary-based counting.

### In-class activity

Students compute category counts from a small dataset.

### Homework

Use loops and dictionaries to summarize structured input data.

## Session 4: Functions and decomposition

### Objectives

- Write reusable functions.
- Use parameters and return values correctly.
- Break a larger task into smaller steps.

### Topics

- Function definitions.
- Scope.
- Docstrings.
- Simple testing.

### In-class activity

Students refactor repetitive code into functions.

### Homework

Implement several small functions and pass an autograder test suite.

## Session 5: Files, modules, and scripts

### Objectives

- Read from and write to files.
- Organize code into scripts and helper functions.
- Run Python programs from the command line.

### Topics

- File paths.
- Text files and CSV files.
- Imports.
- `if __name__ == "__main__"`.

### In-class activity

Students convert notebook logic into a self-contained script.

### Homework

A file-processing assignment that reads input, produces output, and reports basic results.

## Session 6: Unix file system and command line

### Objectives

- Navigate files and directories in a Unix environment.
- Use common command-line tools.
- Understand relative and absolute paths.

### Topics

- `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`.
- Redirection and pipes.
- File organization.
- Basic permissions.

### In-class activity

Students complete a guided terminal workflow exercise.

### Homework

Organize files, run scripts from the shell, and demonstrate correct command-line usage.

## Session 7: Git and reproducible workflow

### Objectives

- Understand why version control matters.
- Track changes with Git.
- Use Git as part of assignment submission.

### Topics

- Repository basics.
- `git status`, `git add`, `git commit`, `git log`.
- Remote repositories.
- Meaningful commit messages.

### In-class activity

Students create a repository, make edits, and inspect commit history.

### Homework

Submit a small assignment through the Git-based workflow with multiple commits.

## Session 8: Python for data analysis

### Objectives

- Load and inspect tabular data.
- Perform simple cleaning and filtering.
- Compute descriptive summaries.

### Topics

- NumPy and Pandas basics.
- DataFrames.
- Selecting, filtering, grouping.
- Missing values.

### In-class activity

Students explore a small real-world dataset.

### Homework

Conduct a basic exploratory data analysis in Python.

## Session 9: Visualization and descriptive statistics

### Objectives

- Create informative plots.
- Compute and interpret basic summary statistics.
- Communicate findings clearly.

### Topics

- Histograms, bar charts, scatter plots, line plots.
- Mean, median, variance, standard deviation.
- Outliers and distribution shape.

### In-class activity

Students compare two variables visually and numerically.

### Homework

Produce plots and descriptive statistics and answer short interpretation prompts.

## Session 10: Simulation and randomness

### Objectives

- Use random number generation in Python.
- Understand repeated trials and empirical estimation.
- Interpret simulation output.

### Topics

- Random seeds.
- Sampling and repeated experiments.
- Monte Carlo intuition.
- Summarizing simulated outcomes.

### In-class activity

Students simulate a simple random process and compare outcomes across runs.

### Homework

Implement a simulation study and explain the results.

## Session 11: Search and hashing

### Objectives

- Understand simple search strategies.
- Use dictionaries for fast lookup.
- Compare algorithmic approaches conceptually.

### Topics

- Linear search.
- Binary search idea.
- Dictionaries and hashing intuition.
- Time-efficiency tradeoffs at an introductory level.

### In-class activity

Students compare different lookup methods on structured data.

### Homework

Write search-related functions and compare their behavior on test inputs.

## Session 12: Graphs and shortest path

### Objectives

- Represent simple graphs in Python.
- Understand pathfinding ideas.
- Compute or trace a shortest path in a small example.

### Topics

- Nodes and edges.
- Adjacency representations.
- Breadth-first search intuition.
- Introductory shortest path logic.

### In-class activity

Students work through a route-finding example.

### Homework

Build a small graph representation and solve a shortest-path problem.

## Session 13: Introductory machine learning

### Objectives

- Understand the basic workflow of supervised learning.
- Split data into training and testing sets.
- Evaluate a simple model.

### Topics

- Features and labels.
- Classification and regression.
- Train/test split.
- Accuracy and error.
- Overfitting at an intuitive level.

### In-class activity

Students train and evaluate a simple model on a toy dataset.

### Homework

Fit a basic model, report results, and discuss limitations.

## Session 14: Integration and review

### Objectives

- Combine programming, analysis, and workflow skills.
- Strengthen debugging and interpretation habits.
- Demonstrate readiness for follow-on coursework.

### Topics

- Review of core Python ideas.
- Debugging and testing.
- Reproducible file organization.
- Connecting programming skills to later data science work.

### In-class activity

Students complete an integrative coding and interpretation exercise.

### Homework

A cumulative assignment combining functions, files, analysis, and one algorithmic component.

## Assignment design principles

Assignments in this course are designed to help students learn by doing. To support that goal, each assignment should:

- be achievable by a beginner with steady effort,
- reinforce the current topic while revisiting earlier skills,
- require readable and structured code rather than one long solution block,
- include at least one element that checks understanding beyond simple output,
- be compatible with automatic testing and repeat submission.

Many assignments should include a small written component such as a short explanation of a function, an interpretation of a chart, a note on debugging steps, or an AI-use disclosure. This helps students practice communicating about code, not just writing it.

## Recommended homework progression

A coherent sequence for the term is:

1. Notebook setup and simple expressions.
2. Strings and conditionals.
3. Loops and dictionaries.
4. Functions.
5. Files and scripts.
6. Unix command line.
7. Git workflow.
8. Data analysis with Pandas.
9. Visualization and descriptive statistics.
10. Simulation.
11. Search and hashing.
12. Shortest path and graph representation.
13. Introductory machine learning.
14. Cumulative integration assignment.

## Instructor notes on implementation

Several implementation choices can help preserve learning value in an AI-rich environment:

- Use hidden tests as well as visible tests.
- Require specific function signatures and file layouts.
- Include short explanation prompts.
- Use brief quizzes tied to recent assignments.
- Ask students to modify or extend earlier code in later assignments.
- When feasible, vary datasets or parameters across students.
- Review commit history when a submission appears inconsistent with the student’s demonstrated level of understanding.

These practices do not eliminate misuse, but they make it much easier to reward genuine learning and much harder to succeed through blind copying.

## Accessibility and support

Students are encouraged to ask questions early and often. Programming is learned through practice, revision, and debugging, not by getting everything correct on the first try. Course support should emphasize office hours, guided troubleshooting, and feedback that helps students build confidence without removing responsibility for the work.

## Closing statement

This course is designed to help beginners become capable, independent, and ethical users of Python in a data analytics setting. The emphasis on iterative homework, transparent AI use, command-line and Git workflow, and practical coding problems is meant to build durable skills that carry into later coursework and professional practice.
