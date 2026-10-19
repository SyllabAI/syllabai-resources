# Binomial Distribution

Course: ial-maths-20-statistics-2 · Section: Statistical Distributions

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-2/flashcards/statistical-distributions/binomial-distribution/


## Card 1 — keyword_definition (`fl_S4YWB4NXT8G6yBGX`)

**FRONT**

Define a **binomial distribution**.


**BACK**

A **binomial distribution** is the discrete probability distribution of a random variable that **counts the number of successes** in a fixed number of trials.

It is written `X \sim \text{B} \left(n , p\right)`, where $n$ is the number of trials and $p$ is the probability of success on any one of them.

The probability of failure is $1 - p$, sometimes written as $q$, and $X$ can take any whole-number value from 0 to $n$.


Spec links: `spcpt_CFPBfrF9PVcrbCk6`


## Card 2 — fill_in_the_blanks (`fl_9K2V3JKT6c4sDftw`)

**FRONT**

A binomial model needs four conditions to hold. Fill in the two that are missing:

the number of trials, $n$, is `\_\_\_\_\_\_`

the trials are **independent** of one another

each trial has exactly **two** outcomes, success or failure

the probability of success, $p$, is `\_\_\_\_\_\_`


**BACK**

The completed conditions are:

the number of trials, $n$, is **fixed**

the probability of success, $p$, is **constant**

None of the four conditions is in the formula booklet, so all four have to be remembered, and a model is ruled out if even one of them breaks.

The number of emails arriving in an hour is the standard example of a count with no fixed $n$ at all.


*Blanks: 0 — answers: ['fixed', 'constant']*

Spec links: `spcpt_CFPBfrF9PVcrbCk6`

Flags: blank_answer_mismatch


## Card 3 — question_and_answer (`fl_7mM7kSKq3qydsg9n`)

**FRONT**

How is the binomial probability formula related to the expansion of `\left(p + q\right)^{n}`, where $q = 1 - p$?


**BACK**

`\text{P} \left(X = r\right)` is exactly the term containing $p^{r}$ in that expansion, which is where the binomial coefficient in the formula comes from.

Since $p + q = 1$, the whole expansion comes to $1^{n} = 1$, so the probabilities of $0 , 1 , \dots , n$ successes are guaranteed to add up to 1.


Spec links: `spcpt_CFPBfrF9PVcrbCk6`


## Card 4 — question_and_answer (`fl_jcmGZbk5dZ82rprK`)

**FRONT**

A biologist models the number of seeds that germinate out of 200 as `X \sim \text{B} \left(200 , 0 . 9\right)`. Find the mean and the variance.


**BACK**

The formula booklet gives `\text{E} \left(X\right) = n p` and `\text{Var} \left(X\right) = n p \left(1 - p\right)`, so the mean is $200 \times 0 . 9 = 180$ and the variance is $200 \times 0 . 9 \times 0 . 1 = 18$.

The standard deviation is $\sqrt{18}$, which is about 4.24, so almost every outcome lies within about 13 seeds of 180.

Notice how much smaller the variance is than the mean, which is a quick check that $p$ and $1 - p$ have not been put in the wrong places.


Spec links: `spcpt_CFPBfrF9PVcrbCk6`


## Card 5 — question_and_answer (`fl_xGnrhXtYQnPr5Xg7`)

**FRONT**

How does the shape of a binomial distribution depend on $p$?


**BACK**

With $p$ close to 0 the vertical line graph has a **tail to the right**, and with $p$ close to 1 it has a **tail to the left**.

At $p = 0 . 5$ it is exactly **symmetrical**, and the nearer $p$ is to 0.5 the more nearly symmetrical it becomes.

The reason is that most of the probability sits near the mean $n p$, which is pushed towards one end whenever $p$ is extreme.


Spec links: `spcpt_CFPBfrF9PVcrbCk6`


## Card 6 — question_and_answer (`fl_V77yfxmfC8nYdFVQ`)

**FRONT**

Before you can write down a binomial model for a situation, what three things must you identify?


**BACK**

What a single **trial** is, what counts as a **success**, and what your **random variable** is.

State the variable in words first, for example "let $X$ be the number of students in a class of 30 with black hair", and only then write it as `X \sim \text{B} \left(30 , p\right)`.

Naming the variable is what turns a story into something the four conditions can actually be tested against.


Spec links: `spcpt_cBCMfVF2MRC2fhZS`


## Card 7 — true_or_false (`fl_6T2G4YXkBj8VgR5d`)

**FRONT**

**True or False?**

The number of yellow cars in a car park of 100 cannot follow a binomial distribution, because cars come in more than two colours.


**BACK**

**False.**

The trial here is whether a given car **is yellow**, and that has exactly two outcomes: yellow, or not yellow.

Grouping every other colour together as a single failure outcome is what makes the two-outcome condition hold, and it is worth looking for whenever a situation seems to have too many outcomes.


Spec links: `spcpt_cBCMfVF2MRC2fhZS`


## Card 8 — question_and_answer (`fl_P8mzGC8BZ774cgFF`)

**FRONT**

Someone eats 5 sweets from a bag holding 6 caramels and 4 marshmallows, and $X$ is the number of caramels eaten. Which binomial condition fails?


**BACK**

The trials are not **independent**.

Eating a caramel first leaves fewer caramels in the bag, so the outcome of one trial changes the probability of success on the next.

Sampling **without replacement** from a small population is the usual way this condition breaks, and it is the condition worth checking first whenever a binomial model looks doubtful.


Spec links: `spcpt_cBCMfVF2MRC2fhZS`


## Card 9 — question_and_answer (`fl_8qP9nj6vVpgfXQPK`)

**FRONT**

A swimmer swims 50 lengths, and $X$ is the number of those lengths completed in under a minute. Which binomial condition is in doubt?


**BACK**

The probability of success is not **constant**.

The swimmer tires as the lengths go on, so the chance of completing a length in under a minute drops steadily instead of staying the same for all 50 trials.

A binomial model needs the same $p$ on every trial, so anything that makes success progressively harder or easier rules it out.


Spec links: `spcpt_cBCMfVF2MRC2fhZS`


## Card 10 — question_and_answer (`fl_HJQzYPbtmnp9Fk4G`)

**FRONT**

It is known that 8% of a **large** population is immune to a virus, and a **random** sample of 50 people is taken. What two assumptions allow a binomial model to be used?


**BACK**

That each person in the sample has the same 8% chance of being immune, and that whether one of them is immune does not affect whether another is.

Removing 50 people from a large population barely changes its make-up, so the probability stays effectively constant, and taking the sample at random is what stops the people in it being connected to one another.

Both assumptions would fail if all 50 came from a single family.


Spec links: `spcpt_cBCMfVF2MRC2fhZS`


## Card 11 — question_and_answer (`fl_yGx7vJy7d3bmHFd3`)

**FRONT**

In the binomial probability formula, what is the binomial coefficient `\binom{n}{x}` counting?


**BACK**

The number of different **orders** in which the $x$ successes could fall among the $n$ trials.

Every one of those orders has the same probability `p^{x} \left(1 - p\right)^{n - x}`, so you work out the probability of one of them and multiply by how many there are.

Without that factor you would have the probability of one **particular** sequence rather than of $x$ successes however they arise.


Spec links: `spcpt_946spf6kFdytWskY`


## Card 12 — question_and_answer (`fl_HmRsVDHx4c6ry2Zv`)

**FRONT**

What does the table of the Binomial Cumulative Distribution Function in the formula booklet give you?


**BACK**

It gives `\text{P} \left(X \le x\right)`, the probability of $x$ successes **or fewer**, to four decimal places.

It is listed only for selected values of $n$ between 5 and 50, and for $p$ running from 0.05 up to 0.5 in steps of 0.05.

Everything in the table is cumulative, so an individual probability such as `\text{P} \left(X = 7\right)` always has to be built out of two of its entries.


Spec links: `spcpt_946spf6kFdytWskY`


## Card 13 — question_and_answer (`fl_n7kgs9Z7gb3TwT7X`)

**FRONT**

A cumulative binomial table gives only `\text{P} \left(X \le x\right)`. How do you get `\text{P} \left(X = 7\right)` out of it?


**BACK**

Subtract the entry below it:

`\text{P} \left(X = 7\right) = \text{P} \left(X \le 7\right) - \text{P} \left(X \le 6\right)`

Everything up to and including 7, minus everything up to and including 6, leaves exactly the value 7.

The one case to watch is `\text{P} \left(X = 0\right)`, where there is no row beneath it, so it is simply the entry `\text{P} \left(X \le 0\right)`.


Spec links: `spcpt_946spf6kFdytWskY`


## Card 14 — fill_in_the_blanks (`fl_QNrjGnqhpK3qnJPv`)

**FRONT**

A cumulative binomial table gives only `\text{P} \left(X \le x\right)`. Complete the two rules that turn an upper tail into something the table holds:

`\text{P} \left(X \ge x\right) = 1 - \text{P} \left(X \le \_\_\_\_\_\_\right)`

`\text{P} \left(X > x\right) = 1 - \text{P} \left(X \le \_\_\_\_\_\_\right)`


**BACK**

The completed rules are:

`\text{P} \left(X \ge x\right) = 1 - \text{P} \left(X \le x - 1\right)`

`\text{P} \left(X > x\right) = 1 - \text{P} \left(X \le x\right)`

**At least** $x$ includes $x$ itself, so what you subtract has to stop one below it, whereas **more than** $x$ excludes $x$, so what you subtract runs all the way up to $x$.

Getting the two the wrong way round loses or gains exactly one term, `\text{P} \left(X = x\right)`.


*Blanks: 0 — answers: ['At least', 'more than']*

Spec links: `spcpt_946spf6kFdytWskY`

Flags: blank_answer_mismatch


## Card 15 — question_and_answer (`fl_9C2dMJgQhkyd7Fw9`)

**FRONT**

`X \sim \text{B} \left(40 , 0 . 35\right)`. How do you find `\text{P} \left(4 \le X \le 9\right)` from the cumulative table?


**BACK**

Take everything up to 9 and remove everything up to 3:

`\text{P} \left(4 \le X \le 9\right) = \text{P} \left(X \le 9\right) - \text{P} \left(X \le 3\right)`

A reliable way to get the two numbers right is to find the biggest integer you want to **include**, which is 9 here, and the biggest integer you want to **exclude**, which is 3.


Spec links: `spcpt_946spf6kFdytWskY`


## Card 16 — true_or_false (`fl_JwnZcqc2QQjmKpJQ`)

**FRONT**

**True or False?**

For `X \sim \text{B} \left(20 , 0 . 4\right)`, the probabilities `\text{P} \left(X > 5\right)` and `\text{P} \left(X \ge 6\right)` are the same.


**BACK**

**True.**

A binomial variable takes whole-number values only, so there is nothing at all between 5 and 6 for the two statements to disagree about.

That is what lets any strict inequality be rewritten as a weak one, and it works downwards too, with `\text{P} \left(X < 5\right) = \text{P} \left(X \le 4\right)`.


Spec links: `spcpt_946spf6kFdytWskY`


## Card 17 — question_and_answer (`fl_jJPrXVzzHDzbxBQ6`)

**FRONT**

The cumulative table lists $p$ only as far as 0.5. How do you use it for `X \sim \text{B} \left(20 , 0 . 7\right)`?


**BACK**

Count the **failures** instead: let `Y \sim \text{B} \left(20 , 0 . 3\right)`, so that $X + Y = 20$ and every question about $X$ becomes a question about $Y$.

Because a large $X$ means a small $Y$, an inequality turns round, giving `\text{P} \left(X \le 8\right) = \text{P} \left(Y \ge 12\right)` and `\text{P} \left(X \ge k\right) = \text{P} \left(Y \le 20 - k\right)`.

An equality needs no turning round, since `\text{P} \left(X = k\right) = \text{P} \left(Y = 20 - k\right)`.


Spec links: `spcpt_946spf6kFdytWskY`


## Card 18 — question_and_answer (`fl_YTJd2xwdndTYnG27`)

**FRONT**

Your $n$ or your $p$ is not one of the values listed in the cumulative table. What do you do instead?


**BACK**

Go back to the formula, work out the individual probabilities yourself, and add up the ones you need.

For `\text{P} \left(X \le 3\right)` that means calculating `\text{P} \left(X = 0\right) , \text{P} \left(X = 1\right) , \text{P} \left(X = 2\right)` and `\text{P} \left(X = 3\right)` and summing them.

Where the range you want is a long one, use the complement instead, since `\text{P} \left(X \ge 4\right) = 1 - \text{P} \left(X \le 3\right)` needs those same four probabilities and no more.


Spec links: `spcpt_946spf6kFdytWskY`

