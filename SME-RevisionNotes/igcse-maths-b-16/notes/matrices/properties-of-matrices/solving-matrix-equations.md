---
note_id: "rn_7HCGBNPXM8Mnj2t7"
title: "Solving Matrix Equations"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/properties-of-matrices/solving-matrix-equations
path: matrices/properties-of-matrices/solving-matrix-equations
updated_at: "2026-01-14T11:42:53.189Z"
spec_point_ids: ["spcpt_JGrDCdnmTzs2Z9Cb"]
spec_point_codes: []
guided_study: false
---

# Solving Matrix Equations

## Solving matrix equations with inverses

> **Spec point** — `spcpt_JGrDCdnmTzs2Z9Cb`

## Solving matrix equations with inverses

- Inverses can be used to **rearrange** and **solve** equations with matrices
- This relies on the essential properties of inverses and of the identity matrix:

  - $\mathrm{AA}^{-1}=A^{-1}A=I$
  - $\mathrm{AI}=\mathrm{IA}=A$
- For example, to solve the matrix equation $\mathrm{AB}=C$** **for $B$

  - First multiply both sides of the equation 'from the left' by $A^{-1}$
  
    - $A^{-1}\mathrm{AB}=A^{-1}C$
  - But $A^{-1}A=I$, so
  
    - $\mathrm{IB}=A^{-1}C$
  - And $\mathrm{IB}=B$, so
  
    - $B=A^{-1}C$
  - Then multiply together the two matrices on the right-hand side to find $B$ explicitly
- Similarly, you can solve the matrix equation $\mathrm{BA}=C$** **for $B$

  - Though here you will need to multiply 'from the right' by $A^{-1}$

$\begin{gathered} BAA^{- 1} & = CA^{- 1} \\ \text{BI} = CA^{- 1} \\ B = CA^{- 1} \end{gathered}$

- This is similar to solving a regular equation by 'doing the same thing to both sides'

  - Except that **order of multiplication** matters with matrices
  
    - Multiplying 'from the left' is **not** the same as multiplying 'from the right'
  - For example, if you tried to solve $\mathrm{BA}=C$** **for $B$ by multiplying 'from the left' by $A^{-1}$
  
    - you would get $A^{-1}\mathrm{BA}=A^{-1}C$
    - which does not simplify any further

> **Exam Hint**
> Remember that a matrix and its inverse only 'collapse' to the identity matrix $I$ when they are next to each other in a multiplication.
> 
> - So $A^{-1}\mathrm{AB}=\mathrm{IB}=B$
> - and $\mathrm{BAA}^{-1}=\mathrm{BI}=B$
> - but $A^{-1}\mathrm{BA}$ does not simplify any further

> **Worked Example**
> $P = ( \begin{gathered} 4 - 2 \\ - 2 & 2 \end{gathered} ) Q = ( \begin{gathered} k 1 \\ 3 0 \end{gathered} ) R = ( \begin{gathered} 10 4 \\ - 2 & - 2 \end{gathered} )$
> 
> where $k$ is a constant.
> 
> (a) Find $P^{-1}$.
> 
> **Answer:**
> 
> > *Use the inverse formula for a *$2\times2$* matrix*
> 
> - *The inverse of *$( \begin{gathered} a b \\ c d \end{gathered} )$* is *$\frac{1}{a d - b c} ( \begin{gathered} d - b \\ - c & a \end{gathered} )$
> 
> $\begin{gathered} P^{- 1} & = \frac{1}{4 \times 2 - ( - 2 ) \times ( - 2 )} ( \begin{gathered} 2 2 \\ 2 4 \end{gathered} ) \\ = \frac{1}{8 - 4} ( \begin{gathered} 2 2 \\ 2 4 \end{gathered} ) \\ = 1 \frac{1}{4} ( \begin{gathered} 2 2 \\ 2 4 \end{gathered} ) \\ = ( \begin{gathered} 1 \frac{1}{4} \times 2 & 1 \frac{1}{4} \times 2 \\ 1 \frac{1}{4} \times 2 & 1 \frac{1}{4} \times 4 \end{gathered} ) \\ = ( \begin{gathered} 1 \frac{1}{2} & 1 \frac{1}{2} \\ 1 \frac{1}{2} & 1 \end{gathered} ) \end{gathered}$
> 
> $\begin{gathered} P^{- 1} & = ( \begin{gathered} 1 \frac{1}{2} & 1 \frac{1}{2} \\ 1 \frac{1}{2} & 1 \end{gathered} ) \end{gathered}$
> 
> (b) Given that $\mathrm{PQ}=R$ find the value of $k$.
> 
> **Answer:**
> 
> > *Use matrix algebra to solve the equation for *$Q$
> 
> - *Multiply both sides of the equation 'from the left' by *$P^{-1}$
> 
> $P^{-1}\mathrm{PQ}=P^{-1}R$
> 
> - *By the definition of the inverse, *$P^{-1}P=I$
> 
> $\mathrm{IQ}=P^{-1}R$
> 
> - *By the properties of the identity matrix, *$\mathrm{IQ}=Q$
> 
> $Q=P^{-1}R$
> 
> > *That gives you a matrix 'formula' for *$Q$
> 
> - *Substitute in matrices *$P^{-1}$* and *$R$
> 
> $Q = ( \begin{gathered} 1 \frac{1}{2} & 1 \frac{1}{2} \\ 1 \frac{1}{2} & 1 \end{gathered} ) ( \begin{gathered} 10 4 \\ - 2 & - 2 \end{gathered} )$
> 
> - *Carry out the multiplication*
> 
> $\begin{gathered} Q = ( \begin{gathered} 1 \frac{1}{2} \times 10 + 1 \frac{1}{2} \times ( - 2 ) & 1 \frac{1}{2} \times 4 + 1 \frac{1}{2} \times ( - 2 ) \\ 1 \frac{1}{2} \times 10 + 1 \times ( - 2 ) & 1 \frac{1}{2} \times 4 + 1 \times - 2 \end{gathered} ) \\ = ( \begin{gathered} 5 - 1 & 2 - 1 \\ 5 - 2 & 2 - 2 \end{gathered} ) \\ = ( \begin{gathered} 4 1 \\ 3 0 \end{gathered} ) \end{gathered}$
> 
> $k=4$
