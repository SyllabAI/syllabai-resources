# Integration

Course: cie-a-level-maths-20-pure-1 · Section: Integration

Source: https://www.savemyexams.com/a-level/maths/cie/20/pure-1/flashcards/integration/integration/


## Card 1 — keyword_definition (`fl_2589zh8cpRj8KTmJ`)

**FRONT**

Define **integration**.


**BACK**

Integration is the **inverse** process of **differentiation**: it undoes differentiating.

So integrating $\frac{\text{d}y}{\text{d}x}$ takes you back to $y$, and integrating $\text{f} ' ( x )$ takes you back to $\text{f} ( x )$.

This is what the **Fundamental Theorem of Calculus** states.


Spec links: `spcpt_hBBQtQpzy6DFVZ5J`


## Card 2 — question_and_answer (`fl_DXBHvPyw55d8ZSXH`)

**FRONT**

Why do $y = 5 x$, $y = 5 x + 2$ and $y = 5 x - 3$ all have the same derivative?


**BACK**

Differentiating a **constant** term gives **0**, because the graph of a constant is a horizontal line and a horizontal line has gradient 0.

The constant leaves no trace in the derivative, and all three give $\frac{\text{d}y}{\text{d}x} = 5$.

Working backwards from $\frac{\text{d}y}{\text{d}x} = 5$, the most you can say is $y = 5 x + c$.


Spec links: `spcpt_hBBQtQpzy6DFVZ5J`


## Card 3 — keyword_definition (`fl_SxZMsyS3QMgYwYSk`)

**FRONT**

Define **indefinite integration**.


**BACK**

Integration carried out **without limits**, so the result is a function rather than a number.

Because the constant term cannot be recovered, the answer always ends with a **constant of integration**, $+ c$, so that, for example:

`\int 2x\,\text{d}x = x^{2} + c`


Spec links: `spcpt_hBBQtQpzy6DFVZ5J`


## Card 4 — true_or_false (`fl_RZCCPmgwM2hmvTzr`)

**FRONT**

**True or False?**

Differentiating a function and then integrating the result always takes you back to exactly the function you started with.


**BACK**

**False.**

You get the original function back **apart from its constant term**, which the differentiation destroyed.

Differentiating $y = 6 x + 3$ gives $\frac{\text{d}y}{\text{d}x} = 6$, and integrating $6$ gives $6 x + c$; nothing in $\frac{\text{d}y}{\text{d}x}$ records that the constant was $3$.

This is why an indefinite integral always ends with $+ c$.


Spec links: `spcpt_hBBQtQpzy6DFVZ5J`


## Card 5 — fill_in_the_blanks (`fl_JcYzj4GhjM4tYyrR`)

**FRONT**

Complete the notation for integrating $3 x^{2} + 5 x + 4$ with respect to $x$, filling in the missing symbol at each end:

`\_\_\_\_\_\_ \left(3x^{2} + 5x + 4\right) \_\_\_\_\_\_`


**BACK**

The completed integral is:

`\int \left(3x^{2} + 5x + 4\right) \text{d}x`

The **integral sign** and the $\text{d} x$ work as a pair. They say "integrate all of $( \dots )$ with respect to $x$", which is why a function of more than one term is written in **brackets** between them.


*Blanks: 0 — answers: []*

Spec links: `spcpt_hBBQtQpzy6DFVZ5J`

Flags: fitb_no_blank_marker


## Card 6 — question_and_answer (`fl_hj9T2b7hC4N58xRv`)

**FRONT**

In the integral `\int \left(3x^{2} + 5x + 4\right)\text{d}x`, what does the $\text{d} x$ tell you?


**BACK**

That you are integrating with respect to $x$, so $x$ is the variable.

Any other letter in the function being integrated is treated as a **constant**, in the same way as an ordinary number.


Spec links: `spcpt_hBBQtQpzy6DFVZ5J`


## Card 7 — keyword_definition (`fl_DY5BCfp3zvvSrtYW`)

**FRONT**

Define the **integrand**.


**BACK**

The function that is being integrated: everything between the integral sign and the $\text{d} x$.

In `integral open parentheses 4 x cubed minus 7 close parentheses text d end text x` the integrand is $4 x^{3} - 7$.


Spec links: `spcpt_hBBQtQpzy6DFVZ5J`


## Card 8 — fill_in_the_blanks (`fl_KPXNdsZGQPYBD2cc`)

**FRONT**

Complete the rule for integrating a power of $x$, filling in the missing **index** and the missing **denominator**:

`\int x^{n}\,\text{d}x = \frac{x^{\_\_\_\_\_\_}}{\_\_\_\_\_\_} + c`


**BACK**

The completed rule is:

`\int x^{n}\,\text{d}x = \frac{x^{n+1}}{n+1} + c`

In words: **increase the power by 1, then divide by the new power**.


*Blanks: 0 — answers: []*

Spec links: `spcpt_rd5TcbbZnVFFCh7N`

Flags: fitb_no_blank_marker


## Card 9 — question_and_answer (`fl_c767fkHV2VdKqbgw`)

**FRONT**

When integrating, which single power of $x$ can the rule "increase the power by 1 and divide by the new power" not be used on, and why?


**BACK**

$x^{-1}$, which is $\frac{1}{x}$.

Increasing $- 1$ by 1 gives a new power of **0**, and the rule would then divide by 0, which is undefined.

`\int \frac{1}{x}\,\text{d}x` does exist, but it is found a different way, later in the course.


Spec links: `spcpt_rd5TcbbZnVFFCh7N`


## Card 10 — true_or_false (`fl_GDPQpbrwTMSG79bg`)

**FRONT**

**True or False?**

To integrate `3x^{2}\left(2x - 1\right)`, you can integrate $3 x^{2}$ and `\left(2x - 1\right)` separately and then multiply the two answers together.


**BACK**

**False.**

There is no rule that lets you integrate a product one factor at a time. **Expand the brackets first**, then integrate term by term:

`\int 3x^{2}\left(2x - 1\right)\text{d}x = \int \left(6x^{3} - 3x^{2}\right)\text{d}x = \frac{3}{2}x^{4} - x^{3} + c`

Multiplying the separate integrals would give `x^{3}\left(x^{2} - x\right) + c`, which is not the same.


Spec links: `spcpt_rd5TcbbZnVFFCh7N`


## Card 11 — question_and_answer (`fl_sr5p2pgDfhDm52J9`)

**FRONT**

Before you can integrate `\frac{\left(x + 3\right)^{2}}{\sqrt{x}}`, what do you need to do to it?


**BACK**

Rewrite it as a sum of separate powers of $x$, because that is the only form the power rule can be applied to.

Expand the numerator, write $\sqrt{x}$ as $x^{\frac{1}{2}}$, then divide each term separately using the index laws:

`\frac{\left(x + 3\right)^{2}}{\sqrt{x}} = \frac{x^{2} + 6x + 9}{x^{\frac{1}{2}}} = x^{\frac{3}{2}} + 6x^{\frac{1}{2}} + 9x^{-\frac{1}{2}}`


Spec links: `spcpt_rd5TcbbZnVFFCh7N`


## Card 12 — question_and_answer (`fl_KfKvcTsXBBVpKVm3`)

**FRONT**

What is `integral 5   text d end text x`, and why?


**BACK**

$5 x + c$.

A constant is a power of $x$ like any other, since $5 = 5 x^{0}$. Increasing the power by 1 and dividing by the new power gives $\frac{5x^{1}}{1} = 5 x$.


Spec links: `spcpt_rd5TcbbZnVFFCh7N`


## Card 13 — question_and_answer (`fl_KkVxCS7K5w2phfFM`)

**FRONT**

After integrating a gradient function, how do you find the value of the constant of integration?


**BACK**

You need the coordinates of **one point that the curve passes through**.

Substitute them into the integrated equation and solve for $c$. For example, if $y = \frac{3}{2} x^{4} - x^{3} + c$ passes through `\left(2, 6\right)`:

`6 = \frac{3}{2}\left(2\right)^{4} - \left(2\right)^{3} + c \Rightarrow c = -10`


Spec links: `spcpt_K8vvF73Wwzx3844Q`


## Card 14 — question_and_answer (`fl_qTzJ7YPbyF42GpdF`)

**FRONT**

When finding the constant of integration, why must you integrate the gradient function before you substitute the coordinates of a point on the curve?


**BACK**

The coordinates satisfy the equation of the **curve**, not the equation of its gradient function, so there is nothing useful to substitute them into until you have integrated.

The constant $c$ also only appears once you have integrated, so before that there is nothing to find.


Spec links: `spcpt_K8vvF73Wwzx3844Q`


## Card 15 — fill_in_the_blanks (`fl_7BThDwdxzpXBYYcD`)

**FRONT**

Complete the definite integration form of the Fundamental Theorem of Calculus:

`\int_{a}^{b} \text{f}'(x)\,\text{d}x = \_\_\_\_\_\_ - \_\_\_\_\_\_`


**BACK**

The completed statement is:

`\int_{a}^{b} \text{f}'(x)\,\text{d}x = \text{f}(b) - \text{f}(a)`

Integrate, then substitute the **upper** limit and subtract the value at the **lower** limit.


*Blanks: 0 — answers: []*

Spec links: `spcpt_cm95VZDQGBnnfkPv`

Flags: fitb_no_blank_marker


## Card 16 — keyword_definition (`fl_Rk7Zn6w2vZKPDnZp`)

**FRONT**

Define the **limits** of a definite integral.


**BACK**

The two values written on the integral sign, which fix the interval the integration is carried out over.

- the one at the bottom, $a$ in `\int_{a}^{b}`, is the **lower limit**
- the one at the top, $b$, is the **upper limit**


Spec links: `spcpt_cm95VZDQGBnnfkPv`


## Card 17 — question_and_answer (`fl_CWtB7pb86wBWCmFn`)

**FRONT**

Why is there no "$+ c$" in the answer to a definite integral?


**BACK**

Because it cancels out.

The constant appears at both limits, and the two copies are subtracted:

`\left(\text{f}(b) + c\right) - \left(\text{f}(a) + c\right) = \text{f}(b) - \text{f}(a)`


Spec links: `spcpt_cm95VZDQGBnnfkPv`


## Card 18 — true_or_false (`fl_j6TbJFQYtsKNrTnZ`)

**FRONT**

**True or False?**

To evaluate `\int_{1}^{3} 4x^{3}\,\text{d}x`, you substitute 3 and 1 into $4 x^{3}$ and subtract.


**BACK**

**False.**

You must **integrate first**, and substitute the limits into the integrated function:

`\int_{1}^{3} 4x^{3}\,\text{d}x = \left[x^{4}\right]_{1}^{3} = 3^{4} - 1^{4} = 80`

Substituting into $4 x^{3}$ itself would give $108 - 4 = 104$, which is not the value of the integral.


Spec links: `spcpt_cm95VZDQGBnnfkPv`


## Card 19 — question_and_answer (`fl_7cTVSBPPvPp5p4gV`)

**FRONT**

Your calculator evaluates a definite integral as $418 . 666667$. Why might that not be an acceptable answer?


**BACK**

Because it is a **rounded decimal**, and many questions ask for an **exact** value.

Here the exact value is $\frac{1256}{3}$, which only comes out of integrating by hand and substituting the limits.

A calculator value is still worth having as a **check** on your working.


Spec links: `spcpt_cm95VZDQGBnnfkPv`


## Card 20 — question_and_answer (`fl_BxrfzRtRyCvK88Rh`)

**FRONT**

What do the square brackets mean in `\left[\frac{3}{4}x^{4} - 3x^{2}\right]_{2}^{4}`?


**BACK**

That the function has been **integrated** but the limits have not been substituted yet.

The limits are written outside the closing bracket, the lower one at the bottom and the upper one at the top. The next line substitutes them:

`\left(\frac{3}{4}\left(4\right)^{4} - 3\left(4\right)^{2}\right) - \left(\frac{3}{4}\left(2\right)^{4} - 3\left(2\right)^{2}\right)`


Spec links: `spcpt_cm95VZDQGBnnfkPv`


## Card 21 — fill_in_the_blanks (`fl_BzpTStdKrs5tvg56`)

**FRONT**

For a linear bracket, complete the reverse chain rule for integration:

`\int \left(ax + b\right)^{n} \text{d}x = \frac{\left(ax + b\right)^{n + 1}}{n + 1} \times \frac{1}{\_\_\_\_\_\_} + c`


**BACK**

The completed rule is:

`\int \left(ax + b\right)^{n} \text{d}x = \frac{\left(ax + b\right)^{n + 1}}{n + 1} \times \frac{1}{a} + c`

Compared with integrating a plain power of $x$, the extra step is the division by $a$, the coefficient of $x$ inside the bracket.


*Blanks: 0 — answers: []*

Spec links: `spcpt_vwFJKqrJdkHZzdFk`

Flags: fitb_no_blank_marker


## Card 22 — true_or_false (`fl_tg2QyDMQMRFvHWfS`)

**FRONT**

**True or False?**

The reverse chain rule can be used to integrate `\left(x^{2} + 1\right)^{5}`.


**BACK**

**False.**

The method only works when the bracket is **linear**, because then its derivative is a constant that can be divided out.

The derivative of $x^{2} + 1$ is $2 x$, and an integral cannot be divided by a function of $x$.


Spec links: `spcpt_vwFJKqrJdkHZzdFk`


## Card 23 — question_and_answer (`fl_fgCYXGwNFYwRhGdY`)

**FRONT**

How do you begin integrating $\frac{1}{\sqrt{3x-1}}$ with the reverse chain rule?


**BACK**

Rewrite it as a bracket raised to a power, `\left(3x - 1\right)^{- \frac{1}{2}}`.

The rule then applies directly and gives $\frac{2\sqrt{3x-1}}{3} + c$.


Spec links: `spcpt_vwFJKqrJdkHZzdFk`


## Card 24 — question_and_answer (`fl_8NZbMPcnnxYdxxGF`)

**FRONT**

Why can `\left(3x - 1\right)^{- \frac{1}{2}}` not be integrated by expanding the bracket?


**BACK**

Because a negative fractional index gives no finite expansion to write down.

Expanding is only ever an option for a positive whole-number power, and even then it is slow once the power is large.


Spec links: `spcpt_vwFJKqrJdkHZzdFk`


## Card 25 — question_and_answer (`fl_SNqRRw7pd4dTRJrG`)

**FRONT**

In the reverse chain rule, why do you divide by the coefficient of $x$ inside the bracket?


**BACK**

Because differentiating `\left(ax + b\right)^{n + 1}` brings out an extra factor of $a$ from the chain rule.

Dividing by $a$ cancels that factor, so the integration undoes the differentiation exactly.


Spec links: `spcpt_vwFJKqrJdkHZzdFk`


## Card 26 — keyword_definition (`fl_ZYmrDnxkn3q6MxJJ`)

**FRONT**

Define **improper integral**.


**BACK**

A definite integral where at least one limit is either **infinite**, or a value at which the function is **undefined**.

Both `\int_{1}^{\infty} \frac{1}{x^{3}} \text{d}x` and `\int_{0}^{5} \frac{1}{\sqrt[3]{x}} \text{d}x` are improper.


Spec links: `spcpt_y96dW6qr3hvnDpFJ`


## Card 27 — question_and_answer (`fl_JgV4b3WP7sXT78hh`)

**FRONT**

How do you evaluate an integral whose upper limit is $\infty$?


**BACK**

Replace the infinite limit with a letter such as $b$, then integrate as normal and leave the answer in terms of $b$.

Now consider what that expression approaches as $b$ grows without bound, and that value is the integral.


Spec links: `spcpt_y96dW6qr3hvnDpFJ`


## Card 28 — fill_in_the_blanks (`fl_NBH369fqsDqxCxk7`)

**FRONT**

Evaluating `\int_{3}^{b} \frac{1}{2x^{2}} \text{d}x` gives $\frac{1}{6} - \frac{1}{2b}$. Complete the value of the improper integral:

`\int_{3}^{\infty} \frac{1}{2x^{2}} \text{d}x = \_\_\_\_\_\_`


**BACK**

The completed value is:

`\int_{3}^{\infty} \frac{1}{2x^{2}} \text{d}x = \frac{1}{6}`

As $b$ grows without bound $\frac{1}{2b}$ approaches $0$, so all that survives is $\frac{1}{6}$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_y96dW6qr3hvnDpFJ`

Flags: fitb_no_blank_marker


## Card 29 — question_and_answer (`fl_XtY2q8htjJYQVGHt`)

**FRONT**

A definite integral has a lower limit of $0$. Does that automatically make it improper?


**BACK**

No. It depends on whether the function is **defined** at $x = 0$.

`\int_{0}^{3} x^{2} \text{d}x` is perfectly ordinary, but `\int_{0}^{3} \frac{1}{2\sqrt{x}} \text{d}x` is improper, because $\frac{1}{2\sqrt{x}}$ is undefined there.


Spec links: `spcpt_y96dW6qr3hvnDpFJ`


## Card 30 — true_or_false (`fl_c4DhF2NnvPY3MrXJ`)

**FRONT**

**True or False?**

An integral with an infinite limit can still have a finite value.


**BACK**

**True.**

As the upper limit grows, the extra amount added on gets smaller and smaller, so the running total can settle on a finite number rather than growing without end.


Spec links: `spcpt_y96dW6qr3hvnDpFJ`

