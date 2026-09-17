---
note_id: "rn_vmfkpVF5w4XxZXkw"
title: "Calculating Poisson Probabilities"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/revision-notes/statistical-distributions/poisson-distribution/calculating-poisson-probabilities
path: statistical-distributions/poisson-distribution/calculating-poisson-probabilities
updated_at: "2026-07-02T08:19:38.656Z"
spec_point_ids: ["spcpt_dchGk3kdpWq5TpJY"]
spec_point_codes: []
guided_study: false
---

# Calculating Poisson Probabilities

## Calculating Poisson Probabilities

> **Spec point** — `spcpt_dchGk3kdpWq5TpJY`

## Calculating Poisson Probabilities

Throughout this section we will use the random variable `X tilde Po left parenthesis lambda right parenthesis`  . For a Poisson distribution, the probability of a *X* taking a non-integer or negative value is always zero. Therefore any values mentioned in this section (other than *λ*) will be assumed to be non-negative integers.

#### Where does the formula for a Poisson distribution come from?

- The formula for calculating an individual **Poisson probability **is

  - $P(X=r)=p_{r}=e^{-λ}\times\frac{λ^{r}}{r!}$ for r = 0, 1, 2 ,...., n
- The derivation of the formula comes from the binomial distribution, however it is outside the scope of this syllabus and will not be proved here

  - Whilst the binomial distribution relies on knowing a fixed number of trials, the Poisson can allow for any number of trials within a time period
  - Only the mean number of occurrences of an event within the given period needs to be known

#### How do I calculate the cumulative probabilities for a Poisson distribution?

- Most of the time the value of λ will be in the table for the 'Poisson Cumulative Distribution Function' in the formula booklet
- $P(X\leqx)$ is asking you to find the probabilities of **all values up to and including *****x***** **

  - This will be the value in the row of *x*
- $P(X<x)$ is asking you to find the probabilities of **all values up to but not including *****x***

  - This means all values that are **less than x**
  - This will be the value in the row of *x *- 1
  
    - $P(X\leqx-1)$
- $P(X\geqx)$ is asking you to find the probabilities of **all values greater than and including x**

  - This means all values that are **at least x**
  - As there is** not a fixed number of trials **this includes an** infinite number of possibilities**
  - To calculate this, use the identity $P(X\geqx)=1-P(X<x)$
  
    - Using above we get: $P(X\geqx)=1-P(X\leqx-1)$
- $P(X>x)$ is asking you to find the probabilities of **all values greater than but not including x**

  - This means all values that are **more than x**
  - Rewrite $P(X>x)=1-P(X\leqx)$ as to calculate this
- If calculating $P(a\leqX\leqb)$ then calculate $P(X\leqb)-P(X\leqa-1)$

  - This is the same idea as for the binomial distribution

#### How do I calculate the cumulative probabilities for a Poisson distribution if λ is not in the table?

- In the unlikely case that λ is not in the table

  - Use the formula to find the individual probabilities and then add them up
  - Make sure you are confident working with inequalities for **discrete values**
  - Only integer values will be included so it is easiest to look at which integer values you should include within your calculation
  - Sometimes it is quicker to find the probabilities that are **not being asked for** and subtract from one

- Having to type a lot of calculations into your calculator can be time consuming and cause errors
- Consider the calculation $P(X\leq3)=e^{-λ}\times\frac{λ^{0}}{0!}+e^{-λ}\times\frac{λ^{1}}{1!}+e^{-λ}\times\frac{λ^{2}}{2!}+e^{-λ}\times\frac{λ^{3}}{3!}$

  - Note that $e^{-λ}$ exists in every term and can be factorised out
  - Recall that $λ^{0}=1$ and 0! = 1
  - Recall also that $λ^{1}=λ$ and 1! = 1
- This calculation could be factorised and simplified to

  - `begin mathsize 16px style P left parenthesis X less or equal than 3 right parenthesis equals e to the power of negative lambda end exponent open parentheses 1 plus lambda plus fraction numerator lambda squared over denominator 2 factorial end fraction plus fraction numerator lambda cubed over denominator 3 factorial end fraction close parentheses end style`
  - This is much simpler and easier to type into your calculator in exam conditions

#### How do I change the mean for a Poisson distribution?

- Sometimes the mean may be given for a different interval of time or space than that which you need to calculate the probability for
- A given value of *λ *can be adjusted to fit the necessary time period

  - For example if a football team score a mean of 2 goals an hour and we want to find the probability of them scoring a certain number of goals in a 90 minute game, then we would use the distribution *X* ~ Po(*3*)
  
    - 90 = 1.5 × 60 so use 1.5λ

> **Worked Example**
> Xiao makes silly mistakes in his maths homework at a mean rate of 2 per page.
> 
> (a) Define a suitable distribution to model the number of silly mistakes Xiao would make in a piece of homework that is five pages long.
> 
> (b) Find the probability that in any random page of Xiao’s  homework book there are
> 
> **Answer:**
> 
> (i) exactly three silly mistakes
> 
> (ii) at most three silly mistakes
> 
> (iii) more than three silly mistakes.
> 
> ![1-2-2-calculating-poisson-probabilities-we-solution-part-1](assets/d9814e590782-image.bin)
> 
> ![1-2-2-calculating-poisson-probabilities-we-solution-part-2](assets/d92a57cfe179-image.bin)

> **Exam Hint**
> - Look carefully at the given time or space interval to check if you need to change the mean before carrying out calculations.
> 
>   - Be prepared for this to change between question parts!
