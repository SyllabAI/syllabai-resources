---
note_id: "rn_dmX9FXM3mGpB3hgS"
title: "Solving Exponential Equations"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/logarithms-indices-and-surds/logarithms-indices-and-exponentials/solving-exponential-equations
path: logarithms-indices-and-surds/logarithms-indices-and-exponentials/solving-exponential-equations
updated_at: "2024-10-16T16:32:44.533Z"
spec_point_ids: ["spcpt_HbVkSMycJQ7Bw5Zw"]
spec_point_codes: []
guided_study: false
---

# Solving Exponential Equations

## Solving Exponential Equations

> **Spec point** — `spcpt_HbVkSMycJQ7Bw5Zw`

## Solving Exponential Equations

### What are exponential equations?

- An **exponential equation** is an equation where the unknown is in a **power**
- In simple cases the solution can be spotted without the use of a calculator

  - For example,

$\begin{gathered} 3^{2 x} & = 27 \\ 3^{3} & = 27 \text{so} \\ 2 x & = 3 \\ x & = \frac{3}{2} \end{gathered}$

- The **change of base** law can also be used to solve some exponential equations

  - For example,

$\begin{gathered} 27^{x} & = 9 \end{gathered}$

- Rewrite using the definition of a logarithm

$\begin{gathered} x = log_{27} 9 \end{gathered}$

- Then use the change of base formula from the exam formula sheet

  - Use base 3 here because 9 and 27 are both powers of 3

$\begin{gathered} x = \frac{log_{3} 9}{log_{3} 27} \\ = \frac{2}{3} \end{gathered}$

- In **more complicated** cases use the **laws of logarithms** to solve exponential equations

### How do I use logarithms to solve exponential equations?

- An exponential equation can be solved by **taking logarithms** of both sides

  - $\mathrm{ln}$,** **or** **$\mathrm{log}_{e}$,** **is often used
  
    - Though a log to any base could be used
  - The **laws of indices** may be needed to rewrite the equation first
  - The **laws of logarithms** can then be used to solve the equation
  - A question may ask you to give your answer in a **particular form**
  
    - For example as an **exact value** in terms of $\mathrm{ln}$
- **STEP 1**
Take logarithms of both sides

$\begin{array}{rcl} 5^{x} & = 27 \\ \ln ( 5^{x} ) & = \ln 27 \end{array}$

- **STEP 2**
Use the laws of logarithms to move powers out of the logarithms

$x\mathrm{ln}5=\mathrm{ln}27$

- **STEP 3**
Rearrange to isolate *x*

$x=\frac{\mathrm{ln}27}{\mathrm{ln}5}$

- Note that this is the **exact solution **to the equation

- **STEP 4**
Use logarithms in your calculator to find the value of $x$

$\begin{array}{rcl} x = 2.047818... \\ = 2.05 ( 3 \mathrm{s} . \mathrm{f} . ) \end{array}$

- Only perform this step if required by the question

### What about hidden quadratics?

- Look for 'hidden' **squared terms** that could be changed to form a **quadratic**

  - In particular look out for terms such as
  
    - $4^{x = ( 2^{2} )^{x} = 2^{2} x} = ( 2^{x} )^{2}$
    - $\mathrm{e}^{2 x} = \mathrm{e}^{x + x} = \mathrm{e}^{x} \times \mathrm{e}^{x} = ( \mathrm{e}^{x} )^{2}$
  - This can be used to **factorise** quadratic expressions
  
    - $4^{x} - 2^{x} = ( 2^{x} )^{2} - 2^{x} = 2^{x} ( 2^{x} - 1 )$
    - $\mathrm{e}^{2 x} - 4 \mathrm{e}^{x} - 5 = ( \mathrm{e}^{x} )^{2} - 4 \mathrm{e}^{x} - 5 = ( \mathrm{e}^{x} + 1 ) ( \mathrm{e}^{x} - 5 )$

> **Exam Hint**
> - Always check which form the question asks you to give your answer in
> 
>   - This can help you decide how to solve it
> - If the question requires an exact value you may need to leave your answer as a logarithm

> **Worked Example**
> Solve the equation $4^{x - 3 ( 2^{x} + 1} ) + 9 = 0$.  Give your answer correct to three significant figures.
> 
> > *Spot the hidden quadratic:  *$4^{x = ( 2^{2} )^{x} = 2^{2} x} = ( 2^{x} )^{2}$
> 
> > *Also note that  *$2^{x+1}=2^{1}\times2^{x}=2\times2^{x}$
> 
> > *Substitute these into the equation and simplify*
> 
> $\begin{gathered} ( 2^{x} )^{2} - 3 ( 2 \times 2^{x} ) + 9 & = 0 \\ ( 2^{x} )^{2} - 6 ( 2^{x} ) + 9 & = 0 \end{gathered}$
> 
> > *Factorise the quadratic*
> 
> > *The left-hand side is in the form  *$y^{2}-6y+9$*  where *$y=2^{x}$* *
> *This factorises to *$( y - 3 )^{2}$
> 
> $( 2^{x} - 3 )^{2} = 0$
> 
> > *Solve for *$2^{x}$
> 
> $\begin{gathered} 2^{x} - 3 & = 0 \\ 2^{x} & = 3 \end{gathered}$
> 
> > *Take logarithms of both sides*
> 
> $\ln ( 2^{x} ) = \ln 3$
> 
> > *Use  *$\mathrm{log}_{a}x^{k}=k\mathrm{log}_{a}x$*  to take the power out of the logarithm*
> 
> > *Remember that  *$\mathrm{ln}=\mathrm{log}_{e}$
> 
> $x\mathrm{ln}2=\mathrm{ln}3$
> 
> > *Solve for *$x$
> 
> $x=\frac{\mathrm{ln}3}{\mathrm{ln}2}$
> 
> > *Use your calculator to find the decimal equivalent of that exact answer*
> 
> $x=1.584962...$
> 
> > *Round to 3 significant figures*
> 
> $x=1.58$ **(3 s.f.)**
> 
> **Once **$2^{x}=3$** is found, the logarithm **$x = log_{2} ( 3 )$** could be used instead to find the value of **$x$** **
