---
note_id: "rn_M4BvnTC9rwJhbdjy"
title: "Integrating e^x & 1/x"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/calculus/integration/integrating-ex-and-1x
path: calculus/integration/integrating-ex-and-1x
updated_at: "2026-07-02T08:19:38.536Z"
spec_point_ids: ["spcpt_N2d7b7XT2gzcq6Mz"]
spec_point_codes: []
guided_study: false
---

# Integrating e^x & 1/x

## Integrating e^x & 1/x

> **Spec point** — `spcpt_N2d7b7XT2gzcq6Mz`

## Integrating e^x & 1/x

### How do I integrate exponentials and 1/x?

- The **integrals** involving$e^{x}$ and$\mathrm{ln}x$ are

`bold space bold integral bold space bold e to the power of bold italic x bold space bold d bold italic x bold equals bold space bold e to the power of bold italic x bold plus bold italic c`

`equation`

where $c$ is the **constant** of **integration**

- For the **linear** function$(ax+b)$, where$a$ and$b$ are constants,

** **`bold space bold integral bold e to the power of bold italic a bold italic x bold plus bold italic b end exponent bold space bold d bold italic x bold equals bold 1 over bold italic a bold e to the power of bold italic a bold italic x bold plus bold italic b end exponent bold plus bold italic c`

`equation`

- It follows from the last result that

`equation`

- which can be deduced using **Reverse Chain Rule**
- With **ln,** it can be useful to write the constant of integration,$c$, as a logarithm

  - using the laws of logarithms, the answer can be written as a single term
  - `equation`where$k$ is a constant
  - This is similar to the special case of **differentiating**$\mathrm{ln}(ax+b)$ when$b=0$

> **Worked Example**
> A curve has the gradient function$f'(x)=\frac{3}{3x+2}+e^{4-x}$.
> 
> Given the exact value of$f(1)$ is$\mathrm{ln}10-e^{3}$ find an expression for$f(x)$.
> 
> > *To find *`f open parentheses x close parentheses`*, we need to integrate the expression for *`f apostrophe open parentheses x close parentheses.`*   *
> 
> `f open parentheses x close parentheses equals integral fraction numerator 3 over denominator 3 x plus 2 end fraction plus e to the power of 4 minus x end exponent space d x`
> 
> > *Rewrite as two separate integrals which can be found individually, and factor out any constants.  *
> 
> `f open parentheses x close parentheses equals 3 integral fraction numerator 1 over denominator 3 x plus 2 end fraction d x space plus space integral e to the power of 4 minus x end exponent space d x`
> 
> *Use the two results:* `integral fraction numerator 1 over denominator a x plus b end fraction d x equals 1 over a ln vertical line a x plus b vertical line space plus space c` `integral e to the power of a x plus b end exponent d x space equals fraction numerator space 1 over denominator a end fraction space e to the power of a x plus b end exponent space plus c`
> 
> `f open parentheses x close parentheses equals 3 open parentheses 1 third ln vertical line 3 x plus 2 vertical line close parentheses space plus space minus 1 e to the power of 4 minus x end exponent space plus c
> f open parentheses x close parentheses equals ln vertical line 3 x plus 2 vertical line space minus space e to the power of 4 minus x end exponent space plus c`
> 
> > *The question states that *`f open parentheses 1 close parentheses equals ln 10 space minus space e cubed`*, so substitute in *$x=1$* and equate to the given expression.  *
> 
> `ln space 10 space minus space e cubed space equals space ln vertical line 3 open parentheses 1 close parentheses plus 2 vertical line space minus space e to the power of 4 minus 1 end exponent plus c`
> 
> > *Simplify and solve to find *$c.$*  *
> 
> $\mathrm{ln}10-e^{3}=\mathrm{ln}5-e^{3}+c\,\mathrm{ln}10-\mathrm{ln}5=c$
> 
> > *Recall from laws of logarithms that *$\mathrm{ln}a-\mathrm{ln}b=\mathrm{ln}\frac{a}{b}.$*  *
> 
> $c=\mathrm{ln}\frac{10}{5}=\mathrm{ln}2$
> 
> > *Rewrite the full expression for *`f open parentheses x close parentheses.`*  *
> 
> `equation`  
> **or by combining logs, this could be written as **`f open parentheses x close parentheses equals ln space open parentheses 2 vertical line 3 x plus 2 vertical line close parentheses space minus space e to the power of 4 minus x end exponent`
