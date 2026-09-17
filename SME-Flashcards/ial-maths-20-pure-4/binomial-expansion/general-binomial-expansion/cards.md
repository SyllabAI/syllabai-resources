# General Binomial Expansion

Course: ial-maths-20-pure-4 · Section: Binomial Expansion

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-4/flashcards/binomial-expansion/general-binomial-expansion/


## Card 1 — keyword_definition (`fl_sC23sRtxVR9vWbqZ`)

**FRONT**

Define the **general binomial expansion**.


**BACK**

The **general binomial expansion** is the expansion of `\left(1 + x\right)^{n}` for **any real** $n$, not merely for positive integers.

In practice that means negative and fractional powers, which the ordinary binomial expansion cannot handle.


Spec links: `spcpt_WRV9vk2NPcPg4nms`


## Card 2 — fill_in_the_blanks (`fl_cFyHP5hkpDP8Pkzn`)

**FRONT**

Complete the general binomial expansion:

`\left(1 + x\right)^{n} = 1 + n x + \frac{n \left(n - 1\right)}{2 !} x^{2} + \frac{\_\_\_\_\_\_}{3 !} x^{3} + \ldots`


**BACK**

The completed expansion is:

`\left(1 + x\right)^{n} = 1 + n x + \frac{n \left(n - 1\right)}{2 !} x^{2} + \frac{n \left(n - 1\right) \left(n - 2\right)}{3 !} x^{3} + \ldots`

Each numerator picks up one more factor than the last, each one lower by $1$, and the factorial underneath keeps pace.


*Blanks: 0 — answers: []*

Spec links: `spcpt_WRV9vk2NPcPg4nms`


## Card 3 — true_or_false (`fl_kTMHkC84yRk8hPqJ`)

**FRONT**

**True or False?**

The general binomial expansion of `\left(1 + x\right)^{n}` always has infinitely many terms.


**BACK**

**False.**

When $n$ is a **positive integer** one of the numerator factors becomes zero, so the expansion stops there and is exact.

For any other real value of $n$ it does run on for ever.


Spec links: `spcpt_WRV9vk2NPcPg4nms`


## Card 4 — question_and_answer (`fl_9jYV94rZq2QnhMTm`)

**FRONT**

For which values of $x$ is the expansion of `\left(1 + x\right)^{n}` valid?


**BACK**

Only for `\left| x \right| < 1`, which is another way of writing $- 1 < x < 1$.

This is called the **validity statement**, and outside that range the infinite series does not add up to the original expression at all.


Spec links: `spcpt_WRV9vk2NPcPg4nms`


## Card 5 — question_and_answer (`fl_pNYh5pBCxBCbrmtf`)

**FRONT**

Why does the expansion only work when `\left| x \right| < 1`?


**BACK**

Because a number smaller than $1$ in size gets **smaller still** when raised to a higher power.

That is what makes the terms shrink towards zero, so the series **converges** rather than growing without limit.


Spec links: `spcpt_WRV9vk2NPcPg4nms`


## Card 6 — question_and_answer (`fl_JyNBvbpwqdXS5yVH`)

**FRONT**

How do you expand `\left(1 + b x\right)^{n}`?


**BACK**

Replace every $x$ in the standard expansion by $b x$, watching the sign carefully if $b$ is negative.

The validity condition travels with it and becomes `\left| b x \right| < 1`.


Spec links: `spcpt_WRV9vk2NPcPg4nms`


## Card 7 — question_and_answer (`fl_yCHsfNvgMRjCNHp5`)

**FRONT**

Why is the general expansion written for `\left(1 + x\right)^{n}` rather than `\left(a + b\right)^{n}`?


**BACK**

Because setting $a = 1$ makes every power of $a$ equal to $1$, so all those factors disappear.

What is left is short enough to write down and work with, which the general two-letter form is not.


Spec links: `spcpt_WRV9vk2NPcPg4nms`


## Card 8 — question_and_answer (`fl_5KNF3NNx7bKK6Mgp`)

**FRONT**

The general binomial expansion is written for $( 1 + x )^{n}$.

What is the **first thing you must do** to expand $( a + b x )^{n}$ when $a \neq 1$?


**BACK**

Factorise $a$ out of the bracket, so the term inside becomes 1:

`(a+bx)^{n} = \left[a\left(1+\frac{b}{a}x\right)\right]^{n} = a^{n}\left(1+\frac{b}{a}x\right)^{n}`

The $a^{n}$ stays outside as a multiplier, and you expand the bracket.


Spec links: `spcpt_f9PhGNgtDD7ss4X9`


## Card 9 — fill_in_the_blanks (`fl_CwhjxzwKKT34RpBY`)

**FRONT**

Fill in the missing **index**:

`\frac{1}{\sqrt[3]{8-3x}} = (8-3x)^{\_\_\_\_\_\_}`


**BACK**

The completed expression is:

`\frac{1}{\sqrt[3]{8-3x}} = (8-3x)^{-\frac{1}{3}}`

A **root** becomes a fractional power, and moving the bracket **out of the denominator** makes that power negative.


*Blanks: 0 — answers: ['root', 'out of the denominator']*

Spec links: `spcpt_f9PhGNgtDD7ss4X9`

Flags: blank_answer_mismatch


## Card 10 — question_and_answer (`fl_kqpJqS4M8W8QzGCH`)

**FRONT**

Why must `\left(a + b x\right)^{n}` be rewritten in the form `\left(1 + \frac{b}{a} x\right)^{n}` before the general binomial expansion can be used?


**BACK**

The expansion in the formula booklet is only given for $( 1 + x )^{n}$, with a **1** as the first term in the bracket.

Once the bracket is in that form you can read the expansion straight off the booklet and replace $x$ with $\frac{b}{a} x$.


Spec links: `spcpt_f9PhGNgtDD7ss4X9`


## Card 11 — question_and_answer (`fl_bJDPwszjHwdH2HGn`)

**FRONT**

What is the range of validity of the expansion of $( a + b x )^{n}$?


**BACK**

`open vertical bar b over a x close vertical bar less than 1`, which rearranges to `vertical line x vertical line less than open vertical bar a over b close vertical bar`.

It comes from the bracket after factorising, not from the original expression. For `left parenthesis 8 minus 3 x right parenthesis to the power of negative 1 third end exponent equals 8 to the power of negative 1 third end exponent open parentheses 1 minus 3 over 8 x close parentheses to the power of negative 1 third end exponent` it gives `vertical line x vertical line less than 8 over 3`.


Spec links: `spcpt_f9PhGNgtDD7ss4X9`


## Card 12 — true_or_false (`fl_CMgSPt3JNM7XRfgX`)

**FRONT**

**True or False?**

The expansions of $( 3 + 2 x )^{-4}$ and $( 1 + 2 x )^{-4}$ are valid for the same values of $x$.


**BACK**

**False.**

The range of validity depends on $\frac{b}{a}$, so changing $a$ changes it.

`left parenthesis 3 plus 2 x right parenthesis to the power of negative 4 end exponent equals 3 to the power of negative 4 end exponent open parentheses 1 plus 2 over 3 x close parentheses to the power of negative 4 end exponent` is valid for `vertical line x vertical line less than 3 over 2`, while $(1+2x)^{-4}$ is valid for `vertical line x vertical line less than 1 half`.


Spec links: `spcpt_f9PhGNgtDD7ss4X9`


## Card 13 — question_and_answer (`fl_b8FSvTjbrdsCFB76`)

**FRONT**

How do you expand an expression containing **more than one** binomial, such as $\frac{\sqrt{1+x}}{3+2x}$?


**BACK**

Break it into separate binomials, here $(1+x)^{\frac{1}{2}}$ and $( 3 + 2 x )^{-1}$.

Expand each one **individually**, then multiply the expansions together and collect like terms.


Spec links: `spcpt_NTrg5qZWvkW2Qvvk`


## Card 14 — true_or_false (`fl_7NWdsQfFC9YNr4vg`)

**FRONT**

**True or False?**

To multiply two binomial expansions together up to the term in $x^{2}$, you must multiply out every pair of terms.


**BACK**

**False.**

Any product whose powers add to more than 2 can be **ignored**, since it only affects terms you are not keeping.

So you only need the pairs that give $x^{0}$, $x^{1}$ and $x^{2}$, which saves a great deal of work.


Spec links: `spcpt_NTrg5qZWvkW2Qvvk`


## Card 15 — question_and_answer (`fl_m2Y2B9FWYv2BkR2f`)

**FRONT**

When expanding an expression that contains more than one binomial, how far must each one be expanded if the final answer is needed up to the term in $x^{3}$?


**BACK**

As far as the term in $x^{3}$ in **each** expansion.

A term in $x^{3}$ in the final answer can come from $1 \times x^{3}$ as well as from $x \times x^{2}$, so stopping any earlier would lose part of it.


Spec links: `spcpt_NTrg5qZWvkW2Qvvk`


## Card 16 — fill_in_the_blanks (`fl_vxY4h5MPB3Bh3CWZ`)

**FRONT**

Expanding $\frac{\sqrt{1+x}}{3+2x}$ uses $(1+x)^{\frac{1}{2}}$, valid for `vertical line x vertical line less than 1`, and $(3+2x)^{-1}$, valid for `vertical line x vertical line less than 3 over 2`.

The whole expansion is valid for `\_\_\_\_\_\_`


**BACK**

The whole expansion is valid for `|x| < 1`.

Both expansions have to be valid at the same time, so the overall range of validity is the **intersection** of the two: the **smaller** boundary wins.


*Blanks: 1 — answers: ['intersection', 'smaller']*

Spec links: `spcpt_NTrg5qZWvkW2Qvvk`

Flags: blank_answer_mismatch


## Card 17 — question_and_answer (`fl_kyHv7TV6thr8DQDq`)

**FRONT**

What lets you apply the general binomial expansion to a rational function such as $\frac{9x+10}{(x+4)(3x-1)}$?


**BACK**

Splitting it into **partial fractions** first:

$\frac{9x+10}{(x+4)(3x-1)} = \frac{2}{x+4} + \frac{3}{3x-1}$

Each partial fraction can then be written as a negative power, $2 ( x + 4 )^{-1} + 3 ( 3 x - 1 )^{-1}$, and expanded.


Spec links: `spcpt_NTrg5qZWvkW2Qvvk`


## Card 18 — question_and_answer (`fl_hnJ4rwwDGv49yPsm`)

**FRONT**

How do you prepare $3 ( 3 x - 1 )^{-1}$ for a binomial expansion, when the constant term is $- 1$?


**BACK**

Factorise the $- 1$ out of the bracket so the constant term becomes $+ 1$:

`3(-1+3x)^{-1} = 3\left[(-1)(1-3x)\right]^{-1} = -3(1-3x)^{-1}`

The $-1$ leaves the bracket raised to the power $n$, here $(-1)^{-1}=-1$.


Spec links: `spcpt_NTrg5qZWvkW2Qvvk`


## Card 19 — question_and_answer (`fl_NbzxtV6vgbZRXdNq`)

**FRONT**

How do you use a binomial expansion to **approximate** a numerical value?


**BACK**

Compare the number you want with the expression that was expanded, solve for $x$, then substitute that $x$ into the expansion.

To approximate `\sqrt[4]{85}` from `\sqrt[4]{81-9x}`, solve $81 - 9 x = 85$ to get $x=-\frac{4}{9}$, and put that into the expansion.


Spec links: `spcpt_sgyKrvgcrwm34Pkz`


## Card 20 — question_and_answer (`fl_jChhrbScXmXFJBrW`)

**FRONT**

What makes a binomial approximation more accurate?


**BACK**

Using **more terms** of the expansion. Each extra term brings the value closer to the true one.

Terms up to $x^{2}$ or $x^{3}$ are usually accurate enough.


Spec links: `spcpt_sgyKrvgcrwm34Pkz`


## Card 21 — question_and_answer (`fl_SD5QBCnxM3Rd9B64`)

**FRONT**

Before using a value of $x$ in a binomial approximation, what must you check about it?


**BACK**

That it lies inside the **range of validity** of the expansion.

`\sqrt[4]{81-9x}` is only valid for `|x| < 9`, so `\sqrt[4]{171}`, which needs $x = - 10$, **cannot** be approximated from it.

Exam questions often hide a validity check inside an approximation question.


Spec links: `spcpt_sgyKrvgcrwm34Pkz`


## Card 22 — true_or_false (`fl_N7CdpXrQB2yJwRqs`)

**FRONT**

**True or False?**

If the value of $x$ you need lies outside the range of validity of a binomial expansion, using more terms will still give a good approximation.


**BACK**

**False.**

Outside the range of validity the series does **not** converge, so extra terms do not settle towards the true value, they make things worse.

The expansion cannot be used for that value at all.


Spec links: `spcpt_sgyKrvgcrwm34Pkz`


## Card 23 — fill_in_the_blanks (`fl_GrDqbGkV7gcvFj6W`)

**FRONT**

Fill in the missing values so a binomial expansion can be used to approximate $\sqrt{710}$:

`\sqrt{710} = \sqrt{\_\_\_\_\_\_ \times 7.1} = \_\_\_\_\_\_\sqrt{7.1}`


**BACK**

The completed working is:

$\sqrt{710} = \sqrt{100\times7.1} = 10 \sqrt{7.1}$

Taking out a **perfect square** leaves a much smaller number, which an expansion can reach.


*Blanks: 0 — answers: ['perfect square']*

Spec links: `spcpt_sgyKrvgcrwm34Pkz`

Flags: blank_answer_mismatch


## Card 24 — question_and_answer (`fl_SwW44ppQw2Kz4FMP`)

**FRONT**

Two expansions can both approximate the same value, one needing $x=0.04$ and the other $x=0.8$.

Which gives the better approximation?


**BACK**

The one using $x = 0 . 04$.

The terms left out are powers of $x$, and those shrink far faster when $x$ is small. A value of $x$ near the edge of the range of validity gives a poor approximation even though the expansion is still valid.


Spec links: `spcpt_sgyKrvgcrwm34Pkz`

