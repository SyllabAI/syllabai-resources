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

- `open parentheses 3 comma space 6 close parentheses` is a **fixed point** on the parabola $y^{2}=12x$
- `open parentheses 3 t squared comma space 6 t close parentheses` is a **general point** on the parabola $y^{2}=12x$

  - It is **algebraic**
  - but it still satisfies the **equation**
  - and it can **move **along the curve (depending on *t*)
- General points are formed from **parametric equations**

  - A general point on $y^{2}=4ax$ is `open parentheses a t squared comma space 2 a t close parentheses`
- You can have two or more** distinct** general points

  - `open parentheses 3 p squared comma space 6 p close parentheses`and `open parentheses 3 q squared comma space 6 q close parentheses` are general points *P*  and *Q * on $y^{2}=12x$

### How do I find the tangent or normal to a parabola at a general point?

- To find the** tangent** to the parabola $y^{2}=12x$ at the point `open parentheses 3 t squared comma space 6 t close parentheses`

  - use `y minus y subscript 1 equals m open parentheses x minus x subscript 1 close parentheses`
  - substitute in $x_{1}=3t^{2}$ and $y_{1}=6t$
  - find $m$ using **calculus** from $\frac{dy}{dx}$ at `open parentheses 3 t squared comma space 6 t close parentheses`
  
    - Make $y$ the subject of $y^{2}=12x$
    - $y=\sqrt{12x}=2\sqrt{3}x^{\frac{1}{2}}$
    - Ignore ±√ for now
    - $\frac{dy}{dx}=2\sqrt{3}\times\frac{1}{2}x^{-\frac{1}{2}}=\sqrt{\frac{3}{x}}$
    - At $x_{1}=3t^{2}$, $\frac{dy}{dx}=\sqrt{\frac{3}{3t^{2}}}=\frac{1}{t}$
  - The tangent is `y minus 6 t equals 1 over t open parentheses x minus 3 t squared close parentheses`
- The **normal **has a perpendicular gradient $-\frac{1}{m}$

  - `y minus 6 t equals negative t open parentheses x minus 3 t squared close parentheses`

## How do I use tangents and normals that pass through general points?

- All methods in **coordinate geometry** still work

  - However points of intersection will be **algebraic** in** **$t$
- Questions can involve **forming** and **solving** equations in $t$

> **Exam Hint**
> If you know **parametric** and** implicit** differentiation, they are also acceptable methods to find $\frac{dy}{dx}$.

> **Worked Example**
> The point $P$ with coordinates `open parentheses 4 t squared comma space 8 t close parentheses` lies on the parabola $y^{2}=16x$.
> 
> (a)  Use calculus to show that the equation of the normal at $P$ is  `y plus t x equals 4 t open parentheses t squared plus 2 close parentheses`
> 
> > *The normal at **P**   has the form *`y minus y subscript 1 equals m open parentheses x minus x subscript 1 close parentheses`*  *
> *Substitute in *$x_{1}=4t^{2}$* and *$y_{1}=8t$
> 
> `y minus 8 t equals m open parentheses x minus 4 t squared close parentheses`* *
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
> > `table row cell fraction numerator straight d y over denominator straight d x end fraction end cell equals cell 4 cross times 1 half x to the power of negative 1 half end exponent end cell row blank equals cell fraction numerator 2 over denominator square root of x end fraction end cell end table`
> * *
> 
> > *Then substitute in *$x_{1}=4t^{2}$
> 
> `table row cell fraction numerator straight d y over denominator straight d x end fraction end cell equals cell fraction numerator 2 over denominator square root of 4 t squared end root end fraction end cell row blank equals cell 1 over t end cell end table`
> 
> > *The negative reciprocal is *$-t$
> *Therefore the equation of the normal is*
> 
> `y minus 8 t equals negative t open parentheses x minus 4 t squared close parentheses`* *
> 
> > *Expand and rearrange*
> 
> `table row cell y minus 8 t end cell equals cell negative t x plus 4 t cubed end cell row y equals cell negative t x plus 4 t cubed plus 8 t end cell row cell y plus t x end cell equals cell 4 t cubed plus 8 t end cell end table`
> 
> > *Then factorise the right-hand side*
> 
> `y plus t x equals 4 t open parentheses t squared plus 2 close parentheses`
> 
> (b)  Hence find the coordinates of the three points on the parabola at which the normal passes through the point `open parentheses 9 comma space 0 close parentheses`.
> 
> > *The equation of the normal above must pass through the point *`open parentheses 9 comma space 0 close parentheses`
> *Substitute in *$x=9$* and *$y=0$
> 
> `0 plus 9 t equals 4 t open parentheses t squared plus 2 close parentheses`* *
> 
> > *This forms an equation in *$t$
> *Rearrange and solve*
> 
> `table row cell 9 t end cell equals cell 4 t cubed plus 8 t end cell row 0 equals cell 4 t cubed minus t end cell row 0 equals cell t open parentheses 4 t squared minus 1 close parentheses end cell row 0 equals cell t open parentheses 2 t minus 1 close parentheses open parentheses 2 t plus 1 close parentheses end cell end table`* *
> 
> $t=0,t=\frac{1}{2},t=-\frac{1}{2}$
> 
> > *The question asks for the coordinates of the points on the curve, **P**, *`open parentheses 4 t squared comma space 8 t close parentheses`
> *Substitute in the three values of *$t$
> 
> `open parentheses 0 comma space 0 close parentheses comma space space open parentheses 1 comma space 4 close parentheses comma space space open parentheses 1 comma space minus 4 close parentheses`
> 
> **It helps to imagine the situation visually (below) to check the answers make sense**
> 
> ![Normals to a general parabola](assets/725c03ed6d89-we-normals-to-a-general-parabola.png)

## Tangents & Normals to a Rectangular Hyperbola

> **Spec point** — `spcpt_jbZvcfGZ7qTzhXZh`

## Tangents & Normals to a Rectangular Hyperbola

### What is a general point on a rectangular hyperbola?

- `open parentheses 5 comma space 5 close parentheses` is a **fixed point** on the rectangular hyperbola $xy=25$
- `open parentheses 5 t comma space fraction numerator space 5 over denominator t end fraction close parentheses` is a **general point** on the rectangular hyperbola $xy=25$

  - It is **algebraic**
  - but it still satisfies the **equation**
  - and it can **move **along the curve (depending on $t$)
  
    - $t\neq0$
- General points are formed from **parametric equations**

  - A general point on $xy=c^{2}$ is `open parentheses c t comma space c over t close parentheses`
- You can have two or more** distinct** general points

  - `open parentheses 5 p comma space 5 over p close parentheses` and `open parentheses 5 q comma space 5 over q close parentheses` are general points *P*  and *Q*  on $xy=25$

### How do I find the tangent or normal to a rectangular hyperbola at a general point?

- To find the** tangent** to the rectangular hyperbola $xy=25$ at the point `open parentheses 5 t comma space 5 over t close parentheses`

  - use `y minus y subscript 1 equals m open parentheses x minus x subscript 1 close parentheses`
  - substitute in $x_{1}=5t$ and $y_{1}=\frac{5}{t}$
  - find $m$ using **calculus** from $\frac{dy}{dx}$ at `open parentheses 5 t comma space 5 over t close parentheses`
  
    - Make $y$ the subject of $xy=25$
    - $y=\frac{25}{x}=25x^{-1}$
    - `fraction numerator straight d y over denominator straight d x end fraction equals 25 cross times open parentheses negative 1 close parentheses x to the power of negative 2 end exponent equals negative 25 over x squared`
    - At $x_{1}=5t$, `fraction numerator straight d y over denominator straight d x end fraction equals negative 25 over open parentheses 5 t close parentheses squared equals negative 1 over t squared`
  - The tangent is `y minus 5 over t equals negative 1 over t squared open parentheses x minus 5 t close parentheses`
- The **normal **has a perpendicular gradient $-\frac{1}{m}$

  - `y minus 5 over t equals t squared open parentheses x minus 5 t close parentheses`

### How do I use tangents and normals that pass through general points?

- All methods in **coordinate geometry** still work

  - However points of intersection will be **algebraic** in** **$t$
- Questions can involve **forming** and **solving** equations in $t$

> **Exam Hint**
> If you know **parametric** and** implicit** differentiation, they are also acceptable methods to find $\frac{dy}{dx}$.

> **Worked Example**
> The point $P$ with coordinates `open parentheses 2 p comma space 2 over p close parentheses` and the point $Q$ with coordinates `open parentheses 2 q comma space 2 over q close parentheses` lie on the rectangular hyperbola $xy=4$, where $p\neq\pmq$.
> 
> (a)  Use calculus to show that the equation of the tangent to the curve at $P$ is  $p^{2}y=-x+4p$.
> 
> > *The tangent at **P ** has the form *`y minus y subscript 1 equals m open parentheses x minus x subscript 1 close parentheses`*  *
> *Substitute in *$x_{1}=2p$* and *$y_{1}=\frac{2}{p}$
> 
> `y minus 2 over p equals m open parentheses x minus 2 p close parentheses`
> 
> > *Find the gradient of the tangent, for example, first make **y**  the subject of the curve*
> 
> $y=\frac{4}{x}=4x^{-1}$
> 
> > *Then differentiate*
> 
> `table row cell fraction numerator straight d y over denominator straight d x end fraction end cell equals cell negative 4 x to the power of negative 2 end exponent end cell row blank equals cell negative 4 over x squared end cell end table`
> 
> > *Then substitute in *$x_{1}=2p$* and simplify*
> 
> `table row cell fraction numerator straight d y over denominator straight d x end fraction end cell equals cell negative 4 over open parentheses 2 p close parentheses squared end cell row blank equals cell negative fraction numerator 4 over denominator 4 p squared end fraction end cell row blank equals cell negative 1 over p squared end cell end table`
> 
> > *Therefore the equation of the tangent is*
> 
> `y minus 2 over p equals negative 1 over p squared open parentheses x minus 2 p close parentheses`
> 
> > *Multiply both sides by *$p^{2}$* then rearrange*
> 
> `table row cell p squared y minus 2 p end cell equals cell negative open parentheses x minus 2 p close parentheses end cell row cell p squared y minus 2 p end cell equals cell negative x plus 2 p end cell end table`
> 
> > *Make *$p^{2}y$* the subject*
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
> > *Make *$y$* the subject of each tangent and set them equal to each other*
> 
> $\frac{-x+4p}{p^{2}}=\frac{-x+4q}{q^{2}}$
> 
> > *Cross-multiply and expand*
> 
> `table row cell q squared open parentheses negative x plus 4 p close parentheses end cell equals cell p squared open parentheses negative x plus 4 q close parentheses end cell row cell negative q squared x plus 4 p q squared end cell equals cell negative p squared x plus 4 p squared q end cell end table`* *
> 
> > *Bring the *$x$*  terms to one side and factorise*
> 
> `p squared x minus q squared x equals 4 p squared q minus 4 p q squared
> open parentheses p squared minus q squared close parentheses x equals 4 p q open parentheses p minus q close parentheses`
> 
> > *Make *$x$*  the subject and use the difference of two squares*
> 
> `table row x equals cell fraction numerator 4 p q open parentheses p minus q close parentheses over denominator p squared minus q squared end fraction end cell row x equals cell fraction numerator 4 p q open parentheses p minus q close parentheses over denominator open parentheses p minus q close parentheses open parentheses p plus q close parentheses end fraction end cell end table`
> 
> > *As *$p\neq\pmq$*, the brackets will never be zero*
> *This means the *`open parentheses p minus q close parentheses`* bracket can be cancelled, giving the final answer*
> 
> $x=\frac{4pq}{p+q}$
> 
> **Note: if **$p=q$** then point ****P****  is the same as point ****Q**
> **Also, if **$p=-q$**, then the tangents at ****P  ****and ****Q****  are parallel**
