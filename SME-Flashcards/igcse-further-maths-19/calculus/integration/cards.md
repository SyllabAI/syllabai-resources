# Integration

Course: igcse-further-maths-19 · Section: Calculus

Source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/flashcards/calculus/integration/


## Card 1 — question_and_answer (`fl_7p42N2rp3w5DzvKw`)

**FRONT**

What is integration?


**BACK**

It is the **inverse** operation to differentiation.

If you differentiate a function and then integrate the result, you arrive back at the function you started with, apart from an unknown constant.


Spec links: `spcpt_3j8Wx3b65DYtPnyQ`


## Card 2 — question_and_answer (`fl_QgzJn6yzBkj35vPN`)

**FRONT**

What does the notation `\int \ldots \text{d}x` mean?


**BACK**

It means the integral, with respect to $x$, of whatever sits between the integral sign and the $\text{d} x$.

The $\text{d} x$ is not decoration: it names the variable you are integrating with respect to.


Spec links: `spcpt_3j8Wx3b65DYtPnyQ`


## Card 3 — question_and_answer (`fl_HJChKcYtPzG7YhYR`)

**FRONT**

What is the difference between an indefinite and a definite integral?


**BACK**

The answer to an **indefinite** integral is another **function**, and it carries a constant of integration.

The answer to a **definite** integral is a **number**, so no constant appears in it.


Spec links: `spcpt_3j8Wx3b65DYtPnyQ`


## Card 4 — question_and_answer (`fl_gKsbnqXZPzmBhs43`)

**FRONT**

Given that the derivative of $x^{3} + \frac{1}{x}$ is $3 x^{2} - \frac{1}{x^{2}}$, write down `\int \left(3 x^{2} - \frac{1}{x^{2}}\right) \text{d}x`.


**BACK**

It is $x^{3} + \frac{1}{x} + c$.

No integrating is needed: the two operations are inverses, so the answer can be read straight off the derivative given.

The constant of integration still has to be written in.


Spec links: `spcpt_3j8Wx3b65DYtPnyQ`


## Card 5 — true_or_false (`fl_CrS9scKtPQ3kg8Xw`)

**FRONT**

**True or False?**

Differentiating the answer to `\int \text{f}'\left(x\right) \text{d}x` gives `\text{f}'\left(x\right)`.


**BACK**

**True.**

The integral comes to `\text{f}\left(x\right) + c`, and differentiating that returns `\text{f}'\left(x\right)` once more.

This is what makes it possible to check any integration by differentiating the answer.


Spec links: `spcpt_3j8Wx3b65DYtPnyQ`


## Card 6 — fill_in_the_blanks (`fl_JghgFK7MxH2QDwSP`)

**FRONT**

Complete the rule for integrating a power of $x$:

`\int x^{n} \text{d}x = \frac{x^{\_\_\_\_\_\_}}{\_\_\_\_\_\_} + c`


**BACK**

The completed rule is:

`\int x^{n} \text{d}x = \frac{x^{n + 1}}{n + 1} + c`

Raise the power by one and divide by the new power, which is exactly the reverse of differentiating.


*Blanks: 0 — answers: []*

Spec links: `spcpt_fhGBfgdfw9WmZGPc`


## Card 7 — question_and_answer (`fl_Fby8Szzdp3npMZ8R`)

**FRONT**

For which value of $n$ does the rule for integrating $x^{n}$ fail?


**BACK**

At $n = - 1$, because raising the power by one gives $0$ and the rule would divide by zero.

So `\int \frac{1}{x} \text{d}x` cannot be found this way, and it is not required on this course.


Spec links: `spcpt_fhGBfgdfw9WmZGPc`


## Card 8 — question_and_answer (`fl_mkBzDgMqHBRW76q9`)

**FRONT**

What is `\int a \text{d}x`?


**BACK**

It is $a x + c$.

A constant is $a x^{0}$, so the same rule applies: raising the power by one turns it into $a x^{1}$.


Spec links: `spcpt_fhGBfgdfw9WmZGPc`


## Card 9 — question_and_answer (`fl_BrPFQStD8dNh8h6k`)

**FRONT**

How do you integrate $\sqrt{x}$ and $\frac{1}{x^{2}}$?


**BACK**

Rewrite each as a power of $x$ first, as $x^{\frac{1}{2}}$ and $x^{-2}$.

The rule then gives $\frac{2}{3} x^{\frac{3}{2}} + c$ and $- x^{-1} + c$, the second of which is $- \frac{1}{x} + c$.


Spec links: `spcpt_fhGBfgdfw9WmZGPc`


## Card 10 — question_and_answer (`fl_3rVDpGh49GfhYgYC`)

**FRONT**

Why can `8 x^{2}\left(2 x - 3\right)` not be integrated as it stands?


**BACK**

Because there is no rule for integrating a product, and multiplying the two separate integrals together does **not** work.

Expand it to $16 x^{3} - 24 x^{2}$ first, and then integrate term by term.


Spec links: `spcpt_fhGBfgdfw9WmZGPc`


## Card 11 — fill_in_the_blanks (`fl_yX7pXpCQSKjJvBd7`)

**FRONT**

Complete the two trigonometric integrals:

`\int \sin a x \text{d}x = \_\_\_\_\_\_ \cos a x + c \text{ and } \int \cos a x \text{d}x = \_\_\_\_\_\_ \sin a x + c`


**BACK**

The completed integrals are:

`\int \sin a x \text{d}x = - \frac{1}{a} \cos a x + c \text{ and } \int \cos a x \text{d}x = \frac{1}{a} \sin a x + c`

Both pick up a factor of $\frac{1}{a}$, and this time the minus sign belongs to $\mathrm{sin}$, the other way round from differentiating.


*Blanks: 0 — answers: []*

Spec links: `spcpt_3RJndX5xhQSKbn6K`


## Card 12 — question_and_answer (`fl_CD7KcVfQFf5bHG8Q`)

**FRONT**

Given `\text{f}'\left(x\right) = 4\cos 3 x - \frac{1}{2}\sin 2 x`, find `\text{f}\left(x\right)`.


**BACK**

Integrating term by term gives `4\left(\frac{1}{3}\sin 3 x\right) - \frac{1}{2}\left(- \frac{1}{2}\cos 2 x\right) + c`.

That simplifies to `\text{f}\left(x\right) = \frac{4}{3}\sin 3 x + \frac{1}{4}\cos 2 x + c`, where the two minus signs have cancelled.


Spec links: `spcpt_3RJndX5xhQSKbn6K`


## Card 13 — true_or_false (`fl_d8g6kBMgqtrY3kym`)

**FRONT**

**True or False?**

Integrating $\mathrm{sin} 2 x$ gives $- \mathrm{cos} 2 x + c$.


**BACK**

**False.**

The factor of $\frac{1}{a}$ has been left out, so the correct integral is $- \frac{1}{2} \mathrm{cos} 2 x + c$.

Differentiating $- \mathrm{cos} 2 x$ gives $2 \mathrm{sin} 2 x$ rather than $\mathrm{sin} 2 x$, which shows the answer is wrong.


Spec links: `spcpt_3RJndX5xhQSKbn6K`


## Card 14 — fill_in_the_blanks (`fl_vW6r45CgsjCMwMtq`)

**FRONT**

Complete the integral of the exponential function:

`\int \text{e}^{a x} \text{d}x = \_\_\_\_\_\_ \text{e}^{\_\_\_\_\_\_} + c`


**BACK**

The completed integral is:

`\int \text{e}^{a x} \text{d}x = \frac{1}{a} \text{e}^{a x} + c`

The exponential is unchanged and picks up a factor of $\frac{1}{a}$, where differentiating would have multiplied by $a$ instead.


*Blanks: 0 — answers: []*

Spec links: `spcpt_D2njzcMRRFh4dvQn`


## Card 15 — question_and_answer (`fl_q3CBVrVjGcMtyJyp`)

**FRONT**

Given `\text{f}'\left(x\right) = \frac{\text{e}^{2 x} - \text{e}^{- 3 x}}{2}`, find `\text{f}\left(x\right)`.


**BACK**

Split the fraction first, so the integrand is $\frac{1}{2} \text{e}^{2x} - \frac{1}{2} \text{e}^{-3x}$.

Integrating gives `\frac{1}{2}\left(\frac{1}{2}\text{e}^{2 x}\right) - \frac{1}{2}\left(- \frac{1}{3}\text{e}^{- 3 x}\right) + c = \frac{1}{4}\text{e}^{2 x} + \frac{1}{6}\text{e}^{- 3 x} + c`.


Spec links: `spcpt_D2njzcMRRFh4dvQn`


## Card 16 — question_and_answer (`fl_HPVQdVXV39Dx9BGs`)

**FRONT**

Why does an indefinite integral need a constant of integration?


**BACK**

Because the derivative of any constant is zero, so many different functions share one derivative.

Each of $x^{3} - 5 x$, $x^{3} - 5 x + 7$ and $x^{3} - 5 x - 498$ differentiates to $3 x^{2} - 5$, and integrating cannot tell you which one you started from.


Spec links: `spcpt_Q2yPvWmbP3hFp5kM`


## Card 17 — question_and_answer (`fl_CSSB6PXtPhmrTSTG`)

**FRONT**

What do different values of $c$ look like on a graph?


**BACK**

They are **vertical translations** of the same curve.

The answer to an indefinite integral is therefore a whole family of identically shaped curves, stacked above and below one another.


Spec links: `spcpt_Q2yPvWmbP3hFp5kM`


## Card 18 — question_and_answer (`fl_6zbpyH24ntP3QX54`)

**FRONT**

What extra information do you need to find the value of $c$?


**BACK**

The value of the function at one value of $x$.

That is usually given as a point the graph passes through, but it may equally be given in words, and either way you substitute and solve for $c$.


Spec links: `spcpt_Q2yPvWmbP3hFp5kM`


## Card 19 — question_and_answer (`fl_nrMjcYFfxp8kHt8Z`)

**FRONT**

The graph of `y = \text{f}\left(x\right)` passes through `\left(3 , - 4\right)` and `\text{f}'\left(x\right) = 3 x^{2} - 4 x - 4`; find `\text{f}\left(x\right)`.


**BACK**

Integrating gives `\text{f}\left(x\right) = x^{3} - 2 x^{2} - 4 x + c`.

Substituting the point, $27 - 18 - 12 + c = - 4$, so $c = - 1$.

Therefore `\text{f}\left(x\right) = x^{3} - 2 x^{2} - 4 x - 1`.


Spec links: `spcpt_Q2yPvWmbP3hFp5kM`


## Card 20 — true_or_false (`fl_dpvWZtTm9Z5FWGh4`)

**FRONT**

**True or False?**

You need two points on the curve to find the constant of integration.


**BACK**

**False.**

One is enough, because integrating has already fixed everything except $c$, leaving a single unknown.

That is unlike finding the equation of a straight line, where two points are needed to get both the gradient and the intercept.


Spec links: `spcpt_Q2yPvWmbP3hFp5kM`

