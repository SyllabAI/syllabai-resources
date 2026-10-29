---
note_id: "rn_TR5KM76JWzQ4PrSj"
title: " Integrating Basic Functions"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/calculus/integration/integrating-basic-functions
path: calculus/integration/integrating-basic-functions
updated_at: "2024-10-20T15:38:46.684Z"
spec_point_ids: ["spcpt_fhGBfgdfw9WmZGPc", "spcpt_3RJndX5xhQSKbn6K", "spcpt_D2njzcMRRFh4dvQn"]
spec_point_codes: []
guided_study: false
---

#  Integrating Basic Functions

## Integrating Powers of x

> **Spec point** — `spcpt_fhGBfgdfw9WmZGPc`

## Integrating Powers of x

### How do I integrate powers of x?

- Powers of$x$ are **integrated** according to the following **formula**:

  - $\int x^{n \mathrm{d} x = \frac{x^{n} + 1} }{n + 1} + c$  (where$c$ is the **constant** of **integration**)
  
    - This is valid for any value of $n$ **except** $n=-1$
    - So you cannot integrate  $\int x^{- 1} \mathrm{d} x = \int \frac{1}{x} \mathrm{d} x$ this way

- If $x^{n}$ is **multiplied by a constant** $a$ then

  - $\int a x^{n \mathrm{d} x = a \int x^{n} \mathrm{d} x = \frac{a x^{n} + 1} }{n + 1} + c$
  
    - This also is **not valid** for $n=-1$
- These formulae are **not** on the exam formula sheet, so you need to remember them
- Remember the **special case:**

  - $\int a \mathrm{d} x = a x + c$
  
    - e.g. $\int 4 \mathrm{d} x = 4 x + c$
  - This allows **constant** terms to be integrated
- Functions involving **roots** will need to be rewritten as **fractional powers**

  - e.g. $\int \sqrt[3]{x} \mathrm{d} x$
  
    - rewrite $\sqrt[3]{x}$ as $x^{\frac{1}{3}}$
    - then integrate
- **Fractions** with $x$ in the **denominator** will need to be rewritten as **negative powers**

  - e.g. $\int \frac{1}{x^{2}} \mathrm{d} x$
  
    - rewrite $\frac{1}{x^{2}}$ as $x^{-2}$
    - then integrate

### How do I integrate sums and differences of powers of x?

- The formulae can be used to integrate **sums or differences** of powers of$x$

  - Just integrate **term by term**
  
    - e.g. $\int ( 8 x^{3} - 2 x + 4 ) \mathrm{d} x$
    - $=\frac{8x^{3+1}}{3+1}-\frac{2x^{1+1}}{1+1}+4x+c$
    - $=2x^{4}-x^{2}+4x+c$
- **Products** and **quotients** cannot be integrated this way

  - You need to **expand** and/or **simplify** first
  
    - e.g. $\int 8 x^{2} ( 2 x - 3 ) \mathrm{d} x$
    - expand $8 x^{2} ( 2 x - 3 )$ as $16x^{3}-24x^{2}$
    - then integrate term by term
    - you **cannot** just multiply the integrals of $8x^{2}$ and $2x-3$ together

### What might I be asked to do once I’ve integrated?

- You may be given the **derivative** of a function and asked to **find** the function

  - Integration and differentiation are **inverse** operations so
  
    - $\int \mathrm{f}^{'} ( x ) \mathrm{d} x = \mathrm{f} ( x ) + c$
    - $\int \frac{ \mathrm{d} y}{ \mathrm{d} x} \mathrm{d} x = y + c$
- With more information the **constant** **of** **integration**,$c$, can be found
- The **area** **under** **a** **curve** can also be found using integration

> **Exam Hint**
> - Remember the basic pattern of integrating powers of *x*
> 
>   - 'Raise the power by one and divide by the new power'
>   - Lots of practice will improve your speed and accuracy
> - It's easy to check your answer when integrating
> 
>   - Just differentiate your answer
>   - It should turn back into the function you were integrating in the first place

> **Worked Example**
> Given that  $\frac{dy}{dx}=2x^{2}+3-\frac{1}{\sqrt{x}}$,  find an expression for$y$ in terms of$x$.
> 
> > *Start by rewriting* $\frac{dy}{dx}$*entirely in powers of* $x$
> 
> > *By laws of indices* $\frac{1}{\sqrt{x}}=x^{-\frac{1}{2}}$
> 
> $\frac{dy}{dx}=2x^{2}+3-x^{-\frac{1}{2}}$
> 
> > *Remember* $\int \frac{ \mathrm{d} y}{ \mathrm{d} x} \mathrm{d} x = y + c$
> 
> > *We can integrate term by term using* $\int a x^{n \mathrm{d} x = \frac{a x^{n} + 1} }{n + 1} + c$
> 
> $\begin{gathered} y = \int ( 2 x^{2} + 3 - x^{- 1 \frac{1}{2}} ) \mathrm{d} x \\ = 2 ( \frac{x^{2 + 1} }{2 + 1} ) + 3 x - \frac{x^{- 1 \frac{1}{2} + 1} }{- 1 \frac{1}{2} + 1} + c \\ = 2 ( \frac{x^{3}}{3} ) + 3 x - \frac{x^{1 \frac{1}{2}} }{1 \frac{1}{2}} + c \\ = \frac{2}{3} x^{3} + 3 x - 2 x^{1 \frac{1}{2}} + c \end{gathered}$
> 
> > *We can't find the value of* $c$ *without further info, so that's the answer to the question*
> 
> > *It's 'nice' to turn* $x^{\frac{1}{2}}$ *back into*$\sqrt{x}$ *for the final answer, but you would also get the marks without doing that*
> 
> $y=\frac{2}{3}x^{3}+3x-2\sqrt{x}+c$

## Integrating Trig Functions

> **Spec point** — `spcpt_3RJndX5xhQSKbn6K`

## Integrating Trig Functions

### How do I integrate sin and cos?

- You can **integrate** $\mathrm{sin}x$ and $\mathrm{cos}x$ by using the formulae

  - $\int \sin x d x = - \cos x + c$
  - $\int \cos x d x = \sin x + c$
  
    - $c$ is the **constant** **of** **integration**

- If $x$ is **multiplied by a constant** $a$ then

  - $\text{integral} \text{sin} a x d x = - \frac{1}{ } a \text{cos} a x + c$
  - $\text{integral} \text{cos} a x d x = \frac{1}{ } a \text{sin} a x + c$

- **None of these formulae** are on the exam formula sheet, so you need to remember them
- For calculus with trigonometric functions angles** must** be measured in **radians**

  - Make sure you know how to change the angle mode on your **calculator**

> **Exam Hint**
> - Remember to include 'c', the constant of integration, for any indefinite integrals
> - As soon as you see a question involving integration and trigonometry
> 
>   - put your calculator into radians mode

> **Worked Example**
> Given that  $\mathrm{f}^{'} ( x ) = 4 \cos 3 x - 1 \frac{1}{2} \sin 2 x$, find an expression for $\mathrm{f} ( x )$ in terms of $x$.
> 
> > *Remember that* $\int \mathrm{f}^{'} ( x ) \mathrm{d} x = \mathrm{f} ( x ) + c$
> 
> > *We can integrate term by term using the integration formulae for* $\mathrm{sin}ax$ *and* $\mathrm{cos}ax$
> 
> $\begin{array}{rcl} \mathrm{f} ( x ) & = \int ( 4 \cos 3 x - 1 \frac{1}{2} \sin 2 x ) \mathrm{d} x \\ = 4 ( 1 \frac{1}{3} \sin 3 x ) - 1 \frac{1}{2} ( - 1 \frac{1}{2} \cos 2 x ) + c \\ = \frac{4}{3} \sin 3 x + 1 \frac{1}{4} \cos 2 x + c \end{array}$
> 
> > *We can't find the value of* $c$ *without further info, so that's the answer to the question*
> 
> $f(x)=\frac{4}{3}\mathrm{sin}3x+\frac{1}{4}\mathrm{cos}2x+c$

## Integrating e^x

> **Spec point** — `spcpt_D2njzcMRRFh4dvQn`

## Integrating e^x

### How do I integrate exponentials?

- $e^{x}$ can be integrated using the **formula**

  - $\text{integral} e^{ } x d x = e^{ } x + c$
  
    - $c$ is the **constant** **of** **integration**
- If $x$ is **multiplied by a constant** $a$ then

  - ** **$\text{integral} e^{ } a x d x = \frac{1}{ } a e^{ } a x + c$

- These formulae are **not** on the exam formula sheet, so you need to remember them

> **Exam Hint**
> - Because '$e^{x}$ is its own integral' it is quite easy to integrate exponentials
> 
>   - Just be careful dealing with the constant in $e^{ax}$

> **Worked Example**
> Given that  $\mathrm{f}^{'} ( x ) = \frac{ \mathrm{e}^{2 x} - \mathrm{e}^{- 3 x} }{2}$, find an expression for $\mathrm{f} ( x )$ in terms of $x$.
> 
> > *Remember that* $\int \mathrm{f}^{'} ( x ) \mathrm{d} x = \mathrm{f} ( x ) + c$
> 
> > *We can integrate term by term using the integration formula for* $e^{ax}$
> 
> > *You might find it easier to split the fraction into two separate fractions first*
> 
> $\begin{gathered} \mathrm{f} ( x ) & = \int ( 1 \frac{1}{2} \mathrm{e}^{2 x} - 1 \frac{1}{2} \mathrm{e}^{- 3 x} ) \mathrm{d} x \\ = 1 \frac{1}{2} ( 1 \frac{1}{2} \mathrm{e}^{2 x} ) - 1 \frac{1}{2} ( \frac{1}{- 3} \mathrm{e}^{- 3 x} ) + c \\ = 1 \frac{1}{4} \mathrm{e}^{2 x} + \frac{1}{6} \mathrm{e}^{- 3 x} + c \end{gathered}$
> 
> > *We can't find the value of* $c$ *without further info, so that's the answer to the question*
> 
> $f(x)=\frac{1}{4}e^{2x}+\frac{1}{6}e^{-3x}+c$
