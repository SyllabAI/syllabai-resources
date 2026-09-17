# Binomial Series

Course: igcse-further-maths-19 · Section: Series

Source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/flashcards/series/binomial-series/


## Card 1 — question_and_answer (`fl_s684ynCQ79gD4G6t`)

**FRONT**

What is the binomial expansion of `\left(a + b\right)^{n}` for a positive integer $n$?


**BACK**

Every term has the form `\binom{n}{r} a^{n - r} b^{r}`, with $r$ running from $0$ up to $n$:

`\left(a + b\right)^{n} = a^{n} + \binom{n}{1} a^{n - 1} b + \ldots + \binom{n}{r} a^{n - r} b^{r} + \ldots + b^{n}`

The powers of $a$ and $b$ in each term always add up to $n$.


Spec links: `spcpt_3hw656HdGSpfGzT2`


## Card 2 — fill_in_the_blanks (`fl_djHyWTHGypFhbhyT`)

**FRONT**

Complete the formula for the binomial coefficient:

`\binom{n}{r} = \frac{n !}{\_\_\_\_\_\_ \left(n - \_\_\_\_\_\_\right) !}`


**BACK**

The completed formula is:

`\binom{n}{r} = \frac{n !}{r ! \left(n - r\right) !}`

It is also written `{}^{n}\text{C}_{r}`, and $n !$ means $1 \times 2 \times 3 \times \dots \times n$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_3hw656HdGSpfGzT2`


## Card 3 — question_and_answer (`fl_YV3tys3d828frGdp`)

**FRONT**

How many terms does the full expansion of `\left(a + b\right)^{n}` have?


**BACK**

Exactly $n + 1$ of them.

The counter $r$ runs from $0$ to $n$ inclusive, and that is $n + 1$ different values.


Spec links: `spcpt_3hw656HdGSpfGzT2`


## Card 4 — question_and_answer (`fl_rjJYMRQKvrwjDwZQ`)

**FRONT**

How does Pascal's triangle give the binomial coefficients?


**BACK**

Each row begins and ends with $1$, and every other entry is the **sum of the two above it**.

Counting the top row as $n = 0$, row $n$ lists `\binom{n}{0}` through to `\binom{n}{n}`.


Spec links: `spcpt_3hw656HdGSpfGzT2`


## Card 5 — true_or_false (`fl_XP2X75jGwy89J6Sk`)

**FRONT**

**True or False?**

The coefficients in the expansion of `\left(a + b\right)^{n}` read the same forwards and backwards.


**BACK**

**True.**

`\binom{n}{r}` and `\binom{n}{n - r}` are always equal, which is why every row of Pascal's triangle is symmetric.

So `\left(a + b\right)^{5}` has coefficients $1 , 5 , 10 , 10 , 5 , 1$.


Spec links: `spcpt_3hw656HdGSpfGzT2`


## Card 6 — question_and_answer (`fl_rbC4mzwQ62vPZ35J`)

**FRONT**

For `\left(p + q x\right)^{n}`, which term comes first in ascending powers of $x$?


**BACK**

The constant term $p^{n}$, since it contains no $x$ at all.

For **descending** powers you start from the other end instead, with `\left(q x\right)^{n}`.


Spec links: `spcpt_3hw656HdGSpfGzT2`


## Card 7 — question_and_answer (`fl_4FPwgWYqGkfpR9ZB`)

**FRONT**

How do you find just the $x^{2}$ coefficient of `\left(p + q x\right)^{n}`?


**BACK**

Use the general term `\binom{n}{r} a^{n - r} b^{r}` with $a = p$, $b = q x$ and $r = 2$.

Choose $r$ by asking which value makes $b^{r}$ produce the power of $x$ you want, so `\left(p + q x^{2}\right)^{n}` would need $r = 1$.


Spec links: `spcpt_3hw656HdGSpfGzT2`


## Card 8 — question_and_answer (`fl_DNjxc7kFsSshjrfK`)

**FRONT**

Find the first three terms of `\left(3 - 2 x\right)^{5}` in ascending powers of $x$.


**BACK**

Take $a = 3$, $b = - 2 x$ and $n = 5$, then work through $r = 0$, $1$ and $2$.

That gives `243 + 5\left(81\right)\left(- 2 x\right) + 10\left(27\right)\left(4 x^{2}\right) = 243 - 810 x + 1080 x^{2} + \ldots`


Spec links: `spcpt_3hw656HdGSpfGzT2`


## Card 9 — question_and_answer (`fl_KrGKmKvJbb7sWc3h`)

**FRONT**

What does the general binomial expansion allow that the ordinary one does not?


**BACK**

It works for **any rational** $n$, so $n$ may be negative or a fraction rather than only a positive integer.

The price is that the series then runs on for ever instead of stopping, and holds only for certain values of $x$.


Spec links: `spcpt_SgDCdWKMBvfBRt2R`


## Card 10 — fill_in_the_blanks (`fl_gv2nFhDGVPTgx6yK`)

**FRONT**

For $n$ rational, complete the condition under which `\left(1 + x\right)^{n}` expands as an infinite series:

`\left| x \right| < \_\_\_\_\_\_ \text{, that is } \_\_\_\_\_\_ < x < 1`


**BACK**

The completed condition is:

`\left| x \right| < 1 \text{, that is } - 1 < x < 1`

This is called the **interval of convergence**, and outside it the series does not settle down to anything at all.


*Blanks: 0 — answers: ['interval of convergence']*

Spec links: `spcpt_SgDCdWKMBvfBRt2R`

Flags: blank_answer_mismatch


## Card 11 — question_and_answer (`fl_McMfdYWMc6czjjfN`)

**FRONT**

How do you expand `\left(p + q x\right)^{n}` when the formula needs a leading $1$?


**BACK**

Factor out $p$ first, so that `\left(p + q x\right)^{n} = p^{n}\left(1 + \frac{q}{p} x\right)^{n}`.

Expand the bracket with $\frac{q}{p} x$ in place of $x$, then remember to multiply everything by $p^{n}$ at the end.


Spec links: `spcpt_SgDCdWKMBvfBRt2R`


## Card 12 — question_and_answer (`fl_qdj98zC7C5wHq2Jw`)

**FRONT**

How does factoring out $p$ change the interval of convergence?


**BACK**

The condition `\left| x \right| < 1` applies to whatever replaced $x$, so it becomes `\left| \frac{q}{p} x \right| < 1`.

For `\left(1 - \frac{x}{3}\right)^{- \frac{1}{2}}` that works out as `\left| x \right| < 3`, so the interval is $- 3 < x < 3$.


Spec links: `spcpt_SgDCdWKMBvfBRt2R`


## Card 13 — question_and_answer (`fl_H73r9sb8XC5JY3TK`)

**FRONT**

How do you rewrite $\frac{1}{\sqrt{9-3x}}$ so the binomial series can be used?


**BACK**

Use the laws of indices to get `\left(9 - 3 x\right)^{- \frac{1}{2}}`, a bracket raised to a rational power.

A square root is a power of $\frac{1}{2}$, and sitting in a denominator makes that power **negative**.


Spec links: `spcpt_SgDCdWKMBvfBRt2R`


## Card 14 — question_and_answer (`fl_Pb2cFjxxpjz2dd66`)

**FRONT**

Expand $\frac{1}{\sqrt{9-3x}}$ up to the term in $x^{2}$.


**BACK**

Write it as `\frac{1}{3}\left(1 - \frac{x}{3}\right)^{- \frac{1}{2}}`, then expand the bracket using $n = - \frac{1}{2}$.

That gives `\frac{1}{3}\left(1 + \frac{1}{6} x + \frac{1}{24} x^{2} + \ldots\right) = \frac{1}{3} + \frac{1}{18} x + \frac{1}{72} x^{2} + \ldots`


Spec links: `spcpt_SgDCdWKMBvfBRt2R`


## Card 15 — true_or_false (`fl_hZxqqFZJx2YvtHhq`)

**FRONT**

**True or False?**

An infinite binomial expansion is only ever an approximation to the function.


**BACK**

**False.**

Inside the interval of convergence the **complete** infinite series is exactly equal to the function it came from.

What makes an approximation is stopping after a few terms, which is what you actually do in practice.


Spec links: `spcpt_SgDCdWKMBvfBRt2R`


## Card 16 — question_and_answer (`fl_9HZgpRZDyCPPwhDH`)

**FRONT**

How do you find a series expansion for $\frac{1+x}{3+2x}$?


**BACK**

Rewrite it as a **product**, `\left(1 + x\right)\left(3 + 2 x\right)^{- 1}`, and expand the second bracket.

Multiplying that expansion by `\left(1 + x\right)` and collecting terms gives $\frac{1}{3} + \frac{1}{9} x - \frac{2}{27} x^{2} + \dots$


Spec links: `spcpt_mpQWyYQ6pCmyzryn`


## Card 17 — question_and_answer (`fl_6FvYdhQVCBRKhYyy`)

**FRONT**

If you expand `\left(3 + 2 x\right)^{- 1}` as far as $x^{3}$, how far is the product valid?


**BACK**

Only as far as the $x^{3}$ term.

Multiplying out does produce an $x^{4}$ term, but other $x^{4}$ terms were never found, so it is **incomplete** and has to be discarded.


Spec links: `spcpt_mpQWyYQ6pCmyzryn`


## Card 18 — question_and_answer (`fl_JnQ5hSKvS8nCgQcN`)

**FRONT**

How do you choose the value of $x$ when using an expansion to estimate a number?


**BACK**

Set the expression that was expanded equal to the number you want, then solve for $x$.

To estimate $\frac{1}{\sqrt{10}}$ from an expansion of $\frac{1}{\sqrt{9-3x}}$, solve $9 - 3 x = 10$ to get $x = - \frac{1}{3}$.


Spec links: `spcpt_mpQWyYQ6pCmyzryn`


## Card 19 — question_and_answer (`fl_xSTMvXYPQcBT4djn`)

**FRONT**

What makes a binomial approximation more accurate?


**BACK**

Using **more terms**, and having $x$ **closer to zero**.

Higher powers of a small $x$ are tiny, so the first three or four terms already carry nearly all of the value.


Spec links: `spcpt_mpQWyYQ6pCmyzryn`


## Card 20 — question_and_answer (`fl_FVWyvBGXnCqpMqgS`)

**FRONT**

What must you check before substituting a value into a binomial expansion?


**BACK**

That the value lies inside the **interval of convergence** for that particular expansion.

Outside it the series does not converge at all, so the approximation is worthless however many terms you take.


Spec links: `spcpt_mpQWyYQ6pCmyzryn`


## Card 21 — fill_in_the_blanks (`fl_mCjnj5d7hR4x8SgW`)

**FRONT**

Complete the percentage error formula, where $v_{E}$ is the exact value and $v_{A}$ the approximation:

`\text{percentage error} = \left(\frac{\_\_\_\_\_\_ - v_{A}}{\_\_\_\_\_\_}\right) \times 100`


**BACK**

The completed formula is:

`\text{percentage error} = \left(\frac{v_{E} - v_{A}}{v_{E}}\right) \times 100`

The **exact** value has to be the one underneath, and the answer is normally given as a positive number.


*Blanks: 0 — answers: ['exact']*

Spec links: `spcpt_mpQWyYQ6pCmyzryn`

Flags: blank_answer_mismatch


## Card 22 — question_and_answer (`fl_m9gzQ6P8zV5MQCRc`)

**FRONT**

Why is it valid to differentiate or integrate a binomial expansion?


**BACK**

Because the expansion and the function it came from are the **same thing** written two ways, so what is true of one is true of the other.

It turns an awkward function into simple **powers of** $x$, which can be differentiated or integrated term by term.


Spec links: `spcpt_mpQWyYQ6pCmyzryn`


## Card 23 — true_or_false (`fl_w7NfzrZhjgBwxmPh`)

**FRONT**

**True or False?**

When estimating a definite integral, the limits must also lie inside the interval of convergence.


**BACK**

**True.**

Every value of $x$ between the limits is used by the integration, so the whole range has to sit inside the interval.

Checking only the answer, or only one of the two endpoints, is not enough.


Spec links: `spcpt_mpQWyYQ6pCmyzryn`

