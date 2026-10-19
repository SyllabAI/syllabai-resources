# Cumulative Distribution Function

Course: ial-maths-20-statistics-2 · Section: Statistical Distributions

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/flashcards/statistical-distributions/cumulative-distribution-function/


## Card 1 — keyword_definition (`fl_nGx26PVJbjWpKXPW`)

**FRONT**

Define the **cumulative distribution function** of a continuous random variable.


**BACK**

It is `\text{F} \left(x_{0}\right) = \text{P} \left(X \le x_{0}\right)`, the probability that $X$ takes a value less than or equal to $x_{0}$.

On the graph of the probability density function this is the **area** under the curve up to the vertical line at $x = x_{0}$.


Spec links: `spcpt_QTHzFn6gZrVKcRdG`


## Card 2 — question_and_answer (`fl_xV4X39NkDtF3Kd5q`)

**FRONT**

What is the difference between `\text{F} \left(x\right)` and `\text{f} \left(x\right)`?


**BACK**

The capital $\text{F}$ is always the **cumulative distribution function** and the lower-case $\text{f}$ is always the **probability density function**, and the two are never used the other way round.

`\text{F} \left(x\right)` is an accumulated probability, so it always lies between 0 and 1, whereas `\text{f} \left(x\right)` is a density and is not a probability at all.

That is why `\text{f} \left(x\right)` is allowed to be greater than 1 while `\text{F} \left(x\right)` never is.


Spec links: `spcpt_QTHzFn6gZrVKcRdG`


## Card 3 — true_or_false (`fl_CbQBYjqgb7VknnpB`)

**FRONT**

**True or False?**

For a continuous random variable `\text{P} \left(X = k\right) = 0` for every $k$, so `\text{F} \left(k\right)` must be 0 as well.


**BACK**

**False.**

`\text{F} \left(k\right)` is `\text{P} \left(X \le k\right)`, the whole accumulated probability up to $k$, and not the probability of the single value $k$.

So a variable can perfectly well have `\text{P} \left(X = 2\right) = 0` and `\text{F} \left(2\right) = 0 . 75` at the same time, and this slips past people far more easily when working with $\text{F}$ than with $\text{f}$.


Spec links: `spcpt_QTHzFn6gZrVKcRdG`


## Card 4 — fill_in_the_blanks (`fl_6GDHKVwtsVbstFQT`)

**FRONT**

One of only two formulae in this module that the formula booklet does not give you links $\text{f}$ and $\text{F}$. Complete both directions:

`\text{F} \left(x\right) = \int_{- \infty}^{x} \_\_\_\_\_\_ \text{d} t`

`\text{f} \left(x\right) = \frac{\text{d}}{\text{d} x} \_\_\_\_\_\_`


**BACK**

The completed formulae are:

`\text{F} \left(x\right) = \int_{- \infty}^{x} \text{f} \left(t\right) \text{d} t`

`\text{f} \left(x\right) = \frac{\text{d}}{\text{d} x} \text{F} \left(x\right)`

Integrating takes you from the density to the accumulated probability, and differentiating brings you straight back the other way.

The dummy variable $t$ in the first is there only because $x$ is already being used as the upper limit.


*Blanks: 0 — answers: []*

Spec links: `spcpt_QTHzFn6gZrVKcRdG`


## Card 5 — true_or_false (`fl_55yqZvHF6WpxbZy5`)

**FRONT**

**True or False?**

The graph of a cumulative distribution function is always continuous, even when $\text{F}$ is defined piecewise.


**BACK**

**True.**

Because `\text{P} \left(X = k\right) = 0` for a continuous variable, no probability is ever added in a single jump, so $\text{F}$ cannot step upwards anywhere.

It climbs without breaks from 0 on the left to 1 on the right, so where two pieces meet their values must agree, which is the quickest check on a piecewise $\text{F}$.


Spec links: `spcpt_QTHzFn6gZrVKcRdG`


## Card 6 — question_and_answer (`fl_mSWTYFZ7Kwm2qnyR`)

**FRONT**

Once you have `\text{F} \left(x\right)`, how do you find `\text{P} \left(a \le X \le b\right)`?


**BACK**

Subtract one value of $\text{F}$ from the other:

`\text{P} \left(a \le X \le b\right) = \text{F} \left(b\right) - \text{F} \left(a\right)`

Everything accumulated up to $b$, less everything accumulated up to $a$, leaves exactly the probability in between.

Once $\text{F}$ is known no integration is needed at all, which is what makes finding $\text{F}$ first worth the effort when several probabilities are wanted.


Spec links: `spcpt_QTHzFn6gZrVKcRdG`


## Card 7 — question_and_answer (`fl_2XjPfKp5jc67S5Ck`)

**FRONT**

You are building `\text{F} \left(x\right)` from a piecewise `\text{f} \left(x\right)`. Why is integrating each piece between its own limits not enough?


**BACK**

Because $\text{F}$ **accumulates**, so each piece has to start from the total already reached at the end of the piece before it.

For a second piece beginning at $x = a$ that gives:

`\text{F} \left(x\right) = \text{F} \left(a\right) + \int_{a}^{x} \text{f} \left(t\right) \text{d} t`

Leaving out the `\text{F} \left(a\right)` is the usual error, and it shows up as a function that fails to reach 1 at the top of the range.


Spec links: `spcpt_QTHzFn6gZrVKcRdG`


## Card 8 — question_and_answer (`fl_Mg5BgfS553Bpqp4X`)

**FRONT**

Part of a cumulative distribution function is constant over an interval. What does that tell you about the variable there?


**BACK**

That $X$ never takes a value in that interval, because no probability at all is being accumulated across it.

The probability density is zero right through the interval, so the graph of `\text{f} \left(x\right)` has a gap exactly where the graph of `\text{F} \left(x\right)` is flat.

A flat stretch of $\text{F}$ is the c.d.f.'s way of showing a hole in the range of the variable.


Spec links: `spcpt_QTHzFn6gZrVKcRdG`


## Card 9 — question_and_answer (`fl_HKyKHfpCPfCjPb9C`)

**FRONT**

How do you find the median and the lower quartile of $X$ from its cumulative distribution function?


**BACK**

Solve `\text{F} \left(m\right) = 0 . 5` for the median and `\text{F} \left(Q_{1}\right) = 0 . 25` for the lower quartile, and `\text{F} \left(p\right) = \frac{n}{100}` for the $n$th percentile.

Because $\text{F}$ gives the probability below a value directly, these are ordinary equations to solve rather than integrals to evaluate.

For a piecewise $\text{F}$, work out its value at the end of each piece first, so that you know which piece the answer lies in before solving anything.


Spec links: `spcpt_QTHzFn6gZrVKcRdG`


## Card 10 — question_and_answer (`fl_cw6q3msG6qPhm3G5`)

**FRONT**

The continuous uniform distribution on $a \leq x \leq b$ has `\text{f} \left(x\right) = \frac{1}{b - a}`. Find its cumulative distribution function.


**BACK**

For $a \leq x \leq b$, `\text{F} \left(x\right)` is the area of the rectangle from $a$ up to $x$, which is `\left(x - a\right) \times \frac{1}{b - a}`:

`\text{F} \left(x\right) = \frac{x - a}{b - a}`

A full answer also states that `\text{F} \left(x\right) = 0` for $x < a$ and `\text{F} \left(x\right) = 1` for $x > b$.

A rectangular density therefore gives a c.d.f. that climbs in a straight line, which is the simplest cumulative distribution function there is.


Spec links: `spcpt_QTHzFn6gZrVKcRdG`

