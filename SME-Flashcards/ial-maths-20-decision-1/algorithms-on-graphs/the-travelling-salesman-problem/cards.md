# The Travelling Salesman Problem

Course: ial-maths-20-decision-1 · Section: Algorithms on Graphs

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/flashcards/algorithms-on-graphs/the-travelling-salesman-problem/


## Card 1 — keyword_definition (`fl_khd7htT5JcTjdyCc`)

**FRONT**

Define the **travelling salesman problem**.


**BACK**

The travelling salesman problem is to find a **route of minimum length that visits every vertex** in an undirected network and returns to where it started.

Such a route is called a **tour**.


Spec links: `spcpt_cm3fwdmGY3HDyvjV`


## Card 2 — question_and_answer (`fl_DbHTvTTFQKBBKjkR`)

**FRONT**

What is the difference between the classical and the practical travelling salesman problem?


**BACK**

In the **classical** problem each vertex is visited **exactly once** before returning to the start.

In the **practical** problem each vertex must be visited **at least once**, so a vertex may be passed through again on the way.


Spec links: `spcpt_cm3fwdmGY3HDyvjV`


## Card 3 — true_or_false (`fl_4b8HGfJZY2vwr2JM`)

**FRONT**

**True or False?**

In the travelling salesman problem, a tour is allowed to visit the same vertex more than once.


**BACK**

**True.**

A tour is a **walk** that visits every vertex and returns to its start, and a walk may pass through a vertex again.

A tour that visits every vertex other than the start exactly once is a **Hamiltonian cycle**, which is the special case the classical problem asks for.


Spec links: `spcpt_cm3fwdmGY3HDyvjV`


## Card 4 — keyword_definition (`fl_bmQmQprHgcdrPND2`)

**FRONT**

What is a **table of least distances**?


**BACK**

A table of least distances gives the **shortest distance** between every pair of vertices in a network, which is not always the direct edge joining them.

It describes a complete network in table form.


Spec links: `spcpt_cm3fwdmGY3HDyvjV`


## Card 5 — question_and_answer (`fl_DGQxQz3RNDNRzKTq`)

**FRONT**

Why is a table of least distances worth constructing for a travelling salesman problem?


**BACK**

Because it turns the **practical** problem into the **classical** one.

The table describes a complete network, and a complete network always contains a Hamiltonian cycle, so every vertex can then be visited exactly once.


Spec links: `spcpt_cm3fwdmGY3HDyvjV`


## Card 6 — fill_in_the_blanks (`fl_5btzdf9T5SMhyx9K`)

**FRONT**

Complete the triangle inequality, which every entry of a table of least distances has to satisfy:

`\text{length } AB \le \text{length } AC + \_\_\_\_\_\_`


**BACK**

The completed inequality is:

$\text{length} A B \leq \text{length} A C + \text{length} C B$

Here $A B$ is a longest length, so going round by way of $C$ can never beat going directly, which is what makes each entry a genuine least distance.


*Blanks: 0 — answers: []*

Spec links: `spcpt_cm3fwdmGY3HDyvjV`


## Card 7 — question_and_answer (`fl_vzM8gKS8HWZn9Rky`)

**FRONT**

You are filling in a row of a table of least distances. What must you check about each direct connection?


**BACK**

Check whether the **direct edge really is the shortest route** between that pair of vertices, since going round through others is sometimes quicker.

Where it is not, the shorter total is the value that belongs in the cell.


Spec links: `spcpt_cm3fwdmGY3HDyvjV`


## Card 8 — question_and_answer (`fl_nq7SxWBSVMr7wCZB`)

**FRONT**

Once a row of a table of least distances is complete, what can you fill in straight away?


**BACK**

The matching **column** for that same vertex, by copying the row's values down it.

A complete network is undirected, so the table is symmetrical about its leading diagonal.


Spec links: `spcpt_cm3fwdmGY3HDyvjV`


## Card 9 — question_and_answer (`fl_TRTWcTrZwvmsKWdJ`)

**FRONT**

Why is the travelling salesman problem usually tackled with bounds rather than solved outright?


**BACK**

Because there is **no efficient algorithm** that always finds the optimal solution.

Instead an upper and a lower bound are found, and the optimal route is known to lie somewhere between them.


Spec links: `spcpt_CDrxV4K9j3rBppb6` `spcpt_9YmCJGKWp5cKsBqG`


## Card 10 — fill_in_the_blanks (`fl_2gPQn4YQJZgfjBcG`)

**FRONT**

Complete the relationship that the two bounds establish:

`\_\_\_\_\_\_ \le \text{optimal solution} \le \_\_\_\_\_\_`


**BACK**

The completed relationship is:

$\text{lower bound} \leq \text{optimal solution} \leq \text{upper bound}$

The aim is to raise the lower bound and to lower the upper bound, so as to squeeze the interval the answer must lie in.


*Blanks: 0 — answers: []*

Spec links: `spcpt_CDrxV4K9j3rBppb6` `spcpt_9YmCJGKWp5cKsBqG`


## Card 11 — question_and_answer (`fl_F9hDdpkSgbVmBks8`)

**FRONT**

How do you find an initial upper bound for a travelling salesman problem from a minimum spanning tree?


**BACK**

Find a minimum spanning tree for the network, then **double its total weight**.

Doubling works because travelling out and back along every edge of the tree certainly visits every vertex and returns to the start.


Spec links: `spcpt_CDrxV4K9j3rBppb6`


## Card 12 — question_and_answer (`fl_7RVyTNH4xGXcyqBX`)

**FRONT**

How can an initial upper bound be improved?


**BACK**

By finding **shortcuts**, replacing a repeated stretch of the tree with a single edge that joins the same two vertices but is not in the tree.

The saving is the weight of the stretch less the weight of the shortcut.


Spec links: `spcpt_CDrxV4K9j3rBppb6`


## Card 13 — question_and_answer (`fl_9V3ZrxrYGcZdS8Kn`)

**FRONT**

An upper bound of $70$ is improved by replacing a repeated pathway of weight $30$ with a single edge of weight $14$. What is the new bound?


**BACK**

The new upper bound is $70 - 30 + 14 = 54$.

The saving is $30 - 14 = 16$, so the bound comes down by exactly that much.


Spec links: `spcpt_CDrxV4K9j3rBppb6`


## Card 14 — question_and_answer (`fl_crS99rq4JSfN8rBC`)

**FRONT**

How is a lower bound found by the deleted vertex method?


**BACK**

Remove one vertex together with all of its edges, find a minimum spanning tree of what is left, and note its total weight.

Then add back the **two shortest edges** that connect the removed vertex to that tree.


Spec links: `spcpt_9YmCJGKWp5cKsBqG`


## Card 15 — keyword_definition (`fl_7fwJHpTMTpBFsPxR`)

**FRONT**

What is a **residual minimum spanning tree**?


**BACK**

It is the minimum spanning tree of the network that remains once one vertex and all of its edges have been taken away.

Its weight forms the first part of a lower bound calculation.


Spec links: `spcpt_9YmCJGKWp5cKsBqG`


## Card 16 — question_and_answer (`fl_WK6kRNrFk4ZzMwg2`)

**FRONT**

In the deleted vertex method, why are exactly two edges added back to the residual minimum spanning tree?


**BACK**

Because in any tour the deleted vertex is **entered once and left once**, so it has to contribute exactly two edges.

Taking the two shortest available keeps the total as small as it can be, which is what makes the result a lower bound rather than just an estimate.


Spec links: `spcpt_9YmCJGKWp5cKsBqG`


## Card 17 — question_and_answer (`fl_NmfFWfTV9MS7m3M8`)

**FRONT**

Deleting a vertex leaves a residual tree of weight $28$, and the two shortest edges back to it are $7$ and $11$. What is the lower bound?


**BACK**

The lower bound is $28 + 7 + 11 = 46$.

The weight of the residual tree and the weights of the two reconnecting edges are simply added together.


Spec links: `spcpt_9YmCJGKWp5cKsBqG`


## Card 18 — question_and_answer (`fl_2hmWps2rPnDmX4Bn`)

**FRONT**

How does the nearest neighbour algorithm build a route?


**BACK**

From the current vertex it always takes the edge of least weight to an **unvisited** vertex, and repeats until every vertex has been reached.

One final edge is then added to return to the starting vertex.


Spec links: `spcpt_h68Jt9Vr3bmcy6FN`


## Card 19 — fill_in_the_blanks (`fl_ggKVgXDywxfzRnb9`)

**FRONT**

Complete the conditions a network must meet before the nearest neighbour algorithm can be used on it:

The network must be `\_\_\_\_\_\_` and must satisfy the `\_\_\_\_\_\_` inequality, and it needs at least three vertices.


**BACK**

The completed conditions are:

The network must be **complete** and must satisfy the **triangle** inequality, and it needs at least three vertices.

Where the network as given is not complete, a table of least distances has to be found first.


*Blanks: 0 — answers: ['complete', 'triangle']*

Spec links: `spcpt_h68Jt9Vr3bmcy6FN`

Flags: blank_answer_mismatch


## Card 20 — question_and_answer (`fl_9B6n9x52v6g2XJTv`)

**FRONT**

What does the nearest neighbour algorithm produce?


**BACK**

A low-weight **Hamiltonian cycle**, whose total weight serves as an **upper bound** for the travelling salesman problem.

It is not necessarily the least-weight cycle, and the best upper bound is the smallest one that can be found.


Spec links: `spcpt_h68Jt9Vr3bmcy6FN`


## Card 21 — true_or_false (`fl_YHRBy85Bghhj2Fkp`)

**FRONT**

**True or False?**

The nearest neighbour algorithm takes the shortest edge from any vertex already visited.


**BACK**

**False.**

Nearest neighbour looks only at the **current** vertex, taking the shortest edge from wherever it has just arrived.

It is **Prim's algorithm** that takes the shortest edge from any vertex already chosen, which is why the two are so easily muddled.


Spec links: `spcpt_h68Jt9Vr3bmcy6FN`


## Card 22 — question_and_answer (`fl_pJcMZCBhS7DTKJDS`)

**FRONT**

What is the only method guaranteed to solve the travelling salesman problem exactly?


**BACK**

Listing **every possible Hamiltonian cycle** and taking whichever has the least weight.

Nothing is known that finds the shortest cycle without doing this, so the method is only ever practical on small networks.


Spec links: `spcpt_vM8dxJfRb45N35rV`


## Card 23 — fill_in_the_blanks (`fl_R6pcgszpRV5k5gdR`)

**FRONT**

Complete the count of Hamiltonian cycles in a complete network with $n$ vertices:

`\text{number of cycles from a fixed start} = \left(n - \_\_\_\_\_\_\right)!`


**BACK**

The completed count is:

`\text{number of cycles from a fixed start} = \left(n - 1\right)!`

Fixing the starting vertex and then arranging all the remaining vertices in every possible order is what produces this.


*Blanks: 0 — answers: []*

Spec links: `spcpt_vM8dxJfRb45N35rV`


## Card 24 — true_or_false (`fl_wmjnhBCJVf9cRxnr`)

**FRONT**

**True or False?**

Reversing a Hamiltonian cycle produces a route with a different total weight.


**BACK**

**False.**

A reversed cycle uses exactly the same edges as the original, so its total weight is identical.

That is why the number of genuinely different tours is only **half** the number of listings.


Spec links: `spcpt_vM8dxJfRb45N35rV`


## Card 25 — question_and_answer (`fl_Y5w67HHPDnxNxVVS`)

**FRONT**

A network has $6$ vertices. Why is listing every Hamiltonian cycle not a sensible way to solve it?


**BACK**

Because there are $120$ of them, which is far too many to work through by hand.

The number grows factorially with the number of vertices, so the method becomes hopeless very quickly indeed.


Spec links: `spcpt_vM8dxJfRb45N35rV`


## Card 26 — question_and_answer (`fl_Wgzry8D27gGTC87W`)

**FRONT**

Why must a network be complete before its travelling salesman problem can be solved by listing Hamiltonian cycles?


**BACK**

Because a Hamiltonian cycle is only the optimal answer when every vertex is joined directly to every other one.

In an incomplete network the best route may have to pass through some vertex twice, which no Hamiltonian cycle ever does.


Spec links: `spcpt_vM8dxJfRb45N35rV`


## Card 27 — question_and_answer (`fl_BTzxJRqRbQF4fMYY`)

**FRONT**

You have found a route and you already know the lower bound. When can you say the route is optimal?


**BACK**

When the route's weight is **equal to the lower bound**.

No route at all can be shorter than the lower bound, so one that matches it exactly cannot be beaten.


Spec links: `spcpt_vM8dxJfRb45N35rV`


## Card 28 — question_and_answer (`fl_WBSV352PYBNtDPrR`)

**FRONT**

What is the essential difference between the travelling salesman and route inspection problems?


**BACK**

The salesman has to reach every **vertex**, because that is where the selling happens, and may leave edges unused.

The postman has to travel every **edge**, because that is where the letters are delivered, and may pass through a vertex several times.


Spec links: `spcpt_vM8dxJfRb45N35rV`

