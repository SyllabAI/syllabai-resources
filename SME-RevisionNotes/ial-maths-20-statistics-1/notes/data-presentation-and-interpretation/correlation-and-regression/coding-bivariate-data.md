---
note_id: "rn_4R8sYbk6yXMQXpqz"
title: "Coding Bivariate Data"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-1/revision-notes/data-presentation-and-interpretation/correlation-and-regression/coding-bivariate-data
path: data-presentation-and-interpretation/correlation-and-regression/coding-bivariate-data
updated_at: "2026-07-02T08:19:38.614Z"
spec_point_ids: ["spcpt_Ts2cmxwNWDPfMXhV", "spcpt_v276T7HQgJMZgXj9"]
spec_point_codes: []
guided_study: false
---

# Coding Bivariate Data

## Coding with PMCC

> **Spec point** — `spcpt_Ts2cmxwNWDPfMXhV`

## Coding with PMCC

#### Does coding affect the product moment correlation coefficient (PMCC)?

- We can code data using **linear transformations**

  - *X* = *px* + *q*
  - *Y* = *my* + *n*
  
    - The new variables won't necessarily be the upper case versions of the old variables - they could be any letter
- $S_{xx},S_{yy}andS_{xy}$ are related to **variances** so they are affected when the coding involves a multiplication

  - $S_{XX}=p^{2}\timesS_{xx}$
  - $S_{YY}=m^{2}\timesS_{yy}$
  - $S_{XY}=pm\timesS_{xy}$
- Coding **does not affect** the product moment correlation coefficient

  - The factors of *p* and *m* cancel out in the formula
  - $r_{XY}=r_{xy}$

## Coding Linear Regression

> **Spec point** — `spcpt_v276T7HQgJMZgXj9`

## Coding Linear Regression

#### Does coding affect the equation of the regression line of y on x?

- Coding **does affect** the equation of the regression line of *y* on *x*
- Coding is used to make numbers simpler to work with
- The equation of the regression line of *Y* on *X *can be calculated using the coded data
- This equation can then be used to find the equation of the regression line of *y* on *x*

#### How do I use coding to find the equation of the regression line of y on x?

- Given the variables *x* and *y* are coded using

  - *X* = *px* + *q*
  - *Y* = *my* + *n*
- The equation of the regression line of *Y* on *X *can be calculated as *Y* = *A* + *BX*
- To find the equation of the regression line of *y* on *x*

  - Substitute the codes into the equation
  
    - *my* + *n *= *A* + *B(px* + *q)*
  - Rearrange into the form *y* = *a* + *bx*

> **Worked Example**
> Stewart collects data to compare the salaries, £*s* , and lengths of service, $l$ years, of employees in a business. Stewart codes the data using the formulae
> 
> $m=\frac{s-30000}{12}\mathrm{and}w=52l$.
> 
> Stewart finds that:
> 
> - the product moment correlation coefficient between $m$ and $w$ is 0.739,
> - the equation of the regression line of $m$on $y$ is $m=-83.1+3.65w$.
> 
> (a) Write down the product moment correlation coefficient between $s$ and $l$.
> 
> (b) The equation of the regression line of $s$ on $l$ can be written as $s=a+bl$. Find the      values of $a$ and $b$ to three significant figures.
> 
> **Answer:**
> 
> ![1-3-3-coding-bivariate-data-we-solution-part-1](assets/ff3ac09d02d1-image.bin)
> 
> ![1-3-3-coding-bivariate-data-we-solution-part-2](assets/a847e7d2f625-image.bin)

> **Exam Hint**
> - When rearranging the equation of the regression it is important that you don’t round your coefficients until the very end. Use your ANS button on your calculator to keep the accuracy.
