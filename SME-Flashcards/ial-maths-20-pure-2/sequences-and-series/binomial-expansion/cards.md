# Binomial Expansion

Course: ial-maths-20-pure-2 · Section: Sequences & Series

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-2/flashcards/sequences-and-series/binomial-expansion/


## Card 1 — keyword_definition (`fl_pRHkk4bHMCdkQtnd`)

**FRONT**

Define the **binomial coefficient**.


**BACK**

The number multiplying each term when $( a + b )^{n}$ is expanded with $n$ a **positive integer**. It is written in two ways, both of which appear in the formula booklet and in exam papers:

`{}^{n}\text{C}_{r} = \binom{n}{r} = \frac{n!}{r!(n-r)!}`

The $!$ symbol means **factorial**, so $4 ! = 4 \times 3 \times 2 \times 1$.


Spec links: `spcpt_GKtcZwdYPVpT9kGZ`


## Card 2 — question_and_answer (`fl_FX9s8Ds8y9ww2PNp`)

**FRONT**

How many terms does the expansion of $( a + b )^{n}$ have when $n$ is a positive integer?


**BACK**

It has $n + 1$ terms.

The coefficients run from `{}^{n}\text{C}_{0}` up to `{}^{n}\text{C}_{n}`, which is $n + 1$ values, so the expansion is **finite** and stops on its own.

For example $( a + b )^{4}$ has 5 terms.


Spec links: `spcpt_GKtcZwdYPVpT9kGZ`


## Card 3 — fill_in_the_blanks (`fl_5v443nzw6hCmQpVy`)

**FRONT**

Fill in the missing values, where $n$ is a **positive integer**:

`{}^{n}\text{C}_{0} = {}^{n}\text{C}_{n} = \_\_\_\_\_\_`

`{}^{n}\text{C}_{1} = {}^{n}\text{C}_{n-1} = \_\_\_\_\_\_`


**BACK**

The completed results are:

`{}^{n}\text{C}_{0} = {}^{n}\text{C}_{n} = 1`

`{}^{n}\text{C}_{1} = {}^{n}\text{C}_{n-1} = n`

These are worth knowing, because they let you write the **first two and last two** terms of any expansion without touching a calculator.


*Blanks: 0 — answers: ['first two and last two']*

Spec links: `spcpt_GKtcZwdYPVpT9kGZ`

Flags: blank_answer_mismatch


## Card 4 — question_and_answer (`fl_GVgkk2MNVrQNtsXg`)

**FRONT**

In the expansion of `\left(a + b\right)^{n}` with $n$ a **positive integer**, how do the powers of $a$ and $b$ behave from term to term?


**BACK**

The power of $a$ starts at $n$ and **decreases** by 1 each term. The power of $b$ starts at 0 and **increases** by 1.

The two powers always add up to $n$, which is a quick way to check a term is right.


Spec links: `spcpt_GKtcZwdYPVpT9kGZ`


## Card 5 — question_and_answer (`fl_QTPR7C33vyTk8pjh`)

**FRONT**

When is **Pascal's triangle** a good way to get binomial coefficients, and when is it not?


**BACK**

It is useful for **small** values of $n$, where reading a row off is quick.

For larger $n$ it is slow and prone to arithmetic slips, because you have to build every row up to the one you want. Use `{}^{n}\text{C}_{r}` on a calculator instead.


Spec links: `spcpt_GKtcZwdYPVpT9kGZ`


## Card 6 — question_and_answer (`fl_fKMr5nqRmgj87BvM`)

**FRONT**

When expanding $( 3 + 2 x )^{4}$, why must the $2 x$ be kept in brackets?


**BACK**

Because the power applies to the **whole** term, not just the $x$.

$( 2 x )^{3} = 8 x^{3}$, not $2 x^{3}$. Forgetting the brackets loses the factor of $2^{3}$.


Spec links: `spcpt_GKtcZwdYPVpT9kGZ`


## Card 7 — true_or_false (`fl_67wfJmpdsMjK2xqM`)

**FRONT**

**True or False?**

In the expansion of $( 2 - 3 x )^{6}$, all the terms are positive.


**BACK**

**False.**

The signs **alternate**.

Here $b = - 3 x$, so $( - 3 x )^{r}$ is negative whenever $r$ is odd. The expansion is $64 - 576 x + 2160 x^{2} - 4320 x^{3} + \dots$


Spec links: `spcpt_GKtcZwdYPVpT9kGZ`


## Card 8 — question_and_answer (`fl_QGSr6brC8YByZQB3`)

**FRONT**

How do you find the coefficient of a particular power of $x$ without expanding the whole binomial?


**BACK**

Pick out the single term whose power of $b$ gives you the power of $x$ you want, using the fact that the subscript of the coefficient matches the power of $b$.

For the $x^{6}$ term of $( 3 + 2 x )^{8}$ you need $( 2 x )^{6}$, so the term is `{}^{8}\text{C}_{6}(3)^{2}(2x)^{6}`, and the powers still add to 8.


Spec links: `spcpt_GKtcZwdYPVpT9kGZ`


## Card 9 — question_and_answer (`fl_3gX2WyyxpvSF4FDm`)

**FRONT**

What does "in ascending powers of $x$" tell you to do?


**BACK**

Start with the **constant** term, the one in $x^{0}$, and work upwards in powers of $x$.

If only the first few terms are asked for, write $\approx$ rather than $=$, since the expansion you are giving is incomplete.


Spec links: `spcpt_GKtcZwdYPVpT9kGZ`

