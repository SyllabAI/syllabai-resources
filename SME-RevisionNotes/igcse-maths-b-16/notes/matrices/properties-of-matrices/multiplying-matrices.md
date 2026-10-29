---
note_id: "rn_p5HCc4mQthDm6Z6w"
title: "Multiplying Matrices"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/properties-of-matrices/multiplying-matrices
path: matrices/properties-of-matrices/multiplying-matrices
updated_at: "2026-01-14T10:53:48.747Z"
spec_point_ids: ["spcpt_gWpj9n8N6CP4TnDv"]
spec_point_codes: []
guided_study: false
---

# Multiplying Matrices

## Multiplying matrices

> **Spec point** — `spcpt_gWpj9n8N6CP4TnDv`

## Multiplying matrices

### How do I multiply two matrices?

- To **multiply** two matrices

  - the number of **columns** in the first matrix
  - must be **equal** to the number of **rows** in the second matrix
- For example, consider $A = ( \begin{gathered} 1 3 \\ 7 4 \end{gathered} )$ and $B = ( \begin{gathered} 1 0 5 \\ 8 2 9 \end{gathered} )$

  - You can multiply $A\timesB$
  
    - because the number of columns in $A$ (2) matches the number of rows in $B$ (2)
  - But you cannot multiply $B\timesA$
  
    - because the number of columns in $B$ (3) does not match the number of rows in $A$ (2)
- Multiplying matrices involves

  - multiplying the corresponding elements in a **row **of the **first** matrix
  
    - with the corresponding elements in a **column** of the **second **matrix
    - and writing the **sum** of the products in the answer matrix
  - It is easiest to see this through some examples
  - The process becomes more natural the more times you do it!

#### How do I multiply a 2×2 matrix by a 2×1 matrix?

- The answer will be a 2 x 1 matrix
- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix

  - $( \begin{gathered} a b \\ c d \end{gathered} ) ( \begin{gathered} x \\ y \end{gathered} ) = ( \begin{gathered} a x + b y \\ c x + d y \end{gathered} )$
- $( \begin{gathered} 1 2 \\ 3 4 \end{gathered} ) ( \begin{gathered} 10 \\ 20 \end{gathered} ) = ( \begin{gathered} 1 \times 10 + 2 \times 20 \\ 3 \times 10 + 4 \times 20 \end{gathered} ) = ( \begin{gathered} 10 + 40 \\ 30 + 80 \end{gathered} ) = ( \begin{gathered} 50 \\ 110 \end{gathered} )$

#### How do I multiply a 2×2 matrix by another 2×2 matrix?

- The answer will be a 2 x 2 matrix
- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix

  - $( \begin{gathered} a b \\ c d \end{gathered} ) ( \begin{gathered} A B \\ C D \end{gathered} ) = ( \begin{gathered} a A + b C & a B + b D \\ c A + d C & c B + d D \end{gathered} )$
- $( \begin{gathered} 1 2 \\ 3 4 \end{gathered} ) ( \begin{gathered} 5 10 \\ 20 25 \end{gathered} ) = ( \begin{gathered} 1 \times 5 + 2 \times 20 & 1 \times 10 + 2 \times 25 \\ 3 \times 5 + 4 \times 20 & 3 \times 10 + 4 \times 25 \end{gathered} ) = ( \begin{gathered} 5 + 40 & 10 + 50 \\ 15 + 80 & 30 + 100 \end{gathered} ) = ( \begin{gathered} 45 60 \\ 95 130 \end{gathered} )$

#### How do I multiply a 2×2 matrix by a 2×3 matrix?

- The answer will be a 2 x 3 matrix
- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix

  - $( \begin{gathered} a b \\ c d \end{gathered} ) ( \begin{gathered} A B C \\ D E F \end{gathered} ) = ( \begin{gathered} a A + b D & a B + b E \\ c A + d D & c B + d E \end{gathered} \begin{gathered} a C + b F \\ c C + d F \end{gathered} )$
- $\begin{gathered} ( \begin{gathered} 1 3 \\ 7 4 \end{gathered} ) ( \begin{gathered} 1 0 5 \\ 8 2 9 \end{gathered} ) & = ( \begin{gathered} 1 \times 1 + 3 \times 8 & 1 \times 0 + 3 \times 2 \\ 7 \times 1 + 4 \times 8 & 7 \times 0 + 4 \times 2 \end{gathered} \begin{gathered} 1 \times 5 + 3 \times 9 \\ 7 \times 5 + 4 \times 9 \end{gathered} ) \\ = ( \begin{gathered} 1 + 24 & 0 + 6 \\ 7 + 32 & 0 + 8 \end{gathered} \begin{gathered} 5 + 27 \\ 35 + 36 \end{gathered} ) \\ = ( \begin{gathered} 25 6 \\ 39 8 \end{gathered} \begin{gathered} 32 \\ 71 \end{gathered} ) \end{gathered}$

#### How do I multiply a 3×3 matrix by another 3×3 matrix?

- The answer will be a 3 x 3 matrix
- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix

  - $( \begin{gathered} a b c \\ d e f \\ g h i \end{gathered} ) ( \begin{gathered} A B C \\ D E F \\ G H I \end{gathered} ) = ( \begin{gathered} a A + b D + c G & a B + b E + c H & a C + b F + c I \\ d A + e D + f G & d B + e E + f H & d C + e F + f I \\ g A + h D + i G & g B + h E + i H & g C + h F + i I \end{gathered} )$
- $\begin{gathered} ( \begin{gathered} 1 0 3 \\ 0 - 5 & 0 \\ 2 7 1 \end{gathered} ) ( \begin{gathered} 0 2 3 \\ - 1 & 0 - 2 \\ 4 0 6 \end{gathered} ) & = ( \begin{gathered} 1 \times 0 + 0 \times ( - 1 ) + 3 \times 4 & 1 \times 2 + 0 \times 0 + 3 \times 0 & 1 \times 3 + 0 \times ( - 2 ) + 3 \times 6 \\ 0 \times 0 + ( - 5 ) \times ( - 1 ) + 0 \times 4 & 0 \times 2 + ( - 5 ) \times 0 + 0 \times 0 & 0 \times 3 + ( - 5 ) \times ( - 2 ) + 0 \times 6 \\ 2 \times 0 + 7 \times ( - 1 ) + 1 \times 4 & 2 \times 2 + 7 \times 0 + 1 \times 0 & 2 \times 3 + 7 \times ( - 2 ) + 1 \times 6 \end{gathered} ) \\ = ( \begin{gathered} 0 + 0 + 12 & 2 + 0 + 0 & 3 + 0 + 18 \\ 0 + 5 + 0 & 0 + 0 + 0 & 0 + 10 + 0 \\ 0 - 7 + 4 & 4 + 0 + 0 & 6 - 14 + 6 \end{gathered} ) \\ = ( \begin{gathered} 12 2 21 \\ 5 0 10 \\ - 3 & 4 - 2 \end{gathered} ) \end{gathered}$

### How do I square a matrix?

- Only **square matrices** (2 x 2 or 3 x 3) can be squared
- **Do not** square each individual element
- Write out a matrix multiplication

  - E.g. if $P = ( \begin{gathered} 2 4 \\ 1 - 3 \end{gathered} )$ then $P^{2} = P \times P = ( \begin{gathered} 2 4 \\ 1 - 3 \end{gathered} ) ( \begin{gathered} 2 4 \\ 1 - 3 \end{gathered} ) = ( \begin{gathered} 2 \times 2 + 4 \times 1 & 2 \times 4 + 4 \times ( - 3 ) \\ 1 \times 2 + ( - 3 ) \times 1 & 1 \times 4 + ( - 3 ) \times ( - 3 ) \end{gathered} ) = ( \begin{gathered} 8 - 4 \\ - 1 & 13 \end{gathered} )$
- It is possible to have **negative** elements after squaring a matrix

### When multiplying, does it matter which matrix is on the left and which is on the right?

- When **multiplying numbers** "swapping the order doesn't change the result"

  - E.g. 5 × 4 = 4 × 5
- This is **not true** for **matrix multiplication**

  - In general, **AB** ≠ **BA**
- For example, $( \begin{gathered} 1 2 \\ 3 4 \end{gathered} ) ( \begin{gathered} 0 1 \\ 5 1 \end{gathered} ) = ( \begin{gathered} 10 3 \\ 20 7 \end{gathered} )$ but $( \begin{gathered} 0 1 \\ 5 1 \end{gathered} ) ( \begin{gathered} 1 2 \\ 3 4 \end{gathered} ) = ( \begin{gathered} 3 4 \\ 8 14 \end{gathered} )$

### How can I multiply more than two matrices together?

- When **multiplying numbers** "it doesn't matter which order you group operations into"

  - E.g. to do 8 x 9 x 10, either (8 x 9) x 10 or 8 x (9 x 10) works
- This is **also true** for **matrix multiplication**

  - **(AB)C** ≡ **A(BC)**
- To multiply** three** matrices together

  - it's fine to start by multiplying the first two together
  
    - then multiplying the answer with the third matrix
  - or to start by multiplying the second two together
  
    - then multiplying the answer with the first matrix
- Just don't switch the order

  - **A(BC) **is not the same as **(BC)A**

### What is special about the identity matrix?

- **Multiplying **any 2×2 or 3×3 matrix by the corresponding ***identity matrix*** leaves it **unchanged**

  - $\mathrm{AI}=A$ and $\mathrm{IA}=A$
- For example, in the 2×2 case

  - $( \begin{gathered} a b \\ c d \end{gathered} ) ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} ) = ( \begin{gathered} a b \\ c d \end{gathered} )$** **and $( \begin{gathered} 1 0 \\ 0 1 \end{gathered} ) ( \begin{gathered} a b \\ c d \end{gathered} ) = ( \begin{gathered} a b \\ c d \end{gathered} )$
  - This result can be proved by multiplying together the two matrices on the left side of each equation
- The 2×2 identity matrix also leaves a 2×1 matrix unchanged

  - $( \begin{gathered} 1 0 \\ 0 1 \end{gathered} ) ( \begin{gathered} a \\ b \end{gathered} ) = ( \begin{gathered} a \\ b \end{gathered} )$
  - This can be relevant to [matrix transformations](https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/transformations-using-matrices/transforming-a-point/)
- The identity matrix is an important matrix which you should know (or recognise as $I$ in a question)

> **Worked Example**
> If $P = ( \begin{gathered} 3 1 \\ - 2 & 0 \end{gathered} )$, $Q = ( \begin{gathered} 5 - 5 \\ 4 2 \end{gathered} )$ and $R = ( \begin{gathered} 10 \\ 8 \end{gathered} )$, find the following:
> 
> (i)  $\mathrm{PR}$
> 
> (ii)  $\mathrm{PQ}$
> 
> (iii)  $Q^{2}$
> 
> **Answer:**
> 
> (i)*  **Write out *$\mathrm{PR}$ *in full*
> 
> $( \begin{gathered} 3 1 \\ - 2 & 0 \end{gathered} ) \times ( \begin{gathered} 10 \\ 8 \end{gathered} )$
> 
> > *Multiply the matrices*
> 
> $( \begin{gathered} ( 3 \times 10 ) + ( 1 \times 8 ) \\ ( - 2 \times 10 ) + ( 0 \times 8 ) \end{gathered} )$
> 
> > *Simplify*
> 
> `Error converting from MathML to accessible text.`
> 
> (ii)*  **Write out *$\mathrm{PQ}$ *in full*
> 
> $( \begin{gathered} 3 1 \\ - 2 & 0 \end{gathered} ) \times ( \begin{gathered} 5 - 5 \\ 4 2 \end{gathered} )$
> 
> > *Multiply the matrices*
> 
> $( \begin{gathered} ( 3 \times 5 + 1 \times 4 ) & ( 3 \times - 5 + 1 \times 2 ) \\ ( - 2 \times 5 + 0 \times 4 ) & ( - 2 \times - 5 + 0 \times 2 ) \end{gathered} ) = ( \begin{gathered} ( 15 + 4 ) & ( - 15 + 2 ) \\ ( - 10 + 0 ) & ( 10 + 0 ) \end{gathered} )$
> 
> > *Simplify*
> 
> `Error converting from MathML to accessible text.`
> 
> (iii)*  **Write out *$Q^{2}$ *as* $Q\timesQ$
> 
> $( \begin{gathered} 5 - 5 \\ 4 2 \end{gathered} ) \times ( \begin{gathered} 5 - 5 \\ 4 2 \end{gathered} )$
> 
> > *Multiply the matrices*
> 
> $( \begin{gathered} ( 5 \times 5 + - 5 \times 4 ) & ( 5 \times - 5 + - 5 \times 2 ) \\ ( 4 \times 5 + 2 \times 4 ) & ( 4 \times - 5 + 2 \times 2 ) \end{gathered} ) = ( \begin{gathered} ( 25 + - 20 ) & ( - 25 + - 10 ) \\ ( 20 + 8 ) & ( - 20 + 4 ) \end{gathered} )$
> 
> > *Simplify*
> 
> `Error converting from MathML to accessible text.`

> **Worked Example**
> If $A = ( \begin{gathered} 0 2 \\ 2 0 \end{gathered} )$ show that $A^{2}=4I$.
> 
> **Answer:**
> 
> > *Write out* $A^{2}$ *as* $A\timesA$
> 
> $( \begin{gathered} 0 2 \\ 2 0 \end{gathered} ) \times ( \begin{gathered} 0 2 \\ 2 0 \end{gathered} )$
> 
> > *Multiply the matrices*
> 
> $( \begin{gathered} 0 2 \\ 2 0 \end{gathered} ) \times ( \begin{gathered} 0 2 \\ 2 0 \end{gathered} ) = ( \begin{gathered} ( 0 \times 0 + 2 \times 2 ) & ( 0 \times 2 + 2 \times 0 ) \\ ( 2 \times 0 + 0 \times 2 ) & ( 2 \times 2 + 0 \times 0 ) \end{gathered} )$
> 
> $= ( \begin{gathered} 4 0 \\ 0 4 \end{gathered} )$
> 
> > *Write in terms of the identity matrix,* $I = ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} )$ *by factoring out 4*
> 
> $( \begin{gathered} 4 0 \\ 0 4 \end{gathered} ) = 4 ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} ) = 4 I$
