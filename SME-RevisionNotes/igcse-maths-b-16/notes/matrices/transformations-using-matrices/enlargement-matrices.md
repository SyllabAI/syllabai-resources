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

  - `A equals open parentheses table row 1 row 0 end table close parentheses` and `C equals open parentheses table row 0 row 1 end table close parentheses`
- Under an **enlargement of scale factor *****k***** with centre at the origin **(including negative scale factors), *A* moves to *A*' and *C* moves to *C*'

  - The **matrix, M** representing this enlargement is `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses`
  - *A*' and *C*' are column vectors of the new positions
  
    - So $M$ is a 2×2 matrix
  - The points *O* and *B* are not needed, as we can draw the enlarged square using just *A*' and *C*' (as *O* won't move)
- `A apostrophe equals open parentheses table row k row 0 end table close parentheses` and `C apostrophe equals open parentheses table row 0 row k end table close parentheses`

  - They are both just moving along the *x* and *y* axes respectively
- So all enlargement matrices have the form `bold M equals open parentheses table row k 0 row 0 k end table close parentheses`

  - This is the same as $M=kI$, where** **$I$ is the identity matrix
- For example:

  - The matrix representation of an enlargement of scale factor 3 with centre at the origin is `open parentheses table row 3 0 row 0 3 end table close parentheses`
  - The matrix representation of an enlargement of scale factor $-\frac{1}{2}$ with centre at the origin is `open parentheses table row cell negative 1 half end cell 0 row 0 cell negative 1 half end cell end table close parentheses`

> **Worked Example**
> The matrix **M** representing a transformation is given by `open parentheses table row cell 1 fourth end cell 0 row 0 cell 1 fourth end cell end table close parentheses`.
> 
> Describe geometrically the transformation represented by **M**.
> 
> **Answer:**
>   
> *The matrix *$M$* can be written as a multiple of the identity matrix, *$I$
> 
> `open parentheses table row cell 1 fourth end cell 0 row 0 cell 1 fourth end cell end table close parentheses equals 1 fourth open parentheses table row 1 0 row 0 1 end table close parentheses`
> 
> > *So the unit square is being scaled by *$\frac{1}{4}$
> 
> **Final answer:** **Enlargement by scale factor **$\frac{1}{4}$**with centre at the origin**
