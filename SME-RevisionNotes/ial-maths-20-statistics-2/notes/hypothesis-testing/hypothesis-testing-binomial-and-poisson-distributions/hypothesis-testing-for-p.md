---
note_id: "rn_CrJphb3KzvGst5pR"
title: "Hypothesis Testing for the Proportion of a Binomial Distribution"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/revision-notes/hypothesis-testing/hypothesis-testing-binomial-and-poisson-distributions/hypothesis-testing-for-p
path: hypothesis-testing/hypothesis-testing-binomial-and-poisson-distributions/hypothesis-testing-for-p
updated_at: "2026-07-02T08:19:38.583Z"
spec_point_ids: ["spcpt_FgTdMGnP4jYnHk7C"]
spec_point_codes: []
guided_study: false
---

# Hypothesis Testing for the Proportion of a Binomial Distribution

## Binomial Hypothesis Testing

> **Spec point** — `spcpt_FgTdMGnP4jYnHk7C`

## Binomial Hypothesis Testing

#### How is a hypothesis test carried out with the binomial distribution?

- The **population parameter** being tested will be the **probability, *****p***** ** in a **binomial distribution ***B(n , p)*
- A hypothesis test is used when the assumed probability is questioned
- The **null hypothesis**, H<sub>0</sub>  and **alternative hypothesis**, H<sub>1</sub> will always be given in terms of *p*

  - Make sure you clearly define *p* before writing the hypotheses
  - The null hypothesis will always be **H**<sub>**0 **</sub>**: *****p = ...***
  - The alternative hypothesis will depend on if it is a one-tailed or two-tailed test
  - A one-tailed test would test to see if the **value of *****p***** ** has **either increased or decreased**
  
    - The **alternative hypothesis, H**<sub>**1 **</sub>**will be H**<sub>**1**</sub>** : *****p > ...*** ** or  H**<sub>**1**</sub>** : *****p < ...*** ** **
  - A two-tailed test would test to see if the **value of *****p***** ** has **changed**
  
    - The **alternative hypothesis, H**<sub>**1 **</sub>**will be H**<sub>**1**</sub>** : *****p ≠ ...***** **
- To carry out a hypothesis test with the binomial distribution, the **test statistic **will be the number of **successes** in a defined number of **trials**
- When defining the test statistic, remember that the value of *p*  is being tested, so this should be written as *p* in the original definition, followed by the null hypothesis stating the assumed value of *p*
- The binomial distribution will be used to **calculate the probability** of the test statistic taking the observed value **or a more extreme value**
- The hypothesis test can be carried out by

  - either calculating the probability of the test statistic taking the observed or a more extreme value and comparing this with the significance level
  
    - You may have to use a normal approximation to calculate the probability
  - or by finding the critical region and seeing whether the observed value of the test statistic lies within it
  
    - Finding the critical region can be more useful for considering more than one observed value or for further testing

#### How is the critical value found in a hypothesis test with the binomial distribution?

- The **critical value** will be the **first value **to fall within the** critical region**

  - The binomial distribution is a** discrete **distribution** **so the probability of the observed value being within the critical region, given a true null hypothesis may be less than the** significance level**
  - This is the **actual significance level** and is the probability of **incorrectly **rejecting the null hypothesis
- For a **one-tailed test **use your calculator to find the first value for which the probability of that **or a more extreme value** is less than the given significance level

  - Check that the next value would cause this probability to be greater than the significance level
  
    - For **H**<sub>**1**</sub>** : ***p < ...**** ***if `straight P left parenthesis X less or equal than c right parenthesis less or equal than alpha percent sign`  and `straight P left parenthesis X less or equal than c plus 1 right parenthesis space greater than alpha percent sign` then *c *is the critical value
    - For **H**<sub>**1**</sub>** : ***p > ... * if `straight P left parenthesis X greater or equal than c right parenthesis less or equal than alpha percent sign`  and `straight P left parenthesis X greater or equal than c minus 1 right parenthesis greater than alpha percent sign` then *c *is the critical value
- For a **two-tailed test **you will need to find **both critical values, **one at each end of the distribution

  - Find the first value for which the probability of that **or a more extreme value** is less than **half** of the given significance level in both the upper and lower tails
  
    - Often one of the critical regions will be bigger than the other

#### What steps should I follow when carrying out a hypothesis test with the binomial distribution?

- **Step 1. **Define the probability, *p*
- **Step 2. **Write the null and alternative hypotheses clearly using the form

H<sub>0</sub> : *p = ...*

H<sub>1</sub> : *p = ...*

- **Step 3. **Define the test statistic, usually `begin mathsize 16px style X tilde B left parenthesis n comma p right parenthesis end style` where *n*  is a defined number of trials and *p* is the population parameter to be tested
- **Step 4. **Calculate either the **critical value(s) **or the **necessary probability **for the test
- **Step 5. **Compare the observed value of the test statistic with the critical value(s) or the probability with the significance level
- **Step 6. **Decide whether there is enough evidence to reject H<sub>0</sub> or whether it has to be accepted
- **Step 7.**Write a conclusion in context

> **Worked Example**
> Jacques, a breadmaker, claims that fewer than 40% of people that shop in a particular supermarket buy his brand of bread.  Jacques takes a random sample of 12 customers that have purchased bread and asks them which brand of bread they have purchased.  He records that 2 of them had purchased his brand of bread.  Test, at the 10% level of significance, whether Jacques’ claim is justified.
> 
> ![2-2-1-binomial-hypothesis-testing-we-solution-part-1](assets/3097d689b891-image.bin)
> 
> ![2-2-1-binomial-hypothesis-testing-we-solution-part-2](assets/dc9d10f9f855-image.bin)

> **Exam Hint**
> - Most of the time the values of n and p will be in the tables
> - if not, you will have to use the formula to calculate the probabilities or use a normal approximation
