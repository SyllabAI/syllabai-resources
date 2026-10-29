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

$A = ( \begin{gathered} a b \\ c d \end{gathered} ) \Leftrightarrow A^{- 1} = \frac{1}{a d - b c} ( \begin{gathered} d - b \\ - c & a \end{gathered} )$

> **Exam Hint**
> The formula for the inverse is on the course Formulae sheet, and will be provided for you in Paper 2 questions where it is needed.
> 
> Determinant questions can also appear in Paper 1, however. While these can usually be answered without having to use the inverse formula, it is still a good idea to know the formula going into the exam.

- Note that if the determinant, $ad-bc$, is equal to zero, then the term $\frac{1}{ad-bc}$ in the formula is not defined

  - If this is the case, then the matrix does **not** have an inverse
  - You will not need to deal with this situation on the exam

> **Worked Example**
> $A = ( \begin{gathered} 1 3 \\ 2 7 \end{gathered} ) B = ( \begin{gathered} 7 - 3 \\ - 2 & 1 \end{gathered} )$
> 
> Show that $B$ is the inverse of $A$.
> 
> **Answer:**
> 
> **Method 1**
> 
> > *If you know the inverse formula, you can use it to calculate the inverse of* $A$ *directly*
> 
> - *The inverse of* $( \begin{gathered} a b \\ c d \end{gathered} )$ *is* $\frac{1}{a d - b c} ( \begin{gathered} d - b \\ - c & a \end{gathered} )$
> 
> $\begin{gathered} A^{- 1} & = \frac{1}{1 \times 7 - 3 \times 2} ( \begin{gathered} 7 - 3 \\ - 2 & 1 \end{gathered} ) \\ = \frac{1}{7 - 6} ( \begin{gathered} 7 - 3 \\ - 2 & 1 \end{gathered} ) \\ = 1 ( \begin{gathered} 7 - 3 \\ - 2 & 1 \end{gathered} ) \\ = ( \begin{gathered} 7 - 3 \\ - 2 & 1 \end{gathered} ) \\ = B \end{gathered}$
> 
> **Final answer:** $B$** is the inverse of **$A$
> ** **
> 
> **Method 2**
> 
> > *If you don't know the inverse formula, you can use the definition of the inverse*
> 
> - *I.e. if* $A^{-1}$ *is the inverse of* $A$*, then* $\mathrm{AA}^{-1}=A^{-1}A=I$
> 
> > *So you can show that* $B$ *is the inverse of* $A$ *by showing*
> 
> - *either that* $\mathrm{AB}=I$
> - *or that* $\mathrm{BA}=I$
> 
> $\begin{gathered} \text{AB} = ( \begin{gathered} 1 3 \\ 2 7 \end{gathered} ) ( \begin{gathered} 7 - 3 \\ - 2 & 1 \end{gathered} ) \\ = ( \begin{gathered} 1 \times 7 + 3 \times ( - 2 ) & 1 \times ( - 3 ) + 3 \times 1 \\ 2 \times 7 + 7 \times ( - 2 ) & 2 \times ( - 3 ) + 7 \times 1 \end{gathered} ) \\ = ( \begin{gathered} 7 - 6 & - 3 + 3 \\ 14 - 14 & - 6 + 7 \end{gathered} ) \\ = ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} ) \\ = I \end{gathered}$
> 
> **Final answer:** $\mathrm{AB}$** is equal to the identity matrix, so **$B$** is the inverse of **$A$
