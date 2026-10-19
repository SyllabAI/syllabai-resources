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

  - `space integral x to the power of n space straight d x equals fraction numerator x to the power of n plus 1 end exponent over denominator n plus 1 end fraction plus c`  (where$c$ is the **constant** of **integration**)
  
    - This is valid for any value of $n$ **except** $n=-1$
    - So you cannot integrate  `integral x to the power of negative 1 end exponent space straight d x equals integral 1 over x space straight d x` this way

- If $x^{n}$ is **multiplied by a constant** $a$ then

  - `space integral a x to the power of n space straight d x equals a integral x to the power of n space straight d x equals fraction numerator a x to the power of n plus 1 end exponent over denominator n plus 1 end fraction plus c`
  
    - This also is **not valid** for $n=-1$
- These formulae are **not** on the exam formula sheet, so you need to remember them
- Remember the **special case:**

  - `space integral a space straight d x equals a x plus c`
  
    - e.g. `space integral 4 space straight d x equals 4 x plus c`
  - This allows **constant** terms to be integrated
- Functions involving **roots** will need to be rewritten as **fractional powers**

  - e.g. `integral cube root of x space straight d x`
  
    - rewrite `cube root of x` as $x^{\frac{1}{3}}$
    - then integrate
- **Fractions** with $x$ in the **denominator** will need to be rewritten as **negative powers**

  - e.g. `integral 1 over x squared space straight d x`
  
    - rewrite $\frac{1}{x^{2}}$ as $x^{-2}$
    - then integrate

### How do I integrate sums and differences of powers of x?

- The formulae can be used to integrate **sums or differences** of powers of$x$

  - Just integrate **term by term**
  
    - e.g. `integral open parentheses 8 x cubed minus 2 x plus 4 close parentheses blank straight d x`
    - $=\frac{8x^{3+1}}{3+1}-\frac{2x^{1+1}}{1+1}+4x+c$
    - $=2x^{4}-x^{2}+4x+c$
- **Products** and **quotients** cannot be integrated this way

  - You need to **expand** and/or **simplify** first
  
    - e.g. `integral 8 x squared open parentheses 2 x minus 3 close parentheses space straight d x`
    - expand `8 x squared open parentheses 2 x minus 3 close parentheses` as $16x^{3}-24x^{2}$
    - then integrate term by term
    - you **cannot** just multiply the integrals of $8x^{2}$ and $2x-3$ together

### What might I be asked to do once I’ve integrated?

- You may be given the **derivative** of a function and asked to **find** the function

  - Integration and differentiation are **inverse** operations so
  
    - `integral straight f to the power of apostrophe open parentheses x close parentheses space straight d x equals straight f open parentheses x close parentheses plus c`
    - `integral fraction numerator straight d y over denominator straight d x end fraction space straight d x equals y plus c`
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
> > *Start by rewriting *$\frac{dy}{dx}$*entirely in powers of *$x$
> 
> > *By laws of indices  *$\frac{1}{\sqrt{x}}=x^{-\frac{1}{2}}$
> 
> $\frac{dy}{dx}=2x^{2}+3-x^{-\frac{1}{2}}$
> 
> > *Remember  *`integral fraction numerator straight d y over denominator straight d x end fraction space straight d x equals y plus c`
> 
> > *We can integrate term by term using  *`space integral a x to the power of n space straight d x equals fraction numerator a x to the power of n plus 1 end exponent over denominator n plus 1 end fraction plus c`
> 
> `table row y equals cell integral open parentheses 2 x squared plus 3 minus x to the power of negative 1 half end exponent close parentheses space straight d x end cell row blank equals cell 2 open parentheses fraction numerator x to the power of 2 plus 1 end exponent over denominator 2 plus 1 end fraction close parentheses plus 3 x minus fraction numerator x to the power of negative 1 half plus 1 end exponent over denominator negative 1 half plus 1 end fraction plus c end cell row blank equals cell 2 open parentheses x cubed over 3 close parentheses plus 3 x minus fraction numerator x to the power of 1 half end exponent over denominator 1 half end fraction plus c end cell row blank equals cell 2 over 3 x cubed plus 3 x minus 2 x to the power of 1 half end exponent plus c end cell end table`
> 
> > *We can't find the value of *$c$* without further info, so that's the answer to the question*
> 
> > *It's 'nice' to turn *$x^{\frac{1}{2}}$* back into*$\sqrt{x}$* for the final answer, but you would also get the marks without doing that*
> 
> $y=\frac{2}{3}x^{3}+3x-2\sqrt{x}+c$

## Integrating Trig Functions

> **Spec point** — `spcpt_3RJndX5xhQSKbn6K`

## Integrating Trig Functions

### How do I integrate sin and cos?

- You can **integrate** $\mathrm{sin}x$ and $\mathrm{cos}x$ by using the formulae

  - `bold integral bold sin bold space bold italic x bold space bold d bold italic x bold equals bold minus bold cos bold space bold italic x bold plus bold italic c`
  - `bold integral bold cos bold space bold italic x bold space bold d bold italic x bold equals bold sin bold space bold italic x bold plus bold italic c`
  
    - $c$ is the **constant** **of** **integration**

- If $x$ is **multiplied by a constant** $a$ then

  - `bold integral bold sin bold space bold italic a bold italic x bold space bold d bold italic x bold equals bold minus bold 1 over bold italic a bold cos bold space bold italic a bold italic x bold plus bold italic c`
  - `bold integral bold cos bold space bold italic a bold italic x bold space bold d bold italic x bold equals bold 1 over bold italic a bold sin bold space bold italic a bold italic x bold plus bold italic c`

- **None of these formulae** are on the exam formula sheet, so you need to remember them
- For calculus with trigonometric functions angles** must** be measured in **radians**

  - Make sure you know how to change the angle mode on your **calculator**

> **Exam Hint**
> - Remember to include 'c', the constant of integration, for any indefinite integrals
> - As soon as you see a question involving integration and trigonometry
> 
>   - put your calculator into radians mode

> **Worked Example**
> Given that  `straight f to the power of apostrophe open parentheses x close parentheses equals 4 cos 3 x minus 1 half sin 2 x`, find an expression for `straight f open parentheses x close parentheses` in terms of $x$.
> 
> > *Remember that  *`integral straight f to the power of apostrophe open parentheses x close parentheses space straight d x italic equals straight f stretchy left parenthesis x stretchy right parenthesis italic plus c`
> 
> > *We can integrate term by term using the integration formulae for *$\mathrm{sin}ax$* and *$\mathrm{cos}ax$
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row cell straight f open parentheses x close parentheses end cell equals cell integral open parentheses 4 cos 3 x minus 1 half sin 2 x close parentheses space straight d x end cell row blank equals cell 4 open parentheses 1 third sin 3 x close parentheses minus 1 half open parentheses negative 1 half cos 2 x close parentheses plus c end cell row blank equals cell 4 over 3 sin 3 x plus 1 fourth cos 2 x plus c end cell end table`
> 
> > *We can't find the value of *$c$* without further info, so that's the answer to the question*
> 
> $f(x)=\frac{4}{3}\mathrm{sin}3x+\frac{1}{4}\mathrm{cos}2x+c$

## Integrating e^x

> **Spec point** — `spcpt_D2njzcMRRFh4dvQn`

## Integrating e^x

### How do I integrate exponentials?

- $e^{x}$ can be integrated using the **formula**

  - `bold integral bold space bold e to the power of bold italic x bold space bold d bold italic x bold equals bold space bold e to the power of bold italic x bold plus bold italic c`
  
    - $c$ is the **constant** **of** **integration**
- If $x$ is **multiplied by a constant** $a$ then

  - ** **`bold integral bold e to the power of bold italic a bold italic x end exponent bold space bold d bold italic x bold equals bold 1 over bold italic a bold e to the power of bold italic a bold italic x end exponent bold plus bold italic c`

- These formulae are **not** on the exam formula sheet, so you need to remember them

> **Exam Hint**
> - Because '$e^{x}$ is its own integral' it is quite easy to integrate exponentials
> 
>   - Just be careful dealing with the constant in $e^{ax}$

> **Worked Example**
> Given that  `straight f to the power of apostrophe open parentheses x close parentheses equals fraction numerator straight e to the power of 2 x end exponent minus straight e to the power of negative 3 x end exponent over denominator 2 end fraction`, find an expression for `straight f open parentheses x close parentheses` in terms of $x$.
> 
> > *Remember that  *`integral straight f to the power of apostrophe open parentheses x close parentheses space straight d x italic equals straight f stretchy left parenthesis x stretchy right parenthesis italic plus c`
> 
> > *We can integrate term by term using the integration formula for *$e^{ax}$
> 
> > *You might find it easier to split the fraction into two separate fractions first*
> 
> `table row cell straight f open parentheses x close parentheses end cell equals cell integral open parentheses 1 half straight e to the power of 2 x end exponent minus 1 half straight e to the power of negative 3 x end exponent close parentheses space straight d x end cell row blank equals cell 1 half open parentheses 1 half straight e to the power of 2 x end exponent close parentheses minus 1 half open parentheses fraction numerator 1 over denominator negative 3 end fraction straight e to the power of negative 3 x end exponent close parentheses plus c end cell row blank equals cell 1 fourth straight e to the power of 2 x end exponent plus 1 over 6 straight e to the power of negative 3 x end exponent plus c end cell end table`
> 
> > *We can't find the value of *$c$* without further info, so that's the answer to the question*
> 
> $f(x)=\frac{1}{4}e^{2x}+\frac{1}{6}e^{-3x}+c$
