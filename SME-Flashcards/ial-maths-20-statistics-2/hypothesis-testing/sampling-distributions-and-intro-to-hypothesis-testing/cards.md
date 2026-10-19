# Sampling Distributions & Introduction to Hypothesis Testing

Course: ial-maths-20-statistics-2 · Section: Hypothesis Testing

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/flashcards/hypothesis-testing/sampling-distributions-and-intro-to-hypothesis-testing/


## Card 1 — fill_in_the_blanks (`fl_JdfSZWnvRcGjR9ZY`)

**FRONT**

Fill in the two missing sampling terms:

A `\_\_\_\_\_\_` is the whole set of things you are interested in.

A `\_\_\_\_\_\_` is a subset of it that you actually collect data from.


**BACK**

The completed statements are:

A **population** is the whole set of things you are interested in.

A **sample** is a subset of it that you actually collect data from.

If a vet wants to know how long a typical French bulldog sleeps, the population is every French bulldog there is, and a sample might be the bulldogs from a few cities.


*Blanks: 0 — answers: ['population', 'sample']*

Spec links: `spcpt_tfzp7PgcTfMs9Ddw`

Flags: blank_answer_mismatch


## Card 2 — question_and_answer (`fl_qvf9Yd368bmRWSSV`)

**FRONT**

What is a **sampling unit**, and what is a **sampling frame**?


**BACK**

A **sampling unit** is one individual member of the population, such as a single French bulldog.

A **sampling frame** is a **list** of all the members of the population, such as a company's list of its employees' names.


Spec links: `spcpt_tfzp7PgcTfMs9Ddw`


## Card 3 — question_and_answer (`fl_DsKy92KmSKJgnzh9`)

**FRONT**

What is the difference between a **population parameter** and a **sample statistic**?


**BACK**

A **population parameter** is a numerical value describing the whole population, such as the mean height $μ$ of all 16-year-olds in the UK, and it is usually **unknown**.

A **sample statistic** is a value computed from the data in a sample, such as the mean height $\overline{x}$ of 200 of them.

Statistics exist in order to **estimate** parameters, which is the whole reason for sampling at all.


Spec links: `spcpt_tfzp7PgcTfMs9Ddw`


## Card 4 — question_and_answer (`fl_3bW4nMp76G4zD2D9`)

**FRONT**

What does a **census** collect, and why is sampling usually preferred?


**BACK**

A census collects data about **every** member of the population, which is what makes its results fully accurate.

It is slow and expensive, and where the members are consumables it destroys the population, as testing every firework a company makes would.

Sampling is quicker, cheaper and leaves less data to analyse, at the cost of possibly not representing the population and of introducing **bias**.


Spec links: `spcpt_tfzp7PgcTfMs9Ddw`


## Card 5 — question_and_answer (`fl_xtQ7tWfz6hgmyfFD`)

**FRONT**

Why is $\frac{Σx}{n} - μ^{2}$ not a statistic, when `\frac{\Sigma x}{n} - \left(\bar{X}\right)^{2}` is?


**BACK**

Because a **statistic** has to be calculable from the sample data alone, and $μ$ is an unknown **population parameter**.

$\overline{X}$ is the mean of the sample, so the second expression can actually be worked out once the sample is in hand, while the first cannot.

That is the test to apply: if an unknown population value appears anywhere in it, it is not a statistic.


Spec links: `spcpt_tfzp7PgcTfMs9Ddw`


## Card 6 — keyword_definition (`fl_q4PyRtWFYFgZtf7t`)

**FRONT**

Define the **sampling distribution** of a statistic.


**BACK**

The **sampling distribution** of a statistic gives all the **possible values** that the statistic can take, together with the probability of each one.

A statistic is itself a **random variable**, because its value depends on which sample happens to be drawn, so it has a distribution like any other random variable.


Spec links: `spcpt_tfzp7PgcTfMs9Ddw`


## Card 7 — question_and_answer (`fl_bDgmSrkNn9GCP4xq`)

**FRONT**

How do you find the sampling distribution of a statistic such as the sample mean?


**BACK**

List every possible sample, work out the value of the statistic for each one, and work out the probability of each sample being drawn.

Then build the distribution table by **adding together** the probabilities of all the samples that give the same value of the statistic.

Grouping samples with the same combination of members as you list them makes that last step much easier.


Spec links: `spcpt_tfzp7PgcTfMs9Ddw`


## Card 8 — true_or_false (`fl_tTnCbJS6NTvCTnwX`)

**FRONT**

**True or False?**

When listing the possible samples, AAB and ABA count as the same sample.


**BACK**

**False.**

They are listed **separately**, because they are different samples even though they contain the same members.

That is why a sample of 3 taken from a population with 2 types of member has $2^{3} = 8$ possible samples rather than fewer, and grouping them by combination afterwards is a shortcut rather than a reason to leave any out.


Spec links: `spcpt_tfzp7PgcTfMs9Ddw`


## Card 9 — question_and_answer (`fl_dNjZMGP5J3SpdBvJ`)

**FRONT**

The population is described as **large**. What does that let you assume when working out each sample's probability?


**BACK**

That the sampling can be treated as though it were **with replacement**.

The probability of drawing each type of member then stays **constant** however many have already been taken, so the selections are independent and their probabilities simply multiply.

Without that assumption every draw would change the make-up of what was left, and the probabilities would have to be recalculated at each step.


Spec links: `spcpt_tfzp7PgcTfMs9Ddw`


## Card 10 — keyword_definition (`fl_dPqGKM79fhXq4nHB`)

**FRONT**

Define the **null hypothesis** and the **alternative hypothesis**.


**BACK**

The **null hypothesis** $\text{H}_{0}$ states the value of the population parameter on the assumption that nothing has changed.

The **alternative hypothesis** $\text{H}_{1}$ states how that parameter might have changed instead.

A test assumes $\text{H}_{0}$ is true the whole way through, and ends by either **rejecting** it or failing to reject it.


Spec links: `spcpt_FyrqXqf8PCg6CTb8`


## Card 11 — fill_in_the_blanks (`fl_kn7yWXYfx6sytWrZ`)

**FRONT**

A hypothesis test concerns a population parameter $θ$. Fill in the two missing relation symbols:

`\text{H}_{0} : \theta \_\_\_\_\_\_ \ldots`

testing for a change, `\text{H}_{1} : \theta \_\_\_\_\_\_ \ldots`


**BACK**

The completed hypotheses are:

$\text{H}_{0} : θ = \dots$

testing for a change, $\text{H}_{1} : θ \neq \dots$

The null hypothesis always takes the **equals** form, whatever kind of test is being run.

A **two-tailed** test uses $\neq$ because it claims only that the parameter has moved, while a **one-tailed** test uses $>$ or $<$ and claims a direction as well.


*Blanks: 0 — answers: ['equals', 'two-tailed', 'one-tailed']*

Spec links: `spcpt_FyrqXqf8PCg6CTb8`

Flags: blank_answer_mismatch


## Card 12 — keyword_definition (`fl_vtgNRjWhyw2pJ7Tj`)

**FRONT**

Define the **significance level** of a hypothesis test.


**BACK**

The **significance level** is the probability threshold the test is judged against: it sets how unlikely the observed result has to be, assuming $\text{H}_{0}$ is true, before $\text{H}_{0}$ is rejected.

It is usually 1%, 5% or 10%, although a question may set some other value.

A smaller significance level demands stronger evidence before the null hypothesis is given up.


Spec links: `spcpt_FyrqXqf8PCg6CTb8`


## Card 13 — question_and_answer (`fl_nzNTsPVVW2Q5NNqV`)

**FRONT**

Why must the significance level be fixed before the test is carried out?


**BACK**

Because choosing it afterwards would let you pick whichever threshold gives the answer you wanted.

The significance level is a statement about how much evidence you are demanding, so it has to be settled independently of what the data turns out to say.

The same observed result can be significant at 5% and not significant at 1%, which is exactly why the level cannot be chosen once the result is known.


Spec links: `spcpt_FyrqXqf8PCg6CTb8`


## Card 14 — keyword_definition (`fl_xfcYyVvZDhT6rz5S`)

**FRONT**

Define the **critical region** and the **critical value**.


**BACK**

The **critical region** is the range of values the test statistic could take that would lead to $\text{H}_{0}$ being **rejected**.

The **critical value** is the boundary of that region, the least extreme value that still causes rejection.

Where the region sits is fixed by the significance level, and the test statistic itself is also called the **observed value**.


Spec links: `spcpt_SXgS5mjTMgfKTPsD`


## Card 15 — true_or_false (`fl_9vD5K4NgF3Y7N3Wr`)

**FRONT**

**True or False?**

The critical value lies just outside the critical region.


**BACK**

**False.**

The critical value is **inside** the region: it is the least extreme value that still leads to $\text{H}_{0}$ being rejected.

So if the critical region is $X \leq 3$ then 3 is the critical value, an observed value of 3 rejects $\text{H}_{0}$, and an observed value of 4 does not.


Spec links: `spcpt_SXgS5mjTMgfKTPsD`


## Card 16 — question_and_answer (`fl_Nbb64PWsk9ns5kSy`)

**FRONT**

For a **discrete** distribution, why is the actual significance level usually below the stated one?


**BACK**

Because the critical value has to be one of the whole values the variable can actually take, so the region cannot be trimmed to land on the stated level exactly.

The probability of falling inside it, assuming $\text{H}_{0}$ is true, therefore comes out at or below the level that was asked for.

That probability is the **actual significance level**, and it is the probability of rejecting a null hypothesis that was in fact true.


Spec links: `spcpt_SXgS5mjTMgfKTPsD`


## Card 17 — question_and_answer (`fl_znd8TH438fcqmxy7`)

**FRONT**

In a two-tailed test, what is a one-tail probability compared with?


**BACK**

**Half** the significance level, since the level has to be split between the two tails.

At the 5% level each tail carries 2.5%, so a one-tail probability of 0.02 is significant while one of 0.03 is not.

Testing a single tail against the full 5% would reject $\text{H}_{0}$ twice as readily as the test is meant to.


Spec links: `spcpt_SXgS5mjTMgfKTPsD`


## Card 18 — question_and_answer (`fl_r3xRDzDTx6ckXrVZ`)

**FRONT**

A test is carried out without finding a critical region. What probability do you work out, and what do you compare it with?


**BACK**

The **p-value**: the probability, assuming $\text{H}_{0}$ is true, of getting a value **at least as extreme** as the one observed.

Testing for an increase makes the extreme values the large ones, so you want `\text{P} \left(X \ge \text{observed}\right)`, while testing for a decrease makes them the small ones and you want `\text{P} \left(X \le \text{observed}\right)`.

Reject $\text{H}_{0}$ if that probability is **less than** the significance level.


Spec links: `spcpt_SXgS5mjTMgfKTPsD`


## Card 19 — question_and_answer (`fl_FTwsMZW7T7KTj9kf`)

**FRONT**

How should the conclusion of a hypothesis test be worded?


**BACK**

**In the context of the question**, reusing its own wording, and never as a definite statement.

Rejecting $\text{H}_{0}$ gives **sufficient evidence to suggest** that the alternative hypothesis is true at that significance level.

Failing to reject it gives **insufficient evidence to suggest** the alternative hypothesis, which is not at all the same as having shown the null hypothesis to be true.


Spec links: `spcpt_mPVJHc5CKHN5mQyS`


## Card 20 — true_or_false (`fl_3j8z8fTDryymXzd3`)

**FRONT**

**True or False?**

A hypothesis test carried out perfectly correctly can still reach the wrong conclusion.


**BACK**

**True.**

The test weighs how **probable** one particular sample was, and an unusual sample can point the wrong way through no fault of the method.

That is why a conclusion is written as **evidence** at a stated significance level rather than as proof, and why a different sample might well have given a different outcome.


Spec links: `spcpt_mPVJHc5CKHN5mQyS`


## Card 21 — question_and_answer (`fl_H9yGcxRhKhcWmXYk`)

**FRONT**

A two-tailed test rejects $\text{H}_{0}$. What may the conclusion claim, and what may it not?


**BACK**

It may claim there is evidence that the population parameter has **changed**.

It may **not** say in which direction, so a conclusion that the parameter has increased or decreased is wrong even when the observed value sat in the upper tail.

Only a **one-tailed** test gives evidence about direction, and it can do so because the direction was named in $\text{H}_{1}$ before any data was seen.


Spec links: `spcpt_mPVJHc5CKHN5mQyS`

