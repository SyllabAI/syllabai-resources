---
note_id: "rn_CjrhsjYdqGdcDmWn"
title: "Inverses of Matrices"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/properties-of-matrices/inverses-of-matrices
path: matrices/properties-of-matrices/inverses-of-matrices
updated_at: "2026-01-14T11:34:25.621Z"
spec_point_ids: ["spcpt_Vr9z3J63Pcc4xWmH"]
spec_point_codes: []
guided_study: false
---

# Inverses of Matrices

## Inverse of a 2x2 matrix

> **Spec point** — `spcpt_Vr9z3J63Pcc4xWmH`

## Inverse of a 2x2 matrix

### What is the inverse of a matrix?

- Only a *square matrix* has an inverse
- The inverse of a square matrix $A$is denoted as the matrix $A^{-1}$

  - The product of these matrices is the **identity** matrix, $\mathrm{AA}^{-1}=A^{-1}A=I$

### How do I find the inverse of a 2x2 matrix?

- The method for finding the inverse of a $2\times2$ matrix is:

  - Switch the two entries on the top left-bottom right diagonal
  - Change the signs of the other two entries
  - Divide by the determinant $ad-bc$

`bold A equals open parentheses table row a b row c d end table close parentheses space space rightwards double arrow space space bold A to the power of bold minus bold 1 end exponent equals fraction numerator 1 over denominator a d minus b c end fraction open parentheses table row d cell negative b end cell row cell negative c end cell a end table close parentheses`

> **Exam Hint**
> The formula for the inverse is on the course Formulae sheet, and will be provided for you in Paper 2 questions where it is needed.
> 
> Determinant questions can also appear in Paper 1, however. While these can usually be answered without having to use the inverse formula, it is still a good idea to know the formula going into the exam.

- Note that if the determinant, $ad-bc$, is equal to zero, then the term $\frac{1}{ad-bc}$ in the formula is not defined

  - If this is the case, then the matrix does **not** have an inverse
  - You will not need to deal with this situation on the exam

> **Worked Example**
> `bold A equals open parentheses table row 1 3 row 2 7 end table close parentheses space space space space space space space bold B equals open parentheses table row 7 cell negative 3 end cell row cell negative 2 end cell 1 end table close parentheses`
> 
> Show that $B$ is the inverse of $A$.
> 
> **Answer:**
> 
> **Method 1**
> 
> > *If you know the inverse formula, you can use it to calculate the inverse of *$A$* directly*
> 
> - *The inverse of *`space open parentheses table row a b row c d end table close parentheses space`* is *`space fraction numerator 1 over denominator a d minus b c end fraction open parentheses table row d cell negative b end cell row cell negative c end cell a end table close parentheses`
> 
> `table row cell bold A to the power of bold minus bold 1 end exponent end cell equals cell fraction numerator 1 over denominator 1 cross times 7 minus 3 cross times 2 end fraction open parentheses table row 7 cell negative 3 end cell row cell negative 2 end cell 1 end table close parentheses end cell row blank equals cell fraction numerator 1 over denominator 7 minus 6 end fraction open parentheses table row 7 cell negative 3 end cell row cell negative 2 end cell 1 end table close parentheses end cell row blank equals cell 1 open parentheses table row 7 cell negative 3 end cell row cell negative 2 end cell 1 end table close parentheses end cell row blank equals cell open parentheses table row 7 cell negative 3 end cell row cell negative 2 end cell 1 end table close parentheses end cell row blank equals bold B end table`
> 
> **Final answer:** $B$** is the inverse of **$A$
> ** **
> 
> **Method 2**
> 
> > *If you don't know the inverse formula, you can use the definition of the inverse*
> 
> - *I.e. if *$A^{-1}$* is the inverse of *$A$*, then *$\mathrm{AA}^{-1}=A^{-1}A=I$
> 
> > *So you can show that *$B$* is the inverse of *$A$* by showing*
> 
> - *either that *$\mathrm{AB}=I$
> - *or that *$\mathrm{BA}=I$
> 
> `table row bold AB equals cell open parentheses table row 1 3 row 2 7 end table close parentheses open parentheses table row 7 cell negative 3 end cell row cell negative 2 end cell 1 end table close parentheses end cell row blank equals cell open parentheses table row cell 1 cross times 7 plus 3 cross times open parentheses negative 2 close parentheses end cell cell 1 cross times open parentheses negative 3 close parentheses plus 3 cross times 1 end cell row cell 2 cross times 7 plus 7 cross times open parentheses negative 2 close parentheses end cell cell 2 cross times open parentheses negative 3 close parentheses plus 7 cross times 1 end cell end table close parentheses end cell row blank equals cell open parentheses table row cell 7 minus 6 end cell cell negative 3 plus 3 end cell row cell 14 minus 14 end cell cell negative 6 plus 7 end cell end table close parentheses end cell row blank equals cell open parentheses table row 1 0 row 0 1 end table close parentheses end cell row blank equals bold I end table`
> 
> **Final answer:** $\mathrm{AB}$** is equal to the identity matrix, so **$B$** is the inverse of **$A$
