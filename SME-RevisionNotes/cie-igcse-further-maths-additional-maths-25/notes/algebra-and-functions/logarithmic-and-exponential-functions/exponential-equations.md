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

`table row cell 5 to the power of 2 x end exponent end cell equals 125 row cell 2 x space end cell equals cell space 3 end cell row cell x space end cell equals cell space 3 over 2 end cell end table`

- In more complicated cases the laws of logarithms should be used to solve exponential equations

- The **change of base** law can be used to solve some exponential equations without a calculator

  - For example,

`table row cell 27 to the power of x space end cell equals cell space 9 end cell row x equals cell log subscript 27 9 end cell row blank equals cell blank fraction numerator log subscript 3 9 over denominator log subscript 3 27 end fraction end cell row blank equals cell 2 over 3 blank end cell end table`

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
> Solve the equation `4 to the power of x minus 3 open parentheses 2 to the power of x plus 1 end exponent close parentheses plus blank 9 equals 0`.  Give your answer correct to three significant figures.
> 
> > *'Spot' the hidden quadratic by noticing that *`4 to the power of x space equals space open parentheses 2 squared close parentheses to the power of x space equals space open parentheses 2 to the power of x close parentheses squared`*.*
> 
> > *Rewrite the first term as a power of 2.*
> 
> `open parentheses 2 to the power of x close parentheses squared space minus space 3 open parentheses 2 to the power of x space plus space 1 end exponent close parentheses space plus space 9 space equals space 0`
> 
> > *Rewrite the middle terms using the laws of indices: If  *`2 to the power of x plus 1 end exponent space equals space 2 to the power of x space cross times space 2 to the power of 1 space equals space 2 open parentheses 2 to the power of x close parentheses`*     *
> 
> > * *`open parentheses 2 to the power of x close parentheses squared space minus space 3 cross times 2 open parentheses 2 to the power of x close parentheses space plus space 9 space equals space 0
> open parentheses 2 to the power of x close parentheses squared space minus space 6 open parentheses 2 to the power of x close parentheses space plus space 9 space equals space 0`*    *
> 
> > *USing a substitution can make this easier to solve. *
> 
> *Let *$u=2^{x}$
> 
> `open parentheses u close parentheses squared space minus space 6 open parentheses u close parentheses space plus space 9 space equals space 0`
> 
> > *Factorise.*
> 
> `u squared space minus space 6 u space plus space 9 space equals space 0
> open parentheses u space minus space 3 close parentheses open parentheses u space minus space 3 close parentheses space equals space 0`
> 
> > *Solve to find **u** and substitute 2*<sup>*x *</sup>*back in.*
> 
> `table row cell u space end cell equals cell space 3 end cell row cell 2 to the power of x space end exponent end cell equals cell space 3 end cell end table`
> 
> > *Solve the exponential equation 2*<sup>*x *</sup>*= 3 by taking logarithms of both sides.*
> 
> $\mathrm{ln}2^{x}=\mathrm{ln}3$
> 
> > *Bring the power down using the law of logs *$\mathrm{ln}x^{m}=m\mathrm{ln}x$*.*
> 
> $x\mathrm{ln}2=\mathrm{ln}3$
> 
> > *Rearrange and solve. *
> 
> $x=\frac{\mathrm{ln}3}{\mathrm{ln}2}=1.584...$
> 
> $x=1.58(3s.f.)$
