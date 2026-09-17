# Graphs

Course: ial-maths-20-decision-1 · Section: Algorithms & Graph Theory

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/flashcards/algorithms-and-graph-theory/graphs/


## Card 1 — keyword_definition (`fl_ty2pB6D5Tg7RWWKY`)

**FRONT**

Define a **graph** in graph theory.


**BACK**

A graph consists of points, called **vertices** or **nodes**, which are connected by lines, called **edges** or **arcs**.

It is a way of representing a set of objects together with the connections between them, such as places and the routes joining them.


Spec links: `spcpt_Sh2bfsQFf7sDZ44z` `spcpt_hrmHmYZTVfcdzcJc`


## Card 2 — question_and_answer (`fl_9TqdHbKVxGhs4WjZ`)

**FRONT**

In a graph, what does it mean for two vertices to be adjacent, and for two edges to be adjacent?


**BACK**

Two **vertices** are adjacent when an edge joins them directly.

Two **edges** are adjacent when they share a common vertex.


Spec links: `spcpt_Sh2bfsQFf7sDZ44z`


## Card 3 — question_and_answer (`fl_PXm3Bp5Q5MsvC4BK`)

**FRONT**

What is a loop, and what are multiple edges?


**BACK**

A **loop** is an edge that starts and finishes at the same vertex.

**Multiple edges** are two or more edges joining the same pair of vertices, and a graph is allowed to contain either.


Spec links: `spcpt_Sh2bfsQFf7sDZ44z`


## Card 4 — true_or_false (`fl_Q8wF78K6vJMXDJHn`)

**FRONT**

**True or False?**

If two edges of a graph are drawn crossing each other, the point where they cross is a vertex.


**BACK**

**False.**

Edges are joined to one another only at **vertices**, so a crossing point with no vertex marked on it is just an artefact of the drawing.

Graphs are usually drawn so that edges do not overlap, for exactly this reason.


Spec links: `spcpt_Sh2bfsQFf7sDZ44z`


## Card 5 — keyword_definition (`fl_KWhnP3dDbz8fPfrZ`)

**FRONT**

Define the **weight** of an edge.


**BACK**

The weight of an edge is a number attached to it, most often a distance, a time or a cost.

The weight of a **walk** is found by adding together the weights of all the edges it uses.


Spec links: `spcpt_g4WGr939XD6DZyBD`


## Card 6 — fill_in_the_blanks (`fl_ZPxvfYY6rWwBF5fm`)

**FRONT**

Complete the three terms for moving through a graph:

A **walk** is a sequence of edges running from vertex to vertex. A `\_\_\_\_\_\_` is a walk in which no vertex is repeated, and a `\_\_\_\_\_\_` is a walk in which no edge is repeated.


**BACK**

The completed sentence is:

A **walk** is a sequence of edges running from vertex to vertex. A **path** is a walk in which no vertex is repeated, and a **trail** is a walk in which no edge is repeated.

Every path is therefore also a trail, but a trail need not be a path.


*Blanks: 0 — answers: ['walk', 'path', 'trail']*

Spec links: `spcpt_g4WGr939XD6DZyBD`

Flags: blank_answer_mismatch


## Card 7 — question_and_answer (`fl_NWmp4nCZgRT9ZxBY`)

**FRONT**

What is a cycle, and what is a tour?


**BACK**

A **cycle**, also called a circuit, is a path that starts and finishes at the same vertex, so it is a closed path.

A **tour** is a walk that visits every vertex and then returns to its starting vertex.


Spec links: `spcpt_g4WGr939XD6DZyBD`


## Card 8 — keyword_definition (`fl_QHTnfW4zGj8vwGxm`)

**FRONT**

Define a **connected graph**.


**BACK**

A connected graph is one in which every vertex is connected to every other vertex.

Two vertices count as connected whenever there is a **path** between them, which does not require an edge joining them directly.


Spec links: `spcpt_h3Gvrwv3BRwysKYT`


## Card 9 — question_and_answer (`fl_WsXdk6JxqVBSsk23`)

**FRONT**

What is a complete graph, and how is one labelled?


**BACK**

A complete graph is a graph in which every vertex is joined by an edge to each of the other vertices.

A complete graph with $n$ vertices is written $K_{n}$.


Spec links: `spcpt_h3Gvrwv3BRwysKYT`


## Card 10 — keyword_definition (`fl_bpdVSRKjx83vj7tn`)

**FRONT**

Define a **network**.


**BACK**

A network is a **weighted graph**, meaning a graph whose edges have each been given a numerical value.

Networks are not usually drawn to scale, so the length of an edge on the page tells you nothing about its weight.


Spec links: `spcpt_h3Gvrwv3BRwysKYT`


## Card 11 — keyword_definition (`fl_YQ8SNynwJzvMMQbQ`)

**FRONT**

Define a **digraph**.


**BACK**

A digraph is a graph whose edges have been given a **direction**, making them directed edges.

Each directed edge may only be travelled along in the direction its arrow indicates.


Spec links: `spcpt_h3Gvrwv3BRwysKYT`


## Card 12 — question_and_answer (`fl_JdmmrpWyfrnt5cfY`)

**FRONT**

What four conditions make a graph a simple graph?


**BACK**

A simple graph contains no **loops** and no **multiple edges**.

It is therefore the plainest kind of graph, with at most one edge between any pair of distinct vertices.


Spec links: `spcpt_h3Gvrwv3BRwysKYT`


## Card 13 — question_and_answer (`fl_PBdwXPG9Mn6rQ5PD`)

**FRONT**

What is a subgraph, and what is a tree?


**BACK**

A **subgraph** of a graph is a graph whose vertices and edges all belong to the original graph.

A **tree** is a connected graph that contains no cycles at all.


Spec links: `spcpt_h3Gvrwv3BRwysKYT`


## Card 14 — keyword_definition (`fl_sNhfS23yV4xFgBhG`)

**FRONT**

Define a **spanning tree** of a graph.


**BACK**

A spanning tree is a subgraph that is itself a **tree** and that includes **every vertex** of the original graph.

Being a tree, it is connected and contains no cycles.


Spec links: `spcpt_h3Gvrwv3BRwysKYT`


## Card 15 — keyword_definition (`fl_yrCFGNDntq7CTNjH`)

**FRONT**

Define **isomorphic graphs**.


**BACK**

Isomorphic graphs are graphs that show the **same information** but are drawn in different ways.

They have the same number of vertices, and the number of edges meeting each vertex matches up between them.


Spec links: `spcpt_h3Gvrwv3BRwysKYT`


## Card 16 — keyword_definition (`fl_WN7qZWq4kbPk6Ptb`)

**FRONT**

Define the **degree** (or valency) of a vertex.


**BACK**

The degree of a vertex is the number of edges **incident** to it, meaning the number of edges that meet it.

A vertex is described as **odd** or **even** according to whether that number is odd or even.


Spec links: `spcpt_g6QKkK28sx7kfVZp`


## Card 17 — question_and_answer (`fl_BMm3k6PrrVhSTBQz`)

**FRONT**

By how much does a loop increase the degree of a vertex?


**BACK**

By **two**, rather than by one.

A loop starts and finishes at the same vertex, so **both** of its ends are incident to that vertex and each end is counted separately.


Spec links: `spcpt_g6QKkK28sx7kfVZp`


## Card 18 — fill_in_the_blanks (`fl_86f8TVZjBrYQVTt5`)

**FRONT**

Complete Euler's handshaking lemma, which holds for any undirected graph:

`\text{sum of the degrees of the vertices} = \_\_\_\_\_\_ \times \text{the number of edges}`


**BACK**

The completed lemma is:

$\text{sum of the degrees of the vertices} = 2 \times \text{the number of edges}$

Every edge has two ends, and each end adds one to the degree of the vertex it meets.


*Blanks: 0 — answers: []*

Spec links: `spcpt_g6QKkK28sx7kfVZp`


## Card 19 — question_and_answer (`fl_2GnkmrTPmv9g9swS`)

**FRONT**

What does the handshaking lemma tell you about the number of odd vertices?


**BACK**

The number of odd vertices in a graph is always **even**, and it may be zero.

Since all the degrees add up to an even total, the odd degrees among them have to pair up.


Spec links: `spcpt_g6QKkK28sx7kfVZp`


## Card 20 — question_and_answer (`fl_spRnntYCpN2d8t35`)

**FRONT**

What is the difference between an Eulerian cycle and an Eulerian trail?


**BACK**

Both use **every edge of the graph exactly once**.

An Eulerian **cycle** returns to the vertex it set out from, while an Eulerian **trail** finishes at a different vertex from the one it began at.


Spec links: `spcpt_Mzny5k3hmzPrjX2J`


## Card 21 — true_or_false (`fl_R35NR2S6VY6DpxBx`)

**FRONT**

**True or False?**

An Eulerian cycle may pass through the same vertex more than once.


**BACK**

**True.**

The condition is on the **edges** rather than the vertices: every edge is used exactly once, and nothing prevents the route arriving at a vertex again along a different edge.

That is why an Eulerian cycle is not a cycle in the ordinary sense of the word.


Spec links: `spcpt_Mzny5k3hmzPrjX2J`


## Card 22 — question_and_answer (`fl_Dbk3P36KHZ8dzhcs`)

**FRONT**

What condition makes a graph Eulerian, and what makes it semi-Eulerian?


**BACK**

A graph is **Eulerian** when every one of its vertices has **even** degree, and it then contains an Eulerian cycle.

It is **semi-Eulerian** when exactly **two** vertices have odd degree, and those two are where an Eulerian trail has to start and finish.


Spec links: `spcpt_Mzny5k3hmzPrjX2J`


## Card 23 — question_and_answer (`fl_cBB3cWzB6Cqc365G`)

**FRONT**

How can you tell quickly whether a graph is Eulerian or semi-Eulerian?


**BACK**

Ask whether the graph can be drawn without lifting your pen from the paper and without going over any edge twice.

If it can, the graph is Eulerian or semi-Eulerian, because tracing it that way is exactly what using every edge once means.


Spec links: `spcpt_Mzny5k3hmzPrjX2J`


## Card 24 — question_and_answer (`fl_xt4Nxt4CKN2JmHXf`)

**FRONT**

A graph has vertices of degree $2$, $4$, $3$, $3$ and $4$. Is it Eulerian, semi-Eulerian, or neither?


**BACK**

It is **semi-Eulerian**, because exactly two of its vertices have odd degree, namely the two of degree $3$.

An Eulerian trail therefore exists, and it must begin at one of those two vertices and end at the other.


Spec links: `spcpt_Mzny5k3hmzPrjX2J`


## Card 25 — keyword_definition (`fl_Zh2QdMDxHgMdTgWN`)

**FRONT**

Define a **Hamiltonian cycle**.


**BACK**

A Hamiltonian cycle is a cycle that visits **every vertex** of the graph exactly once and returns to the vertex it started from.

A graph that contains one is called a **Hamiltonian graph**.


Spec links: `spcpt_Y6ZGFfHSfjhqhh5t`


## Card 26 — question_and_answer (`fl_rjPWRt4pgWsPZFkj`)

**FRONT**

How does a Hamiltonian path differ from a Hamiltonian cycle?


**BACK**

A Hamiltonian **path** visits every vertex exactly once but does not have to come back to where it began.

A Hamiltonian **cycle** does the same and then returns to its starting vertex.


Spec links: `spcpt_Y6ZGFfHSfjhqhh5t`


## Card 27 — question_and_answer (`fl_6zzhWcWf8P6GgVT4`)

**FRONT**

What makes a graph semi-Hamiltonian?


**BACK**

A graph is semi-Hamiltonian when it contains a Hamiltonian **path** but no Hamiltonian **cycle**.

Every vertex can be visited once in a single journey, but there is no way of closing that journey back to its starting point.


Spec links: `spcpt_Y6ZGFfHSfjhqhh5t`


## Card 28 — true_or_false (`fl_s8gNQzvCrmkWnCr4`)

**FRONT**

**True or False?**

A Hamiltonian cycle must use every edge of the graph.


**BACK**

**False.**

A Hamiltonian cycle places its condition on the **vertices**: each one has to be visited exactly once.

Any edges that are not needed in order to make that journey are simply left unused.


Spec links: `spcpt_Y6ZGFfHSfjhqhh5t`


## Card 29 — question_and_answer (`fl_r82bPJdm9twPQX8D`)

**FRONT**

You are asked to show that a graph is Hamiltonian. What is the only way to do it?


**BACK**

**Identify an actual Hamiltonian cycle** and write it out, for example as the sequence of vertices $A B C F D E A$.

There is no test on the degrees of the vertices that settles the question, so the cycle itself has to serve as the evidence.


Spec links: `spcpt_Y6ZGFfHSfjhqhh5t`


## Card 30 — question_and_answer (`fl_Xt6VyjYX4vCNj26H`)

**FRONT**

A graph has been shown to be Hamiltonian by writing down one Hamiltonian cycle. Could a different answer also be correct?


**BACK**

A graph can contain **several** different Hamiltonian cycles, so another student's answer may be just as correct.

Any one of them is enough to establish that the graph is Hamiltonian.


Spec links: `spcpt_Y6ZGFfHSfjhqhh5t`

