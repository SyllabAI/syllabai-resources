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

- A point (*x*,*y*) in a 2D plane can be **transformed** onto another point (*x*',*y*') by a **matrix**, $M$

  - (*x*,*y*) is the **object **and (*x*',*y*') is the **image**
- The **coordinates** of the image point can be found using **matrix multiplication**
- To transform (*x*, *y*) by the matrix $( \begin{gathered} a b \\ c d \end{gathered} )$

  - Write (*x*, *y*) as a **column vector,** $( \begin{gathered} x \\ y \end{gathered} )$
  
    - Note that this is the same as a $2\times1$ matrix
  - Use **matrix multiplication **to work out $( \begin{gathered} a b \\ c d \end{gathered} ) ( \begin{gathered} x \\ y \end{gathered} )$, which gives $( \begin{gathered} x ' \\ y ' \end{gathered} )$
  
    - $( \begin{gathered} x ' \\ y ' \end{gathered} ) = ( \begin{gathered} a b \\ c d \end{gathered} ) ( \begin{gathered} x \\ y \end{gathered} ) = ( \begin{gathered} a x + b y \\ c x + d y \end{gathered} )$
  - **Write down** the image point **coordinates**, (*x*', *y*')
- In harder questions you may be given the image coordinates, (*x*', *y*') and asked to find the original coordinates

  - Introduce letters (e.g. *x* and *y*) for the original coordinates, (*x*, *y*)
  
    - then use the matrix $M$ to set up and solve **simultaneous equations** to find *x* and *y*
  - Alternatively, you could use the **inverse** matrix $M^{-1}$ to **undo the transformation**
  
    - `| M ( | x | y | ) | = ( | x ' | | y ' | | ) left right double arrow ( | x | y | ) = M ^ - 1 ( | x ' | | y ' | | ) | |`
    - You can see this by solving the matrix equation for $( \begin{gathered} x \\ y \end{gathered} )$:

$\begin{gathered} M ( \begin{gathered} x \\ y \end{gathered} ) & = ( \begin{gathered} x ' \\ y ' \end{gathered} ) \\ M^{- 1} M ( \begin{gathered} x \\ y \end{gathered} ) & = M^{- 1} ( \begin{gathered} x ' \\ y ' \end{gathered} ) \\ I ( \begin{gathered} x \\ y \end{gathered} ) & = M^{- 1} ( \begin{gathered} x ' \\ y ' \end{gathered} ) \\ ( \begin{gathered} x \\ y \end{gathered} ) & = M^{- 1} ( \begin{gathered} x ' \\ y ' \end{gathered} ) \end{gathered}$

> **Worked Example**
> A matrix, $M$, is given by  $M = ( \begin{gathered} 4 5 \\ 1 - 2 \end{gathered} )$.
> 
> (a)  Work out the coordinates of the image of the point $( 2 , 3 )$ using the transformation represented by $M$.
> 
> **Answer:**
> 
> *Multiply the coordinates, written as a column vector, by the transformation matrix* $M$
> 
> $( \begin{gathered} 4 5 \\ 1 - 2 \end{gathered} ) ( \begin{gathered} 2 \\ 3 \end{gathered} ) = ( \begin{gathered} 4 \times 2 + 5 \times 3 \\ 1 \times 2 + - 2 \times 3 \end{gathered} ) = ( \begin{gathered} 23 \\ - 4 \end{gathered} )$
> 
> > *Rewrite the answer as coordinates*
> 
> $(23,-4)$
> 
> (b) The image of another point, $P$, using the transformation represented by $M$ is $( 11 , 6 )$.
> 
> Work out the coordinates of $P$.
> 
> **Answer:**
> 
> **Method 1**
> 
> *You do not know the coordinates of* $P$*, so you can write it as* $( x , y )$*  *
> 
> *Let* $P = ( x , y )$* *
> 
> > *Multiply the coordinates of **P**, written as a column vector, by the transformation matrix *$M$
> 
> - *This time, you know the image of the point after it is transformed, so can fill this in as the "answer"*
> 
> $\begin{gathered} ( \begin{gathered} 4 5 \\ 1 - 2 \end{gathered} ) ( \begin{gathered} x \\ y \end{gathered} ) & = ( \begin{gathered} 11 \\ 6 \end{gathered} ) \\ ( \begin{gathered} 4 x + 5 y \\ x - 2 y \end{gathered} ) & = ( \begin{gathered} 11 \\ 6 \end{gathered} ) \end{gathered}$
> 
> > *Equate the matching elements of the two matrices*
> 
> > $\begin{gathered} 4 x + 5 y & = 11 \\ x - 2 y & = 6 \end{gathered}$* *
> 
> > *You now have a pair of simultaneous equations which can be solved using either elimination or substitution*
> 
> > *Using substitution, start by rearranging the second equation to make* $x$ *the subject*
> 
> $x=2y+6$
> 
> > *Substitute this into the first equation, and solve to find* $y$* *
> 
> $\begin{gathered} 4 ( 2 y + 6 ) + 5 y & = 11 \\ 8 y + 24 + 5 y & = 11 \\ 13 y + 24 & = 11 \\ 13 y & = - 13 \\ y = - 1 \end{gathered}$
> 
> > *Substitute* $y=-1$ *into the second equation to find* $x$* *
> 
> $\begin{gathered} x - 2 ( - 1 ) & = 6 \\ x + 2 & = 6 \\ x = 4 \end{gathered}$
> 
> **Final answer:** **P**** is**** **$(4,-1)$
> 
> **Method 2**
> 
> > *Find the inverse of matrix* $M$
> 
> - *The inverse of* $( \begin{gathered} a b \\ c d \end{gathered} )$ *is* $\frac{1}{a d - b c} ( \begin{gathered} d - b \\ - c & a \end{gathered} )$
> 
> $\begin{gathered} M^{- 1} & = \frac{1}{4 \times ( - 2 ) - 5 \times 1} ( \begin{gathered} - 2 & - 5 \\ - 1 & 4 \end{gathered} ) \\ = \frac{1}{- 13} ( \begin{gathered} - 2 & - 5 \\ - 1 & 4 \end{gathered} ) \\ = ( \begin{gathered} \frac{2}{13} & \frac{5}{13} \\ \frac{1}{13} & - \frac{4}{13} \end{gathered} ) \end{gathered}$
> 
> > *If* $M ( \begin{gathered} x \\ y \end{gathered} ) = ( \begin{gathered} 11 \\ 6 \end{gathered} )$*, then* $( \begin{gathered} x \\ y \end{gathered} ) = M^{- 1} ( \begin{gathered} 11 \\ 6 \end{gathered} )$
> 
> $\begin{gathered} ( \begin{gathered} x \\ y \end{gathered} ) & = ( \begin{gathered} \frac{2}{13} & \frac{5}{13} \\ \frac{1}{13} & - \frac{4}{13} \end{gathered} ) ( \begin{gathered} 11 \\ 6 \end{gathered} ) \\ = ( \begin{gathered} \frac{2}{13} \times 11 + \frac{5}{13} \times 6 \\ \frac{1}{13} \times 11 + ( - \frac{4}{13} ) \times 6 \end{gathered} ) \\ = ( \begin{gathered} \frac{52}{13} \\ - \frac{13}{13} \end{gathered} ) \\ = ( \begin{gathered} 4 \\ - 1 \end{gathered} ) \end{gathered}$
> 
> > *Write as coordinates*
> 
> **Final answer:** **P**** is**** **$(4,-1)$
