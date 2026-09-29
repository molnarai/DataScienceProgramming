+++
title = "Shaping Data"
description = "Tabular data and how to query them."
weight = 70
outputs = ["Reveal"]
math = false
thumbnail = "../imgs/slides/pandas-working-on-sql.png"

[reveal_hugo]
custom_theme = "css/reveal-robinson.css"
slide_number = true
transition = "none"

+++

<style>
  .reveal .slides section { box-sizing: border-box; }
  .reveal .dc-kicker { color: #CC0000; font-size: 0.55em; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin: 0 0 4px 0; }
  .reveal .dc-small { font-size: 0.6em; }
  .reveal .dc-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; align-items: start; }
  .reveal .dc-cols h4 { font-size: 0.6em; margin: 0; color: #003478; }
  .reveal .dc-ex { font-size: 0.5em; font-weight: 700; color: #333; text-align: left; margin: 10px 0 0 0; border-bottom: 1px solid #d5dbe5; }
  .reveal .dc-cols .highlight pre, .reveal .dc-cols pre { width: 100%; font-size: 0.42em; margin: 4px 0; box-shadow: none; }
  .reveal .dc-cols pre code { max-height: none; padding: 6px 10px; }
</style>

<!-- 00: Shaping Data: The Core Operations of Data Transformation -->
{{< slide content-image="/imgs/shaping-data/shaping-data00.png" >}}
<h1></h1>

{{% note %}}
Today is about concepts, not syntax. Every analysis you will write in SQL or pandas is built from a handful of operations that change the shape of a table. If you can picture the shape before and after, the code becomes the easy part.
{{% /note %}}

***

<!-- 01: The Canvas: Rows, Columns, and Grain -->
{{< slide content-image="/imgs/shaping-data/shaping-data01.png" >}}
<h1></h1>

{{% note %}}
A row is one observation, a column is one attribute, and a null is a value we don't know, which is not the same as zero. The grain says what one row represents: one order, one order line, one customer. Ask "what is one row?" before every analysis.
{{% /note %}}

***

<!-- 01b: The orders table -->
<h2>One Table: <code>orders</code></h2>
<svg class="dc-tbl" style="width:100%;height:auto;margin-top:10px" viewBox="0 0 1165 402" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The orders table with five example rows: order_id is the primary key; customer_id, employee_id and ship_via are foreign keys; one row is one order; some values are NULL"><style>.dc-tbl text{font-family:"Source Sans Pro",Helvetica,Arial,sans-serif;fill:#222}.dc-tbl .m{font-family:Menlo,Consolas,monospace;font-size:12.5px}.dc-tbl .h{font-family:Menlo,Consolas,monospace;font-size:12.5px;font-weight:700;fill:#fff}.dc-tbl .t{font-family:Menlo,Consolas,monospace;font-size:10.5px;fill:#cfd8e8}.dc-tbl .null{fill:#8a94a6;font-style:italic}.dc-tbl .k{font-size:11px;font-weight:700}.dc-tbl .c{font-size:14px}.dc-tbl .cb{font-size:14px;font-weight:700}.dc-tbl .lead{fill:none;stroke-width:1.5}</style><rect x="696" y="70" width="71" height="216" fill="#0a8fb5" fill-opacity="0.12"/><text class="k" x="53.5" y="44" text-anchor="middle" fill="#CC0000" style="fill:#CC0000">PK</text><text x="53.5" y="60" text-anchor="middle" font-size="11" style="fill:#CC0000">unique</text><text class="k" x="144.0" y="44" text-anchor="middle" fill="#003478" style="fill:#003478">FK</text><text x="144.0" y="60" text-anchor="middle" font-size="11" style="fill:#003478">→ customers</text><text class="k" x="246.0" y="44" text-anchor="middle" fill="#003478" style="fill:#003478">FK</text><text x="246.0" y="60" text-anchor="middle" font-size="11" style="fill:#003478">→ employees</text><text class="k" x="656.5" y="44" text-anchor="middle" fill="#003478" style="fill:#003478">FK</text><text x="656.5" y="60" text-anchor="middle" font-size="11" style="fill:#003478">→ shippers</text><rect x="14" y="70" width="1137" height="44" fill="#003478"/><text class="h" x="23" y="89">order_id</text><text class="t" x="23" y="105">smallint</text><text class="h" x="102" y="89">customer_id</text><text class="t" x="102" y="105">bpchar</text><text class="h" x="204" y="89">employee_id</text><text class="t" x="204" y="105">smallint</text><text class="h" x="306" y="89">order_date</text><text class="t" x="306" y="105">date</text><text class="h" x="400" y="89">required_date</text><text class="t" x="400" y="105">date</text><text class="h" x="517" y="89">shipped_date</text><text class="t" x="517" y="105">date</text><text class="h" x="626" y="89">ship_via</text><text class="t" x="626" y="105">smallint</text><text class="h" x="705" y="89">freight</text><text class="t" x="705" y="105">real</text><text class="h" x="776" y="89">ship_city</text><text class="t" x="776" y="105">varchar(15)</text><text class="h" x="878" y="89">ship_region</text><text class="t" x="878" y="105">varchar(15)</text><text class="h" x="980" y="89">ship_country</text><text class="t" x="980" y="105">varchar(15)</text><text class="h" x="1089" y="89">…</text><text class="t" x="1089" y="105">+3 more</text><rect x="14" y="114" width="1137" height="30" fill="#ffffff" fill-opacity="0.85"/><text class="m" x="84" y="134" text-anchor="end">10501</text><text class="m" x="102" y="134">MAPLE</text><text class="m" x="288" y="134" text-anchor="end">3</text><text class="m" x="306" y="134">2026-03-02</text><text class="m" x="400" y="134">2026-03-30</text><text class="m" x="517" y="134">2026-03-05</text><text class="m" x="687" y="134" text-anchor="end">1</text><text class="m" x="758" y="134" text-anchor="end">12.40</text><text class="m" x="776" y="134">Toronto</text><text class="m" x="878" y="134">ON</text><text class="m" x="980" y="134">Canada</text><rect x="14" y="144" width="1137" height="30" fill="#f4f6f9" fill-opacity="0.85"/><text class="m" x="84" y="164" text-anchor="end">10502</text><text class="m" x="102" y="164">RIVER</text><text class="m" x="288" y="164" text-anchor="end">7</text><text class="m" x="306" y="164">2026-03-02</text><text class="m" x="400" y="164">2026-03-30</text><text class="m" x="517" y="164">2026-03-09</text><text class="m" x="687" y="164" text-anchor="end">3</text><text class="m" x="758" y="164" text-anchor="end">48.75</text><text class="m" x="776" y="164">Lyon</text><text class="m null" x="878" y="164">NULL</text><text class="m" x="980" y="164">France</text><rect x="14" y="174" width="1137" height="30" fill="#ffffff" fill-opacity="0.85"/><text class="m" x="84" y="194" text-anchor="end">10503</text><text class="m" x="102" y="194">SUNNY</text><text class="m" x="288" y="194" text-anchor="end">5</text><text class="m" x="306" y="194">2026-03-03</text><text class="m" x="400" y="194">2026-03-31</text><text class="m" x="517" y="194">2026-03-06</text><text class="m" x="687" y="194" text-anchor="end">2</text><text class="m" x="758" y="194" text-anchor="end">23.65</text><text class="m" x="776" y="194">Atlanta</text><text class="m" x="878" y="194">GA</text><text class="m" x="980" y="194">USA</text><rect x="14" y="204" width="1137" height="30" fill="#f4f6f9" fill-opacity="0.85"/><text class="m" x="84" y="224" text-anchor="end">10504</text><text class="m" x="102" y="224">ALPIN</text><text class="m" x="288" y="224" text-anchor="end">1</text><text class="m" x="306" y="224">2026-03-04</text><text class="m" x="400" y="224">2026-04-01</text><text class="m" x="517" y="224">2026-03-06</text><text class="m" x="687" y="224" text-anchor="end">1</text><text class="m" x="758" y="224" text-anchor="end">95.20</text><text class="m" x="776" y="224">Graz</text><text class="m null" x="878" y="224">NULL</text><text class="m" x="980" y="224">Austria</text><rect x="14" y="234" width="1137" height="30" fill="#ffffff" fill-opacity="0.85"/><text class="m" x="84" y="254" text-anchor="end">10505</text><text class="m" x="102" y="254">MAPLE</text><text class="m" x="288" y="254" text-anchor="end">3</text><text class="m" x="306" y="254">2026-03-04</text><text class="m" x="400" y="254">2026-04-01</text><text class="m null" x="517" y="254">NULL</text><text class="m" x="687" y="254" text-anchor="end">2</text><text class="m" x="758" y="254" text-anchor="end">7.10</text><text class="m" x="776" y="254">Toronto</text><text class="m" x="878" y="254">ON</text><text class="m" x="980" y="254">Canada</text><text class="m" x="23" y="280" style="fill:#888">⋮</text><text x="102" y="280" font-size="12" font-style="italic" style="fill:#888">the real Northwind table has 830 orders</text><rect x="696" y="70" width="71" height="216" fill="none" stroke="#0a8fb5" stroke-width="2.5" rx="2"/><rect x="10" y="234" width="1145" height="30" fill="none" stroke="#CC0000" stroke-width="2.5" rx="3"/><rect x="14" y="70" width="1137" height="194" fill="none" stroke="#b8c2d3" stroke-width="1"/><path class="lead" d="M44,264 V314 H44 V332" stroke="#CC0000"/><rect x="14" y="332" width="272" height="62" rx="5" fill="#fff" stroke="#CC0000" stroke-width="1.8"/><text class="cb" x="26" y="355" style="fill:#CC0000">ROW = one observation</text><text class="c" x="26" y="377">order 10505: one order</text><path class="lead" d="M538,264 V314 H342 V332" stroke="#6b7a90"/><rect x="302" y="332" width="272" height="62" rx="5" fill="#fff" stroke="#6b7a90" stroke-width="1.8"/><text class="cb" x="314" y="355" style="fill:#6b7a90">NULL = unknown</text><text class="c" x="314" y="377">not shipped yet — not “zero”</text><path class="lead" d="M731.5,286 V314 H630 V332" stroke="#0a8fb5"/><rect x="590" y="332" width="272" height="62" rx="5" fill="#fff" stroke="#0a8fb5" stroke-width="1.8"/><text class="cb" x="602" y="355" style="fill:#0a8fb5">COLUMN = one attribute</text><text class="c" x="602" y="377">freight: one meaning, one type</text><rect x="878" y="332" width="272" height="62" rx="5" fill="#fff" stroke="#003478" stroke-width="1.8"/><text class="cb" x="890" y="355" style="fill:#003478">GRAIN: one row per order</text><text class="c" x="890" y="377">order_id unique; customer_id repeats</text></svg>

{{% note %}}
A concrete table before we start transforming anything: the orders table from the Northwind database, with made-up values. One row is one order (the grain), so order_id, the primary key, never repeats. customer_id, employee_id and ship_via are foreign keys: they point to rows in other tables, and they can repeat, since MAPLE has two orders here. Each column holds one attribute with one type; the second header line shows the SQL type. NULL means unknown: order 10505 hasn't shipped yet, and a French or Austrian address simply has no region. Neither is zero or an empty string.
{{% /note %}}

***

<!-- 02: The Transformation Pipeline -->
{{< slide content-image="/imgs/shaping-data/shaping-data02.png" >}}
<h1></h1>

{{% note %}}
Here is the whole session on one assembly line: filter and sort, join, group by, aggregate, window. We'll take the stations one at a time and watch what each does to the height (rows) and width (columns) of the table.
{{% /note %}}

***

<!-- 03: FILTER: Keep only the rows that matter. -->
{{< slide content-image="/imgs/shaping-data/shaping-data03.png" >}}
<h1></h1>

{{% note %}}
A filter removes rows and keeps every column, so the grain stays the same and you just have fewer observations. SQL: WHERE. pandas: df.loc[mask]. Watch out for nulls: a row whose value is unknown does not pass a test like amount > 50.
{{% /note %}}

***

<!-- 03b: FILTER in code: SQL and pandas -->
<p class="dc-kicker">Filter in code</p>

## FILTER: `WHERE` ↔ `df.loc[mask]`

<div class="dc-cols"><h4>SQL</h4><h4>pandas</h4></div>
<p class="dc-ex">One condition: orders with freight above $50</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT *
FROM orders
WHERE freight > 50;          -- 10504
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
orders.loc[orders["freight"] > 50]
                             # 10504
{{< /highlight >}}
</div>
</div>
<p class="dc-ex">Several conditions, and only some columns</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT order_id, customer_id, freight
FROM orders
WHERE ship_country = 'Canada'
  AND order_date >= '2026-03-03';  -- 10505
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
orders.loc[
    (orders["ship_country"] == "Canada")
    & (orders["order_date"] >= "2026-03-03"),
    ["order_id", "customer_id", "freight"],
]                                  # 10505
{{< /highlight >}}
</div>
</div>
<p class="dc-ex">Missing values: orders not shipped yet</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT order_id, order_date
FROM orders
WHERE shipped_date IS NULL;  -- 10505
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
orders.loc[orders["shipped_date"].isna(),
           ["order_id", "order_date"]]
                             # 10505
{{< /highlight >}}
</div>
</div>

<p class="dc-small">Rows get fewer, columns stay the same (unless you pick them). <code>= NULL</code> never matches: use <code>IS NULL</code> / <code>.isna()</code>. In pandas, put each condition in <code>( )</code> and combine with <code>&amp;</code> (and) or <code>|</code> (or).</p>

{{% note %}}
Same three questions, two notations, run against the orders table from the start of the deck. The results (the comments) are the rows from that slide. SQL names the table in FROM and the condition in WHERE. pandas builds a True/False mask and passes it to .loc, with an optional list of columns as the second argument. Point out the two classic traps: shipped_date = NULL returns nothing because nothing equals an unknown value, and in pandas the parentheses around each comparison are required because & binds tighter than ==.
{{% /note %}}

***

<!-- 04: SORT: Reveal patterns through sequence. -->
{{< slide content-image="/imgs/shaping-data/shaping-data04.png" >}}
<h1></h1>

{{% note %}}
Sorting changes nothing but the order. Every row survives. It's how we find the largest, smallest, or most recent. A SQL result has no guaranteed order without ORDER BY, so sort explicitly whenever order matters, and add a tie-breaker.
{{% /note %}}

***

<!-- 04b: SORT in code: SQL and pandas -->
<p class="dc-kicker">Sort in code</p>

## SORT: `ORDER BY` ↔ `sort_values()`

<div class="dc-cols"><h4>SQL</h4><h4>pandas</h4></div>
<p class="dc-ex">Most expensive shipping first</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT order_id, freight
FROM orders
ORDER BY freight DESC;  -- 10504, 10502, ...
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
orders.sort_values("freight", ascending=False)
                        # 10504, 10502, ...
{{< /highlight >}}
</div>
</div>
<p class="dc-ex">Several sort keys, with a tie-breaker</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT *
FROM orders
ORDER BY ship_country,
         order_date DESC,
         order_id;
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
orders.sort_values(
    ["ship_country", "order_date", "order_id"],
    ascending=[True, False, True],
)
{{< /highlight >}}
</div>
</div>
<p class="dc-ex">Top 3, with missing values at the end</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT order_id, shipped_date
FROM orders
ORDER BY shipped_date DESC NULLS LAST
LIMIT 3;
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
(orders
 .sort_values("shipped_date", ascending=False,
              na_position="last")
 .head(3)[["order_id", "shipped_date"]])
{{< /highlight >}}
</div>
</div>

<p class="dc-small">Every row survives; only the order changes. Without <code>ORDER BY</code>, SQL promises <b>no</b> order. Add a unique column (<code>order_id</code>) as the last key so ties come out the same every time.</p>

{{% note %}}
Sorting never changes which rows you have, only their sequence. DESC / ascending=False reverses a key, and each key can have its own direction. The tie-breaker matters: two orders on the same date could come out in either order, and a unique last key such as order_id makes the result reproducible, also between SQL and pandas. Nulls differ between tools: PostgreSQL puts NULLs last when sorting ascending but first when sorting descending, while pandas puts them last either way unless na_position says otherwise. Writing NULLS LAST / na_position="last" explicitly removes the guesswork. LIMIT and head() only make sense after a sort: "top 3" of an unsorted table is just three arbitrary rows.
{{% /note %}}

***

<!-- 05: The Multi-Table World -->
{{< slide content-image="/imgs/shaping-data/shaping-data05.png" >}}
<h1></h1>

{{% note %}}
Why do businesses split data across tables? Normalization: store each fact with the entity it describes. A customer's address lives once in Customers, not on every order. That prevents inconsistent copies, but to answer most questions we have to bring the tables back together. The key is the bridge.
{{% /note %}}

***

<!-- 05b: The Northwind Database -->
<h2>The Northwind Database</h2>
<svg class="dc-erd" style="width:100%;height:auto;margin-top:6px" viewBox="0 0 1402 580" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Entity-relationship diagram of the Northwind database: 14 tables linked by primary and foreign keys"><style>.dc-erd text{font-family:"Source Sans Pro",Helvetica,Arial,sans-serif}.dc-erd .col{font-family:Menlo,Consolas,monospace;font-size:11.5px;fill:#222}.dc-erd .more{fill:#888;font-style:italic}.dc-erd .hd{font-family:Menlo,Consolas,monospace;font-size:12.5px;font-weight:700;fill:#fff}.dc-erd .mk{font-size:9.5px;font-weight:700}.dc-erd .rel{fill:none;stroke:#003478;stroke-width:1.6}</style><path class="rel" d="M204,42.5 H225.0 V59.5 H246"/><path class="rel" d="M210,36.5 L210,48.5"/><path class="rel" d="M236,59.5 L246,53.5 M236,59.5 L246,59.5 M236,59.5 L246,65.5"/><path class="rel" d="M344.0,142 V72"/><path class="rel" d="M338.0,136 L350.0,136"/><path class="rel" d="M344.0,82 L338.0,72 M344.0,82 L344.0,72 M344.0,82 L350.0,72"/><path class="rel" d="M442,176.5 H463.0 V193.5 H484"/><path class="rel" d="M448,170.5 L448,182.5"/><path class="rel" d="M474,193.5 L484,187.5 M474,193.5 L484,193.5 M474,193.5 L484,199.5"/><path class="rel" d="M582.0,89 V142"/><path class="rel" d="M576.0,95 L588.0,95"/><path class="rel" d="M582.0,132 L576.0,142 M582.0,132 L582.0,142 M582.0,132 L588.0,142"/><path class="rel" d="M582.0,392 V325"/><path class="rel" d="M576.0,386 L588.0,386"/><path class="rel" d="M582.0,335 L576.0,325 M582.0,335 L582.0,325 M582.0,335 L588.0,325"/><path class="rel" d="M680,176.5 H701.0 V176.5 H722"/><path class="rel" d="M686,170.5 L686,182.5"/><path class="rel" d="M712,176.5 L722,170.5 M712,176.5 L722,176.5 M712,176.5 L722,182.5"/><path class="rel" d="M960,176.5 H939.0 V193.5 H918"/><path class="rel" d="M954,170.5 L954,182.5"/><path class="rel" d="M928,193.5 L918,187.5 M928,193.5 L918,193.5 M928,193.5 L918,199.5"/><path class="rel" d="M1058.0,89 V142"/><path class="rel" d="M1052.0,95 L1064.0,95"/><path class="rel" d="M1058.0,132 L1052.0,142 M1058.0,132 L1058.0,142 M1058.0,132 L1064.0,142"/><path class="rel" d="M1198,176.5 H1177.0 V210.5 H1156"/><path class="rel" d="M1192,170.5 L1192,182.5"/><path class="rel" d="M1166,210.5 L1156,204.5 M1166,210.5 L1156,210.5 M1166,210.5 L1156,216.5"/><path class="rel" d="M680,426.5 H701.0 V426.5 H722"/><path class="rel" d="M686,420.5 L686,432.5"/><path class="rel" d="M712,426.5 L722,420.5 M712,426.5 L722,426.5 M712,426.5 L722,432.5"/><path class="rel" d="M960,426.5 H939.0 V443.5 H918"/><path class="rel" d="M954,420.5 L954,432.5"/><path class="rel" d="M928,443.5 L918,437.5 M928,443.5 L918,443.5 M928,443.5 L918,449.5"/><path class="rel" d="M1198,426.5 H1177.0 V460.5 H1156"/><path class="rel" d="M1192,420.5 L1192,432.5"/><path class="rel" d="M1166,460.5 L1156,454.5 M1166,460.5 L1156,460.5 M1166,460.5 L1156,466.5"/><path class="rel" d="M484,426.5 H462 V511.5 H484"/><path class="rel" d="M478,420.5 L478,432.5"/><path class="rel" d="M474,511.5 L484,505.5 M474,511.5 L484,511.5 M474,511.5 L484,517.5"/><g><rect x="8" y="8" width="196" height="64" rx="5" fill="#fff" stroke="#6b7a90" stroke-width="1.5"/><path d="M8,13 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#6b7a90"/><text class="hd" x="17" y="24.5">customer_demographics</text><text class="mk" x="14" y="46" fill="#CC0000">PK</text><text class="col" x="50" y="46" font-weight="700">customer_type_id</text><text class="col" x="50" y="63">customer_desc</text></g><g><rect x="246" y="8" width="196" height="64" rx="5" fill="#fff" stroke="#6b7a90" stroke-width="1.5"/><path d="M246,13 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#6b7a90"/><text class="hd" x="255" y="24.5">customer_customer_demo</text><text class="mk" x="252" y="46" fill="#CC0000">PK</text><text class="mk" x="268" y="46" fill="#003478">FK</text><text class="col" x="288" y="46" font-weight="700">customer_id</text><text class="mk" x="252" y="63" fill="#CC0000">PK</text><text class="mk" x="268" y="63" fill="#003478">FK</text><text class="col" x="288" y="63" font-weight="700">customer_type_id</text></g><g><rect x="484" y="8" width="196" height="81" rx="5" fill="#fff" stroke="#6b7a90" stroke-width="1.5"/><path d="M484,13 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#6b7a90"/><text class="hd" x="493" y="24.5">shippers</text><text class="mk" x="490" y="46" fill="#CC0000">PK</text><text class="col" x="526" y="46" font-weight="700">shipper_id</text><text class="col" x="526" y="63">company_name</text><text class="col" x="526" y="80">phone</text></g><g><rect x="960" y="8" width="196" height="81" rx="5" fill="#fff" stroke="#003478" stroke-width="1.5"/><path d="M960,13 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#003478"/><text class="hd" x="969" y="24.5">categories</text><text class="mk" x="966" y="46" fill="#CC0000">PK</text><text class="col" x="1002" y="46" font-weight="700">category_id</text><text class="col" x="1002" y="63">category_name</text><text class="col" x="1002" y="80">description</text></g><g><rect x="1198" y="8" width="196" height="98" rx="5" fill="#fff" stroke="#6b7a90" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M1198,13 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#6b7a90"/><text class="hd" x="1207" y="24.5">us_states</text><text class="mk" x="1204" y="46" fill="#CC0000">PK</text><text class="col" x="1240" y="46" font-weight="700">state_id</text><text class="col" x="1240" y="63">state_name</text><text class="col" x="1240" y="80">state_abbr</text><text class="col more" x="1240" y="97">no relationships</text></g><g><rect x="246" y="142" width="196" height="149" rx="5" fill="#fff" stroke="#003478" stroke-width="1.5"/><path d="M246,147 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#003478"/><text class="hd" x="255" y="158.5">customers</text><text class="mk" x="252" y="180" fill="#CC0000">PK</text><text class="col" x="288" y="180" font-weight="700">customer_id</text><text class="col" x="288" y="197">company_name</text><text class="col" x="288" y="214">contact_name</text><text class="col" x="288" y="231">city</text><text class="col" x="288" y="248">region</text><text class="col" x="288" y="265">country</text><text class="col more" x="288" y="282">+ 5 more</text></g><g><rect x="484" y="142" width="196" height="183" rx="5" fill="#fff" stroke="#003478" stroke-width="1.5"/><path d="M484,147 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#003478"/><text class="hd" x="493" y="158.5">orders</text><text class="mk" x="490" y="180" fill="#CC0000">PK</text><text class="col" x="526" y="180" font-weight="700">order_id</text><text class="mk" x="506" y="197" fill="#003478">FK</text><text class="col" x="526" y="197">customer_id</text><text class="mk" x="506" y="214" fill="#003478">FK</text><text class="col" x="526" y="214">employee_id</text><text class="col" x="526" y="231">order_date</text><text class="col" x="526" y="248">shipped_date</text><text class="mk" x="506" y="265" fill="#003478">FK</text><text class="col" x="526" y="265">ship_via</text><text class="col" x="526" y="282">freight</text><text class="col" x="526" y="299">ship_country</text><text class="col more" x="526" y="316">+ 6 more</text></g><g><rect x="722" y="142" width="196" height="115" rx="5" fill="#fff" stroke="#003478" stroke-width="1.5"/><path d="M722,147 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#003478"/><text class="hd" x="731" y="158.5">order_details</text><text class="mk" x="728" y="180" fill="#CC0000">PK</text><text class="mk" x="744" y="180" fill="#003478">FK</text><text class="col" x="764" y="180" font-weight="700">order_id</text><text class="mk" x="728" y="197" fill="#CC0000">PK</text><text class="mk" x="744" y="197" fill="#003478">FK</text><text class="col" x="764" y="197" font-weight="700">product_id</text><text class="col" x="764" y="214">unit_price</text><text class="col" x="764" y="231">quantity</text><text class="col" x="764" y="248">discount</text></g><g><rect x="960" y="142" width="196" height="166" rx="5" fill="#fff" stroke="#003478" stroke-width="1.5"/><path d="M960,147 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#003478"/><text class="hd" x="969" y="158.5">products</text><text class="mk" x="966" y="180" fill="#CC0000">PK</text><text class="col" x="1002" y="180" font-weight="700">product_id</text><text class="col" x="1002" y="197">product_name</text><text class="mk" x="982" y="214" fill="#003478">FK</text><text class="col" x="1002" y="214">supplier_id</text><text class="mk" x="982" y="231" fill="#003478">FK</text><text class="col" x="1002" y="231">category_id</text><text class="col" x="1002" y="248">unit_price</text><text class="col" x="1002" y="265">units_in_stock</text><text class="col" x="1002" y="282">discontinued</text><text class="col more" x="1002" y="299">+ 3 more</text></g><g><rect x="1198" y="142" width="196" height="115" rx="5" fill="#fff" stroke="#003478" stroke-width="1.5"/><path d="M1198,147 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#003478"/><text class="hd" x="1207" y="158.5">suppliers</text><text class="mk" x="1204" y="180" fill="#CC0000">PK</text><text class="col" x="1240" y="180" font-weight="700">supplier_id</text><text class="col" x="1240" y="197">company_name</text><text class="col" x="1240" y="214">city</text><text class="col" x="1240" y="231">country</text><text class="col more" x="1240" y="248">+ 8 more</text></g><g><rect x="484" y="392" width="196" height="149" rx="5" fill="#fff" stroke="#003478" stroke-width="1.5"/><path d="M484,397 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#003478"/><text class="hd" x="493" y="408.5">employees</text><text class="mk" x="490" y="430" fill="#CC0000">PK</text><text class="col" x="526" y="430" font-weight="700">employee_id</text><text class="col" x="526" y="447">last_name</text><text class="col" x="526" y="464">first_name</text><text class="col" x="526" y="481">title</text><text class="col" x="526" y="498">hire_date</text><text class="mk" x="506" y="515" fill="#003478">FK</text><text class="col" x="526" y="515">reports_to</text><text class="col more" x="526" y="532">+ 12 more</text></g><g><rect x="722" y="392" width="196" height="64" rx="5" fill="#fff" stroke="#6b7a90" stroke-width="1.5"/><path d="M722,397 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#6b7a90"/><text class="hd" x="731" y="408.5">employee_territories</text><text class="mk" x="728" y="430" fill="#CC0000">PK</text><text class="mk" x="744" y="430" fill="#003478">FK</text><text class="col" x="764" y="430" font-weight="700">employee_id</text><text class="mk" x="728" y="447" fill="#CC0000">PK</text><text class="mk" x="744" y="447" fill="#003478">FK</text><text class="col" x="764" y="447" font-weight="700">territory_id</text></g><g><rect x="960" y="392" width="196" height="81" rx="5" fill="#fff" stroke="#6b7a90" stroke-width="1.5"/><path d="M960,397 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#6b7a90"/><text class="hd" x="969" y="408.5">territories</text><text class="mk" x="966" y="430" fill="#CC0000">PK</text><text class="col" x="1002" y="430" font-weight="700">territory_id</text><text class="col" x="1002" y="447">territory_description</text><text class="mk" x="982" y="464" fill="#003478">FK</text><text class="col" x="1002" y="464">region_id</text></g><g><rect x="1198" y="392" width="196" height="64" rx="5" fill="#fff" stroke="#6b7a90" stroke-width="1.5"/><path d="M1198,397 a5,5 0 0 1 5,-5 h186 a5,5 0 0 1 5,5 v19 h-196 z" fill="#6b7a90"/><text class="hd" x="1207" y="408.5">region</text><text class="mk" x="1204" y="430" fill="#CC0000">PK</text><text class="col" x="1240" y="430" font-weight="700">region_id</text><text class="col" x="1240" y="447">region_description</text></g><g font-size="11.5"><rect x="722" y="8" width="196" height="118" rx="5" fill="#f4f6f9"/><text x="732" y="26" font-weight="700" fill="#222">Legend</text><text class="mk" x="732" y="45" fill="#CC0000">PK</text><text x="756" y="45" fill="#222">primary key</text><text class="mk" x="732" y="62" fill="#003478">FK</text><text x="756" y="62" fill="#222">foreign key</text><path class="rel" d="M732,79 H772"/><path class="rel" d="M738,73 L738,85"/><path class="rel" d="M762,79 L772,73 M762,79 L772,79 M762,79 L772,85"/><text x="780" y="83" fill="#222">one … many</text><rect x="732" y="94" width="12" height="10" fill="#003478"/><text x="750" y="103" fill="#222">used in the notebooks</text><rect x="732" y="109" width="12" height="10" fill="#6b7a90"/><text x="750" y="118" fill="#222">supporting tables</text></g></svg>

{{% note %}}
Here is the database we query in the notebooks. Read the lines as one-to-many: one customer places many orders, one order has many order lines, one product appears on many order lines. order_details sits in the middle and resolves the many-to-many relationship between orders and products; its primary key is the pair (order_id, product_id). Two things to point out: unit_price appears in both order_details (the price actually charged) and products (today's list price), and employees.reports_to points back into employees, which is a self-join. The gray tables are supporting data we won't use.
{{% /note %}}

***

<!-- 06: JOIN: Combine tables by matching keys. -->
{{< slide content-image="/imgs/shaping-data/shaping-data06.png" >}}
<h1></h1>

{{% note %}}
A join adds columns: the order row picks up the customer's name. The number of rows depends on the matches. One-to-one keeps it, one-to-many multiplies it, and duplicate keys can silently inflate totals. Always name the key (ON / on=) and check the row count afterwards.
{{% /note %}}

***

<!-- 06b: INNER JOIN, step by step -->
<h2>INNER JOIN, step by step</h2>
<svg class="dc-join" style="width:100%;height:auto;margin-top:4px" viewBox="0 0 1147 486" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Inner join of orders and customers on customer_id: four matched orders survive; order 10504 with unknown customer ALPIN and customer OAKLY with no orders are dropped; customer MAPLE appears twice in the result"><style>.dc-join text{font-family:"Source Sans Pro",Helvetica,Arial,sans-serif;fill:#222}.dc-join .m{font-family:Menlo,Consolas,monospace;font-size:12.5px}.dc-join .off{fill:#9aa3b2}.dc-join .h{font-family:Menlo,Consolas,monospace;font-size:12.5px;font-weight:700;fill:#fff}.dc-join .tt{font-size:17px;font-weight:700;fill:#003478}.dc-join .st{font-size:12.5px;fill:#666;font-style:italic}.dc-join .code{font-family:Menlo,Consolas,monospace;font-size:12.5px}.dc-join .kw{font-weight:700;fill:#003478}.dc-join .x{font-size:12px;font-weight:700;fill:#CC0000;stroke:#fff;stroke-width:5px;stroke-linejoin:round;paint-order:stroke}.dc-join .xn{fill:#b26a00}.dc-join .null{fill:#8a94a6;font-style:italic}.dc-join .c{font-size:14px}.dc-join .cb{font-size:14px;font-weight:700}</style><text x="30" y="30" class="tt">orders</text><text x="30" y="45" class="st">left table · one row per order</text><rect x="30" y="52" width="81" height="30" fill="#003478"/><text class="h" x="40" y="72">order_id</text><rect x="111" y="52" width="104" height="30" fill="#003478"/><text class="h" x="121" y="72">customer_id</text><rect x="215" y="52" width="73" height="30" fill="#003478"/><text class="h" x="225" y="72">freight</text><rect x="30" y="82" width="258" height="28" fill="#fff"/><text class="m" x="101" y="101" text-anchor="end">10501</text><rect x="114" y="86" width="98" height="20" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="121" y="101">MAPLE</text><text class="m" x="278" y="101" text-anchor="end">12.40</text><rect x="30" y="110" width="258" height="28" fill="#f4f6f9"/><text class="m" x="101" y="129" text-anchor="end">10502</text><rect x="114" y="114" width="98" height="20" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="121" y="129">RIVER</text><text class="m" x="278" y="129" text-anchor="end">48.75</text><rect x="30" y="138" width="258" height="28" fill="#fff"/><text class="m" x="101" y="157" text-anchor="end">10503</text><rect x="114" y="142" width="98" height="20" rx="4" fill="#c9900c" fill-opacity="0.18" stroke="#c9900c" stroke-width="1.4"/><text class="m" x="121" y="157">SUNNY</text><text class="m" x="278" y="157" text-anchor="end">23.65</text><rect x="30" y="166" width="258" height="28" fill="#f4f6f9"/><text class="m off" x="101" y="185" text-anchor="end">10504</text><text class="m off" x="121" y="185">ALPIN</text><text class="m off" x="278" y="185" text-anchor="end">95.20</text><line x1="34" y1="180.0" x2="284" y2="180.0" stroke="#CC0000" stroke-width="1.3" stroke-opacity="0.7"/><rect x="30" y="194" width="258" height="28" fill="#fff"/><text class="m" x="101" y="213" text-anchor="end">10505</text><rect x="114" y="198" width="98" height="20" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="121" y="213">MAPLE</text><text class="m" x="278" y="213" text-anchor="end">7.10</text><rect x="30" y="52" width="258" height="170" fill="none" stroke="#b8c2d3"/><text x="463" y="30" class="tt">customers</text><text x="463" y="45" class="st">right table · one row per customer</text><rect x="463" y="52" width="104" height="30" fill="#1d6f7a"/><text class="h" x="473" y="72">customer_id</text><rect x="567" y="52" width="149" height="30" fill="#1d6f7a"/><text class="h" x="577" y="72">company_name</text><rect x="716" y="52" width="81" height="30" fill="#1d6f7a"/><text class="h" x="726" y="72">city</text><rect x="463" y="82" width="334" height="28" fill="#fff"/><rect x="466" y="86" width="98" height="20" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="473" y="101">MAPLE</text><text class="m" x="577" y="101">Maple Street Deli</text><text class="m" x="726" y="101">Toronto</text><rect x="463" y="110" width="334" height="28" fill="#f4f6f9"/><text class="m off" x="473" y="129">OAKLY</text><text class="m off" x="577" y="129">Oak Lane Grocers</text><text class="m off" x="726" y="129">Portland</text><line x1="467" y1="124.0" x2="793" y2="124.0" stroke="#CC0000" stroke-width="1.3" stroke-opacity="0.7"/><rect x="463" y="138" width="334" height="28" fill="#fff"/><rect x="466" y="142" width="98" height="20" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="473" y="157">RIVER</text><text class="m" x="577" y="157">Riverside Bistro</text><text class="m" x="726" y="157">Lyon</text><rect x="463" y="166" width="334" height="28" fill="#f4f6f9"/><rect x="466" y="170" width="98" height="20" rx="4" fill="#c9900c" fill-opacity="0.18" stroke="#c9900c" stroke-width="1.4"/><text class="m" x="473" y="185">SUNNY</text><text class="m" x="577" y="185">Sunny Side Café</text><text class="m" x="726" y="185">Atlanta</text><rect x="463" y="52" width="334" height="142" fill="none" stroke="#b8c2d3"/><path d="M288,96.0 C375.5,96.0 375.5,96.0 463,96.0" fill="none" stroke="#0a8fb5" stroke-width="2.2"/><circle cx="288" cy="96.0" r="3.5" fill="#0a8fb5"/><circle cx="463" cy="96.0" r="3.5" fill="#0a8fb5"/><path d="M288,124.0 C375.5,124.0 375.5,152.0 463,152.0" fill="none" stroke="#e0604f" stroke-width="2.2"/><circle cx="288" cy="124.0" r="3.5" fill="#e0604f"/><circle cx="463" cy="152.0" r="3.5" fill="#e0604f"/><path d="M288,152.0 C375.5,152.0 375.5,180.0 463,180.0" fill="none" stroke="#c9900c" stroke-width="2.2"/><circle cx="288" cy="152.0" r="3.5" fill="#c9900c"/><circle cx="463" cy="180.0" r="3.5" fill="#c9900c"/><path d="M288,208.0 C375.5,208.0 375.5,96.0 463,96.0" fill="none" stroke="#0a8fb5" stroke-width="2.2"/><circle cx="288" cy="208.0" r="3.5" fill="#0a8fb5"/><circle cx="463" cy="96.0" r="3.5" fill="#0a8fb5"/><text class="x" x="298" y="184.0">✕ no customer ALPIN</text><text class="x" x="453" y="128.0" text-anchor="end">no orders ✕</text><rect x="827" y="22" width="312" height="206" rx="6" fill="#f4f6f9"/><text class="cb" x="841" y="44" style="fill:#003478">INNER JOIN on customer_id</text><text x="841" y="68" font-size="12" font-weight="700" style="fill:#666">SQL</text><text class="code" x="841.0" y="86">SELECT *</text><text class="code" x="841.0" y="103">FROM orders AS o</text><text class="code" x="841.0" y="120">INNER JOIN customers AS c</text><text class="code" x="856.2" y="137">ON o.customer_id = c.customer_id;</text><text x="841" y="162" font-size="12" font-weight="700" style="fill:#666">pandas</text><text class="code" x="841.0" y="180">orders.merge(customers,</text><text class="code" x="871.4" y="197">on="customer_id", how="inner")</text><path d="M180,234 V254" stroke="#003478" stroke-width="2" fill="none" marker-end="url(#arr-inner)"/><defs><marker id="arr-inner" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#003478"/></marker></defs><text x="30" y="272" class="tt">result</text><text x="30" y="287" class="st">one row per matched order · 4 rows × 5 columns</text><rect x="30" y="294" width="81" height="30" fill="#003478"/><text class="h" x="40" y="314">order_id</text><rect x="111" y="294" width="104" height="30" fill="#003478"/><text class="h" x="121" y="314">customer_id</text><rect x="215" y="294" width="73" height="30" fill="#003478"/><text class="h" x="225" y="314">freight</text><rect x="288" y="294" width="149" height="30" fill="#1d6f7a"/><text class="h" x="298" y="314">company_name</text><rect x="437" y="294" width="73" height="30" fill="#1d6f7a"/><text class="h" x="447" y="314">city</text><rect x="30" y="324" width="480" height="28" fill="#fff"/><text class="m" x="101" y="343" text-anchor="end">10501</text><rect x="114" y="328" width="98" height="20" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="121" y="343">MAPLE</text><text class="m" x="278" y="343" text-anchor="end">12.40</text><text class="m" x="298" y="343">Maple Street Deli</text><text class="m" x="447" y="343">Toronto</text><rect x="30" y="352" width="480" height="28" fill="#f4f6f9"/><text class="m" x="101" y="371" text-anchor="end">10502</text><rect x="114" y="356" width="98" height="20" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="121" y="371">RIVER</text><text class="m" x="278" y="371" text-anchor="end">48.75</text><text class="m" x="298" y="371">Riverside Bistro</text><text class="m" x="447" y="371">Lyon</text><rect x="30" y="380" width="480" height="28" fill="#fff"/><text class="m" x="101" y="399" text-anchor="end">10503</text><rect x="114" y="384" width="98" height="20" rx="4" fill="#c9900c" fill-opacity="0.18" stroke="#c9900c" stroke-width="1.4"/><text class="m" x="121" y="399">SUNNY</text><text class="m" x="278" y="399" text-anchor="end">23.65</text><text class="m" x="298" y="399">Sunny Side Café</text><text class="m" x="447" y="399">Atlanta</text><rect x="30" y="408" width="480" height="28" fill="#f4f6f9"/><text class="m" x="101" y="427" text-anchor="end">10505</text><rect x="114" y="412" width="98" height="20" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="121" y="427">MAPLE</text><text class="m" x="278" y="427" text-anchor="end">7.10</text><text class="m" x="298" y="427">Maple Street Deli</text><text class="m" x="447" y="427">Toronto</text><rect x="30" y="294" width="480" height="142" fill="none" stroke="#b8c2d3"/><rect x="290" y="327.0" width="218" height="22" rx="4" fill="none" stroke="#0a8fb5" stroke-width="1.6" stroke-dasharray="4 3"/><rect x="290" y="411.0" width="218" height="22" rx="4" fill="none" stroke="#0a8fb5" stroke-width="1.6" stroke-dasharray="4 3"/><text x="550" y="288" font-size="19" font-weight="700" style="fill:#2e7d32">✓</text><text class="cb" x="578" y="286" style="fill:#2e7d32">Matched rows survive</text><text class="c" x="578" y="306">4 of the 5 orders have a customer, so the result has 4 rows.</text><text x="550" y="338" font-size="19" font-weight="700" style="fill:#CC0000">✕</text><text class="cb" x="578" y="336" style="fill:#CC0000">Unmatched rows disappear</text><text class="c" x="578" y="356">Order 10504 (customer ALPIN is unknown) and customer OAKLY (no orders).</text><text x="550" y="388" font-size="19" font-weight="700" style="fill:#0a8fb5">↻</text><text class="cb" x="578" y="386" style="fill:#0a8fb5">One-to-many repeats the “one” side</text><text class="c" x="578" y="406">MAPLE has two orders, so its name and city appear twice.</text><text x="550" y="438" font-size="19" font-weight="700" style="fill:#003478">⇔</text><text class="cb" x="578" y="436" style="fill:#003478">Shape: width grows, height depends</text><text class="c" x="578" y="456">3 + 2 columns (the key once); rows = number of matched pairs.</text></svg>

{{% note %}}
Walk through it line by line. Each order looks up its customer_id in customers; the colored lines are the matches. Order 10504 points to ALPIN, which doesn't exist in customers, so an inner join drops it. OAKLY never ordered anything, so it's dropped too. MAPLE has two orders, so both find the same customer row, and MAPLE's name and city are copied into two result rows. That's normal for one-to-many, but it's why summing a customer-level number after this join would double-count. Ask the class: how many rows would we get if customers accidentally had MAPLE twice? (Answer: 6, since each MAPLE order matches both copies.) In pandas, validate="many_to_one" would catch that.
{{% /note %}}

***

<!-- 06c: LEFT JOIN, step by step -->
<h2>LEFT JOIN, step by step</h2>
<svg class="dc-join" style="width:100%;height:auto;margin-top:4px" viewBox="0 0 1147 486" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Left join of orders and customers on customer_id: all five orders survive; order 10504 with unknown customer ALPIN gets NULL company_name and city; customer OAKLY with no orders is dropped"><style>.dc-join text{font-family:"Source Sans Pro",Helvetica,Arial,sans-serif;fill:#222}.dc-join .m{font-family:Menlo,Consolas,monospace;font-size:12.5px}.dc-join .off{fill:#9aa3b2}.dc-join .h{font-family:Menlo,Consolas,monospace;font-size:12.5px;font-weight:700;fill:#fff}.dc-join .tt{font-size:17px;font-weight:700;fill:#003478}.dc-join .st{font-size:12.5px;fill:#666;font-style:italic}.dc-join .code{font-family:Menlo,Consolas,monospace;font-size:12.5px}.dc-join .kw{font-weight:700;fill:#003478}.dc-join .x{font-size:12px;font-weight:700;fill:#CC0000;stroke:#fff;stroke-width:5px;stroke-linejoin:round;paint-order:stroke}.dc-join .xn{fill:#b26a00}.dc-join .null{fill:#8a94a6;font-style:italic}.dc-join .c{font-size:14px}.dc-join .cb{font-size:14px;font-weight:700}</style><text x="30" y="30" class="tt">orders</text><text x="30" y="45" class="st">left table · one row per order</text><rect x="30" y="52" width="81" height="30" fill="#003478"/><text class="h" x="40" y="72">order_id</text><rect x="111" y="52" width="104" height="30" fill="#003478"/><text class="h" x="121" y="72">customer_id</text><rect x="215" y="52" width="73" height="30" fill="#003478"/><text class="h" x="225" y="72">freight</text><rect x="30" y="82" width="258" height="28" fill="#fff"/><text class="m" x="101" y="101" text-anchor="end">10501</text><rect x="114" y="86" width="98" height="20" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="121" y="101">MAPLE</text><text class="m" x="278" y="101" text-anchor="end">12.40</text><rect x="30" y="110" width="258" height="28" fill="#f4f6f9"/><text class="m" x="101" y="129" text-anchor="end">10502</text><rect x="114" y="114" width="98" height="20" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="121" y="129">RIVER</text><text class="m" x="278" y="129" text-anchor="end">48.75</text><rect x="30" y="138" width="258" height="28" fill="#fff"/><text class="m" x="101" y="157" text-anchor="end">10503</text><rect x="114" y="142" width="98" height="20" rx="4" fill="#c9900c" fill-opacity="0.18" stroke="#c9900c" stroke-width="1.4"/><text class="m" x="121" y="157">SUNNY</text><text class="m" x="278" y="157" text-anchor="end">23.65</text><rect x="30" y="166" width="258" height="28" fill="#f4f6f9"/><text class="m" x="101" y="185" text-anchor="end">10504</text><rect x="114" y="170" width="98" height="20" rx="4" fill="none" stroke="#b26a00" stroke-width="1.4" stroke-dasharray="4 3"/><text class="m" x="121" y="185">ALPIN</text><text class="m" x="278" y="185" text-anchor="end">95.20</text><rect x="30" y="194" width="258" height="28" fill="#fff"/><text class="m" x="101" y="213" text-anchor="end">10505</text><rect x="114" y="198" width="98" height="20" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="121" y="213">MAPLE</text><text class="m" x="278" y="213" text-anchor="end">7.10</text><rect x="30" y="52" width="258" height="170" fill="none" stroke="#b8c2d3"/><text x="463" y="30" class="tt">customers</text><text x="463" y="45" class="st">right table · one row per customer</text><rect x="463" y="52" width="104" height="30" fill="#1d6f7a"/><text class="h" x="473" y="72">customer_id</text><rect x="567" y="52" width="149" height="30" fill="#1d6f7a"/><text class="h" x="577" y="72">company_name</text><rect x="716" y="52" width="81" height="30" fill="#1d6f7a"/><text class="h" x="726" y="72">city</text><rect x="463" y="82" width="334" height="28" fill="#fff"/><rect x="466" y="86" width="98" height="20" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="473" y="101">MAPLE</text><text class="m" x="577" y="101">Maple Street Deli</text><text class="m" x="726" y="101">Toronto</text><rect x="463" y="110" width="334" height="28" fill="#f4f6f9"/><text class="m off" x="473" y="129">OAKLY</text><text class="m off" x="577" y="129">Oak Lane Grocers</text><text class="m off" x="726" y="129">Portland</text><line x1="467" y1="124.0" x2="793" y2="124.0" stroke="#CC0000" stroke-width="1.3" stroke-opacity="0.7"/><rect x="463" y="138" width="334" height="28" fill="#fff"/><rect x="466" y="142" width="98" height="20" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="473" y="157">RIVER</text><text class="m" x="577" y="157">Riverside Bistro</text><text class="m" x="726" y="157">Lyon</text><rect x="463" y="166" width="334" height="28" fill="#f4f6f9"/><rect x="466" y="170" width="98" height="20" rx="4" fill="#c9900c" fill-opacity="0.18" stroke="#c9900c" stroke-width="1.4"/><text class="m" x="473" y="185">SUNNY</text><text class="m" x="577" y="185">Sunny Side Café</text><text class="m" x="726" y="185">Atlanta</text><rect x="463" y="52" width="334" height="142" fill="none" stroke="#b8c2d3"/><path d="M288,96.0 C375.5,96.0 375.5,96.0 463,96.0" fill="none" stroke="#0a8fb5" stroke-width="2.2"/><circle cx="288" cy="96.0" r="3.5" fill="#0a8fb5"/><circle cx="463" cy="96.0" r="3.5" fill="#0a8fb5"/><path d="M288,124.0 C375.5,124.0 375.5,152.0 463,152.0" fill="none" stroke="#e0604f" stroke-width="2.2"/><circle cx="288" cy="124.0" r="3.5" fill="#e0604f"/><circle cx="463" cy="152.0" r="3.5" fill="#e0604f"/><path d="M288,152.0 C375.5,152.0 375.5,180.0 463,180.0" fill="none" stroke="#c9900c" stroke-width="2.2"/><circle cx="288" cy="152.0" r="3.5" fill="#c9900c"/><circle cx="463" cy="180.0" r="3.5" fill="#c9900c"/><path d="M288,208.0 C375.5,208.0 375.5,96.0 463,96.0" fill="none" stroke="#0a8fb5" stroke-width="2.2"/><circle cx="288" cy="208.0" r="3.5" fill="#0a8fb5"/><circle cx="463" cy="96.0" r="3.5" fill="#0a8fb5"/><text class="x xn" x="298" y="184.0">no match → NULLs</text><text class="x" x="453" y="128.0" text-anchor="end">no orders ✕</text><rect x="827" y="22" width="312" height="206" rx="6" fill="#f4f6f9"/><text class="cb" x="841" y="44" style="fill:#003478">LEFT JOIN on customer_id</text><text x="841" y="68" font-size="12" font-weight="700" style="fill:#666">SQL</text><text class="code" x="841.0" y="86">SELECT *</text><text class="code" x="841.0" y="103">FROM orders AS o</text><text class="code" x="841.0" y="120">LEFT JOIN customers AS c</text><text class="code" x="856.2" y="137">ON o.customer_id = c.customer_id;</text><text x="841" y="162" font-size="12" font-weight="700" style="fill:#666">pandas</text><text class="code" x="841.0" y="180">orders.merge(customers,</text><text class="code" x="871.4" y="197">on="customer_id", how="left")</text><path d="M180,234 V254" stroke="#003478" stroke-width="2" fill="none" marker-end="url(#arr-left)"/><defs><marker id="arr-left" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#003478"/></marker></defs><text x="30" y="272" class="tt">result</text><text x="30" y="287" class="st">one row per order · 5 rows × 5 columns (as many rows as orders)</text><rect x="30" y="294" width="81" height="30" fill="#003478"/><text class="h" x="40" y="314">order_id</text><rect x="111" y="294" width="104" height="30" fill="#003478"/><text class="h" x="121" y="314">customer_id</text><rect x="215" y="294" width="73" height="30" fill="#003478"/><text class="h" x="225" y="314">freight</text><rect x="288" y="294" width="149" height="30" fill="#1d6f7a"/><text class="h" x="298" y="314">company_name</text><rect x="437" y="294" width="73" height="30" fill="#1d6f7a"/><text class="h" x="447" y="314">city</text><rect x="30" y="324" width="480" height="28" fill="#fff"/><text class="m" x="101" y="343" text-anchor="end">10501</text><rect x="114" y="328" width="98" height="20" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="121" y="343">MAPLE</text><text class="m" x="278" y="343" text-anchor="end">12.40</text><text class="m" x="298" y="343">Maple Street Deli</text><text class="m" x="447" y="343">Toronto</text><rect x="30" y="352" width="480" height="28" fill="#f4f6f9"/><text class="m" x="101" y="371" text-anchor="end">10502</text><rect x="114" y="356" width="98" height="20" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="121" y="371">RIVER</text><text class="m" x="278" y="371" text-anchor="end">48.75</text><text class="m" x="298" y="371">Riverside Bistro</text><text class="m" x="447" y="371">Lyon</text><rect x="30" y="380" width="480" height="28" fill="#fff"/><text class="m" x="101" y="399" text-anchor="end">10503</text><rect x="114" y="384" width="98" height="20" rx="4" fill="#c9900c" fill-opacity="0.18" stroke="#c9900c" stroke-width="1.4"/><text class="m" x="121" y="399">SUNNY</text><text class="m" x="278" y="399" text-anchor="end">23.65</text><text class="m" x="298" y="399">Sunny Side Café</text><text class="m" x="447" y="399">Atlanta</text><rect x="30" y="408" width="480" height="28" fill="#f4f6f9"/><text class="m" x="101" y="427" text-anchor="end">10504</text><rect x="114" y="412" width="98" height="20" rx="4" fill="none" stroke="#b26a00" stroke-width="1.4" stroke-dasharray="4 3"/><text class="m" x="121" y="427">ALPIN</text><text class="m" x="278" y="427" text-anchor="end">95.20</text><rect x="291" y="412" width="143" height="20" rx="4" fill="#eef0f4" stroke="#8a94a6" stroke-width="1" stroke-dasharray="3 3"/><text class="m null" x="298" y="427">NULL</text><rect x="440" y="412" width="67" height="20" rx="4" fill="#eef0f4" stroke="#8a94a6" stroke-width="1" stroke-dasharray="3 3"/><text class="m null" x="447" y="427">NULL</text><rect x="30" y="436" width="480" height="28" fill="#fff"/><text class="m" x="101" y="455" text-anchor="end">10505</text><rect x="114" y="440" width="98" height="20" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="121" y="455">MAPLE</text><text class="m" x="278" y="455" text-anchor="end">7.10</text><text class="m" x="298" y="455">Maple Street Deli</text><text class="m" x="447" y="455">Toronto</text><rect x="30" y="294" width="480" height="170" fill="none" stroke="#b8c2d3"/><rect x="290" y="327.0" width="218" height="22" rx="4" fill="none" stroke="#0a8fb5" stroke-width="1.6" stroke-dasharray="4 3"/><rect x="290" y="439.0" width="218" height="22" rx="4" fill="none" stroke="#0a8fb5" stroke-width="1.6" stroke-dasharray="4 3"/><text x="550" y="288" font-size="19" font-weight="700" style="fill:#2e7d32">✓</text><text class="cb" x="578" y="286" style="fill:#2e7d32">Every left row survives</text><text class="c" x="578" y="306">5 orders in, 5 rows out: the grain of orders is kept.</text><text x="550" y="338" font-size="19" font-weight="700" style="fill:#b26a00">∅</text><text class="cb" x="578" y="336" style="fill:#b26a00">No match → NULL</text><text class="c" x="578" y="356">Order 10504 stays; its company_name and city are NULL.</text><text x="550" y="388" font-size="19" font-weight="700" style="fill:#CC0000">✕</text><text class="cb" x="578" y="386" style="fill:#CC0000">Right-only rows still disappear</text><text class="c" x="578" y="406">Customer OAKLY has no orders, so it is not in the result.</text><text x="550" y="438" font-size="19" font-weight="700" style="fill:#003478">⚠</text><text class="cb" x="578" y="436" style="fill:#003478">Check the row count</text><text class="c" x="578" y="456">Unique key on the right: rows out = rows in. More means duplicates.</text></svg>

{{% note %}}
Same two tables, one word changed: LEFT instead of INNER. Now every order survives. Order 10504 still has no matching customer, but instead of disappearing it's kept, and the customer columns are filled with NULL: we don't know who ALPIN is. OAKLY is still missing, because a left join only protects rows of the left table. This is the join to use when the left table defines the grain you want, for example every order in a report whether or not the customer record is complete. The row-count check: if customer_id is unique in customers, a left join returns exactly as many rows as orders. More rows means the right key has duplicates. Finding the unmatched rows (WHERE c.customer_id IS NULL, or indicator=True in pandas) is also a quick data-quality check.
{{% /note %}}

***

<!-- 07: The Join Matrix: Deciding what survives. -->
{{< slide content-image="/imgs/shaping-data/shaping-data07.png" >}}
<h1></h1>

{{% note %}}
Inner: only matched pairs. Left: every left row, with nulls where there is no match. Right: the mirror image. Full outer: everything. The choice is a business decision. Do you want to see orders from unknown customers, or customers who never ordered? In Northwind, a left join finds the two customers with no orders.
{{% /note %}}

***

<!-- 07b: JOIN in code: SQL and pandas -->
<p class="dc-kicker">Join in code</p>

## JOIN: `JOIN … ON` ↔ `merge(on=, how=)`

<div class="dc-cols"><h4>SQL</h4><h4>pandas</h4></div>
<p class="dc-ex">Inner join: orders with their customer's name</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT o.order_id, o.freight, c.company_name
FROM orders AS o
INNER JOIN customers AS c
  ON o.customer_id = c.customer_id;  -- 4 rows
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
orders.merge(
    customers[["customer_id", "company_name"]],
    on="customer_id", how="inner",
)[["order_id", "freight", "company_name"]]  # 4 rows
{{< /highlight >}}
</div>
</div>
<p class="dc-ex">Left join: find orders whose customer is missing</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT o.order_id, o.customer_id
FROM orders AS o
LEFT JOIN customers AS c
  ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;         -- 10504
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
j = orders.merge(customers, on="customer_id",
                 how="left", indicator=True)
j.loc[j["_merge"] == "left_only",
      ["order_id", "customer_id"]]   # 10504
{{< /highlight >}}
</div>
</div>
<p class="dc-ex">Right and full outer join</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
-- every customer survives: 5 rows
... RIGHT JOIN customers AS c ON ...
-- everything survives: 6 rows
... FULL OUTER JOIN customers AS c ON ...
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
# every customer survives: 5 rows
orders.merge(customers, on="customer_id", how="right")
# everything survives: 6 rows
orders.merge(customers, on="customer_id", how="outer")
{{< /highlight >}}
</div>
</div>

<p class="dc-small">Always name the key (<code>ON</code> / <code>on=</code>); for different names use <code>left_on=</code> / <code>right_on=</code>. Check the row count after every join. <code>validate="many_to_one"</code> makes pandas stop if a customer appears twice.</p>

{{% note %}}
The same joins from the diagrams, now as code; the row counts in the comments match the pictures. SQL uses table aliases (o, c) so every column says where it comes from. pandas merge needs the key in on= and the join type in how=; the default is inner. The second example is a pattern worth memorizing: a left join followed by "right side is NULL" finds rows without a match. In pandas, indicator=True adds a _merge column saying both, left_only, or right_only. Right join is just a left join with the tables swapped; most people write left joins. Full outer (how="outer") keeps everything, which is useful for reconciling two lists. Warn against leaving out the key: pandas then joins on every column name the tables share, and SQL NATURAL JOIN does the same. In Northwind, orders and products both have unit_price, and a join on both silently drops rows.
{{% /note %}}

***

<!-- 08: GROUP BY: Partition rows by a shared attribute. -->
{{< slide content-image="/imgs/shaping-data/shaping-data08.png" >}}
<h1></h1>

{{% note %}}
Grouping on its own doesn't remove anything. It sorts the rows into buckets that share a key, here the customer ID. It's the preparation step, and the next slide shows what we do with each bucket.
{{% /note %}}

***

<!-- 09: AGGREGATE: Reduce groups to a single result. -->
{{< slide content-image="/imgs/shaping-data/shaping-data09.png" >}}
<h1></h1>

{{% note %}}
Aggregation collapses each group to one row: a count, sum, or average. The grain changes from one row per order to one row per customer, and the individual orders are gone. COUNT(*) counts rows, COUNT(column) counts known values. WHERE filters before grouping, HAVING after.
{{% /note %}}

***

<!-- 09b: GROUP BY and aggregate, step by step -->
<h2>GROUP BY + aggregate, step by step</h2>
<svg class="dc-gb" style="width:100%;height:auto;margin-top:4px" viewBox="0 0 1202 430" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="GROUP BY customer_id and aggregate: seven orders are sorted into four customer groups, then each group is reduced to one row with COUNT(*), COUNT(freight) and SUM(freight); MAPLE has three orders but only two known freight values"><style>.dc-gb text{font-family:"Source Sans Pro",Helvetica,Arial,sans-serif;fill:#222}.dc-gb .m{font-family:Menlo,Consolas,monospace;font-size:12.5px}.dc-gb .null{fill:#8a94a6;font-style:italic}.dc-gb .h{font-family:Menlo,Consolas,monospace;font-size:12.5px;font-weight:700;fill:#fff}.dc-gb .hs{font-family:Menlo,Consolas,monospace;font-size:10.5px;fill:#d6e6ea}.dc-gb .gh{font-family:Menlo,Consolas,monospace;font-size:11.5px;font-weight:700;fill:#fff}.dc-gb .tt{font-size:17px;font-weight:700;fill:#003478}.dc-gb .st{font-size:12.5px;fill:#666;font-style:italic}.dc-gb .c{font-size:13.5px}.dc-gb .cb{font-size:14px;font-weight:700}</style><text class="tt" x="16" y="28">1 · orders</text><text class="st" x="16" y="46">one row per order · 7 rows</text><rect x="16" y="58" width="92" height="30" fill="#003478"/><text class="h" x="26" y="78">order_id</text><rect x="108" y="58" width="116" height="30" fill="#003478"/><text class="h" x="118" y="78">customer_id</text><rect x="224" y="58" width="82" height="30" fill="#003478"/><text class="h" x="234" y="78">freight</text><rect x="16" y="88" width="290" height="27" fill="#fff"/><text class="m" x="98" y="106" text-anchor="end">10501</text><rect x="111" y="92" width="110" height="19" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="118" y="106">MAPLE</text><text class="m" x="296" y="106" text-anchor="end">12.40</text><rect x="16" y="115" width="290" height="27" fill="#f4f6f9"/><text class="m" x="98" y="133" text-anchor="end">10502</text><rect x="111" y="119" width="110" height="19" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="118" y="133">RIVER</text><text class="m" x="296" y="133" text-anchor="end">48.75</text><rect x="16" y="142" width="290" height="27" fill="#fff"/><text class="m" x="98" y="160" text-anchor="end">10503</text><rect x="111" y="146" width="110" height="19" rx="4" fill="#c9900c" fill-opacity="0.18" stroke="#c9900c" stroke-width="1.4"/><text class="m" x="118" y="160">SUNNY</text><text class="m" x="296" y="160" text-anchor="end">23.65</text><rect x="16" y="169" width="290" height="27" fill="#f4f6f9"/><text class="m" x="98" y="187" text-anchor="end">10504</text><rect x="111" y="173" width="110" height="19" rx="4" fill="#7b5ea7" fill-opacity="0.18" stroke="#7b5ea7" stroke-width="1.4"/><text class="m" x="118" y="187">ALPIN</text><text class="m" x="296" y="187" text-anchor="end">95.20</text><rect x="16" y="196" width="290" height="27" fill="#fff"/><text class="m" x="98" y="214" text-anchor="end">10505</text><rect x="111" y="200" width="110" height="19" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="118" y="214">MAPLE</text><text class="m" x="296" y="214" text-anchor="end">7.10</text><rect x="16" y="223" width="290" height="27" fill="#f4f6f9"/><text class="m" x="98" y="241" text-anchor="end">10506</text><rect x="111" y="227" width="110" height="19" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="118" y="241">RIVER</text><text class="m" x="296" y="241" text-anchor="end">30.00</text><rect x="16" y="250" width="290" height="27" fill="#fff"/><text class="m" x="98" y="268" text-anchor="end">10507</text><rect x="111" y="254" width="110" height="19" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="118" y="268">MAPLE</text><rect x="227" y="254" width="76" height="19" rx="4" fill="#eef0f4" stroke="#8a94a6" stroke-dasharray="3 3"/><text class="m null" x="234" y="268">NULL</text><rect x="16" y="58" width="290" height="219" fill="none" stroke="#b8c2d3"/><text class="tt" x="426" y="28">2 · GROUP BY customer_id</text><text class="st" x="426" y="46">rows sorted into buckets · still 7 rows</text><rect x="426" y="58" width="174" height="105" rx="5" fill="#fff" stroke="#0a8fb5" stroke-width="2"/><path d="M426,63 a5,5 0 0 1 5,-5 h164 a5,5 0 0 1 5,5 v19 h-174 z" fill="#0a8fb5"/><text class="gh" x="436" y="75">customer_id = MAPLE</text><text class="m" x="508" y="100" text-anchor="end">10501</text><text class="m" x="590" y="100" text-anchor="end">12.40</text><text class="m" x="508" y="127" text-anchor="end">10505</text><text class="m" x="590" y="127" text-anchor="end">7.10</text><text class="m" x="508" y="154" text-anchor="end">10507</text><rect x="521" y="140" width="76" height="19" rx="4" fill="#eef0f4" stroke="#8a94a6" stroke-dasharray="3 3"/><text class="m null" x="528" y="154">NULL</text><rect x="426" y="175" width="174" height="78" rx="5" fill="#fff" stroke="#e0604f" stroke-width="2"/><path d="M426,180 a5,5 0 0 1 5,-5 h164 a5,5 0 0 1 5,5 v19 h-174 z" fill="#e0604f"/><text class="gh" x="436" y="192">customer_id = RIVER</text><text class="m" x="508" y="217" text-anchor="end">10502</text><text class="m" x="590" y="217" text-anchor="end">48.75</text><text class="m" x="508" y="244" text-anchor="end">10506</text><text class="m" x="590" y="244" text-anchor="end">30.00</text><rect x="426" y="265" width="174" height="51" rx="5" fill="#fff" stroke="#c9900c" stroke-width="2"/><path d="M426,270 a5,5 0 0 1 5,-5 h164 a5,5 0 0 1 5,5 v19 h-174 z" fill="#c9900c"/><text class="gh" x="436" y="282">customer_id = SUNNY</text><text class="m" x="508" y="307" text-anchor="end">10503</text><text class="m" x="590" y="307" text-anchor="end">23.65</text><rect x="426" y="328" width="174" height="51" rx="5" fill="#fff" stroke="#7b5ea7" stroke-width="2"/><path d="M426,333 a5,5 0 0 1 5,-5 h164 a5,5 0 0 1 5,5 v19 h-174 z" fill="#7b5ea7"/><text class="gh" x="436" y="345">customer_id = ALPIN</text><text class="m" x="508" y="370" text-anchor="end">10504</text><text class="m" x="590" y="370" text-anchor="end">95.20</text><path d="M306,101.5 C366.0,101.5 366.0,95.5 426,95.5" fill="none" stroke="#0a8fb5" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,128.5 C366.0,128.5 366.0,212.5 426,212.5" fill="none" stroke="#e0604f" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,155.5 C366.0,155.5 366.0,302.5 426,302.5" fill="none" stroke="#c9900c" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,182.5 C366.0,182.5 366.0,365.5 426,365.5" fill="none" stroke="#7b5ea7" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,209.5 C366.0,209.5 366.0,122.5 426,122.5" fill="none" stroke="#0a8fb5" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,236.5 C366.0,236.5 366.0,239.5 426,239.5" fill="none" stroke="#e0604f" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,263.5 C366.0,263.5 366.0,149.5 426,149.5" fill="none" stroke="#0a8fb5" stroke-width="1.8" stroke-opacity="0.85"/><text class="tt" x="720" y="28">3 · aggregate each group</text><text class="st" x="720" y="46">one row per customer · 4 rows</text><rect x="720" y="98" width="116" height="42" fill="#003478"/><text class="h" x="730" y="116">customer_id</text><text class="hs" x="730" y="132">group key</text><rect x="836" y="98" width="96" height="42" fill="#1d6f7a"/><text class="h" x="846" y="116">n_orders</text><text class="hs" x="846" y="132">COUNT(*)</text><rect x="932" y="98" width="126" height="42" fill="#1d6f7a"/><text class="h" x="942" y="116">n_freight</text><text class="hs" x="942" y="132">COUNT(freight)</text><rect x="1058" y="98" width="132" height="42" fill="#1d6f7a"/><text class="h" x="1068" y="116">total_freight</text><text class="hs" x="1068" y="132">SUM(freight)</text><rect x="720" y="140" width="470" height="27" fill="#fff"/><rect x="723" y="144" width="110" height="19" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="730" y="158">MAPLE</text><text class="m" x="922" y="158" text-anchor="end">3</text><text class="m" x="1048" y="158" text-anchor="end">2</text><text class="m" x="1180" y="158" text-anchor="end">19.50</text><rect x="720" y="167" width="470" height="27" fill="#f4f6f9"/><rect x="723" y="171" width="110" height="19" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="730" y="185">RIVER</text><text class="m" x="922" y="185" text-anchor="end">2</text><text class="m" x="1048" y="185" text-anchor="end">2</text><text class="m" x="1180" y="185" text-anchor="end">78.75</text><rect x="720" y="194" width="470" height="27" fill="#fff"/><rect x="723" y="198" width="110" height="19" rx="4" fill="#c9900c" fill-opacity="0.18" stroke="#c9900c" stroke-width="1.4"/><text class="m" x="730" y="212">SUNNY</text><text class="m" x="922" y="212" text-anchor="end">1</text><text class="m" x="1048" y="212" text-anchor="end">1</text><text class="m" x="1180" y="212" text-anchor="end">23.65</text><rect x="720" y="221" width="470" height="27" fill="#f4f6f9"/><rect x="723" y="225" width="110" height="19" rx="4" fill="#7b5ea7" fill-opacity="0.18" stroke="#7b5ea7" stroke-width="1.4"/><text class="m" x="730" y="239">ALPIN</text><text class="m" x="922" y="239" text-anchor="end">1</text><text class="m" x="1048" y="239" text-anchor="end">1</text><text class="m" x="1180" y="239" text-anchor="end">95.20</text><rect x="720" y="98" width="470" height="150" fill="none" stroke="#b8c2d3"/><rect x="838" y="142" width="218" height="23" rx="4" fill="none" stroke="#CC0000" stroke-width="1.8"/><path d="M600,110.5 C660.0,110.5 660.0,153.5 714,153.5" fill="none" stroke="#0a8fb5" stroke-width="2.2" marker-end="url(#arr-gb-MAPLE)"/><defs><marker id="arr-gb-MAPLE" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#0a8fb5"/></marker></defs><path d="M600,214.0 C660.0,214.0 660.0,180.5 714,180.5" fill="none" stroke="#e0604f" stroke-width="2.2" marker-end="url(#arr-gb-RIVER)"/><defs><marker id="arr-gb-RIVER" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#e0604f"/></marker></defs><path d="M600,290.5 C660.0,290.5 660.0,207.5 714,207.5" fill="none" stroke="#c9900c" stroke-width="2.2" marker-end="url(#arr-gb-SUNNY)"/><defs><marker id="arr-gb-SUNNY" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#c9900c"/></marker></defs><path d="M600,353.5 C660.0,353.5 660.0,234.5 714,234.5" fill="none" stroke="#7b5ea7" stroke-width="2.2" marker-end="url(#arr-gb-ALPIN)"/><defs><marker id="arr-gb-ALPIN" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#7b5ea7"/></marker></defs><rect x="720" y="274" width="4" height="36" fill="#CC0000"/><text class="cb" x="734" y="288" style="fill:#CC0000">MAPLE: 3 orders, but only 2 known freight values</text><text class="c" x="734" y="307">COUNT(*) counts rows; COUNT(freight) and SUM(freight) skip NULL.</text><rect x="720" y="326" width="4" height="36" fill="#003478"/><text class="cb" x="734" y="340" style="fill:#003478">The grain changes: 7 orders → 4 customers</text><text class="c" x="734" y="359">Individual orders are gone; only the key and the summaries remain.</text><rect x="720" y="378" width="4" height="36" fill="#1d6f7a"/><text class="cb" x="734" y="392" style="fill:#1d6f7a">Every output column is the key or an aggregate</text><text class="c" x="734" y="411">order_id is not in the result: which of MAPLE's three would it be?</text></svg>

{{% note %}}
Two new orders arrived since the orders slide: a second one for RIVER and a third for MAPLE whose freight isn't known yet. Step 2 is GROUP BY on its own: nothing is removed, the seven rows are just sorted into one bucket per customer. Step 3 is the aggregation: each bucket becomes exactly one row, and every column is either the group key or a summary of the bucket. Point at MAPLE: COUNT(*) says 3 because there are three rows, COUNT(freight) says 2 because one freight is NULL, and SUM(freight) adds only the two known values. The NULL is skipped, not treated as zero. Ask: why can't order_id be in the result? MAPLE has three of them, and a group row can only hold one value per column.
{{% /note %}}

***

<!-- 09c: GROUP BY and aggregate in code: SQL and pandas -->
<p class="dc-kicker">Group and aggregate in code</p>

## GROUP BY ↔ `groupby().agg()`

<div class="dc-cols"><h4>SQL</h4><h4>pandas</h4></div>
<p class="dc-ex">Several summaries per customer, largest total first</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT customer_id,
       COUNT(*)       AS n_orders,
       COUNT(freight) AS n_freight,
       SUM(freight)   AS total_freight
FROM orders
GROUP BY customer_id
ORDER BY total_freight DESC;
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
(orders
 .groupby("customer_id", as_index=False)
 .agg(n_orders=("order_id", "size"),
      n_freight=("freight", "count"),
      total_freight=("freight", "sum"))
 .sort_values("total_freight", ascending=False))
{{< /highlight >}}
</div>
</div>
<p class="dc-ex">Filter groups after aggregating: HAVING</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT customer_id, COUNT(*) AS n_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 2;         -- MAPLE, RIVER
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
n = (orders.groupby("customer_id", as_index=False)
     .agg(n_orders=("order_id", "size")))
n.loc[n["n_orders"] >= 2]     # MAPLE, RIVER
{{< /highlight >}}
</div>
</div>
<p class="dc-ex">Filter rows before grouping: WHERE</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT customer_id, SUM(freight) AS total
FROM orders
WHERE order_date >= '2026-03-03'
GROUP BY customer_id;
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
(orders.loc[orders["order_date"] >= "2026-03-03"]
 .groupby("customer_id", as_index=False)
 .agg(total=("freight", "sum")))
{{< /highlight >}}
</div>
</div>

<p class="dc-small"><code>COUNT(*)</code> / <code>"size"</code> count rows; <code>COUNT(col)</code> / <code>"count"</code> skip NULL. <code>WHERE</code> filters rows <b>before</b> grouping, <code>HAVING</code> filters groups <b>after</b>.</p>

{{% note %}}
The first example is the diagram as code: it produces exactly the table from the previous slide, sorted by total. In pandas, agg takes one argument per output column: new_name=(input column, function). "size" counts rows like COUNT(*), "count" counts non-missing values like COUNT(freight). as_index=False keeps customer_id as a normal column, so the result looks like the SQL table. The second and third examples are the classic WHERE-versus-HAVING question. HAVING can use an aggregate because it runs after grouping; WHERE can't, because the groups don't exist yet. pandas has no HAVING keyword: aggregate first, then filter the aggregated table with a normal mask. One difference to mention: for a group whose values are all NULL, SQL SUM returns NULL but pandas sum returns 0 unless you use sum(min_count=1). Also, neither tool promises a particular group order unless you sort: pandas happens to sort the keys, SQL gives no guarantee.
{{% /note %}}

***

<!-- 10: The Dilemma: Seeing the forest and the trees. -->
{{< slide content-image="/imgs/shaping-data/shaping-data10.png" >}}
<h1></h1>

{{% note %}}
Aggregating gives the totals but loses the details. Filtering and sorting keep the details but give no totals. What if the question needs both, like "each order next to that customer's average"? Ask the class how they would do it with what we have so far (answer: aggregate, then join back).
{{% /note %}}

***

<!-- 11: WINDOWING: Calculate across groups, retain every row. -->
{{< slide content-image="/imgs/shaping-data/shaping-data11.png" >}}
<h1></h1>

{{% note %}}
A window function computes over related rows but keeps every row and adds the result as a new column. SQL: AVG(amount) OVER (PARTITION BY customer_id). pandas: groupby(...).transform("mean"). Ranks, running totals, and previous-row values (LAG / shift) work the same way.
{{% /note %}}

***

<!-- 11b: WINDOWING, step by step -->
<h2>WINDOW functions, step by step</h2>
<svg class="dc-win" style="width:100%;height:auto;margin-top:4px" viewBox="0 0 1256 475" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Window functions: seven orders are partitioned by customer_id; within each window SUM(freight) and ROW_NUMBER ordered by order_id are computed; the result keeps all seven rows and adds customer_total and order_no"><style>.dc-win text{font-family:"Source Sans Pro",Helvetica,Arial,sans-serif;fill:#222}.dc-win .m{font-family:Menlo,Consolas,monospace;font-size:12.5px}.dc-win .sb{font-weight:700;fill:#2e7d32}.dc-win .nb{font-weight:700;fill:#2e7d32;font-size:12px}.dc-win .null{fill:#8a94a6;font-style:italic}.dc-win .h{font-family:Menlo,Consolas,monospace;font-size:12.5px;font-weight:700;fill:#fff}.dc-win .hs{font-family:Menlo,Consolas,monospace;font-size:10.5px;fill:#dcefdc}.dc-win .gh{font-family:Menlo,Consolas,monospace;font-size:11.5px;font-weight:700;fill:#fff}.dc-win .fs{font-size:12px;font-weight:700}.dc-win .tt{font-size:17px;font-weight:700;fill:#003478}.dc-win .st{font-size:12.5px;fill:#666;font-style:italic}.dc-win .c{font-size:13.5px}.dc-win .cb{font-size:14px;font-weight:700}</style><text class="tt" x="16" y="28">1 · orders</text><text class="st" x="16" y="46">one row per order · 7 rows</text><rect x="16" y="58" width="92" height="30" fill="#003478"/><text class="h" x="26" y="78">order_id</text><rect x="108" y="58" width="116" height="30" fill="#003478"/><text class="h" x="118" y="78">customer_id</text><rect x="224" y="58" width="82" height="30" fill="#003478"/><text class="h" x="234" y="78">freight</text><rect x="16" y="88" width="290" height="27" fill="#fff"/><text class="m" x="98" y="106" text-anchor="end">10501</text><rect x="111" y="92" width="110" height="19" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="118" y="106">MAPLE</text><text class="m" x="296" y="106" text-anchor="end">12.40</text><rect x="16" y="115" width="290" height="27" fill="#f4f6f9"/><text class="m" x="98" y="133" text-anchor="end">10502</text><rect x="111" y="119" width="110" height="19" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="118" y="133">RIVER</text><text class="m" x="296" y="133" text-anchor="end">48.75</text><rect x="16" y="142" width="290" height="27" fill="#fff"/><text class="m" x="98" y="160" text-anchor="end">10503</text><rect x="111" y="146" width="110" height="19" rx="4" fill="#c9900c" fill-opacity="0.18" stroke="#c9900c" stroke-width="1.4"/><text class="m" x="118" y="160">SUNNY</text><text class="m" x="296" y="160" text-anchor="end">23.65</text><rect x="16" y="169" width="290" height="27" fill="#f4f6f9"/><text class="m" x="98" y="187" text-anchor="end">10504</text><rect x="111" y="173" width="110" height="19" rx="4" fill="#7b5ea7" fill-opacity="0.18" stroke="#7b5ea7" stroke-width="1.4"/><text class="m" x="118" y="187">ALPIN</text><text class="m" x="296" y="187" text-anchor="end">95.20</text><rect x="16" y="196" width="290" height="27" fill="#fff"/><text class="m" x="98" y="214" text-anchor="end">10505</text><rect x="111" y="200" width="110" height="19" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="118" y="214">MAPLE</text><text class="m" x="296" y="214" text-anchor="end">7.10</text><rect x="16" y="223" width="290" height="27" fill="#f4f6f9"/><text class="m" x="98" y="241" text-anchor="end">10506</text><rect x="111" y="227" width="110" height="19" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="118" y="241">RIVER</text><text class="m" x="296" y="241" text-anchor="end">30.00</text><rect x="16" y="250" width="290" height="27" fill="#fff"/><text class="m" x="98" y="268" text-anchor="end">10507</text><rect x="111" y="254" width="110" height="19" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="118" y="268">MAPLE</text><rect x="227" y="254" width="76" height="19" rx="4" fill="#eef0f4" stroke="#8a94a6" stroke-dasharray="3 3"/><text class="m null" x="234" y="268">NULL</text><rect x="16" y="58" width="290" height="219" fill="none" stroke="#b8c2d3"/><text class="tt" x="406" y="28">2 · PARTITION BY customer_id</text><text class="st" x="406" y="46">each row sees its window · ORDER BY order_id</text><rect x="406" y="58" width="206" height="127" rx="5" fill="#fff" stroke="#0a8fb5" stroke-width="2"/><path d="M406,63 a5,5 0 0 1 5,-5 h196 a5,5 0 0 1 5,5 v19 h-206 z" fill="#0a8fb5"/><text class="gh" x="416" y="75">window: MAPLE</text><text class="gh" x="604" y="75" text-anchor="end">#</text><text class="m" x="480" y="100" text-anchor="end">10501</text><text class="m" x="558" y="100" text-anchor="end">12.40</text><circle cx="590.0" cy="95.5" r="10" fill="#2e7d32" fill-opacity="0.14" stroke="#2e7d32"/><text class="m nb" x="590.0" y="100" text-anchor="middle">1</text><text class="m" x="480" y="127" text-anchor="end">10505</text><text class="m" x="558" y="127" text-anchor="end">7.10</text><circle cx="590.0" cy="122.5" r="10" fill="#2e7d32" fill-opacity="0.14" stroke="#2e7d32"/><text class="m nb" x="590.0" y="127" text-anchor="middle">2</text><text class="m" x="480" y="154" text-anchor="end">10507</text><rect x="493" y="140" width="72" height="19" rx="4" fill="#eef0f4" stroke="#8a94a6" stroke-dasharray="3 3"/><text class="m null" x="500" y="154">NULL</text><circle cx="590.0" cy="149.5" r="10" fill="#2e7d32" fill-opacity="0.14" stroke="#2e7d32"/><text class="m nb" x="590.0" y="154" text-anchor="middle">3</text><line x1="412" y1="163" x2="606" y2="163" stroke="#0a8fb5" stroke-dasharray="3 3"/><text class="fs" x="416" y="179" style="fill:#2e7d32">SUM(freight) =</text><text class="m sb" x="558" y="179" text-anchor="end">19.50</text><rect x="406" y="195" width="206" height="100" rx="5" fill="#fff" stroke="#e0604f" stroke-width="2"/><path d="M406,200 a5,5 0 0 1 5,-5 h196 a5,5 0 0 1 5,5 v19 h-206 z" fill="#e0604f"/><text class="gh" x="416" y="212">window: RIVER</text><text class="gh" x="604" y="212" text-anchor="end">#</text><text class="m" x="480" y="237" text-anchor="end">10502</text><text class="m" x="558" y="237" text-anchor="end">48.75</text><circle cx="590.0" cy="232.5" r="10" fill="#2e7d32" fill-opacity="0.14" stroke="#2e7d32"/><text class="m nb" x="590.0" y="237" text-anchor="middle">1</text><text class="m" x="480" y="264" text-anchor="end">10506</text><text class="m" x="558" y="264" text-anchor="end">30.00</text><circle cx="590.0" cy="259.5" r="10" fill="#2e7d32" fill-opacity="0.14" stroke="#2e7d32"/><text class="m nb" x="590.0" y="264" text-anchor="middle">2</text><line x1="412" y1="273" x2="606" y2="273" stroke="#e0604f" stroke-dasharray="3 3"/><text class="fs" x="416" y="289" style="fill:#2e7d32">SUM(freight) =</text><text class="m sb" x="558" y="289" text-anchor="end">78.75</text><rect x="406" y="305" width="206" height="73" rx="5" fill="#fff" stroke="#c9900c" stroke-width="2"/><path d="M406,310 a5,5 0 0 1 5,-5 h196 a5,5 0 0 1 5,5 v19 h-206 z" fill="#c9900c"/><text class="gh" x="416" y="322">window: SUNNY</text><text class="gh" x="604" y="322" text-anchor="end">#</text><text class="m" x="480" y="347" text-anchor="end">10503</text><text class="m" x="558" y="347" text-anchor="end">23.65</text><circle cx="590.0" cy="342.5" r="10" fill="#2e7d32" fill-opacity="0.14" stroke="#2e7d32"/><text class="m nb" x="590.0" y="347" text-anchor="middle">1</text><line x1="412" y1="356" x2="606" y2="356" stroke="#c9900c" stroke-dasharray="3 3"/><text class="fs" x="416" y="372" style="fill:#2e7d32">SUM(freight) =</text><text class="m sb" x="558" y="372" text-anchor="end">23.65</text><rect x="406" y="388" width="206" height="73" rx="5" fill="#fff" stroke="#7b5ea7" stroke-width="2"/><path d="M406,393 a5,5 0 0 1 5,-5 h196 a5,5 0 0 1 5,5 v19 h-206 z" fill="#7b5ea7"/><text class="gh" x="416" y="405">window: ALPIN</text><text class="gh" x="604" y="405" text-anchor="end">#</text><text class="m" x="480" y="430" text-anchor="end">10504</text><text class="m" x="558" y="430" text-anchor="end">95.20</text><circle cx="590.0" cy="425.5" r="10" fill="#2e7d32" fill-opacity="0.14" stroke="#2e7d32"/><text class="m nb" x="590.0" y="430" text-anchor="middle">1</text><line x1="412" y1="439" x2="606" y2="439" stroke="#7b5ea7" stroke-dasharray="3 3"/><text class="fs" x="416" y="455" style="fill:#2e7d32">SUM(freight) =</text><text class="m sb" x="558" y="455" text-anchor="end">95.20</text><path d="M306,101.5 C356.0,101.5 356.0,95.5 406,95.5" fill="none" stroke="#0a8fb5" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,128.5 C356.0,128.5 356.0,232.5 406,232.5" fill="none" stroke="#e0604f" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,155.5 C356.0,155.5 356.0,342.5 406,342.5" fill="none" stroke="#c9900c" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,182.5 C356.0,182.5 356.0,425.5 406,425.5" fill="none" stroke="#7b5ea7" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,209.5 C356.0,209.5 356.0,122.5 406,122.5" fill="none" stroke="#0a8fb5" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,236.5 C356.0,236.5 356.0,259.5 406,259.5" fill="none" stroke="#e0604f" stroke-width="1.8" stroke-opacity="0.85"/><path d="M306,263.5 C356.0,263.5 356.0,149.5 406,149.5" fill="none" stroke="#0a8fb5" stroke-width="1.8" stroke-opacity="0.85"/><text class="tt" x="712" y="28">3 · result</text><text class="st" x="712" y="46">still one row per order · 7 rows, 2 new columns</text><rect x="712" y="58" width="92" height="42" fill="#003478"/><text class="h" x="722" y="84">order_id</text><rect x="804" y="58" width="116" height="42" fill="#003478"/><text class="h" x="814" y="84">customer_id</text><rect x="920" y="58" width="82" height="42" fill="#003478"/><text class="h" x="930" y="84">freight</text><rect x="1002" y="58" width="132" height="42" fill="#2e7d32"/><text class="h" x="1012" y="76">customer_total</text><text class="hs" x="1012" y="92">SUM() OVER</text><rect x="1134" y="58" width="110" height="42" fill="#2e7d32"/><text class="h" x="1144" y="76">order_no</text><text class="hs" x="1144" y="92">ROW_NUMBER()</text><rect x="712" y="100" width="532" height="27" fill="#fff"/><rect x="1002" y="100" width="242" height="27" fill="#2e7d32" fill-opacity="0.07"/><text class="m" x="794" y="118" text-anchor="end">10501</text><rect x="807" y="104" width="110" height="19" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="814" y="118">MAPLE</text><text class="m" x="992" y="118" text-anchor="end">12.40</text><text class="m sb" x="1124" y="118" text-anchor="end">19.50</text><text class="m sb" x="1234" y="118" text-anchor="end">1</text><rect x="712" y="127" width="532" height="27" fill="#f4f6f9"/><rect x="1002" y="127" width="242" height="27" fill="#2e7d32" fill-opacity="0.07"/><text class="m" x="794" y="145" text-anchor="end">10502</text><rect x="807" y="131" width="110" height="19" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="814" y="145">RIVER</text><text class="m" x="992" y="145" text-anchor="end">48.75</text><text class="m sb" x="1124" y="145" text-anchor="end">78.75</text><text class="m sb" x="1234" y="145" text-anchor="end">1</text><rect x="712" y="154" width="532" height="27" fill="#fff"/><rect x="1002" y="154" width="242" height="27" fill="#2e7d32" fill-opacity="0.07"/><text class="m" x="794" y="172" text-anchor="end">10503</text><rect x="807" y="158" width="110" height="19" rx="4" fill="#c9900c" fill-opacity="0.18" stroke="#c9900c" stroke-width="1.4"/><text class="m" x="814" y="172">SUNNY</text><text class="m" x="992" y="172" text-anchor="end">23.65</text><text class="m sb" x="1124" y="172" text-anchor="end">23.65</text><text class="m sb" x="1234" y="172" text-anchor="end">1</text><rect x="712" y="181" width="532" height="27" fill="#f4f6f9"/><rect x="1002" y="181" width="242" height="27" fill="#2e7d32" fill-opacity="0.07"/><text class="m" x="794" y="199" text-anchor="end">10504</text><rect x="807" y="185" width="110" height="19" rx="4" fill="#7b5ea7" fill-opacity="0.18" stroke="#7b5ea7" stroke-width="1.4"/><text class="m" x="814" y="199">ALPIN</text><text class="m" x="992" y="199" text-anchor="end">95.20</text><text class="m sb" x="1124" y="199" text-anchor="end">95.20</text><text class="m sb" x="1234" y="199" text-anchor="end">1</text><rect x="712" y="208" width="532" height="27" fill="#fff"/><rect x="1002" y="208" width="242" height="27" fill="#2e7d32" fill-opacity="0.07"/><text class="m" x="794" y="226" text-anchor="end">10505</text><rect x="807" y="212" width="110" height="19" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="814" y="226">MAPLE</text><text class="m" x="992" y="226" text-anchor="end">7.10</text><text class="m sb" x="1124" y="226" text-anchor="end">19.50</text><text class="m sb" x="1234" y="226" text-anchor="end">2</text><rect x="712" y="235" width="532" height="27" fill="#f4f6f9"/><rect x="1002" y="235" width="242" height="27" fill="#2e7d32" fill-opacity="0.07"/><text class="m" x="794" y="253" text-anchor="end">10506</text><rect x="807" y="239" width="110" height="19" rx="4" fill="#e0604f" fill-opacity="0.18" stroke="#e0604f" stroke-width="1.4"/><text class="m" x="814" y="253">RIVER</text><text class="m" x="992" y="253" text-anchor="end">30.00</text><text class="m sb" x="1124" y="253" text-anchor="end">78.75</text><text class="m sb" x="1234" y="253" text-anchor="end">2</text><rect x="712" y="262" width="532" height="27" fill="#fff"/><rect x="1002" y="262" width="242" height="27" fill="#2e7d32" fill-opacity="0.07"/><text class="m" x="794" y="280" text-anchor="end">10507</text><rect x="807" y="266" width="110" height="19" rx="4" fill="#0a8fb5" fill-opacity="0.18" stroke="#0a8fb5" stroke-width="1.4"/><text class="m" x="814" y="280">MAPLE</text><rect x="923" y="266" width="76" height="19" rx="4" fill="#eef0f4" stroke="#8a94a6" stroke-dasharray="3 3"/><text class="m null" x="930" y="280">NULL</text><text class="m sb" x="1124" y="280" text-anchor="end">19.50</text><text class="m sb" x="1234" y="280" text-anchor="end">3</text><rect x="712" y="58" width="532" height="231" fill="none" stroke="#b8c2d3"/><rect x="1004" y="102.0" width="128" height="23" rx="4" fill="none" stroke="#0a8fb5" stroke-width="1.6" stroke-dasharray="4 3"/><rect x="1004" y="210.0" width="128" height="23" rx="4" fill="none" stroke="#0a8fb5" stroke-width="1.6" stroke-dasharray="4 3"/><rect x="1004" y="264.0" width="128" height="23" rx="4" fill="none" stroke="#0a8fb5" stroke-width="1.6" stroke-dasharray="4 3"/><path d="M612,95.5 C662.0,95.5 662.0,113.5 712,113.5" fill="none" stroke="#0a8fb5" stroke-width="1.8" stroke-opacity="0.85"/><path d="M612,232.5 C662.0,232.5 662.0,140.5 712,140.5" fill="none" stroke="#e0604f" stroke-width="1.8" stroke-opacity="0.85"/><path d="M612,342.5 C662.0,342.5 662.0,167.5 712,167.5" fill="none" stroke="#c9900c" stroke-width="1.8" stroke-opacity="0.85"/><path d="M612,425.5 C662.0,425.5 662.0,194.5 712,194.5" fill="none" stroke="#7b5ea7" stroke-width="1.8" stroke-opacity="0.85"/><path d="M612,122.5 C662.0,122.5 662.0,221.5 712,221.5" fill="none" stroke="#0a8fb5" stroke-width="1.8" stroke-opacity="0.85"/><path d="M612,259.5 C662.0,259.5 662.0,248.5 712,248.5" fill="none" stroke="#e0604f" stroke-width="1.8" stroke-opacity="0.85"/><path d="M612,149.5 C662.0,149.5 662.0,275.5 712,275.5" fill="none" stroke="#0a8fb5" stroke-width="1.8" stroke-opacity="0.85"/><rect x="712" y="313" width="4" height="36" fill="#2e7d32"/><text class="cb" x="726" y="327" style="fill:#2e7d32">Height unchanged, width grows</text><text class="c" x="726" y="346">7 rows in, 7 rows out; the window results become new columns.</text><rect x="712" y="363" width="4" height="36" fill="#0a8fb5"/><text class="cb" x="726" y="377" style="fill:#0a8fb5">The group value is repeated on every row of the group</text><text class="c" x="726" y="396">All three MAPLE orders show 19.50, including 10507 whose freight is NULL.</text><rect x="712" y="413" width="4" height="36" fill="#003478"/><text class="cb" x="726" y="427" style="fill:#003478">Compare GROUP BY: same numbers, but the orders are kept</text><text class="c" x="726" y="446">Now you can ask “what share of the customer’s total is this order?”</text></svg>

{{% note %}}
Same seven orders and the same buckets as the GROUP BY slide, but look at the lines on the right: seven go out, one per order, instead of four. PARTITION BY says which rows belong together, like GROUP BY, but nothing is collapsed. Each row looks at its own window, and the result is written back onto that row. SUM(freight) OVER the MAPLE window is 19.50, and all three MAPLE rows get it, even 10507, whose own freight is unknown. ROW_NUMBER needs an order inside the window, here order_id, and numbers the rows 1, 2, 3 within each customer. This answers the dilemma from two slides ago: each individual order next to its customer's total. From there, freight / customer_total is each order's share.
{{% /note %}}

***

<!-- 11c: WINDOWING in code: SQL and pandas -->
<p class="dc-kicker">Windows in code</p>

## WINDOW: `OVER (…)` ↔ `transform()`

<div class="dc-cols"><h4>SQL</h4><h4>pandas</h4></div>
<p class="dc-ex">The customer's total next to every order</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT order_id, customer_id, freight,
       SUM(freight) OVER (PARTITION BY customer_id)
           AS customer_total
FROM orders;                       -- still 7 rows
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
orders["customer_total"] = (orders
    .groupby("customer_id")["freight"]
    .transform("sum"))             # still 7 rows
{{< /highlight >}}
</div>
</div>
<p class="dc-ex">Number the orders within each customer</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT order_id, customer_id,
       ROW_NUMBER() OVER (PARTITION BY customer_id
           ORDER BY order_id) AS order_no
FROM orders;
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
orders = orders.sort_values(["customer_id", "order_id"])
orders["order_no"] = (orders
    .groupby("customer_id").cumcount() + 1)
{{< /highlight >}}
</div>
</div>
<p class="dc-ex">The previous order's freight, per customer (sorted as above)</p>
<div class="dc-cols">
<div>
{{< highlight sql >}}
SELECT order_id, customer_id, freight,
       LAG(freight) OVER (PARTITION BY customer_id
           ORDER BY order_id) AS prev_freight
FROM orders;
{{< /highlight >}}
</div>
<div>
{{< highlight python >}}
orders["prev_freight"] = (orders
    .groupby("customer_id")["freight"]
    .shift(1))                     # first row: NaN
{{< /highlight >}}
</div>
</div>

<p class="dc-small"><code>PARTITION BY</code> = which rows belong together; <code>ORDER BY</code> inside <code>OVER</code> = their sequence. The row count never changes. In pandas: <code>transform</code> for group values; sort first, then <code>cumcount</code>, <code>shift</code>, <code>cumsum</code>.</p>

{{% note %}}
Compare with the GROUP BY code slide: the SQL is almost the same aggregate, SUM(freight), but OVER (PARTITION BY ...) replaces GROUP BY, and the result keeps all rows. In pandas the difference is one word: .agg() returns one row per group, .transform() returns one value per original row, lined up with the original index, so it can be assigned as a new column. The second and third examples need an order inside each window. SQL puts it in OVER (... ORDER BY ...). pandas has no such clause, so we sort the table first; cumcount and shift then follow the current row order within each group. Forgetting to sort is the most common bug here. LAG returns NULL for the first row of each window, and shift returns NaN: there is no previous order. Mention that the final output order in SQL is still undefined unless the outer query has ORDER BY; the ORDER BY inside OVER only controls the calculation.
{{% /note %}}

***

<!-- 12: Summarization: Two Paths -->
{{< slide content-image="/imgs/shaping-data/shaping-data12.png" >}}
<h1></h1>

{{% note %}}
Side by side: GROUP BY destroys the grain, windowing preserves it. "Total sales per customer" means GROUP BY. "Every sale next to its customer's total" means a window. Before writing code, decide whether the answer should have one row per group or one row per original record.
{{% /note %}}

***

<!-- 13: The Conceptual Pipeline -->
{{< slide content-image="/imgs/shaping-data/shaping-data13.png" >}}
<h1></h1>

{{% note %}}
A full business question: total spending by active customers, highest first. Join customers and orders, filter to active, group and aggregate, sort. SQL is declarative: you state the result and the database plans the steps. In pandas you chain the same steps yourself. Same pipeline, different notation.
{{% /note %}}

***

<!-- 14: Data transformation is structural. -->
{{< slide content-image="/imgs/shaping-data/shaping-data14.png" >}}
<h1></h1>

{{% note %}}
The four moves: carve (filter and sort), connect (join), compress (aggregate), contextualize (window). For any operation, ask what one row is before and after, and how the height and width change. Next up are the notebooks, where we run each move in both SQL and pandas on Northwind.
{{% /note %}}
