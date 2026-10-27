# Normal Distribution

Course: cie-as-maths-20-probability-and-statistics-1 · Section: Statistical Distributions

Source: https://www.savemyexams.com/as/maths/cie/20/probability-and-statistics-1/flashcards/statistical-distributions/normal-distribution/


## Card 1 — keyword_definition (`fl_FMnSD5r9dX52Zqds`)

**FRONT**

Define **continuous random variable**.


**BACK**

A continuous random variable is a random variable that can take **any value within a range**, rather than only certain separate values.

Continuous random variables usually **measure** something, so height, weight and time are all continuous.

That is the contrast with a discrete random variable, which counts, and the difference decides which distributions can model the variable.


Spec links: `spcpt_HS83hxfdbps62xPW`


## Card 2 — question_and_answer (`fl_C6zfJ4YMFMQXynmt`)

**FRONT**

For a continuous distribution, what is `\text{P} \left(X = k\right)`, and what follows from it?


**BACK**

`\text{P} \left(X = k\right) = 0` for **every** value of $k$, because probability is the **area under the graph** and a single value is a line with no width.

What has a probability is a **range** of values: the area between $x = a$ and $x = b$ is `\text{P} \left(a \leq X \leq b\right)`, and the total area under the graph is 1.

What follows is convenient: since the endpoints contribute nothing, strict and weak inequalities give the same answer.

`\text{P} \left(X \leq k\right) = \text{P} \left(X < k\right)`


Spec links: `spcpt_HS83hxfdbps62xPW`


## Card 3 — true_or_false (`fl_2pYwyb7X66NZTHky`)

**FRONT**

**True or False?**

In `X \sim \text{N} \left(\mu , \sigma^{2}\right)`, the second number in the bracket is the standard deviation.


**BACK**

**False.**

The second number is the **variance**, $σ^{2}$: the notation says so, but it is easy to read past.

So `W \sim \text{N} \left(50 , 36\right)` has variance 36 and standard deviation $\sqrt{36} = 6$.

This matters because calculators ask for the **standard deviation**, so entering the second number straight from the bracket is a common error; square root it first, unless the variance is already written as a square, as in `\text{N} \left(20 , 5^{2}\right)`.


Spec links: `spcpt_HS83hxfdbps62xPW`


## Card 4 — question_and_answer (`fl_JMpHWBVrgndTXrfM`)

**FRONT**

A normal distribution is symmetrical about $x = μ$. What two things follow from that?


**BACK**

The three averages all coincide:

$\text{mean} = \text{median} = \text{mode} = μ$

and half the area lies on each side of the mean:

`\text{P} \left(X < \mu\right) = \text{P} \left(X > \mu\right) = 0.5`

The second is worth having ready. It gives you a probability with no calculation, and it is often the quickest way to check that an answer is on the right side of the mean.


Spec links: `spcpt_HS83hxfdbps62xPW`


## Card 5 — fill_in_the_blanks (`fl_j8kfR7fDcS3Q9FR9`)

**FRONT**

Complete the proportions of a normal distribution that lie within one, two and three standard deviations of the mean:

within $μ \pm σ$, about `\_\_\_\_\_\_`% of the data

within $μ \pm 2 σ$, about `\_\_\_\_\_\_`% of the data

within $μ \pm 3 σ$, about `\_\_\_\_\_\_`% of the data


**BACK**

The completed proportions are:

within $μ \pm σ$, about **68**% of the data, which is roughly two thirds

within $μ \pm 2 σ$, about **95**% of the data

within $μ \pm 3 σ$, about **99.7**% of the data, which is nearly all of it

These are worth knowing by heart as a sense check. If a calculation says that 40% of the data lies within one standard deviation of the mean, something has gone wrong.


*Blanks: 0 — answers: []*

Spec links: `spcpt_HS83hxfdbps62xPW`

Flags: fitb_no_blank_marker


## Card 6 — question_and_answer (`fl_4Ydqn3K7q6r5CwGk`)

**FRONT**

Where are the points of inflection on a normal distribution curve?


**BACK**

At $x = μ \pm σ$, exactly **one standard deviation** either side of the mean.

Those are the two places where the curve stops bending one way and starts bending the other, as it changes from falling ever more steeply to falling ever less steeply.

This gives you a way to read $σ$ off a sketch: it is the horizontal distance from the mean to a point of inflection.


Spec links: `spcpt_HS83hxfdbps62xPW`


## Card 7 — question_and_answer (`fl_CNQ3kdnZmwT9JcJ7`)

**FRONT**

How does a normal curve change when $μ$ changes, and how when $σ^{2}$ changes?


**BACK**

Changing $μ$ **translates** the curve horizontally, moving the whole shape along without altering it.

Changing $σ^{2}$ **stretches** it horizontally: a small variance gives a tall curve with a narrow centre, and a large variance a short curve with a wide centre.

The reason a narrower curve has to be taller is that the **total area is always 1**, so squeezing the curve inwards must push it upwards.


Spec links: `spcpt_HS83hxfdbps62xPW`


## Card 8 — question_and_answer (`fl_zw2WMT55nt3c7FSv`)

**FRONT**

What has to be true of a real-life variable before a normal distribution is a sensible model for it?


**BACK**

It must be **continuous**, so it measures something, its distribution must be **symmetrical** and **bell-shaped** with a **single mode**, and the population needs to be large enough.

So, **for example**, a variable produced by a random number generator cannot be modelled this way, because every value is equally likely and it has no mode.

Nor can how long a human lives, because that distribution is not symmetrical.


Spec links: `spcpt_V6WDFPgHhTqd5tyN`


## Card 9 — true_or_false (`fl_djnnK7dnmg5k2z3Z`)

**FRONT**

**True or False?**

A normal distribution cannot model height, because it allows any real value and a height cannot be negative.


**BACK**

**False.**

It is true that a normal distribution is defined for every real number, but values more than about **four standard deviations** from the mean have a probability density of practically zero.

So a normal model of human height puts a negligible probability on the impossible values and describes the realistic ones well, which is what makes it usable for quantities like height and weight that have a natural floor.

A model does not have to be perfect to be useful, only good enough over the range that matters.


Spec links: `spcpt_V6WDFPgHhTqd5tyN`


## Card 10 — keyword_definition (`fl_63B5BvTf2yTHWgZ3`)

**FRONT**

Define the **standard normal distribution**.


**BACK**

The **standard normal distribution** is the normal distribution with mean 0 and standard deviation 1, written `Z \sim \text{N}(0, 1^{2})`.

Its probabilities have been worked out once and printed as a table, which can then be used for **every** normal distribution.

The letter $Z$ is reserved for it, so seeing $Z$ in a question tells you the mean and standard deviation without being told.


Spec links: `spcpt_khQ8s7M7XpHHbF5t`


## Card 11 — fill_in_the_blanks (`fl_V5GTb4nZy4BKZS3f`)

**FRONT**

Complete the formula that converts any normal variable to the standard one:

`Z = \frac{X - \_\_\_\_\_\_}{\_\_\_\_\_\_}`


**BACK**

The completed formula is:

$Z = \frac{X-μ}{σ}$

Subtracting the mean shifts the distribution so that its centre sits at 0, and dividing by the standard deviation rescales it so that its spread is 1.

So standardising is a translation followed by a stretch, and it turns any normal curve into the same one.


*Blanks: 0 — answers: []*

Spec links: `spcpt_khQ8s7M7XpHHbF5t`

Flags: fitb_no_blank_marker


## Card 12 — question_and_answer (`fl_W5FdrZhCKStrVpwd`)

**FRONT**

What does a $z$-value of $1 . 5$ tell you about a data value?


**BACK**

That it lies **one and a half standard deviations above the mean**.

A negative $z$ means the value is below the mean, and $z = 0$ means it sits exactly at the mean.

So a $z$-value is a measure of position expressed in standard deviations rather than in the original units.


Spec links: `spcpt_khQ8s7M7XpHHbF5t`


## Card 13 — true_or_false (`fl_2BvBbdGZGPrqYrcG`)

**FRONT**

**True or False?**

Two students with different marks in different exams can have the same $z$-value.


**BACK**

**True.**

A $z$-value records how far a mark sits from **its own** mean, measured in **its own** standard deviations, so 70 in one exam and 55 in another can standardise to the same value.

That is exactly what makes standardising worth doing: it puts results from different distributions onto one common scale so they can be compared.


Spec links: `spcpt_khQ8s7M7XpHHbF5t`


## Card 14 — question_and_answer (`fl_YKT4cRXsc2pHSHZw`)

**FRONT**

What does $Φ ( z )$ mean?


**BACK**

It is the probability that $Z$ is **less than** $z$, so $Φ ( z ) = \text{P} ( Z < z )$.

This is the function the normal distribution table gives, and the table lists it for values of $z$ from 0 to 3.

Beyond $z = 3$ the remaining probability is small enough to be treated as negligible.


Spec links: `spcpt_khQ8s7M7XpHHbF5t`


## Card 15 — question_and_answer (`fl_fPMYntcmmq8xFM5k`)

**FRONT**

How do you read $Φ ( 1 . 234 )$ from the normal distribution table?


**BACK**

Find where the $1 . 2$ row meets the $3$ column, which gives $Φ ( 1 . 23 ) = 0 . 8907$.

Then use the ADD section to the right of the table for the third decimal place: the ADD 4 entry on that row is 7, meaning $0 . 0007$.

Adding it gives $Φ ( 1 . 234 ) = 0 . 8914$, and the ADD entries are always counted in ten-thousandths.


Spec links: `spcpt_khQ8s7M7XpHHbF5t`


## Card 16 — fill_in_the_blanks (`fl_ZDMYZsnNYDmyTsQ8`)

**FRONT**

The table only gives $Φ ( z )$ for positive $z$. Fill in the other two cases:

`\text{P}(Z > z) = \_\_\_\_\_\_`

`\text{P}(Z > -z) = \_\_\_\_\_\_`


**BACK**

The completed results are:

$\text{P} ( Z > z ) = 1 - Φ ( z )$

$\text{P} ( Z > - z ) = Φ ( z )$

The first uses the total area being 1, and the second uses the curve being symmetrical about 0.

Between them, those two ideas turn the one column of table values into every case you could be asked for.


*Blanks: 0 — answers: []*

Spec links: `spcpt_khQ8s7M7XpHHbF5t`

Flags: fitb_no_blank_marker


## Card 17 — question_and_answer (`fl_sr4npKCkRvnX2My8`)

**FRONT**

How do you find $z$ when $\text{P} ( Z < z ) = 0 . 3$?


**BACK**

The table only lists probabilities of $0 . 5$ and above, so look up $1 - 0 . 3 = 0 . 7$ instead, which gives $0 . 524$.

A probability below $0 . 5$ puts the value to the **left** of the mean, so the answer is the negative of what you looked up: $z = - 0 . 524$.

Writing the minus sign down at the start, before doing the lookup, is what stops it going missing.


Spec links: `spcpt_khQ8s7M7XpHHbF5t`


## Card 18 — question_and_answer (`fl_j3mt2Bj6x2FFX58f`)

**FRONT**

What values can a normally distributed variable take?


**BACK**

**Any real number**, including negative and non-integer values, however unlikely the extremes may be.

That is the contrast with a binomial variable, which can only take whole numbers from 0 to $n$.

It is also why a normal question always concerns a range of values rather than a list of them.


Spec links: `spcpt_G3bwVT83ZxbRTDXc`


## Card 19 — question_and_answer (`fl_swKZhBrVSnTMYrGb`)

**FRONT**

How do you find $\text{P} ( X < a )$ when `X \sim \text{N}(\mu, \sigma^{2})`?


**BACK**

Sketch the curve and shade the region you want, then standardise $a$ into a $z$-value.

Read the corresponding probability from the normal distribution table, and use the sketch to decide whether that is the answer or whether you need 1 minus it.

The sketch is doing real work here: it is what settles the direction, and it costs a few seconds.


Spec links: `spcpt_FQfrWpTYmFd4Q2NS`


## Card 20 — fill_in_the_blanks (`fl_WRqhGdgsBdyFzkYJ`)

**FRONT**

Complete the rule for a normal probability between two values:

`\text{P}(a < X < b) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \_\_\_\_\_\_`


**BACK**

The completed rule is:

`\text{P}(a < X < b) = \Phi\left(\frac{b - \mu}{\sigma}\right) - \Phi\left(\frac{a - \mu}{\sigma}\right)`

You are taking the area up to $b$ and removing the area up to $a$, leaving the strip between them.

Both ends are standardised with the **same** $μ$ and $σ$, and if either $z$ comes out negative you will need the symmetry result before you can look it up.


*Blanks: 0 — answers: []*

Spec links: `spcpt_FQfrWpTYmFd4Q2NS`

Flags: fitb_no_blank_marker


## Card 21 — true_or_false (`fl_JpJjnXwdXvbzW27W`)

**FRONT**

**True or False?**

Standardising changes the probability you are calculating.


**BACK**

**False.**

Standardising is a change of **scale**, not a change of the event: the region under the curve is exactly the same region, measured in different units.

That is precisely why a single table of probabilities is enough for every normal distribution there is.


Spec links: `spcpt_FQfrWpTYmFd4Q2NS`


## Card 22 — question_and_answer (`fl_5Cq3ZT8mGMsXzM4V`)

**FRONT**

For `X \sim \text{N}(20, 5^{2})`, how do you find $\text{P} ( 18 \leq X < 27 )$?


**BACK**

Standardise both ends, which gives $z = - 0 . 4$ and $z = 1 . 4$.

Then take the difference of the two cumulative probabilities:

$Φ ( 1 . 4 ) - Φ ( - 0 . 4 ) = 0 . 9192 - 0 . 3446 = 0 . 5746$

The negative $z$ has to be converted before it can be looked up, which is the step most often rushed.


Spec links: `spcpt_FQfrWpTYmFd4Q2NS`


## Card 23 — question_and_answer (`fl_qHwZj6c4BVqHHPYC`)

**FRONT**

You are told that $\text{P} ( X > a ) = 0 . 7676$ and want to find $a$. What do you do?


**BACK**

Find the $z$-value that gives that probability, then substitute it into $z = \frac{a-μ}{σ}$ and solve for $a$.

Here the probability is above $0 . 5$, so $a$ lies **below** the mean and $z$ is negative.

Finishing with a check that $a$ really is on the expected side of the mean catches a lost minus sign immediately.


Spec links: `spcpt_Gjxd6ZdfXrrzF7TM`


## Card 24 — question_and_answer (`fl_bSFNGRzWH5kZYg8x`)

**FRONT**

You are told that `\text{P}(\mu - a < X < \mu + a) = 80\%`. How do you find $a$?


**BACK**

The remaining 20% is shared **equally** between the two tails by symmetry, so 10% lies above $μ + a$ and therefore `\text{P}(X < \mu + a) = 90\%`.

Look up the $z$-value for $0 . 9$, then use the fact that standardising $μ + a$ gives simply $\frac{a}{σ}$, since the means cancel.

A sketch makes the halving obvious and is much easier than remembering a formula for it.


Spec links: `spcpt_Gjxd6ZdfXrrzF7TM`


## Card 25 — fill_in_the_blanks (`fl_SXFp2dJ9pWSSmRsj`)

**FRONT**

Complete the rearrangement of the standardisation formula that is most useful when a parameter is unknown:

`x = \mu + \_\_\_\_\_\_`


**BACK**

The completed rearrangement is:

$x = μ + σ z$

It says that any value is the mean plus so many standard deviations, which is the same statement as the standardisation formula read the other way round.

This form is the one to use here, because it is **linear** in $μ$ and $σ$ and so gives an equation that is easy to solve or to combine with another.


*Blanks: 0 — answers: []*

Spec links: `spcpt_kPmz4sKBr5fYwwtS`

Flags: fitb_no_blank_marker


## Card 26 — question_and_answer (`fl_2qsPKk6PDHVP7n3k`)

**FRONT**

You know $σ$ and one probability, and want to find $μ$. What do you do?


**BACK**

Find the $z$-value for that probability, then substitute the known $x$, $z$ and $σ$ into $x = μ + σ z$ and solve for $μ$.

One probability is enough because only one parameter is missing, so one equation determines it.

The same works the other way round: knowing $μ$ and one probability gives $σ$.


Spec links: `spcpt_kPmz4sKBr5fYwwtS`


## Card 27 — question_and_answer (`fl_zXBTbg2k476RJkyQ`)

**FRONT**

Both $μ$ and $σ$ are unknown. What must the question give you, and what do you do with it?


**BACK**

**Two** probabilities, each attached to a different value of $x$.

Each one gives a $z$-value and hence one equation in $μ$ and $σ$, and the pair is then solved simultaneously.

Writing both equations in the form $x = μ + σ z$ first is what makes the pair straightforward to handle.


Spec links: `spcpt_kPmz4sKBr5fYwwtS`


## Card 28 — true_or_false (`fl_rCnr936nWD3773mb`)

**FRONT**

**True or False?**

You can work out $σ$ without ever knowing $μ$.


**BACK**

**True.**

Subtracting one of the two equations from the other removes $μ$ altogether, leaving a single equation in $σ$ alone.

So $σ$ comes out first, and $μ$ is recovered afterwards by substituting back, even though neither equation on its own determines either parameter.


Spec links: `spcpt_kPmz4sKBr5fYwwtS`


## Card 29 — question_and_answer (`fl_kwBJm7QNwKhmCm77`)

**FRONT**

When two equations are formed from two probabilities, what is the commonest mistake?


**BACK**

Pairing a $z$-value with the **wrong** $x$.

Each probability belongs to one particular value of $x$, and its $z$-value has to go into the equation for that value and no other.

Labelling them as $z_{1}$ with $x_{1}$ and $z_{2}$ with $x_{2}$ before substituting anything is what prevents it.


Spec links: `spcpt_kPmz4sKBr5fYwwtS`


## Card 30 — question_and_answer (`fl_mnsmbprcdkFMkpH3`)

**FRONT**

Why should a $z$-value be taken to three decimal places in this kind of question?


**BACK**

Because $z$ gets **multiplied by** $σ$ and then added to $μ$, so any error in it is magnified into the final answer.

Three decimal places keeps the result reliable to three significant figures.

That is why the formula booklet carries a separate table of critical values quoted to exactly that accuracy.


Spec links: `spcpt_kPmz4sKBr5fYwwtS`


## Card 31 — question_and_answer (`fl_SXc8p8x5N2rjGxKj`)

**FRONT**

10% of students take under 12 minutes and 5% take over 40 minutes. How do you find $μ$ and $σ$?


**BACK**

The two $z$-values are $- 1 . 282$ and $1 . 645$, one negative because 12 is below the mean and one positive because 40 is above it.

That gives the pair of equations

$- 1 . 282 σ = 12 - μ \text{and} 1 . 645 σ = 40 - μ$

Solving them gives $σ = 9 . 57$ and $μ = 24 . 3$ minutes.


Spec links: `spcpt_kPmz4sKBr5fYwwtS`

