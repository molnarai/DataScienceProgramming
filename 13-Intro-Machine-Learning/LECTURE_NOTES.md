# Lecture Notes — Session 13: Introductory Machine Learning

## 1. The problem

Every program earlier in this course followed a rule that a person wrote:
*if the area is below one acre, call it small*. Some rules nobody can write
down.

- Which customers are about to cancel?
- Which transactions are fraudulent?
- Will tomorrow be a busy day?
- Which restaurants will have closed by next year?

Experts have intuitions about these, and the intuitions do not reduce to a
few `if` statements. What usually does exist is **a record of past cases with
their outcomes**: last year's customers and who cancelled, past transactions
and which were fraud. **Machine learning** is the idea of handing those
examples to a program and letting it find a rule: the examples are the input
and the rule is the output.

Producing predictions this way takes three lines of code. That is not the
problem. The problem is everything around those three lines:

- **Is the model any good?** Compared with what?
- **Will it work on cases it has not seen?** A model can score perfectly on
  its own examples and be useless on new ones.
- **Which mistakes does it make?** Missing a fraud and raising a false alarm
  are not the same error.
- **Is it cheating?** A model will use any column that helps, including ones
  that would not exist at the moment a real prediction is needed.

A model that is wrong does not raise an error. It prints a number, and the
number looks fine. This session is about how to tell.

## 2. Core concepts, and how Python realizes them

### The packages

| Package | Purpose | What it gives you |
|---|---|---|
| **scikit-learn** (`sklearn`) | machine learning | dozens of models behind one interface (`fit`, `predict`, `score`); splitting data; metrics; baselines; cross-validation |
| **pandas** | preparing the data | building the table of features: filling blanks, encoding categories, selecting columns |
| **NumPy** | arrays | what scikit-learn computes on and returns |
| **matplotlib** | looking | plots of accuracy against model complexity; pictures of what a model has learned |

scikit-learn's strength is uniformity. Every model, from a decision tree to
methods far beyond this course, is used with the same four steps, so what you
learn on one transfers to all.

### Concept 1 — Features and target

The table is cut into two pieces.

| | Name | Example |
|---|---|---|
| what the model may look at | **features**, `X` | temperature, rain, weekend |
| what it should predict | **target**, `y` | busy or not |

```python
X = days[["temperature", "rain", "weekend"]]
y = days["busy"]
```

A target that is a category makes the task **classification**; a target that
is a number makes it **regression**. This session covers classification with
two classes, coded 0 and 1, where 1 is the outcome you are looking for.

A model works on numbers only, so the features have to be prepared:

- **missing values**: fill them, and keep the fact that they were missing in
  a column of its own (`price.fillna(0)` together with
  `price.notna().astype(int)`), because a blank is often informative;
- **True/False**: 1 and 0;
- **categories**: one 0/1 column per value ("one-hot encoding"). Numbering
  the categories 1, 2, 3 would invent an order and distances that are not
  there;
- **identifiers and names**: leave them out. They let a model memorise rows.

### Concept 2 — Train and test

Train a model on all the data, ask how many of those same rows it gets right,
and the answer is often close to 100 %. That is an exam whose questions were
handed out beforehand: a high mark shows the answers were remembered.

The most important habit in the subject: **before any learning, put some rows
aside.** The model learns from the **training set** and is measured on the
**test set**, rows it has never seen.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=13)
```

`random_state` is the seed of the shuffle: the same seed gives the same
split, so the result can be reproduced.

Three rules follow, and breaking any of them produces a number that looks
better than the truth:

1. the test set is put aside **first**;
2. nothing that is learned or chosen may use it;
3. it is used **once**, at the end.

A random split suits data whose rows are independent. When the model will
predict the future from the past, the honest test set is the *later* part of
the data, not a random part.

### Concept 3 — The baseline

Before any model: how well does the simplest possible guess do? Always answer
with whichever class is more common in the training set.

```python
majority = y_train.value_counts().idxmax()
baseline = (y_test == majority).mean()
```

That number changes how every other number reads. "70 % accurate" means
little if always saying "no" scores 67 %. When one class is rare, the
baseline is very high: if one case in forty is positive, "never" is 97.5 %
accurate and finds nothing. A model that does not beat the baseline is a
finding, and should be reported as one.

### Concept 4 — A decision tree

A **decision tree** predicts by asking yes/no questions about the features,
one after another, like the game of twenty questions. Each question compares
one feature with a number: *is the temperature at most 15 degrees?* Each
answer leads to another question or to a verdict.

Training means **choosing the questions**. For the first one, the program
tries every feature and every threshold, and keeps the question that sorts
the training examples most cleanly. Then it does the same on each side, with
the examples that landed there.

```python
from sklearn.tree import DecisionTreeClassifier, export_text

model = DecisionTreeClassifier(max_depth=2, random_state=13)   # make
model.fit(X_train, y_train)                                    # learn
predictions = model.predict(X_test)                            # predict
model.score(X_test, y_test)                                    # accuracy

print(export_text(model, feature_names=list(X.columns)))       # read it
```

Those four steps, make, fit, predict, score, are the same for every model in
scikit-learn.

A small tree can be **read**, and checked against common sense. That is its
great advantage over models that predict a little better and explain nothing.

### Concept 5 — Overfitting

`max_depth` limits how many questions the tree may ask in a row. Let it grow
without limit and it keeps splitting until nearly every training example has
a verdict of its own. Drawn as regions, a small tree shades one broad area
("cold days are busy") and an unlimited one shades a bar code of slivers,
each there to get one or two particular days right.

That is **overfitting**: fitting the training examples, noise included, and
doing worse on anything new. It shows when both accuracies are measured as
the model grows:

| Depth | Accuracy on training rows | Accuracy on unseen rows |
|---:|---:|---:|
| 1 | modest | modest |
| 4 | better | best |
| 20 | nearly 100 % | lower again |

Training accuracy can only rise. Test accuracy rises, stalls, then falls. The
widening gap is the picture of overfitting, and a deep enough tree can end up
**below the baseline** on new data while scoring 99 % on its own.

Which depth, then? Not the one with the best test score: that would use the
test set to choose. Split the *training* set again and choose on a
**validation set**:

```text
 all rows ──▶ training set ──▶ fit part          models are trained here
          │                └──▶ validation part  the settings are chosen here
          └──▶ test set                          the final model is measured here, once
```

`cross_val_score` repeats the validation split several times and reports all
the results, which shows how much one split's number can move by chance.

### Concept 6 — Beyond accuracy

Accuracy counts mistakes without saying which. Lay the predictions against
what happened, with 1 as the class being looked for:

| | Is 1 | Is 0 |
|---|---|---|
| **Predicted 1** | true positive | false positive: a false alarm |
| **Predicted 0** | false negative: a miss | true negative |

This is the **confusion matrix**. Two scores come from it besides accuracy:

| Score | Formula | Question |
|---|---|---|
| **precision** | tp / (tp + fp) | when it says 1, how often is it right? |
| **recall** | tp / (tp + fn) | of the real 1s, how many does it find? |

Precision is about false alarms; recall is about misses. They pull against
each other: flag everything and recall is 100 % with terrible precision. Which
matters more depends on what each kind of mistake costs, which is a business
decision, not a setting.

```python
from sklearn.metrics import confusion_matrix, precision_score, recall_score

confusion_matrix(y_test, predictions)     # laid out [[tn, fp], [fn, tp]]
```

The baseline "always 0" has recall 0, and its precision is 0 divided by 0:
undefined. So a model can match the baseline on accuracy and be useless, or
lose to it on accuracy and be the useful one. With a rare class, compare
precision and recall, never accuracy alone.

### Concept 7 — Leakage

A feature **leaks** when it carries information that would not be available
at the moment a real prediction is needed: a column filled in after the
outcome, an average that includes the row itself, a statistic computed over
training and test rows together. The model seizes on it, scores brilliantly,
and is worthless in use.

Its symptom is a score too good to be true. The checks: read what the model
uses (print the tree); ask of every feature, *would I have this value on the
day?*; and compute anything learned from data, including fill values and
group averages, from the training rows only.

### What a model is not

- It finds **what goes together**, not what causes what.
- It knows **only the world it was shown**. It predicts the future only as far
  as the future resembles the past.
- It has **no judgement about its inputs**. It will use any column that
  helps.

## 3. Business use cases

**Staffing a coffee cart.** A year of records: temperature, rain, weekend,
and whether the day was busy. A tree trained and scored on all the days is
95 % accurate; scored on days put aside, 65 %. Always saying "quiet" gets
57 %. So the model has earned eight points, not ninety-five. A tree of depth
two says cold days are busy, which the owner can check against experience. An
unlimited tree memorises the year. For the owner the two kinds of mistake
differ: predicting "quiet" on a busy day means a queue down the street;
predicting "busy" on a quiet day means paying someone to stand around. Recall
and precision put numbers on those two.

**Which complaints will be answered late?** A regulator forwards 1.3 million
consumer complaints to companies; one in forty is answered late. An agency
would like to flag those on arrival.

- Always saying "on time" is 97.5 % accurate.
- A first model, using the product, the channel and the date, is also 97.5 %
  accurate, and flags nothing: recall 0. Reported by its accuracy alone it
  would look excellent.
- A second model reaches perfect precision by using the company's response
  category, one value of which is "untimely response". That column is written
  after the outcome. The model is reading the answer, and has to be
  discarded.
- A feature built with thought does better: each company's past share of late
  answers, computed from the training rows only. Accuracy moves from 97.5 %
  to 97.9 %; recall goes from 0 to about 0.3, with seven alarms in ten real. A
  change that barely moves the accuracy turned a model that does nothing into
  one that does something.
- Trained on earlier years and tested on later ones, its precision falls to
  about five in ten: companies change, and a random split had been
  optimistic.

Most of the improvement came from the choice of feature, not from the
algorithm, which is the usual experience.

**Which restaurants close?** A review site lists 52,000 restaurants, a third
of them closed. From rating, review count, price level and whether hours are
listed, a tree of moderate depth is right for 72 % of restaurants it has not
seen, against 67 % for always saying "open": a real but modest gain. A tree
of depth 30 is 99 % right on its training restaurants and 65 % on new ones,
below the baseline. A small tree's first question is whether opening hours
are listed. Does a restaurant close because it lists no hours, or does a closed
restaurant's listing lose its hours? The model cannot say. A lender tempted
to use such a model to decide on loans would need to ask what happens to the
restaurants it gets wrong, in each direction, and whether a pattern in past
listings says anything about restaurants that open next year.

**Fraud, churn, defects, disease.** These share the shape of the complaints
example: the interesting class is rare, so accuracy is the wrong score, the
baseline is high, and the real questions are how many cases are found
(recall), how many alarms are real (precision), and what each kind of error
costs.

## What to report

- the task and the target; the data and how the classes divide;
- the features, and what was left out and why;
- the split and its seed;
- **the baseline**;
- how settings were chosen (on a validation set);
- the result **on the test set**: accuracy, precision, recall;
- how steady it is across seeds;
- what the model cannot tell you.

## Key points

- The examples are the input; the rule is the output.
- Put the test rows aside first, and use them once.
- Compute the baseline before any model.
- Watch training and test accuracy together: the gap is overfitting.
- Choose settings on a validation set, never on the test set.
- Report which mistakes, not only how many.
- A score that is too good is a warning. Look for a leak.
