# Binomial Theorem

Course: cie-igcse-further-maths-additional-maths-25 · Section: Sequences & Series

Source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/flashcards/sequences-and-series/binomial-theorem/


## Card 1 — fill_in_the_blanks (`fl_jjjvH7rBwffzhBqj`)

**FRONT**

Complete the start of the binomial theorem, for positive integer $n$:

`(a+b)^{n} = a^{n} + \binom{n}{1}\_\_\_\_\_\_\,b + \binom{n}{2}a^{n-2}\_\_\_\_\_\_ + \ldots`


**BACK**

The completed expansion begins:

`(a+b)^{n} = a^{n} + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^{2} + \ldots`

The power of $a$ falls by one each time while the power of $b$ rises by one.


*Blanks: 0 — answers: []*

Spec links: `spcpt_pwBvmphGXzWcW2xh`

Flags: fitb_no_blank_marker


## Card 2 — question_and_answer (`fl_ZdCMXmVtxSTrT7wg`)

**FRONT**

How is Pascal's triangle built?


**BACK**

Every row starts and ends with 1, and each number in between is the **sum of the two above it**.

The first row is a single 1, and each new row is one entry longer than the last.


Spec links: `spcpt_pwBvmphGXzWcW2xh`


## Card 3 — question_and_answer (`fl_YP9smKVTmqFVGN9V`)

**FRONT**

How does Pascal's triangle relate to the binomial coefficients?


**BACK**

Row $n$ of the triangle lists the values of `\binom{n}{r}`, counting the top row as row 0 and the first entry of each row as $r = 0$.

It is a quick way to get coefficients for small $n$ without a calculator, but slow and error-prone once $n$ grows.


Spec links: `spcpt_pwBvmphGXzWcW2xh`


## Card 4 — fill_in_the_blanks (`fl_6qts6QgFkWVcPrJK`)

**FRONT**

Complete the general term of the expansion of $( a + b )^{n}$ by filling in the two missing **powers**:

`\binom{n}{r}a^{\_\_\_\_\_\_}b^{\_\_\_\_\_\_}`


**BACK**

The completed general term is:

`\binom{n}{r}a^{n-r}b^{r}`

This single expression is what you use when a question wants one particular term rather than the whole expansion.


*Blanks: 0 — answers: []*

Spec links: `spcpt_pwBvmphGXzWcW2xh`

Flags: fitb_no_blank_marker


## Card 5 — true_or_false (`fl_GG4p3wBMJWWTjFty`)

**FRONT**

**True or False?**

In every term of the expansion of $( a + b )^{n}$, the powers of $a$ and $b$ add up to $n$.


**BACK**

**True.**

The general term is `\binom{n}{r}a^{n-r}b^{r}`, and $( n - r ) + r = n$ whatever $r$ is.

This makes a quick check on any expansion: if the powers in a term do not total $n$, something has gone wrong.


Spec links: `spcpt_pwBvmphGXzWcW2xh`


## Card 6 — question_and_answer (`fl_3WxMhMzbzfmN2hq7`)

**FRONT**

To find the coefficient of $x^{r}$ in $( a + b x )^{n}$, how do you know which value of $r$ to use?


**BACK**

The $x$ sits only in the second bracket term, so the term `\binom{n}{r}a^{n-r}(bx)^{r}` carries exactly $x^{r}$.

When the bracket contains $x^{2}$ or $\frac{1}{x}$ instead, work out the power of $x$ the general term produces and set it equal to the one you want.


Spec links: `spcpt_pwBvmphGXzWcW2xh`


## Card 7 — question_and_answer (`fl_NwQBPPf5wgYXdKzT`)

**FRONT**

What is the difference between ascending and descending powers of $x$?


**BACK**

**Ascending** starts with the constant term $a^{n}$ and works up through increasing powers of $x$.

**Descending** starts at the other end, with the highest power of $x$, so the same terms are simply written in reverse.


Spec links: `spcpt_Rzg2QGvB2x64zyTp`


## Card 8 — question_and_answer (`fl_MgcWD2cYYbZpc43X`)

**FRONT**

Find the first three terms of $( 3 - 2 x )^{5}$ in ascending powers of $x$.


**BACK**

Take $a = 3$ and $b = - 2 x$, keeping the negative sign inside the bracket:

`3^{5} + \binom{5}{1}3^{4}(-2x) + \binom{5}{2}3^{3}(-2x)^{2}`

This simplifies to $243 - 810 x + 1080 x^{2} + \dots$, where the third term is positive because $( - 2 x )^{2}$ is.


Spec links: `spcpt_Rzg2QGvB2x64zyTp`


## Card 9 — question_and_answer (`fl_FqWzHdk4ZZdCb3jq`)

**FRONT**

In the expansion of `\left(3x + \frac{2}{x}\right)^{8}`, which term is the constant one?


**BACK**

The general term contains $x^{8-r} \times x^{-r}$, which is $x^{8-2r}$.

A constant term needs $8 - 2 r = 0$, so it is the term with $r = 4$.


Spec links: `spcpt_Rzg2QGvB2x64zyTp`

