---
note_id: "rn_fKGy7ns686KpchbB"
title: "Inverse Matrices"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/matrices/matrix-algebra/inverse-matrices
path: matrices/matrix-algebra/inverse-matrices
updated_at: "2024-04-10T09:29:41.495Z"
spec_point_ids: ["spcpt_QxWTPpG7ytN8DXtk", "spcpt_7B4b9yCcrc9JWHbc"]
spec_point_codes: []
guided_study: false
---

# Inverse Matrices

## Determinant of a 2x2 Matrix

> **Spec point** — `spcpt_QxWTPpG7ytN8DXtk`

## Determinant of a 2x2 Matrix

### What is the determinant?

- The **determinant** is a **numerical value** (positive or negative) calculated from elements of a **square** matrix

  - It is used to find the **inverse** of a matrix
- For a 2 × 2 matrix, $A$, the determinant, $\mathrm{det}(A)$ or `open vertical bar bold A close vertical bar`, is given by

`bold A equals open parentheses table row a b row c d end table close parentheses space space space rightwards double arrow space space det space bold A equals open vertical bar bold A close vertical bar equals a d minus b c`

### What properties of determinants do I need to know?

- If $\mathrm{det}(A)=0$ then $A$** **is called a **singular matrix**
- If $\mathrm{det}(A)\neq0$ then $A$** **is called a **non-singular matrix**
- The determinant of the **identity matrix** is 1

  - $\mathrm{det}(I)=1$
- The determinant of the **zero matrix** is 0

  - $\mathrm{det}(0)=0$
- You do **not** need to know the following rules, but they can be **good checks** in an exam:

  - $\mathrm{det}(\mathrm{AB})=\mathrm{det}(A)\times\mathrm{det}(B)$
  - `det open parentheses bold A to the power of negative 1 end exponent close parentheses equals fraction numerator 1 over denominator det open parentheses bold A close parentheses end fraction`

> **Worked Example**
> Consider the matrix `bold A equals open parentheses table row 3 cell negative 6 end cell row p 7 end table close parentheses`, where $p$ is a constant.
> 
> Given that $\mathrm{det}A=-3$, find the value of $p$.
> 
> > *Use that if *`bold A equals open parentheses table row a b row c d end table close parentheses space`* then *`det space bold A equals open vertical bar bold A close vertical bar equals a d minus b c`
> *Work out the determinant algebraically*
> 
> `table row cell det open parentheses bold A close parentheses end cell equals cell 3 cross times 7 minus open parentheses negative 6 close parentheses cross times p end cell row blank equals cell 21 plus 6 p end cell end table`
> 
> > *Set this expression equal to -3 and solve for *$p$
> 
> `table row cell 21 plus 6 p end cell equals cell negative 3 end cell row cell 6 p end cell equals cell negative 24 end cell end table`
> 
> $p=-4$

## Inverse of a 2x2 Matrix

> **Spec point** — `spcpt_7B4b9yCcrc9JWHbc`

## Inverse of a 2x2 Matrix

### What is the inverse of a matrix?

- The** inverse** of a **square** matrix $A$is the matrix $A^{-1}$ which, when **multiplied **together (in either order), gives the** identity** matrix

  - $\mathrm{AA}^{-1}=A^{-1}A=I$
  - $A^{-1}$  has the same dimensions (order) as $A$

### How do I find the inverse of a 2x2 matrix?

- To find the inverse of a 2 × 2 matrix:

  - **Switch** the two entries on** leading diagonal** (top-left to bottom right)
  - **Change** the** signs** of the **other** two entries
  - **Divide** by the **determinant**

`bold A equals open parentheses table row a b row c d end table close parentheses space space rightwards double arrow space space bold A to the power of negative 1 end exponent equals fraction numerator 1 over denominator det space bold A end fraction open parentheses table row d cell negative b end cell row cell negative c end cell a end table close parentheses`

- Note that you **cannot divide **by zero

  - If $\mathrm{det}A=0$, then $A$ is not invertible ( $A^{-1}$ does **not exist**)
  
    - $A$ is **singular**
  - If $\mathrm{det}A\neq0$, then $A$ is **invertible**

### How do I find the inverse of a product of matrices?

- The inverse of a **product** of matrices is the product of the inverses of the matrices in **reverse order**

  - `open parentheses bold AB close parentheses to the power of negative 1 end exponent equals bold B to the power of negative 1 end exponent bold A to the power of negative 1 end exponent`

> **Exam Hint**
> There are two ways to check whether your inverse matrix is correct:
> 
> - use a calculator (they can find inverses),
> - or calculate $\mathrm{AA}^{-1}$ to see if you get the identity $I$.

> **Worked Example**
> Let `bold P equals open parentheses table row 1 cell negative 2 end cell row 4 k end table close parentheses` where $k\neq-8$.
> 
> (a)   Find $P^{-1}$, giving your answer in terms of $k$.
> 
> > *Use that *`bold A equals open parentheses table row a b row c d end table close parentheses space space rightwards double arrow space space bold A to the power of negative 1 end exponent equals fraction numerator 1 over denominator det space bold A end fraction open parentheses table row d cell negative b end cell row cell negative c end cell a end table close parentheses`* where *$\mathrm{det}A=ad-bc$
> *First find *`det open parentheses bold P close parentheses`
> 
> `table row cell det open parentheses bold P close parentheses end cell equals cell 1 cross times k minus 4 cross times open parentheses negative 2 close parentheses end cell row blank equals cell k plus 8 end cell end table`
> 
> > *Now divide *$P$* by *`det open parentheses bold P close parentheses`*, swap *$a$*  and *$d$*, and change signs of *$b$* and *$c$
> 
> `bold P to the power of negative 1 end exponent equals fraction numerator 1 over denominator k plus 8 end fraction open parentheses table row k 2 row cell negative 4 end cell 1 end table close parentheses`
> 
> **You can also write this as **`bold P to the power of negative 1 end exponent equals open parentheses table row cell fraction numerator k over denominator k plus 8 end fraction end cell cell fraction numerator 2 over denominator k plus 8 end fraction end cell row cell negative fraction numerator 4 over denominator k plus 8 end fraction end cell cell fraction numerator 1 over denominator k plus 8 end fraction end cell end table close parentheses`
> 
> (b)  Verify that $P^{-1}P=I$, where $I$ is the identity matrix.
> 
> > *Verify means check that it is true*
> *Substitute *$P^{-1}$* and *$P$* into the left-hand side and multiply out the matrices*
> 
> `table row cell bold P to the power of negative 1 end exponent bold P end cell equals cell fraction numerator 1 over denominator k plus 8 end fraction open parentheses table row k 2 row cell negative 4 end cell 1 end table close parentheses open parentheses table row 1 cell negative 2 end cell row 4 k end table close parentheses end cell row blank equals cell fraction numerator 1 over denominator k plus 8 end fraction open parentheses table row cell k cross times 1 plus 2 cross times 4 end cell cell k cross times open parentheses negative 2 close parentheses plus 2 cross times k end cell row cell negative 4 cross times 1 plus 1 cross times 4 end cell cell negative 4 cross times open parentheses negative 2 close parentheses plus 1 cross times k end cell end table close parentheses end cell row blank equals cell fraction numerator 1 over denominator k plus 8 end fraction open parentheses table row cell k plus 8 end cell 0 row 0 cell 8 plus k end cell end table close parentheses end cell end table`* *
> 
> > *The *$8+k$* is the same as *$k+8$
> *Since *$k\neq-8$* in the question, cancel the *`open parentheses k plus 8 close parentheses`*'s *
> 
> `bold P to the power of negative 1 end exponent bold P equals open parentheses table row 1 0 row 0 1 end table close parentheses`
> 
> > *The right-hand side is the 2 × 2 identity matrix*
> 
> $P^{-1}P=I$
> 
> **Even though **$\mathrm{PP}^{-1}=I$** is also true, this question only asks for the order shown **
