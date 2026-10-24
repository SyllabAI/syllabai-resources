---
note_id: "rn_bMf2GZb3JfjBRYPD"
title: "Equating Real & Imaginary Parts"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/complex-numbers/operations-with-complex-numbers/equating-real-and-imaginary-parts
path: complex-numbers/operations-with-complex-numbers/equating-real-and-imaginary-parts
updated_at: "2024-04-10T08:25:42.973Z"
spec_point_ids: ["spcpt_t53s6pXwMkTNqYjz"]
spec_point_codes: []
guided_study: false
---

# Equating Real & Imaginary Parts

## Equating Real & Imaginary Parts

> **Spec point** — `spcpt_t53s6pXwMkTNqYjz`

## Equating Real & Imaginary Parts

### How do I equate real and imaginary parts?

- If two complex expressions are** equal**, then

  - their **real **parts are **equal**
  - and their **imaginary **parts are **equal**
- If $a+bi=8-10i$ where $a$ and $b$ are real

  - then $a=8$ (equating real parts)
  - and $b=-10$ (equating imaginary parts)

### How do I solve equations using real and imaginary parts?

- **Introduce** $z=x+yi$ for expressions in $z$
- For example, solve $z+2z\ast=12-i$

  - Let $z=x+yi$
  - **Substitute** in
  
    - $( x + y \mathrm{i} ) + 2 ( x - y \mathrm{i} ) = 12 - i$
  - **Expand **and **collect **terms
  
    - $3x-yi=12-i$
  - **Equate real** and** imaginary **parts
  
    - $3x=12$ gives $x=4$
    - $-y=-1$ gives $y=1$
  - **Substitute back** into $z$
  
    - $z=4+i$

### How do I use real and imaginary parts with modulus signs?

- If $z=x+yi$ then $\vert z \vert = \sqrt{x^{2} + y^{2}}$
- Helpful** modulus rules **are:

  - $\vert z_{1} z_{2} \vert = \vert z_{1} \vert \vert z_{2} \vert$
  - `| z _ 1 / z _ 2 | = (| z _ 1 |)/(| z _ 2 |)`
  - $\vert z \vert = \vert z \text{asterisk} \times \vert$
  - $z z \text{asterisk} \times = z \text{asterisk} \times z = \vert z \vert^{2}$
  
    - Proved using $z=x+yi$ and $z\ast=x-yi$
- For example, find $p$ if $z_{1}=p+pi$, $z_{2}=2i$ and $\vert z_{1} z_{2} \vert = 6 \sqrt{2}$

  - Use $\vert z_{1} z_{2} \vert = \vert z_{1} \vert \vert z_{2} \vert$
  
    - $\vert p + p \mathrm{i} \vert \vert 2 \mathrm{i} \vert = 6 \sqrt{2}$
  - Use $\vert z \vert = \sqrt{x^{2} + y^{2}}$
  
    - $\sqrt{p^{2}+p^{2}}\times2=6\sqrt{2}$ so $2\sqrt{2p^{2}}=6\sqrt{2}$
  - **Square both sides** and simplify
  
    - $p^{2}=9$
    - $p=\pm3$

> **Exam Hint**
> Harder exam questions may not tell you to write $z$ as $x+yi$ (you have to spot it yourself).

> **Worked Example**
> Let $z$ and $w$ be complex numbers.
> It is known that $w=5+2i$ and that $z^{2}+10w=zz\ast$.
> 
> Find the two possible values of $z$.
> 
> > *Write *$z$* ** in the form *$x+yi$
> 
> $z=x+yi$
> 
> > *Substitute this, and *$w$*, into the equation*
> 
> * *$( x + y \mathrm{i} )^{2} + 10 ( 5 + 2 \mathrm{i} ) = ( x + y \mathrm{i} ) ( x - y \mathrm{i} )$
> 
> > *Expand the brackets and use *$i^{2}=-1$
> 
> $x^{2}+2xyi+y^{2}i^{2}+50+20i=x^{2}-y^{2}i^{2}\,x^{2}+2xyi-y^{2}+50+20i=x^{2}+y^{2}$
> 
> > *Equate the real parts and solve for *$y$
> 
> $\begin{gathered} x^{2} - y^{2} + 50 & = x^{2} + y^{2} \\ 50 = 2 y^{2} \\ 25 = y^{2} \\ y = \pm 5 \end{gathered}$
> 
> > *Now equate the imaginary parts and solve for *$x$
> *Note that there are no imaginary parts on the right*
> 
> $\begin{gathered} 2 x y + 20 & = 0 \\ x y & = - 10 \\ x = - \frac{10}{y} \end{gathered}$
> 
> > *When *$y=5$*, then** *$x=-2$
> *When *$y=-5$*, then** *$x=2$
> *Substitute these back in to get *$z$
> 
> **Final answer:** $-2+5i$** or **$2-5i$
