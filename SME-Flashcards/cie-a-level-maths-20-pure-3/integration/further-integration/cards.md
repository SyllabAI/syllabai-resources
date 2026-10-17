# Further Integration

Course: cie-a-level-maths-20-pure-3 · Section: Integration

Source: https://www.savemyexams.com/a-level/maths/cie/20/pure-3/flashcards/integration/further-integration/


## Card 1 — fill_in_the_blanks (`fl_hfstWZYPmwVTJYXd`)

**FRONT**

Complete these two standard integrals:

`\int \sin x \text{ d} x = \_\_\_\_\_\_`

`\int \cos x \text{ d} x = \_\_\_\_\_\_`


**BACK**

The completed integrals are:

`\int \sin x \text{ d} x = - \cos x + c`

`\int \cos x \text{ d} x = \sin x + c`

The minus sign changes sides: differentiating puts it on the **cosine**, integrating puts it on the **sine**.


*Blanks: 0 — answers: []*

Spec links: `spcpt_wyhNQnwTntpyh6Zq`

Flags: fitb_no_blank_marker


## Card 2 — true_or_false (`fl_j6VxcKvCpynZfdtG`)

**FRONT**

**True or False?**

`\int \cos 3 x \text{ d} x = \sin 3 x + c`


**BACK**

**False.**

The answer is $\frac{1}{3} \mathrm{sin} 3 x + c$, because differentiating $\mathrm{sin} 3 x$ would produce an extra factor of $3$ that has to be divided out.

The same adjustment applies to $\text{e}^{kx}$ and to any other function of a multiple of $x$.


Spec links: `spcpt_wyhNQnwTntpyh6Zq`


## Card 3 — question_and_answer (`fl_bPjj3q3Hfm8nhtTc`)

**FRONT**

What is `\int \frac{1}{x} \text{ d} x`, and why does it need a modulus?


**BACK**

It is `\ln \left|x\right| + c`.

The modulus is needed because $\frac{1}{x}$ is defined for negative $x$ while $\mathrm{ln} x$ is not, so without it the answer would cover only half the domain.


Spec links: `spcpt_wyhNQnwTntpyh6Zq`


## Card 4 — question_and_answer (`fl_g55RgJM6gky7mGpB`)

**FRONT**

What is `\int \tan x \text{ d} x`?


**BACK**

It is `\ln \left|\sec x\right| + c`.

This one is worth knowing as a standard result, since unlike most of the others it does not appear in the list of formulae.


Spec links: `spcpt_wyhNQnwTntpyh6Zq`


## Card 5 — question_and_answer (`fl_tRx5NJF8JXKXJd9g`)

**FRONT**

What is `\int \frac{1}{1 + x^{2}} \text{ d} x`?


**BACK**

It is $\mathrm{tan}^{-1} x + c$, since $\mathrm{tan}^{-1} x$ is the function whose derivative is $\frac{1}{1+x^{2}}$.

The general version is `\int \frac{1}{a^{2} + x^{2}} \text{ d} x = \frac{1}{a} \tan^{- 1} \left(\frac{x}{a}\right) + c`.


Spec links: `spcpt_wyhNQnwTntpyh6Zq`


## Card 6 — question_and_answer (`fl_ZVSNP4WYSbmKqDnk`)

**FRONT**

What are `\int \sec^{2} x \text{ d} x` and `\int \text{cosec}^{2} x \text{ d} x`?


**BACK**

They are $\mathrm{tan} x + c$ and $- \mathrm{cot} x + c$.

Both are just the matching derivatives read backwards, which is why neither needs an identity first.


Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`


## Card 7 — question_and_answer (`fl_X3F5yx4tz8z4v2Dk`)

**FRONT**

How do you integrate $\mathrm{tan}^{2} x$ and $\mathrm{cot}^{2} x$?


**BACK**

Rewrite each one first: $\mathrm{tan}^{2} x = \mathrm{sec}^{2} x - 1$ and $\mathrm{cot}^{2} x = \text{cosec}^{2} x - 1$.

Neither squared function can be integrated as it stands, but both of the rearranged pieces can be.


Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`


## Card 8 — fill_in_the_blanks (`fl_gwJFfzympcvtFxcZ`)

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


## Card 9 — question_and_answer (`fl_hvr2cvG2fjxKyjH6`)

**FRONT**

How do you integrate $\mathrm{sin} 6 x \mathrm{cos} 6 x$?


**BACK**

Use $\mathrm{sin} 2 A \equiv 2 \mathrm{sin} A \mathrm{cos} A$ with $A = 6 x$, so that $\mathrm{sin} 6 x \mathrm{cos} 6 x = \frac{1}{2} \mathrm{sin} 12 x$.

That replaces a product with a single term, and the integral comes out as $- \frac{1}{24} \mathrm{cos} 12 x + c$.


Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`


## Card 10 — true_or_false (`fl_cfw3vz9sDH3bT8w8`)

**FRONT**

**True or False?**

Integrating $\mathrm{sin} x \mathrm{cos}^{3} x$ requires a trigonometric identity.


**BACK**

**False.**

No identity is needed, because $\mathrm{sin} x$ is already the derivative of $\mathrm{cos} x$, apart from a sign.

The integral is $- \frac{1}{4} \mathrm{cos}^{4} x + c$, and the expression only looks as though it wants an identity because of the two trigonometric factors.


Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`


## Card 11 — true_or_false (`fl_dZ7DDV6P9NzqbtmR`)

**FRONT**

**True or False?**

Two students integrate $\mathrm{sin} x \mathrm{cos} x$ and get $- \frac{1}{4} \mathrm{cos} 2 x$ and $\frac{1}{2} \mathrm{sin}^{2} x$. Both can be right.


**BACK**

**True.**

The two expressions differ by the constant $\frac{1}{4}$, and the arbitrary constant of integration absorbs any difference of that kind.

Differentiating each of them is the quickest way to confirm that both are genuine antiderivatives.


Spec links: `spcpt_4gB9kJCGSJWph7Rs` `spcpt_23tNQxHx7XQvT4bw`


## Card 12 — fill_in_the_blanks (`fl_t62bvYDztNSrRPbv`)

**FRONT**

Complete the standard result:

`\int \frac{\text{f} ' \left(x\right)}{\text{f} \left(x\right)} \text{d} x = \_\_\_\_\_\_`


**BACK**

The completed result is:

`\int \frac{\text{f} ' \left(x\right)}{\text{f} \left(x\right)} \text{d} x = \ln \left|\text{f} \left(x\right)\right| + c`

The modulus is there for the same reason as in `\int \frac{1}{x} \text{d} x`: the logarithm needs a positive argument.


*Blanks: 0 — answers: []*

Spec links: `spcpt_JwrdCCvhVRQqRksD`

Flags: fitb_no_blank_marker


## Card 13 — question_and_answer (`fl_wx4qmT7bM4DkhRRn`)

**FRONT**

How do you test whether a fraction is of the form `\frac{\text{f} ' \left(x\right)}{\text{f} \left(x\right)}`?


**BACK**

**Differentiate the denominator** and compare the result with the numerator.

Ignore any coefficients while comparing: if the two match apart from a constant multiple, the form applies.


Spec links: `spcpt_JwrdCCvhVRQqRksD`


## Card 14 — question_and_answer (`fl_4ffgNGk88VCrwB64`)

**FRONT**

The numerator is a constant multiple of the derivative of the denominator, but not equal to it. What do you do?


**BACK**

Adjust for that constant, exactly as in the reverse chain rule.

In `\int \frac{x}{x^{2} + 1} \text{d} x` the denominator differentiates to $2 x$, so write it as `\frac{1}{2} \int \frac{2 x}{x^{2} + 1} \text{d} x`, giving `\frac{1}{2} \ln \left|x^{2} + 1\right| + c`.


Spec links: `spcpt_JwrdCCvhVRQqRksD`


## Card 15 — true_or_false (`fl_TBSGCt2rDZJrkXDM`)

**FRONT**

**True or False?**

`\int \frac{2 x + 1}{x^{2} + x} \text{d} x = \ln \left|x^{2} + x\right| + c`


**BACK**

**True.**

Differentiating $x^{2} + x$ gives exactly $2 x + 1$, which is the numerator, so there is no constant to adjust for.

This is the cleanest form the pattern takes.


Spec links: `spcpt_JwrdCCvhVRQqRksD`


## Card 16 — question_and_answer (`fl_KRJPcCs7kYBvmmYC`)

**FRONT**

Why does this pattern integrate to a logarithm?


**BACK**

Because differentiating `\ln \left(\text{f} \left(x\right)\right)` gives `\frac{\text{f} ' \left(x\right)}{\text{f} \left(x\right)}`, by the chain rule.

The integral is that result read backwards, which is why no separate rule has to be learned for it.


Spec links: `spcpt_JwrdCCvhVRQqRksD`


## Card 17 — keyword_definition (`fl_yR26ndYWcMPPsPGr`)

**FRONT**

Define **integration by substitution**.


**BACK**

Replacing part of an integrand with a single new variable $u$, so that the integral becomes one you can do.

It is the formal counterpart of the reverse chain rule: the same underlying process, written out in full rather than spotted.


Spec links: `spcpt_2Z5vBCjNv9Ydr5b3`


## Card 18 — question_and_answer (`fl_xJ5rbNT76sYYz7Fr`)

**FRONT**

Why can $\frac{\text{d}u}{\text{d}x}$ be treated like a fraction here?


**BACK**

It is shorthand for swapping $\text{d} x$ for $\text{d} u$, and it is a licensed step in a substitution even though $\frac{\text{d}y}{\text{d}x}$ must never be split when rearranging an implicit derivative.

From $u = x^{2} + 1$, $\frac{\text{d}u}{\text{d}x} = 2 x$ is used in the form $\text{d} u = 2 x \text{d} x$.


Spec links: `spcpt_2Z5vBCjNv9Ydr5b3`


## Card 19 — question_and_answer (`fl_MDHMgSHHwVzJ5tzn`)

**FRONT**

What has to be replaced when you substitute?


**BACK**

**Everything.** Every $x$ term must become a $u$ term, including the $\text{d} x$.

An integral containing both letters cannot be integrated, so anything left in $x$ has to be dealt with before you go on.


Spec links: `spcpt_2Z5vBCjNv9Ydr5b3`


## Card 20 — question_and_answer (`fl_3bns9XhWxjp5M7c4`)

**FRONT**

For a definite integral, what happens to the limits under a substitution?


**BACK**

They must be converted from $x$ values into $u$ values, using the substitution itself.

Doing so lets you evaluate straight away in $u$; leaving them means substituting $x$ back in first.


Spec links: `spcpt_2Z5vBCjNv9Ydr5b3`


## Card 21 — true_or_false (`fl_Bt7qBRQs2Q5yMqDY`)

**FRONT**

**True or False?**

After integrating in $u$, you must always substitute $x$ back in.


**BACK**

**False.**

For an **indefinite** integral you must, because the answer has to be a function of $x$.

For a **definite** integral whose limits have already been converted to $u$, you can evaluate in $u$ and never return to $x$ at all.


Spec links: `spcpt_2Z5vBCjNv9Ydr5b3`


## Card 22 — question_and_answer (`fl_NdSXvpqmXZqzftpH`)

**FRONT**

What is different about a harder substitution question?


**BACK**

The substitution is **given to you**, because it is not one you would be expected to spot.

The method that follows is exactly the same as before; it is the algebra in between that gets heavier.


Spec links: `spcpt_XhXVThpfcZ9CPFM8`


## Card 23 — question_and_answer (`fl_VjRg94mV9D5PzhKw`)

**FRONT**

You are given the substitution $u = \sqrt{x+1}$. How do you get $\text{d} x$ in terms of $\text{d} u$?


**BACK**

Rearrange the substitution first, then differentiate: squaring gives $x = u^{2} - 1$, so $\frac{\text{d}x}{\text{d}u} = 2 u$ and $\text{d} x = 2 u \text{d} u$.

Rearranging before differentiating is usually easier than differentiating a root as it stands.


Spec links: `spcpt_XhXVThpfcZ9CPFM8`


## Card 24 — question_and_answer (`fl_8x4k2Jr2qjzQr7B9`)

**FRONT**

Why is it useful to rearrange a given substitution to make $x$ the subject?


**BACK**

Because the integrand usually contains $x$ terms that are not part of the obvious swap, and those have to be converted too.

With $u = \sqrt{x+1}$, rearranging to $x = u^{2} - 1$ gives a ready replacement for every one of them.


Spec links: `spcpt_XhXVThpfcZ9CPFM8`


## Card 25 — true_or_false (`fl_7Y6tMd8Z3vzYV8Kg`)

**FRONT**

**True or False?**

Being given the substitution makes the question easier than having to find it yourself.


**BACK**

**False.**

The substitution is given precisely because it is not one you would be expected to find, and the algebra that follows it is heavier than in a standard substitution question.

What you are handed removes one difficulty and signals another.


Spec links: `spcpt_XhXVThpfcZ9CPFM8`


## Card 26 — question_and_answer (`fl_RcypWq3wvsKcc729`)

**FRONT**

How do you know a harder substitution has been carried out correctly?


**BACK**

The integral should contain **only** $u$ and $\text{d} u$, with no $x$ left anywhere, and it should be something you can actually integrate.

If it is no simpler than what you started with, the substitution has been applied wrongly rather than chosen wrongly, since it was chosen for you.


Spec links: `spcpt_XhXVThpfcZ9CPFM8`


## Card 27 — fill_in_the_blanks (`fl_yP8mf437dQmBhVS6`)

**FRONT**

Complete the integration by parts formula:

`\int u \frac{\text{d} v}{\text{d} x} \text{d} x = u v - \_\_\_\_\_\_`


**BACK**

The completed formula is:

`\int u \frac{\text{d} v}{\text{d} x} \text{d} x = u v - \int v \frac{\text{d} u}{\text{d} x} \text{d} x`

Note that the product being integrated is made from $u$ and $\frac{\text{d}v}{\text{d}x}$, not from $u$ and $v$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_ysNvB269Jc4fKjT3`

Flags: fitb_no_blank_marker


## Card 28 — question_and_answer (`fl_3xBMxJthzs8cMN66`)

**FRONT**

Which differentiation rule does integration by parts reverse?


**BACK**

The **product rule**, which is why it is the method for integrating a product of two functions.

That makes it the counterpart of the reverse chain rule, which undoes the chain rule instead.


Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 29 — question_and_answer (`fl_Qq5dVvdKHQBzdPtP`)

**FRONT**

How do you choose $u$ and $\frac{\text{d}v}{\text{d}x}$?


**BACK**

Take $u$ to be the part that becomes **simpler** when differentiated, and $\frac{\text{d}v}{\text{d}x}$ to be a part you can integrate easily.

No rule always works, so if the second integral comes out harder than the first, swap the two choices over and start again.


Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 30 — question_and_answer (`fl_WVhY2fbRvQfTPcgb`)

**FRONT**

Why are $\text{e}^{x}$ and $\mathrm{sin} x$ awkward choices for $u$?


**BACK**

Because they **cycle**: differentiating them repeatedly never makes them any simpler.

$\text{e}^{x}$ returns to itself every time, and $\mathrm{sin} x$ runs through $\mathrm{cos} x$, $- \mathrm{sin} x$ and $- \mathrm{cos} x$ before coming back.


Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 31 — question_and_answer (`fl_KcpjVyBTMNvRtdsH`)

**FRONT**

How do you integrate $\mathrm{ln} x$, which is not a product at all?


**BACK**

Write it as $1 \times \mathrm{ln} x$, then take $u = \mathrm{ln} x$ and $\frac{\text{d}v}{\text{d}x} = 1$.

That gives `x \ln x - \int x \times \frac{1}{x} \text{d} x = x \ln x - x + c`.


Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 32 — true_or_false (`fl_WkWp4GwJVbMgspqr`)

**FRONT**

**True or False?**

Integration by parts can be applied more than once in the same question.


**BACK**

**True.**

If the second integral is still a product, apply the formula to that as well.

It is rare to need it more than twice, so a third application that still does not finish usually means something went wrong earlier.


Spec links: `spcpt_ysNvB269Jc4fKjT3`


## Card 33 — question_and_answer (`fl_d34hqDBqVfKwNgF8`)

**FRONT**

When should you integrate using partial fractions?


**BACK**

When the integrand is a fraction whose denominator is degree 2 or more and **factorises** into linear factors.

Splitting it turns one integral you cannot do into two or three that you can.


Spec links: `spcpt_ZFbY6XYPkJtMsk93`


## Card 34 — question_and_answer (`fl_m6Y7rcT5jTqJmcX3`)

**FRONT**

Why does integrating partial fractions usually give logarithms?


**BACK**

Because each piece has a **linear** denominator, which puts it in the `\frac{\text{f} ' \left(x\right)}{\text{f} \left(x\right)}` form up to a constant.

Each one therefore integrates to $\mathrm{ln}$ of its own denominator.


Spec links: `spcpt_ZFbY6XYPkJtMsk93`


## Card 35 — question_and_answer (`fl_GZkzkNtnGYDtccRg`)

**FRONT**

Integrate `\frac{5}{\left(x - 3\right) \left(x + 2\right)}`.


**BACK**

Split it into $\frac{1}{x-3} - \frac{1}{x+2}$, then integrate each piece separately.

That gives `\ln \left|x - 3\right| - \ln \left|x + 2\right| + c`, which tidies to `\ln \left|\frac{x - 3}{x + 2}\right| + c`.


Spec links: `spcpt_ZFbY6XYPkJtMsk93`


## Card 36 — question_and_answer (`fl_W5WxZ72t2nQRY4S6`)

**FRONT**

How do you integrate a partial fraction such as $\frac{3}{2x+1}$?


**BACK**

Adjust for the coefficient of $x$: the denominator differentiates to $2$, so the answer is `\frac{3}{2} \ln \left|2 x + 1\right| + c`.

Dropping that factor is the commonest slip once the splitting has been done correctly.


Spec links: `spcpt_ZFbY6XYPkJtMsk93`


## Card 37 — true_or_false (`fl_nbsjgX4sFvF7dysX`)

**FRONT**

**True or False?**

Any fraction with a quadratic denominator can be integrated using partial fractions.


**BACK**

**False.**

The denominator has to **factorise** into linear factors first.

$\frac{1}{x^{2}+1}$ does not split at all, and it integrates to an inverse trigonometric function instead, but that is a method beyond this course.


Spec links: `spcpt_ZFbY6XYPkJtMsk93`


## Card 38 — question_and_answer (`fl_9qQzRv6nPt2F33Xy`)

**FRONT**

What is the first thing to check when deciding how to integrate?


**BACK**

Whether it is already a **standard integral**, or can be turned into one just by rewriting.

Expanding brackets, splitting a fraction or simplifying a quotient often removes the need for any technique at all.


Spec links: `spcpt_SrFpVvthH46W55tj`


## Card 39 — question_and_answer (`fl_2tXkJqvRTYq2QnSS`)

**FRONT**

The integrand is a product of two functions. Which methods should you consider?


**BACK**

**Reverse chain rule** first, if one factor is the derivative of something sitting inside the other.

If it is not, then **integration by parts**, or a **substitution** where one factor suggests an obvious $u$.


Spec links: `spcpt_SrFpVvthH46W55tj`


## Card 40 — question_and_answer (`fl_ZmzpFyY2JnSYhRXv`)

**FRONT**

The integrand is a fraction. What does its denominator tell you?


**BACK**

A **linear** denominator points towards a logarithm, and one that **factorises** points towards partial fractions.

If the numerator is close to the derivative of the denominator, it is the `\frac{\text{f} ' \left(x\right)}{\text{f} \left(x\right)}` form.


Spec links: `spcpt_SrFpVvthH46W55tj`


## Card 41 — question_and_answer (`fl_RzzNx3XqQ3fKVB56`)

**FRONT**

Why look again for the reverse chain rule after using an identity?


**BACK**

Because rewriting an expression changes its shape, and a reverse chain rule that was not available before may be available now.

This is the easiest thing to miss, since applying the identity feels like the answer rather than a step towards it.


Spec links: `spcpt_SrFpVvthH46W55tj`


## Card 42 — true_or_false (`fl_5qqJ5vCKwhXyKwb7`)

**FRONT**

**True or False?**

If a substitution does not work, the integral cannot be done by substitution at all.


**BACK**

**False.**

A substitution failing almost always means the **wrong** $u$ was chosen, not that the method is unavailable.

The usual fix is to substitute a different part of the integrand and try again.


Spec links: `spcpt_SrFpVvthH46W55tj`

