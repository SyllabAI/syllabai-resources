---
note_id: "rn_p6Mx48RtMn9ShxRp"
title: "Transforming a Point"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/transformations-using-matrices/transforming-a-point
path: matrices/transformations-using-matrices/transforming-a-point
updated_at: "2026-01-14T14:13:12.697Z"
spec_point_ids: ["spcpt_cfsNsZkBNfQ2hWbY"]
spec_point_codes: []
guided_study: false
---

# Transforming a Point

## Transforming a Point

> **Spec point** — `spcpt_cfsNsZkBNfQ2hWbY`

## Transforming a point

### How do I transform a point using a matrix?

- A point (*x*,* y*) in a 2D plane can be **transformed** onto another point (*x*',*y*') by a **matrix**, $M$

  - (*x*,* y*) is the **object **and (*x*',*y*') is the **image**
- The **coordinates** of the image point can be found using **matrix multiplication**
- To transform (*x*, *y*) by the matrix `open parentheses table row a b row c d end table close parentheses`

  - Write (*x*, *y*) as a **column vector,** `open parentheses table row x row y end table close parentheses`
  
    - Note that this is the same as a $2\times1$ matrix
  - Use **matrix multiplication **to work out `open parentheses table row a b row c d end table close parentheses open parentheses table row x row y end table close parentheses`, which gives `open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses`
  
    - `open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses equals open parentheses table row a b row c d end table close parentheses open parentheses table row x row y end table close parentheses equals open parentheses table row cell a x plus b y end cell row cell c x plus d y end cell end table close parentheses`
  - **Write down** the image point **coordinates**, (*x*', *y*')
- In harder questions you may be given the image coordinates, (*x*', *y*') and asked to find the original coordinates

  - Introduce letters (e.g. *x* and *y*) for the original coordinates, (*x*, *y*)
  
    - then use the matrix $M$ to set up and solve **simultaneous equations** to find *x* and *y*
  - Alternatively, you could use the **inverse** matrix $M^{-1}$ to **undo the transformation**
  
    - `table row cell bold M open parentheses table row x row y end table close parentheses end cell equals cell open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses space space left right double arrow space space open parentheses table row x row y end table close parentheses equals bold M to the power of negative 1 end exponent open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses end cell end table`
    - You can see this by solving the matrix equation for `open parentheses table row x row y end table close parentheses`:

`table row cell bold M open parentheses table row x row y end table close parentheses end cell equals cell open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses end cell row cell bold M to the power of negative 1 end exponent bold M open parentheses table row x row y end table close parentheses end cell equals cell bold M to the power of negative 1 end exponent open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses end cell row cell bold I open parentheses table row x row y end table close parentheses end cell equals cell bold M to the power of negative 1 end exponent open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses end cell row cell open parentheses table row x row y end table close parentheses end cell equals cell bold M to the power of negative 1 end exponent open parentheses table row cell x apostrophe end cell row cell y apostrophe end cell end table close parentheses end cell end table`

> **Worked Example**
> A matrix, $M$, is given by  `bold M equals open parentheses table row 4 5 row 1 cell negative 2 end cell end table close parentheses`.
> 
> (a)  Work out the coordinates of the image of the point `open parentheses 2 comma space 3 close parentheses` using the transformation represented by $M$.
> 
> **Answer:**
> 
> *Multiply the coordinates, written as a column vector, by the transformation matrix *$M$
> 
> `open parentheses table row 4 5 row 1 cell negative 2 end cell end table close parentheses open parentheses table row 2 row 3 end table close parentheses equals open parentheses table row cell 4 cross times 2 space plus space 5 cross times 3 end cell row cell 1 cross times 2 space plus space minus 2 cross times 3 end cell end table close parentheses equals open parentheses table row 23 row cell negative 4 end cell end table close parentheses`
> 
> > *Rewrite the answer as coordinates*
> 
> $(23,-4)$
> 
> (b) The image of another point, $P$, using the transformation represented by $M$ is `open parentheses 11 comma space 6 close parentheses`.
> 
> Work out the coordinates of $P$.
> 
> **Answer:**
> 
> **Method 1**
> 
> *You do not know the coordinates of *$P$*, so you can write it as *`open parentheses x comma y close parentheses`*  *
> 
> *Let *`P equals open parentheses x comma y close parentheses`* *
> 
> > *Multiply the coordinates of **P**, written as a column vector, by the transformation matrix *$M$
> 
> - *This time, you know the image of the point after it is transformed, so can fill this in as the "answer"*
> 
> `table row cell open parentheses table row 4 5 row 1 cell negative 2 end cell end table close parentheses open parentheses table row x row y end table close parentheses end cell equals cell open parentheses table row 11 row 6 end table close parentheses end cell row cell open parentheses table row cell 4 x plus 5 y end cell row cell x minus 2 y end cell end table close parentheses end cell equals cell open parentheses table row 11 row 6 end table close parentheses end cell end table`
> 
> > *Equate the matching elements of the two matrices*
> 
> > `table row cell 4 x plus 5 y end cell equals 11 row cell x minus 2 y end cell equals 6 end table`* *
> 
> > *You now have a pair of simultaneous equations which can be solved using either elimination or substitution*
> 
> > *Using substitution, start by rearranging the second equation to make *$x$* the subject*
> 
> $x=2y+6$
> 
> > *Substitute this into the first equation, and solve to find *$y$* *
> 
> `table row cell 4 open parentheses 2 y plus 6 close parentheses plus 5 y end cell equals 11 row cell 8 y plus 24 plus 5 y end cell equals 11 row cell 13 y plus 24 end cell equals 11 row cell 13 y end cell equals cell negative 13 end cell row y equals cell negative 1 end cell end table`
> 
> > *Substitute *$y=-1$* into the second equation to find *$x$* *
> 
> `table row cell x minus 2 open parentheses negative 1 close parentheses end cell equals 6 row cell x plus 2 end cell equals 6 row x equals 4 end table`
> 
> **Final answer:** **P**** is**** **$(4,-1)$
> 
> **Method 2**
> 
> > *Find the inverse of matrix *$M$
> 
> - *The inverse of *`space open parentheses table row a b row c d end table close parentheses space`* is *`space fraction numerator 1 over denominator a d minus b c end fraction open parentheses table row d cell negative b end cell row cell negative c end cell a end table close parentheses`
> 
> `table row cell bold M to the power of bold minus bold 1 end exponent end cell equals cell fraction numerator 1 over denominator 4 cross times open parentheses negative 2 close parentheses minus 5 cross times 1 end fraction open parentheses table row cell negative 2 end cell cell negative 5 end cell row cell negative 1 end cell 4 end table close parentheses end cell row blank equals cell fraction numerator 1 over denominator negative 13 end fraction open parentheses table row cell negative 2 end cell cell negative 5 end cell row cell negative 1 end cell 4 end table close parentheses end cell row blank equals cell open parentheses table row cell 2 over 13 end cell cell 5 over 13 end cell row cell 1 over 13 end cell cell negative 4 over 13 end cell end table close parentheses end cell end table`
> 
> > *If *`bold space bold M open parentheses table row x row y end table close parentheses equals open parentheses table row 11 row 6 end table close parentheses`*, then *`space open parentheses table row x row y end table close parentheses equals bold M to the power of negative 1 end exponent open parentheses table row 11 row 6 end table close parentheses`
> 
> `table row cell open parentheses table row x row y end table close parentheses end cell equals cell open parentheses table row cell 2 over 13 end cell cell 5 over 13 end cell row cell 1 over 13 end cell cell negative 4 over 13 end cell end table close parentheses open parentheses table row 11 row 6 end table close parentheses end cell row blank equals cell open parentheses table row cell 2 over 13 cross times 11 plus 5 over 13 cross times 6 end cell row cell 1 over 13 cross times 11 plus open parentheses negative 4 over 13 close parentheses cross times 6 end cell end table close parentheses end cell row blank equals cell open parentheses table row cell 52 over 13 end cell row cell negative 13 over 13 end cell end table close parentheses end cell row blank equals cell open parentheses table row 4 row cell negative 1 end cell end table close parentheses end cell end table`
> 
> > *Write as coordinates*
> 
> **Final answer:** **P**** is**** **$(4,-1)$
