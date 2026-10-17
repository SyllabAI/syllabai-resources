---
note_id: "rn_N7pggdgXQ8P3xPSB"
title: "Unbiased Estimates"
source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/revision-notes/statistical-sampling-and-estimation/sampling-and-estimation/unbiased-estimates
path: statistical-sampling-and-estimation/sampling-and-estimation/unbiased-estimates
updated_at: "2026-07-02T08:19:38.276Z"
spec_point_ids: ["spcpt_fRD8dzP7gVHcXjn6"]
spec_point_codes: []
guided_study: true
---

# Unbiased Estimates

## Unbiased Estimates

> **Spec point** — `spcpt_fRD8dzP7gVHcXjn6`

## Unbiased Estimates

#### What is an unbiased estimator of a population parameter?

- An **estimator** is a ***statistic***** **that is used to estimate a **population parameter**

  - When a sample is used with the estimator, the value that it produces is called an **estimate**
- An estimator is called **unbiased** if the **expected value** of the estimator is **equal** to the **population parameter**

  - An estimate from an unbiased estimator is called an unbiased estimate
  - This means that the **mean** of the **unbiased estimates** will get **closer** to the **population parameter** as more samples are taken

#### What are the unbiased estimates for the mean and variance of a population?

- If you had the data for a **whole population** you could find the **actual population mean** and **variance** using

  - $μ=\frac{Σx}{n}$
  - $σ^{2}=\frac{Σ(x-μ)^{2}}{n}=\frac{Σx^{2}}{n}-μ^{2}$
- If you are using a **sample to estimate** the **mean** of a population then an **unbiased estimate** is given by

  - $\overline{x}=\frac{Σx}{n}$
  - This is the **same formula** for the population mean
- If you are using a **sample to estimate** the **variance** of a population then an **unbiased estimate** is given by

  - $s^{2}=\frac{Σ(x-\overline{x})^{2}}{n-1}$
  - This can be written in different ways
  - `begin mathsize 16px style s squared equals fraction numerator capital sigma open parentheses x minus x with bar on top close parentheses squared over denominator n minus 1 end fraction equals fraction numerator 1 over denominator n minus 1 end fraction open parentheses capital sigma x squared minus open parentheses capital sigma x close parentheses squared over n close parentheses equals fraction numerator n over denominator n minus 1 end fraction open parentheses fraction numerator capital sigma x squared over denominator n end fraction minus x with bar on top squared close parentheses end style`
  - This is a **different formula** to the population variance
  - The last formula shows a method for finding an unbiased estimate for the variance
  
    - Find the variance of the sample (treating it as a population)
    - Multiply this by $\frac{n}{n-1}$

#### Is there an unbiased estimate for the standard deviation?

- Unfortunately square rooting an unbiased variance **does not** result in an unbiased standard deviation
- There is **not a formula** for an unbiased estimate for the **standard deviation** that works for all populations

  - Therefore it is better to just work with the variance and not the standard deviation
- If you need an estimate for the standard deviation then you can use:

  - You can use the square root of your unbiased estimate for the population variance
  
    - `begin mathsize 16px style s equals square root of fraction numerator straight capital sigma left parenthesis x minus x with bar on top right parenthesis squared over denominator n minus 1 end fraction end root equals square root of fraction numerator 1 over denominator n minus 1 end fraction open parentheses capital sigma x squared minus open parentheses capital sigma x close parentheses squared over n close parentheses end root end style`
  - This **won’t be unbiased** but it will be a good estimate

#### How do I calculate unbiased estimates?

- If you are given the **summary statistics **$Σx$ and $Σx^{2}$ then you can simply use the formulae in the **formula booklet**

  - $\overline{x}=\frac{Σx}{n}$
  - `begin mathsize 16px style s squared equals fraction numerator 1 over denominator n minus 1 end fraction open parentheses straight capital sigma x squared minus open parentheses straight capital sigma x close parentheses squared over n close parentheses end style`
- If you are given the **raw** data then you will **first** need to **calculate **$Σx$ **and **$Σx^{2}$

> **Worked Example**
> The times, $T$ minutes, spent on daily revision of a random sample of 50 A Level students from the UK are summarised as follows.
> 
> $n=50$      $Σt=6174$        $Σt^{2}=831581$
> 
> Calculate unbiased estimates of the population mean and variance of the times spent on daily revision by A Level students in the UK
> 
> **Answer:**
> 
> ![1-2-1-unbiased-estimates-we-solution](assets/114db671eb85-image.bin)

> **Exam Hint**
> - Always check whether you need to divide by n or n-1 by looking carefully at the wording in the question.
