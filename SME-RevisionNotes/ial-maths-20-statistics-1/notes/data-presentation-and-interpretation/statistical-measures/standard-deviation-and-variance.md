---
note_id: "rn_T4jKybvYV5tsrF5C"
title: "Standard Deviation & Variance"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-1/revision-notes/data-presentation-and-interpretation/statistical-measures/standard-deviation-and-variance
path: data-presentation-and-interpretation/statistical-measures/standard-deviation-and-variance
updated_at: "2026-07-02T08:19:38.611Z"
spec_point_ids: ["spcpt_73stmsk3vHbph42y"]
spec_point_codes: []
guided_study: false
---

# Standard Deviation & Variance

## Standard Deviation & Variance

> **Spec point** — `spcpt_73stmsk3vHbph42y`

## Standard Deviation & Variance

The **variance **is another measure for the spread of the data, it measures the variability from the mean of the data.

#### What is the variance and the standard deviation?

- The variance is a statistic that tells us how **varied **a set of data is

  - Data that is more spread out will have a greater variance
  - Data that is consistent and close together will have a smaller variance
- The **standard deviation **is the square root of the variance
- The symbol for the population standard deviation is the lowercase Greek letter sigma, **σ**  and for variance is sigma squared, **σ**<sup>2</sup>
- Standard deviation and variance are used interchangeably within this course so make sure you look out for which one a question shows or asks for

#### How are the variance and standard deviation calculated?

- There is more than one formula that can be used for calculating the variance, and you should choose the most useful one
- For a set of $n$ values $x_{1},x_{2},...,x_{i},...,x_{n}$the variance is the sum of the squares of the deviations from the mean, divided by the frequency

  - Variance =$\frac{Σ(x-\overline{x})^{2}}{n}$
  
    - This formula can be time consuming and therefore is rarely used in this statistics course
- A second, **easier to use version of the variance** is:

  - Variance = $\frac{Σx^{2}}{n}-\overline{x}^{2}$
  - This version is easier to work with and should be used in most instances
  
    - The **summary statistic **`begin mathsize 16px style S subscript x x end subscript equals straight capital sigma left parenthesis x subscript i space minus space top enclose x right parenthesis squared space equals space straight capital sigma x subscript i squared minus end style`$\frac{(Σx_{i})^{2}}{n}$** ** can help derive different formulae as shown below:

Variance =`begin mathsize 16px style sigma squared equals fraction numerator straight capital sigma left parenthesis x minus x with bar on top right parenthesis squared over denominator n end fraction equals S subscript x x end subscript over n equals 1 over n open parentheses straight capital sigma x squared minus left parenthesis straight capital sigma x right parenthesis squared over n close parentheses equals fraction numerator straight capital sigma x squared over denominator n end fraction minus open parentheses fraction numerator straight capital sigma x over denominator n end fraction close parentheses squared equals fraction numerator straight capital sigma x squared over denominator n end fraction minus x with bar on top squared space space end style`

- An easy way to remember this is to think of it as ‘*the sum of x squared over n minus the sum of the mean squared’*
- Most calculators can be used to find summary statistic such as the standard deviation and variance fairly quickly, practice finding it on yours

- The **standard deviation **is the square root of the variance

  - Standard deviation = $σ=\sqrt{\frac{Σ(x-\overline{x})^{2}}{n}}=\sqrt{\frac{Σx^{2}}{n}-\overline{x}^{2}}=\sqrt{\frac{S_{xx}}{n}}$
  
    - You are given the formula for *S*<sub>*xx*</sub> but not for variance or standard deviation
- The units for standard deviation are the same as the units for the data and the units for variance are the same as the units for the data but squared

#### How are the variance and standard deviation calculated from a frequency table?

- The method for finding the variance from a frequency table is similar to that of the mean

  - If calculating from a grouped frequency table, find the midpoints, $x$,  first
  - Multiply each $x$ value by its corresponding frequency and use these values within the formulae
  - The formulae will become
  
    - Variance = `sigma squared equals space fraction numerator straight capital sigma f left parenthesis x minus x with bar on top right parenthesis squared over denominator straight capital sigma f end fraction equals fraction numerator straight capital sigma f x squared over denominator straight capital sigma f end fraction minus open parentheses fraction numerator straight capital sigma f x over denominator straight capital sigma f end fraction close parentheses squared`
    - Standard deviation = `sigma space equals space square root of fraction numerator straight capital sigma f left parenthesis x minus x with bar on top right parenthesis squared over denominator straight capital sigma f end fraction end root equals square root of fraction numerator straight capital sigma f x squared over denominator straight capital sigma f end fraction minus open parentheses fraction numerator straight capital sigma f x over denominator straight capital sigma f end fraction close parentheses end root squared`

> **Worked Example**
> Phoom recorded the length of time, $t$ , it took him, in minutes, to answer a selection of further calculus exam questions. The data is summarised in the table below.
> 
> | **Time (minutes)** | **Frequency** |
> |---|---|
> | $2\leqt<4$ | 1 |
> | $4\leqt<6$ | 4 |
> | $6\leqt<8$ | 7 |
> | $8\leqt<10$ | 5 |
> | $10\leqt<12$ | 2 |
> | $12\leqt<20$ | 2 |
> 
> (i) Calculate an estimate of the variance of the time taken to complete a question, include units with your answer.
> 
> (ii) Write down an estimate of the standard deviation of the time taken to complete a question, include units with your answer.
> 
> **Answer:**
> 
> ![2-1-3-sd-and-variance-we-solution-part-1](assets/fb6631117b23-image.bin)
> 
> ![2-1-3-sd-and-variance-we-solution-part-2](assets/8b8df8b34c5b-image.bin)

> **Exam Hint**
> - Look out for whether a question gives or asks for the standard deviation or variance, especially if the question is using sigma notation.
> - Choose which formula to use wisely, most of the time the summary statistics will be given so only one of the formulae will be possible. On the rare occasion that you are asked to calculate directly from a table think carefully about which version of the formula is quickest and easiest to use. It will almost always be the second version given in this revision note.
