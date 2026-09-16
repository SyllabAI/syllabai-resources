# Mark Schemes — The Route Inspection Algorithm
**Algorithms on Graphs** · Edexcel International A Level (IAL) Maths (YMA01) — Decision 1


## Q1 — medium — 15 marks · exam-questions

### 4((a)) — 6 marks
Dijkstra's algorithm settles the towns in order of increasing time from $A$, recording at each one its order of labelling, its final value, and every working value tried on the way

Each time a town receives its final value, look along the roads leaving it and replace any neighbouring working value that can now be beaten

| Vertex | Order of labelling | Final value | Working values |
|---|---|---|---|
| **A** | *1* | *0* | *0* |
| **B** | *6* | *19* | *21, 20, 19* |
| **D** | *5* | *17* | *17* |
| **E** | *3* | *15* | *15* |
| **F** | *4* | *16* | *16* |
| **G** | *7* | *24* | *24* |
| **H** | *8* | *29* | *30, 29* |
| **J** | *2* | *13* | *13* |
| **K** | *9* | *32* | *38, 34, 33, 32* |

**[M1 A1 A1 A1]**

A working value is written down only when it improves on the one already there, so nothing is recorded at $F$ when $E$ offers 22, at $B$ when $E$ offers 20, or at $G$ when $F$ offers 26

Trace the route back from $K$, keeping any step where the gap between two final values is exactly the time on the road joining them

$K$ has final value 32 and $H K$ takes 3, and $H$ has final value 29, so $H$ lies on the route

The same test gives $G$ at 24, then back to $A$

**Final answer:** **A – G – H – K**

**[A1]**

$\text{shortest time} = 32  \text{minutes}$

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces a larger working value with a smaller one at least once, at $B$ or at $H$ or at $K$.
> 
> **A1**: All values at J, E, F and D correct, with the working values in the correct order.
> 
> **A1**: All values at B and G correct, with the working values in the correct order.
> 
> **A1**: All values at H and K correct, with the working values in the correct order. Follow through from your earlier values.
> 
> **A1**: The route A, G, H, K and no other.
> 
> **A1**: The time 32. Follow through from your own final value at K, and a missing unit is condoned.
> 
> The order of the working values inside a box is marked, not just the set of them. At K they must read 38, 34, 33, 32 in that order.
> 
> An error in the order of labelling is penalised only once in the whole question. B and G must be labelled in that order, and B must be labelled after J, E, F and D. H and K must be labelled in that order, and H must be labelled after every other town except K.
> 
> Additional working values of 22 at F, 20 at B and 26 at G are condoned, since each is a genuine candidate that simply fails to improve on the value already there.

> **[exam-tip]**
> Take the order of labelling from the final values, never from the picture. $J$ is labelled second, at 13, even though Figure 1 draws it on the far side of the network, because the single road $A J$ beats every route to $E$ or to $F$.
> 
> - The shortest route out of $A$ starts along $A G$, which at 24 is the slowest road leaving $A$, so guessing the route off the diagram will not work
> - Trace back from $K$ instead, one final value at a time

### 4((b)) — 2 marks
A journey from $B$ to $K$ that must include $A$ splits at $A$ into the quickest route from $B$ to $A$, followed by the quickest route from $A$ to $K$

The roads run both ways, so the first half is the part (a) route to $B$ written backwards, and its time is the final value at $B$

The second half is the route already found in part (a), and its time is the final value at $K$

**Final answer:** **B – D – E – A – G – H – K**

**[B1]**

$19 + 32$

$\text{shortest time} = 51  \text{minutes}$

**[B1]**

> **[mark-scheme]**
> **B1**: The route B, D, E, A, G, H, K and no other.
> 
> **B1**: The time 51. Follow through as your own final value at B added to your own final value at K, and a missing unit is condoned.

> **[exam-tip]**
> There is no need to run Dijkstra's algorithm again from $B$. Part (a) has already found the quickest route from $A$ to every town, and a road takes the same time in either direction.
> 
> - Splitting the journey at the named town turns it into two problems that are both already solved
> - The two halves share only $A$, so their times simply add

### 4((c)) — 7 marks
Oliver has to travel along every road at least once and return to his starting point, so this is a route inspection problem

A closed route repeating nothing exists only when every town has even degree, so start by counting the roads at each town

$D$ has degree 2, and $E$, $G$, $J$ and $K$ have degree 4, so the odd towns are $A$, $B$, $F$ and $H$

Four odd towns can be paired up in three ways, and each pairing is joined by its quickest route

Pair $A$ to $B$ through $E$ and $D$, and $F$ to $H$ through $G$

`\left(15 + 2 + 2\right) + \left(10 + 5\right) = 34`

Pair $A$ to $F$ directly, and $B$ to $H$ through $K$

`16 + \left(15 + 3\right) = 34`

Pair $A$ to $H$ through $G$, and $B$ to $F$ through $D$ and $E$

`\left(24 + 5\right) + \left(2 + 2 + 7\right) = 40`

**[M1 A1 A1 A1]**

The first two pairings tie at 34 minutes, so there are two different sets of roads Oliver could repeat, and the question asks for both

**Final answer:** **Repeat the roads AF, BK and KH**

**[A1]**

**Final answer:** **Or repeat the roads AE, ED, DB, FG and GH**

**[A1]**

The inspection time is the total of every road in Figure 1 plus the repeat total

$196 + 34 = 230$

$\text{shortest time} = 230  \text{minutes}$

**[A1]**

> **[mark-scheme]**
> **M1**: Three distinct pairings of the correct four odd nodes, $A$, $B$, $F$ and $H$.
> 
> **A1**: One row correct, including both its pairing and its total.
> 
> **A1**: Two rows correct, including pairings and totals.
> 
> **A1**: All three rows correct, including pairings and totals.
> 
> **A1**: A correct answer only for one of the two sets of roads that have to be repeated.
> 
> **A1**: A correct answer only for both sets.
> 
> **A1**: A correct answer only, 230.
> 
> The roads must be named as roads, explicitly stated and not implied by the working above them. Writing a path such as AEDB, or describing one indirectly as A to B through E and D, does not earn the answer marks.
> 
> Follow through is allowed on the three row marks if you use your own final values at B, F and H from part (a), but for the lengths of AB, AF and AH only.

> **[exam-tip]**
> Two pairings tie at 34 here, which is why the question asks for all the combinations rather than just the time. A tie costs nothing extra in the arithmetic and everything in the answer if you stop at the first one.
> 
> - Join each pair by its quickest route, not by the direct road: there is no road at all from $B$ to $H$, and the 18 comes from going through $K$
> - The 196 is printed under Figure 1, so only the repeat total has to be added to it

## Q2 — medium — 16 marks · exam-questions

### 2((a)) — 6 marks
Dijkstra's algorithm settles the towns in order of increasing distance from $A$, recording at each one its order of labelling, its final value, and every working value tried on the way

Each time a town receives its final value, look along the roads leaving it and replace any neighbouring working value that can now be beaten

| Vertex | Order of labelling | Final value | Working values |
|---|---|---|---|
| **A** | *1* | *0* | *0* |
| **B** | *2* | *4* | *4* |
| **C** | *3* | *7* | *7* |
| **D** | *4* | *8* | *8* |
| **E** | *5* | *15* | *17, 15* |
| **F** | *8* | *27* | *30, 29, 28, 27* |
| **G** | *7* | *24* | *24* |
| **H** | *6* | *20* | *21, 20* |
| **J** | *9* | *28* | *34, 31, 29, 28* |

**[M1 A1 A1 A1]**

A working value is written down only when it improves on the one already there, so nothing is recorded at $D$ when $B$ offers 14

Trace the path back from $J$, keeping any step where the gap between two final values is exactly the length of the road joining them

$J$ has final value 28 and $F J$ is 1 mile, and $F$ has final value 27, so $F$ lies on the path

The same test gives $G$ at 24, then $D$ at 8, then back to $A$

**Final answer:** **A – D – G – F – J**

**[A1]**

$\text{length} = 28  \text{miles}$

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces a larger working value with a smaller one at least twice, among the working values at E, F, H and J.
> 
> **A1**: All values at B, C, D and E correct, with the working values in the correct order.
> 
> **A1**: All values at H and G correct, with the working values in the correct order.
> 
> **A1**: All values at F and J correct, with the working values in the correct order. Follow through from your earlier values.
> 
> **A1**: The path A, D, G, F, J and no other. It must be given in that direction, not the other way round as J, F, G, D, A.
> 
> **A1**: The length 28. Follow through from your own final value at J only, so 28 written down when your own final value at J is something else earns nothing.
> 
> The order of the working values inside a box is marked, not just the set of them. At H they must read 21, 20 in that order, and 20, 21 is not accepted.
> 
> The order of labelling must be strictly increasing. Repeating a number, as in 1, 2, 3, 3, 4, is penalised once; skipping numbers, as in 1, 2, 3, 5, 6, is not penalised at all. Errors in the final and working values are penalised before any error in the order of labelling.
> 
> An additional working value of 14 at D is condoned, since it is a genuine candidate that fails to improve on the 8 already there.

> **[exam-tip]**
> Two of the nine boxes here hold four working values each, so leave yourself room at $F$ and $J$. $F$ is improved three times, from 30 down to 27, and each of those improvements has to be visible and in the right order.
> 
> - $A F$ is a direct road of 30 miles and the shortest way from $A$ to $F$ is 27, so the direct road is not on the path at all
> - Read the path back from $J$ one final value at a time, and write it out in the direction the question asked for

### 2((b)) — 2 marks
A journey from $J$ to $H$ that must pass through $A$ splits at $A$ into the shortest path from $J$ to $A$, followed by the shortest path from $A$ to $H$

The roads run both ways, so the first half is the part (a) path written backwards, and its length is the final value at $J$

The second half runs $A$, $B$, $C$, $E$, $H$, and its length is the final value at $H$

**Final answer:** **J – F – G – D – A – B – C – E – H**

**[B1]**

$28 + 20$

$\text{length} = 48  \text{miles}$

**[B1]**

> **[mark-scheme]**
> **B1**: The path J, F, G, D, A, B, C, E, H and no other. Naming the roads instead, as JF, FG, GD, DA, AB, BC, CE, EH, is equally acceptable.
> 
> **B1**: The length 48. Follow through as your own final value at J added to your own final value at H.

> **[exam-tip]**
> Part (a) has already found the shortest distance from $A$ to every town, so both halves of this journey are done. Only the second half is new, and it is read straight off the final value at $H$.
> 
> - The two halves meet at $A$ and share nothing else, so their lengths simply add
> - Going directly from $J$ to $H$ would be 11 miles, but the question requires the detour through $A$

### 2((c)) — 5 marks
Jan has to travel along every road at least once and return to $A$, so this is a route inspection problem

A closed route repeating nothing exists only when every town has even degree, so start by counting the roads at each town

$C$ has degree 2, $D$, $H$ and $J$ have degree 4 and $B$ has degree 6, so the odd towns are $A$, $E$, $F$ and $G$

Four odd towns can be paired up in three ways, and each pairing is joined by its shortest path

Pair $A$ to $E$ through $B$ and $C$, and $F$ to $G$ directly

`\left(4 + 3 + 8\right) + 3 = 18`

Pair $A$ to $G$ through $D$, and $E$ to $F$ through $H$

`\left(8 + 16\right) + \left(5 + 8\right) = 37`

Pair $A$ to $F$ through $D$ and $G$, and $E$ to $G$ through $H$ and $F$

`\left(8 + 16 + 3\right) + \left(5 + 8 + 3\right) = 43`

**[M1 A1 A1]**

The first pairing is the cheapest at 18 miles, so those are the roads Jan repeats

**Final answer:** **Repeat the roads AB, BC, CE and FG**

**[A1]**

The inspection route is the total of every road in Figure 1 plus the repeat total

$193 + 18 = 211$

$\text{length} = 211  \text{miles}$

**[A1]**

> **[mark-scheme]**
> **M1**: Three distinct pairings of the nodes $A$, $E$, $F$ and $G$.
> 
> **A1**: Any two rows correct, including both their pairings and their totals.
> 
> **A1**: All three rows correct, including pairings and totals.
> 
> **A1**: A correct answer only, with the roads clearly stated as AB, BC, CE and FG. Reversed names such as BA and CB are accepted.
> 
> **A1**: The length 211. Follow through as 193 plus your own least total from a choice of three.
> 
> The roads must be stated as roads and not left inside the working above. Writing the path ABCE, or describing the repeat as A to E via B and C, does not earn that mark.
> 
> Note that the first accuracy mark here needs any TWO rows complete, so one correct row on its own earns nothing beyond the method mark.

> **[exam-tip]**
> The cheapest pairing is not the one joining the two towns that look closest together. $F$ and $G$ are 3 miles apart, but what makes this pairing win is that it leaves $A$ and $E$ to be joined for 15 rather than $A$ to $F$ for 27.
> 
> - Cost the pairing as a whole, never one half of it
> - The 193 is printed under Figure 1, so only the repeat total has to be added to it

### 2((d)) — 3 marks
A route that starts and finishes at different towns leaves those two towns odd, so they are the two that are not paired

$G$ is fixed as the start, so $G$ is never paired, and the finish is whichever of $A$, $E$ and $F$ is left over

That leaves exactly one pair to join, and there are three ways to choose it

Finishing at $F$ would repeat the path from $A$ to $E$ through $B$ and $C$

$4 + 3 + 8 = 15$

Finishing at $E$ would repeat the path from $A$ to $F$ through $D$ and $G$

$8 + 16 + 3 = 27$

Finishing at $A$ would repeat the path from $E$ to $F$ through $H$

$5 + 8 = 13$

**[M1]**

The path from $E$ to $F$ is the cheapest of the three at 13 miles, and it is the least of the three paths that do not involve $G$

**Final answer:** **The route should finish at A**

**[A1]**

$193 + 13 = 206$

$\text{length} = 206  \text{miles}$

**[A1]**

> **[mark-scheme]**
> **M1**: Identifies that exactly one of the paths AE, AF and EF has to be repeated, or lists those three as the only possibilities. This mark depends on either the method mark in part (c) or on all three paths being listed here.
> 
> **A1**: Identifies EF as the least and $A$ as the finishing point. EF must be explicitly named as the least path not involving $G$.
> 
> **A1**: A correct answer only, 206.
> 
> Listing more than these three paths is allowed provided it is clear from the working that only these three are actually being considered. Stating just two of them, such as AE and AF, is enough for the method mark, as long as nothing in the working suggests that a path through $G$ should be repeated.

> **[exam-tip]**
> An open inspection route saves you the cost of joining the start to the finish, so the two odd towns you leave unpaired are exactly those two. Fixing the start at $G$ therefore fixes $G$ as unpaired and leaves only the finish to choose.
> 
> - Three odd towns remain and one pair is joined, so there are three cases and not six
> - The cheapest of them is 13 against the 18 of part (c), so the open route is 5 miles shorter

## Q3 — medium — 15 marks · exam-questions

### 6((a)) — 6 marks
Dijkstra's algorithm settles the towns in order of increasing time from $A$, recording at each one its order of labelling, its final value, and every working value tried on the way

Diagram 1 already gives the entries at $A$ and the entries at $J$, and neither of the roads into $H$ carries the unknown, so $H$ can be labelled in the ordinary way

| Vertex | Order of labelling | Final value | Working values |
|---|---|---|---|
| **A** | *1* | *0* | *0* |
| **B** | *4* | *31* | *34, 31* |
| **C** | *3* | *23* | *24, 23* |
| **D** | *2* | *12* | *12* |
| **E** | *6* | *52* | *58, 52* |
| **F** | *5* | *39* | *43, 39* |
| **G** | *7* | *61* | *66, 61* |
| **H** | *8* | *71* | *74, 73, 71* |
| **J** | *9* | $61 + x$ | $91 , 61 + x$ |

**[M1 A1 A1 A1]**

The final value at $H$ is the fastest time from $A$

$\text{fastest time} = 71  \text{minutes}$

**[A1]**

Trace the route back from $H$, keeping any step where the gap between two final values is exactly the time on the road joining them

$H$ has final value 71 and $G H$ takes 10, and $G$ has final value 61, so $G$ lies on the route

The same test gives $B$ at 31, then $C$ at 23, then $D$ at 12, then back to $A$

**Final answer:** **A – D – C – B – G – H**

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces a larger value with a smaller one at least twice, among the working values at B, C, E, F, G and H.
> 
> **A1**: All values at D, C and B correct, with the working values in the correct order.
> 
> **A1**: All values at F and E correct, with the working values in the correct order.
> 
> **A1**: All values at G and H correct, with the working values in the correct order. Follow through from your earlier values.
> 
> **A1**: The time 71. Follow through from your own final value at H only, so 71 given when your own final value at H is something else earns nothing.
> 
> **A1**: A correct answer only for the route, A, D, C, B, G, H.
> 
> The order of the working values inside a box is marked, not just the set of them. At H they must read 74, 73, 71 in that order, and 74, 71, 73 is not accepted.
> 
> The order of labelling must be strictly increasing. Repeating a number, as in 1, 2, 3, 3, 4, is penalised once; skipping numbers, as in 1, 2, 3, 5, 6, is not penalised at all. Errors in the final and working values are penalised before any error in the order of labelling.

> **[exam-tip]**
> The unknown never reaches $H$. $x$ sits on $G J$, and $J$ is labelled last of all, so nothing that depends on $x$ is ever used to improve another town.
> 
> - That is why Diagram 1 hands you $J$ already filled in: it is not needed for this part, but part (b) uses it
> - $H$ is improved twice, from 74 to 73 to 71, and the last of those comes from $G$ rather than from the direct road out of $C$

### 6((b)) — 6 marks
Ezra travels every road at least once and returns to $A$, so this is a route inspection problem

Counting the roads at each town gives $A$, $D$, $E$ and $H$ as the odd ones

Four odd towns can be paired up in three ways, and each pairing is joined by its quickest route

Pair $A$ to $D$ directly, and $E$ to $H$ directly

$12 + 21 = 33$

Pair $A$ to $E$ through $D$, $C$ and $B$, and $D$ to $H$ through $C$, $B$ and $G$

$52 + 59 = 111$

Pair $A$ to $H$ through $D$, $C$, $B$ and $G$, and $D$ to $E$ through $C$ and $B$

$71 + 40 = 111$

**[M1 A1 A1 A1]**

The cheapest pairing repeats 33 minutes, so the inspection route is every road once plus 33, and that is at least 440

`\left(383 + x\right) + 33 \geq 440`

**[M1]**

$x \geq 24$

Diagram 1 supplies the other end. The working values at $J$ improve from 91 to $61 + x$, so the second of those has to be the smaller

$61 + x < 91$

$x < 30$

$24 \leq x < 30$

**[A1]**

> **[mark-scheme]**
> **M1**: Three distinct pairings of the nodes A, D, E and H.
> 
> **A1**: Any one row correct, including both its pairing and its total.
> 
> **A1**: Any two rows correct, including pairings and totals.
> 
> **A1**: All three rows correct, including pairings and totals.
> 
> **M1**: Forms 383 + x plus your own least pairing total, set against 440. This mark depends on the first method mark in this part. Any inequality sign is accepted, and so is an equals sign.
> 
> **A1**: A correct answer only, 24 is less than or equal to x, which is less than 30. Writing the upper end as x less than or equal to 29 is condoned.
> 
> All three distinct pairings of the four odd nodes must be shown. The benefit of the doubt is given if not every total is written out, provided the one used really is the least of those shown.

> **[exam-tip]**
> Only the lower end of the range comes from the route inspection. The upper end is already sitting in Diagram 1, in the fact that $61 + x$ was written to the right of 91 rather than the other way round.
> 
> - A working value is only ever recorded because it improves on the one before it, so $61 + x < 91$ is information the diagram gives you for free
> - The 33 is the least of the three totals, so a bigger pairing would give a smaller lower bound for $x$ and a wrong answer

### 6((c)) — 1 marks
The route travels every road in Figure 4 once, and the repeated roads $A D$ and $E H$ a second time

Start at $A$ and walk the network, taking each repeated road twice where it is convenient to do so

**Final answer:** **ABCADCEBGCFHEHGJFDA**

**[B1]**

> **[mark-scheme]**
> **B1**: Any correct route. It may be given as a list of arcs instead.
> 
> A route can be checked against four things: it starts and finishes at A, it holds 19 nodes, the roads AD and EH each appear twice, and the towns are visited A three times, C three times, J once, and B, D, E, F, G and H twice each.

> **[exam-tip]**
> There are many correct routes here and no way to be marked down for choosing an awkward one, so take the roads in whatever order keeps the pen on the paper.
> 
> - $J$ has only two roads at it, to $F$ and to $G$, so any route arrives along one of them and leaves along the other
> - Count the nodes when you have finished: 16 roads plus 2 repeats is 18 steps, so 19 towns are written down

### 6((d)) — 2 marks
Adding a direct road from $D$ to $H$ gives each of them one more road, so both become even

*A and E are then the only odd towns, so the route repeats just the quickest route from A to E*

That quickest route runs $A$, $D$, $C$, $B$, $E$, and part (b) has already costed it at 52 minutes

The inspection route is now every road in Figure 4, plus the new road, plus that repeat

`\left(383 + x\right) + 25 + 52 = 488`

**[M1]**

$460 + x = 488$

$x = 28$

**[A1]**

> **[mark-scheme]**
> **M1**: Forms 383 + x, plus 25 for the new road, plus your own shortest path from A to E. Your own 52 must be the length of your shortest path from A to E in part (a) or part (b), or you must state or imply here that it is 52. A correct value of 28 with no working implies this mark only.
> 
> **A1**: A correct answer only, 28, from correct working together with correct reasoning. The reasoning has to say that A and E are now the only odd nodes, or that only A and E need pairing. Naming A and E is enough; any mention of the new road from D to H is ignored.

> **[exam-tip]**
> One new road removes two odd towns at once, because it touches both of them. Four odd towns become two, so one path is repeated instead of two and the whole pairing table from part (b) is thrown away.
> 
> - The new road is part of the network now, so its 25 minutes is added to the 383 as well as being available to walk along
> - Check the answer against part (b): 28 does lie in the range found there, which it has to

## Q4 — medium — 10 marks · exam-questions

### 5((a)) — 3 marks
Chan must travel along every road at least once and return to his starting point, so this is a route inspection problem

A closed route that repeats nothing exists only when every vertex has even degree, so start by counting the roads at each vertex

$A$, $B$, $E$, $F$ and $G$ each have degree 4, and $H$ and $J$ have degree 2

That leaves $C$ with degree 5 and $D$ with degree 3

*The odd vertices are C and D*

**[B1]**

Two odd vertices give a single pairing, joined by the shortest route between them

The quickest way from $C$ to $D$ runs through $F$ and $G$, which beats the direct road $C D$ at 8 minutes

Add that to the total weight of the network, given under Figure 4 as 82

`82 + \left(1 + 3 + 3\right) = 89`

$\text{shortest time} = 89  \text{minutes}$

**[B1]**

Now write down a route that uses every road once and the three repeated roads twice, starting and finishing at $G$

**Final answer:** **A possible route is GCABCDAEBFCFEHJGDGFG**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, stating that C and D are the odd vertices. Naming C and D, or CD, without saying that they are odd earns nothing. Stating the repeated arcs CF, FG and DG instead also earns this mark.
> 
> **B1**: A correct answer only, 89. The unit is not required.
> 
> **B1**: Any correct route.
> 
> A route can be checked against four things: it starts and finishes at G, it lists 20 vertices, the arcs CF, FG and DG each appear twice, and the vertices are visited A twice, B twice, C three times, D twice, E twice, F three times, G four times, H once and J once.

> **[exam-tip]**
> Count the degrees first, because the number of odd vertices tells you how much work the question holds. Two odd vertices mean one pairing and no table to draw.
> 
> - The shortest route between the odd vertices is not the direct road here: $C D$ takes 8 minutes but $C$ to $F$ to $G$ to $D$ takes only 7
> - Write the route out from the network rather than from your head, and check each repeated road really does appear twice

### 5((b)) — 5 marks
A route that starts and finishes at different vertices leaves exactly those two vertices odd, and every other vertex even

$B$ and $G$ both have degree 4, so both have to be made odd, while $C$ and $D$ are odd already and have to be made even

So all four of $B$, $C$, $D$ and $G$ are paired up, and four vertices can be paired in three ways

Pair $B$ to $C$ through $F$, and $D$ to $G$ directly

`\left(5 + 1\right) + 3 = 9`

Pair $B$ to $D$ through $F$ and $G$, and $C$ to $G$ through $F$

`\left(5 + 3 + 3\right) + \left(1 + 3\right) = 15`

Pair $B$ to $G$ through $F$, and $C$ to $D$ through $F$ and $G$

`\left(5 + 3\right) + \left(1 + 3 + 3\right) = 15`

**[M1 A1 A1 A1]**

The first pairing is the cheapest at 9 minutes, so those are the roads Chan repeats

**Final answer:** **Repeat the roads BF, CF and DG**

**[A1]**

> **[mark-scheme]**
> **M1**: Three distinct pairings of the correct four odd nodes, B, C, D and G.
> 
> **A1**: Any one row correct, including both its pairing and its total.
> 
> **A1**: Any two rows correct, including their pairings and their totals.
> 
> **A1**: All three rows correct, including their pairings and their totals.
> 
> **A1**: A correct answer only, with the arcs clearly stated as BF, CF and DG.
> 
> The arcs must be stated as the answer and not left inside the working above. BC is refused, and so are BFC and any description such as BC via F: the answer is the three arcs themselves.

> **[exam-tip]**
> A start and a finish that are already even is the case that catches people out. $B$ and $G$ have to become odd, so they join the pairing rather than dropping out of it, and two odd vertices turn into four.
> 
> - The rule is the same every time: after the repeats, every vertex is even except the start and the finish
> - Three of the four marks here are for the rows, so write all three totals out even once you can see which is smallest

### 5((c)) — 2 marks
Both routes travel every road at least once, so both start from the same total weight of 82 and differ only in what they repeat

The closed route from $G$ repeats 7 minutes of road, and the open route from $B$ to $G$ repeats 9

$82 + 9 = 91$

$91 - 89 = 2$

**[B1]**

So the open route from $B$ takes 2 minutes longer

**Final answer:** **The route starting at G is quicker**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only. Saying instead that the route from B to G is the slower of the two is accepted, provided it is clear that the route starting at G is the quicker one.
> 
> **B1**: A correct answer only. The difference of 2, or a comparison of 89 with 91, or a comparison of the repeat totals 7 and 9, all earn it.
> 
> The first mark depends on the repeated arcs found in parts (a) and (b) being correct, and that may be implied rather than restated, either by the earlier parts or by correct values used here.

> **[exam-tip]**
> The whole comparison is already done once you have the two repeat totals, since the 82 is common to both routes. Comparing 7 with 9 answers the question just as well as comparing 89 with 91.
> 
> - Being allowed to finish somewhere other than where you started does not automatically make a route shorter, and here it makes it longer

## Q5 — medium — 10 marks · exam-questions

### 5((a)) — 6 marks
Lance must cycle along every lane at least once and return to his starting point, so this is a route inspection problem

A closed route that repeats nothing exists only when every vertex has even degree, so start by counting the lanes at each vertex

$B$, $F$, $G$, $H$ and $J$ each have degree 4, so they need nothing doing to them

$A$, $D$ and $E$ have degree 3 and $C$ has degree 5, so those four are the odd vertices and all four have to be paired up

Four vertices can be paired in three ways, and each pairing is joined by the shortest route between its two ends

Pair $A$ to $C$ through $D$ and $G$, and $D$ to $E$ through $G$ and $H$

`\left(5 + 3 + 4\right) + \left(3 + 5 + 1\right) = 21`

Pair $A$ to $D$ directly, and $C$ to $E$ through $G$ and $H$

`5 + \left(4 + 5 + 1\right) = 15`

Pair $A$ to $E$ through $D$, $G$ and $H$, and $C$ to $D$ through $G$

`\left(5 + 3 + 5 + 1\right) + \left(4 + 3\right) = 21`

**[M1 A1 A1 A1]**

The second pairing is the cheapest at 15 km, so those are the lanes Lance repeats

**Final answer:** **Repeat the cycle lanes AD, CG, GH and EH**

**[A1]**

The length of the route is the total of every lane, given under Figure 3 as 166, plus the total of the repeated ones

$166 + 15 = 181$

$\text{length of the route} = 181  \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: Three distinct pairings of the correct four odd nodes, A, C, D and E.
> 
> **A1**: Any one row correct, including both its pairing and its total.
> 
> **A1**: Any two rows correct, including their pairings and their totals.
> 
> **A1**: All three rows correct, including their pairings and their totals.
> 
> **A1**: The arcs of the smallest pairing, accepted as AD, CG, GH and EH and no others.
> 
> **A1**: The length 181. Follow through as 166 plus your own least total, so a length that is consistent with a wrong smallest pairing still earns it.
> 
> The pairings must be costed by the shortest route between the two ends, not by the direct lane where one exists. C to D is 11 directly but only 7 through G, and A to C is 15 directly but only 12 through D and G.

> **[exam-tip]**
> Four odd vertices always give exactly three pairings, and the marks here are mostly for producing all three rather than for spotting the winner.
> 
> - Work out the shortest route between each pair before you start, since five of the six pairs here are joined through other vertices rather than by a direct lane
> - The two losing pairings both total 21, so a single arithmetic slip in either one is enough to change which pairing looks smallest

### 5((b)) — 1 marks
Count the lanes at $C$ rather than writing the route out

$C$ has degree 5 in Figure 3, and the repeated lane $C G$ gives it one more, so six lane ends meet at $C$ in the inspection route

Every visit to $C$ arrives along one lane and leaves along another, so it uses two of those six

**Final answer:** **Vertex C appears 3 times**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 3.

> **[exam-tip]**
> Counting a vertex from the degrees is far quicker and far safer than writing out a route and counting the letters.
> 
> - A vertex that is neither the start nor the finish appears half as many times as the number of lane ends meeting it, once the repeats are added in
> - The start of a closed route is the exception, because it is both left at the beginning and returned to at the end

### 5((c)) — 3 marks
A route that starts and finishes at different vertices leaves exactly those two vertices odd, and every other vertex even

$A$ is fixed as the start, so $A$ is allowed to stay odd and the finishing vertex is whichever of $C$, $D$ and $E$ is left odd as well

Whichever is chosen, the other two have to be paired, and all three of those shortest routes are already worked out in part (a)

Finishing at $C$ leaves $D$ to $E$ to pair through $G$ and $H$

$3 + 5 + 1 = 9$

Finishing at $D$ leaves $C$ to $E$ to pair through $G$ and $H$

$4 + 5 + 1 = 10$

Finishing at $E$ leaves $C$ to $D$ to pair through $G$

$4 + 3 = 7$

**[M1]**

The smallest of the three is $C$ to $D$ at 7 km, which is the least of the routes that avoid $A$, so that is the pairing to repeat and the vertex left over is the finish

**Final answer:** **The route finishes at E**

**[A1]**

Only 7 km is repeated now instead of the 15 km of part (a)

$166 + 7 = 173$

$\text{length of the route} = 173  \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: Identifies that one of the three paths DE, CE and CD has to be repeated, all three of which avoid A. This may be implicit in the working, and as a minimum stating one of these three paths earns it. It depends on either the method mark in part (a) or all three paths being stated here.
> 
> **A1**: Identifies C to D through G as the least of the paths that do not include A, and E as the finishing point. The leastness must be stated explicitly, either by listing CD, CE and DE with no others, or by saying that CD is the least of those that avoid A. Saying only that CD is the least is not enough.
> 
> **A1**: A correct answer only, 173.

> **[exam-tip]**
> The start and the finish are the two vertices you are allowed to leave odd, so an open route saves you the cost of pairing them. With $A$ fixed, the job is to pick the finish that leaves the cheapest pairing behind.
> 
> - $A$ is one of the odd vertices here, which is what makes an open route worth having: the three paths to compare are exactly the ones that do not touch $A$
> - What decides the finish is the cost of pairing the two vertices you leave behind, not how far the finish itself is from $A$

## Q6 — medium — 13 marks · exam-questions

### 4((a)) — 2 marks
Every entry is the shortest distance between two towns, which is not always the direct road

$A$ to $C$ has no direct road, and the shortest way round is $A$ to $E$ at 25, then $E$ to $F$ at 6, then $F$ to $C$ at 11

$C$ to $D$ has no direct road either, and the shortest is $C$ to $F$ at 11, then $F$ to $E$ at 6, then $E$ to $D$ at 15

$D$ to $F$ does have a direct road of 23, but going through $E$ costs only 15 and 6

|   | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| **A** | - | 21 | **Final answer:** **42** | 17 | 25 | 31 | 41 |
| **B** | 21 | - | 26 | 27 | 12 | 15 | 20 |
| **C** | **Final answer:** **42** | 26 | - | **Final answer:** **32** | 17 | 11 | 46 |
| **D** | 17 | 27 | **Final answer:** **32** | - | 15 | **Final answer:** **21** | 47 |
| **E** | 25 | 12 | 17 | 15 | - | 6 | 32 |
| **F** | 31 | 15 | 11 | **Final answer:** **21** | 6 | - | 35 |
| **G** | 41 | 20 | 46 | 47 | 32 | 35 | - |

**[B1] [B1]**

> **[mark-scheme]**
> **B1**: At least two of the six values correct in either copy of the table.
> 
> **B1**: All six values correct in both copies of the table.
> 
> The three distances are 42 for AC, 32 for CD and 21 for DF, and each appears twice because the table is symmetric. Two copies of the same value, as 42 in both cell AC and cell CA, count as two of the six for the first mark.
> 
> The direct road from $D$ to $F$ is 23, so 23 is the answer a student gets by reading Figure 3 rather than looking for a shorter route. It is not accepted, because the table records least distances.

> **[exam-tip]**
> Check every entry you write against the possibility of a shorter route through a third town, because a direct road is not automatically the shortest way.
> 
> - $D$ to $F$ is the trap here: there is a road, and it is longer than the route through $E$
> - $E$ and $F$ are only 6 apart and sit near the middle of the network, so most short cuts run through one of them

### 4((b)) — 2 marks
The nearest neighbour algorithm starts at $A$ and repeatedly moves to the nearest town not yet visited, then returns to $A$ at the end

From $A$ the nearest is $D$ at 17, then $E$ at 15, then $F$ at 6, then $C$ at 11, then $B$ at 26

*A – D – E – F – C – B*

**[M1]**

Only $G$ is left, at 20 from $B$, and then the route closes back to $A$ at 41

**Final answer:** **A – D – E – F – C – B – G – A**

$17 + 15 + 6 + 11 + 26 + 20 + 41$

$\text{upper bound} = 136  \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: Applies nearest neighbour from $A$ with at least the first six towns correct, A, D, E, F, C and B.
> 
> **A1**: A correct answer only, covering both the length 136 and the route, which must return to $A$. The route may be stated as a list of arcs instead of a list of towns.
> 
> Work from the completed table rather than from Figure 3, since the algorithm needs a distance between every pair of towns.

> **[exam-tip]**
> Cross out each town's column as you visit it, so the nearest unvisited town is the smallest uncrossed entry in the current row.
> 
> - The last two legs, 20 and 41, are forced rather than chosen, which is why they are the longest
> - $G$ is 41 from $A$ and at least 20 from everywhere, so leaving it late is expensive however you order the rest

### 4((c)) — 1 marks
The table holds least distances, so a leg of the route may pass through towns that are not named in it

$C$ to $B$ is 26, which is $C$ to $F$ at 11 then $F$ to $B$ at 15, and $G$ to $A$ is 41, which is $G$ to $B$ at 20 then $B$ to $A$ at 21

**Final answer:** **A – D – E – F – C – F – B – G – B – A**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, ADEFCFBGBA, or the same route given as a list of arcs.
> 
> Every other leg of the part (b) route is a single road, so only those two legs expand.

> **[exam-tip]**
> Compare each leg of your route with Figure 3 and expand only the legs whose length does not appear there as a single road.
> 
> - Two legs expand here, which is why $F$ and $B$ each appear twice in the answer
> - A quick check is that the expanded route still has the same total length, since the legs were shortest paths to begin with

### 4((d)) — 3 marks
Deleting $A$ leaves the six towns $B$ to $G$, and a lower bound is the minimum spanning tree of what is left plus the two shortest arcs back to $A$

The residual minimum spanning tree uses $E F$ at 6, $C F$ at 11, $B E$ at 12, $D E$ at 15, $B G$ at 20

$6 + 11 + 12 + 15 + 20 = 64$

**[B1]**

The two shortest arcs at $A$ are $A D$ at 17 and $A B$ at 21, and both are added on separately

$64 + 17 + 21$

**[M1]**

$\text{lower bound} = 102  \text{km}$

**[A1]**

> **[mark-scheme]**
> **B1**: The weight of the residual minimum spanning tree is 64. This may be seen as the sum 12 + 6 + 11 + 15 + 20, or implied by correct later working in the lower bound calculation.
> 
> **M1**: Adds the weight of the residual tree to the two smallest arcs at $A$, 17 and 21. A residual weight anywhere from 58 to 70 is allowed.
> 
> **A1**: A correct answer only, 102.
> 
> A bare 102 with no working at all scores the method and accuracy marks but not the first mark.

> **[exam-tip]**
> Build the residual tree from the table with row $A$ and column $A$ struck out, not from Figure 3, because the bound is about least distances.
> 
> - Five arcs for six towns, so a residual tree built from four or six arcs has gone wrong
> - The two arcs at $A$ are the two smallest entries in row $A$, and they are added separately rather than as a single 38

### 4((e)) — 5 marks
Clive travels along the roads themselves, not between least distances, so this is a route inspection problem on Figure 3

A route that starts and finishes at the same vertex needs every vertex to be even; one that starts at $A$ and finishes at $G$ needs $A$ and $G$ to be odd and everything else even

Counting the roads at each vertex gives $C$ degree 3 and $E$ degree 5, with $A$, $B$, $D$, $F$ and $G$ all even

So four vertices have the wrong parity, $A$, $C$, $E$ and $G$, and they can be paired up in three ways, each pairing joined by its shortest path

Pair $A$ to $C$ and $E$ to $G$

$42 + 32 = 74$

Pair $A$ to $E$ and $C$ to $G$

$25 + 46 = 71$

Pair $A$ to $G$ and $C$ to $E$

$41 + 17 = 58$

**[M1 A1 A1]**

The last pairing is the cheapest at 58, and both of its paths run through a third town: $A$ to $G$ goes through $B$ and $C$ to $E$ goes through $F$

**Final answer:** **Repeat the roads AB, BG, CF and EF**

**[A1]**

The length is every road once plus the repeated ones a second time

$291 + 58$

$\text{length of the route} = 349  \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: The correct three pairings of the correct four odd nodes, $A$, $C$, $E$ and $G$.
> 
> **A1**: Any two of the three rows correct, including both the pairings and the totals.
> 
> **A1**: All three rows correct, including pairings and totals.
> 
> **A1**: A correct answer only, with the repeated roads clearly stated as the arcs AB, BG, CF and EF rather than being left inside the working.
> 
> **A1**: The length 349. Follow through as 291 plus your own smallest pairing total.
> 
> The answer must name arcs, not a path. Writing AG, or ABG, or AG through B, does not earn the mark, and the same applies to CE.
> 
> $A$ and $G$ are even in Figure 3 and are still paired, because the route has to start at one and finish at the other. That is what makes this an open route inspection rather than the usual closed one.

> **[exam-tip]**
> The start and finish of an open route are the two vertices you want left odd, so add them to the genuinely odd list before pairing rather than after.
> 
> - Here that turns two odd vertices into four, and so turns one pairing into three
> - $A$ and $G$ end up paired with each other in the winning combination, which looks odd but is simply the cheapest of the three
> 
> Each pairing is costed by the shortest path, which is often not the direct road.
> 
> - $A$ to $G$ is 45 by road but only 41 through $B$, and $C$ to $E$ is 19 by road but only 17 through $F$
> - Both of those short cuts matter here, since the winning pairing uses them, and taking the direct roads instead would give 64 rather than 58

## Q7 — medium — 17 marks · exam-questions

### 5((a)) — 6 marks
Dijkstra's algorithm settles the cities in order of increasing distance from $A$, recording at each one its order of labelling, its final value, and every working value tried on the way

Each time a city receives its final value, look along the roads leaving it and replace any neighbouring working value that can now be beaten

| Vertex | Order of labelling | Final value | Working values |
|---|---|---|---|
| **A** | *1* | *0* | *0* |
| **B** | *2* | *13* | *13* |
| **C** | *3* | *20* | *22, 20* |
| **D** | *4* | *35* | *35* |
| **E** | *5* | *36* | *36* |
| **F** | *6* | *41* | *45, 44, 41* |
| **G** | *7* | *47* | *47* |
| **H** | *10* | *68* | *70, 68* |
| **J** | *9* | *67* | *69, 67* |
| **K** | *8* | *62* | *63, 62* |

**[M1 A1 A1 A1]**

A working value is written down only when it improves on the one already there, so nothing is recorded at $E$ when $D$ offers 45

Trace the path back from $H$, keeping any step where the gap between two final values is exactly the length of the road joining them

$H$ has final value 68 and $H K$ is 6 miles, and $K$ has final value 62, so $K$ lies on the path

The same test gives $G$ at 47, then $D$ at 35, then $B$ at 13, then back to $A$

**Final answer:** **A – B – D – G – K – H**

**[A1]**

$\text{length} = 68  \text{miles}$

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces a larger working value with a smaller one at least once.
> 
> **A1**: All values at A, B, C, D and E correct, with the working values in the correct order.
> 
> **A1**: All values at F, G and K correct, with the working values in the correct order.
> 
> **A1**: All values at J and H correct, with the working values in the correct order. Follow through from your earlier values.
> 
> **A1**: The path A, B, D, G, K, H and no other.
> 
> **A1**: The length 68. Follow through from your own final value at H, and a missing unit is condoned.
> 
> The order of the working values inside a box is marked, not just the set of them. At F they must read 45, 44, 41 in that order.
> 
> The order of labelling must be strictly increasing. Repeating a number, as in 1, 2, 3, 3, 4, is penalised once; skipping numbers, as in 1, 2, 3, 5, 6, is not penalised at all. Errors in the final and working values are penalised before any error in the order of labelling.
> 
> An additional working value of 45 at E is condoned, since it is a genuine candidate that fails to improve on the 36 already there.

> **[exam-tip]**
> $F$ sits in the middle of Figure 1 with six roads at it, and it is still not on the shortest path to $H$. The path goes the long way round the top instead, through $D$ and $G$.
> 
> - $F$ is improved twice before it settles, at 45, then 44, then 41, and all three have to be written in that order
> - $K$ is reached from $G$ at 62 rather than from $F$ at 63, and that single mile is what sends the whole path round the top

### 5((b)) — 2 marks
A journey from $F$ to $K$ that must include $A$ splits at $A$ into the shortest route from $F$ to $A$, followed by the shortest route from $A$ to $K$

The roads run both ways, so the first half is the shortest route from $A$ to $F$ written backwards, and its length is the final value at $F$

The second half is the opening of the part (a) path, and its length is the final value at $K$

**Final answer:** **F – E – C – B – A – B – D – G – K**

**[B1]**

$41 + 62$

$\text{length} = 103  \text{miles}$

**[B1]**

> **[mark-scheme]**
> **B1**: The route F, E, C, B, A, B, D, G, K and no other. A list of arcs is equally acceptable, as FE, EC, CB, BA, AB, BD, DG, GK.
> 
> **B1**: The length 103. Follow through as your own final value at F added to your own final value at K.

> **[exam-tip]**
> The two halves both use the road $A B$, so it is travelled twice and the route doubles back on itself. That is allowed, and trying to avoid it only makes the journey longer.
> 
> - The road out of $A$ towards $C$ is 22 miles, against 13 to $B$ and 7 on to $C$, so even reaching $C$ is quicker through $B$
> - Both lengths are read straight off the final values, so nothing has to be added up along the route

### 5((c)) — 6 marks
An inspection route that starts and finishes at different cities leaves exactly those two cities odd, and every other city even

In Figure 1 the odd cities are $C$ and $E$, while $A$ and $J$ are both even

So $C$ and $E$ have to be made even, and $A$ and $J$ have to be made odd, which means all four of them are paired up

Four cities can be paired in three ways, and each pairing is joined by its shortest route

Pair $A$ to $J$ through $B$, $D$, $G$ and $K$, and $C$ to $E$ directly

$67 + 16 = 83$

Pair $A$ to $C$ through $B$, and $E$ to $J$ through $F$ and $K$

`\left(13 + 7\right) + \left(5 + 22 + 5\right) = 52`

Pair $A$ to $E$ through $B$ and $C$, and $C$ to $J$ through $E$, $F$ and $K$

$36 + 48 = 84$

**[M1 A1 A1 A1]**

The second pairing is the cheapest at 52 miles, so those are the roads James repeats

**Final answer:** **Repeat the roads AB, BC, EF, FK and JK**

**[A1]**

The inspection route is every road in Figure 1 once, plus the repeat total

$253 + 52 = 305$

$\text{length} = 305  \text{miles}$

**[A1]**

> **[mark-scheme]**
> **M1**: Three distinct pairings of the correct four odd nodes, A, C, E and J.
> 
> **A1**: Any one row correct, including both its pairing and its total.
> 
> **A1**: Any two rows correct, including pairings and totals.
> 
> **A1**: All three rows correct, including pairings and totals.
> 
> **A1**: A correct answer only, with the arcs clearly stated as AB, BC, EF, FK and JK. They must be these arcs, and not left inside the working above.
> 
> **A1**: The length 305. Follow through as 253 plus your own smallest pairing total.

> **[exam-tip]**
> The pairing that wins is the one joining $A$ to the nearest odd city rather than the one joining the two odd cities to each other. $C$ and $E$ are only 16 miles apart, and pairing them still gives the worst of the three rows once $A$ has to reach $J$.
> 
> - Five roads are repeated here, because two of the three shortest routes have several roads in them
> - Read each repeated road off the route it belongs to, and write it as a road rather than as the pairing it came from

### 5((d)) — 1 marks
A city is entered and left once on each pair of roads meeting there, so a city of even degree $d$ that is not an end of the route appears $d \div 2$ times

$F$ has degree 6 in Figure 1, and the repeated roads $E F$ and $F K$ add two more, giving 8

$F$ is neither the start nor the finish, so the 8 roads pair up into 4 visits

**Final answer:** **James passes through F 4 times**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 4.

> **[exam-tip]**
> Count the roads at the city, remembering to add the repeated ones, and then halve. Writing the whole route out and counting the letters gives the same answer far more slowly.
> 
> - Only $E F$ and $F K$ of the five repeated roads touch $F$, so the degree goes from 6 to 8 and not to 10

### 5((e)) — 1 marks
The route starts at $D$ and may finish anywhere, so $D$ has to end up odd and the finishing city has to end up odd as well

$C$ and $E$ are already odd, so finishing at one of those two leaves only two cities to pair, while finishing anywhere else leaves four

Finishing at $C$ asks only for $D$ to become odd and $E$ to become even, which joins $D$ to $E$ along the road between them

$10$

Finishing at $E$ would instead join $D$ to $C$, and every finish outside $C$ and $E$ costs at least 17

$26$

**Final answer:** **The new inspection route will finish at C**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, C.

> **[exam-tip]**
> Choosing the finish is choosing which cities you do not have to pair. Finishing at a city that is already odd halves the job, because only two cities are left with the wrong parity instead of four.
> 
> - That narrows the choice to $C$ and $E$ straight away, and then it is a single comparison between 10 and 26
> - $D$ and $E$ are joined directly by a 10 mile road, and no repeat anywhere in Figure 1 is cheaper

### 5((f)) — 1 marks
The route in part (c) repeats 52 miles of road, and the new route from $D$ to $C$ repeats only the 10 miles of $D E$

Both routes travel every road in Figure 1 once, so the difference between them is just the difference between the two repeat totals

`305 - \left(253 + 10\right) = 42`

$\text{difference} = 42  \text{miles}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 42.

> **[exam-tip]**
> The 253 cancels, so the answer is 52 minus 10 and there is no need to work out either route length in full.
> 
> - Subtracting the repeat totals is the quick route, and it is also the one least likely to go wrong

## Q8 — medium — 11 marks · exam-questions

### 7((a)) — 7 marks
Dijkstra's algorithm settles the towns in order of increasing time from $A$, recording at each one its order of labelling, its final value, and every working value tried on the way

The two roads into $H$ carry the unknown $x$, so $H$ is the one town that cannot be labelled: its three working values cannot be put in order until $x$ is known

Every other town is labelled as usual, and each of the three roads into $H$ then gives one working value there

| Vertex | Order of labelling | Final value | Working values |
|---|---|---|---|
| **A** | *1* | *0* | *0* |
| **B** | *2* | *10* | *10* |
| **C** | *4* | *20* | *22, 21, 20* |
| **D** | *3* | *18* | *20, 18* |
| **E** | *5* | *23* | *25, 23* |
| **F** | *6* | *27* | *29, 27* |
| **G** | *7* | *36* | *36* |
| **H** |   |   | $70 , 37 + 2 x , 51 + x$ |

**[M1 A1 A1 A1]**

Reading back from each of $D$, $E$ and $G$ gives the three routes into $H$, and any of them could be the quickest depending on $x$

**Final answer:** **A – B – D – H, taking **$70$** minutes**

**[A1]**

**Final answer:** **A – B – D – E – H, taking **$37 + 2 x$** minutes**

**[A1]**

**Final answer:** **A – B – D – E – G – H, taking **$51 + x$** minutes**

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces a larger working value with a smaller one in at least two of the working value boxes, at any town other than A, B, G and H. Doing it once at H also earns it, provided at least two working values are shown there.
> 
> **A1**: All values at A, B, D and C correct, with the working values in the correct order at D and C, and with the order of labelling correct.
> 
> **A1**: All values at E and F correct, with the working values in the correct order.
> 
> **A1**: All values at G and H correct, with the working values at H in the correct order. Follow through from your earlier values.
> 
> **A1**: The route A, B, D, H, of length 70.
> 
> **A1**: The route A, B, D, E, H, of length 37 + 2x.
> 
> **A1**: The route A, B, D, E, G, H, of length 51 + x.
> 
> The permanent label and the final value at H are ignored, since neither can be decided without a value for x. Unsimplified expressions in x are accepted for the working values at H, so 23 + 14 + 2x need not be tidied to 37 + 2x.
> 
> The order of the working values inside a box is marked, not just the set of them. At C they must read 22, 21, 20 in that order, and 22, 20, 21 is not accepted. The same applies at H, although the benefit of the doubt is given there.
> 
> The order of labelling must be strictly increasing. Repeating a number, as in 1, 2, 3, 3, 4, is penalised once; skipping numbers, as in 1, 2, 3, 5, 6, is not penalised at all. Errors in the final and working values are penalised before any error in the order of labelling.
> 
> If none of the last three marks is earned, one mark is still available for stating all three routes correctly, or for stating all three lengths explicitly rather than leaving them in the working values at H.

> **[exam-tip]**
> $H$ is deliberately unlabellable, and that is the whole question rather than a snag in it. Leave its order of labelling and its final value blank, and write all three working values in.
> 
> - Take the working values at $H$ in the order their feeding towns were labelled: $D$ is third, $E$ fifth and $G$ seventh, giving 70, then 37 + 2x, then 51 + x
> - Each route is read back from its feeding town in the ordinary way, so all three share the opening $A$, $B$, $D$

### 7((b)) — 4 marks
A closed inspection route repeating nothing exists only when every town has even degree, so count the roads at each town

$F$ and $G$ have degree 2, $B$, $C$ and $E$ have degree 4 and $D$ has degree 6, so $A$ and $H$ are the only odd towns

*With only two odd towns there is one pairing, so the repeated roads form a shortest path from A to H*

**[M1]**

Malcolm repeats exactly four roads, and of the three routes in part (a) only $A$, $B$, $D$, $E$, $H$ uses four roads, so that is the path repeated

The inspection route is every road in Figure 3 once, plus that path a second time

$205 + 3 x + 37 + 2 x = 307$

**[M1]**

$5 x = 65$

$x = 13$

**[A1]**

Now put $x = 13$ into the three route lengths from part (a)

$37 + 2 \times 13 = 63$

$51 + 13 = 64$

The route through $D H$ takes 70 minutes whatever $x$ is, so 63 is the smallest of the three

$\text{minimum time} = 63  \text{minutes}$

**[A1]**

> **[mark-scheme]**
> **M1**: Shows that the repeated roads form a path from A to H. As a minimum, states that A and H are the odd nodes of the network. Naming A and H without saying that they are the odd ones is not enough.
> 
> **M1**: Forms the equation 3x + 205 + 37 + 2x = 307, using one of your own paths involving x.
> 
> **A1**: A correct answer only, x = 13. This mark depends on the second method mark only.
> 
> **A1**: A correct answer only, 63. This mark depends on the second method mark only.
> 
> Stating a route from A to H that has five nodes, or simply stating the need to repeat a path or route from A to H, also earns the first method mark. It is awarded for making the method clear rather than for any particular wording.
> 
> If neither method mark is earned, correct answers of x = 13 and 63 together score one mark, awarded as an independent mark for the 63.

> **[exam-tip]**
> The phrase "exactly four roads twice" is the clue that fixes the repeated path before any algebra happens. $A$, $B$, $D$, $H$ uses three roads, $A$, $B$, $D$, $E$, $H$ uses four, and $A$, $B$, $D$, $E$, $G$, $H$ uses five.
> 
> - Count roads, not towns: the four road route has five towns in it
> - Check the answer back, because the repeated path has to be the shortest one: at $x = 13$ it costs 63 against 64 and 70, so it is

## Q9 — medium — 15 marks · exam-questions

### 6((a)) — 6 marks
Dijkstra's algorithm settles the towns in order of increasing time from $A$, recording at each one its order of labelling, its final value, and every working value tried on the way

Each time a town receives its final value, look along the roads leaving it and replace any neighbouring working value that can now be beaten

| Vertex | Order of labelling | Final value | Working values |
|---|---|---|---|
| **A** | *1* | *0* | *0* |
| **B** | *4* | *12* | *14, 12* |
| **C** | *2* | *5* | *5* |
| **D** | *5* | *20* | *22, 20* |
| **E** | *3* | *7* | *8, 7* |
| **F** | *6* | *24* | *26, 24* |
| **G** | *8* | *35* | *43, 39, 35* |
| **H** | *7* | *26* | *33, 27, 26* |
| **J** | *9* | *45* | *49, 46, 45* |

**[M1 A1 A1 A1]**

The final value at $J$ is the shortest time from $A$

$\text{shortest time} = 45  \text{minutes}$

**[A1]**

Trace the route back from $J$, keeping any step where the gap between two final values is exactly the time on the road joining them

$J$ has final value 45 and $G J$ takes 10, and $G$ has final value 35, so $G$ lies on the route

The same test gives $F$ at 24, then $D$ at 20, then $B$ at 12, then $C$ at 5, then back to $A$

**Final answer:** **A – C – B – D – F – G – J**

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces a larger value with a smaller one in at least two of the working value boxes, at any town other than A and C.
> 
> **A1**: All values at C, E, B and D correct, with the working values in the correct order, and the order of labelling correct.
> 
> **A1**: All values at F and H correct, with the working values in the correct order. F and H must be labelled in that order, and F must be labelled after C, E, B and D.
> 
> **A1**: All values at G and J correct, with the working values in the correct order. Follow through from your earlier values.
> 
> **A1**: The time 45. Follow through from your own final value at J only, so 45 given when your own final value at J is something else earns nothing. A missing unit is condoned.
> 
> **A1**: A correct answer only for the route, in either direction, so ACBDFGJ or JGFDBCA.
> 
> The order of the working values inside a box is marked, not just the set of them. At J they must read 49, 46, 45 in that order, and 49, 45, 46 is not accepted.
> 
> The order of labelling must be strictly increasing. Repeating a number, as in 1, 2, 3, 3, 4, is penalised once; skipping numbers, as in 1, 2, 3, 5, 6, is not penalised at all. Errors in the final and working values are penalised before any error in the order of labelling.

> **[exam-tip]**
> $E$ is labelled third, at 7, even though the direct road $A E$ takes 8. Going the long way round through $C$ is quicker, and that improvement is the first thing the algorithm finds.
> 
> - Three boxes here need three working values, at $H$, $G$ and $J$, so give yourself room on the right of each
> - The quickest route uses none of the four longest roads in Figure 3, so do not try to pick it out by eye

### 6((b)) — 5 marks
An inspection route that starts and finishes at different towns leaves exactly those two towns odd, and every other town even

In Figure 3 the odd towns are $A$ and $J$, while $H$ and $D$ are both even

So $A$ and $J$ have to be made even, and $H$ and $D$ have to be made odd, which means all four of them are paired up

Four towns can be paired in three ways, and each pairing is joined by its quickest route

Pair $A$ to $D$ through $C$ and $B$, and $H$ to $J$ directly

`\left(5 + 7 + 8\right) + 20 = 40`

Pair $A$ to $H$ through $C$, $B$, $D$ and $F$, and $D$ to $J$ through $F$ and $G$

`\left(5 + 7 + 8 + 4 + 2\right) + \left(4 + 11 + 10\right) = 51`

Pair $A$ to $J$ through $C$, $B$, $D$, $F$ and $G$, and $D$ to $H$ through $F$

`45 + \left(4 + 2\right) = 51`

**[M1 A1 A1 A1]**

The first pairing is the cheapest at 40 minutes, so those are the roads Alan repeats

**Final answer:** **Repeat the roads AC, BC, BD and HJ**

**[A1]**

> **[mark-scheme]**
> **M1**: Three distinct pairings of the correct four odd nodes, A, D, H and J.
> 
> **A1**: Any one row correct, including both its pairing and its total.
> 
> **A1**: Any two rows correct, including pairings and totals.
> 
> **A1**: All three rows correct, including pairings and totals.
> 
> **A1**: A correct answer only, with the arcs clearly stated as AC, BC, BD and HJ.
> 
> The arcs must be stated and not left inside the working above. AD is refused, and so are ACBD and any description such as A to D through B and C: the answer is the four arcs themselves.

> **[exam-tip]**
> A start and a finish that are already even is the case that catches people out. $H$ and $D$ have to become odd, so they join the pairing rather than being excluded from it, and two odd towns turn into four.
> 
> - The test is always the same: after the repeats, every town is even except the start and the finish
> - Pairing $A$ with $J$ is the worst of the three here at 51, even though they are the only naturally odd towns

### 6((c)) — 2 marks
A town is entered and left once on each pair of roads meeting there, so a town of even degree $d$ that is not an end of the route appears $d \div 2$ times

Repeating a road adds one to the degree at each of its ends, so add the repeats from part (b) before counting

**(i)**

$C$ has degree 6 in Figure 3, and the repeated roads $A C$ and $B C$ add two more, giving 8

**Final answer:** **Vertex C appears 4 times**

**[B1]**

**(ii)**

$D$ has degree 4 in Figure 3, and the repeated road $B D$ adds one more, giving 5

$D$ is the finish, so it is left one time fewer than it is entered, and 5 roads at $D$ give 3 appearances

**Final answer:** **Vertex D appears 3 times**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 4.
> 
> **B1**: A correct answer only, 3.

> **[exam-tip]**
> Count the roads at the town, not the letters in a route you have written out. Writing the whole route out to count the letters works, but it is slow and one wrong turn changes the answer.
> 
> - Add the repeated roads to the degree first, then halve
> - An odd total means the town is an end of the route, and there the count rounds up

### 6((d)) — 2 marks
Closing the route at $H$ makes $H$ an ordinary town again, so it no longer has to be odd

*A and J are then the only odd towns, so a closed route from H repeats only the quickest route between A and J*

**[B1]**

That quickest route is the one found in part (a), and its time is the final value at $J$

The closed route is every road in Figure 3 once, plus that route a second time

$269 + 45 = 314$

The route from $H$ to $D$ repeats only 40 minutes instead

$269 + 40 = 309$

$314 > 309$

**Final answer:** **It is quicker to start at H and finish at D**

**[B1]**

> **[mark-scheme]**
> **B1**: Correct reasoning that a closed route from H would repeat only the shortest path between A and J. As a minimum this needs either the words "A to J only", or A and J named as the only odd nodes. Naming them as odd nodes without saying they are the only ones is not enough.
> 
> **B1**: The conclusion, together with a correct numerical argument. Quoting 314 and 309, or 45 and 40, without comparing the two values does not earn it.
> 
> Either form of the conclusion is accepted: that closing the route at H would be slower, or that starting at H and finishing at D is quicker.

> **[exam-tip]**
> The whole comparison rests on the repeat totals, so there is no need to work out either route in full. 45 against 40 settles it just as well as 314 against 309.
> 
> - Whichever pair you quote, write the comparison down: a bare pair of numbers and the word "slower" is not an argument
> - Closing the route costs more here because $A$ and $J$ are far apart, at 45 minutes, while pairing them off against $H$ and $D$ costs only 40

## Q10 — medium — 18 marks · exam-questions

### 3((a)) — 2 marks
A lower bound comes from the total number of pupils: even if every tour group were filled exactly to its limit, this many groups would still be needed

Add the ten school sizes

$8 + 17 + 9 + 14 + 18 + 12 + 22 + 10 + 15 + 7 = 132$

Divide the total by the maximum size of one tour group

$\frac{132}{42} = 3 . 14 \dots$

Tour groups come whole, so round up rather than to the nearest whole number

$\text{lower bound} = 4  \text{tour groups}$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Attempts the total number of pupils divided by 42. A value of 3.14 or better seen with no working can imply this mark.
> 
> **A1**: A correct solution only, meaning the correct calculation, or 3.14 followed by 4. A value of 3.1 is accepted provided the correct calculation is also seen.
> 
> An answer of 4 with no working at all scores nothing in this part, so the division has to be visible.

> **[exam-tip]**
> The lower bound is the quotient rounded up, never rounded to the nearest whole number, so 3.14 gives 4 even though it is much closer to 3.
> 
> - Write the division down even if your calculator does it in one step, because the answer alone earns nothing here
> - A lower bound only rules out fewer groups, but it is worth knowing the target before you start: part (b) turns out to reach it

### 3((b)) — 2 marks
First-fit works along the list in its original order, putting each school into the first tour group that still has room for it

Each tour group holds at most 42 pupils

8 opens Group 1, and 17 joins it at 25

9 also fits in Group 1, taking it to 34, but 14 does not, so it opens Group 2

18 joins 14 in Group 2 at 32, and 12 fits in neither, so it opens Group 3

22 joins 12 in Group 3 at 34, and 10 completes Group 2 at exactly 42

15 fits in none of the three, so it opens Group 4, and 7 fills Group 1 to 41

**Final answer:** **Group 1: 8, 17, 9, 7**

**Final answer:** **Group 2: 14, 18, 10**

**Final answer:** **Group 3: 12, 22**

**Final answer:** **Group 4: 15**

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Places the first six items, 8, 17, 9, 14, 18 and 12, correctly and puts at least eight items into groups.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> Writing cumulative running totals beside each group instead of the numbers of pupils is condoned for the method mark only.

> **[exam-tip]**
> Four groups matches the lower bound from part (a), so first-fit has already found the best possible allocation here. That is luck rather than a property of the algorithm, and part (d) shows the sorted version doing no better.
> 
> - Always rescan from Group 1 for each new school, which is why the 7 travels back into a group opened at the very start
> - Pupils from one school must stay together, which is what makes this a bin packing question rather than a division

### 3((c)) — 4 marks
A quick sort picks a pivot, then splits the list into the numbers that belong before it and the numbers that belong after it

The specification fixes the pivot as the middle item, at position `\frac{1}{2} \left(N + 1\right)` when $N$ is odd and `\frac{1}{2} \left(N + 2\right)` when $N$ is even

The list is being sorted into descending order, so the larger numbers go to the left of the pivot

Pivots are shown in brackets, and every pivot already placed stays fixed for the rest of the sort

Ten numbers gives a first pivot at position 6, which is 12

*8, 17, 9, 14, 18, (12), 22, 10, 15, 7*

Five numbers are larger than 12 and four are smaller, so the next two sublists have five and four numbers, with pivots at positions 3 and 3

*17, 14, (18), 22, 15, 12, 8, 9, (10), 7*

**[M1 A1]**

Only 22 lies above 18, and 10 is the largest of its own sublist, so 8, 9 and 7 all fall below it

*(22), 18, 17, (14), 15, 12, 10, 8, (9), 7*

14 leaves 17 and 15 above it and nothing below, and 9 likewise has nothing above it, with 8 and 7 below

*22, 18, 17, (15), 14, 12, 10, 9, 8, (7)*

**[A1]**

No sublist now holds more than one number, so the sort is complete

**Final answer:** **22, 18, 17, 15, 14, 12, 10, 9, 8, 7**

**[A1]**

> **[mark-scheme]**
> **M1**: Chooses a pivot and produces a first pass giving the numbers above the pivot, then the pivot, then the numbers below it. The pivot must be the middle left or the middle right item; choosing the first or the last item scores nothing.
> 
> **A1**: The first pass correct, and the pivots for the second pass chosen correctly, which for the middle right choice are 18 and 10, or 14 for the middle left. The second pass does not itself have to be correct for this mark.
> 
> **A1**: The second and third passes correct. Allow follow through from your own first pass and choice of pivots, and you are not required to choose a pivot for the fourth pass for this mark.
> 
> **A1**: A fully correct solution, including a fourth pass in which 15 and 7 are used as pivots, or a fifth pass using 8 if you are choosing the middle left item throughout.
> 
> Choosing only one pivot per iteration, rather than one in each sublist, limits this part to the method mark.
> 
> Sorting into ascending order and then reversing the list can still score full marks. If the list is not reversed, the last two accuracy marks are lost, and if you say it needs reversing without showing the reversed list, the final mark goes. Where you sort into ascending order, the statement that the sort is complete has to appear before the list is reversed.

> **[exam-tip]**
> The fourth pass changes nothing at all here, and it is still required: 15 and 7 have to be used as pivots before the sort can be declared finished. A list that already looks sorted is not evidence that the algorithm has terminated.
> 
> - Recount the length of each sublist before picking its pivot, because the position rule applies to the sublist and not to the original ten numbers
> - From the second pass onwards you choose a pivot in every sublist at once, not one pivot for the whole list
> - Sorting into ascending order is allowed, but the reversal has to be shown and the completion statement has to come first

### 3((d)) — 2 marks
First-fit decreasing works down the sorted list from part (c), putting each school into the first tour group that can still take it

Each tour group holds at most 42 pupils

22 opens Group 1, and 18 joins it at 40

17 will not fit beside them, so it opens Group 2, and 15 joins it at 32

14 fits in neither, so it opens Group 3, and 12 joins it at 26

10 completes Group 2 at exactly 42, and 9 joins Group 3 at 35

8 fits in none of the three, so it opens Group 4, and 7 fills Group 3 to exactly 42

**Final answer:** **Group 1: 22, 18**

**Final answer:** **Group 2: 17, 15, 10**

**Final answer:** **Group 3: 14, 12, 9, 7**

**Final answer:** **Group 4: 8**

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Places the first six items, 22, 18, 17, 15, 14 and 12, correctly and puts at least eight items into groups.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> Writing cumulative running totals beside each group instead of the numbers of pupils is condoned for the method mark only.

> **[exam-tip]**
> First-fit decreasing also uses four groups here, so it has not improved on part (b). Sorting first usually helps and is not guaranteed to, and where plain first-fit has already matched the lower bound there is nothing left to gain.
> 
> - Two groups fill to exactly 42 here, which is a useful check that nothing has overflowed
> - The allocation is different from part (b) even though the number of groups is the same, so the two answers are not interchangeable

### 3((e)) — 4 marks
Sally has to travel along every corridor at least once and return to her starting point, so this is a route inspection problem

A closed route repeating nothing exists only when every vertex has even degree, so start by counting the arcs at each vertex

$A$ and $D$ have degree 2, and $E$, $F$, $I$ and $J$ have degree 4, so the odd vertices are $B$, $C$, $G$ and $H$, each of degree 3

Four odd vertices can be paired up in three ways, and each pairing is joined by its shortest path

Pair $B$ to $C$ through $E$, and $G$ to $H$ through $I$

`\left(11 . 2 + 14 . 5\right) + \left(8 . 3 + 17 . 2\right) = 51 . 2`

Pair $B$ to $G$ through $F$, and $C$ to $H$ through $E$ and $J$

`\left(10 . 3 + 15 . 2\right) + \left(14 . 5 + 7 . 5 + 16 . 2\right) = 63 . 7`

Pair $B$ to $H$ through $E$ and $J$, and $C$ to $G$ through $E$ and $F$

`\left(11 . 2 + 7 . 5 + 16 . 2\right) + \left(14 . 5 + 4 . 3 + 15 . 2\right) = 68 . 9`

**[M1 A1 A1]**

The first pairing is the cheapest, so those are the corridors Sally repeats

**Final answer:** **Repeat the corridors BE, CE, GI and HI**

**[A1]**

> **[mark-scheme]**
> **M1**: The correct three pairings of the correct four odd nodes, $B$, $C$, $G$ and $H$.
> 
> **A1**: Any one of the three rows correct, including both its pairing and its total.
> 
> **A1**: All three rows correct, including pairings and totals.
> 
> **A1**: A correct answer only, with the arcs clearly stated as BE, CE, GI and HI.
> 
> The official scheme stages the first three marks over the same table of pairings, so all three depend on it: the method mark on the pairings being the right ones, then a mark for one row complete and a mark for all three.
> 
> The final mark is for the four arcs themselves. Naming paths instead, such as BEC or GIH, does not earn it, and neither does describing an arc indirectly, such as BC through E.

> **[exam-tip]**
> Count the degrees before anything else. With four odd vertices there are exactly three pairings to test, and with two there would be only one, so the number of odd vertices tells you immediately how much work the question holds.
> 
> - Each pairing must use the shortest path between the two vertices, which is not always the direct arc: $G$ to $H$ is 27.3 directly but only 25.5 through $I$
> - Write out all three totals even once you can see which is smallest, since two of the four marks are for the rows rather than for the answer
> - The answer is a list of arcs, so name each one by its two endpoints and do not run them together into a path

### 3((f)) — 2 marks
A shortest route travels every corridor once and the four repeated corridors a second time, and it must start and finish at $A$

Build it by walking the network, taking each repeated corridor twice in succession where that is convenient

**Final answer:** **A possible route is ABEBFECEJIFGIGHIHJDCA**

**[B1]**

The length is the total of every corridor in the museum plus the total of the four repeated ones

$227 . 2 + 51 . 2 = 278 . 4$

$\text{length} = 278 . 4  \text{m}$

**[B1]**

> **[mark-scheme]**
> **B1**: Any correct route.
> 
> **B1**: The correct length. Allow follow through as 227.2 plus your own smallest repeat total from part (e), provided at least two of the three totals were written down there and the method mark in part (e) was earned.
> 
> A route can be checked against four things: it has 21 vertices, it starts and ends at $A$, the arcs BE, CE, GI and HI each appear twice, and the vertices are visited $A$ twice, $B$ twice, $C$ twice, $D$ once, $E$ three times, $F$ twice, $G$ twice, $H$ twice, $I$ three times and $J$ twice.

> **[exam-tip]**
> There are many correct routes and only one correct length, so the length is the safer of the two marks. Work it out from the total network weight rather than by adding up your own route, which is slow and easy to get wrong.
> 
> - The 227.2 is given under Figure 2, so it does not have to be calculated
> - Check your route by counting how many times each vertex appears: a vertex of degree 3 that gains a repeated arc becomes degree 4 and so is passed through twice

### 3((g)) — 2 marks
A route that starts and finishes at different vertices leaves those two vertices odd, so only the other two odd vertices need pairing

$H$ is fixed as the start, so the choice is which of $B$, $C$ and $G$ becomes the finish

Whichever is chosen, the remaining two must be joined by their shortest path, and those three paths are already worked out in part (e)

Finishing at $B$ would repeat $C$ to $G$ at 34.0, finishing at $G$ would repeat $B$ to $C$ at 25.7, and finishing at $C$ would repeat $B$ to $G$ at 25.5, which is the smallest

**Final answer:** **The finishing vertex is C**

**[B1]**

The saving is the repeat total from part (f) less the new repeat total, which is the path from $B$ to $G$ through $F$

`51 . 2 - \left(10 . 3 + 15 . 2\right) = 25 . 7`

$\text{difference in length} = 25 . 7  \text{m}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, $C$.
> 
> **B1**: A correct answer only, 25.7.
> 
> The correct method subtracts the new repeated path from the old repeat total, as 51.2 minus the sum of BF and FG.
> 
> Watch this one carefully, because the correct answer can come from incorrect working: adding BE and EC gives 11.2 plus 14.5, which is also 25.7, and that scores nothing. A correct answer of 25.7 with no working at all is given the benefit of the doubt.

> **[exam-tip]**
> The two odd vertices you leave unpaired are exactly the start and the finish, so an open route saves you the cost of joining them. Choose the finish that leaves the cheapest pairing of the two vertices that are left, not the one nearest the start.
> 
> - Every pairing you need is already in the table from part (e), so this part is a comparison rather than a fresh calculation
> - The coincidence here is worth knowing about: 25.5 and 25.7 both appear in part (e), and the two shortest paths BC and BG differ by only 0.2, so check which one you have subtracted
