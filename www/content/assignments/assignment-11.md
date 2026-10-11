+++
date = '2026-11-11'
due_date = '2026-11-25T23:59:00'
draft = false
title = 'Homework 11: Fewest Hops'
weight = 110
status = 'Scheduled'
+++

You are in Atlanta and want to get to Sydney, and there is no direct flight. A booking site answers in a second; how did it find that among 37,041 routes between 3,257 airports? A table has rows, but this data has connections, and the question is about following them. Across seven test-driven phases you will read a file of airline routes into an edge list, build a graph as a dictionary of dictionaries, and find the fewest flights between any two airports with a search that spreads outward from the start one flight at a time. Then you will reconstruct the route itself, find which airports hang together at all, and discover that the route with the fewest flights from Atlanta to Sydney goes the wrong way round the planet, 9,066 km longer than another with just as many flights.

<!-- more -->


Related session: [Session 12 — Graphs and Shortest Path](../../topics/topic-12/)

### The Phases

| | |
|---|---|
| **1** | An edge list — reading the routes |
| **2** | An adjacency list — the graph |
| **3** | Asking the graph — neighbours, degree, hubs |
| **4** | Breadth-first search — hops to every reachable airport |
| **5** | The path itself — walking back from the target |
| **6** | What belongs together — reachability and connected components |
| **7** | Hops are not kilometres |

Breadth-first search explores in rings: everything one flight away before
anything two flights away, which is why the first distance it records is the
smallest. It counts flights and nothing else. *Shortest* depends on what you
measure, and the last phase puts the route with the fewest flights beside the
route with the fewest kilometres.

### Topics Covered

- Graphs as a model of connections: nodes, edges, directed and weighted
- Edge lists and adjacency lists, and what each is good for
- Representing a graph with dictionaries
- Breadth-first search with a queue
- Reconstructing a shortest path from the search's notes
- Reachability and connected components
- Fewest hops versus smallest total weight; a first look at Dijkstra's algorithm

### Instructions

The full instructions, the starter file, and the per-phase tests are released
through the course template after the November 11 session. Once they are
out, run `ifi8410-update` on the course server, then read
`Assignments/HW11/instructions/homework11_instructions.md` and work in
`Assignments/HW11/submission/`.

The real file is already on the cluster at `/data/public/openflights/routes.csv`
— do not copy it. A small network of 25 routes between 11 airports is in
`test/fixtures/routes.csv`; work with that one, and draw it. Use only the
standard library — no pandas, no numpy, and do not import networkx in your
submission: it is on the cluster but not in the pipeline. Hand in with
`ifi8410-test` and `ifi8410-submit`.
