---
note_id: "rn_Qjx3NtbZ7wCPPWdv"
title: "The Travelling Salesman Problem"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/algorithms-on-graphs/the-travelling-salesman-problem/the-travelling-salesman-problem
path: algorithms-on-graphs/the-travelling-salesman-problem/the-travelling-salesman-problem
updated_at: "2026-07-02T08:19:38.633Z"
spec_point_ids: ["spcpt_cm3fwdmGY3HDyvjV"]
spec_point_codes: []
guided_study: false
---

# The Travelling Salesman Problem

## The Classical & Practical Travelling Salesman Problem

> **Spec point** — `spcpt_cm3fwdmGY3HDyvjV`

## The Classical & Practical Travelling Salesman Problem

### What is the Travelling Salesman Problem?

- In the **Travelling Salesman Problem**, the objective is to find the **tour of least weight** in a given network

  - A **tour **is a **walk **that **visits every vertex** in the network and returns to the **start vertex**
  
    - A tour could visit a vertex** more than once**
    - A tour is** **a** Hamiltonian cycle i**f it visits each vertex (other than the start vertex)** exactly once **
- For the **classical **travelling salesman problem

  - Each vertex is visited **exactly once** before returning to the start vertex
- For the **practical** travelling salesman problem

  - Each vertex must be visited **at least once** before returning to the start vertex
- There is no algorithm that will **always** provide an **optimal solution**

  - A **lower** and **upper** bound can be generated for the **tour** of **least** **weight**
  - If the **lower** and **upper** bound happen to be **equal**, an **optimal** solution has been found

### What is a table of least distances?

- A **table of least distances** shows the **shortest** distance between any **two vertices** in a graph

  - In some cases, the **direct route** between two vertices may **not** be the **shortest**
- The table of least distances creates a **complete** network

  - Therefore it will contain a **Hamiltonian cycle**
- The table of least distances turns a **practical travelling salesman problem** into a **classical travelling salesman problem**

### How do I find the table of least distances?

- For smaller networks, values in the **table of least distances** can often be found by** inspection**

  - Using **Dijkstra's algorithm **will always find the shortest routes between pairs of vertices
  
    - An exam question will be clear if this is required but this is uncommon
- A **table of least distances** is created by ensuring every entry satisfies the **triangle inequality**

  - The** longest side** of a triangle **≤ **the** sum **of the lengths of the** other two sides**
  - 'Sides of the triangle' could be made from one or more edges in a network
  
    - There would be lots of them, even in small networks!
- To construct a table of least distances follow the steps below

- **STEP 1**
Put a line through each cell along the leading diagonal

  - There will be no loops!

- **STEP 2**
Complete the row for a particular vertex with the **distance** between that vertex and each **adjacent** vertex

  - Check (by inspection) if the direct connections are actually the **shortest **distances and change as necessary
- **STEP 3**
Complete the rest of the connections between that **particular vertex **and all **remaining (non-adjacent) vertices**
Make sure the value used is the **shortest route **that can be travelled between each pair
- **STEP 4**
Copy the values in the completed row down the **corresponding column**

  - A complete network is undirected so the table of least distances will have symmetry

- **STEP 5**
Repeat STEP 2 to STEP 4 for each vertex until the table is **complete**

> **Exam Hint**
> - Remember that the table of least values has a **line of symmetry **along the leading diagonal for an **undirected network**
> 
>   - Complete one half carefully first, then map over to the second half

> **Worked Example**
> The network below contains six vertices representing villages and the edges (roads) that connect them. The weighting of the edges represents the time, in minutes, that it takes to walk along a particular road between two villages.
> 
> ![3-10-6-ib-ai-hl-bounds-for-travelling-salesman-problem-we-1](assets/b45f53a83550-3-10-6-ib-ai-hl-bounds-for-travelling-salesman-p.png)
> 
> a) Explain why the network in the diagram is not a complete network.
> ** Answer:**
> 
> **Final answer:** **It is not a complete network as each vertex is not connected**
> **to every other vertex by a single edge**
> **e.g. there is no single edge that connects vertices B and D**
> 
> b) Complete the table of least distances for the network below.
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A |   |   |   |   |   |   |
> | B |   |   |   |   |   |   |
> | C |   |   |   |   |   |   |
> | D |   |   |   |   |   |   |
> | E |   |   |   |   |   |   |
> | F |   |   |   |   |   |   |
> 
> ** Answer:**
> 
> - *STEP 1*
> *Put a line through each cell on the leading diagonal*
> * *
> - *STEP 2*
> *Fill in the table with the direct connections from the graph, starting from vertex A*
> 
>   - *Check that the direct connection is the shortest route in all cases*
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* |   |   |
> | B |   | *-* |   |   |   |   |
> | C |   |   | *-* |   |   |   |
> | D |   |   |   | *-* |   |   |
> | E |   |   |   |   | *-* |   |
> | F |   |   |   |   |   | *-* |
> 
> - *STEP 3*
> *Find the shortest routes between vertices A and E, and A and F, then fill these values in the table*
> 
> * A*$\rightarrow$*E:    A*$\rightarrow$*C*$\rightarrow$*E = 13*
> 
> *A*$\rightarrow$*F:    A*$\rightarrow$*C*$\rightarrow$*E*$\rightarrow$*F = 21*
> * *
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B |   | *-* |   |   |   |   |
> | C |   |   | *-* |   |   |   |
> | D |   |   |   | *-* |   |   |
> | E |   |   |   |   | *-* |   |
> | F |   |   |   |   |   | *-* |
> 
> - *STEP 4*
> *Complete column A with the values recorded in row A.*
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B | *14* | *-* |   |   |   |   |
> | C | *7* |   | *-* |   |   |   |
> | D | *11* |   |   | *-* |   |   |
> | E | *13* |   |   |   | *-* |   |
> | F | *21* |   |   |   |   | *-* |
> 
> - *STEP 5*
> *The table is not complete so return to Step 2*
> 
> - *STEP 2*
> *Fill in the table with the direct connections from vertex B*
> 
> > *  *
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B | *14* | *-* | *13* |   | *13* | *9* |
> | C | *7* |   | *-* |   |   |   |
> | D | *11* |   |   | *-* |   |   |
> | E | *13* |   |   |   | *-* |   |
> | F | *21* |   |   |   |   | *-* |
> 
> - *STEP 3*
> *Complete the table with the shortest route between the non-adjacent vertices B and D*
> 
> * B*$\rightarrow$*D:    B*$\rightarrow$*C*$\rightarrow$*D = 18*
> *  *
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B | *14* | *-* | *13* | * 18* | *13* | *9* |
> | C | *7* |   | *-* |   |   |   |
> | D | *11* |   |   | *-* |   |   |
> | E | *13* |   |   |   | *-* |   |
> | F | *21* |   |   |   |   | *-* |
> 
> - *STEP 4*
> *Complete column B with the values recorded in row B*
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B | *14* | *-* | *13* | * 18* | *13* | *9* |
> | C | *7* | * 13* | *-* |   |   |   |
> | D | *11* | * 18* |   | *-* |   |   |
> | E | *13* | * 13* |   |   | *-* |   |
> | F | *21* | * 9* |   |   |   | *-* |
> 
> - *STEP 5*
> *The table is not complete so return to Step 2*
> 
> - *STEP 2*
> *Fill in the table with the direct connections from vertex C*
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B | *14* | *-* | *13* | * 18* | *13* | *9* |
> | C | *7* | * 13* | *-* | *5* | *6* |   |
> | D | *11* | * 18* |   | *-* |   |   |
> | E | *13* | * 13* |   |   | *-* |   |
> | F | *21* | * 9* |   |   |   | *-* |
> 
> - *STEP 3*
> *Complete the table with the shortest route between the non-adjacent vertices C and F*
> 
> * CF:    C*$\rightarrow$*E*$\rightarrow$*F = 14*
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B | *14* | *-* | *13* | * 18* | *13* | *9* |
> | C | *7* | * 13* | *-* | *5* | *6* | *14* |
> | D | *11* | * 18* |   | *-* |   |   |
> | E | *13* | * 13* |   |   | *-* |   |
> | F | *21* | * 9* |   |   |   | *-* |
> 
> - *STEP 4*
> *Complete column C with the values recorded in row C*
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B | *14* | *-* | *13* | * 18* | *13* | *9* |
> | C | *7* | * 13* | *-* | *5* | *6* | *14* |
> | D | *11* | * 18* | *5* | *-* |   |   |
> | E | *13* | * 13* | *6* |   | *-* |   |
> | F | *21* | * 9* | *14* |   |   | *-* |
> 
> - *STEP 5*
> *The table is not complete so return to Step 2*
> 
> - *STEP 2*
> *Fill in the table with the direct connections from vertex D*
> *The direct route between D and F is not the shortest route*
> 
> *D*$\rightarrow$*F = 20*
> * *
> 
> *D*$\rightarrow$*E*$\rightarrow$*F = 18*
> 
> > *    *
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B | *14* | *-* | *13* | * 18* | *13* | *9* |
> | C | *7* | * 13* | *-* | *5* | *6* | *14* |
> | D | *11* | * 18* | *5* | *-* | *10* | *18* |
> | E | *13* | * 13* | *6* |   | *-* |   |
> | F | *21* | * 9* | *14* |   |   | *-* |
> 
> - *STEP 3*
> *There are no non-adjacent vertices for D left to complete*
> * *
> - *STEP 4*
> *Complete column D with the values recorded in row D*
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B | *14* | *-* | *13* | * 18* | *13* | *9* |
> | C | *7* | * 13* | *-* | *5* | *6* | *14* |
> | D | *11* | * 18* | *5* | *-* | *10* | *18* |
> | E | *13* | * 13* | *6* | * 10* | *-* |   |
> | F | *21* | * 9* | *14* | * 18* |   | *-* |
> 
> - *STEP 5*
> *The table is not complete so return to Step 2*
> 
> - *STEP 2*
> *Fill in the table with the direct connections from vertex E*
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | *-* | *14* | *7* | *11* | *13* | *21* |
> | B | *14* | *-* | *13* | * 18* | *13* | *9* |
> | C | *7* | * 13* | *-* | *5* | *6* | *14* |
> | D | *11* | * 18* | *5* | *-* | *10* | *18* |
> | E | *13* | * 13* | *6* | *10* | *-* | *8* |
> | F | *21* | * 9* | *14* | *18* |   | *-* |
> 
> - *STEP 3*
> *There are no other connections for vertex E*
> 
> - *STEP 4*
> *Complete column E with the values recorded in row E*
> 
> - *STEP 5*
> *The table is complete so stop*
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | **Final answer:** **-** | **Final answer:** **14** | **Final answer:** **7** | **Final answer:** **11** | **Final answer:** **13** | **Final answer:** **21** |
> | B | **Final answer:** **14** | **Final answer:** **-** | **Final answer:** **13** | **Final answer:** ** 18** | **Final answer:** **13** | **Final answer:** **9** |
> | C | **Final answer:** **7** | **Final answer:** **13** | **Final answer:** **-** | **Final answer:** **5** | **Final answer:** **6** | **Final answer:** **14** |
> | D | **Final answer:** **11** | **Final answer:** **18** | **Final answer:** **5** | **Final answer:** **-** | **Final answer:** **10** | **Final answer:** **18** |
> | E | **Final answer:** **13** | **Final answer:** **13** | **Final answer:** **6** | **Final answer:** ** 10** | **Final answer:** **-** | **Final answer:** **8** |
> | F | **Final answer:** **21** | **Final answer:** **9** | **Final answer:** **14** | **Final answer:** ** 18** | **Final answer:** **8** | **Final answer:** **-** |
