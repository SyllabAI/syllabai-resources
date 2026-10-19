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

  - `A equals open parentheses table row 1 row 0 end table close parentheses` and `C equals open parentheses table row 0 row 1 end table close parentheses`
- Under a **reflection about an axis (or *****y***** = ± *****x*****)**, *A* moves to *A*' and *C* moves to *C*'

  - The **matrix, M** representing this reflection is `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses`
  - *A*' and *C*' are column vectors of the new positions
  
    - So $M$ is a 2×2 matrix
  - The points *O* and *B* are not needed, as we can draw the reflected square using just *A*' and *C*' (as *O* won't move)
- For example:

  - To find the matrix representing a reflection about the *x*-axis
  
    - *A* stays where it is, so `A apostrophe equals open parentheses table row 1 row 0 end table close parentheses`
    - *C* goes to `C apostrophe equals open parentheses table row 0 row cell negative 1 end cell end table close parentheses` (on the negative *y*-axis)
    - `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses equals open parentheses table row 1 0 row 0 cell negative 1 end cell end table close parentheses`
  - To find the matrix representing a reflection in the line *y* = *x*
  
    - A goes to `A apostrophe equals open parentheses table row 0 row 1 end table close parentheses` (on the positive *y*-axis)
    - *C* goes to `C apostrophe equals open parentheses table row 1 row 0 end table close parentheses` (on the positive *x*-axis)
    - `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses equals open parentheses table row 0 1 row 1 0 end table close parentheses`
    
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
> *The point A *`open parentheses table row 1 row 0 end table close parentheses`* moves to A' *`open parentheses table row cell negative 1 end cell row 0 end table close parentheses`* *
> 
> *The point C *`open parentheses table row 0 row 1 end table close parentheses`* remains in the same place*
> 
> > *The transformation matrix is given by *`bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses`* *
> 
> **Final answer:** `straight M equals stretchy left parenthesis table row cell negative 1 end cell 0 row 0 1 end table stretchy right parenthesis`
> ** **
> 
> (b) The matrix **N** represents a reflection in the line $y=-x$. Work out **N**.
> 
> **Answer:**
> 
> > *Consider how the points A and C on the unit square are transformed by a reflection in the line *$y=-x$
> 
> ![reflection-matrix-we-2](assets/bce90e3b034a-reflection-matrix-we-2.png)
> 
> *The point A *`open parentheses table row 1 row 0 end table close parentheses`* moves to A' *`open parentheses table row 0 row cell negative 1 end cell end table close parentheses`* *
> 
> *The point C *`open parentheses table row 0 row 1 end table close parentheses`* moves to C' *`open parentheses table row cell negative 1 end cell row 0 end table close parentheses`
> 
> > *The transformation matrix is given by *`bold N equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses`* *
> 
> `straight N equals stretchy left parenthesis table row 0 cell negative 1 end cell row cell negative 1 end cell 0 end table stretchy right parenthesis`
