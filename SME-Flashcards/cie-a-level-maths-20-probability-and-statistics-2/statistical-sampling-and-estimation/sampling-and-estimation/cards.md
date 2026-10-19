# Sampling & Estimation

Course: cie-a-level-maths-20-probability-and-statistics-2 · Section: Statistical Sampling & Estimation

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/flashcards/statistical-sampling-and-estimation/sampling-and-estimation/


## Card 1 — keyword_definition (`fl_Gk55YvbX33MHhQ3j`)

**FRONT**

Define **unbiased estimate**.


**BACK**

An **unbiased estimate** is one produced by a statistic whose expected value is equal to the population parameter being estimated.

In plainer terms, individual estimates will vary from sample to sample, but the process gives an accurate result **on average**.

So the mean of many such estimates closes in on the true parameter as more samples are taken.


Spec links: `spcpt_fRD8dzP7gVHcXjn6`


## Card 2 — fill_in_the_blanks (`fl_BZfQpWK4x9m87ZRT`)

**FRONT**

Complete the unbiased estimate of a population variance from a sample of size $n$:

`s^{2} = \frac{1}{\_\_\_\_\_\_}\left(\Sigma x^{2} - \frac{\left(\Sigma x\right)^{2}}{n}\right)`


**BACK**

The completed formula is:

`s^{2} = \frac{1}{n - 1}\left(\Sigma x^{2} - \frac{\left(\Sigma x\right)^{2}}{n}\right)`

Notice that the $n$ inside the bracket is still $n$: only the divisor outside it changes.

Getting those two the wrong way round is the commonest slip in the whole calculation.


*Blanks: 0 — answers: []*

Spec links: `spcpt_fRD8dzP7gVHcXjn6`

Flags: fitb_no_blank_marker


## Card 3 — question_and_answer (`fl_gyJKWJxWsNvWrRYm`)

**FRONT**

What is the one difference between the formula for a population variance and the unbiased estimate of it from a sample?


**BACK**

The **divisor**.

A population variance divides by $n$, while the unbiased estimate from a sample divides by $n - 1$; everything else is identical.

So one route to the estimate is to work out the sample's own variance and then multiply it by $\frac{n}{n-1}$.


Spec links: `spcpt_fRD8dzP7gVHcXjn6`


## Card 4 — true_or_false (`fl_8F2tNHDYg2fqD7Fv`)

**FRONT**

**True or False?**

The unbiased estimate of a population mean is just the sample mean.


**BACK**

**True.**

It is exactly the same formula, $\overline{x} = \frac{Σx}{n}$, with no adjustment of any kind.

The mean needs no correction; it is only the variance that does, which is what makes the two cases worth keeping apart in your head.


Spec links: `spcpt_fRD8dzP7gVHcXjn6`


## Card 5 — true_or_false (`fl_PRT6PtFswNKcfd4r`)

**FRONT**

**True or False?**

Square-rooting an unbiased estimate of the variance gives an unbiased estimate of the standard deviation.


**BACK**

**False.**

Square-rooting does not preserve unbiasedness, and there is no formula that gives an unbiased estimate of the standard deviation for every population.

The square root of $s^{2}$ is still a perfectly good estimate and is what you would quote, but it is better to work with the variance wherever you can.


Spec links: `spcpt_fRD8dzP7gVHcXjn6`


## Card 6 — question_and_answer (`fl_G6KqRyCjwpXJWKs7`)

**FRONT**

From $n = 50$, $Σ t = 6174$ and $Σ t^{2} = 831581$, what are the unbiased estimates?


**BACK**

The mean is $\frac{6174}{50} = 123$ minutes to 3 significant figures.

The variance is

`\frac{1}{49}\left(831581 - \frac{6174^{2}}{50}\right) = 1410 \text{ min}^{2}`

Note the units: a variance carries the **square** of the unit of the original data.


Spec links: `spcpt_fRD8dzP7gVHcXjn6`


## Card 7 — question_and_answer (`fl_J5QgdBBzyZN8n4fK`)

**FRONT**

A question gives you the raw data rather than the summary statistics. What is the first thing to do?


**BACK**

Work out $Σ x$ and $Σ x^{2}$ from the data yourself, then use exactly the same formulae.

The formulae are written in terms of those two sums precisely so that raw data and summarised data can be handled the same way.

It is worth writing both sums down before substituting anything, because each is used more than once.


Spec links: `spcpt_fRD8dzP7gVHcXjn6`


## Card 8 — question_and_answer (`fl_zGD5R3wYGj9Vw4cX`)

**FRONT**

What does $\overline{X}$ stand for, and why is it a random variable?


**BACK**

$\overline{X}$ is the mean of a sample of size $n$ taken from a population.

It is a **random variable** because a different sample gives a different value for it, so before the sample is taken its value is unknown.

Its distribution is the distribution of all the values a sample mean could take.


Spec links: `spcpt_c4NPrDp59NSdW45n`


## Card 9 — fill_in_the_blanks (`fl_TsD5r4rmJ7ky9JHS`)

**FRONT**

For a sample of size $n$ from a population with mean $μ$ and variance $σ^{2}$, fill in the two results:

`\text{E}(\bar{X}) = \_\_\_\_\_\_`

`\text{Var}(\bar{X}) = \_\_\_\_\_\_`


**BACK**

The completed results are:

$\text{E} ( \overline{X} ) = μ$

$\text{Var} ( \overline{X} ) = \frac{σ^{2}}{n}$

Averaging does not shift the centre, so the mean is unchanged; what it does is reduce the spread.

The variance is divided by $n$ itself, not by the square root of it.


*Blanks: 0 — answers: []*

Spec links: `spcpt_c4NPrDp59NSdW45n`

Flags: fitb_no_blank_marker


## Card 10 — question_and_answer (`fl_hStNJgwTB6HZSQm6`)

**FRONT**

What is the standard deviation of $\overline{X}$, and what happens to it as $n$ grows?


**BACK**

It is $\frac{σ}{\sqrt{n}}$, so it is inversely proportional to the **square root** of the sample size.

A larger sample therefore makes the distribution of sample means narrower and taller.

The square root is what makes this expensive: quadrupling the sample only halves the spread.


Spec links: `spcpt_c4NPrDp59NSdW45n`


## Card 11 — question_and_answer (`fl_H7yrQCzSMyVtKwrm`)

**FRONT**

If `X \sim \text{N}(30, 25)` and a sample of 10 is taken, what is the distribution of $\overline{X}$?


**BACK**

It is `\bar{X} \sim \text{N}(30, 2.5)`.

The mean stays at 30 and the variance becomes $\frac{25}{10}$.

Because the population is normal, this is **exact**, with no approximation involved anywhere.


Spec links: `spcpt_c4NPrDp59NSdW45n`


## Card 12 — question_and_answer (`fl_thCfr55h6q86bpqC`)

**FRONT**

Why is the mean of a sample a more reliable estimate of $μ$ than a single observation?


**BACK**

Taking a mean dilutes the effect of any one extreme value, since a high reading can be offset by a low one.

The distribution of sample means is correspondingly narrower than the population's, and the larger the sample the narrower it gets.

So a sample mean clusters much more tightly around $μ$ than a single reading ever does.


Spec links: `spcpt_c4NPrDp59NSdW45n`


## Card 13 — keyword_definition (`fl_TsCycFHZd8XNhMcb`)

**FRONT**

Define the **Central Limit Theorem**.


**BACK**

For a random sample of size $n$ from **any** population with mean $μ$ and variance $σ^{2}$, the **Central Limit Theorem** says that $\overline{X}$ can be approximated by `\text{N}\left(\mu, \frac{\sigma^{2}}{n}\right)`, provided $n$ is large enough.

Large enough is usually taken to mean at least 30.

Its power is that it says nothing at all about the shape of the population.


Spec links: `spcpt_9GfWnqSpBjXwDKVj`


## Card 14 — true_or_false (`fl_yJnCnKmtMCT3Wqkv`)

**FRONT**

**True or False?**

If the population is normal, the sample mean is exactly normal however small the sample.


**BACK**

**True.**

A normal population gives an exactly normal distribution of sample means at any sample size, with no approximation at all.

So the Central Limit Theorem is **not needed** here: it is only for populations that are not normal, and then only when the sample is large.


Spec links: `spcpt_9GfWnqSpBjXwDKVj`


## Card 15 — question_and_answer (`fl_ZcScrvqPbrbwfW9D`)

**FRONT**

Susie's 40 numbers come from a population with mean 15 and variance 70. How do you find $\text{P} ( \overline{X} < 13 )$?


**BACK**

The population is not normal, but 40 is a large sample, so the Central Limit Theorem gives `\bar{X} \approx \text{N}\left(15, \frac{70}{40}\right)`.

Standardising 13 against that distribution gives $z = - 1 . 512$.

The probability is then $0 . 0653$, and the answer should say that the Central Limit Theorem was used and why.


Spec links: `spcpt_9GfWnqSpBjXwDKVj`


## Card 16 — keyword_definition (`fl_NNpD9TxRkqypb34B`)

**FRONT**

Define **confidence interval**.


**BACK**

A **confidence interval** is an interval, calculated from a sample, within which a population parameter is likely to lie.

Its **confidence level** is the probability that an interval constructed in that way contains the parameter.

It is the best that can be done when the exact value of a parameter cannot be found from a sample.


Spec links: `spcpt_4rg88C35yg494Krw`


## Card 17 — question_and_answer (`fl_JFtm9jGTxBX9ThVq`)

**FRONT**

Why is it wrong to say there is a 95% probability that $μ$ lies inside a particular confidence interval?


**BACK**

Because $μ$ is a **fixed** number: it either is inside that particular interval or it is not, and there is no probability about it.

The 95% describes the **procedure** instead. If 100 samples were taken and an interval built from each, about 95 of those intervals would contain $μ$.

That is why the wording is always "the interval contains the parameter" rather than the other way round.


Spec links: `spcpt_4rg88C35yg494Krw`


## Card 18 — fill_in_the_blanks (`fl_g27yRrpj6PkdNfwr`)

**FRONT**

Fill in the $z$-values for these three confidence levels:

90%: `z = \_\_\_\_\_\_`

95%: `z = \_\_\_\_\_\_`

99%: `z = \_\_\_\_\_\_`


**BACK**

The completed values are:

90%: $z = 1 . 645$

95%: $z = 1 . 960$

99%: $z = 2 . 576$

They are quoted to three decimal places because $z$ is multiplied by a standard deviation, so an error in it is magnified.

All three appear in the table of critical values, so they need not be memorised, but recognising them is a useful check.


*Blanks: 0 — answers: []*

Spec links: `spcpt_4rg88C35yg494Krw`

Flags: fitb_no_blank_marker


## Card 19 — question_and_answer (`fl_yrMBqpZPkhG3bv8F`)

**FRONT**

For a 90% confidence interval, why do you look up $0 . 95$ rather than $0 . 90$?


**BACK**

The 90% sits in the **middle** of the distribution, so the remaining 10% is shared equally between the two tails, leaving 5% above $z$.

The probability below $z$ is therefore 95%, which is what the table needs.

In general you look up $\frac{α+100}{2}$ per cent for a confidence level of $α$%.


Spec links: `spcpt_4rg88C35yg494Krw`


## Card 20 — question_and_answer (`fl_RgkvjQw6dc3b235N`)

**FRONT**

What two things affect the width of a confidence interval, and in which direction?


**BACK**

A **higher confidence level** makes it wider, because catching the parameter more often requires casting a wider net.

A **larger sample** makes it narrower, because $\frac{σ}{\sqrt{n}}$ shrinks as $n$ grows.

The two pull against each other, which is why more confidence is not simply better.


Spec links: `spcpt_4rg88C35yg494Krw`


## Card 21 — true_or_false (`fl_9WbTrkmWn7HNq2hw`)

**FRONT**

**True or False?**

The sample mean affects both where a confidence interval for $μ$ sits and how wide it is.


**BACK**

**False.**

The sample mean is the **midpoint**, so it fixes where the interval sits, but the width is $2 z \times \frac{σ}{\sqrt{n}}$ and does not contain $\overline{x}$ at all.

An interval for a **proportion** behaves differently: there the sample proportion appears in the width as well as at the centre.


Spec links: `spcpt_4rg88C35yg494Krw`


## Card 22 — question_and_answer (`fl_bk9p4kzzphs2ppZr`)

**FRONT**

A 95% confidence interval for $μ$ is 18.5 to 22.1, and someone claims that $μ = 23$. What can you say?


**BACK**

23 lies **outside** the interval, so there is **not enough evidence to support** the claim.

A value lying inside the interval would be supported by it instead.

The wording matters either way: a confidence interval gives evidence rather than proof, so it never establishes a value or rules one out for certain.


Spec links: `spcpt_4rg88C35yg494Krw`


## Card 23 — question_and_answer (`fl_w8kH55T929tnWbzH`)

**FRONT**

What is the confidence interval for a population proportion?


**BACK**

It is `\hat{p} \pm z \times \sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}`, where `\hat{p}` is the proportion in the sample.

It may only be used when the sample is large enough for the Central Limit Theorem to apply.

The formula booklet gives the distribution of the sample proportion as `\text{N}\left(p, \frac{p(1 - p)}{n}\right)`, which is where the square root comes from.


Spec links: `spcpt_WrdZ9XXxJsS2Jrd3`


## Card 24 — question_and_answer (`fl_7kTPXCzBgd66DT9w`)

**FRONT**

How can a confidence interval for a proportion test whether a coin is fair?


**BACK**

Work out the proportion of heads in a sample and build a confidence interval for the population proportion $p$.

A fair coin would have $p = 0 . 5$, so check whether $0 . 5$ lies inside the interval.

If it lies outside there is evidence the coin is not fair; if it lies inside, there is not enough evidence to say so.


Spec links: `spcpt_WrdZ9XXxJsS2Jrd3`

