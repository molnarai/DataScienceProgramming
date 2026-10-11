# Lecture Notes — Session 12: Graphs and Shortest Path

## 1. The problem

A table describes things: one row per customer, per product, per airport,
with their properties. Some questions are not about the things at all. They
are about what lies **between** them.

- How do I get from Atlanta to Sydney, and with how many changes?
- Which web pages can be reached from the home page?
- How many introductions separate two people who have never met?
- If this one road closes, is the town cut off?
- Which of these accounts belong to the same ring of connected accounts?

None of these is a filter, a join or a group-by. They are questions about
**connections**, and about **following** connections from one thing to the
next. The structure for that is a **graph**, and the basic operation is a
**search** that spreads outward from a starting point.

The problem space of this session:

- **representing** a network so that a program can follow its connections
  quickly;
- **reachability**: what can be reached from where, and which parts of a
  network hang together;
- **shortest paths**: the best route between two points, and the realisation
  that "shortest" has no meaning until you say what is being measured.

Often the hardest step is the first: recognising that a problem *is* a graph
problem. A word puzzle, a course catalogue and an airline timetable look
nothing alike and are solved by the same twenty lines.

## 2. Core concepts, and how Python realizes them

### The tools

| Tool | Purpose | What it gives you |
|---|---|---|
| **`dict`, `set`** | representing a graph | an adjacency list: each node mapped to its neighbours; neighbours and "is there an edge?" in one step |
| **`collections.deque`** (standard library) | a queue | add at one end, remove from the other, each in one step: the engine of breadth-first search |
| **`heapq`** (standard library) | a priority queue | always hands back the smallest item: the engine of shortest paths by distance |
| **networkx** | the graph library | graph objects; shortest paths with and without weights, components, hundreds of other algorithms; simple drawing |

The first three are enough to write every algorithm in this session by hand,
which is worth doing once. For real work, networkx is tested, fast and
complete.

### Concept 1 — Nodes and edges

A **graph** is two sets and nothing else:

| | Called | Example |
|---|---|---|
| the things | **nodes** (vertices) | people, airports, web pages, words |
| the connections between pairs of them | **edges** (links) | friendships, routes, hyperlinks |

Where a node is drawn means nothing. Only which nodes are joined matters.

Some vocabulary: a node's **neighbours** are the nodes one edge away; its
**degree** is the number of edges at it; a **path** is a sequence of nodes
each joined to the next; a path's length in edges is counted in **hops**.

Edges come in two variations:

- **Directed or undirected.** "Knows" goes both ways. "Follows", "links to"
  and "flies to" need not: an edge with a direction is an arrow, and whether a
  path exists then depends on the direction of travel.
- **Weighted or unweighted.** An edge can carry a number: a distance, a
  travel time, a cost.

### Concept 2 — Writing a graph down

An **edge list** is the natural form for a file: one connection per row.

```python
edges = [("Ana", "Ben"), ("Ana", "Chi"), ("Chi", "Dev")]
```

It is a poor form to ask. "Who are Dev's neighbours?" means reading every
edge, a linear search, and a search through a graph asks that question
constantly.

An **adjacency list** reorganises the edges so that each node's neighbours
are one lookup away:

```python
def build_graph(edges, directed=False):
    graph = {}
    for a, b in edges:
        graph.setdefault(a, set())
        graph.setdefault(b, set())      # b too, even if nothing leaves it
        graph[a].add(b)
        if not directed:
            graph[b].add(a)
    return graph
```

For a weighted graph, each node maps to a dictionary:
`graph["ATL"] = {"MIA": 950, "LAX": 3100}`.

The second `setdefault` guards against the most common bug in a first graph
program. In a directed graph a node may only ever appear as a *target*.
Without that line it never becomes a key, and the first function that reaches
it fails with a `KeyError`. **Every node must be a key**, with an empty
collection if nothing leaves it.

### Concept 3 — Breadth-first search

How many steps from one node to every other? Work outward in **rings**:
everything one step away, then everything new that is two steps away, and so
on. Because nearer rings are finished first, the first time a node is reached
is by a route with the fewest steps.

A **queue** produces that order by itself: nodes join at the back and are
taken from the front, so whoever was found first is expanded first.

```python
from collections import deque

def hop_distances(graph, start):
    hops = {start: 0}                    # found so far, and how far away
    queue = deque([start])
    while queue:
        node = queue.popleft()           # from the FRONT
        for neighbour in graph[node]:
            if neighbour not in hops:    # skip what has been seen
                hops[neighbour] = hops[node] + 1
                queue.append(neighbour)  # to the BACK
    return hops
```

Three details decide whether it works:

- **Take from the front.** Taking from the back sends the search down one
  route as far as it goes before trying another. That is a different search,
  *depth-first*, which reaches the same nodes with the wrong distances.
- **Skip what has been seen.** Otherwise any cycle traps the search for ever.
- **Record a node when it joins the queue**, not when it leaves, or it joins
  once for every edge that leads to it.

The cost is about one step per node plus one per edge: a single search costs
roughly as much as reading the graph once.

### Concept 4 — The path

Knowing that a destination is three steps away is not an itinerary. The
search already knows the route: every time it finds a new node, it finds it
*from* some other node. Record that one fact per node.

```python
came_from = {start: None}
...
        if neighbour not in came_from:
            came_from[neighbour] = node
            queue.append(neighbour)
```

Afterwards, start at the target and follow the notes back until the start,
whose note is `None`; then reverse the list.

**Shortest paths are not unique.** When several routes have the same number
of steps, the search returns whichever it met first, which depends on the
order it looks at neighbours. All of them are correct. To check a shortest
path, test that it is a real path and that its length is right, never that it
is one particular path.

### Concept 5 — Reachability and components

The set of nodes a search reaches from a start is what is **reachable** from
there. A network can fall into pieces. A **connected component** is one such
piece: nodes that can all reach each other, with no edge leading out.

```python
def components(graph):
    seen, parts = set(), []
    for node in graph:
        if node not in seen:
            part = set(hop_distances(graph, node))
            seen |= part
            parts.append(part)
    return parts
```

Looking at the components is one of the first things to do with any real
network. Typically there is one giant component with nearly everything in it
and a scatter of small ones, and the small ones are frequently either the
answer to the question or a sign of something odd in the data.

### Concept 6 — When edges have lengths

Four towns. The direct road from the first to the last is 90 km. A route
through two other towns uses three roads and totals 60 km. Breadth-first
search returns the direct road: it was asked for the fewest roads, and it
counts roads.

**Fewest steps is not shortest distance.** To find the shortest route by
distance, the search must take nodes in order of their **distance from the
start**, always the nearest unfinished one, in place of the order in which
they were found. That is **Dijkstra's algorithm**. The queue becomes a
priority queue (`heapq`), and a node's distance may be improved until the
node is finally taken out.

| | Breadth-first search | Dijkstra |
|---|---|---|
| question | fewest edges | smallest total weight |
| takes next | the oldest node in the queue | the nearest node |
| container | `deque` | `heapq` |
| needs | nothing | weights that are not negative |

With every weight equal to 1, the two give the same answer.

What "shortest" means is therefore a **modelling decision**, made by what is
put on the edges: 1 for fewest changes, kilometres for distance, minutes for
speed, the fare for cost.

### The library

```python
import networkx as nx

G = nx.Graph()                               # nx.DiGraph() for directed
G.add_weighted_edges_from(edges, weight="km")

nx.shortest_path(G, "Alba", "Dale")                 # fewest edges
nx.shortest_path(G, "Alba", "Dale", weight="km")    # shortest distance
nx.connected_components(G)
```

The same function gives two different routes depending on whether it is told
about the weights. Forgetting `weight=` is the usual mistake, and it produces
a plausible wrong answer.

## 3. Business use cases

**Introductions.** Eight people, some of whom know each other. Who can
introduce Ana to Fay, and through how many people? The path through the
friendship graph is the chain of introductions; two people in different
components cannot be introduced at all. Professional networking sites compute
exactly this when they label someone a "second-degree connection".

**Routing passengers.** An airline network has about 37,000 routes between
3,300 airports. There is no direct flight from Atlanta to Sydney. A search by
number of flights finds a two-flight route from Atlanta to Sydney, through
Dubai, that is 24,000 km long. Another two-flight route, through Los Angeles,
is 15,000 km. Both have the fewest flights. A booking system therefore has to
decide what it is minimising, and real ones weigh time, price and changes
together. The same network also shows hubs (a handful of airports with over
two hundred routes each), one-way routes, and small groups of airports cut
off from the rest.

**Delivery and road networks.** Towns and roads with their lengths. The
direct road is not always the shortest route. For a logistics company the
weight is driving time or fuel, and the shortest path changes with the time
of day. The components of a road network answer a different question: which
places become unreachable if a bridge is closed.

**A puzzle that is secretly a graph.** Change COLD into WARM one letter at a
time, every step a real word. Make each four-letter word a node and join two
words that differ in one letter: 2,400 nodes, 10,600 edges. The shortest
ladder is a shortest path (four steps). Most words are within five or six
steps of COLD, and the two words farthest apart are seventeen steps from each
other; 81 have no neighbour at all; and the second-largest component
turns out to be a cluster of Roman numerals that had found their way into the
word list. Nobody was looking for them. Examining the components of a network
is a remarkably effective way to find things in data that should not be
there, and the same idea is used to find rings of connected accounts in fraud
detection.

Building that graph raises a cost question too. Comparing every pair of words
grows with the square of their number. Filing each word under its four
"one letter blanked" patterns in a dictionary, and joining words that share a
pattern, does it in a hundredth of a second.

**Dependencies.** Courses and their prerequisites, tasks in a project,
software packages that require other packages: nodes with directed edges
meaning "must come before". Which courses can be taken first? What does
removing one package break? These are reachability questions.

## Key points

- A graph is things and connections. Say what a node is and what an edge
  means.
- Store edges in a file; ask an adjacency list. Every node must be a key.
- Breadth-first search: a queue, taken from the front, skipping what was
  seen. It finds the fewest steps.
- Keep a "came from" note per node to recover the path. Shortest paths are
  not unique.
- Look at the components before anything else.
- "Shortest" depends on what the edges carry. Decide before searching.
