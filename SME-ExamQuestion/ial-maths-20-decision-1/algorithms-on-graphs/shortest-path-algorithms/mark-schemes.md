# Mark Schemes — Shortest Path Algorithms
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

## Q4 — medium — 14 marks · exam-questions

### 6((a)) — 6 marks
Dijkstra's algorithm settles the towns in order of increasing distance from $A$, recording at each one its order of labelling, its final value, and every working value tried on the way

Each time a town receives its final value, look along the roads leaving it and replace any neighbouring working value that can now be beaten

| Vertex | Order of labelling | Final value | Working values |
|---|---|---|---|
| **A** | *1* | *0* | *0* |
| **B** | *2* | *7* | *7* |
| **C** | *3* | *8* | *8* |
| **D** | *4* | *9* | *9* |
| **E** | *5* | *11* | *19, 13, 11* |
| **F** | *6* | *18* | *23, 21, 18* |
| **G** | *7* | *25* | *27, 25* |
| **H** | *8* | *26* | *33, 28, 26* |

**[M1 A1 A1 A1]**

Once $C$ is labelled it offers $E$ a value of 18, which is worse than the 13 already sitting there, so nothing new is written down

The final values are the least distances from $A$, so they are exactly the entries the table is missing

|   | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| **A** | - | *7* | *8* | *9* | *11* | *18* | *25* | *26* |

Enter those values in the table

|   | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| A | - | **Final answer:** **7** | **Final answer:** **8** | **Final answer:** **9** | **Final answer:** **11** | **Final answer:** **18** | **Final answer:** **25** | **Final answer:** **26** |
| B | **Final answer:** **7** | - | 14 | 2 | 4 | 11 | 18 | 19 |
| C | **Final answer:** **8** | 14 | - | 12 | 10 | 15 | 22 | 23 |
| D | **Final answer:** **9** | 2 | 12 | - | 2 | 9 | 16 | 17 |
| E | **Final answer:** **11** | 4 | 10 | 2 | - | 7 | 14 | 15 |
| F | **Final answer:** **18** | 11 | 15 | 9 | 7 | - | 7 | 8 |
| G | **Final answer:** **25** | 18 | 22 | 16 | 14 | 7 | - | 1 |
| H | **Final answer:** **26** | 19 | 23 | 17 | 15 | 8 | 1 | - |

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Replaces a larger working value with a smaller one at at least two of the towns $E$, $F$, $G$ and $H$.
> 
> **A1**: All values at $A$, $B$, $C$ and $D$ correct, with the working values in the correct order.
> 
> **A1**: All values at $E$ and $F$ correct, with the working values in the correct order.
> 
> **A1**: All values at $E$, $G$ and $H$ correct, with the working values in the correct order. Follow through from your own earlier values.
> 
> **M1**: Correct entries in the table, following through from your own final values. Only the row for $A$ or the column for $A$ has to be filled in, not both.
> 
> **A1**: A correct answer only.
> 
> The order of the working values inside a box is marked, not just the set of them. At $F$ they must read 23, 21, 18 in that order, and the same three numbers written 23, 18, 21 does not earn the mark.
> 
> The order of labelling must be strictly increasing. Repeating a number, as in 1, 2, 3, 3, 4, is penalised once for the whole question, and skipping numbers, as in 1, 2, 3, 5, 6, is not penalised at all. Errors in the final and working values are penalised before any error in the order of labelling.
> 
> A missing 0 among $A$'s working values is condoned, and starting the order of labelling at 0 rather than 1 is accepted.
> 
> The second method mark depends on the first one having been earned.

> **[exam-tip]**
> Update a town only at the moment one of its neighbours becomes permanent, and write each new working value immediately to the right of the last, so the order of the improvements stays visible.
> 
> - The sequence in a box is part of the answer rather than rough work, because it records which town fed which improvement
> - $G$ takes 27 from $E$ before 25 from $F$, since $E$ is labelled fifth and $F$ sixth, and that order is marked
> 
> Fill in the whole $A$ row from the final values in one go at the end, rather than transferring them as you label.
> 
> - The table is symmetric, so the $A$ column repeats the $A$ row and only one of them is needed

### 6((b)) — 2 marks
With the table of least distances complete, the nearest neighbour algorithm can start at $A$ and repeatedly move to the nearest town not yet visited, returning to $A$ at the end

From $A$ the nearest is $B$ at 7, then $D$ at 2, then $E$ at 2, then $F$ at 7, then $G$ at 7, then $H$ at 1, then $C$ at 23, and finally back to $A$ at 8

**Final answer:** **A – B – D – E – F – G – H – C – A**

**[B1]**

$7 + 2 + 2 + 7 + 7 + 1 + 23 + 8$

$\text{upper bound} = 57  \text{km}$

**[B1]**

> **[mark-scheme]**
> **B1**: The correct nearest neighbour route, which must start and finish at $A$.
> 
> **B1**: A correct answer only on the length, 57.
> 
> The route may be given as a list of arcs rather than a list of towns.

> **[exam-tip]**
> Run this on the completed table, not on Figure 5, because the algorithm needs a distance between every pair of towns and Figure 5 has only fifteen roads.
> 
> - The 23 from $H$ to $C$ is the price of leaving $C$ until last, which is the characteristic weakness of nearest neighbour
> - The final leg back to $A$ is forced rather than chosen, so a large number there is not a mistake

### 6() — 4 marks
**(i)**

Deleting $A$ leaves the seven towns $B$ to $H$, and Prim's algorithm grows one tree outwards from $C$

From $C$ the cheapest is $C E$ at 10, then from $C$ and $E$ the cheapest to a new town is $D E$ at 2, then $B D$ at 2

*CE, DE, BD*

**[M1]**

With $B$, $C$, $D$ and $E$ in the tree, $E F$ at 7 brings in $F$, then $F G$ at 7 brings in $G$ and $G H$ at 1 brings in $H$

**Final answer:** **CE, DE, BD, EF, FG, GH**

**[A1]**

**(ii)**

A lower bound is the weight of that residual tree plus the two shortest arcs from the deleted town back into it

$10 + 2 + 2 + 7 + 7 + 1 = 29$

The two shortest arcs at $A$ are $A B$ at 7 and $A C$ at 8, and both are added on separately

$29 + 7 + 8$

**[M1]**

$\text{lower bound} = 44  \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: Selects the first three arcs in order, CE, DE and BD, or all seven towns in order, C, E, D, B, F, G and H. Numbering the columns 4, 1, 3, 2, 5, 6, 7 across the top of the reduced table shows the same thing.
> 
> **A1**: A correct answer only, with all six arcs stated and in the correct order and no additional arcs.
> 
> **M1**: Adds the weight of the residual tree to the two smallest arcs at $A$, 7 and 8. A residual weight anywhere from 19 to 39 is allowed.
> 
> **A1**: A correct answer only, 44.
> 
> Prim's algorithm never rejects an arc, so showing any rejection in part (i) loses the first method mark however good the rest of the answer is. Starting at a town other than $C$ scores nothing here, because the question names the starting point.
> 
> The first accuracy mark is for the arcs, not the nodes. A list of towns in the order they join, or a numbering across the top of the table, is accepted for the method mark but not for the accuracy mark unless the correct list of arcs also appears.
> 
> The second accuracy mark depends on Prim's algorithm having been used in part (i). Circling six values in the table and adding 15 to them reaches 44 but shows no order of selection, so it does not earn it.

> **[exam-tip]**
> The reduced table is the given one with row $A$ and column $A$ struck out, so there is no need to rewrite it.
> 
> - Deleting $A$ removes seven arcs, and only $A B$ and $A C$ come back, which is what makes this a lower bound rather than a tour
> - Show the two arcs at $A$ as separate numbers, since combining them into a single 15 loses the accuracy mark even though the answer is the same
> 
> The word "Hence" in part (ii) means the tree from part (i) must be used.
> 
> - An answer of 44 with no visible order of arc selection scores nothing in part (ii)

### 6((d)) — 2 marks
The optimal route is at least the lower bound from part (c)(ii) and at most the upper bound from part (b)

$44 \leq \text{optimal distance} \leq 57$

**[B1] [B1]**

> **[mark-scheme]**
> **B1**: Any interval running from your answer to part (c)(ii) up to your answer to part (b), with at least one of the two values correct.
> 
> **B1**: A correct answer only. Both $44 \leq \text{optimal distance} \leq 57$ and $44 < \text{optimal distance} \leq 57$ are accepted.
> 
> The official scheme awards these two marks together, as two marks for a fully correct interval with one mark for an interval built from your own two values where at least one of them is correct.
> 
> An interval written the wrong way round, as 57 to 44, scores nothing, and so does the single number 13 obtained by subtracting one bound from the other.

> **[exam-tip]**
> The lower bound goes on the left and the upper bound on the right, so check the inequality reads the right way round before writing it down.
> 
> - The two ends come from different parts, the lower from (c)(ii) and the upper from (b), so an interval built from one part alone cannot be right
> - The question says to use only the results from (b) and (c), so there is nothing further to calculate here

## Q5 — medium — 10 marks · exam-questions

### 1((a)) — 2 marks
Three separate conditions have to appear, and each one carries part of the credit

**Final answer:** **A path is a finite list of edges in which every edge ends at the vertex the following edge starts from, and in which no vertex is visited more than once**

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Any one of the three conditions stated clearly: that the sequence of edges is finite, that each edge ends where the next begins, or that no vertex is used more than once.
> 
> **B1**: All three conditions stated clearly.
> 
> Defining a path as a walk in which no vertex appears more than once earns the first mark but not the second, because it leans on another definition rather than giving the three conditions.

> **[exam-tip]**
> Marks here are counted condition by condition, so a fluent one-line definition can still score less than a clumsy list of three.
> 
> - Write the three conditions as three separate clauses and check each is actually present before moving on
> - Defining a path in terms of a walk is the common way to lose the second mark: it is correct mathematics, but it hands back the definition you were asked for

### 1((b)) — 6 marks
Dijkstra's algorithm settles the vertices in order of increasing distance from $A$, recording at each one its order of labelling, its final value, and every working value tried along the way

Each time a vertex receives its final value, look along the arcs leaving it and replace any neighbouring working value that can now be beaten

| Vertex | Order of labelling | Final value | Working values |
|---|---|---|---|
| **A** | *1* | *0* | *0* |
| **B** | *3* | *8* | *8* |
| **C** | *2* | *5* | *5* |
| **D** | *5* | *14* | *17, 14* |
| **E** | *7* | *21* | *23, 21* |
| **F** | *4* | *13* | *15, 14, 13* |
| **G** | *6* | *20* | *24, 23, 20* |
| **H** | *8* | *26* | *26* |
| **J** | *9* | *33* | *40, 35, 33* |

**[M1 A1 A1 A1]**

Trace the route back from $J$, keeping any step where the gap between two final values is exactly the weight of the arc joining them

$J$ has final value 33 and $H J$ has weight 7, and $H$ has final value 26, so $H$ lies on the route

The same test gives $E$ at 21, then $B$ at 8, then back to $A$

**Final answer:** **A – B – E – H – J**

**[A1]**

$\text{length} = 33  \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces a larger working value with a smaller one at at least two of the vertices D, E, F, G and J.
> 
> **A1**: All values at A, C, B, F and D correct, with the working values in the correct order.
> 
> **A1**: All values at G and E correct, with the working values in the correct order.
> 
> **A1**: All values at H and J correct, with the working values in the correct order. Follow through from your earlier values.
> 
> **A1**: The path A, B, E, H, J and no other.
> 
> **A1**: The length 33. Follow through from your own final value at J, and a missing unit is condoned.
> 
> The order of the working values inside a box is marked, not just the set of them. At F they must read 15, 14, 13 in that order; the same three numbers written 15, 13, 14 does not earn the mark.
> 
> The order of labelling must be strictly increasing. Repeating a number, as in 1, 2, 3, 3, 4, is penalised once, but skipping numbers, as in 1, 2, 3, 5, 6, is not penalised at all.
> 
> Errors in the final and working values are penalised before any error in the order of labelling.

> **[exam-tip]**
> Update a vertex only at the moment one of its neighbours becomes permanent, and write each new working value immediately to the right of the last, so the order of improvements stays visible.
> 
> - The sequence in a box is part of the answer, not rough work: 15, 14, 13 at F records three genuine improvements, and the same digits in another order records something that never happened
> - When G is labelled it offers E a value of 36, which is worse than the 21 already sitting there, so nothing new is written down
> 
> To read the path back, start at J and step to any vertex whose final value differs from it by exactly the weight of the arc between them.
> 
> - Working backwards is reliable; guessing the route from the picture is not, because the shortest path is often not the one that looks straightest

### 1((c)) — 2 marks
A journey from $J$ to $A$ that has to pass through $G$ splits into the shortest route from $J$ to $G$, followed by the shortest route from $G$ to $A$

The arcs run both ways, so the shortest route from $G$ back to $A$ is the one already found in part (b), and its length is the final value at $G$

Tracing back from $G$ gives $D$ at 14, then $C$ at 5, then $A$, and the direct arc $G J$ has weight 15

**Final answer:** **J – G – D – C – A**

**[B1]**

$20 + 15$

$\text{length} = 35  \text{km}$

**[B1]**

> **[mark-scheme]**
> **B1**: The path J, G, D, C, A and no other.
> 
> **B1**: The length 35. Follow through by adding 15 to your own final value at G.

> **[exam-tip]**
> There is no need to run Dijkstra's again from J. The final value at G is already the length of the shortest route between A and G, and the arcs work in either direction.
> 
> - Splitting a "via" journey at the named vertex turns it into two shorter problems you have usually already solved
> - Check that the arc you use out of J really is the cheapest way to reach G: here JG at 15 beats going round through H and E, which costs 28

## Q6 — medium — 10 marks · exam-questions

### 5((a)) — 2 marks
Dijkstra's algorithm run from one vertex finds the shortest route from that vertex to every other one, in a single pass

Tamasi wants two routes, from $A$ to $J$ and from $A$ to $K$, and $A$ is the vertex they have in common

**Final answer:** **Start at A**

**[B1]**

**Final answer:** **A lies on both of the required routes, so one run of the algorithm starting at A gives the shortest route to J and the shortest route to K together**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, A. Naming more than one vertex scores nothing.
> 
> **B1**: A correct reason for starting at A. This mark depends on the first one.
> 
> The reason must either state explicitly that A appears on both of the required routes, or state that starting at A finds the shortest route to every other vertex, or at least to both J and K. A reason that only says A is convenient, or that A is where Tamasi lives, is not enough.

> **[exam-tip]**
> Dijkstra's algorithm is one to many, not one to one. It costs no more to reach every vertex than to reach a single chosen one, which is exactly why the shared vertex is the one to start from.
> 
> - Starting at $J$ would give the shortest route from $J$ to $A$, but nothing at all about $K$, so a second run would be needed
> - The second mark is for the reason, and it is only awarded if the first is, so name the vertex before explaining the choice

### 5((b)) — 7 marks
Dijkstra's algorithm settles the vertices in order of increasing distance from $A$, recording at each one its order of labelling, its final value, and every working value tried on the way

Each time a vertex receives its final value, look along the arcs leaving it and replace any neighbouring working value that can now be beaten

| Vertex | Order of labelling | Final value | Working values |
|---|---|---|---|
| **A** | *1* | *0* | *0* |
| **B** | *4* | *31* | *32, 31* |
| **C** | *2* | *12* | *12* |
| **D** | *3* | *23* | *24, 23* |
| **E** | *6* | *41* | *43, 41* |
| **F** | *7* | *48* | *51, 49, 48* |
| **G** | *5* | *40* | *43, 40* |
| **H** | *8* | *51* | *55, 51* |
| **J** | *9* | *80* | *84, 82, 80* |
| **K** | *10* | *81* | *92, 89, 81* |

**[M1 A1 A1 A1]**

Trace each route back from its end vertex, keeping any step where the gap between two final values is exactly the length of the arc joining them

$J$ has final value 80 and $F J$ is 32, and $F$ has final value 48, so $F$ lies on that route, and the same test then gives $G$ at 40, $D$ at 23 and $C$ at 12

$K$ has final value 81 and $H K$ is 30, and $H$ has final value 51, so $H$ lies on that route, and the same test then gives $E$ at 41, $B$ at 31, $D$ at 23 and $C$ at 12

**Final answer:** **A – C – D – G – F – J**

**[A1]**

**Final answer:** **A – C – D – B – E – H – K**

**[A1]**

$\text{length of the route to J} = 80  \text{miles}$

$\text{length of the route to K} = 81  \text{miles}$

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces a larger working value with a smaller one at any two vertices other than A and C. This is a method mark, so the values themselves do not have to be correct.
> 
> **A1**: All values at A, C, D, B and G correct, with the working values in the correct order, and those five labelled in that order.
> 
> **A1**: All values at E, F and H correct, with the working values in the correct order. E, F and H must be labelled in that order, and E must be labelled after A, C, D, B and G.
> 
> **A1**: All values at J and K correct, with the working values in the correct order. Follow through from your earlier values.
> 
> **A1**: Either one of the two routes correct.
> 
> **A1**: Both routes correct.
> 
> **A1**: Both lengths correct. Follow through from your own final values at J and at K.
> 
> A route may be reversed, or given as a list of arcs instead, so JFGDCA and AC, CD, DG, GF, FJ are both accepted.
> 
> A missing zero as the working value at A is condoned. The order of the working values inside a box is marked, not just the set of them: at F they must read 51, 49, 48 in that order, and 51, 48, 49 is not accepted.
> 
> The order of labelling must be strictly increasing. Repeating a number is penalised once; skipping numbers is not penalised at all. Errors in the final and working values are penalised before any error in the order of labelling.
> 
> Running the algorithm from J or from K instead is not treated as a misread, and caps this part at 4 of the 7 marks. Running it twice, once from J and once from K, can still earn all seven.

> **[exam-tip]**
> One labelling serves both routes, which is the whole point of part (a). Both traces run back through $D$ and $C$ and only separate at $D$.
> 
> - $A J$ is a direct arc of 84 miles and the shortest route to $J$ is 80, so the direct arc is not used
> - Both lengths are read straight off the final values at $J$ and $K$, so there is nothing to add up

### 5((c)) — 1 marks
The journey splits at $A$ into the shortest route from $F$ to $A$, followed by the shortest route from $A$ to $H$

The arcs run both ways, so the first half is the route to $F$ from part (b) written backwards, and the second half is the opening of the route to $K$

The two halves share the arcs $A C$ and $C D$, so both of those are travelled twice

**Final answer:** **F – G – D – C – A – C – D – B – E – H**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, F, G, D, C, A, C, D, B, E, H.
> 
> Stated as a list of arcs it is FG, GD, DC, CA, AC, CD, DB, BE, EH, and AC and CD must each appear twice in it. A route that visits A and then goes straight on to H without retracing those two arcs is not the shortest.

> **[exam-tip]**
> A via route is allowed to repeat itself. Splitting at the named vertex gives the shortest route each side, and if those two halves overlap then the overlap is simply travelled twice.
> 
> - Do not try to avoid the repeat by finding some other way back out of $A$, because that only makes the journey longer
> - The route has ten vertices in it and two of them, $C$ and $D$, appear twice

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

## Q10 — medium — 11 marks · exam-questions

### 2((a)) — 6 marks
Dijkstra's algorithm settles the villages in order of increasing distance from $A$, recording at each one its order of labelling, its final value, and every working value tried on the way

Each time a village receives its final value, look along the roads leaving it and replace any neighbouring working value that can now be beaten

| Vertex | Order of labelling | Final value | Working values |
|---|---|---|---|
| **A** | *1* | *0* | *0* |
| **B** | *2* | *3* | *3* |
| **C** | *3* | *7* | *8, 7* |
| **D** | *4* | *12* | *12* |
| **E** | *5* | *20* | *24, 22, 20* |
| **F** | *6* | *41* | *41* |
| **G** | *7* | *46* | *46* |
| **H** | *8* | *48* | *48* |
| **J** | *10* | *76* | *88, 78, 76* |
| **K** | *9* | *70* | *72, 70* |

**[M1 A1 A1 A1]**

Note that $K$ is labelled ninth and $J$ tenth, because $K$ settles at 70 while $J$ is still holding a working value of 78

Trace the route back from $J$, keeping any step where the gap between two final values is exactly the weight of the road joining them

$J$ has final value 76 and $J K$ has weight 6, and $K$ has final value 70, so $K$ lies on the route

The same test gives $H$ at 48, then $F$ at 41, then $E$ at 20, then $D$ at 12, then $B$ at 3, and back to $A$

**Final answer:** **A – B – D – E – F – H – K – J**

**[A1]**

$\text{length} = 76  \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: Replaces a larger working value with a smaller one at at least two of the villages $C$, $E$, $J$ and $K$.
> 
> **A1**: All values at $A$, $B$, $C$, $D$ and $E$ correct, with the working values in the correct order.
> 
> **A1**: All values at $F$, $G$ and $H$ correct, with the working values in the correct order.
> 
> **A1**: All values at $K$ and $J$ correct, with the working values in the correct order. Follow through from your own earlier values.
> 
> **A1**: A correct answer only, the route ABDEFHKJ.
> 
> **A1**: The length 76. Follow through from your own final value at $J$.
> 
> The order of the working values inside a box is marked, not just the set of them. At $E$ they must read 24, 22, 20 in that order, and the same three numbers written 24, 20, 22 does not earn the mark.
> 
> The order of labelling must be strictly increasing. Repeating a number, as in 1, 2, 3, 3, 4, is penalised once for the whole question, and skipping numbers, as in 1, 2, 3, 5, 6, is not penalised at all. Errors in the final and working values are penalised before any error in the order of labelling.
> 
> A missing 0 among $A$'s working values is condoned, and starting the order of labelling at 0 rather than 1 is accepted.
> 
> An extra working value of 56 at $H$, written after the 48, is not an error, so 48 then 56 is accepted. Any other number there, or 56 before the 48, is not.
> 
> The route must be given from $A$ to $J$, not from $J$ to $A$.

> **[exam-tip]**
> Update a village only at the moment one of its neighbours becomes permanent, and write each new working value immediately to the right of the last, so the order of the improvements stays visible.
> 
> - When $G$ is labelled it offers $H$ a value of 56, which is worse than the 48 already there, so nothing has to be written down
> - $K$ is labelled before $J$ even though $J$ appears earlier in the alphabet, and the order of labelling records what actually happened rather than the letters
> 
> To read the route back, start at $J$ and step to any village whose final value differs from it by exactly the weight of the road between them.
> 
> - Working backwards is reliable; picking the route off the picture is not, because the shortest route here goes the long way round through $K$ rather than straight along $H J$

### 2((b)) — 2 marks
A minimum connector is a minimum spanning tree, and Prim's algorithm grows one outwards from $A$, each time adding the shortest road that reaches a village not yet in it

From $A$ the cheapest road is $A B$ at 3, and then $B C$ at 4 brings in $C$

*AB, BC*

**[M1]**

With $A$, $B$ and $C$ in the tree, $B D$ at 9 brings in $D$, and then $D E$ at 8 brings in $E$

**Final answer:** **AB, BC, BD, DE**

**[A1]**

> **[mark-scheme]**
> **M1**: Selects the first two arcs in order, AB and BC, or the first three villages in order, A, B and C.
> 
> **A1**: A correct solution only, with all four arcs stated and in the correct order and no additional arcs. Starting BA, CB is accepted, since an arc may be named either way round.
> 
> Prim's algorithm never rejects a road, so showing any rejection at any point loses the method mark. A list of weights on their own, with no arcs named, also earns nothing.
> 
> This part asks only for the five villages $A$ to $E$. Carrying on to build a minimum connector for the whole network is not ignored as subsequent working, and loses the accuracy mark.

> **[exam-tip]**
> Cover up the other five villages before you start, so that the roads leaving $E$ towards $F$ never come into consideration.
> 
> - Four arcs for five villages, so a connector with three or five arcs has gone wrong
> - $A C$ at 8 looks tempting from $A$ but is never selected, because $C$ is reached more cheaply through $B$

### 2((c)) — 2 marks
Kruskal's algorithm considers the roads in ascending order of weight, adding each one unless it would close a cycle

$F G$ at 5, $J K$ at 6 and $F H$ at 7 all join villages not yet connected to one another, so all three are added

$G H$ at 10 is rejected, because $G$ and $H$ are already linked through $F$

**Final answer:** **FG (5) add, JK (6) add, FH (7) add, GH (10) reject**

**[M1]**

$H K$ at 22 joins the group holding $F$, $G$ and $H$ to the group holding $J$ and $K$, which completes the connector

**Final answer:** **HK (22) add**

**[A1]**

> **[mark-scheme]**
> **M1**: Works in ascending order of weight with the first two arcs correct, FG and JK, and at least one rejection shown somewhere in the list.
> 
> **A1**: A correct solution only, with every selection and every rejection correct and shown at the right point in the list.
> 
> $H J$ at 30, $F K$ at 31 and $G J$ at 42 do not have to be considered, because the connector is finished once HK has been added. If you do write them down they must all be rejected, and after HK rather than before it.
> 
> Listing every road in weight order and then listing separately the roads that make up the connector is accepted for both marks.
> 
> This part asks only for the five villages $F$ to $K$, so applying Kruskal's algorithm to the whole network scores nothing.

> **[exam-tip]**
> The question asks you to show every road you consider and say whether you are including it, so the rejection is part of the answer rather than rough work.
> 
> - Four arcs for five villages, so stop as soon as the fourth is added
> - $G H$ at 10 is the only rejection you have to write down, and leaving it out costs the method mark even if every selection is right

### 2((d)) — 1 marks
The two connectors keep each half of the network reachable, but nothing yet joins the halves to one another

$E F$ is the only road between the two groups of villages, so it has to be kept clear as well

$24 + 40 + 21$

$\text{total length of road} = 85  \text{km}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 85.
> 
> The 24 from part (b) and the 40 from part (c) are not enough on their own, because the two connectors are not joined to each other. The road $E F$ must be added.

> **[exam-tip]**
> Ten villages need nine roads to be all reachable, and parts (b) and (c) supply only four each, so exactly one more is needed.
> 
> - $E F$ is the only candidate, since it is the only road with one end in each half
> - That also means its length of 21 is unavoidable however the rest is chosen, so it is worth spotting before adding anything up
