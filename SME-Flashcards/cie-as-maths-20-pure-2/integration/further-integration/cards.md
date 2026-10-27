# Further Integration

Course: cie-as-maths-20-pure-2 · Section: Integration

Source: https://www.savemyexams.com/as/maths/cie/20/pure-2/flashcards/integration/further-integration/


## Card 1 — fill_in_the_blanks (`fl_jRyNgWNtNMmZN5p8`)

**FRONT**

Complete these three standard integrals:

`\int \sin x \text{d} x = \_\_\_\_\_\_ + c`

`\int \sec^{2} x \text{d} x = \_\_\_\_\_\_ + c`

`\int \text{e}^{x} \text{d} x = \_\_\_\_\_\_ + c`


**BACK**

The completed integrals are:

`\int \sin x \text{d} x = - \cos x + c`

`\int \sec^{2} x \text{d} x = \tan x + c`

`\int \text{e}^{x} \text{d} x = \text{e}^{x} + c`

Each one is a **standard derivative read backwards**: $\mathrm{tan} x$ appears, for instance, because its derivative is $\mathrm{sec}^{2} x$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_KpkfJZF2Mbzc8tpt`

Flags: fitb_no_blank_marker


## Card 2 — question_and_answer (`fl_8x7Sb7mM64vyJT8x`)

**FRONT**

What is `\int \frac{1}{x} \text{d} x`, and why does the answer need a modulus sign?


**BACK**

The integral is:

`\int \frac{1}{x} \text{d} x = \ln \left| x \right| + c`

$\mathrm{ln} x$ is only defined for $x > 0$, but $\frac{1}{x}$ exists for negative values of $x$ as well, so the **modulus** is what lets the result cover both.


Spec links: `spcpt_KpkfJZF2Mbzc8tpt`


## Card 3 — true_or_false (`fl_Dfsk45chgV2xnCjZ`)

**FRONT**

**True or False?**

Differentiating $\mathrm{cos} x$ introduces a minus sign, but integrating $\mathrm{cos} x$ does not.


**BACK**

**True.**

`\frac{\text{d}}{\text{d} x} \left(\cos x\right) = - \sin x`, whereas `\int \cos x \text{d} x = \sin x + c`.

The minus sign belongs to **differentiating** $\mathrm{cos} x$ and to **integrating** $\mathrm{sin} x$, not to $\mathrm{cos} x$ in both directions.


Spec links: `spcpt_KpkfJZF2Mbzc8tpt`


## Card 4 — question_and_answer (`fl_c4bFQyXYGD9yPZxg`)

**FRONT**

Find `\int \text{e}^{5 x} \text{d} x`.


**BACK**

The integral is:

`\int \text{e}^{5 x} \text{d} x = \frac{1}{5} \text{e}^{5 x} + c`

Differentiating $\text{e}^{5x}$ would multiply it by 5, so integrating has to **divide** by 5 to undo that.


Spec links: `spcpt_KpkfJZF2Mbzc8tpt`


## Card 5 — true_or_false (`fl_nWxNcPR69jVy78rv`)

**FRONT**

**True or False?**

`\int \frac{4}{x^{2}} \text{d} x = 4 \ln \left| x^{2} \right| + c`


**BACK**

**False.**

$\frac{4}{x^{2}}$ is $4 x^{-2}$, an ordinary power of $x$, and integrating it gives $- \frac{4}{x} + c$.

A logarithm appears only when the power of $x$ in the denominator is exactly **1**.


Spec links: `spcpt_KpkfJZF2Mbzc8tpt`


## Card 6 — question_and_answer (`fl_p5y4YcMzpZsg4fyq`)

**FRONT**

Find `\int \frac{1}{2 x + 3} \text{d} x`.


**BACK**

The integral is:

`\int \frac{1}{2 x + 3} \text{d} x = \frac{1}{2} \ln \left| 2 x + 3 \right| + c`

The whole linear bracket goes **inside** the logarithm unchanged, and the $\frac{1}{2}$ is there because $x$ has a coefficient of 2.


Spec links: `spcpt_KpkfJZF2Mbzc8tpt`


## Card 7 — question_and_answer (`fl_Qy6vrmP5jWnfjYVY`)

**FRONT**

Why does reversing a standard derivative work for $\text{e}^{5x}$ but not for $\text{e}^{x^{2}}$?


**BACK**

Because differentiating $\text{e}^{5x}$ brings out a **constant** factor, whereas differentiating $\text{e}^{x^{2}}$ brings out $2 x$.

A constant can be compensated for, but a factor containing $x$ cannot.

This is why the standard results are only quoted for **linear** brackets of the form $a x + b$.


Spec links: `spcpt_KpkfJZF2Mbzc8tpt`


## Card 8 — question_and_answer (`fl_ZVSNP4WYSbmKqDnk`)

**FRONT**

What are `\int \sec^{2} x \text{ d} x` and `\int \text{cosec}^{2} x \text{ d} x`?


**BACK**

They are $\mathrm{tan} x + c$ and $- \mathrm{cot} x + c$.

Both are just the matching derivatives read backwards, which is why neither needs an identity first.


Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`


## Card 9 — question_and_answer (`fl_X3F5yx4tz8z4v2Dk`)

**FRONT**

How do you integrate $\mathrm{tan}^{2} x$ and $\mathrm{cot}^{2} x$?


**BACK**

Rewrite each one first: $\mathrm{tan}^{2} x = \mathrm{sec}^{2} x - 1$ and $\mathrm{cot}^{2} x = \text{cosec}^{2} x - 1$.

Neither squared function can be integrated as it stands, but both of the rearranged pieces can be.


Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`


## Card 10 — fill_in_the_blanks (`fl_gwJFfzympcvtFxcZ`)

**FRONT**

Complete the rearrangement that makes $\mathrm{sin}^{2} x$ integrable, given $\mathrm{cos} 2 A \equiv 1 - 2 \mathrm{sin}^{2} A$:

`\sin^{2} A \equiv \_\_\_\_\_\_`


**BACK**

The completed rearrangement is:

`\sin^{2} A \equiv \frac{1}{2} \left(1 - \cos 2 A\right)`

Integrating that gives `\int \sin^{2} x \text{ d} x = \frac{1}{2} x - \frac{1}{4} \sin 2 x + c`, and the same trick with $\mathrm{cos} 2 A \equiv 2 \mathrm{cos}^{2} A - 1$ handles $\mathrm{cos}^{2} x$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`

Flags: fitb_no_blank_marker


## Card 11 — question_and_answer (`fl_hvr2cvG2fjxKyjH6`)

**FRONT**

How do you integrate $\mathrm{sin} 6 x \mathrm{cos} 6 x$?


**BACK**

Use $\mathrm{sin} 2 A \equiv 2 \mathrm{sin} A \mathrm{cos} A$ with $A = 6 x$, so that $\mathrm{sin} 6 x \mathrm{cos} 6 x = \frac{1}{2} \mathrm{sin} 12 x$.

That replaces a product with a single term, and the integral comes out as $- \frac{1}{24} \mathrm{cos} 12 x + c$.


Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`


## Card 12 — true_or_false (`fl_cfw3vz9sDH3bT8w8`)

**FRONT**

**True or False?**

Integrating $\mathrm{sin} x \mathrm{cos}^{3} x$ requires a trigonometric identity.


**BACK**

**False.**

No identity is needed, because $\mathrm{sin} x$ is already the derivative of $\mathrm{cos} x$, apart from a sign.

The integral is $- \frac{1}{4} \mathrm{cos}^{4} x + c$, and the expression only looks as though it wants an identity because of the two trigonometric factors.


Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`


## Card 13 — true_or_false (`fl_dZ7DDV6P9NzqbtmR`)

**FRONT**

**True or False?**

Two students integrate $\mathrm{sin} x \mathrm{cos} x$ and get $- \frac{1}{4} \mathrm{cos} 2 x$ and $\frac{1}{2} \mathrm{sin}^{2} x$. Both can be right.


**BACK**

**True.**

The two expressions differ by the constant $\frac{1}{4}$, and the arbitrary constant of integration absorbs any difference of that kind.

Differentiating each of them is the quickest way to confirm that both are genuine antiderivatives.


Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`


## Card 14 — keyword_definition (`fl_bgRVH6Htg74gWbVH`)

**FRONT**

Define the **trapezium rule**.


**BACK**

A numerical method for estimating the value of a **definite integral**.

The region is divided into strips of equal width, and each strip is treated as a **trapezium** rather than as its exact shape.


Spec links: `spcpt_QzpfK3ZQD5hPS8bj`


## Card 15 — fill_in_the_blanks (`fl_BXDcZHv5xkDzT6dW`)

**FRONT**

Complete the trapezium rule, filling in the two missing groups of $y$-values:

`\int_{a}^{b} y \text{d} x \approx \frac{1}{2} h \left[ \left( \_\_\_\_\_\_ \right) + 2 \left( \_\_\_\_\_\_ \right) \right]`


**BACK**

The completed rule is:

`\int_{a}^{b} y \text{d} x \approx \frac{1}{2} h \left[ \left( y_{0} + y_{n} \right) + 2 \left( y_{1} + y_{2} + \ldots + y_{n - 1} \right) \right]`

The **first and last** $y$-values are counted once, and every one in between is counted twice.


*Blanks: 0 — answers: []*

Spec links: `spcpt_QzpfK3ZQD5hPS8bj`

Flags: fitb_no_blank_marker


## Card 16 — question_and_answer (`fl_Q723sbXWJ4TKHSJV`)

**FRONT**

A definite integral from $x = 1$ to $x = 9$ is to be estimated using 4 strips. What is the strip width, and how many $y$-values are needed?


**BACK**

The strip width is $h = \frac{9-1}{4} = 2$, from $h = \frac{b-a}{n}$.

**Five** $y$-values are needed, $y_{0}$ to $y_{4}$, because $n$ strips have $n + 1$ edges.

Questions often call the strips **intervals** instead.


Spec links: `spcpt_QzpfK3ZQD5hPS8bj`


## Card 17 — question_and_answer (`fl_7WZRHsp664SFQwkq`)

**FRONT**

The curve `y = \text{f} \left(x\right)` bends upwards throughout the interval, like $y = x^{2}$. Does the trapezium rule over-estimate or under-estimate `\int_{a}^{b} \text{f} \left(x\right) \text{d} x`, and why?


**BACK**

It **over-estimates** it.

The top of each strip is a straight chord joining two points on the curve, and where the curve bends upwards it sags **below** that chord, so every trapezium carries a sliver of extra area.

A curve bending the other way, such as $y = \mathrm{ln} x$, gives an under-estimate.


Spec links: `spcpt_QzpfK3ZQD5hPS8bj`


## Card 18 — true_or_false (`fl_x3Gx3ph6HHRjgR9c`)

**FRONT**

**True or False?**

If the graph is a straight line, the trapezium rule gives the exact value of the integral, however few strips are used.


**BACK**

**True.**

A trapezium's sloping top joins two points on the graph, so for a straight line it lies **along** the graph itself.

The trapezium and the region are then identical, and even a single strip gives the exact answer.


Spec links: `spcpt_QzpfK3ZQD5hPS8bj`


## Card 19 — question_and_answer (`fl_wmwqtBWmktv7gyNj`)

**FRONT**

Why is the trapezium rule needed to evaluate `\int_{0}^{2} \sqrt{1 + x^{3}} \text{d} x`?


**BACK**

Because $\sqrt{1+x^{3}}$ cannot be matched to any of the standard integrals, so there is no exact answer to be found by reversing a derivative.

The integral still has a definite value, and the trapezium rule estimates it from a small number of $y$-values.


Spec links: `spcpt_QzpfK3ZQD5hPS8bj`


## Card 20 — question_and_answer (`fl_YzBr6G7552hFTfKG`)

**FRONT**

How does increasing the number of strips change a trapezium rule estimate?


**BACK**

It makes the estimate **more accurate**.

Narrower strips mean each sloping top stays closer to the curve, so less area is wrongly included or left out.


Spec links: `spcpt_QzpfK3ZQD5hPS8bj`

