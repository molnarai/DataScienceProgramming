---
date: 2026-11-11
classdates: '2026-11-11'
draft: false
title: 'Graphs and Shortest Path'
theoretical: "Graphs as a model of relationships: nodes, edges, directed and weighted variants. Adjacency representations and their tradeoffs. Breadth-first search and shortest-path intuition."
technical: "Represent a graph with dictionaries; implement neighbor traversal and BFS with a queue; reconstruct a path. In-class: work through a route-finding example."
weight: 120
numsession: 12
---
## Theory
Introduce the graph as a model for anything defined by relationships rather than by rows: road networks, social connections, dependencies, web links. Define nodes and edges, and distinguish undirected from directed edges and unweighted from weighted ones, since each distinction changes what a "shortest" path means. Compare adjacency representations — an edge list, an adjacency matrix, and an adjacency list built from a dictionary of neighbor lists — in terms of memory and the cost of asking who is adjacent to a given node. Develop breadth-first search as exploration in rings of increasing distance, and derive the key result intuitively: because BFS reaches nodes in order of hop count, the first time it reaches the target it has found a shortest path in an unweighted graph. Note where weights break that argument and where Dijkstra's idea picks up, without developing it formally.

## Technical
Build a graph in Python as a dictionary mapping each node to its neighbors, and write helper functions to add edges, list neighbors, and check adjacency. Implement breadth-first search with an explicit queue (`collections.deque`) and a visited set, and reason about what goes wrong without the visited set. Extend BFS to record a predecessor for each discovered node, then reconstruct the actual path by walking predecessors back from the target — the step that turns a traversal into a usable answer. Handle the cases that matter: unreachable targets, the start node itself, and a disconnected graph. In-class activity: students work through a route-finding example on a small map, tracing BFS by hand before running the code. Homework: build a small graph representation and solve a shortest-path problem.

