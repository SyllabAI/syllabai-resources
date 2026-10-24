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
- For a 2 × 2 matrix, $A$, the determinant, $\mathrm{det}(A)$ or $\left| A \right|$, is given by

$A = ( \begin{gathered} a b \\ c d \end{gathered} ) \Leftrightarrow \det A = \left| A \right| = a d - b c$

### What properties of determinants do I need to know?

- If $\mathrm{det}(A)=0$ then $A$** **is called a **singular matrix**
- If $\mathrm{det}(A)\neq0$ then $A$** **is called a **non-singular matrix**
- The determinant of the **identity matrix** is 1

  - $\mathrm{det}(I)=1$
- The determinant of the **zero matrix** is 0

  - $\mathrm{det}(0)=0$
- You do **not** need to know the following rules, but they can be **good checks** in an exam:

  - $\mathrm{det}(\mathrm{AB})=\mathrm{det}(A)\times\mathrm{det}(B)$
  - $\det ( A^{- 1} ) = \frac{1}{\det ( A )}$

> **Worked Example**
> Consider the matrix $A = ( \begin{gathered} 3 - 6 \\ p 7 \end{gathered} )$, where $p$ is a constant.
> 
> Given that $\mathrm{det}A=-3$, find the value of $p$.
> 
> > *Use that if *$A = ( \begin{gathered} a b \\ c d \end{gathered} )$* then *$\det A = \left| A \right| = a d - b c$
> *Work out the determinant algebraically*
> 
> $\begin{gathered} \det ( A ) & = 3 \times 7 - ( - 6 ) \times p \\ = 21 + 6 p \end{gathered}$
> 
> > *Set this expression equal to -3 and solve for *$p$
> 
> $\begin{gathered} 21 + 6 p & = - 3 \\ 6 p & = - 24 \end{gathered}$
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

$A = ( \begin{gathered} a b \\ c d \end{gathered} ) \Leftrightarrow A^{- 1} = \frac{1}{\det A} ( \begin{gathered} d - b \\ - c & a \end{gathered} )$

- Note that you **cannot divide **by zero

  - If $\mathrm{det}A=0$, then $A$ is not invertible ( $A^{-1}$ does **not exist**)
  
    - $A$ is **singular**
  - If $\mathrm{det}A\neq0$, then $A$ is **invertible**

### How do I find the inverse of a product of matrices?

- The inverse of a **product** of matrices is the product of the inverses of the matrices in **reverse order**

  - $( \text{AB} )^{- 1} = B^{- 1} A^{- 1}$

> **Exam Hint**
> There are two ways to check whether your inverse matrix is correct:
> 
> - use a calculator (they can find inverses),
> - or calculate $\mathrm{AA}^{-1}$ to see if you get the identity $I$.

> **Worked Example**
> Let $P = ( \begin{gathered} 1 - 2 \\ 4 k \end{gathered} )$ where $k\neq-8$.
> 
> (a)   Find $P^{-1}$, giving your answer in terms of $k$.
> 
> > *Use that *$A = ( \begin{gathered} a b \\ c d \end{gathered} ) \Leftrightarrow A^{- 1} = \frac{1}{\det A} ( \begin{gathered} d - b \\ - c & a \end{gathered} )$* where *$\mathrm{det}A=ad-bc$
> *First find *$\det ( P )$
> 
> $\begin{gathered} \det ( P ) & = 1 \times k - 4 \times ( - 2 ) \\ = k + 8 \end{gathered}$
> 
> > *Now divide *$P$* by *$\det ( P )$*, swap *$a$*  and *$d$*, and change signs of *$b$* and *$c$
> 
> $P^{- 1} = \frac{1}{k + 8} ( \begin{gathered} k 2 \\ - 4 & 1 \end{gathered} )$
> 
> **You can also write this as **$P^{- 1} = ( \begin{gathered} \frac{k}{k + 8} & \frac{2}{k + 8} \\ - \frac{4}{k + 8} & \frac{1}{k + 8} \end{gathered} )$
> 
> (b)  Verify that $P^{-1}P=I$, where $I$ is the identity matrix.
> 
> > *Verify means check that it is true*
> *Substitute *$P^{-1}$* and *$P$* into the left-hand side and multiply out the matrices*
> 
> $\begin{gathered} P^{- 1} P & = \frac{1}{k + 8} ( \begin{gathered} k 2 \\ - 4 & 1 \end{gathered} ) ( \begin{gathered} 1 - 2 \\ 4 k \end{gathered} ) \\ = \frac{1}{k + 8} ( \begin{gathered} k \times 1 + 2 \times 4 & k \times ( - 2 ) + 2 \times k \\ - 4 \times 1 + 1 \times 4 & - 4 \times ( - 2 ) + 1 \times k \end{gathered} ) \\ = \frac{1}{k + 8} ( \begin{gathered} k + 8 & 0 \\ 0 8 + k \end{gathered} ) \end{gathered}$* *
> 
> > *The *$8+k$* is the same as *$k+8$
> *Since *$k\neq-8$* in the question, cancel the *$( k + 8 )$*'s *
> 
> $P^{- 1} P = ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} )$
> 
> > *The right-hand side is the 2 × 2 identity matrix*
> 
> $P^{-1}P=I$
> 
> **Even though **$\mathrm{PP}^{-1}=I$** is also true, this question only asks for the order shown **
