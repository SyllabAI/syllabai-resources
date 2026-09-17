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

`table row cell 3 to the power of 2 x end exponent end cell equals 27 row cell 3 cubed end cell equals cell 27 space space space so end cell row cell 2 x space end cell equals cell space 3 end cell row cell x space end cell equals cell space 3 over 2 end cell end table`

- The **change of base** law can also be used to solve some exponential equations

  - For example,

`table row cell 27 to the power of x space end cell equals cell space 9 blank end cell end table`

- Rewrite using the definition of a logarithm

`table row x equals cell log subscript 27 9 end cell end table`

- Then use the change of base formula from the exam formula sheet

  - Use base 3 here because 9 and 27 are both powers of 3

`table row x equals cell blank fraction numerator log subscript 3 9 over denominator log subscript 3 27 end fraction end cell row blank equals cell 2 over 3 end cell end table`

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

`table attributes columnalign right center left columnspacing 0px end attributes row cell 5 to the power of x end cell equals 27 row cell ln open parentheses 5 to the power of x close parentheses end cell equals cell ln 27 end cell end table`

- **STEP 2**
Use the laws of logarithms to move powers out of the logarithms

$x\mathrm{ln}5=\mathrm{ln}27$

- **STEP 3**
Rearrange to isolate *x*

$x=\frac{\mathrm{ln}27}{\mathrm{ln}5}$

- Note that this is the **exact solution **to the equation

- **STEP 4**
Use logarithms in your calculator to find the value of $x$

`table attributes columnalign right center left columnspacing 0px end attributes row x equals cell 2.047818... end cell row blank equals cell 2.05 space open parentheses 3 space straight s. straight f. close parentheses end cell end table`

- Only perform this step if required by the question

### What about hidden quadratics?

- Look for 'hidden' **squared terms** that could be changed to form a **quadratic**

  - In particular look out for terms such as
  
    - `4 to the power of x equals open parentheses 2 squared close parentheses to the power of x equals 2 to the power of 2 x end exponent equals open parentheses 2 to the power of x close parentheses squared`
    - `straight e to the power of 2 x end exponent equals straight e to the power of x plus x end exponent equals straight e to the power of x cross times straight e to the power of x equals open parentheses straight e to the power of x close parentheses squared`
  - This can be used to **factorise** quadratic expressions
  
    - `4 to the power of x minus 2 to the power of x equals open parentheses 2 to the power of x close parentheses squared minus 2 to the power of x equals 2 to the power of x open parentheses 2 to the power of x minus 1 close parentheses`
    - `straight e to the power of 2 x end exponent minus 4 straight e to the power of x minus 5 equals open parentheses straight e to the power of x close parentheses squared minus 4 straight e to the power of x minus 5 equals open parentheses straight e to the power of x plus 1 close parentheses open parentheses straight e to the power of x minus 5 close parentheses`

> **Exam Hint**
> - Always check which form the question asks you to give your answer in
> 
>   - This can help you decide how to solve it
> - If the question requires an exact value you may need to leave your answer as a logarithm

> **Worked Example**
> Solve the equation `4 to the power of x minus 3 open parentheses 2 to the power of x plus 1 end exponent close parentheses plus blank 9 equals 0`.  Give your answer correct to three significant figures.
> 
> > *Spot the hidden quadratic:  *`4 to the power of x equals open parentheses 2 squared close parentheses to the power of x equals 2 to the power of 2 x end exponent equals open parentheses 2 to the power of x close parentheses squared`
> 
> > *Also note that  *$2^{x+1}=2^{1}\times2^{x}=2\times2^{x}$
> 
> > *Substitute these into the equation and simplify*
> 
> `table row cell open parentheses 2 to the power of x close parentheses squared minus 3 open parentheses 2 cross times 2 to the power of x close parentheses plus 9 end cell equals 0 row cell open parentheses 2 to the power of x close parentheses squared minus 6 open parentheses 2 to the power of x close parentheses plus 9 end cell equals 0 end table`
> 
> > *Factorise the quadratic*
> 
> > *The left-hand side is in the form  *$y^{2}-6y+9$*  where *$y=2^{x}$* *
> *This factorises to *`open parentheses y minus 3 close parentheses squared`
> 
> `open parentheses 2 to the power of x minus 3 close parentheses squared equals 0`
> 
> > *Solve for *$2^{x}$
> 
> `table row cell 2 to the power of x minus 3 end cell equals 0 row cell 2 to the power of x end cell equals 3 end table`
> 
> > *Take logarithms of both sides*
> 
> `ln open parentheses 2 to the power of x close parentheses equals ln 3`
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
> **Once **$2^{x}=3$** is found, the logarithm **`x equals log subscript 2 open parentheses 3 close parentheses`** could be used instead to find the value of **$x$** **
