# Session 12: Graphs and Shortest Path

A table describes things, one row each. Some questions are not about the
things but about what is between them: who knows whom, which page links to
which, what can be reached from where. The structure for that is a graph, and
this session is about building one and searching it.

1. **Nodes and edges.** A graph is a set of things and a set of connections
   between pairs of them; edges may have a direction and a weight.
2. **Writing a graph down.** An edge list is easy to store; an adjacency list
   is quick to ask.
3. **Breadth-first search.** Explore in rings: everything one step away, then
   two, then three.
4. **The path.** Remember where each node was reached from, and walk back.
5. **What belongs together.** Reachability, and the separate parts of a
   network.
6. **When edges have lengths.** Fewest steps is not shortest distance, and
   needs another search.

> **Run these on ARC, with the kernel set to Conda Python 3.12.** Notebook 02
> reads `four_letter_words.txt`, which is in this folder.

Nothing here repeats earlier sessions. Dictionaries and sets, and why a lookup
in them takes one step, are Sessions 3, 4 and 11.

## Notebooks

Rename a notebook before you edit it, so that the next course release does not
overwrite your work.

### `01_Things_and_Connections.ipynb` — the ideas

An overview of the six ideas on graphs small enough to draw. Eight people and
who knows whom introduce nodes, edges, neighbours, degree and paths; "who
follows whom" makes the edges directed. The same graph is written as an edge
list and as an adjacency list, and the most common bug of a first graph
program, a node missing because nothing leaves it, is shown before it can
bite. Breadth-first search is done by hand in rings and then with a queue,
followed step by step; taking from the wrong end of the queue gives wrong
distances around a table of six. Notes of where each node was reached from
turn distances into a path. Four towns and their roads show that the route
with the fewest roads is not the shortest in kilometres, Dijkstra's algorithm
is read side by side with breadth-first search, and networkx does all of it
in one line each.

Four exercises, and a table mapping each idea to a phase of Homework 11.

### `02_Word_Ladders_Example.ipynb` — one graph, built and explored

A worked example where nothing looks like a graph until you decide to see
one: Lewis Carroll's word ladders, COLD to WARM one letter at a time. Every
four-letter word is a node, and two words are joined when they differ in one
letter: 2,442 nodes and 10,575 edges. Comparing all pairs takes seconds;
filing every word under four patterns in a dictionary takes a hundredth of
one. The shortest ladder is the shortest path of notebook 01, unchanged. Most
words lie within six steps of "cold"; 81 have no neighbour at all; and a look
at the components turns up a cluster of Roman numerals that nobody asked
about. The two words farthest apart need seventeen steps, found by searching
from every word.

Five exercises on the same graph.

### `03_Graphs_Reference.ipynb` — a lookup guide

Meant to be searched, not read through, and to stay open during Homework 11.
Twelve sections with runnable examples on the eleven airports of the
homework's test network: the vocabulary; edge lists, adjacency lists and
matrices; building a graph with every node present; asking it; breadth-first
search and its three rules; a shortest path; reachability and components;
depth-first search and what it is for; weighted edges and Dijkstra with
`heapq`; the same operations in networkx; what each costs; and a table of
symptoms and causes.

## Homework

[Homework 11](../../Assignments/HW11/instructions/homework11_instructions.md)
has you write the searches of notebook 01 on a real network: 37,041 airline
routes between 3,257 airports. Atlanta to Sydney takes two flights either way,
and the route your search finds is 9,000 km longer than the best one. The
overlap with these notebooks is deliberate. networkx is used in the homework
notebook to check your answers and must not be imported in what you hand in.
