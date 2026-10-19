# Integration

Course: cie-igcse-further-maths-additional-maths-25 · Section: Calculus

Source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/flashcards/calculus/integration/


## Card 1 — question_and_answer (`fl_sJ4SWZx3QtKYBJYN`)

**FRONT**

What is integration?


**BACK**

It is the **reverse of differentiation**: the process of recovering a function from its derivative.

That relationship is the Fundamental Theorem of Calculus, which says the two operations undo each other.


Spec links: `spcpt_zHBZvh2CZth3D8dz`


## Card 2 — question_and_answer (`fl_zhxG36VKQMGY7MzJ`)

**FRONT**

In `\int \text{f}(x)\,\text{d}x`, what does each part mean?


**BACK**

The sign `\int` means **integrate**, $\text{f} ( x )$ is the function being integrated, and $\text{d} x$ says which variable to integrate with respect to.

The function being integrated is called the **integrand**, and it needs brackets if it has more than one term.


Spec links: `spcpt_zHBZvh2CZth3D8dz`


## Card 3 — question_and_answer (`fl_yGgVzQNbTWHhbN77`)

**FRONT**

Why does an indefinite integral need "$+ c$"?


**BACK**

Because constants **disappear** when you differentiate, so integrating cannot tell you which constant was there.

Every curve in the family $y = x^{2} + c$ has the same gradient function $2 x$, and $c$ acknowledges that they are all valid answers.


Spec links: `spcpt_zHBZvh2CZth3D8dz`


## Card 4 — keyword_definition (`fl_SCKV8xqqhBRT2BNP`)

**FRONT**

Define the **constant of integration**.


**BACK**

The **constant of integration** is the unknown constant $c$ added to the result of an indefinite integral.

It represents the whole family of curves that share the derivative you started from.


Spec links: `spcpt_zHBZvh2CZth3D8dz`


## Card 5 — true_or_false (`fl_rJnnvvprHXHZ5zfT`)

**FRONT**

**True or False?**

Differentiating a function and then integrating the result gets you back exactly where you started.


**BACK**

**False.**

You get back the original function **plus an unknown constant**, because differentiating destroyed whatever constant it had.

Without extra information there is no way to recover that constant.


Spec links: `spcpt_zHBZvh2CZth3D8dz`


## Card 6 — question_and_answer (`fl_TvThg58VHqm9Z4Qs`)

**FRONT**

Why do the brackets matter in `\int (3x^{2} + 4x)\,\text{d}x`?


**BACK**

They show that **everything inside** is being integrated, not just the first term.

Read it as "integrate all of $3 x^{2} + 4 x$ with respect to $x$", with the $\text{d} x$ closing the instruction.


Spec links: `spcpt_zHBZvh2CZth3D8dz`


## Card 7 — fill_in_the_blanks (`fl_SYDngRnQRS5FZHZk`)

**FRONT**

Complete the rule for integrating a power of $x$:

`\int x^{n}\,\text{d}x = \_\_\_\_\_\_ + c`


**BACK**

The completed rule is:

`\int x^{n}\,\text{d}x = \frac{x^{n+1}}{n+1} + c`

In words: **raise the power by one, then divide by the new power**, which is exactly the reverse of differentiating.


*Blanks: 0 — answers: []*

Spec links: `spcpt_b8YJ77mKsSyF3zCy`

Flags: fitb_no_blank_marker


## Card 8 — true_or_false (`fl_MrpshZ52x8sskNdR`)

**FRONT**

**True or False?**

The rule for integrating $x^{n}$ fails when $n = - 1$.


**BACK**

**True.**

Raising $- 1$ by one gives a new power of zero, and the rule would then divide by zero.

That is why `\int \frac{1}{x}\,\text{d}x` needs a logarithm instead, and is dealt with separately.


Spec links: `spcpt_b8YJ77mKsSyF3zCy`


## Card 9 — question_and_answer (`fl_4rqHP4XHtjjNyy9s`)

**FRONT**

How do you integrate a constant, such as `\int 4\,\text{d}x`?


**BACK**

The answer is $4 x + c$.

Think of the constant as $4 x^{0}$, so the rule still applies and raises the power to 1.


Spec links: `spcpt_b8YJ77mKsSyF3zCy`


## Card 10 — question_and_answer (`fl_SbWC6YhS2kV5QXZS`)

**FRONT**

How would you begin integrating `5\sqrt[3]{x}` and $\frac{4}{x^{2}}$?


**BACK**

Rewrite both as powers of $x$ first, giving $5 x^{\frac{1}{3}}$ and $4 x^{-2}$.

The power rule works on any rational power, but only once the expression is actually written as one.


Spec links: `spcpt_b8YJ77mKsSyF3zCy`


## Card 11 — question_and_answer (`fl_j27nMSVtKTC7BkYF`)

**FRONT**

Why can you not integrate $8 x^{2} ( 2 x - 3 )$ as it stands?


**BACK**

The rule works on a **sum or difference** of powers of $x$, not on a product.

Expanding first gives $16 x^{3} - 24 x^{2}$, which integrates term by term to $4 x^{4} - 8 x^{3} + c$.


Spec links: `spcpt_b8YJ77mKsSyF3zCy`


## Card 12 — question_and_answer (`fl_XxrdpWJM4RHxNZs8`)

**FRONT**

What must a question give before $c$ can be found?


**BACK**

Integrate as usual, keeping the $+ c$, then substitute the coordinates of a **given point** on the curve.

That produces an equation in $c$ alone, which you solve.


Spec links: `spcpt_ZQNM4dHgZkvDTmXJ`


## Card 13 — question_and_answer (`fl_PKDRc4PS4VCQySv3`)

**FRONT**

What extra information must a question give before $c$ can be found?


**BACK**

A **point the curve passes through**, or an equivalent condition such as a value of $\text{f} ( 1 )$.

Without it there is nothing to pin the constant down, and $+ c$ has to stay in the answer.


Spec links: `spcpt_ZQNM4dHgZkvDTmXJ`


## Card 14 — question_and_answer (`fl_2r2vZVtshMRNGNBh`)

**FRONT**

$\text{f} ( x ) = \frac{2}{5} x^{\frac{5}{2}} + 4 x^{\frac{3}{2}} + 18 x^{\frac{1}{2}} + c$ and $\text{f} ( 1 ) = 25$. Find $c$.


**BACK**

Substituting $x = 1$ makes every power equal 1, leaving $\frac{2}{5} + 4 + 18 + c = 25$.

So $22 \frac{2}{5} + c = 25$, giving $c = \frac{13}{5}$.


Spec links: `spcpt_ZQNM4dHgZkvDTmXJ`


## Card 15 — question_and_answer (`fl_8W2J5j8HfJ8V5NW8`)

**FRONT**

How do you evaluate a definite integral?


**BACK**

Integrate as usual, writing the result in **square brackets** with the limits outside.

Then substitute the **upper** limit, substitute the **lower** limit, and subtract the second value from the first.


Spec links: `spcpt_D8yXJgjNvHXZ9KQk`


## Card 16 — question_and_answer (`fl_33sVqSP7XRmRgfSr`)

**FRONT**

Why is no constant of integration needed for a definite integral?


**BACK**

Because the $+ c$ would appear in **both** substitutions.

Since you subtract one from the other, the two constants cancel and make no difference to the answer.


Spec links: `spcpt_D8yXJgjNvHXZ9KQk`


## Card 17 — question_and_answer (`fl_WQScF8DMrDrj3qS5`)

**FRONT**

Evaluate `\int_{2}^{4} (3x^{3} - 6x)\,\text{d}x`.


**BACK**

Integrating gives `\left[\frac{3}{4}x^{4} - 3x^{2}\right]_{2}^{4}`.

Substituting the limits gives $( 192 - 48 ) - ( 12 - 12 ) = 144$.


Spec links: `spcpt_D8yXJgjNvHXZ9KQk`


## Card 18 — fill_in_the_blanks (`fl_d6Swz5zbsmyFbVRj`)

**FRONT**

Complete these two properties of definite integrals:

`\int_{a}^{a} \text{f}(x)\,\text{d}x = \_\_\_\_\_\_`

`\int_{a}^{b} \text{f}(x)\,\text{d}x = \_\_\_\_\_\_`


**BACK**

The completed properties are:

`\int_{a}^{a} \text{f}(x)\,\text{d}x = 0`

`\int_{a}^{b} \text{f}(x)\,\text{d}x = -\int_{b}^{a} \text{f}(x)\,\text{d}x`

Equal limits give zero because you subtract a value from itself, and swapping the limits reverses the subtraction.


*Blanks: 0 — answers: []*

Spec links: `spcpt_D8yXJgjNvHXZ9KQk`

Flags: fitb_no_blank_marker


## Card 19 — question_and_answer (`fl_x4BxfHXRBhHDTkmW`)

**FRONT**

Can a constant factor be taken outside a definite integral?


**BACK**

Yes: `\int_{a}^{b} k\,\text{f}(x)\,\text{d}x = k \int_{a}^{b} \text{f}(x)\,\text{d}x`.

This is worth doing when $k$ is a fraction or negative, since it keeps the messy number out of the working.


Spec links: `spcpt_D8yXJgjNvHXZ9KQk`


## Card 20 — question_and_answer (`fl_6QsJhvqm2NBTMr6v`)

**FRONT**

How can a definite integral be split into two parts?


**BACK**

By choosing an intermediate value $c$ between the limits:

`\int_{a}^{b} \text{f}(x)\,\text{d}x = \int_{a}^{c} \text{f}(x)\,\text{d}x + \int_{c}^{b} \text{f}(x)\,\text{d}x`

This is what lets you handle a region that changes character partway along.


Spec links: `spcpt_D8yXJgjNvHXZ9KQk`


## Card 21 — true_or_false (`fl_5Gq2WrHpQbt89Tjx`)

**FRONT**

**True or False?**

The value of a definite integral can be negative or zero.


**BACK**

**True.**

A definite integral is just a number produced by a subtraction, so nothing forces it to be positive.

It is only when you are asked for an **area** that a negative value needs further thought.


Spec links: `spcpt_D8yXJgjNvHXZ9KQk`


## Card 22 — question_and_answer (`fl_P5fCGgpkqvPqgPr3`)

**FRONT**

What does "the area under a curve" mean?


**BACK**

The region bounded by the curve $y = \text{f} ( x )$, the $x$-axis, and the two vertical lines $x = a$ and $x = b$.

Those two lines are the limits of the integral that finds it.


Spec links: `spcpt_NfNBhBGVj6NP5t5s`


## Card 23 — question_and_answer (`fl_r5ksV9WWCXGbt8bx`)

**FRONT**

How do you find the area under a curve?


**BACK**

Evaluate the **definite integral** of the function between the two limits.

That single calculation gives the area, provided the curve stays above the $x$-axis throughout.


Spec links: `spcpt_NfNBhBGVj6NP5t5s`


## Card 24 — question_and_answer (`fl_C8ZHFgmxnNJChGGq`)

**FRONT**

What do you do if a question gives you no limits?


**BACK**

They are almost always the $x$-axis intercepts of the curve.

Set $y = 0$ and solve to find them, since that is where the region naturally begins and ends.


Spec links: `spcpt_NfNBhBGVj6NP5t5s`


## Card 25 — question_and_answer (`fl_fgTJKpjJjGdvbX2W`)

**FRONT**

What happens when the region lies below the $x$-axis?


**BACK**

The integral comes out **negative**.

An area cannot be negative, so take the **modulus** of the integral to get the area itself.


Spec links: `spcpt_NfNBhBGVj6NP5t5s`


## Card 26 — question_and_answer (`fl_hS6tmsRcnHqwCN69`)

**FRONT**

A region lies partly above and partly below the $x$-axis. How do you find its total area?


**BACK**

**Split** it at the point where the curve crosses the axis and integrate each part separately.

Take the modulus of each result **before** adding them together.


Spec links: `spcpt_NfNBhBGVj6NP5t5s`


## Card 27 — true_or_false (`fl_PhdFY22rNdg5VRCr`)

**FRONT**

**True or False?**

For a region partly above and partly below the axis, one integral over the whole interval gives the total area.


**BACK**

**False.**

The part below the axis contributes a negative amount, which **cancels** some of the positive part.

The single integral gives the net value, not the area, so the region must be split and the moduli added.


Spec links: `spcpt_NfNBhBGVj6NP5t5s`


## Card 28 — question_and_answer (`fl_75DZ3bZyhGqW8Vqf`)

**FRONT**

Why is it worth sketching the curve before finding an area?


**BACK**

Because the sketch shows where the curve crosses the $x$-axis, and so whether the region needs splitting at all.

Without it you cannot tell that part of the region is below the axis, and the sign problem passes unnoticed.


Spec links: `spcpt_NfNBhBGVj6NP5t5s`


## Card 29 — question_and_answer (`fl_RDzw5dKsM8xRn8yS`)

**FRONT**

How do you find the area enclosed between a curve and a line?


**BACK**

Find the area under each one separately, then **subtract the smaller from the larger**.

Which way round depends on the sketch: if the curve is on top you subtract the line's area from it, and if the line is on top you do the reverse.


Spec links: `spcpt_Pdm8xXYjwCtVmfjN`


## Card 30 — question_and_answer (`fl_r7GCVntJm8rfktTd`)

**FRONT**

What do you need before you can set up the integrals?


**BACK**

The **points of intersection** of the line and the curve, since they give the limits.

Find them by setting the two equations equal to each other and solving.


Spec links: `spcpt_Pdm8xXYjwCtVmfjN`


## Card 31 — question_and_answer (`fl_6jJNYhx9KmzNjDvb`)

**FRONT**

Is integration the only way to find the area under the straight line?


**BACK**

No: the region under a line is a **triangle, rectangle or trapezium**, so the ordinary area formulae work.

That is usually quicker and less error-prone than integrating, and it is worth spotting from the sketch.


Spec links: `spcpt_Pdm8xXYjwCtVmfjN`


## Card 32 — true_or_false (`fl_DJbhDwHNysZQp2VF`)

**FRONT**

**True or False?**

You must integrate the curve and the line separately before subtracting.


**BACK**

**False.**

You can subtract **first** and integrate once, treating the line as a second curve.

Both routes are valid, though subtracting first offers more chances to slip up with signs.


Spec links: `spcpt_Pdm8xXYjwCtVmfjN`


## Card 33 — fill_in_the_blanks (`fl_YJJ55BMnfnj7ZtwM`)

**FRONT**

Complete the integral for the area between two curves:

`\text{Area} = \int_{a}^{b} (\_\_\_\_\_\_ - \_\_\_\_\_\_)\,\text{d}x`


**BACK**

The completed integral is:

`\text{Area} = \int_{a}^{b} (\text{upper curve} - \text{lower curve})\,\text{d}x`

The limits $a$ and $b$ are the values of $x$ where the two curves meet.


*Blanks: 0 — answers: []*

Spec links: `spcpt_m4WMGrn2YKjy9nqy`

Flags: fitb_no_blank_marker


## Card 34 — question_and_answer (`fl_XDJ2sFcB39KXpMs7`)

**FRONT**

Why does "upper minus lower" work even below the $x$-axis?


**BACK**

Because the subtraction measures the **vertical gap** between the two curves, wherever they happen to sit.

The height of the strip between them is positive as long as you take the upper curve first, so the sign looks after itself.


Spec links: `spcpt_m4WMGrn2YKjy9nqy`


## Card 35 — question_and_answer (`fl_HSsnxZ8hW294GqVt`)

**FRONT**

Two curves cross partway through the region you want. What must you do?


**BACK**

**Split** the region at the crossing point and integrate each part separately, then add the results.

This is necessary because the curves swap over, so whichever was the upper curve is no longer on top after the crossing.


Spec links: `spcpt_m4WMGrn2YKjy9nqy`


## Card 36 — true_or_false (`fl_bRWmprnqHyj3R6Db`)

**FRONT**

**True or False?**

You split an area at a crossing point for the same reason whether it is the $x$-axis or another curve.


**BACK**

**False.**

Crossing the $x$-axis matters because the integral changes sign, and the fix is to take the modulus of each piece.

Two **curves** crossing matters because they swap which is on top, and the fix is to reverse the order of the subtraction.


Spec links: `spcpt_m4WMGrn2YKjy9nqy`


## Card 37 — fill_in_the_blanks (`fl_XYcYWKdXKrn6Kwvv`)

**FRONT**

Complete the three standard trigonometric integrals:

`\int \sin x\,\text{d}x = \_\_\_\_\_\_ + c`

`\int \cos x\,\text{d}x = \_\_\_\_\_\_ + c`

`\int \sec^{2} x\,\text{d}x = \_\_\_\_\_\_ + c`


**BACK**

The completed integrals are:

`\int \sin x\,\text{d}x = -\cos x + c`

`\int \cos x\,\text{d}x = \sin x + c`

`\int \sec^{2} x\,\text{d}x = \tan x + c`

Each is simply the derivative result read backwards.


*Blanks: 0 — answers: []*

Spec links: `spcpt_MyGktwWfzWjM9zbv`

Flags: fitb_no_blank_marker


## Card 38 — true_or_false (`fl_cPBvbTDMGxc4wJcQ`)

**FRONT**

**True or False?**

`\int \cos x\,\text{d}x = -\sin x + c`


**BACK**

**False.**

It is `\int \cos x\,\text{d}x = \sin x + c`, with no minus sign.

The minus belongs to the **sine** integral instead, which is the opposite way round from differentiation.


Spec links: `spcpt_MyGktwWfzWjM9zbv`


## Card 39 — question_and_answer (`fl_MJK3MTXHv2Nqkzq4`)

**FRONT**

What is `\int \sin(ax + b)\,\text{d}x`?


**BACK**

It is $- \frac{1}{a} \mathrm{cos} ( a x + b ) + c$.

The bracket is unchanged, and you **divide** by $a$, where differentiating would have multiplied by it.


Spec links: `spcpt_MyGktwWfzWjM9zbv`


## Card 40 — question_and_answer (`fl_vWPsfdTpXWG6Rdgz`)

**FRONT**

Find `\int \sec^{2}\left(3x - \frac{\pi}{3}\right)\text{d}x`.


**BACK**

Use `\int \sec^{2}(ax + b)\,\text{d}x = \frac{1}{a}\tan(ax + b) + c`.

Here $a = 3$, so the answer is `\frac{1}{3}\tan\left(3x - \frac{\pi}{3}\right) + c`.


Spec links: `spcpt_MyGktwWfzWjM9zbv`


## Card 41 — true_or_false (`fl_GRtFpvyG9StYzqPh`)

**FRONT**

**True or False?**

These integrals only hold when the angle is in radians.


**BACK**

**True.**

Every calculus result for trigonometric functions assumes radians, integration as much as differentiation.

The formulas give numbers either way, which is what makes working in degrees so easy to miss.


Spec links: `spcpt_MyGktwWfzWjM9zbv`


## Card 42 — question_and_answer (`fl_MFtnBngcrsW42wcJ`)

**FRONT**

Find `\int 2\sin\left(2x + \frac{\pi}{6}\right)\text{d}x`.


**BACK**

Take the 2 outside, then integrate, which brings in a factor of $\frac{1}{2}$:

`2 \times \left(-\frac{1}{2}\cos\left(2x + \frac{\pi}{6}\right)\right) = -\cos\left(2x + \frac{\pi}{6}\right)`

So the integral is `-\cos\left(2x + \frac{\pi}{6}\right) + c`, the two factors having cancelled.


Spec links: `spcpt_MyGktwWfzWjM9zbv`


## Card 43 — fill_in_the_blanks (`fl_ZThDSNHpW9XNHp24`)

**FRONT**

Complete the two standard integrals:

`\int \text{e}^{x}\,\text{d}x = \_\_\_\_\_\_ + c`

`\int \frac{1}{x}\,\text{d}x = \_\_\_\_\_\_ + c`


**BACK**

The completed integrals are:

`\int \text{e}^{x}\,\text{d}x = \text{e}^{x} + c`

`\int \frac{1}{x}\,\text{d}x = \ln\left|x\right| + c`

The second one is what fills the gap left by the power rule, which fails when the power is $- 1$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_N2d7b7XT2gzcq6Mz`

Flags: fitb_no_blank_marker


## Card 44 — question_and_answer (`fl_yjn973pM4NjhZY6Z`)

**FRONT**

What are `\int \text{e}^{ax+b}\,\text{d}x` and `\int \frac{1}{ax+b}\,\text{d}x`?


**BACK**

They are $\frac{1}{a} \text{e}^{ax+b} + c$ and `\frac{1}{a}\ln\left|ax + b\right| + c`.

In both cases you **divide** by $a$, the derivative of the linear bracket.


Spec links: `spcpt_N2d7b7XT2gzcq6Mz`


## Card 45 — question_and_answer (`fl_bgt4vGBsX6NhPNf8`)

**FRONT**

Why is the answer written `\ln\left|x\right|` rather than $\mathrm{ln} x$?


**BACK**

Because a logarithm is only defined for a **positive** argument, while $\frac{1}{x}$ exists for negative $x$ too.

The modulus lets the result cover both sides of the origin, so dropping it narrows the answer without warning.


Spec links: `spcpt_N2d7b7XT2gzcq6Mz`


## Card 46 — question_and_answer (`fl_fM8JmNg23p2JgMv2`)

**FRONT**

What is `\int \frac{a}{ax+b}\,\text{d}x`?


**BACK**

It is `\ln\left|ax + b\right| + c`, with no fraction in front.

The $a$ on top cancels the $\frac{1}{a}$ the rule would otherwise produce, since the numerator is exactly the derivative of the denominator.


Spec links: `spcpt_N2d7b7XT2gzcq6Mz`


## Card 47 — question_and_answer (`fl_q3SFQb9J2w9KSS9T`)

**FRONT**

Find `\int \text{e}^{4-x}\,\text{d}x`.


**BACK**

Here $a = - 1$, so dividing by $a$ means multiplying by $- 1$.

The integral is therefore $- \text{e}^{4-x} + c$, and the sign is easy to lose when $x$ has a negative coefficient.


Spec links: `spcpt_N2d7b7XT2gzcq6Mz`


## Card 48 — question_and_answer (`fl_n2Pq4YJmDCvjqVmX`)

**FRONT**

Why is the constant of integration sometimes written as $\mathrm{ln} k$?


**BACK**

Because it can then be **absorbed** into the logarithm using the laws of logarithms.

So `\ln\left|x\right| + \ln k` becomes the single term `\ln k\left|x\right|`, which is why two correct answers can look quite different.


Spec links: `spcpt_N2d7b7XT2gzcq6Mz`


## Card 49 — question_and_answer (`fl_z4TNjTHDn2JSNT8d`)

**FRONT**

When can you use the reverse chain rule?


**BACK**

When the integrand is a **composite function multiplied by the derivative of its inner function**.

You are spotting that the chain rule would have produced this expression, and running that process backwards.


Spec links: `spcpt_r82JktHqvqwp3wHw`


## Card 50 — true_or_false (`fl_nTTwjsS7Xx4p2yR2`)

**FRONT**

**True or False?**

`\int \text{e}^{\text{f}(x)}\,\text{d}x = \frac{1}{\text{f}'(x)}\text{e}^{\text{f}(x)} + c` for any function $\text{f} ( x )$.


**BACK**

**False.**

Dividing by the derivative only works when $\text{f} ( x )$ is **linear**, of the form $a x + b$.

For a general inner function you must have its derivative already present as a factor, which is what the reverse chain rule requires.


Spec links: `spcpt_r82JktHqvqwp3wHw`


## Card 51 — question_and_answer (`fl_Nq9345bSmzv7jfrQ`)

**FRONT**

What does "adjust and compensate" mean?


**BACK**

Forcing the constant you need **inside** the integral, and dividing outside by the same constant to keep the value unchanged.

So `\int 5x\text{e}^{x^{2}}\,\text{d}x` becomes `\frac{5}{2}\int 2x\text{e}^{x^{2}}\,\text{d}x`, which is now a reverse chain rule.


Spec links: `spcpt_r82JktHqvqwp3wHw`


## Card 52 — question_and_answer (`fl_vTGyhqMWT7pjq4W2`)

**FRONT**

Why does adjust and compensate only work for a constant factor?


**BACK**

Because a constant can be moved freely across the integral sign without changing anything.

A term involving $x$ cannot, so you can never manufacture a missing function this way, only a missing number.


Spec links: `spcpt_r82JktHqvqwp3wHw`


## Card 53 — question_and_answer (`fl_9WQ2k796wVnWtVtK`)

**FRONT**

Integrate $5 x^{2} \mathrm{sin} ( 2 x^{3} )$, given the result passes through $( 0 , 1 )$.


**BACK**

The inner function $2 x^{3}$ differentiates to $6 x^{2}$, so adjust and compensate to get `\frac{5}{6}\int 6x^{2}\sin(2x^{3})\,\text{d}x`.

That integrates to $- \frac{5}{6} \mathrm{cos} ( 2 x^{3} ) + c$, and substituting $( 0 , 1 )$ gives $- \frac{5}{6} + c = 1$, so $c = \frac{11}{6}$.


Spec links: `spcpt_r82JktHqvqwp3wHw`


## Card 54 — fill_in_the_blanks (`fl_WRSBG3fv3bc4zhyn`)

**FRONT**

Complete this particularly useful reverse chain rule result:

`\int \frac{\text{f}'(x)}{\text{f}(x)}\,\text{d}x = \_\_\_\_\_\_ + c`


**BACK**

The completed result is:

`\int \frac{\text{f}'(x)}{\text{f}(x)}\,\text{d}x = \ln\left|\text{f}(x)\right| + c`

Look for it whenever the numerator is the derivative of the denominator, or a constant multiple of it.


*Blanks: 0 — answers: []*

Spec links: `spcpt_r82JktHqvqwp3wHw`

Flags: fitb_no_blank_marker


## Card 55 — question_and_answer (`fl_5kxQPp6S3cGHvD8x`)

**FRONT**

What is `\int (ax + b)^{n}\,\text{d}x`, where $n \neq - 1$?


**BACK**

Raise the power by one, divide by the new power, then divide by $a$:

`\int (ax + b)^{n}\,\text{d}x = \frac{(ax + b)^{n+1}}{a(n + 1)} + c`

The extra division by $a$ is what makes this different from integrating a plain power of $x$.


Spec links: `spcpt_Zndqd25fHNYPKVMZ`


## Card 56 — question_and_answer (`fl_8g7y68Rvfh8zCKQF`)

**FRONT**

How can you always check an integral is right?


**BACK**

**Differentiate your answer** and see whether you get back what you integrated.

The two operations are inverses, so this catches a wrong coefficient immediately.


Spec links: `spcpt_Zndqd25fHNYPKVMZ`

