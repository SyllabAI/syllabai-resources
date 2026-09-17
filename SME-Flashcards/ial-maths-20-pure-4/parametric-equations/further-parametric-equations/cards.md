# Further Parametric Equations

Course: ial-maths-20-pure-4 · Section: Parametric Equations

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-4/flashcards/parametric-equations/further-parametric-equations/


## Card 1 — fill_in_the_blanks (`fl_H9kmhK4w4vfmtVyH`)

**FRONT**

Complete the rule for differentiating parametric equations:

`\frac{\text{d} y}{\text{d} x} = \frac{\text{d} y}{\text{d} t} \div \_\_\_\_\_\_`


**BACK**

The completed rule is:

$\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}t} \div \frac{\text{d}x}{\text{d}t}$

It follows from the chain rule with the reciprocal property, since $\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}t} \times \frac{\text{d}t}{\text{d}x}$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_YXNKYW4W32K6HFn5`


## Card 2 — question_and_answer (`fl_Xc2nSVGw4HDKmrNq`)

**FRONT**

Why is it acceptable for $\frac{\text{d}y}{\text{d}x}$ to come out in terms of $t$?


**BACK**

Because every point on the curve is identified by its parameter value rather than by its $x$ coordinate.

To get a numerical gradient you find the value of $t$ at the point you want and substitute that, which is one step earlier than in ordinary differentiation.


Spec links: `spcpt_YXNKYW4W32K6HFn5`


## Card 3 — question_and_answer (`fl_dVNb7dJHRtcxkwBN`)

**FRONT**

How do you find the gradient of a parametric curve at a given point?


**BACK**

Differentiate both equations to get $\frac{\text{d}y}{\text{d}t}$ and $\frac{\text{d}x}{\text{d}t}$, then divide to get $\frac{\text{d}y}{\text{d}x}$ in terms of $t$.

Find the value of $t$ at that point and substitute it in.


Spec links: `spcpt_YXNKYW4W32K6HFn5`


## Card 4 — question_and_answer (`fl_r7zqqdYy9sjrcmcg`)

**FRONT**

What condition gives a stationary point on a parametric curve?


**BACK**

$\frac{\text{d}y}{\text{d}x} = 0$, which happens exactly when $\frac{\text{d}y}{\text{d}t} = 0$.

It is the numerator of the quotient that has to vanish, so it is the $y$ equation you differentiate and set to zero.


Spec links: `spcpt_YXNKYW4W32K6HFn5`


## Card 5 — question_and_answer (`fl_qdX5B6mBMkq5t9qs`)

**FRONT**

What happens where $\frac{\text{d}x}{\text{d}t} = 0$?


**BACK**

The gradient $\frac{\text{d}y}{\text{d}x}$ is **undefined**, since the quotient would be dividing by zero.

Geometrically the tangent there is **vertical**, which is something an ordinary `y = \text{f} \left(x\right)` curve can never show.


Spec links: `spcpt_YXNKYW4W32K6HFn5`


## Card 6 — true_or_false (`fl_BChSN5mBJGzsWfs3`)

**FRONT**

**True or False?**

To find $\frac{\text{d}y}{\text{d}x}$ you must first eliminate the parameter.


**BACK**

**False.**

Differentiating each equation with respect to $t$ and dividing is quicker, and it still works when the parameter cannot be eliminated neatly.

Eliminating first is extra work that usually makes the differentiation harder rather than easier.


Spec links: `spcpt_YXNKYW4W32K6HFn5`


## Card 7 — fill_in_the_blanks (`fl_7JtqH43R8Qmz89wS`)

**FRONT**

Complete the rule for the area under a parametrically defined curve:

`\int y \text{d} x = \int y \_\_\_\_\_\_ \text{d} t`


**BACK**

The completed rule is:

`\int y \text{d} x = \int y \frac{\text{d} x}{\text{d} t} \text{d} t`

The $\text{d} x$ is replaced by $\frac{\text{d}x}{\text{d}t} \text{d} t$, and $y$ has to be written in terms of $t$ as well.


*Blanks: 0 — answers: []*

Spec links: `spcpt_WPr865MC2MCwFhys`


## Card 8 — question_and_answer (`fl_t4WTYydCQCBqhmBc`)

**FRONT**

What is the key thing to change when integrating parametrically?


**BACK**

The **limits**, which must be converted from $x$ values into the matching values of the parameter.

Leaving $x$ limits on an integral that is now with respect to $t$ is the commonest error in the topic.


Spec links: `spcpt_WPr865MC2MCwFhys`


## Card 9 — question_and_answer (`fl_mtKPYrCJR79Cg5w7`)

**FRONT**

An area is required from $x = 0$ to $x = 4$, and $x = t^{2}$. What are the limits in $t$?


**BACK**

$t = 0$ and $t = 2$, found by solving $t^{2} = 0$ and $t^{2} = 4$.

Where solving gives two possible values, the stated range of the parameter decides which one belongs to the region you want.


Spec links: `spcpt_WPr865MC2MCwFhys`


## Card 10 — question_and_answer (`fl_kTCKhv3vHHYnqYcC`)

**FRONT**

Why must $y$ be rewritten in terms of $t$ before integrating?


**BACK**

Because the integral is now with respect to $t$, so nothing in it may still be written in terms of $x$.

That is the same requirement as in any substitution: every part of the integral changes together or none of it does.


Spec links: `spcpt_WPr865MC2MCwFhys`


## Card 11 — true_or_false (`fl_w3rH7wtW93Sxm3NC`)

**FRONT**

**True or False?**

Parametric integration is a substitution in disguise.


**BACK**

**True.**

The parameter plays exactly the part that $u$ plays in an ordinary substitution: replace $\text{d} x$, rewrite the integrand, convert the limits.

Seeing that means there is no separate method to learn here, only a familiar one to recognise.


Spec links: `spcpt_WPr865MC2MCwFhys`


## Card 12 — question_and_answer (`fl_v7N7vBMV9T4hcjrQ`)

**FRONT**

Why can a volume of revolution not always be found from $y$ written in terms of $x$?


**BACK**

Because the curve may be given parametrically, as `x = \text{f} \left(t\right)` and `y = \text{g} \left(t\right)`.

Depending on those two functions, eliminating $t$ to get $y$ in terms of $x$ may be inconvenient or simply impossible.


Spec links: `spcpt_xrD7jwQVsVdCqgQM`


## Card 13 — fill_in_the_blanks (`fl_Wn5rrwp9246JNJMr`)

**FRONT**

Complete the volume of revolution for a curve given parametrically:

`V = \pi \int_{t_{1}}^{t_{2}} \left[\text{g} \left(t\right)\right]^{2} \_\_\_\_\_\_ \text{d} t`


**BACK**

The completed formula is:

`V = \pi \int_{t_{1}}^{t_{2}} \left[\text{g} \left(t\right)\right]^{2} \text{f} ' \left(t\right) \text{d} t`

That factor is the derivative of $x$ with respect to $t$, which is what allows the whole integral to be taken over $t$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_xrD7jwQVsVdCqgQM`


## Card 14 — question_and_answer (`fl_DCg7dpkRnKVGhmKK`)

**FRONT**

Which part of a parametric volume should you work out on its own first?


**BACK**

`\left[\text{g} \left(t\right)\right]^{2}`, the square of $y$ written in terms of $t$.

With a parameter, a derivative and a squaring all in play at once, dealing with the squaring separately is what keeps the assembled integral readable.


Spec links: `spcpt_xrD7jwQVsVdCqgQM`


## Card 15 — true_or_false (`fl_txYw6MYZx9Nk2bJj`)

**FRONT**

**True or False?**

The limits of a parametric volume of revolution are values of $x$.


**BACK**

**False.**

Once the integral is with respect to $t$, its limits must be values of $t$ too, found by solving `x_{1} = \text{f} \left(t_{1}\right)` and `x_{2} = \text{f} \left(t_{2}\right)`.

A volume integral is no different from any other in that respect.


Spec links: `spcpt_xrD7jwQVsVdCqgQM`


## Card 16 — question_and_answer (`fl_gKXxGtN62T7GWdHf`)

**FRONT**

How does the parametric volume formula relate to `V = \pi \int y^{2} \text{d} x`?


**BACK**

It is that same formula with every part rewritten in terms of $t$.

Nothing new is being integrated; only the variable the integration is carried out over has changed.


Spec links: `spcpt_xrD7jwQVsVdCqgQM`

