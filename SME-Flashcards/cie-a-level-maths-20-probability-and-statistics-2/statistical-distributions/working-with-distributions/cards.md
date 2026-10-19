# Working with Distributions

Course: cie-a-level-maths-20-probability-and-statistics-2 · Section: Statistical Distributions

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/flashcards/statistical-distributions/working-with-distributions/


## Card 1 — question_and_answer (`fl_t9nWBkySJMz57zkr`)

**FRONT**

What is the first question to ask when choosing a distribution to model something?


**BACK**

Whether the variable **counts** something or **measures** something.

Counting points to a discrete distribution, and measuring to a continuous one, which settles half the question immediately.

After that it is a matter of which counting situation, or whether the measured data is symmetrical and bell-shaped.


Spec links: `spcpt_JctJy4spgKD9pRHB`


## Card 2 — fill_in_the_blanks (`fl_MfFhSVMfFxmQrfS4`)

**FRONT**

Fill in the three conditions for a Poisson model:

the mean number of occurrences, $λ$, is known and `\_\_\_\_\_\_`

the events occur at `\_\_\_\_\_\_`

the events occur singly and `\_\_\_\_\_\_`


**BACK**

The completed conditions are:

the mean number of occurrences, $λ$, is known and **finite**

the events occur at **random**

the events occur singly and **independently**

Independence is the one worth checking hardest, because it is the condition a real context most often breaks.


*Blanks: 0 — answers: []*

Spec links: `spcpt_JctJy4spgKD9pRHB`

Flags: fitb_no_blank_marker


## Card 3 — question_and_answer (`fl_V5zr7JpDskqpWvxg`)

**FRONT**

Both a binomial and a Poisson variable count something. What decides between them?


**BACK**

Whether there is a **fixed number of trials**.

A binomial counts successes among a fixed number $n$ of trials, so it can never exceed $n$.

A Poisson counts occurrences in an interval of time or space with no fixed number of trials at all, so it has no upper limit.


Spec links: `spcpt_JctJy4spgKD9pRHB`


## Card 4 — question_and_answer (`fl_kFfqGPWqvxGF7ybr`)

**FRONT**

What distinguishes a geometric model from a binomial one?


**BACK**

A geometric variable counts the **trials up to and including the first success**, so the trials continue until that success happens.

A binomial fixes the number of trials in advance and counts how many succeed.

The three other conditions are the same for both: independent trials, two outcomes, and a constant probability of success.


Spec links: `spcpt_JctJy4spgKD9pRHB`


## Card 5 — true_or_false (`fl_SSvvfB6P4x8dKYsC`)

**FRONT**

**True or False?**

A histogram of real data can tell you whether a normal model is reasonable.


**BACK**

**True.**

If the histogram is roughly symmetrical and bell-shaped, a normal model is worth using.

As more data is collected the outline should smooth out and come to resemble the normal curve itself, so a lopsided or two-peaked histogram is telling you to look elsewhere.


Spec links: `spcpt_JctJy4spgKD9pRHB`


## Card 6 — question_and_answer (`fl_cDPSgXq3N8GgdbSN`)

**FRONT**

Why must you always state what your variables and parameters represent?


**BACK**

Because a question can involve more than one variable measuring quite different things, such as a mass and a count.

Writing each one down in words is what stops a mass being fed into a distribution that counts, or a parameter from one model being used in another.

It also forces you to decide what is actually being modelled before choosing anything.


Spec links: `spcpt_JctJy4spgKD9pRHB`


## Card 7 — fill_in_the_blanks (`fl_D6H8KRyfvhnwQk8Z`)

**FRONT**

Fill in the condition for approximating a Poisson distribution by a normal one:

$λ$ must be large, in practice greater than about `\_\_\_\_\_\_`


**BACK**

The completed condition is:

$λ$ must be large, in practice greater than about **15**

The larger $λ$ becomes, the more symmetrical the Poisson distribution is, and the better a bell-shaped curve fits it.

Below that the distribution still has a noticeable tail to the right, and a symmetrical curve fits it badly.


*Blanks: 0 — answers: []*

Spec links: `spcpt_H5hw3Xwrd5q3tMVf`

Flags: fitb_no_blank_marker


## Card 8 — question_and_answer (`fl_6kCBYmyvVqktP4jD`)

**FRONT**

Which normal distribution approximates `X \sim \text{Po}(\lambda)`?


**BACK**

It is $\text{N} ( λ , λ )$: both the mean and the variance are $λ$.

That is because a Poisson distribution has its mean and variance **exactly** equal, so matching them to the normal puts the same number in both places.

The standard deviation you then standardise with is $\sqrt{λ}$, not $λ$.


Spec links: `spcpt_H5hw3Xwrd5q3tMVf`


## Card 9 — question_and_answer (`fl_8QBxsn3dqZStwW2r`)

**FRONT**

For `X \sim \text{Po}(40)`, how do you approximate $\text{P} ( X > 50 )$?


**BACK**

$λ = 40$ is large, so use `X_{N} \sim \text{N}(40, 40)`.

Apply the continuity correction, which turns $X > 50$ into $X_{N} > 50 . 5$, then standardise with $\sqrt{40}$:

$z = \frac{50.5-40}{\sqrt{40}} = 1 . 660$

That gives $1 - Φ ( 1 . 660 ) = 0 . 0485$.


Spec links: `spcpt_H5hw3Xwrd5q3tMVf`


## Card 10 — question_and_answer (`fl_pkbsrgrrfNbV7xdy`)

**FRONT**

Which of the two approximations needs a continuity correction, and why only that one?


**BACK**

Only the **normal** approximation to a Poisson, because it replaces a **discrete** variable with a **continuous** one.

A Poisson approximation to a binomial needs none at all, since both distributions are discrete and whole numbers stay whole numbers.

Applying a correction where none is needed is as much an error as leaving one out where it is.


Spec links: `spcpt_z3bqrJJTTNNyrnj2`


## Card 11 — fill_in_the_blanks (`fl_Vm2zZ6Pzd4VDf5JZ`)

**FRONT**

Fill in the two conditions for approximating a binomial distribution by a Poisson one:

$n$ is large, in practice greater than about `\_\_\_\_\_\_`

$p$ is small, so that $n p$ is less than about `\_\_\_\_\_\_`


**BACK**

The completed conditions are:

$n$ is large, in practice greater than about **50**

$p$ is small, so that $n p$ is less than about **5**

The Poisson distribution arises from the binomial as $n$ grows and $p$ shrinks with their product staying finite, which is why those two pull in opposite directions.

Notice this is the reverse of what a **normal** approximation to a binomial wants, where $n p$ has to be large.


*Blanks: 0 — answers: []*

Spec links: `spcpt_z3bqrJJTTNNyrnj2`

Flags: fitb_no_blank_marker


## Card 12 — question_and_answer (`fl_qvTd7jJ6BGGyn8ZN`)

**FRONT**

What is $λ$ when a binomial distribution is approximated by a Poisson one?


**BACK**

It is $n p$, the mean of the binomial.

The approximating distribution is matched to the original by its **mean**, and a Poisson has only that one parameter to fix.

So 3000 trials with probability $0 . 001$ each give $\text{Po} ( 3 )$.


Spec links: `spcpt_z3bqrJJTTNNyrnj2`


## Card 13 — question_and_answer (`fl_qtXk5Tn5KQ3Sd2Ny`)

**FRONT**

You cannot compute a probability from the original distribution. What do you decide first?


**BACK**

**Which distribution you are approximating from**, since that limits what you can approximate to.

A binomial can be approximated by either a Poisson or a normal distribution, depending on which conditions hold.

A Poisson can only be approximated by a normal distribution.


Spec links: `spcpt_yJjTB6XVN77V49nJ`


## Card 14 — true_or_false (`fl_W5XKsfnq5kBQPyDs`)

**FRONT**

**True or False?**

An approximation is always second best, since the exact distribution would give a better answer.


**BACK**

**False.**

The exact answer is better only if you can actually reach it, and a cumulative probability spanning dozens of values needs one term for each.

When $n$ or $λ$ is large enough, the approximation is not a compromise but the only practical route, and the conditions exist precisely to keep it accurate.


Spec links: `spcpt_yJjTB6XVN77V49nJ`


## Card 15 — question_and_answer (`fl_3tDpHFQT9nTPZb3D`)

**FRONT**

A binomial has $n = 3000$ and $p = 0 . 001$. Which approximation fits, and why not the other one?


**BACK**

A **Poisson** approximation, with $λ = n p = 3$, since $n$ is well over 50 and $n p$ is under 5.

A normal approximation would fail here: it needs $n p$ to be greater than 5, and 3 is not.

The two sets of conditions are close to being opposites, so checking $n p$ almost always settles which one is meant.


Spec links: `spcpt_yJjTB6XVN77V49nJ`

