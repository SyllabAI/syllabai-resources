---
note_id: "rn_W9R2RtZ6wSz7zs99"
title: "Combining Matrix Transformations"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/transformations-using-matrices/combining-matrix-transformations
path: matrices/transformations-using-matrices/combining-matrix-transformations
updated_at: "2026-01-14T14:36:08.992Z"
spec_point_ids: ["spcpt_5snY7JPdgrqvFRhY"]
spec_point_codes: []
guided_study: false
---

# Combining Matrix Transformations

## Combining Transformation Matrices

> **Spec point** — `spcpt_5snY7JPdgrqvFRhY`

## Combining transformation matrices

### How do I find a single matrix that represents a combination of transformations?

- A point (*x*,* y*) can be transformed **twice**

  - **First** by the matrix $P$, then** second** by the matrix $Q$
  - This is called a **combined** (or **composite**) transformation
- A** single **matrix, $M$, representing the combined transformation can be found using **matrix multiplication** as follows:

  - $M=\mathrm{QP}$
  
    - The **order** matters: the **first** transformation is the **last** in the multiplication
    - The order is the **reverse** of what you may expect!
    
      - The first transformation is on the right, with the second transformation to its left
  - $\mathrm{PQ}$ would represent** **$Q$ first, followed by $P$

> **Exam Hint**
> If a question asks you to prove a geometric fact about combined transformations "using matrix multiplication", you cannot just draw a sequence of diagrams for your answer
> 
> - You should write each transformation as a matrix
> - and combine them using **QP** or **PQ** (depending on the order)

> **Worked Example**
> Three transformations in the $x$-$y$ plane are given below.
> 
> `bold A equals open parentheses table row cell negative 1 end cell 0 row 0 cell negative 1 end cell end table close parentheses`**  **represents an enlargement by scale factor -1 about the origin
> `bold B equals open parentheses table row cell negative 1 end cell 0 row 0 1 end table close parentheses`** **represents a reflection in the *y*-axis
> `bold C equals open parentheses table row 1 0 row 0 cell negative 1 end cell end table close parentheses`** **represents a reflection in the *x*-axis
> 
> Use matrix multiplication to prove that **A** is the same as **B** followed by **C**.
> 
> **Answer:**
> 
> > *Transformation *$B$* followed by transformation *$C$* would be combined into a single matrix by finding *$\mathrm{CB}$* (note the order)*
> 
> > *Find the matrix multiplication *$\mathrm{CB}$
> 
> `table row cell bold CB space end cell equals cell space open parentheses table row 1 0 row 0 cell negative 1 end cell end table close parentheses cross times open parentheses table row cell negative 1 end cell 0 row 0 1 end table close parentheses end cell row blank equals cell open parentheses table row cell 1 cross times open parentheses negative 1 close parentheses plus 0 cross times 0 end cell cell 1 cross times 0 plus 0 cross times 1 end cell row cell 0 cross times open parentheses negative 1 close parentheses plus open parentheses negative 1 close parentheses cross times 0 end cell cell 0 cross times 0 plus open parentheses negative 1 close parentheses cross times 1 end cell end table close parentheses end cell row blank equals cell open parentheses table row cell negative 1 plus 0 end cell cell 0 plus 0 end cell row cell 0 plus 0 end cell cell 0 minus 1 end cell end table close parentheses end cell row blank equals cell open parentheses table row cell negative 1 end cell 0 row 0 cell negative 1 end cell end table close parentheses end cell end table`
> 
> > *This is the same as *$A$
> 
> - *This makes sense geometrically as well*
> 
>   - *A reflection in the** y**-axis followed by a reflection in the **x**-axis *
>   - *is equivalent to an enlargement of scale factor -1 (which is the same as a rotation of 180° about the origin)*
> 
> `CB equals stretchy left parenthesis table row cell negative 1 end cell 0 row 0 cell negative 1 end cell end table stretchy right parenthesis equals straight A`
