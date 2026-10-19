# Normal Distribution

Course: ial-maths-20-statistics-1 · Section: Statistical Distributions

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-1/flashcards/statistical-distributions/normal-distribution/


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


*Blanks: 0 — answers: ['68', '95', '99.7']*

Spec links: `spcpt_HS83hxfdbps62xPW`

Flags: blank_answer_mismatch


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


## Card 10 — keyword_definition (`fl_4nZPp93xztPxc5hG`)

**FRONT**

Define the **standard normal distribution**.


**BACK**

The standard normal distribution is the normal distribution with **mean 0** and **standard deviation 1**, written `Z \sim \text{N} \left(0 , 1^{2}\right)`.

It is always denoted by the letter $Z$.

It matters because its probabilities are the ones tabulated in the formula booklet.


Spec links: `spcpt_gmwKSJM4VXDr4T7d`


## Card 11 — question_and_answer (`fl_PC5gttPHTRG8rQXz`)

**FRONT**

Why is every normal distribution converted to $Z$ before its probabilities are found?


**BACK**

Because the normal probability density function is too complicated to integrate, so the areas under it have to be worked out **numerically** and looked up rather than calculated.

Tabulating every possible pair of $μ$ and $σ$ would be impossible, so **one** table is produced for the standard normal distribution and every other normal distribution is mapped onto it.


Spec links: `spcpt_gmwKSJM4VXDr4T7d`


## Card 12 — fill_in_the_blanks (`fl_sDhssp9FnZTvvxHD`)

**FRONT**

Complete the formula that maps any normal distribution onto the standard normal distribution:

`Z = \frac{X - \_\_\_\_\_\_}{\_\_\_\_\_\_}`


**BACK**

The completed formula is:

$Z = \frac{X-μ}{σ}$

Subtracting the mean **translates** the curve so that its centre sits at 0, and dividing by the standard deviation **stretches** it so that its spread becomes 1.

This one is not in the formula booklet: it is on the list of formulae you are expected to know.


*Blanks: 0 — answers: ['translates', 'stretches']*

Spec links: `spcpt_gmwKSJM4VXDr4T7d`

Flags: blank_answer_mismatch


## Card 13 — question_and_answer (`fl_BTg3Fsf6ZpR67pVY`)

**FRONT**

What does a $z$-value of $- 1$ tell you about the original value of $X$?


**BACK**

That $X$ lies exactly **one standard deviation below the mean**.

A $z$-value measures how many standard deviations a value sits away from the mean, so $z = 2$ would put it two above.

The sign carries the direction, so any value below the mean has a **negative** $z$-value.


Spec links: `spcpt_gmwKSJM4VXDr4T7d`


## Card 14 — true_or_false (`fl_HSmVfMvD9Tggcw8k`)

**FRONT**

**True or False?**

A mark of 70 in one exam and a mark of 65 in another can be compared fairly by turning each into a $z$-value.


**BACK**

**True.**

Standardising expresses each mark as the number of standard deviations it lies from its own exam's mean, which puts the two on the same scale.

So 70 with $z = 0 . 8$ is the **worse** performance of the two if 65 came out at $z = 1 . 4$, even though the raw mark is higher.


Spec links: `spcpt_gmwKSJM4VXDr4T7d`


## Card 15 — question_and_answer (`fl_dmjHkv5SzJ2gMjkX`)

**FRONT**

What does `\Phi \left(z\right)` stand for, and what does the table in the formula booklet give you?


**BACK**

`\Phi \left(z\right)` is `\text{P} \left(Z < z\right)`, the probability that the standard normal variable takes a value **below** $z$.

The table lists `\Phi \left(z\right)` to four decimal places for $z$ running from 0 up to 4, so you find your $z$ and read the probability beside it.

Above $z = 4$ the remaining probability is small enough to count as negligible, which is why the table stops there.


Spec links: `spcpt_gmwKSJM4VXDr4T7d`


## Card 16 — question_and_answer (`fl_n89fhvZfFCdRW24y`)

**FRONT**

The table only gives `\Phi \left(z\right)` for **positive** $z$. How do you find `\text{P} \left(Z < - 1 . 5\right)`?


**BACK**

Use the symmetry of the curve, `\Phi \left(- z\right) = 1 - \Phi \left(z\right)`, so `\text{P} \left(Z < - 1 . 5\right) = 1 - \Phi \left(1 . 5\right)`.

The area below $- 1 . 5$ is the mirror image of the area above $1 . 5$, and that area is whatever is left when `\Phi \left(1 . 5\right)` is taken from the total area of 1.

The same symmetry gives `\text{P} \left(Z > - z\right) = \Phi \left(z\right)`.


Spec links: `spcpt_gmwKSJM4VXDr4T7d`


## Card 17 — question_and_answer (`fl_YbPXry8TpKKh3kDs`)

**FRONT**

You need `\Phi \left(3 . 14\right)`, but $3 . 14$ is not one of the values listed in the table. What do you do?


**BACK**

Use the **closest** value that is listed, which here is $z = 3 . 15$.

Where the value you want sits exactly between two listed ones, as $2 . 25$ does between $2 . 24$ and $2 . 26$, either neighbour may be used.

Interpolating between the table's entries is **not** required at this level.


Spec links: `spcpt_gmwKSJM4VXDr4T7d`


## Card 18 — question_and_answer (`fl_wRJw2gBB9tw3CpQX`)

**FRONT**

The formula booklet holds a second normal table, of critical values. What does it give, and when is it the quicker one to use?


**BACK**

It gives the value of $z$ for which `\text{P} \left(Z > z\right) = p`, to four decimal places, for a short list of common probabilities: $0 . 5 , 0 . 4 , 0 . 3 , 0 . 2 , 0 . 15 , 0 . 1 , 0 . 05 , 0 . 025 , 0 . 01 , 0 . 005 , 0 . 001$ and $0 . 0005$.

It is quicker whenever a question uses one of those round percentages, because it runs straight from the probability to $z$ instead of making you hunt through the main table for a probability.


Spec links: `spcpt_gmwKSJM4VXDr4T7d`


## Card 19 — question_and_answer (`fl_FwJdtZB24QNzbHbY`)

**FRONT**

`X \sim \text{N} \left(20 , 5^{2}\right)`. How do you find `\text{P} \left(X < 22\right)` from the tables?


**BACK**

**Standardise** the boundary value and look the result up: `\text{P} \left(X < 22\right) = \text{P} \left(Z < \frac{22 - 20}{5}\right) = \Phi \left(0 . 4\right)`.

Every normal probability starts this way, by turning the $x$ into a $z$ before the table can be used at all.

Sketch the curve first and shade the area you want, so you can see whether the answer ought to come out above or below 0.5.


Spec links: `spcpt_j6mhY3GsmrfJcws5`


## Card 20 — question_and_answer (`fl_2ZwVnbVJWgT7vB67`)

**FRONT**

How do you find `\text{P} \left(X > a\right)` once you have standardised $a$?


**BACK**

Subtract from 1, giving `\text{P} \left(X > a\right) = 1 - \Phi \left(\frac{a - \mu}{\sigma}\right)`.

The table only ever gives the area to the **left** of a value, and the total area under the whole curve is 1, so whatever is not to the left must be to the right.


Spec links: `spcpt_j6mhY3GsmrfJcws5`


## Card 21 — fill_in_the_blanks (`fl_BXKZ2RGtfCHbgqmM`)

**FRONT**

Complete the rule for the probability that a normal variable lies between two values:

`\text{P} \left(a < X < b\right) = \Phi \left(\_\_\_\_\_\_\right) - \Phi \left(\_\_\_\_\_\_\right)`


**BACK**

The completed rule is:

`\text{P} \left(a < X < b\right) = \Phi \left(\frac{b - \mu}{\sigma}\right) - \Phi \left(\frac{a - \mu}{\sigma}\right)`

Each $Φ$ is the area to the **left** of one end, so taking one from the other leaves exactly the strip in between.

Subtracting them the wrong way round gives a negative probability, which is the quickest sign that something has slipped.


*Blanks: 0 — answers: ['left']*

Spec links: `spcpt_j6mhY3GsmrfJcws5`

Flags: blank_answer_mismatch


## Card 22 — question_and_answer (`fl_tVx8GWvBYpj55BY7`)

**FRONT**

You are told that `\text{P} \left(X < a\right) = 0 . 7` for a normal distribution with known $μ$ and $σ$. How do you find $a$?


**BACK**

Work backwards through the table: search the body of it for the probability $0 . 7$ and read off the $z$-value beside it.

Then substitute into $z = \frac{a-μ}{σ}$ and solve for $a$.

This is the reverse of finding a probability, so the table is being read from the inside out rather than from the edge in.


Spec links: `spcpt_GyGBcHPyjz7RJsv9`


## Card 23 — question_and_answer (`fl_zYYJw9gDc2HFPNts`)

**FRONT**

You are told that `\text{P} \left(X < a\right) = 0 . 2`. Before touching the tables, what can you already say about $a$ and about $z$?


**BACK**

That $a$ lies **below the mean**, so its $z$-value will be **negative**.

Only 0.2 of the distribution lies below $a$, and a full half of it lies below the mean, so $a$ must be on the low side of the mean.

Since the table only holds probabilities from 0.5 upwards, subtract 0.2 from 1, look up 0.8, and then make the $z$-value negative.


Spec links: `spcpt_GyGBcHPyjz7RJsv9`


## Card 24 — question_and_answer (`fl_YvT4Q6Wd9HMhXjWt`)

**FRONT**

You are told that `\text{P} \left(\mu - a < X < \mu + a\right) = 90 \%`. How do you find $a$?


**BACK**

Split the remaining 10% symmetrically, so 5% lies beyond each end and `\text{P} \left(X < \mu + a\right) = 95 \%`.

Look up $0 . 95$ to get the $z$-value, then use `z = \frac{\left(\mu + a\right) - \mu}{\sigma} = \frac{a}{\sigma}`, which rearranges to $a = σ z$.

The mean cancels out completely, which is why this case can be solved without knowing what $μ$ is.


Spec links: `spcpt_GyGBcHPyjz7RJsv9`


## Card 25 — question_and_answer (`fl_TsvDXZkCkdPywWvz`)

**FRONT**

What is the first thing to do when a question gives you a probability and asks for an unknown $μ$ or $σ$?


**BACK**

**Sketch the normal curve**, marking on it the mean and the value you have been given, and shade the area the probability describes.

The sketch is what tells you whether the $z$-value you are about to look up comes out positive or negative, which is the step most often got wrong.

It also shows at a glance whether the given value should end up above or below the mean, which checks the final answer.


Spec links: `spcpt_7dZQhQhG2scX7Drv`


## Card 26 — question_and_answer (`fl_gTZtb3b5tgMnZ83s`)

**FRONT**

$σ$ is known, $μ$ is unknown, and you are given one probability. Which form of the standardising formula is the useful one here?


**BACK**

The rearranged form $x = μ + σ z$, because it is already solved for $x$ and leaves a **linear** equation in the unknown parameter.

Find $z$ from the given probability using the table, substitute the known $x$ and $σ$, then solve for $μ$.

It is the same relationship as $z = \frac{x-μ}{σ}$, written the other way round.


Spec links: `spcpt_7dZQhQhG2scX7Drv`


## Card 27 — true_or_false (`fl_pNF2vM26dytc2YGY`)

**FRONT**

**True or False?**

One given probability is enough to find both $μ$ and $σ$.


**BACK**

**False.**

Two unknowns need two equations, and each probability supplies only one of them.

A question that leaves both unknown always gives a **second** probability attached to a second value of $x$, so that two equations of the form $x = μ + σ z$ can be solved simultaneously.


Spec links: `spcpt_7dZQhQhG2scX7Drv`


## Card 28 — question_and_answer (`fl_wgSw222Jp2TSpNw8`)

**FRONT**

10% of students take less than 12 minutes over lunch and 5% take more than 40 minutes. What two equations would you solve?


**BACK**

From the first, $12 = μ + σ z_{1}$ where `\text{P} \left(Z < z_{1}\right) = 0 . 1`, and $z_{1}$ is **negative** because 12 sits below the mean.

From the second, $40 = μ + σ z_{2}$ where `\text{P} \left(Z > z_{2}\right) = 0 . 05`, and $z_{2}$ is **positive** because only 5% lies above 40.

Solving the pair simultaneously gives $μ$ and $σ$, and the two $z$-values coming out with opposite signs is the check that the setup is right.


Spec links: `spcpt_7dZQhQhG2scX7Drv`


## Card 29 — question_and_answer (`fl_CYn4t2WH5K66D82Q`)

**FRONT**

Why must the $z$-value be carried to four decimal places when finding $μ$ or $σ$?


**BACK**

Because $z$ gets multiplied by $σ$ on the way to the answer, so any error in it is magnified rather than absorbed.

Rounding $z$ early can shift the final value of $μ$ or $σ$ far enough to change its third significant figure.

That is exactly why the tables give $z$ to four decimal places in the first place.


Spec links: `spcpt_7dZQhQhG2scX7Drv`


## Card 30 — question_and_answer (`fl_tGPTMpQC96JBYhF4`)

**FRONT**

Your working gives $σ = - 4 . 2$ for a normal distribution. What has gone wrong?


**BACK**

A standard deviation can never be **negative**, so a sign has been mishandled somewhere in the working.

The usual culprit is a $z$-value given the wrong sign, since a $z$ that should have been negative turns the whole rearrangement around.


Spec links: `spcpt_7dZQhQhG2scX7Drv`

