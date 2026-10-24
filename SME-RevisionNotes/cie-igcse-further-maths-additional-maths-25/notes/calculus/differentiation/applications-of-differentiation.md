---
note_id: "rn_WjxTSVwpz98rQBmD"
title: "Applications of Differentiation"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/calculus/differentiation/applications-of-differentiation
path: calculus/differentiation/applications-of-differentiation
updated_at: "2026-07-02T08:19:38.531Z"
spec_point_ids: ["spcpt_7sd9RjXKbFpCY5kB", "spcpt_r46Wb9qP6W5PWX9W", "spcpt_FScGqnRknDzxbdmN"]
spec_point_codes: []
guided_study: false
---

# Applications of Differentiation

## Finding Gradients

> **Spec point** — `spcpt_7sd9RjXKbFpCY5kB`

## Finding gradients

### How do I use the derivative to find the gradient of a curve?

- The **gradient of a curve** at a point is the **gradient of the tangent** to the curve at that point
- To find the gradient of a curve, at any point on the curve

  - **differentiate** to find $\frac{dy}{dx}$ (unless $\frac{dy}{dx}$is already known)
  - substitute the ***x*****‑coordinate** of the point into the derivative $\frac{dy}{dx}$** **and evaluate

![Grad Tang Norm Illustr 1, A Level & AS Maths: Pure revision notes](../../../assets/14d5046df61d-7-2-1-grad-tang-norm-illustr-1.png)

### How do I find the approximate change in y as x increases?

- $\mathrm{gradient}=\frac{\mathrm{change} \mathrm{in}y}{\mathrm{change} \mathrm{in}x}$so, for **small** changes you can write

  - $\mathrm{change} \mathrm{in}y=\mathrm{gradient}\times\mathrm{change} \mathrm{in}x$
- For example, if the gradient of $y=x-\frac{1}{x}$ at $x=2$ is $\frac{5}{4}$

  - what is the approximate change in $y$ as $x$ increases from $2$ to $2+h$, where $h$ is small?
  
    - $\mathrm{change} \mathrm{in}y=\mathrm{gradient}\times\mathrm{change} \mathrm{in}x=\frac{5}{4}h$

> **Exam Hint**
> - Read the question carefully; sometimes you are given $\frac{dy}{dx}$ and so don't need to differentiate initially - don't just automatically differentiate the first thing you see!
> - The following mean the same thing:
> 
>   - "Find the gradient of the curve at $x=2$"
>   - "Find the gradient of the tangent at $x=2$"
>   
>     - the tangent gradient = curve gradient at that point
>   - "Find the **rate of change** of *y* with respect to *x* at $x=2$"

> **Worked Example**
> A curve has the equation $y=\frac{4}{3}x^{3}+3x-8$.
> 
> (a) Find the gradient of the curve when $x=2$.
> 
> > $y$* is already in a form that can be differentiated*
> 
> $\frac{dy}{dx}=4x^{2}+3$
> 
> > *Substitute *$x=2$* into *$\frac{dy}{dx}$
> 
> $\frac{dy}{dx}=4\times2^{2}+3=19$
> 
> **Final answer:** **The gradient of the curve at **$x=2$** is 19**
> 
> (b) Work out the possible values of $x$ for which the rate of change of $y$ with respect to $x$ is 4.
> 
> > *"Rate of change" is another way of describing the derivative*
> 
> $\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = 4 \\ 4 x^{2} + 3 & = 4 \end{gathered}$
> 
> *Solve this equation to find *$x$
>  *Note that it is quadratic equation so it could have up to two solutions* 
> *The question refers to 'values' implying there is (or could be) more than one value for *$x$
> 
> $\begin{gathered} 4 x^{2} & = 1 \\ x^{2} & = 1 \frac{1}{4} \\ x = \pm \sqrt{1 \frac{1}{4}} \\ x = \pm 1 \frac{1}{2} \end{gathered}$
> 
> **Final answer:** **The possible values of **$x$**, that give a rate of change of 4, are **$x=\frac{1}{2}$** and **$x=-\frac{1}{2}$

## Increasing & Decreasing Functions

> **Spec point** — `spcpt_r46Wb9qP6W5PWX9W`

## Increasing & decreasing functions

### What are increasing and decreasing functions?

- A function is **increasing** when $\frac{dy}{dx}>0$** (the gradient is positive)**

  - This means graph of a function goes **up** as $x$ increases
- A function is **decreasing **when $\frac{dy}{dx}<0$** (the gradient is negative)**

  - This means graph of a function goes **down** as $x$ increases

![Incr Decr Illustr 1, A Level & AS Maths: Pure revision notes](../../../assets/724b0a64d283-7-2-2-incr-decr-illustr-1.png)

### How do I find where functions are increasing or decreasing?

- To identify the **intervals** on which a function is increasing or decreasing

**STEP 1**

Find the derivative **f'(*****x*****)**

**STEP 2**

Solve the inequalities

$f'(x)>0$ (for increasing intervals) and/or

$f'(x)<0$ (for decreasing intervals)

- Most functions are a combination of **increasing, decreasing** and **stationary**

  - a range of values of$x$ (**interval**)** **is given where a function satisfies each condition
  - e.g.  The function$f(x)=x^{2}$ has **derivative**$f^{'}(x)=2x$ so
  
    - $f(x)$ is **decreasing** for $x<0$
    - $f(x)$ is **stationary** at $x=0$
    - $f(x)$ is **increasing** for $x>0$

- To identify the intervals (the range of $x$ values) for which a curve is increasing or decreasing you need to:

1. Find the derivative $\frac{dy}{dx}$
2. Solve the inequalities $\frac{dy}{dx}>0$ (for increasing intervals) or $\frac{dy}{dx}<0$ (for decreasing intervals)

> **Exam Hint**
> - In an exam, if you need to show a function is increasing or decreasing you can use either strict (<, >) or non-strict (≤, ≥) inequalities
> 
>   - You will get the marks either way in this course

> **Worked Example**
> For what values of $x$ is $y=2x^{3}-3x^{2}+5$ a decreasing function?
> 
> > *The function is decreasing when its gradient *$( \frac{d y}{d x} )$* is less than 0.*
> 
> > *Find the derivative of the function by differentiating.*
> 
> > $\begin{gathered} \frac{d y}{d x} & = 6 x^{2} - 6 x \end{gathered}$* *
> 
> > *Solve the inequality *$\frac{dy}{dx}<0$* to find the set of values where the gradient is negative.*
> 
> $\begin{gathered} 6 x^{2} - 6 x & < 0 \end{gathered}$
> 
> > *Factorise.*
> 
> $\begin{gathered} 6 x ( x - 1 ) & < 0 \end{gathered}$
> 
> > *The solutions to *$\frac{dy}{dx}=0$* are *$x=0$* and  *$x=1$*. Find the correct way around for the inequalities by considering the graph of *$\frac{dy}{dx}$*. The graph is a positive quadratic, so the function is negative between the values of 0 and 1 (where it is below the *$x$*-axis).*
> 
> > *Considering a sketch of the graph of the gradient function may help you see this.*
> 
> ![3CqZzydq_aqa-fm-increasing-and-decreasing-functions-rn-diagram-we-1](assets/aa13fabfd646-3cqzzydq-aqa-fm-increasing-and-decreasing-functi.png)
> 
> > * *
> 
> > *You can check your answers by considering a sketch of the original function, it should be decreasing at the point where *$0<x<1.$
> 
> ![aqa-fm-increasing-and-decreasing-functions-rn-diagram-we-2](assets/21d2082619df-aqa-fm-increasing-and-decreasing-functions-rn-di.png)
> 
> $0<x<1$

## Tangents & Normals

> **Spec point** — `spcpt_FScGqnRknDzxbdmN`

## Tangents & normals

### What is a tangent?

- At any point on the graph of a (non-linear) **function**, the **tangent** is the straight line that **touches** the graph at a point **without crossing** through it
- Its **gradient** is given by the **derivative function**

![Grad Tang Norm Illustr 2](../../../assets/e709449608bc-7-2-1-grad-tang-norm-illustr-2.png)

### How do I find the equation of a tangent?

- To find the **equation of a straight line**, a **point** and the **gradient** are needed
- The **gradient**, $m$, of the **tangent** to the function $y = \mathrm{f} ( x )$ at $(x_{1},y_{1})$ is $f'(x_{1})$

  - You can find this by differentiating the function, and then substituting the $x$-coordinate of the point into the derivative
- Therefore find the **equation** of the **tangent** to the function $y=f(x)$ at the point $(x_{1},y_{1})$ by substituting the gradient, $\mathrm{f} ' ( x_{1} )$, and point $(x_{1},y_{1})$ into $y - y_{1} = m ( x - x_{1} )$, giving:

  - $y-y_{1}=f^{'}(x_{1})(x-x_{1})$
- (You could also substitute into $y=mx+c$)

### What is a normal?

- At any point on the graph of a (non-linear) function, the **normal** is the straight line that passes through that point and is **perpendicular** to the **tangent**

![Grad Tang Norm Illustr 3](../../../assets/b9f8a429b5c9-7-2-1-grad-tang-norm-illustr-3.png)

### How do I find the equation of a normal?

- The gradients of two perpendicular lines are **negative reciprocals**

  - This means that if** **$m_{1}$ is the gradient of the first line and $m_{2}$ is the gradient of a line perpendicular to the first line, then $m_{2}=\frac{-1}{m_{1}}$
  - Rearranging the formula above, $m_{1}\timesm_{2}=-1$ is a useful way to test whether two lines are perpendicular
- Therefore **gradient** of the **normal** to the function $y = \mathrm{f} ( x )$at $(x_{1},y_{1})$ is $\frac{-1}{f'(x_{1})}$
- Find the **equation** of the **normal** to the function $y=f(x)$ at the point $(x_{1},y_{1})$ by using $y-y_{1}=\frac{-1}{f^{'}(x_{1})}(x-x_{1})$

  - (or $y = \frac{- 1}{ \mathrm{f}^{'} ( x_{1} )} x + c$)

> **Exam Hint**
> - To be successful in this topic, first make sure you are confident with finding the equation of a straight line!

> **Worked Example**
> The function $f(x)$ is defined by
> 
> $f(x)=2x^{4}+\frac{3}{x^{2}}x\neq0$
> 
> a) Find an equation for the tangent to the curve $y=f(x)$ at the point where $x=1$, giving your answer in the form $y=mx+c$.
> 
> > *First find the derivative *$\mathrm{f} ' ( x )$* by differentiating*
> 
> > *Start by rewriting *$\mathrm{f} ( x )$*as powers of **x*
> 
> $\mathrm{f} ( x ) = 2 x^{4 + 3 x^{-2} }$
> 
> > *Now differentiate*
> 
> $\mathrm{f} ' ( x ) = 8 x^{3} - 6 x^{- 3}$
> 
> > *Now substitute *$x=1$* into *$\mathrm{f} ' ( x )$* to find the gradient of the tangent*
> 
> $\begin{array}{rcl} \mathrm{f} ' ( 1 ) & = 8 ( 1 )^{3} - 6 ( 1 )^{- 3} \\ = 8 - 6 \\ = 2 \end{array}$
> 
> > *We also need the **y**-coordinate, so substitute *$x=1$* into *$\mathrm{f} ( x )$* also*
> 
> $\begin{gathered} \mathrm{f} ( 1 ) & = 2 ( 1 )^{4 + 3 ( 1 )^{-2} } \\ = 2 + 3 \\ = 5 \end{gathered}$
> 
> > *Now we can substitute the point (1, 5) and the gradient, 2, into *$y - y_{1} = m ( x_{1} ) ( x - x_{1} )$
> 
> $\begin{gathered} y - 5 & = 2 ( x - 1 ) \end{gathered}$
> 
> > *Note that we are asked for the final answer in the form *$y=mx+c$*, so rearrange to this form*
> 
> $\begin{array}{rcl} y - 5 & = 2 x - 2 \end{array}$
> 
> $y=2x+3$
> 
> b) Find an equation for the normal at the point where $x=1$, giving your answer in the form $ax+by+d=0$, where $a$, $b$ and $d$ are integers.
> 
> > *We already have the gradient of the tangent; the gradient of the normal is *$\frac{-1}{m}$* where *$m$* is the gradient of the tangent*
> 
> *gradient of normal = *$\frac{-1}{2}$
> 
> > *Substitute the point (1, 5) from part (a) and the gradient of the normal into *$y - y_{1} = m ( x - x_{1} )$
> 
> $\begin{gathered} y - 5 & = ( \frac{- 1}{2} ) ( x - 1 ) \end{gathered}$
> 
> > *And rearrange into the form required*
> 
> $\begin{gathered} y - 5 & = - 1 \frac{1}{2} x + 1 \frac{1}{2} \\ 1 \frac{1}{2} x + y - 5 1 \frac{1}{2} & = 0 \end{gathered}$
> 
> > *Note that *$a$*, *$b$* and *$d$* must be integers so multiply by 2 to clear the fractions*
> 
> $\begin{gathered} x + 2 y - 11 & = 0 \end{gathered}$
