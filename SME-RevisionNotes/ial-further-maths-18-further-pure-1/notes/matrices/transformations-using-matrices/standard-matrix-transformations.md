---
note_id: "rn_8krmy8tRfYbXRGNM"
title: "Standard Matrix Transformations"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/matrices/transformations-using-matrices/standard-matrix-transformations
path: matrices/transformations-using-matrices/standard-matrix-transformations
updated_at: "2024-04-10T13:26:25.736Z"
spec_point_ids: ["spcpt_fk4V4Cvw8BX5hfwZ", "spcpt_DdchQvsnwcKxhX8Q", "spcpt_yzsdTrmn8KXkYjYM"]
spec_point_codes: []
guided_study: false
---

# Standard Matrix Transformations

## Reflection Matrices

> **Spec point** — `spcpt_fk4V4Cvw8BX5hfwZ`

## Reflection Matrices

### How do I find reflection matrices?

- Imagine the** unit** square *OABC*

  - It has a side-length **1 unit**
  - *O * is the origin

![The unit square](../../../assets/396bfef694c0-unit-square.png)

- The **coordinates** of ***A ***** and *****C***  as **column vectors** are

  - `A equals open parentheses table row 1 row 0 end table close parentheses` and `C equals open parentheses table row 0 row 1 end table close parentheses`
- Under a **reflection **about an** axis or **$y=\pmx$, *A * moves to *A*'  and *C*  moves to *C*'

  - The **matrix, **$M$ representing this reflection is `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses`
  - ***A*****' ** **and** ***C*****'**  are column vectors of their **new positions**
  
    - The points ***O**** * **and** ***B***  are **not needed**, as we can draw the reflected square using just *A*'  and *C*'  (*O*  won't move)
- For example:

  - To find the matrix representing a **reflection about the **$x$**-axis**
  
    - *A * stays where it is, so `A apostrophe equals open parentheses table row 1 row 0 end table close parentheses`
    - *C*  goes to `C apostrophe equals open parentheses table row 0 row cell negative 1 end cell end table close parentheses` (on the negative $y$-axis)
    - `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses equals open parentheses table row 1 0 row 0 cell negative 1 end cell end table close parentheses`
  - To find the matrix representing a **reflection in the line **$y=x$
  
    - *A*  goes to `A apostrophe equals open parentheses table row 0 row 1 end table close parentheses` (on the positive *y*-axis)
    - *C * goes to `C apostrophe equals open parentheses table row 1 row 0 end table close parentheses` (on the positive *x*-axis)
    - `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses equals open parentheses table row 0 1 row 1 0 end table close parentheses`
    - (This is not the same as the identity matrix, as the 1s are on the wrong diagonal)

> **Worked Example**
> (a)  The matrix $M$ represents a reflection in the *y*-axis.
> 
> Work out $M$.
> 
> > *Consider how the points **A**  and **C**   on the unit square are transformed by a reflection in the *$y$*-axis*
> 
> ![TuW80_W4_reflection-matrix-we-1](assets/496add2d026c-tuw80-w4-reflection-matrix-we-1.png)
> 
> *The point ***A *** *`open parentheses table row 1 row 0 end table close parentheses`* moves to ***A'***  *`open parentheses table row cell negative 1 end cell row 0 end table close parentheses`* *
> 
> *The point ***C *** *`open parentheses table row 0 row 1 end table close parentheses`* remains in the same place*
> 
> > *The transformation matrix is given by *`bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses`* *
> 
> `bold M equals stretchy left parenthesis table row cell negative 1 end cell 0 row 0 1 end table stretchy right parenthesis`
> 
> (b)  Describe fully the transformation represented by the matrix `bold N equals open parentheses table row 0 cell negative 1 end cell row cell negative 1 end cell 0 end table close parentheses`.
> 
> > *Consider how the points **A**  and **C**  on the unit square are transformed *
> 
> *The point ***A *** *`open parentheses table row 1 row 0 end table close parentheses`* moves to ***A' **`open parentheses table row 0 row cell negative 1 end cell end table close parentheses`* *
> 
> *The point ***C *** *`open parentheses table row 0 row 1 end table close parentheses`* moves to ***C'***  *`open parentheses table row cell negative 1 end cell row 0 end table close parentheses`
> 
> > *It helps to draw a picture of the unit square being transformed with vertices clearly labelled*
> 
> ![reflection-matrix-we-2](assets/bce90e3b034a-reflection-matrix-we-2.png)
> 
> > *This transformation could be a rotation of 180**°** about **O** or a reflection in *$y=-x$* *
> *The vertices **A'**  and **C'**  are in the correct places for a reflection, but not a rotation*
> 
> **Final answer:** **The matrix N represents a reflection in the line **$y=-x$

## Enlargement & Stretch Matrices

> **Spec point** — `spcpt_DdchQvsnwcKxhX8Q`

## Enlargement & Stretch Matrices

### Which matrix represents an enlargement?

- The matrix  `bold M equals open parentheses table row k 0 row 0 k end table close parentheses` represents an** enlargement** of **scale factor **$k$**  **about the **origin, *****O***

  - This is the same as $M=kI$
  
    - $I$ is the identity matrix

### Which matrix represents a stretch?

- The matrix  `bold M equals open parentheses table row a 0 row 0 1 end table close parentheses` represents a** stretch parallel **to the** **$x$**-axis **of **scale factor **$a$** **

  - The point `open parentheses x comma space y close parentheses` becomes `open parentheses a x comma space y close parentheses`

- The matrix  `bold M equals open parentheses table row 1 0 row 0 b end table close parentheses` represents a** stretch parallel **to the** **$y$**-axis **of **scale factor **$b$** **

  - The point `open parentheses x comma space y close parentheses` becomes `open parentheses x comma space b y close parentheses`
- The matrix  `bold M equals open parentheses table row a 0 row 0 b end table close parentheses` represents a **combined stretch **of **scale factor **$a$  **parallel **to the $x$**-axis** and **scale factor **$b$**  parallel **to the $y$**-axis**

  - If $a=b$, the combined stretch is an **enlargement**

> **Exam Hint**
> Use phrases like "parallel to the $x$-axis"  or "parallel to the $y$-axis" to describe stretches (not "left" or "up"!)

> **Worked Example**
> A transformation is represented by the matrix `bold M equals open parentheses table row cell 3 plus p end cell 0 row 0 cell 3 minus p end cell end table close parentheses`.
> 
> Describe fully the transformation in each of the following cases:
> 
> (a)  $p=0$
> 
> > *Substitute in *$p=0$
> 
> `bold M equals open parentheses table row cell 3 plus 0 end cell 0 row 0 cell 3 minus 0 end cell end table close parentheses equals open parentheses table row 3 0 row 0 3 end table close parentheses`
> 
> > *This has the form *`bold M equals open parentheses table row k 0 row 0 k end table close parentheses`* where *$k=3$
> 
> **Final answer:** $M$** represents an enlargement of scale factor 3 about the origin**
> 
> **You must give its scale factor and centre of enlargement**
> 
> (b)  $p=2$
> 
> > *Substitute in *$p=2$
> 
> `bold M equals open parentheses table row cell 3 plus 2 end cell 0 row 0 cell 3 minus 2 end cell end table close parentheses equals open parentheses table row 5 0 row 0 1 end table close parentheses`
> 
> > *This has the form *`bold M equals open parentheses table row a 0 row 0 1 end table close parentheses`* where *$a=5$
> 
> **Final answer:** $M$** represents a stretch of scale factor 5 parallel to the **$x$**-axis**
> 
> **You must give its scale factor and direction**

## Rotation Matrices

> **Spec point** — `spcpt_yzsdTrmn8KXkYjYM`

## Rotation Matrices

### How do I find matrices for rotations by multiples of 90°?

- Imagine the** unit** square *OABC*

  - It has a side-length of** 1 unit**
  - *O* is the origin

![unit-square](../../../assets/396bfef694c0-unit-square.png)

- The **coordinates** of *A* and *C* as **column vectors** are

  - `A equals open parentheses table row 1 row 0 end table close parentheses` and `C equals open parentheses table row 0 row 1 end table close parentheses`
- Under a **rotation about the origin**, *A * moves to *A*'  and *C*  moves to *C*'

  - The **matrix, **$M$ representing this rotation is `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses`
  - *A*'  and *C*'  are **column vectors** of their new positions
  
    - The points *O * and *B*  are not needed, as we can draw the rotated square using just *A*'  and *C*'  (*O   *won't move)
- For example:

  - To find the matrix representing a **rotation of 90° anticlockwise** about the origin
  
    - *A*  goes to `A apostrophe equals open parentheses table row 0 row 1 end table close parentheses` (on the positive* *$y$-axis)
    - *C*  goes to `C apostrophe equals open parentheses table row cell negative 1 end cell row 0 end table close parentheses` (on the negative $x$-axis)
    - `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses equals open parentheses table row 0 cell negative 1 end cell row 1 0 end table close parentheses`
  - To find the matrix representing a **rotation of 180° **about the origin
  
    - *A*  goes to `A apostrophe equals open parentheses table row cell negative 1 end cell row 0 end table close parentheses` (on the negative $x$-axis)
    - *C * goes to `C apostrophe equals open parentheses table row 0 row cell negative 1 end cell end table close parentheses` (on the negative $y$-axis)
    - `bold M equals open parentheses table row cell A apostrophe space vertical line end cell cell C apostrophe end cell end table close parentheses equals open parentheses table row cell negative 1 end cell 0 row 0 cell negative 1 end cell end table close parentheses`
    - This is the same as $M=-I$ where* *$I$ is the identity matrix

> **Exam Hint**
> Students often confuse rotations of 180° with reflections in the lines $y=\pmx$ .

### How do I find matrices for rotations by any angle?

- A **rotation anticlockwise **by any **angle**, $θ$, about the** origin** is represented by the matrix:

  - `bold M equals open parentheses table row cell cos space theta end cell cell negative sin space theta end cell row cell sin space theta end cell cell cos space theta end cell end table close parentheses`
  
    - $θ$ can be in degrees or **radians**
- A **negative** value of $θ$ represents a **clockwise **rotation

  - Remember that  `sin open parentheses negative theta close parentheses equals negative sin space theta` but that `cos open parentheses negative theta close parentheses equals cos space theta`
- You can **substitute** in multiples of 90° to get the matrices above
- You may be required to recognise **common angles** from their ratios

  - For example, `fraction numerator square root of 3 over denominator 2 end fraction equals cos open parentheses straight pi over 6 close parentheses`

> **Exam Hint**
> You are given the rotation matrix in the Formulae Booklet.

> **Worked Example**
> (a)  Describe fully the transformation represented by the matrix `bold P equals open parentheses table row 0 1 row cell negative 1 end cell 0 end table close parentheses`.
> 
> > *Consider how the points **A**  and **C**  on the unit square are transformed *
> 
> *The point ***A *** *`open parentheses table row 1 row 0 end table close parentheses`* moves to ***A' **`open parentheses table row 0 row cell negative 1 end cell end table close parentheses`* *
> 
> *The point ***C *** *`open parentheses table row 0 row 1 end table close parentheses`* moves to ***C'***  *`open parentheses table row 1 row 0 end table close parentheses`
> 
> > *It helps to draw a picture of the unit square being transformed with vertices clearly labelled*
> 
> ![A rotation of 90 degrees anticlockwise](assets/830fb34638c3-transforming-a-point-we.png)
> 
> > *This transformation could be a rotation of 90**° clockwise** about **O ** or a reflection in the *$x$*-axis*
> *The vertices **A'**  and **C'**  are not in the correct places for a reflection, but are for a rotation*
> 
> **The matrix P represents a rotation of 90***°*** clockwise about the origin**
> 
> **You must give its angle, direction and centre of rotation**
> **270***°*** anticlockwise would also be accepted**
> 
> (b)  Find $Q$, the matrix that represents a clockwise rotation of 120°  about the origin, giving your answer in an exact form.
> 
> > *The matrix for an anticlockwise rotation by *$θ$* is*`open parentheses table row cell cos space theta end cell cell negative sin space theta end cell row cell sin space theta end cell cell cos space theta end cell end table close parentheses`
> $θ$* is negative, as the rotation is clockwise*
> 
> $θ=-120^{\circ}$
> 
> > *Substitute this value of *$θ$* into the matrix*
> *Use that *`cos open parentheses negative theta close parentheses equals cos space theta`* and that *`sin open parentheses negative theta close parentheses equals negative sin space theta`
> 
> `open parentheses table row cell cos open parentheses negative 120 degree close parentheses end cell cell negative sin open parentheses negative 120 degree close parentheses end cell row cell sin open parentheses negative 120 degree close parentheses end cell cell cos open parentheses negative 120 degree close parentheses end cell end table close parentheses equals open parentheses table row cell cos open parentheses 120 degree close parentheses end cell cell sin open parentheses 120 degree close parentheses end cell row cell negative sin open parentheses 120 degree close parentheses end cell cell cos open parentheses 120 degree close parentheses end cell end table close parentheses`
> 
> > *Use a calculator to find these values (or common angles and symmetry)*
> 
> `bold Q equals stretchy left parenthesis table row cell negative 1 half end cell cell fraction numerator square root of 3 over denominator 2 end fraction end cell row cell negative fraction numerator square root of 3 over denominator 2 end fraction end cell cell negative 1 half end cell end table stretchy right parenthesis`
