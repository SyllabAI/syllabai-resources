---
note_id: "rn_yZfZgdKGYGCYJjjv"
title: "Calculating Binomial Probabilities"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/revision-notes/statistical-distributions/binomial-distribution/calculating-binomial-probabilities
path: statistical-distributions/binomial-distribution/calculating-binomial-probabilities
updated_at: "2026-07-02T08:19:38.617Z"
spec_point_ids: ["spcpt_946spf6kFdytWskY"]
spec_point_codes: []
guided_study: false
---

# Calculating Binomial Probabilities

## Calculating Binomial Probabilities

> **Spec point** — `spcpt_946spf6kFdytWskY`

## Calculating Binomial Probabilities

Throughout this section we will use the random variable `X tilde straight B left parenthesis n comma p right parenthesis`. For binomial, the probability of a *X*  taking a non-integer or negative value is always zero. Therefore any values mentioned in this section will be assumed to be non-negative integers.

#### What are the tables for the binomial cumulative distribution function?

- In your **formulae booklet** you get **tables** which list the values of for different values of *x*, *p and* *n*

  - $n$ can be **5, 6, 7, 8, 9 10, 12, 15, 20, 25, 30, 40, 50**
  - $p$ can be **05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5**
  - $x$ can be different values depending on *n*
- The probabilities are rounded to **4 decimal places**
- The values of $p$ **only go up to 0.5**

  - You can instead count the number of failures `Y tilde B left parenthesis n comma 1 minus p right parenthesis` if the probability of success is bigger than 0.5
  - Remember $X+Y=n$, which leads to identities:
  
    - $P(X=k)=P(Y=n-k)$
    - $P(X\leqk)=P(Y\geqn-k)$
    - $P(X\geqk)=P(Y\leqn-k)$

#### How do I calculate, P(X = x) the probability of a single value for a binomial distribution?

- You can use the formula given in the formulae booklet

  - `P left parenthesis X equals x right parenthesis equals open parentheses table row n row x end table close parentheses space p to the power of x open parentheses 1 minus p close parentheses to the power of n minus x end exponent`
  
    - The number of times this can happen is calculated by the **binomial coefficient **`open parentheses table row n row x end table close parentheses equals C presuperscript n subscript x equals fraction numerator n factorial over denominator x factorial left parenthesis n minus x right parenthesis factorial end fraction`
- You can also use the tables for the ***Binomial Cumulative Distribution Function*** in the formulae booklet

  - $P(X=k)=P(X\leqk)-P(X\leqk-1)$

#### How do I calculate, P(X ≤ x), the cumulative probabilities for a binomial distribution?

- If x is small, you could find the probability of each possible value of x and then add them together
- Otherwise, you will have to use the tables for the ***Binomial Cumulative Distribution Function*** in the formulae booklet
- If p is bigger than 0.5 then you will have to use the number of failures `Y tilde B left parenthesis n comma 1 minus p right parenthesis`

  - $P(X\leqx)=P(Y\geqn-x)$

#### How do I find P(X ≥ x)?

- $X\geqx$**: **This means all values of *X* which are **at least *****x***

  - These are **all** values of ***X*** **except** the ones that are **less than *****x***
- $P(X\geqx)=1-P(X<x)$
- As *x*  is an integer then $P(X<x)=P(X\leqx-1)$ as the probability of *X* is zero for non-integer values for a binomial distribution
- Therefore, to calculate $P(X\geqx)$:

  - $P(X\geqx)=1-P(X\leqx-1)$
  - For example: $P(X\geq10)=1-P(X\leq9)$

#### How do I find  P(a ≤ X ≤ b)?

- $a\leqX\leqb$: This means all values of *X* which are **at** **least *****a***** and at most *****b***

  - This is **all** the values of *X* which are **no greater than *****b*** **except** the ones which are **less than *****a***
- $P(a\leqX\leqb)=P(X\leqb)-P(X<a)$
- As *X* is an integer then $P(X<a)=P(X\leqa-1)$ as the $P(X=x)=0$  for non-integer value of x for a binomial distribution
- Therefore to calculate $P(a\leqX\leqb)$:

  - $P(a\leqX\leqb)=P(X\leqb)-P(X\leqa-1)$
  - For example: $P(4\leqX\leq9)=P(X\leq9)-P(X\leq3)$

#### What if an inequality does not have the equals sign (strict inequality)?

- For a binomial distribution (as it is discrete) you could rewrite all strict inequalities (< and >) as weak inequalities (≤ and ≥) by using the identities for a binomial distribution

  - $P(X<x)=P(X\leqx-1)$ and $P(X>x)=P(X\geqx+1)$
  - For example: $P(X<5)=P(X\leq4)$ and $P(X>5)=P(X\geq6)$
  - Though it helps to understand how they work
- It helps to think about the **range of integers** you want
- Always find the **biggest integer** that you want to **include** and the **biggest integer** that you then want to **exclude**
- For example, : $P(4<X\leq10)$

  - You want the integers 5 to 10
  - You want the integers up to 10 excluding the integers up to 4
  - $P(X\leq10)-P(X\leq4)$
- For example, P(X > 6)  :

  - You want the all the integers from 7 onwards
  - You want to include all integers excluding the integers up to 6
  - 1- P(*X ≤ 6)*
- For example, P(X < 8)  :

  - You want the integers 0 to 7
  - P(X ≤ 7)

> **Worked Example**
> The random variable `X tilde straight B left parenthesis 40 comma 0.35 right parenthesis` . Find:
> 
> (a) $P(X=10)$
> 
> (b) $P(X\leq10)$
> 
> (c) $P(X\geq10)$
> 
> (d) $P(8<X<10)$
> 
> **Answer:**
> 
> ![1-1-2-calculating-binomial-prob-we-solution-part-1](assets/0ac8b6e51aae-image.bin)
> 
> ![1-1-2-calculating-binomial-prob-we-solution-part-2](assets/5dafc51d0c19-image.bin)
> 
> ![1-1-2-calculating-binomial-prob-we-solution-part-3](assets/d0e1020358e9-image.bin)
> 
> ![1-1-2-calculating-binomial-prob-we-solution-part-4](assets/6b8a077071ed-image.bin)

> **Exam Hint**
> - Some calculators will calculate probabilities for binomial distributions
> - These are great for checking your answers once you have answered your question showing the appropriate method
