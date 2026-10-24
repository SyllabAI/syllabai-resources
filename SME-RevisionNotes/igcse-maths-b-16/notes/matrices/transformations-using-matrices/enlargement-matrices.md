---
note_id: "rn_VxT5D9w6CFghjsQV"
title: "Enlargement Matrices"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/transformations-using-matrices/enlargement-matrices
path: matrices/transformations-using-matrices/enlargement-matrices
updated_at: "2026-01-14T14:22:11.830Z"
spec_point_ids: ["spcpt_H5Sb2tfDwbqy6x2t"]
spec_point_codes: []
guided_study: false
---

# Enlargement Matrices

## Enlargement matrices

> **Spec point** — `spcpt_H5Sb2tfDwbqy6x2t`

## Enlargement matrices

### How do I find enlargement matrices?

- Imagine the** unit** square *OABC*

  - It has a side-length of 1 unit
  - *O* is the origin

![unit-square](../../../assets/396bfef694c0-unit-square.png)

- The **coordinates** of *A* and *C* as **column vectors** are

  - $A = ( \begin{gathered} 1 \\ 0 \end{gathered} )$ and $C = ( \begin{gathered} 0 \\ 1 \end{gathered} )$
- Under an **enlargement of scale factor *****k***** with centre at the origin **(including negative scale factors), *A* moves to *A*' and *C* moves to *C*'

  - The **matrix, M** representing this enlargement is $M = ( \begin{gathered} A ' \vert & C ' \end{gathered} )$
  - *A*' and *C*' are column vectors of the new positions
  
    - So $M$ is a 2×2 matrix
  - The points *O* and *B* are not needed, as we can draw the enlarged square using just *A*' and *C*' (as *O* won't move)
- $A ' = ( \begin{gathered} k \\ 0 \end{gathered} )$ and $C ' = ( \begin{gathered} 0 \\ k \end{gathered} )$

  - They are both just moving along the *x* and *y* axes respectively
- So all enlargement matrices have the form $M = ( \begin{gathered} k 0 \\ 0 k \end{gathered} )$

  - This is the same as $M=kI$, where** **$I$ is the identity matrix
- For example:

  - The matrix representation of an enlargement of scale factor 3 with centre at the origin is $( \begin{gathered} 3 0 \\ 0 3 \end{gathered} )$
  - The matrix representation of an enlargement of scale factor $-\frac{1}{2}$ with centre at the origin is $( \begin{gathered} - 1 \frac{1}{2} & 0 \\ 0 - 1 \frac{1}{2} \end{gathered} )$

> **Worked Example**
> The matrix **M** representing a transformation is given by $( \begin{gathered} 1 \frac{1}{4} & 0 \\ 0 1 \frac{1}{4} \end{gathered} )$.
> 
> Describe geometrically the transformation represented by **M**.
> 
> **Answer:**
>   
> *The matrix *$M$* can be written as a multiple of the identity matrix, *$I$
> 
> $( \begin{gathered} 1 \frac{1}{4} & 0 \\ 0 1 \frac{1}{4} \end{gathered} ) = 1 \frac{1}{4} ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} )$
> 
> > *So the unit square is being scaled by *$\frac{1}{4}$
> 
> **Final answer:** **Enlargement by scale factor **$\frac{1}{4}$**with centre at the origin**
