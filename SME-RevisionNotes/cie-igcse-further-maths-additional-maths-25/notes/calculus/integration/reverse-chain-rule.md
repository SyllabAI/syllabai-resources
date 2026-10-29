---
note_id: "rn_jB7byhHQQZ27z58W"
title: "Reverse Chain Rule"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/calculus/integration/reverse-chain-rule
path: calculus/integration/reverse-chain-rule
updated_at: "2026-07-02T08:19:38.536Z"
spec_point_ids: ["spcpt_r82JktHqvqwp3wHw", "spcpt_Zndqd25fHNYPKVMZ"]
spec_point_codes: []
guided_study: false
---

# Reverse Chain Rule

## Reverse Chain Rule

> **Spec point** — `spcpt_r82JktHqvqwp3wHw`

## Reverse chain rule

### What is the reverse chain rule?

- The **Chain Rule** is a way of differentiating two (or more) functions
- The **Reverse** **Chain** **Rule** (RCR) refers to **integrating** by **inspection**

  - Spotting that chain rule would be used in the reverse (differentiating) process

### How do I know when to use the reverse chain rule?

- The **reverse** **chain** **rule** is used when we have the **product** of a **composite** **function** and the **derivative** of its **second** **function**
- Integration is trickier than differentiation; many of the shortcuts do not work

  - For example, in general $\int \mathrm{e}^{ \mathrm{f} ( x )} \mathrm{d} x \text{eq} \frac{1}{ \mathrm{f} ' ( x )} \mathrm{e}^{ \mathrm{f} ( x )}$
  - However, this result **is true** if$f(x)$ is linear$(ax+b)$
- Formally, in **function** **notation**, the **reverse** **chain** **rule** is used for **integrands** of the form

$I = \int g^{'} ( x ) f^{'} ( g ( x ) ) \mathrm{d} x$

- This does not have to be strictly true, but ‘*algebraically’* it should be
- If the **coefficients** do not match ‘**adjust** and **compensate’** can be used

  - For example, $e^{x^{2}}$ differentiates to $2xe^{x^{2}}$ with the  chain rule
  
    - so$\int 2 x \mathrm{e}^{x^{2}} \mathrm{d} x = \mathrm{e}^{x^{2}} + c$ with the reverse chain rule
  - But to do $\int 5 x \mathrm{e}^{x^{2}} \mathrm{d} x$  we need to:
  
    - **Take out** the five: $5 \int x \mathrm{e}^{x^{2}} \mathrm{d} x$
    - Force a 2 inside (**adjust**) and divide the outside by a 2 (**compensate**): $\frac{5}{2} \int 2 x \mathrm{e}^{x^{2}} \mathrm{d} x$
    - The bit inside the integral is now a reverse chain rule
    - The answer is $\frac{5}{2}e^{x^{2}}+c$
- A particularly useful instance of the reverse chain rule to recognise is

$I = \int \frac{f ' ( x )}{f ( x )} \mathrm{d} x = \ln \vert f ( x ) \vert + c$

- i.e.  the **numerator** is (almost) the **derivative** of the **denominator**

  - '**adjust** and **compensate**' may need to be used to deal with any coefficients
  
    - e.g.  $I = \int \frac{x^{2} + 1}{x^{3} + 3 x} \mathrm{d} x = 1 \frac{1}{3} \int 3 \frac{x^{2} + 1}{x^{3} + 3 x} \mathrm{d} x = 1 \frac{1}{3} \int \frac{3 x^{2} + 3}{x^{3} + 3 x} \mathrm{d} x = 1 \frac{1}{3} \ln \vert x^{3} + 3 x \vert + c$

> **Exam Hint**
> - You can always check your work by differentiating, if you have time

> **Worked Example**
> A curve has the gradient function$f'(x)=5x^{2}\mathrm{sin}(2x^{3})$.
> 
> Given that the curve passes through the point$(0,1)$, find an expression for$f(x)$.
> 
> > *Write f(**x**)** **as an integral.*
> 
> $\mathrm{f} ( x ) = \int 5 x^{2} \sin ( 2 x^{3} ) \mathrm{d} x$
> 
> > *Take 5 out of the integral as a factor.*
> 
> $\mathrm{f} ( x ) = 5 \int x^{2} \sin ( 2 x^{3} ) \mathrm{d} x$
> 
> > *The main function is sin(...), which would have come from -cos(...).*
> 
> > *Adjust and compensate the coefficients. 2**x*<sup>*3*</sup><sup>* *</sup>*would differentiate to 6**x*<sup>*2* </sup>*so -cos(2**x*<sup>*3*</sup>*) would differentiate to (6**x*<sup>*2*</sup>*)sin(2x*<sup>*3*</sup>*)*
> 
> $\mathrm{f} ( x ) = 5 \times ( \frac{1}{6} ) \times \int ( 6 x^{2} ) \sin ( 2 x^{3} ) \mathrm{d} x$
> 
> > *Integrate.*
> 
> $\mathrm{f} ( x ) = ( \frac{5}{6} ) \times - \cos ( 2 x^{3} ) + c$
> 
> $f(x)=-\frac{5}{6}\mathrm{cos}(2x^{3})+c$

## Integrating Composite Functions (ax+b)

> **Spec point** — `spcpt_Zndqd25fHNYPKVMZ`

## Integrating composite functions (ax+b)

### What is a composite function?

- A **composite** **function** involves one function being applied after another
- A composite function may be described as a “function of a function”
- This Revision Note focuses on one of the functions being **linear** – i.e. of the form$ax+b$

### How do I integrate linear (ax+b) functions?

- The reverse chain rule can be used for integrating functions in the form y = (*ax* + *b*)<sup>n</sup>

  - Make sure you are confident using **the chain rule** to **differentiate **functions in the form y = (*ax* + *b*)<sup>n</sup>
  - The reverse chain rule works backwards
- For *n = 2* you will most likely **expand the brackets** and **integrate each term separately**
- If *n > 2* this becomes **time-consuming** and if *n* is not a positive integer we need a different method completely
- To use the **reverse chain rule** $\int ( a x + b )^{n} d x$(provided *n* is not -1)

  - **Raise** the **power of *****n***** by 1**
  - **Divide** by this **new power**
  - **Divide** this whole function by the **coefficient of *****x***
  
    - $\int ( a x + b )^{n \mathrm{d} x = \frac{( a x + b )^{n} + 1} }{n + 1} \times \frac{1}{a} + c$
- You can **check your answer by differentiating it**

  - You should get the original function when you differentiate your answer
- Note that this method **only works** when the function in the brackets is **linear (*****ax***** + *****b*****)**
- The special cases for **trigonometric** **functions** and **exponential** and **logarithmic** **functions** are

  - ** **$\int \sin ( a x + b ) \mathrm{d} x = - \frac{1}{a} \cos ( a x + b ) + c$
  - ** **$\int \cos ( a x + b ) \mathrm{d} x = \frac{1}{a} \sin ( a x + b ) + c$
  - $\int \mathrm{e}^{a x + b} \mathrm{d} x = \frac{1}{a} \mathrm{e}^{a x + b} + c$
  - $\int \frac{1}{a x + b} \mathrm{d} x = \frac{1}{a} \ln \left| a x + b \right| + c$
- $c$, in all cases, is the **constant** of **integration**
- All the above can be deduced using **reverse** **chain** **rule**

  - However, spotting them can make solutions more efficient

> **Worked Example**
> Find the following integrals
> 
> a)      $\int 3 ( 7 - 2 x )^{ \frac{5}{3} } \mathrm{d} x$
> 
> > *Name the integral.*
> 
> $I = \int 3 ( 7 - 2 x )^{ \frac{5}{3} } \mathrm{d} x = 3 \int ( 7 - 2 x )^{ \frac{5}{3} } \mathrm{d} x$
> 
> > *Using the rule 'raise the power by one, divide by the new power and then multiply by the reciprocal of the derivative' integrate the expression.*
> 
> $I = 3 [ \frac{1}{\frac{8}{3}} ( 7 - 2 x ) ^{\frac{8}{3}} \times \frac{1}{ - 2} ] + c$
> 
> > *Simplify.*
> 
> $I = 3 [ - \frac{3}{16} ( 7 - 2 x )^{ \frac{8}{3} } ] + c$
> 
> $I=-\frac{9}{16}(7-2x)^{\frac{8}{3}}+c$
> 
> b)      $\int 1 \frac{1}{2} \cos ( 3 x - 2 ) \mathrm{d} x$
> 
> > *Name the integral.*
> 
> $I = \int 1 \frac{1}{2} \cos ( 3 x - 2 ) \mathrm{d} x = 1 \frac{1}{2} \int \cos ( 3 x - 2 ) \mathrm{d} x$
> 
> > *Using the rule* $\int \cos ( a x + b ) \mathrm{d} x = \frac{1}{a} \sin ( a x + b ) + c$*, integrate the expression.*
> 
> $I = 1 \frac{1}{2} [ 1 \frac{1}{3} \sin ( 3 x - 2 ) ] + c$
> 
> > *Simplify.*
> 
> $I=\frac{1}{6}\mathrm{sin}(3x-2)+c$
