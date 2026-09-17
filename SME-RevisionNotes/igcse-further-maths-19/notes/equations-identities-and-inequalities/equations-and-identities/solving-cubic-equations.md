---
note_id: "rn_cJZHNWZx7mKNfRYH"
title: "Solving Cubic Equations"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/equations-identities-and-inequalities/equations-and-identities/solving-cubic-equations
path: equations-identities-and-inequalities/equations-and-identities/solving-cubic-equations
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

  - `a x cubed plus b x squared plus c x plus d equals open parentheses x minus alpha close parentheses open parentheses x minus beta close parentheses open parentheses x minus gamma close parentheses`
  
    - Any two of the factors could be multiplied together to give a **quadratic factor**
- A cubic with **one real root** $α$ can be written as the product of a **linear** and a **quadratic** factor

  - `a x cubed plus b x squared plus c x plus d equals open parentheses x minus alpha close parentheses open parentheses p x squared plus q x plus r close parentheses`
  
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
  
    - If $x=α$ is a root, then `open parentheses x minus alpha close parentheses` is a factor
- You can then **divide** $ax^{3}+bx^{2}+cx+d$ by `open parentheses x minus alpha close parentheses` to find a **quadratic factor**

  - `a x cubed plus b x squared plus c x plus d equals open parentheses x minus alpha close parentheses open parentheses p x squared plus q x plus r close parentheses`
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
> **Final answer:** `table row cell 2 open parentheses 2 close parentheses cubed minus open parentheses 2 close parentheses squared minus 8 open parentheses 2 close parentheses plus 4 end cell equals cell 16 minus 4 minus 16 plus 4 equals 0 end cell end table`
> 
> **Therefore **$x=2$** is a solution**
> 
> (b) Find the other solutions to the equation.
> 
> **Answer:**
> 
> > *By the factor theorem, you know that *`open parentheses x minus 2 close parentheses`* is a factor of *$2x^{3}-x^{2}-8x+4$* *
> 
> `table row cell 2 x cubed minus x squared minus 8 x plus 4 end cell equals cell open parentheses x minus 2 close parentheses open parentheses p x squared plus q x plus r close parentheses end cell end table`
> 
> > *You can find the values of *$p$*, *$q$* and *$r$* by comparing coefficients*
> 
> - *You might also be able to do this by inspection*
> 
>   - *or else you could use algebraic division*
> - *Start by expanding the brackets*
> 
> `table row cell 2 x cubed minus x squared minus 8 x plus 4 end cell equals cell p x cubed plus open parentheses q minus 2 p close parentheses x squared plus open parentheses r minus 2 q close parentheses x minus 2 r end cell end table`
> 
> - *The *$x^{3}$* coefficient and constant term give you *$p$* and *$r$* right away*
> 
> $2x^{3}=px^{3}\Rightarrowp=2\,\,4=-2r\Rightarrowr=-2$
> 
> - *Use either the *$x^{2}$* or *$x$* coefficients to find the value of *$q$
> 
> > `negative x squared equals open parentheses q minus 2 p close parentheses x squared`
> * *`table attributes columnalign right center left columnspacing 0px end attributes row cell q minus 2 p end cell equals cell negative 1 end cell row cell q minus 2 open parentheses 2 close parentheses end cell equals cell negative 1 end cell row cell q minus 4 end cell equals cell negative 1 end cell row q equals 3 end table`
> 
> > *Now you can write the cubic in factorised form*
> 
> `open parentheses x minus 2 close parentheses open parentheses 2 x squared plus 3 x minus 2 close parentheses equals 0`
> 
> > *To find the other solutions you need to solve  *$2x^{2}+3x-2=0$
> 
> - *Any quadratic solving method would work*
> - *But it is easiest here if you can spot the factorisation*
> 
> `open parentheses x minus 2 close parentheses open parentheses x plus 2 close parentheses open parentheses 2 x minus 1 close parentheses equals 0`
> 
> - *So the other solutions are *
> 
>   - $x=-2$*,  from the factor *`open parentheses x plus 2 close parentheses`
>   - $x=\frac{1}{2}$*,  from the factor *`open parentheses 2 x minus 1 close parentheses equals 2 open parentheses x minus 1 half close parentheses`
> 
> $x=-2\mathrm{and}x=\frac{1}{2}$
