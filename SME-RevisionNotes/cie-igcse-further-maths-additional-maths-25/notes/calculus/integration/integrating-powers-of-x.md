---
note_id: "rn_jXDdP3MMJ8dSbSYx"
title: "Integrating Powers of x"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/calculus/integration/integrating-powers-of-x
path: calculus/integration/integrating-powers-of-x
updated_at: "2026-07-02T08:19:38.534Z"
spec_point_ids: ["spcpt_b8YJ77mKsSyF3zCy", "spcpt_ZQNM4dHgZkvDTmXJ"]
spec_point_codes: []
guided_study: false
---

# Integrating Powers of x

## Integrating Powers of x

> **Spec point** — `spcpt_b8YJ77mKsSyF3zCy`

## Integrating powers of x

### How do I integrate powers of x?

- Powers of$x$ are integrated according to the following formulae:

  - If$f(x)=x^{n}$ then$\int f ( x ) \mathrm{d} x = \frac{x^{n + 1} }{n + 1} + c$ where$n\inℚ,n\neq-1$ and$c$ is the **constant** of **integration**
  - For each term …
  
    - … increase the power (of x) by 1
    - … divide by the new power
  - This does not apply when the original power is -1
  
    - the new power would be 0 and division by 0 is undefined

![Formula for integrating x to the power of a constant](../../../assets/8b60ecd8ff7e-8-1-2-notes-fig2.png)

- If the power of$x$ is multiplied by a constant then the integral is also multiplied by that constant

  - If$f(x)=ax^{n}$ then$\int f ( x ) \mathrm{d} x = \frac{a x^{n + 1} }{n + 1} + c$ where$n\inℚ,n\neq-1$ and$a$ is a constant and$c$ is the **constant** of **integration**
- Remember the special case:

  - $\int a \mathrm{d} x = a x + c$
  
    - e.g. $\int 4 \mathrm{d} x = 4 x + c$
  - This allows **constant** terms to be integrated

### How do I integrate expressions containing powers of x?

- The formulae for integrating powers of$x$ apply to **all** **rational** **numbers** so it is possible to integrate any expression that is a sum or difference of powers of$x$

  - e.g.  If$f(x)=8x^{3}-2x+4$ then$\int f ( x ) \mathrm{d} x = \frac{8 x^{3 + 1} }{3 + 1} - \frac{2 x^{1 + 1} }{1 + 1} + 4 x + c = 2 x^{4} - x^{2} + 4 x + c$
- Functions involving **roots** will need to be rewritten as **fractional powers** of$x$ first

  - eg. If$f ( x ) = 5 \sqrt[3]{x}$ then rewrite as$f(x)=5x^{\frac{1}{3}}$ and integrate
- Functions involving **fractions** with **denominators** in **terms** of$x$ will need to be rewritten as **negative powers** of$x$ first

  - e.g.  If$f(x)=\frac{4}{x^{2}}+x^{2}$ then rewrite as$f(x)=4x^{-2}+x^{2}$ and integrate
- **Products** and **quotients** cannot be integrated this way so would need **expanding**/**simplifying** first

  - e.g.  If$f(x)=8x^{2}(2x-3)$ then`Error converting from MathML to accessible text.`

> **Exam Hint**
> - You can speed up the process of integration in the exam by committing the pattern of basic integration to memory
> 
>   - In general you can think of it as 'raising the power by one and dividing by the new power'
>   - Practice this lots before your exam so that it comes quickly and naturally when doing more complicated integration questions

> **Worked Example**
> Given that
> 
> $\frac{dy}{dx}=3x^{4}-2x^{2}+3-\frac{1}{\sqrt{x}}$
> 
> find an expression for$y$ in terms of$x$.
> 
> > *Rewrite all terms as powers of **x **using the laws of indices for fractional and negative powers on the last term.*
> 
> $\frac{dy}{dx}=3x^{4}-2x^{2}+3-x^{-\frac{1}{2}}$
> 
> > *Find **y **by integrating each term. *
> 
> $y = \int ( 3 x^{4 - 2 x^{2} + 3 - x^{-1} \frac{1}{2}} ) \mathrm{d} x$
> 
> $y=\frac{3x^{5}}{5}-\frac{2x^{3}}{3}+3x-\frac{x^{\frac{1}{2}}}{\frac{1}{2}}+c$
> 
> > *Rewrite using the same format given in the question.*
> 
> $y=\frac{3}{5}x^{5}-\frac{2}{3}x^{3}+3x-2\sqrt{x}+c$

## Finding the Constant of Integration

> **Spec point** — `spcpt_ZQNM4dHgZkvDTmXJ`

## Finding the constant of integration

### How do I find the constant of integration?

- **STEP 1 **

  - Rewrite the function into a more easily *integrable* form
  
    - Each term needs to be a power of **x** (or a constant)
- **STEP 2**

  - Integrate each term and remember “+c”
  
    - Increase power by 1 and divide by new power
- **STEP 3**

  - Substitute the coordinates of a given point in to form an equation in **c**
  
    - Solve the equation to find **c**

![Notes fig3, A Level & AS Level Pure Maths Revision Notes](../../../assets/fe8672720279-8-1-2-notes-fig3.png)

![Example of finding the constant of integration](../../../assets/3b93c867ccea-8-1-2-notes-fig4.png)

> **Exam Hint**
> - If a constant of integration can be found then the question will need to give you some extra information
> 
>   - If this is given then make sure you use it to find the value of c

> **Worked Example**
> Given $\mathrm{f} ' ( x ) = \frac{( x + 3 )^{2}}{ \sqrt{x} }$ and $\mathrm{f} ( 1 ) = 25$, find $\mathrm{f} ( x )$.
> 
> > *Rewrite* $\mathrm{f}^{'} ( x )$ *in a form the can be integrated more easily.*
> 
> > $\begin{gathered} \mathrm{f}^{'} ( x ) & = \frac{( x + 3 ) ( x + 3 )}{ \sqrt{x} } \\ = \frac{x^{2 } + 6 x + 9}{x^{1 \frac{1}{2}} } \\ = \frac{ x^{2}}{x^{1 \frac{1}{2}} } + \frac{ 6 x}{x^{1 \frac{1}{2}} } + \frac{ 9}{x^{1 \frac{1}{2}} } \\ = x^{ \frac{3}{2} } + 6 x^{1 \frac{1}{2}} + 9 x^{- 1 \frac{1}{2}} \end{gathered}$*   *
> 
> > *Integrate each term, remember to include a constant of integration.*
> 
> > $\mathrm{f} ( x ) = \frac{ x ^{\frac{5}{2}}}{\frac{5}{2}} + \frac{6 x ^{\frac{3}{2}}}{\frac{3}{2}} + \frac{9 x^{1} half}{1 half} + c$*   *
> 
> > *Simplify.*
> 
> $\mathrm{f} ( x ) = \frac{2}{5} x^{ \frac{5}{2} } + 4 x^{ \frac{3}{2} } + 18 x^{1 \frac{1}{2}} + c$
> 
> > *Use f(1) =25 to find the value of **c.*
> 
> $\mathrm{f} ( 1 ) = \frac{2}{5} ( 1 )^{ \frac{5}{2} } + 4 ( 1 )^{ \frac{3}{2} } + 18 ( 1 )^{1 \frac{1}{2}} + c
>$
> 
> $\begin{gathered} \frac{2}{5} + 4 + 18 + c & = 25 \\ 22 \frac{2}{5} + c & = 25 \\ c & = \frac{ 13 }{5} \end{gathered}$
> 
> $f(x)=\frac{2}{5}x^{\frac{5}{2}}+4x^{\frac{3}{2}}+18x^{\frac{1}{2}}+\frac{13}{5}$
