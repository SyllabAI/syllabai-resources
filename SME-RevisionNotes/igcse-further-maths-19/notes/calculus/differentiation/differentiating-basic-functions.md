---
note_id: "rn_zYGSdvYtzd5NYsMB"
title: " Differentiating Basic Functions"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/calculus/differentiation/differentiating-basic-functions
path: calculus/differentiation/differentiating-basic-functions
updated_at: "2024-10-20T15:15:35.583Z"
spec_point_ids: ["spcpt_WF2fQCGtJgftqVQg", "spcpt_BGg7StnV5sBwkBDx", "spcpt_5gZxgh7z7kWnnc2Y"]
spec_point_codes: []
guided_study: false
---

#  Differentiating Basic Functions

## Differentiating Powers of x

> **Spec point** — `spcpt_WF2fQCGtJgftqVQg`

## Differentiating Powers of x

### What is differentiation?

- **Differentiation** is the process of finding the **derivative** (**gradient** **function**) of a function

### How do I differentiate powers of x?

- **Powers of **$x$ are **differentiated** according to the following formula:

  - If$f(x)=x^{n}$ then$f'(x)=nx^{n-1}$
  
    - Bring the power down in front as a **multiplier**
    - Then** subtract 1** from the power
  - This formula is **not** on the exam formula sheet, so you need to remember it
- If the power of $x$ term is **multiplied** **by a** **constant **$a$

  - then the derivative is **also** multiplied by that constant
  
    - If $f(x)=ax^{n}$  then $f^{'}(x)=anx^{n-1}$
- The **alternative notation** (to$f^{'}(x)$) is to use $\frac{dy}{dx}$

  - If $y=ax^{n}$ then $\frac{dy}{dx}=anx^{n-1}$
- Don't forget these **two** **special cases**:

  - If$f(x)=ax$ then$f^{'}(x)=a$
  
    - e.g.  If $y=6x$ then $\frac{dy}{dx}=6$
  - If$f(x)=a$ then$f^{'}(x)=0$
  
    - e.g.  If $y=5$  (or if $y$ equals any constant) then $\frac{dy}{dx}=0$
- Functions involving **roots** will need to be rewritten as **fractional powers**

  - e.g.  $f(x)=2\sqrt{x}$
  
    - rewrite as$f(x)=2x^{\frac{1}{2}}$
    - then differentiate
- Functions involving **fractions** with $x$ in the **denominator** will need to be rewritten as **negative powers**

  - e.g.  $f(x)=\frac{4}{x}$
  
    - rewrite as$f(x)=4x^{-1}$
    - then differentiate

### How do I differentiate sums and differences of powers of x?

- The formulae can be used to differentiate **sums** or **differences** of **powers** of $x$

  - Just differentiate term by term
  
    - e.g. $f(x)=5x^{4}-3x^{\frac{2}{3}}+4$
    - `table row cell straight f apostrophe left parenthesis x right parenthesis end cell equals cell 5 cross times 4 x to the power of 4 minus 1 end exponent minus 3 cross times 2 over 3 x to the power of 2 over 3 minus 1 end exponent plus 0 end cell end table`
    - `table row cell straight f apostrophe left parenthesis x right parenthesis end cell equals cell 20 x cubed minus 2 x to the power of negative 1 third end exponent end cell end table`
- **Products** and **quotients cannot** be differentiated in this way

  - These need to be **expanded/simplifying** first
  
    - e.g.  $f(x)=(2x-3)(x^{2}-4)$
    - Expand to$f(x)=2x^{3}-3x^{2}-8x+12$
    - Then differentiate term by term
    - You **can't** just multiply the derivatives of $2x-3$ and $x^{2}-4$ together!
  - These can also be differentiated using the **product rule** or **quotient rule**

> **Exam Hint**
> - Be careful with negative and fractional powers
> - It's easy to make a mistake when subtracting 1 from these

> **Worked Example**
> The function$f(x)$ is given by
> 
> $f(x)=2x^{3}+\frac{4}{\sqrt{x}}$,  where $x>0$
> 
> Find the derivative of `straight f open parentheses x close parentheses`.
> 
> > *Start by rewriting the *$\frac{4}{\sqrt{x}}$* term as a power of *$x$
> 
> > *By laws of indices, *$\frac{1}{\sqrt{x}}=x^{-\frac{1}{2}}$
> 
> `straight f open parentheses x close parentheses equals 2 x cubed plus 4 x to the power of negative 1 half end exponent`
> 
> > *Now differentiate as powers of *$x$
> 
> `table row cell straight f to the power of apostrophe open parentheses x close parentheses end cell equals cell 2 open parentheses 3 x to the power of 3 minus 1 end exponent close parentheses plus 4 open parentheses negative 1 half x to the power of negative 1 half minus 1 end exponent close parentheses end cell row blank equals cell 2 open parentheses 3 x squared close parentheses plus 4 open parentheses negative 1 half x to the power of negative 3 over 2 end exponent close parentheses end cell row blank equals cell 6 x squared minus 2 x to the power of negative 3 over 2 end exponent end cell end table`
> 
> $f^{'}(x)=6x^{2}-2x^{-\frac{3}{2}}$

## Differentiating Trig Functions

> **Spec point** — `spcpt_BGg7StnV5sBwkBDx`

## Differentiating Trig Functions

### How do I differentiate sin and cos?

- The derivative of  $y=\mathrm{sin}x$  is  $\frac{dy}{dx}=\mathrm{cos}x$ ** **
- The derivative of is  $y=\mathrm{cos}x$  is  $\frac{dy}{dx}=-\mathrm{sin}x$
- If $x$ is **multiplied by a constant** $a$ then

  - the derivative of  $y=\mathrm{sin}ax$  is  $\frac{dy}{dx}=a\mathrm{cos}ax$
  - the derivative of  $y=\mathrm{cos}ax$  is  $\frac{dy}{dx}=-a\mathrm{sin}ax$
  
    - These can be derived by using the **chain rule**
    - but it's easier (and quicker) just to **remember** them
- **None of these formulae** are on the exam formula sheet, so you need to remember them
- For calculus with trigonometric functions angles **must** be measured in **radians**

  - Make sure you know how to change the angle mode on your **calculator**

> **Exam Hint**
> - As soon as you see a question involving differentiation and trigonometry
> 
>   - put your calculator into radians mode

> **Worked Example**
> (a) Given the function `straight f open parentheses x close parentheses equals cos 5 x`, find $f^{'}(x)$.
> 
> > *Use  *$y=\mathrm{cos}ax\Rightarrow\frac{dy}{dx}=-a\mathrm{sin}ax$*  with  *$a=5$
> 
> $f^{'}(x)=-5\mathrm{sin}5x$
> 
> (b) A curve has the equation $y=3\mathrm{sin}\frac{x}{2}$.
> Find the gradient of the curve at the point where  $x=\frac{π}{3}$, giving your answer as an exact value.
> 
> > *Start by finding *$\frac{dy}{dx}$
> 
> > *Use  *$y=\mathrm{sin}ax\Rightarrow\frac{dy}{dx}=a\mathrm{cos}ax$*  with  *$a=\frac{1}{2}$
> 
> `fraction numerator straight d y over denominator straight d x end fraction equals 3 open parentheses 1 half cos x over 2 close parentheses equals 3 over 2 cos x over 2`
> 
> > *Substitute *$x=\frac{π}{3}$* into *$\frac{dy}{dx}$* to find the gradient*
> 
> `gradient equals 3 over 2 cos open parentheses fraction numerator open parentheses pi over 3 close parentheses over denominator 2 end fraction close parentheses equals 3 over 2 cos pi over 6 equals 3 over 2 open parentheses fraction numerator square root of 3 over denominator 2 end fraction close parentheses equals fraction numerator 3 square root of 3 over denominator 4 end fraction`
> 
> $\frac{3\sqrt{3}}{4}$

## Differentiating e^x

> **Spec point** — `spcpt_5gZxgh7z7kWnnc2Y`

## Differentiating e^x

### How do I differentiate exponentials?

- The derivative of  $y=e^{x}$  is  $\frac{dy}{dx}=e^{x}$

  - Note that $e^{x}$ is its own derivative!
- If $x$ is **multiplied by a constant** $a$ then

  - the derivative of  $y=e^{ax}$  is  $\frac{dy}{dx}=ae^{ax}$
  
    - This can be derived by using the **chain rule**
    - but it's easier (and quicker) just to **remember** it

> **Exam Hint**
> - Remember this is not a 'powers of $x$' differentiation
> 
>   - the derivative of $e^{kx}$ is $ke^{kx}$, NOT $kxe^{kx-1}$

> **Worked Example**
> A curve has the equation$y=2e^{-3x}$.
> 
> Find the gradient of the curve at the point where$x=\frac{1}{2}$, giving your answer correct to 3 significant figures.
> 
> > *Differentiate using *$y=e^{ax}\Rightarrow\frac{dy}{dx}=ae^{ax}$
> 
> `fraction numerator straight d y over denominator straight d x end fraction equals 2 open parentheses negative 3 straight e to the power of negative 3 x end exponent close parentheses equals negative 6 straight e to the power of negative 3 x end exponent`
> 
> > *Substitute *$x=\frac{1}{2}$* into *$\frac{dy}{dx}$* to find the gradient*
> 
> `gradient equals negative 6 straight e to the power of negative 3 open parentheses 1 half close parentheses end exponent equals negative 6 straight e to the power of negative 3 over 2 end exponent`
> 
> > *Note that  *$-6e^{-\frac{3}{2}}=-\frac{6}{e\sqrt{e}}$*  is the exact value answer*
> 
> > *Use a calculator to find the decimal version*
> 
> $-6e^{-\frac{3}{2}}=-1.338780...$
> 
> $-1.34(3s.f.)$
