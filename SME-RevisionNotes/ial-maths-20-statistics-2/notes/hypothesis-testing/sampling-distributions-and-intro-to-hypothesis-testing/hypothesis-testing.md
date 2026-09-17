---
note_id: "rn_Pt6dkX8WKZ5jPWN3"
title: "Hypothesis Testing"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/revision-notes/hypothesis-testing/sampling-distributions-and-intro-to-hypothesis-testing/hypothesis-testing
path: hypothesis-testing/sampling-distributions-and-intro-to-hypothesis-testing/hypothesis-testing
updated_at: "2026-07-02T08:19:38.483Z"
spec_point_ids: ["spcpt_FyrqXqf8PCg6CTb8", "spcpt_SXgS5mjTMgfKTPsD", "spcpt_mPVJHc5CKHN5mQyS"]
spec_point_codes: []
guided_study: false
---

# Hypothesis Testing

## Language of Hypothesis Testing

> **Spec point** — `spcpt_FyrqXqf8PCg6CTb8`

## Language of Hypothesis Testing

#### What is a hypothesis test?

- A hypothesis test uses a **sample of data** in an experiment to test a **statement** made about the value of a **population parameter**
- A hypothesis test is used when the value of the assumed population parameter is questioned
- The hypothesis test will look at the which outcomes are unlikely to occur if assumed population parameter is true
- The probability found will be compared against a given **significance level** to determine whether there is **evidence to believe **that the assumed population parameter is not true

#### What are the key terms used in statistical hypothesis testing?

- Every hypothesis test **must **begin with a clear **null hypothesis **(what we believe to already be true) and **alternative hypothesis **(how we believe the data pattern or probability distribution might have changed)
- A **hypothesis **is an assumption that is made about a particular **population parameter**

  - A **population parameter **is a numerical characteristic which helps define a population
  
    - One example of a population parameter is the **probability, *****p***** ** of an event occurring
    - Another example is the mean of a population
  - The **null hypothesis** is denoted **H**<sub>**0**</sub> and sets out the assumed population parameter given that no change has happened
  - The **alternative hypothesis **is denoted **H**<sub>**1**</sub>  and sets out how we think the population parameter could have changed
  - When a hypothesis test is carried out, the null hypothesis is **assumed to be true** and this assumption will either be **accepted** or **rejected**
- A hypothesis test could be a **one-tailed **test or a **two-tailed **test
- The null hypothesis will always be **H**<sub>**0**</sub>** : *****θ***** = ...**
- The alternate hypothesis will depend on if it is a one-tailed or two-tailed test

  - A one-tailed test would test to see if the **population parameter, *****θ*****,** has **either increased or decreased**
  
    - The **alternative hypothesis, H**<sub>**1 **</sub> **will be H**<sub>**1**</sub> : ***θ > ...*** ** or  H**<sub>**1**</sub> : ***θ < ...***
  - A two-tailed test would test to see if the **population parameter, *****θ*** , has **changed**
  
    - The **alternative hypothesis, H**<sub>**1 **</sub> **will be H**<sub>**1**</sub> : ***θ ≠ ...*****  **
  - It is important to read the wording of the question carefully to decide whether your hypothesis test should be one-tailed or two-tailed
- To carry out a hypothesis test an experiment will be carried out on a **sample of data**, the result of this experiment will be the **test statistic**

  - A **sample of data **is a subset of data taken from the population
  - The **test statistic** is a numerical value calculated from the data
  
    - The test statistic is sometimes also referred to as the **observed value**
- A hypothesis test will always be carried out at an appropriate **significance level**

  - The significance level sets the **smallest probability **that an event could have occurred by chance.
  
    - Any probability smaller than the significance level would suggest that the event is unlikely to have happened by chance
  - The **significance level **must be set **before **the hypothesis test is carried out
  - The significance level will usually be 1%, 5% or 10%, however it may vary

> **Worked Example**
> A hypothesis test is carried out at the 5% level of significance to test if a normal coin is fair or not.
> 
> (i) Describe what the population parameter could be for the hypothesis test.
> 
> (ii) State whether the hypothesis test should be a one-tailed test or a two-tailed test, give a reason for your answer.
> 
> (iii) Clearly defining your population parameter, state suitable null and alternative hypotheses for the test.
> 
> **Answer:**
> 
> ![5-1-1-language-of-hypothesis-testing-we-solution](assets/9213c1a3ac77-image.bin)

> **Exam Hint**
> - Make sure you read the question carefully to determine whether the test you are carrying out is for a one-tailed or a two-tailed test.

## Critical Regions

> **Spec point** — `spcpt_SXgS5mjTMgfKTPsD`

## Critical Regions

#### How do we decide whether to reject or accept the null hypothesis?

- The null hypothesis would be rejected if the **observed value **falls **within the critical region**

  - The **critical region **is the range of values that the observed value could take which will lead to the **null hypothesis** being **rejected**
- The **critical value **is the boundary of the critical region

  - It is the least extreme value that would lead to the rejection of the null hypothesis
  - The** critical value **is determined by the **significance level**
  - In a **two-tailed test** the significance level is halved and both the upper and the lower tails are tested
  - For **discrete distributions** the critical value is the first value that falls within the critical region and so the probability of the observed value falling within the critical region may be lower than the given significance level
  
    - This probability will be known as the **actual significance level**
    - The actual significance level is the probability of incorrectly rejecting the null hypothesis
  - Finding the critical region will be different for a **two-tailed test** than it is for a **one-tailed test**
- For an $α$*%*  significance level

  - In a one-tailed test the critical region will consist of $α$*%* in the tail that is being tested for
  - In a two-tailed test the critical region will consist of `alpha over 2 percent sign` in each tail

#### Do we always need to find the critical region?

- In most cases the best method of conducting a hypothesis test is to find the critical region

  - It allows you to see how far the observed value is from the critical value and make decisions about whether further testing is necessary
- In some cases a hypothesis test can be carried out without finding the critical region
- The null hypothesis would be rejected if the** **probability of a value being **at least as extreme** as the observed value, assuming that the null hypothesis is true, is **less than the significance level**

  - If the test is looking for a decrease then extreme values are smaller than the observed value, so find the probability of less than or equal to the observed value
  - If the test is looking for an increase then extreme values are bigger than the observed value, so find the probability of greater than or equal to the observed value
  - This probability is called the "**p-value**"
- In a **two-tailed test **it is common to half the significance level and compare this with the probability found in one of the tails

> **Worked Example**
> For the following situations, state at the 1% and 5% significance levels whether the null hypothesis should be rejected or not.
> 
> (i) The critical region is $X\leq3$and the observed value is 4.
> 
> (ii) Assuming the null hypothesis is true, the probability of a value being at least as extreme as the test statistic in a one-tailed hypothesis test is 0.0429.
> 
> (iii) Assuming the null hypothesis is true, the probability of a value being at least as extreme as the test statistic in a two-tailed hypothesis test is 0.00705.
> 
> **Answer:**
> 
> ![3-1-1-critical-regions-and-p-values-we-solution-](assets/ae4ebaad8065-image.bin)

## Conclusions of Hypothesis Testing

> **Spec point** — `spcpt_mPVJHc5CKHN5mQyS`

## Conclusions of Hypothesis Testing

#### How is a hypothesis test carried out?

- There are a number of ways that a hypothesis test can be carried out for different models, however the following steps should form the base for your test:
- **Step 1.** Define the test statistic and population parameter
- **Step 2. **Write the null and alternative hypotheses clearly
- **Step 3. **Calculate the **critical value(s) **or the necessary probability for the test
- **Step 4. **Compare the observed value with the critical value(s) or the probability with the significance level
- **Step 5. **Decide whether there is enough evidence to reject H<sub>0</sub> or whether it has to be accepted
- ** Step 6. **Write a conclusion in context

#### How should a conclusion be written for a hypothesis test?

- Your conclusion **must** be written in the context of the question
- Use the wording in the question to help you write your conclusion

  - If rejecting the null hypothesis your conclusion should state that there is **sufficient** **evidence to suggest** the alternative hypothesis is true at this level of significance
  - If accepting the null hypothesis your conclusion should state that there is **not enough evidence** to suggest the alternative hypothesis is true at this level of significance
- Your conclusion **must** **not** be definitive

  - There is a chance that the test has led to an incorrect conclusion
  - The outcome is dependent on the sample, a different sample might lead to a different outcome
- The conclusion of a two-tailed test can state if there is evidence of a change

  - You should not state whether this change is an increase or decrease

> **Worked Example**
> A teacher carried out a hypothesis test at the 10% significance level to test if her students perform better in exams after using a new revision technique. Under the null hypothesis she calculates the probability that a value will be at least as extreme as the observed value to be 0.09142. Write a conclusion for her hypothesis test.
> 
> **Answer:**
> 
> ![5-1-1-conclusions-of-hypothesis-testing-we-solution](assets/cc0da7b64016-image.bin)

> **Exam Hint**
> - It is best to use the exact wording from the question when writing your conclusion for the hypothesis test, do not be afraid to sound repetitive.
