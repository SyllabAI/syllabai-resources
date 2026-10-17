# Further Differentiation

Course: cie-a-level-maths-20-pure-3 · Section: Differentiation

Source: https://www.savemyexams.com/a-level/maths/cie/20/pure-3/flashcards/differentiation/further-differentiation/


## Card 1 — fill_in_the_blanks (`fl_kWDNYkcz7QJh538Z`)

**FRONT**

Complete these standard derivatives:

`\frac{\text{d}}{\text{d} x} \left(\text{e}^{x}\right) = \_\_\_\_\_\_`

`\frac{\text{d}}{\text{d} x} \left(\ln x\right) = \_\_\_\_\_\_`

`\frac{\text{d}}{\text{d} x} \left(\tan x\right) = \_\_\_\_\_\_`


**BACK**

The completed derivatives are:

`\frac{\text{d}}{\text{d} x} \left(\text{e}^{x}\right) = \text{e}^{x}`

`\frac{\text{d}}{\text{d} x} \left(\ln x\right) = \frac{1}{x}`

`\frac{\text{d}}{\text{d} x} \left(\tan x\right) = \sec^{2} x`

The exponential is the only function that is its own derivative.


*Blanks: 0 — answers: []*

Spec links: `spcpt_9M6txgmvBvxkgYb5`

Flags: fitb_no_blank_marker


## Card 2 — question_and_answer (`fl_ngvgWW3vbFr8TTQ8`)

**FRONT**

What are the derivatives of $\mathrm{sin} x$ and $\mathrm{cos} x$?


**BACK**

$\mathrm{sin} x$ differentiates to $\mathrm{cos} x$, and $\mathrm{cos} x$ differentiates to $- \mathrm{sin} x$.

The **minus sign appears on the cosine only**, which is the single most common slip in this pair.


Spec links: `spcpt_9M6txgmvBvxkgYb5`


## Card 3 — question_and_answer (`fl_NTkKfrPQryFTbxR8`)

**FRONT**

How do you differentiate $\text{e}^{kx}$?


**BACK**

The answer is $k \text{e}^{kx}$: the exponential is unchanged and the constant $k$ comes down in front.

That is the chain rule at work, with $k$ being the derivative of the index $k x$.


Spec links: `spcpt_9M6txgmvBvxkgYb5`


## Card 4 — true_or_false (`fl_vp9JTntX5hGRhVJ6`)

**FRONT**

**True or False?**

$\mathrm{ln} x$ and $\mathrm{ln} 5 x$ have the same derivative.


**BACK**

**True.**

Both differentiate to $\frac{1}{x}$, because $\mathrm{ln} 5 x = \mathrm{ln} 5 + \mathrm{ln} x$ and the $\mathrm{ln} 5$ is a constant, which differentiates to zero.

The constant inside the logarithm disappears entirely, which surprises almost everyone the first time.


Spec links: `spcpt_9M6txgmvBvxkgYb5`


## Card 5 — question_and_answer (`fl_2K8tWbmrqdjZVFZB`)

**FRONT**

How can you differentiate $\mathrm{sec} x$ using only the derivative of $\mathrm{cos} x$?


**BACK**

Rewrite it as `\left(\cos x\right)^{- 1}` and apply the chain rule.

That turns a function with no standard derivative of its own into one you already know, and the same rewrite works for $\text{cosec} x$ and $\mathrm{cot} x$.


Spec links: `spcpt_9M6txgmvBvxkgYb5`


## Card 6 — fill_in_the_blanks (`fl_VMJvXJXZs7FDzwpV`)

**FRONT**

Complete the derivatives of the reciprocal trigonometric functions:

`\frac{\text{d}}{\text{d} x} \left(\sec x\right) = \_\_\_\_\_\_`

`\frac{\text{d}}{\text{d} x} \left(\text{cosec} x\right) = \_\_\_\_\_\_`

`\frac{\text{d}}{\text{d} x} \left(\cot x\right) = \_\_\_\_\_\_`


**BACK**

The completed derivatives are:

`\frac{\text{d}}{\text{d} x} \left(\sec x\right) = \sec x \tan x`

`\frac{\text{d}}{\text{d} x} \left(\text{cosec} x\right) = - \text{cosec} x \cot x`

`\frac{\text{d}}{\text{d} x} \left(\cot x\right) = - \text{cosec}^{2} x`

The two beginning with **co** are the two that carry a minus sign.


*Blanks: 0 — answers: []*

Spec links: `spcpt_9M6txgmvBvxkgYb5`

Flags: fitb_no_blank_marker


## Card 7 — fill_in_the_blanks (`fl_7xhNhspGpx9H7hnN`)

**FRONT**

For $y = u v$, where $u$ and $v$ are functions of $x$, complete the product rule:

`\frac{\text{d} y}{\text{d} x} = u \frac{\text{d} v}{\text{d} x} + \_\_\_\_\_\_`


**BACK**

The completed rule is:

$\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$

In the shorter notation that is $y ' = u v ' + v u '$: each function is paired with the **other** one's derivative.


*Blanks: 0 — answers: []*

Spec links: `spcpt_6nDMwtQJ7WfdvgPb`

Flags: fitb_no_blank_marker


## Card 8 — question_and_answer (`fl_F6xPPBFzmq8xcDcf`)

**FRONT**

What is the difference between a product of two functions and a composite function?


**BACK**

A **product** is two functions multiplied together, while a **composite** is one function applied to the output of another.

With `\text{f} \left(x\right) = 3 x^{2}` and `\text{g} \left(x\right) = x - 3`, the product is $3 x^{3} - 9 x^{2}$ but the composite `\text{fg} \left(x\right)` is $3 x^{2} - 18 x + 27$.

Products need this rule; composites need the chain rule.


Spec links: `spcpt_6nDMwtQJ7WfdvgPb`


## Card 9 — true_or_false (`fl_TnyZD2wkcKV5PNtr`)

**FRONT**

**True or False?**

The derivative of a product is the product of the derivatives.


**BACK**

**False.**

Take $y = x \times x = x^{2}$, which differentiates to $2 x$.

Multiplying the separate derivatives would give $1 \times 1 = 1$, which is not the same thing at all.


Spec links: `spcpt_6nDMwtQJ7WfdvgPb`


## Card 10 — question_and_answer (`fl_R2Y2TBg7S6rdQypV`)

**FRONT**

How do you apply the product rule?


**BACK**

Label the two factors $u$ and $v$, differentiate each of them separately, then substitute all four expressions into the rule.

Setting the working out as four short labelled lines before you combine them is what keeps the terms from getting mixed up.


Spec links: `spcpt_6nDMwtQJ7WfdvgPb`


## Card 11 — true_or_false (`fl_tybF2j7VSxQJJ5bY`)

**FRONT**

**True or False?**

It does not matter which factor you call $u$ and which you call $v$.


**BACK**

**True.**

The rule adds its two terms together, and addition can be done in either order, so swapping the labels simply produces the same two terms the other way round.

That is not true of every rule of this kind, so it is worth knowing which ones tolerate it.


Spec links: `spcpt_6nDMwtQJ7WfdvgPb`


## Card 12 — question_and_answer (`fl_2ypTBBgYzVQ8WDZW`)

**FRONT**

What do you do when one factor of a product needs the chain rule?


**BACK**

Differentiate that factor with the chain rule as a separate step, then feed the result into the product rule as usual.

Differentiating `\left(5 \sin x - 7 \cos x\right) \text{e}^{3 x + 2}` needs the chain rule for $\text{e}^{3x+2}$, giving $3 \text{e}^{3x+2}$, before the product rule is applied at all.


Spec links: `spcpt_6nDMwtQJ7WfdvgPb`


## Card 13 — fill_in_the_blanks (`fl_jptRnYsWMs57W3QK`)

**FRONT**

For $y = \frac{u}{v}$, where $u$ and $v$ are functions of $x$, complete the quotient rule:

`\frac{\text{d} y}{\text{d} x} = \frac{v \frac{\text{d} u}{\text{d} x} - u \frac{\text{d} v}{\text{d} x}}{\_\_\_\_\_\_}`


**BACK**

The completed rule is:

$\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$

The denominator is the **bottom function squared**, not the derivative of anything, and the whole formula is given in the formulae booklet.


*Blanks: 0 — answers: []*

Spec links: `spcpt_NMz2QnW3vCFZCZmm`

Flags: fitb_no_blank_marker


## Card 14 — question_and_answer (`fl_C4PttYhHwWNdz3pT`)

**FRONT**

Why does the order of the two terms matter in the quotient rule?


**BACK**

Because of the **minus sign** in the numerator: swapping the terms reverses the sign of the whole answer.

The term beginning with $v$, the bottom function, is the one that comes first.


Spec links: `spcpt_NMz2QnW3vCFZCZmm`


## Card 15 — question_and_answer (`fl_wHmB537rGxM2BZB4`)

**FRONT**

How can you recognise a quotient rule question written as `\text{g} \left(x\right) \left(\text{h} \left(x\right)\right)^{- 1}`?


**BACK**

A negative power applied to a whole function is a division in disguise, since `\text{g} \left(x\right) \left(\text{h} \left(x\right)\right)^{- 1} = \frac{\text{g} \left(x\right)}{\text{h} \left(x\right)}`.

It can be done with the product and chain rules instead, but the quotient rule is usually quicker.


Spec links: `spcpt_NMz2QnW3vCFZCZmm`


## Card 16 — question_and_answer (`fl_PM2n4V9vK6DHCpG2`)

**FRONT**

Differentiate $y = \frac{\mathrm{sin}x}{x}$.


**BACK**

Taking $u = \mathrm{sin} x$ and $v = x$:

$\frac{\text{d}y}{\text{d}x} = \frac{x\mathrm{cos}x-\mathrm{sin}x}{x^{2}}$

Answers from the quotient rule rarely simplify much, so leaving the result as a single fraction is normal.


Spec links: `spcpt_NMz2QnW3vCFZCZmm`


## Card 17 — true_or_false (`fl_fDkNhXDfgMVmbdWD`)

**FRONT**

**True or False?**

Every quotient has to be differentiated using the quotient rule.


**BACK**

**False.**

A quotient that simplifies should be simplified first: $\frac{x^{3}+x}{x}$ is just $x^{2} + 1$, which differentiates in one line.

The rule is for quotients that cannot be reduced to a sum of simpler terms.


Spec links: `spcpt_NMz2QnW3vCFZCZmm`

