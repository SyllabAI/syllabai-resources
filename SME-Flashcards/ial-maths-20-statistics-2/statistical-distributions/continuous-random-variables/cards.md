# Continuous Random Variables

Course: ial-maths-20-statistics-2 · Section: Statistical Distributions

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/flashcards/statistical-distributions/continuous-random-variables/


## Card 1 — keyword_definition (`fl_Kjtn2F4j3P8jnZxW`)

**FRONT**

Define a **probability density function**.


**BACK**

A **probability density function** is a function used to model how probability is spread across the values of a **continuous** random variable.

It is written `\text{f} \left(x\right)` and is usually given **piecewise**, with a rule for each part of the range and 0 everywhere else.

It has to be defined for every real value of $x$, so a complete answer includes the parts where `\text{f} \left(x\right) = 0`.


Spec links: `spcpt_JMz3SfGShXWm8TqR`


## Card 2 — question_and_answer (`fl_PNDY2yhrgMMWTsdZ`)

**FRONT**

What two conditions must a function satisfy before it can be a probability density function?


**BACK**

It can never be **negative**, so `\text{f} \left(x\right) \ge 0` for every value of $x$.

The total **area** under its graph must come to exactly 1:

`\int_{- \infty}^{\infty} \text{f} \left(x\right) \text{d} x = 1`

These are the continuous versions of `\text{P} \left(X = x\right) \ge 0` and `\Sigma \text{P} \left(X = x\right) = 1`, and showing that a given function can represent a p.d.f. means checking both of them.


Spec links: `spcpt_JMz3SfGShXWm8TqR`


## Card 3 — fill_in_the_blanks (`fl_WPbBQSVBkRdt3TtQ`)

**FRONT**

This is one of only two formulae in this module that the formula booklet does not give you. Complete it:

`\text{P} \left(a \le X \le b\right) = \int_{a}^{b} \_\_\_\_\_\_ \text{d} x`


**BACK**

The completed formula is:

`\text{P} \left(a \le X \le b\right) = \int_{a}^{b} \text{f} \left(x\right) \text{d} x`

The integral is the **area** under the graph of `y = \text{f} \left(x\right)` between $a$ and $b$, and for a continuous variable that area is what a probability is.

Since `\text{P} \left(X = n\right) = 0` for every $n$, the endpoints contribute nothing, so `\text{P} \left(a \le X \le b\right)` and `\text{P} \left(a < X < b\right)` come to the same thing.


*Blanks: 0 — answers: ['area']*

Spec links: `spcpt_JMz3SfGShXWm8TqR`

Flags: blank_answer_mismatch


## Card 4 — true_or_false (`fl_JmDs4Y52pV3mMkGg`)

**FRONT**

**True or False?**

The graph of a probability density function must be continuous.


**BACK**

**False.**

It may jump, and it need not start or finish on the horizontal axis: a perfectly good `\text{f} \left(x\right)` can climb to a height of 1 at $x = 1$, drop straight to zero, and start again at $x = 1 . 5$.

What matters is the **area** underneath rather than whether the curve joins up, and a gap in the graph simply means the variable never takes values there.


Spec links: `spcpt_JMz3SfGShXWm8TqR`


## Card 5 — question_and_answer (`fl_FQX6MXpV6MsGSxd5`)

**FRONT**

A p.d.f. is defined piecewise, and the range you want spans two of its pieces. How do you find the probability?


**BACK**

Split the integral at the boundary between the pieces and add the two results together.

If one rule holds on $1 \leq x \leq 2$ and another on $2 \leq x \leq 6$, then `\text{P} \left(1 . 5 \le X \le 2 . 5\right)` means integrating the first rule from 1.5 to 2 and the second from 2 to 2.5.

Using a single rule right across the range is the usual error, and it produces the area under the wrong graph.


Spec links: `spcpt_JMz3SfGShXWm8TqR`


## Card 6 — question_and_answer (`fl_nqCdg2CZqNsWkt5J`)

**FRONT**

You are told that `\text{P} \left(0 \le X \le a\right) = 0 . 09` and asked to find $a$. How do you set that up?


**BACK**

Write down the same integral as usual but with $a$ as the unknown upper limit, then set the result equal to 0.09 and solve.

Integrating leaves an expression in $a$, so what started as a probability question turns into an ordinary equation.

Check at the end that the value you get lies inside the range on which that piece of `\text{f} \left(x\right)` is defined.


Spec links: `spcpt_JMz3SfGShXWm8TqR`


## Card 7 — question_and_answer (`fl_bcvSSqpPdQmpNWBz`)

**FRONT**

What equation does the median $m$ of a continuous random variable satisfy?


**BACK**

The median splits the distribution into two equal halves, so `\text{P} \left(X < m\right) = \text{P} \left(X > m\right) = 0 . 5`, and it is found by solving:

`\int_{- \infty}^{m} \text{f} \left(x\right) \text{d} x = 0 . 5`

Where the graph of `y = \text{f} \left(x\right)` is **symmetrical** the median can be written down without integrating at all, since it sits on the axis of symmetry.

For a piecewise `\text{f} \left(x\right)`, work out which piece the median falls in before deciding what to integrate.


Spec links: `spcpt_yyQVJRMwfJDN5gPx`


## Card 8 — question_and_answer (`fl_TGtvDsKmkJ7Q4W27`)

**FRONT**

For the 15th percentile $k$ of a continuous random variable, do you solve `\text{P} \left(X \le k\right) = 0 . 15` or `\text{P} \left(X \ge k\right) = 0 . 15`?


**BACK**

`\text{P} \left(X \le k\right) = 0 . 15`, because a percentile is fixed by how much of the distribution lies **below** it.

Solving `\text{P} \left(X \ge k\right) = 0 . 15` would leave 85% below $k$, so it gives the **85th** percentile instead.

The quartiles work the same way, with `\text{P} \left(X \le Q_{1}\right) = 0 . 25` for the lower quartile and `\text{P} \left(X \le Q_{3}\right) = 0 . 75` for the upper.


Spec links: `spcpt_yyQVJRMwfJDN5gPx`


## Card 9 — keyword_definition (`fl_h25K4h7gdtVJTNfR`)

**FRONT**

Define the **mode** of a continuous random variable.


**BACK**

The **mode** is the value of $x$ that makes `\text{f} \left(x\right)` as large as possible.

It is the place where the probability density is greatest, which on the graph is the highest point reached by the curve.

Note that the mode is that value of $x$, not the height `\text{f} \left(x\right)` reaches there.


Spec links: `spcpt_yyQVJRMwfJDN5gPx`


## Card 10 — question_and_answer (`fl_FwTcQ6NRGq3y84Jm`)

**FRONT**

The graph of a p.d.f. is a curve with a maximum point inside its range. How do you find the mode?


**BACK**

Differentiate and solve `\text{f}' \left(x\right) = 0`, exactly as you would for any stationary point.

If that gives more than one solution, discard any that fall outside the range on which `\text{f} \left(x\right)` is defined, and use `\text{f}'' \left(x\right)` to decide which of the survivors is a maximum.

The **endpoints** of the range are worth checking too, since the greatest value of `\text{f} \left(x\right)` can occur at one of them without being a stationary point.


Spec links: `spcpt_yyQVJRMwfJDN5gPx`


## Card 11 — question_and_answer (`fl_KGZR7W2mtzSHVTJ9`)

**FRONT**

For a discrete random variable the mean is `\Sigma x \text{P} \left(X = x\right)`. What is the continuous version doing in place of that sum?


**BACK**

The formula booklet gives `\text{E} \left(X\right) = \mu = \int_{- \infty}^{\infty} x \text{f} \left(x\right) \text{d} x`, which weights each value of $x$ by how much probability sits near it.

The integral replaces the sum because a continuous variable has infinitely many possible values, so probability is spread out as a **density** rather than heaped on individual values.

That is why `\text{f} \left(x\right)` stands where `\text{P} \left(X = x\right)` stood, even though `\text{f} \left(x\right)` is not itself a probability.


Spec links: `spcpt_dH2h38ZK6svbtC8J`


## Card 12 — question_and_answer (`fl_WpWwTPs75PDCT6k3`)

**FRONT**

The mean of a continuous random variable is written with limits of $- \infty$ and $\infty$. Why do you almost never integrate between those limits?


**BACK**

Because `\text{f} \left(x\right)` is zero outside the range where the variable actually lives, and a zero integrand contributes nothing.

So for an `\text{f} \left(x\right)` defined on $0 \leq x \leq 2$ and zero elsewhere, the mean is simply `\text{E} \left(X\right) = \int_{0}^{2} x \text{f} \left(x\right) \text{d} x`.

Where `\text{f} \left(x\right)` has several non-zero pieces the integral has to be split across all of them and the results added.


Spec links: `spcpt_dH2h38ZK6svbtC8J`


## Card 13 — question_and_answer (`fl_jwSSg4hc42Hmsncm`)

**FRONT**

The graph of `y = \text{f} \left(x\right)` is symmetrical about $x = 3$. What is `\text{E} \left(X\right)`?


**BACK**

`\text{E} \left(X\right) = 3`, with no integration needed at all.

The mean is the balance point of the distribution, and a symmetrical shape balances on its axis of symmetry.

Looking for symmetry before reaching for the integral saves a great deal of work, and it also gives you a way to check an answer you have integrated for.


Spec links: `spcpt_dH2h38ZK6svbtC8J`


## Card 14 — true_or_false (`fl_4mR3grk6c82yynHk`)

**FRONT**

**True or False?**

For a continuous random variable, `\int_{- \infty}^{\infty} x^{2} \text{f} \left(x\right) \text{d} x` is the variance.


**BACK**

**False.**

That integral is `\text{E} \left(X^{2}\right)`, the **mean of the squares**, and the variance is what is left once the **square of the mean** has been taken away from it:

`\text{Var} \left(X\right) = \text{E} \left(X^{2}\right) - \left[\text{E} \left(X\right)\right]^{2}`

Stopping at the integral is the commonest way to get a variance wrong, and the giveaway is an answer that comes out far too large.


Spec links: `spcpt_dH2h38ZK6svbtC8J`


## Card 15 — question_and_answer (`fl_qwkc2rCbQvXHxWJX`)

**FRONT**

The formula booklet gives `\text{E} \left(\text{g} \left(X\right)\right) = \int_{- \infty}^{\infty} \text{g} \left(x\right) \text{f} \left(x\right) \text{d} x`. What does it let you find?


**BACK**

The expected value of **any** function of $X$, such as `\text{E} \left(X^{2}\right)`, `\text{E} \left(\frac{1}{X}\right)` or `\text{E} \left(\sqrt{X}\right)`.

You multiply that function by `\text{f} \left(x\right)` and integrate, exactly as for the mean but with `\text{g} \left(x\right)` standing where $x$ stood.

What you must **not** do is work out `\text{E} \left(X\right)` and then feed it into $\text{g}$, because the mean of a function is not in general the function of the mean.


Spec links: `spcpt_dH2h38ZK6svbtC8J`


## Card 16 — question_and_answer (`fl_mGr66YxK7Mv5B4fW`)

**FRONT**

What must be found before the variance of a continuous random variable can be calculated?


**BACK**

The **mean**, because $μ^{2}$ appears inside the variance formula.

The variance is not self-contained: whichever form of it you use, `\text{E} \left(X\right)` has to be found and squared before anything can be subtracted.

If a variance comes out negative then the subtraction has gone the wrong way round, since a variance can never be less than zero.


Spec links: `spcpt_dH2h38ZK6svbtC8J`


## Card 17 — keyword_definition (`fl_sXMkYXW5qWDXvssj`)

**FRONT**

Define the **continuous uniform distribution**.


**BACK**

The **continuous uniform distribution**, also called the **rectangular distribution**, is a continuous distribution whose probability density is **constant** over a range $a \leq x \leq b$ and zero everywhere outside it.

Its graph is therefore a rectangle standing on the horizontal axis between $a$ and $b$.

It is one of the two named special cases of a probability density function met on this course, the other being the normal distribution.


Spec links: `spcpt_fpRcGzr3vWBCjwQV`


## Card 18 — question_and_answer (`fl_DRrCz84p5bvcgrgC`)

**FRONT**

A continuous uniform distribution on $a \leq x \leq b$ has a constant probability density. Why must that constant be $\frac{1}{b-a}$?


**BACK**

Because the area under any probability density function has to come to 1, and this one is a rectangle.

Its width is $b - a$, so its height $h$ has to satisfy `h \left(b - a\right) = 1`, which gives $h = \frac{1}{b-a}$.

The height is forced by the width: once you know where the distribution starts and stops, there is no freedom left in it at all.


Spec links: `spcpt_fpRcGzr3vWBCjwQV`


## Card 19 — question_and_answer (`fl_vxQSNFm8cmgDy9GC`)

**FRONT**

$X$ is uniformly distributed on $1 . 5 \leq x \leq 4$. Find `\text{P} \left(2 . 5 \le X \le 3\right)`.


**BACK**

The probability is the area of a rectangle of width $3 - 2 . 5 = 0 . 5$ and height $\frac{1}{4-1.5} = 0 . 4$, so it comes to $0 . 5 \times 0 . 4 = 0 . 2$.

Every probability for a uniform distribution works out this way, so integration is never needed for one.

The same answer can be read straight off as $\frac{0.5}{2.5}$, the part of the range you want divided by the whole range.


Spec links: `spcpt_fpRcGzr3vWBCjwQV`


## Card 20 — question_and_answer (`fl_k3TgNvYxycW48PK4`)

**FRONT**

The formula booklet gives `\text{E} \left(X\right) = \frac{1}{2} \left(a + b\right)` for a continuous uniform distribution. How is that result obtained?


**BACK**

Evaluate the mean integral with the constant density substituted in:

`\text{E} \left(X\right) = \int_{a}^{b} \frac{x}{b - a} \text{d} x = \left[\frac{x^{2}}{2 \left(b - a\right)}\right]_{a}^{b} = \frac{b^{2} - a^{2}}{2 \left(b - a\right)}`

The numerator factorises as `\left(b - a\right) \left(b + a\right)`, so the $b - a$ cancels and what is left is `\frac{1}{2} \left(a + b\right)`.


Spec links: `spcpt_fpRcGzr3vWBCjwQV`


## Card 21 — question_and_answer (`fl_8RH2jMmMvBRm2FtF`)

**FRONT**

How would you obtain the result `\text{Var} \left(X\right) = \frac{1}{12} \left(b - a\right)^{2}` for a continuous uniform distribution?


**BACK**

Start from `\text{Var} \left(X\right) = \text{E} \left(X^{2}\right) - \left[\text{E} \left(X\right)\right]^{2}` and work out the first term:

`\text{E} \left(X^{2}\right) = \int_{a}^{b} \frac{x^{2}}{b - a} \text{d} x = \frac{b^{3} - a^{3}}{3 \left(b - a\right)} = \frac{a^{2} + a b + b^{2}}{3}`

Taking away `\frac{1}{4} \left(a + b\right)^{2}` and putting everything over 12 leaves $\frac{a^{2}-2ab+b^{2}}{12}$, which is exactly `\frac{1}{12} \left(b - a\right)^{2}`.


Spec links: `spcpt_fpRcGzr3vWBCjwQV`


## Card 22 — true_or_false (`fl_PcZKmds5JhpyXhm7`)

**FRONT**

**True or False?**

Doubling the width of the range of a continuous uniform distribution doubles its standard deviation.


**BACK**

**True.**

The variance is `\frac{1}{12} \left(b - a\right)^{2}`, so the standard deviation is $\frac{b-a}{\sqrt{12}}$, which is simply proportional to the width.

The squaring in the variance is what makes this look wrong: the **variance** really is multiplied by 4, but taking the square root undoes that and leaves the spread doubled.


Spec links: `spcpt_fpRcGzr3vWBCjwQV`


## Card 23 — question_and_answer (`fl_Gvc47sNqnVrFydGx`)

**FRONT**

What are the median and the mode of a continuous uniform distribution?


**BACK**

The median is `\frac{1}{2} \left(a + b\right)`, the same as the mean, because the rectangle is symmetrical about its centre.

There is **no mode**: `\text{f} \left(x\right)` takes the same value everywhere between $a$ and $b$, so no single value of $x$ stands out as more likely than any other.

That makes this distribution unusual, since for most continuous distributions the three averages all come out different.


Spec links: `spcpt_fpRcGzr3vWBCjwQV`

