---
note_id: "rn_ZHbHKcJHGNhPdqzh"
title: "Multiplying Matrices"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/matrices/matrix-algebra/multiplying-matrices
path: matrices/matrix-algebra/multiplying-matrices
updated_at: "2024-04-10T13:17:14.799Z"
spec_point_ids: ["spcpt_DFnsnvP295B5FmbK", "spcpt_zBy7BQ9swFbWk3ZJ"]
spec_point_codes: []
guided_study: false
---

# Multiplying Matrices

## Multiplying Matrices

> **Spec point** — `spcpt_DFnsnvP295B5FmbK`

## Multiplying Matrices

### How do I multiply a 2x2 matrix by a 2x1 matrix?

- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix
- The answer will be a **2 × 1 matrix**

  - $( \begin{gathered} a b \\ c d \end{gathered} ) ( \begin{gathered} x \\ y \end{gathered} ) = ( \begin{gathered} a x + b y \\ c x + d y \end{gathered} )$
- $( \begin{gathered} 1 2 \\ 3 4 \end{gathered} ) ( \begin{gathered} 10 \\ 20 \end{gathered} ) = ( \begin{gathered} 1 \times 10 + 2 \times 20 \\ 3 \times 10 + 4 \times 20 \end{gathered} ) = ( \begin{gathered} 10 + 40 \\ 30 + 80 \end{gathered} ) = ( \begin{gathered} 50 \\ 110 \end{gathered} )$

### How do I multiply a 2x2 matrix by another 2x2 matrix?

- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix
- The answer will be a **2 × 2** **matrix**

  - $( \begin{gathered} a b \\ c d \end{gathered} ) ( \begin{gathered} A B \\ C D \end{gathered} ) = ( \begin{gathered} a A + b C & a B + b D \\ c A + d C & c B + d D \end{gathered} )$
- $( \begin{gathered} 1 2 \\ 3 4 \end{gathered} ) ( \begin{gathered} 5 10 \\ 20 25 \end{gathered} ) = ( \begin{gathered} 1 \times 5 + 2 \times 20 & 1 \times 10 + 2 \times 25 \\ 3 \times 5 + 4 \times 20 & 3 \times 10 + 4 \times 25 \end{gathered} ) = ( \begin{gathered} 5 + 40 & 10 + 50 \\ 15 + 80 & 30 + 100 \end{gathered} ) = ( \begin{gathered} 45 60 \\ 95 130 \end{gathered} )$
- This process becomes more natural the more times you do it!

### How do I square a matrix?

- **Do not** square each individual element inside the matrix
- Write out a **matrix multiplication**

  - If $P = ( \begin{gathered} 2 4 \\ 1 - 3 \end{gathered} )$ then $P^{2} = P \times P = ( \begin{gathered} 2 4 \\ 1 - 3 \end{gathered} ) ( \begin{gathered} 2 4 \\ 1 - 3 \end{gathered} ) = ( \begin{gathered} 2 \times 2 + 4 \times 1 & 2 \times 4 + 4 \times ( - 3 ) \\ 1 \times 2 + ( - 3 ) \times 1 & 1 \times 4 + ( - 3 ) \times ( - 3 ) \end{gathered} ) = ( \begin{gathered} 8 - 4 \\ - 1 & 13 \end{gathered} )$
- It is possible to have **negative** elements in a squared matrix

### How do I multiply matrices of any dimensions?

- To multiply a matrix by another matrix:

  - The **number of columns** in the **first **matrix must be **equal** to the **number of rows** in the **second **matrix
  - For example, the **first** matrix is $m\timesn$ and the **second** matrix is $n\timesp$
  - The **order **of the r**esultant** matrix will be $m\timesp$
- Multiply corresponding elements in the **row** of the **first** matrix with the corresponding elements in the **column** of the **second **matrix

  - Place their **sums** in the resultant matrix
  
    - For example, if $A = ( \begin{gathered} a b c \\ d e f \end{gathered} )$, $B = ( \begin{gathered} g h \\ i j \\ k l \end{gathered} )$
    - then `Error converting from MathML to accessible text.`
    - whereas  $\text{BA} = ( \begin{gathered} ( g a + h d ) & ( g b + h e ) & ( g c + h f ) \\ ( i a + j d ) & ( i b + j e ) & ( i c + j f ) \\ ( k a + l d ) & ( k b + l e ) & ( k c + l f ) \end{gathered} )$
- It is possible for **AB **to exist but **BA***** ***not to exist

  - For **square matrices** of the same order, **AB***** ***and* ***BA***** ***will both exist

### What does commutative mean?

- **Commutative** means "swapping the order doesn't change the result"

  - 5 × 4 = 4 × 5 and 3 + 2 = 2 + 3
  
    - Multiplication and addition of **numbers** are commutative
  - 4 ÷ 2 ≠ 2 ÷ 4 and 5 - 3 ≠ 3 - 5
  
    - Division and subtraction of **numbers** are not commutative
- However,** matrix multiplication** is **not commutative**

  - In general **AB** ≠ **BA**
- For example, $( \begin{gathered} 1 2 \\ 3 4 \end{gathered} ) ( \begin{gathered} 0 1 \\ 5 1 \end{gathered} ) = ( \begin{gathered} 10 3 \\ 20 7 \end{gathered} )$ but $( \begin{gathered} 0 1 \\ 5 1 \end{gathered} ) ( \begin{gathered} 1 2 \\ 3 4 \end{gathered} ) = ( \begin{gathered} 3 4 \\ 8 14 \end{gathered} )$

### What does associative mean?

- **Associative** means "it doesn't matter which order you group operations into"

  - To do 5 + 4 + 3, either (5 + 4) + 3 or 5 + (4 + 3) works
  - To do 8 × 9 × 10, either (8 × 9) × 10 or 8 × (9 × 10) works
  
    - Multiplication and addition of **numbers** are associative
  - (8 ÷ 4) ÷ 2 ≠ 8 ÷ (4 ÷ 2) and (5 - 4) - 3 ≠ 5 - (4 - 3)
  
    - Division and subtraction of **numbers** are not associative
- **Matrix multiplication** is** associative**

  - **(AB)C** ≡ **A(BC)**
- To multiply** three** matrices together, it is fine to either:

  - start by multiplying the first two together,
  - or start by multiplying the second two together
  
    - Just don't switch the order
    - **A(BC) **is not the same as **(BC)A**

> **Worked Example**
> If $P = ( \begin{gathered} 3 1 \\ - 2 & 0 \end{gathered} )$, $Q = ( \begin{gathered} 5 - 5 \\ 4 2 \end{gathered} )$ and $R = ( \begin{gathered} 10 - 1 & 4 \\ 8 0 5 \end{gathered} )$, find the following:
> 
> (a)  $\mathrm{PQ}$
> 
> > *Write out *$\mathrm{PQ}$* in full*
> 
> $( \begin{gathered} 3 1 \\ - 2 & 0 \end{gathered} ) \times ( \begin{gathered} 5 - 5 \\ 4 2 \end{gathered} )$
> 
> > *Multiply the matrices*
> 
> $( \begin{gathered} ( 3 \times 5 + 1 \times 4 ) & ( 3 \times - 5 + 1 \times 2 ) \\ ( - 2 \times 5 + 0 \times 4 ) & ( - 2 \times - 5 + 0 \times 2 ) \end{gathered} ) = ( \begin{gathered} ( 15 + 4 ) & ( - 15 + 2 ) \\ ( - 10 + 0 ) & ( 10 + 0 ) \end{gathered} )$
> 
> > *Simplify*
> 
> $\text{PQ} = ( \begin{gathered} 19 - 13 \\ - 10 & 10 \end{gathered} )$
> 
> (b)  $\mathrm{PR}$
> 
> > *Write out *$\mathrm{PR}$* in full*
> 
> $( \begin{gathered} 3 1 \\ - 2 & 0 \end{gathered} ) \times ( \begin{gathered} 10 - 1 & 4 \\ 8 0 5 \end{gathered} )$
> 
> > *The order (dimensions) agree, as *$P$* has 2 columns and *$R$* has 2 rows*
> *Multiply the matrices*
> 
> $( \begin{gathered} ( 3 \times 10 + 1 \times 8 ) & ( 3 \times - 1 + 1 \times 0 ) & ( 3 \times 4 + 1 \times 5 ) \\ ( - 2 \times 10 + 0 \times 8 ) & ( - 2 \times - 1 + 0 \times 0 ) & ( - 2 \times 4 + 0 \times 5 ) \end{gathered} )$
> 
> > *Simplify*
> 
> $\text{PR} = ( \begin{gathered} 38 - 3 & 17 \\ - 20 & 2 - 8 \end{gathered} )$
> 
> (c)  $Q^{2}$
> 
> > *Write out *$Q^{2}$* as *$Q\timesQ$
> 
> $( \begin{gathered} 5 - 5 \\ 4 2 \end{gathered} ) \times ( \begin{gathered} 5 - 5 \\ 4 2 \end{gathered} )$
> 
> > *Multiply the matrices*
> 
> $( \begin{gathered} ( 5 \times 5 + - 5 \times 4 ) & ( 5 \times - 5 + - 5 \times 2 ) \\ ( 4 \times 5 + 2 \times 4 ) & ( 4 \times - 5 + 2 \times 2 ) \end{gathered} ) = ( \begin{gathered} ( 25 + - 20 ) & ( - 25 + - 10 ) \\ ( 20 + 8 ) & ( - 20 + 4 ) \end{gathered} )$
> 
> > *Simplify*
> 
> $Q^{2} = ( \begin{gathered} 5 - 35 \\ 28 - 16 \end{gathered} )$
> 
> (d)  Explain why the matrix $\mathrm{RP}$ does not exist.
> 
> > *An *$m\timesn$*  matrix can only be multiplied by an *$n\timesp$*  matrix*
> 
> **Final answer:** **The order (dimensions) do not agree, as **$R$** has 3 columns but **$P$** has 2 rows**

## The Identity Matrix

> **Spec point** — `spcpt_zBy7BQ9swFbWk3ZJ`

## The Identity Matrix

### What is the Identity Matrix?

- The **identity** **matrix**, $I$, is a **square** matrix with:

  - **Ones** along the **leading diagonal** (from top-left to bottom-right)
  - and **zeros** everywhere else
  
    - The **2 × 2** identity matrix is $I = ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} )$
    - The **3 × 3** identity matrix is $I = ( \begin{gathered} 1 0 0 \\ 0 1 0 \\ 0 0 1 \end{gathered} )$
  - The notation $I_{n}$ can be used to specify the $n\timesn$ identity matrix
- **Multiplying** any **square** matrix by the same-sized** identity** matrix leaves it **unchanged**

  - Both $\mathrm{AI}=A$ and $\mathrm{IA}=A$
  - $( \begin{gathered} a b \\ c d \end{gathered} ) ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} ) = ( \begin{gathered} a b \\ c d \end{gathered} )$** **and $( \begin{gathered} 1 0 \\ 0 1 \end{gathered} ) ( \begin{gathered} a b \\ c d \end{gathered} ) = ( \begin{gathered} a b \\ c d \end{gathered} )$
  
    - This result can be proved by multiplying together the matrices

> **Exam Hint**
> The identity matrix is an important matrix which you should know or recognise as $I$ in a question.

> **Worked Example**
> If $A = ( \begin{gathered} 0 2 \\ 2 0 \end{gathered} )$ show that $A^{2}=4I$.
> 
> > *Write out *$A^{2}$* as *$A\timesA$
> 
> $( \begin{gathered} 0 2 \\ 2 0 \end{gathered} ) \times ( \begin{gathered} 0 2 \\ 2 0 \end{gathered} )$
> 
> > *Multiply the matrices*
> 
> $\begin{gathered} ( \begin{gathered} 0 2 \\ 2 0 \end{gathered} ) \times ( \begin{gathered} 0 2 \\ 2 0 \end{gathered} ) & = ( \begin{gathered} ( 0 \times 0 + 2 \times 2 ) & ( 0 \times 2 + 2 \times 0 ) \\ ( 2 \times 0 + 0 \times 2 ) & ( 2 \times 2 + 0 \times 0 ) \end{gathered} ) \\ = ( \begin{gathered} 4 0 \\ 0 4 \end{gathered} ) \end{gathered}$
> 
> > *Write in terms of the identity matrix, *$I = ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} )$* **by factorising out 4*
> 
> $( \begin{gathered} 4 0 \\ 0 4 \end{gathered} ) = 4 ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} ) = 4 I$
