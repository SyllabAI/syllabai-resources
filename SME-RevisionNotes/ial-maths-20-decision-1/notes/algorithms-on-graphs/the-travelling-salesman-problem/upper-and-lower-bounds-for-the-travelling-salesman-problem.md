---
note_id: "rn_Y5GQSK9GNvgTMqrh"
title: "Upper & Lower Bounds for the Travelling Salesman Problem"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/algorithms-on-graphs/the-travelling-salesman-problem/upper-and-lower-bounds-for-the-travelling-salesman-problem
path: algorithms-on-graphs/the-travelling-salesman-problem/upper-and-lower-bounds-for-the-travelling-salesman-problem
updated_at: "2026-07-02T08:19:38.618Z"
spec_point_ids: ["spcpt_CDrxV4K9j3rBppb6", "spcpt_9YmCJGKWp5cKsBqG", "spcpt_h68Jt9Vr3bmcy6FN"]
spec_point_codes: []
guided_study: false
---

# Upper & Lower Bounds for the Travelling Salesman Problem

## Finding an Upper Bound using a Minimum Connector

> **Spec point** — `spcpt_CDrxV4K9j3rBppb6`

## Finding an Upper Bound using a Minimum Connector

### Why do I need to find an upper bound?

- There is **no efficient algorithm** to find the optimal solution for the** travelling salesman problem**

  - An **upper and lower bound** for the solution to the problem can be found
  - The **optimal solution** (the shortest route)** **will lie **within **these bounds
  
    - Lower bound$\leq$ **optimal solution **$\leq$ upper bound
- The aim is to find a **minimum value for the upper bound**

  - This will reduce the size of the interval between the upper and lower bounds

### How do I find the upper bound?

- Use a** minimum spanning tree** to find an **upper bound **for a network
- **STEP 1**
Find a **minimum spanning tree** for the network using either **Prim's** or **Kruskal's **algorithm

  - If you have the **table of distances**, use Prim's algorithm
  - If you have the **graph** only, use Prim's or Kruskal's algorithm
- **STEP 2**
**Double the weight** of the minimum spanning tree to find an **initial **upper bound

  - Each vertex can therefore definitely be visited and the starting vertex returned to
- **STEP 3**
**Improve** the upper bound by finding shortcuts

  - Use some of the **edges** **not included** in the minimum spanning tree to **reduce the weight**

> **Worked Example**
> The network below contains six vertices representing villages and the edges (roads) that connect them. The weighting of the edges represents the time, in minutes, that it takes to walk along a particular road between two villages.
> 
> ![3-10-6-ib-ai-hl-bounds-for-travelling-salesman-problem-we-1](assets/b45f53a83550-3-10-6-ib-ai-hl-bounds-for-travelling-salesman-p.png)
> 
> a) Find an initial upper bound for the travelling salesman problem.
> 
> **Answer:**
> 
> - *STEP 1*
> *The question contains the graph but you have not been asked to find the table of least distances*
> *Apply Kruskal's algorithm to find a minimum spanning tree of the network*
> *List the edges in order of increasing weight*
> 
> *CD (5)*
> *CE (6)*
> *AC (7)*
> *EF (8)*
> *BF (9)*
> *DE (10)*
> *AD (11)*
> *BC (13)*
> *BE (13)*
> *AB (14)*
> *DF (20)*
> *  *
> 
> > *Add the edge of least weight (CD), then the next edge of least weight (CE)*
> *Repeat adding the next edge of least weight each time provided it does not create a cycle until all vertices are connected*
> * *
> 
> *Edges added in the order: CD (5), CE (6), AC (7), EF (8), BF (9) *
> *  *
> 
> ![WdntKlV2_mst](assets/b18cf9798ec1-wdntklv2-mst.png)
> 
> - *STEP 2*
> *Find the weight of the minimum spanning tree*
> 
> *5 + 6 + 7 + 8 + 9 = 35*
> 
> > *Double the weight of the minimum spanning tree to find the initial upper bound of the solution*
> 
> *35 x 2 = 70*
> 
> **Initial upper bound = 70 minutes**
> ** **
> 
> b) Show that the initial upper bound can be reduced to 54 by finding one shortcut.
> 
> **Answer:**
> 
> - *STEP 3*
> *Identify which edges could be used to replace repeated edges in the minimum spanning tree*
> 
> *Single edge: AB (14)*
> 
> *Repeated pathway: AC + CE + EF + FB (30)*
> 
> > *Subtract the weight of the single edge from the repeated pathway to calculate the weight saved by using the short cut*
> 
> *30 - 14 = 16*
> 
> > *Subtract the weight saving from the initial upper bound*
> 
> *70 - 16 = 54*
> 
> **Final answer:** **Improved upper bound = 54 minutes**
> 
> > *This can also be seen as 70 - 30 + 14 = 54*
> *Subtract the 'repeated pathway' then add the 'shortcut'*

## Finding a Lower Bound using a Minimum Connector

> **Spec point** — `spcpt_9YmCJGKWp5cKsBqG`

## Finding a Lower Bound using a Minimum Connector

### Why do I need to find the lower bound?

- There is **no efficient algorithm** to find the **optimal** solution for the travelling salesman problem

  - An **upper and lower bound** for the solution to the problem can be found
  - The **optimal solution** (the shortest route)** **will lie **within **these bounds
  
    - Lower bound $\leq$ **optimal solution **$\leq$** **upper bound
- The aim is to find a **maximum value **for the** lower bound**

  - This will reduce the size of the interval between the upper and lower bounds
- An **optimal solution** is found if

  - The **lower bound** gives a **Hamiltonian cycle**
  
    - This is only true if the MST is created from a** table of least distances**
  - The** lower bound **has the** same value **as the **upper bound**
- If the lower bound is **not **a Hamiltonian cycle then** **

  - lower bound < optimal solution

### How do I find the lower bound?

- Use a **minimum spanning tree** to find a **lower bound** for a network

  - Apply the steps of the algorithm below to a **table of least distances**
  ** **
- **STEP 1**
Remove a** vertex** and all of its **associated edge**s from the network
- **STEP 2**
Find a **minimum spanning tree **for the remaining **network **and write down its** total weight**

  - This spanning tree is known as the **residual minimum spanning tree** (RMST)
- **STEP 3**
Identify the** two shortest individual edges **that can **connect** the **missing vertex **to the **RMST**
Find the** sum **of the** total weight **of the** RMST **and the** two connecting edges**
** **
- **STEP 4**
Repeat Steps 1 to 3 for **each vertex** in the network
- **STEP 5**
When the network has been tested for **each missing vertex**, identify the** maximum value**

  - This maximum value is the **greatest possible lower bound**

- In many problems Steps 4 and 5 will not be required

  - An exam question will often dictate which vertex to delete
  - There will be no need to repeat for each vertex
- This method may be referred to as the **deleted vertex method**

> **Worked Example**
> The table below contains six vertices representing villages and the roads that connect them. The weighting of the edges represents the time in minutes that it takes to walk along a particular road between two villages.
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | - | 14 | 7 | 11 | 13 | 21 |
> | B | 14 | - | 13 | 18 | 13 | 9 |
> | C | 7 | 13 | - | 5 | 6 | 14 |
> | D | 11 | 18 | 5 | - | 10 | 18 |
> | E | 13 | 13 | 6 | 10 | - | 8 |
> | F | 21 | 9 | 14 | 18 | 8 | - |
> 
> a) By deleting vertex A and using Prim’s algorithm, find a lower bound for the time taken to start at village A, visit each of the other villages and return to village A
> 
> **Answer:**
> 
> - *STEP 1*
> *Delete vertex A in the table*
> - *STEP 2*
> *Perform Prim's algorithm on the remaining vertices in the table*
> 
> ![table-1](assets/eb6c44a1c13f-table-1.png)
> 
> *Edges added in the order: BF (9), EF (8), CE (6), CD (5)*
> 
> *Total weight of the residual minimum spanning tree = 9 + 8 + 6 + 5 = 28*
> *  *
> 
> - *STEP 3*
> *Identify the two shortest edges that connect A to the minimum spanning tree*
> 
> *AC (7), AD (11)*
> 
> > *Add together the total weight of the minimum spanning tree and the weights of the two shortest lengths connecting it to A*
> 
> *28 + 7 + 11 = 46*
> 
> **Final answer:** **Lower bound = 46 minutes**
> 
> b) Show that by deleting vertex E instead, a higher lower bound can be found.
> 
> **Answer:**
> 
> - *STEP 1*
> *Delete vertex A in the table*
> - *STEP 2*
> *Perform Prim's algorithm on the remaining vertices in the table*
> 
> ![delete-vertex-e](assets/10a70e31f499-delete-vertex-e.png)
> 
> * *
> *Edges added in the order: AC (7), CD (5), BD/DF (18), BF (9) *
> 
> *Total weight of the residual minimum spanning tree = 7 + 5 + 18 + 9 = 39*
> *  *
> 
> - *STEP 3*
> *Identify the two shortest edges that connect E to the minimum spanning tree*
> 
> *CE (6), EF (8)*
> 
> > *Add together the total weight of the minimum spanning tree and the weights of the two shortest lengths connecting it to E*
> 
> *39 + 6 + 8 = 53*
> 
> **Final answer:** **Lower bound = 53 minutes**
> **This is a higher lower bound than found when vertex A was deleted (46 minutes)**

## Nearest Neighbour Algorithm

> **Spec point** — `spcpt_h68Jt9Vr3bmcy6FN`

## Nearest Neighbour Algorithm

### What is the nearest neighbour algorithm?

- The **nearest neighbour algorithm** is another method to find an **upper bound**
- The algorithm can be performed on a **complete** network with** at least 3 vertices**

  - It will generate a **low** **weight **Hamiltonian cycle
  
    - This low weight cycle will not necessarily be the least weight cycle
  - The weight of the cycle can be considered an **upper bound**
- The **best upper bound** is the upper bound with the **smallest value**
- The nearest neighbour algorithm can only be used on certain types of graph

  - The graph must be **complete** and satisfy the **triangle inequality**
- If needs be, the **table of least distances **should be found first

### What are the steps of the nearest neighbour algorithm?

- **STEP 1**
Choose a **starting vertex**
** **
- **STEP 2**
Select the **edge of least weigh**t from the **current vertex** to an **adjacent unvisited vertex**

  - If there is more than one edge of least weight pick one at random
  - Move to this vertex (column in matrix form)
  - If this is the **final vertex** to be visited go to STEP 3
  - Otherwise disregard (cross out in matrix form) any edges that go to vertices already visited and repeat STEP 2
- **STEP 3**
Add a final edge to return to the **starting vertex**
** **
- **STEP 4**
Find the **weight** of the resulting Hamiltonian cycle
This is an upper bound for the travelling salesman problem
- **STEP 5**
Repeat STEP 1 to STEP 4 starting with a different **vertex** in the network
When the network has been tested for **each vertex** as the starting vertex, identify the** minimum value**
This minimum value is the **least possible upper bound **that can be found by the nearest neighbour algorithm
- In many problems STEP 5 will not be required

  - An exam question will dictate which vertex to start at
  - There will be no requirement to repeat with all vertices as the starting vertex

> **Exam Hint**
> - Be careful not to confuse the **nearest neighbour algorithm** with **Prim's algorithm**
> 
>   - This is a common mistake because they are both performed on tables!
> - Questions may ask you to explain the difference between the two algorithms
> 
>   - The nearest neighbour algorithm selects the nearest vertex adjacent to the **current** vertex
>   - Prim's algorithm selects the nearest vertex adjacent to **any** vertex already visited

> **Worked Example**
> The table below contains six vertices representing villages and the roads that connect them. The weighting of the edges represents the time in minutes that it takes to walk along a particular road between two villages.
> 
> |   | A | B | C | D | E | F |
> |---|---|---|---|---|---|---|
> | A | - | 14 | 7 | 11 | 13 | 21 |
> | B | 14 | - | 13 | 18 | 13 | 9 |
> | C | 7 | 13 | - | 5 | 6 | 14 |
> | D | 11 | 18 | 5 | - | 10 | 18 |
> | E | 13 | 13 | 6 | 10 | - | 8 |
> | F | 21 | 9 | 14 | 18 | 8 | - |
> 
> Starting at village A, use the nearest neighbour algorithm to find an upper bound for the time it would take to visit each village and return to village A.
> 
> **Answer:**
> 
> - *STEP 1*
> *Start at vertex A (column A)*
> - *STEP 2*
> *Select the edge of least weight in column A (AC) and write it down*
> 
> ![~8028F-4_table-1](assets/806b103021c6-8028f-4-table-1.png)
> 
> *AC (7)*
> 
> > *Move to vertex/column C*
> *C is not the final vertex to be visited*
> *Disregard (cross out) the edge (value) in column C that would connect C to A as vertex A has already been visited*
> *Repeat Step 2*
> 
> - *STEP 2*
> *Select the edge of least weight (from those remaining) in column C (CD) and write it down*
> 
> ![0IaJRg_O_table-2](assets/a0476b30eb46-0iajrg-o-table-2.png)
> 
> *AC (7), CD (5)*
> 
> > *Move to column D*
> *D is not the final vertex*
> *Cross out the values for the vertices already visited (A and C)*
> *Repeat Step 2*
> 
> - *STEP 2*
> *Select the edge of least weight (from the remaining) in column D (DE) and write it down*
> 
> ![table-3](assets/d1a4e72f7b64-table-3.png)
> 
> * **AC (7), CD (5), DE (10)*
> 
> > *Move to column E*
> *E is not the final vertex*
> *Cross out the values for the vertices already visited (A, C and D)*
> *Repeat Step 2*
> 
> - *STEP 2*
> *Select the edge of least weight (from the remaining values) in column E (EF) and write it down*
> 
> ![table-4](assets/d2e823f9207f-table-4.png)
> 
> *AC (7), CD (5), DE (10), EF (8)*
> 
> > *Move to vertex F*
> *F is not the final vertex*
> *Cross out the values for the vertices already visited (A, C, D and E)*
> *Repeat Step 2*
> 
> - *STEP 2*
> *Select the edge of least weight (from the remaining values) in column F (BF) and write it down*
> 
> ![table-5](assets/abd06c95fd2e-table-5.png)
> 
> *AC (7), CD (5), DE (10), EF (8), BF (9)*
> 
> > *Move to vertex B*
> *B is the final vertex to be visited*
> *Go to Step 3*
> 
> - *STEP 3*
> *Choose the final edge (value) to get back from the last vertex (B) to the starting vertex (A)*
> 
> ![table-6](assets/1096a36046b7-table-6.png)
> 
> *AC (7), CD (5), DE (10), EF (8), BF (9), AB (14)*
> 
> *Hamiltonian cycle: ACDEFBA*
> 
> - *STEP 4*
> *Find the weight of the Hamiltonian cycle by adding together the weights of the edges forming it *
> 
> *Total weight = 7 + 5 + 10 + 8 + 9 + 14 = 53*
> 
> > *This is an upper bound for the travelling salesman problem*
> 
> **Final answer:** **Upper bound = 53 minutes**
