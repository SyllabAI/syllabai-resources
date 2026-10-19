---
note_id: "rn_JsyCQ72Nk8TMfM3R"
title: "The Poisson Distribution"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/revision-notes/statistical-distributions/poisson-distribution/the-poisson-distribution
path: statistical-distributions/poisson-distribution/the-poisson-distribution
updated_at: "2026-07-02T08:19:38.655Z"
spec_point_ids: ["spcpt_gQsJPB7Szy6ZvMBZ", "spcpt_GPmq8k46YXs6B3kX"]
spec_point_codes: []
guided_study: false
---

# The Poisson Distribution

## Properties of Poisson Distribution

> **Spec point** — `spcpt_gQsJPB7Szy6ZvMBZ`

## Properties of Poisson Distribution

#### What is a Poisson distribution?

- A Poisson distribution is a **discrete probability distribution**
- The **discrete random variable** *X* follows a **Poisson distribution** if it **counts the number of events that occur at random in a given time or space**
- For a Poisson distribution to be valid it** must **satisfy the following properties:

  - Events occur **singly **and at **random** in a **given interval** of time or space
  - The **mean number of occurrences in the given interval(λ) ** is known and finite
  
    - λ has to be positive but does not have to be an integer
  - Each occurrence is **independent **of the other occurrences
- If *X* follows a Poisson distribution then it is denoted `X tilde Po left parenthesis lambda right parenthesis`

  - **λ **is the mean number of occurrences of the event
- The formula for the probability of r occurrences in a given interval is:

  - $P(X=r)=e^{-λ}\times\frac{λ^{r}}{r!}$ for r=0, 1, 2, ...,*n*
  - *e* is the constant 2.718…
  - `r factorial equals r open parentheses r minus 1 close parentheses open parentheses r minus 2 close parentheses....2 cross times 1`

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

> **Spec point** — `spcpt_GPmq8k46YXs6B3kX`

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
