---
note_id: "rn_3PRDhmmSPV7XgF7k"
title: "Rotation Matrices"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/transformations-using-matrices/rotation-matrices
path: matrices/transformations-using-matrices/rotation-matrices
updated_at: "2026-01-14T14:16:44.497Z"
spec_point_ids: ["spcpt_gkqmXrkrWnQC27tP"]
spec_point_codes: []
guided_study: false
---

# Rotation Matrices

## Rotation matrices

> **Spec point** — `spcpt_gkqmXrkrWnQC27tP`

## Rotation matrices

### How do I find rotation matrices?

- Imagine the** unit** square *OABC*

  - It has a side-length of 1 unit
  - *O* is the origin

![unit-square](../../../assets/396bfef694c0-unit-square.png)

- The **coordinates** of *A* and *C* as **column vectors** are

  - $A = ( \begin{gathered} 1 \\ 0 \end{gathered} )$ and $C = ( \begin{gathered} 0 \\ 1 \end{gathered} )$
- Under a **rotation about the origin**, *A* moves to *A*' and *C* moves to *C*'

  - The **matrix, M** representing this rotation is $M = ( \begin{gathered} A ' \vert & C ' \end{gathered} )$
  - *A*' and *C*' are **column vectors** of the new positions
  
    - So $M$ is a 2×2 matrix
  - The points *O* and *B* are not needed, as we can draw the rotated square using just *A*' and *C*' (as *O* won't move)
- For example:

  - To find the matrix representing a rotation of 90° anticlockwise about the origin
  
    - A goes to $A ' = ( \begin{gathered} 0 \\ 1 \end{gathered} )$ (on the positive *y*-axis)
    - *C* goes to $C ' = ( \begin{gathered} - 1 \\ 0 \end{gathered} )$ (on the negative *x*-axis)
    - $M = ( \begin{gathered} A ' \vert & C ' \end{gathered} ) = ( \begin{gathered} 0 - 1 \\ 1 0 \end{gathered} )$
  - To find the matrix representing a rotation of 180° about the origin
  
    - A goes to $A ' = ( \begin{gathered} - 1 \\ 0 \end{gathered} )$ (on the negative *x*-axis)
    - *C* goes to $C ' = ( \begin{gathered} 0 \\ - 1 \end{gathered} )$ (on the negative *y*-axis)
    - $M = ( \begin{gathered} A ' \vert & C ' \end{gathered} ) = ( \begin{gathered} - 1 & 0 \\ 0 - 1 \end{gathered} )$
    
      - This is the same as $M=-I$ where* *$I$ is the identity matrix

> **Worked Example**
> The matrix $M$ represents a rotation of 270° anticlockwise about the origin.
> 
> Work out $M$.
>  
> **Answer:**
> 
> > *A rotation of 270° anticlockwise is the same as a rotation of 90° clockwise*
> 
> > *Consider how the points A and C on the unit square are transformed*
> 
> ![transforming-a-point-we](assets/830fb34638c3-transforming-a-point-we.png)
> 
> *The point A *$( \begin{gathered} 1 \\ 0 \end{gathered} )$* moves to A' *$( \begin{gathered} 0 \\ - 1 \end{gathered} )$
> 
> *The point C *$( \begin{gathered} 0 \\ 1 \end{gathered} )$* moves to C' *$( \begin{gathered} 1 \\ 0 \end{gathered} )$
> 
> > *The transformation matrix is given by *$M = ( \begin{gathered} A ' \vert & C ' \end{gathered} )$
> 
> $\mathrm{M} = ( \begin{gathered} 0 1 \\ - 1 & 0 \end{gathered} )$
