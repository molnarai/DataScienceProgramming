+++
title = "Graphs and Shortest Path"
description = "Graphs as a model of connections: adjacency lists, breadth-first search, path reconstruction, connected components, and what 'shortest' means"
weight = 120
outputs = ["Reveal"]
math = false
thumbnail = "../imgs/slides/.png"

[reveal_hugo]
custom_theme = "css/reveal-robinson.css"
slide_number = true
transition = "none"

+++

<style>
  .reveal .slides section { box-sizing: border-box; }
  .reveal .dc-sub { color: #666; font-size: 0.9em; }
  .reveal .dc-kicker { color: #CC0000; font-size: 0.55em; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin: 0 0 4px 0; }
  .reveal .dc-small { font-size: 0.75em; }
  .reveal .dc-muted { color: #666; }
  .reveal .dc-quote { font-size: 0.85em; border-left: 5px solid #CC0000; background: #f4f6f9; padding: 12px 18px; text-align: left; margin: 18px 0; }

  /* Cards */
  .reveal .dc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px; }
  .reveal .dc-grid.three { grid-template-columns: 1fr 1fr 1fr; }
  .reveal .dc-card { background: #f4f6f9; border-left: 5px solid #003478; padding: 10px 14px; border-radius: 4px; }
  .reveal .dc-card h3 { margin: 0 0 4px 0; font-size: 0.85em; }
  .reveal .dc-card p { margin: 0; font-size: 0.62em; }
  .reveal .dc-card .dc-from { color: #666; font-size: 0.58em; margin-bottom: 6px; }
  .reveal .dc-card.red { border-left-color: #CC0000; }
  .reveal .dc-card.red h3 { color: #CC0000; }
  .reveal .dc-card.green { border-left-color: #2e7d32; }
  .reveal .dc-card.green h3 { color: #2e7d32; }

  /* Flow */
  .reveal .dc-flow { display: flex; align-items: center; justify-content: center; gap: 8px; margin: 20px 0; }
  .reveal .dc-node { background: #f4f6f9; border: 2px solid #003478; border-radius: 6px; padding: 10px 14px; font-size: 0.62em; text-align: center; }
  .reveal .dc-node.dark { background: #003478; color: #fff; }
  .reveal .dc-node .dc-owner { margin-top: 4px; font-size: 0.85em; font-style: italic; color: #CC0000; }
  .reveal .dc-node.dark .dc-owner { color: #cfd8e8; }
  .reveal .dc-arrow { color: #003478; font-size: 0.9em; font-weight: 700; }

  /* Two columns */
  .reveal .dc-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }
  .reveal .dc-cols h4 { font-size: 0.65em; margin: 6px 0 0 0; }
  .reveal .dc-cols h4.bad { color: #CC0000; }
  .reveal .dc-cols h4.good { color: #2e7d32; }

  /* Code */
  .reveal .highlight pre, .reveal pre { width: 100%; font-size: 0.5em; margin: 8px 0; }
  .reveal .dc-code-lg pre { font-size: 0.58em; }

  /* Bullets */
  .reveal .dc-points { margin-top: 8px; }
  .reveal .dc-points li { font-size: 0.72em; margin-bottom: 0.4em; }

  .reveal .dc-table { font-size: 0.58em; width: 100%; margin-top: 10px; }
  .reveal .dc-table td { vertical-align: top; }

  .reveal .dc-nb { font-size: 0.6em; }
  .reveal .dc-nb .num { display: inline-block; width: 1.6em; height: 1.6em; line-height: 1.6em; text-align: center; border-radius: 50%; background: #003478; color: #fff; font-weight: 700; margin-right: 6px; }
</style>

<p class="dc-kicker">IFI 8410 — Session 12: Graphs and Shortest Path</p>
<h1>Things and Connections</h1>
<p class="dc-sub">Questions about what lies between things</p>

{{% note %}}
A table describes things, one row each. Today the questions are not about the things at all.
{{% /note %}}

***

<p class="dc-kicker">The problem</p>

## Not a filter, a join, or a group-by

<ul class="dc-points">
  <li>How do I get from Atlanta to Sydney, and with how many changes?</li>
  <li>Which web pages can be reached from the home page?</li>
  <li>How many introductions separate two people who have never met?</li>
  <li>If this one road closes, is the town cut off?</li>
  <li>Which of these accounts belong to the same ring of connected accounts?</li>
</ul>

<div class="dc-grid three">
  <div class="dc-card"><h3>Representing</h3><p>a network so a program can follow its connections quickly.</p></div>
  <div class="dc-card"><h3>Reachability</h3><p>what can be reached from where, and which parts hang together.</p></div>
  <div class="dc-card"><h3>Shortest paths</h3><p>the best route, once you say what is being measured.</p></div>
</div>

{{% note %}}
Often the hardest step is the first: recognising that a problem is a graph problem. A word puzzle, a course catalogue and an airline timetable look nothing alike and are solved by the same twenty lines.
{{% /note %}}

***

<p class="dc-kicker">The tools</p>

## Three from the standard library, and one library

<div class="dc-grid">
  <div class="dc-card"><h3><code>dict</code>, <code>set</code></h3><p class="dc-from">representing a graph</p><p>An adjacency list: each node mapped to its neighbours. "Is there an edge?" in one step.</p></div>
  <div class="dc-card"><h3><code>collections.deque</code></h3><p class="dc-from">a queue</p><p>Add at one end, remove from the other, each in one step. The engine of breadth-first search.</p></div>
  <div class="dc-card"><h3><code>heapq</code></h3><p class="dc-from">a priority queue</p><p>Always hands back the smallest item. The engine of shortest paths by distance.</p></div>
  <div class="dc-card green"><h3>networkx</h3><p class="dc-from">the graph library</p><p>Graph objects, shortest paths with and without weights, components, hundreds of other algorithms.</p></div>
</div>

<p class="dc-small" style="margin-top: 18px;">The first three are enough to write every algorithm in this session by hand, which is worth doing once. For real work, networkx is tested, fast and complete.</p>

***

<p class="dc-kicker">Concept 1</p>

## Nodes and edges

<table class="dc-table">
  <thead><tr><th></th><th>Called</th><th>Example</th></tr></thead>
  <tbody>
    <tr><td>the things</td><td><b>nodes</b> (vertices)</td><td>people, airports, web pages, words</td></tr>
    <tr><td>the connections between pairs of them</td><td><b>edges</b> (links)</td><td>friendships, routes, hyperlinks</td></tr>
  </tbody>
</table>

<p class="dc-small">Where a node is drawn means nothing. Only which nodes are joined matters. <b>Neighbours</b> are one edge away; <b>degree</b> is the number of edges at a node; a <b>path</b> is a sequence of nodes each joined to the next, its length counted in <b>hops</b>.</p>

<div class="dc-grid">
  <div class="dc-card"><h3>Directed or undirected</h3><p>"Knows" goes both ways. "Follows", "links to" and "flies to" need not: whether a path exists then depends on the direction of travel.</p></div>
  <div class="dc-card"><h3>Weighted or unweighted</h3><p>An edge can carry a number: a distance, a travel time, a cost.</p></div>
</div>

***

<p class="dc-kicker">Concept 2</p>

## Writing a graph down

<div class="dc-cols">
<div>
<h4>Edge list</h4>
{{< highlight python >}}
edges = [("Ana", "Ben"),
         ("Ana", "Chi"),
         ("Chi", "Dev")]
{{< /highlight >}}
<p class="dc-small">Natural for a file. Poor to ask: "who are Dev's neighbours?" means reading every edge.</p>
</div>
<div>
<h4>Adjacency list</h4>
{{< highlight python >}}
def build_graph(edges, directed=False):
    graph = {}
    for a, b in edges:
        graph.setdefault(a, set())
        graph.setdefault(b, set())   # b too!
        graph[a].add(b)
        if not directed:
            graph[b].add(a)
    return graph
{{< /highlight >}}
</div>
</div>

<p class="dc-quote"><b>Every node must be a key</b>, with an empty collection if nothing leaves it. Otherwise: <code>KeyError</code>.</p>

{{% note %}}
The second setdefault guards against the most common bug in a first graph program: in a directed graph a node may only ever appear as a target. For a weighted graph each node maps to a dictionary: graph["ATL"] = {"MIA": 950, "LAX": 3100}.
{{% /note %}}

***

<p class="dc-kicker">Concept 3</p>

## Breadth-first search

<div class="dc-cols">
<div>
{{< highlight python >}}
from collections import deque

def hop_distances(graph, start):
    hops = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()        # FRONT
        for neighbour in graph[node]:
            if neighbour not in hops:
                hops[neighbour] = hops[node] + 1
                queue.append(neighbour)   # BACK
    return hops
{{< /highlight >}}
</div>
<div>
<ul class="dc-points">
  <li>Work outward in <b>rings</b>: everything one step away, then everything new that is two steps away.</li>
  <li>A <b>queue</b> produces that order by itself: found first, expanded first.</li>
  <li>Nearer rings are finished first, so the first time a node is reached is by a route with the <b>fewest steps</b>.</li>
  <li>Cost: about one step per node plus one per edge.</li>
</ul>
</div>
</div>

{{% note %}}
Do it by hand first on the friendship graph from notebook 1: eight people, who can introduce Ana to Fay, and through how many people?
{{% /note %}}

***

<p class="dc-kicker">Concept 3, continued</p>

## Three details decide whether it works

<div class="dc-grid three">
  <div class="dc-card red"><h3>Take from the front</h3><p>Taking from the back sends the search down one route as far as it goes. That is <i>depth-first</i>: the same nodes, with the wrong distances.</p></div>
  <div class="dc-card red"><h3>Skip what has been seen</h3><p>Otherwise any cycle traps the search for ever.</p></div>
  <div class="dc-card red"><h3>Record a node when it joins the queue</h3><p>Not when it leaves, or it joins once for every edge that leads to it.</p></div>
</div>

***

<p class="dc-kicker">Concept 4</p>

## The path

<div class="dc-cols">
<div>
{{< highlight python >}}
came_from = {start: None}
...
    if neighbour not in came_from:
        came_from[neighbour] = node
        queue.append(neighbour)

path = []
node = target
while node is not None:
    path.append(node)
    node = came_from[node]
path.reverse()
{{< /highlight >}}
</div>
<div>
<ul class="dc-points">
  <li>Three steps away is not an itinerary.</li>
  <li>Every time the search finds a new node, it finds it <b>from</b> some other node. Record that one fact.</li>
  <li>Afterwards, follow the notes back from the target to the start, then reverse.</li>
</ul>
</div>
</div>

<p class="dc-quote"><b>Shortest paths are not unique.</b> Check that it is a real path of the right length, never that it is one particular path.</p>

***

<p class="dc-kicker">Concept 5</p>

## Reachability and components

<div class="dc-code-lg">
{{< highlight python >}}
def components(graph):
    seen, parts = set(), []
    for node in graph:
        if node not in seen:
            part = set(hop_distances(graph, node))    # everything reachable
            seen |= part
            parts.append(part)
    return parts
{{< /highlight >}}
</div>

<ul class="dc-points">
  <li>A <b>connected component</b>: nodes that can all reach each other, with no edge leading out.</li>
  <li>Typically one giant component with nearly everything in it, and a scatter of small ones.</li>
  <li>The small ones are frequently either the answer to the question or a sign of something odd in the data.</li>
</ul>

<p class="dc-small">Looking at the components is one of the first things to do with any real network.</p>

***

<p class="dc-kicker">Concept 6</p>

## When edges have lengths

<p class="dc-small">Four towns. The direct road is 90 km. A route through two other towns uses three roads and totals 60 km. Breadth-first search returns the direct road: it counts roads.</p>

<table class="dc-table">
  <thead><tr><th></th><th>Breadth-first search</th><th>Dijkstra</th></tr></thead>
  <tbody>
    <tr><td>question</td><td>fewest edges</td><td>smallest total weight</td></tr>
    <tr><td>takes next</td><td>the oldest node in the queue</td><td>the <b>nearest</b> node</td></tr>
    <tr><td>container</td><td><code>deque</code></td><td><code>heapq</code></td></tr>
    <tr><td>needs</td><td>nothing</td><td>weights that are not negative</td></tr>
  </tbody>
</table>

<p class="dc-quote">What "shortest" means is a <b>modelling decision</b>, made by what is put on the edges: 1 for fewest changes, kilometres, minutes, the fare.</p>

{{% note %}}
With every weight equal to 1, the two give the same answer. Dijkstra is the same search with the queue replaced by a priority queue; a node's distance may be improved until the node is finally taken out.
{{% /note %}}

***

<p class="dc-kicker">The library</p>

## networkx

<div class="dc-code-lg">
{{< highlight python >}}
import networkx as nx

G = nx.Graph()                               # nx.DiGraph() for directed
G.add_weighted_edges_from(edges, weight="km")

nx.shortest_path(G, "Alba", "Dale")                 # fewest edges
nx.shortest_path(G, "Alba", "Dale", weight="km")    # shortest distance
nx.connected_components(G)
{{< /highlight >}}
</div>

<p class="dc-small">The same function gives two different routes depending on whether it is told about the weights. <b>Forgetting <code>weight=</code> is the usual mistake</b>, and it produces a plausible wrong answer.</p>

***

<p class="dc-kicker">Use case</p>

## Routing passengers

<p class="dc-small">About 37,000 routes between 3,300 airports. There is no direct flight from Atlanta to Sydney.</p>

<table class="dc-table">
  <thead><tr><th></th><th>Route</th><th>Flights</th><th>Distance</th></tr></thead>
  <tbody>
    <tr><td>fewest flights, as found</td><td>Atlanta → Dubai → Sydney</td><td>2</td><td>24,000 km</td></tr>
    <tr><td>fewest kilometres</td><td>Atlanta → Los Angeles → Sydney</td><td>2</td><td>15,000 km</td></tr>
  </tbody>
</table>

<ul class="dc-points">
  <li>Both have the fewest flights. A booking system has to decide what it is minimising.</li>
  <li>The same network shows <b>hubs</b> (a handful of airports with over two hundred routes), <b>one-way routes</b>, and small groups of airports <b>cut off</b> from the rest.</li>
</ul>

{{% note %}}
This is the data of Homework 11. Other graphs of the same shape: road networks, where the weight is driving time and components say what a closed bridge cuts off; and dependencies, such as course prerequisites, where the edges are directed.
{{% /note %}}

***

<p class="dc-kicker">Worked example — notebook 2</p>

## A puzzle that is secretly a graph

<div class="dc-flow">
  <div class="dc-node dark">COLD</div>
  <div class="dc-arrow">→</div>
  <div class="dc-node">CORD</div>
  <div class="dc-arrow">→</div>
  <div class="dc-node">WORD</div>
  <div class="dc-arrow">→</div>
  <div class="dc-node">WARD</div>
  <div class="dc-arrow">→</div>
  <div class="dc-node dark">WARM</div>
</div>

<p class="dc-small" style="text-align: center;">Each four-letter word is a node; two words that differ in one letter are joined: <b>2,400 nodes, 10,600 edges</b>. The shortest ladder is a shortest path.</p>

<div class="dc-grid">
  <div class="dc-card"><h3>Distances</h3><p>Most words are within five or six steps of COLD. The two farthest apart are seventeen steps from each other.</p></div>
  <div class="dc-card red"><h3>Components</h3><p>81 words have no neighbour at all. The second-largest component is a cluster of <b>Roman numerals</b> that had found their way into the word list.</p></div>
</div>

<p class="dc-small" style="margin-top: 14px;">Building it: comparing every pair of words grows with the square of their number. Filing each word under its four "one letter blanked" patterns in a dictionary does it in a hundredth of a second.</p>

{{% note %}}
The graph is something you decide to see. Nobody was looking for the Roman numerals: examining components is a remarkably effective way to find things in data that should not be there, and the same idea finds rings of connected accounts in fraud detection. The ladder shown is one of several of the same length; run the notebook for the one your search finds.
{{% /note %}}

***

<p class="dc-kicker">To take away</p>

## Key points

<ul class="dc-points">
  <li>A graph is things and connections. Say what a node is and what an edge means.</li>
  <li>Store edges in a file; ask an adjacency list. Every node must be a key.</li>
  <li>Breadth-first search: a queue, taken from the front, skipping what was seen. It finds the fewest steps.</li>
  <li>Keep a "came from" note per node to recover the path. Shortest paths are not unique.</li>
  <li>Look at the components before anything else.</li>
  <li>"Shortest" depends on what the edges carry. Decide before searching.</li>
</ul>

***

<p class="dc-kicker">Now: hands-on</p>

## Over to the notebooks

<p class="dc-small">Folder <a href="https://github.com/molnarai/DataScienceProgramming/tree/main/12-Graphs-Shortest-Path"><code>12-Graphs-Shortest-Path</code></a> — work them in this order:</p>

<div class="dc-grid three">
  <div class="dc-card green"><h3><span class="dc-nb"><span class="num">1</span></span>Things and Connections</h3><p class="dc-from">Concepts</p><p>Eight people and their friendships: building a graph, breadth-first search, paths, components, and weights. Four exercises.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">2</span></span>Word Ladders</h3><p class="dc-from">Worked example</p><p>COLD to WARM in seven steps, checked against networkx. Run it on ARC.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">3</span></span>Reference</h3><p class="dc-from">Look things up</p><p>Graph patterns and networkx calls to keep open while you work.</p></div>
</div>

<p class="dc-small" style="margin-top: 20px;">As you work, ask of every network: <b>what is a node, what is an edge, and what does "shortest" measure?</b><br>Homework: <a href="../../assignments/assignment-11/">Homework 11: Fewest Hops</a></p>
