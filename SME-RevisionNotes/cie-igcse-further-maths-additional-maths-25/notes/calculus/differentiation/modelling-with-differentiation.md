---
note_id: "rn_3Qj5d35dS6pyXzF7"
title: "Modelling with Differentiation"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/calculus/differentiation/modelling-with-differentiation
path: calculus/differentiation/modelling-with-differentiation
updated_at: "2026-07-02T08:19:38.534Z"
spec_point_ids: ["spcpt_rxyn2MtzRV7t5ZtP", "spcpt_n3Yp8bCGKw2Nc93Z"]
spec_point_codes: []
guided_study: false
---

# Modelling with Differentiation

## Modelling with Differentiation

> **Spec point** — `spcpt_rxyn2MtzRV7t5ZtP`

## Modelling with differentiation

### How is differentiation used in modelling questions?

- **Derivatives** can be calculated for any variables – not just ***y*** and ***x***
- The derivative is a formula giving the **rate of change** of one variable with **respect** to the other variable

  - For example if $A=4πr^{2}$ then $\frac{dA}{dr}=8πr$
  - $\frac{dA}{dr}$ is the **rate of change** of $A$ with **respect** to $r$
- The phrase 'increasing at a rate of' means the **rate of change** of one variable with **respect** to time

  - $\frac{d}{dt}$

- **Differentiation** can be used to find **maximum** and **minimum** points of a function

  - In modelling, this is called **optimisation**
  - Second derivative tests help to determine is the point is a maximum or minimum

> **Exam Hint**
> - Read the question carefully to determine which variables you will need to use
> 
>   - The question may give you a formula to help you

> **Worked Example**
> The volume, $V$, of a sphere of radius $r$ is given by $V=\frac{4}{3}πr^{3}.$
> 
> Find the rate of change of the volume with respect to the radius.
> 
> > *Differentiate the formula given for the volume of a sphere.*
> 
> $\frac{dV}{dr}=3\times\frac{4}{3}π\timesr^{2}$
> 
> $\frac{dV}{dr}=4πr^{2}$

## Optimisation

> **Spec point** — `spcpt_n3Yp8bCGKw2Nc93Z`

## Optimisation

### What is optimisation?

- In general, optimisation is finding the best way to do something
- In mathematics, optimisation is finding the maximum or minimum output of a function

  - For example, finding the maximum possible profit or minimum costs

- Differentiation can be used to **solve optimisation problems** in **modelling** questions

  - For example you may want to
  
    - **Maximise** the **volume** of a **container**
    - **Minimise** the **amount** of **fuel** used

![Example of using differentiation to maximise a function](../../../assets/42b148ac6bab-7-2-6-model-diff-illustr-2.png)

> **Exam Hint**
> - Exam questions on this topic will often be divided into two parts:
> 
>   - First a 'Show that...' part where you derive a given formula from the information in the question
>   - And then a 'Find...' part where you use differentiation to answer a question about the formula
> - Even if you can't answer the first part you can still use the formula to answer the second part

> **Worked Example**
> A cuboid has length $4x$ cm, width $x$ cm, and height $( \frac{3}{x} - 5 )$ cm.
> 
> (a)$\begin{gathered} \\ \\ \end{gathered}$ Show that the volume, $V$ cm<sup>3</sup> is given by $V=12x-20x^{2}$.
>  
> *The volume of a cuboid is "*$V=length\timeswidth\timesheight$*"*
> 
> $\therefore V = 4 x \times x \times ( \frac{3}{x} - 5 )$
> 
> > *Expand and simplify*
> 
> $\begin{gathered} V = 4 x^{2} ( \frac{3}{x} - 5 ) \\ V = \frac{12 x^{2}}{x} - 20 x^{2} \end{gathered}$
> 
> > $\thereforeV=12x-20x^{2}$*  *
> 
> (b) Find the maximum volume of the cuboid.   *Differentiate **V** with respect to **x*
> 
> $\frac{dV}{dx}=12-40x$
> 
> > *At the maximum volume,* $\frac{dV}{dx}=0$
> 
> $\therefore12-40x=0$
> 
> > *Solve for **x*
> 
> $\begin{array}{rcl} 40 x & = 12 \\ x = \frac{12}{40} = 0.3 \end{array}$
> 
> > *So the value of **x**, at the maximum volume is 0.3 Find the maximum volume by substituting **x** = 0.3 in to the formula for **V*
> 
> $V = 12 ( 0.3 ) - 20 ( 0.3 )^{2} = 1.8$
> 
> **Final answer:** **The maximum volume of the cuboid is 1.8 cm**<sup>**3**</sup>**  **
> 
> (c) Prove that your answer is a maximum value.
> 
> > *Using the second derivative is usually the easiest way to find the nature of a stationary point*
> 
> $\frac{ \mathrm{d}^{2} y}{ \mathrm{d} x^{2}} = - 40 ( < 0 )$
> 
> **Final answer:** **The value of the second derivative (at **$x=0.3$**) is negative**
> 
> **Final answer:** **Therefore ****V**** = 1.8 cm**<sup>**3**</sup>** is a maximum volume**
