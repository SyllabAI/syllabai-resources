---
note_id: "rn_BH34b52QZKBx3nqG"
title: "Probability Density Function"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/revision-notes/statistical-distributions/continuous-random-variables/probability-density-function
path: statistical-distributions/continuous-random-variables/probability-density-function
updated_at: "2026-07-02T08:19:38.652Z"
spec_point_ids: ["spcpt_JMz3SfGShXWm8TqR", "spcpt_yyQVJRMwfJDN5gPx"]
spec_point_codes: []
guided_study: false
---

# Probability Density Function

## Calculating Probabilities using PDF

> **Spec point** — `spcpt_JMz3SfGShXWm8TqR`

## Calculating Probabilities using PDF

#### What is a probability density function (p.d.f.)?

- For a ***continuous random variable***, it is often possible to model probabilities using a function

  - This function is called a **probability density function (p.d.f.)**
  - For the continuous random variable, *X*  , it would usually be denoted as a function of x  (such as f(x)  or g(x) ) and is usually given **piecewise**

e.g.

`straight f left parenthesis x right parenthesis equals open curly brackets table row x cell 0 less or equal than x less or equal than 1 end cell row 1 cell 1.5 less or equal than x less or equal than 2 end cell row 0 otherwise end table close`

- f(x) should be defined for all values of $x\inℝ$
- The distribution (or **density**) of probabilities can be illustrated by the graph of f(x)
- The graph does not need to start and end on the x-axis
- The graph does not have to be continuous

![1-3-1-ial-fig1-pdf-graph](../../../assets/bffa6f41d2bb-1-3-1-ial-fig1-pdf-graph.png)

- For f(x) to **represent** a p.d.f. the following conditions must apply

  - $f(x)\geq0$ for **all** values of x
  
    - This is the equivalent to $P(X=x)\geq0$  for a discrete random variable
  - The **area under the graph** must total 1

`integral subscript negative infinity end subscript superscript infinity straight f left parenthesis x right parenthesis space straight d x equals 1`

- This is equivalent to $Σ$ $P(X=x)=1$ for a discrete random variable

#### How do I find probabilities using a probability density function (p.d.f.)?

- The probability that the continuous random variable *X* lies in the interval
$a\leqX\leqb$, where *X* has the probability density function f(x) , is given by

`straight P left parenthesis a less or equal than X less or equal than b right parenthesis equals integral subscript a superscript b straight f left parenthesis straight x right parenthesis space dx`

- As with the **normal** **distribution **$P(a\leqX\leqb)=P(a<X<b)$

  - for any continuous random variable, $P(X=n)=0$  for all values of n
  - One way to think of this is that $a=b$ in the integral above

- ***Piecewise Function*** are often used as the p.d.f. is not often a single function of x

  - Finding a probability may involve splitting the area across more than one piece of the function
  - This will depend on the limits a and b in $P(a\leqX\leqb)$ that is being found

#### How do I solve problems using the PDF?

- Some questions may ask for justification of the use of a given function for a probability density function

  - In such cases check that the function meets the two conditions $f(x)\geq0$ for all values of $x$ and the total area under the graph is 1

- If asked to find a probability

  - STEP 1
  As the **probability** **density** **function**, f(x), is usually given **piecewise** make sure you are clear about the values of x for which each part applies

e.g.  `straight f left parenthesis straight x right parenthesis equals open curly brackets table row cell x minus 1 space space space 1 less or equal than x less or equal than 2 end cell row cell 3 minus x space space space 2 less or equal than x less or equal than 3 end cell row cell 0 space space space space space space space space otherwise end cell end table close`

- STEP 2

If simple to do so, **sketching** the **graph** of y= f(x) may help to find the probability

- Look for **basic** **shapes** such as **triangles** or **rectangles**; finding **areas** of these is easy and avoids integration
- Look for **symmetry** in the graph that may make the problem easier

- STEP 3

  - Identify the **range** of X, particularly noting if it is split across different parts of the p.d.f.
  - Find the required **area (probability)**, either by **basic** **shapes** or **integrate f(x)** and evaluate it between the two limits, splitting if necessary
- Trickier problems may involve finding a limit of the integral given its value

  - i.e. one of the values in the range of *X*, given the probability
  e.g.        Find the value of  given $P(0\leqX\leqa)=0.09$

> **Worked Example**
> The continuous random variable, $X$ , has probability density function
> 
> `straight f left parenthesis x right parenthesis equals open curly brackets table row cell 0.4 left parenthesis x minus 1 right parenthesis end cell cell 1 less or equal than x less or equal than 2 end cell row cell 0.1 left parenthesis 6 minus x right parenthesis end cell cell 2 less or equal than x less or equal than 6 end cell row cell space space space space space space space 0 end cell otherwise end table close`
> 
> (a) Show that $f(x)$ can represent a probability density function.
> 
> (b) Find
> 
> (i) $P(X>4)$
> 
> (ii) $P(X=3.2)$
> 
> (iii) $P(1.5\leqX\leq2.5)$
> 
> **Answer:**
> 
> ![1-3-1-ial-fig2-we-solution-part-1](assets/50e0f4b45421-image.bin)
> 
> ![1-3-1-ial-fig2-we-solution-part-2](assets/36bfdc99cd34-image.bin)
> 
> ![1-3-1-ial-fig2-we-solution-part-3](assets/17e2828d66e6-image.bin)

> **Exam Hint**
> - If the graph is easy to draw, then a sketch of f(x) is helpful
> 
>   - Some p.d.f. graphs have **symmetry**, common shapes such as **triangles** or **rectangles** so areas are easier to find, avoiding the need for integration
> - Always keep an eye for probabilities that are split across different parts of a piecewise function

## Median and Mode of a CRV

> **Spec point** — `spcpt_yyQVJRMwfJDN5gPx`

## Median and Mode of a CRV

#### What is meant by the median of a continuous random variable?

- The **median**, ***m***, of a continuous random variable, *X* , with **probability** **density** **function f(x)** is defined as the value of the **continuous** **random** **variable** *X*, such that

$P(X<m)=P(X>m)=0.5$

- ** **Since $P(X=m)=0$ this can also be written as $P(X\leqm)=P(X\geqm)=0.5$
- If the p.d.f. is **symmetrical** (i.e. the graph of y = f(x) is symmetrical) then the median will be halfway between the lower and upper limits of x

  - In such cases the graph of y=f(x) has axis of symmetry in the line x = m

#### How do I find the median of a continuous random variable?

- By solving one of the equations to find *m*

`integral subscript negative infinity end subscript superscript m straight f left parenthesis x right parenthesis space dx space equals space 0.5`

and

`integral subscript m superscript infinity straight f left parenthesis straight x right parenthesis space dx equals 0.5`

- If the graph of $y=f(x)$ is **symmetrical**, symmetry may be used to deduce the median
- For ***piecewise functions***, you will need to determine which part of the function the median lies within to determine which equation to use

  - If there are more than two (non-zero) parts to a function then the integration may need splitting
- You can also use the **cumulative** **distribution** **function** to find the median

#### How do I find quartiles (or percentiles) of a continuous random variable?

- In a similar way to finding the median

  - The lower quartile will be the value *L *such that P(*X* ≤ *L*) = 0.25 or
  P(*X* ≥ *L*) = 0.75
  - The upper quartile will be the value *U* such that P(*X* ≤ *U*) = 0.75 or
  P(*X* ≥ *U*) = 0.25
- Percentiles can be find in the same way

  - The 15<sup>th</sup> percentile will be the value *k* such that P(*X* ≤ *k*) = 0.15 or
  P(*X* ≥ *k*) = 0.85
- In all cases start by determining which part(s) of the function are involved

#### What is meant by the mode of a continuous random variable?

- The **mode** of a continuous random variable, *X*  , with **probability** **density** **function f(x)** is the value of x that produces the greatest value of f(x) .

#### How do I find the mode of a PDF?

- This will depend on the type of function f(x); the easiest way to find the mode is by considering the shape of the graph of y= f(x)
- If the graph is a curve with a (local) **maximum** **point**, the mode can be found by **differentiating** and solving the equation f'(x) = 0

  - If there is more than one solution to f'(x) =  0 , further work may be needed to deduce which answer is the mode
  
    - Look for valid values of $x$ from the **definition** of the p.d.f.
    - Use the **second** **derivative** (f'' (x) ) to deduce the nature of each **stationary** **point**
    - You may need to check the values of f(x) at the **endpoints** too

> **Worked Example**
> The continuous random variable $X$  has probability density function $f(x)$ defined as
> 
> `straight f left parenthesis x right parenthesis equals open curly brackets table row cell 1 over 64 x open parentheses 16 minus x squared close parentheses end cell cell 0 less or equal than x less or equal than 4 end cell row cell space space space space space space space space 0 end cell otherwise end table close space space space space space space space space space space space space space space space space space space space space space space`
> 
> (a) Find the median of *X*, giving your answer to three significant figures
> 
> (b) Find the *exact* value of the mode of *X*
> 
> **Answer:**
> 
> ![2-3-1-cie-fig3-we-solution_a](assets/6282648adc49-image.bin)
> 
> ![2-3-1-cie-fig3-we-solution_b](assets/a13c21bf64a3-image.bin)

> **Exam Hint**
> - Avoid spending too long sketching the graph of  y = f(x), only do this if the graph is straightforward as finding the median and mode by other means can be just as quick
