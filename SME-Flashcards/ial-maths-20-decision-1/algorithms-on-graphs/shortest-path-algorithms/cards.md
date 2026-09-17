# Shortest Path Algorithms

Course: ial-maths-20-decision-1 · Section: Algorithms on Graphs

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/flashcards/algorithms-on-graphs/shortest-path-algorithms/


## Card 1 — question_and_answer (`fl_QKYF7HbSFhw6V24V`)

**FRONT**

What does Dijkstra's algorithm find?


**BACK**

The **shortest distance** between two vertices of a network, together with the route that achieves it.

Run across a whole network it gives the shortest distance from one fixed start vertex to **every** other vertex.


Spec links: `spcpt_GzzWTsWwZ252dRpv`


## Card 2 — question_and_answer (`fl_ZWHj3ZsKwZm6rSys`)

**FRONT**

What does a 'working value' at a vertex represent?


**BACK**

A working value is the shortest distance to that vertex found **so far**, along whichever routes have been explored up to that point.

It is provisional, and a vertex may collect several working values as the algorithm goes on.


Spec links: `spcpt_GzzWTsWwZ252dRpv`


## Card 3 — keyword_definition (`fl_XQMXMxpdzgDhR6SM`)

**FRONT**

Define the **final label** of a vertex in Dijkstra's algorithm.


**BACK**

The final label of a vertex is the **shortest distance from the start vertex** to that vertex, along the best route through the network.

Every vertex ends up with one, and together they are what the algorithm was run to produce.


Spec links: `spcpt_GzzWTsWwZ252dRpv`


## Card 4 — question_and_answer (`fl_jRHdwmMzZnGTr6ZN`)

**FRONT**

How is the start vertex labelled at the beginning of Dijkstra's algorithm?


**BACK**

It is given labelling order $1$ and a final label of $0$.

The zero is right because the shortest distance from the start vertex to itself is no distance at all.


Spec links: `spcpt_GzzWTsWwZ252dRpv`


## Card 5 — question_and_answer (`fl_CyNFttv3f766R5PN`)

**FRONT**

A vertex already has a working value, and a new route reaches it with another. When do you write the new one in?


**BACK**

Only when the new value is **smaller** than the one already there.

A working value records the best distance found so far, so a larger figure tells you nothing and is simply not written down.


Spec links: `spcpt_GzzWTsWwZ252dRpv`


## Card 6 — question_and_answer (`fl_bVrWDrQj7fWcjNJq`)

**FRONT**

Several vertices have working values but no final label yet. Which one is made final next?


**BACK**

The one carrying the **smallest working value** anywhere in the network.

That working value becomes its final label, and the vertex takes the next number in the labelling order.


Spec links: `spcpt_GzzWTsWwZ252dRpv`


## Card 7 — true_or_false (`fl_pZw4gDtf4hwctyQQ`)

**FRONT**

**True or False?**

In Dijkstra's algorithm, a vertex's final label can be improved later if a shorter route to it is found.


**BACK**

**False.**

A final label is permanent, which is why it is sometimes called a permanent label instead.

The algorithm only makes a vertex final when nothing still unexplored could possibly reach it more cheaply, so there is never anything left to improve.


Spec links: `spcpt_GzzWTsWwZ252dRpv`


## Card 8 — fill_in_the_blanks (`fl_PgJsw5YwbNrNNTGz`)

**FRONT**

Complete the fact about stopping Dijkstra's algorithm early:

The algorithm may be stopped as soon as the `\_\_\_\_\_\_` vertex has been given its final label, which saves a good deal of work on a large network.


**BACK**

The completed fact is:

The algorithm may be stopped as soon as the **destination** vertex has been given its final label, which saves a good deal of work on a large network.

There is no need to settle every vertex when only one destination has been asked for.


*Blanks: 0 — answers: ['destination']*

Spec links: `spcpt_GzzWTsWwZ252dRpv`

Flags: blank_answer_mismatch


## Card 9 — question_and_answer (`fl_zKtpX3B4XvGFVtRc`)

**FRONT**

Every vertex now has its final label. How do you read off the shortest route itself?


**BACK**

Work **backwards** from the destination towards the start vertex.

Two vertices lie on the shortest route when the **difference between their final labels** is exactly equal to the weight of the edge joining them.


Spec links: `spcpt_GzzWTsWwZ252dRpv`


## Card 10 — question_and_answer (`fl_5JgTYnsfKBvHmnXV`)

**FRONT**

Two adjacent vertices have final labels $8$ and $15$, and the edge joining them has weight $7$. Do they lie on the shortest route?


**BACK**

They do lie on it.

The difference $15 - 8 = 7$ matches the weight of that edge exactly, which is the test for an edge belonging to the shortest route.


Spec links: `spcpt_GzzWTsWwZ252dRpv`

