---
note_id: "rn_YRsjqyyYmVmbGffs"
title: "The Poisson Distribution"
source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/revision-notes/statistical-distributions/poisson-distribution/the-poisson-distribution
path: statistical-distributions/poisson-distribution/the-poisson-distribution
updated_at: "2026-07-02T08:19:38.434Z"
spec_point_ids: ["spcpt_CbcjyRyGd65mXstM", "spcpt_w54vBS6Fm24wnJVB", "spcpt_F5rFq42MxcZZYVvp"]
spec_point_codes: []
guided_study: true
---

# The Poisson Distribution

## Properties of Poisson Distribution

> **Spec point** — `spcpt_CbcjyRyGd65mXstM`

## Properties of Poisson Distribution

#### What is a Poisson distribution?

- A Poisson distribution is a **discrete probability distribution**
- The **discrete random variable** $X$ follows a **Poisson distribution** if it **counts the number of events that occur at random in a given time or space**
- For a Poisson distribution to be valid it** must **satisfy the following properties:

  - Events occur **singly **and at **random** in a **given interval** of time or space
  - The **mean number of occurrences in the given interval(λ) ** is known and finite
  
    - λ has to be positive but does not have to be an integer
  - Each occurrence is **independent **of the other occurrences
- If $X$ follows a Poisson distribution then it is denoted $X \sim \text{Po} ( \\lambda )$

  - $λ$** **is the mean number of trials
- The formula for the probability of r occurrences in a given interval is:

  - $P(X=r)=e^{-λ}\times\frac{λ^{r}}{r!}$                for r=0, 1, 2, .....,$n$
  - *e* is the constant 2.718…
  - $r \text{factorial} = r ( r - 1 ) ( r - 2 )....2 \times 1$

#### What are the important properties of a Poisson distribution?

- The **mean **and **variance** of a Poisson distribution are roughly **equal**
- The distribution can be represented visually using a vertical line graph

  - If λ is **close to 0** then the graph has a **tail to the right** (positive skew)
  - If λ is **at least 5** then the graph is **roughly symmetrical**
- The Poisson distribution becomes more symmetrical as the value of the mean (*λ*) increases

![2-1-1-poisson-distribution-diagram-1](../../../assets/fcf2e242c17b-2-1-1-poisson-distribution-diagram-1.png)

> **Worked Example**
> $X$ is the random variable ‘The number of cars that pass a traffic camera per day’. State the conditions that would need to be met for $X$ to follow a Poisson distribution.
> 
> **Answer:**
> 
> ![2-1-1-the-poisson-distribution-we-solution-1](assets/106071c4552f-image.bin)

## Modelling with Poisson Distribution

> **Spec point** — `spcpt_w54vBS6Fm24wnJVB`

## Modelling with Poisson Distribution

#### How do I set up a Poisson model?

- Find the** mean **and** variance **and check that they are** roughly equal**

  - You may have to** change the mean **depending on the given time/space interval
- Make sure you **clearly state** what your **random variable** is

  - For example, let *X* be the number of typing errors per page in an academic article
- **Identify** what **probability **you are looking for

#### What can be modelled using a Poisson distribution?

- Anything that occurs **singly** and **randomly **in a given interval of time or space and satisfies the conditions
- For example, let *X*  be the random variable 'the number of emails that arrive into your inbox per day'

  - There is a given interval of a day, this is an example of an interval of time
  - We can assume the emails arrive into your inbox at random
  - We can assume each email is independent of the other emails
  
    - This is something that you would have to consider before using the Poisson distribution as a model
  - If you know the mean number of emails per day a Poisson distribution can be used
- Sometimes the given interval will be for space

  - For example, the number of daisies that exist on a square metre of grass
  - look carefully at the units given as you may have to change them when calculating probabilities

> **Worked Example**
> State, with reasons, whether the following can be modelled using a Poisson distribution and if so write the distribution.
> 
> (i) Faults occur in a length of cloth at a mean rate of 2 per metre.
> 
> (ii) On average 4% of a certain population has green eyes.
> 
> (iii) An emergency service company receives, on average, 15 calls per hour.
> 
> **Answer:**
> 
> ![2-1-1-modelling-with-a-poisson-we-solution-2](assets/a227e6bb10e3-image.bin)

> **Exam Hint**
> - If you are asked to criticise a Poisson model always consider whether the trials are independent, this is usually the one that stops a variable from following a Poisson distribution!

## Calculating Poisson Probabilities

> **Spec point** — `spcpt_F5rFq42MxcZZYVvp`

## Calculating Poisson Probabilities

Throughout this section we will use the random variable $X \sim \text{Po} ( \\lambda )$  . For a Poisson distribution, the probability of a *X* taking a non-integer or negative value is always zero. Therefore any values mentioned in this section (other than *λ*) will be assumed to be non-negative integers.

#### Where does the formula for a Poisson distribution come from?

- The formula for calculating an individual **Poisson probability **is

  - $P(X=r)=p_{r}=e^{-λ}\times\frac{λ^{r}}{r!}$ for r = 0, 1, 2 ,....
- The derivation of the formula comes from the binomial distribution, however it is outside the scope of this syllabus and will not be proved here

  - Whilst the binomial distribution relies on knowing a fixed number of trials, the Poisson can allow for any number of trials within a time period
  - Only the mean number of occurrences of an event within the given period needs to be known

#### How do I calculate the cumulative probabilities for a Poisson distribution?

- To find an individual probability use the formula $p_{r}=e^{-λ}\times\frac{λ^{r}}{r!}$
- Most of the time you will be required to calculate** cumulative Poisson probabilities **rather than individual ones

  - Use the formula to find the individual probabilities and then add them up
  - Make sure you are confident working with inequalities for **discrete values**
  - Only integer values will be included so it is easiest to look at which integer values you should include within your calculation
  - Sometimes it is quicker to find the probabilities that are **not being asked for** and subtract from one
- $P(X\leqx)$ is asking you to find the probabilities of **all values up to and including *****x***

  - This means all values that are **at most *****x***
  - Don’t forget to include P(*X = 0*)
- $P(X<x)$ is asking you to find the probabilities of **all values up to but not including *****x***

  - This means all values that are **less than x**
  - Stop at *x-1*
- $P(X\geqx)$ is asking you to find the probabilities of **all values greater than and including x**

  - This means all values that are **at least x**
  - As there is** not a fixed number of trials **this includes an** infinite number of possibilities**
  - To calculate this, use the identity $P(X\geqx)=1-P(X<x)$
- $P(X>x)$is asking you to find the probabilities of **all values greater than but not including x**

  - This means all values that are **more than x**
  - Rewrite $P(X>x)=1-P(X\leqx)$ as to calculate this
- If calculating $P(a\leqX\leqb)$pay attention to whether the probability of a and b should be included in the calculation or not

  - For example, $P(4<X\leq10)$ :
  
    - You want the integers 5 to 10

#### How can calculating probabilities for a Poisson distribution be made easier?

- Having to type a lot of calculations into your calculator can be time consuming and cause errors
- Consider the calculation $P(X\leq3)=e^{-λ}\times\frac{λ^{0}}{0!}+e^{-λ}\times\frac{λ^{1}}{1!}+e^{-λ}\times\frac{λ^{2}}{2!}+e^{-λ}\times\frac{λ^{3}}{3!}$

  - Note that $e^{-λ}$exists in every term and can be factorised out
  - Recall that $λ^{0}=1$ and 0! = 1
  - Recall also that $λ^{1}=λ$ and 1! = 1
- This calculation could be factorised and simplified to

  - $P ( X \text{less} \text{or} \text{equal} \text{than} 3 ) = e^{- \\lambda } ( 1 + \\lambda + \frac{\\lambda ^{2}}{2 factorial} + \frac{\\lambda ^{3}}{3 factorial} )$
  - This is much simpler and easier to type into your calculator in exam conditions

#### How do I change the mean for a Poisson distribution?

- Sometimes the mean may be given for a different interval of time or space than that which you need to calculate the probability for
- A given value of *λ *can be adjusted to fit the necessary time period

  - For example if a football team score a mean of 2 goals an hour and we want to find the probability of them scoring a certain number of goals in a 90 minute game, then we would use the distribution *X* ~ Po(*3*)
  
    - 90 = 1.5 (60) so use 1.5λ
- A very useful property of the Poisson distribution is that if *X* and *Y* are **two independent Poisson** distributions then their sums, ***X *****+***** Y*** is also a **Poisson** distribution

  - If *X* ~ Po(*λ*) and *Y* ~ Po(*μ*) then *X* + *Y* ~ Po(*λ* + *μ*)
  - Note that, for an integer value of *a *and *b *greater than 1, *aX + bY* no longer follows a Poisson distribution

> **Worked Example**
> Xiao makes silly mistakes in his maths homework at a mean rate of 2 per page.
> 
> (a) Define a suitable distribution to model the number of silly mistakes Xiao would make in a piece of homework that is five pages long. State any assumptions you have made.
> 
> **Answer:**
> 
> ![2-1-1-calculating-poisson-probabilities-we-solution-3_a](assets/3d7f811112c5-2-1-1-calculating-poisson-probabilities-we-solut.png)
> 
> (b) Find the probability that in any random page of Xiao’s homework book there are
> 
> (i) exactly three silly mistakes
> 
> (ii) at most three silly mistakes
> 
> (iii) more than three silly mistakes.
> 
> **Answer:**
> 
> ![2-1-1-calculating-poisson-probabilities-we-solution-3_b](assets/f0a3bac9ca50-image.bin)

> **Exam Hint**
> - Look carefully at the given time or space interval to check if you need to change the mean before carrying out calculations. Be prepared for this to change between question parts!
