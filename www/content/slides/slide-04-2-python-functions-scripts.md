+++
title = "Functions as Decomposition"
description = "How the four payoffs of decomposition — clarity, reuse, checking, collaboration — become Python function design"
weight = 42
outputs = ["Reveal"]
math = false
thumbnail = "/imgs/Programming_Function_Coding_Contract.png"

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
  .reveal .dc-node.dark { background: #003478; color: #fff; padding: 18px 22px; }
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

  /* Pillar tag */
  .reveal .dc-map { display: flex; gap: 10px; align-items: center; font-size: 0.6em; margin: 0 0 10px 0; }
  .reveal .dc-map span { padding: 3px 10px; border-radius: 12px; background: #f4f6f9; border: 1px solid #003478; }
  .reveal .dc-map span.py { background: #003478; color: #fff; }

  .reveal .dc-table { font-size: 0.58em; width: 100%; margin-top: 10px; }
  .reveal .dc-table td { vertical-align: top; }
  .reveal .dc-table td:first-child { width: 36%; }

  .reveal .dc-nb { font-size: 0.6em; }
  .reveal .dc-nb .num { display: inline-block; width: 1.6em; height: 1.6em; line-height: 1.6em; text-align: center; border-radius: 50%; background: #003478; color: #fff; font-weight: 700; margin-right: 6px; }
  .reveal .dc-path { font-family: var(--r-code-font); font-size: 0.6em; background: #f4f6f9; border: 1px solid #ccc; border-radius: 4px; padding: 8px 12px; display: inline-block; }
</style>

<p class="dc-kicker">IFI 8410 — Session 4: Functions and Decomposition</p>
<h1>Functions as Decomposition</h1>
<p class="dc-sub">From tasks and handoffs to contracts and return values</p>

{{% note %}}
Picks up where the decomposition deck ended: "In Python, the pieces are functions." This deck makes that claim precise, one payoff at a time, and ends by sending students into the notebooks.
{{% /note %}}

***

<p class="dc-kicker">The core idea</p>

## A function is a boundary around one task

<p>Decomposition gave us tasks with inputs, dependencies, and an owner. In Python, a <b>function</b> is how we draw that boundary explicitly.</p>

<div class="dc-flow" style="margin-top: 36px;">
  <div class="dc-node">Inputs<div class="dc-owner">parameters</div></div>
  <div class="dc-arrow">→</div>
  <div class="dc-node dark"><b>clean_age_column</b><div class="dc-owner">one job, a clear name</div></div>
  <div class="dc-arrow">→</div>
  <div class="dc-node">Output<div class="dc-owner">return value</div></div>
</div>

<p class="dc-small" style="text-align: center; margin-top: 26px;">Everything the task needs comes <b>in</b> through parameters.<br>Everything it produces goes <b>out</b> through <code>return</code>.</p>

***

<p class="dc-kicker">The map</p>

## Four payoffs → four design habits

<div class="dc-grid">
  <div class="dc-card"><h3>Clarity → explicit contracts</h3><p class="dc-from">Vague goals become concrete actions; dependencies surface.</p><p>Descriptive names, explicit parameters, and return values — not global state or <code>print</code>.</p></div>
  <div class="dc-card"><h3>Reuse → local scope, pure functions</h3><p class="dc-from">Proven approaches preserved for future use.</p><p>Isolated local variables, new data returned, no unannounced side effects or mutation.</p></div>
  <div class="dc-card"><h3>Checking → validation and tests</h3><p class="dc-from">Review intermediate results before problems spread.</p><p>Guard clauses raising <code>TypeError</code> / <code>ValueError</code>; <code>pytest</code> assertions at the boundary.</p></div>
  <div class="dc-card"><h3>Collaboration → docstrings, type hints</h3><p class="dc-from">Clear handoffs and responsibilities.</p><p>A public contract others can call without reading the implementation.</p></div>
</div>

{{% note %}}
The next four slides take one card each. Grey text is the decomposition idea from the last deck; black text is the Python habit.
{{% /note %}}

***

<p class="dc-kicker">Pillar 1 of 4</p>

## Clarity ↔ explicit function contracts

<div class="dc-map"><span>A task with visible inputs and outputs</span><span class="dc-arrow">↔</span><span class="py">name · parameters · return value · assumptions</span></div>

<div class="dc-cols">
  <div>
    <h4 class="bad">Hidden dependency, output for humans only</h4>
{{< highlight python >}}
TAX_RATE = 0.08
prices = [4.50, 3.25, 5.00]

def total():
    print(sum(prices) * (1 + TAX_RATE))

total()   # can't reuse the number
{{< /highlight >}}
  </div>
  <div>
    <h4 class="good">Inputs explicit, result returned</h4>
{{< highlight python >}}
def order_total(prices: list[float],
                tax_rate: float) -> float:
    return sum(prices) * (1 + tax_rate)

total = order_total([4.50, 3.25, 5.00], 0.08)
print(f"${total:.2f}")   # printing is the caller's choice
{{< /highlight >}}
  </div>
</div>

<ul class="dc-points">
  <li><b>Parameters</b> replace hidden globals — every dependency is listed in the signature.</li>
  <li><b>Return</b> instead of <code>print</code> — the next step (or a test) can use the result.</li>
</ul>

***

<p class="dc-kicker">Pillar 2 of 4</p>

## Reuse ↔ local scope and pure functions

<div class="dc-map"><span>A reusable template</span><span class="dc-arrow">↔</span><span class="py">no state leaks in or out of a call</span></div>

<div class="dc-code-lg">
{{< highlight python >}}
def without_missing(values: list) -> list:
    """Return a NEW list with None values removed. Input is unchanged."""
    return [value for value in values if value is not None]

measurements = [2.1, None, 3.4]
cleaned = without_missing(measurements)

print("returned:", cleaned)          # [2.1, 3.4]
print("original:", measurements)     # [2.1, None, 3.4] -- still auditable
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li><b>Local scope</b>: temporary names disappear when the function returns.</li>
  <li><b>Return new objects</b> instead of mutating inputs — the raw data keeps its provenance.</li>
  <li>No unannounced side effects → safe to reuse in any script or parallel pipeline.</li>
</ul>

***

<p class="dc-kicker">Pillar 3 of 4 — at run time</p>

## Checking ↔ validating inputs

<div class="dc-map"><span>A checkpoint before the next task starts</span><span class="dc-arrow">↔</span><span class="py">guard clauses at the function boundary</span></div>

<div class="dc-cols">
  <div class="dc-code-lg">
{{< highlight python >}}
def mean(values: list[float]) -> float:
    if not isinstance(values, list):
        raise TypeError("values must be a list")
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
{{< /highlight >}}
  </div>
  <div>
    <div class="dc-card red" style="margin-top: 8px;"><h3>TypeError</h3><p>Wrong <b>kind</b> of value — a string where a list was expected.</p></div>
    <div class="dc-card red" style="margin-top: 10px;"><h3>ValueError</h3><p>Right kind, <b>unusable value</b> — an empty list, an age of −5.</p></div>
  </div>
</div>

<p class="dc-small" style="margin-top: 14px;">Fail <b>before</b> computing — so a bad input never becomes a plausible-looking wrong answer downstream.</p>

***

<p class="dc-kicker">Pillar 3 of 4 — before you ship</p>

## Checking ↔ unit tests

<div class="dc-map"><span>Review each result against the standard</span><span class="dc-arrow">↔</span><span class="py">pytest runs the contract as code</span></div>

<div class="dc-code-lg">
{{< highlight python >}}
def test_validate_age():
    assert validate_age("42") == 42        # normal
    assert validate_age(" 7 ") == 7        # messy but valid
    assert validate_age("0") == 0          # boundary
    assert validate_age("120") == 120      # boundary
    assert validate_age("121") is None     # just outside
    assert validate_age("abc") is None     # not a number
    assert validate_age(None) is None      # missing
{{< /highlight >}}
</div>

<p class="dc-small">Each function is tested <b>in isolation</b> under normal, boundary, and extreme conditions — exactly the "check each piece" idea from decomposition.</p>

***

<p class="dc-kicker">Pillar 4 of 4</p>

## Collaboration ↔ contracts others can call

<div class="dc-map"><span>A clear handoff between people</span><span class="dc-arrow">↔</span><span class="py">a contract you can call without reading the code</span></div>

<div class="dc-cols">
  <div class="dc-code-lg">
{{< highlight python >}}
def validate_age(age: object) -> "int | None":
    """Return age as an int, or None when it is
    missing or implausible.

    Args:
        age: A raw age value from the survey,
             typically a string.

    Returns:
        An int between 0 and 120 inclusive,
        or None if the value cannot be used.
    """
    ...
{{< /highlight >}}
  </div>
  <div>
    <ul class="dc-points" style="margin-top: 10px;">
      <li><b>Type annotations</b> state what goes in and comes out.</li>
      <li>The <b>docstring</b> states the promise — including edge cases.</li>
      <li>A colleague calls it using <code>help(validate_age)</code>, not by reading the body.</li>
      <li>The author can <b>refactor the inside</b> freely, as long as the contract holds.</li>
    </ul>
  </div>
</div>

***

<p class="dc-kicker">The whole process</p>

## Decomposition steps → pipeline design

<table class="dc-table">
  <thead><tr><th>Decomposition process</th><th>Python pipeline</th></tr></thead>
  <tbody>
    <tr><td><b>1.</b> Describe the final outcome</td><td>Define the pipeline's return type and output schema.</td></tr>
    <tr><td><b>2.</b> Identify major tasks</td><td>Top-level functions: <code>load_data</code>, <code>clean_data</code>, <code>summarize</code>, <code>export</code>.</td></tr>
    <tr><td><b>3.</b> Divide into smaller steps</td><td>Focused helpers for granular work, e.g. <code>validate_age</code>.</td></tr>
    <tr><td><b>4.</b> Order tasks, find dependencies</td><td>Chain functions: each return value becomes the next argument.</td></tr>
    <tr><td><b>5.</b> Assign responsibility and checks</td><td>Guard clauses (<code>TypeError</code> / <code>ValueError</code>) and <code>pytest</code> tests per function.</td></tr>
    <tr><td><b>6.</b> Review and adjust</td><td>Refactor internals while keeping docstrings and type hints consistent.</td></tr>
  </tbody>
</table>

***

<p class="dc-kicker">Putting it together</p>

## Design the stages first

<div class="dc-code-lg">
{{< highlight python >}}
def load_survey_data(path: str) -> list[dict]: ...
def validate_age(age: object) -> "int | None": ...
def clean_age_column(rows: list[dict]) -> list[dict]: ...
def summarize_by_region(rows: list[dict]) -> list[dict]: ...
def export_summary(summary: list[dict], path: str) -> None: ...

rows    = load_survey_data("survey.csv")
cleaned = clean_age_column(rows)
summary = summarize_by_region(cleaned)
export_summary(summary, "summary_by_region.csv")
{{< /highlight >}}
</div>

<p class="dc-small">Five named stages. Each one can now be <b>discussed, tested, and replaced</b> on its own — before a single body is written.</p>

{{% note %}}
This skeleton is taken directly from the Deep Dive notebook. Point out that the signatures alone already record the handoffs: the list[dict] returned by one stage is the argument to the next.
{{% /note %}}

***

<p class="dc-kicker">Now: hands-on</p>

## Over to the notebooks

<p class="dc-small">Folder <a href="https://github.com/molnarai/DataScienceProgramming/tree/main/04-Functions-Decomposition"><code>04-Functions-Decomposition</code></a> — same material at three altitudes. Work them in this order:</p>

<div class="dc-grid three" style="margin-top: 18px;">
  <div class="dc-card green"><h3><span class="dc-nb"><span class="num">1</span></span>Examples</h3><p class="dc-from">Practice</p><p>25 worked examples, easy to medium, each with a <i>Try it</i> cell: parameters and <code>return</code>, tables, edge cases, functions as values.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">2</span></span>Anatomy</h3><p class="dc-from">Mechanics</p><p>Every part of a function: scope and LEGB, arguments, defaults, <code>*args</code> / <code>**kwargs</code>, annotations, <code>lambda</code>, closures.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">3</span></span>Deep Dive</h3><p class="dc-from">Design reasoning</p><p>Why functions are designed this way: contracts, side effects, validation, the survey pipeline from today's slides.</p></div>
</div>

<p class="dc-small" style="margin-top: 20px;">As you work, ask of every function: <b>is it clear, reusable, checkable, and callable by someone else?</b></p>

{{% note %}}
Several Anatomy cells are written to fail or surprise (UnboundLocalError, the mutable default trap, a closure loop printing [40, 40, 40]) — tell students that is intentional, so they run the cells rather than skip them.
{{% /note %}}

***

<p class="dc-kicker">Let's code</p>

<h2 style="margin-top: 40px;">Open your first notebook</h2>

<p class="dc-path">04-Functions-Decomposition/Examples_of_Python_Functions_orig.ipynb</p>

<ol class="dc-points" style="margin-top: 30px;">
  <li>Pull the latest course repository.</li>
  <li>Open the notebook and run the cells from the top.</li>
  <li>Stop at each <i>Try it</i> cell — change something and predict the result before you run it.</li>
</ol>

<p class="dc-small dc-muted" style="margin-top: 30px;">Reference while you work: <a href="../slide-04-1-decomposition/">Decomposition deck</a> · <a href="../../blog/decomposition/">Decomposition reading</a></p>
