---
note_id: "rn_7nBDnbvzmVPb9gPm"
title: "Comparing MST Algorithms"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/algorithms-on-graphs/minimum-spanning-trees/comparing-mst-algorithms
path: algorithms-on-graphs/minimum-spanning-trees/comparing-mst-algorithms
updated_at: "2026-07-02T08:19:38.619Z"
spec_point_ids: ["spcpt_wdmRbpKyGXsKZdMF"]
spec_point_codes: []
guided_study: false
---

# Comparing MST Algorithms

## Comparing MST Algorithms

> **Spec point** — `spcpt_wdmRbpKyGXsKZdMF`

## Comparing MST Algorithms

### Which should I use - Prim’s or Kruskal’s algorithm?

- Both algorithms find a ***minimum spanning tree***

  - They may give different answers but both will produce a **minimal solution**
- **Prim’s algorithm **can be used in **either graph or matrix** form

  - If an MST is asked for and the information is given in **table/matrix** form, use **Prim’s algorithm**
- **Kruskal’s algorithm** can be used when the information is in **graph **form** **(or if a list of edges is available)

  - If trying to use Kruskal's algorithm from a table/matrix, it is best to draw a graph first
- **Kruskal's algorithm** allows edges to be added in **any** order

  - I.e. the tree can be **'split'** (unconnected) at stages of the algorithm
  - Prim's algorithm** 'builds' **as edges are added such that they will connect to edges **already** in the tree
- **Prim’s algorithm** is sometimes considered to be more **efficient** than **Kruskal’s algorithm** as

  - the edges **do not need to be ordered** at the start
  - it does not require **checking for cycles** at each step

- An **exam question** will usually specify which method should be used, otherwise either is fine

> **Exam Hint**
> - A common exam question is to state that **certain edges** need to be included in a spanning tree
> 
>   - You are then asked to describe which algorithm you should use and how it should be adapted
>   - You should start off by drawing in the edges given, and then complete the tree using Kruskal's algorithm!
>   
>     - This may not be a** minimum** spanning tree (depending on the edges that have to be included)
