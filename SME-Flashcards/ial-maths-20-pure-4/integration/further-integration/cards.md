# Further Integration

Course: ial-maths-20-pure-4 · Section: Integration

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-4/flashcards/integration/further-integration/


## Card 1 — keyword_definition (`fl_GNpzPmdj4cJwBjJm`)

**FRONT**

Define **integration by substitution**.


**BACK**

Replacing part of an integral with a single new variable $u$, so that an awkward integral turns into one you can actually do.

It is the reverse chain rule made explicit, for cases where spotting it directly would be too hard.


Spec links: `spcpt_Mn93R9Cd6pxFDHgQ`


## Card 2 — question_and_answer (`fl_Sr2Hz968vCTX7TVh`)

**FRONT**

When the substitution is not given, which part of the integral do you replace?


**BACK**

The **'second' function**, the one tucked inside the main one, rather than the main function itself.

In `\int x \left(x^{2} + 1\right)^{5} \text{d} x` that means taking $u = x^{2} + 1$, the expression sitting inside the power.


Spec links: `spcpt_Mn93R9Cd6pxFDHgQ`


## Card 3 — true_or_false (`fl_BcHrZfR3fWW939Jn`)

**FRONT**

**True or False?**

In a definite integral, the limits stay the same after a substitution.


**BACK**

**False.**

The limits are values of $x$, so once the integral is written in terms of $u$ they have to be converted using the substitution itself.

Converting them saves having to turn the answer back into $x$ at the end.


Spec links: `spcpt_Mn93R9Cd6pxFDHgQ`


## Card 4 — question_and_answer (`fl_pnQbgv6NF6nT6cgd`)

**FRONT**

You have chosen $u = x^{2} + 1$. How do you deal with the $\text{d} x$?


**BACK**

Differentiate the substitution to get $\frac{\text{d}u}{\text{d}x} = 2 x$, then treat that like a fraction to give $\text{d} u = 2 x \text{d} x$.

The $\text{d} x$ has to be replaced along with everything else, since nothing in $x$ may survive into the new integral.


Spec links: `spcpt_Mn93R9Cd6pxFDHgQ`


## Card 5 — question_and_answer (`fl_CN2SfDp4x9bwY7jZ`)

**FRONT**

How do you finish an **indefinite** integral done by substitution?


**BACK**

Integrate in terms of $u$, then substitute $x$ back in so that the answer is a function of $x$ again.

The constant of integration is added as usual once that is done.


Spec links: `spcpt_Mn93R9Cd6pxFDHgQ`


## Card 6 — question_and_answer (`fl_NdnKC5kCP9hHkchc`)

**FRONT**

Why does integration by substitution work?


**BACK**

Because it undoes the **chain rule**, which is what produced the awkward integrand in the first place.

Differentiating a function of a function leaves the inner function's derivative multiplying the outside, and substitution strips that structure back off.


Spec links: `spcpt_Mn93R9Cd6pxFDHgQ`


## Card 7 — question_and_answer (`fl_NdSXvpqmXZqzftpH`)

**FRONT**

What is different about a harder substitution question?


**BACK**

The substitution is **given to you**, because it is not one you would be expected to spot.

The method that follows is exactly the same as before; it is the algebra in between that gets heavier.


Spec links: `spcpt_XhXVThpfcZ9CPFM8`


## Card 8 — question_and_answer (`fl_VjRg94mV9D5PzhKw`)

**FRONT**

You are given the substitution $u = \sqrt{x+1}$. How do you get $\text{d} x$ in terms of $\text{d} u$?


**BACK**

Rearrange the substitution first, then differentiate: squaring gives $x = u^{2} - 1$, so $\frac{\text{d}x}{\text{d}u} = 2 u$ and $\text{d} x = 2 u \text{d} u$.

Rearranging before differentiating is usually easier than differentiating a root as it stands.


Spec links: `spcpt_XhXVThpfcZ9CPFM8`


## Card 9 — question_and_answer (`fl_8x4k2Jr2qjzQr7B9`)

**FRONT**

Why is it useful to rearrange a given substitution to make $x$ the subject?


**BACK**

Because the integrand usually contains $x$ terms that are not part of the obvious swap, and those have to be converted too.

With $u = \sqrt{x+1}$, rearranging to $x = u^{2} - 1$ gives a ready replacement for every one of them.


Spec links: `spcpt_XhXVThpfcZ9CPFM8`


## Card 10 — true_or_false (`fl_7Y6tMd8Z3vzYV8Kg`)

**FRONT**

**True or False?**

Being given the substitution makes the question easier than having to find it yourself.


**BACK**

**False.**

The substitution is given precisely because it is not one you would be expected to find, and the algebra that follows it is heavier than in a standard substitution question.

What you are handed removes one difficulty and signals another.


Spec links: `spcpt_XhXVThpfcZ9CPFM8`


## Card 11 — question_and_answer (`fl_RcypWq3wvsKcc729`)

**FRONT**

How do you know a harder substitution has been carried out correctly?


**BACK**

The integral should contain **only** $u$ and $\text{d} u$, with no $x$ left anywhere, and it should be something you can actually integrate.

If it is no simpler than what you started with, the substitution has been applied wrongly rather than chosen wrongly, since it was chosen for you.


Spec links: `spcpt_XhXVThpfcZ9CPFM8`


## Card 12 — fill_in_the_blanks (`fl_yP8mf437dQmBhVS6`)

**FRONT**

Complete the integration by parts formula:

`\int u \frac{\text{d} v}{\text{d} x} \text{d} x = u v - \_\_\_\_\_\_`


**BACK**

The completed formula is:

`\int u \frac{\text{d} v}{\text{d} x} \text{d} x = u v - \int v \frac{\text{d} u}{\text{d} x} \text{d} x`

Note that the product being integrated is made from $u$ and $\frac{\text{d}v}{\text{d}x}$, not from $u$ and $v$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 13 — question_and_answer (`fl_3xBMxJthzs8cMN66`)

**FRONT**

Which differentiation rule does integration by parts reverse?


**BACK**

The **product rule**, which is why it is the method for integrating a product of two functions.

That makes it the counterpart of the reverse chain rule, which undoes the chain rule instead.


Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 14 — question_and_answer (`fl_Qq5dVvdKHQBzdPtP`)

**FRONT**

How do you choose $u$ and $\frac{\text{d}v}{\text{d}x}$?


**BACK**

Take $u$ to be the part that becomes **simpler** when differentiated, and $\frac{\text{d}v}{\text{d}x}$ to be a part you can integrate easily.

No rule always works, so if the second integral comes out harder than the first, swap the two choices over and start again.


Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 15 — question_and_answer (`fl_WVhY2fbRvQfTPcgb`)

**FRONT**

Why are $\text{e}^{x}$ and $\mathrm{sin} x$ awkward choices for $u$?


**BACK**

Because they **cycle**: differentiating them repeatedly never makes them any simpler.

$\text{e}^{x}$ returns to itself every time, and $\mathrm{sin} x$ runs through $\mathrm{cos} x$, $- \mathrm{sin} x$ and $- \mathrm{cos} x$ before coming back.


Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 16 — question_and_answer (`fl_KcpjVyBTMNvRtdsH`)

**FRONT**

How do you integrate $\mathrm{ln} x$, which is not a product at all?


**BACK**

Write it as $1 \times \mathrm{ln} x$, then take $u = \mathrm{ln} x$ and $\frac{\text{d}v}{\text{d}x} = 1$.

That gives `x \ln x - \int x \times \frac{1}{x} \text{d} x = x \ln x - x + c`.


Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 17 — true_or_false (`fl_WkWp4GwJVbMgspqr`)

**FRONT**

**True or False?**

Integration by parts can be applied more than once in the same question.


**BACK**

**True.**

If the second integral is still a product, apply the formula to that as well.

It is rare to need it more than twice, so a third application that still does not finish usually means something went wrong earlier.


Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 18 — question_and_answer (`fl_d34hqDBqVfKwNgF8`)

**FRONT**

When should you integrate using partial fractions?


**BACK**

When the integrand is a fraction whose denominator is degree 2 or more and **factorises** into linear factors.

Splitting it turns one integral you cannot do into two or three that you can.


Spec links: `spcpt_ZFbY6XYPkJtMsk93`


## Card 19 — question_and_answer (`fl_m6Y7rcT5jTqJmcX3`)

**FRONT**

Why does integrating partial fractions usually give logarithms?


**BACK**

Because each piece has a **linear** denominator, which puts it in the `\frac{\text{f} ' \left(x\right)}{\text{f} \left(x\right)}` form up to a constant.

Each one therefore integrates to $\mathrm{ln}$ of its own denominator.


Spec links: `spcpt_ZFbY6XYPkJtMsk93`


## Card 20 — question_and_answer (`fl_GZkzkNtnGYDtccRg`)

**FRONT**

Integrate `\frac{5}{\left(x - 3\right) \left(x + 2\right)}`.


**BACK**

Split it into $\frac{1}{x-3} - \frac{1}{x+2}$, then integrate each piece separately.

That gives `\ln \left|x - 3\right| - \ln \left|x + 2\right| + c`, which tidies to `\ln \left|\frac{x - 3}{x + 2}\right| + c`.


Spec links: `spcpt_ZFbY6XYPkJtMsk93`


## Card 21 — question_and_answer (`fl_W5WxZ72t2nQRY4S6`)

**FRONT**

How do you integrate a partial fraction such as $\frac{3}{2x+1}$?


**BACK**

Adjust for the coefficient of $x$: the denominator differentiates to $2$, so the answer is `\frac{3}{2} \ln \left|2 x + 1\right| + c`.

Dropping that factor is the commonest slip once the splitting has been done correctly.


Spec links: `spcpt_ZFbY6XYPkJtMsk93`


## Card 22 — true_or_false (`fl_nbsjgX4sFvF7dysX`)

**FRONT**

**True or False?**

Any fraction with a quadratic denominator can be integrated using partial fractions.


**BACK**

**False.**

The denominator has to **factorise** into linear factors first.

$\frac{1}{x^{2}+1}$ does not split at all, and it integrates to an inverse trigonometric function instead, but that is a method beyond this course.


Spec links: `spcpt_ZFbY6XYPkJtMsk93`


## Card 23 — keyword_definition (`fl_jjTrDdFgBMFqjtwp`)

**FRONT**

Define **solid of revolution**.


**BACK**

The three-dimensional shape formed when an area bounded by a curve is rotated $360 ^{\circ}$ about an axis.

Its **volume of revolution** is simply the volume of that shape.


Spec links: `spcpt_ds4XvRtRsX2jTn7N`


## Card 24 — fill_in_the_blanks (`fl_gxJMTXPkGpBtcF2f`)

**FRONT**

Complete the formula for a volume of revolution about the $x$-axis:

`V = \pi \int_{a}^{b} \_\_\_\_\_\_ \text{d} x`


**BACK**

The completed formula is:

`V = \pi \int_{a}^{b} y^{2} \text{d} x`

Remember that $y$ is a function of $x$, so once it is substituted in everything is in terms of $x$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_ds4XvRtRsX2jTn7N`


## Card 25 — question_and_answer (`fl_kfJYhyYPqfZS4csq`)

**FRONT**

Volume is three-dimensional, so why does the formula only use $y^{2}$?


**BACK**

Because rotating a single point about the axis gives a **circle** of radius $y$, whose area is $π y^{2}$.

The integration then stacks up all those circular slices between $a$ and $b$, and that is what supplies the third dimension.


Spec links: `spcpt_ds4XvRtRsX2jTn7N`


## Card 26 — true_or_false (`fl_bDDtJNdXfWTw8Jm4`)

**FRONT**

**True or False?**

Rotating an area about the $x$-axis and about the $y$-axis give the same volume.


**BACK**

**False.**

The two rotations sweep out completely different solids, so their volumes differ.

The formula in this subtopic is specifically for rotation about the $x$-axis, which is why its limits are values of $x$.


Spec links: `spcpt_ds4XvRtRsX2jTn7N`


## Card 27 — question_and_answer (`fl_zZ6QsPdHpX3NrQgw`)

**FRONT**

What is the first thing to do when using the volume of revolution formula?


**BACK**

**Square** $y$, before worrying about $π$, the limits or the integration.

Getting the squaring out of the way first keeps the algebra clean, particularly where $y$ is itself a sum or a product.


Spec links: `spcpt_ds4XvRtRsX2jTn7N`


## Card 28 — question_and_answer (`fl_PFGjhBQp7CyNfcKv`)

**FRONT**

Where do the limits $a$ and $b$ in a volume of revolution come from?


**BACK**

They are the $x$-values between which the area is being rotated.

They may be given directly, or they may have to be read off a graph, often as the points where the curve meets the $x$-axis.


Spec links: `spcpt_ds4XvRtRsX2jTn7N`


## Card 29 — question_and_answer (`fl_zpBhMJQjmP9P7vr7`)

**FRONT**

When does a volume of revolution need a subtraction?


**BACK**

When the area being rotated does **not** have the axis of rotation as one of its boundaries.

The solid then has a hole running down its centre, and the volume of that hole has to be taken off.


Spec links: `spcpt_Gqg9pFnhtP3GjvBq`


## Card 30 — question_and_answer (`fl_4X9H3SR6x4wXSRT8`)

**FRONT**

What shape do you get by rotating a rectangle that does not touch the $x$-axis?


**BACK**

A cylinder with a hole through it, much like a toilet roll.

A rectangle that **does** border the axis gives a solid cylinder instead, which is exactly why the gap matters.


Spec links: `spcpt_Gqg9pFnhtP3GjvBq`


## Card 31 — fill_in_the_blanks (`fl_ZDVxx59fvbtBz4Qv`)

**FRONT**

Complete the single integral that replaces two subtracted volumes over the same limits:

`V = \pi \int_{a}^{b} \left(y_{1}\right)^{2} \text{d} x - \pi \int_{a}^{b} \left(y_{2}\right)^{2} \text{d} x = \pi \int_{a}^{b} \left(\_\_\_\_\_\_\right) \text{d} x`


**BACK**

The completed integral is:

`V = \pi \int_{a}^{b} \left(\left(y_{1}\right)^{2} - \left(y_{2}\right)^{2}\right) \text{d} x`

Note that this is `\left(y_{1}\right)^{2} - \left(y_{2}\right)^{2}` and **not** `\left(y_{1} - y_{2}\right)^{2}`, which is a different quantity altogether.


*Blanks: 0 — answers: ['not']*

Spec links: `spcpt_Gqg9pFnhtP3GjvBq`

Flags: blank_answer_mismatch


## Card 32 — true_or_false (`fl_DN43gcNrzjXHPxWh`)

**FRONT**

**True or False?**

Two volumes being **added** can be combined into a single integral in the same way.


**BACK**

**False.**

Volumes being added almost always come from **different** limits, because they are different parts of the solid.

If their limits were the same you would be adding part of the same volume twice over.


Spec links: `spcpt_Gqg9pFnhtP3GjvBq`


## Card 33 — question_and_answer (`fl_V2h2bjHJ3Cs4bcVd`)

**FRONT**

How do you decide whether to add or subtract volumes of revolution?


**BACK**

Think in **two dimensions** first, about the area rather than about the solid.

"Region under the curve minus region under the line" then translates straight into the corresponding subtraction of volumes.


Spec links: `spcpt_Gqg9pFnhtP3GjvBq`


## Card 34 — question_and_answer (`fl_bsCGrTY67Yh3ght6`)

**FRONT**

Why is an upright object like a vase often modelled lying horizontally?


**BACK**

So that its axis of symmetry lies along the $x$-axis, which is the axis the volume formula rotates about.

The object itself is unchanged; only its orientation on the diagram is chosen to suit the mathematics.


Spec links: `spcpt_vKYDHtGp9nMnQPyB`


## Card 35 — question_and_answer (`fl_MnjDjZWpyn8ZwxFT`)

**FRONT**

Which parts of a real object are left out of a volume of revolution model?


**BACK**

Anything that is not part of the **main body**, such as a vase's handles or the lip round the top of a bucket.

A solid of revolution can only represent a shape with rotational symmetry, so features like those cannot be included.


Spec links: `spcpt_vKYDHtGp9nMnQPyB`


## Card 36 — true_or_false (`fl_dhRDXmNtkTQXY5ZG`)

**FRONT**

**True or False?**

The thickness of a container's walls is normally ignored in these models.


**BACK**

**True.**

The thickness is usually very small compared with the size of the object, so leaving it out changes the answer very little.

Where it genuinely matters, the object has to be modelled as two solids of revolution with one subtracted from the other.


Spec links: `spcpt_vKYDHtGp9nMnQPyB`


## Card 37 — question_and_answer (`fl_GJnmwJS2rmC6yXGy`)

**FRONT**

What does it mean if a question refers to a container's **internal** dimensions?


**BACK**

That the solid of revolution being found is the **inside** of the object, in other words the space it can hold.

That distinguishes the capacity of the container from the space the whole object takes up.


Spec links: `spcpt_vKYDHtGp9nMnQPyB`


## Card 38 — fill_in_the_blanks (`fl_ZJkH8N5TF3sPF7cP`)

**FRONT**

Complete the conversion needed when a capacity is asked for in litres:

`\_\_\_\_\_\_ \text{ cm}^{3} = 1 \text{ litre}`


**BACK**

The completed conversion is:

$1000 \text{cm}^{3} = 1 \text{litre}$

A volume of revolution comes out in cubic units, so a question asking for capacity in litres needs this conversion at the very end.


*Blanks: 0 — answers: []*

Spec links: `spcpt_vKYDHtGp9nMnQPyB`


## Card 39 — question_and_answer (`fl_9qQzRv6nPt2F33Xy`)

**FRONT**

What is the first thing to check when deciding how to integrate?


**BACK**

Whether it is already a **standard integral**, or can be turned into one just by rewriting.

Expanding brackets, splitting a fraction or simplifying a quotient often removes the need for any technique at all.


Spec links: `spcpt_SrFpVvthH46W55tj`


## Card 40 — question_and_answer (`fl_2tXkJqvRTYq2QnSS`)

**FRONT**

The integrand is a product of two functions. Which methods should you consider?


**BACK**

**Reverse chain rule** first, if one factor is the derivative of something sitting inside the other.

If it is not, then **integration by parts**, or a **substitution** where one factor suggests an obvious $u$.


Spec links: `spcpt_SrFpVvthH46W55tj`


## Card 41 — question_and_answer (`fl_ZmzpFyY2JnSYhRXv`)

**FRONT**

The integrand is a fraction. What does its denominator tell you?


**BACK**

A **linear** denominator points towards a logarithm, and one that **factorises** points towards partial fractions.

If the numerator is close to the derivative of the denominator, it is the `\frac{\text{f} ' \left(x\right)}{\text{f} \left(x\right)}` form.


Spec links: `spcpt_SrFpVvthH46W55tj`


## Card 42 — question_and_answer (`fl_RzzNx3XqQ3fKVB56`)

**FRONT**

Why look again for the reverse chain rule after using an identity?


**BACK**

Because rewriting an expression changes its shape, and a reverse chain rule that was not available before may be available now.

This is the easiest thing to miss, since applying the identity feels like the answer rather than a step towards it.


Spec links: `spcpt_SrFpVvthH46W55tj`


## Card 43 — true_or_false (`fl_5qqJ5vCKwhXyKwb7`)

**FRONT**

**True or False?**

If a substitution does not work, the integral cannot be done by substitution at all.


**BACK**

**False.**

A substitution failing almost always means the **wrong** $u$ was chosen, not that the method is unavailable.

The usual fix is to substitute a different part of the integrand and try again.


Spec links: `spcpt_SrFpVvthH46W55tj`

