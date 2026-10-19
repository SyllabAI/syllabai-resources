# Differential Equations

Course: ial-maths-20-pure-4 · Section: Integration

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-4/flashcards/integration/differential-equations/


## Card 1 — question_and_answer (`fl_xzyZPVyCr6J23MB9`)

**FRONT**

What is the difference between a first order and a second order differential equation?


**BACK**

A **first order** equation contains only first derivatives, such as $\frac{\text{d}y}{\text{d}x}$.

A **second order** equation contains a second derivative, such as $\frac{\text{d}^{2}y}{\text{d}x^{2}}$.


Spec links: `spcpt_kp9mJX8PDbPPf4w6`


## Card 2 — keyword_definition (`fl_wvNCvsw6KjBp49Kr`)

**FRONT**

Define **general solution**.


**BACK**

The solution of a differential equation that still contains an arbitrary constant, written in the form `y = \text{g} \left(x\right) + c`.

Since $c$ can take any value, it describes not one curve but a whole **family** of them.


Spec links: `spcpt_kp9mJX8PDbPPf4w6`


## Card 3 — question_and_answer (`fl_cSGwQ25m4P3KzvQf`)

**FRONT**

Why does a differential equation have infinitely many solutions?


**BACK**

Because integrating introduces a constant that the equation itself does nothing to fix.

Every value of $c$ gives a curve with the right gradient function, so they all satisfy the equation and differ from one another only by a vertical shift.


Spec links: `spcpt_kp9mJX8PDbPPf4w6`


## Card 4 — question_and_answer (`fl_TZW9xkwYJGQdcRkx`)

**FRONT**

What does solving a differential equation involve?


**BACK**

**Integration**, working back from a derivative to the function itself.

Which technique is needed depends on the equation, and for many of them the variables have to be separated before you can start.


Spec links: `spcpt_kp9mJX8PDbPPf4w6`


## Card 5 — true_or_false (`fl_ZC5xt9gphzMX4RVW`)

**FRONT**

**True or False?**

Every member of the family of solutions has the same gradient at a given value of $x$.


**BACK**

**True.**

The curves differ only in the value of $c$, which shifts them vertically without changing any gradient.

That is exactly why the differential equation cannot tell them apart: it describes the gradient and nothing else.


Spec links: `spcpt_kp9mJX8PDbPPf4w6`


## Card 6 — keyword_definition (`fl_TNtx3sqRFbrQ3DX6`)

**FRONT**

Define **particular solution**.


**BACK**

The single member of the family of solutions that satisfies a given extra piece of information.

Finding it means pinning down the one value of $c$ that fits, so the answer is one curve rather than infinitely many.


Spec links: `spcpt_JfCD3zwDvrF2qW4F`


## Card 7 — keyword_definition (`fl_ZhVGyVTZJdB6Y3Vx`)

**FRONT**

Define **boundary condition**.


**BACK**

A piece of extra information giving the value of one variable when the other is known, which is what fixes the constant of integration.

An example is $y = 4$ when $x = 0$.


Spec links: `spcpt_JfCD3zwDvrF2qW4F`


## Card 8 — question_and_answer (`fl_FgmZnywjTvprR2V3`)

**FRONT**

When is a boundary condition called an **initial condition**?


**BACK**

When it describes the situation at the **start** of a model or experiment.

That usually means $t = 0$, so an initial condition is simply a boundary condition placed at the beginning of the timescale.


Spec links: `spcpt_JfCD3zwDvrF2qW4F`


## Card 9 — question_and_answer (`fl_V97DGgp864jx4CVq`)

**FRONT**

How many conditions are needed to find the particular solution of a differential equation?


**BACK**

**One.**

Integrating once introduces a single constant of integration, and one boundary condition is enough to fix its value.

Knowing $y=4$ when $x=0$ is exactly such a condition.


Spec links: `spcpt_JfCD3zwDvrF2qW4F`


## Card 10 — true_or_false (`fl_3nCQpD5QnPgVwF3m`)

**FRONT**

**True or False?**

A boundary condition has to describe the start of the situation.


**BACK**

**False.**

It can describe **any** known pairing of the two variables, at any point at all.

A particle coming to rest after a certain time gives a perfectly good boundary condition, and it is nowhere near the start.


Spec links: `spcpt_JfCD3zwDvrF2qW4F`


## Card 11 — question_and_answer (`fl_5d4NcM6mgw32TVBF`)

**FRONT**

What makes a differential equation **separable**?


**BACK**

It can be written as a **product** of a function of $x$ and a function of $y$, that is `\frac{\text{d} y}{\text{d} x} = \text{f} \left(x\right) \text{g} \left(y\right)`.

That form is what allows every $y$ term to be moved to one side and every $x$ term to the other.


Spec links: `spcpt_sH6wmW3VVsjtnMYT`


## Card 12 — question_and_answer (`fl_nJHyfgg6mRvSCb5S`)

**FRONT**

Is `\frac{\text{d} y}{\text{d} x} = \text{g} \left(y\right)` separable, when there is no $x$ in it at all?


**BACK**

Yes. Read it as `\frac{\text{d} y}{\text{d} x} = 1 \times \text{g} \left(y\right)`, so that `\text{f} \left(x\right) = 1`.

Separating then gives `\int \frac{1}{\text{g} \left(y\right)} \text{d} y = \int 1 \text{d} x`, and the right-hand side simply integrates to $x$.


Spec links: `spcpt_sH6wmW3VVsjtnMYT`


## Card 13 — question_and_answer (`fl_mNz6dKSBBC94QR3d`)

**FRONT**

What are the steps of separation of variables?


**BACK**

Get every $y$ term with the $\text{d} y$ on one side and every $x$ term with the $\text{d} x$ on the other, then **integrate both sides**.

Use any boundary condition to find the constant, and rearrange into whatever form the question asks for.


Spec links: `spcpt_sH6wmW3VVsjtnMYT`


## Card 14 — fill_in_the_blanks (`fl_yvyKnNDVkfkSqj6h`)

**FRONT**

Complete the statement, filling in what is added after integrating both sides:

`\int \frac{1}{\text{g} \left(y\right)} \text{d} y = \int \text{f} \left(x\right) \text{d} x + \_\_\_\_\_\_`


**BACK**

The completed statement is:

`\int \frac{1}{\text{g} \left(y\right)} \text{d} y = \int \text{f} \left(x\right) \text{d} x + c`

Only **one** constant is needed rather than one for each side, since two would immediately combine into a single overall constant anyway.


*Blanks: 0 — answers: ['one']*

Spec links: `spcpt_sH6wmW3VVsjtnMYT`

Flags: blank_answer_mismatch


## Card 15 — true_or_false (`fl_kqwfqZKNdphHR3ny`)

**FRONT**

**True or False?**

Every first order differential equation can be solved by separating the variables.


**BACK**

**False.**

The right-hand side has to be a **product** of a function of $x$ and a function of $y$ before the two can come apart.

$\frac{\text{d}y}{\text{d}x} = x + y$ cannot be separated at all, and solving it needs a method beyond this course.


Spec links: `spcpt_sH6wmW3VVsjtnMYT`


## Card 16 — question_and_answer (`fl_6Mv6Zc5xdmRMvJmF`)

**FRONT**

What phrase in a question tells you a differential equation is needed?


**BACK**

**"Rate of change"**, which always signals a derivative term.

A rate measured against time gives $\frac{\text{d}V}{\text{d}t}$ or similar, so the phrase translates straight into notation.


Spec links: `spcpt_fT888hj3nWRtGBpn`


## Card 17 — question_and_answer (`fl_9XcsvwPTgWWb3mH8`)

**FRONT**

How do you write "the rate of change of $y$ is directly proportional to $y$" as an equation?


**BACK**

$\frac{\text{d}y}{\text{d}t} = k y$, introducing a constant of proportionality $k$.

Inversely proportional to $y$ would give $\frac{\text{d}y}{\text{d}t} = \frac{k}{y}$ instead.


Spec links: `spcpt_fT888hj3nWRtGBpn`


## Card 18 — question_and_answer (`fl_VqcgZMBXQqpvRrHv`)

**FRONT**

What does the instruction **formulate** ask you to do?


**BACK**

Write the situation as an **equation**.

You may have to choose and define your own letters first, such as $V$ for a volume and $h$ for a height, since working that uses undefined letters cannot be followed.


Spec links: `spcpt_fT888hj3nWRtGBpn`


## Card 19 — question_and_answer (`fl_Ww4fxQnDMRcbRVyS`)

**FRONT**

A quantity is **decreasing**. What must its differential equation show?


**BACK**

A **negative** rate of change, so the equation reads $\frac{\text{d}y}{\text{d}t} = - k y$ with $k$ taken positive.

Cooling, decay and anything draining away all need that minus sign, and leaving it out models growth instead.


Spec links: `spcpt_fT888hj3nWRtGBpn`


## Card 20 — true_or_false (`fl_5pnTVRGdDJJY8kvs`)

**FRONT**

**True or False?**

Setting up a differential equation and solving it are the same skill.


**BACK**

**False.**

Setting one up is a translation from words into notation; solving it is integration.

A question can perfectly well ask you to formulate an equation without ever asking you to solve it.


Spec links: `spcpt_fT888hj3nWRtGBpn`


## Card 21 — question_and_answer (`fl_9GThZYYw2nzr4Z98`)

**FRONT**

After solving, a model gives $\mathrm{ln} y = k t + c$. How do you put it in a useful form?


**BACK**

Take exponentials of both sides: $y = \text{e}^{kt+c} = \text{e}^{c} \text{e}^{kt}$.

Since $\text{e}^{c}$ is just another constant, rename it $A$, giving $y = A \text{e}^{kt}$, the standard growth and decay form.


Spec links: `spcpt_PnxgBf2qYcvSjRfZ`


## Card 22 — question_and_answer (`fl_mhrY8vBtv6BjBWBj`)

**FRONT**

Once you have the particular solution, what can you do with it?


**BACK**

Substitute any value of the independent variable to **predict** the quantity at that moment.

The solution is an ordinary function, so a temperature after four minutes, or sales after three months, is only a substitution away.


Spec links: `spcpt_PnxgBf2qYcvSjRfZ`


## Card 23 — question_and_answer (`fl_mn9BqgVCKKV7Jqtf`)

**FRONT**

A model gives $y = A \text{e}^{kt}$. How do you find **when** $y$ reaches a given value?


**BACK**

Substitute that value and solve for $t$, which needs **logarithms** because $t$ sits in the power.

It is the reverse of predicting the quantity at a known time, and the algebra runs the other way round.


Spec links: `spcpt_PnxgBf2qYcvSjRfZ`


## Card 24 — question_and_answer (`fl_RWdjsHwd7mXsSgdH`)

**FRONT**

A cooling model solves to $T = 20 + A \text{e}^{-kt}$. What does that say about the long term?


**BACK**

That $T$ approaches $20$ without ever quite reaching it, since $A \text{e}^{-kt}$ tends to zero but is never zero.

The $20$ is the temperature of the surroundings, and reading it straight off the solution is what interpreting a model looks like.


Spec links: `spcpt_PnxgBf2qYcvSjRfZ`


## Card 25 — true_or_false (`fl_qp6CFgXtchx4HKf3`)

**FRONT**

**True or False?**

A differential equation model needs a boundary condition before it can be used to predict anything.


**BACK**

**True.**

Without one you have only the general solution, which is a whole family of curves rather than a single prediction.

Modelling questions therefore almost always supply one, most often the value at $t = 0$.


Spec links: `spcpt_PnxgBf2qYcvSjRfZ`

