---
note_id: "rn_mTmtcSqk9HKWBzGD"
title: "Hypothesis Testing for the Mean of a Poisson Distribution"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/revision-notes/hypothesis-testing/hypothesis-testing-binomial-and-poisson-distributions/hypothesis-testing-for-lambda
path: hypothesis-testing/hypothesis-testing-binomial-and-poisson-distributions/hypothesis-testing-for-lambda
updated_at: "2026-07-02T08:19:38.585Z"
spec_point_ids: ["spcpt_2cYxMfGpbS5NYNxv"]
spec_point_codes: []
guided_study: false
---

# Hypothesis Testing for the Mean of a Poisson Distribution

## Poisson Hypothesis Testing

> **Spec point** — `spcpt_2cYxMfGpbS5NYNxv`

## Poisson Hypothesis Testing

#### How is a hypothesis test carried out for the mean of a Poisson distribution?

- The **population parameter** being tested will be the **mean, λ ,** in a **Poisson distribution Po(λ)**

  - As it is the population mean, sometimes *μ *will be used instead
- A hypothesis test is used when the mean is questioned
- The **null hypothesis**, H<sub>0</sub>  and **alternative hypothesis**, H<sub>1 </sub>will be given in terms of λ (or *μ*)

  - Make sure you clearly define λ before writing the hypotheses
  - The null hypothesis will always be **H**<sub>**0**</sub>** **: λ = ...
  - The alternative hypothesis will depend on if it is a one-tailed or two-tailed test
  - A one-tailed test would test to see if the **value of λ** has **either increased or decreased**
  
    - The **alternative hypothesis, will be H**<sub>**1 **</sub>**will be  H**<sub>**1**</sub>** : λ > ...or H**<sub>**1**</sub>** : λ < ...**
  - A two-tailed test would test to see if the **value of λ** has **changed**
  
    - The **alternative hypothesis, H**<sub>**1 **</sub>**will be  H**<sub>**1**</sub>** : λ  ≠ ...**
- To carry out a hypothesis test with the Poisson distribution, the **random variable **will be the mean number of occurrences of the event within the given time/space interval

  - Remember you may need to change the mean to fit the interval of time or space for your observed value
- When defining the distribution, remember that the value of λ  is being tested, so this should be written as λ in the original definition, followed by the null hypothesis stating the assumed value of λ
- The Poisson distribution will be used to **calculate the probability** of the random variable taking the observed value **or a more extreme value**
- The hypothesis test can be carried out by

  - either calculating the probability of the random variable taking the observed or a more extreme value and comparing this with the significance level
  - or by finding the critical region and seeing whether the observed value of the test statistic lies within it
  
    - Finding the critical region can be more useful for considering more than one observed value or for further testing

#### How is the critical value found in a hypothesis test with the Poisson distribution?

- The **critical value** will be the **first value **to fall within the** critical region**

  - The Poisson distribution is a** discrete **distribution** **so the probability of the observed value being within the critical region, given a true null hypothesis may be less than the** significance level**
  - This is the **actual significance level** and is the probability of **incorrectly **rejecting the null hypothesis (a Type I error)
- For a **one-tailed test **use the formula to find the first value for which the probability of that **or a more extreme value** is less than the given significance level

  - Check that the next value would cause this probability to be greater than the significance level
  
    - For H<sub>1</sub> : λ < ...   if `straight P left parenthesis X less or equal than c right parenthesis less or equal than alpha percent sign` and `straight P left parenthesis X less or equal than c plus 1 right parenthesis greater than alpha percent sign` then *c *is the critical value
    - For H<sub>1</sub> : λ > ... if `straight P left parenthesis X greater or equal than c right parenthesis less or equal than alpha percent sign` and `straight P left parenthesis X greater or equal than c minus 1 right parenthesis greater than alpha percent sign` then *c *is the critical value
- For a **two-tailed test **you will need to find **both critical values, **one at each end of the distribution

#### What steps should I follow when carrying out a hypothesis test with the Poisson distribution?

**Step 1. ** Define the mean, *λ*

**Step 2.  **Write the null and alternative hypotheses clearly using the form

**H**<sub>**0**</sub>** **: λ = ...

**H**<sub>**1**</sub>** **: λ = ...

**Step 3.  **Define the distribution, usually `begin mathsize 16px style X tilde Po left parenthesis lambda right parenthesis end style`  where *λ *is the mean to be tested

**Step 4.  **Calculate the probability of the random variable being at least as extreme as the observed value

- Or if told to find the critical region

**Step 5.  **Compare this probability with the significance level

- Or compare the observed value with the critical region

**Step 6.  **Decide whether there is enough evidence to reject H<sub>0</sub> or whether it has to be accepted

**Step 7.  **Write a conclusion in context

> **Worked Example**
> Mr Viajo believes that his travel blog receives an average of 8 likes per day (24 hour period).  He tries a new advertising campaign and carries out a hypothesis test at the 5% level of significance to see if there is a change in the number of likes he gets. Over a 12-hour period chosen at random Mr Viajo’s travel blog receives 7 likes.
> 
> (i) State null and alternative hypotheses for Mr Viajo’s test.
> 
> (ii) Find the critical regions for the test.
> 
> (iii) Find the actual level of significance.
> 
> (iv) Carry out the hypothesis test, writing your conclusion clearly.
> 
> ![2-2-2-poisson-hyp-testing-we-solution-part-1](assets/b599a440596d-image.bin)
> 
> ![2-2-2-poisson-hyp-testing-we-solution-part-2](assets/f92b95b20c6f-image.bin)

> **Exam Hint**
> - You might have to change the value of λ based on the length of the interval
> 
>   - Always make it clear to the examiner which value of λ you are using when you calculate probabilities
