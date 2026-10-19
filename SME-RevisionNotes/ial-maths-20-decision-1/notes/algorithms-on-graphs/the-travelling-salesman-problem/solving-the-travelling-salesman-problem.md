---
note_id: "rn_68dk3QZ4ndYqsPhy"
title: "Solving the Travelling Salesman Problem"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/algorithms-on-graphs/the-travelling-salesman-problem/solving-the-travelling-salesman-problem
path: algorithms-on-graphs/the-travelling-salesman-problem/solving-the-travelling-salesman-problem
updated_at: "2026-07-02T08:19:38.632Z"
spec_point_ids: ["spcpt_vM8dxJfRb45N35rV"]
spec_point_codes: []
guided_study: false
---

# Solving the Travelling Salesman Problem

## Solving the Travelling Salesman Problem

> **Spec point** — `spcpt_vM8dxJfRb45N35rV`

## Solving the Travelling Salesman Problem

### How do I solve the travelling salesman problem?

- List **all** of the possible **Hamiltonian cycles** and find the cycle of **least weight**

  - A complete graph with 3 vertices will have 2 possible Hamiltonian cycles
  - A complete graph with 4 vertices will have 6 possible Hamiltonian cycles
  - A complete graph with 5 vertices will have 24 possible Hamiltonian cycles
  
    - Although each of these values can be halved as each route will be the reverse of another route, e.g. DCBA is the reverse of the route ABCD
- There is **no known algorithm** guaranteed to find the shortest Hamiltonian cycle in a graph

  - This method is therefore only suitable for **small graphs**
- A Hamiltonian cycle will only be the optimal solution if the graph is a **complete** graph

  - So this solution method is only suitable for complete graphs
- If you find a route where the **weight **is **equal **to the **lower bound** then this route is **optimal**

> **Exam Hint**
> - You need to remember the difference between the** travelling salesman problem** and the **Chinese postman problem**
> 
>   - The salesman is interested in selling at each destination (vertex)
>   - The postman wants to walk along every road (edge) in order to deliver the letters

> **Worked Example**
> The network below contains six vertices representing villages and the edges (roads) that connect them. The weighting of the edges represents the time, in minutes, that it takes to walk along a particular road between two villages.
> 
> The dashed lines indicate the edges that are to be repeated to convert the network into a complete network.
> 
> ![complete-network](assets/b6b2a70b8711-complete-network.png)
> 
> The lower bound for the time taken to walk a route that visits every vertex and returns to the start vertex is 53 minutes.
> 
> Starting from vertex A, find a route that shows that this is an optimal solution.
> 
> **Answer:**
> 
> > *Because the network has 6 vertices there will be 120 possible different Hamiltonian cycles*
> *This is too many to check!*
> 
> > *You are told to start at vertex A and you are told to confirm that the route you have found is the optimal solution*
> *This means that it should have the same weight as the lower bound for the problem*
> *(An optimal solution can't be less than the lower bound, so if you find a solution that is equal to the lower bound it must be optimal)*
> 
> > *Find a Hamiltonian cycle starting at vertex A*
> 
> *AB (14)*
> *BF (9)*
> *EF (8)*
> *CE (6)*
> *CD (5)*
> *AD (11)*
> 
> > *Calculate the total weight of the cycle*
> 
> *14 + 9 + 8 + 6 + 5 + 11 = 53*
> 
> **Final answer:** **The route ABFECDA has the same weight (53 minutes) as the lower bound of the problem,**
> **therefore it is an optimal solution**
