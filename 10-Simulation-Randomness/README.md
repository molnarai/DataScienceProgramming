# Session 10: Simulation and Randomness

Until now every program in this course gave the same answer each time it ran.
This session is about programs that use chance on purpose. A simulation
answers a question by running an experiment many times and counting, which
makes problems approachable before the mathematics is.

1. **Simulate to answer.** The share of successes in many trials estimates a
   probability.
2. **Pseudorandom numbers.** The numbers follow from a seed, so a run can be
   repeated exactly.
3. **One trial, many trials.** The experiment is a function of a generator;
   one generator, made once, serves the whole study.
4. **An estimate is uncertain.** It changes from run to run, and its standard
   error says by how much.
5. **More trials, slowly better.** The error shrinks with the square root of
   the number of trials.
6. **Fair comparisons and resampling.** Compare options on the same random
   draws; apply the same machinery to real data with the bootstrap.

> **Run these on ARC, with the kernel set to Conda Python 3.12.** None of the
> three notebooks reads a data file.

Nothing here repeats earlier sessions. Mean, standard deviation, quantiles and
every plot used are in `../09-Visualization-Descriptive-Statistics/`.

## Notebooks

Rename a notebook before you edit it, so that the next course release does not
overwrite your work.

### `01_Chance_on_Purpose.ipynb` — the ideas

An overview of the six ideas on problems whose answers are known. Two dice
that add up to seven introduce simulating and counting. Seeds make the
"random" numbers repeat, and a generator held in a variable replaces the
shared one of the `random` module. The Monty Hall problem is written as one
trial and run ten thousand times, and a generator made inside the trial shows
what goes wrong. Twenty runs of a correct program give twenty answers; the
standard error predicts their spread from a single run, and 192 of 200
intervals contain the truth. A table over trial counts shows that a hundred
times the work buys one decimal place. Two stock levels are compared unfairly
and then fairly, and twelve delivery times are resampled to get an interval
for their mean and their median.

Four exercises, and a table mapping each idea to a phase of Homework 9.

### `02_Help_Desk_Example.ipynb` — one study, start to finish

A worked example with no formula behind it: a campus help desk where a student
arrives every four minutes and needs three and a half. *How long do students
wait, and is a second person worth it?* The randomness goes into one function
and the queue arithmetic into another, which is first checked on four days
whose answers are obvious. One simulated day is looked at closely, then four
more that look nothing like it, then two thousand. With one person the mean
wait is a quarter of an hour and one day in four is worse than twenty minutes;
with two, on the same simulated days, it is under a minute. A sensitivity
analysis shows the wait climbing faster and faster as the desk gets busier.
The notebook ends with what an honest report includes and what the model
leaves out.

Five exercises on the same model.

### `03_Simulation_Reference.ipynb` — a lookup guide

Meant to be searched, not read through, and to stay open during Homework 9.
Eleven sections of "you want / write this" tables with runnable examples:
generators and seeds; drawing numbers and which distribution to use; choosing
and shuffling, with and without replacement; reading code that uses Python's
`random` module; the two layers of a simulation; standard error, intervals
and how many trials are enough; drawing all the trials at once; comparing
options on the same draws; the bootstrap; the rules that keep results
reproducible; and a reporting checklist with a table of symptoms and causes.

## Homework

[Homework 9](../../Assignments/HW09/instructions/homework09_instructions.md)
has the shape of notebook 02: a problem with a known answer first (the
birthday problem), then a decision with no formula (how many pastries a coffee
cart should bake), then the bootstrap on real data. The overlap is deliberate.
Each phase uses an idea from notebook 01 and tools listed in notebook 03.
