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
- **Var (X) **is the **variance** of the continuous random variable* X*

  - **Standard** **deviation** is the **square** **root** of the **variance**

#### How do I find the mean and variance of a continuous random variable?

- The **mean**, for a **continuous** **random** **variable *****X*** is given by

`bold E bold left parenthesis bold italic X bold right parenthesis bold equals bold italic mu bold equals bold integral subscript bold minus bold infinity end subscript superscript bold infinity bold italic x bold f bold left parenthesis bold italic x bold right parenthesis bold space bold d bold italic x`

- This is equivalent to $ΣxP(X=x)$ for discrete random variables
- If the graph of $y=f(x)$has **axis** of **symmetry,** x = a , then  E(X) = a

- The **variance** is given by

`bold Var bold left parenthesis bold italic X bold right parenthesis bold equals bold italic sigma to the power of bold 2 bold equals bold integral subscript bold minus bold infinity end subscript superscript bold infinity bold italic x to the power of bold 2 bold f bold left parenthesis bold italic x bold right parenthesis bold d bold italic x bold minus bold italic mu to the power of bold 2`

- This is equivalent to $Σx^{2}P(X=x)-μ^{2}$  for discrete random variables
- Be careful about confusing $E(X^{2})$  and `begin mathsize 16px style open square brackets E open parentheses X close parentheses close square brackets squared end style`

  - `E left parenthesis X squared right parenthesis equals integral subscript negative infinity end subscript superscript infinity x squared straight f left parenthesis x right parenthesis space straight d x`                “mean of the squares”
  - `open square brackets E left parenthesis X right parenthesis close square brackets squared equals open square brackets integral subscript negative infinity end subscript superscript infinity x space straight f left parenthesis x right parenthesis space straight d x close square brackets squared`       “square of the mean”
  - If you are happy with the difference between these and how to calculate them the variance formula becomes very straightforward

`Var left parenthesis X right parenthesis equals straight E left parenthesis X squared right parenthesis minus open square brackets straight E left parenthesis X right parenthesis close square brackets squared`

#### How do I calculate E(g(X))?

- `straight E open parentheses g open parentheses X close parentheses close parentheses equals integral subscript negative infinity end subscript superscript infinity g open parentheses x close parentheses straight f left parenthesis x right parenthesis space straight d x`
- In particular:

  - `straight E left parenthesis X squared right parenthesis equals integral subscript negative infinity end subscript superscript infinity x squared straight f left parenthesis x right parenthesis space straight d x`as seen above
- If $g(X)=aX+b$(a linear function) then

  - `straight E open parentheses g open parentheses X close parentheses close parentheses equals straight E open parentheses a X plus b close parentheses equals a straight E open parentheses X close parentheses plus b`
  - `Var open parentheses g left parenthesis X right parenthesis close parentheses equals Var open parentheses a X plus b close parentheses equals a squared Var open parentheses X close parentheses`

> **Worked Example**
> A continuous random variable, *X*, is modelled by the probability distribution function f(x), such that
> 
> `straight f left parenthesis x right parenthesis equals open curly brackets table row cell 1.5 x squared left parenthesis 1 minus 0.5 x right parenthesis end cell cell 0 less or equal than x less or equal than 2 end cell row cell space space space space space space space space 0 end cell otherwise end table close`
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
