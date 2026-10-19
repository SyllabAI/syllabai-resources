# Further Differentiation

Course: ial-maths-20-pure-3 · Section: Differentiation

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-3/flashcards/differentiation/further-differentiation/


## Card 1 — fill_in_the_blanks (`fl_wJxTbw7sWS3s5BnD`)

**FRONT**

Complete the derivatives of the three basic trigonometric functions:

`\frac{\text{d}}{\text{d} x} \left(\sin x\right) = \_\_\_\_\_\_`

`\frac{\text{d}}{\text{d} x} \left(\cos x\right) = \_\_\_\_\_\_`

`\frac{\text{d}}{\text{d} x} \left(\tan x\right) = \_\_\_\_\_\_`


**BACK**

The completed derivatives are:

`\frac{\text{d}}{\text{d} x} \left(\sin x\right) = \cos x`

`\frac{\text{d}}{\text{d} x} \left(\cos x\right) = - \sin x`

`\frac{\text{d}}{\text{d} x} \left(\tan x\right) = \sec^{2} x`

Only the cosine picks up a minus sign, and these results hold only when $x$ is in **radians**.


*Blanks: 0 — answers: ['radians']*

Spec links: `spcpt_qMxPw37Fv75Pk8Ts`

Flags: blank_answer_mismatch


## Card 2 — question_and_answer (`fl_6N7srjMTW8MJPYq6`)

**FRONT**

What is the derivative of $\mathrm{ln} x$?


**BACK**

`\frac{\text{d}}{\text{d} x} \left(\ln x\right) = \frac{1}{x}`.

A logarithm differentiates to something with no logarithm left in it at all, which is what makes the result so useful.


Spec links: `spcpt_qMxPw37Fv75Pk8Ts`


## Card 3 — true_or_false (`fl_5vvYm6Jk2Wx4r727`)

**FRONT**

**True or False?**

The derivative of $\mathrm{ln} k x$ is $\frac{k}{x}$.


**BACK**

**False.**

The $k$ makes no difference at all, because $\mathrm{ln} k x = \mathrm{ln} k + \mathrm{ln} x$ and $\mathrm{ln} k$ is a constant, which differentiates to zero.

The derivative is therefore exactly what it would be without the $k$ there.


Spec links: `spcpt_qMxPw37Fv75Pk8Ts`


## Card 4 — question_and_answer (`fl_Kd76NZ57Shhvvj2V`)

**FRONT**

What is the derivative of $a^{x}$, for $a > 0$?


**BACK**

`\frac{\text{d}}{\text{d} x} \left(a^{x}\right) = a^{x} \ln a`.

The base is carried through untouched, and it is the natural logarithm of that base that appears alongside it as a multiplier.


Spec links: `spcpt_qMxPw37Fv75Pk8Ts`


## Card 5 — question_and_answer (`fl_xpdyqqpDQxzK29xp`)

**FRONT**

How is the derivative of $a^{kx}$ found from that of $a^{x}$?


**BACK**

By the **chain rule**, which brings the $k$ down as an extra multiplier.

So `\frac{\text{d}}{\text{d} x} \left(a^{k x}\right) = k a^{k x} \ln a`.


Spec links: `spcpt_qMxPw37Fv75Pk8Ts`


## Card 6 — question_and_answer (`fl_tYmv2QWnmCySjbKc`)

**FRONT**

What does `\frac{\text{d}}{\text{d} x} \left(a^{x}\right) = a^{x} \ln a` give when $a = \text{e}$?


**BACK**

The multiplier becomes $\mathrm{ln} \text{e}$, which is $1$, so it vanishes altogether.

That is precisely why $\text{e}$ is singled out from every other possible base.


Spec links: `spcpt_qMxPw37Fv75Pk8Ts`


## Card 7 — fill_in_the_blanks (`fl_4FXY3nBQDPWMbHFT`)

**FRONT**

If $y$ is a function of $u$, and $u$ is a function of $x$, complete the chain rule:

`\frac{\text{d} y}{\text{d} x} = \frac{\text{d} y}{\text{d} u} \times \_\_\_\_\_\_`


**BACK**

The completed rule is:

$\frac{\text{d}y}{\text{d}x} = \frac{\text{d}y}{\text{d}u} \times \frac{\text{d}u}{\text{d}x}$

The $\text{d} u$ terms look as though they cancel, which is a useful way to remember it, though it is not a proof.


*Blanks: 0 — answers: []*

Spec links: `spcpt_J6Fzys4Bj5SFqMnY`


## Card 8 — question_and_answer (`fl_bKfV8vKqjdkYd7kS`)

**FRONT**

What kind of function does the chain rule differentiate?


**BACK**

A **composite** function, meaning one function applied to the output of another.

So `\sin \left(x^{2}\right)` needs it: the squaring happens first, and the sine acts on the result.


Spec links: `spcpt_J6Fzys4Bj5SFqMnY`


## Card 9 — question_and_answer (`fl_8rKRj5m98q3BbQyF`)

**FRONT**

How do you differentiate `\left(\text{f} \left(x\right)\right)^{n}`?


**BACK**

Bring the power down, reduce it by one, and multiply by the derivative of the inside:

`n \left(\text{f} \left(x\right)\right)^{n - 1} \text{f} ' \left(x\right)`

The inside function is differentiated but not otherwise changed.


Spec links: `spcpt_J6Fzys4Bj5SFqMnY`


## Card 10 — question_and_answer (`fl_sFXz2q8bMyKCFcbz`)

**FRONT**

What does $\frac{\text{d}y}{\text{d}x} = \frac{1}{\frac{\text{d}x}{\text{d}y}}$ allow you to do?


**BACK**

Differentiate a relationship that is given as $x$ in terms of $y$, rather than the other way round.

Differentiate as it stands to get $\frac{\text{d}x}{\text{d}y}$, then take the reciprocal.


Spec links: `spcpt_J6Fzys4Bj5SFqMnY`


## Card 11 — question_and_answer (`fl_RMSTMpQqrTS6H9Bd`)

**FRONT**

What is the derivative of `\ln \left(\text{f} \left(x\right)\right)`?


**BACK**

`\frac{\text{f} ' \left(x\right)}{\text{f} \left(x\right)}`.

This shape, a derivative sitting over the original function, is worth recognising: it is the pattern that makes certain fractions integrate to a logarithm later in the course.


Spec links: `spcpt_J6Fzys4Bj5SFqMnY`


## Card 12 — true_or_false (`fl_sb7qc6WSBt2KnGm4`)

**FRONT**

**True or False?**

`\frac{\text{d}}{\text{d} x} \left(\left(3 x + 1\right)^{5}\right) = 5 \left(3 x + 1\right)^{4}`


**BACK**

**False.**

The derivative of the inside, which is $3$, has to be included as well, giving `15 \left(3 x + 1\right)^{4}`.

Forgetting that final factor is the commonest chain rule error.


Spec links: `spcpt_J6Fzys4Bj5SFqMnY`


## Card 13 — fill_in_the_blanks (`fl_Bt7WqD52z7b75hsp`)

**FRONT**

For $y = u v$, where $u$ and $v$ are functions of $x$, complete the product rule:

`\frac{\text{d} y}{\text{d} x} = u \frac{\text{d} v}{\text{d} x} + \_\_\_\_\_\_`


**BACK**

The completed rule is:

$\frac{\text{d}y}{\text{d}x} = u \frac{\text{d}v}{\text{d}x} + v \frac{\text{d}u}{\text{d}x}$

It is often remembered in the shorter form $y ' = u v ' + v u '$, and it is **not** in the formulae booklet.


*Blanks: 0 — answers: ['not']*

Spec links: `spcpt_v8zhdj7wJHgNznpD`

Flags: blank_answer_mismatch


## Card 14 — question_and_answer (`fl_H5WJSwmsWgr5bV4P`)

**FRONT**

What is the difference between a **product** of two functions and a **composite** function?


**BACK**

A product is two functions **multiplied** together, such as $x^{2} \mathrm{sin} x$.

A composite is a function **of** a function, such as `\sin \left(x^{2}\right)`, and it needs the chain rule instead.


Spec links: `spcpt_v8zhdj7wJHgNznpD`


## Card 15 — question_and_answer (`fl_4Gb7YYZsfhFSpHyK`)

**FRONT**

Why is the derivative of a product not the product of the derivatives?


**BACK**

Because each term of the product rule keeps **one** of the two functions unchanged.

Differentiating both at once, turning $x^{2} \mathrm{sin} x$ into $2 x \mathrm{cos} x$, throws that structure away entirely and gives the wrong answer.


Spec links: `spcpt_v8zhdj7wJHgNznpD`


## Card 16 — question_and_answer (`fl_NTSH9P3pPDj5PStJ`)

**FRONT**

Differentiate $y = x^{2} \mathrm{sin} x$.


**BACK**

Taking $u = x^{2}$ and $v = \mathrm{sin} x$:

$\frac{\text{d}y}{\text{d}x} = x^{2} \mathrm{cos} x + 2 x \mathrm{sin} x$

Each of the two terms still contains one of the original functions untouched, which is the pattern to check your answer against.


Spec links: `spcpt_v8zhdj7wJHgNznpD`


## Card 17 — true_or_false (`fl_5QXJjh99cPz3DMVN`)

**FRONT**

**True or False?**

In the product rule it makes no difference which function you call $u$ and which you call $v$.


**BACK**

**True.**

The two terms are added together, so swapping $u$ and $v$ simply writes the same answer in the other order.

The rule is symmetric in the two functions.


Spec links: `spcpt_v8zhdj7wJHgNznpD`


## Card 18 — fill_in_the_blanks (`fl_jptRnYsWMs57W3QK`)

**FRONT**

For $y = \frac{u}{v}$, where $u$ and $v$ are functions of $x$, complete the quotient rule:

`\frac{\text{d} y}{\text{d} x} = \frac{v \frac{\text{d} u}{\text{d} x} - u \frac{\text{d} v}{\text{d} x}}{\_\_\_\_\_\_}`


**BACK**

The completed rule is:

$\frac{\text{d}y}{\text{d}x} = \frac{v\frac{\text{d}u}{\text{d}x}-u\frac{\text{d}v}{\text{d}x}}{v^{2}}$

The denominator is the **bottom function squared**, not the derivative of anything, and the whole formula is given in the formulae booklet.


*Blanks: 0 — answers: ['bottom function squared']*

Spec links: `spcpt_NMz2QnW3vCFZCZmm`

Flags: blank_answer_mismatch


## Card 19 — question_and_answer (`fl_C4PttYhHwWNdz3pT`)

**FRONT**

Why does the order of the two terms matter in the quotient rule?


**BACK**

Because of the **minus sign** in the numerator: swapping the terms reverses the sign of the whole answer.

The term beginning with $v$, the bottom function, is the one that comes first.


Spec links: `spcpt_NMz2QnW3vCFZCZmm`


## Card 20 — question_and_answer (`fl_wHmB537rGxM2BZB4`)

**FRONT**

How can you recognise a quotient rule question written as `\text{g} \left(x\right) \left(\text{h} \left(x\right)\right)^{- 1}`?


**BACK**

A negative power applied to a whole function is a division in disguise, since `\text{g} \left(x\right) \left(\text{h} \left(x\right)\right)^{- 1} = \frac{\text{g} \left(x\right)}{\text{h} \left(x\right)}`.

It can be done with the product and chain rules instead, but the quotient rule is usually quicker.


Spec links: `spcpt_NMz2QnW3vCFZCZmm`


## Card 21 — question_and_answer (`fl_PM2n4V9vK6DHCpG2`)

**FRONT**

Differentiate $y = \frac{\mathrm{sin}x}{x}$.


**BACK**

Taking $u = \mathrm{sin} x$ and $v = x$:

$\frac{\text{d}y}{\text{d}x} = \frac{x\mathrm{cos}x-\mathrm{sin}x}{x^{2}}$

Answers from the quotient rule rarely simplify much, so leaving the result as a single fraction is normal.


Spec links: `spcpt_NMz2QnW3vCFZCZmm`


## Card 22 — true_or_false (`fl_fDkNhXDfgMVmbdWD`)

**FRONT**

**True or False?**

Every quotient has to be differentiated using the quotient rule.


**BACK**

**False.**

A quotient that simplifies should be simplified first: $\frac{x^{3}+x}{x}$ is just $x^{2} + 1$, which differentiates in one line.

The rule is for quotients that cannot be reduced to a sum of simpler terms.


Spec links: `spcpt_NMz2QnW3vCFZCZmm`


## Card 23 — fill_in_the_blanks (`fl_qXDDCRmcGGSRB3Fr`)

**FRONT**

Complete the derivatives of these reciprocal trigonometric functions:

`\frac{\text{d}}{\text{d} x} \left(\sec x\right) = \_\_\_\_\_\_`
`\frac{\text{d}}{\text{d} x} \left(\cot x\right) = \_\_\_\_\_\_`


**BACK**

The completed derivatives are:

`\frac{\text{d}}{\text{d} x} \left(\sec x\right) = \sec x \tan x`
`\frac{\text{d}}{\text{d} x} \left(\cot x\right) = - \text{cosec}^{2} x`

The third of the set is `\frac{\text{d}}{\text{d} x} \left(\text{cosec} \, x\right) = - \text{cosec} \, x \cot x`, and notice that the two functions beginning with "co" are the two carrying a minus sign.


*Blanks: 0 — answers: []*

Spec links: `spcpt_yM3rChg2z3sgcRPz`


## Card 24 — question_and_answer (`fl_ydp2dkm7DrRB6KKH`)

**FRONT**

How do you derive the derivative of $\mathrm{sec} x$?


**BACK**

Write `\sec x = \left(\cos x\right)^{- 1}` and apply the **chain rule**.

That gives `- \left(\cos x\right)^{- 2} \times \left(- \sin x\right) = \frac{\sin x}{\cos^{2} x}`, which splits into $\mathrm{sec} x \mathrm{tan} x$.


Spec links: `spcpt_yM3rChg2z3sgcRPz`


## Card 25 — question_and_answer (`fl_RGCjZmHh5vJpVmBY`)

**FRONT**

How do you derive the derivative of $\mathrm{arcsin} x$?


**BACK**

Write $y = \mathrm{arcsin} x$, so that $x = \mathrm{sin} y$, and differentiate to get $\frac{\text{d}x}{\text{d}y} = \mathrm{cos} y$.

Taking the reciprocal gives $\frac{\text{d}y}{\text{d}x} = \frac{1}{\mathrm{cos}y}$, and $\mathrm{sin}^{2} y + \mathrm{cos}^{2} y \equiv 1$ turns that into $\frac{1}{\sqrt{1-x^{2}}}$.


Spec links: `spcpt_yM3rChg2z3sgcRPz`


## Card 26 — question_and_answer (`fl_ZWzBCGqDGC6k9qQX`)

**FRONT**

For which values of $x$ is the derivative of $\mathrm{arcsin} x$ defined?


**BACK**

Only for $- 1 < x < 1$.

At $x = \pm 1$ the denominator $\sqrt{1-x^{2}}$ becomes zero, which matches the graph of $\mathrm{arcsin} x$ turning vertical at each end of its domain.


Spec links: `spcpt_yM3rChg2z3sgcRPz`

