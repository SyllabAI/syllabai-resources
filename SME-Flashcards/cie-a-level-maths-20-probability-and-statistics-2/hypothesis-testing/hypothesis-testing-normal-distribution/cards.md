# Hypothesis Testing (Normal Distribution)

Course: cie-a-level-maths-20-probability-and-statistics-2 · Section: Hypothesis Testing

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/flashcards/hypothesis-testing/hypothesis-testing-normal-distribution/


## Card 1 — question_and_answer (`fl_9jNBXFpvhG7dMB2b`)

**FRONT**

In a test on a population mean, which distribution does the test actually work with?


**BACK**

The distribution of the **sample mean** $\overline{X}$, not the population distribution $X$ the question quotes.

Assuming $\text{H}_{0}$ is true, `\bar{X} \sim \text{N} \left(\mu, \frac{\sigma^{2}}{n}\right)`, and the observed sample mean is judged against that.

Using the population distribution instead treats a mean of $n$ readings as though it were a single reading.


Spec links: `spcpt_DBjZPz9tFvYW9SQs`


## Card 2 — fill_in_the_blanks (`fl_NH7SRqk2m9Sn8GMR`)

**FRONT**

Complete the test statistic for a hypothesis test on the mean of a normal distribution.

`z = \frac{\bar{x} - \mu}{\frac{\sigma}{\_\_\_\_\_\_}}`


**BACK**

The completed test statistic is:

$z = \frac{\overline{x}-μ}{\frac{σ}{\sqrt{n}}}$

The denominator is the standard deviation of $\overline{X}$, so it carries $\sqrt{n}$ rather than $n$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_DBjZPz9tFvYW9SQs`

Flags: fitb_no_blank_marker


## Card 3 — question_and_answer (`fl_bWrJTwDRRSMW8T9Q`)

**FRONT**

For `X \sim \text{N} \left(204, 81\right)` and a sample of 12, what is the denominator of $z$?


**BACK**

It is $\frac{9}{\sqrt{12}} = 2 . 598$ to three decimal places.

The 81 is the **variance**, so the standard deviation is $\sqrt{81} = 9$, and it is the standard deviation that goes into the formula.

Putting 81 in the numerator of the fraction is the commonest slip here.


Spec links: `spcpt_DBjZPz9tFvYW9SQs`


## Card 4 — question_and_answer (`fl_swbm9QV7fDqd83gp`)

**FRONT**

How is the critical $z$ value found for a 5% one-tailed test?


**BACK**

Read it from the **table of critical values** for the standard normal distribution, which gives $z = 1 . 645$ at 5%.

Use $- 1 . 645$ when the test is for a decrease, since the critical region is then in the lower tail.


Spec links: `spcpt_DBjZPz9tFvYW9SQs`


## Card 5 — true_or_false (`fl_BrDQVjS45vFD7CPk`)

**FRONT**

**True or False?**

A test statistic of $z = - 1 . 15$ does not lie in the critical region of a 5% lower-tailed test.


**BACK**

**True.**

The critical value is $- 1 . 645$, and $- 1 . 15$ is **closer to zero** than that, so it sits outside the region.

Compare how far each value is from 0 rather than which is numerically larger, or the negative signs will reverse the decision.


Spec links: `spcpt_DBjZPz9tFvYW9SQs`


## Card 6 — question_and_answer (`fl_bTcCn3fyDvV3XW6r`)

**FRONT**

How is the critical value found as a value of $\overline{x}$?


**BACK**

Set the test statistic equal to the critical $z$ from the table, then solve for $\overline{x}$.

For `\text{N} \left(204, 81\right)` with $n = 12$ at 5% for a decrease, $- 1 . 645 = \frac{\overline{x}-204}{2.598}$ gives $\overline{x} = 199 . 7$.

The observed sample mean can then be compared directly, in the units of the question.


Spec links: `spcpt_DBjZPz9tFvYW9SQs`


## Card 7 — question_and_answer (`fl_4BsbPTDSdq9qMWRc`)

**FRONT**

What are the two critical values in a two-tailed test on a normal mean?


**BACK**

The positive and negative $z$ for **half** the significance level, which have the same size because the normal distribution is symmetrical.

Solving with each in turn gives two values of $\overline{x}$, and they should come out the same distance either side of the mean.

That symmetry is a useful check on the arithmetic.


Spec links: `spcpt_DBjZPz9tFvYW9SQs`

