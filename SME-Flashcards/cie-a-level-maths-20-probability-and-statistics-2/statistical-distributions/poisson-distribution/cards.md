# Poisson Distribution

Course: cie-a-level-maths-20-probability-and-statistics-2 · Section: Statistical Distributions

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/flashcards/statistical-distributions/poisson-distribution/


## Card 1 — keyword_definition (`fl_Krz7bcpTVPNFbThN`)

**FRONT**

Define **Poisson distribution**.


**BACK**

The **Poisson distribution** models a discrete random variable that counts the number of events occurring at random in a given interval of time or space.

It is written `X \sim \text{Po}(\lambda)`, where $λ$ is the mean number of occurrences in that interval.

Unlike a binomial there is no fixed number of trials, so $X$ can in principle be any non-negative whole number.


Spec links: `spcpt_CbcjyRyGd65mXstM`


## Card 2 — fill_in_the_blanks (`fl_gnRzW8vTXdP7Gqm7`)

**FRONT**

Fill in the three conditions a Poisson model requires:

events occur `\_\_\_\_\_\_` and at random in the interval

the mean number of occurrences, $λ$, is known and `\_\_\_\_\_\_`

each occurrence is `\_\_\_\_\_\_` of the others


**BACK**

The completed conditions are:

events occur **singly** and at random in the interval

the mean number of occurrences, $λ$, is known and **finite**

each occurrence is **independent** of the others

Singly means two events cannot happen at exactly the same instant, and $λ$ must be positive but need not be a whole number.


*Blanks: 0 — answers: []*

Spec links: `spcpt_CbcjyRyGd65mXstM`

Flags: fitb_no_blank_marker


## Card 3 — question_and_answer (`fl_z4F9zK92GRBbx8qc`)

**FRONT**

For `X \sim \text{Po}(\lambda)`, what are $\text{E} ( X )$ and $\text{Var} ( X )$?


**BACK**

They are both **exactly** $λ$.

The mean and the variance of a Poisson distribution are equal, which no other distribution on this course does.

The standard deviation is therefore $\sqrt{λ}$, and there is only ever one parameter to find.


Spec links: `spcpt_CbcjyRyGd65mXstM`


## Card 4 — question_and_answer (`fl_NM6XNvMbJTJfr7MN`)

**FRONT**

How does the shape of a Poisson distribution depend on $λ$?


**BACK**

A small $λ$ gives a strong **tail to the right**, with most of the probability piled up at 0 and 1.

As $λ$ grows the distribution becomes steadily more **symmetrical**, and by about $λ = 5$ it is already roughly so.

That drift towards symmetry is exactly why a large $λ$ can be approximated by a normal distribution.


Spec links: `spcpt_CbcjyRyGd65mXstM`


## Card 5 — fill_in_the_blanks (`fl_TZYxPvZStb8DdtW6`)

**FRONT**

Complete the formula for the probability of exactly $r$ occurrences:

`\text{P}(X = r) = e^{-\lambda} \times \frac{\lambda^{r}}{\_\_\_\_\_\_}`


**BACK**

The completed formula is:

$\text{P} ( X = r ) = e^{-λ} \times \frac{λ^{r}}{r!}$

It applies for $r = 0 , 1 , 2 , \dots$ with no upper limit, which is what distinguishes it from a binomial.

Any non-integer or negative value of $r$ has probability zero.


*Blanks: 0 — answers: []*

Spec links: `spcpt_F5rFq42MxcZZYVvp`

Flags: fitb_no_blank_marker


## Card 6 — question_and_answer (`fl_FCs9Dq7MC6zvZkcX`)

**FRONT**

Before choosing a Poisson model for some data, what quick check can you make?


**BACK**

Work out the **mean** and the **variance** of the data and see whether they come out **roughly equal**.

A Poisson distribution has them exactly equal, so data whose variance is far from its mean is telling you the model does not fit.

It is only a check, not a proof: the three conditions still have to be considered.


Spec links: `spcpt_w54vBS6Fm24wnJVB`


## Card 7 — question_and_answer (`fl_jRj65VRv2YV3rCjb`)

**FRONT**

What must you state before writing down a Poisson model?


**BACK**

What your **random variable** is, in words, for example "let $X$ be the number of typing errors per page".

The interval matters as much as the count, since $λ$ is a mean **per interval** and is meaningless without one.

Only then write `X \sim \text{Po}(\lambda)` with the value of $λ$ that belongs to that interval.


Spec links: `spcpt_w54vBS6Fm24wnJVB`


## Card 8 — question_and_answer (`fl_pBqzRHjTbcxdkcZ4`)

**FRONT**

A team scores a mean of 2 goals an hour. What distribution models the goals in a 90-minute game?


**BACK**

It is $\text{Po} ( 3 )$, because 90 minutes is $1 . 5$ hours and $λ$ scales with the interval.

So multiply the given mean by however many of the stated intervals the question asks about.

This is worth checking at every part of a question, because the interval often changes between parts.


Spec links: `spcpt_w54vBS6Fm24wnJVB`


## Card 9 — question_and_answer (`fl_sR9KBGNjB5FdYdpz`)

**FRONT**

How do you find $\text{P} ( X \leq 3 )$ for a Poisson distribution without typing four separate terms?


**BACK**

Every term contains $e^{-λ}$, so factorise it out:

`\text{P}(X \le 3) = e^{-\lambda}\left(1 + \lambda + \frac{\lambda^{2}}{2!} + \frac{\lambda^{3}}{3!}\right)`

The first two terms simplify because $λ^{0} = 1$ and $0 ! = 1 ! = 1$.

That single bracket is far quicker to type and much less prone to slips than four separate products.


Spec links: `spcpt_F5rFq42MxcZZYVvp`


## Card 10 — true_or_false (`fl_Q5FDW4P5HFftRczx`)

**FRONT**

**True or False?**

For a Poisson distribution, subtracting from 1 is merely a quicker way of finding $\text{P} ( X > k )$.


**BACK**

**False.**

It is the **only** way. A Poisson variable has no upper limit, so there are infinitely many values greater than $k$ and they cannot be added up directly.

So $\text{P} ( X > k ) = 1 - \text{P} ( X \leq k )$ is a necessity here, where for a binomial it would only have been a convenience.


Spec links: `spcpt_F5rFq42MxcZZYVvp`

