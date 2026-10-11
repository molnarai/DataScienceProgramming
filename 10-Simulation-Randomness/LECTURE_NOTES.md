# Lecture Notes — Session 10: Simulation and Randomness

## 1. The problem

Some questions cannot be answered by looking something up in a table,
because the answer depends on things that have not happened yet and that vary
by chance.

- How many pastries should a bakery make each morning, when the number of
  customers changes from day to day?
- Is one person at a service desk enough, when people arrive in bursts and
  some problems take ten times as long as others?
- A survey of 2,000 customers gives an average. How far might that be from
  the average of all customers?

For a few such questions there is a formula. For most there is not, or the
formula stops working the moment the situation gets slightly more realistic.
There is a method that works regardless: **build a small model of the
situation, let the computer live through it thousands of times, and count
what happens.** That is a simulation. It trades mathematics for computing
time, and it makes problems approachable before the mathematics is.

Simulation brings a new difficulty that nothing earlier in the course had:
**run the program again and the answer changes.** A simulated number is an
estimate, not a fact. Two things follow, and they are what this session is
about:

1. the randomness must be **controlled**, so that a result can be reproduced,
   checked and debugged;
2. every result must come with a statement of **how far it can be trusted**.

## 2. Core concepts, and how Python realizes them

### The packages

| Package | Purpose | What it gives you |
|---|---|---|
| **NumPy** (`numpy.random`) | random numbers in bulk | a `Generator` object created with `np.random.default_rng(seed)`; draws from many distributions; thousands or millions of draws in one call; sampling, shuffling |
| **`random`** (standard library) | random numbers, one at a time | `random.randint`, `random.choice`, `random.shuffle`; simple, built in, and one shared generator for the whole program |
| **pandas**, **matplotlib** | summarising and showing the outcomes | means, quantiles, histograms of simulated results |

### Concept 1 — Simulate to answer

Roll two dice: how likely is a total of seven? The exact answer is 6 of 36
pairs, 0.1667. The simulation rolls two dice ten thousand times and counts:

```python
import random

sevens = 0
for roll in range(10_000):
    if random.randint(1, 6) + random.randint(1, 6) == 7:
        sevens += 1
print(sevens / 10_000)
```

The printed share is close to 0.1667 and not equal to it, and it is different
on the next run. Both halves of that sentence matter: the share of successes
**estimates** the probability, and the estimate **is not the answer**.

Methods of this kind are called **Monte Carlo** methods. A sound habit: try
the method first on a problem whose answer is known, so that you can see it
work before trusting it on one where you cannot check.

### Concept 2 — Pseudorandom numbers and seeds

A computer follows instructions exactly; it cannot produce chance. Its
"random" numbers come from a recipe that turns one number into the next in a
sequence scrambled enough to pass for random. The first number is the
**seed**.

- The same seed gives the same sequence, every time, on every machine.
- Another seed gives another sequence.
- With no seed, one is taken from the clock, and every run differs.

That is why the numbers are called **pseudorandom**, and it is a feature. A
result that cannot be repeated cannot be checked or debugged. Fix the seed
and a simulation is as repeatable as any other program.

The modern tool is a generator that is a **value** you hold:

```python
import numpy as np

rng = np.random.default_rng(8410)     # a generator, started from seed 8410
rng.integers(1, 7, size=10)           # ten dice: whole numbers from 1 to 6
rng.random()                          # one number between 0 and 1
```

Note `rng.integers(1, 7)`: the upper end is left out, like `range`. (The
standard library's `random.randint(1, 6)` includes it. Mixing the two up is a
classic source of dice that never show a six.)

A generator has a **state**: each draw moves it forward, and the next draw
continues from there.

| You want | Write |
|---|---|
| a whole number from `low` to `high − 1` | `rng.integers(low, high)` |
| a number between 0 and 1 | `rng.random()` |
| True with probability p | `rng.random() < p` |
| a measurement around a mean | `rng.normal(mean, spread)` |
| a count of arrivals | `rng.poisson(mean)` |
| a waiting time | `rng.exponential(mean)` |
| one of a list | `rng.choice(items)` |
| several, repeats allowed | `rng.choice(items, size=5)` |
| several different ones | `rng.choice(items, size=5, replace=False)` |
| a random order | `rng.permutation(items)` |

Sampling **with replacement** means an item can be picked again (rolling a
die); **without replacement** means it cannot (dealing cards). Which one a
problem needs is the first question to ask.

### Concept 3 — One trial, many trials

Every simulation has two layers.

```python
def trial(rng):
    """Run the experiment once; return its outcome."""
    return rng.integers(1, 7, size=2).sum() == 7


def run_trials(trial, trials, rng):
    """Run it many times; keep every outcome."""
    outcomes = np.empty(trials)
    for number in range(trials):
        outcomes[number] = trial(rng)
    return outcomes


rng = np.random.default_rng(1)
outcomes = run_trials(trial, 10_000, rng)
outcomes.mean()                       # True counts as 1: the share of successes
```

Three rules keep this reproducible:

- **The trial takes the generator as an argument.** It does not make its own.
- **One generator, made once, at the top**, and passed along.
- **Never create a generator inside the loop.** It would restart the sequence
  on every pass, and all ten thousand trials would be the same trial. The
  program runs, prints a number, and the number is 0 or 1.

A further habit pays off repeatedly: put the randomness in one small function
("draw a day's demand") and the arithmetic in another ("given this demand,
what is the profit?"). The second can then be checked by hand on inputs you
make up.

### Concept 4 — An estimate is uncertain

Run the same simulation with twenty seeds and you get twenty answers,
scattered around the truth. How scattered is the **standard error**, and it
can be computed from a single run:

```text
standard error = standard deviation of the outcomes / sqrt(number of trials)
```

```python
mean = outcomes.mean()
se = outcomes.std(ddof=1) / np.sqrt(len(outcomes))
low, high = mean - 1.96 * se, mean + 1.96 * se
```

The interval from `low` to `high` is the honest form of the result: *0.167,
interval 0.160 to 0.175, from 10,000 trials*. Its claim is about the method:
if the whole simulation were repeated with many seeds, about 95 of 100 such
intervals would contain the true value. About one in twenty will not.

### Concept 5 — More trials, slowly better

The standard error shrinks with the **square root** of the number of trials.

| To make the error | you need |
|---|---|
| half as large | 4 times the trials |
| a tenth as large | 100 times the trials |

A hundred times the work buys one more decimal place. So "how many trials?"
has an answer: enough that the interval is narrower than the difference you
care about, and no more. And more digits in the printout are not more truth:
print as many as the standard error supports.

When a loop of trials is too slow, NumPy can often draw them all at once:

```python
dice = rng.integers(1, 7, size=(100_000, 2))     # 100,000 rows of two dice
(dice.sum(axis=1) == 7).mean()
```

This is hundreds of times faster. It also draws its numbers in a different
order than the loop, so the two versions give *different digits from the same
seed*, both correct. Simulations are compared by whether they agree within
their standard errors, never digit for digit.

### Concept 6 — Comparing options fairly

Test one plan on Monday's customers and another on Saturday's and you cannot
tell the plan from the day. Simulation has a cure that real experiments
rarely have: **give every option exactly the same random numbers.** Draw the
random inputs once, and try each option on them.

```python
demand = rng.poisson(40, size=10_000)              # drawn once

profit_a = profit(42, demand)                      # both plans, the same days
profit_b = profit(43, demand)
difference = profit_b - profit_a                   # one difference per day
```

The day-to-day luck is in both results and cancels out of the difference, so
the standard error of the difference is far smaller than that of either plan.
If its interval excludes zero, the data tell the two options apart. If it
contains zero, they do not, and saying so is a result. This technique is
called **common random numbers**.

### Concept 7 — Resampling real data: the bootstrap

The same machinery answers a question about real data: *I have a sample and
its average. How much would the average move with a different sample?* You
cannot sample the world again. But the sample is your best picture of the
world, so draw from **it**: as many values as it has, **with replacement**,
many times over.

```python
means = [rng.choice(sample, size=len(sample), replace=True).mean()
         for number in range(5_000)]
low, high = np.quantile(means, [0.025, 0.975])
```

The spread of those resampled means shows how firm the sample's mean is. The
method needs no formula and works for a median, a quantile or a correlation
as well. Its limit is the sample itself: it can only reshuffle what was
observed, and a small sample knows little about rare, extreme values.

### Reporting

> A simulated number without its seed and its number of trials cannot be
> checked, and without its interval cannot be judged.

Report the estimate, its interval, the number of trials, the seed, and the
model: what was assumed. The simulation answers the model, not the world.

## 3. Business use cases

**A game-show decision.** Three doors, a prize behind one. You pick a door;
the host, who knows where the prize is, opens one of the others to show it is
empty, and offers a switch. Most people say it makes no difference. Ten
thousand simulated games say that switching wins two times in three. This is
the smallest example of a general use: settling an argument about
probabilities by running the experiment.

**How many to bake.** A coffee cart bakes pastries each morning at $1 and
sells them at $3; leftovers are thrown away, and when they run out, customers
leave. About forty people a day want one, give or take. Simulating ten
thousand days for each batch size gives a profit curve that is nearly flat at
its top: 42 and 43 differ by a few cents a day, and which one "wins" depends
on the seed. Compared on the same simulated days, the difference has an
interval that may include zero. The honest advice to the owner is a number, a
statement of how sure it is, and what being off by one would cost, which is
almost nothing.

**Stocking a seasonal item.** A shop sells umbrellas, more on wet days.
Should it stock 22 or 23? Tested on separate sets of random days, the answer
swings by several dollars and changes sign. Tested on the same days, it is
steady to a few tenths. The business lesson is the method: when comparing
plans in a simulation, hold the luck constant.

**One person at the help desk, or two?** A campus service desk gets a visitor
every four minutes on average, and a visit takes three and a half. On paper
one person keeps up, with time to spare. The simulation shows a different
picture: because arrivals come in bursts and some visits are long, queues
build and take an hour to clear. The average wait with one person is about a
quarter of an hour, and one day in four is worse than twenty minutes. With
two people, on the same simulated days, the wait is under a minute. The model
also shows that waiting does not grow in step with traffic: as the desk
approaches full use, a small rise in arrivals adds a large amount of waiting.
That kind of sensitivity analysis, varying the inputs you guessed, is one of
the most valuable things a simulation can do.

**How far can a survey average be trusted?** An agency has measurements from
2,000 sites out of several hundred thousand. Resampling those 2,000 gives an
interval for the mean and one for the median. The data are heavily skewed, a
few huge values among many small ones, and the interval for the mean is wide
and sometimes fails to contain the true value, because the sample may have
missed the few giants that carry the mean. The interval for the median holds
up far better. A method that reports its own uncertainty can still be wrong
about it when the sample has not seen the extremes.

## Key points

- A simulation answers a question by running an experiment many times and
  counting.
- The numbers follow from a seed. Fix it, and hold the generator in a
  variable.
- One generator, made once, passed to every function that draws.
- An estimate changes from run to run. Report its interval.
- A hundred times the trials for one more decimal place.
- Compare options on the same random draws.
- Report the seed, the number of trials, the interval and the assumptions.
