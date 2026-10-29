---
note_id: "rn_QgchJ42HYg9HdZ2Z"
title: "Combinations of Matrix Transformations"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/matrices/transformations-using-matrices/combinations-of-matrix-transformations
path: matrices/transformations-using-matrices/combinations-of-matrix-transformations
updated_at: "2024-04-10T13:34:45.939Z"
spec_point_ids: ["spcpt_kZwP597VC4kn3npw"]
spec_point_codes: []
guided_study: false
---

# Combinations of Matrix Transformations

## Combinations of Matrix Transformations

> **Spec point** — `spcpt_kZwP597VC4kn3npw`

## Combinations of Matrix Transformations

### How do I find a single matrix that represents a combination of transformations?

- A point $( x , y )$ can be transformed **twice**

  - **Firstly** by the matrix $P$, then** secondly** by the matrix $Q$
  - This is called a **combined** (or **composite** or **successive**) transformation
- A** single **matrix, $M$, representing the combined transformation can be found using **matrix multiplication** as follows:

  - $M=\mathrm{QP}$** **
  
    - The **order** matters: the **first** transformation is on the **right** in the multiplication
    - This order is the **reverse** of what you might expect!
  - Be careful: $\mathrm{PQ}$  represents** **$Q$ first, followed by $P$ second

### How do I find the inverse of a combined transformation?

- The inverse of a **product** of matrices is the product of the inverses of the matrices in **reverse order**

  - $( \text{AB} )^{- 1} = B^{- 1} A^{- 1}$
- Let $M$ represent the transformation **first** by $P$, then** second** by $Q$

  - That means$M=\mathrm{QP}$ from above
- Algebraically, $M^{ - } 1 = ( QP ) ^{ - } 1$ which gives $M^{-1}=P^{-1}Q^{-1}$

  - This shows that the **inverse**, $M^{-1}$**,**  first reverses $Q$** **, then reverses $P$
  
    - That is the order we would expect

> **Worked Example**
> Three transformations in the $x$-$y$ plane are represented by the matrices below.
> 
> $A = ( \begin{gathered} - 1 & 0 \\ 0 - 1 \end{gathered} )$**  **represents a rotation of 180° about the origin
> $B = ( \begin{gathered} - 1 & 0 \\ 0 1 \end{gathered} )$** **represents a reflection in the *y*-axis
> $C = ( \begin{gathered} 1 0 \\ 0 - 1 \end{gathered} )$** **represents a reflection in the *x*-axis
> 
> (a)  Use matrix multiplication to prove that a reflection in the *y*-axis followed by a reflection in the *x*-axis is equivalent to a rotation of 180° about the origin.
> 
> > *The question requires transformation* $B$ *followed by transformation* $C$
> *This is the same as the matrix* $\mathrm{CB}$ *in that order (the first transformation appears on the right)*
> 
> $\mathrm{CB}$
> 
> > *Use matrix multiplication to find* $\mathrm{CB}$
> 
> $\text{CB} = ( \begin{gathered} 1 0 \\ 0 - 1 \end{gathered} ) \times ( \begin{gathered} - 1 & 0 \\ 0 1 \end{gathered} ) = ( \begin{gathered} ( 1 \times - 1 + 0 \times 0 ) & ( 1 \times 0 + 0 \times 1 ) \\ ( 0 \times - 1 + - 1 \times 0 ) & ( 0 \times 0 + - 1 \times 1 ) \end{gathered} )$
> 
> > *The question claims that this is equivalent to transformation* $A$
> *Simplify the working above and show that it is the same as matrix* $A$
> 
> **Final answer:** $\text{CB} = ( \begin{gathered} - 1 & 0 \\ 0 - 1 \end{gathered} ) = A$
> **Therefore a reflection in the**** y****-axis followed by a reflection in the ****x****-axis is equivalent to a rotation of 180° about the origin**
> 
> **You would not get the marks for multiplying BC (it must be CB)**
> 
> (b)  A different transformation is represented by $\mathrm{CD}$ where $D^{- 1} = ( \begin{gathered} 2 0 \\ 0 1 \end{gathered} )$.
> 
> Find and simplify the matrix representing the inverse of the transformation.
> 
> > *Y**ou need to find the inverse of *$\mathrm{CD}$
> *You need the rule that* $( \text{CD} )^{- 1} = D^{- 1} C^{- 1}$
> *You can substitute in* $D^{-1}$ *from the question*
> 
> $\begin{gathered} ( \text{CD} )^{- 1} & = D^{- 1} C^{- 1} \\ = ( \begin{gathered} 2 0 \\ 0 1 \end{gathered} ) C^{- 1} \end{gathered}$
> 
> > *You need to find* $C^{-1}$
> *Use that* $M = ( \begin{gathered} a b \\ c d \end{gathered} ) \Leftrightarrow M^{- 1} = \frac{1}{\det M} ( \begin{gathered} d - b \\ - c & a \end{gathered} )$ *where* $\mathrm{det}M=ad-bc$
> 
> $\begin{gathered} C^{- 1} & = \frac{1}{1 \times ( - 1 ) - 0 \times 0} ( \begin{gathered} - 1 & 0 \\ 0 1 \end{gathered} ) \\ = ( \begin{gathered} 1 0 \\ 0 - 1 \end{gathered} ) \end{gathered}$
> 
> > *(Note that a reflection in the **x-**axis is its own inverse!)*
> *Substitute this into the working above and multiply the matrices*
> 
> $\begin{gathered} ( \text{CD} )^{- 1} & = ( \begin{gathered} 2 0 \\ 0 1 \end{gathered} ) ( \begin{gathered} 1 0 \\ 0 - 1 \end{gathered} ) \\ = ( \begin{gathered} 2 0 \\ 0 - 1 \end{gathered} ) \end{gathered}$
> 
> $\begin{gathered} ( \begin{gathered} 2 0 \\ 0 - 1 \end{gathered} ) \end{gathered}$
> 
> **There are other ways to do this question, for example finding **$D$** first**
> **If you saw that **$C^{-1}=C$** (as it is a reflection in the ****x****-axis), explain why clearly**
