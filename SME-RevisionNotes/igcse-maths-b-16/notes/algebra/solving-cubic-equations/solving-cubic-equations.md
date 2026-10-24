---
note_id: "rn_cJZHNWZx7mKNfRYH"
title: "Solving Cubic Equations"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/algebra/solving-cubic-equations/solving-cubic-equations
path: algebra/solving-cubic-equations/solving-cubic-equations
updated_at: "2025-12-11T13:27:34.558Z"
spec_point_ids: ["spcpt_2btTTD747RgNBmbB"]
spec_point_codes: []
guided_study: false
---

# Solving Cubic Equations

## Solving Cubic Equations

> **Spec point** — `spcpt_2btTTD747RgNBmbB`

## Solving Cubic Equations

### How many real solutions can a cubic equation have?

- A **cubic equation **$ax^{3}+bx^{2}+cx+d=0$** **will **always** have either **one** or **three real roots** (or **solutions**)

  - Some of these roots may be **repeated**
  - So it is possible to have one, two, or three **unique** solutions
- A cubic with **three real roots** $α$, $β$ and $γ$ can be written as a product of three **linear factors**

  - $a x^{3} + b x^{2} + c x + d = ( x - \\alpha ) ( x - \\beta ) ( x - \\gamma )$
  
    - Any two of the factors could be multiplied together to give a **quadratic factor**
- A cubic with **one real root** $α$ can be written as the product of a **linear** and a **quadratic** factor

  - $a x^{3} + b x^{2} + c x + d = ( x - \\alpha ) ( p x^{2} + q x + r )$
  
    - The quadratic factor will **not** have any real roots
    - So its **discriminant **$q^{2}-4pr$ will be negative

### How do I solve cubic equations?

- Suppose you have a **cubic equation** $ax^{3}+bx^{2}+cx+d=0$
- An exam question will often **give** you one root

  - You may be asked to **show** that the root is a solution to the equation
  - Or you might have to **find** a root $x=α$* *by substituting values into the equation until it equals 0
  
    - Try small integer values ($1,-1,2,-2,...$)
- If you know a **root** then you know a **factor**

  - This is because of the **factor theorem**
  
    - If $x=α$ is a root, then $( x - \\alpha )$ is a factor
- You can then **divide** $ax^{3}+bx^{2}+cx+d$ by $( x - \\alpha )$ to find a **quadratic factor**

  - $a x^{3} + b x^{2} + c x + d = ( x - \\alpha ) ( p x^{2} + q x + r )$
  - Use **algebraic division**, or factorise by **inspection **or by **comparing coefficients**
- Then you can find any **other roots** by solving  $px^{2}+qx+r=0$

  - If that equation has no real solutions, then $x=α$ is the **only** real solution of the cubic

> **Exam Hint**
> - Solving cubic questions may also include a graph of the cubic function
> 
>   - Remember that roots correspond to *x*-intercepts on the graph

> **Worked Example**
> (a) Show that $x=2$ is a solution to the cubic equation $2x^{3}-x^{2}-8x+4=0$.
> 
> **Answer:**
> 
> > *Substitute *$x=2$* into the equation*
> 
> **Final answer:** $\begin{gathered} 2 ( 2 )^{3} - ( 2 )^{2} - 8 ( 2 ) + 4 & = 16 - 4 - 16 + 4 = 0 \end{gathered}$
> 
> **Therefore **$x=2$** is a solution**
> 
> (b) Find the other solutions to the equation.
> 
> **Answer:**
> 
> > *By the factor theorem, you know that *$( x - 2 )$* is a factor of *$2x^{3}-x^{2}-8x+4$* *
> 
> $\begin{gathered} 2 x^{3} - x^{2} - 8 x + 4 & = ( x - 2 ) ( p x^{2} + q x + r ) \end{gathered}$
> 
> > *You can find the values of *$p$*, *$q$* and *$r$* by comparing coefficients*
> 
> - *You might also be able to do this by inspection*
> 
>   - *or else you could use algebraic division*
> - *Start by expanding the brackets*
> 
> $\begin{gathered} 2 x^{3} - x^{2} - 8 x + 4 & = p x^{3} + ( q - 2 p ) x^{2} + ( r - 2 q ) x - 2 r \end{gathered}$
> 
> - *The *$x^{3}$* coefficient and constant term give you *$p$* and *$r$* right away*
> 
> $2x^{3}=px^{3}\Rightarrowp=2\,\,4=-2r\Rightarrowr=-2$
> 
> - *Use either the *$x^{2}$* or *$x$* coefficients to find the value of *$q$
> 
> > $- x^{2} = ( q - 2 p ) x^{2}$
> * *$\begin{array}{rcl} q - 2 p & = - 1 \\ q - 2 ( 2 ) & = - 1 \\ q - 4 & = - 1 \\ q = 3 \end{array}$
> 
> > *Now you can write the cubic in factorised form*
> 
> $( x - 2 ) ( 2 x^{2} + 3 x - 2 ) = 0$
> 
> > *To find the other solutions you need to solve  *$2x^{2}+3x-2=0$
> 
> - *Any quadratic solving method would work*
> - *But it is easiest here if you can spot the factorisation*
> 
> $( x - 2 ) ( x + 2 ) ( 2 x - 1 ) = 0$
> 
> - *So the other solutions are *
> 
>   - $x=-2$*,  from the factor *$( x + 2 )$
>   - $x=\frac{1}{2}$*,  from the factor *$( 2 x - 1 ) = 2 ( x - 1 \frac{1}{2} )$
> 
> $x=-2\mathrm{and}x=\frac{1}{2}$
