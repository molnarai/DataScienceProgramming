---
draft: false
title: Tabular Data
weight: 60
description: How business data lives in related tables, and how to query, summarize, and join it with confidence in SQL and pandas.
date: 2026-09-28
lastmod: 2026-09-28
---
This post explains why business applications keep their data in related tables, and how to work with them in SQL and pandas. It starts with how to describe a table by its grain, keys, and column types, and how to deal with missing values. Then it walks through selecting, filtering, sorting, aggregating, and window calculations, and how to choose a join and check that it did what you meant. It closes with SQL's declarative approach: you describe the result you want, not the steps to get it.
<!-- more -->

> **Conventions:** SQL examples use PostgreSQL syntax. pandas examples use nullable dtypes. The small `orders` and `customers` example below is runnable; the later Northwind example is conceptual and assumes a Northwind edition with the indicated tables and names. Northwind variants may name or quote tables differently.

## 1. What is a data table?

A **data table** organizes observations into rows and attributes into columns. The **grain** of a table specifies what one row represents. In an orders table, each row can represent one order, while `order_id`, `customer_id`, `amount`, and `order_date` describe it.

Columns can have different types: `order_id` may be an integer, `amount` a decimal number, and `order_date` a date. Values within a column should conform to its declared or intended type. SQL declares column types; pandas assigns a dtype to each column, though an `object` column can contain mixed Python objects. An identifier stored as an integer is still an identifier, not a meaningful quantity to add.

A **primary key** identifies rows uniquely; a **foreign key** refers to a key in another table. The sample below deliberately has an order whose customer record is absent, so its `customer_id` column does not have an enforced foreign-key constraint.

### Running example

**orders**

| order_id | customer_id | amount | order_date |
|---:|---:|---:|---|
| 1 | 10 | 100.00 | 2026-01-05 |
| 2 | 10 | 50.00 | 2026-01-08 |
| 3 | 20 | NULL | 2026-01-09 |
| 4 | 99 | 30.00 | 2026-01-10 |

**customers**

| customer_id | name |
|---:|---|
| 10 | Ada |
| 20 | Ben |
| 30 | Cy |

Customer 99 has an order but no customer record. Cy has no order. Order 3 has an unknown amount, **not** a zero amount.

### Reproducible setup

**SQL (PostgreSQL)**

```sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount NUMERIC(10, 2),
    order_date DATE
);
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT
);
INSERT INTO orders (order_id, customer_id, amount, order_date) VALUES
    (1, 10, 100.00, DATE '2026-01-05'),
    (2, 10,  50.00, DATE '2026-01-08'),
    (3, 20,   NULL, DATE '2026-01-09'),
    (4, 99,  30.00, DATE '2026-01-10');
INSERT INTO customers (customer_id, name) VALUES
    (10, 'Ada'), (20, 'Ben'), (30, 'Cy');
```

**Python pandas**

```python
import pandas as pd

orders = pd.DataFrame({
    "order_id": pd.Series([1, 2, 3, 4], dtype="Int64"),
    "customer_id": pd.Series([10, 10, 20, 99], dtype="Int64"),
    "amount": pd.Series([100, 50, pd.NA, 30], dtype="Float64"),
    "order_date": pd.to_datetime([
        "2026-01-05", "2026-01-08", "2026-01-09", "2026-01-10"
    ]),
})
customers = pd.DataFrame({
    "customer_id": pd.Series([10, 20, 30], dtype="Int64"),
    "name": pd.Series(["Ada", "Ben", "Cy"], dtype="string"),
})
```

SQL `NUMERIC(10,2)` uses decimal arithmetic, whereas pandas `Float64` here uses floating-point arithmetic. They are suitable for teaching the same table operations, but do not have identical numeric precision.

## 2. Why businesses use multiple tables: Northwind

Business applications manage different entities and events at different **grains**. Microsoft's Northwind sample database illustrates this with customers, orders, order details, products, suppliers, categories, and other tables. Names and schemas differ among Northwind editions and ports.

| Table | What one row means | Relationship |
|---|---|---|
| `Customers` | One customer | A customer can place many orders |
| `Orders` | One order | An order belongs to a customer and has many lines |
| `Order Details` | One product line on one order | Relates an order to a product |
| `Products` | One catalog product | A product can occur on many order lines |
| `Suppliers` | One supplier | A supplier can supply many products |

```text
Customers  1 ──< many Orders  1 ──< many Order Details
                                            many >── 1 Products  many >── 1 Suppliers
```

`Order Details` resolves the many-to-many relationship between orders and products: an order can contain multiple products, and a product can occur in multiple orders. If an order contains three products, it has three detail rows rather than columns called `Product1`, `Product2`, and `Product3`.

### Why not one giant table?

A single table of sale lines with customer addresses, order dates, product descriptions, suppliers, quantity, and price would repeat customer and order information for every line. A popular product's catalog information would repeat across many transactions. Separating these facts:

- Reduces unnecessary repetition and inconsistent copies.
- Makes customer and product updates easier: change their records rather than every transaction row.
- Supports any number of order lines without adding columns.
- Allows keys and relationship constraints to express business rules.
- Preserves distinctions between a **current catalog price** in `Products` and the **price actually charged** on an order line in `Order Details`. Retaining both is intentional because they are different facts.

This design is associated with **normalization**: store each fact with the entity or event it describes. It does not prohibit intentional historical snapshots. For example, a shipping address captured at purchase time may need to remain unchanged even if a customer later changes their current address.

### Build a view by joining

Use joins to construct the order-line view an application or report needs. The following uses common Northwind names; adapt quoting and names to the specific edition.

```sql
SELECT
    o.OrderID,
    c.CompanyName,
    o.OrderDate,
    p.ProductName,
    od.Quantity,
    od.UnitPrice,
    od.Discount,
    od.Quantity * od.UnitPrice * (1 - od.Discount) AS LineTotal
FROM Orders AS o
JOIN Customers AS c ON c.CustomerID = o.CustomerID
JOIN "Order Details" AS od ON od.OrderID = o.OrderID
JOIN Products AS p ON p.ProductID = od.ProductID
WHERE o.OrderID = 10248;
```

One result row represents **one order line**, not one order. Joining an order-level value onto its detail lines repeats that value; blindly summing it afterward can inflate totals.

Assuming the same columns are present in four pandas DataFrames:

```python
report = (
    orders
    .merge(customers, on="CustomerID", validate="many_to_one")
    .merge(order_details, on="OrderID", validate="one_to_many")
    .merge(products, on="ProductID", validate="many_to_one")
)
```

Here each `validate` check applies to the DataFrames at **that step**. Use actual relationship cardinalities for the edition and data at hand; for example, duplicated product IDs would invalidate the last check. The pandas and SQL snippets are for illustrating the shape of a report, not for modifying the small runnable example above.

## 3. Null and missing values

**Null** represents absent or unknown data. SQL uses `NULL`; pandas uses dtype-dependent markers such as `pd.NA`, `NaN`, and `NaT`. Missing is not zero, an empty string, or the text `"NULL"`.

| Operation | SQL | Python pandas |
|---|---|---|
| Find missing amounts | `SELECT * FROM orders WHERE amount IS NULL;` | `orders.loc[orders["amount"].isna()]` |
| Find known amounts | `SELECT * FROM orders WHERE amount IS NOT NULL;` | `orders.loc[orders["amount"].notna()]` |
| Supply zero for display/calculation | `SELECT order_id, COALESCE(amount, 0) AS amount_or_zero FROM orders;` | `orders.assign(amount_or_zero=orders["amount"].fillna(0))[["order_id", "amount_or_zero"]]` |
| Sum known amounts | `SELECT SUM(amount) AS total FROM orders;` | `orders["amount"].sum()` |

The sum of known amounts is **180**; that does not establish that order 3's value was zero. SQL `SUM` ignores null inputs and returns `NULL` if there are no non-null inputs. pandas `sum()` skips missing values by default and can return zero for an all-missing group. To preserve the SQL-style missing total, use `sum(min_count=1)`:

```python
orders.groupby("customer_id")["amount"].sum(min_count=1)
```

This returns missing for customer 20. Test nulls with SQL `IS NULL` / `IS NOT NULL`, not `= NULL`; use pandas `.isna()` / `.notna()`.

## 4. Selecting, filtering, and sorting

**Projection** chooses columns; **filtering** chooses rows; **sorting** imposes an order on the result.

| Operation | SQL | Python pandas |
|---|---|---|
| Select columns | `SELECT order_id, amount FROM orders;` | `orders[["order_id", "amount"]]` |
| Find one order | `SELECT * FROM orders WHERE order_id = 2;` | `orders.loc[orders["order_id"].eq(2)]` |
| Combine conditions | `SELECT * FROM orders WHERE customer_id = 10 AND amount >= 50;` | `orders.loc[orders["customer_id"].eq(10) & orders["amount"].ge(50)]` |
| Sort by amount descending, nulls last | `SELECT * FROM orders ORDER BY amount DESC NULLS LAST;` | `orders.sort_values("amount", ascending=False, na_position="last")` |
| Select rows and columns together | `SELECT order_id, amount FROM orders WHERE amount > 50;` | `orders.loc[orders["amount"].gt(50), ["order_id", "amount"]]` |

Use parentheses around each pandas comparison when composing Boolean masks with `&` or `|`. Explicitly sort final results when order matters; a SQL result without `ORDER BY` has no guaranteed presentation order. SQL `WHERE amount > 50` excludes a null amount because the test is not true; a missing entry in the corresponding nullable pandas Boolean mask is not selected by `.loc`.

## 5. Grouping and aggregation

**Grouping** partitions rows by a key. **Aggregation** reduces each group to a result, such as count or total. The two orders for customer 10 yield one group with total amount 150.

| Operation | SQL | Python pandas |
|---|---|---|
| Count orders | `SELECT customer_id, COUNT(*) AS n FROM orders GROUP BY customer_id;` | `orders.groupby("customer_id", as_index=False).agg(n=("order_id", "size"))` |
| Count known amounts | `SELECT customer_id, COUNT(amount) AS n FROM orders GROUP BY customer_id;` | `orders.groupby("customer_id", as_index=False).agg(n=("amount", "count"))` |
| Total, preserving all-missing groups | `SELECT customer_id, SUM(amount) AS total FROM orders GROUP BY customer_id;` | `orders.groupby("customer_id", as_index=False).agg(total=("amount", lambda s: s.sum(min_count=1)))` |
| Keep groups with two or more orders | `SELECT customer_id, COUNT(*) AS n FROM orders GROUP BY customer_id HAVING COUNT(*) >= 2;` | `counts = orders.groupby("customer_id").size().reset_index(name="n"); counts.loc[counts["n"].ge(2)]` |

`COUNT(*)` counts rows; `COUNT(amount)` counts non-null amounts. In pandas the corresponding distinction is `size` versus `count`. SQL `WHERE` filters rows **before** grouping; `HAVING` filters groups **after** aggregation. Similarly, decide whether pandas filtering belongs before or after `.groupby()`.

## 6. Window calculations

An aggregate generally returns fewer rows. A **window calculation** computes across related rows while **retaining each original row**. SQL uses `OVER (...)`; pandas often uses `groupby(...).transform(...)`, `cumcount()`, cumulative functions, or rolling functions.

### Average amount beside each order

**SQL**

```sql
SELECT order_id, customer_id, amount,
       AVG(amount) OVER (PARTITION BY customer_id) AS customer_avg
FROM orders;
```

**Python pandas**

```python
orders_with_avg = orders.assign(
    customer_avg=orders.groupby("customer_id")["amount"].transform("mean")
)
```

Both customer-10 orders remain visible, each with customer average 75. Customer 20's average is missing.

### Number orders within each customer

**SQL**

```sql
SELECT order_id, customer_id,
       ROW_NUMBER() OVER (
           PARTITION BY customer_id ORDER BY order_date, order_id
       ) AS order_number
FROM orders;
```

**Python pandas**

```python
ordered = orders.sort_values(
    ["customer_id", "order_date", "order_id"]
).copy()
ordered["order_number"] = ordered.groupby("customer_id").cumcount() + 1
```

`order_id` breaks date ties. The SQL window's `ORDER BY` controls **numbering**, not necessarily final display order; add an outer `ORDER BY` to display rows in that sequence.

## 7. Joining tables

A **join** combines rows according to a key relationship. Here `orders.customer_id` matches `customers.customer_id`. The join type determines which unmatched rows are retained.

| Join type | SQL | Python pandas | Result here |
|---|---|---|---|
| Inner | `SELECT * FROM orders o INNER JOIN customers c ON o.customer_id = c.customer_id;` | `orders.merge(customers, on="customer_id", how="inner")` | Orders 1, 2, 3; excludes order 4 and Cy |
| Left | `SELECT * FROM orders o LEFT JOIN customers c ON o.customer_id = c.customer_id;` | `orders.merge(customers, on="customer_id", how="left")` | All orders; order 4 has a missing name |
| Right | `SELECT * FROM orders o RIGHT JOIN customers c ON o.customer_id = c.customer_id;` | `orders.merge(customers, on="customer_id", how="right")` | All customers; Cy has no order |
| Full outer | `SELECT * FROM orders o FULL OUTER JOIN customers c ON o.customer_id = c.customer_id;` | `orders.merge(customers, on="customer_id", how="outer")` | Includes both order 4 and Cy |
| Cross | `SELECT o.order_id, c.name FROM orders o CROSS JOIN customers c;` | `orders.merge(customers, how="cross")[["order_id", "name"]]` | 4 × 3 = 12 pairs |

`SELECT *` abbreviates the SQL examples, but for dependable outputs select and alias your desired columns. In a full SQL join, `COALESCE(o.customer_id, c.customer_id) AS customer_id` combines the left and right identifiers into one reported key. A **self-join** uses a table twice, with separate aliases: for example, employees joined to the employees who manage them.

### Same-named columns that are not keys

Imagine that both tables have a `status` column: order shipment status and customer account status. These fields mean different things and must **not** be added to the join key. The following SQL qualifies both columns and gives them distinct output names:

```sql
SELECT o.order_id,
       o.status AS order_status,
       c.status AS customer_status
FROM orders AS o
JOIN customers AS c ON o.customer_id = c.customer_id;
```

The corresponding pandas merge specifies the key and descriptive suffixes:

```python
result = orders.merge(
    customers, on="customer_id", how="inner",
    suffixes=("_order", "_customer")
)
```

These examples **assume `status` has been added** to both example tables; it is not present in the reproducible setup. SQL `SELECT status` would be ambiguous, and SQL `SELECT *` can expose two columns with that name. pandas would otherwise default to `status_x` and `status_y`. To discard a redundant column before merging, select only needed right-side columns, such as `customers[["customer_id", "name"]]`.

**Always specify the join key:** pandas `merge` without `on=` infers the key using *all shared column names*. SQL `NATURAL JOIN` also matches on all shared names. If both tables contain `customer_id` and `status`, either shortcut could accidentally require both fields to match.

## 8. Common join pitfalls

| Pitfall | Consequence | Prevention |
|---|---|---|
| Wrong join type | Inner join drops unmatched orders or customers | Decide which side's rows must survive |
| Duplicated keys | Matching rows multiply; later sums can be inflated | Check uniqueness and expected cardinality; pandas `validate=` |
| Incomplete key | Unrelated records match, e.g., same `product_id` in different stores | Join on every component: `store_id` **and** `product_id` |
| Inferred join keys | Non-key columns accidentally participate | Explicit SQL `ON` or pandas `on=` |
| Missing keys | SQL equality does not match two nulls; pandas `merge` matches missing keys on both sides | Inspect or exclude missing keys deliberately |
| Overlapping column names | Ambiguous output or confusing `_x`/`_y` columns | SQL aliases; pandas suffixes or pre-rename |
| Filter on right table after left join | Unmatched left rows disappear | Put right-side eligibility test in SQL `ON`, or filter right DataFrame before merge |
| Assumed row ordering | Reports appear in surprising order | Sort final output explicitly |
| Unexpected many-to-many/cross join | Very large intermediate result | Inspect key frequencies and result row counts |

### An outer-join filtering trap

Assume `customers` has a `status` column. This version preserves **every order** while attaching only active customers:

```sql
SELECT o.order_id, c.name
FROM orders AS o
LEFT JOIN customers AS c
  ON o.customer_id = c.customer_id AND c.status = 'active';
```

This version **removes** orders without an active matching customer:

```sql
SELECT o.order_id, c.name
FROM orders AS o
LEFT JOIN customers AS c ON o.customer_id = c.customer_id
WHERE c.status = 'active';
```

To preserve every order in pandas, filter the right-hand table **before** merging:

```python
joined = orders.merge(
    customers.loc[customers["status"].eq("active")],
    on="customer_id", how="left",
    validate="many_to_one", indicator=True,
)
```

Again, `status` is an illustrative added column. `validate="many_to_one"` rejects duplicate right-side customer keys. `indicator=True` adds `_merge` so you can identify matching (`both`) and unmatched (`left_only`) orders.

For a left join on a right-side unique key, verify that the row count stays equal to the left input and that left primary keys have not repeated:

```python
joined = orders.merge(
    customers, on="customer_id", how="left",
    validate="many_to_one", indicator=True,
)
assert len(joined) == len(orders)
assert joined["order_id"].is_unique
print(joined["_merge"].value_counts())
```

Here there should be four result rows: three matched orders and one unmatched order. In SQL, compare counts and find unmatched orders with `WHERE c.customer_id IS NULL` after a left join. Check for duplicate customer keys with `GROUP BY customer_id HAVING COUNT(*) > 1`; enforce uniqueness with a database constraint where appropriate.

## 9. Why SQL looks the way it does

SQL is primarily **declarative**: specify the desired result, not a loop describing exactly how to retrieve each row. The database chooses an execution plan. SQL is also **set-oriented** in programming style: operations describe collections of rows at once. Ordinary SQL can nevertheless contain duplicate result rows, so it is not literally restricted to mathematical sets.

- **1970:** E. F. Codd published *A Relational Model of Data for Large Shared Data Banks*. A major goal was **data independence**: applications should ask logical questions without depending on physical storage paths.
- **1970s:** At IBM, Donald Chamberlin and Raymond Boyce developed SEQUEL, later SQL. IBM's System R project demonstrated practical relational querying and optimization.
- **1980s:** SQL became standardized, establishing shared query concepts across database products, even though dialect differences remain.

SQL was inspired by the relational model but is not identical to its mathematical ideal: duplicate rows, nulls, ordering, and practical extensions require precise SQL-specific rules.

### Relating SQL to pandas

A SQL query states a desired result for the database engine to plan. A pandas program composes DataFrame operations explicitly in Python. Both can ask the same business question, but pandas method chains are not generally optimized or reordered by a SQL database optimizer.

**Question:** Show total known spending by customer, largest first. This produces one output row per customer **with a matched order**.

**SQL**

```sql
SELECT c.name, SUM(o.amount) AS total_spent
FROM orders AS o
JOIN customers AS c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spent DESC;
```

**Python pandas**

```python
result = (
    orders
    .merge(customers, on="customer_id", how="inner")
    .groupby(["customer_id", "name"], as_index=False)
    .agg(total_spent=("amount", lambda s: s.sum(min_count=1)))
    .sort_values("total_spent", ascending=False, na_position="last")
    [["name", "total_spent"]]
)
```

The shared conceptual pipeline is **join → group → aggregate → sort → choose columns**. Ada has 150; Ben has a missing total. Cy is absent because she has no order; order 4 is absent because customer 99 has no matching customer. `min_count=1` gives pandas the same all-missing aggregate behavior as SQL `SUM` in this example.

| Concept | SQL | pandas |
|---|---|---|
| Choose columns | `SELECT` | `df[[...]]` |
| Filter rows | `WHERE` | `df.loc[mask]` |
| Sort | `ORDER BY` | `sort_values()` |
| Join | `JOIN ... ON` | `merge(..., on=...)` |
| Group and aggregate | `GROUP BY`, `SUM`, `COUNT`, etc. | `groupby(...).agg(...)` |
| Filter groups | `HAVING` | Filter aggregated result |
| Retain rows while calculating by group | `OVER (PARTITION BY ...)` | `groupby(...).transform(...)` or related methods |

**General workflow:** State the business question; specify the grain of each input and output; identify keys; predict nulls, unmatched records, and row multiplication; then write the SQL or pandas code and validate the result.

## References

- [Microsoft: Northwind database diagram](https://support.microsoft.com/en-us/access/northwind-database-diagram)
- [Microsoft: Northwind 2.0 Developer Edition—Orders](https://support.microsoft.com/en-us/office/northwind-2-0-developer-edition-orders-40c61470-c7c4-4fdb-9f90-d9af2a807c7a)
- [IBM: The relational database](https://www.ibm.com/history/relational-database)
- [Communications of the ACM: 50 Years of Queries](https://cacm.acm.org/research/50-years-of-queries/)
- [PostgreSQL: Table expressions and joins](https://www.postgresql.org/docs/current/queries-table-expressions.html)
- [PostgreSQL: Window functions](https://www.postgresql.org/docs/current/functions-window.html)
- [pandas: Comparison with SQL](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html)
- [pandas: DataFrame.merge](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
- [pandas: Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [pandas: Group by](https://pandas.pydata.org/docs/user_guide/groupby.html)

