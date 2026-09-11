# Session 4: Functions and Decomposition

The point at which a program stops being a sequence of commands and becomes a
system of named behaviors. A function puts a boundary around a piece of work and
states a contract: what goes in, what comes out, what must be true, and what it
touches on the way. That boundary is what makes analysis code reusable,
testable, auditable, and safe to run at scale.

Three notebooks cover the same material at three altitudes — practice,
mechanics, and design reasoning. Work them in the order below.

## Notebooks

### 1. `Examples_of_Python_Functions_orig.ipynb`

Twenty-five worked examples, ordered from easy to medium, and the place to
start. Each one gives the problem and the idea behind it, a runnable solution
with demonstrated output, and a *Try it* cell to change. The examples build on
each other rather than restarting: Part A covers parameters, `return`, defaults
and validation; Part B works over lists, dictionaries and the coffee-cart table
from Session 3; Part C handles edge cases, errors and mutation; Part D treats
functions as values, ending with closures, `functools.partial`, a dispatch
table, and a memoizing wrapper that shows what a decorator actually is.

### 2. `Anatomy_of_Python_Functions_orig.ipynb`

The reference notebook: every part of a function, what it is called, and what
Python does with it. Ten sections cover the `def` statement part by part, scope
and the LEGB rule, parameters versus arguments, named arguments and defaults,
flexible signatures (`*args`, `**kwargs`, `/` and `*`), return values, type
annotations, `lambda`, functions as objects, and closures and currying. Many
cells are written to fail or to surprise — an `UnboundLocalError` from a single
assignment, a `True` silently swallowed by `*args`, a closure loop printing
`[40, 40, 40]` — because the mechanics stick when the surprising case is
executed rather than described.

### 3. `Deep_Dive_Python_Functions_orig.ipynb`

The argument behind the mechanics: *why* functions are designed this way. It
treats a function as a contract of name, parameters, return value and
preconditions, then works through the consequences — returning versus printing,
scope and hidden global state, decomposition as a design step, type and
edge-case policy, announced versus unannounced side effects, why shared mutable
state breaks under parallel execution, and how docstrings and tests turn a
contract into evidence. Read it once the syntax is comfortable; it is about
judgment, not syntax.

## Objectives

- Write a function with an explicit contract: name, parameters, return value,
  and documented edge cases.
- Explain why a function should return a value rather than print one.
- Trace name resolution through local, enclosing, global, and built-in scope.
- Use positional, named, default, variadic, and keyword-only parameters.
- Annotate parameters and return values, and say what annotations do *not* do.
- Choose deliberately between raising an exception and returning a missing
  value, and between returning new data and mutating in place.
- Decompose a task into named, independently testable stages.
- Pass functions as arguments and return them as values.

## Topics

- The `def` statement: parameters, body, docstring, `return`.
- `return` versus `print`; implicit `None`.
- Scope and the LEGB rule; `global` and `nonlocal`; why globals hide inputs.
- Arguments passed by assignment: rebinding versus mutating.
- Named arguments, defaults, and the mutable-default trap.
- `*args`, `**kwargs`, positional-only `/`, keyword-only `*`, call unpacking.
- Returning tuples and dictionaries; keeping return types consistent.
- Type annotations, `float | None`, `Callable`; validation at boundaries.
- `TypeError` versus `ValueError`; collecting problems instead of raising.
- Side effects, mutation, and the shallow-versus-deep copy of a table.
- `lambda` and the `key=` parameter.
- Functions as objects: dispatch tables, higher-order functions, closures,
  currying, `functools.partial`, decorators.
- Docstrings and tests as executable evidence of a contract.

## Call to Action

1. Work through `Examples_of_Python_Functions_orig.ipynb` (rename it first to
   drop the `_orig`). Run every cell in order and attempt each *Try it* cell
   before moving on.
2. Keep `Anatomy_of_Python_Functions_orig.ipynb` open as a reference while you
   work, and read it end to end when a mechanism is unclear.
3. Read `Deep_Dive_Python_Functions_orig.ipynb` once the syntax is comfortable.
4. Then start **[HW03](https://ifi8410.molnar.ai/assignments/assignment-03/)**

All three notebooks use the campus coffee-cart table from Session 3 — a list of
dictionaries, one dictionary per row — so no new dataset is introduced and no
library beyond the standard library is required.
