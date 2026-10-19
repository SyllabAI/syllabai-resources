# Discrete Random Variables

Course: ial-maths-20-statistics-1 · Section: Statistical Distributions

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-1/flashcards/statistical-distributions/discrete-random-variables/


## Card 1 — keyword_definition (`fl_JW39ffJ54fbwV8Sz`)

**FRONT**

Define a **discrete random variable**.


**BACK**

A **random variable** is one whose value depends on the outcome of a random event, so it is not known until that event happens.

A **discrete** random variable can take only certain separate values within a set, and it usually **counts** something, such as the number of heads in 20 coin flips.

Random variables are written with capital letters and their particular outcomes with lower-case ones.


Spec links: `spcpt_hNzSdgbyZxJrpzwx`


## Card 2 — question_and_answer (`fl_JGC8vsWP6dqR3Gr3`)

**FRONT**

In `\text{P} \left(X = x\right)`, why is one letter a capital and the other lower case?


**BACK**

The capital $X$ is the **random variable** itself, the thing whose value is not yet known.

The lower-case $x$ is a **particular value** that it might take.

So the whole expression reads as the probability that the random variable $X$ takes the value $x$, and the two letters are doing genuinely different jobs.


Spec links: `spcpt_hNzSdgbyZxJrpzwx`


## Card 3 — true_or_false (`fl_n4qQMRHVGcC5JrHj`)

**FRONT**

**True or False?**

A discrete random variable can only take a finite number of values.


**BACK**

**False.**

Discrete means the values are **separate** from one another, not that there are finitely many of them.

The number of times a dice is rolled until it lands on a six can be $1 , 2 , 3 , \dots$ with no upper limit, and it is still discrete; what makes a variable continuous is being able to take **any** value in a range.


Spec links: `spcpt_hNzSdgbyZxJrpzwx`


## Card 4 — question_and_answer (`fl_f4ZQYNYBQmtFTzgQ`)

**FRONT**

What must a discrete probability distribution tell you, and in which three ways can it be presented?


**BACK**

It must give **every** value the random variable can take, together with the probability of each one.

It can be presented as a **table**, as a **function** (a probability mass function), or as a **vertical line graph** with the values along the horizontal axis and the probabilities up the vertical one.


Spec links: `spcpt_qBdSyWddQNFVvkBj`


## Card 5 — fill_in_the_blanks (`fl_h3Gj6TXDDXWHbV2G`)

**FRONT**

Complete the property that every discrete probability distribution has:

`\Sigma \text{P} \left(X = x\right) = \_\_\_\_\_\_`


**BACK**

The completed property is:

`\Sigma \text{P} \left(X = x\right) = 1`

The variable is certain to take one of its values, so the probabilities of all of them have to add up to 1.

This is what turns an unknown probability into an equation, so a distribution written in terms of $k$ can be solved for $k$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_qBdSyWddQNFVvkBj`


## Card 6 — question_and_answer (`fl_JhWMcKGbWD8WzrPf`)

**FRONT**

What does the cumulative distribution function `\text{F} \left(x\right)` give you?


**BACK**

`\text{F} \left(x\right) = \text{P} \left(X \le x\right)`, the probability that the random variable takes a value **less than or equal to** $x$.

You find it by adding together the probabilities of every possible value that is less than or equal to $x$.

This one is not in the formula booklet, so it is a formula to know.


Spec links: `spcpt_zVjsVNNSk6nRc5FQ`


## Card 7 — question_and_answer (`fl_f5DYQW3Hd4m8n5rg`)

**FRONT**

$X$ can take only the values 1, 2 and 3. What is `\text{P} \left(X = 5\right)`?


**BACK**

**Zero.** If a value is not one the random variable can take, the probability of it is 0.

It is worth being deliberate about this, because it makes `\text{P} \left(X \le 5\right) = 1` here: every value the variable can take already lies below 5.


Spec links: `spcpt_zVjsVNNSk6nRc5FQ`


## Card 8 — question_and_answer (`fl_dzdDxRqPQrMrwdq3`)

**FRONT**

For a discrete random variable, why must you distinguish carefully between `\text{P} \left(X < k\right)` and `\text{P} \left(X \le k\right)`?


**BACK**

Because $k$ may itself be one of the values the variable can take, and then `\text{P} \left(X = k\right)` is not zero, so the two differ by exactly that amount.

That is why `\text{P} \left(X > k\right) = 1 - \text{P} \left(X \le k\right)` while `\text{P} \left(X \ge k\right) = 1 - \text{P} \left(X < k\right)`, and picking the wrong one loses a whole term.

The wording decides which you need: **at least** $k$ means $X \geq k$, while **more than** $k$ means $X > k$.


Spec links: `spcpt_zVjsVNNSk6nRc5FQ`


## Card 9 — question_and_answer (`fl_rB85TsmHjy36FQ3h`)

**FRONT**

$X$ can take the values $- 3 , - 1 , 2$ and $4$. How do you find `\text{P} \left(X^{2} < 5\right)`?


**BACK**

Work out which of the **values** satisfy the condition, then add up their probabilities.

Here `\left(- 3\right)^{2} = 9` and $4^{2} = 16$ are both too big, while `\left(- 1\right)^{2} = 1` and $2^{2} = 4$ are not, so

`\text{P} \left(X^{2} < 5\right) = \text{P} \left(X = - 1\right) + \text{P} \left(X = 2\right)`

The negative value is the one that catches people out, because squaring it makes it positive.


Spec links: `spcpt_zVjsVNNSk6nRc5FQ`


## Card 10 — keyword_definition (`fl_yQKcHYTYRDQqJyPY`)

**FRONT**

Define the **expected value** of a discrete random variable.


**BACK**

The expected value `\text{E} \left(X\right)` is the **mean** of the random variable: what its value would average out to over very many repetitions.

It is found by multiplying each value by its probability and adding the results, `\Sigma x \text{P} \left(X = x\right)`.

That formula is given in the formula booklet.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 11 — question_and_answer (`fl_XXSw9bgJf8DCFv8b`)

**FRONT**

$X$ takes the values 1, 5 and 9 with probabilities 0.3, 0.4 and 0.3. What is `\text{E} \left(X\right)`, and how can you see it without calculating?


**BACK**

**5.** The values are spread symmetrically about 5 and their probabilities are symmetrical too, so the distribution balances there.

For a symmetrical distribution the mean is equal to the median, so spotting the symmetry saves the whole calculation.

Multiplying out gives $1 \times 0 . 3 + 5 \times 0 . 4 + 9 \times 0 . 3 = 5$, which confirms it.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 12 — true_or_false (`fl_rNqsQrmM9bqnJWff`)

**FRONT**

**True or False?**

`\text{E} \left(X^{2}\right)` is the same thing as `\left(\text{E} \left(X\right)\right)^{2}`.


**BACK**

**False.**

`\text{E} \left(X^{2}\right)` is the **mean of the squares** while `\left(\text{E} \left(X\right)\right)^{2}` is the **square of the mean**, and squaring before averaging is not the same as averaging before squaring.

Take $X$ equal to $1$ or $- 1$ with equal chance: the mean is 0 so the square of the mean is 0, but both squares are 1 so the mean of the squares is 1.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 13 — question_and_answer (`fl_7Nd7MwvtRNvgqn5y`)

**FRONT**

How do you calculate `\text{E} \left(X^{2}\right)`, and how would you calculate `\text{E} \left(\frac{1}{X}\right)`?


**BACK**

Apply the function to each **value** of $X$ first, then multiply by the probabilities and add, giving `\text{E} \left(X^{2}\right) = \Sigma x^{2} \text{P} \left(X = x\right)`.

The same recipe handles any function at all, so `\text{E} \left(\frac{1}{X}\right) = \Sigma \frac{1}{x} \text{P} \left(X = x\right)`.

The probabilities are **never** touched by the function; only the values are.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 14 — question_and_answer (`fl_gCqTTfw998hJD4FH`)

**FRONT**

How is `\text{Var} \left(X\right)` calculated for a random variable, and what is its standard deviation?


**BACK**

Using `\text{Var} \left(X\right) = \text{E} \left(X^{2}\right) - \left(\text{E} \left(X\right)\right)^{2}`, the mean of the squares minus the square of the mean, which is given in the formula booklet.

The **standard deviation** is the square root of that.

It is worth noticing that the variance of a set of data is built the same way round, as the mean of the squares minus the square of the mean.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 15 — question_and_answer (`fl_mXVfKrQyq7w6f568`)

**FRONT**

$X$ takes values between 2 and 7, and your calculation gives `\text{E} \left(X\right) = 9`. What has gone wrong?


**BACK**

Something in the calculation, because the mean of a random variable must lie **within the range of its values**.

`\text{E} \left(X\right)` is a weighted average of those values, so it can never come out larger than the largest of them or smaller than the smallest.

It could only equal one of those extremes if that value had probability 1, which would leave $X$ not really random at all.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 16 — fill_in_the_blanks (`fl_Bv2wvdgQTHnX4zHC`)

**FRONT**

Complete the two results for a linear transformation of a random variable, where $a$ and $b$ are constants:

`\text{E} \left(a X + b\right) = \_\_\_\_\_\_ \text{E} \left(X\right) + \_\_\_\_\_\_ \text{, } \text{Var} \left(a X + b\right) = \_\_\_\_\_\_ \text{Var} \left(X\right)`


**BACK**

The completed results are:

`\text{E} \left(a X + b\right) = a \text{E} \left(X\right) + b \text{, } \text{Var} \left(a X + b\right) = a^{2} \text{Var} \left(X\right)`

Neither of these is in the formula booklet, so both have to be known.

The mean is changed by the multiplication **and** by the addition, while the variance is changed by the multiplication only.


*Blanks: 0 — answers: ['and']*

Spec links: `spcpt_z62kKf5gJXGW9M9q`

Flags: blank_answer_mismatch


## Card 17 — question_and_answer (`fl_8RKPtdDNTsWQ6D2z`)

**FRONT**

Why does the $+ b$ disappear from `\text{Var} \left(a X + b\right)` but not from `\text{E} \left(a X + b\right)`?


**BACK**

Because the variance measures **spread** while the mean measures **location**.

Adding $b$ shifts every value along by the same amount, so the whole distribution slides without becoming any more or less spread out, and its centre slides with it.

Multiplying by $a$ genuinely stretches the distribution, so that does change the spread.


Spec links: `spcpt_z62kKf5gJXGW9M9q`


## Card 18 — question_and_answer (`fl_TSkWJJBMYbpSS9sK`)

**FRONT**

Why does the multiplier appear as $a^{2}$ in `\text{Var} \left(a X + b\right)` rather than as $a$?


**BACK**

Because the variance is built out of **squared** deviations, so any factor applied to the values gets squared along with them.

Multiplying every value by $a$ multiplies every deviation from the mean by $a$, and squaring those deviations then multiplies each squared deviation by $a^{2}$.


Spec links: `spcpt_z62kKf5gJXGW9M9q`


## Card 19 — question_and_answer (`fl_4pRhWgkyC4T74h4Z`)

**FRONT**

A random variable has `\text{E} \left(X\right) = 5` and `\text{Var} \left(X\right) = 4`. Find `\text{E} \left(3 X + 5\right)` and `\text{Var} \left(3 X + 5\right)`.


**BACK**

`\text{E} \left(3 X + 5\right) = 3 \times 5 + 5 = 20`, and `\text{Var} \left(3 X + 5\right) = 3^{2} \times 4 = 36`.

The $+ 5$ contributes to the mean and contributes nothing at all to the variance, while the 3 goes in as 3 for the mean and as 9 for the variance.


Spec links: `spcpt_z62kKf5gJXGW9M9q`


## Card 20 — true_or_false (`fl_W4ppH9wvVrD98yHR`)

**FRONT**

**True or False?**

`\text{Var} \left(\frac{X}{4}\right) = \frac{1}{4} \text{Var} \left(X\right)`


**BACK**

**False.**

Dividing by 4 is multiplying by $\frac{1}{4}$, so $a = \frac{1}{4}$ and the variance is multiplied by $a^{2} = \frac{1}{16}$, giving `\text{Var} \left(\frac{X}{4}\right) = \frac{1}{16} \text{Var} \left(X\right)`.

The **mean** really is divided by 4, since `\text{E} \left(\frac{X}{4}\right) = \frac{1}{4} \text{E} \left(X\right)`, which is what makes the variance version look wrong.


Spec links: `spcpt_z62kKf5gJXGW9M9q`


## Card 21 — question_and_answer (`fl_zKmbjPrzHjbvK2gh`)

**FRONT**

How do you apply the two results to `\text{Var} \left(2 - X\right)`?


**BACK**

Rewrite it as a multiplication plus an addition: `2 - X = \left(- 1\right) X + 2`, so $a = - 1$ and $b = 2$.

Then `\text{Var} \left(2 - X\right) = \left(- 1\right)^{2} \text{Var} \left(X\right) = \text{Var} \left(X\right)`.

Reversing the sign of a random variable leaves its variance completely unchanged, which is exactly what the squared multiplier guarantees.


Spec links: `spcpt_z62kKf5gJXGW9M9q`


## Card 22 — keyword_definition (`fl_MpkPyMqkbvCFW4kV`)

**FRONT**

Define a **discrete uniform distribution**.


**BACK**

A discrete random variable follows a discrete uniform distribution when there is a **finite number** of distinct outcomes and **every outcome is equally likely**.

With $n$ outcomes, `\text{P} \left(X = x\right) = \frac{1}{n}` for each of them, and 0 for anything else.

Drawn as a vertical line graph, all of its lines have **equal height**.


Spec links: `spcpt_XNbkj4YzrTHZD8Wv`


## Card 23 — fill_in_the_blanks (`fl_CCtsZQnXQ4ct84rS`)

**FRONT**

For a discrete uniform distribution whose outcomes are the integers $1 , 2 , 3 , \dots , n$, complete the mean and the variance:

`\text{E} \left(X\right) = \frac{\_\_\_\_\_\_}{2} \text{, } \text{Var} \left(X\right) = \frac{\_\_\_\_\_\_}{12}`


**BACK**

The completed formulae are:

`\text{E} \left(X\right) = \frac{n + 1}{2} \text{, } \text{Var} \left(X\right) = \frac{n^{2} - 1}{12}`

Neither of these is in the formula booklet, and neither is on the list of formulae you are told to know, so they have to be memorised or worked out from first principles.

The mean is simply the midpoint of $1$ and $n$, which is both a way of remembering it and a way of checking it.


*Blanks: 0 — answers: []*

Spec links: `spcpt_XNbkj4YzrTHZD8Wv`


## Card 24 — question_and_answer (`fl_WydfW6gNBJsKs3yP`)

**FRONT**

One of the first five Fibonacci numbers, $1 , 1 , 2 , 3 , 5$, is chosen at random. Why is the number chosen **not** discrete uniform?


**BACK**

Because the outcomes are not **equally likely**: the value 1 appears twice among the five numbers, so it is twice as likely to be picked as any of the others.

The second digit produced by a random number generator **is** discrete uniform, because its ten outcomes $0$ to $9$ really are equally likely.


Spec links: `spcpt_XNbkj4YzrTHZD8Wv`


## Card 25 — question_and_answer (`fl_JVD2q9sWgV4SRKKz`)

**FRONT**

Why can a discrete uniform distribution not model the number you get when someone is asked to write down any integer they like?


**BACK**

Because there are **infinitely many** possible outcomes, and a discrete uniform distribution needs a **finite** number of them.

With $n$ outcomes each one has probability $\frac{1}{n}$, and there is no number that can play the part of $\frac{1}{n}$ when the outcomes never run out.


Spec links: `spcpt_XNbkj4YzrTHZD8Wv`


## Card 26 — true_or_false (`fl_mrsb66vPhgMQ4J7T`)

**FRONT**

**True or False?**

A discrete uniform distribution has no mode.


**BACK**

**True.**

The mode is the most likely outcome, and here every outcome is exactly as likely as every other, so no single one of them stands out.

The distribution is symmetrical, so the **median** does exist and is equal to the mean.


Spec links: `spcpt_XNbkj4YzrTHZD8Wv`


## Card 27 — question_and_answer (`fl_2qnfYHMXSjKKyCR6`)

**FRONT**

A discrete uniform variable has outcomes $2 , 5 , 8$ and $11$ rather than $1$ to $n$. How can the standard formulae still give its mean and variance?


**BACK**

Those formulae only apply to the integers $1$ to $n$, but these outcomes form an **arithmetic sequence**, so they can be written as $Y = 3 X - 1$ where $X$ takes the values $1 , 2 , 3 , 4$.

Find `\text{E} \left(X\right)` and `\text{Var} \left(X\right)` from the standard formulae with $n = 4$, then feed them through `\text{E} \left(a X + b\right)` and `\text{Var} \left(a X + b\right)`.

The outcomes never had to be $1$ to $n$ for the distribution to be uniform; they only had to be equally likely.


Spec links: `spcpt_XNbkj4YzrTHZD8Wv`

