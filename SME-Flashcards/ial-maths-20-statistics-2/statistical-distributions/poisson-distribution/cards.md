# Poisson Distribution

Course: ial-maths-20-statistics-2 · Section: Statistical Distributions

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/flashcards/statistical-distributions/poisson-distribution/


## Card 1 — keyword_definition (`fl_gng3MRhHWtyH87vC`)

**FRONT**

Define a **Poisson distribution**.


**BACK**

A **Poisson distribution** is the discrete probability distribution of a random variable that **counts the number of events occurring at random in a given interval** of time or space.

It is written `X \sim \text{Po} \left(\lambda\right)`, where $λ$ is the mean number of occurrences in that interval.

The interval may be a length of time, such as a day, or a region of space, such as a square metre of grass.


Spec links: `spcpt_gQsJPB7Szy6ZvMBZ`


## Card 2 — fill_in_the_blanks (`fl_6FfXVKvMBnJzZRVr`)

**FRONT**

A Poisson model needs three conditions to hold. Fill in the two that are missing:

events occur `\_\_\_\_\_\_` and at random in a given interval of time or space

the mean number of occurrences in that interval, $λ$, is known and finite

the occurrences are `\_\_\_\_\_\_` of one another


**BACK**

The completed conditions are:

events occur **singly** and at random in a given interval

the occurrences are **independent** of one another

None of the three conditions is in the formula booklet, so all three have to be remembered.

Occurrences that arrive in clusters, such as customers entering a shop as a family, break both of these at once.


*Blanks: 0 — answers: ['singly', 'independent']*

Spec links: `spcpt_gQsJPB7Szy6ZvMBZ`

Flags: blank_answer_mismatch


## Card 3 — true_or_false (`fl_24hQdGKqRVMNfPD7`)

**FRONT**

**True or False?**

In `X \sim \text{Po} \left(\lambda\right)`, the value of $λ$ must be a whole number.


**BACK**

**False.**

$λ$ is a **mean** number of occurrences rather than a count, so a rate such as 2.4 faults per metre is perfectly sensible.

All that is required of $λ$ is that it is **positive and finite**, and the variable $X$ itself still only ever takes whole-number values.


Spec links: `spcpt_gQsJPB7Szy6ZvMBZ`


## Card 4 — question_and_answer (`fl_5gP8qsf35gVwgKP3`)

**FRONT**

What is the relationship between the mean and the variance of a Poisson distribution?


**BACK**

They are **equal**: the formula booklet gives both the mean and the variance of `X \sim \text{Po} \left(\lambda\right)` as $λ$.

The standard deviation is therefore $\sqrt{λ}$.

Knowing the mean of a Poisson distribution is knowing everything about it, since the single parameter $λ$ fixes the whole distribution.


Spec links: `spcpt_gQsJPB7Szy6ZvMBZ`


## Card 5 — true_or_false (`fl_S4vtRvS673vysZPn`)

**FRONT**

**True or False?**

There is no upper limit to the number of occurrences that a Poisson distribution allows.


**BACK**

**True.**

$X$ can take any of the values $0 , 1 , 2 , 3 , \dots$ with no largest value, because there is no fixed number of trials to cap it.

The probabilities of very large values become vanishingly small but are never exactly zero, which is one clear difference from a binomial distribution, where $X$ can never exceed $n$.


Spec links: `spcpt_gQsJPB7Szy6ZvMBZ`


## Card 6 — question_and_answer (`fl_BJDwsqzwW6vsfYny`)

**FRONT**

How does the shape of a Poisson distribution depend on $λ$?


**BACK**

With $λ$ close to 0 the vertical line graph has a **tail to the right**, since almost all of the probability sits on the smallest values.

Once $λ$ reaches about 5 the graph is **roughly symmetrical**, and it becomes more symmetrical still as $λ$ grows.

That growing symmetry is what eventually makes a bell-shaped curve a good approximation to a Poisson distribution.


Spec links: `spcpt_gQsJPB7Szy6ZvMBZ`


## Card 7 — question_and_answer (`fl_qDbrb44NGFngJQWm`)

**FRONT**

For a Poisson distribution the mean and the variance are both $λ$. How does that help you judge whether a data set can be modelled by one?


**BACK**

Work out the mean and the variance of the data and see whether they come out **roughly equal**.

If they are far apart then no value of $λ$ can fit both at once, and a Poisson model should be rejected straight away.

Roughly equal is only a first test, though, and the three conditions still have to be checked before the model is accepted.


Spec links: `spcpt_GPmq8k46YXs6B3kX`


## Card 8 — question_and_answer (`fl_yFJWRyWPXqbqhxnj`)

**FRONT**

Why must a Poisson model always state the interval of time or space that it refers to?


**BACK**

Because $λ$ is the mean number of occurrences **in a stated interval**, so on its own a bare number such as 2 is not yet a distribution at all.

Faults at a mean rate of 2 per metre and calls at a mean rate of 2 per hour are both `\text{Po} \left(2\right)` only because the interval has been fixed in each case.

The interval a question asks about is often not the one the rate was quoted in, and the two give different distributions.


Spec links: `spcpt_GPmq8k46YXs6B3kX`


## Card 9 — question_and_answer (`fl_cYVDCvVnv8zxVZDq`)

**FRONT**

On average 4% of a population has green eyes. Why can the number of green-eyed people not be modelled by a Poisson distribution?


**BACK**

Because there is no **interval** of time or space for occurrences to happen in, only a proportion of a group.

A Poisson distribution needs a mean number of occurrences per unit of time or space, and 4% is not a rate of that kind.

Counting green-eyed people in a sample of fixed size is a **binomial** situation instead, with $n$ the size of the sample and $p = 0 . 04$.


Spec links: `spcpt_GPmq8k46YXs6B3kX`


## Card 10 — question_and_answer (`fl_ffvByjQrCdGRfKyV`)

**FRONT**

A shop's customers arrive far more often at lunchtime than at other times of day. Why is a Poisson model for the number of arrivals per hour doubtful?


**BACK**

Because the arrivals are not happening **at random at a steady rate**: the mean number of them is genuinely different for a lunchtime hour and for a mid-morning one.

There is therefore no single $λ$ that describes every hour, and the model can only be rescued by restricting it to a period over which the rate really is steady.


Spec links: `spcpt_GPmq8k46YXs6B3kX`


## Card 11 — question_and_answer (`fl_Tyx7DQvqSvkBdT5Z`)

**FRONT**

The Poisson formula is derived from the binomial distribution. What does a Poisson situation not need that a binomial one does?


**BACK**

A **fixed number of trials**.

A binomial distribution must know $n$ in advance, whereas a Poisson distribution is built from the mean number of occurrences in an interval and never asks how many trials there were.

That is why the number of emails arriving in an hour can be Poisson but cannot be binomial: there is no list of trials to count successes among.


Spec links: `spcpt_dchGk3kdpWq5TpJY`


## Card 12 — question_and_answer (`fl_rMGxtPVP2mVZvWXZ`)

**FRONT**

A football team scores at a mean rate of 2 goals per hour. What distribution models the number of goals in a 90 minute match?


**BACK**

`X \sim \text{Po} \left(3\right)`, because 90 minutes is 1.5 hours and the mean scales with the length of the interval.

$λ$ always has to match the interval the question asks about, so a rate quoted per hour must be converted before anything else is done.

A 30 minute period would scale the other way, giving `\text{Po} \left(1\right)`.


Spec links: `spcpt_dchGk3kdpWq5TpJY`


## Card 13 — question_and_answer (`fl_R9bKmGrBrvxZ67fX`)

**FRONT**

What does the table of the Poisson Cumulative Distribution Function in the formula booklet give you?


**BACK**

It gives `\text{P} \left(X \le x\right)`, the probability of $x$ occurrences **or fewer**, to four decimal places.

It is indexed by $λ$ alone rather than by a pair of parameters, and only certain values of $λ$ are listed.

Everything in it is cumulative, so an individual probability such as `\text{P} \left(X = 3\right)` has to be built as `\text{P} \left(X \le 3\right) - \text{P} \left(X \le 2\right)`.


Spec links: `spcpt_dchGk3kdpWq5TpJY`


## Card 14 — fill_in_the_blanks (`fl_nzg7B7NrkC8SfyD9`)

**FRONT**

A Poisson cumulative table gives only `\text{P} \left(X \le x\right)`. Complete the two rules that turn other inequalities into table entries:

`\text{P} \left(X < x\right) = \text{P} \left(X \le \_\_\_\_\_\_\right)`

`\text{P} \left(a \le X \le b\right) = \text{P} \left(X \le b\right) - \text{P} \left(X \le \_\_\_\_\_\_\right)`


**BACK**

The completed rules are:

`\text{P} \left(X < x\right) = \text{P} \left(X \le x - 1\right)`

`\text{P} \left(a \le X \le b\right) = \text{P} \left(X \le b\right) - \text{P} \left(X \le a - 1\right)`

Both work because $X$ takes whole-number values only, so stepping down from $x$ to $x - 1$ misses nothing out in between.

In the second rule the value $a$ is itself wanted, which is why what you take away has to stop at $a - 1$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_dchGk3kdpWq5TpJY`


## Card 15 — true_or_false (`fl_6XvxdcMJsn6SzHHb`)

**FRONT**

**True or False?**

For `X \sim \text{Po} \left(\lambda\right)`, the probability of no occurrences at all is $\text{e}^{-λ}$.


**BACK**

**True.**

Putting $r = 0$ into the formula gives `\text{P} \left(X = 0\right) = \text{e}^{- \lambda} \times \frac{\lambda^{0}}{0 !}`, and since $λ^{0} = 1$ and $0 ! = 1$ the whole thing collapses to $\text{e}^{-λ}$.

It is worth recognising, because a question about something happening **at least once** is then quickest as $1 - \text{e}^{-λ}$.


Spec links: `spcpt_dchGk3kdpWq5TpJY`


## Card 16 — question_and_answer (`fl_7NDYSJ65XWdVKVPB`)

**FRONT**

Your value of $λ$ is not one of those listed in the cumulative table. How do you find `\text{P} \left(X \le 3\right)`?


**BACK**

Use the formula on each value in turn and add them up, so `\text{P} \left(X \le 3\right)` is the sum of `\text{P} \left(X = 0\right)` through to `\text{P} \left(X = 3\right)`.

Because $\text{e}^{-λ}$ appears in every one of those terms, it can be taken outside a bracket:

`\text{P} \left(X \le 3\right) = \text{e}^{- \lambda} \left(1 + \lambda + \frac{\lambda^{2}}{2 !} + \frac{\lambda^{3}}{3 !}\right)`

That leaves one calculation to work through rather than four.


Spec links: `spcpt_dchGk3kdpWq5TpJY`


## Card 17 — question_and_answer (`fl_qC5ZXCNrgHSVfcdr`)

**FRONT**

Xiao makes silly mistakes at a mean rate of 2 per page, so `X \sim \text{Po} \left(2\right)`. How do you write **at most three** mistakes and **more than three** mistakes as table entries?


**BACK**

**At most three** is `\text{P} \left(X \le 3\right)`, which is read straight off the table, and **more than three** is `1 - \text{P} \left(X \le 3\right)`.

The two use the same entry because they are exactly complementary: every outcome is either three or fewer, or else more than three.

**At least three** would be different again, `1 - \text{P} \left(X \le 2\right)`, because that phrase includes 3 itself.


Spec links: `spcpt_dchGk3kdpWq5TpJY`

