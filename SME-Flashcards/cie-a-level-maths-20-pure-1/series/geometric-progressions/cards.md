# Geometric Progressions

Course: cie-a-level-maths-20-pure-1 · Section: Series

Source: https://www.savemyexams.com/a-level/maths/cie/20/pure-1/flashcards/series/geometric-progressions/


## Card 1 — keyword_definition (`fl_K3rrM35wXb7bkxgh`)

**FRONT**

Define **geometric progression**.


**BACK**

A **geometric progression** is a progression in which each term is found by multiplying the previous term by a fixed number.

That fixed number is called the **common ratio**, written $r$.


Spec links: `spcpt_VSNb6zQgMQgcmHQp`


## Card 2 — question_and_answer (`fl_bk4PZHPSKtJVCFFk`)

**FRONT**

In a geometric progression with first term $a$ and common ratio $r$, what is the $n$th term?


**BACK**

The $n$th term is:

$u_{n} = a r^{n-1}$

Here $a$ is the first term and $r$ is the common ratio.


Spec links: `spcpt_VSNb6zQgMQgcmHQp`


## Card 3 — fill_in_the_blanks (`fl_p9ckkQz5rwd4GcZc`)

**FRONT**

A geometric progression has first term $5$ and common ratio $2$. Complete the working for its 7th term, filling in the missing **index** and then the missing value:

`u_{7} = 5 \times 2^{\_\_\_\_\_\_} = \_\_\_\_\_\_`


**BACK**

The completed working is:

$u_{7} = 5 \times 2^{6} = 320$

The first term is already $5$, so reaching the 7th term multiplies by the common ratio only 6 times.


*Blanks: 0 — answers: []*

Spec links: `spcpt_VSNb6zQgMQgcmHQp`

Flags: fitb_no_blank_marker


## Card 4 — true_or_false (`fl_PxzNvKrgw8N99Hm5`)

**FRONT**

**True or False?**

In a geometric progression, a negative common ratio makes the terms alternate between positive and negative.


**BACK**

**True.**

Multiplying by a negative number flips the sign every time: with first term $2$ and common ratio $- 0 . 5$ the progression is $2 ,  - 1 ,  0 . 5 ,  - 0 . 25 ,  \dots$


Spec links: `spcpt_VSNb6zQgMQgcmHQp`


## Card 5 — question_and_answer (`fl_H6YwTTgvjR5sgqtP`)

**FRONT**

The first three terms of a geometric progression are $2 - x$, $3 x$ and $x^{2}$. What equation does being geometric give you?


**BACK**

There is only one common ratio, so the second term divided by the first must equal the third divided by the second:

$\frac{3x}{2-x} = \frac{x^{2}}{3x}$

Cross-multiplying gives `9x^{2} = x^{2}\left(2 - x\right)`, which rearranges to $x^{3} + 7 x^{2} = 0$.


Spec links: `spcpt_VSNb6zQgMQgcmHQp`


## Card 6 — question_and_answer (`fl_qQFgPWxWNMJ3jKKx`)

**FRONT**

You know the 6th term and the 10th term of a geometric progression. Why do you divide one equation by the other rather than subtract?


**BACK**

Because every term is the first term multiplied by a power of the common ratio, so dividing cancels the first term and leaves a single power of $r$, here $r^{4}$.

Subtracting would leave both $a$ and $r$ in the equation, which gets you no closer to either of them.


Spec links: `spcpt_VSNb6zQgMQgcmHQp`


## Card 7 — question_and_answer (`fl_mym7RTNm7CJDM8pt`)

**FRONT**

What are the two formulae for the sum of the first $n$ terms of a geometric progression, and how do you choose between them?


**BACK**

The two forms are:

`S_{n} = \frac{a\left(1 - r^{n}\right)}{1 - r}`   or   `S_{n} = \frac{a\left(r^{n} - 1\right)}{r - 1}`

The first is more convenient when $r < 1$ and the second when $r > 1$, and they give the same answer either way.


Spec links: `spcpt_NHY4TmNTZp5NHCT4`


## Card 8 — question_and_answer (`fl_wXMftp9gHjRwrwsv`)

**FRONT**

In the proof of the geometric series formula, why is the sum multiplied by $r$ and then subtracted from the original?


**BACK**

Because multiplying by $r$ shifts every term along one place, so subtracting makes all the middle terms cancel in pairs.

Only the first term and one extra term at the end survive, which is what leaves a formula containing just $a$, $r$ and $n$.


Spec links: `spcpt_NHY4TmNTZp5NHCT4`


## Card 9 — question_and_answer (`fl_GPVyGHqrS8M9kPSd`)

**FRONT**

A geometric progression has common ratio $0 . 9$, and the sum of its first 5 terms is $409 . 51$. How do you find the first term?


**BACK**

Substitute $r = 0 . 9$ and $n = 5$ into the sum formula, which turns everything apart from $a$ into a single number, $4 . 0951$.

The equation becomes $409 . 51 = 4 . 0951 a$, giving $a = 100$.


Spec links: `spcpt_NHY4TmNTZp5NHCT4`


## Card 10 — fill_in_the_blanks (`fl_kn8pxmnhDj7x2tTx`)

**FRONT**

Complete the formula for the sum to infinity of a geometric progression with first term $a$ and common ratio $r$:

`S_{\infty} = \frac{a}{\_\_\_\_\_\_}`


**BACK**

The completed formula is:

$S_{\infty} = \frac{a}{1-r}$

It is only valid when `|r| < 1`.


*Blanks: 0 — answers: []*

Spec links: `spcpt_NHY4TmNTZp5NHCT4`

Flags: fitb_no_blank_marker


## Card 11 — question_and_answer (`fl_SJDf9vG2bPHP7tzk`)

**FRONT**

Why does a geometric progression only have a sum to infinity when `|r| < 1`?


**BACK**

Because each term is then smaller in size than the one before, so the terms shrink towards zero and the running total settles on a finite value.

If `|r| \ge 1` the terms do not shrink towards zero, so the running total never settles on a single value and the series is said to **diverge**.


Spec links: `spcpt_NHY4TmNTZp5NHCT4`


## Card 12 — true_or_false (`fl_dTKrd58vt8XwXKc6`)

**FRONT**

**True or False?**

The sum to infinity of a geometric progression is always larger than the sum of its first few terms.


**BACK**

**False.**

With a negative common ratio the terms alternate in sign, so a partial sum can overshoot the sum to infinity.

For $a = 2$ and $r = - 0 . 5$ the sum to infinity is $\frac{4}{3}$, but the first term on its own is already $2$.


Spec links: `spcpt_NHY4TmNTZp5NHCT4`

