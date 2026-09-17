# Further Integration

Course: ial-maths-20-pure-3 · Section: Integration

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-3/flashcards/integration/further-integration/


## Card 1 — fill_in_the_blanks (`fl_bpRcK42xjts6GxnG`)

**FRONT**

Complete the two standard trigonometric integrals:

`\int \sin x \text{d} x = \_\_\_\_\_\_`

`\int \cos x \text{d} x = \_\_\_\_\_\_`


**BACK**

The completed integrals are:

`\int \sin x \text{d} x = - \cos x + c`

`\int \cos x \text{d} x = \sin x + c`

The minus sign attaches to the integral of $\mathrm{sin}$, which is the opposite way round from differentiation, where it attaches to $\mathrm{cos}$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_JSx6YPY39mt6vdzt`


## Card 2 — question_and_answer (`fl_hsx87T7yGHbkR9wb`)

**FRONT**

Why does an indefinite integral always end in $+ c$?


**BACK**

Because a constant differentiates to **zero**, so infinitely many functions share the same derivative.

The $+ c$ stands for all of them at once, and it is dropped only once limits are applied.


Spec links: `spcpt_JSx6YPY39mt6vdzt`


## Card 3 — question_and_answer (`fl_Q9yq5sz5w255sG7m`)

**FRONT**

What is `\int \text{e}^{k x} \text{d} x`?


**BACK**

$\frac{1}{k} \text{e}^{kx} + c$.

Differentiating $\text{e}^{kx}$ multiplies by $k$, so going the other way has to divide by it.


Spec links: `spcpt_JSx6YPY39mt6vdzt`


## Card 4 — question_and_answer (`fl_3HKyhWBGVT6ykJ7K`)

**FRONT**

Why can the rule for integrating $x^{n}$ not be used on $\frac{1}{x}$?


**BACK**

Because $\frac{1}{x} = x^{-1}$, and raising that index by $1$ would leave a denominator of zero.

The integral is `\ln \left| x \right| + c` instead, which is why this one has to be learned separately.


Spec links: `spcpt_JSx6YPY39mt6vdzt`


## Card 5 — true_or_false (`fl_hshT9KNvTy8YswjT`)

**FRONT**

**True or False?**

Any of these standard integrals can be checked by differentiating the answer.


**BACK**

**True.**

Integration is the reverse of differentiation, so differentiating your answer has to return what you started with.

It is the quickest way to settle a sign you are unsure of.


Spec links: `spcpt_JSx6YPY39mt6vdzt`


## Card 6 — question_and_answer (`fl_Y66TCV7kjsT3pg8w`)

**FRONT**

What is `\int \tan x \text{d} x`?


**BACK**

`\ln \left| \sec x \right| + c`.

The modulus is needed because $\mathrm{sec} x$ takes negative values as well as positive ones, and a logarithm cannot accept those.


Spec links: `spcpt_JSx6YPY39mt6vdzt`


## Card 7 — question_and_answer (`fl_hMXnD9NDZbF6CyXf`)

**FRONT**

What does the reverse chain rule undo?


**BACK**

A differentiation that used the **chain rule**, so the integrand is a composite function multiplied by the derivative of its inside.

Recognising that shape is what lets you integrate by inspection, without setting up a formal substitution.


Spec links: `spcpt_D4wJgrNQvPv7GK8x`


## Card 8 — question_and_answer (`fl_MWFRGvKZDFJJyyhv`)

**FRONT**

What are the steps of the reverse chain rule?


**BACK**

Spot the **main** function, write down what would differentiate to give it, then **adjust and compensate** for any constant that the chain rule would have produced.

Simplify at the end.


Spec links: `spcpt_D4wJgrNQvPv7GK8x`


## Card 9 — question_and_answer (`fl_Gqw5rvY78FTK5vH4`)

**FRONT**

What does it mean to "adjust and compensate" when integrating?


**BACK**

Put in the constant your answer needs, then multiply by its reciprocal outside, so that nothing has actually been changed.

Integrating $\text{e}^{5x}$ needs a $5$ from the chain rule, so you write $\frac{1}{5} \text{e}^{5x}$: the $\frac{1}{5}$ compensates for the $5$ that differentiating would bring out.


Spec links: `spcpt_D4wJgrNQvPv7GK8x`


## Card 10 — question_and_answer (`fl_rWxQhnHjdV8ynr2j`)

**FRONT**

How can you check an integration answer?


**BACK**

**Differentiate it.** You should get back exactly what you set out to integrate.

This is worth doing whenever the integral was reached by inspection rather than by a formal method, because inspection is where a constant is most easily dropped.


Spec links: `spcpt_D4wJgrNQvPv7GK8x`


## Card 11 — true_or_false (`fl_Bngp9dh2CfyKFjXq`)

**FRONT**

**True or False?**

The reverse chain rule works whenever the integrand is a composite function.


**BACK**

**False.**

The derivative of the inside function has to be present as well, at least up to a constant multiple.

`\int 2 x \text{e}^{x^{2}} \text{d} x` works because the $2 x$ is the derivative of $x^{2}$, whereas `\int \text{e}^{x^{2}} \text{d} x` cannot be done at all by elementary means.


Spec links: `spcpt_D4wJgrNQvPv7GK8x`


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


## Card 17 — question_and_answer (`fl_WpX5WkTYcSQxn69W`)

**FRONT**

Why do you sometimes need a trigonometric identity before integrating?


**BACK**

Because the expression as written is not one of the standard integrals, but an identity can turn it into one that is.

Most often it is a **squared** trigonometric term that has to be rewritten.


Spec links: `spcpt_phxNfbj7rSHTghdc`


## Card 18 — question_and_answer (`fl_tFmpH6DCfXvbDg8H`)

**FRONT**

How do you integrate $\mathrm{sin}^{2} x$ or $\mathrm{cos}^{2} x$?


**BACK**

Rewrite them with the double angle identity for $\mathrm{cos} 2 A$, which turns a square into a linear expression in $\mathrm{cos} 2 x$.

From $\mathrm{cos} 2 x = 1 - 2 \mathrm{sin}^{2} x$ you get `\sin^{2} x = \frac{1}{2} \left(1 - \cos 2 x\right)`, which integrates term by term.


Spec links: `spcpt_phxNfbj7rSHTghdc`


## Card 19 — question_and_answer (`fl_pycBdJN6Br5rZxFt`)

**FRONT**

How do you integrate $\mathrm{sin} 3 x \mathrm{cos} 3 x$?


**BACK**

Use $\mathrm{sin} 2 A = 2 \mathrm{sin} A \mathrm{cos} A$ backwards, which gives $\mathrm{sin} 3 x \mathrm{cos} 3 x = \frac{1}{2} \mathrm{sin} 6 x$.

That is a standard integral, so the answer is $- \frac{1}{12} \mathrm{cos} 6 x + c$.


Spec links: `spcpt_phxNfbj7rSHTghdc`


## Card 20 — fill_in_the_blanks (`fl_r9STxPp27dXPT3fw`)

**FRONT**

Complete the identities used to integrate these squared functions:

`\tan^{2} x = \_\_\_\_\_\_ - 1`
`\cot^{2} x = \_\_\_\_\_\_ - 1`


**BACK**

The completed identities are:

$\mathrm{tan}^{2} x = \mathrm{sec}^{2} x - 1$
$\mathrm{cot}^{2} x = \text{cosec}^{2} x - 1$

Each turns a square you cannot integrate directly into one you can, since $\mathrm{sec}^{2} x$ and $\text{cosec}^{2} x$ are both standard integrals.


*Blanks: 0 — answers: []*

Spec links: `spcpt_phxNfbj7rSHTghdc`


## Card 21 — true_or_false (`fl_fJbMSNzsMfP7trCG`)

**FRONT**

**True or False?**

`\int \sin^{4} x \cos x \text{d} x` needs a trigonometric identity.


**BACK**

**False.**

It looks as though it should, but $\mathrm{cos} x$ is the derivative of $\mathrm{sin} x$, so this is a **reverse chain rule** integral and the answer is $\frac{1}{5} \mathrm{sin}^{5} x + c$.

Anything of the form $\mathrm{sin}^{n} k x \mathrm{cos} k x$ behaves the same way and needs no identity at all.


Spec links: `spcpt_phxNfbj7rSHTghdc`

