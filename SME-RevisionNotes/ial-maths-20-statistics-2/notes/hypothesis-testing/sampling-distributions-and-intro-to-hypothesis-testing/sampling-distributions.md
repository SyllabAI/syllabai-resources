---
note_id: "rn_fMgm8rrmN9ftVg2y"
title: "Sampling Distributions"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/revision-notes/hypothesis-testing/sampling-distributions-and-intro-to-hypothesis-testing/sampling-distributions
path: hypothesis-testing/sampling-distributions-and-intro-to-hypothesis-testing/sampling-distributions
updated_at: "2026-07-02T08:19:38.633Z"
spec_point_ids: ["spcpt_tfzp7PgcTfMs9Ddw"]
spec_point_codes: []
guided_study: false
---

# Sampling Distributions

## Sampling Distributions

> **Spec point** — `spcpt_tfzp7PgcTfMs9Ddw`

## Sampling Distributions

#### What key words do I need to know about sampling?

- The **population** refers to the **whole set** of things which you are interested in

  - For example: if a vet wanted to know how long a typical French bulldog slept for in a day then the population would be all the French bulldogs in the world
- A **sampling unit** is an individual member of the population

  - For example: a French bulldog would be a sampling unit in the above population
- A **sample** refers to a **subset of the population** which is used to collect data from

  - For example: the vet might take a sample of French bulldogs from different cities and record how long they sleep in a day
- A **sampling frame** is a **list** of all members of the **population**

  - For example: a list of employees’ names within a company
- A **population parameter** is a **numerical value** which describes a **characteristic of the population**

  - These are usually unknown
  - For example: the mean (*μ*) height of all 16-year-olds in the UK
- A **sample statistic** is a **value** computed using **data from the sample**

  - These are used to estimate population parameters
  - For example: the mean ($\overline{x}$) height of 200 16-year-olds from randomly selected cities in the UK

#### What are the differences between a census and sampling?

- A **census** collects data about **all** the members of a **population**

  - For example: the Government in England does a national census every 10 years to collect data about every person living in England at the time
- The main advantage of a census is that it gives fully accurate results
- The disadvantages of a census are:

  - It is time consuming and expensive to carry out
  - It can destroy or use up all the members of a population when they are consumables (imagine a company testing every single firework)
- **Sampling** is used to collect data from a **subset of the population**
- The advantages of sampling are:

  - It is quicker and cheaper than a census
  - It leads to less data needing to be analysed
- The disadvantages of sampling are:

  - It might not represent the population accurately
  - It could introduce ***bias***

#### What is a statistic and its sampling distribution?

- A **statistic** is a **random variable** that is calculated by **only** using the **data from a sample**

  - It **does not contain** any **unknown values** such as population parameters
  - $\frac{Σx}{n}-\overline{X}^{2}$ would be a statistic as $\overline{X}$ is the mean of the sample
  - $\frac{Σx}{n}-μ^{2}$ would not be a statistic as μ is an unknown population parameter
- Common examples for a statistic include:

  - Sample mean, sample median, range of the sample, sample variance
- The **sampling distribution** of a statistic gives all the **possible values** of the statistic along with their **associated probabilities**

#### How do I find the sampling distribution of a statistic?

- **STEP 1**: **List all** the possible samples

  - Some samples can have the same combination of members but still list each one separately
  
    - AAB and ABA both contain two A's and one B
    - It can be helpful to group these together
  - Consider how many possible samples there are
  
    - If there are 2 different types of members in a population and you take a sample of 3 then there are 8 possible samples (2<sup>3 </sup>or 2 × 2 × 2)
- **STEP 2**: **Calculate** the **value** of the **statistic** for each possible sample

  - This is why grouping the samples with the same combination is helpful
- **STEP 3**: **Calculate** the **probability** of each sample being picked

  - The samples will be independent
  - If the population is described as being large then you can treat the sampling as if it were with replacement
  
    - The probability of selecting a type of member will be constant regardless of how many has already been selected
- **STEP 4**: **Construct** the **distribution** table

  - Add together the probabilities of the samples that result in the same value of the statistic

> **Worked Example**
> A money box contains a large number of £5, £10 and £20 notes.  50% are £5 notes, 30% are £10 notes and 20% are £20 notes.
> 
> A random sample of two notes is taken from the money box.
> 
> (a)    List all the possible samples.
> 
> (b)    Find the sampling distribution of the mean.
> 
> **Answer:**
> 
> ![2-1-1-sampling-distribution-we-solution-part-1](assets/4f03a0c32f18-image.bin)
> 
> ![2-1-1-sampling-distribution-we-solution-part-2](assets/e24b1cba8a3f-image.bin)
> 
> ![2-1-1-sampling-distribution-we-solution-part-3](assets/32b9b58b338f-image.bin)

> **Exam Hint**
> - Remember the probabilities in a sampling distribution should add up to 1. You can use this to either check your answer or as a shortcut to find the final probability once you have the others.
