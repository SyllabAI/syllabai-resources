---
note_id: "rn_RWQCs9fkcfGVjVhY"
title: "Reflection Matrices"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/transformations-using-matrices/reflection-matrices
path: matrices/transformations-using-matrices/reflection-matrices
updated_at: "2026-01-14T14:13:53.724Z"
spec_point_ids: ["spcpt_GG7jc43bG3xTkft4"]
spec_point_codes: []
guided_study: false
---

# Reflection Matrices

## Reflection matrices

> **Spec point** — `spcpt_GG7jc43bG3xTkft4`

## Reflection matrices

### How do I find reflection matrices?

- Imagine the** unit** square *OABC*

  - It has a side-length 1 unit
  - *O* is the origin

![unit-square](../../../assets/396bfef694c0-unit-square.png)

- The **coordinates** of *A* and *C* as **column vectors** are

  - $A = ( \begin{gathered} 1 \\ 0 \end{gathered} )$ and $C = ( \begin{gathered} 0 \\ 1 \end{gathered} )$
- Under a **reflection about an axis (or *****y***** = ± *****x*****)**, *A* moves to *A*' and *C* moves to *C*'

  - The **matrix, M** representing this reflection is $M = ( \begin{gathered} A ' \vert & C ' \end{gathered} )$
  - *A*' and *C*' are column vectors of the new positions
  
    - So $M$ is a 2×2 matrix
  - The points *O* and *B* are not needed, as we can draw the reflected square using just *A*' and *C*' (as *O* won't move)
- For example:

  - To find the matrix representing a reflection about the *x*-axis
  
    - *A* stays where it is, so $A ' = ( \begin{gathered} 1 \\ 0 \end{gathered} )$
    - *C* goes to $C ' = ( \begin{gathered} 0 \\ - 1 \end{gathered} )$ (on the negative *y*-axis)
    - $M = ( \begin{gathered} A ' \vert & C ' \end{gathered} ) = ( \begin{gathered} 1 0 \\ 0 - 1 \end{gathered} )$
  - To find the matrix representing a reflection in the line *y* = *x*
  
    - A goes to $A ' = ( \begin{gathered} 0 \\ 1 \end{gathered} )$ (on the positive *y*-axis)
    - *C* goes to $C ' = ( \begin{gathered} 1 \\ 0 \end{gathered} )$ (on the positive *x*-axis)
    - $M = ( \begin{gathered} A ' \vert & C ' \end{gathered} ) = ( \begin{gathered} 0 1 \\ 1 0 \end{gathered} )$
    
      - This is not the same as the identity matrix as the 1s are on the wrong diagonal

> **Worked Example**
> (a)  The matrix **M** represents a reflection in the *y*-axis. Work out **M**.
> 
> **Answer:**
> 
> > *Consider how the points A and C on the unit square are transformed by a reflection in the **y**-axis*
> 
> ![TuW80_W4_reflection-matrix-we-1](assets/496add2d026c-tuw80-w4-reflection-matrix-we-1.png)
> 
> *The point A* $( \begin{gathered} 1 \\ 0 \end{gathered} )$ *moves to A'* $( \begin{gathered} - 1 \\ 0 \end{gathered} )$* *
> 
> *The point C* $( \begin{gathered} 0 \\ 1 \end{gathered} )$ *remains in the same place*
> 
> > *The transformation matrix is given by* $M = ( \begin{gathered} A ' \vert & C ' \end{gathered} )$* *
> 
> **Final answer:** $\mathrm{M} = ( \begin{gathered} - 1 & 0 \\ 0 1 \end{gathered} )$
> ** **
> 
> (b) The matrix **N** represents a reflection in the line $y=-x$. Work out **N**.
> 
> **Answer:**
> 
> > *Consider how the points A and C on the unit square are transformed by a reflection in the line* $y=-x$
> 
> ![reflection-matrix-we-2](assets/bce90e3b034a-reflection-matrix-we-2.png)
> 
> *The point A* $( \begin{gathered} 1 \\ 0 \end{gathered} )$ *moves to A'* $( \begin{gathered} 0 \\ - 1 \end{gathered} )$* *
> 
> *The point C* $( \begin{gathered} 0 \\ 1 \end{gathered} )$ *moves to C'* $( \begin{gathered} - 1 \\ 0 \end{gathered} )$
> 
> > *The transformation matrix is given by* $N = ( \begin{gathered} A ' \vert & C ' \end{gathered} )$* *
> 
> $\mathrm{N} = ( \begin{gathered} 0 - 1 \\ - 1 & 0 \end{gathered} )$
