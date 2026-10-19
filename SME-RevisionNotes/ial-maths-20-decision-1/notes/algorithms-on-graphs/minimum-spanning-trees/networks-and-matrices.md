---
note_id: "rn_wk2WMXjHqTdBFXRf"
title: "Networks & Matrices"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/algorithms-on-graphs/minimum-spanning-trees/networks-and-matrices
path: algorithms-on-graphs/minimum-spanning-trees/networks-and-matrices
updated_at: "2026-07-02T08:19:38.617Z"
spec_point_ids: ["spcpt_mpPyxNyDHWtynYG8", "spcpt_c4x6xkBRwStbd9wY"]
spec_point_codes: []
guided_study: false
---

# Networks & Matrices

## Introduction to Networks & Matrices

> **Spec point** — `spcpt_mpPyxNyDHWtynYG8`

## Introduction to Networks & Matrices

### What is a network?

- A **network** is a **weighted graph**

  - A **network** is used to model real-world situations
  - The **weight** of an edge usually represents a **measure** such as **distance** or **time**

### What is a matrix?

- A **matrix** can be used to **represent a graph **or **network **in the form of a **table**

  - The** elements** within the matrix give information about the **connections** between the **different vertices**
- A matrix is typically set up with the following** labelling system**

  - **Rows **are labelled with the** 'from' **vertices
  - **Columns **are labelled with the** 'to' **vertices

## Networks & Matrices

> **Spec point** — `spcpt_c4x6xkBRwStbd9wY`

## Networks & Matrices

### What is an adjacency matrix?

- An **adjacency matrix** is a **square** matrix

  - All of the **vertices** in the graph are listed as the** headings** for both the **rows and columns**
  - The** leading diagonal** is the the line going from the top left cell to the bottom right cell
- An adjacency matrix can be used to show the **number of direct connections** between two vertices
- An entry of **1** in the matrix means that there is a **direct connection** (i.e. an edge) between that pair of vertices
- An entry of **0** in the matrix means that there is **no direct connection** between that pair of vertices
- In a **simple** graph the only entries are 0 or 1
- A **loop** is indicated in an adjacency matrix with a value in the **leading diagonal**

  - In an **undirected matrix** the value in the leading diagonal will be **2**
  
    - You can use the loop to travel out of and into the vertex in two different directions
  - In a **directed matrix**, if the loop has direction, the value in the leading diagonal will be **1**
  
    - You can only travel along the loop out of and back into the vertex in one direction
    - An undirected loop in a directed matrix will still have a value of 2
  - For a graph with **no loops** every entry in the leading diagonal will be **0**
- An **undirected graph** is **symmetrical** about the **leading diagonal**

  - A **directed graph** is **not** **symmetrical** about the **leading diagonal**

### What is a distance matrix?

- A **distance matrix** is different to an adjacency matrix

  - The **value** in each cell is the **weight** of the edge connecting that pair of vertices
  - Weight could be cost, distance, time etc.
- An **empty cell** is used to indicate that there is **no connection** (i.e. no edge) between a pair of vertices
- An **undirected network** is **symmetrical** about the **leading diagonal**

  - A **directed network** is **not** **symmetrical** about the **leading diagonal**
- When drawing a network from its distance matrix be careful when **labelling the edges**

  - For an **undirected graph** the two cells between a pair of vertices will be the same
  
    - Connect the vertices with **one edge** labelled with the relevant weight
  - For a **directed graph** where two cells between a pair of vertices have different values
  
    - Draw **two edges** between the vertices
    - Label each with the correct weight and direction
- A distance matrix can be used to work out the weight of different **walks** in the network

> **Worked Example**
> a) Write down the adjacency matrix for the graph shown below.
> 
> ![3-10-2-ib-hl-ai-walks--adjacency-matrices-we-1](assets/113a1d9b15bb-3-10-2-ib-hl-ai-walks-adjacency-matrices-we-1.png)
> 
> **Answer:**
> 
> `table row blank cell table row bold A bold B bold C bold D bold E end table end cell row cell table row bold A row bold B row bold C row bold D row bold E end table end cell cell stretchy left parenthesis table row 0 1 1 0 1 row 1 0 0 0 0 row 1 0 1 1 1 row 0 0 0 0 1 row 2 1 1 1 2 end table stretchy right parenthesis end cell end table`
> 
> b) The table below shows the time taken in minutes to travel by car between 4 different towns.
> 
> |   | A | B | C | D |
> |---|---|---|---|---|
> | A |   | 16 | 35 |   |
> | B | 16 |   | 20 | 18 |
> | C | 35 | 20 |   | 34 |
> | D |   | 23 | 34 |   |
> 
> Draw the network described by this distance matrix.
> 
> **Answer:**
> 
> ![qoHMRvSL_picture-1](assets/7e5d6e4c513d-qohmrvsl-picture-1.png)
