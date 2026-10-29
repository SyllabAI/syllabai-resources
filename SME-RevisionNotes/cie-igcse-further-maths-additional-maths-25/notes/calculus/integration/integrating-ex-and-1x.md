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

$\text{integral} e^{ } x d x = e^{ } x + c$

`equation`

where $c$ is the **constant** of **integration**

- For the **linear** function$(ax+b)$, where$a$ and$b$ are constants,

** **$\text{integral} e^{ } a x + b d x = \frac{1}{ } a e^{ } a x + b + c$

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
> > *To find* $f ( x )$*, we need to integrate the expression for* $f ' ( x ).$*   *
> 
> $f ( x ) = \int \frac{3}{3 x + 2} + e^{4 - x} d x$
> 
> > *Rewrite as two separate integrals which can be found individually, and factor out any constants.*
> 
> $f ( x ) = 3 \int \frac{1}{3 x + 2} d x + \int e^{4 - x} d x$
> 
> *Use the two results:* $\int \frac{1}{a x + b} d x = \frac{1}{a} \ln \vert a x + b \vert + c$ $\int e^{a x + b} d x = \frac{ 1}{a} e^{a x + b} + c$
> 
> $f ( x ) = 3 ( 1 \frac{1}{3} \ln \vert 3 x + 2 \vert ) + - 1 e^{4 - x} + c
> f ( x ) = \ln \vert 3 x + 2 \vert - e^{4 - x} + c$
> 
> > *The question states that* $f ( 1 ) = \ln 10 - e^{3}$*, so substitute in* $x=1$ *and equate to the given expression.*
> 
> $\ln 10 - e^{3} = \ln \vert 3 ( 1 ) + 2 \vert - e^{4 - 1} + c$
> 
> > *Simplify and solve to find* $c.$*  *
> 
> $\mathrm{ln}10-e^{3}=\mathrm{ln}5-e^{3}+c\,\mathrm{ln}10-\mathrm{ln}5=c$
> 
> > *Recall from laws of logarithms that* $\mathrm{ln}a-\mathrm{ln}b=\mathrm{ln}\frac{a}{b}.$*  *
> 
> $c=\mathrm{ln}\frac{10}{5}=\mathrm{ln}2$
> 
> > *Rewrite the full expression for* $f ( x ).$*  *
> 
> `equation`  
> **or by combining logs, this could be written as **$f ( x ) = \ln ( 2 \vert 3 x + 2 \vert ) - e^{4 - x}$
