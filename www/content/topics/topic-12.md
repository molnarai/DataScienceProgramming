---
date: 2026-11-11
classdates: '2026-11-11'
draft: false
title: 'Graphs and Shortest Path'
concept: "Graphs as a model of relationships: nodes, edges, directed and weighted variants. Adjacency representations and their tradeoffs. Breadth-first search and shortest-path intuition."
practice: "Represent a graph with dictionaries; implement neighbor traversal and BFS with a queue; reconstruct a path. In-class: work through a route-finding example."
weight: 120
numsession: 12
---
A table describes things: one row per customer, per product, per airport. Some questions are not about the things at all but about what lies between them. How do I get from Atlanta to Sydney, and with how many changes? Which pages can be reached from the home page? If this road closes, is the town cut off? None of these is a filter, a join, or a group-by. They are questions about connections, and the structure for them is a **graph**: a set of **nodes** and a set of **edges** between pairs of them, where an edge may have a direction and may carry a weight. Often the hardest step is the first — recognising that a word puzzle, a course catalogue, and an airline timetable are the same problem. An edge list is the natural form for a file and a poor one to ask; an adjacency list, a dictionary mapping each node to its neighbours, puts every node's connections one lookup away, provided every node is a key.
<!--more-->
The basic operation is a search that spreads outward from a start. **Breadth-first search** works in rings: everything one step away, then everything new that is two steps away. A queue produces that order by itself, and because nearer rings finish first, the first time a node is reached is by a route with the fewest steps. Three details decide whether it works: take from the front of the queue, skip what has been seen, and record a node when it joins the queue. One "came from" note per node recovers the path itself; shortest paths are not unique, and all of them are correct. The nodes a search reaches form a **connected component**, and looking at the components is one of the first things to do with any real network. Finally, fewest steps is not shortest distance. When edges have lengths the search must take the nearest node next, which is Dijkstra's algorithm, and what "shortest" means becomes a modelling decision made by what is put on the edges.

TODO: marquee image

## Listen

TODO: podcast

## Presentation

TODO: presentation

## Read

- [Graphs and Shortest Path](../../blog/graphs-shortest-path/) (lecture notes)

## Hands-on

Notebooks in [12-Graphs-Shortest-Path](https://github.com/molnarai/DataScienceProgramming/tree/main/12-Graphs-Shortest-Path)

## Homework

- [Homework 11: Fewest Hops](../../assignments/assignment-11/) — due Wednesday, November 25, 2026
