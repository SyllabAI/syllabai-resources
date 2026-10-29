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

- A point $( x , y )$ in a 2D plane can be **transformed** (**mapped**) on to another point $( x ' , y ' )$ by a 2 × 2 **matrix**, $M$

  - This is called a **linear transformation**
  
    - $( x , y )$ is the **object **and $( x ' , y ' )$ is the **image**
- The **coordinates** of the image point can be found using **matrix multiplication**
- To transform $( x , y )$ by the matrix $( \begin{gathered} a b \\ c d \end{gathered} )$

  - Write $( x , y )$ as a **column vector,** $( \begin{gathered} x \\ y \end{gathered} )$
  - Use **matrix multiplication **to work out $( \begin{gathered} a b \\ c d \end{gathered} ) ( \begin{gathered} x \\ y \end{gathered} )$, which gives $( \begin{gathered} x ' \\ y ' \end{gathered} )$
  - **Write down** the image point **coordinates**, $( x ' , y ' )$
- If given image coordinates, $( x ' , y ' )$, and asked to find original coordinates

  - use **inverse** matrices
  - $M ( \begin{gathered} x \\ y \end{gathered} ) = ( \begin{gathered} x ' \\ y ' \end{gathered} ) \Leftrightarrow ( \begin{gathered} x \\ y \end{gathered} ) = M^{- 1} ( \begin{gathered} x ' \\ y ' \end{gathered} )$

## How do I transform a set of vertices?

- **Vertices** of a **shape** can be transformed **one-by-one** using the method above

  - This gives the vertices of the **new** shape
  
    - **Straight lines** between the vertices will still be straight lines in the new shape
  - Sometimes the order (**clockwise** or **anticlockwise**) of the vertices is** reversed**
  
    - This is also called changing the **sense **of the vertices
- An** alternative method** is to stack **column vectors** of **coordinates** into a **vertex matrix**

  - $( 1 , 2 )$, $( 3 , 4 )$, $( 5 , 6 )$ and $( 0 , 10 )$ become $( \begin{gathered} 1 3 5 0 \\ 2 4 6 10 \end{gathered} )$
  - Then **multiply **the **matrix** $M$ by the **vertex matrix** above
  - The **new** **columns** represent the corresponding **image** **coordinates**

> **Worked Example**
> The matrix $M$ is given by $M = ( \begin{gathered} 4 5 \\ 1 - 2 \end{gathered} )$.
> A triangle has coordinates $( 1 , 0 )$, $( 2 , 3 )$ and $( - 1 , 5 )$.
> 
> Work out the coordinates of the triangle after the transformation represented by the matrix $M$ has been applied.
> 
> > *Multiply the matri**x *$M$* by each set **of coordinates, written as a column vectors*
> 
> $\begin{gathered} ( \begin{gathered} 4 5 \\ 1 - 2 \end{gathered} ) ( \begin{gathered} 1 \\ 0 \end{gathered} ) & = ( \begin{gathered} 4 \times 1 + 5 \times 0 \\ 1 \times 1 + - 2 \times 0 \end{gathered} ) = ( \begin{gathered} 4 \\ 1 \end{gathered} ) \\ ( \begin{gathered} 4 5 \\ 1 - 2 \end{gathered} ) ( \begin{gathered} 2 \\ 3 \end{gathered} ) & = ( \begin{gathered} 4 \times 2 + 5 \times 3 \\ 1 \times 2 + - 2 \times 3 \end{gathered} ) = ( \begin{gathered} 23 \\ - 4 \end{gathered} ) \\ ( \begin{gathered} 4 5 \\ 1 - 2 \end{gathered} ) ( \begin{gathered} - 1 \\ 5 \end{gathered} ) & = ( \begin{gathered} 4 \times ( - 1 ) + 5 \times 5 \\ 1 \times ( - 1 ) + - 2 \times 5 \end{gathered} ) = ( \begin{gathered} 21 \\ - 11 \end{gathered} ) \end{gathered}$
> 
> > *Rewrite the answers as coordinates*
> 
> **Final answer:** $( 4 , 1 )$**, **$( 23 , - 4 )$** and **$( 21 , - 11 )$
> 
> ** Alternatively, you can multi****ply **$M$** by a vertex mat****rix: **$( \begin{gathered} 4 5 \\ 1 - 2 \end{gathered} ) ( \begin{gathered} 1 2 - 1 \\ 0 3 5 \end{gathered} ) = ( \begin{gathered} 4 23 21 \\ 1 - 4 & - 11 \end{gathered} )$

## Determinants as Area Scale Factors

> **Spec point** — `spcpt_jHbjfY6F8Vh77FP9`

## Determinants as Area Scale Factors

### How are 2x2 determinants and areas related?

- When **transforming **vertices of an** object** using the **matrix **$M$** **to give vertices of the **image**

  - the** magnitude** of the **determinant **of $M$ is the **area scale factor** of **enlargement **from the** **object to the image
  - $\vert \det ( M ) \vert$is the area scale factor
- For example, if a shape is transformed by $M = ( \begin{gathered} 1 3 \\ 2 4 \end{gathered} )$ then

  - $\det ( M ) = 1 \times 4 - 2 \times 3 = - 2$
  - so$\vert \det ( M ) \vert = \vert - 2 \vert = 2$
  
    - This transformation** doubles** the area of any shape
- A **negative determinant** means the **sense** (**clockwise **or **anticlockwise**) of the vertices is **reversed**

> **Exam Hint**
> Remember the modulus signs around the determinant as this can often lead to two solutions in algebraic questions.

> **Worked Example**
> A transformation, represented  by the matrix $M = ( \begin{gathered} 3 2 \\ 4 k + 1 \end{gathered} )$, where $k$ is a constant, maps a quadrilateral of area 45 square units to a quadrilateral of area 450 square units.
> 
> Find the possible values of $k$.
> 
> > *Find the scale factor of enlargement of the area from 45 to 450*
> 
> > *Area scale factor is 10*
> 
> > *The magnitude of the determinant is the area scale factor*
> *Start by finding and simplifying the determinant of* $M$
> 
> $\begin{gathered} \det ( M ) & = 3 ( k + 1 ) - 2 \times 4 \\ = 3 k + 3 - 8 \\ = 3 k - 5 \end{gathered}$
> 
> > *Set the magnitude of the determinant equal to 10*
> 
> $\vert 3 k - 5 \vert = 10$
> 
> > *This means* $3k-5$ *is either equal to 10 or -10*
> *Solve each equation*
> 
> $\begin{gathered} 3 k - 5 & = 10 \\ 3 k & = 15 \\ k = 5 \end{gathered}$
> 
> > *or*
> 
> $\begin{gathered} 3 k - 5 & = - 10 \\ 3 k & = - 5 \\ k = - \frac{5}{3} \end{gathered}$
> 
> > *Write out the two answers*
> 
> $k=5\mathrm{or}k=-\frac{5}{3}$
> 
> **If the question had said "where **$k$** is an integer" then only **$k=5$** would be accepted**
