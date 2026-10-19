# Hypothesis Testing (Binomial & Poisson Distributions)

Course: ial-maths-20-statistics-2 · Section: Hypothesis Testing

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/flashcards/hypothesis-testing/hypothesis-testing-binomial-and-poisson-distributions/


## Card 1 — question_and_answer (`fl_9FnQfvCFgRK3pffn`)

**FRONT**

In a binomial hypothesis test, what is the population parameter being tested and what is the test statistic?


**BACK**

The parameter is $p$, the probability of success, and the test statistic is the **number of successes** in a fixed number of trials $n$.

So the hypotheses are written in terms of $p$, as $\text{H}_{0} : p = \dots$, and under $\text{H}_{0}$ the test statistic follows `X \sim \text{B} \left(n , p\right)` with the assumed value of $p$ substituted in.

Say in words what $p$ is the probability **of** before writing anything down, since the hypotheses mean nothing without it.


Spec links: `spcpt_FgTdMGnP4jYnHk7C`


## Card 2 — fill_in_the_blanks (`fl_z2VS9s37nwwBZVXH`)

**FRONT**

Complete the two conditions that make $c$ the critical value in a one-tailed binomial test at the `\alpha \%` level.

Testing for a decrease:

`\text{P} \left(X \le c\right) \le \alpha \% \text{, and } \text{P} \left(X \le \_\_\_\_\_\_\right) > \alpha \%`

Testing for an increase:

`\text{P} \left(X \ge c\right) \le \alpha \% \text{, and } \text{P} \left(X \ge \_\_\_\_\_\_\right) > \alpha \%`


**BACK**

The completed conditions are:

`\text{P} \left(X \le c\right) \le \alpha \% \text{, and } \text{P} \left(X \le c + 1\right) > \alpha \%`

`\text{P} \left(X \ge c\right) \le \alpha \% \text{, and } \text{P} \left(X \ge c - 1\right) > \alpha \%`

The second condition in each pair is the check that you have not gone one value too far into the tail.

The offsets run opposite ways because the next value the region would swallow is $c + 1$ in a lower tail and $c - 1$ in an upper one.


*Blanks: 0 — answers: []*

Spec links: `spcpt_FgTdMGnP4jYnHk7C`


## Card 3 — question_and_answer (`fl_P3QGcwQgHmX4SRcN`)

**FRONT**

When finding a binomial critical value, why is it not enough to find some value $c$ with `\text{P} \left(X \le c\right) \le \alpha \%`?


**BACK**

Because plenty of values satisfy that on their own, and what you need is the **largest** of them.

The critical value is the least extreme value that still rejects $\text{H}_{0}$, so the region has to be as big as the significance level allows and no bigger, which is exactly what the second condition confirms.

Stopping at the first value that happens to work gives a critical region that is too small, and an actual significance level well below the one the question asked for.


Spec links: `spcpt_FgTdMGnP4jYnHk7C`


## Card 4 — question_and_answer (`fl_ymMZDFK742FbKc93`)

**FRONT**

How do you find the critical regions for a **two-tailed** binomial test?


**BACK**

Halve the significance level and search each tail separately, using `\frac{\alpha}{2} \%` as the ceiling in the lower tail and again in the upper one.

That gives two critical values, one at each end, and $\text{H}_{0}$ is rejected if the observed value falls in either region.

The two regions usually come out **different sizes**, because a binomial distribution is only symmetrical when $p = 0 . 5$.


Spec links: `spcpt_FgTdMGnP4jYnHk7C`


## Card 5 — true_or_false (`fl_4WVdsRmT2GW5Bh2v`)

**FRONT**

**True or False?**

In a two-tailed binomial test at the 5% level, each critical region carries a probability of exactly 2.5%.


**BACK**

**False.**

2.5% is the **ceiling** for each tail rather than the probability achieved: the distribution is discrete, so each region ends up at or below 2.5%.

The two are usually different from one another as well, and adding them gives the **actual significance level**, which comes out below 5%.


Spec links: `spcpt_FgTdMGnP4jYnHk7C`


## Card 6 — question_and_answer (`fl_Bw7pwSD7Ggrtvh3G`)

**FRONT**

Your values of $n$ and $p$ are not in the cumulative binomial table. How can the test still be carried out?


**BACK**

Work the probabilities out from the binomial formula instead, or use a **normal approximation** where $n$ is large and $p$ is close to 0.5.

The approximation route needs a continuity correction, since it puts a continuous distribution in place of a discrete one.

Which route is open to you is decided by the values of $n$ and $p$ rather than by preference.


Spec links: `spcpt_FgTdMGnP4jYnHk7C`


## Card 7 — question_and_answer (`fl_4hTTg2YGyJ58jzJ8`)

**FRONT**

Jacques claims fewer than 40% of shoppers buy his bread. Of a random sample of 12, two do. Test his claim at the 10% level.


**BACK**

With $p$ the proportion of shoppers who buy his bread, $\text{H}_{0} : p = 0 . 4$ and $\text{H}_{1} : p < 0 . 4$, and under $\text{H}_{0}$ the count follows `X \sim \text{B} \left(12 , 0 . 4\right)`.

The cumulative table gives `\text{P} \left(X \le 2\right) = 0 . 0834`, which is less than 0.10.

So $\text{H}_{0}$ is rejected: there is sufficient evidence at the 10% level to support Jacques' claim that fewer than 40% of shoppers buy his bread.


Spec links: `spcpt_FgTdMGnP4jYnHk7C`


## Card 8 — question_and_answer (`fl_p3ZMcSNjS4XYtns9`)

**FRONT**

In a Poisson hypothesis test, what is the population parameter being tested and what is the random variable?


**BACK**

The parameter is $λ$, the mean number of occurrences in the stated interval, sometimes written $μ$ because it is a population mean.

The random variable counts the occurrences in that interval, so under $\text{H}_{0}$ it follows `X \sim \text{Po} \left(\lambda\right)` with the assumed value of $λ$ put in.

Define $λ$ in words, naming the interval it refers to, before writing $\text{H}_{0} : λ = \dots$.


Spec links: `spcpt_2cYxMfGpbS5NYNxv`


## Card 9 — question_and_answer (`fl_MDjh5HqhbQggs5Vt`)

**FRONT**

A blog averages 8 likes per 24 hours, and the test uses a randomly chosen 12-hour period. What value of $λ$ do you test with?


**BACK**

$λ = 4$, because $λ$ has to match the interval the observation actually covers and 12 hours is half of 24.

The claimed rate of 8 belongs to a 24-hour interval, so it must be rescaled before a single probability is worked out.

Getting this wrong changes every probability in the test, and it is the step most easily missed because the rate and the interval are usually stated in different sentences.


Spec links: `spcpt_2cYxMfGpbS5NYNxv`


## Card 10 — question_and_answer (`fl_n4bCJy5KfztPPWNv`)

**FRONT**

Why is searching the **upper** tail for a Poisson critical value different from searching the lower tail?


**BACK**

Because a Poisson variable has no largest value, so the upper region can never be listed out and totalled directly.

You work with `\text{P} \left(X \ge c\right) = 1 - \text{P} \left(X \le c - 1\right)` instead, taking a cumulative entry from the table and subtracting it from 1.

The lower tail needs none of that, since `\text{P} \left(X \le c\right)` is read straight off the table.


Spec links: `spcpt_2cYxMfGpbS5NYNxv`


## Card 11 — question_and_answer (`fl_ZkxDMrd9mGDQXxJw`)

**FRONT**

What is a **Type I error**, and which quantity measures its probability?


**BACK**

A **Type I error** is rejecting the null hypothesis when it was in fact true.

Its probability is the **actual significance level** of the test, which for a discrete distribution such as the Poisson comes out at or below the level the question stated.

It is the unavoidable price of the method: a result inside the critical region is unlikely when $\text{H}_{0}$ holds, but unlikely is not impossible.


Spec links: `spcpt_2cYxMfGpbS5NYNxv`


## Card 12 — question_and_answer (`fl_DBPx3KkqPHVR96wg`)

**FRONT**

`X \sim \text{Po} \left(4\right)` and a two-tailed test is run at the 5% level. Find the critical regions.


**BACK**

Each tail takes 2.5%, so in the lower tail `\text{P} \left(X \le 0\right) = 0 . 0183` is under it while `\text{P} \left(X \le 1\right) = 0 . 0916` is over, giving the region $X \leq 0$.

In the upper tail `\text{P} \left(X \ge 9\right) = 1 - 0 . 9786 = 0 . 0214` is under 0.025 while `\text{P} \left(X \ge 8\right) = 1 - 0 . 9489 = 0 . 0511` is over, giving the region $X \geq 9$.

The two regions come out very different in size, which is what a small value of $λ$ does to a Poisson distribution.


Spec links: `spcpt_2cYxMfGpbS5NYNxv`


## Card 13 — question_and_answer (`fl_HWzrrPTwb2PSfPYV`)

**FRONT**

A two-tailed Poisson test has critical regions $X \leq 0$ and $X \geq 9$, with tail probabilities $0 . 0183$ and $0 . 0214$. Find the actual significance level.


**BACK**

Add the two tail probabilities: $0 . 0183 + 0 . 0214 = 0 . 0397$, so the actual significance level is `3 . 97 \%`.

It falls short of the 5% asked for because a discrete distribution cannot place its critical values so as to use the whole allowance.

An observed value of 7 lies in neither region, so $\text{H}_{0}$ would not be rejected and there is insufficient evidence of a change.


Spec links: `spcpt_2cYxMfGpbS5NYNxv`


## Card 14 — true_or_false (`fl_vqjfvFCNp9r2c3m3`)

**FRONT**

**True or False?**

A two-tailed Poisson test can have no lower critical region at all.


**BACK**

**True.**

If $λ$ is small enough that even `\text{P} \left(X = 0\right)` exceeds half the significance level, then no value is extreme enough to reject $\text{H}_{0}$ in the lower tail.

For `\text{Po} \left(1\right)` at the 5% level `\text{P} \left(X = 0\right) = 0 . 368` against a ceiling of 0.025, so the lower tail is empty and only large values can produce a rejection.


Spec links: `spcpt_2cYxMfGpbS5NYNxv`

