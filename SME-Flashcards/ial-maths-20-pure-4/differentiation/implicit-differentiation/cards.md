# Implicit Differentiation

Course: ial-maths-20-pure-4 · Section: Differentiation

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-4/flashcards/differentiation/implicit-differentiation/


## Card 1 — keyword_definition (`fl_VGDgxnXvrbF4BHdK`)

**FRONT**

What does it mean to differentiate an equation **implicitly**?


**BACK**

Differentiating both sides with respect to $x$ without first rearranging the equation into the form `y = \text{f} \left(x\right)`.

It is used whenever writing $y$ explicitly in terms of $x$ would be awkward or impossible, as for $x^{2} + y^{2} = 25$.


Spec links: `spcpt_pYT5j4mkfqgGVyG8`


## Card 2 — fill_in_the_blanks (`fl_pzRX39B8d7YVP8dC`)

**FRONT**

Complete the rule for differentiating a function of $y$ with respect to $x$:

`\frac{\text{d}}{\text{d} x} \left(\text{f} \left(y\right)\right) = \text{f} ' \left(y\right) \times \_\_\_\_\_\_`


**BACK**

The completed rule is:

`\frac{\text{d}}{\text{d} x} \left(\text{f} \left(y\right)\right) = \text{f} ' \left(y\right) \frac{\text{d} y}{\text{d} x}`

This is the **chain rule**: $y$ is itself a function of $x$, so differentiating anything built from $y$ brings out a factor of $\frac{\text{d}y}{\text{d}x}$.


*Blanks: 0 — answers: ['chain rule']*

Spec links: `spcpt_pYT5j4mkfqgGVyG8`

Flags: blank_answer_mismatch


## Card 3 — question_and_answer (`fl_fJQrBjZB7PDHg5jx`)

**FRONT**

What is `\frac{\text{d}}{\text{d} x} \left(y^{3}\right)`?


**BACK**

$3 y^{2} \frac{\text{d}y}{\text{d}x}$.

Differentiate the power exactly as usual, then multiply by $\frac{\text{d}y}{\text{d}x}$ because the variable being differentiated is $y$ rather than $x$.


Spec links: `spcpt_pYT5j4mkfqgGVyG8`


## Card 4 — question_and_answer (`fl_bwcgmQWgFFNWkZHQ`)

**FRONT**

What is `\frac{\text{d}}{\text{d} x} \left(x y\right)`?


**BACK**

$x \frac{\text{d}y}{\text{d}x} + y$.

A term containing both variables is a **product**, so it needs the product rule as well: differentiating $x$ gives $1$, and differentiating $y$ gives $\frac{\text{d}y}{\text{d}x}$.


Spec links: `spcpt_pYT5j4mkfqgGVyG8`


## Card 5 — question_and_answer (`fl_V2XXCHmgXtBq7gDT`)

**FRONT**

Why must you never split $\frac{\text{d}y}{\text{d}x}$ when rearranging?


**BACK**

Because it is a **single algebraic object**, not a fraction with $\text{d} y$ on top and $\text{d} x$ underneath.

Collect it and factorise it out in exactly the way you would treat any single unknown letter.


Spec links: `spcpt_pYT5j4mkfqgGVyG8`


## Card 6 — question_and_answer (`fl_4Q6QYMRD3CQb6GSR`)

**FRONT**

Will implicit differentiation always give $\frac{\text{d}y}{\text{d}x}$ as a function of $x$ alone?


**BACK**

No. The answer is usually in terms of both $x$ and $y$, and that is perfectly acceptable.

To get a numerical gradient you substitute both coordinates of the point, rather than just the $x$-value.


Spec links: `spcpt_pYT5j4mkfqgGVyG8`


## Card 7 — true_or_false (`fl_hvXTYzb6vzvnRsdj`)

**FRONT**

**True or False?**

Implicit differentiation is just the chain rule applied to terms containing $y$.


**BACK**

**True.**

Every step comes from treating $y$ as a function of $x$ and applying the chain rule, with the product rule joining in for terms that contain both variables.

There is no new rule to learn here, only a new situation in which to use the old ones.


Spec links: `spcpt_pYT5j4mkfqgGVyG8`

