---
note_id: "rn_jFGbjbvCm4qjqMcJ"
title: "Differentiating Special Functions"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/calculus/differentiation/differentiating-special-functions
path: calculus/differentiation/differentiating-special-functions
updated_at: "2026-07-02T08:19:38.521Z"
spec_point_ids: ["spcpt_H8NsM2cXt3FHHgD2", "spcpt_4grcDgq3ZPzXqWcx"]
spec_point_codes: []
guided_study: false
---

# Differentiating Special Functions

## Differentiating Trig Functions

> **Spec point** — `spcpt_H8NsM2cXt3FHHgD2`

## Differentiating trig functions

### How do I differentiate trig functions?

- For calculus with trigonometric functions, angles must be measured in **radians**
- The derivative of $y=\mathrm{sin}x$ is $\frac{dy}{dx}=\mathrm{cos}x$  ** **
- The derivative of $y=\mathrm{cos}x$ is $\frac{dy}{dx}=-\mathrm{sin}x$
- The derivative of $y=\mathrm{tan}x$ is $\frac{dy}{dx}=\mathrm{sec}^{2}x$
- The following two sets of relationships can be derived using the **chain rule**, but are useful to know!
- For the **linear** function$ax+b$, where $a$ and $b$ are constants,

  - the derivative of  $y=\mathrm{sin}(ax+b)$ is $\frac{dy}{dx}=a\mathrm{cos}(ax+b)$
  - the derivative of $y=\mathrm{cos}(ax+b)$ is $\frac{dy}{dx}=-a\mathrm{sin}(ax+b)$
  - the derivative of $y=\mathrm{tan}(ax+b)$ is $\frac{dy}{dx}=a\mathrm{sec}^{2}(ax+b)$
- For the **general** function $f(x)$,

  - the derivative of $y=\mathrm{sin}(f(x))$ is** **`Error converting from MathML to accessible text.`
  - the derivative of $y=\mathrm{cos}(f(x))$ is $\frac{dy}{dx}=-f^{'}(x)\mathrm{sin}(f(x))$
  - the derivative of $y=\mathrm{tan}(f(x))$ is $\frac{dy}{dx}=f^{'}(x)\mathrm{sec}^{2}(f(x))$

> **Exam Hint**
> - Remember that these rules only work in radians!

> **Worked Example**
> a) Find $f'(x)$ for the functions
> 
> i. $f(x)=\mathrm{sin}x$
> 
> ii.$f(x)=\mathrm{cos}2x$
> 
> ii.$f(x)=3\mathrm{sin}4x-\mathrm{cos}(2x-3)$
> 
> i.
> 
> $f'(x)=\mathrm{cos}x$
> 
> ii.    *Use the chain rule or remember that when *$y = \cos ( a x + b )$*, then *$\frac{ \mathrm{d} y}{ \mathrm{d} x} = - a \sin ( a x + b )$
> 
> $f'(x)=-2\mathrm{sin}(2x)$
> 
> iii.   *Differentiate 'term by term'*
> 
> $\mathrm{f} ' ( x ) = 3 ( 4 \cos 4 x ) - ( - 2 \sin ( 2 x - 3 ) )$
> 
> $f'(x)=12\mathrm{cos}4x+2\mathrm{sin}(2x-3)$
> 
> b)$\begin{gathered} \\ \end{gathered}$ Find the gradient of the tangent to the curve $y=\mathrm{sin}(2x+\frac{π}{6})$ at the point where $x=\frac{π}{8}$.
> 
> > *Gradient of tangent is equal to gradient of curve. To find the gradient, differentiate...*
> 
> $\frac{ \mathrm{d} y}{ \mathrm{d} x} = 2 \cos ( 2 x + \frac{\pi }{6} )$
> 
> > *... and substitute *$x=\frac{π}{8}$* into the derivative*
> 
> $\frac{ \mathrm{d} y}{ \mathrm{d} x} = 2 \cos ( 2 ( \frac{\pi }{8} ) + \frac{\pi }{6} )$
> 
> > *Ensure that your calculator is in radians*
> 
> $=\frac{\sqrt{6}-\sqrt{2}}{2}=0.517638090...$
> 
> **Final answer:** **Answer = **$\frac{\sqrt{6}-\sqrt{2}}{2}$**, or 0.518 to 3 significant figures**

## Differentiating e^x & lnx

> **Spec point** — `spcpt_4grcDgq3ZPzXqWcx`

## Differentiating e^x & lnx

### How do I differentiate exponentials and logarithms?

- The derivative of $y=e^{x}$ is $\frac{dy}{dx}=e^{x}$ where $x\inℝ$
- The derivative of $y=\mathrm{ln}x$ is $\frac{dy}{dx}=\frac{1}{x}$ where $x>0$
- In addition, the results below can all be found using the **chain rule** but are worthwhile knowing, to save time in an exam
- For the **linear** function $ax+b$, where $a$ and $b$ are constants,

  - the derivative of $y=e^{(ax+b)}$ is $\frac{dy}{dx}=ae^{(ax+b)}$
  - the derivative of $y=\mathrm{ln}(ax+b)$ is $\frac{dy}{dx}=\frac{a}{(ax+b)}$
  
    - in the special case $b=0$, $\frac{dy}{dx}=\frac{1}{x}$     ($a$'s cancel)
- For the **general** function $f(x)$,

  - the derivative of $y=e^{f(x)}$ is $\frac{dy}{dx}=f'(x)e^{f(x)}$
  - the derivative of $y=\mathrm{ln}(f(x))$ is $\frac{dy}{dx}=\frac{f'(x)}{f(x)}$

> **Exam Hint**
> - Remember to avoid the common mistakes:
> 
>   - the derivative of$\mathrm{ln}kx$ with respect to $x$ is$\frac{1}{x}$*, *NOT$\frac{k}{x}$ !
>   - the derivative of $e^{kx}$ with respect to $x$ is $ke^{kx}$, NOT $kxe^{kx-1}$!

> **Worked Example**
> A curve has the equation $y=e^{-3x}+2\mathrm{ln}x$.
> 
> Find the gradient of the curve at the point where $x=2$ giving your answer in the form $a+be^{c}$, where $a,b$ and $c$ are integers to be found.
> 
> > *Differentiate each term separately. *
> 
> $\frac{ \mathrm{d} y}{ \mathrm{d} x} = - 3 \mathrm{e}^{- 3 x} + 2 ( \frac{1}{x} )$
> 
> > *Substitute *$x=2$* into the derivative.*
> 
> > $\frac{ \mathrm{d} y}{ \mathrm{d} x} = - 3 \mathrm{e}^{- 3 ( 2 )} + 2 ( 1 \frac{1}{2} )$* *
> 
> > *Rearrange to the required form.*
> 
> $\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = - 3 \mathrm{e}^{- 6} + 1 = 1 - 3 \mathrm{e}^{- 6} \end{gathered}$
> 
> > *Do not use your calculator to evaluate this as the question asks for the answer given in this form.*
> 
> $1-3e^{-6}$
