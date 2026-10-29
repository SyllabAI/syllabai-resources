---
note_id: "rn_wHJKVptgngBPYqhV"
title: "Factor & Remainder Theorems"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/equations-identities-and-inequalities/equations-and-identities/factor-and-remainder-theorems
path: equations-identities-and-inequalities/equations-and-identities/factor-and-remainder-theorems
updated_at: "2026-01-06T10:39:15.043Z"
spec_point_ids: ["spcpt_PFKXgTYx2k2g6pny", "spcpt_hBfjzzFk2GFdSfMr"]
spec_point_codes: []
guided_study: false
---

# Factor & Remainder Theorems

## Factor Theorem

> **Spec point** — `spcpt_PFKXgTYx2k2g6pny`

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
  - Hence  $\frac{f(x)}{x-a}=Q(x)$
  
    - I.e. $Q ( x )$ is the **quotient** when $\mathrm{f} ( x )$ is divided by $( x - a )$
    - And the **remainder** is equal to zero
- If the linear factor has a **coefficient of *****x**** *(other than 1) you must first factorise out the coefficient

  - For the linear factor  $( b x - c ) = b ( x - \frac{c}{b} )$
  
    - $\mathrm{f} ( \frac{c}{b} ) = 0$
    - $\mathrm{f} ( x ) = b ( x - \frac{c}{b} ) \times Q ( x )$

> **Exam Hint**
> - Be careful with the minus sign in a factor $( x - a )$
> 
>   - That means $a$ is a solution to $f ( x ) = 0$, not $-a$ !
> - If you are looking for **integer** solutions to $\mathrm{f} ( x ) = 0$  (where $\mathrm{f} ( x )$ is a polynomial)
> 
>   - those solutions will always be factors of the constant term in $\mathrm{f} ( x )$

> **Worked Example**
> a) Consider the function$f(x)=x^{3}-2x^{2}-x+2$. Given that $x=2$ is a solution to the equation $\mathrm{f} ( x ) = 0$, write down a linear factor of $\mathrm{f} ( x )$.
> 
> *By the factor theorem, if* $\mathrm{f} ( a ) = 0$ *then* $( x - a )$ *is a factor of* $\mathrm{f} ( x )$
> 
> > $x-2$* *
> 
> b) Use the factor theorem to determine whether $( x + 1 )$ is a factor of $g(x)=2x^{3}+3x^{2}-x+5$.
> 
> > *By the factor theorem,* $( x - a )$ *can only be a factor of* $\mathrm{g} ( x )$ *if* $\mathrm{g} ( a ) = 0$*.*
> 
> > *But be careful – here* $a$ *is equal to* $-1$*, not* $1$
> 
> **Final answer:** $\begin{gathered} \mathrm{g} ( - 1 ) & = 2 ( - 1 )^{3} + 3 ( - 1 )^{2} - ( - 1 ) + 5 \\ = - 2 + 3 + 1 + 5 \\ = 7 \end{gathered}$
> $g(-1)\neq0$**, so **$(x+1)$** is not a factor of **$g(x)$
> 
> c) It is given that $( 2 x - 3 )$ is a factor of $\mathrm{h} ( x ) = 2 x^{3} - b x^{2} + 7 x - 6$. Find the value of $b$.
> 
> > $( 2 x - 3 ) = 2 ( x - \frac{3}{2} )$*,  so* $( x - \frac{3}{2} )$ *is a factor of* $\mathrm{h} ( x )$*.*
> 
> > *Therefore by the factor theorem,* $\mathrm{h} ( \frac{3}{2} ) = 0$*.*
> 
> $\begin{gathered} 2 ( \frac{3}{2} )^{3} - b ( \frac{3}{2} )^{2} + 7 ( \frac{3}{2} ) - 6 & = 0 \\ \frac{27}{4} - \frac{9}{4} b + \frac{21}{2} - 6 & = 0 \\ \frac{45}{4} - \frac{9}{4} b & = 0 \\ \frac{9}{4} b & = \frac{45}{4} \\ b = \frac{4}{9} \times \frac{45}{4} \end{gathered}$
> 
> $b=5$

## Remainder Theorem

> **Spec point** — `spcpt_hBfjzzFk2GFdSfMr`

## Remainder Theorem

### What is the remainder theorem?

- The **remainder theorem** is used to find the remainder when we divide a **polynomial** function by a linear function
- When a polynomial function $\mathrm{f} ( x )$ is divided by a linear function $( x - a )$, the value of the **remainder **$R$ is given by $\mathrm{f} ( a ) = R$

  - Note, if $\mathrm{f} ( a ) = 0$ then $( x - a )$ is a factor of $\mathrm{f} ( x )$; this is the factor theorem

### How do I use the remainder theorem?

- Consider a polynomial function $\mathrm{f} ( x )$ and a linear function  $( x - a )$

  - $\frac{ \mathrm{f} ( x )}{( x - a )} = Q ( x ) + \frac{R}{( x - a )}$
  
    - $Q ( x )$ is the **quotient** (also a polynomial function)
    - $R$ is the **remainder **(a real number)
  - This may also be written as $\mathrm{f} ( x ) = Q ( x ) \times ( x - a ) + R$
  - The **remainder theorem** tells us that  $R = \mathrm{f} ( a )$
  
    - I.e. we don't need to do the **algebraic division** to find the remainder!
- If the linear factor has a **coefficient of *****x*** (other than 1) then you must first factorise out the coefficient

  - For the linear function $( b x - c ) = b ( x - \frac{c}{b} )$
  
    - $R = \mathrm{f} ( \frac{c}{b} )$

> **Exam Hint**
> - Be careful with the minus sign in $( x - a )$
> 
>   - You need to put $a$ into $\mathrm{f} ( x )$ to find the remainder, not $-a$!

> **Worked Example**
> a) Find the remainder when the function $\mathrm{f} ( x ) = 2 x^{4} - 2 x^{3} - x^{2} - 3 x + 1$ is divided by $( x - 2 )$.
> 
> > *We're dividing by* $( x - a ) = ( x - 2 )$
> 
> > *So* $a=2$
> 
> > *By the remainder theorem the remainder will be*
> 
> $\begin{gathered} \mathrm{f} ( 2 ) & = 2 ( 2 )^{4} - 2 ( 2 )^{3} - ( 2 )^{2} - 3 ( 2 ) + 1 \\ = 32 - 16 - 4 - 6 + 1 \\ = 7 \end{gathered}$
> 
> **Final answer:** **Remainder = 7**
> 
> b) The remainder when $\mathrm{g} ( x ) = 2 x^{3} + x^{2} + b x + 1$ is divided by $( 2 x + 1 )$ is 3.  Find the value of $b$.
> 
> $( 2 x + 1 ) = 2 ( x + 1 \frac{1}{2} ) = 2 ( x - ( - 1 \frac{1}{2} ) )$
> 
> > *So here the value of* $a$ *to use is* $-\frac{1}{2}$
> 
> > *By the remainder theorem the remainder will be equal to* $\mathrm{g} ( - 1 \frac{1}{2} )$
> 
> $\begin{gathered} 2 ( - 1 \frac{1}{2} )^{3} + ( - 1 \frac{1}{2} )^{2} + b ( - 1 \frac{1}{2} ) + 1 & = 3 \\ - 1 \frac{1}{4} + 1 \frac{1}{4} - \frac{b}{2} + 1 & = 3 \\ - \frac{b}{2} & = 2 \end{gathered}$
> 
> $b=-4$
