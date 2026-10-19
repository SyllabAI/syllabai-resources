---
note_id: "rn_r2JDy9yvCxhQ7jYZ"
title: "Route Inspection & Repeated Routes"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/algorithms-on-graphs/the-route-inspection-algorithm/route-inspection-and-repeated-routes
path: algorithms-on-graphs/the-route-inspection-algorithm/route-inspection-and-repeated-routes
updated_at: "2026-07-02T08:19:38.660Z"
spec_point_ids: ["spcpt_37mJDmGbj5wYYzWF"]
spec_point_codes: []
guided_study: false
---

# Route Inspection & Repeated Routes

## Networks with more than 2 Odd Vertices

> **Spec point** — `spcpt_37mJDmGbj5wYYzWF`

## Networks with more than 2 Odd Vertices

### How do I solve the Chinese postman problem when a network has more than 2 odd nodes?

- In any graph there will always be an **even number of odd vertices (nodes)**

  - The **total sum of the degrees** of the nodes is **double** the **number of edges**
- If there are **more than two** **odd vertices (nodes)**

  - The **shortest path** between** each possible pairing** of the odd nodes must be considered
  - The **shortest **of these pairings will be the **minimum weight** of the **paths** that need to be repeated
- In cases of **four odd nodes,** there will be **three** pairings of odd nodes

  - For example in a graph where the four odd nodes are P, Q, R and S the pairings would be
  
    - PQ and RS
    - PR and QS
    - PS and QR
  - In an exam question there will be a **maximum of 4 odd nodes**

### What are the steps of the Chinese postman algorithm for networks with more than 2 odd nodes?

- **STEP 1**
Inspect the degree of all nodes and identify any **odd nodes**
- **STEP 2**
Find **all possible pairings** between the odd nodes
- **STEP 3**
For each possible pairing of odd nodes, find (by inspection) the **shortest path **between each pair of nodes
The** pairing with the smallest total of shortest paths **will be **repeated**
**Add** any **repeated edges** required to the network
- **STEP 4**
Write down an **Eulerian circuit **of the **adjusted network** to find a possible route
Find the **sum of the edges traversed** to find the total weight

### What variations may there be on the Chinese postman algorithm?

- A variation on the **4 odd nodes** problem is that the **start **and **end** nodes can be **any two** of the odd nodes

  - The problem is to find the **shortest route and** the corresponding **start** and **end** nodes
  - To solve this problem
  
    - Find the length of the shortest paths for **all** possible pairings of the odd nodes
    - Choose the **shortest of the shortest paths** between any 2 of them to be **repeated**
    - The** other two** odd vertices will be your **start and finish points**
- Another variation is that the **weighting** of an edge between a pair of nodes may change

  - This could depend on whether it is the **first time** it is being traversed or whether it is being **repeated**
  - For example, if an inspector was checking a pipeline for defects
  
    - The first time going along a section of pipeline could take longer during inspection
    - Walking along an already inspected section to get from one node to another may take less time

> **Worked Example**
> The network shown below displays the distances, in kilometres, of the main roads between towns A, B, C, D and E.
> Each road is to be inspected for potholes.
> 
> ![chinese-postman-example-2](assets/464bc5f385e2-chinese-postman-example-2.png)
> 
> a) Explain why the network does not contain an Eulerian circuit.
> 
> **Answer:**
> 
> > *Inspect the degree of each node*
> 
> *A: 3 (odd)*
> *B: 3 (odd)*
> *C: 3 (odd)*
> *D: 3 (odd)*
> *E: 2 (even)*
> 
> **Final answer:** **The graph does not contain an Eulerian circuit as some of the vertices are odd**
> 
> b) Find the shortest route that starts and finishes at town A and allows for each road to be inspected.
> 
> **Answer:**
> 
> - *STEP 1*
> *There are 4 odd nodes, A, B, C and D*
> * *
> - *STEP 2*
> *The possible pairings between the odd nodes are AB and CD, AC and BD, and AD and BC*
> * *
> - *STEP 3*
> *By inspection, find the shortest paths (and the edges involved) for each pairing*
> 
> *AB + CD = (ABD) + (CD) = 12 + 10 = 22*
>  
> *AC + BD = (ADC) + (BD) = 18 + 4 = 22*
>  
> *AD + BC = (AD) + (BC) = 8 + 9 = 17  *$\underset{}{\leftarrow}$*   shortest *
> 
> > *The shortest total of paths to be repeated is for AD and BC, so add the edges AD and BC to the graph*
> * *
> 
> ![chinese-postman-example-2-2](assets/6abf36cda68d-chinese-postman-example-2-2.png)
> 
> - *STEP 4*
> *Write down an Eulerian circuit (from the adjusted graph) starting at vertex A*
> 
> **Final answer:** **Eulerian circuit: ADABDCBCEA**
> 
> > *There are other possible Eulerian circuits that you could find*
> 
> c) State the total length of the shortest route.
> 
> **Answer:**
> 
> > *Add the length of each edge in the graph, then add the weight of the repeated edges*
> 
> *15 + 17 + 8 + 4 + 9 + 10 + 6 = 69 (edges in the original graph)*
> 
> *17 (repeated edges)*
> 
> **Final answer:** **Total length of the shortest route: 86 km**
