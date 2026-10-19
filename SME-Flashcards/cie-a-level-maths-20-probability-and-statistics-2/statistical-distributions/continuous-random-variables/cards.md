# Continuous Random Variables

Course: cie-a-level-maths-20-probability-and-statistics-2 · Section: Statistical Distributions

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/flashcards/statistical-distributions/continuous-random-variables/


## Card 1 — keyword_definition (`fl_h7cXMXt4t8Vc4Myx`)

**FRONT**

Define **probability density function**.


**BACK**

A **probability density function**, written $\text{f} ( x )$, is a function used to model the probabilities of a **continuous** random variable.

Probability is represented by **area** under the graph of $y = \text{f} ( x )$ rather than by the height of the curve.

That is why a density can exceed 1 while a probability never can.


Spec links: `spcpt_v7Mj9nd2MKFtYff7`


## Card 2 — fill_in_the_blanks (`fl_VZbjNhDF7Whbv2BY`)

**FRONT**

Fill in the two conditions a function must satisfy to be a probability density function:

`\text{f}(x) \_\_\_\_\_\_ 0` for all values of $x$

`\int_{-\infty}^{\infty} \text{f}(x) \text{ d}x = \_\_\_\_\_\_`


**BACK**

The completed conditions are:

$\text{f} ( x ) \geq 0$ for all values of $x$

`\int_{-\infty}^{\infty} \text{f}(x) \text{ d}x = 1`

These are the continuous versions of the two conditions on a discrete distribution, that no probability is negative and that they all total 1.

A question asking you to show a function can be a density function is asking you to check both.


*Blanks: 0 — answers: []*

Spec links: `spcpt_v7Mj9nd2MKFtYff7`

Flags: fitb_no_blank_marker


## Card 3 — true_or_false (`fl_Jm3v2jdnhncjfmRt`)

**FRONT**

**True or False?**

Every probability from a probability density function has to be found by integrating.


**BACK**

**False.**

The probability is the **area** under the graph, so whenever that area is a triangle or a rectangle you can simply work it out.

A quick sketch is worth doing for that reason alone, and it may also reveal symmetry that saves further work.


Spec links: `spcpt_v7Mj9nd2MKFtYff7`


## Card 4 — question_and_answer (`fl_gt94mgbVjNWKsK4f`)

**FRONT**

For a continuous random variable, what is $\text{P} ( X = n )$, and what follows?


**BACK**

It is **zero** for every value of $n$, because the area under the graph between $n$ and itself is zero.

It follows that the endpoints contribute nothing, so $\text{P} ( a \leq X \leq b ) = \text{P} ( a < X < b )$.

Strict and weak inequalities can therefore be used interchangeably throughout, which is never true of a discrete variable.


Spec links: `spcpt_v7Mj9nd2MKFtYff7`


## Card 5 — question_and_answer (`fl_z5hCwwX2y3ZxWFqc`)

**FRONT**

A question gives $\text{P} ( 0 \leq X \leq a ) = 0 . 09$ and asks for $a$. How do you find it?


**BACK**

Integrate the density from 0 to $a$, leaving $a$ as an unknown limit, then set the result equal to $0 . 09$ and solve.

The integral produces an expression in $a$, so the probability question turns into an ordinary equation.

Check at the end that the value you get actually lies in the range over which the density is defined.


Spec links: `spcpt_v7Mj9nd2MKFtYff7`


## Card 6 — fill_in_the_blanks (`fl_fw35kv2hpmm7JdqR`)

**FRONT**

Complete the equation defining the median $m$ of a continuous random variable:

`\int_{-\infty}^{m} \text{f}(x) \text{ d}x = \_\_\_\_\_\_`


**BACK**

The completed equation is:

`\int_{-\infty}^{m} \text{f}(x) \text{ d}x = 0.5`

The median is the value with half the area to its left and half to its right, so $\text{P} ( X < m ) = \text{P} ( X > m ) = 0 . 5$.

Integrating from $m$ upwards and setting that equal to $0 . 5$ works equally well, and one of the two is usually easier.


*Blanks: 0 — answers: []*

Spec links: `spcpt_VdGVXD7z4VX9BsBs`

Flags: fitb_no_blank_marker


## Card 7 — question_and_answer (`fl_fRnXCbXBYDj8fqJj`)

**FRONT**

How do you find the lower quartile or the 15th percentile of a continuous random variable?


**BACK**

Exactly as for the median, but with a different area: the lower quartile $L$ satisfies $\text{P} ( X \leq L ) = 0 . 25$.

The 15th percentile $k$ satisfies $\text{P} ( X \leq k ) = 0 . 15$, and any percentile works the same way.

Each is an equation in one unknown limit, solved by integrating up to that limit.


Spec links: `spcpt_VdGVXD7z4VX9BsBs`


## Card 8 — question_and_answer (`fl_Cycrg22vwG6Cgs3X`)

**FRONT**

What is the mode of a continuous random variable, and how do you find it?


**BACK**

The **mode** is the value of $x$ at which $\text{f} ( x )$ is **greatest**.

Where the graph is a curve with a maximum, differentiate and solve $\text{f} ' ( x ) = 0$.

If that gives more than one solution, use the second derivative or check the endpoints, and discard any value outside the range where the density is defined.


Spec links: `spcpt_VdGVXD7z4VX9BsBs`


## Card 9 — question_and_answer (`fl_dd6nQjZhkFkJjtnz`)

**FRONT**

When can the median be written down without any integration at all?


**BACK**

When the graph of $y = \text{f} ( x )$ is **symmetrical**.

The axis of symmetry then splits the area into two equal halves, so the median sits on it, halfway between the lower and upper limits.

A sketch is what reveals this, and it turns a page of integration into one line.


Spec links: `spcpt_VdGVXD7z4VX9BsBs`


## Card 10 — fill_in_the_blanks (`fl_qwKM27K9MYBk2dgv`)

**FRONT**

Complete the mean of a continuous random variable with density $\text{f} ( x )$:

`\text{E}(X) = \int_{-\infty}^{\infty} \_\_\_\_\_\_ \text{ d}x`


**BACK**

The completed formula is:

`\text{E}(X) = \int_{-\infty}^{\infty} x\,\text{f}(x) \text{ d}x`

Each value is weighted by the density at that value and then totalled, which is what an integral does.

It is the continuous version of $Σ x \text{P} ( X = x )$, with the sum replaced by an integral.


*Blanks: 0 — answers: []*

Spec links: `spcpt_tQpsd6ts3DXRzHSR`

Flags: fitb_no_blank_marker


## Card 11 — question_and_answer (`fl_qGSvtQXKxmkSf2Qr`)

**FRONT**

How do you find $\text{E} ( \text{g} ( X ) )$ for a continuous random variable?


**BACK**

Integrate $\text{g} ( x )  \text{f} ( x )$ over the whole range, so `\text{E}(\text{g}(X)) = \int_{-\infty}^{\infty} \text{g}(x)\,\text{f}(x) \text{ d}x`.

The density is left untouched: it is only the quantity being averaged that the function is applied to.

Taking $\text{g} ( x ) = x^{2}$ gives $\text{E} ( X^{2} )$, which is the case you need most often.


Spec links: `spcpt_tQpsd6ts3DXRzHSR`


## Card 12 — fill_in_the_blanks (`fl_Bq29DSXJ9b78zwXR`)

**FRONT**

Complete the variance of a continuous random variable:

`\text{Var}(X) = \int_{-\infty}^{\infty} x^{2}\,\text{f}(x) \text{ d}x - \_\_\_\_\_\_`


**BACK**

The completed formula is:

`\text{Var}(X) = \int_{-\infty}^{\infty} x^{2}\,\text{f}(x) \text{ d}x - \left[\text{E}(X)\right]^{2}`

The integral is $\text{E} ( X^{2} )$, so this is the familiar mean of the squares minus the square of the mean.

The standard deviation is the square root of the result.


*Blanks: 0 — answers: []*

Spec links: `spcpt_tQpsd6ts3DXRzHSR`

Flags: fitb_no_blank_marker


## Card 13 — question_and_answer (`fl_QQmt2M89KSyCpMVB`)

**FRONT**

What is the difference between $\text{E} ( X^{2} )$ and `\left[\text{E}(X)\right]^{2}`?


**BACK**

$\text{E} ( X^{2} )$ is the **mean of the squares**: square the variable first, then integrate against the density.

`\left[\text{E}(X)\right]^{2}` is the **square of the mean**: integrate first, then square the single number you get.

The order is what separates them, and doing it the wrong way round is the usual reason a variance comes out negative.


Spec links: `spcpt_tQpsd6ts3DXRzHSR`


## Card 14 — question_and_answer (`fl_Pvj9DWnChX8QCRFF`)

**FRONT**

For $\text{f} ( x ) = 1 . 5 x^{2} ( 1 - 0 . 5 x )$ on $0 \leq x \leq 2$, how do you get to the variance?


**BACK**

Work out $\text{E} ( X ) = 1 . 2$ by integrating $x  \text{f} ( x )$, then $\text{E} ( X^{2} ) = 1 . 6$ by integrating $x^{2}  \text{f} ( x )$.

Subtracting gives

$\text{Var} ( X ) = 1 . 6 - 1 . 2^{2} = 1 . 6 - 1 . 44 = 0 . 16$

Both integrals run only over the interval where the density is non-zero, since it contributes nothing elsewhere.


Spec links: `spcpt_tQpsd6ts3DXRzHSR`


## Card 15 — true_or_false (`fl_XP96mz29q6wgtH9v`)

**FRONT**

**True or False?**

If the graph of the density function is symmetrical about $x = a$, then $\text{E} ( X ) = a$.


**BACK**

**True.**

The weighting either side of the axis of symmetry balances exactly, so the mean sits on that axis.

Spotting it saves the whole integration for the mean, and it gives the median at the same time, since the two coincide for a symmetrical density.


Spec links: `spcpt_tQpsd6ts3DXRzHSR`


## Card 16 — keyword_definition (`fl_s9NsK4rqJ5YpKnpp`)

**FRONT**

Define **continuous uniform distribution**.


**BACK**

The **continuous uniform distribution**, also called the **rectangular** distribution, has a density that is **constant and non-zero** over one interval and zero everywhere else.

So every part of the interval is equally likely, and the graph of $\text{f} ( x )$ is a horizontal line segment.

It is the simplest continuous distribution there is, and the one where no integration is ever needed.


Spec links: `spcpt_KybbZBNFjfVCQzYj`


## Card 17 — question_and_answer (`fl_bYDB6cTJNzrVvhxQ`)

**FRONT**

For a uniform distribution on $a \leq x \leq b$, what is the height of the density?


**BACK**

It is $\frac{1}{b-a}$.

The area under the graph has to be 1, and the shape is a rectangle of width $b - a$, so the height must be the reciprocal of that width.

A narrow interval therefore gives a tall density, which is how a density can exceed 1 without anything being wrong.


Spec links: `spcpt_KybbZBNFjfVCQzYj`


## Card 18 — question_and_answer (`fl_smkVJNSckpYtTTjr`)

**FRONT**

How do you find a probability for a continuous uniform distribution?


**BACK**

Sketch the rectangle and work out the **area** of the part you want, which is just width multiplied by height.

So $\text{P} ( 2 . 5 \leq X \leq 3 )$ for a density of $0 . 4$ is $0 . 5 \times 0 . 4 = 0 . 2$.

Integration would give the same answer, but there is never any reason to use it here.


Spec links: `spcpt_KybbZBNFjfVCQzYj`


## Card 19 — fill_in_the_blanks (`fl_y5Cx9KmRQrCwFH8x`)

**FRONT**

For a uniform distribution on $a \leq x \leq b$, fill in the mean and the variance:

`\text{E}(X) = \_\_\_\_\_\_`

`\text{Var}(X) = \_\_\_\_\_\_`


**BACK**

The completed results are:

$\text{E} ( X ) = \frac{1}{2} ( a + b )$

$\text{Var} ( X ) = \frac{1}{12} ( b - a )^{2}$

The mean is simply the midpoint, which is the axis of symmetry of the rectangle, and the median is the same value.

The variance depends only on the **width** of the interval, not on where that interval sits.


*Blanks: 0 — answers: []*

Spec links: `spcpt_KybbZBNFjfVCQzYj`

Flags: fitb_no_blank_marker


## Card 20 — true_or_false (`fl_MCpVsz4sxS64Qcjh`)

**FRONT**

**True or False?**

A continuous uniform distribution has no mode.


**BACK**

**True.**

The mode is the value where the density is greatest, and here the density takes the **same** value everywhere on the interval.

No single value is more likely than any other, so there is nothing for the mode to be.


Spec links: `spcpt_KybbZBNFjfVCQzYj`


## Card 21 — question_and_answer (`fl_cq3B8p52RMnG5WWd`)

**FRONT**

A uniform density is $0 . 4$ on $a \leq x \leq 4$. How do you find $a$?


**BACK**

The total area must be 1, so $0 . 4 \times ( 4 - a ) = 1$, giving $4 - a = 2 . 5$ and $a = 1 . 5$.

The height and the width of the rectangle are reciprocals of one another, so knowing either one fixes the other.

That single equation is enough whenever one endpoint or the height is missing.


Spec links: `spcpt_KybbZBNFjfVCQzYj`

