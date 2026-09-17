# Numerical Methods

Course: ial-maths-20-pure-3 · Section: Numerical Methods

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-3/flashcards/numerical-methods/numerical-methods/


## Card 1 — question_and_answer (`fl_pjTkH2HhmRkNTK4C`)

**FRONT**

What does a change of sign between `\text{f} \left(a\right)` and `\text{f} \left(b\right)` tell you?


**BACK**

That a **root** lies somewhere between $a$ and $b$.

To get from a positive value to a negative one the curve has to cross the $x$-axis, and crossing the axis is exactly what a root is.


Spec links: `spcpt_tnGXWDF39HwFf7Pk`


## Card 2 — true_or_false (`fl_JXTVjyxN6zSFnv4Y`)

**FRONT**

**True or False?**

A sign change guarantees a root only if the function is continuous across the interval.


**BACK**

**True.**

Continuity is part of the condition, not an optional extra.

Without it a sign change is equally consistent with a jump across an **asymptote**, where nothing has been crossed and there is no root.


Spec links: `spcpt_tnGXWDF39HwFf7Pk`


## Card 3 — question_and_answer (`fl_j9zykrv5CpMNKCPB`)

**FRONT**

How do you show that a root is $2 . 35$ correct to 2 decimal places?


**BACK**

Test the two **bounds** of the values that round to it, by evaluating `\text{f} \left(2 . 345\right)` and `\text{f} \left(2 . 355\right)`.

A sign change between them puts the root inside the interval that rounds to $2 . 35$.


Spec links: `spcpt_tnGXWDF39HwFf7Pk`


## Card 4 — question_and_answer (`fl_FHvm2WP7nD7zsQDZ`)

**FRONT**

What must you state when concluding a change of sign argument?


**BACK**

That the function is **continuous** on the interval, that there is a **sign change**, and therefore that a root lies within it.

The conclusion is not valid on the sign change alone, since the continuity condition is what rules out a jump.


Spec links: `spcpt_tnGXWDF39HwFf7Pk`


## Card 5 — question_and_answer (`fl_7NzGhCmM2RZHqqRm`)

**FRONT**

How do you find an interval to test in the first place?


**BACK**

Sketch the function, or evaluate it at a few whole-number values until the sign flips.

Even a rough sketch shows roughly where the curve crosses, which narrows the search down to one or two integers.


Spec links: `spcpt_tnGXWDF39HwFf7Pk`


## Card 6 — question_and_answer (`fl_PFcCzGWStZBY7FWR`)

**FRONT**

How can the change of sign method miss roots entirely?


**BACK**

If the interval contains an **even** number of roots, the signs at the two ends match and no change is detected.

Two roots inside an interval look exactly the same from the endpoints as no roots at all.


Spec links: `spcpt_jWc24T7YJ3vg83h5`


## Card 7 — question_and_answer (`fl_Z6hDYVKPyRWHFJyt`)

**FRONT**

There is a sign change. Why might there still be more roots than the one you have found?


**BACK**

Because any **odd** number of roots produces a single sign change, so three roots look like one.

The method reports whether the number of crossings is odd or even, and nothing more than that.


Spec links: `spcpt_jWc24T7YJ3vg83h5`


## Card 8 — question_and_answer (`fl_fz4QXdQR92s9W96k`)

**FRONT**

Why does a repeated root defeat the method?


**BACK**

Because the curve **touches** the $x$-axis without passing through it, so the function never changes sign.

There is a genuine root present and no sign change anywhere near it.


Spec links: `spcpt_jWc24T7YJ3vg83h5`


## Card 9 — question_and_answer (`fl_34tG9NGZwFmP5zwH`)

**FRONT**

How can a sign change appear where there is no root?


**BACK**

At a **discontinuity**, most often an asymptote, where the function jumps from large positive values to large negative ones.

Nothing has been crossed, so the sign change is real but the root is not.


Spec links: `spcpt_jWc24T7YJ3vg83h5`


## Card 10 — true_or_false (`fl_JW89RRqpqtNsTCF5`)

**FRONT**

**True or False?**

Making the interval smaller removes every one of these failures.


**BACK**

**False.**

It does deal with the failures caused by **several roots** sitting in the interval at once, since a small enough interval will hold only one.

It does nothing at all about a curve that merely touches the axis, which produces no sign change at any interval size.


Spec links: `spcpt_jWc24T7YJ3vg83h5`


## Card 11 — fill_in_the_blanks (`fl_QrFmXfqZzVCcyb5c`)

**FRONT**

Complete the notation for an iterative formula:

`x_{n + 1} = \_\_\_\_\_\_`


**BACK**

The completed notation is:

`x_{n + 1} = \text{g} \left(x_{n}\right)`

Each answer becomes the input for the next step, which makes an iterative formula a **recurrence relation**.


*Blanks: 0 — answers: ['recurrence relation']*

Spec links: `spcpt_BfHcWctk2Fw8QtZj`

Flags: blank_answer_mismatch


## Card 12 — question_and_answer (`fl_8TkqkSyKrhCNFM4r`)

**FRONT**

What has to be done to an equation before it can be iterated?


**BACK**

Rearrange it into the form `x = \text{g} \left(x\right)`, with a single $x$ on its own on the left.

The same equation can usually be rearranged in several different ways, and they do not all behave alike.


Spec links: `spcpt_BfHcWctk2Fw8QtZj`


## Card 13 — question_and_answer (`fl_WPVWJH3TvCTztzS8`)

**FRONT**

How do you use an iterative formula?


**BACK**

Start from the given value $x_{0}$, substitute it to get $x_{1}$, then feed each answer straight back in.

Stop once successive values agree to the accuracy the question has asked for.


Spec links: `spcpt_BfHcWctk2Fw8QtZj`


## Card 14 — question_and_answer (`fl_SCnbh4R3bgBqkvqC`)

**FRONT**

What are staircase and cobweb diagrams?


**BACK**

Pictures of an iteration, drawn by plotting $y = x$ against `y = \text{g} \left(x\right)` and stepping between the two.

A **staircase** closes in from one side, while a **cobweb** spirals in from alternate sides.


Spec links: `spcpt_BfHcWctk2Fw8QtZj`


## Card 15 — question_and_answer (`fl_bmcbQzDKKHj53CRJ`)

**FRONT**

Where is the root on such a diagram?


**BACK**

At the point where $y = x$ and `y = \text{g} \left(x\right)` **cross**.

There the equation `x = \text{g} \left(x\right)` is satisfied exactly, which is what being a root of the rearranged equation means.


Spec links: `spcpt_BfHcWctk2Fw8QtZj`


## Card 16 — true_or_false (`fl_8gydGvFVKqHcXxG4`)

**FRONT**

**True or False?**

Every rearrangement into `x = \text{g} \left(x\right)` converges to the root.


**BACK**

**False.**

Some rearrangements **diverge**, moving further from the root at every step.

That is why a question tells you which iterative formula to use rather than leaving the rearrangement to you.


Spec links: `spcpt_BfHcWctk2Fw8QtZj`

