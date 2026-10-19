---
note_id: "rn_mpWN47tBs4bgsyzc"
title: "Correlation & Regression"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-1/revision-notes/data-presentation-and-interpretation/correlation-and-regression/correlation-and-regression
path: data-presentation-and-interpretation/correlation-and-regression/correlation-and-regression
updated_at: "2026-07-02T08:19:38.613Z"
spec_point_ids: ["spcpt_rSrCNWrrpTwPkFVq", "spcpt_v8HQfZhT6bcFJ28H"]
spec_point_codes: []
guided_study: false
---

# Correlation & Regression

## PMCC

> **Spec point** — `spcpt_rSrCNWrrpTwPkFVq`

## PMCC

#### What is the product moment correlation coefficient?

- The product moment correlation coefficient (PMCC) is a way of giving a numerical value to **linear correlation** of bivariate data
- The PMCC of a sample is denoted by the letter *r*

  - *r *can take any value such that $-1\leqr\leq1$
  
    - Can be written as `vertical line r vertical line less or equal than 1`
  - A positive value of *r *describes positive correlation
  - A negative value of *r * describes negative correlation
  - If *r = 0* there is no correlation
  - *r = 1 *means perfect positive correlation and *r = -1* means perfect negative correlation
  - The closer to 1 or -1, the stronger the correlation
- The gradient of the regression line does not change the value of *r*

![2-5-1-pmcc-diagram-1](../../../assets/2712b41c7ae0-2-5-1-pmcc-diagram-1.png)

#### How is the product moment correlation coefficient (PMCC) calculated?

- For *n* pairs of bivariate data (*x*, *y*) we define the following statistics

  - `begin mathsize 16px style S subscript x x end subscript equals straight capital sigma x squared minus open parentheses straight capital sigma x close parentheses squared over n end style`
  - `begin mathsize 16px style S subscript y y end subscript equals Σy squared minus open parentheses Σy close parentheses squared over n end style`
  - `begin mathsize 16px style S subscript x y end subscript equals straight capital sigma x y minus fraction numerator open parentheses straight capital sigma x close parentheses open parentheses straight capital sigma y close parentheses over denominator n end fraction end style`
  - These are given in the formula booklet
- These are related to variance and can be written in several different ways:

  - $S_{xx}$
  
    - `begin mathsize 16px style straight capital sigma open parentheses x minus x with bar on top close parentheses squared end style`
    - $Σx^{2}-n\overline{x}^{2}$
    - $nσ_{x}^{2}$
  - $S_{xy}$
  
    - $Σ(x-\overline{x})(y-\overline{y})$
    - $Σxy-n\overline{x}\overline{y}$
- The product moment correlation coefficient (PMCC) is then calculated using the formula

  - $r=\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}$
  - This is given in the formula booklet

## Calculating Regression Line

> **Spec point** — `spcpt_v8HQfZhT6bcFJ28H`

## Calculating Regression Line

If the PMCC is close to 1 or -1 then this suggests the data follows a linear model. In this case a regression line of the form *y* = *a* + *bx* is appropriate.

#### How do I calculate the equation of the regression line of y on x?

- The **gradient *****b*** of the **regression line** is calculated using the formula

  - $b=\frac{S_{xy}}{S_{xx}}$
  - This is given in the formulae booklet
- The **y-intercept** *a* of the **regression line** is calculated using the formula

  - $a=\overline{y}-b\overline{x}$
  - This is given in the formulae booklet
  - This is found using the fact that the point `open parentheses x with bar on top comma space y with bar on top close parentheses` lies on the regression line
- If you are asked to find the equation of the regression line of ***x***** on *****y***

  - *x = c + dy *
  - $d=\frac{S_{xy}}{S_{yy}}$
  - $c=\overline{x}-d\overline{y}$
  - These are not given in the formulae booklet

> **Worked Example**
> Ashika is a football coach to 20 children. She records how long it takes each of them to run a lap of the football pitch, $p$ seconds, and the distance that they can kick the football, $d$ metres.
> 
> Ashika calculates the following summary statistics:
> 
> $S_{pp}=687.2$        $\overline{p}=62.8$       $Σd=1566$       $Σd^{2}=124240$       $Σpd=99127$.
> 
> (a) Calculate $S_{pd}$.
> 
> (b) Calculate the product moment correlation coefficient between $p$ and $d$.
> 
> (c) Calculate the equation of the regression line of $d$ on $p$ giving your answer in the form $d=a+bp$
> 
> **Answer:           **
> 
> ![1-3-2-correlation-regression-we-solution-part-1](assets/e1222c21b89e-image.bin)
> 
> ![1-3-2-correlation-regression-we-solution-part-2](assets/8dc5e7e5cbf6-image.bin)
> 
> ![1-3-2-correlation-regression-we-solution-part-3](assets/f2795ce0504a-image.bin)

> **Exam Hint**
> - Questions typically use different variables instead of *x* and *y*. It might help to label the independent variable as *x* and the dependent variable as *y*, this will help you when calculating the equation of the regression line.
