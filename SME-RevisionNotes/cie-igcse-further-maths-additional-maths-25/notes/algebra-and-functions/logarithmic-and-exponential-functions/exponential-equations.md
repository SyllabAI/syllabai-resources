---
note_id: "rn_scPmvt5cTMwynHQR"
title: "Exponential Equations"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/algebra-and-functions/logarithmic-and-exponential-functions/exponential-equations
path: algebra-and-functions/logarithmic-and-exponential-functions/exponential-equations
updated_at: "2026-07-02T08:19:38.508Z"
spec_point_ids: ["spcpt_rVQXdvGwFqtnNSvD"]
spec_point_codes: []
guided_study: false
---

# Exponential Equations

## Solving Exponential Equations

> **Spec point** — `spcpt_rVQXdvGwFqtnNSvD`

## Solving exponential equations

### What are exponential equations?

- An exponential equation is an equation where the unknown is a power

  - In simple cases the solution can be spotted without the use of a calculator
  - For example,

$\begin{gathered} 5^{2 x} & = 125 \\ 2 x & = 3 \\ x & = \frac{3}{2} \end{gathered}$

- In more complicated cases the laws of logarithms should be used to solve exponential equations

- The **change of base** law can be used to solve some exponential equations without a calculator

  - For example,

$\begin{gathered} 27^{x} & = 9 \\ x = log_{27} 9 \\ = \frac{log_{3} 9}{log_{3} 27} \\ = \frac{2}{3} \end{gathered}$

### How do we use logarithms to solve exponential equations?

- An exponential equation can be solved by taking logarithms of both sides
- The **laws of indices** may be needed to rewrite the equation first
- The **laws of logarithms** can then be used to solve the equation

  - **ln (log**<sub>**e**</sub>**) **is often used
  - The answer is often written in terms of ln
- A question my ask you to give your answer in a particular form
- Follow these steps to solve exponential equations

  - **STEP 1**: Take logarithms of both sides
  - **STEP 2**: Use the laws of logarithms to remove the powers
  - **STEP 3**: Rearrange to isolate *x*
  - **STEP 4**: Use logarithms to solve for *x*

### What about hidden quadratics?

- Look for hidden squared terms that could be changed to form a quadratic

  - In particular look out for terms such as
  
    - 4<sup>*x*</sup><sup> </sup>= (2<sup>2</sup>)<sup>*x*</sup><sup> </sup>= 2<sup>2</sup><sup>*x*</sup><sup> </sup>= (2<sup>*x*</sup>)<sup>2</sup>
    - e<sup> 2</sup><sup>*x*</sup><sup> </sup>= (e<sup>*2*</sup>)<sup>x </sup>= (e<sup>*x*</sup>)<sup>2</sup>

> **Exam Hint**
> - Always check which form the question asks you to give your answer in, this can help you decide how to solve it
> - If the question requires an exact value you may need to leave your answer as a logarithm

> **Worked Example**
> Solve the equation $4^{x - 3 ( 2^{x} + 1} ) + 9 = 0$.  Give your answer correct to three significant figures.
> 
> > *'Spot' the hidden quadratic by noticing that* $4^{x} = ( 2^{2} )^{x} = ( 2^{x} )^{2}$*.*
> 
> > *Rewrite the first term as a power of 2.*
> 
> $( 2^{x )^{2} - 3 ( 2^{x} + 1} ) + 9 = 0$
> 
> > *Rewrite the middle terms using the laws of indices: If* $2^{x + 1} = 2^{x} \times 2^{1} = 2 ( 2^{x} )$*     *
> 
> > * *$( 2^{x} )^{2} - 3 \times 2 ( 2^{x} ) + 9 = 0
> ( 2^{x} )^{2} - 6 ( 2^{x} ) + 9 = 0$*    *
> 
> > *USing a substitution can make this easier to solve.*
> 
> *Let* $u=2^{x}$
> 
> $( u )^{2} - 6 ( u ) + 9 = 0$
> 
> > *Factorise.*
> 
> $u^{2} - 6 u + 9 = 0
> ( u - 3 ) ( u - 3 ) = 0$
> 
> > *Solve to find **u** and substitute 2*<sup>*x* </sup>*back in.*
> 
> $\begin{gathered} u & = 3 \\ 2^{x } & = 3 \end{gathered}$
> 
> > *Solve the exponential equation 2*<sup>*x* </sup>*= 3 by taking logarithms of both sides.*
> 
> $\mathrm{ln}2^{x}=\mathrm{ln}3$
> 
> > *Bring the power down using the law of logs* $\mathrm{ln}x^{m}=m\mathrm{ln}x$*.*
> 
> $x\mathrm{ln}2=\mathrm{ln}3$
> 
> > *Rearrange and solve.*
> 
> $x=\frac{\mathrm{ln}3}{\mathrm{ln}2}=1.584...$
> 
> $x=1.58(3s.f.)$
