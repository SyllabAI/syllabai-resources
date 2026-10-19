# Working with Distributions

Course: ial-maths-20-statistics-2 · Section: Statistical Distributions

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/flashcards/statistical-distributions/working-with-distributions/


## Card 1 — question_and_answer (`fl_3NmYWfkjhsBjJTf6`)

**FRONT**

What is the first question to ask when choosing a distribution to model a variable?


**BACK**

Whether the variable **counts** something or **measures** something.

A variable that counts is **discrete**, so the candidates are the binomial and the Poisson distributions.

A variable that measures is **continuous**, so the candidate is the normal distribution.


Spec links: `spcpt_BSThwNTGCsyfmCbs`


## Card 2 — question_and_answer (`fl_44sDxhVQx3TPSMyy`)

**FRONT**

Two counts: the number of faults in a 10 metre roll of cloth, and the number of faulty items in a box of 10. Which distribution suits each?


**BACK**

The faults in the cloth are **Poisson**, because they occur across an interval of space with no fixed number of trials to count them among.

The faulty items are **binomial**, because there are exactly 10 trials, one per item, and each is faulty or not.

That is the discriminator between the two: a fixed number of trials points to the binomial, and an interval of time or space points to the Poisson.


Spec links: `spcpt_BSThwNTGCsyfmCbs`


## Card 3 — true_or_false (`fl_9W7xDGM4RH3DggR9`)

**FRONT**

**True or False?**

In a sample of 10 cows, "weighs more than 700 kg" can be treated as a successful trial.


**BACK**

**True.**

Any criterion that each member of a sample either meets or does not meet is a trial with exactly two outcomes.

That is what lets a **count of how many members satisfy a criterion** be modelled by a binomial distribution, even though nothing in the situation looks like an experiment being repeated.


Spec links: `spcpt_BSThwNTGCsyfmCbs`


## Card 4 — question_and_answer (`fl_Kdzw2FfJVFnpMCpM`)

**FRONT**

Cow masses are modelled by `\text{N} \left(550 , 80^{2}\right)` kg, and 10 cows are sampled. To find the probability that at most one weighs over 700 kg, which two distributions do you need?


**BACK**

First the **normal** distribution, to find `p = \text{P} \left(X > 700\right)` for a single cow.

Then a **binomial** distribution `Y \sim \text{B} \left(10 , p\right)` counting how many of the 10 are over 700 kg, from which you want `\text{P} \left(Y \le 1\right)`.

Be deliberate about which letter is which: $X$ is a mass in kilograms and $Y$ is a count of cows, so they have different distributions and nothing in common but the criterion linking them.


Spec links: `spcpt_BSThwNTGCsyfmCbs`


## Card 5 — question_and_answer (`fl_xFNG7sKgsNJVPHGM`)

**FRONT**

You have real data and want to know whether a normal distribution is a reasonable model for it. What can you look at?


**BACK**

Draw a **histogram** of the data and see whether it is roughly **symmetrical** and **bell-shaped**.

If the variable really is normally distributed then collecting more data should smooth the outline of the histogram out, so that it comes to resemble the normal curve more and more closely.

A histogram that stays lopsided however much data is added is evidence that a normal model is the wrong choice.


Spec links: `spcpt_BSThwNTGCsyfmCbs`


## Card 6 — question_and_answer (`fl_GJJdXh3KcpvXzHtP`)

**FRONT**

Why is a continuity correction needed when a discrete distribution is approximated by a normal one?


**BACK**

Because a discrete variable takes separate whole-number values while a normal variable takes any value at all, so each whole number has to be widened into the interval that rounds to it.

A Poisson value of $X = 4$ becomes everything from 3.5 to 4.5, giving `\text{P} \left(X = 4\right) \approx \text{P} \left(3 . 5 < X_{N} < 4 . 5\right)`.

Without the widening there would be nothing to find, since a normal distribution gives probability zero to any single value.


Spec links: `spcpt_PjFxtJZSDVwMp4RJ`


## Card 7 — fill_in_the_blanks (`fl_9RtsSFhd9Xqsb5q6`)

**FRONT**

Complete the two continuity corrections for the upper-tail inequalities, filling in each missing number **including its sign**:

`\text{P} \left(X \ge k\right) \approx \text{P} \left(X_{N} > k \_\_\_\_\_\_\right)`

`\text{P} \left(X > k\right) \approx \text{P} \left(X_{N} > k \_\_\_\_\_\_\right)`


**BACK**

The completed corrections are:

`\text{P} \left(X \ge k\right) \approx \text{P} \left(X_{N} > k - 0 . 5\right)`

`\text{P} \left(X > k\right) \approx \text{P} \left(X_{N} > k + 0 . 5\right)`

These two look backwards, because **at least** $k$ takes away 0.5 while **more than** $k$ adds it.

They are the right way round because $X \geq k$ includes $k$, so the boundary has to drop far enough to swallow the whole of $k$'s interval, whereas $X > k$ excludes it and the boundary has to rise clear of it.


*Blanks: 0 — answers: ['at least', 'more than']*

Spec links: `spcpt_PjFxtJZSDVwMp4RJ`

Flags: blank_answer_mismatch


## Card 8 — question_and_answer (`fl_RcyQNzRMtqyPvQ9r`)

**FRONT**

Rather than memorising four separate continuity corrections, what single question tells you which way to move a boundary?


**BACK**

Ask whether the value $k$ is **included** in the range you want.

If it is included, move the boundary outwards by 0.5 so that the whole of $k$'s interval is taken in; if it is excluded, move the boundary inwards by 0.5 so that the interval is left out.

That is why `\text{P} \left(X \le k\right) \approx \text{P} \left(X_{N} < k + 0 . 5\right)` while `\text{P} \left(X < k\right) \approx \text{P} \left(X_{N} < k - 0 . 5\right)`.


Spec links: `spcpt_PjFxtJZSDVwMp4RJ`


## Card 9 — true_or_false (`fl_KVXrbTtjRqCtn6CH`)

**FRONT**

**True or False?**

A continuity correction is needed whenever a discrete distribution is approximated by a normal distribution.


**BACK**

**True.**

It does not matter which discrete distribution you started from: the correction is needed because the approximating distribution is **continuous** and the original was not.

So both a binomial and a Poisson distribution need one when a normal distribution stands in for them.


Spec links: `spcpt_PjFxtJZSDVwMp4RJ`


## Card 10 — question_and_answer (`fl_qNN8sh5s4jQtZpjn`)

**FRONT**

How do you apply a continuity correction to a closed inequality such as `\text{P} \left(a < X \le b\right)`?


**BACK**

Treat each end completely separately and then put the two results together.

Here $X > a$ becomes $X_{N} > a + 0 . 5$ because $a$ is excluded, and $X \leq b$ becomes $X_{N} < b + 0 . 5$ because $b$ is included, giving:

`\text{P} \left(a < X \le b\right) \approx \text{P} \left(a + 0 . 5 < X_{N} < b + 0 . 5\right)`

Notice that both ends moved **up** here, so do not assume the two corrections always have opposite signs.


Spec links: `spcpt_PjFxtJZSDVwMp4RJ`


## Card 11 — question_and_answer (`fl_zTw8YTFZwsJzkhcB`)

**FRONT**

When can a Poisson distribution be approximated by a normal one, and by which normal distribution?


**BACK**

When $λ$ is **large**, and the approximating distribution is `\text{N} \left(\lambda , \lambda\right)`.

Both parameters are $λ$ because the mean and the variance of a Poisson distribution are equal, so matching them to the normal distribution uses the same number twice.

The approximation is never exact, but the larger $λ$ is the closer it gets.


Spec links: `spcpt_YkKMWYDSjftxhVK2`


## Card 12 — question_and_answer (`fl_YymNDcpr3rdX5wvm`)

**FRONT**

In the normal approximation to `\text{Po} \left(\lambda\right)`, why is the standard deviation $\sqrt{λ}$ rather than $λ$?


**BACK**

Because the second number in `\text{N} \left(\mu , \sigma^{2}\right)` is the **variance**, and it is the variance of the Poisson distribution that equals $λ$.

Standardising needs $σ$, so the square root has to be taken before any $z$-value is worked out.

This is a slip worth guarding against precisely because the mean and the variance are the same number here, which makes it easy to reach for $λ$ twice.


Spec links: `spcpt_YkKMWYDSjftxhVK2`


## Card 13 — question_and_answer (`fl_M3BSpzcSNTx26KQV`)

**FRONT**

Hits on a web page follow `\text{Po} \left(40\right)`. Use a normal approximation to set up the probability of more than 50 hits in an hour.


**BACK**

The approximating distribution is `X_{N} \sim \text{N} \left(40 , 40\right)`, and **more than** 50 excludes 50, so the boundary moves up to 50.5.

That gives `\text{P} \left(X > 50\right) \approx \text{P} \left(X_{N} > 50 . 5\right)`, which standardises to:

$z = \frac{50.5-40}{\sqrt{40}} = 1 . 66$

The table then gives `1 - \Phi \left(1 . 66\right) = 1 - 0 . 9515 = 0 . 0485`.


Spec links: `spcpt_YkKMWYDSjftxhVK2`


## Card 14 — question_and_answer (`fl_cjTVp6gf7KfBRRJz`)

**FRONT**

A binomial distribution is being approximated by a normal one. What are the mean and variance of the approximating distribution?


**BACK**

Exactly the binomial's own, so $μ = n p$ and `\sigma^{2} = n p \left(1 - p\right)`.

An approximating distribution is chosen by **matching** what you already know about the original, and the mean and variance are what a normal distribution needs.

Remember to square-root the variance before standardising, since `\text{N} \left(\mu , \sigma^{2}\right)` carries the variance rather than the standard deviation.


Spec links: `spcpt_YY4h2CNvvKYfq4Sk`


## Card 15 — question_and_answer (`fl_4h92kfzTyPBzg94D`)

**FRONT**

Why must $p$ be close to 0.5 for a normal approximation to a binomial to work well?


**BACK**

Because a normal distribution is perfectly **symmetrical**, so it can only fit a binomial distribution that is nearly symmetrical itself.

A binomial distribution is exactly symmetrical at $p = 0 . 5$ and grows more and more lopsided as $p$ moves away from it, developing a long tail on one side.

Fitting a symmetrical curve to a strongly skewed distribution would give poor answers in both tails, which is where the interesting probabilities usually are.


Spec links: `spcpt_YY4h2CNvvKYfq4Sk`


## Card 16 — question_and_answer (`fl_Tfq9w2fFCSzcvTkD`)

**FRONT**

`X \sim \text{B} \left(1250 , 0 . 4\right)`. Set up a normal approximation to `\text{P} \left(485 \le X \le 530\right)`.


**BACK**

The parameters are $μ = 1250 \times 0 . 4 = 500$ and $σ^{2} = 1250 \times 0 . 4 \times 0 . 6 = 300$, so `X_{N} \sim \text{N} \left(500 , 300\right)`.

Both 485 and 530 are included in the range, so both boundaries move outwards:

`\text{P} \left(485 \le X \le 530\right) \approx \text{P} \left(484 . 5 < X_{N} < 530 . 5\right)`

Standardising with $\sqrt{300}$ then gives $z$-values of $- 0 . 89$ and $1 . 76$ to read from the table.


Spec links: `spcpt_YY4h2CNvvKYfq4Sk`


## Card 17 — question_and_answer (`fl_gChmvCXdDsCztNNR`)

**FRONT**

A binomial distribution is being approximated by a Poisson one. What is $λ$, and why is that the only parameter needed?


**BACK**

$λ = n p$, the binomial distribution's own mean.

A Poisson distribution has just one parameter, so matching the mean is all there is to do, unlike the normal case where a variance has to be matched as well.

The approximation exists because a Poisson distribution is what a binomial one turns into as $n$ grows without limit and $p$ shrinks towards zero.


Spec links: `spcpt_PhRPk9SkcSgp9q8p`


## Card 18 — true_or_false (`fl_K66vx68n5PfN7QVS`)

**FRONT**

**True or False?**

A continuity correction is needed when a binomial distribution is approximated by a Poisson distribution.


**BACK**

**False.**

Both the binomial and the Poisson distributions are **discrete**, so both count in whole numbers and there is no switch from counting to measuring to correct for.

A correction is only ever needed when the approximating distribution is a continuous one.


Spec links: `spcpt_PhRPk9SkcSgp9q8p`


## Card 19 — question_and_answer (`fl_wy59J7Jn42HHCbNw`)

**FRONT**

One person in a thousand who visits a website subscribes, and the site had 3000 visits. Use a suitable approximation to find the probability that more than 5 subscribed.


**BACK**

Here $n = 3000$ and $p = 0 . 001$, so $λ = 3000 \times 0 . 001 = 3$ and $X$ is approximately `\text{Po} \left(3\right)`.

More than 5 means everything above 5, so no continuity correction is involved and `\text{P} \left(X > 5\right) = 1 - \text{P} \left(X \le 5\right)`.

The cumulative table at $λ = 3$ gives `\text{P} \left(X \le 5\right) = 0 . 9161`, so the answer is $0 . 0839$.


Spec links: `spcpt_PhRPk9SkcSgp9q8p`


## Card 20 — true_or_false (`fl_CkQPSSYjH4twNBWX`)

**FRONT**

**True or False?**

When `\text{B} \left(n , p\right)` is approximated by `\text{Po} \left(n p\right)`, the approximating distribution has the same variance as the original.


**BACK**

**False.**

The binomial variance is `n p \left(1 - p\right)` while the Poisson variance is $n p$, so the approximation makes the spread too large by a factor of $\frac{1}{1-p}$.

That factor is what the small-$p$ condition is really about: with $p = 0 . 001$ the variance is out by a tenth of one per cent, but with $p = 0 . 4$ it would be out by two thirds.


Spec links: `spcpt_PhRPk9SkcSgp9q8p`


## Card 21 — question_and_answer (`fl_NfhQHp2b8MfgCQWf`)

**FRONT**

`\text{B} \left(100 , 0 . 02\right)` and `\text{B} \left(100 , 0 . 45\right)` both need approximating. Which approximation suits each?


**BACK**

`\text{B} \left(100 , 0 . 02\right)` takes a **Poisson** approximation, because $p$ is small, giving `\text{Po} \left(2\right)`.

`\text{B} \left(100 , 0 . 45\right)` takes a **normal** approximation, because $p$ is close to 0.5, giving `\text{N} \left(45 , 24 . 75\right)`.

With $n$ large in both cases it is the value of $p$ alone that decides, and the choice changes whether a continuity correction is needed.


Spec links: `spcpt_dhBtPN6YhDdPNKHp`


## Card 22 — question_and_answer (`fl_GfjdFk3vHtKB6mXh`)

**FRONT**

Why can a binomial distribution such as `\text{B} \left(1250 , 0 . 4\right)` not simply be worked out directly?


**BACK**

The cumulative table in the formula booklet lists $n$ only as far as 50, so a distribution with $n = 1250$ has no entry in it anywhere.

Falling back on the formula would mean working out and adding dozens of individual probabilities, which is not realistic under exam conditions.

The same test settles the Poisson case: if the mean is bigger than any $λ$ the booklet lists, an approximation is the only route left.


Spec links: `spcpt_dhBtPN6YhDdPNKHp`


## Card 23 — question_and_answer (`fl_w2Bs8tNrNZm5C8vK`)

**FRONT**

Your distribution is a Poisson one rather than a binomial one. Which approximations are open to you?


**BACK**

Only the **normal** one.

A binomial distribution has two possible approximations to choose between, but a Poisson distribution has just the one, so once you have established what you are approximating **from** there is no decision left to make.

That makes identifying the original distribution the first thing to settle, since it may remove the choice altogether.


Spec links: `spcpt_dhBtPN6YhDdPNKHp`

