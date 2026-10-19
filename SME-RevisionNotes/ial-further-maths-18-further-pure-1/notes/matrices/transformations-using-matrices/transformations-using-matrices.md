---
note_id: "rn_SqCkPhNkGWS5Sf8n"
title: "Transformations using Matrices"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/matrices/transformations-using-matrices/transformations-using-matrices
path: matrices/transformations-using-matrices/transformations-using-matrices
updated_at: "2024-04-10T13:20:40.819Z"
spec_point_ids: ["spcpt_zNkvbSrS3xysKQyQ", "spcpt_jHbjfY6F8Vh77FP9"]
spec_point_codes: []
guided_study: false
---

# Transformations using Matrices

## Transforming Points using Matrices

> **Spec point** — `spcpt_zNkvbSrS3xysKQyQ`

## Transforming Points using Matrices

### How do I transform a point using a matrix?

- A point `open parentheses x comma space y close parentheses` in a 2D plane can be **transformed** (**mapped**) on to another point `open parentheses x apostrophe comma space y apostrophe close parentheses` by a 2 × 2 **matrix**, $M$

  - This is called a **linear transformation**
  
    - `open parentheses x comma space y close parentheses` is the **object **and `open parentheses x apostrophe comma space y apostrophe close parentheses` is the **image**
- The **coordinates** of the image point can be found using **matrix multiplication**
- To transform `open parentheses x comma space y close parentheses` by the matrix `open parentheses table row a b row c d end table close parentheses`

  - Write `open parentheses x comma space y close parentheses` as a **column vector,** `open parentheses table row x row y end table close parentheses`
  - Use **matrix multiplication **to work out `open parentheses table row a b row c d end table close parentheses open parentheses table row x row y end table close parentheses`, which gives `open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses`
  - **Write down** the image point **coordinates**, `open parentheses x apostrophe comma space y apostrophe close parentheses`
- If given image coordinates, `open parentheses x apostrophe comma space y apostrophe close parentheses`, and asked to find original coordinates

  - use **inverse** matrices
  - `bold M open parentheses table row x row y end table close parentheses equals open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses space space space rightwards double arrow space space space open parentheses table row x row y end table close parentheses equals bold M to the power of negative 1 end exponent open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses`

## How do I transform a set of vertices?

- **Vertices** of a **shape** can be transformed **one-by-one** using the method above

  - This gives the vertices of the **new** shape
  
    - **Straight lines** between the vertices will still be straight lines in the new shape
  - Sometimes the order (**clockwise** or **anticlockwise**) of the vertices is** reversed**
  
    - This is also called changing the **sense **of the vertices
- An** alternative method** is to stack **column vectors** of **coordinates** into a **vertex matrix**

  - `open parentheses 1 comma space 2 close parentheses`, `open parentheses 3 comma space 4 close parentheses`, `open parentheses 5 comma space 6 close parentheses` and `open parentheses 0 comma space 10 close parentheses` become `open parentheses table row 1 3 5 0 row 2 4 6 10 end table close parentheses`
  - Then **multiply **the **matrix** $M$ by the **vertex matrix** above
  - The **new** **columns** represent the corresponding **image** **coordinates**

> **Worked Example**
> The matrix $M$ is given by `bold M equals open parentheses table row 4 5 row 1 cell negative 2 end cell end table close parentheses`.
> A triangle has coordinates `open parentheses 1 comma space 0 close parentheses`, `open parentheses 2 comma space 3 close parentheses` and `open parentheses negative 1 comma space 5 close parentheses`.
> 
> Work out the coordinates of the triangle after the transformation represented by the matrix $M$ has been applied.
> 
> > *Multiply the matri**x *$M$* by each set **of coordinates, written as a column vectors*
> 
> `table row cell open parentheses table row 4 5 row 1 cell negative 2 end cell end table close parentheses open parentheses table row 1 row 0 end table close parentheses end cell equals cell open parentheses table row cell 4 cross times 1 space plus space 5 cross times 0 end cell row cell 1 cross times 1 space plus space minus 2 cross times 0 end cell end table close parentheses equals open parentheses table row 4 row 1 end table close parentheses end cell row cell open parentheses table row 4 5 row 1 cell negative 2 end cell end table close parentheses open parentheses table row 2 row 3 end table close parentheses end cell equals cell open parentheses table row cell 4 cross times 2 space plus space 5 cross times 3 end cell row cell 1 cross times 2 space plus space minus 2 cross times 3 end cell end table close parentheses equals open parentheses table row 23 row cell negative 4 end cell end table close parentheses end cell row cell open parentheses table row 4 5 row 1 cell negative 2 end cell end table close parentheses open parentheses table row cell negative 1 end cell row 5 end table close parentheses end cell equals cell open parentheses table row cell 4 cross times open parentheses negative 1 close parentheses space plus space 5 cross times 5 end cell row cell 1 cross times open parentheses negative 1 close parentheses space plus space minus 2 cross times 5 end cell end table close parentheses equals open parentheses table row 21 row cell negative 11 end cell end table close parentheses end cell end table`
> 
> > *Rewrite the answers as coordinates*
> 
> **Final answer:** `open parentheses 4 comma space 1 close parentheses`**, **`open parentheses 23 comma space minus 4 close parentheses`** and **`open parentheses 21 comma space minus 11 close parentheses`
> 
> ** Alternatively, you can multi****ply **$M$** by a vertex mat****rix: **`open parentheses table row 4 5 row 1 cell negative 2 end cell end table close parentheses open parentheses table row 1 2 cell negative 1 end cell row 0 3 5 end table close parentheses equals open parentheses table row 4 23 21 row 1 cell negative 4 end cell cell negative 11 end cell end table close parentheses`

## Determinants as Area Scale Factors

> **Spec point** — `spcpt_jHbjfY6F8Vh77FP9`

## Determinants as Area Scale Factors

### How are 2x2 determinants and areas related?

- When **transforming **vertices of an** object** using the **matrix **$M$** **to give vertices of the **image**

  - the** magnitude** of the **determinant **of $M$ is the **area scale factor** of **enlargement **from the** **object to the image
  - `vertical line det open parentheses bold M close parentheses vertical line`is the area scale factor
- For example, if a shape is transformed by `bold M equals open parentheses table row 1 3 row 2 4 end table close parentheses` then

  - `det open parentheses bold M close parentheses equals 1 cross times 4 minus 2 cross times 3 equals negative 2`
  - so`vertical line det open parentheses bold M close parentheses vertical line equals vertical line minus 2 vertical line equals 2`
  
    - This transformation** doubles** the area of any shape
- A **negative determinant** means the **sense** (**clockwise **or **anticlockwise**) of the vertices is **reversed**

> **Exam Hint**
> Remember the modulus signs around the determinant as this can often lead to two solutions in algebraic questions.

> **Worked Example**
> A transformation, represented  by the matrix `bold M equals open parentheses table row 3 2 row 4 cell space space space k plus 1 end cell end table close parentheses`, where $k$ is a constant, maps a quadrilateral of area 45 square units to a quadrilateral of area 450 square units.
> 
> Find the possible values of $k$.
> 
> > *Find the scale factor of enlargement of the area from 45 to 450*
> 
> > *Area scale factor is 10 *
> 
> > *The magnitude of the determinant is the area scale factor*
> *Start by finding and simplifying the determinant of *$M$
> 
> `table row cell det open parentheses bold M close parentheses end cell equals cell 3 open parentheses k plus 1 close parentheses minus 2 cross times 4 end cell row blank equals cell 3 k plus 3 minus 8 end cell row blank equals cell 3 k minus 5 end cell end table`
> 
> > *Set the magnitude of the determinant equal to 10*
> 
> `vertical line 3 k minus 5 vertical line equals 10`
> 
> > *This means *$3k-5$* is either equal to 10 or -10*
> *Solve each equation*
> 
> `table row cell 3 k minus 5 end cell equals 10 row cell 3 k end cell equals 15 row k equals 5 end table`
> 
> > *or*
> 
> `table row cell 3 k minus 5 end cell equals cell negative 10 end cell row cell 3 k end cell equals cell negative 5 end cell row k equals cell negative 5 over 3 end cell end table`
> 
> > *Write out the two answers*
> 
> $k=5\mathrm{or}k=-\frac{5}{3}$
> 
> **If the question had said "where **$k$** is an integer" then only **$k=5$** would be accepted**
