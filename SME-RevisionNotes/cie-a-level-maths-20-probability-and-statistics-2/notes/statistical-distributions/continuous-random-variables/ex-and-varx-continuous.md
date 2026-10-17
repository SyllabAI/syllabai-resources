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
- **Var (X) **is the **variance** of the continuous random variable* X*

  - **Standard** **deviation** is the **square** **root** of the **variance**

#### How do I find the mean and variance of a continuous random variable?

- The **mean**, for a **continuous** **random** **variable *****X*** is given by

`bold E bold left parenthesis bold italic X bold right parenthesis bold equals bold integral subscript bold minus bold infinity end subscript superscript bold infinity bold italic x bold f bold left parenthesis bold italic x bold right parenthesis bold space bold d bold italic x`

- This is equivalent to $ΣxP(X=x)$ for discrete random variables
- If the graph of $y=f(x)$has **axis** of **symmetry,** x = a , then  E(X) = a

- The **variance** is given by

`bold Var bold left parenthesis bold italic X bold right parenthesis bold equals bold integral subscript bold minus bold infinity end subscript superscript bold infinity bold italic x to the power of bold 2 bold f bold left parenthesis bold italic x bold right parenthesis bold d bold italic x bold minus stretchy left square bracket E open parentheses X close parentheses stretchy right square bracket to the power of bold 2`

- This is equivalent to `straight capital sigma x squared straight P left parenthesis X equals x right parenthesis minus stretchy left square bracket E open parentheses X close parentheses stretchy right square bracket squared`  for discrete random variables
- Be careful about confusing $E(X^{2})$  and `begin mathsize 16px style open square brackets E open parentheses X close parentheses close square brackets squared end style`

  - `E left parenthesis X squared right parenthesis equals integral subscript negative infinity end subscript superscript infinity x squared straight f left parenthesis x right parenthesis space straight d x`                “mean of the squares”
  - `open square brackets E left parenthesis X right parenthesis close square brackets squared equals open square brackets integral subscript negative infinity end subscript superscript infinity x space straight f left parenthesis x right parenthesis space straight d x close square brackets squared`       “square of the mean”
  - If you are happy with the difference between these and how to calculate them the variance formula becomes very straightforward

`Var left parenthesis X right parenthesis equals straight E left parenthesis X squared right parenthesis minus open square brackets straight E left parenthesis X right parenthesis close square brackets squared`

#### How do I calculate E(g(X))?

- `straight E open parentheses g open parentheses X close parentheses close parentheses equals integral subscript negative infinity end subscript superscript infinity g open parentheses x close parentheses straight f left parenthesis x right parenthesis space straight d x`
- In particular:

  - `straight E left parenthesis X squared right parenthesis equals integral subscript negative infinity end subscript superscript infinity x squared straight f left parenthesis x right parenthesis space straight d x`as seen above

> **Worked Example**
> A continuous random variable, $X$, is modelled by the probability distribution function $f(x)$, such that
> 
> `straight f left parenthesis x right parenthesis equals open curly brackets table row cell 1.5 x squared left parenthesis 1 minus 0.5 x right parenthesis end cell cell 0 less or equal than x less or equal than 2 end cell row cell space space space space space space space space space space space space 0 end cell otherwise end table close`
> 
> (i) Find `E open parentheses X close parentheses`
> 
> **Answer:**
> 
> ![2-3-2-cie-fig1-we-solution_a](assets/5338b0703d78-image.bin)
> 
> (ii) Find `Var open parentheses X close parentheses`
> 
> **Answer:**
> 
> ![2-3-2-cie-fig1-we-solution_b](assets/44ec122e6a3c-image.bin)

> **Exam Hint**
> - A **sketch** of the graph of y =  f(x) can highlight any **symmetrical** properties which can help reduce the work involved in finding the **mean** and **variance**
> - Take care with awkward **values** and **negatives** – use the **memory** features on your calculator and **avoid** **rounding** until your **final** answer (if rounding at all!)
