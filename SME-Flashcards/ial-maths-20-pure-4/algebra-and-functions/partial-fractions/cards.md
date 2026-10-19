# Partial Fractions

Course: ial-maths-20-pure-4 · Section: Algebra & Functions

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-4/flashcards/algebra-and-functions/partial-fractions/


## Card 1 — keyword_definition (`fl_pzpMvSMvbz4NmjQn`)

**FRONT**

Define **partial fractions**.


**BACK**

Writing a single algebraic fraction as a **sum** of simpler fractions with smaller denominators.

It is the reverse of adding fractions: instead of finding a common denominator, you split one back into its parts.


Spec links: `spcpt_xb6FKshx3XgKkYfc`


## Card 2 — question_and_answer (`fl_G6xftk66JtFKMPN4`)

**FRONT**

What form does a **linear factor** take?


**BACK**

`\left(a x + b\right)`, with $x$ appearing to the first power only.

A denominator that is not itself linear can often be factorised into a product of such factors, and that is what makes the method work.


Spec links: `spcpt_xb6FKshx3XgKkYfc`


## Card 3 — fill_in_the_blanks (`fl_CVnNyJhQjwn8Xbw7`)

**FRONT**

Complete the split into partial fractions:

`\frac{7 x + 1}{\left(x + 2\right) \left(x - 3\right)} \equiv \frac{A}{\_\_\_\_\_\_} + \frac{B}{\_\_\_\_\_\_}`


**BACK**

The completed split is:

`\frac{7 x + 1}{\left(x + 2\right) \left(x - 3\right)} \equiv \frac{A}{x + 2} + \frac{B}{x - 3}`

Each linear factor of the denominator gets a fraction of its own, with a constant on top.


*Blanks: 0 — answers: []*

Spec links: `spcpt_xb6FKshx3XgKkYfc`


## Card 4 — question_and_answer (`fl_B2YT8NfPb9TTQc3c`)

**FRONT**

You have written `\frac{7 x + 1}{\left(x + 2\right) \left(x - 3\right)} \equiv \frac{A}{x + 2} + \frac{B}{x - 3}`. How do you find $A$ and $B$?


**BACK**

Multiply through by the whole denominator to clear the fractions, giving `7 x + 1 \equiv A \left(x - 3\right) + B \left(x + 2\right)`.

Then substitute the values of $x$ that make each bracket zero, taking $x = 3$ and $x = - 2$ in turn.


Spec links: `spcpt_xb6FKshx3XgKkYfc`


## Card 5 — question_and_answer (`fl_dJNh79FQHKvsn3JT`)

**FRONT**

Why do you substitute the values of $x$ that make a bracket zero?


**BACK**

Because each one **kills off** all but one of the unknown constants.

That leaves a single equation in a single unknown, which is far quicker than solving the constants simultaneously.


Spec links: `spcpt_xb6FKshx3XgKkYfc`


## Card 6 — question_and_answer (`fl_xgqtpTspx3QTc8KD`)

**FRONT**

What is the alternative to substituting values of $x$?


**BACK**

**Comparing coefficients** on the two sides of the identity.

The two sides have to be equal for every value of $x$, so the number of $x^{2}$ terms, of $x$ terms and of constants must match separately.


Spec links: `spcpt_xb6FKshx3XgKkYfc`


## Card 7 — question_and_answer (`fl_JsD28WrDprS2S9xK`)

**FRONT**

What are partial fractions actually used for?


**BACK**

**Binomial expansions** and **integration**.

Both are straightforward on a simple fraction and awkward on a compound one, so splitting first is what makes them workable.


Spec links: `spcpt_xb6FKshx3XgKkYfc`


## Card 8 — question_and_answer (`fl_JrQGhWCnZdRzkbDf`)

**FRONT**

For `\frac{4 x + 1}{\left(x + 2\right) \left(x - 1\right) \left(x - 3\right)^{2}}`, how many partial fractions are needed?


**BACK**

**Four**, not three.

The squared bracket contributes **two** factors, `\left(x - 3\right)` and `\left(x - 3\right)^{2}`, and each of them needs its own fraction.


Spec links: `spcpt_f5fqHB9YCMFNPmSz`


## Card 9 — fill_in_the_blanks (`fl_ywnHg4JGypFVY6K7`)

**FRONT**

Complete the split:

`\frac{5}{\left(x + 1\right) \left(x - 4\right)^{2}} \equiv \frac{A}{x + 1} + \frac{B}{\_\_\_\_\_\_} + \frac{C}{\_\_\_\_\_\_}`


**BACK**

`\frac{5}{\left(x + 1\right) \left(x - 4\right)^{2}} \equiv \frac{A}{x + 1} + \frac{B}{x - 4} + \frac{C}{\left(x - 4\right)^{2}}`

The three constants are then found in the usual way, by multiplying through and substituting values of $x$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_f5fqHB9YCMFNPmSz`


## Card 10 — keyword_definition (`fl_Q76wM83NdNRbMPQB`)

**FRONT**

Define **squared linear factor**.


**BACK**

A factor of the form `\left(a x + b\right)^{2}`, that is a linear factor repeated.

The repetition is what makes it behave differently from two distinct linear factors.


Spec links: `spcpt_f5fqHB9YCMFNPmSz`


## Card 11 — true_or_false (`fl_JwsdfNqJbt83xHFZ`)

**FRONT**

**True or False?**

An $x^{2}$ in a denominator counts as a squared linear factor.


**BACK**

**True.**

A linear factor is `\left(a x + b\right)` and $b$ is allowed to be zero, so $x$ is linear and $x^{2}$ is its square.

Such a denominator therefore needs fractions over both $x$ and $x^{2}$.


Spec links: `spcpt_f5fqHB9YCMFNPmSz`


## Card 12 — question_and_answer (`fl_bZbkDTBTqWwXbp9y`)

**FRONT**

Why is `\frac{A}{x + 1} + \frac{B}{\left(x - 4\right)^{2}}` not a complete split of `\frac{5}{\left(x + 1\right) \left(x - 4\right)^{2}}`?


**BACK**

Because the term over `\left(x - 4\right)` is missing.

That leaves only two constants to match a numerator which in general needs three, so the identity cannot be made to hold for every value of $x$.


Spec links: `spcpt_f5fqHB9YCMFNPmSz`

