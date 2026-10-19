# Working with Distributions

Course: cie-a-level-maths-20-probability-and-statistics-1 · Section: Statistical Distributions

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/flashcards/statistical-distributions/working-with-distributions/


## Card 1 — question_and_answer (`fl_5QFtfrTVFfrbBNk7`)

**FRONT**

When choosing a distribution to model something, what is the first question to ask?


**BACK**

Whether the variable **counts** or **measures**.

Counting points to a **discrete** distribution and measuring to a **continuous** one.

That single question rules out two of the three distributions straight away, which is why it is worth asking before anything else.


Spec links: `spcpt_nVvnsMCXrxRzgX4r`


## Card 2 — fill_in_the_blanks (`fl_tj6nD8NFvgjJfmms`)

**FRONT**

Fill in which distribution each description points to:

counts successes in a fixed number of trials: `\_\_\_\_\_\_`

counts trials up to and including the first success: `\_\_\_\_\_\_`

measures something with a symmetrical, bell-shaped spread: `\_\_\_\_\_\_`


**BACK**

The completed matches are:

counts successes in a fixed number of trials: **binomial**

counts trials up to and including the first success: **geometric**

measures something with a symmetrical, bell-shaped spread: **normal**

The two discrete ones differ only in what is fixed and what varies, so the phrase to look for is whether the number of trials is decided in advance.


*Blanks: 0 — answers: []*

Spec links: `spcpt_nVvnsMCXrxRzgX4r`

Flags: fitb_no_blank_marker


## Card 3 — question_and_answer (`fl_3VD6T7Tch3fXjm9y`)

**FRONT**

How can real data tell you whether a normal model is reasonable?


**BACK**

Draw a **histogram** of the data and look at its shape: roughly symmetrical and bell-shaped supports a normal model.

As more data is collected the outline of the histogram should smooth out and come to resemble the normal curve itself.

A histogram that is lopsided, or that has two peaks, is telling you to look elsewhere.


Spec links: `spcpt_nVvnsMCXrxRzgX4r`


## Card 4 — true_or_false (`fl_DXb32rCh3nX7Bfwn`)

**FRONT**

**True or False?**

A variable that counts something can never be modelled by a normal distribution.


**BACK**

**False.**

A count is discrete, so strictly a continuous distribution does not fit it.

But where the count ranges over a great many values, a normal distribution can describe it closely enough to be worth using, which is exactly what a normal approximation does.


Spec links: `spcpt_nVvnsMCXrxRzgX4r`


## Card 5 — question_and_answer (`fl_K5PStYHKDrpKK8BP`)

**FRONT**

Cow masses follow $\text{N} ( 550 , 80^{2} )$ and a cow is "beefy" if it exceeds 700 kg. For 10 cows, how do you find the probability that at most one is beefy?


**BACK**

Use the **normal** distribution first to find the probability that one cow is beefy: $p = \text{P} ( M > 700 ) = 0 . 0303$.

Then use that as the probability of success in a **binomial**, so the number of beefy cows is `X \sim \text{B}(10, 0.0303)`, and find $\text{P} ( X \leq 1 )$.

The normal supplies the parameter and the binomial answers the question.


Spec links: `spcpt_nVvnsMCXrxRzgX4r`


## Card 6 — question_and_answer (`fl_w8N7ptjVpV9f7mw3`)

**FRONT**

In a question using two distributions, why must you state what each variable represents?


**BACK**

Because the two variables measure completely different things: one is a mass in kilograms, the other a count of cows out of 10.

Mixing them up means putting a mass into a binomial or a count into a normal, which is the usual way these questions go wrong.

Writing "let $M$ be the mass of a cow" and "let $X$ be the number of beefy cows" before calculating anything prevents it.


Spec links: `spcpt_nVvnsMCXrxRzgX4r`


## Card 7 — question_and_answer (`fl_Sw6CWWxMZQz9d2mK`)

**FRONT**

Why approximate a binomial by a normal distribution rather than using the binomial formula?


**BACK**

A cumulative binomial probability needs one term for **every** value in the range, so a range spanning dozens of values means dozens of separate calculations.

A normal calculation replaces all of them with a single standardisation and a couple of table lookups.

The pay-off grows with $n$, which is exactly when the binomial becomes unmanageable.


Spec links: `spcpt_BxG2b7KqnDXhkGcJ`


## Card 8 — fill_in_the_blanks (`fl_PRMsrqbDFM5h4FfV`)

**FRONT**

For a normal approximation, $n$ must be large enough that two quantities both exceed 5. Fill them in:

`\_\_\_\_\_\_ > 5`

`\_\_\_\_\_\_ > 5`


**BACK**

The completed conditions are:

$n p > 5$

$n q > 5$

where $q = 1 - p$.

Both are needed because each guards one end: a small $n p$ crowds the distribution against 0 and a small $n q$ crowds it against $n$, and either way it is too lopsided for a symmetrical curve to fit.


*Blanks: 0 — answers: []*

Spec links: `spcpt_BxG2b7KqnDXhkGcJ`

Flags: fitb_no_blank_marker


## Card 9 — question_and_answer (`fl_fRm8vsRSN9vGYVRZ`)

**FRONT**

Which normal distribution approximates `X \sim \text{B}(n, p)`?


**BACK**

The one with the **same mean and the same variance** as the binomial, so

$μ = n p \text{and} σ^{2} = n p ( 1 - p )$

Matching those two quantities is the whole of what makes the approximation work.

Remember that the second of them is the **variance**, so it needs square-rooting before it can be used in a standardisation.


Spec links: `spcpt_BxG2b7KqnDXhkGcJ`


## Card 10 — keyword_definition (`fl_JntXyRGqgVWNHDTk`)

**FRONT**

Define **continuity correction**.


**BACK**

A **continuity correction** is the adjustment made when a **discrete** variable is approximated by a **continuous** one.

Each whole number is widened to the interval reaching half a unit either side of it, since every number in that interval rounds to it.

So $X = 4$ becomes $3 . 5 < X_{N} < 4 . 5$.


Spec links: `spcpt_BxG2b7KqnDXhkGcJ`


## Card 11 — fill_in_the_blanks (`fl_BSKfBK39bzXS77nG`)

**FRONT**

Fill in the continuity correction each inequality needs:

$\text{P} ( X \leq k )$ becomes `\text{P}(X_{N} < \_\_\_\_\_\_)`

$\text{P} ( X < k )$ becomes `\text{P}(X_{N} < \_\_\_\_\_\_)`


**BACK**

The completed corrections are:

$\text{P} ( X \leq k )$ becomes $\text{P} ( X_{N} < k + 0 . 5 )$

$\text{P} ( X < k )$ becomes $\text{P} ( X_{N} < k - 0 . 5 )$

The correction always reaches to the **upper edge of the largest whole number you want to include**.

For $X \leq k$ that largest value is $k$ itself, whose edge is at $k + 0 . 5$; for $X < k$ it is $k - 1$, whose edge is at $k - 0 . 5$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_BxG2b7KqnDXhkGcJ`

Flags: fitb_no_blank_marker


## Card 12 — question_and_answer (`fl_XzcqhT5HJ7ZmVvGP`)

**FRONT**

For `X \sim \text{B}(1250, 0.4)`, how do you approximate $\text{P} ( 485 \leq X \leq 530 )$?


**BACK**

First find the approximating distribution: $μ = 500$ and $σ^{2} = 300$, so use $\text{N} ( 500 , 300 )$.

Both endpoints are included, so the correction widens the range outwards to $484 . 5 \leq X_{N} \leq 530 . 5$.

Standardising both ends and using the table then gives $0 . 776$.


Spec links: `spcpt_BxG2b7KqnDXhkGcJ`


## Card 13 — true_or_false (`fl_MsDYyQwxZ8fpGJw9`)

**FRONT**

**True or False?**

The normal approximation gives a probability to values the binomial says are impossible.


**BACK**

**True.**

The approximating normal distribution is continuous and defined for every real number, so it assigns probability to non-integer values, and to values below 0 or above $n$.

Those probabilities are negligible when $n p$ and $n q$ both exceed 5, which is precisely what those conditions are protecting against.


Spec links: `spcpt_BxG2b7KqnDXhkGcJ`

