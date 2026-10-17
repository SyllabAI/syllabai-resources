# Binomial & Geometric Distribution

Course: cie-a-level-maths-20-probability-and-statistics-1 · Section: Statistical Distributions

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/flashcards/statistical-distributions/binomial-and-geometric-distribution/


## Card 1 — fill_in_the_blanks (`fl_7tzfCrvt2mdywD7Z`)

**FRONT**

A binomial distribution needs four conditions. Fill in the two that are missing:

the number of trials, $n$, is `\_\_\_\_\_\_`

the trials are **independent**

each trial has exactly **two** outcomes, success or failure

the probability of success, $p$, is `\_\_\_\_\_\_`


**BACK**

The completed conditions are:

the number of trials, $n$, is **fixed**

the probability of success, $p$, is **constant**

A number of trials that is not fixed in advance, or a probability that drifts as the trials go on, rules a binomial model out however well the other two conditions hold.

All four have to be satisfied together, which is why a question asking you to criticise a model is really asking which one has failed.


*Blanks: 0 — answers: []*

Spec links: `spcpt_CFPBfrF9PVcrbCk6`

Flags: fitb_no_blank_marker


## Card 2 — question_and_answer (`fl_zPJ5jFBs5RnQmmCv`)

**FRONT**

What do the two numbers in `X \sim \text{B}(n, p)` stand for?


**BACK**

$n$ is the **fixed number of trials** and $p$ is the **probability of success** on a single trial.

The variable $X$ itself counts how many of those $n$ trials are successes, so it can take any whole-number value from 0 to $n$.

The probability of failure is $1 - p$, which is often written as $q$.


Spec links: `spcpt_CFPBfrF9PVcrbCk6`


## Card 3 — fill_in_the_blanks (`fl_DKsrCVdxwVRhFk7j`)

**FRONT**

Complete the formula for the probability of exactly $r$ successes, filling in the missing **index**:

`\text{P}(X = r) = \begin{bmatrix} n \\ r \end{bmatrix} p^{r} \left(1 - p\right)^{\_\_\_\_\_\_}`


**BACK**

The completed formula is:

`\text{P}(X = r) = \begin{bmatrix} n \\ r \end{bmatrix} p^{r} \left(1 - p\right)^{n - r}`

If $r$ of the $n$ trials succeed then the other $n - r$ must fail, so the two indices always add up to $n$.

That is a quick way to check you have written the formula down correctly.


*Blanks: 0 — answers: []*

Spec links: `spcpt_CFPBfrF9PVcrbCk6`

Flags: fitb_no_blank_marker


## Card 4 — question_and_answer (`fl_jjSbjd4bmc68BPbx`)

**FRONT**

In the binomial probability formula, what is the binomial coefficient counting?


**BACK**

The number of different **orders** in which the $r$ successes could fall among the $n$ trials.

Every one of those orders has the same probability, so you work out the probability of one of them and multiply by how many there are.

Without that factor you would be finding the probability of one particular sequence rather than of $r$ successes however they arise.


Spec links: `spcpt_CFPBfrF9PVcrbCk6`


## Card 5 — fill_in_the_blanks (`fl_w26HTSqyy88KzQwH`)

**FRONT**

Fill in the mean and the variance for `X \sim \text{B}(n, p)`:

`\text{E}(X) = \_\_\_\_\_\_`

`\text{Var}(X) = \_\_\_\_\_\_`


**BACK**

The completed results are:

$\text{E} ( X ) = n p$

$\text{Var} ( X ) = n p ( 1 - p )$

The mean is what intuition expects: 50 trials with a 0.08 chance each give 4 successes on average.

Square-rooting the variance gives the standard deviation, and note that the variance is largest when $p$ is 0.5.


*Blanks: 0 — answers: []*

Spec links: `spcpt_CFPBfrF9PVcrbCk6`

Flags: fitb_no_blank_marker


## Card 6 — question_and_answer (`fl_74BTcGR6PMZRhpJD`)

**FRONT**

How does the shape of a binomial distribution depend on $p$?


**BACK**

With $p$ below 0.5 the graph has a **tail to the right**, and with $p$ above 0.5 a **tail to the left**.

At exactly $p = 0 . 5$ it is **symmetrical**, and the closer $p$ is to 0.5 the more nearly symmetrical it becomes.

The reason is simply that the bulk of the probability sits near $n p$, which is near one end when $p$ is extreme.


Spec links: `spcpt_CFPBfrF9PVcrbCk6`


## Card 7 — question_and_answer (`fl_sBSDgQFKQWsbzKhn`)

**FRONT**

What three things must you identify before writing down a binomial model?


**BACK**

What one **trial** is, what counts as a **success**, and what your **random variable** is.

State the variable in words, for example "let $X$ be the number of students in a class of 30 with black hair", and only then write `X \sim \text{B}(30, p)`.

This matters because the four conditions are conditions on a **variable**, not on a story, so until the variable is named there is nothing to check them against.


Spec links: `spcpt_cBCMfVF2MRC2fhZS`


## Card 8 — true_or_false (`fl_rxmnMzb78j6yvHRT`)

**FRONT**

**True or False?**

The number of yellow cars in a car park of 100 cannot be binomial, because cars come in more than two colours.


**BACK**

**False.**

The trial is whether a given car **is yellow**, and that has exactly two outcomes: yellow, or not yellow.

Grouping every other colour together as "not yellow" is what makes the two-outcome condition hold, and it is worth looking for whenever a situation seems to have too many outcomes.


Spec links: `spcpt_cBCMfVF2MRC2fhZS`


## Card 9 — question_and_answer (`fl_FPyYpVPCHpqWqKdc`)

**FRONT**

Someone eats 5 sweets from a bag of 6 caramels and 4 marshmallows, and $X$ is the number of caramels eaten. Which binomial condition fails?


**BACK**

The trials are not **independent**.

Eating a caramel first leaves fewer caramels in the bag, so what happens on one trial changes the probability on the next.

Sampling without replacement from a small population is the usual way this condition breaks, and it is the condition worth checking first whenever a binomial model looks doubtful.


Spec links: `spcpt_cBCMfVF2MRC2fhZS`


## Card 10 — question_and_answer (`fl_MNsmY6NpTndfcP2R`)

**FRONT**

8% of a **large** population is immune to a virus, and a **random** sample of 50 is taken. What two assumptions let a binomial model be used?


**BACK**

That every person in the sample has the same 8% chance of being immune, and that whether one person is immune does not affect whether another is.

The sample being random and the population being large are what make both of those reasonable, since removing 50 people barely changes the make-up of the population.

If all 50 came from the same family neither assumption would hold.


Spec links: `spcpt_cBCMfVF2MRC2fhZS`


## Card 11 — question_and_answer (`fl_n9BRsYJc2BcCwYRD`)

**FRONT**

How do you find $\text{P} ( X \leq 3 )$ for a binomial distribution?


**BACK**

Work out $\text{P} ( X = 0 )$, $\text{P} ( X = 1 )$, $\text{P} ( X = 2 )$ and $\text{P} ( X = 3 )$ separately from the formula, then add them.

There is no single formula for a cumulative binomial probability, so the sum is the method rather than a shortcut.

Forgetting $\text{P} ( X = 0 )$ is the usual slip, and it is easy to make because zero successes feels like nothing happening.


Spec links: `spcpt_JpjTxPV33Mm5vDvf`


## Card 12 — question_and_answer (`fl_k2RqCwJtQRKT2vS9`)

**FRONT**

What is $\text{P} ( X = 2 . 5 )$ for a binomial distribution, and why?


**BACK**

It is **zero**.

A binomial variable counts successes among a whole number of trials, so the only values it can take are the integers from 0 to $n$, and every other value has probability zero.

That is why every binomial inequality comes down to deciding which **integers** are included.


Spec links: `spcpt_JpjTxPV33Mm5vDvf`


## Card 13 — fill_in_the_blanks (`fl_Vgm8XxgXJB6pNkSg`)

**FRONT**

For a binomial distribution, fill in the integers each probability covers:

$\text{P} ( X < 4 )$ covers $X = 0$ up to and including `\_\_\_\_\_\_`

$\text{P} ( 4 < X \leq 10 )$ covers $X = 10$ down to and including `\_\_\_\_\_\_`


**BACK**

The completed ranges are:

$\text{P} ( X < 4 )$ covers $X = 0$ up to and including **3**

$\text{P} ( 4 < X \leq 10 )$ covers $X = 10$ down to and including **5**

A strict inequality excludes its own endpoint, so $X < 4$ stops at 3 and $4 < X$ starts at 5.

Writing out the list of integers before calculating anything is the surest way to avoid an off-by-one error.


*Blanks: 0 — answers: []*

Spec links: `spcpt_JpjTxPV33Mm5vDvf`

Flags: fitb_no_blank_marker


## Card 14 — true_or_false (`fl_2V5gNMGs6V5KsVGh`)

**FRONT**

**True or False?**

For a binomial distribution, $\text{P} ( X \leq 3 )$ and $\text{P} ( X < 4 )$ are the same.


**BACK**

**True.**

There is no value between 3 and 4 for the two to disagree about, so both cover exactly the integers 0, 1, 2 and 3.

Rewriting one as the other is often what lets you reuse a cumulative result you have already worked out.


Spec links: `spcpt_JpjTxPV33Mm5vDvf`


## Card 15 — question_and_answer (`fl_d7CQXcPS2wQVkMHZ`)

**FRONT**

For `X \sim \text{B}(10, 0.35)`, why find $\text{P} ( X > 3 )$ as $1 - \text{P} ( X \leq 3 )$?


**BACK**

Because $X$ can be any integer from 0 to 10, so "greater than 3" covers seven values while "at most 3" covers only four.

Subtracting from 1 therefore replaces seven separate binomial calculations with four.

Whenever the unwanted values are fewer than the wanted ones, this is the quicker route.


Spec links: `spcpt_JpjTxPV33Mm5vDvf`


## Card 16 — question_and_answer (`fl_TCBbnxBzP8qPFS3s`)

**FRONT**

For `X \sim \text{B}(10, 0.35)`, how do you find $\text{P} ( 3 < X < 6 )$?


**BACK**

Both inequalities are strict, so 3 and 6 are excluded and only $X = 4$ and $X = 5$ are wanted.

Work out each from the formula and add:

`\begin{bmatrix} 10 \\ 4 \end{bmatrix} (0.35)^{4}(0.65)^{6} + \begin{bmatrix} 10 \\ 5 \end{bmatrix} (0.35)^{5}(0.65)^{5} = 0.391`

With only two terms there is nothing to be gained by subtracting from 1 here.


Spec links: `spcpt_JpjTxPV33Mm5vDvf`


## Card 17 — keyword_definition (`fl_Xn4kckZD8RkjnR7J`)

**FRONT**

Define **geometric distribution**.


**BACK**

The **geometric distribution** describes the number of trials needed up to and **including** the first success.

It is written `X \sim \text{Geo}(p)`, where $p$ is the probability of success on any single trial.

Because a success might never have happened yet, $X$ can be any positive whole number, so the distribution has infinitely many values.


Spec links: `spcpt_7RxxhPNkwYwmz3vV`


## Card 18 — question_and_answer (`fl_DtvfvPnqZRrkPJW6`)

**FRONT**

What is the difference between what a binomial variable counts and what a geometric variable counts?


**BACK**

A **binomial** variable counts the number of **successes** in a fixed number of trials.

A **geometric** variable counts the number of **trials** taken to reach the first success.

So the binomial fixes the trials and lets the successes vary, while the geometric fixes the successes at one and lets the trials vary.


Spec links: `spcpt_7RxxhPNkwYwmz3vV`


## Card 19 — fill_in_the_blanks (`fl_4d5sQhKvgtPTTxpp`)

**FRONT**

Complete the geometric probability formula, filling in the missing **index**:

`\text{P}(X = r) = \left(1 - p\right)^{\_\_\_\_\_\_} p`


**BACK**

The completed formula is:

`\text{P}(X = r) = \left(1 - p\right)^{r - 1} p`

If the first success comes on trial $r$, then the $r - 1$ trials before it must all have **failed** and the last one succeeded.

That is why there is a single factor of $p$ sitting outside the power rather than inside it.


*Blanks: 0 — answers: []*

Spec links: `spcpt_CrCq4jsdbsJthgqb`

Flags: fitb_no_blank_marker


## Card 20 — question_and_answer (`fl_FDkkDbfPnJJ9S8BW`)

**FRONT**

Why is `\text{P}(X > r) = \left(1 - p\right)^{r}` for a geometric distribution?


**BACK**

Saying $X > r$ says the first success has **not** happened within the first $r$ trials, so all $r$ of them failed.

The probability of that is just $1 - p$ multiplied by itself $r$ times.

This one short expression replaces an infinite sum, which is what makes geometric inequalities much easier than binomial ones.


Spec links: `spcpt_CrCq4jsdbsJthgqb`


## Card 21 — question_and_answer (`fl_VwSM4zgqfmsPvq72`)

**FRONT**

How do you find $\text{P} ( 3 \leq X < 8 )$ for `X \sim \text{Geo}(0.4)`?


**BACK**

Turn it into a difference of two "greater than" probabilities, which are the easy ones to work out:

$\text{P} ( X > 2 ) - \text{P} ( X > 7 ) = 0 . 6^{2} - 0 . 6^{7} = 0 . 332$

Getting the two indices right is the whole difficulty: $X \geq 3$ means more than 2 trials, and $X < 8$ means at most 7.

Writing down which integers are wanted before converting is what keeps them straight.


Spec links: `spcpt_CrCq4jsdbsJthgqb`


## Card 22 — true_or_false (`fl_RbNd6NsFjdcmryvY`)

**FRONT**

**True or False?**

The most likely number of trials to the first success is 1, however small $p$ is.


**BACK**

**True.**

Whatever the value of $p$, the single value $r = 1$ has a higher probability than any other, so the **mode** of every geometric distribution is 1.

That surprises people who expect a small $p$ to push the most likely wait further out; what a small $p$ actually does is flatten the decline, not move the peak.


Spec links: `spcpt_7RxxhPNkwYwmz3vV`


## Card 23 — question_and_answer (`fl_8Rs3ZjrMqFPRvv9V`)

**FRONT**

For a geometric distribution, why does `\text{P}(X = 8 \vert X > 5)` equal $\text{P} ( X = 3 )$?


**BACK**

The trials are independent and $p$ never changes, so five failures leave you in exactly the situation you started in.

Counting afresh from that point, needing the success on trial 8 is needing it on the third trial from now.

This property is called being **memoryless**, and it is what "given that" questions on a geometric distribution are testing.


Spec links: `spcpt_CrCq4jsdbsJthgqb`


## Card 24 — question_and_answer (`fl_gVdgqj2FpY2CFBGy`)

**FRONT**

For `X \sim \text{Geo}(p)`, what is $\text{E} ( X )$?


**BACK**

It is $\frac{1}{p}$.

So a success with probability 0.25 takes 4 trials on average, and a success with probability 0.1 takes 10.

The rarer the success, the longer the expected wait, which is exactly what intuition would say.


Spec links: `spcpt_7RxxhPNkwYwmz3vV`


## Card 25 — question_and_answer (`fl_gdNm6MSNb3hY5Bmn`)

**FRONT**

Why do the probabilities of a geometric distribution form a geometric progression, and what do they sum to?


**BACK**

Each probability is the one before it multiplied by $1 - p$, so they form a progression with first term $p$ and common ratio $1 - p$.

Its sum to infinity is $\frac{p}{1-(1-p)} = 1$, which is exactly what any probability distribution has to total.

That sum is also where the distribution gets its name.


Spec links: `spcpt_7RxxhPNkwYwmz3vV`


## Card 26 — question_and_answer (`fl_MW5bmwvVvGsvFhMX`)

**FRONT**

A skateboarder attempts a trick repeatedly until they land it. Why might a geometric model be unsuitable here?


**BACK**

Because the probability of success should **increase** with practice, so it is not constant from trial to trial.

The trials are not really independent either, since each attempt teaches the skateboarder something about the next.

Anything involving practising, learning or tiring is worth checking for this, and it is the condition that fails most often.


Spec links: `spcpt_VxJMMF37MG3rQ92M`


## Card 27 — question_and_answer (`fl_RkJnFfZDV6HvzXBj`)

**FRONT**

A switch is pressed on and off until it wears out. Why is that geometric rather than binomial?


**BACK**

What is being counted is the number of presses **up to and including** the one that breaks it, not how many failures occur in a fixed number of presses.

The "success" here is the switch failing, which shows that a success just means the outcome you are interested in rather than a good outcome.

Any situation where the **first** occurrence of something is what matters is a geometric one.


Spec links: `spcpt_VxJMMF37MG3rQ92M`

