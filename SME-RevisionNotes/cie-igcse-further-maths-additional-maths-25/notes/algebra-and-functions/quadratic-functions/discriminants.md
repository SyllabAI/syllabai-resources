---
note_id: "rn_b77xQnhSDm5kc4pg"
title: "Discriminants"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/algebra-and-functions/quadratic-functions/discriminants
path: algebra-and-functions/quadratic-functions/discriminants
updated_at: "2026-07-02T08:19:38.503Z"
spec_point_ids: ["spcpt_NvHCD8kCbVz7tb7N", "spcpt_cWq7d2hrR4fZkxtW"]
spec_point_codes: []
guided_study: false
---

# Discriminants

## Discriminants

> **Spec point** — `spcpt_NvHCD8kCbVz7tb7N`

## Discriminants

### What is a discriminant?

- The **discriminant** is the part of the quadratic formula that is **under the square root** sign
- It is $b^{2}-4ac$

  - The **quadratic formula,** in full, is

$x=\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}$

where the quadratic equation is written in the form

$ax^{2}+bx+c=0$

- It is sometimes denoted by the Greek letter $Δ$ (capital delta)

> **Worked Example**
> Find, in terms of the constant $k$, the discriminant of the quadratic equation $3x^{2}+2kx-k=kx^{2}-4kx+2$.
> 
> > *First write the quadratic equation in the form *$ax^{2}+bx+c=0$*.*
> 
> `table row cell 3 x squared minus k x squared plus 2 k x plus 4 k x minus k minus 2 end cell equals 0 row cell open parentheses 3 minus k close parentheses x squared plus 6 k x minus open parentheses k plus 2 close parentheses end cell equals 0 end table`
> 
> > *It can be easier/clearer to pick out *$a,b$* and *$c$* first, before finding the discriminant.*
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row a equals cell 3 minus k end cell row b equals cell 6 k end cell row c equals cell negative open parentheses k plus 2 close parentheses end cell end table`
> 
> > *The discriminant is *$b^{2}-4ac$*.*
> 
> `table row increment equals cell open parentheses 6 k close parentheses squared minus 4 cross times open parentheses 3 minus k close parentheses cross times negative open parentheses k plus 2 close parentheses end cell row increment equals cell 36 k squared plus 4 open parentheses 6 plus k minus k squared close parentheses space end cell end table`
> 
> $\Delta=32k^{2}+4k+24$

## Applications of Discriminant

> **Spec point** — `spcpt_cWq7d2hrR4fZkxtW`

## Applications of discriminant

### How does the value of the discriminant affect roots?

- There are three options for the outcome of the discriminant:

  - If $b^{2}-4ac>0$ the square root part of the quadratic formula can be calculated leading to two solutions (values of $x$)
  
    - i.e. **two** different **real roots**
  - If  $b^{2}-4ac=0$ the square root part of the quadratic formula will be zero leading to one solution
  
    - i.e. **one repeated** root or **two equal roots**
  - If  $b^{2}-4ac<0$ the square root part of the quadratic formula cannot be calculated leading to no solutions
  
    - i.e.** no (real) roots**

### How do I sketch quadratic graphs using the discriminant?

- If $b^{2}-4ac>0$ the quadratic equation has **two** different real **roots**

  - The graph of the quadratic will **intersect** the $x$-axis **twice** (at the roots)
- If  $b^{2}-4ac=0$ the quadratic equation has two equal roots **(one root)**

  - The graph of the quadratic will **intersect** (touch) the $x$-axis **once** (at the root)
- If  $b^{2}-4ac<0$ the quadratic equation has **no** (real) **roots**

  - The graph of the quadratic will **not intercept** the $x$-axis

![The discriminant determines how many roots a quadratic graph has](../../../assets/74e5af0fc89b-2-2-2-discrimamts-notes-diagram-2.png)

### How do I use the discriminant to find the number of intersections between a line and a curve?

- For the graphs of two functions, `y equals straight f open parentheses x close parentheses` and `y equals straight g open parentheses x close parentheses` where

  - `straight f open parentheses x close parentheses` is **quadratic**
  - `straight g open parentheses x close parentheses` is **linear**

the number of intersections between the graphs can be found using the discriminant.

- **STEP 1**

  - Set `straight f open parentheses x close parentheses equals straight g open parentheses x close parentheses`
- **STEP 2**

  - Rearrange into the form `straight h open parentheses x close parentheses equals 0` such that `straight h open parentheses x close parentheses` is in the quadratic form $ax^{2}+bx+c=0$
- **STEP 3**

  - Find the **discriminant** and thus determine the **number** of **intersections** between the graphs of `y equals straight f open parentheses x close parentheses`and `y equals straight g open parentheses x close parentheses`
  
    - if $b^{2}-4ac>0$ (two real roots) the graphs **intersect twice**
    - if $b^{2}-4ac=0$ (equal roots) the graphs **intersect once**
    - this means the line (`straight g open parentheses x close parentheses`) is a *tangent* to the curve (`straight f open parentheses x close parentheses`)
    - if $b^{2}-4ac<0$ (no real roots) the graphs **do not intersect**

![The possible intersections between a line and a quadratic](../../../assets/b463f361330f-discriminants-and-lines-and-quadratics.png)

> **Worked Example**
> Show that the line with equation $y=3x-7$ is tangent to the curve with equation `y equals open parentheses x plus 3 close parentheses open parentheses x minus 2 close parentheses`.
> 
> > *STEP 1 - set the equations of the line and curve equal to each other.*
> 
> `3 x minus 7 equals open parentheses x plus 3 close parentheses open parentheses x minus 2 close parentheses`
> 
> > *STEP 2 - rearrange to quadratic form.*
> 
> `table row cell 3 x minus 7 end cell equals cell x squared plus x minus 6 end cell row cell x squared minus 2 x plus 1 end cell equals 0 end table`
> 
> > *STEP 3 - find the discriminant and interpret its value.*
> 
> `increment equals open parentheses negative 2 close parentheses squared minus 4 open parentheses 1 close parentheses open parentheses 1 close parentheses equals 0`
> 
> **Final answer:** **Since the discriminant is zero, the line and the curve intersect at one point only. Therefore the line is a tangent to the curve.**
