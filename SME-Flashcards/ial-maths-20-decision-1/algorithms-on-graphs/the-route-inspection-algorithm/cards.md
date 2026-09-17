# The Route Inspection Algorithm

Course: ial-maths-20-decision-1 · Section: Algorithms on Graphs

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/flashcards/algorithms-on-graphs/the-route-inspection-algorithm/


## Card 1 — keyword_definition (`fl_87QQCVg3w96G66mv`)

**FRONT**

What is the **route inspection problem**?


**BACK**

The route inspection problem, also known as the **Chinese postman problem**, is to find the route of **least weight** that travels along every edge of a graph and returns to its starting vertex.

Some edges may have to be covered more than once, and the aim is to keep the total weight of those repeats as small as possible.


Spec links: `spcpt_zRs4Yh5KvWq3WyKS`


## Card 2 — fill_in_the_blanks (`fl_TDsYFKBx5vyNjwwN`)

**FRONT**

A network has no odd vertices at all. Complete the conclusion:

The graph is `\_\_\_\_\_\_` so a closed route using every edge exactly once already exists, and nothing has to be repeated.


**BACK**

The completed conclusion is:

The graph is **Eulerian** so a closed route using every edge exactly once already exists, and nothing has to be repeated.

The length of the shortest inspection route is then simply the sum of the weights of all the edges in the network.


*Blanks: 0 — answers: ['Eulerian']*

Spec links: `spcpt_SWNq6cfM2PcV7PNX`

Flags: blank_answer_mismatch


## Card 3 — question_and_answer (`fl_JHKWqNZyznvn23xv`)

**FRONT**

A network has exactly two odd vertices, and the route must start and finish at the same vertex. What has to be repeated?


**BACK**

The **shortest path between the two odd vertices**, whose edges are then added to the graph.

The length of the route is the sum of every edge in the network plus the weight of that repeated path.


Spec links: `spcpt_SWNq6cfM2PcV7PNX`


## Card 4 — question_and_answer (`fl_4wT3bjJG62S7Frzc`)

**FRONT**

Why does repeating the shortest path between the two odd vertices make a closed inspection route possible?


**BACK**

Each repeated edge adds one to the degree at both of its ends, so the two odd vertices gain one each and turn even, while every vertex in the middle of the path gains two and keeps the parity it already had.

With no odd vertices left, the adjusted graph is Eulerian and a closed route using every edge now exists.


Spec links: `spcpt_SWNq6cfM2PcV7PNX`


## Card 5 — true_or_false (`fl_JrtxPKYcq79DmDwZ`)

**FRONT**

**True or False?**

A route inspecting every edge of a network with two odd vertices can sometimes avoid repeating any edge at all.


**BACK**

**True.**

If the route is allowed to **start at one odd vertex and finish at the other**, it is an Eulerian trail and nothing needs repeating.

Repetition is only forced when the route has to begin and end at the same vertex.


Spec links: `spcpt_SWNq6cfM2PcV7PNX`


## Card 6 — question_and_answer (`fl_JryWxphsDYm9kSmm`)

**FRONT**

Why should you not assume that the direct edge is the shortest path between two odd vertices?


**BACK**

A path made up of **several shorter edges** can easily total less than one long direct edge.

Every route between the two odd vertices has to be compared, not just the one joining them directly.


Spec links: `spcpt_SWNq6cfM2PcV7PNX`


## Card 7 — question_and_answer (`fl_BKnhGy5hfCJRQXrB`)

**FRONT**

The edges of a network total $73$, and its two odd vertices are joined by a shortest path of weight $14$. How long is the shortest closed inspection route?


**BACK**

The route has length $73 + 14 = 87$.

The weight of the repeated path is added to the total of every edge, because each repeated edge is travelled a second time.


Spec links: `spcpt_SWNq6cfM2PcV7PNX`


## Card 8 — question_and_answer (`fl_3sC792XqNyxXJpxt`)

**FRONT**

What variations on the route inspection problem can arise?


**BACK**

The start and finish vertices may be **different** from one another, or certain edges may be **disregarded**, for instance because of a road closure.

Repetition may even be **required** rather than avoided, as for a road sweeper that has to cover both sides of every road.


Spec links: `spcpt_zRs4Yh5KvWq3WyKS`


## Card 9 — question_and_answer (`fl_CYyBVzkVrjzCJ8z4`)

**FRONT**

A network has four odd vertices. What must you consider before you can decide which edges to repeat?


**BACK**

**All the possible pairings** of the odd vertices, and the shortest path between the two vertices making up each pair.

For odd vertices P, Q, R and S the pairings are PQ with RS, PR with QS, and PS with QR.


Spec links: `spcpt_37mJDmGbj5wYYzWF`


## Card 10 — true_or_false (`fl_7zb2rKBXSmGWNFJ5`)

**FRONT**

**True or False?**

A network can have an odd number of odd vertices.


**BACK**

**False.**

The number of odd vertices in any graph is always even.

That is exactly why the odd vertices can always be split into pairs with none left over, which is what makes the pairing method work at all.


Spec links: `spcpt_37mJDmGbj5wYYzWF`


## Card 11 — fill_in_the_blanks (`fl_6dvmW7BsV68CYZ5Y`)

**FRONT**

Complete the count of pairings for a network with four odd vertices:

Four odd vertices can be split into `\_\_\_\_\_\_` different pairings, and each pairing uses up all `\_\_\_\_\_\_` of the odd vertices.


**BACK**

The completed count is:

Four odd vertices can be split into **three** different pairings, and each pairing uses up all **four** of the odd vertices.

Every odd vertex has to be paired off, since any left odd would still block a closed route.


*Blanks: 0 — answers: ['three', 'four']*

Spec links: `spcpt_37mJDmGbj5wYYzWF`

Flags: blank_answer_mismatch


## Card 12 — question_and_answer (`fl_7sCmBthZBkFkmVj8`)

**FRONT**

Once you have all the pairings, which one decides the edges to repeat?


**BACK**

The pairing whose **two shortest paths add to the smallest total**.

Those two paths are the ones repeated, and their edges are added into the network.


Spec links: `spcpt_37mJDmGbj5wYYzWF`


## Card 13 — question_and_answer (`fl_N2GQqYrtbR7qYy2d`)

**FRONT**

The repeated edges have been added to the network. How do you finish the route inspection problem?


**BACK**

Write down an **Eulerian circuit** of the adjusted network, which is now possible because adding those paths has made every vertex even.

Any such circuit is a valid answer, and there is usually more than one to choose from.


Spec links: `spcpt_37mJDmGbj5wYYzWF`


## Card 14 — question_and_answer (`fl_yWFwd9GzvdNqGnQj`)

**FRONT**

With four odd vertices, the route may start and finish at any two of them. How does that change the method?


**BACK**

Find the shortest paths for **all** the pairings as usual, then repeat only the **single shortest** of those paths.

The two odd vertices it does not touch become the start and finish points, since a route is allowed to begin and end at odd vertices.


Spec links: `spcpt_37mJDmGbj5wYYzWF`


## Card 15 — question_and_answer (`fl_cNkt9whHrQyNDBgR`)

**FRONT**

How can the weight of an edge depend on whether it is being repeated?


**BACK**

A first traversal may cost more than a second one along the same edge.

An inspector walking a pipeline takes longer over a section being checked than over one already inspected, so the return journey along it carries a smaller weight.


Spec links: `spcpt_37mJDmGbj5wYYzWF`

