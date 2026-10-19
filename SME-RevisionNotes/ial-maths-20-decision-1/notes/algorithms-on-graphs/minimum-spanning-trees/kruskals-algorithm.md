---
note_id: "rn_MKNVGw6RMMppfB22"
title: "Kruskal's Algorithm"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/algorithms-on-graphs/minimum-spanning-trees/kruskals-algorithm
path: algorithms-on-graphs/minimum-spanning-trees/kruskals-algorithm
updated_at: "2026-07-02T08:19:38.618Z"
spec_point_ids: ["spcpt_jsvMbYSNrrYY9h3d"]
spec_point_codes: []
guided_study: false
---

# Kruskal's Algorithm

## Kruskal's Algorithm

> **Spec point** — `spcpt_jsvMbYSNrrYY9h3d`

## Kruskal's Algorithm

### What is Kruskal's algorithm?

- **Kruskal's algorithm** is a mathematical tool that can be used to connect all of the vertices in a **network **in a way that **reduces** costs, materials or time

  - It achieves this by finding a ***minimum spanning tree*** (MST).

### Why do we use Kruskal’s Algorithm?

- **Kruskal’s algorithm** is a series of steps that when followed will produce a **minimum spanning** **tree** for a **network**
- Finding a minimum spanning tree is useful in a lot of practical applications

  - It connects **all of the vertices** in the **most efficient way** possible
- The **number of edges** in a minimum spanning tree will always be **one less** than the **number of vertices** in the graph
- A minimum spanning tree **cannot** contain any cycles

### What are the steps of Kruskal’s Algorithm?

- **STEP 1**
Sort the **edges** in terms of **increasing weight**
- **STEP 2**
Select the **edge of least weight**

  - If there is more than one edge of the same weight, either may be used
- **STEP 3**
Select the **next edge of least weight** that has not already been chosen

  - **Reject **it if it forms a **cycle **with the other selected edges
  - Otherwise, **add it to your tree**
- **STEP 4** Repeat STEP 3 until **all of the vertices** in the graph are** connected**

  - If there are *n* nodes then there will be *n* - 1 edges in the minimum spanning tree
- **STEP 5**
**List the edges** in the minimum spanning tree in the **order they were added**

> **Exam Hint**
> **Draw the edges** included in the minimum spanning tree **as you go along; **this will make it easier to spot potential cycles.
> 
> Remember to state the **order** in which the edges are selected or rejected to get full marks for working!

> **Worked Example**
> Consider the network below.
> 
> ![Geometric diagram with labelled vertices A to H, connected by lines with various numeric labels, forming a larger outer and smaller inner square structure.](assets/15e168919877-7074-kruskals-mst.png)
> 
> a) Use Kruskal’s algorithm to find the minimum spanning tree. Show each step of the algorithm clearly.
> 
> **Answer**:
> 
> - *STEP 1** *
> *List the edges in order of increasing weight*
> 
> *EH (1)*
> *DH (2)*
> *AB (4)*
> *EF (5)*
> *FG (5)*
> *GH (6)*
> *BC (6)*
> *BF (7)*
> *CD (8)*
> *AD (9)*
> *AE (11)*
> *CG (15)*
> 
> - *STEP 2** *
> *Add the edge of least weight (EH)*
> 
> - *STEP 3 *
> *Add the next edge of least weight (DH)*
> 
> - *STEP 4** *
> *Repeat Step 3 *
> *Repeat adding the next edge of least weight each time provided it does not create a cycle until all vertices are connected*
> 
>   - *Add AB*
>   - *Add EF*
>   - *Add FG*
>   - *Reject GH as it forms a cycle*
>   - *Add BC*
>   - *Add BF*
> 
> ![_0QbiNdw_picture-1](assets/40efcc0511f9-0qbindw-picture-1.png)
> 
> **Final answer:** **Edges are added in the order: EH (1), DH (2), AB (4), EF (5), FG (5), reject GH, BC (6), BF (7)**** **
> 
> b) State the total weight of the minimum spanning tree.
> 
> **Answer**:
> 
> > *Add up the weights of the edges in the minimum spanning tree  *
> 
> *1 + 2 + 4 + 5 + 5 + 6 + 7 = 30  *
> 
> **Final answer:** **Total weight = 30**
