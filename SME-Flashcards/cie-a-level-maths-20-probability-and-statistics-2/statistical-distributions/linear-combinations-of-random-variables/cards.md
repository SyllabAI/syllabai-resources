# Linear Combinations of Random Variables

Course: cie-a-level-maths-20-probability-and-statistics-2 · Section: Statistical Distributions

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/flashcards/statistical-distributions/linear-combinations-of-random-variables/


## Card 1 — fill_in_the_blanks (`fl_2V4pFG5bZyTyWdGH`)

**FRONT**

For constants $a$ and $b$, fill in the two results:

`\text{E}(aX + b) = \_\_\_\_\_\_`

`\text{Var}(aX + b) = \_\_\_\_\_\_`


**BACK**

The completed results are:

$\text{E} ( a X + b ) = a \text{E} ( X ) + b$

$\text{Var} ( a X + b ) = a^{2} \text{Var} ( X )$

The mean is affected by both the multiplication and the addition, but the variance is affected only by the multiplication.

The $a$ is **squared** in the variance, because variance is built from squared deviations.


*Blanks: 0 — answers: []*

Spec links: `spcpt_ZKTsy2RrhrRGDxnH`

Flags: fitb_no_blank_marker


## Card 2 — question_and_answer (`fl_fBd3NDb6Pcw8P9vH`)

**FRONT**

Why does adding a constant leave the variance unchanged?


**BACK**

Adding a constant slides every value along by the same amount, so the whole distribution shifts without being stretched.

Variance measures **spread** about the mean, and shifting the values and the mean together leaves every deviation exactly as it was.

So $\text{Var} ( X + 7 )$ and $\text{Var} ( X )$ are the same number.


Spec links: `spcpt_ZKTsy2RrhrRGDxnH`


## Card 3 — question_and_answer (`fl_4HmwGHGMBrbw8JKz`)

**FRONT**

If $X$ is normal, is $a X + b$ normal? What if $X$ is Poisson?


**BACK**

If $X$ is normal then $a X + b$ is **also normal**, specifically $\text{N} ( a μ + b , a^{2} σ^{2} )$.

A binomial, geometric or Poisson variable does **not** keep its type: doubling a Poisson count gives only even numbers, which no Poisson distribution does.

That closure under linear change is one of the things that makes the normal distribution so convenient.


Spec links: `spcpt_ZKTsy2RrhrRGDxnH`


## Card 4 — fill_in_the_blanks (`fl_86SJfYrrk6WRtbF7`)

**FRONT**

For independent $X$ and $Y$, fill in the two results:

`\text{E}(aX + bY) = \_\_\_\_\_\_`

`\text{Var}(aX + bY) = \_\_\_\_\_\_`


**BACK**

The completed results are:

$\text{E} ( a X + b Y ) = a \text{E} ( X ) + b \text{E} ( Y )$

$\text{Var} ( a X + b Y ) = a^{2} \text{Var} ( X ) + b^{2} \text{Var} ( Y )$

The result for the expectation holds for **any** two random variables, but the one for the variance needs them to be **independent**.

Both constants are squared in the variance, exactly as in the single-variable case.


*Blanks: 0 — answers: []*

Spec links: `spcpt_Bjg5yWKMV4mBYjrW`

Flags: fitb_no_blank_marker


## Card 5 — true_or_false (`fl_7SPjdWGkGsYVRCR4`)

**FRONT**

**True or False?**

$\text{Var} ( X - Y )$ is the same as $\text{Var} ( X + Y )$ for independent $X$ and $Y$.


**BACK**

**True.**

Subtracting $Y$ is adding $- Y$, and the coefficient is **squared** in the variance, so $( - 1 )^{2} = 1$ and nothing changes.

Variances therefore **add** for a difference just as they do for a sum, which is the single most commonly lost mark in this topic.


Spec links: `spcpt_Bjg5yWKMV4mBYjrW`


## Card 6 — question_and_answer (`fl_DNdYgPSqQtfFmwJ4`)

**FRONT**

If $X$ and $Y$ are independent normal variables, what is the distribution of $a X + b Y$?


**BACK**

It is **normal** as well, with mean $a μ_{1} + b μ_{2}$ and variance $a^{2} σ_{1}^{2} + b^{2} σ_{2}^{2}$.

This is what makes questions about differences and totals of normal variables tractable at all.

It holds for a difference too, with the means subtracting while the variances still add.


Spec links: `spcpt_Bjg5yWKMV4mBYjrW`


## Card 7 — question_and_answer (`fl_bZ8zBfnd95YxY6gf`)

**FRONT**

If $X$ and $Y$ are independent Poisson variables, when is a combination of them Poisson?


**BACK**

Only for the plain **sum**: if `X \sim \text{Po}(\lambda)` and `Y \sim \text{Po}(\mu)` then `X + Y \sim \text{Po}(\lambda + \mu)`.

Once constants are involved it fails: $a X + b Y$ is **not** Poisson for values of $a$ and $b$ other than 0 and 1.

The normal is closed under any linear combination, but the Poisson is closed only under addition.


Spec links: `spcpt_Bjg5yWKMV4mBYjrW`


## Card 8 — question_and_answer (`fl_MvCzxgMZ7RvsjWyw`)

**FRONT**

$X$ and $Y$ are independent with $\text{Var} ( X ) = 3$ and $\text{Var} ( Y ) = 4$. What is $\text{Var} ( 4 X - Y )$?


**BACK**

It is $4^{2} \times 3 + ( - 1 )^{2} \times 4 = 48 + 4 = 52$.

Both coefficients are squared and the two terms are then **added**, however the original expression was signed.

Writing the squares in explicitly, rather than doing them in your head, is what stops the minus sign getting through.


Spec links: `spcpt_Bjg5yWKMV4mBYjrW`


## Card 9 — question_and_answer (`fl_yHgsBpmNhF9b22jK`)

**FRONT**

What is the difference between $2 X$ and $X_{1} + X_{2}$?


**BACK**

$2 X$ means **one** observation of $X$, doubled; $X_{1} + X_{2}$ means **two** separate observations added together.

They have the same expected value, $2 \text{E} ( X )$, but different variances: $\text{Var} ( 2 X ) = 4 \text{Var} ( X )$ while $\text{Var} ( X_{1} + X_{2} ) = 2 \text{Var} ( X )$.

If $X$ could be 0 or 1 then $2 X$ can only be 0 or 2, whereas $X_{1} + X_{2}$ can also be 1, which shows they are genuinely different variables.


Spec links: `spcpt_44sx7ZCBmc2kxvPj`


## Card 10 — question_and_answer (`fl_THNckZBtqSH9sMZ7`)

**FRONT**

A carton holds six eggs. Why is the total mass not modelled by $C + 6 E$?


**BACK**

Because the six eggs have six **different** masses, so the model must be $C + E_{1} + E_{2} + E_{3} + E_{4} + E_{5} + E_{6}$.

Writing $6 E$ would mean weighing one egg and multiplying by six, which would give a larger variance than the real situation has.

Asking whether the question means one thing repeated or several separate things is what decides between the two.


Spec links: `spcpt_44sx7ZCBmc2kxvPj`

