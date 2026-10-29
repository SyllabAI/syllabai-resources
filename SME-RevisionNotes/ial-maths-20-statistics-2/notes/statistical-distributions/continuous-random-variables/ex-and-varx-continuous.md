---
note_id: "rn_RkQkq5VHytTm7D9C"
title: "E(X) & Var(X) (Continuous)"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/revision-notes/statistical-distributions/continuous-random-variables/ex-and-varx-continuous
path: statistical-distributions/continuous-random-variables/ex-and-varx-continuous
updated_at: "2026-07-02T08:19:38.652Z"
spec_point_ids: ["spcpt_dH2h38ZK6svbtC8J"]
spec_point_codes: []
guided_study: false
---

# E(X) & Var(X) (Continuous)

## E(X) & Var(X) (Continuous)

> **Spec point** — `spcpt_dH2h38ZK6svbtC8J`

## E(X) & Var(X) (Continuous)

#### What are E(X) and Var(X)?

- E(X)is the **expected** **value**, or **mean**, of a **random** **variable X**

  - E(X) is the same as the population mean so can also be denoted by *µ*
- **Var (X) **is the **variance** of the continuous random variable *X*

  - **Standard** **deviation** is the **square** **root** of the **variance**

#### How do I find the mean and variance of a continuous random variable?

- The **mean**, for a **continuous** **random** **variable *****X*** is given by

$E ( X ) = \mu = integral_{ } - \text{infinity} ^{ } \text{infinity} x f ( x ) d x$

- This is equivalent to $ΣxP(X=x)$ for discrete random variables
- If the graph of $y=f(x)$has **axis** of **symmetry,** x = a , then  E(X) = a

- The **variance** is given by

$Var ( X ) = \text{sigma} ^{ } 2 = integral_{ } - \text{infinity} ^{ } \text{infinity} x^{ } 2 f ( x ) d x - \mu^{ } 2$

- This is equivalent to $Σx^{2}P(X=x)-μ^{2}$  for discrete random variables
- Be careful about confusing $E(X^{2})$  and $[ E ( X ) ]^{2}$

  - $E ( X ^{2} ) = integral_{ - } \text{infinity} ^{infinity} x ^{2} \mathrm{f} ( x ) \mathrm{d} x$                “mean of the squares”
  - $[ E ( X ) ] ^{2} = [ integral_{ - } \text{infinity} ^{infinity} x \mathrm{f} ( x ) \mathrm{d} x ] ^{2}$       “square of the mean”
  - If you are happy with the difference between these and how to calculate them the variance formula becomes very straightforward

$\text{Var} ( X ) = \mathrm{E} ( X^{2} ) - [ \mathrm{E} ( X ) ]^{2}$

#### How do I calculate E(g(X))?

- $\mathrm{E} ( g ( X ) ) = integral_{ - } \text{infinity} ^{infinity} g ( x ) \mathrm{f} ( x ) \mathrm{d} x$
- In particular:

  - $\mathrm{E} ( X ^{2} ) = integral_{ - } \text{infinity} ^{infinity} x ^{2} \mathrm{f} ( x ) \mathrm{d} x$as seen above
- If $g(X)=aX+b$(a linear function) then

  - $\mathrm{E} ( g ( X ) ) = \mathrm{E} ( a X + b ) = a \mathrm{E} ( X ) + b$
  - $Var ( g ( X ) ) = Var ( a X + b ) = a ^{2} Var ( X )$

> **Worked Example**
> A continuous random variable, *X*, is modelled by the probability distribution function f(x), such that
> 
> `f ( x ) = { | 1.5 x ^2 ( 1 - 0.5 x ) | 0 <= x <= 2 | | 0 | otherwise | close`
> 
> (a) Find $E(X)$ .
> 
> (b) Find $\mathrm{Var}(X)$.
> 
> **Answer:**
> 
> ![1-3-2-ial-fig1-we-solution-part-1](assets/eb8992a6148b-image.bin)
> 
> ![1-3-2-ial-fig1-we-solution-part-2](assets/abacdccb6a51-image.bin)

> **Exam Hint**
> - A **sketch** of the graph of y =  f(x) can highlight any **symmetrical** properties which can help reduce the work involved in finding the **mean** and **variance**
> - Take care with awkward **values** and **negatives** – use the **memory** features on your calculator and **avoid** **rounding** until your **final** answer (if rounding at all!)
> - The formulae for $\text{E}(X)=μ$ and $Var(X)=σ^{2}$ are given in the formulae booklet
