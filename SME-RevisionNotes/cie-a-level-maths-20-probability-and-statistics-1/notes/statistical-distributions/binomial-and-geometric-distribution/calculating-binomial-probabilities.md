---
note_id: "rn_JgZhprbWpgpfH976"
title: "Calculating Binomial Probabilities"
source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/revision-notes/statistical-distributions/binomial-and-geometric-distribution/calculating-binomial-probabilities
path: statistical-distributions/binomial-and-geometric-distribution/calculating-binomial-probabilities
updated_at: "2026-07-02T08:19:38.481Z"
spec_point_ids: ["spcpt_JpjTxPV33Mm5vDvf"]
spec_point_codes: []
guided_study: true
---

# Calculating Binomial Probabilities

## Calculating Binomial Probabilities

> **Spec point** — `spcpt_JpjTxPV33Mm5vDvf`

## Calculating Binomial Probabilities

Throughout this section we will use the random variable $X \sim \mathrm{B} ( n , p )$. For binomial, the probability of a *X* taking a non-integer or negative value is always zero. Therefore any values mentioned in this section will be assumed to be non-negative integers.

#### Where does the formula for a binomial distribution come from?

- The formula for calculating an individual **binomial probability **is

  - $\mathrm{P} ( X = r ) = p_{r} = ( \begin{gathered} n \\ r \end{gathered} ) p^{r ( 1 - p )^{n} - r}$
  
    - If there are *r* successes then there are $( n - r )$ failures
    - The number of times this can happen is calculated by the **binomial coefficient**
    - $( \begin{gathered} n \\ r \end{gathered} ) = C pre^{n}_{r} = \frac{n factorial}{r \text{factorial} ( n - r ) factorial}$
- This can be seen by considering a **probability tree diagram** with *n *trials, where *p* is the probability of success and the tree diagram is being used to find *r *successes
- $( \begin{gathered} n \\ r \end{gathered} )$ is the number of pathways through the tree there would be exactly *r* successes within the *n* trials
- The formula allows statisticians to quickly find probabilities for larger values of *n* without needing to draw the whole tree diagram
- Your calculator may have a function that would allow you to calculate binomial probabilities

  - You can learn how to use this to check your work but it is important you always show your working using the formula to get the marks in the exam

#### How do I calculate the cumulative probabilities for a binomial distribution?

- Most of the time you will be required to calculate** cumulative binomial probabilities **rather than individual ones
- Use the formula to find the individual probabilities and then add them up
- Make sure you are confident working with inequalities for **discrete values**

  - Only integer values will be included so it is easiest to look at which integer values you should include within your calculation
  - Sometimes it is quicker to find the probabilities that are **not being asked for** and subtract from one
- $P(X\leqr)$is asking you to find the probabilities of **all values up to and including *****r***

  - This means all values that are **at most *****r***
  - Don’t forget to include P(*X *= 0)
  - It could also be written as $P(X\leqr)=1-P(X>r)$
- $P(X<r)$is asking you to find the probabilities of **all values up to but not including *****r***

  - This means all values that are **less than *****r***
  - Stop at *r - 1*
  - It could also be written as $P(X<r)=1-P(X\geqr)$
- $P(X\geqr)$ is asking you to find the probabilities of **all values greater than and including *****r***

  - This means all values that are **at least *****r***
  - It could also be written as  $P(X\geqr)=1-P(X<r)$
- $P(X>r)$is asking you to find the probabilities of **all values greater than but not including *****r***

  - This means all values that are **more than r**
  - Start at *r + 1*
  - It could also be written as $P(X>r)=1-P(X\leqr)$
- If calculating $P(a\leqX\leqb)$ pay attention to whether the probability of *a* and *b* should be included in the calculation or not

  - For example, $P(4<X\leq10)$ :
  
    - You want the integers 5 to 10

> **Worked Example**
> If $X$ is the random variable $X \sim \mathrm{B} ( 10 , 0.35 )$. Find:
> 
> (i) $P(X=3)$
> 
> (ii) $P(X\leq3)$
> 
> (iii) $P(X>3)$
> 
> (iv) $P(3<X<6)$
> 
> **Answer:**
> 
> ![3-2-2-calculating-binomial-probabilities-we-solution](assets/fa956f713b35-image.bin)

> **Exam Hint**
> - Looking carefully at the inequality within the probability is key here, make sure you consider which integers should be counted within your calculations.
