---
note_id: "rn_6JfgD9zknhMB3kJz"
title: "The Factor Theorem"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/algebra/the-factor-theorem-and-algebraic-division/the-factor-theorem
path: algebra/the-factor-theorem-and-algebraic-division/the-factor-theorem
updated_at: "2026-01-06T10:49:23.195Z"
spec_point_ids: ["spcpt_HBwF9SP8dhSGhZZk"]
spec_point_codes: []
guided_study: false
---

# The Factor Theorem

## Factor Theorem

> **Spec point** — `spcpt_HBwF9SP8dhSGhZZk`

## Factor Theorem

### What is the factor theorem?

- The **factor theorem** is used to find the linear **factors** of a function

  - This is closely related to finding the **roots** (or **solutions**) of a function or equation
- For a function $\mathrm{f} ( x )$, the **factor theorem** tells us that

  - If  $\mathrm{f} ( a ) = 0$, then $( x - a )$ is a factor of $\mathrm{f} ( x )$
  - If $( x - a )$ is a factor of $\mathrm{f} ( x )$, then  $\mathrm{f} ( a ) = 0$

### How do I use the factor theorem?

- Consider the  function $\mathrm{f} ( x )$ where $( x - a )$ is a factor

  - Then by the factor theorem we know that $\mathrm{f} ( a ) = 0$
  
    - I.e., $x=a$ is a solution to the equation  $\mathrm{f} ( x ) = 0$
- Or consider the function $\mathrm{f} ( x )$ where $\mathrm{f} ( a ) = 0$

  - Then by the factor theorem we know  that $( x - a )$ is a factor of $\mathrm{f} ( x )$
  - Therefore  $f(x)=(x-a)\timesQ(x)$
  
    - where $Q ( x )$ is a function that is also a factor of $\mathrm{f} ( x )$
  - Hence  $\frac{ \mathrm{f} ( x )}{( x - a )} = Q ( x )$
  
    - I.e. $Q ( x )$ is the **quotient** when $\mathrm{f} ( x )$ is divided by $( x - a )$
    - And the **remainder** is equal to zero
- If the linear factor has a **coefficient of *****x**** *(other than 1) you must first factorise out the coefficient

  - For the linear factor  $( b x - c ) = b ( x - \frac{c}{b} )$
  
    - $\mathrm{f} ( \frac{c}{b} ) = 0$
    - $\mathrm{f} ( x ) = b ( x - \frac{c}{b} ) \times Q ( x ) = ( b x - c ) \times Q ( x )$

> **Exam Hint**
> Be careful with the minus sign in a factor $( x - a )$.
> 
> - That means $a$ is a solution to $f ( x ) = 0$, not $-a$ !
> 
> If you are looking for **integer** solutions to $\mathrm{f} ( x ) = 0$  (where $\mathrm{f} ( x )$ is a polynomial)
> 
> - those solutions will always be factors of the constant term in $\mathrm{f} ( x )$

> **Worked Example**
> (a) Consider the function$f(x)=x^{3}-2x^{2}-x+2$. Given that $x=2$ is a solution to the equation $\mathrm{f} ( x ) = 0$, write down a linear factor of $\mathrm{f} ( x )$.
> 
> **Answer:**
> 
> > *By the factor theorem, if  *$\mathrm{f} ( a ) = 0$* then *$( x - a )$* is a factor of *$\mathrm{f} ( x )$
> 
> > $x-2$* *
> 
> (b) Use the factor theorem to determine whether $( x + 1 )$ is a factor of $g(x)=2x^{3}+3x^{2}-x+5$.
> 
> **Answer:**
> 
> > *By the factor theorem, *$( x - a )$* can only be a factor of *$\mathrm{g} ( x )$* if  *$\mathrm{g} ( a ) = 0$
> 
> > *But be careful, here *$a$* is equal to *$-1$*, not *$1$
> 
> $\begin{gathered} \mathrm{g} ( - 1 ) & = 2 ( - 1 )^{3} + 3 ( - 1 )^{2} - ( - 1 ) + 5 \\ = - 2 + 3 + 1 + 5 \\ = 7 \end{gathered}$
> 
> **Final answer:** $g(-1)\neq0$**, so **$(x+1)$** is not a factor of **$g(x)$
> 
> (c) Given that $( 2 x - 3 )$ is a factor of $\mathrm{h} ( x ) = 2 x^{3} - b x^{2} + 7 x - 6$, find the value of $b$.
> 
> **Answer:**
> 
> > $( 2 x - 3 ) = 2 ( x - \frac{3}{2} )$*,  so *$( x - \frac{3}{2} )$* is a factor of *$\mathrm{h} ( x )$
> 
> > *Therefore by the factor theorem, *$\mathrm{h} ( \frac{3}{2} ) = 0$
> 
> $\begin{gathered} 2 ( \frac{3}{2} )^{3} - b ( \frac{3}{2} )^{2} + 7 ( \frac{3}{2} ) - 6 & = 0 \\ \frac{27}{4} - \frac{9}{4} b + \frac{21}{2} - 6 & = 0 \\ \frac{45}{4} - \frac{9}{4} b & = 0 \\ \frac{9}{4} b & = \frac{45}{4} \\ b = \frac{4}{9} \times \frac{45}{4} \end{gathered}$
> 
> $b=5$
