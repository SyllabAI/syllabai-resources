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

  - `A equals open parentheses table row 1 row 0 end table close parentheses` and `C equals open parentheses table row 0 row 1 end table close parentheses`
- Under a **rotation about the origin**, *A* moves to *A*' and *C* moves to *C*'

  - The **matrix, M** representing this rotation is `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses`
  - *A*' and *C*' are **column vectors** of the new positions
  
    - So $M$ is a 2×2 matrix
  - The points *O* and *B* are not needed, as we can draw the rotated square using just *A*' and *C*' (as *O* won't move)
- For example:

  - To find the matrix representing a rotation of 90° anticlockwise about the origin
  
    - A goes to `A apostrophe equals open parentheses table row 0 row 1 end table close parentheses` (on the positive *y*-axis)
    - *C* goes to `C apostrophe equals open parentheses table row cell negative 1 end cell row 0 end table close parentheses` (on the negative *x*-axis)
    - `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses equals open parentheses table row 0 cell negative 1 end cell row 1 0 end table close parentheses`
  - To find the matrix representing a rotation of 180° about the origin
  
    - A goes to `A apostrophe equals open parentheses table row cell negative 1 end cell row 0 end table close parentheses` (on the negative *x*-axis)
    - *C* goes to `C apostrophe equals open parentheses table row 0 row cell negative 1 end cell end table close parentheses` (on the negative *y*-axis)
    - `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses equals open parentheses table row cell negative 1 end cell 0 row 0 cell negative 1 end cell end table close parentheses`
    
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
> *The point A *`open parentheses table row 1 row 0 end table close parentheses`* moves to A' *`open parentheses table row 0 row cell negative 1 end cell end table close parentheses`
> 
> *The point C *`open parentheses table row 0 row 1 end table close parentheses`* moves to C' *`open parentheses table row 1 row 0 end table close parentheses`
> 
> > *The transformation matrix is given by *`bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses`
> 
> `straight M equals stretchy left parenthesis table row 0 1 row cell negative 1 end cell 0 end table stretchy right parenthesis`
