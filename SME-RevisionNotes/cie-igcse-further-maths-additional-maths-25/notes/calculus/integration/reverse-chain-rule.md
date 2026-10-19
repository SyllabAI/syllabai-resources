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

  - For example, in general `integral straight e to the power of straight f left parenthesis x right parenthesis end exponent space straight d x not equal to fraction numerator 1 over denominator straight f apostrophe left parenthesis x right parenthesis end fraction straight e to the power of straight f left parenthesis x right parenthesis end exponent`
  - However, this result **is true** if$f(x)$ is linear$(ax+b)$
- Formally, in **function** **notation**, the **reverse** **chain** **rule** is used for **integrands** of the form

`I equals integral g to the power of apostrophe open parentheses x close parentheses f to the power of apostrophe open parentheses g open parentheses x close parentheses close parentheses space straight d x`

- This does not have to be strictly true, but ‘*algebraically’* it should be
- If the **coefficients** do not match ‘**adjust** and **compensate’** can be used

  - For example, $e^{x^{2}}$ differentiates to $2xe^{x^{2}}$ with the  chain rule
  
    - so`integral 2 x straight e to the power of x squared end exponent space straight d x equals straight e to the power of x squared end exponent plus c` with the reverse chain rule
  - But to do `integral 5 x straight e to the power of x squared end exponent straight d x`  we need to:
  
    - **Take out** the five: `5 integral x straight e to the power of x squared end exponent straight d x`
    - Force a 2 inside (**adjust**) and divide the outside by a 2 (**compensate**): `5 over 2 integral 2 x straight e to the power of x squared end exponent space straight d x`
    - The bit inside the integral is now a reverse chain rule
    - The answer is $\frac{5}{2}e^{x^{2}}+c$
- A particularly useful instance of the reverse chain rule to recognise is

`I equals integral fraction numerator f apostrophe left parenthesis x right parenthesis over denominator f left parenthesis x right parenthesis end fraction space straight d x equals ln space vertical line f left parenthesis x right parenthesis vertical line plus c`

- i.e.  the **numerator** is (almost) the **derivative** of the **denominator**

  - '**adjust** and **compensate**' may need to be used to deal with any coefficients
  
    - e.g.  `I equals integral fraction numerator x squared plus 1 over denominator x cubed plus 3 x end fraction space space straight d x equals 1 third integral 3 fraction numerator x squared plus 1 over denominator x cubed plus 3 x end fraction space space straight d x equals 1 third integral fraction numerator 3 x squared plus 3 over denominator x cubed plus 3 x end fraction space space straight d x equals 1 third ln space vertical line x cubed plus 3 x vertical line plus c`

> **Exam Hint**
> - You can always check your work by differentiating, if you have time

> **Worked Example**
> A curve has the gradient function$f'(x)=5x^{2}\mathrm{sin}(2x^{3})$.
> 
> Given that the curve passes through the point$(0,1)$, find an expression for$f(x)$.
> 
> > *Write f(**x**)** **as an integral.*
> 
> `straight f open parentheses x close parentheses space equals space integral 5 x squared space sin space open parentheses 2 x cubed close parentheses space straight d x space`
> 
> > *Take 5 out of the integral as a factor. *
> 
> `straight f open parentheses x close parentheses space equals space 5 integral x squared space sin space open parentheses 2 x cubed close parentheses space straight d x space`
> 
> > *The main function is sin(...), which would have come from -cos(...). *
> 
> > *Adjust and compensate the coefficients. 2**x*<sup>*3*</sup><sup>* *</sup>*would differentiate to 6**x*<sup>*2 *</sup>*so -cos(2**x*<sup>*3*</sup>*) would differentiate to (6**x*<sup>*2*</sup>*)sin(2x*<sup>*3*</sup>*)*
> 
> `straight f open parentheses x close parentheses space equals space 5 space cross times open parentheses 1 over 6 close parentheses cross times integral open parentheses 6 x squared close parentheses sin space open parentheses 2 x cubed close parentheses space straight d x space`
> 
> > *Integrate.*
> 
> `straight f open parentheses x close parentheses space equals space open parentheses 5 over 6 close parentheses cross times negative cos open parentheses 2 x cubed close parentheses space plus space c`
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
- To use the **reverse chain rule** `integral left parenthesis a x plus b right parenthesis to the power of n d x`(provided *n* is not -1)

  - **Raise** the **power of *****n***** by 1**
  - **Divide** by this **new power**
  - **Divide** this whole function by the **coefficient of *****x***
  
    - `integral left parenthesis a x blank plus blank b right parenthesis to the power of n blank straight d x equals fraction numerator open parentheses a x plus b close parentheses to the power of n plus 1 end exponent over denominator n plus 1 end fraction cross times 1 over a plus c`
- You can **check your answer by differentiating it**

  - You should get the original function when you differentiate your answer
- Note that this method **only works** when the function in the brackets is **linear (*****ax***** + *****b*****)**
- The special cases for **trigonometric** **functions** and **exponential** and **logarithmic** **functions** are

  - ** **`space integral sin left parenthesis a x plus b right parenthesis space straight d x equals negative 1 over a cos left parenthesis a x plus b right parenthesis plus c`
  - ** **`space integral cos left parenthesis a x plus b right parenthesis space straight d x equals 1 over a sin left parenthesis a x plus b right parenthesis plus c`
  - `space integral straight e to the power of a x plus b end exponent space straight d x equals 1 over a straight e to the power of a x plus b end exponent plus c`
  - `space integral fraction numerator 1 over denominator a x plus b end fraction space straight d x equals 1 over a ln open vertical bar a x plus b close vertical bar plus c`
- $c$, in all cases, is the **constant** of **integration**
- All the above can be deduced using **reverse** **chain** **rule**

  - However, spotting them can make solutions more efficient

> **Worked Example**
> Find the following integrals
> 
> a)      `space integral 3 left parenthesis 7 minus 2 x right parenthesis to the power of 5 over 3 end exponent space straight d x`
> 
> > *Name the integral.*
> 
> `I italic space equals integral 3 open parentheses 7 minus 2 x close parentheses to the power of 5 over 3 end exponent straight d x space equals space 3 integral open parentheses 7 minus 2 x close parentheses to the power of 5 over 3 end exponent straight d x space`
> 
> > *Using the rule 'raise the power by one, divide by the new power and then multiply by the reciprocal of the derivative' integrate the expression.*
> 
> `I italic space equals space 3 open square brackets fraction numerator 1 over denominator 8 over 3 end fraction open parentheses 7 minus 2 x close parentheses to the power of 8 over 3 end exponent space cross times fraction numerator 1 over denominator negative 2 end fraction close square brackets space plus c`
> 
> > *Simplify. *
> 
> `I italic space equals space 3 open square brackets negative fraction numerator 3 over denominator 16 end fraction open parentheses 7 minus 2 x close parentheses to the power of 8 over 3 end exponent space close square brackets space plus c`
> 
> $I=-\frac{9}{16}(7-2x)^{\frac{8}{3}}+c$
> 
> b)      `space integral 1 half cos left parenthesis 3 x minus 2 right parenthesis space straight d x`
> 
> > *Name the integral.*
> 
> `I italic space equals integral 1 half cos open parentheses 3 x minus 2 close parentheses straight d x space equals space 1 half integral cos open parentheses 3 x minus 2 close parentheses straight d x space space`
> 
> > *Using the rule *`space integral cos left parenthesis a x plus b right parenthesis space straight d x equals 1 over a sin left parenthesis a x plus b right parenthesis plus c`*, integrate the expression. *
> 
> `I italic space equals space 1 half open square brackets 1 third sin open parentheses 3 x minus 2 close parentheses close square brackets space plus c`
> 
> > *Simplify. *
> 
> $I=\frac{1}{6}\mathrm{sin}(3x-2)+c$
