---
note_id: "rn_MVmdjj8cvSzN5HQW"
title: "Cumulative Distribution Function"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/revision-notes/statistical-distributions/cumulative-distribution-function/cumulative-distribution-function
path: statistical-distributions/cumulative-distribution-function/cumulative-distribution-function
updated_at: "2026-07-02T08:19:38.659Z"
spec_point_ids: ["spcpt_QTHzFn6gZrVKcRdG"]
spec_point_codes: []
guided_study: false
---

# Cumulative Distribution Function

## Cumulative Distribution Function

> **Spec point** — `spcpt_QTHzFn6gZrVKcRdG`

## Cumulative Distribution Function

#### What is the cumulative distribution function (c.d.f.)?

- For a **continuous** **random** **variable**,*X* , with **probability** **density** **function f(x)** the **cumulative** **distribution** **function** (c.d.f.) is defined as

`bold F bold left parenthesis bold italic x subscript bold 0 bold right parenthesis bold equals bold italic P bold left parenthesis bold italic X bold less or equal than bold italic x subscript bold 0 bold right parenthesis bold equals bold integral subscript bold minus bold infinity end subscript superscript bold x subscript bold 0 end superscript bold f bold left parenthesis bold italic t bold right parenthesis bold space bold d bold italic t`

- Compare this to the cumulative distribution function for a **discrete random variable**

$F(x_{0})=P(X\leqx_{0})=$$\underset{x\leqx_{0}}{\sum}P(X=x)$

- F(x<sub>0</sub>) is the probability that *X* is a value less than or equal to x<sub>0</sub>
- Notice the use of **uppercase **$\text{F}$ for the **c.d.f.** but **lowercase** $\text{f}$  for the **p.d.f.**
- On the graph of the p.d.f. y= f(x)  this would be the area under the graph up to the (vertical) line x=x<sub>0</sub>
- F(x) should be defined for all values of $x\inℝ$
- The graph of the c.d.f. y = F(x) will

  - start on the x-axis (i.e. start at a probability of 0)
  - end at x = 1  (i.e. finish at a probability of 1)
  - will be **continuous** function, even when defined ***piecewise***

e.g.

`straight F left parenthesis x right parenthesis equals open curly brackets table row 0 cell x less than 0 end cell row cell 0.5 x squared end cell cell 0 less or equal than x less or equal than 1 end cell row cell 0.5 end cell cell 1 less or equal than x less or equal than 1.5 end cell row cell x minus 1 end cell cell 1.5 less or equal than x less or equal than 2 end cell row 1 cell x greater than 2 end cell end table close`

![BSM6-gbH_1-4-1-ial-fig1-cdf-graph](../../../assets/fd8fa9752435-bsm6-gbh-1-4-1-ial-fig1-cdf-graph.png)

- The horizontal lines at F(x) = 0 and F(x) = 1 may not always be shown

#### How do I find probabilities using the cumulative frequency distribution?

- $P(a\leqX\leqb)=F(b)-F(a)$
- Although $P(X=k)$, for all values of k , F(k) is not necessarily zero

#### How do I find the cumulative frequency distribution (c.d.f.) from the probability density function (p.d.f.) and vice versa?

- To find the c.d.f.,F(x)  , from the p.d.f.,f(x), **integrate**

`straight F left parenthesis x right parenthesis equals integral subscript negative infinity end subscript superscript x straight f left parenthesis t right parenthesis space d t`

- Ensure you define F(x) fully for$x\inℝ$  so include values of x for which F(x) = 0  and values of x for which F(x) = 1
- For piecewise functions as well as integrating you will need to add on the value of the c.d.f. at the end of the previous part

  - Suppose there are two sections to a p.d.f. $x\leqa$ and $x>a$
  - For $x>a$:

`straight F left parenthesis x right parenthesis equals integral subscript negative infinity end subscript superscript x straight f left parenthesis t right parenthesis space straight d t space equals integral subscript negative infinity end subscript superscript a straight f left parenthesis t right parenthesis space straight d t space plus integral subscript a superscript x straight f left parenthesis t right parenthesis space straight d t space equals space straight F left parenthesis a right parenthesis plus integral subscript a superscript x straight f left parenthesis t right parenthesis space straight d t`

- Therefore the c.d.f can be calculated for the interval *a < x < b*  by using

`straight F left parenthesis x right parenthesis space equals space straight F left parenthesis a right parenthesis space plus space integral subscript a superscript x straight f left parenthesis t right parenthesis space straight d t`

- See part (b) in the Worked Example below

- To find the p.d.f from the c.d.f., **differentiate**

$f(x)=\frac{d}{dx}F(x)$

- Any part of a c.d.f that is constant corresponds to the p.d.f. for that part being zero (the derivative of a constant is zero)

#### How do I find the median, quartiles and percentiles using the cumulative frequency distribution (c.d.f.)?

- For piecewise functions, first identify the section the required value lies in

  - To do this find the upper limit of each section of the c.d.f.
- To find the **median**, $m$, solve the equation F(m) = 0.5

  - The median is sometimes referred to as the second quartile, Q<sub>2</sub>
- To find the **lower quartile**, Q<sub>1</sub>, solve the equation F(Q<sub>1</sub>) = 0.25
- To find the **upper quartile**,Q<sub>3</sub>  , solve the equation F(Q<sub>3</sub> ) = 0.75
- To find the **n**<sup>**th**</sup>** percentile**, solve the equation ** **$F(p)=\frac{n}{100}$

> **Worked Example**
> a) The continuous random variable, $X$ , has cumulative distribution function
> 
> `straight F left parenthesis x right parenthesis equals open curly brackets table row cell space space space space space space space 0 end cell cell x less than 0 end cell row cell 1 fourth x open parentheses 4 minus x close parentheses end cell cell 0 less or equal than x less or equal than 2 end cell row cell space space space space space space space 1 end cell cell x greater than 2 end cell end table close`
> 
> Find
> 
> (i) $P(X>1.5)$
> 
> (ii) $P(0.5\leqX\leq1)$
> 
> (iii) The lower quartile of $X$.
> 
> (b) The continuous random variable, $X$, has probability density function
> 
> `f left parenthesis x right parenthesis equals open curly brackets table row cell 0.5 x end cell cell 0 less or equal than x less or equal than 1 end cell row cell 0.5 end cell cell 1 less or equal than x less or equal than 2.5 end cell row 0 otherwise end table close
> `
> 
> Find the cumulative frequency distribution, $F(x)$ .
> 
> **Answer:**
> 
> ![1-4-1-ial-fig2-we-solution-part-1](assets/3c9f2d6d5fc6-image.bin)
> 
> ![1-4-1-ial-fig2-we-solution-part-2](assets/ad80c247277a-image.bin)

> **Exam Hint**
> - Remember that P(X=k) = 0  , for any value of k, is zero
> 
>   - This can be easily missed when working with c.d.f. rather than a p.d.f.
> - A quick check you can do is verify that your c.d.f. is continuous
> 
>   - The value of the c.d.f. at the upper limit of one section should equal the value of the c.d.f at the lower limit of the next section
