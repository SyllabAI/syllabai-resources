---
note_id: "rn_kDtdvRBvw3BzTCNp"
title: "Tangents & Normals"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/calculus/applications-of-differentiation/tangents-and-normals
path: calculus/applications-of-differentiation/tangents-and-normals
updated_at: "2024-10-20T15:26:36.641Z"
spec_point_ids: ["spcpt_9g3SMYJGHKqj8sr5"]
spec_point_codes: []
guided_study: false
---

# Tangents & Normals

## Tangents & Normals

> **Spec point** — `spcpt_9g3SMYJGHKqj8sr5`

## Tangents & Normals

### What is a tangent?

- At any **point** on the graph of a (non-linear) **function**

  - the **tangent** is the straight line that **touches** the graph at the point **without cutting** through it
  - Its **gradient** is given by the **derivative** of the function

![Tangent to a curve](../../../assets/e709449608bc-7-2-1-grad-tang-norm-illustr-2.png)

### How do I find the equation of a tangent?

- You need a **point** and the **gradient** to find the **equation of a straight line**

  - The **gradient** of the **tangent** to the function $y = \mathrm{f} ( x )$ at the point $(x_{1},y_{1})$ is $f^{'}(x_{1})$
- Therefore to find the **equation** of the **tangent** to the function $y=f(x)$ at the point $(x_{1},y_{1})$

  - Find  $\mathrm{f}^{'} ( x )$
  - Substitute $x_{1}$ into $\mathrm{f} ' ( x )$ to find the gradient $\mathrm{f}^{'} ( x_{1} )$,
  - Use the  $y - y_{1} = m ( x - x_{1} )$ form of the line equation
  
    - $y-y_{1}=f^{'}(x_{1})(x-x_{1})$
  - Rearrange the equation into whatever form the question requires

### What is a normal?

- At any point on the graph of a (non-linear) function

  - the **normal** is the straight line that passes through that point
  - and is **perpendicular** to the **tangent**

![Normal to a curve](../../../assets/b9f8a429b5c9-7-2-1-grad-tang-norm-illustr-3.png)

### How do I find the equation of a normal?

- You need a **point** and the **gradient** to find the **equation of a straight line**

  - The **tangent **and the **normal** are **perpendicular**
  - Therefore the **gradient** of the **normal** to the function $y = \mathrm{f} ( x )$ at the point $(x_{1},y_{1})$ is $-\frac{1}{f^{'}(x_{1})}$
- To find the **equation** of the **normal** to the function $y=f(x)$ at the point $(x_{1},y_{1})$

  - Find  $\mathrm{f}^{'} ( x )$
  - Substitute $x_{1}$ into $\mathrm{f} ' ( x )$ to find the gradient of the tangent $\mathrm{f}^{'} ( x_{1} )$
  - Use that to find the gradient of the normal $- \frac{1}{ \mathrm{f}^{'} ( x_{1} )}$
  - Use the  $y - y_{1} = m ( x - x_{1} )$ form of the line equation
  
    - $y-y_{1}=-\frac{1}{f^{'}(x_{1})}(x-x_{1})$
  - Rearrange the equation into whatever form the question requires

> **Exam Hint**
> - Make sure you are confident with finding the equation of a straight line
> 
>   - In particular when you know the gradient and one point on the line
>   - This is an essential skill for finding tangents and normals

> **Worked Example**
> The function $f(x)$ is defined by
> 
> $f(x)=2x^{4}+\frac{3}{x^{2}}x\neq0$
> 
> a) Find an equation for the tangent to the curve $y=f(x)$ at the point where $x=1$, giving your answer in the form $y=mx+c$.
> 
> > *Substitute *$x=1$* into *$\mathrm{f} ( x )$* to find the *$y$*-coordinate of the point *
> 
> $\mathrm{f} ( 1 ) = 2 ( 1 )^{4} + \frac{3}{( 1 )^{2}} = 2 + 3 = 5$
> 
> > *So the point in question is *$( 1 , 5 )$
> 
> > *Now differentiate to find *$\mathrm{f}^{'} ( x )$*, first using laws of indices to rewrite *$\frac{3}{x^{2}}$* as *$3x^{-2}$
> 
> $\mathrm{f} ( x ) = 2 x^{4 + 3 x^{-2} }$
> 
> $\begin{gathered} \mathrm{f}^{'} ( x ) & = 2 ( 4 x^{4 - 3} ) + 3 ( - 2 x^{- 2 - 1} ) \\ = 8 x^{3} - 6 x^{- 3} \\ = 8 x^{3} - \frac{6}{x^{3}} \end{gathered}$
> 
> > *Substitute *$x=1$* into *$\mathrm{f}^{'} ( x )$* to find the gradient of the tangent at the point*
> 
> $\mathrm{f}^{'} ( 1 ) = 8 ( 1 )^{3} - \frac{6}{( 1 )^{3}} = 8 - 6 = 2$
> 
> > *Now use  *$y - y_{1} = m ( x - x_{1} )$*  to find the equation of the line*
> 
> > *Here *$m=2$* and *$( x_{1} , y_{1} ) = ( 1 , 5 )$
> 
> $\begin{array}{rcl} y - 5 & = 2 ( x - 1 ) \\ y - 5 & = 2 x - 2 \\ y = 2 x + 3 \end{array}$
> 
> $y=2x+3$
> 
> b) Find an equation for the normal to the curve $y = \mathrm{f} ( x )$ at the point where $x=1$, giving your answer in the form $ax+by=c$, where $a$, $b$ and $c$ are integers.
> 
> > *The normal and tangent are perpendicular*
> 
> > *So the gradient of the normal will be  *$- \frac{1}{ \mathrm{f}^{'} ( 1 )}$
> 
> $- \frac{1}{ \mathrm{f}^{'} ( 1 )} = - 1 \frac{1}{2}$
> 
> > *Now use  *$y - y_{1} = m ( x - x_{1} )$*  to find the equation of the line*
> 
> > *Here *$m=-\frac{1}{2}$* and *$( x_{1} , y_{1} ) = ( 1 , 5 )$
> 
> $y - 5 = - 1 \frac{1}{2} ( x - 1 )
> y - 5 = - 1 \frac{1}{2} x + 1 \frac{1}{2}$
> 
> > *Multiply both sides by 2 to get rid of the fractions*
> 
> > *Then rearrange into the required form *
> 
> $\begin{array}{rcl} 2 y - 10 & = - x + 1 \\ x + 2 y & = 11 \end{array}$
> 
> $x+2y=11$
