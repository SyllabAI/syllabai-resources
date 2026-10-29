---
note_id: "rn_WVBnHQwp2ZnGfTMn"
title: "E(X) & Var(X) (Continuous)"
source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/revision-notes/statistical-distributions/continuous-random-variables/ex-and-varx-continuous
path: statistical-distributions/continuous-random-variables/ex-and-varx-continuous
updated_at: "2026-07-02T08:19:38.468Z"
spec_point_ids: ["spcpt_tQpsd6ts3DXRzHSR"]
spec_point_codes: []
guided_study: true
---

# E(X) & Var(X) (Continuous)

## E(X) & Var(X) (Continuous)

> **Spec point** — `spcpt_tQpsd6ts3DXRzHSR`

## E(X) & Var(X) (Continuous)

#### What are E(X) and Var(X)?

- E(X)is the **expected** **value**, or **mean**, of a **random** **variable X**

  - E(X) is the same as the population mean so can also be denoted by *µ*
- **Var (X) **is the **variance** of the continuous random variable *X*

  - **Standard** **deviation** is the **square** **root** of the **variance**

#### How do I find the mean and variance of a continuous random variable?

- The **mean**, for a **continuous** **random** **variable *****X*** is given by

$E ( X ) = integral_{ } - \text{infinity} ^{ } \text{infinity} x f ( x ) d x$

- This is equivalent to $ΣxP(X=x)$ for discrete random variables
- If the graph of $y=f(x)$has **axis** of **symmetry,** x = a , then  E(X) = a

- The **variance** is given by

`Var ( X ) = integral _ - inf end _ ^ inf x ^ 2 f ( x ) d x - stretchy left square bracket E ( X ) stretchy right square bracket ^ 2`

- This is equivalent to `capital sigma x ^2 P ( X = x ) - stretchy left square bracket E ( X ) stretchy right square bracket ^2`  for discrete random variables
- Be careful about confusing $E(X^{2})$  and $[ E ( X ) ]^{2}$

  - $E ( X ^{2} ) = integral_{ - } \text{infinity} ^{infinity} x ^{2} \mathrm{f} ( x ) \mathrm{d} x$                “mean of the squares”
  - $[ E ( X ) ] ^{2} = [ integral_{ - } \text{infinity} ^{infinity} x \mathrm{f} ( x ) \mathrm{d} x ] ^{2}$       “square of the mean”
  - If you are happy with the difference between these and how to calculate them the variance formula becomes very straightforward

$\text{Var} ( X ) = \mathrm{E} ( X^{2} ) - [ \mathrm{E} ( X ) ]^{2}$

#### How do I calculate E(g(X))?

- $\mathrm{E} ( g ( X ) ) = integral_{ - } \text{infinity} ^{infinity} g ( x ) \mathrm{f} ( x ) \mathrm{d} x$
- In particular:

  - $\mathrm{E} ( X ^{2} ) = integral_{ - } \text{infinity} ^{infinity} x ^{2} \mathrm{f} ( x ) \mathrm{d} x$as seen above

> **Worked Example**
> A continuous random variable, $X$, is modelled by the probability distribution function $f(x)$, such that
> 
> `f ( x ) = { | 1.5 x ^2 ( 1 - 0.5 x ) | 0 <= x <= 2 | | 0 | otherwise | close`
> 
> (i) Find $E ( X )$
> 
> **Answer:**
> 
> ![2-3-2-cie-fig1-we-solution_a](assets/5338b0703d78-image.bin)
> 
> (ii) Find $Var ( X )$
> 
> **Answer:**
> 
> ![2-3-2-cie-fig1-we-solution_b](assets/44ec122e6a3c-image.bin)

> **Exam Hint**
> - A **sketch** of the graph of y =  f(x) can highlight any **symmetrical** properties which can help reduce the work involved in finding the **mean** and **variance**
> - Take care with awkward **values** and **negatives** – use the **memory** features on your calculator and **avoid** **rounding** until your **final** answer (if rounding at all!)
