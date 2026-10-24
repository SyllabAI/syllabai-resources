---
note_id: "rn_nnBDSgNV7PRX4wQF"
title: "Linear Interpolation"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/numerical-solutions-of-equations/numerical-solutions-of-equations/linear-interpolation
path: numerical-solutions-of-equations/numerical-solutions-of-equations/linear-interpolation
updated_at: "2024-04-04T17:00:44.619Z"
spec_point_ids: ["spcpt_vywmYvX3FQXf7n75"]
spec_point_codes: []
guided_study: false
---

# Linear Interpolation

## Linear Interpolation

> **Spec point** — `spcpt_vywmYvX3FQXf7n75`

## Linear Interpolation

### What is linear interpolation?

- **Linear interpolation** draws a **straight line** between the points *A* and *B* with coordinates  $( a , \mathrm{f} ( a ) )$ and $( b , \mathrm{f} ( b ) )$, where $a<x<b$ is an interval containing a root to the equation $\mathrm{f} ( x ) = 0$

  - As $\mathrm{f} ( a )$ and $\mathrm{f} ( b )$ have **different signs**, *A *and *B* are on **either side **of the *x*-axis
  - The **approximation** to the root is  where this straight line **cuts the *****x*****-axis**
  
    - This is at the point *X* with coordinates $( x , 0 )$
    - Points *A, X *and *B* lie on the same straight line
- It helps to use the **gradient formula**

  - The gradient between $( x_{1} , y_{1} )$ and $( x_{2} , y_{2} )$ is $\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$

### How do I apply linear interpolation using gradients?

- This is best explained with an example
- If the root of $\mathrm{f} ( x ) = 0$ lies in the interval $[ 1 , 2 ]$ and $\mathrm{f} ( 1 ) = - 5$ and $\mathrm{f} ( 2 ) = 10$, then:

  - *A* is the point $( 1 , - 5 )$
  - *B* is the point $( 2 , 10 )$
  - *X* is the point $( x , 0 )$
  
    - This is the *x*-intercept of the line *AB*
    - *A, X *and *B* lie on the same **straight line**
  - The **gradient **of ***AX*** equals the** gradient** of ***XB***
  
    - The** order** matters (not *BX*)
  - Use the **gradient formula** to set these equal
  
    - $\frac{0 - ( - 5 )}{x - 1} = \frac{10 - 0}{2 - x}$ giving $\frac{5}{x-1}=\frac{10}{2-x}$
  - **Solve** the equation to find $x$
  
    - $5 ( 2 - x ) = 10 ( x - 1 )$
    - expand and solve to get $x=\frac{4}{3}$
- This process can be **repeated **to get the next approximation
- This gradient method does** not** require a** sketch**

### What other methods can I use to do linear interpolation?

- You can **sketch** the points *A*, *B* and *X* on a diagram and use **similar triangles** either side of the *x*-axis to find an **equation** in $x$

  - This leads to the same equation as the gradients above
- Or you can use **coordinate geometry** to find the **equation** of the **line *****AB***

  - Use $y - y_{1} = m ( x - x_{1} )$
  - Then find its ***x*****-intercept**
  
    - Substitute in $y=0$ and solve for $x$

> **Exam Hint**
> If the calculations involve lengthy decimals, you can use $\mathrm{f} ( a )$ and $\mathrm{f} ( b )$ to stand for their numbers  in your working!

> **Worked Example**
> The equation $\mathrm{f} ( x ) = 0$ where $\mathrm{f} ( x ) = x^{3} - \sqrt{x} - 2$ has a root in the interval $[ 1.4 , 1.5 ]$.
> 
> Use linear interpolation once to find an approximation to the root, giving your answer to 3 decimal places.
> 
> > *Find *$\mathrm{f} ( 1.4 )$* and *$\mathrm{f} ( 1.5 )$
> 
> $\begin{gathered} \mathrm{f} ( 1.4 ) & = 1.4^{3} - \sqrt{1.4} - 2 = - 0.439215... \\ \mathrm{f} ( 1.5 ) & = 1.5^{3} - \sqrt{1.5} - 2 = 0.150255... \end{gathered}$
> 
> > *It is easier to write them as *$\mathrm{f} ( 1.4 )$* and *$\mathrm{f} ( 1.5 )$* for now*
> *Let **A**, **B** and **X** be the points *$( 1.4 , \mathrm{f} ( 1.4 ) )$*, *$( 1.5 , \mathrm{f} ( 1.5 ) )$* and *$( x , 0 )$
> *Use the gradient formula *$\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$* to find the gradient of **AX*
> 
> *gradient of ***AX ***is *$\frac{0 - \mathrm{f} ( 1.4 )}{x - 1.4}$
> 
> > *Use the gradient formula *$\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$* to find the gradient of **XB*
> 
> *gradient of ***XB ***is *$\frac{ \mathrm{f} ( 1.5 ) - 0}{1.5 - x}$
> 
> > *Set the two gradients equal to each other*
> 
> $\frac{0 - \mathrm{f} ( 1.4 )}{x - 1.4} = \frac{ \mathrm{f} ( 1.5 ) - 0}{1.5 - x}$
> 
> > *Simplify and cross multiply*
> 
> $\begin{gathered} \frac{- \mathrm{f} ( 1.4 )}{x - 1.4} & = \frac{ \mathrm{f} ( 1.5 )}{1.5 - x} \\ - \mathrm{f} ( 1.4 ) ( 1.5 - x ) & = \mathrm{f} ( 1.5 ) ( x - 1.4 ) \end{gathered}$
> 
> > *Expand and collect the *$x$* terms on the right-hand side*
> 
> $\begin{gathered} - 1.5 \mathrm{f} ( 1.4 ) + \mathrm{f} ( 1.4 ) x & = \mathrm{f} ( 1.5 ) x - 1.4 \mathrm{f} ( 1.5 ) \\ 1.4 \mathrm{f} ( 1.5 ) - 1.5 \mathrm{f} ( 1.4 ) & = \mathrm{f} ( 1.5 ) x - \mathrm{f} ( 1.4 ) x \end{gathered}$
> 
> > *Factorise out the *$x$*, then make *$x$* the subject*
> 
> $\begin{gathered} 1.4 \mathrm{f} ( 1.5 ) - 1.5 \mathrm{f} ( 1.4 ) & = x [ \mathrm{f} ( 1.5 ) - \mathrm{f} ( 1.4 ) ] \\ \frac{1.4 \mathrm{f} ( 1.5 ) - 1.5 \mathrm{f} ( 1.4 )}{ \mathrm{f} ( 1.5 ) - \mathrm{f} ( 1.4 )} & = x \end{gathered}$
> 
> > *Substitute in  *$\mathrm{f} ( 1.4 )$* and *$\mathrm{f} ( 1.5 )$* from above*
> 
> $\begin{gathered} \frac{1.4 \times 0.150255... - 1.5 \times ( - 0.439215... )}{0.150255... - ( - 0.439215... )} & = x \\ 1.47451... & = x \end{gathered}$
> 
> > *Give your final answer to 3 decimal places*
> 
> **Final answer:** $1.475$** to 3 decimal places**
> 
> **If you did the working without **$\mathrm{f} ( 1.4 )$** and **$\mathrm{f} ( 1.5 )$**, keep lots of decimal places**
