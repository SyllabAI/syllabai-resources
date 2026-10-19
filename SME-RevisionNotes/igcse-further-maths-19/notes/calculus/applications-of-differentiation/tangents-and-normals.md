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

  - The **gradient** of the **tangent** to the function `y equals straight f open parentheses x close parentheses` at the point $(x_{1},y_{1})$ is $f^{'}(x_{1})$
- Therefore to find the **equation** of the **tangent** to the function $y=f(x)$ at the point $(x_{1},y_{1})$

  - Find  `straight f to the power of apostrophe open parentheses x close parentheses`
  - Substitute $x_{1}$ into `straight f apostrophe open parentheses x close parentheses` to find the gradient `straight f to the power of apostrophe open parentheses x subscript 1 close parentheses`,
  - Use the  `y minus y subscript 1 equals m open parentheses x minus x subscript 1 close parentheses` form of the line equation
  
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
  - Therefore the **gradient** of the **normal** to the function `y equals straight f open parentheses x close parentheses` at the point $(x_{1},y_{1})$ is $-\frac{1}{f^{'}(x_{1})}$
- To find the **equation** of the **normal** to the function $y=f(x)$ at the point $(x_{1},y_{1})$

  - Find  `straight f to the power of apostrophe open parentheses x close parentheses`
  - Substitute $x_{1}$ into `straight f apostrophe open parentheses x close parentheses` to find the gradient of the tangent `straight f to the power of apostrophe open parentheses x subscript 1 close parentheses`
  - Use that to find the gradient of the normal `negative fraction numerator 1 over denominator straight f to the power of apostrophe open parentheses x subscript 1 close parentheses end fraction`
  - Use the  `y minus y subscript 1 equals m open parentheses x minus x subscript 1 close parentheses` form of the line equation
  
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
> > *Substitute *$x=1$* into *`straight f open parentheses x close parentheses`* to find the *$y$*-coordinate of the point *
> 
> `straight f open parentheses 1 close parentheses equals 2 open parentheses 1 close parentheses to the power of 4 plus 3 over open parentheses 1 close parentheses squared equals 2 plus 3 equals 5`
> 
> > *So the point in question is *`open parentheses 1 comma space 5 close parentheses`
> 
> > *Now differentiate to find *`straight f to the power of apostrophe open parentheses x close parentheses`*, first using laws of indices to rewrite *$\frac{3}{x^{2}}$* as *$3x^{-2}$
> 
> `straight f open parentheses x close parentheses equals 2 x to the power of 4 plus 3 x to the power of negative 2 end exponent`
> 
> `table row cell straight f to the power of apostrophe open parentheses x close parentheses end cell equals cell 2 open parentheses 4 x to the power of 4 minus 3 end exponent close parentheses plus 3 open parentheses negative 2 x to the power of negative 2 minus 1 end exponent close parentheses end cell row blank equals cell 8 x cubed minus 6 x to the power of negative 3 end exponent end cell row blank equals cell 8 x cubed minus 6 over x cubed end cell end table`
> 
> > *Substitute *$x=1$* into *`straight f to the power of apostrophe open parentheses x close parentheses`* to find the gradient of the tangent at the point*
> 
> `straight f to the power of apostrophe open parentheses 1 close parentheses equals 8 open parentheses 1 close parentheses cubed minus 6 over open parentheses 1 close parentheses cubed equals 8 minus 6 equals 2`
> 
> > *Now use  *`y minus y subscript 1 equals m open parentheses x minus x subscript 1 close parentheses`*  to find the equation of the line*
> 
> > *Here *$m=2$* and *`open parentheses x subscript 1 comma space y subscript 1 close parentheses equals open parentheses 1 comma space 5 close parentheses`
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row cell y minus 5 end cell equals cell 2 open parentheses x minus 1 close parentheses end cell row cell y minus 5 end cell equals cell 2 x minus 2 end cell row y equals cell 2 x plus 3 end cell end table`
> 
> $y=2x+3$
> 
> b) Find an equation for the normal to the curve `y equals straight f open parentheses x close parentheses` at the point where $x=1$, giving your answer in the form $ax+by=c$, where $a$, $b$ and $c$ are integers.
> 
> > *The normal and tangent are perpendicular*
> 
> > *So the gradient of the normal will be  *`negative fraction numerator 1 over denominator straight f to the power of apostrophe open parentheses 1 close parentheses end fraction`
> 
> `negative fraction numerator 1 over denominator straight f to the power of apostrophe open parentheses 1 close parentheses end fraction equals negative 1 half`
> 
> > *Now use  *`y minus y subscript 1 equals m open parentheses x minus x subscript 1 close parentheses`*  to find the equation of the line*
> 
> > *Here *$m=-\frac{1}{2}$* and *`open parentheses x subscript 1 comma space y subscript 1 close parentheses equals open parentheses 1 comma space 5 close parentheses`
> 
> `y minus 5 equals negative 1 half open parentheses x minus 1 close parentheses
> y minus 5 equals negative 1 half x plus 1 half`
> 
> > *Multiply both sides by 2 to get rid of the fractions*
> 
> > *Then rearrange into the required form *
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row cell 2 y minus 10 end cell equals cell negative x plus 1 end cell row cell x plus 2 y end cell equals 11 end table`
> 
> $x+2y=11$
