+++
date = '2026-09-02'
due_date = '2026-09-15'
draft = false
title = 'Homework 1: Types, Strings, and Conditionals'
weight = 10
status = 'Scheduled'
+++

Build a complete command-line program that analyzes a corpus of newsgroup messages using nothing but core Python — no machine learning libraries, no regular expressions. Across ten test-driven phases you will read and tokenize text files, score each article for sentiment against the AFINN-111 lexicon, count terms with nested dictionaries, and rank the most distinctive keywords of each newsgroup by TF–IDF, then assemble everything into a single deterministic report. Every phase ships with its own tests, so you find out whether the piece you just wrote works before you build the next one on top of it.

<!-- more -->

---
# Homework 1: Text Analysis of the 20 Newsgroups Corpus

**Posted:** September 2, 2026 &nbsp;&nbsp;|&nbsp;&nbsp; **Due:** Tuesday, September 15, 2026 at 23:59

Related session: [Session 2 — Types, Strings, and Conditionals](../../topics/topic-02/)


## Learning objectives

In this assignment you will write a Python program that analyzes a collection of
newsgroup messages. Your program will:

1. Read text documents from files and directories.
2. Clean and tokenize text using elementary string operations.
3. Perform **lexicon-based sentiment analysis** with the AFINN-111 lexicon.
4. Compute document and corpus statistics using dictionaries.
5. Calculate TF–IDF scores.
6. Identify important keywords for each newsgroup category.
7. Produce a clear, deterministic text report.

"Sentiment analysis" here means **lexicon-based scoring**, not a trained machine
learning classifier. "Topic discovery" means **TF–IDF keyword extraction**, which
is not probabilistic topic modeling such as LDA or NMF — it is the simpler,
deterministic cousin. Everything stays at the level of core Python: file
handling, lists, dictionaries, functions, sorting, and string operations.
Regular expressions are optional and not required anywhere.

Background reading on the math: [`tfidf_tutorial.md`](tfidf_tutorial.md).

## How to work on this assignment

**Do not write the whole program and then run it.** The assignment is split into
ten phases. Each phase adds one or two functions, and each phase has its own
test file. Work in this order:

1. Read the phase description.
2. Implement only the functions in that phase.
3. Run that phase's tests: `./run_tests.sh 2` for Phase 2.
4. Fix your code until every test in that phase passes.
5. Only then move to the next phase.

Later phases call the functions you wrote in earlier phases, so a bug you leave
behind in Phase 2 will produce confusing failures in Phase 8. Catching it in
Phase 2 costs you a minute; catching it in Phase 8 can cost you an evening.

You test in two places, and they do different jobs:

| | Where | When | What it is for |
|---|---|---|---|
| **Locally** | on the cluster, `./run_tests.sh N` | constantly, while you work | Fast feedback on the phase you are writing |
| **Pipeline** | GitLab, on merge into `testing` | once a phase is done | The record of what passed; this is what counts |

Work locally. A local run takes under a second and shows you only the phase you
asked for. Merge to `testing` when a phase is finished, not after every edit.

The test suite is not hidden. It lives in [`../test/`](../test/) and you are
expected to read it. If a test fails, read the test, work out what behavior it
expects, and then decide whether the test or your understanding is right.

## Setup

Work on the `work` branch of your course repository:

```bash
git checkout work
```

The cluster environment already has everything you need: Python 3, `pytest`,
and the `stop_words` package that the starter file imports. If you are working
somewhere else, install the last two with:

```bash
pip install pytest stop-words
```

Copy the starter file into `submission/`. From the `HW01` directory:

```bash
mkdir -p submission
cp starter/news_analyzer.py submission/news_analyzer.py
```

Your directory should then look like this:

```text
Assignments/HW01/
├── instructions/
│   ├── homework01_instructions.md
│   └── tfidf_tutorial.md
├── starter/
│   └── news_analyzer.py     <- the untouched template; leave it alone
├── submission/              <- everything you write goes here
│   └── news_analyzer.py     <- the file you edit
└── test/                    <- the test suite; read it, do not edit it
    ├── conftest.py
    ├── run_tests.sh
    ├── fixtures/
    └── test_*.py
```

**Everything you submit goes in `submission/`, and the file must be named
`news_analyzer.py`.** That is where both the tests and the pipeline look. A file
left anywhere else, or under another name, is not part of your submission.

Check that the tests can find your file:

```bash
cd Assignments/HW01/test
./run_tests.sh
```

You should see a long list of failures. That is correct — you have not written
anything yet. If instead you see `Could not find news_analyzer.py`, your file is
in the wrong place; re-read the tree above.

Every `./run_tests.sh` command in this handout is run from that `test/`
directory.

## How testing works

### Locally, while you work

From `Assignments/HW01/test`:

```bash
./run_tests.sh 2      # just Phase 2's tests
./run_tests.sh        # all 156
./run_tests.sh 3 -x   # Phase 3, stopping at the first failure
```

The number is the phase you are on. This is what you should be running most of
the time — it takes under a second and shows you only the tests that matter
right now.

### In the pipeline, when a phase is done

Your repository has two branches that matter:

| Branch | What it is for |
|---|---|
| `work` | Where you write code. Commit and push here as often as you like; nothing is tested. |
| `testing` | Where you send finished work. Merging into it runs the tests and records the result. |

```bash
git add Assignments/HW01/submission
git commit -m "HW01: phase 2 complete"
git push origin work
```

Then, in GitLab, open a merge request from `work` into `testing` and merge it.
The pipeline runs the whole suite — the same 156 tests you have, taken from the
course template, plus additional tests you do not have — and reports the result
on the merge request. It runs only when files under
`Assignments/HW01/submission/` changed, so merging unrelated work does not
re-run it.

Two places show you what happened:

- **Pipelines → the `hw01` job** — the full log, every test name and every
  failure message.
- **The merge request's "Tests" tab** — a summary grouped by file, quicker to
  scan.

### What to expect while the assignment is unfinished

The pipeline always runs the whole suite. When you finish Phase 2, Phases 3
through 9 are still unwritten, so most of the pipeline will be red. **That is
expected.** Locally you look at one phase at a time; in the pipeline you look
for the phase you just finished and ignore the rest.

Only at Phase 10 should the pipeline be fully green. It will report more tests
than the 156 you can run locally; the extra ones cover the same rules this
handout describes, in cases the shipped suite does not reach. If one of them
fails while all 156 of yours pass, read the failure message — it names the rule
it is checking.

### Things to know

- **Editing `test/` achieves nothing.** The pipeline does not run your copy of
  the tests. It runs the original suite from the course template, plus
  additional tests you do not have. A weakened local test hides a failure from
  you and from nobody else.
- **Run locally first.** A red pipeline costs you a round trip; `./run_tests.sh`
  costs you a second.
- **`python3 news_analyzer.py ...` runs like any other script.** From Phase 9
  on, run the whole program yourself.

## Dataset

The corpus is supplied as newsgroup **text files**. Each `.txt` file holds many
articles, separated by header lines:

```text
Newsgroup: sci.space
document_id: 61234
Subject: Re: Space Station Redesign

The redesign proposal was released yesterday...

Newsgroup: sci.space
document_id: 61235
Subject: Shuttle launch window

The launch window opens Tuesday...
```

Two details matter:

- The **first** article in a file may be missing its `Newsgroup:` and
  `document_id:` header lines. In that case its category is the file name
  without `.txt`.
- Some files contain bytes that are not valid UTF-8. Open every file with
  `encoding="utf-8", errors="ignore"` so that these do not crash your program.

Your program must accept either a **directory** of such `.txt` files or a
**single** `.txt` file.

Do not hard-code the category names. There are 20 in the full corpus, but your
program must work with two, or with one, or with none.

## Sentiment lexicon

Sentiment comes from **AFINN-111**, a tab-separated file where each line is a
word and an integer score between −5 and +5:

```text
abandon	-2
abandoned	-2
...
wonderful	4
wow	4
```

An article's sentiment score is the **sum of the scores of its tokens**. A word
that appears three times contributes three times. Then:

| Score | Label |
|---:|---|
| Greater than 0 | `positive` |
| Less than 0 | `negative` |
| Equal to 0 | `neutral` |

This differs from a simple positive-minus-negative word count: AFINN weights
`wonderful` (+4) more heavily than `okay` (+1).

## Required command-line interface

```bash
python3 news_analyzer.py INPUT_PATH AFINN_FILE
```

For example:

```bash
python3 news_analyzer.py data/20_newsgroups AFINN-111.txt
python3 news_analyzer.py data/20_newsgroups/sci.space.txt AFINN-111.txt
```

The program prints its report to standard output. It must never wait for
interactive input.

## Required functions

Keep these names and parameter lists **exactly** as shown. You may add helper
functions, but do not remove, rename, or re-order the required ones — the tests
call them directly.

| Phase | Function | Purpose |
|---:|---|---|
| 1 | `read_afinn_lexicon(filename)` | Read AFINN-111 into a `word -> score` dictionary |
| 2 | `tokenize(text)` | Convert text into a list of normalized tokens |
| 3 | `parse_articles_from_text(text, default_category)` | Split one file's text into article records |
| 3 | `read_articles(input_path)` | Read a directory or a single file into article records |
| 4 | `sentiment_score(tokens, afinn)` | Return the integer sentiment score |
| 4 | `sentiment_label(score)` | Return `positive`, `negative`, or `neutral` |
| 5 | `document_frequencies(articles)` | Map each term to the number of documents containing it |
| 5 | `category_term_frequencies(articles)` | Nested dictionary: category → term → total count |
| 6 | `idf(number_of_documents, frequency)` | Compute IDF using `math.log` |
| 6 | `top_keywords(category_counts, document_frequency, number_of_documents, limit)` | Return ranked `(term, score)` pairs |
| 7 | `analyze_articles(articles, afinn)` | Build the overall analysis structure |
| 8 | `format_report(results, keyword_limit)` | Return the complete report as one string |
| 9 | `main()` | Parse arguments, run the analysis, print the report |

---

# The phases

## Phase 1 — Read the sentiment lexicon

Implement `read_afinn_lexicon(filename)`.

Return a dictionary mapping a lowercase word to an **integer** score, not a
string. Convert with `int()`: you will be adding these values up later, and
`"-2" + "-2"` is not `-4`.

Rules:

- Strip surrounding whitespace from the word and from the score.
- Lowercase every word.
- Skip blank lines and whitespace-only lines.
- Skip any line that does not split into exactly two tab-separated fields.
- Skip any line whose score is not an integer (use `try` / `except ValueError`).
- Skip entries whose word is empty.
- Open with `encoding="utf-8", errors="ignore"`.

AFINN-111 contains a few multi-word phrases such as `cool stuff`. Store them as
they are; they simply never match a token.

```bash
./run_tests.sh 1
```

That runs test_read_afinn_lexicon.py.

**Do not continue until all 10 pass.**

## Phase 2 — Tokenize

Implement `tokenize(text)`.

A valid token:

- contains **only letters** — no digits, no punctuation
- has **at least 3 characters**
- is **not** a stop word

Return a **list**, not a set: repeated words must repeat, because term
frequency depends on it. Preserve the original order.

The simplest approach is to walk the lowercased text one character at a time,
keeping letters and replacing everything else with a space, then `.split()` the
result and filter. This automatically handles the tricky cases:

| Input | Output | Why |
|---|---|---|
| `"The Quick, brown fox jumps!"` | `["quick", "brown", "fox", "jumps"]` | punctuation separates; `the` is a stop word |
| `"apollo11 mission"` | `["apollo", "mission"]` | digits are not letters, so they split the word |
| `"rocket-fast"` | `["rocket", "fast"]` | the hyphen separates |
| `"NASA's rockets"` | `["nasa", "rockets"]` | the leftover `s` is too short |
| `"1969 1972 42"` | `[]` | nothing but digits |

`STOP_WORDS` is already defined at the top of the starter file. Use it as given.

```bash
./run_tests.sh 2
```

That runs test_tokenize.py.

**Do not continue until all 19 pass.**

> **A note you will need later.** The stop-word list contains several words that
> also carry AFINN scores — `good`, `great`, `best`, `better`, `like`, `want`,
> `help`, `problem`. Because tokenizing happens before sentiment scoring, those
> words can never contribute to a score. This is a real consequence of the
> design, and one of the test cases pins it down. Mention it in your write-up.

## Phase 3 — Parse and read articles

Implement `parse_articles_from_text(text, default_category)` first, then
`read_articles(input_path)`.

Both return a list of dictionaries with **exactly** these two keys:

```python
{"category": "sci.space", "tokens": ["rocket", "launch", ...]}
```

### `parse_articles_from_text(text, default_category)`

- A line starting with `"Newsgroup: "` ends the previous article and begins a
  new one. Strip the category name.
- The `"document_id: "` line that **immediately follows** a `Newsgroup:` line is
  a header and is discarded. A `document_id:` line anywhere else is ordinary
  body text and gets tokenized like any other line.
- Header lines never contribute tokens.
- Join the body lines with `"\n"` before tokenizing, so words are not glued
  together across line breaks.
- Text before the first header belongs to `default_category`.
- An article with an empty body is still an article — one with zero tokens.
- Text with no headers at all is one article.
- Empty text produces no articles.

### `read_articles(input_path)`

Use `os.path.isdir(input_path)` to choose between two cases.

**Directory:** each `.txt` file inside is one newsgroup file, and its default
category is the file name without `.txt`. Iterate over
`sorted(os.listdir(input_path))` — **not** plain `os.listdir()`. Filesystem
order differs between machines, and your report must be reproducible. Skip
hidden files (names starting with `.`), files that do not end in `.txt`, and
subdirectories.

**Single file:** parse that one file, with the default category taken from its
file name.

Open every file with `encoding="utf-8", errors="ignore"`.

```bash
./run_tests.sh 3
```

That runs test_parse_articles_from_text.py and test_read_articles.py.

**Do not continue until all 23 pass.**

## Phase 4 — Sentiment

Implement `sentiment_score(tokens, afinn)` and `sentiment_label(score)`.

`sentiment_score` returns the sum of the AFINN scores of the tokens. Tokens not
in the lexicon contribute nothing. Every occurrence counts, so
`["awful", "awful", "awful"]` with `awful = -3` scores `-9`. An empty token list
scores `0`. Do not modify either argument.

`sentiment_label` returns `"positive"` for a score above zero, `"negative"` for
a score below zero, and `"neutral"` for exactly zero.

```bash
./run_tests.sh 4
```

That runs test_sentiment_score.py and test_sentiment_label.py.

**Do not continue until all 19 pass.**

## Phase 5 — Count terms

Implement `document_frequencies(articles)` and
`category_term_frequencies(articles)`.

These two look similar and count differently. Getting them backwards is the most
common mistake in this assignment.

| | Counts | Loop over |
|---|---|---|
| `document_frequencies` | documents containing the term | `set(article["tokens"])` |
| `category_term_frequencies` | total occurrences of the term | `article["tokens"]` |

Given these two articles:

```python
[{"category": "sci.space", "tokens": ["rocket", "rocket", "rocket"]},
 {"category": "sci.space", "tokens": ["rocket", "launch"]}]
```

- `document_frequencies` returns `{"rocket": 2, "launch": 1}` — `rocket` appears
  in two documents, however many times it occurs in each.
- `category_term_frequencies` returns
  `{"sci.space": {"rocket": 4, "launch": 1}}` — every occurrence counts.

A category whose articles have no tokens still appears in the result, mapped to
an empty dictionary.

```bash
./run_tests.sh 5
```

That runs test_document_frequencies.py and test_category_term_frequencies.py.

**Do not continue until all 14 pass.**

## Phase 6 — TF–IDF

Implement `idf(number_of_documents, frequency)` and then `top_keywords(...)`.

### `idf(number_of_documents, frequency)`

$$IDF(t) = \log\left(\frac{N}{DF(t)}\right)$$

Use `math.log`, which is the **natural** logarithm, not `math.log10`.

Raise `ValueError` when `number_of_documents <= 0`, when `frequency <= 0`, or
when `frequency > number_of_documents`. Each of those is impossible for real
data, so a raised exception means a bug somewhere upstream — that is exactly
what you want.

A term that appears in every document has `DF = N` and therefore `IDF = 0`. It
scores zero no matter how often it occurs. That is the whole point of IDF.

### `top_keywords(category_counts, document_frequency, number_of_documents, limit=10)`

$$score(t, c) = TF(t, c) \times IDF(t)$$

Rules:

- Skip terms whose corpus document frequency is 1 or 0. Look the frequency up
  with `.get(term, 0)` so a missing term does not raise `KeyError`.
- Sort by score **descending**, then by term **alphabetically ascending** for
  ties.
- Return at most `limit` items, as a list of `(term, score)` tuples.
- `limit` defaults to `10`.

Both sort rules come from one sort:

```python
scored.sort(key=lambda item: (-item[1], item[0]))
```

The tie-breaking rule is not decoration. Without it, two terms with identical
scores could come out in either order, and your output would not be
reproducible. **Do not** pass `reverse=True` here — it would reverse the
alphabetical tie-break as well.

```bash
./run_tests.sh 6
```

That runs test_idf.py and test_top_keywords.py.

**Do not continue until all 22 pass.**

## Phase 7 — Assemble the analysis

Implement `analyze_articles(articles, afinn)`.

This function does no new counting. It calls the functions you already wrote and
packs the results into one dictionary with **exactly** this structure:

```python
{
    "document_count": 4,
    "categories": {
        "sci.space": {
            "article_count": 2,
            "positive_count": 1,
            "negative_count": 1,
            "neutral_count": 0,
            "sentiment_total": 2,
            "term_counts": {"rocket": 3, "launch": 3, ...},
        },
        ...
    },
    "document_frequency": {"rocket": 3, "launch": 2, ...},
}
```

- Every category found in `articles` appears in `"categories"`.
- `"term_counts"` comes straight from `category_term_frequencies()`.
- `"document_frequency"` comes straight from `document_frequencies()`.
- `"sentiment_total"` is the sum of the article scores in that category — the
  sum of the raw scores, not of the labels.
- The three label counters must add up to `"article_count"`.
- An empty article list gives `document_count` 0 and two empty dictionaries.

```bash
./run_tests.sh 7
```

That runs test_analyze_articles.py.

**Do not continue until all 13 pass.**

## Phase 8 — Format the report

Implement `format_report(results, keyword_limit=10)`. It returns the report as
**one string**; it does not print anything.

```text
20 Newsgroups Analysis
Documents analyzed: 4
Categories analyzed: 2

Category: rec.sport
Articles: 2
Sentiment: positive=1 negative=0 neutral=1 average=0.500
Top keywords:
  game  2.079
  team  1.386
  awful  0.693
  wonderful  0.693
  rocket  0.288
  subject  0.000

Category: sci.space
Articles: 2
Sentiment: positive=1 negative=1 neutral=0 average=1.000
Top keywords:
  launch  2.079
  rocket  0.863
  awful  0.693
  wonderful  0.693
  subject  0.000
```

Requirements, all of which are tested:

- Categories appear **alphabetically**, regardless of filesystem order.
- Average sentiment is `sentiment_total / article_count`, or `0.0` when the
  category has no articles.
- Averages and keyword scores print with **exactly three** decimal places —
  `"{:.3f}"`.
- Keyword lines begin with **two spaces**, and **two spaces** separate the term
  from its score.
- One blank line follows each category block.
- The string ends with exactly one `"\n"` — no trailing blank line. Build a list
  of lines whose last element is `""` and `"\n".join(...)` it.
- Show `keyword_limit` keywords per category, or fewer if fewer valid terms
  exist. `keyword_limit` defaults to `10`.
- Do not print article contents, file names, or debugging output.

The whitespace is checked character by character against
[`test/fixtures/expected_report.txt`](../test/fixtures/expected_report.txt). If
`test_matches_the_expected_report` fails, run `./run_tests.sh 8` and read the
diff carefully. It is almost always a missing blank line, a stray trailing
newline, or two spaces where you wrote one.

```bash
./run_tests.sh 8
```

That runs test_format_report.py.

**Do not continue until all 12 pass.**

## Phase 9 — Wire up `main()`

Implement `main()`. The argument check is already written for you in the starter
file; complete the rest.

- Exactly two arguments after the program name. Otherwise print a usage message
  to `sys.stderr` and return `1`.
- Read the lexicon, read the articles, analyze them, and print the report with
  `print(format_report(results), end="")`. The `end=""` matters: the report
  already ends with a newline.
- Return `0` on success.
- Catch `FileNotFoundError`, `PermissionError`, and `ValueError`. For each,
  print a message to `sys.stderr` and return `1`.
- The report goes to **stdout**; every error message goes to **stderr**. Nothing
  is printed to stdout when the program fails.

```bash
./run_tests.sh 9
```

That runs test_main.py and test_cli_end_to_end.py.

**Do not continue until all 24 pass.**

These are the last tests to go green. If an earlier phase is still
red, fix it first — every one of those is a bug `main()` inherits.

## Phase 10 — Whole suite, then the real corpus

Every test at once:

```bash
./run_tests.sh
```

All **156** must pass. Then merge into `testing` and confirm the `hw01` job is
green too — this is the first time you should expect to see no red at all.

Then run your program on the supplied corpus:

```bash
python3 news_analyzer.py data/20_newsgroups AFINN-111.txt
```

Sanity-check the result yourself before submitting:

- Are the categories in alphabetical order?
- Does `Documents analyzed` match the size of the corpus?
- Do the per-category article counts add up to it?
- Do the keywords look like they belong to their category? `sci.space` should
  not have `hockey` near the top.
- Run it twice and compare. The output must be byte-identical:

  ```bash
  python3 news_analyzer.py data/20_newsgroups AFINN-111.txt > run1.txt
  python3 news_analyzer.py data/20_newsgroups AFINN-111.txt > run2.txt
  diff run1.txt run2.txt && echo "deterministic"
  ```

---

# Reference

## The fixture corpus

The tests run against a four-article corpus in
[`test/fixtures/`](../test/fixtures/), small enough to check by hand. When a
test fails, this table tells you what the correct intermediate values are.

| Article | Category | Tokens after `tokenize()` | Score | Label |
|---:|---|---|---:|---|
| 3 | `rec.sport` | subject night team played wonderful game awful game rocket fast | +1 | positive |
| 4 | `rec.sport` | subject schedule team plays game tomorrow | 0 | neutral |
| 1 | `sci.space` | subject launch report rocket launch wonderful rocket engines performed brilliant | +8 | positive |
| 2 | `sci.space` | subject telemetry rocket telemetry awful launch terrible | −6 | negative |

The lexicon is `wonderful 4`, `brilliant 4`, `awful −3`, `terrible −3`,
`bad −2`, `abandon −2`.

Document frequencies over all `N = 4` articles: `subject` 4, `rocket` 3,
`game` 2, `team` 2, `launch` 2, `wonderful` 2, `awful` 2, and 1 for everything
else.

The `rec.sport` keyword scores in full:

| Term | TF | DF | Score |
|---|---:|---:|---|
| `game` | 3 | 2 | 3 × log(4/2) = 2.079 |
| `team` | 2 | 2 | 2 × log(4/2) = 1.386 |
| `awful` | 1 | 2 | log(4/2) = 0.693 |
| `wonderful` | 1 | 2 | log(4/2) = 0.693 |
| `rocket` | 1 | 3 | log(4/3) = 0.288 |
| `subject` | 2 | 4 | 2 × log(4/4) = 0.000 |

`awful` and `wonderful` tie at 0.693, so the alphabetical rule puts `awful`
first. `night`, `played`, `fast`, `schedule`, `plays` and `tomorrow` all have
`DF = 1` and are skipped.

## Debugging tips

**Narrow it down**

- **One phase at a time.** `./run_tests.sh 2` shows you only Phase 2.
- **One file.** `./run_tests.sh 2 -q` for a short summary, or
  `python3 -m pytest test_tokenize.py -v` if you prefer calling pytest directly.
- **One test.**
  `python3 -m pytest test_tokenize.py::test_digits_are_stripped_and_split_the_word -v`
- **Stop at the first failure.** `./run_tests.sh 3 -x`
- **See your own output.** `./run_tests.sh 3 -s` lets `print()` through.

**Read what the failure tells you**

- **Read the assertion, not just the test name.** pytest prints the values it
  compared. `assert ['rocket'] == ['rocket', 'launch']` says a token went
  missing; the name alone does not.
- **Test names describe the rule.** `test_counts_documents_not_occurrences` says
  exactly what went wrong: something counted occurrences.
- **Read the test.** Every test file is plain Python. If you cannot tell what a
  test wants, open it — the assertion says precisely what the expected value is.
- **Fix the earliest red phase first.** A broken `tokenize()` fails tests in six
  other files. Everything downstream of a bug is noise until the bug is gone.

**Try things by hand**

```bash
cd Assignments/HW01/submission
python3 -c "import news_analyzer as n; print(n.tokenize('The Quick, brown fox!'))"
```

Or interactively, which is better for exploring:

```bash
python3
>>> import news_analyzer as n
>>> n.tokenize("apollo11 mission")
```

The [Reference](#the-fixture-corpus) section gives the exact corpus, tokens,
scores and keyword values the tests use, so you can reproduce any failing
expectation by hand and see where your output diverges.

## Restrictions

- Use only the Python standard library, plus the `stop_words` package that the
  starter file already imports.
- Do **not** use `sklearn`, `nltk`, `pandas`, `numpy`, a prebuilt sentiment
  package, or a prebuilt TF–IDF implementation. `test_cli_end_to_end.py` checks
  your source for these imports.
- You may use `os`, `sys`, `math`, and optionally `re`.
- Write your own tokenization and TF–IDF logic.
- Do not modify required function names, parameter lists, return types, or the
  command-line interface.
- Do not modify anything in `test/`. Your submission is graded with the original
  test suite plus additional hidden tests, so a weakened test hides a failure
  rather than fixing one.
- Submit work you understand and can explain.
- Disclose AI tool use and any other help in `JOURNAL.md`. Disclosed use
  costs you nothing; undisclosed use is an integrity violation.

## What to submit

All four files go in `Assignments/HW01/submission/`, committed on `work` and
merged into `testing`:

```text
Assignments/HW01/submission/
├── news_analyzer.py
├── report.txt
├── NOTES.md
└── JOURNAL.md
```

1. `news_analyzer.py` — your program.
2. `report.txt` — the output of
   `python3 news_analyzer.py <corpus> AFINN-111.txt`, saved with
   `> report.txt`.
3. `NOTES.md` — half a page is plenty:
   - anything that surprised you in the results
   - the stop-word / AFINN overlap from Phase 2 and what you would do about it
   - one keyword per category that you think is a poor topic indicator, and why
4. `JOURNAL.md` — see below.

Confirm the merge into `testing` completed and its pipeline passed. An
unmerged branch is not a submission.

### `JOURNAL.md`

Write a truthful account of how you actually developed this program. Cover:

- **How you worked.** Which phase you started with, what you wrote in what
  order, what you tried and threw away.
- **AI tools.** Did you use any — ChatGPT, Claude, Copilot, Gemini, or anything
  else? Say which, and say how: whole functions, autocompleted lines, explaining
  an error message, generating test cases, rubber-ducking a design. If you used
  none, say that.
- **Other help.** Classmates, tutors, office hours, Stack Overflow, blog posts,
  documentation. Name what you used.
- **Where you got stuck**, and how you got unstuck. This is the most useful part
  — be specific. "Phase 5: I was counting occurrences in `document_frequencies`
  instead of documents, and `test_counts_documents_not_occurrences` caught it"
  is worth more than "it was hard."

**The journal is not graded on content.** Using AI tools does not cost you
points. Getting stuck does not cost you points. Needing help does not cost you
points. The 5 points are for writing a journal that is *meaningful* — specific
enough that someone reading it can see how the work actually went. A journal
that says "I wrote the code and it worked" earns nothing, whether or not it is
true.

Honesty here is the point of the exercise. You are being asked to observe your
own process, which is a skill worth having, and disclosure of AI use is a
professional norm you will meet again outside this course.

## Grading

| Area | Points | What is assessed |
|---|---:|---|
| File and corpus reading | 15 | Lexicon, article parsing, directory and single-file input |
| Tokenization and filtering | 15 | Normalization and the required exclusion rules |
| Sentiment analysis | 15 | Correct AFINN scoring, labels, and category summaries |
| TF–IDF calculations | 25 | Document frequencies, IDF, category scores, ranking, tie-breaks |
| Program design | 15 | Small functions, appropriate data structures, readable code |
| Output and robustness | 10 | Required format, deterministic ordering, error behavior |
| Journal | 5 | A meaningful `JOURNAL.md`; content does not affect the grade |
| **Total** | **100** | |

A program that passes all 156 supplied tests is not automatically full marks —
program design is graded by reading your code — but a program that fails them
cannot earn full marks in the first four rows.

---

# Instructor notes

*Remove this section before distributing the handout.*

## Files

- `starter/news_analyzer.py` — the student-facing skeleton, with the same
  docstrings and `TODO` markers described above.
- `solution/news_analyzer.py` — the reference implementation. Do not distribute.
- `test/` — 156 tests, one file per function plus an end-to-end file, shipped
  to students. `run_tests.sh N` selects the files for phase N; that mapping
  lives in the script, and the per-phase counts quoted in the handout come from
  this suite. Update both if you add tests.
- `grading/` — 21 further tests, never distributed. See `grading/README.md`.

## How students are tested

There are two suites:

| | Ships to students | Run by CI | Purpose |
|---|---|---|---|
| `test/` (156) | yes | yes, from **this** repository | The phase-by-phase suite students work against locally |
| `grading/` (21) | never | yes | Edge cases that decide marginal submissions |

Each student project is configured with *Settings → CI/CD → General pipelines →
CI/CD configuration file* set to
`ci/homework-tests.yml@ifi8410fall2026/course-template`. GitLab then ignores any
`.gitlab-ci.yml` in the student repository and uses this project's pipeline, so
students cannot add jobs. That is what makes the rest safe: the pipeline can
hold credentials and run tests students may not read.

The job downloads this repository through the GitLab archive API, deletes every
`Assignments/*/solution/` from its copy, and runs `test grading` from the
downloaded tree against the student's `submission/` folder with
`$SUBMISSION_DIR` pointing at it. The student's own copy of `test/` is never
used, so weakening it changes nothing — verified: a submission whose local suite
was edited to add a passing test and remove an assertion still ran the
untouched 177.

Deleting `solution/` is the other safeguard. Without it, a submission missing
`news_analyzer.py` would fall through `conftest.py`'s lookup chain to the
reference implementation and report a pass for work that was never read.

### Setup checklist

1. Course template → *Settings → CI/CD → Job token permissions*: allow the
   student projects. (Or set a group variable `COURSE_TEMPLATE_TOKEN` holding a
   read-only token for this project; the pipeline prefers it when present.)
2. Each student project → *Settings → CI/CD → General pipelines → CI/CD
   configuration file* → `ci/homework-tests.yml@ifi8410fall2026/course-template`.
3. Student projects need **no** `.gitlab-ci.yml` and **no** read access to this
   repository.

Because the suite is fetched at run time, editing a test here changes grading
for every student on their next merge, with no student-repo update. It also
means a broken commit on `main` breaks every pipeline at once — pin
`COURSE_TEMPLATE_REF` to a tag during the term if you want to decouple them.

## Keeping the two suites honest

Both must pass against the reference before you commit:

```bash
cd Assignments/HW01
python3 -m pytest test grading -q     # 177
```

A hidden test that the reference fails will fail every student. See
`grading/README.md`.

## Module resolution

`test/conftest.py` locates the module under test from `$NEWS_ANALYZER` first, so
`./run_tests.sh <path>` grades any file. Its fallback order is `$NEWS_ANALYZER`, `$SUBMISSION_DIR/news_analyzer.py`,
`../submission/news_analyzer.py`, `../solution/news_analyzer.py`,
`../news_analyzer.py`, `./news_analyzer.py`. In this repository, where no
`submission/` exists, a bare `pytest` therefore tests the reference solution.

## Hidden-test strategy

The supplied suite is deliberately visible so students can work phase by phase.
For hidden tests, extend rather than duplicate it:

- Lexicon files with CRLF line endings, a BOM, or duplicate entries.
- Files whose first article lacks headers *and* whose category name collides
  with a later `Newsgroup:` line.
- A category whose every article tokenizes to nothing.
- A corpus of exactly one document, where every term has `DF = N` and every
  score is 0.000.
- A category with fewer than `keyword_limit` valid terms.
- Filesystem enumeration order — the supplied
  `test_sorted_order_does_not_depend_on_the_filesystem` monkeypatches
  `os.listdir`; a hidden test can do the same with a different permutation.

The supplied suite was validated by mutation testing: nineteen deliberate bugs
were injected into the reference implementation — reversed tie-breaks,
occurrence-counting document frequencies, `>= 0` sentiment labels, unsorted
categories, two-decimal formatting, an ignored `limit`, a dropped `sorted()` —
and every one is caught. Apply the same check to any tests you add.

## The stop-word overlap

`STOP_WORDS` comes from the `stop_words` package, whose English list contains
`good`, `great`, `best`, `better`, `like`, `want`, `help` and `problem` — all
AFINN entries. Because `tokenize()` runs before scoring, those words can never
affect a sentiment score, which measurably flattens sentiment on the real
corpus.

This is left in deliberately and is the subject of a `NOTES.md` question. If you
would rather remove it, the fix is to score sentiment over a token stream that
is filtered for length and letters but *not* for stop words — which means
`sentiment_score` needs its own tokenization, and the fixture expectations in
`test/` change accordingly.

`test_tokenize.py::test_common_sentiment_words_are_stop_words` pins the current
behavior, and the fixture corpus uses `wonderful`, `brilliant`, `awful` and
`terrible`, none of which are stop words.

## The journal

`JOURNAL.md` is worth 5 points and is scored only on whether it is meaningful —
specific enough to show how the work went. Content is explicitly not graded, and
students are told so plainly, because the point is to make honest disclosure the
cheap option. A student who used an AI tool for most of the program and says so
clearly gets all 5; a student who writes three vague sentences gets none.

Read the journals before the code. They tell you which phases the class got
stuck on, and that is the most useful signal this assignment produces for
planning the next lecture.

## Post-assignment discussion

`sklearn.feature_extraction.text.TfidfVectorizer` is a good comparison point
once the assignment is submitted: it computes the same idea with smoothing and
L2 normalization, and running it beside a student's output makes the effect of
those two choices concrete. See also the "Normalized TF" and "Smoothed IDF"
sections of [`tfidf_tutorial.md`](tfidf_tutorial.md).
