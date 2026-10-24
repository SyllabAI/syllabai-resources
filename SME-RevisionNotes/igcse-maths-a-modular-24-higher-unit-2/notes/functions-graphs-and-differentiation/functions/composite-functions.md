---
note_id: "rn_5r2THGvJSbv3HKnW"
title: "Composite Functions"
source: https://www.savemyexams.com/igcse/maths/edexcel/a-modular/24/higher-unit-2/revision-notes/functions-graphs-and-differentiation/functions/composite-functions
path: functions-graphs-and-differentiation/functions/composite-functions
updated_at: "2026-01-27T17:19:32.495Z"
spec_point_ids: ["spcpt_XWbj3PG2n8tdWF2w"]
spec_point_codes: []
guided_study: false
---

# Composite Functions

## Composite Functions

> **Spec point** — `spcpt_XWbj3PG2n8tdWF2w`

## Composite functions

### What is a composite function?

- A **composite function** is a function applied to the **output **of another function

### What notation is used for composite functions?

- If $\mathrm{f} ( x )$ and $\mathrm{g} ( x )$ are two functions, then

  - $\mathrm{g} ( \mathrm{f} ( x ) )$ is a **composite **function
  
    - Also written $\mathrm{gf}:x$
  - It means the input $x$goes through **function **$f$** first**
  
    - This gives the output $\mathrm{f} ( x )$
    - Then this output, $\mathrm{f} ( x )$, becomes the **input** of function $g$, giving $\mathrm{g} ( \mathrm{f} ( x ) )$
  - $gf ( x )$ is the shorthand** notation used **for $\mathrm{g} ( \mathrm{f} ( x ) )$
  
    - It means do $f$ first, then $g$
    - The** order **of applying the functions goes from **right to left**
    - (the letter nearest the bracket goes first)
    - This is often the opposite of what people expect!
  - $fg ( x )$ means do $\mathrm{g} ( x )$ **first** then $\mathrm{f} ( x )$ **second**
  - $ff ( x )$ means apply $\mathrm{f} ( x )$ twice!
  
    - This can be written $\mathrm{f}^{2} ( x )$
    - This does not mean the same as $[ \mathrm{f} ( x ) ]^{2}$

> **Exam Hint**
> A good trick in the exam is to write brackets around $gf ( x )$ to make it $\mathrm{g} ( \mathrm{f} ( x ) )$, to see that it is "g" of "f(x)".

### How do I substitute numbers into composite functions?

- If you are putting a **number **into a composite function

  - put the number into the function closest to (*x*)
  - then make the **output** of the **first **function the **input **of the **second **function
- For example, if $\mathrm{f} ( x ) = 2 x + 1$ and $\mathrm{g} ( x ) = \frac{1}{x}$

  - to find $gf ( 2 )$:
  
    - Put the 2 in as the input of $f$ first
    - $\mathrm{f} ( 2 ) = 2 ( 2 ) + 1 = 5$
    - Then put 5 in as the input of $g$
    - So $\text{gf} ( 2 ) = \mathrm{g} ( \mathrm{f} ( 2 ) ) = \mathrm{g} ( 5 ) = 1 \frac{1}{5}$
  - to find $fg ( 2 )$:
  
    - Put the 2 in as the input of $g$ first
    - $\mathrm{g} ( 2 ) = 1 \frac{1}{2}$
    - Then put $\frac{1}{2}$ in as the input of $f$
    - So $\text{fg} ( 2 ) = \mathrm{f} ( \mathrm{g} ( 2 ) ) = \mathrm{f} ( 1 \frac{1}{2} ) = 2 ( 1 \frac{1}{2} ) + 1 = 2$
  - to find $ff ( 2 )$:
  
    - $\mathrm{f} ( 2 ) = 2 \times 2 + 1 = 5$
    - $\mathrm{f} ( 5 ) = 2 \times 5 + 1 = 11$
    - so $ff ( 2 ) = 11$

### How do I find composite functions algebraically?

- If you are using algebra, **substitute **the whole **algebraic expression** as your input

  - For example, if $f(x)=2x+1$ and $g(x)=\frac{1}{x}$
  
    - $\text{fg} ( x ) = \mathrm{f} ( \mathrm{g} ( x ) ) = \mathrm{f} ( \frac{1}{x} ) = 2 \times ( \frac{1}{x} ) + 1 = \frac{2}{x} + 1$
    - $\text{gf} ( x ) = \mathrm{g} ( \mathrm{f} ( x ) ) = \mathrm{g} ( 2 x + 1 ) = \frac{1}{2 x + 1}$
    - $\text{ff} ( x ) = \mathrm{f} ( \mathrm{f} ( x ) ) = \mathrm{f} ( 2 x + 1 ) = 2 ( 2 x + 1 ) + 1$ which simplifies to $\text{ff} ( x ) = 4 x + 3$

> **Worked Example**
> In this question, $\mathrm{f} ( x ) = 2 x - 1$ and $\mathrm{g} : x \rightarrow ( x + 2 )^{2}$.
> 
> (a) Find  $fg ( 4 )$.
> 
> **Answer:**
> 
> > *"g" is on the inside of the composite function, so apply g first*
> 
> $\mathrm{g} ( 4 ) = ( 4 + 2 )^{2} = 6^{2} = 36$
> 
> > *Now apply the function "f" to 36*
> 
> $\begin{gathered} \mathrm{f} ( 36 ) & = 2 ( 36 ) - 1 \\ = 72 - 1 \end{gathered}$
> 
> $\mathrm{fg}(4)=71$
> 
> (b) Find  $gf ( x )$.
> 
> **Answer:**
> 
> > *"f" is on the inside of the composite function so substitute the function f(**x**) into g(**x**)*
> *It can help to write *$\text{gf} ( x ) = \mathrm{g} ( \mathrm{f} ( x ) )$
> 
> * *$\text{gf} ( x ) = \mathrm{g} ( \mathrm{f} ( x ) ) = \mathrm{g} ( 2 x - 1 ) = ( ( 2 x - 1 ) + 2 )^{2}$
> 
> > *Simplify inside the bracket*
> 
> $\begin{gathered} \text{gf} ( x ) & = ( 2 x - 1 + 2 )^{2} \end{gathered}$
> 
> $\mathrm{gf}(x)=(2x+1)^{2}$
