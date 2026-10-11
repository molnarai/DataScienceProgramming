+++
title = "Introductory Machine Learning"
description = "Features and target, train and test, the baseline, decision trees, overfitting, precision and recall, and leakage: how to tell whether a model is any good"
weight = 130
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

<p class="dc-kicker">IFI 8410 — Session 13: Introductory Machine Learning</p>
<h1>Learning from Examples</h1>
<p class="dc-sub">The examples are the input; the rule is the output</p>

{{% note %}}
Every program earlier in this course followed a rule that a person wrote. Today the program finds the rule, and the session is about how to tell whether the rule is any good.
{{% /note %}}

***

<p class="dc-kicker">The problem</p>

## Rules nobody can write down

<ul class="dc-points">
  <li>Which customers are about to cancel?</li>
  <li>Which transactions are fraudulent?</li>
  <li>Will tomorrow be a busy day?</li>
  <li>Which restaurants will have closed by next year?</li>
</ul>

<p class="dc-small">What usually exists is <b>a record of past cases with their outcomes</b>. Machine learning hands those examples to a program and lets it find a rule. That takes three lines of code. The problem is everything around them:</p>

<div class="dc-grid">
  <div class="dc-card"><h3>Is the model any good?</h3><p>Compared with what?</p></div>
  <div class="dc-card"><h3>Will it work on cases it has not seen?</h3><p>A model can score perfectly on its own examples and be useless on new ones.</p></div>
  <div class="dc-card red"><h3>Which mistakes does it make?</h3><p>Missing a fraud and raising a false alarm are not the same error.</p></div>
  <div class="dc-card red"><h3>Is it cheating?</h3><p>A model will use any column that helps, including ones that would not exist when a real prediction is needed.</p></div>
</div>

{{% note %}}
A model that is wrong does not raise an error. It prints a number, and the number looks fine.
{{% /note %}}

***

<p class="dc-kicker">The tools</p>

## Four packages

<div class="dc-grid">
  <div class="dc-card green"><h3>scikit-learn</h3><p class="dc-from">machine learning</p><p>Dozens of models behind one interface: <code>fit</code>, <code>predict</code>, <code>score</code>. Splitting data, metrics, baselines, cross-validation.</p></div>
  <div class="dc-card"><h3>pandas</h3><p class="dc-from">preparing the data</p><p>Building the table of features: filling blanks, encoding categories, selecting columns.</p></div>
  <div class="dc-card"><h3>NumPy</h3><p class="dc-from">arrays</p><p>What scikit-learn computes on and returns.</p></div>
  <div class="dc-card"><h3>matplotlib</h3><p class="dc-from">looking</p><p>Accuracy against model complexity; pictures of what a model has learned.</p></div>
</div>

<p class="dc-small" style="margin-top: 18px;">scikit-learn's strength is uniformity: every model is used with the same four steps, so what you learn on one transfers to all.</p>

***

<p class="dc-kicker">Concept 1</p>

## Features and target

<div class="dc-cols">
<div>
{{< highlight python >}}
X = days[["temperature", "rain", "weekend"]]
y = days["busy"]
{{< /highlight >}}
<table class="dc-table">
  <thead><tr><th></th><th>Name</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td>what the model may look at</td><td><b>features</b>, <code>X</code></td><td>temperature, rain, weekend</td></tr>
    <tr><td>what it should predict</td><td><b>target</b>, <code>y</code></td><td>busy or not</td></tr>
  </tbody>
</table>
</div>
<div>
<ul class="dc-points">
  <li><b>Missing values</b>: fill them, and keep the fact in a column of its own. A blank is often informative.</li>
  <li><b>True/False</b>: 1 and 0.</li>
  <li><b>Categories</b>: one 0/1 column per value (one-hot). Numbering them 1, 2, 3 invents an order.</li>
  <li><b>Identifiers and names</b>: leave them out. They let a model memorise rows.</li>
</ul>
</div>
</div>

<p class="dc-small">A target that is a category makes the task <b>classification</b>; a number makes it <b>regression</b>. Today: two classes, 0 and 1, where 1 is the outcome you are looking for.</p>

{{% note %}}
A model works on numbers only, so the features have to be prepared. price.fillna(0) together with price.notna().astype(int).
{{% /note %}}

***

<p class="dc-kicker">Concept 2</p>

## Train and test

<div class="dc-code-lg">
{{< highlight python >}}
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=13)
{{< /highlight >}}
</div>

<p class="dc-small">Score a model on the rows it learned from and the answer is often close to 100 %. That is an exam whose questions were handed out beforehand.</p>

<ol class="dc-points">
  <li>The test set is put aside <b>first</b>.</li>
  <li><b>Nothing</b> that is learned or chosen may use it.</li>
  <li>It is used <b>once</b>, at the end.</li>
</ol>

<p class="dc-small">Breaking any of the three produces a number that looks better than the truth. When the model will predict the future from the past, the honest test set is the <b>later</b> part of the data, not a random part.</p>

{{% note %}}
The most important habit in the subject. random_state is the seed of the shuffle, as in Session 10.
{{% /note %}}

***

<p class="dc-kicker">Concept 3</p>

## The baseline

<div class="dc-code-lg">
{{< highlight python >}}
majority = y_train.value_counts().idxmax()     # learned from the training set
baseline = (y_test == majority).mean()         # measured on the test set
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>Before any model: how well does the simplest possible guess do?</li>
  <li>"70 % accurate" means little if always saying "no" scores 67 %.</li>
  <li>When one class is rare, the baseline is very high: one positive in forty, and "never" is <b>97.5 % accurate and finds nothing</b>.</li>
</ul>

<p class="dc-quote">A model that does not beat the baseline is a finding, and should be reported as one.</p>

***

<p class="dc-kicker">Concept 4</p>

## A decision tree

<div class="dc-code-lg">
{{< highlight python >}}
from sklearn.tree import DecisionTreeClassifier, export_text

model = DecisionTreeClassifier(max_depth=2, random_state=13)   # make
model.fit(X_train, y_train)                                    # learn
predictions = model.predict(X_test)                            # predict
model.score(X_test, y_test)                                    # accuracy

print(export_text(model, feature_names=list(X.columns)))       # read it
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>Twenty questions: <i>is the temperature at most 15 degrees?</i> Each answer leads to another question or to a verdict.</li>
  <li>Training means <b>choosing the questions</b>: the one that sorts the training examples most cleanly, then the same on each side.</li>
  <li>A small tree can be <b>read</b>, and checked against common sense.</li>
</ul>

{{% note %}}
Make, fit, predict, score: the same four steps for every model in scikit-learn.
{{% /note %}}

***

<p class="dc-kicker">Concept 5</p>

## Overfitting

<div class="dc-cols">
<div>
<table class="dc-table">
  <thead><tr><th>Depth</th><th>Training rows</th><th>Unseen rows</th></tr></thead>
  <tbody>
    <tr><td>1</td><td>modest</td><td>modest</td></tr>
    <tr><td>4</td><td>better</td><td><b>best</b></td></tr>
    <tr><td>20</td><td>nearly 100 %</td><td><b>lower again</b></td></tr>
  </tbody>
</table>
<p class="dc-small">Training accuracy can only rise. Test accuracy rises, stalls, then falls. <b>The widening gap is the picture of overfitting.</b></p>
</div>
<div>
<ul class="dc-points">
  <li><code>max_depth</code> limits how many questions the tree may ask in a row.</li>
  <li>Without a limit it keeps splitting until nearly every training example has a verdict of its own.</li>
  <li>A small tree shades one broad area: "cold days are busy". An unlimited one shades a bar code of slivers.</li>
  <li>A deep enough tree can end up <b>below the baseline</b> on new data while scoring 99 % on its own.</li>
</ul>
</div>
</div>

{{% note %}}
Notebook 1 draws the regions. Overfitting is fitting the training examples, noise included, and doing worse on anything new.
{{% /note %}}

***

<p class="dc-kicker">Concept 5, continued</p>

## Choosing the depth honestly

<p class="dc-small">Which depth, then? <b>Not the one with the best test score</b>: that would use the test set to choose.</p>

<div class="dc-code-lg">
{{< highlight text >}}
 all rows ──▶ training set ──▶ fit part          models are trained here
          │                └──▶ validation part  the settings are chosen here
          └──▶ test set                          the final model is measured here, once
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>The choice is part of the learning, so it gets its own rows.</li>
  <li><code>cross_val_score</code> repeats the validation split several times, which shows how much one split's number can move by chance.</li>
</ul>

***

<p class="dc-kicker">Concept 6</p>

## Beyond accuracy

<div class="dc-cols">
<div>
<h4>The confusion matrix</h4>
<table class="dc-table">
  <thead><tr><th></th><th>Is 1</th><th>Is 0</th></tr></thead>
  <tbody>
    <tr><td><b>Predicted 1</b></td><td>true positive</td><td>false positive:<br>a false alarm</td></tr>
    <tr><td><b>Predicted 0</b></td><td>false negative:<br>a miss</td><td>true negative</td></tr>
  </tbody>
</table>
</div>
<div>
<h4>Two more scores</h4>
<table class="dc-table">
  <thead><tr><th>Score</th><th>Formula</th><th>Question</th></tr></thead>
  <tbody>
    <tr><td><b>precision</b></td><td>tp / (tp + fp)</td><td>when it says 1, how often is it right?</td></tr>
    <tr><td><b>recall</b></td><td>tp / (tp + fn)</td><td>of the real 1s, how many does it find?</td></tr>
  </tbody>
</table>
</div>
</div>

<ul class="dc-points">
  <li>Precision is about false alarms; recall is about misses. They pull against each other.</li>
  <li>Which matters more depends on what each mistake costs: <b>a business decision, not a setting</b>.</li>
  <li>"Always 0" has recall 0 and undefined precision. With a rare class, never compare accuracy alone.</li>
</ul>

<p class="dc-small"><code>confusion_matrix(y_test, predictions)</code> is laid out <code>[[tn, fp], [fn, tp]]</code>.</p>

***

<p class="dc-kicker">Concept 7</p>

## Leakage

<p class="dc-quote">A feature <b>leaks</b> when it carries information that would not be available at the moment a real prediction is needed.</p>

<div class="dc-grid">
  <div class="dc-card red"><h3>What it looks like</h3><p>A column filled in after the outcome. An average that includes the row itself. A statistic computed over training and test rows together.</p></div>
  <div class="dc-card red"><h3>The symptom</h3><p>A score too good to be true. The model seizes on the leak, scores brilliantly, and is worthless in use.</p></div>
</div>

<ul class="dc-points">
  <li>Read what the model uses: print the tree.</li>
  <li>Ask of every feature: <i>would I have this value on the day?</i></li>
  <li>Compute anything learned from data, including fill values and group averages, from the <b>training rows only</b>.</li>
</ul>

***

<p class="dc-kicker">Worked example — notebook 1</p>

## Staffing a coffee cart

<p class="dc-small">A year of records: temperature, rain, weekend, and whether the day was busy.</p>

<div class="dc-grid three">
  <div class="dc-card red"><h3>95 %</h3><p>A tree trained <b>and scored</b> on all the days.</p></div>
  <div class="dc-card"><h3>65 %</h3><p>The same kind of tree, scored on days put aside.</p></div>
  <div class="dc-card"><h3>57 %</h3><p>Always saying "quiet".</p></div>
</div>

<ul class="dc-points">
  <li>The model has earned <b>eight points, not ninety-five</b>.</li>
  <li>A tree of depth two says cold days are busy, which the owner can check against experience.</li>
  <li>Predicting "quiet" on a busy day means a queue down the street; "busy" on a quiet day means paying someone to stand around. Recall and precision put numbers on those two.</li>
</ul>

***

<p class="dc-kicker">Worked example — notebook 2</p>

## 97.5 % accurate and useless

<p class="dc-small">1.3 million consumer complaints; one in forty is answered late. An agency would like to flag those on arrival.</p>

<table class="dc-table">
  <thead><tr><th>Model</th><th>What happened</th></tr></thead>
  <tbody>
    <tr><td>Always "on time"</td><td>97.5 % accurate.</td></tr>
    <tr><td>Product, channel, date</td><td>Also 97.5 %, and flags nothing: <b>recall 0</b>.</td></tr>
    <tr><td>Adds the company's response category</td><td>Perfect precision. One value is "untimely response", written <b>after</b> the outcome. <b>A leak</b>: discard.</td></tr>
    <tr><td>Each company's past share of late answers, from training rows only</td><td>Accuracy 97.5 % → 97.9 %. Recall 0 → about 0.3, with seven alarms in ten real.</td></tr>
    <tr><td>Trained on earlier years, tested on later ones</td><td>Precision falls to about five in ten. The random split had been optimistic.</td></tr>
  </tbody>
</table>

<p class="dc-small">Most of the improvement came from the <b>choice of feature</b>, not from the algorithm, which is the usual experience.</p>

{{% note %}}
A change that barely moves the accuracy turned a model that does nothing into one that does something. Fraud, churn, defects and disease share this shape: the interesting class is rare, so accuracy is the wrong score.
{{% /note %}}

***

<p class="dc-kicker">Reporting</p>

## What a model is not, and what to report

<div class="dc-grid three">
  <div class="dc-card"><h3>It finds what goes together</h3><p>Not what causes what. Does a restaurant close because it lists no hours, or does a closed restaurant's listing lose its hours?</p></div>
  <div class="dc-card"><h3>It knows only the world it was shown</h3><p>It predicts the future only as far as the future resembles the past.</p></div>
  <div class="dc-card"><h3>It has no judgement about its inputs</h3><p>It will use any column that helps.</p></div>
</div>

<ul class="dc-points">
  <li>the task, the target, and how the classes divide; the features, and what was left out and why;</li>
  <li>the split and its seed; <b>the baseline</b>; how settings were chosen;</li>
  <li>the result <b>on the test set</b>: accuracy, precision, recall; how steady it is across seeds;</li>
  <li>what the model cannot tell you.</li>
</ul>

{{% note %}}
The restaurant question is the data of Homework 12: 52,000 restaurants, a third closed. A moderate tree is right for 72 % of unseen restaurants against 67 % for always saying open; a tree of depth 30 is 99 % right on its training restaurants and 65 % on new ones, below the baseline.
{{% /note %}}

***

<p class="dc-kicker">To take away</p>

## Key points

<ul class="dc-points">
  <li>The examples are the input; the rule is the output.</li>
  <li>Put the test rows aside first, and use them once.</li>
  <li>Compute the baseline before any model.</li>
  <li>Watch training and test accuracy together: the gap is overfitting.</li>
  <li>Choose settings on a validation set, never on the test set.</li>
  <li>Report which mistakes, not only how many.</li>
  <li>A score that is too good is a warning. Look for a leak.</li>
</ul>

***

<p class="dc-kicker">Now: hands-on</p>

## Over to the notebooks

<p class="dc-small">Folder <a href="https://github.com/molnarai/DataScienceProgramming/tree/main/13-Intro-Machine-Learning"><code>13-Intro-Machine-Learning</code></a> — work them in this order:</p>

<div class="dc-grid three">
  <div class="dc-card green"><h3><span class="dc-nb"><span class="num">1</span></span>Learning from Examples</h3><p class="dc-from">Concepts</p><p>The coffee cart: features, the split, the baseline, a tree, overfitting, and the confusion matrix. Four exercises.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">2</span></span>Late Answers</h3><p class="dc-from">Worked example</p><p>A model that is 97.5 % accurate and useless, and how to do better, in nine steps. Run it on ARC.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">3</span></span>Reference</h3><p class="dc-from">Look things up</p><p>scikit-learn calls and the modelling workflow to keep open while you work.</p></div>
</div>

<p class="dc-small" style="margin-top: 20px;">As you work, ask of every score: <b>compared with what, and on which rows?</b><br>Homework: <a href="../../assignments/assignment-12/">Homework 12: Does It Beat Guessing?</a></p>
