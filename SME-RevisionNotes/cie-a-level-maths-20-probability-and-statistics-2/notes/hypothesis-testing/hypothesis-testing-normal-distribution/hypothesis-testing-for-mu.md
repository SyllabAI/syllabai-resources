---
note_id: "rn_kRqJsVwzTjS9TStP"
title: "Hypothesis Testing for the Mean of a Normal Distribution"
source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/revision-notes/hypothesis-testing/hypothesis-testing-normal-distribution/hypothesis-testing-for-mu
path: hypothesis-testing/hypothesis-testing-normal-distribution/hypothesis-testing-for-mu
updated_at: "2026-07-02T08:19:38.464Z"
spec_point_ids: ["spcpt_DBjZPz9tFvYW9SQs"]
spec_point_codes: []
guided_study: true
---

# Hypothesis Testing for the Mean of a Normal Distribution

## Normal Hypothesis Testing

> **Spec point** — `spcpt_DBjZPz9tFvYW9SQs`

## Normal Hypothesis Testing

#### What steps should I follow when carrying out a hypothesis test for the mean of a normal distribution?

- Following these steps will help when carrying out a hypothesis test for the mean of a normal distribution:
- **Step 1.**  Define the distribution of the **population mean** usually `X tilde size 16px N size 16px left parenthesis size 16px μ size 16px comma size 16px σ ^ size 16px 2 size 16px right parenthesis`
- **Step 2.  **Write the null and alternative hypotheses clearly

- **Step 3.   **Assuming the null hypothesis to be true, define the **statistic**
- **Step 4.   **Calculate either the **critical value(s) **or the probability of the observed value** **for the test
- **Step 5.   **Compare the observed value of the test statistic with the critical value(s) or the probability with the significance level

  - Or compare the z-value corresponding to the observed value with the z-value corresponding to the critical value
- **Step 6.   **Decide whether there is enough evidence to reject H<sub>0</sub> or whether it has to be accepted
- **Step 7.  **Write a conclusion in context

#### How should I define the distribution of the population mean and the statistic?

- The **population parameter** being tested will be the **population mean, *****μ **** *in a **normally distributed random variable **N *(μ, σ*<sup>*2*</sup>*)*

#### How should I define the hypotheses?

- A hypothesis test is used when the value of the assumed population mean is questioned
- The **null hypothesis**, H<sub>0</sub> and **alternative hypothesis**, H<sub>1</sub> will always be given in terms of *µ*

  - Make sure you clearly define *µ* before writing the hypotheses, if it has not been defined in the question
  - The null hypothesis will always be **H**<sub>**0**</sub>** : *****µ = ...***
  - The alternative hypothesis will depend on if it is a **one-tailed** or **two-tailed** test
  - A one-tailed test would test to see if the **value of  *****µ ***has **either increased or decreased**
  
    - The **alternative hypothesis, H**<sub>**1**</sub> **will be H**<sub>**1 **</sub>**: ** ***µ > ...***** or H**<sub>**1 **</sub>**: ** ***µ < ...***
  - A two-tailed test would test to see if the **value of *****µ*** has **changed**
  
    - The **alternative hypothesis, H**<sub>**1**</sub> **will be H**<sub>**1 **</sub>**: ** ***µ ≠ ..***

#### How should I define the statistic?

- The population mean is tested by looking at the mean of a sample taken from the population

  - The sample mean is denoted $\overline{x}$
  - For a random variable `X tilde size 16px N size 16px left parenthesis size 16px μ size 16px comma size 16px σ ^ size 16px 2 size 16px right parenthesis` the distribution of the sample mean would be `X with bar on top tilde N left parenthesis μ comma σ ² / n right parenthesis`
- To carry out a hypothesis test with the normal distribution, the **statistic used to carry out the test **will be the **sample mean, **`top enclose X`

  - Remember that the **variance** of the sample mean distribution will be the variance of the population distribution **divided by *****n***
  - the **mean** of the sample mean distribution will be the same as the mean of the population distribution

#### How should I carry out the test?

- The hypothesis test can be carried out by

  - either calculating the probability of a value taking the observed or a more extreme value and comparing this with the significance level
  
    - The normal distribution will be used to **calculate the probability** of a value of the random variable $\overline{X}$ taking the observed value **or a more extreme value**
  - or by finding the critical region and seeing whether the observed value lies within it
  
    - Finding the critical region can be more useful for considering more than one observed value or for further testing
- A third method is to compare the z-values of your observed value with the z-values at the boundaries of the critical region(s)

  - Find the z-value for your sample mean using $z=\frac{\overline{x}-μ}{\frac{σ}{\sqrt{n}}}$
  
    - This is sometimes known as your **test statistic**
  - Use the table of critical values to find the z-value for the significance level
  - If the z-value for your test statistic is further away from 0 than the critical z-value then reject H<sub>0</sub>

#### How is the critical value found in a hypothesis test for the mean of a normal distribution?

- The **critical value(s)** will be the boundary of the** critical region**

  - The probability of the observed value being within the critical region, given a true null hypothesis will be the same as the** significance level**
- For an* *$α$*%*  significance level:

  - In a one-tailed test the critical region will consist of  $α$*%* in the tail that is being tested for
  - In a two-tailed test the critical region will consist of `alpha over 2 percent sign` in each tail

![1-2-2-confidence-intervals-diagram-1-1](../../../assets/5a506f9c71af-1-2-2-confidence-intervals-diagram-1-1.png)

- To find the critical value(s) use the standard normal distribution:

  - Step 1.  Find the distribution of the sample means, assuming H<sub>0</sub> is true
  - Step 2.  Use the coding $Z=\frac{\overline{x}-μ}{\frac{σ}{\sqrt{n}}}$ to standardise to Z
  - Step 3.  Use the table to find the z - value for which the probability of Z being equal to or more extreme than the value is equal to the significance level
  
    - You can often find this in the table of the critical values
  - Step 4.  Equate this value to your expression found in step 2
  - Step 5.  Solve to find the corresponding value of $\overline{x}$
- If using this method for a two-tailed test be aware of the following:

  - The symmetry of the normal distribution means that the z - values will have the same absolute value
  - You can solve the equation for both the positive and negative z – value to find the two critical values
  
    - Check that the two critical values are the same distance from the mean

> **Worked Example**
> The time,  minutes, that it takes Amelea to complete a 1000-piece puzzle can be modelled using `X tilde straight N left parenthesis 204 comma 81 right parenthesis` .  Amelea gets prescribed a new pair of glasses and claims that the time it takes her to complete a 1000-piece puzzle has decreased.  Wearing her new glasses, Amelea completes 12 separate 1000-piece puzzles and calculates her mean time on these puzzles to be 201 minutes.  Use these 12 puzzles as a sample to test, at the 5% level of significance, whether there is evidence to support Amelea’s claim. You may assume the variance is unchanged.
> 
> **Answer:**
> 
> ![3-3-1-hypothesis-nd-we-solution](assets/a4312846cd9c-image.bin)

> **Exam Hint**
> - Use a diagram to help, especially if looking for the critical value and comparing this with an observed value of a test statistic or if working with z-values.
