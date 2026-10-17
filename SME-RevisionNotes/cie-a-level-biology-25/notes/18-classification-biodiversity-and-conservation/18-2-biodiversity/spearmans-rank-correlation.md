---
note_id: "rn_DF2NtMNFh27byY4G"
title: "Spearman's Rank Correlation"
source: https://www.savemyexams.com/a-level/biology/cie/25/revision-notes/18-classification-biodiversity-and-conservation/18-2-biodiversity/spearmans-rank-correlation
path: 18-classification-biodiversity-and-conservation/18-2-biodiversity/spearmans-rank-correlation
updated_at: "2026-10-15T18:23:47.423Z"
spec_point_ids: ["spcpt_khDYmn8DZHCNCXYr"]
spec_point_codes: []
guided_study: true
---

# Spearman's Rank Correlation

## Spearman's Rank Correlation

> **Spec point** — `spcpt_khDYmn8DZHCNCXYr` · use Spearman’s rank correlation and Pearson’s linear correlation to analyse the relationships between two variables, including how biotic and abiotic factors affect the distribution and abundance of species

## Spearman's rank correlation

- **Spearman’s rank** correlation test can be used to determine whether there is correlation between variables when:

  - Data is **not quantitative**, e.g. an abundance scale has been used rather than a count of individuals
  - A visual inspection of data suggests a **non-linear** correlation
  - Data may **not** be *normally distributed*
- Method:

  - **Step 1:** Create a scatter graph and identify a possible correlation (the relationship does not need to be linear, but should be consistently increasing or decreasing)
  - **Step 2:** State a null hypothesis
  - **Step 3:** Use the following equation to work out Spearman’s rank correlation coefficient *r*

![Spearmans rank equation, downloadable AS & A Level Biology revision notes](../../../assets/0905e901d299-spearmans-rank-equation.png)

Where:

- **r**<sub>**s**</sub> = Spearman’s rank coefficient
- **D** = difference in rank
- **n** = number of samples

- **Step 4:** Refer to a table that relates critical values of r<sub>s </sub>to levels of probability

- If the value calculated for Spearman’s rank (**ignoring any negative sign**) is greater than the critical value for the number of samples in the data ( *n* ) at the 0.05 *probability level*** ***(p)*,  then the **null hypothesis can be rejected**, meaning there is a correlation between two variables

> **Worked Example**
> A group of students conducted an experiment using quadrats to measure the abundance of different plant species in a neglected allotment. They wanted to see if there was correlation between the abundance of species C and D.  When they looked at their data and plotted a scatter graph they saw some correlation.
> 
> Investigate the possible correlation using Spearman’s rank correlation coefficient.
> 
> ![Scatter plot of species interaction, showing a positive correlation between individuals of species C (x-axis) and species D (y-axis).](assets/2ed4b54907f5-47659-httpscdn-savemyexams-comuploads202011spear.png)
> 
> *Scatter graph showing the correlation between the abundance of species C and species D*

Because the **data was not normally distributed** they decided to use Spearman’s rank correlation coefficient.

**Null hypothesis**: there is no correlation between the abundance of species C and species D.

- n = 10 because there are 10 quadrat samples

| **Quadrat** | **No. of individuals of species C** | **Rank for species C** | **No. of individuals of species D** | **Rank for species D** | **Difference in rank (D)** | **D**<sup>**2**</sup> |
|---|---|---|---|---|---|---|
| 1 | 36 | 7 | 25 | 6 | 1 | 1 |
| 2 | 1 | 1 | 4 | 1 | 0 | 0 |
| 3 | 23 | 5 | 8 | 4 | 1 | 1 |
| 4 | 51 | 10 | 32 | 9 | 1 | 1 |
| 5 | 26 | 6 | 27 | 7 | -1 | 1 |
| 6 | 8 | 2 | 5 | 2 | 0 | 0 |
| 7 | 43 | 9 | 35 | 10 | -1 | 1 |
| 8 | 12 | 3 | 6 | 3 | 0 | 0 |
| 9 | 20 | 4 | 10 | 5 | -1 | 1 |
| 10 | 41 | 8 | 29 | 8 | 0 | 0 |
|   |   |   |   |   |   | ∑D<sup>2</sup> = 6 |

**Step 1:** Rank each set of data (rank 1 being the smallest data figure)

**Step 2:** Find the difference in rank between the two species, **D**

**Step 3: **Square the difference in rank, **D**<sup>**2**</sup>

**Step 4:** Add up the values of D<sup>2</sup> to give **∑D**<sup>**2**</sup> (= 6)

**Step 5**: Substitute the appropriate numbers into the equation (remember ***n*** = 10)

`straight r subscript straight s equals 1 minus open parentheses fraction numerator 6 cross times sum from blank to blank of straight D squared over denominator straight n cubed minus straight n end fraction close parentheses`

`straight r subscript straight s equals 1 minus open parentheses fraction numerator 6 open parentheses 6 close parentheses over denominator 10 cubed minus 10 end fraction close parentheses equals 0.964`

**Step 5:**  Refer to a table that relates values of *r*<sub>*s*</sub> to probability. Look for the 0.05 probability level with n = 10

| **n** | **10** |
|---|---|
| Critical value of r<sub>s</sub> | 0.65 |

- Because R<sub>s</sub> = 0.964, it is greater than the critical value of 0.65
- The **null hypothesis can be rejected**, there is genuine **positive correlation** between the abundance of species C and D

> **Exam Hint**
> You will be provided with the formula for Spearman’s rank correlation in the exam. You need to be able to carry out the calculation to test for correlation, as you could be asked to do this in the exam. You should understand when it is appropriate to use the different statistical tests that crop up in this topic, and the conditions in which each is valid.
> 
> **Correlation does not always mean causation. **Just because there is a correlation between the abundance of species C and species D it does not mean that the presence of species C causes the presence of species D.
