---
note_id: "rn_qrkKrVGt8HxcNpds"
title: "Tangents & Normals"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/coordinate-systems/coordinate-systems/tangents-and-normals
path: coordinate-systems/coordinate-systems/tangents-and-normals
updated_at: "2024-04-10T08:40:08.093Z"
spec_point_ids: ["spcpt_NfbRPQ3SV5hfMXG5", "spcpt_jbZvcfGZ7qTzhXZh"]
spec_point_codes: []
guided_study: false
---

# Tangents & Normals

## Tangents & Normals to a Parabola

> **Spec point** — `spcpt_NfbRPQ3SV5hfMXG5`

## Tangents & Normals to a Parabola

### What is a general point on a parabola?

- $( 3 , 6 )$ is a **fixed point** on the parabola $y^{2}=12x$
- $( 3 t^{2} , 6 t )$ is a **general point** on the parabola $y^{2}=12x$

  - It is **algebraic**
  - but it still satisfies the **equation**
  - and it can **move **along the curve (depending on *t*)
- General points are formed from **parametric equations**

  - A general point on $y^{2}=4ax$ is $( a t^{2} , 2 a t )$
- You can have two or more** distinct** general points

  - $( 3 p^{2} , 6 p )$and $( 3 q^{2} , 6 q )$ are general points *P*  and *Q* on $y^{2}=12x$

### How do I find the tangent or normal to a parabola at a general point?

- To find the** tangent** to the parabola $y^{2}=12x$ at the point $( 3 t^{2} , 6 t )$

  - use $y - y_{1} = m ( x - x_{1} )$
  - substitute in $x_{1}=3t^{2}$ and $y_{1}=6t$
  - find $m$ using **calculus** from $\frac{dy}{dx}$ at $( 3 t^{2} , 6 t )$
  
    - Make $y$ the subject of $y^{2}=12x$
    - $y=\sqrt{12x}=2\sqrt{3}x^{\frac{1}{2}}$
    - Ignore ±√ for now
    - $\frac{dy}{dx}=2\sqrt{3}\times\frac{1}{2}x^{-\frac{1}{2}}=\sqrt{\frac{3}{x}}$
    - At $x_{1}=3t^{2}$, $\frac{dy}{dx}=\sqrt{\frac{3}{3t^{2}}}=\frac{1}{t}$
  - The tangent is $y - 6 t = \frac{1}{t} ( x - 3 t^{2} )$
- The **normal **has a perpendicular gradient $-\frac{1}{m}$

  - $y - 6 t = - t ( x - 3 t^{2} )$

## How do I use tangents and normals that pass through general points?

- All methods in **coordinate geometry** still work

  - However points of intersection will be **algebraic** in** **$t$
- Questions can involve **forming** and **solving** equations in $t$

> **Exam Hint**
> If you know **parametric** and** implicit** differentiation, they are also acceptable methods to find $\frac{dy}{dx}$.

> **Worked Example**
> The point $P$ with coordinates $( 4 t^{2} , 8 t )$ lies on the parabola $y^{2}=16x$.
> 
> (a)  Use calculus to show that the equation of the normal at $P$ is  $y + t x = 4 t ( t^{2} + 2 )$
> 
> > *The normal at **P**   has the form *$y - y_{1} = m ( x - x_{1} )$*  *
> *Substitute in* $x_{1}=4t^{2}$ *and* $y_{1}=8t$
> 
> $y - 8 t = m ( x - 4 t^{2} )$* *
> 
> > *The gradient of the normal is the negative reciprocal of the gradient of the tangent*
> *Find the gradient of the tangent*
> *For example first make **y**  the subject of the curve*
> *(Use the positive square root)*
> 
> > $y=\sqrt{16x}=4x^{\frac{1}{2}}$* *
> 
> > *Then differentiate*
> 
> > $\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = 4 \times 1 \frac{1}{2} x^{- 1 \frac{1}{2}} \\ = \frac{2}{ \sqrt{x} } \end{gathered}$
> * *
> 
> > *Then substitute in* $x_{1}=4t^{2}$
> 
> $\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = \frac{2}{ \sqrt{4 t^{2}} } \\ = \frac{1}{t} \end{gathered}$
> 
> > *The negative reciprocal is* $-t$
> *Therefore the equation of the normal is*
> 
> $y - 8 t = - t ( x - 4 t^{2} )$* *
> 
> > *Expand and rearrange*
> 
> $\begin{gathered} y - 8 t & = - t x + 4 t^{3} \\ y = - t x + 4 t^{3} + 8 t \\ y + t x & = 4 t^{3} + 8 t \end{gathered}$
> 
> > *Then factorise the right-hand side*
> 
> $y + t x = 4 t ( t^{2} + 2 )$
> 
> (b)  Hence find the coordinates of the three points on the parabola at which the normal passes through the point $( 9 , 0 )$.
> 
> > *The equation of the normal above must pass through the point* $( 9 , 0 )$
> *Substitute in* $x=9$ *and* $y=0$
> 
> $0 + 9 t = 4 t ( t^{2} + 2 )$* *
> 
> > *This forms an equation in* $t$
> *Rearrange and solve*
> 
> $\begin{gathered} 9 t & = 4 t^{3} + 8 t \\ 0 = 4 t^{3} - t \\ 0 = t ( 4 t^{2} - 1 ) \\ 0 = t ( 2 t - 1 ) ( 2 t + 1 ) \end{gathered}$* *
> 
> $t=0,t=\frac{1}{2},t=-\frac{1}{2}$
> 
> > *The question asks for the coordinates of the points on the curve, **P**, *$( 4 t^{2} , 8 t )$
> *Substitute in the three values of* $t$
> 
> $( 0 , 0 ) , ( 1 , 4 ) , ( 1 , - 4 )$
> 
> **It helps to imagine the situation visually (below) to check the answers make sense**
> 
> ![Normals to a general parabola](assets/725c03ed6d89-we-normals-to-a-general-parabola.png)

## Tangents & Normals to a Rectangular Hyperbola

> **Spec point** — `spcpt_jbZvcfGZ7qTzhXZh`

## Tangents & Normals to a Rectangular Hyperbola

### What is a general point on a rectangular hyperbola?

- $( 5 , 5 )$ is a **fixed point** on the rectangular hyperbola $xy=25$
- $( 5 t , \frac{ 5}{t} )$ is a **general point** on the rectangular hyperbola $xy=25$

  - It is **algebraic**
  - but it still satisfies the **equation**
  - and it can **move **along the curve (depending on $t$)
  
    - $t\neq0$
- General points are formed from **parametric equations**

  - A general point on $xy=c^{2}$ is $( c t , \frac{c}{t} )$
- You can have two or more** distinct** general points

  - $( 5 p , \frac{5}{p} )$ and $( 5 q , \frac{5}{q} )$ are general points *P*  and *Q*  on $xy=25$

### How do I find the tangent or normal to a rectangular hyperbola at a general point?

- To find the** tangent** to the rectangular hyperbola $xy=25$ at the point $( 5 t , \frac{5}{t} )$

  - use $y - y_{1} = m ( x - x_{1} )$
  - substitute in $x_{1}=5t$ and $y_{1}=\frac{5}{t}$
  - find $m$ using **calculus** from $\frac{dy}{dx}$ at $( 5 t , \frac{5}{t} )$
  
    - Make $y$ the subject of $xy=25$
    - $y=\frac{25}{x}=25x^{-1}$
    - $\frac{ \mathrm{d} y}{ \mathrm{d} x} = 25 \times ( - 1 ) x^{- 2} = - \frac{25}{x^{2}}$
    - At $x_{1}=5t$, $\frac{ \mathrm{d} y}{ \mathrm{d} x} = - \frac{25}{( 5 t )^{2}} = - \frac{1}{t^{2}}$
  - The tangent is $y - \frac{5}{t} = - \frac{1}{t^{2}} ( x - 5 t )$
- The **normal **has a perpendicular gradient $-\frac{1}{m}$

  - $y - \frac{5}{t} = t^{2} ( x - 5 t )$

### How do I use tangents and normals that pass through general points?

- All methods in **coordinate geometry** still work

  - However points of intersection will be **algebraic** in** **$t$
- Questions can involve **forming** and **solving** equations in $t$

> **Exam Hint**
> If you know **parametric** and** implicit** differentiation, they are also acceptable methods to find $\frac{dy}{dx}$.

> **Worked Example**
> The point $P$ with coordinates $( 2 p , \frac{2}{p} )$ and the point $Q$ with coordinates $( 2 q , \frac{2}{q} )$ lie on the rectangular hyperbola $xy=4$, where $p\neq\pmq$.
> 
> (a)  Use calculus to show that the equation of the tangent to the curve at $P$ is  $p^{2}y=-x+4p$.
> 
> > *The tangent at **P ** has the form *$y - y_{1} = m ( x - x_{1} )$*  *
> *Substitute in* $x_{1}=2p$ *and* $y_{1}=\frac{2}{p}$
> 
> $y - \frac{2}{p} = m ( x - 2 p )$
> 
> > *Find the gradient of the tangent, for example, first make **y**  the subject of the curve*
> 
> $y=\frac{4}{x}=4x^{-1}$
> 
> > *Then differentiate*
> 
> $\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = - 4 x^{- 2} \\ = - \frac{4}{x^{2}} \end{gathered}$
> 
> > *Then substitute in* $x_{1}=2p$ *and simplify*
> 
> $\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = - \frac{4}{( 2 p )^{2}} \\ = - \frac{4}{4 p^{2}} \\ = - \frac{1}{p^{2}} \end{gathered}$
> 
> > *Therefore the equation of the tangent is*
> 
> $y - \frac{2}{p} = - \frac{1}{p^{2}} ( x - 2 p )$
> 
> > *Multiply both sides by* $p^{2}$ *then rearrange*
> 
> $\begin{gathered} p^{2} y - 2 p & = - ( x - 2 p ) \\ p^{2} y - 2 p & = - x + 2 p \end{gathered}$
> 
> > *Make* $p^{2}y$ *the subject*
> 
> $p^{2}y=-x+4p$
> 
> (b)  Hence find the $x$-coordinate of the point of intersection between the tangent at $P$ and the tangent at $Q$, giving your answer in fully simplified form.
> 
> > *Finding the tangent at** Q**  requires the exact same steps as above, but with *$q$*  **instead of *$p$
> *You can therefore write down the tangent at **Q  **with no working*
> 
> $q^{2}y=-x+4q$
> 
> > *The tangent at **P**  intersects the tangent at **Q** *
> 
> ![Tangents to a rectangular hyperbola intersecting each other](assets/5b85e264102c-we-tangents-to-a-general-rectangular-hyperbola.png)
> 
> > *Make* $y$ *the subject of each tangent and set them equal to each other*
> 
> $\frac{-x+4p}{p^{2}}=\frac{-x+4q}{q^{2}}$
> 
> > *Cross-multiply and expand*
> 
> $\begin{gathered} q^{2} ( - x + 4 p ) & = p^{2} ( - x + 4 q ) \\ - q^{2} x + 4 p q^{2} & = - p^{2} x + 4 p^{2} q \end{gathered}$* *
> 
> > *Bring the* $x$ *terms to one side and factorise*
> 
> $p^{2} x - q^{2} x = 4 p^{2} q - 4 p q^{2}
> ( p^{2} - q^{2} ) x = 4 p q ( p - q )$
> 
> > *Make* $x$ *the subject and use the difference of two squares*
> 
> $\begin{gathered} x = \frac{4 p q ( p - q )}{p^{2} - q^{2}} \\ x = \frac{4 p q ( p - q )}{( p - q ) ( p + q )} \end{gathered}$
> 
> > *As* $p\neq\pmq$*, the brackets will never be zero*
> *This means the* $( p - q )$ *bracket can be cancelled, giving the final answer*
> 
> $x=\frac{4pq}{p+q}$
> 
> **Note: if **$p=q$** then point ****P****  is the same as point ****Q**
> **Also, if **$p=-q$**, then the tangents at ****P  ****and ****Q****  are parallel**
