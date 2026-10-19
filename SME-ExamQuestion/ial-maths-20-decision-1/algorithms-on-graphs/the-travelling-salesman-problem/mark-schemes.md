# Mark Schemes — The Travelling Salesman Problem
**Algorithms on Graphs** · Edexcel International A Level (IAL) Maths (YMA01) — Decision 1


## Q1 — medium — 8 marks · exam-questions

### 1((a)) — 2 marks
The shortcut method starts from the closed walk that goes along every arc of the minimum spanning tree twice, then replaces a repeated stretch by a single direct arc

The tree in the answer book has weight 521, so travelling every arc twice gives a route of

$2 \times 521 = 1042$

Liz only has to visit each town at least once, so she may pass through a town twice, and that is what makes a shortcut possible

Going out to $C$ and then coming all the way back through $B$, $A$ and $E$ to reach $D$ uses four arcs of the tree

$110 + 122 + 109 + 98 = 439$

Replace that whole stretch by the single road $C D$, which costs only 204

- The route it gives is A – F – A – B – C – D – E – A, which visits every town and returns to $A$

*Shortcut: add CD and remove BC, AB, AE and DE*

$1042 - 439 + 204$

$\text{upper bound} = 807  \text{km}$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Starts from twice the weight of the given tree and adds and subtracts at least one arc, reaching a value below 810 and stating that length.
> 
> **A1**: A correct answer only. The shortcut and the length must be consistent with each other, the arcs added and subtracted must be clearly stated, and the resulting network must be connected with every town on an even number of arcs.
> 
> The official scheme prints five acceptable shortcuts and any of them earns both marks: CD giving 807, CF and AD giving 793, CF and BD giving 664, AD, EF and FC giving 715, and DF and FC giving 785.
> 
> The length has to be stated, not just implied by the working.

> **[exam-tip]**
> Doubling the tree is the safe starting point, because it is always a route: the only work left is to find one stretch worth cutting out.
> 
> - Look for a pair of towns that are far apart in the tree but close in the table, since the saving is the difference between the two
> - The question fixes a target of 810, so check your answer against it before moving on
> - Anything below 810 scores here, so there is no need to hunt for the very best shortcut

### 1((b)) — 2 marks
The nearest neighbour algorithm starts at $A$ and repeatedly moves to the nearest town not yet visited, then returns to $A$ at the end

From $A$ the nearest town is $F$ at 82, then $E$ at 113, then $D$ at 98, then $B$ at 130, then $C$ at 110

The last leg back to $A$ is forced, and $C A$ at 217 is the longest road on the route

**Final answer:** **A – F – E – D – B – C – A**

**[B1]**

$82 + 113 + 98 + 130 + 110 + 217$

$\text{upper bound} = 750  \text{km}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, the route A – F – E – D – B – C – A, which must return to $A$.
> 
> **B1**: A correct answer only, 750.
> 
> Doubling the length afterwards is not ignored as subsequent working, so leave the total as it stands.

> **[exam-tip]**
> Nearest neighbour never looks ahead, so it can be forced into an expensive last leg. Here it saves the two longest roads in the table for the end and still beats part (a).
> 
> - Cross out each town in the table as you visit it, so you never offer yourself one twice
> - The return to $A$ is not a choice, so include it even when it looks wrong

### 1((c)) — 3 marks
Deleting $F$ leaves the five towns $A$ to $E$, and a lower bound is built from the minimum spanning tree of what is left plus the two shortest roads back to $F$

The residual minimum spanning tree uses $D E$ at 98, $A E$ at 109, $B C$ at 110, $A B$ at 122

$98 + 109 + 110 + 122 = 439$

**[B1]**

The two shortest roads at $F$ are $A F$ at 82 and $E F$ at 113, and both are added on separately

$439 + 82 + 113$

**[M1]**

$\text{lower bound} = 634  \text{km}$

**[A1]**

> **[mark-scheme]**
> **B1**: A correct answer only, the weight of the residual minimum spanning tree is 439. This may also be seen as the sum 98 + 109 + 110 + 122.
> 
> **M1**: Adds the two shortest arcs at $F$ to the weight of your residual tree. Follow through from your own tree, but a residual tree that does not have four arcs loses this mark.
> 
> **A1**: A correct answer only, 634.
> 
> The two arcs at $F$ must appear separately as 82 and 113. Writing 439 + 195 = 634, with the two already combined, loses the accuracy mark even though the answer is the same.

> **[exam-tip]**
> Deleting $F$ removes five roads from the table, and only $A F$ was in the original tree, so the residual tree here is the answer book's tree with $A F$ taken out.
> 
> - That shortcut only works because $F$ had a single arc in the tree, so check the tree before relying on it
> - Rebuild the residual tree from the table if $F$ had two or more arcs in it, since removing them can change the whole shape

### 1((d)) — 1 marks
The optimal length is at least the lower bound from part (c) and at most the best upper bound found so far

Parts (a) and (b) gave 807 and 750, and the better upper bound is the smaller of the two

$634 < \text{optimal length} \leq 750$

**[B1]**

> **[mark-scheme]**
> **B1**: An interval running from your lower bound in part (c) up to your best upper bound from either part (a) or part (b), so follow through applies to both ends.
> 
> The upper bound has to be the smaller of the two you found, since a smaller upper bound gives a narrower interval.

> **[exam-tip]**
> Smaller is better for an upper bound and larger is better for a lower bound, which is the opposite way round from what most people expect first time.
> 
> - Put the lower bound on the left and the upper bound on the right, and check the inequality reads the right way round before writing it down
> - The two ends come from different parts, so an interval built from one part alone cannot be right

## Q2 — medium — 7 marks · exam-questions

### 1((a)) — 3 marks
The nearest neighbour algorithm starts at $A$ and repeatedly moves to the nearest classroom not yet visited, then returns to $A$ at the end

From $A$ the nearest classroom is $B$ at 43, then $D$ at 45, then $F$ at 49

*A – B – D – F*

**[M1]**

From $F$ the two nearest unvisited classrooms are $C$ and $G$, both at 55, and that tie is what produces two different routes

Taking $C$ first leads to $E$ at 50, then $G$ at 48, then back to $A$ at 55

**Final answer:** **A – B – D – F – C – E – G – A**

$43 + 45 + 49 + 55 + 50 + 48 + 55$

$\text{length} = 345  \text{m}$

**[A1]**

Taking $G$ first leads to $E$ at 48, then $C$ at 50, then back to $A$ at 52

**Final answer:** **A – B – D – F – G – E – C – A**

$43 + 45 + 49 + 55 + 48 + 50 + 52$

$\text{length} = 342  \text{m}$

**[A1]**

> **[mark-scheme]**
> **M1**: Applies nearest neighbour from $A$ with the first four classrooms correct, $A$, $B$, $D$ and $F$. The arcs AB, BD, DF earn it instead, and so do the weights 43, 45, 49.
> 
> **A1**: One correct route with its corresponding correct length. The route may be given as classrooms or as arcs, but not as weights alone, and it must return to $A$.
> 
> **A1**: Both routes correct with both their corresponding lengths.
> 
> Units are not required on either length.

> **[exam-tip]**
> The question tells you there are two routes, so look for the point where the algorithm has a genuine choice rather than hunting for a second answer at the end.
> 
> - The fork is at $F$, which is 55 from both $C$ and $G$
> - Follow each branch through to the end separately rather than trying to keep both going at once
> - The two routes use the same seven distances apart from one, 55 against 52, so the whole difference of 3 sits in the final leg home

### 1((b)) — 3 marks
Deleting $A$ leaves the six classrooms $B$ to $G$, and a lower bound is built from the minimum spanning tree of what is left plus the two shortest distances back to $A$

Six classrooms need five arcs, one more than the four-arc trees of the other questions on this topic

The residual minimum spanning tree uses $B D$ at 45, $B E$ at 46, $B G$ at 47, $D F$ at 49, $C E$ at 50

$45 + 46 + 47 + 49 + 50 = 237$

**[B1]**

The two shortest distances at $A$ are $A B$ at 43 and $A D$ at 47, and both are added on separately

$237 + 43 + 47$

**[M1]**

$\text{lower bound} = 327  \text{m}$

**[A1]**

> **[mark-scheme]**
> **B1**: A correct answer only, the weight of the residual minimum spanning tree is 237. Naming its five arcs BD, BE, BG, DF, CE, or writing the sum 45 + 46 + 47 + 49 + 50, earns it equally.
> 
> **M1**: Adds 43 and 47, the two shortest arcs at $A$, to your attempt at the residual weight. The official scheme accepts any attempt weighing between 224 and 250, provided it is a five-arc tree, so a spanning tree that is not minimal can still earn this mark. An unsimplified answer that implies the right two arcs added to a five-arc tree is allowed as well.
> 
> **A1**: A correct answer only, 327.
> 
> The official scheme is generous here: 327 seen with no working at all scores all three marks in this part.
> 
> The two arcs at $A$ still have to appear separately as 43 and 47 wherever working is shown.

> **[exam-tip]**
> Count the arcs in the residual tree before adding anything on. Seven classrooms leave six, so the tree needs five arcs, and the four-arc habit built up on six-vertex questions loses the method mark here.
> 
> - Rebuild the tree from the table rather than editing a route from part (a), which is a tour and not a tree
> - The two arcs at $A$ are the two smallest numbers in row $A$, so read them straight off

### 1((c)) — 1 marks
The optimal distance is at least the lower bound from part (b) and at most the better of the two upper bounds from part (a)

Part (a) gave 345 and 342, and the better upper bound is the smaller of the two

$327 \leq \text{optimal distance} \leq 342$

**[B1]**

> **[mark-scheme]**
> **B1**: Your answer to part (b) and the least of your values from part (a), used with correct inequalities, so follow through applies to both ends. A strict inequality at the lower end is allowed.
> 
> Writing 327 to 342 with a dash and no inequalities scores nothing. Set notation such as `\left[327, 342\right]` is accepted.
> 
> The upper bound must be the smaller of the two lengths found in part (a), and two different values must have been given there.

> **[exam-tip]**
> Smaller is better for an upper bound, so the tighter of part (a)'s two routes is the one that goes on the right of the interval.
> 
> - Write the inequality signs in, since a dash between the two numbers earns nothing here
> - Put the lower bound on the left and check the inequality reads the right way round before writing it down

## Q3 — medium — 14 marks · exam-questions

### 3((a)) — 3 marks
Kruskal's algorithm works through the arcs in ascending order of weight, adding each one unless it would close a cycle

The six shortest roads are all added, because each joins two towns not yet connected to one another

$C H$ at 17 is the first rejection, since $C$ and $H$ are already linked through $P$, $B$, $A$

**Final answer:** **AB (6) add, BP (10) add, CW (11) add, CP (12) add, HM (14) add, AH (15) add, CH (17) reject**

**[M1]**

$A C$ at 18 and $A P$ at 20 are rejected for the same reason, and so is $M W$ at 21

$L Y$ at 21 brings in two new towns, then $A S$ at 26 and $L S$ at 28 attach $S$ and join the two groups together

**Final answer:** **AC (18) reject, AP (20) reject, MW (21) reject, LY (21) add, AS (26) add, LS (28) add**

**[A1] [A1]**

> **[mark-scheme]**
> **M1**: Works in ascending order of weight with the first four arcs correct, AB, BP, CW and CP, and at least one rejection shown somewhere in the list.
> 
> **A1**: All nine arcs of the tree selected correctly and in the correct order, AB, BP, CW, CP, HM, AH, LY, AS and LS, with no other arcs in the tree.
> 
> **A1**: A correct solution only, with every rejection correct and shown at the right point in the list.
> 
> $M W$ and $L Y$ both weigh 21, so they may be considered in either order. Rejecting MW first and then adding LY is what the official scheme prints, and adding LY first and then rejecting MW is equally acceptable.
> 
> The roads BS, LM, HL, SY and AL never have to be considered, because the tree is complete once LS has been added. If you do write any of them down they must be rejected in the right place, that is after LS.
> 
> Listing every arc in weight order and then listing separately the arcs that make up the tree can score all three marks.

> **[exam-tip]**
> Ten towns need nine arcs, so count your additions as you go and stop the moment you reach nine rather than working to the end of the list.
> 
> - Every arc you consider must be written down with its verdict, because one whole mark is for the rejections being in the right places
> - Two arcs weigh 21, so decide which one you are taking first and keep to that order for the rest of the list

### 3((b)) — 3 marks
Prim's algorithm grows one tree outwards from $A$, each time adding the shortest arc that joins the tree to a town not yet in it

Cross out column $A$, then scan row $A$ for its smallest entry, which is 6 at $B$, and repeat with every row now in the tree

That gives $A B$ at 6, then $B P$ at 10, then $C P$ at 12

*AB, BP, CP*

**[M1]**

$C W$ at 11 brings in $W$, then $A H$ at 15 and $H M$ at 14 bring in $H$ and $M$

*AB, BP, CP, CW, AH, HM*

**[A1]**

Only $S$, $L$ and $Y$ are left, reached most cheaply by $A S$ at 26, then $L S$ at 28, then $L Y$ at 21

**Final answer:** **AB, BP, CP, CW, AH, HM, AS, LS, LY**

**[A1]**

> **[mark-scheme]**
> **M1**: Selects the first three arcs in order, AB, BP and CP, or the first four nodes in order, A, B, P and C. Numbering the columns 1, 2, 4 across the top of the table, with the rest blank, shows the same thing.
> 
> **A1**: Selects the first six arcs in order, AB, BP, CP, CW, AH and HM, or all ten nodes in order, A, B, P, C, W, H, M, S, L and Y. Across the top of the table that numbering reads 1, 2, 4, 6, 9, 7, 3, 8, 5, 10, and no node may be missing from it.
> 
> **A1**: A correct solution only, with all nine arcs stated and in the correct order and no additional arcs.
> 
> Prim's builds a single connected tree, so it can never reject anything. Showing any explicit rejection caps this part at the method mark.
> 
> The final mark is for the arcs, not the nodes. An order of selection written across the top of the table, or a list of towns in the order they join, is accepted for the first two marks but not for the last one unless the correct list of arcs also appears.

> **[exam-tip]**
> Prim's on a table is a column-crossing exercise: cross out the column of each town as it joins, then look for the smallest uncrossed entry anywhere in the rows already in the tree.
> 
> - Number the columns 1 to 10 in the order the towns join, since that record alone is worth the first two marks
> - The tree here is not the one part (a) found, because part (a) ran on the roads of Figure 2 and this runs on the table of least distances

### 3((c)) — 1 marks
The weight is the total of the nine arcs selected in part (b)

$6 + 10 + 12 + 11 + 15 + 14 + 26 + 28 + 21$

$\text{weight of the minimum spanning tree} = 143  \text{miles}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 143. This mark can also be earned in part (b) if the total appears there; where a total is given in both places, part (c) is the one that is marked.

> **[exam-tip]**
> Keep a running total as you select each arc in part (b), because this weight is needed again in parts (d) and (g).
> 
> - Nine numbers for ten towns, so a total built from eight or ten weights has an arc missing or an extra one

### 3((d)) — 1 marks
Travelling out and back along every arc of a minimum spanning tree gives a closed walk that reaches every town and returns to the start

That walk is not a tour, but its length is certainly achievable, so twice the weight of the tree is an upper bound

$2 \times 143$

$\text{initial upper bound} = 286  \text{miles}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 286. Follow through as double your answer to part (c).

> **[exam-tip]**
> This is the one upper bound available without any further work, which is why it is worth only a single mark for a single multiplication.
> 
> - Expect nearest neighbour in part (e) to beat it comfortably, because doubling the tree walks every road twice

### 3((e)) — 2 marks
The nearest neighbour algorithm starts at $W$ and repeatedly moves to the nearest town not yet visited, then returns to $W$ at the end

Reading along each row of the table in turn, the nearest unvisited town to $W$ is $C$ at 11, then $P$ at 12, then $B$ at 10, then $A$ at 6, then $H$ at 15

*W – C – P – B – A – H*

**[M1]**

From $H$ the nearest is $M$ at 14, then $L$ at 40, then $Y$ at 21, then $S$ at 48, and finally back to $W$ at 55

**Final answer:** **W – C – P – B – A – H – M – L – Y – S – W**

$11 + 12 + 10 + 6 + 15 + 14 + 40 + 21 + 48 + 55$

$\text{upper bound} = 232  \text{miles}$

**[A1]**

> **[mark-scheme]**
> **M1**: Applies nearest neighbour from $W$ with at least the first six towns correct, W, C, P, B, A and H.
> 
> **A1**: A correct answer only, covering both the length 232 and the route, which must return to $W$. The route may be stated as a list of arcs instead of a list of towns.
> 
> The last two legs are forced rather than chosen, and they are the two longest in the tour at 48 and 55. That is the usual shape of a nearest neighbour route and is not a sign of an error.

> **[exam-tip]**
> Cross out each town's column as you visit it, so that the nearest unvisited town is simply the smallest uncrossed entry in the current row.
> 
> - The final leg back to the start is not a choice, so do not look for a small number there
> - The question asks for the route as well as the bound, and both are needed for the accuracy mark

### 3((f)) — 1 marks
An upper bound is a length that can definitely be achieved, so the best one available is the smallest of those found

Part (d) gave 286, part (e) gave 232, and starting at $Y$ gave 212

**Final answer:** $\text{best upper bound} = 212  \text{miles}$**, because it is the smallest of the three**

**[B1]**

> **[mark-scheme]**
> **B1**: An indication that 212 is the minimum of 286, 232 and 212. Naming it as the one starting at $Y$, or as the route of weight 212, is accepted without the other two values being quoted, provided parts (d) and (e) are correct.
> 
> This mark is dependent on the correct values in parts (d) and (e).
> 
> The question asks for a reason, so a bare 212 scores nothing. Saying that it is the smallest, or the least, is enough.

> **[exam-tip]**
> Smaller is better for an upper bound and larger is better for a lower bound, which is the opposite way round from what most people expect.
> 
> - The reason is worth as much as the value here, so write the comparison down rather than leaving it implied

### 3((g)) — 2 marks
Deleting $W$ leaves nine towns, and a lower bound is the minimum spanning tree of what is left plus the two shortest arcs back to $W$

$C W$ was the only arc at $W$ in the part (b) tree, so the residual tree is that tree with $C W$ taken out

$143 - 11 = 132$

The two shortest arcs at $W$ are $C W$ at 11 and $M W$ at 21, and both are added on separately

$132 + 11 + 21$

**[M1]**

$\text{lower bound} = 164  \text{miles}$

**[A1]**

> **[mark-scheme]**
> **M1**: Adds the weight of the residual minimum spanning tree to the two smallest arcs at $W$, 11 and 21. A residual weight of 132 taken directly from your part (c) answer is accepted, and so is a residual tree built from scratch.
> 
> **A1**: A correct answer only, 164.
> 
> The subtraction and addition of 11 cancel, so the working may equally be written as 143 plus 21 without the intermediate step, or as 132 plus 11 and 21. Either is accepted.
> 
> A correct answer of 164 can imply both marks.

> **[exam-tip]**
> The shortcut here works only because $W$ had exactly one arc in the part (b) tree, so removing it leaves a tree spanning the other nine towns.
> 
> - Check that before relying on it: a town with two or more tree arcs leaves a disconnected fragment, and the residual tree has to be rebuilt
> - Show the two arcs at $W$ as separate numbers rather than as their total of 32

### 3((h)) — 1 marks
The table gives least distances, not roads, so a leg of the route may run through towns that are not named in it

Every leg of the part (e) route is a direct road except the last one: $S$ to $W$ is 55, which is $S$ to $A$ at 26, then $A$ to $C$ at 18, then $C$ to $W$ at 11

**Final answer:** **W – C – P – B – A – H – M – L – Y – S – A – C – W**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, the route written out in full as WCPBAHMLYSACW, or the same route given as a list of arcs.
> 
> It is enough that the route clearly begins exactly as in part (e), which must therefore be correct, and that after $S$ the towns $A$ and $C$ are visited before returning to $W$.
> 
> Stating only that $A$, $C$ and $W$ are visited twice, without the route, earns nothing.

> **[exam-tip]**
> Check each leg of your route against Figure 2 and mark the ones that are not a single road, since only those need expanding.
> 
> - Here just one leg does: the 55 from $S$ to $W$, which is why $A$ and $C$ appear a second time
> - A quick check on the table is that 26 and 18 and 11 add to 55, so the three roads really do make up that leg

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

## Q5 — medium — 15 marks · exam-questions

### 3((a)) — 3 marks
Prim's algorithm grows a single tree outwards from the starting vertex, each time adding the shortest arc that joins the tree to a vertex not yet in it

From $A$ the cheapest arc is $A E$ at 23, then from $A$ and $E$ the cheapest arc to a new vertex is $E G$ at 24, and then $C E$ at 25

*AE, EG, CE*

**[M1]**

With $A$, $C$, $E$ and $G$ in the tree, $D G$ at 26 brings in $D$ and $C F$ at 32 brings in $F$

*AE, EG, CE, DG, CF*

**[A1]**

Only $H$ and $B$ are left, reached most cheaply by $D H$ at 33 and then $B F$ at 34

**Final answer:** **AE, EG, CE, DG, CF, DH, BF**

**[A1]**

> **[mark-scheme]**
> **M1**: Selects the first three arcs in order, AE, EG and CE, or the first four vertices in order, A, E, G and C.
> 
> **A1**: Selects the first five arcs in order, AE, EG, CE, DG and CF, or all eight vertices in order, A, E, G, C, D, F, H and B.
> 
> **A1**: A correct solution only, with all seven arcs stated and in the correct order and no additional arcs.
> 
> Prim's builds one connected tree, so nothing is ever rejected. Showing any explicit rejection caps this part at the method mark however good the rest of the answer is.
> 
> Starting at a vertex other than $A$ can score the method mark only, and then only if the first three arcs are correct and in order.
> 
> For the final mark you must be listing the arcs. Listing the vertices in order, or writing the order of selection across the top of the matrix, is accepted for the first two marks but not for the last one unless the correct list of arcs also appears.

> **[exam-tip]**
> Working on a matrix, cross out the column of each vertex as it joins and then scan every uncrossed entry in the rows already in the tree, which is faster than redrawing the network.
> 
> - Number the columns 1 to 8 in the order the vertices join, since that record is worth the first two marks on its own
> - Never write a rejection down: Prim's cannot produce one, and showing one costs you both accuracy marks

### 3((b)) — 1 marks
The weight of the tree is the total of the seven arcs selected in part (a)

$23 + 24 + 25 + 26 + 32 + 33 + 34$

$\text{weight of the minimum spanning tree} = 197$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 197, coming from the seven weights 23, 24, 25, 26, 32, 33 and 34. A missing unit is ignored.

> **[exam-tip]**
> Add the weights as you select each arc in part (a) rather than going back for them, because the running total is needed twice more, in parts (c) and (f).
> 
> - Seven numbers for eight cities, so a total built from six or eight weights has an arc missing or an extra one

### 3((c)) — 1 marks
Doubling a minimum spanning tree gives a closed route that visits every city, because travelling out and back along every arc returns you to the start

That route is not usually the best one, but it is certainly achievable, so it is an upper bound for the cheapest tour

$2 \times 197$

$\text{initial upper bound} = 394$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 394. Follow through as double your answer to part (b).

> **[exam-tip]**
> This is the one upper bound you can write down without doing any more work, so it is worth a mark for a single multiplication.
> 
> - Nearest neighbour in part (d) does far better, which is the general pattern: doubling the tree is quick and crude

### 3((d)) — 4 marks
The nearest neighbour algorithm starts at $A$ and repeatedly moves to the nearest city not yet visited, then returns to $A$ at the end

From $A$ the nearest city is $E$ at 23, then $G$ at 24, then $D$ at 26, then $H$ at 33

*A – E – G – D – H*

**[M1]**

From $H$ the two nearest unvisited cities are $B$ and $F$, both at 38, and that tie is what produces two different routes

Taking $B$ first leads to $F$ at 34, then $C$ at 32, then back to $A$ at 38

**Final answer:** **A – E – G – D – H – B – F – C – A**

$23 + 24 + 26 + 33 + 38 + 34 + 32 + 38$

$\text{cost} = 248$

**[A1]**

Taking $F$ first leads to $C$ at 32, then $B$ at 35, then back to $A$ at 36

**Final answer:** **A – E – G – D – H – F – C – B – A**

$23 + 24 + 26 + 33 + 38 + 32 + 35 + 36$

$\text{cost} = 247$

**[A1] [A1]**

> **[mark-scheme]**
> **M1**: Applies nearest neighbour from $A$ with the first five vertices correct, A, E, G, D and H.
> 
> **A1**: One correct route, which must return to $A$.
> 
> **A1**: Either one correct cost, or both routes correct.
> 
> **A1**: Both costs correct and both routes correct, with both returning to $A$.
> 
> Every route has to close back to $A$. Giving the two correct Hamiltonian paths without the return, AEGDHBFC costing 210 and AEGDHFCB costing 211, scores the method mark and the first accuracy mark only.
> 
> Doubling the costs is not ignored as subsequent working, so leave the totals as they stand.

> **[exam-tip]**
> The question says there are two routes, so look for the moment the algorithm has a genuine choice. Here it is at $H$, which is 38 from both $B$ and $F$.
> 
> - Follow each branch through to the end separately rather than trying to keep both going at once
> - The last leg back to $A$ is forced, not chosen, so it can be long: the cheaper route pays 36 to get home and the dearer one pays 38

### 3((e)) — 1 marks
An upper bound is a cost that can definitely be achieved, so the best one is the smallest found so far

Part (c) gave 394 and part (d) gave 248 and 247, and 247 is the smallest of the three

$\text{best upper bound} = 247$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 247. Follow through as the smallest route length in your own part (d), provided you have found two Hamiltonian cycles there or here.

> **[exam-tip]**
> Smaller is better for an upper bound and larger is better for a lower bound, which is the opposite way round from what most people expect first time.
> 
> - The initial upper bound of 394 is never the best one once nearest neighbour has been run, so there is no need to compare it in detail

### 3((f)) — 3 marks
Deleting $A$ leaves the seven cities $B$ to $H$, and a lower bound is built from the minimum spanning tree of what is left plus the two cheapest ways back to $A$

The residual minimum spanning tree uses $E G$ at 24, $C E$ at 25, $D G$ at 26, $C F$ at 32, $D H$ at 33, $B F$ at 34

$24 + 25 + 26 + 32 + 33 + 34 = 174$

**[B1]**

The two shortest arcs at $A$ are $A E$ at 23 and $A H$ at 35, and both are added on separately

$174 + 23 + 35$

**[M1]**

$\text{lower bound} = 232$

**[A1]**

> **[mark-scheme]**
> **B1**: The weight of the residual minimum spanning tree is 174. This may also be seen as the sum 24 + 25 + 26 + 32 + 33 + 34, or as your part (b) answer less 23. Follow through from your own tree.
> 
> **M1**: Adds the weight of the residual tree to the two shortest arcs at $A$. A residual weight anywhere from 151 to 197 is allowed, but if the residual tree clearly does not have six arcs this mark is lost.
> 
> **A1**: A correct answer only, 232.
> 
> The two arcs at $A$ must appear separately as 23 and 35. Writing 174 + 58 = 232, with the two arcs already combined, loses the accuracy mark, and a bare 232 with no working at all scores the method and accuracy marks but not the first mark.

> **[exam-tip]**
> Deleting $A$ removes seven arcs from the network but only one of them, $A E$, was in the minimum spanning tree, so the residual tree is just part (a)'s tree with $A E$ taken out.
> 
> - That shortcut only works because $A$ happened to have a single arc in the tree, so check the tree before relying on it
> - Show the two arcs at $A$ as separate numbers, since combining them into one total loses a mark even though the answer is the same

### 3((g)) — 2 marks
The optimal cost is at least the lower bound from part (f) and at most the best upper bound from part (e)

$232 \leq \text{optimal cost} \leq 247$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Any interval running from your answer to part (f) up to your answer to part (e), with at least one of the two values correct.
> 
> **A1**: A correct answer only. Both $232 \leq \text{optimal cost} \leq 247$ and $232 < \text{optimal cost} \leq 247$ are accepted.

> **[exam-tip]**
> Put the lower bound on the left and the upper bound on the right, and check the inequality reads the right way round before you write it down.
> 
> - The two ends come from different parts, the lower from (f) and the upper from (e), so an interval built from one part alone cannot be right

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

## Q7 — medium — 12 marks · exam-questions

### 4((a)) — 2 marks
Both problems ask for the shortest closed route that reaches every vertex of a network, and they differ only in how many times a vertex may be visited

**Final answer:** **In the classical problem every vertex must be visited exactly once**

**Final answer:** **In the practical problem every vertex must be visited at least once**

**[B1] [B1]**

> **[mark-scheme]**
> **B1**: Shows that the difference is about how many times a vertex may be visited, referring to both problems.
> 
> **B1**: Correctly identifies the classical problem as visiting every vertex exactly once and the practical problem as visiting every vertex at least once.
> 
> The practical problem allows a vertex to be visited more than once but does not require it, so describing it as visiting every vertex more than once is not accepted.
> 
> The word vertex, or node, has to appear. Singular and plural are condoned, as is poor spelling, but a vaguer word such as place is not enough.
> 
> Both problems must be mentioned. Because the first mark is about the idea and the second about getting the two the right way round, a script scoring the second without the first is not possible.

> **[exam-tip]**
> Name both problems and say what each one does, rather than describing one and leaving the other to be inferred.
> 
> - The phrase that earns the mark is "at least once" for the practical problem, and it is worth learning as it stands
> - Saying "more than once" instead sounds similar and is wrong, because it rules out the vertices a practical route happens to pass through only once

### 4((b)) — 2 marks
The nearest neighbour algorithm starts at $A$ and repeatedly moves to the nearest museum not yet visited, then returns to $A$ at the end

From $A$ the nearest is $B$ at 25, then $D$ at 24, then $F$ at 35, then $C$ at 27, then $G$ at 29, then $E$ at 31, and finally back to $A$ at 35

**Final answer:** **A – B – D – F – C – G – E – A**

**[B1]**

$25 + 24 + 35 + 27 + 29 + 31 + 35$

$\text{upper bound} = 206  \text{km}$

**[B1]**

> **[mark-scheme]**
> **B1**: The correct nearest neighbour route, which must return to $A$. It may be given as a list of arcs, AB, BD, DF, FC, CG, GE and EA, instead of a list of museums.
> 
> **B1**: A correct answer only on the length, 206.

> **[exam-tip]**
> Cross out each museum's column as you visit it, so the nearest unvisited museum is the smallest uncrossed entry in the current row.
> 
> - The 35 from $D$ to $F$ comes early and is one of the longest legs, which is what nearest neighbour does when a cheap early choice strands you
> - The final leg back to $A$ is forced rather than chosen, so 35 there is not an error

### 4((c)) — 1 marks
An upper bound is a length that can definitely be achieved, so the smaller of two upper bounds is the better one

**Final answer:** **Yes, the bound of 203 found by starting at D is better, because it is smaller than the 206 found in part (b)**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, identifying the bound found from $D$ as the better one, together with some indication that 203 is smaller than your part (b) answer. Writing "203 is less than 206, so yes it is" is enough.
> 
> This mark depends on the upper bound in part (b) being correct.
> 
> The question asks whether it is better, so the answer may begin with a plain yes.

> **[exam-tip]**
> Say which and say why, because the reason is what the mark is for and the choice on its own is a fifty-fifty guess.
> 
> - Smaller is better for an upper bound, since it is the tighter promise about what can be achieved
> - Part (e) asks the same question about a lower bound, where the comparison runs the other way

### 4() — 4 marks
**(i)**

Deleting $G$ leaves the six museums $A$ to $F$, and Prim's algorithm grows one tree outwards from $A$

From $A$ the cheapest is $A B$ at 25, then from $A$ and $B$ the cheapest to a new museum is $B D$ at 24, then $B E$ at 27

*AB, BD, BE*

**[M1]**

With $A$, $B$, $D$ and $E$ in the tree, $E F$ at 28 brings in $F$ and $C F$ at 27 brings in $C$

**Final answer:** **AB, BD, BE, EF, CF**

**[A1]**

**(ii)**

A lower bound is the weight of that residual tree plus the two shortest arcs from the deleted museum back into it

$25 + 24 + 27 + 28 + 27 = 131$

The two shortest arcs at $G$ are $C G$ at 29 and $E G$ at 31, and both are added on separately

$131 + 29 + 31$

**[M1]**

$\text{lower bound} = 191  \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: Selects the first three arcs in order, AB, BD and BE, or the first six museums in order, A, B, D, E, F and C. Numbering the columns 1, 2, 6, 3, 4, 5 across the top of the reduced table shows the same thing.
> 
> **A1**: A correct answer only, with all five arcs stated and in the correct order and no additional arcs.
> 
> **M1**: Adds the weight of the residual tree to the two smallest arcs at $G$, 29 and 31. A residual weight anywhere from 100 to 160 is allowed.
> 
> **A1**: A correct answer only, 191.
> 
> Prim's algorithm must be used here, not the nearest neighbour algorithm, and starting at a museum other than $A$ scores nothing because the question names the starting point.
> 
> The first accuracy mark is for the arcs. A list of museums in the order they join, or a numbering across the top of the table, is accepted for the method mark but not for this one.
> 
> Listing CG and EG at the end of part (i), as many scripts do while looking ahead to part (ii), is condoned.

> **[exam-tip]**
> The reduced table is the given one with row $G$ and column $G$ struck out, so there is no need to copy it out again.
> 
> - Five arcs for six museums, so a residual tree with four or six arcs has gone wrong
> - Show the two arcs at $G$ as separate numbers rather than as a single 60, since the separate form is what the method mark looks for

### 4((e)) — 1 marks
A lower bound is a length the optimal route cannot go below, so the larger of two lower bounds is the better one

**Final answer:** **No, the bound of 188 found by deleting A is not better, because it is smaller than the 191 found in part (d)(ii)**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, identifying the bound found by deleting $G$ as the better one, together with some indication that 188 is smaller than your part (d)(ii) answer. Writing "188 is less than 191, so no it is not" is enough.
> 
> This mark depends on the lower bound in part (d)(ii) being correct.
> 
> The question asks whether it is better, so the answer may begin with a plain no.

> **[exam-tip]**
> Larger is better for a lower bound, which is the opposite of the rule you have just used in part (c), so read the question before deciding which way the comparison goes.
> 
> - A lower bound is a guarantee that nothing shorter exists, and the higher that guarantee the more it tells you
> - Deleting a different vertex gives a different bound, and there is no way to tell in advance which choice will give the larger one

### 4((f)) — 2 marks
The optimal route is at least the better lower bound from part (e) and at most the better upper bound from part (c)

$191 \leq \text{optimal distance} \leq 203$

**[B1] [B1]**

> **[mark-scheme]**
> **B1**: Your own two numbers used correctly, with the larger of the two lower bounds on the left and the smaller of the two upper bounds on the right. Any inequality, or any clear indication of an interval, is accepted.
> 
> **B1**: A correct answer only, 191 to 203, with correct inequalities. Both $191 \leq \text{optimal distance} \leq 203$ and $191 < \text{optimal distance} \leq 203$ are accepted.
> 
> The official scheme awards these two marks together, as one mark for using your own values correctly and a second, dependent on it, for the fully correct interval.
> 
> If your answer to part (b) is below 188 there are no marks at all here, because the interval would then be impossible.
> 
> Subtracting one bound from the other and writing 12 is not an interval, and scores the first mark only.

> **[exam-tip]**
> Take the two ends from parts (c) and (e) rather than from parts (b) and (d)(ii), because the question asks for the smallest interval you can be confident about.
> 
> - Using 191 and 206 instead would give a wider interval and lose the second mark
> - Check the inequality reads the right way round before writing it down, since a reversed interval scores nothing

## Q8 — medium — 7 marks · exam-questions

### 3((a)) — 2 marks
The shortcut method starts from the closed walk that goes along every arc of the given tree twice, then replaces a repeated stretch by a single direct arc

The tree has weight 314, printed underneath it, so travelling every arc twice gives a route of

$2 \times 314 = 628$

Mei only has to visit each town at least once, so she may pass through a town twice, and that is what makes a shortcut possible

Reaching $C$ and then coming back through $B$ and $A$ to get to $D$ uses three arcs of the tree

$59 + 57 + 67 = 183$

Replace that whole stretch by the single road $C D$, which costs only 71

- The route it gives is A – F – A – B – E – B – C – D – A, which visits every town and returns to $A$

*Shortcut: add CD and remove AD, BA and BC*

$628 - 183 + 71$

$\text{upper bound} = 516  \text{km}$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Starts from twice the weight of the given tree, 628, and adds and subtracts at least one arc to reach a network of weight below 628. The network left behind must be connected and Eulerian, which means every town sits on an even number of arcs.
> 
> **A1**: A correct answer only, with the shortcut and the length consistent with each other and the length stated below 520. The arcs added and subtracted must both be clearly stated.
> 
> Adding EF and removing EB, BA and AF, which gives 509, is the other shortcut the official scheme prints, and it earns both marks equally.

> **[exam-tip]**
> Write down which arcs you are adding and which you are removing, in words. The scheme asks for both, and a bare final number scores nothing here however right it is.
> 
> - Check every town ends up on an even number of arcs, since a route that has to come back to its start cannot leave a town on an odd number
> - The question fixes a target of 520, so test your answer against it before moving on

### 3((b)) — 2 marks
The nearest neighbour algorithm starts at $A$ and repeatedly moves to the nearest town not yet visited, then returns to $A$ at the end

From $A$ the nearest town is $B$ at 57, then $E$ at 66, then $F$ at 69, then $D$ at 78, then $C$ at 71

**Final answer:** **A – B – E – F – D – C – A**

**[B1]**

The last leg back to $A$ is forced rather than chosen, and $C A$ costs 76

$57 + 66 + 69 + 78 + 71 + 76$

$\text{upper bound} = 417  \text{km}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, the route A – B – E – F – D – C – A, which must return to $A$. It may be given as the towns or as the arcs, AB, BE, EF, FD, DC, CA, but not the weights alone.
> 
> **B1**: A correct answer only, 417.

> **[exam-tip]**
> Nearest neighbour beats the shortcut method here by nearly a hundred kilometres, so it is worth running even when part (a) has already produced a bound below the target.
> 
> - Cross each town out of the table as you visit it, so you never offer yourself one twice
> - A list of weights with no towns or arcs named scores nothing, however correct the total

### 3((c)) — 3 marks
Deleting $E$ leaves the five towns $A$, $B$, $C$, $D$ and $F$, and a lower bound is built from the minimum spanning tree of what is left plus the two shortest roads back to $E$

The residual minimum spanning tree uses $A B$ at 57, $A D$ at 59, $A F$ at 65, $B C$ at 67

$57 + 59 + 65 + 67 = 248$

**[B1]**

The two shortest roads at $E$ are $B E$ at 66 and $E F$ at 69, and both are added on separately

$248 + 66 + 69$

**[M1]**

$\text{lower bound} = 383  \text{km}$

**[A1]**

> **[mark-scheme]**
> **B1**: The correct length of the residual minimum spanning tree, 248. This mark may be implied by later working.
> 
> **M1**: Adds 66 and 69, the two shortest arcs at $E$, to the weight of your residual tree. The official scheme accepts any residual weight from 231 to 265 for this mark and gives the benefit of the doubt, but the tree must contain only four arcs. The mark may also be implied by a correct lower bound.
> 
> **A1**: A correct answer only, 383.
> 
> An answer of 383 with no working at all still earns the method and accuracy marks but loses the first mark, since nothing shows the residual tree weight.
> 
> The two arcs at $E$ must appear separately as 66 and 69. Combining them into 135 before adding loses the accuracy mark even though the answer is the same.

> **[exam-tip]**
> Deleting $E$ takes out five roads, and only $B E$ was in the given tree, so the residual tree here is that tree with $B E$ removed.
> 
> - Count the arcs before adding anything on: five towns need exactly four
> - Show the two roads at $E$ as separate numbers, since combining them loses a mark even though the total is unchanged

## Q9 — medium — 5 marks · exam-questions

### 1((a)) — 2 marks
The nearest neighbour algorithm starts at $A$ and repeatedly moves to the nearest point not yet visited, then returns to $A$ at the end

From $A$ the nearest point is $B$ at 35, then $F$ at 31, then $D$ at 44, then $E$ at 39, then $C$ at 53

**Final answer:** **A – B – F – D – E – C – A**

**[M1]**

The last leg back to $A$ is forced rather than chosen, and $C A$ costs 42

$35 + 31 + 44 + 39 + 53 + 42$

$\text{upper bound} = 244  \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: Applies nearest neighbour from $A$ and reaches $A$, $B$, $F$, $D$, $E$, $C$. A route that does not return to the start is condoned for this mark, and the correct length of 244 on its own also earns it.
> 
> **A1**: A correct answer only, both the route and the length. The route may be given as vertices, ABFDECA, or as arcs, AB, BF, FD, DE, EC, CA, and the arcs may also be numbered 1 2 6 4 5 3 across the top of the table. The weights are not accepted on their own, on either mark.
> 
> Doubling the length to 488 is not ignored as subsequent working, so leave the total at 244.

> **[exam-tip]**
> The two marks here are for two different things, so answering only half the question costs one of them: the route earns the first and the length earns the second.
> 
> - Write the route out in full, ending back at $A$, since a route stopping at $C$ scores the method mark but not the accuracy mark
> - Naming the arcs instead of the points is fine, but a bare list of weights is not

### 1((b)) — 3 marks
Deleting $B$ leaves the five points $A$, $C$, $D$, $E$ and $F$, and a lower bound is built from the minimum spanning tree of what is left plus the two shortest distances back to $B$

The residual minimum spanning tree uses $D E$ at 39, $A C$ at 42, $D F$ at 44, $C D$ at 47

$39 + 42 + 44 + 47 = 172$

**[B1]**

The two shortest distances at $B$ are $B F$ at 31 and $A B$ at 35, and both are added on separately

$172 + 31 + 35$

**[M1]**

$\text{lower bound} = 238  \text{km}$

**[A1]**

> **[mark-scheme]**
> **B1**: A correct answer only, the weight of the residual minimum spanning tree is 172. The official scheme names its four arcs as AC, CD, DF, DE and prints the sum as 42 + 47 + 44 + 39, so any order earns the mark, and it may be implied by later working.
> 
> **M1**: Adds 31 and 35, the two shortest arcs at $B$, to the weight of your residual tree, which must contain only four arcs.
> 
> **A1**: A correct answer only, 238.
> 
> An answer of 238 with no working at all still earns the method and accuracy marks but loses the first mark, since nothing shows the residual tree weight.
> 
> The two arcs at $B$ must appear separately as 31 and 35. Combining them into 66 before adding loses the accuracy mark even though the answer is the same.

> **[exam-tip]**
> Deleting $B$ takes out five distances, and the residual tree has to be rebuilt from the table rather than trimmed from part (a)'s route, which is a tour and not a tree.
> 
> - Count the arcs before adding anything on: five points need exactly four
> - Show the two distances at $B$ as separate numbers, since combining them loses a mark even though the total is unchanged

## Q10 — medium — 8 marks · exam-questions

### 1((a)) — 3 marks
The nearest neighbour algorithm starts at $A$ and repeatedly moves to the nearest city not yet visited, then returns to $A$ at the end

From $A$ the nearest city is $D$ at 27, then $E$ at 25, then $F$ at 21, then $B$ at 34, then $C$ at 58

**Final answer:** **A – D – E – F – B – C – A**

**[M1 A1]**

The last leg back to $A$ is forced rather than chosen, and at 56 it is the second longest road on the route

$27 + 25 + 21 + 34 + 58 + 56$

$\text{upper bound} = 221  \text{km}$

**[A1]**

> **[mark-scheme]**
> **M1**: Applies nearest neighbour from $A$ with the first five cities correct, $A$, $D$, $E$, $F$ and $B$. Numbering the cities 1 5 6 2 3 4 across the top of the table is accepted instead.
> 
> **A1**: The route correctly stated, which must return to $A$. A link drawn back to $A$ is accepted.
> 
> **A1**: The length correctly stated, 221.
> 
> Doubling the route length afterwards is not ignored as subsequent working, so leave the total at 221.

> **[exam-tip]**
> Doubling a nearest neighbour route is a common reflex, because doubling is how the *initial* upper bound is built from a spanning tree. It is wrong here: the route is already a closed tour.
> 
> - Nearest neighbour never looks ahead, so it can be left with an expensive last leg, as it is here
> - Cross each city out of the table as you visit it, so you never offer yourself one twice

### 1((b)) — 3 marks
Deleting $A$ leaves the five cities $B$ to $F$, and a lower bound is built from the minimum spanning tree of what is left plus the two shortest roads back to $A$

The residual minimum spanning tree uses $E F$ at 21, $D E$ at 25, $B F$ at 34, $C E$ at 38

$21 + 25 + 34 + 38 = 118$

**[B1]**

The two shortest roads at $A$ are $A D$ at 27 and $A E$ at 38, and both are added on separately

$118 + 27 + 38$

**[M1]**

$\text{lower bound} = 183  \text{km}$

**[A1]**

> **[mark-scheme]**
> **B1**: A correct answer only, the weight of the residual minimum spanning tree is 118. The sum written in any order earns it, so 34 + 21 + 25 + 38 is equally acceptable, and the mark may be implied by later working.
> 
> **M1**: Adds 27 and 38, the two shortest arcs at $A$, to the weight of your residual tree, which must contain only four arcs.
> 
> **A1**: A correct answer only, 183.
> 
> The official scheme is unusually generous here: 183 seen with no working at all scores all three marks in this part.
> 
> The two arcs at $A$ still have to appear separately as 27 and 38 wherever working is shown.

> **[exam-tip]**
> Count the arcs in your residual tree before adding anything on. Five cities need exactly four arcs, and a tree with the wrong number of arcs loses the method mark whatever the arithmetic does.
> 
> - Rebuild the tree from the table rather than editing part (a)'s route, which is a tour and not a tree
> - The two arcs at $A$ are the two smallest numbers in row $A$, so read them straight off

### 1((c)) — 2 marks
The optimal length is at least the lower bound from part (b) and at most the upper bound from part (a)

Part (b) gave 183 and part (a) gave 221

$183 \leq \text{length} \leq 221$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Your answers to parts (a) and (b) correctly used. Any inequalities, or any indication of an interval running from 183 to 221, earn this mark, so writing 183 to 221 is enough. The upper bound must be larger than the lower bound.
> 
> **A1**: A correct answer only. No follow through on your own values here, and correct inequalities or equivalent set notation are needed.
> 
> The strict form $183 < \text{length} \leq 221$ is condoned.

> **[exam-tip]**
> Smaller is better for an upper bound and larger is better for a lower bound, which is the opposite way round from what most people expect first time.
> 
> - Put the lower bound on the left and the upper bound on the right, and check the inequality reads the right way round before writing it down
> - The two ends come from different parts, so an interval built from one part alone cannot be right
