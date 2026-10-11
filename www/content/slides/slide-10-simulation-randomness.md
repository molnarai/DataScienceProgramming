+++
title = "Simulation and Randomness"
description = "Monte Carlo simulation with seeded generators: trials, standard errors and intervals, fair comparisons, and the bootstrap"
weight = 100
outputs = ["Reveal"]
math = false
thumbnail = "../imgs/slides/.png"

[reveal_hugo]
custom_theme = "css/reveal-robinson.css"
slide_number = true
transition = "none"

+++

<style>
  .reveal .slides section { box-sizing: border-box; }
  .reveal .dc-sub { color: #666; font-size: 0.9em; }
  .reveal .dc-kicker { color: #CC0000; font-size: 0.55em; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin: 0 0 4px 0; }
  .reveal .dc-small { font-size: 0.75em; }
  .reveal .dc-muted { color: #666; }
  .reveal .dc-quote { font-size: 0.85em; border-left: 5px solid #CC0000; background: #f4f6f9; padding: 12px 18px; text-align: left; margin: 18px 0; }

  /* Cards */
  .reveal .dc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px; }
  .reveal .dc-grid.three { grid-template-columns: 1fr 1fr 1fr; }
  .reveal .dc-card { background: #f4f6f9; border-left: 5px solid #003478; padding: 10px 14px; border-radius: 4px; }
  .reveal .dc-card h3 { margin: 0 0 4px 0; font-size: 0.85em; }
  .reveal .dc-card p { margin: 0; font-size: 0.62em; }
  .reveal .dc-card .dc-from { color: #666; font-size: 0.58em; margin-bottom: 6px; }
  .reveal .dc-card.red { border-left-color: #CC0000; }
  .reveal .dc-card.red h3 { color: #CC0000; }
  .reveal .dc-card.green { border-left-color: #2e7d32; }
  .reveal .dc-card.green h3 { color: #2e7d32; }

  /* Flow */
  .reveal .dc-flow { display: flex; align-items: center; justify-content: center; gap: 8px; margin: 20px 0; }
  .reveal .dc-node { background: #f4f6f9; border: 2px solid #003478; border-radius: 6px; padding: 10px 14px; font-size: 0.62em; text-align: center; }
  .reveal .dc-node.dark { background: #003478; color: #fff; }
  .reveal .dc-node .dc-owner { margin-top: 4px; font-size: 0.85em; font-style: italic; color: #CC0000; }
  .reveal .dc-node.dark .dc-owner { color: #cfd8e8; }
  .reveal .dc-arrow { color: #003478; font-size: 0.9em; font-weight: 700; }

  /* Two columns */
  .reveal .dc-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }
  .reveal .dc-cols h4 { font-size: 0.65em; margin: 6px 0 0 0; }
  .reveal .dc-cols h4.bad { color: #CC0000; }
  .reveal .dc-cols h4.good { color: #2e7d32; }

  /* Code */
  .reveal .highlight pre, .reveal pre { width: 100%; font-size: 0.5em; margin: 8px 0; }
  .reveal .dc-code-lg pre { font-size: 0.58em; }

  /* Bullets */
  .reveal .dc-points { margin-top: 8px; }
  .reveal .dc-points li { font-size: 0.72em; margin-bottom: 0.4em; }

  .reveal .dc-table { font-size: 0.58em; width: 100%; margin-top: 10px; }
  .reveal .dc-table td { vertical-align: top; }

  .reveal .dc-nb { font-size: 0.6em; }
  .reveal .dc-nb .num { display: inline-block; width: 1.6em; height: 1.6em; line-height: 1.6em; text-align: center; border-radius: 50%; background: #003478; color: #fff; font-weight: 700; margin-right: 6px; }
</style>

<p class="dc-kicker">IFI 8410 — Session 10: Simulation and Randomness</p>
<h1>Chance on Purpose</h1>
<p class="dc-sub">Run the experiment ten thousand times, and say how sure you are</p>

{{% note %}}
Up to now every answer came out of a table. Today the answer depends on things that have not happened yet.
{{% /note %}}

***

<p class="dc-kicker">The problem</p>

## Questions no table can answer

<ul class="dc-points">
  <li>How many pastries should a bakery make each morning, when the number of customers changes from day to day?</li>
  <li>Is one person at a service desk enough, when people arrive in bursts?</li>
  <li>A survey of 2,000 customers gives an average. How far might that be from the average of all customers?</li>
</ul>

<p class="dc-quote">Build a small model of the situation, let the computer live through it thousands of times, and <b>count what happens</b>.</p>

<div class="dc-grid">
  <div class="dc-card red"><h3>New difficulty</h3><p>Run the program again and the answer changes. A simulated number is an <b>estimate</b>, not a fact.</p></div>
  <div class="dc-card"><h3>So, two requirements</h3><p>The randomness must be <b>controlled</b>, and every result must say <b>how far it can be trusted</b>.</p></div>
</div>

{{% note %}}
For a few such questions there is a formula. For most there is not, or it stops working when the situation gets slightly more realistic. Simulation trades mathematics for computing time.
{{% /note %}}

***

<p class="dc-kicker">Concept 1</p>

## Simulate to answer

<div class="dc-code-lg">
{{< highlight python >}}
import random

sevens = 0
for roll in range(10_000):
    if random.randint(1, 6) + random.randint(1, 6) == 7:
        sevens += 1
print(sevens / 10_000)        # close to 0.1667, and different on the next run
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>The exact answer: 6 of 36 pairs, 0.1667.</li>
  <li>The share of successes <b>estimates</b> the probability. The estimate <b>is not the answer</b>.</li>
  <li>Try the method first on a problem whose answer is known, before trusting it where you cannot check.</li>
</ul>

{{% note %}}
Methods of this kind are called Monte Carlo methods. The notebook also runs the three-doors game show: most people say switching makes no difference; ten thousand simulated games say it wins two times in three.
{{% /note %}}

***

<p class="dc-kicker">Concept 2</p>

## Pseudorandom numbers and seeds

<div class="dc-cols">
<div>
<ul class="dc-points">
  <li>A computer cannot produce chance. Its numbers come from a recipe, started from a <b>seed</b>.</li>
  <li>The same seed gives the same sequence, every time, on every machine.</li>
  <li>With no seed, one is taken from the clock.</li>
  <li>That is a <b>feature</b>: a result that cannot be repeated cannot be checked or debugged.</li>
</ul>
</div>
<div>
{{< highlight python >}}
import numpy as np

rng = np.random.default_rng(8410)

rng.integers(1, 7, size=10)   # ten dice
rng.random()                  # 0 to 1
rng.poisson(40)               # arrivals
rng.exponential(4)            # a waiting time
rng.choice(items, size=5)     # with repeats
rng.choice(items, size=5, replace=False)
rng.permutation(items)        # a random order
{{< /highlight >}}
</div>
</div>

<p class="dc-small"><code>rng.integers(1, 7)</code> leaves out the upper end, like <code>range</code>. <code>random.randint(1, 6)</code> includes it. Mix them up and your dice never show a six.</p>

{{% note %}}
The generator is a value you hold, with a state: each draw moves it forward. Sampling with replacement is rolling a die; without replacement is dealing cards. Which one a problem needs is the first question to ask.
{{% /note %}}

***

<p class="dc-kicker">Concept 3</p>

## One trial, many trials

<div class="dc-code-lg">
{{< highlight python >}}
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
run_trials(trial, 10_000, rng).mean()     # True counts as 1: the share
{{< /highlight >}}
</div>

<p class="dc-small"><code>run_trials</code> knows nothing about dice. It runs any trial. Put the <b>randomness</b> in one small function and the <b>arithmetic</b> in another, which can then be checked by hand.</p>

***

<p class="dc-kicker">Concept 3, the classic bug</p>

## One generator, made once, at the top

<div class="dc-cols">
<div>
<h4 class="bad">Every trial is the same trial</h4>
{{< highlight python >}}
for number in range(trials):
    rng = np.random.default_rng(1)
    outcomes[number] = trial(rng)

# runs, prints a number,
# and the number is 0 or 1
{{< /highlight >}}
</div>
<div>
<h4 class="good">The generator is passed along</h4>
{{< highlight python >}}
rng = np.random.default_rng(1)

for number in range(trials):
    outcomes[number] = trial(rng)
{{< /highlight >}}
</div>
</div>

<ul class="dc-points">
  <li>The trial <b>takes the generator as an argument</b>. It does not make its own.</li>
  <li><b>Never create a generator inside the loop</b>: it restarts the sequence on every pass.</li>
  <li>No global generators (<code>np.random.seed</code>, <code>random.random()</code>): any other code that draws changes your result.</li>
</ul>

***

<p class="dc-kicker">Concept 4</p>

## An estimate is uncertain

<div class="dc-code-lg">
{{< highlight python >}}
mean = outcomes.mean()
se   = outcomes.std(ddof=1) / np.sqrt(len(outcomes))    # the standard error
low, high = mean - 1.96 * se, mean + 1.96 * se
{{< /highlight >}}
</div>

<p class="dc-quote"><i>0.167, interval 0.160 to 0.175, from 10,000 trials</i></p>

<ul class="dc-points">
  <li>Twenty seeds give twenty answers, scattered around the truth. The <b>standard error</b> says how scattered, from a single run.</li>
  <li>The claim is about the method: about 95 of 100 such intervals contain the true value. About one in twenty will not.</li>
</ul>

***

<p class="dc-kicker">Concept 5</p>

## More trials, slowly better

<div class="dc-cols">
<div>
<table class="dc-table">
  <thead><tr><th>To make the error</th><th>you need</th></tr></thead>
  <tbody>
    <tr><td>half as large</td><td>4 times the trials</td></tr>
    <tr><td>a tenth as large</td><td>100 times the trials</td></tr>
  </tbody>
</table>
<ul class="dc-points">
  <li>The error shrinks with the <b>square root</b> of the trials.</li>
  <li>Enough trials: the interval is narrower than the difference you care about.</li>
  <li>Print as many digits as the standard error supports.</li>
</ul>
</div>
<div>
{{< highlight python >}}
dice = rng.integers(1, 7, size=(100_000, 2))
(dice.sum(axis=1) == 7).mean()
{{< /highlight >}}
<p class="dc-small">Hundreds of times faster than the loop. It draws in a different order, so it gives <b>different digits from the same seed</b>, both correct.</p>
</div>
</div>

<p class="dc-small">Simulations are compared by whether they agree within their standard errors, never digit for digit.</p>

***

<p class="dc-kicker">Concept 6</p>

## Comparing options fairly

<div class="dc-code-lg">
{{< highlight python >}}
demand = rng.poisson(40, size=10_000)     # drawn once

profit_a = profit(42, demand)             # both plans, the same days
profit_b = profit(43, demand)
difference = profit_b - profit_a          # one difference per day
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>Test one plan on Monday's customers and another on Saturday's, and you cannot tell the plan from the day.</li>
  <li><b>Give every option exactly the same random numbers.</b> The luck is in both results and cancels out.</li>
  <li>Interval of the difference excludes zero: the data tell them apart. Contains zero: they do not, <b>and saying so is a result</b>.</li>
</ul>

{{% note %}}
This is called common random numbers. The coffee cart: 42 and 43 pastries differ by a few cents a day, and which one wins depends on the seed. The umbrella shop: tested on separate days the answer swings by dollars and changes sign; on the same days it is steady to a few tenths.
{{% /note %}}

***

<p class="dc-kicker">Concept 7</p>

## Resampling real data: the bootstrap

<div class="dc-code-lg">
{{< highlight python >}}
means = [rng.choice(sample, size=len(sample), replace=True).mean()
         for number in range(5_000)]
low, high = np.quantile(means, [0.025, 0.975])
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>You cannot sample the world again. The sample is your best picture of it, so draw from <b>it</b>, with replacement.</li>
  <li>No formula needed: works for a median, a quantile, or a correlation as well.</li>
  <li>Its limit is the sample: a small sample knows little about rare, extreme values.</li>
</ul>

{{% note %}}
2,000 of several hundred thousand infestation areas: heavily skewed. The interval for the mean is wide and sometimes misses the true value, because the sample may have missed the few giants. The interval for the median holds up far better.
{{% /note %}}

***

<p class="dc-kicker">Worked example — notebook 2</p>

## One person at the help desk, or two?

<p class="dc-small">A visitor every four minutes on average; a visit takes three and a half. On paper one person keeps up.</p>

<div class="dc-flow">
  <div class="dc-node">The model<div class="dc-owner">randomness in one function</div></div>
  <div class="dc-arrow">→</div>
  <div class="dc-node">Check<div class="dc-owner">on known answers</div></div>
  <div class="dc-arrow">→</div>
  <div class="dc-node dark">Many days<div class="dc-owner">with intervals</div></div>
  <div class="dc-arrow">→</div>
  <div class="dc-node">1 vs 2<div class="dc-owner">on the same days</div></div>
  <div class="dc-arrow">→</div>
  <div class="dc-node">What if<div class="dc-owner">it gets busier?</div></div>
</div>

<div class="dc-grid">
  <div class="dc-card red"><h3>One person</h3><p>Average wait about a quarter of an hour. One day in four is worse than twenty minutes.</p></div>
  <div class="dc-card green"><h3>Two people</h3><p>On the same simulated days, the wait is under a minute.</p></div>
</div>

<p class="dc-small" style="margin-top: 14px;">Waiting does not grow in step with traffic: near full use, a small rise in arrivals adds a large amount of waiting.</p>

{{% note %}}
Arrivals come in bursts and some visits are long, so queues build and take an hour to clear. Varying the inputs you guessed (sensitivity analysis) is one of the most valuable things a simulation can do. The notebook ends with what the model leaves out.
{{% /note %}}

***

<p class="dc-kicker">Reporting</p>

## What goes with a simulated number

<p class="dc-quote">A simulated number without its seed and its number of trials cannot be checked, and without its interval cannot be judged.</p>

<ul class="dc-points">
  <li>the <b>estimate</b> and its <b>interval</b>;</li>
  <li>the <b>number of trials</b> and the <b>seed</b>;</li>
  <li>the <b>model</b>: what was assumed.</li>
</ul>

<p class="dc-small">The simulation answers the model, not the world.</p>

***

<p class="dc-kicker">To take away</p>

## Key points

<ul class="dc-points">
  <li>A simulation answers a question by running an experiment many times and counting.</li>
  <li>The numbers follow from a seed. Fix it, and hold the generator in a variable.</li>
  <li>One generator, made once, passed to every function that draws.</li>
  <li>An estimate changes from run to run. Report its interval.</li>
  <li>A hundred times the trials for one more decimal place.</li>
  <li>Compare options on the same random draws.</li>
  <li>Report the seed, the number of trials, the interval and the assumptions.</li>
</ul>

***

<p class="dc-kicker">Now: hands-on</p>

## Over to the notebooks

<p class="dc-small">Folder <a href="https://github.com/molnarai/DataScienceProgramming/tree/main/10-Simulation-Randomness"><code>10-Simulation-Randomness</code></a> — work them in this order:</p>

<div class="dc-grid three">
  <div class="dc-card green"><h3><span class="dc-nb"><span class="num">1</span></span>Chance on Purpose</h3><p class="dc-from">Concepts</p><p>Dice, doors, seeds, trials, standard errors, fair comparisons, and resampling. Four exercises.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">2</span></span>Help Desk</h3><p class="dc-from">Worked example</p><p>A simulation study in eight steps, from the model to the recommendation. Run it on ARC.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">3</span></span>Reference</h3><p class="dc-from">Look things up</p><p>Generator methods and simulation patterns to keep open while you work.</p></div>
</div>

<p class="dc-small" style="margin-top: 20px;">As you work, ask of every number: <b>what would it be with another seed?</b><br>Homework: <a href="../../assignments/assignment-09/">Homework 9: An Answer with Error Bars</a></p>
