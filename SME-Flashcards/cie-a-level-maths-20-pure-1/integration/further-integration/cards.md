# Further Integration

Course: cie-a-level-maths-20-pure-1 · Section: Integration

Source: https://www.savemyexams.com/a-level/maths/cie/20/pure-1/flashcards/integration/further-integration/


## Card 1 — keyword_definition (`fl_3qynTcbGCZbDCMwK`)

**FRONT**

Define the **area under a curve** $y = \text{f} ( x )$ between $x = a$ and $x = b$.


**BACK**

The area of the region bounded by four things:

- the curve $y = \text{f} ( x )$
- the $x$-axis
- the vertical line $x = a$
- the vertical line $x = b$

The $x$-axis is the boundary that is easiest to forget: "under the curve" means between the curve and the $x$-axis, not simply below the curve.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 2 — question_and_answer (`fl_Mmd4BQgmrmzmkjy2`)

**FRONT**

What has to be true about a curve between $x = a$ and $x = b$ for the area under it to be given by `\int_{a}^{b} \text{f} \left(x\right) \text{d} x`?


**BACK**

The curve must lie on or above the $x$-axis across the whole of that interval.

Where it dips below, the integral counts that part as **negative**, so the value it returns is no longer the area.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 3 — question_and_answer (`fl_DQq4WGyFyGhvqJZG`)

**FRONT**

A question asks for the area between a curve and the $x$-axis but gives no limits. Where do the limits come from?


**BACK**

From the curve's $x$-axis intercepts, which are the natural edges of the region.

Set $y = 0$ and solve. For example, `y = x\left(5 - x\right)` gives $x = 0$ and $x = 5$, so the area is `\int_{0}^{5} \left(5x - x^{2}\right)\text{d}x`.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 4 — true_or_false (`fl_dp5dCyDrnwtXykN5`)

**FRONT**

**True or False?**

If a definite integral gives a negative value, you have made a mistake.


**BACK**

**False.**

A region lying below the $x$-axis gives a negative integral. That is the integral behaving correctly, not an error.

An area cannot be negative, so take the **modulus**: an integral of $- \frac{22}{3}$, for example, means an area of $\frac{22}{3}$ square units.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 5 — question_and_answer (`fl_Gb4JKWkT94HtVBvN`)

**FRONT**

Before integrating to find the total area between a curve and the $x$-axis, what must you check?


**BACK**

Whether the curve crosses the $x$-axis anywhere inside the interval.

Solve `\text{f} \left(x\right) = 0` to find out; each crossing splits the region into a separate piece, and each piece needs its own integral.

For example, $y = x^{3} - 12 x^{2} + 35 x$ crosses at $x = 0$, $x = 5$ and $x = 7$.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 6 — question_and_answer (`fl_jYD7Zv5Z3nXMz3xD`)

**FRONT**

A region between a curve and the $x$-axis lies partly above and partly below the axis. Why does a single definite integral across the whole interval not give its total area?


**BACK**

The part below the axis contributes a **negative** value, so it cancels part of the positive contribution from the part above. The result is smaller than the true area, and can even be zero.

Integrate each piece separately, take the **modulus** of each, then add; for example, two pieces giving $\frac{375}{4}$ and $- 8$ have a total area of $\frac{375}{4} + 8 = \frac{407}{4}$ square units.


Spec links: `spcpt_CQhzHWwghqFHzphh`


## Card 7 — question_and_answer (`fl_ZhTnKxzFjM5Z6cR9`)

**FRONT**

Why do you need to solve the equations of a curve and a line simultaneously before finding the area enclosed between them?


**BACK**

Their points of intersection are the **limits of integration**: the enclosed region only exists between them.

Set the two expressions for $y$ equal and solve. For example, for $y = 5 + 4 x - x^{2}$ and $y = 10 - 2 x$:

$10 - 2 x = 5 + 4 x - x^{2} \Rightarrow x^{2} - 6 x + 5 = 0$

so the limits are $x = 1$ and $x = 5$.


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 8 — question_and_answer (`fl_gxWX4BRnb6fHjWBn`)

**FRONT**

The region enclosed between a curve and a line runs from $x = a$ to $x = b$, with the curve above the line. How do you find its area by working out two separate areas?


**BACK**

Find the area under the curve and the area under the line over the same interval, then **subtract** the smaller from the larger:

`R = \int_{a}^{b}\text{f}(x)\,\text{d}x - \int_{a}^{b}\text{g}(x)\,\text{d}x`

Whichever graph is on top has the larger area underneath it, so with the curve on top it is the area under the line that is subtracted.


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 9 — true_or_false (`fl_Wzm7PRgMMDySXs3J`)

**FRONT**

**True or False?**

To find the area under a straight line between two $x$-values, you have to use definite integration.


**BACK**

**False.**

The region under a straight line is a **rectangle, triangle or trapezium**, so a basic area formula is usually quicker and less error-prone.

For example, the area under $y = 10 - 2 x$ from $x = 1$ to $x = 5$ is a triangle of base 4 and height 8, giving $\frac{1}{2} \times 4 \times 8 = 16$.


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 10 — question_and_answer (`fl_6hCS6ywKnbZSnFKp`)

**FRONT**

How can you find the area enclosed between a curve and a line using only one integral?


**BACK**

Subtract the two functions **before** integrating, taking the lower graph away from the upper one, then integrate the result between the intersections.

For example, with the curve $y = 5 + 4 x - x^{2}$ above the line $y = 10 - 2 x$ between $x = 1$ and $x = 5$:

`R = \int_{1}^{5}\left[\left(5 + 4x - x^{2}\right) - \left(10 - 2x\right)\right]\text{d}x = \int_{1}^{5}\left(-x^{2} + 6x - 5\right)\text{d}x`


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 11 — true_or_false (`fl_mBRR3n4JdXrg6qTW`)

**FRONT**

**True or False?**

When you subtract one function from the other to find the area enclosed between a curve and a line, it does not matter which way round you subtract, because an area cannot be negative.


**BACK**

**False.**

Subtracting the wrong way round gives the **negative** of the area, and it will not be corrected for you.

Always take the **lower** graph away from the **upper** one over the interval concerned, which means deciding from a sketch which of the two is on top.


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 12 — question_and_answer (`fl_YNBHmJt9GSHVhD7G`)

**FRONT**

Why must the whole of a line's equation be put in brackets when it is subtracted from a curve's equation?


**BACK**

Because **every** term of the line is being subtracted, not just the first one. For example:

`\left(5 + 4x - x^{2}\right) - \left(10 - 2x\right) = -x^{2} + 6x - 5`

Without the brackets the $- 2 x$ would keep its own sign, giving $- x^{2} + 2 x - 5$ and an answer that is wrong from that line onwards.


Spec links: `spcpt_8YwGfFZ89FzYxVj9`


## Card 13 — question_and_answer (`fl_q2MvK4wrnBcVftmY`)

**FRONT**

What changes when both boundaries of a region are curves?


**BACK**

Nothing about the method: it is still the integral of **upper minus lower**, taken between the intersections.

What is lost is the shortcut of using a triangle or trapezium formula for one boundary, since neither of them is a straight line any more.


Spec links: `spcpt_FfdPp8vTNhhpwWJ7`


## Card 14 — question_and_answer (`fl_7GvFnZWR7Zc48vDr`)

**FRONT**

Two curves meet at three points. How many integrals does the enclosed area need?


**BACK**

**Two**, one for each enclosed region: from the first intersection to the second, and from the second to the third.

Each region is bounded separately, so each needs its own integral with its own pair of limits.


Spec links: `spcpt_FfdPp8vTNhhpwWJ7`


## Card 15 — question_and_answer (`fl_fQF7dHGwBPXBBCxh`)

**FRONT**

Why must you check which curve is on top for **each** region separately?


**BACK**

Because the two curves swap over at every point where they cross.

A curve that was above before an intersection is below after it, so "upper minus lower" means a different subtraction in each region.


Spec links: `spcpt_FfdPp8vTNhhpwWJ7`


## Card 16 — question_and_answer (`fl_sVFrWkthTfyqcykB`)

**FRONT**

Why is a sketch essential here?


**BACK**

Because it is the only reliable way to see how many separate regions there are, and which curve is on top in each of them.

The algebra gives you the intersections; only the picture tells you what to do with them.


Spec links: `spcpt_FfdPp8vTNhhpwWJ7`


## Card 17 — true_or_false (`fl_w9fwYjcKsZKPGB6s`)

**FRONT**

**True or False?**

The total area between two curves is the integral of their difference across the whole interval.


**BACK**

**False.**

Wherever the curves swap over, the difference changes sign, so one region subtracts from another and the total comes out too small.

Integrate each region separately, take each as a positive area, and then add them.


Spec links: `spcpt_FfdPp8vTNhhpwWJ7`


## Card 18 — keyword_definition (`fl_HpNJtwrnr6jPxJJs`)

**FRONT**

Define **solid of revolution**.


**BACK**

The solid formed when an area bounded by a curve, and by other boundary lines, is rotated $360 ^{\circ}$ about an axis.

The volume of that solid is called the **volume of revolution**.


Spec links: `spcpt_VrW7TGsVKVSz59w3` `spcpt_n23tkV4bCqrNVV52`


## Card 19 — fill_in_the_blanks (`fl_8qMqZYsbGwmNQMHW`)

**FRONT**

An area bounded by `y = \text{f}\left(x\right)`, the lines $x = a$ and $x = b$, and the $x$-axis is rotated $360 ^{\circ}$ about the $x$-axis. Complete the volume:

`V = \pi \int_{a}^{b} \_\_\_\_\_\_ \, \text{d}x`


**BACK**

The completed formula is:

`V = \pi \int_{a}^{b} y^{2} \, \text{d}x`

Once the expression for $y$ is substituted in, everything is in terms of $x$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_n23tkV4bCqrNVV52`

Flags: fitb_no_blank_marker


## Card 20 — question_and_answer (`fl_jDCzq9zFsKn9X69K`)

**FRONT**

Volume is three-dimensional, so why does the formula only involve $y^{2}$?


**BACK**

Because rotating a single point at height $y$ about the axis sweeps out a **circle** of radius $y$, whose area is $π y^{2}$.

Integrating adds up all those circular cross-sections along the axis, and it is the integration that supplies the third dimension.


Spec links: `spcpt_n23tkV4bCqrNVV52`


## Card 21 — question_and_answer (`fl_fhZyCwHtFn9YjC5n`)

**FRONT**

What is the volume when an area is rotated $360 ^{\circ}$ about the $y$-axis between $y = c$ and $y = d$?


**BACK**

The volume is:

`V = \pi \int_{c}^{d} x^{2} \, \text{d}y`

The integration is with respect to $y$, so the limits are $y$-values and everything inside must be in terms of $y$.


Spec links: `spcpt_VrW7TGsVKVSz59w3`


## Card 22 — question_and_answer (`fl_4DSW2D2fST2rxY6K`)

**FRONT**

Why must `y = \text{f}\left(x\right)` be rearranged before rotating about the $y$-axis?


**BACK**

Because the formula needs $x^{2}$ expressed in terms of $y$, so the equation has to be written in the form `x = \text{g}\left(y\right)` first.

An integral with respect to $y$ cannot be left with any $x$ terms in it.


Spec links: `spcpt_VrW7TGsVKVSz59w3`


## Card 23 — true_or_false (`fl_CBmwQwpnQMVY95fK`)

**FRONT**

**True or False?**

When rotating about the $y$-axis, $x$ is sometimes squared twice.


**BACK**

**True.**

Once when rearranging $y = 2 \sqrt{x}$ into $x = \frac{1}{4} y^{2}$, and again when the formula asks for $x^{2}$, giving $x^{2} = \frac{1}{16} y^{4}$.

The two squarings do different jobs and both are needed.


Spec links: `spcpt_VrW7TGsVKVSz59w3`


## Card 24 — question_and_answer (`fl_ht7SPcSrdFZG98hJ`)

**FRONT**

Why can a volume of revolution never come out negative?


**BACK**

Because the integrand is $y^{2}$ or $x^{2}$, which is never negative whatever the sign of the curve.

A region below the $x$-axis sweeps out exactly the same solid as its mirror image above it.


Spec links: `spcpt_n23tkV4bCqrNVV52`


## Card 25 — question_and_answer (`fl_4YtV8hYQPkvNbw7K`)

**FRONT**

The area under $y = 2 \sqrt{x}$ between $x = 1$ and $x = 4$ is rotated about the $x$-axis. What is the first thing to work out?


**BACK**

Square $y$, which gives $y^{2} = 4 x$.

The integral is then `\pi \int_{1}^{4} 4x \, \text{d}x`, which comes to $30 π$ cubic units.


Spec links: `spcpt_n23tkV4bCqrNVV52`


## Card 26 — question_and_answer (`fl_Xp5h7w8kvNssKBmB`)

**FRONT**

A region that does not touch the $x$-axis is rotated about the $x$-axis. What does the solid look like?


**BACK**

It has a **hole** running all the way through the middle, like a tube or a toilet roll.

A region that does reach the axis, by contrast, gives a solid with no hole in it.


Spec links: `spcpt_hb4MJpGfS2FgyN9s`


## Card 27 — true_or_false (`fl_CcyCQK82dFFHng2X`)

**FRONT**

**True or False?**

To subtract two volumes of revolution you integrate `\left(y_{1} - y_{2}\right)^{2}`.


**BACK**

**False.**

Each function must be squared **first** and the squares then subtracted, so the integrand is $y_{1}^{2} - y_{2}^{2}$.

The square of a difference is not the difference of the squares, and using it would give the wrong volume.


Spec links: `spcpt_hb4MJpGfS2FgyN9s`


## Card 28 — question_and_answer (`fl_fXW3y38TxcyPFZ79`)

**FRONT**

How do you tell whether two volumes of revolution should be added or subtracted?


**BACK**

Subtract when one solid sits **inside** the other over the same limits, so that the smaller one is a hole.

Add when the solid is made of separate pieces lying **end to end** along the axis, each with its own pair of limits.


Spec links: `spcpt_hb4MJpGfS2FgyN9s`


## Card 29 — fill_in_the_blanks (`fl_3znQ9RPGF9PSdj3J`)

**FRONT**

A rectangle bounded by $x = a$, $x = b$, $y = c$ and $y = d$, where $0 < c < d$, is rotated about the $x$-axis. Complete the volume:

`V = \pi \int_{a}^{b} d^{2} \, \text{d}x - \pi \int_{a}^{b} \_\_\_\_\_\_ \, \text{d}x`


**BACK**

The completed volume is:

`V = \pi \int_{a}^{b} d^{2} \, \text{d}x - \pi \int_{a}^{b} c^{2} \, \text{d}x`

This is a cylinder of radius $d$ with a cylinder of radius $c$ removed from inside it.


*Blanks: 0 — answers: []*

Spec links: `spcpt_hb4MJpGfS2FgyN9s`

Flags: fitb_no_blank_marker


## Card 30 — question_and_answer (`fl_BR9fvCPrT5PMHZ4f`)

**FRONT**

A region is bounded by $y = 1$ from $x = 1$ to $x = 6$, and by $y = x - 5$ from $x = 6$ to $x = 9$. How is the volume found when it is rotated about the $x$-axis?


**BACK**

As two separate integrals with different limits, added together:

`V = \pi \int_{1}^{6} 1^{2} \, \text{d}x + \pi \int_{6}^{9} \left(x - 5\right)^{2} \, \text{d}x`

The solid is a cylinder joined to a cone, rather like a funnel, and its volume is $26 π$ cubic units.


Spec links: `spcpt_hb4MJpGfS2FgyN9s`


## Card 31 — question_and_answer (`fl_gfN2rhKm4pXJhKcX`)

**FRONT**

Which everyday objects can be modelled as a solid of revolution?


**BACK**

Objects with a circular cross-section all the way along, such as buckets, beakers, vases and lamp shades.

The model is used to work out a volume, or other information about the object, before it is manufactured.


Spec links: `spcpt_fQM5Yz4kNsymJxKw`


## Card 32 — question_and_answer (`fl_76Fb4hXMM32w8ssB`)

**FRONT**

A vase with handles is modelled as a solid of revolution. What is left out of the model?


**BACK**

The handles, and any lip or rim around the top: only the **main body** of the object is rotated.

The thickness of the material is usually ignored as well, since it is small compared with the size of the object.


Spec links: `spcpt_fQM5Yz4kNsymJxKw`


## Card 33 — true_or_false (`fl_qNKwCBKZnRyr64gR`)

**FRONT**

**True or False?**

If the thickness of a container matters, one volume of revolution is enough to model it.


**BACK**

**False.**

A container whose thickness is significant has to be modelled as **two** solids of revolution, an outer one and an inner one.

This is why a question may refer to the 'inside' of an object, or give its internal dimensions.


Spec links: `spcpt_fQM5Yz4kNsymJxKw`


## Card 34 — fill_in_the_blanks (`fl_sPmrzdhXQfcJ2Br8`)

**FRONT**

A model gives a miniature vase's volume as $40 π \text{cm}^{3}$. Complete the conversion into litres:

`\frac{40\pi}{\_\_\_\_\_\_} = 0.126 \text{ litres (3 s.f.)}`


**BACK**

The completed conversion is:

$\frac{40π}{1000} = 0 . 126 \text{litres (3 s.f.)}$

There are $1000 \text{cm}^{3}$ in a litre, and $40 π \text{cm}^{3}$ is about $125 . 66 \text{cm}^{3}$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_fQM5Yz4kNsymJxKw`

Flags: fitb_no_blank_marker


## Card 35 — question_and_answer (`fl_f6FPQCYkVvrsHC4D`)

**FRONT**

A bucket is modelled as a solid of revolution. What does the volume of revolution represent?


**BACK**

The **capacity** of the bucket, which is how much it can hold.

The model gives the volume of the shape swept out, and in the context of the question that shape is the inside of the bucket.


Spec links: `spcpt_fQM5Yz4kNsymJxKw`

