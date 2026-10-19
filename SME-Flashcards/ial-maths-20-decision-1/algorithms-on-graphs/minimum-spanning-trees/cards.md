# Minimum Spanning Trees

Course: ial-maths-20-decision-1 · Section: Algorithms on Graphs

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/flashcards/algorithms-on-graphs/minimum-spanning-trees/


## Card 1 — question_and_answer (`fl_pTzzG84wwSNYVNB2`)

**FRONT**

In a matrix representing a graph, what do the rows and columns stand for?


**BACK**

The **rows** are labelled with the 'from' vertices and the **columns** with the 'to' vertices.

Each entry therefore describes the connection running from its row's vertex to its column's vertex.


Spec links: `spcpt_mpPyxNyDHWtynYG8`


## Card 2 — keyword_definition (`fl_x2NB2kg7k2n5mZdk`)

**FRONT**

Define an **adjacency matrix**.


**BACK**

An adjacency matrix is a **square** matrix whose rows and columns are both headed by all the vertices of the graph.

Each entry records the **number of direct connections** between that pair of vertices, rather than how long or how costly those connections are.


Spec links: `spcpt_c4x6xkBRwStbd9wY`


## Card 3 — keyword_definition (`fl_k3KTM8MSX8THDCPm`)

**FRONT**

Define a **distance matrix**.


**BACK**

A distance matrix records the **weight** of the edge joining each pair of vertices, where the weight may be a cost, a distance or a time.

It is not the same thing as an adjacency matrix, which counts connections rather than measuring them.


Spec links: `spcpt_c4x6xkBRwStbd9wY`


## Card 4 — fill_in_the_blanks (`fl_NRTnbfnT99NKzppJ`)

**FRONT**

Complete the contrast between the two kinds of matrix:

In an adjacency matrix, no connection between a pair of vertices is shown by an entry of `\_\_\_\_\_\_` in the cell, whereas in a distance matrix it is shown by leaving the cell `\_\_\_\_\_\_` instead.


**BACK**

The completed contrast is:

In an adjacency matrix, no connection between a pair of vertices is shown by an entry of **0** in the cell, whereas in a distance matrix it is shown by leaving the cell **empty** instead.

A distance matrix cannot use zero for this, because zero would be a perfectly good weight.


*Blanks: 0 — answers: ['0', 'empty']*

Spec links: `spcpt_c4x6xkBRwStbd9wY`

Flags: blank_answer_mismatch


## Card 5 — question_and_answer (`fl_5MYH6JHngCP9Thjr`)

**FRONT**

How does a loop show up in an adjacency matrix, and what value does it take?


**BACK**

A loop appears as a value on the **leading diagonal**, the line of cells running from the top left to the bottom right.

In an undirected graph that value is **2**, because the loop can be travelled in either direction, while a directed loop gives **1**.


Spec links: `spcpt_c4x6xkBRwStbd9wY`


## Card 6 — true_or_false (`fl_Bn9rKBrhFzywTvkd`)

**FRONT**

**True or False?**

A matrix representing an undirected graph is symmetrical about its leading diagonal.


**BACK**

**True.**

In an undirected graph the connection from $A$ to $B$ is the very same connection as the one from $B$ to $A$, so the two cells must agree.

A **directed** graph is not symmetrical, because the two directions can carry different values or exist only one way.


Spec links: `spcpt_c4x6xkBRwStbd9wY`


## Card 7 — question_and_answer (`fl_FsNTr8bBTYRK62FD`)

**FRONT**

You are drawing a network from a distance matrix, and two cells between a pair of vertices hold different values. What does that tell you?


**BACK**

The graph is **directed**, so those two vertices must be joined by **two separate edges**, each labelled with its own weight and its own direction.

Where the two cells agree, a single undirected edge carrying that weight is all that is needed.


Spec links: `spcpt_c4x6xkBRwStbd9wY`


## Card 8 — question_and_answer (`fl_tDgr5DmKm36NVnjw`)

**FRONT**

Why is a matrix a useful way to present a network?


**BACK**

It holds every connection and its weight as a table, so a network can be given in full without any drawing at all.

The weight of a **walk** through the network can then be worked out simply by reading off and adding the relevant entries.


Spec links: `spcpt_mpPyxNyDHWtynYG8`


## Card 9 — keyword_definition (`fl_krGHn6qKgGvhnTMD`)

**FRONT**

Define a **minimum spanning tree**.


**BACK**

A minimum spanning tree is a spanning tree whose total edge weight is as **small as possible**.

It is sometimes called a **minimum connector**, since it joins every vertex of the network together in the most economical way.


Spec links: `spcpt_jsvMbYSNrrYY9h3d`


## Card 10 — fill_in_the_blanks (`fl_hxM5xtJvnmWYGMZz`)

**FRONT**

Complete the fact about the size of a minimum spanning tree:

A minimum spanning tree of a network with $n$ vertices contains exactly `\_\_\_\_\_\_` edges.


**BACK**

The completed fact is:

A minimum spanning tree of a network with $n$ vertices contains exactly $n - 1$ edges.

Any more would close a **cycle**, which a tree can never contain, and any fewer would leave some vertex unconnected.


*Blanks: 0 — answers: ['cycle']*

Spec links: `spcpt_jsvMbYSNrrYY9h3d`

Flags: blank_answer_mismatch


## Card 11 — question_and_answer (`fl_bv9Y7vPN6QQRc4kx`)

**FRONT**

What must you do before Kruskal's algorithm can begin?


**BACK**

Sort **every edge of the network into increasing order of weight**.

The algorithm then works its way down that list, so the ordering has to be complete before the first edge is chosen.


Spec links: `spcpt_jsvMbYSNrrYY9h3d`


## Card 12 — true_or_false (`fl_pYT7Gs4NDSfCMcsv`)

**FRONT**

**True or False?**

Kruskal's algorithm begins by choosing a starting vertex.


**BACK**

**False.**

Kruskal's algorithm begins with the **edge of least weight** in the whole network, wherever in the network that edge happens to lie.

It is the edges that are ranked, not the vertices, so no starting vertex is ever chosen.


Spec links: `spcpt_jsvMbYSNrrYY9h3d`


## Card 13 — question_and_answer (`fl_Wr5vDYVJMYQzhc98`)

**FRONT**

In Kruskal's algorithm you come to the next edge on the sorted list. When should you reject it?


**BACK**

Reject it whenever adding it would form a **cycle** with the edges already chosen.

Otherwise add it to the tree and carry on down the list, and where two edges have equal weight either one may be taken.


Spec links: `spcpt_jsvMbYSNrrYY9h3d`


## Card 14 — question_and_answer (`fl_GgZWZXn9FYjz3fQN`)

**FRONT**

How do you know when Kruskal's algorithm has finished?


**BACK**

It is finished once **every vertex of the network has been connected** into the tree.

At that point no further edge could be added without closing a cycle.


Spec links: `spcpt_jsvMbYSNrrYY9h3d`


## Card 15 — question_and_answer (`fl_7fjpPY5qNqMpGxkr`)

**FRONT**

Kruskal's algorithm selects edges of weight $1$, $2$, $4$, $5$, $5$, $6$ and $7$. What is the total weight of the minimum spanning tree?


**BACK**

The total weight is $30$, found by adding the weights of the selected edges: $1 + 2 + 4 + 5 + 5 + 6 + 7 = 30$.

Edges that were rejected along the way are never counted, since they form no part of the tree.


Spec links: `spcpt_jsvMbYSNrrYY9h3d`


## Card 16 — question_and_answer (`fl_cqHq5Ms2Rzmf4N2W`)

**FRONT**

What does Prim's algorithm find, and what forms of information can it use?


**BACK**

Prim's algorithm finds a **minimum spanning tree** for a network.

It can be applied whether the network is presented as a **graph** or as a **matrix**, which is not true of every method.


Spec links: `spcpt_dm8d8NdqXZ86qCtJ`


## Card 17 — question_and_answer (`fl_K7h5gyvxbGmb3Tpn`)

**FRONT**

How does Prim's algorithm begin?


**BACK**

Start at **any vertex** you like, and add the edge of least weight that is connected to it.

There is no rule about which vertex to pick, so any of them will serve.


Spec links: `spcpt_6MrxckS4B59GZns8`


## Card 18 — question_and_answer (`fl_CQgFwM6KrQhcXVs9`)

**FRONT**

At each stage of Prim's algorithm, which edge do you add next?


**BACK**

The edge of **least weight** that joins a vertex already in the tree to a vertex **not yet in it**.

Where two such edges have equal weight, either one may be taken.


Spec links: `spcpt_6MrxckS4B59GZns8`


## Card 19 — question_and_answer (`fl_Cf4K9P4NM7PvKpxS`)

**FRONT**

Why does Prim's algorithm never need to check whether an edge forms a cycle?


**BACK**

Because every edge it adds reaches a vertex that is **not yet in the tree**, and an edge to a brand-new vertex cannot close a loop.

Cycles are ruled out by the rule for choosing edges, rather than by testing for them after the event.


Spec links: `spcpt_6MrxckS4B59GZns8`


## Card 20 — true_or_false (`fl_2JcXYj84vjv5YXpy`)

**FRONT**

**True or False?**

Starting Prim's algorithm at a different vertex can change the total weight of the minimum spanning tree it produces.


**BACK**

**False.**

The total weight of a minimum spanning tree is a property of the **network** itself, not of where you happened to start.

A different starting vertex may build the tree up in a different order, but the weight it ends at is the same.


Spec links: `spcpt_6MrxckS4B59GZns8`


## Card 21 — question_and_answer (`fl_yNG3NzKR9pKrmF59`)

**FRONT**

You are running Prim's algorithm on a distance matrix. What do you do with the starting vertex's row and column?


**BACK**

**Label its row** with a $1$, and **cross out its column** entirely.

Deleting the column stops that vertex from being chosen again, since a vertex already in the tree must never be entered a second time.


Spec links: `spcpt_NrWwXjJZ9DMCbpZn`


## Card 22 — fill_in_the_blanks (`fl_4SmWdM4xS23MqrKB`)

**FRONT**

Complete the selection rule for Prim's algorithm carried out on a distance matrix:

Circle the `\_\_\_\_\_\_` value appearing anywhere in the rows labelled so far, then cross out the rest of that value's `\_\_\_\_\_\_` in the table.


**BACK**

The completed rule is:

Circle the **smallest** value appearing anywhere in the rows labelled so far, then cross out the rest of that value's **column** in the table.

The vertex heading that column then has its own row labelled with the next number.


*Blanks: 0 — answers: ['smallest', 'column']*

Spec links: `spcpt_NrWwXjJZ9DMCbpZn`

Flags: blank_answer_mismatch


## Card 23 — question_and_answer (`fl_gNrcNyRYrbCjh3GS`)

**FRONT**

Running Prim's on a matrix, what does crossing out a column correspond to in the graph version of the algorithm?


**BACK**

It corresponds to that vertex being **already in the tree**, so that no further edge is allowed to lead into it.

The two versions are one algorithm: labelled rows are the vertices in the tree, and crossed-out columns are the vertices no longer available.


Spec links: `spcpt_NrWwXjJZ9DMCbpZn`


## Card 24 — question_and_answer (`fl_w6T75N5WjmMsp496`)

**FRONT**

Kruskal's and Prim's algorithms give different trees for the same network. Has one of them gone wrong?


**BACK**

Neither has gone wrong.

Both algorithms always produce a **minimum** spanning tree, and a network can have more than one different tree sharing that same minimal total weight.


Spec links: `spcpt_wdmRbpKyGXsKZdMF`


## Card 25 — true_or_false (`fl_jTyCWKs6QFQ7tJJX`)

**FRONT**

**True or False?**

Kruskal's algorithm can be applied directly to a network given as a table of distances.


**BACK**

**False.**

Kruskal's works from a list of edges ranked by weight, so a table has to be turned into a graph, or at least into a list of edges, before it can begin.

**Prim's** algorithm is the one that runs directly on a table.


Spec links: `spcpt_wdmRbpKyGXsKZdMF`


## Card 26 — question_and_answer (`fl_KDShDDtn7Qzry969`)

**FRONT**

Part-way through its working, one of the two minimum spanning tree algorithms can have several disconnected pieces. Which one, and why?


**BACK**

**Kruskal's**, because it takes edges purely in order of weight and those edges may lie in quite separate parts of the network.

**Prim's** cannot do this, since every edge it adds has to touch the tree it has already built.


Spec links: `spcpt_wdmRbpKyGXsKZdMF`


## Card 27 — question_and_answer (`fl_m9M9mJKSct2hbQtn`)

**FRONT**

Why is Prim's algorithm sometimes considered more efficient than Kruskal's?


**BACK**

Because it does not require every edge in the network to be **sorted into order of weight** before it starts.

On a large network that initial sort can be a considerable piece of work in its own right.


Spec links: `spcpt_wdmRbpKyGXsKZdMF`


## Card 28 — question_and_answer (`fl_jpP9r57RN9KWBM6N`)

**FRONT**

Certain named edges must be included in a spanning tree. How do you build the rest of it, and what is true of the result?


**BACK**

Draw in the edges you are required to use first, then complete the tree using **Kruskal's algorithm**, rejecting any edge that would close a cycle.

The result satisfies the requirement but is **not necessarily a minimum** spanning tree, because the forced edges may not be the ones a free choice would have taken.


Spec links: `spcpt_wdmRbpKyGXsKZdMF`

