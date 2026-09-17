# Integration

Course: ial-maths-20-pure-2 · Section: Integration

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-2/flashcards/integration/integration/


## Card 1 — keyword_definition (`fl_QQVWFHZzjWJDKwWs`)

**FRONT**

Define the **limits** of a definite integral.


**BACK**

The **limits** are the two values written on the integral sign: the one at the bottom is the **lower** limit and the one at the top is the **upper** limit.

They are the values of $x$ between which the integration is carried out.


Spec links: `spcpt_9Cpr29P5QKVBBZY6`


## Card 2 — fill_in_the_blanks (`fl_vMjnHBYKtWCdcbtg`)

**FRONT**

Complete the result that evaluates a definite integral:

`\int_{a}^{b} \text{f} ' \left(x\right) \text{d} x = \_\_\_\_\_\_ - \_\_\_\_\_\_`


**BACK**

The completed result is:

`\int_{a}^{b} \text{f} ' \left(x\right) \text{d} x = \text{f} \left(b\right) - \text{f} \left(a\right)`

Getting the subtraction the wrong way round flips the sign of the answer.


*Blanks: 0 — answers: []*

Spec links: `spcpt_9Cpr29P5QKVBBZY6`


## Card 3 — question_and_answer (`fl_fkPHnhrVdHr9cXrH`)

**FRONT**

Why is there no constant of integration in a definite integral?


**BACK**

Because it **cancels**: a $+ c$ appears in the value at each limit, and one is then subtracted from the other.

Writing the subtraction as `\left(\ldots + c\right) - \left(\ldots + c\right)` shows that the two constants destroy each other whatever $c$ happens to be.


Spec links: `spcpt_9Cpr29P5QKVBBZY6`


## Card 4 — true_or_false (`fl_jgv7Wfbp4dGXMZBj`)

**FRONT**

**True or False?**

The value of a definite integral is a number, not an expression in $x$.


**BACK**

**True.**

Once both limits have been substituted, every $x$ has been replaced by a number.

That is what separates it from an indefinite integral, which returns a function.


Spec links: `spcpt_9Cpr29P5QKVBBZY6`


## Card 5 — question_and_answer (`fl_t5h72qKYTGWh4Kyb`)

**FRONT**

How is a definite integral written down before the limits are substituted?


**BACK**

With the integrated function inside **square brackets**, and the limits placed just after the closing bracket.

For example `\left[\frac{3}{4} x^{4} - 3 x^{2}\right]_{2}^{4}`, with the lower limit below and the upper limit above.


Spec links: `spcpt_9Cpr29P5QKVBBZY6`


## Card 6 — question_and_answer (`fl_9FjtdMxH3QN33SBJ`)

**FRONT**

You are asked for `\int_{2}^{4} 3 x \left(x^{2} - 2\right) \text{d} x`. What has to happen before this can be integrated?


**BACK**

The brackets have to be **expanded**, giving `\int_{2}^{4} \left(3 x^{3} - 6 x\right) \text{d} x`.

A product like that cannot be integrated term by term as it stands, so it must first be written as a sum of powers of $x$.


Spec links: `spcpt_9Cpr29P5QKVBBZY6`


## Card 7 — question_and_answer (`fl_kKSZfNVMSWKzxRpP`)

**FRONT**

Why work out a definite integral by hand when a calculator can do it?


**BACK**

Because a calculator returns a **decimal**, not the exact value.

An integral worth $\frac{1256}{3}$ comes back as $418 . 666 \dots$, which is no use when an exact answer is asked for.


Spec links: `spcpt_9Cpr29P5QKVBBZY6`


## Card 8 — keyword_definition (`fl_3qynTcbGCZbDCMwK`)

**FRONT**

Define the **area under a curve** $y = \text{f} ( x )$ between $x = a$ and $x = b$.


**BACK**

The area of the region bounded by four things:

- the curve $y = \text{f} ( x )$
- the $x$-axis
- the vertical line $x = a$
- the vertical line $x = b$

The $x$-axis is the boundary that is easiest to forget: "under the curve" means between the curve and the $x$-axis, not simply below the curve.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 9 — question_and_answer (`fl_Mmd4BQgmrmzmkjy2`)

**FRONT**

What has to be true about a curve between $x = a$ and $x = b$ for the area under it to be given by `\int_{a}^{b} \text{f} \left(x\right) \text{d} x`?


**BACK**

The curve must lie on or above the $x$-axis across the whole of that interval.

Where it dips below, the integral counts that part as **negative**, so the value it returns is no longer the area.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 10 — question_and_answer (`fl_DQq4WGyFyGhvqJZG`)

**FRONT**

A question asks for the area between a curve and the $x$-axis but gives no limits. Where do the limits come from?


**BACK**

From the curve's $x$-axis intercepts, which are the natural edges of the region.

Set $y = 0$ and solve. For example, `y = x\left(5 - x\right)` gives $x = 0$ and $x = 5$, so the area is `\int_{0}^{5} \left(5x - x^{2}\right)\text{d}x`.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 11 — true_or_false (`fl_dp5dCyDrnwtXykN5`)

**FRONT**

**True or False?**

If a definite integral gives a negative value, you have made a mistake.


**BACK**

**False.**

A region lying below the $x$-axis gives a negative integral. That is the integral behaving correctly, not an error.

An area cannot be negative, so take the **modulus**: an integral of $- \frac{22}{3}$, for example, means an area of $\frac{22}{3}$ square units.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 12 — question_and_answer (`fl_Gb4JKWkT94HtVBvN`)

**FRONT**

Before integrating to find the total area between a curve and the $x$-axis, what must you check?


**BACK**

Whether the curve crosses the $x$-axis anywhere inside the interval.

Solve `\text{f} \left(x\right) = 0` to find out; each crossing splits the region into a separate piece, and each piece needs its own integral.

For example, $y = x^{3} - 12 x^{2} + 35 x$ crosses at $x = 0$, $x = 5$ and $x = 7$.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 13 — question_and_answer (`fl_jYD7Zv5Z3nXMz3xD`)

**FRONT**

A region between a curve and the $x$-axis lies partly above and partly below the axis. Why does a single definite integral across the whole interval not give its total area?


**BACK**

The part below the axis contributes a **negative** value, so it cancels part of the positive contribution from the part above. The result is smaller than the true area, and can even be zero.

Integrate each piece separately, take the **modulus** of each, then add; for example, two pieces giving $\frac{375}{4}$ and $- 8$ have a total area of $\frac{375}{4} + 8 = \frac{407}{4}$ square units.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 14 — question_and_answer (`fl_ZhTnKxzFjM5Z6cR9`)

**FRONT**

Why do you need to solve the equations of a curve and a line simultaneously before finding the area enclosed between them?


**BACK**

Their points of intersection are the **limits of integration**: the enclosed region only exists between them.

Set the two expressions for $y$ equal and solve. For example, for $y = 5 + 4 x - x^{2}$ and $y = 10 - 2 x$:

$10 - 2 x = 5 + 4 x - x^{2} \Rightarrow x^{2} - 6 x + 5 = 0$

so the limits are $x = 1$ and $x = 5$.


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 15 — question_and_answer (`fl_gxWX4BRnb6fHjWBn`)

**FRONT**

The region enclosed between a curve and a line runs from $x = a$ to $x = b$, with the curve above the line. How do you find its area by working out two separate areas?


**BACK**

Find the area under the curve and the area under the line over the same interval, then **subtract** the smaller from the larger:

`R = \int_{a}^{b}\text{f}(x)\,\text{d}x - \int_{a}^{b}\text{g}(x)\,\text{d}x`

Whichever graph is on top has the larger area underneath it, so with the curve on top it is the area under the line that is subtracted.


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 16 — true_or_false (`fl_Wzm7PRgMMDySXs3J`)

**FRONT**

**True or False?**

To find the area under a straight line between two $x$-values, you have to use definite integration.


**BACK**

**False.**

The region under a straight line is a **rectangle, triangle or trapezium**, so a basic area formula is usually quicker and less error-prone.

For example, the area under $y = 10 - 2 x$ from $x = 1$ to $x = 5$ is a triangle of base 4 and height 8, giving $\frac{1}{2} \times 4 \times 8 = 16$.


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 17 — question_and_answer (`fl_6hCS6ywKnbZSnFKp`)

**FRONT**

How can you find the area enclosed between a curve and a line using only one integral?


**BACK**

Subtract the two functions **before** integrating, taking the lower graph away from the upper one, then integrate the result between the intersections.

For example, with the curve $y = 5 + 4 x - x^{2}$ above the line $y = 10 - 2 x$ between $x = 1$ and $x = 5$:

`R = \int_{1}^{5}\left[\left(5 + 4x - x^{2}\right) - \left(10 - 2x\right)\right]\text{d}x = \int_{1}^{5}\left(-x^{2} + 6x - 5\right)\text{d}x`


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 18 — true_or_false (`fl_mBRR3n4JdXrg6qTW`)

**FRONT**

**True or False?**

When you subtract one function from the other to find the area enclosed between a curve and a line, it does not matter which way round you subtract, because an area cannot be negative.


**BACK**

**False.**

Subtracting the wrong way round gives the **negative** of the area, and it will not be corrected for you.

Always take the **lower** graph away from the **upper** one over the interval concerned, which means deciding from a sketch which of the two is on top.


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 19 — question_and_answer (`fl_YNBHmJt9GSHVhD7G`)

**FRONT**

Why must the whole of a line's equation be put in brackets when it is subtracted from a curve's equation?


**BACK**

Because **every** term of the line is being subtracted, not just the first one. For example:

`\left(5 + 4x - x^{2}\right) - \left(10 - 2x\right) = -x^{2} + 6x - 5`

Without the brackets the $- 2 x$ would keep its own sign, giving $- x^{2} + 2 x - 5$ and an answer that is wrong from that line onwards.


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 20 — question_and_answer (`fl_q2MvK4wrnBcVftmY`)

**FRONT**

What changes when both boundaries of a region are curves?


**BACK**

Nothing about the method: it is still the integral of **upper minus lower**, taken between the intersections.

What is lost is the shortcut of using a triangle or trapezium formula for one boundary, since neither of them is a straight line any more.


Spec links: `spcpt_FfdPp8vTNhhpwWJ7`


## Card 21 — question_and_answer (`fl_7GvFnZWR7Zc48vDr`)

**FRONT**

Two curves meet at three points. How many integrals does the enclosed area need?


**BACK**

**Two**, one for each enclosed region: from the first intersection to the second, and from the second to the third.

Each region is bounded separately, so each needs its own integral with its own pair of limits.


Spec links: `spcpt_FfdPp8vTNhhpwWJ7`


## Card 22 — question_and_answer (`fl_fQF7dHGwBPXBBCxh`)

**FRONT**

Why must you check which curve is on top for **each** region separately?


**BACK**

Because the two curves swap over at every point where they cross.

A curve that was above before an intersection is below after it, so "upper minus lower" means a different subtraction in each region.


Spec links: `spcpt_FfdPp8vTNhhpwWJ7`


## Card 23 — question_and_answer (`fl_sVFrWkthTfyqcykB`)

**FRONT**

Why is a sketch essential here?


**BACK**

Because it is the only reliable way to see how many separate regions there are, and which curve is on top in each of them.

The algebra gives you the intersections; only the picture tells you what to do with them.


Spec links: `spcpt_FfdPp8vTNhhpwWJ7`


## Card 24 — true_or_false (`fl_w9fwYjcKsZKPGB6s`)

**FRONT**

**True or False?**

The total area between two curves is the integral of their difference across the whole interval.


**BACK**

**False.**

Wherever the curves swap over, the difference changes sign, so one region subtracts from another and the total comes out too small.

Integrate each region separately, take each as a positive area, and then add them.


Spec links: `spcpt_FfdPp8vTNhhpwWJ7`


## Card 25 — keyword_definition (`fl_Bqc2yTHNQPptFPGM`)

**FRONT**

Define the **trapezium rule**.


**BACK**

The **trapezium rule** is a numerical method that **approximates** a definite integral by adding up the areas of trapezium-shaped strips beneath the curve.

It is used where the function cannot be integrated by algebraic methods at all.


Spec links: `spcpt_RVNjC2y684mYfGyD`


## Card 26 — fill_in_the_blanks (`fl_cVm5863vWDsnczkp`)

**FRONT**

Complete the strip width used by the trapezium rule with $n$ strips between $x = a$ and $x = b$:

`h = \frac{\_\_\_\_\_\_}{n}`


**BACK**

The completed formula is:

$h = \frac{b-a}{n}$

The width of the whole interval is simply shared equally between the strips.


*Blanks: 0 — answers: []*

Spec links: `spcpt_RVNjC2y684mYfGyD`


## Card 27 — question_and_answer (`fl_TY3JfJgMJhcyfQtn`)

**FRONT**

How many $y$-values do you need for a trapezium rule with $n$ strips?


**BACK**

$n + 1$ of them, running from $y_{0}$ to $y_{n}$.

Each strip needs a height at both of its edges, and neighbouring strips share an edge, so there is always one more value than there are strips.


Spec links: `spcpt_RVNjC2y684mYfGyD`


## Card 28 — true_or_false (`fl_nKxdDHK8FvYPNprg`)

**FRONT**

**True or False?**

The trapezium rule always gives an underestimate of the true area.


**BACK**

**False.**

It depends on which way the curve bends: a curve bending **downwards** leaves the trapezia below it, giving an underestimate.

A curve bending **upwards** has the trapezia sitting above it instead, giving an overestimate.


Spec links: `spcpt_RVNjC2y684mYfGyD`


## Card 29 — question_and_answer (`fl_G4HRjYT4ghCKSwzk`)

**FRONT**

In the trapezium rule formula, which $y$-values are doubled?


**BACK**

All the **inner** ones, $y_{1}$ through to $y_{n-1}$.

The two **outer** values $y_{0}$ and $y_{n}$ are counted once each, because each of them is an edge of only one strip.


Spec links: `spcpt_RVNjC2y684mYfGyD`


## Card 30 — question_and_answer (`fl_txdxJSZ58MKhNdVM`)

**FRONT**

How do you make a trapezium rule estimate more accurate?


**BACK**

Use **more strips**.

Narrower strips have tops that hug the curve more closely, so less area is missed or double-counted at each one.


Spec links: `spcpt_RVNjC2y684mYfGyD`


## Card 31 — question_and_answer (`fl_dfcKrNNfhqC5nJw3`)

**FRONT**

How can you measure how accurate a trapezium rule estimate was?


**BACK**

By working out the **percentage error** against the true value.

That is only possible where the exact value can be found some other way.


Spec links: `spcpt_RVNjC2y684mYfGyD`

