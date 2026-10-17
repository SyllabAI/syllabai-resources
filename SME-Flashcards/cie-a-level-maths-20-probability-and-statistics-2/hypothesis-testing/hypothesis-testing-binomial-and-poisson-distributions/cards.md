# Hypothesis Testing (Binomial & Poisson Distributions)

Course: cie-a-level-maths-20-probability-and-statistics-2 · Section: Hypothesis Testing

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/flashcards/hypothesis-testing/hypothesis-testing-binomial-and-poisson-distributions/


## Card 1 — question_and_answer (`fl_G2ySzcyPBFV5fgKK`)

**FRONT**

In a binomial hypothesis test, what is the population parameter and what does the random variable count?


**BACK**

The parameter is the **probability of success**, $p$, in a binomial distribution $\text{B} ( n , p )$.

The random variable counts the number of **successes** in a fixed number of trials $n$, and its value for the sample is the observed value.


Spec links: `spcpt_mWctnbvnpcSVbDh5`


## Card 2 — question_and_answer (`fl_vKj4CNrCkfw2z7Gh`)

**FRONT**

Why is the distribution written as `X \sim \text{B}(12, p)` rather than `X \sim \text{B}(12, 0.6)`?


**BACK**

Because $p$ is the quantity being **tested**, so it must stay as a letter when the distribution is first defined.

The assumed value 0.6 enters only through the null hypothesis, and is used from that point on to calculate probabilities assuming $\text{H}_{0}$ is true.


Spec links: `spcpt_mWctnbvnpcSVbDh5`


## Card 3 — fill_in_the_blanks (`fl_dpHNRnQcM7tXhy34`)

**FRONT**

Complete the conditions that make $c$ the critical value of an **upper-tailed** binomial test at the `\alpha \%` level.

`\text{P}(X \geq c) \_\_\_\_\_\_ \alpha \%`

`\text{P}(X \geq c - 1) \_\_\_\_\_\_ \alpha \%`


**BACK**

The completed conditions are:

`\text{P}(X \geq c) \leq \alpha \%`

`\text{P}(X \geq c - 1) > \alpha \%`

The critical value is the **first** value inside the region, so the value one step nearer the middle has to fall outside it.


*Blanks: 0 — answers: []*

Spec links: `spcpt_mWctnbvnpcSVbDh5`

Flags: fitb_no_blank_marker


## Card 4 — question_and_answer (`fl_tzDGMt3SY9HFnzpF`)

**FRONT**

How do the critical value conditions change for a lower-tailed test?


**BACK**

The tail is reversed, so the conditions become `\text{P}(X \leq c) \leq \alpha \%` and `\text{P}(X \leq c + 1) > \alpha \%`.

The second condition still steps **towards** the middle of the distribution, which for a lower tail means going up rather than down.


Spec links: `spcpt_mWctnbvnpcSVbDh5`


## Card 5 — true_or_false (`fl_h6b36VPrWVzgkhbC`)

**FRONT**

**True or False?**

In a two-tailed binomial test the two critical regions are the same size.


**BACK**

**False.**

The binomial distribution is only symmetrical when $p = 0 . 5$, so in general one tail reaches its half of the significance level sooner than the other.

Often one of the two regions is much larger than the other.


Spec links: `spcpt_mWctnbvnpcSVbDh5`


## Card 6 — question_and_answer (`fl_CqMhCKvpDbW8jg6Y`)

**FRONT**

How is $\text{P} ( X \geq 10 )$ found for `X \sim \text{B}(12, 0.6)`?


**BACK**

Either add the three individual probabilities for $X = 10$, $X = 11$ and $X = 12$, or subtract the cumulative probability from one as $1 - \text{P} ( X \leq 9 )$.

Both give $0 . 0834$ to three significant figures.


Spec links: `spcpt_mWctnbvnpcSVbDh5`


## Card 7 — question_and_answer (`fl_RgBdJccjkkWtD9DK`)

**FRONT**

Which route through a binomial test usually needs fewer calculations?


**BACK**

Finding the **probability** of a value at least as extreme as the observed one, which takes a single cumulative calculation.

Finding the **critical region** means testing candidate values one at a time until the boundary is located, so it costs more unless the question asks for the region.


Spec links: `spcpt_mWctnbvnpcSVbDh5`


## Card 8 — question_and_answer (`fl_pD9WDSPv5S8PR4Wq`)

**FRONT**

What must be done when the observed value covers a different time interval from the stated mean?


**BACK**

Scale the mean in proportion so that it applies to the **same interval** as the observation.

A mean of 8 per 24 hours becomes a mean of 2 per 6 hours, and the calculation then uses `X \sim \text{Po}(2)`.

The random variable counts occurrences in that interval, so the two have to match before any probability is worked out.


Spec links: `spcpt_QmfvPPDFyty4DBtv`


## Card 9 — question_and_answer (`fl_7VJfszsd8FsRTR2y`)

**FRONT**

When the mean has been rescaled, which value of $λ$ do the hypotheses use?


**BACK**

The value for the interval $λ$ was **defined** in, so a mean defined as likes per day keeps $\text{H}_{0} : λ = 8$.

The rescaled mean of 2 belongs to the distribution used for the calculation, not to the hypotheses.

Defining $λ$ with its interval in words is what keeps the two apart.


Spec links: `spcpt_QmfvPPDFyty4DBtv`


## Card 10 — question_and_answer (`fl_3ZpjPfhpghqpvyHR`)

**FRONT**

Why is an upper-tail Poisson probability found by subtracting from one?


**BACK**

A Poisson variable has no upper limit, so $\text{P} ( X \geq c )$ cannot be reached by adding terms.

Use $\text{P} ( X \geq c ) = 1 - \text{P} ( X \leq c - 1 )$, which turns it into a finite cumulative sum.

The upper tail is where mistakes are most often made, usually by dropping or adding one to the limit.


Spec links: `spcpt_QmfvPPDFyty4DBtv`


## Card 11 — question_and_answer (`fl_y9jgKZN83jHGyshc`)

**FRONT**

How is the rejection region found for an upper-tailed Poisson test at the 5% level?


**BACK**

Work out $\text{P} ( X \geq c )$ for candidate values of $c$ until it first drops below 0.05.

Check the value one step lower is still above 0.05, which confirms $c$ is the boundary.

With $λ = 2$ this gives $\text{P} ( X \geq 5 ) = 0 . 0527$ and $\text{P} ( X \geq 6 ) = 0 . 0166$, so the region is $X \geq 6$.


Spec links: `spcpt_QmfvPPDFyty4DBtv`


## Card 12 — true_or_false (`fl_3Y3jRN5ZT7sD2j8Q`)

**FRONT**

**True or False?**

For `X \sim \text{Po}(2)` tested at the 5% level for an increase, an observed value of 5 is not enough to reject $\text{H}_{0}$.


**BACK**

**True.**

The rejection region is $X \geq 6$, and 5 falls outside it.

A Poisson distribution has a long right tail, so a value two and a half times the mean can still be unremarkable.


Spec links: `spcpt_QmfvPPDFyty4DBtv`


## Card 13 — question_and_answer (`fl_6nZYPv7bs3qGhXpc`)

**FRONT**

What is different about finding the critical region for a two-tailed Poisson test?


**BACK**

Two critical values are needed, one in each tail, each found against **half** the significance level.

The lower tail is a direct cumulative probability, while the upper tail still has to be reached by subtracting from one.


Spec links: `spcpt_QmfvPPDFyty4DBtv`


## Card 14 — question_and_answer (`fl_K5JDCsGDT3Hm2q7p`)

**FRONT**

A test on `X \sim \text{Po}(2)` has rejection region $X \geq 6$. What is the probability of a Type I error?


**BACK**

It is $\text{P} ( X \geq 6 )$ worked out with $λ = 2$, since a Type I error means landing in the rejection region while $\text{H}_{0}$ is true.

That gives $1 - \text{P} ( X \leq 5 ) = 1 - 0 . 9834 = 0 . 0166$ to three significant figures.


Spec links: `spcpt_QmfvPPDFyty4DBtv`

