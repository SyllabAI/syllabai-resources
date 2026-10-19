# Probability Distributions

Course: cie-a-level-maths-20-probability-and-statistics-1 · Section: Statistical Distributions

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/flashcards/statistical-distributions/probability-distributions/


## Card 1 — keyword_definition (`fl_f3wF7jB8qqJXyvRx`)

**FRONT**

Define **discrete random variable**.


**BACK**

A **random variable** is a variable whose value depends on the outcome of a random event, so it is not known until that event happens.

It is **discrete** when it can take only certain **separate** values rather than any value in a range.

Discrete random variables usually **count** something, such as the number of heads in 20 coin flips.


Spec links: `spcpt_gNXFxJ55T59nCGk5`


## Card 2 — true_or_false (`fl_CSf4FDKNSRyWSH9c`)

**FRONT**

**True or False?**

A discrete random variable can take values that are not whole numbers.


**BACK**

**True.**

**Discrete** means the values it can take are **separate** from one another, not that they are integers.

So, **for example**, a spinner whose sectors are labelled $- 2$, $0$, $\frac{1}{3}$ and $5$ gives a perfectly good discrete random variable, with one value negative and one a fraction.


Spec links: `spcpt_gNXFxJ55T59nCGk5`


## Card 3 — question_and_answer (`fl_SqCTsfF8DgJVfZrq`)

**FRONT**

In probability notation, what is the difference between $X$ and $x$?


**BACK**

The **upper case** $X$ is the random variable itself, and the **lower case** $x$ is a particular value that it might take.

So $\text{P} ( X = x )$ reads as the probability that the random variable $X$ takes the value $x$.

Keeping the two cases apart is what makes the rest of the notation readable, and mixing them up is the commonest way to lose track of a question.


Spec links: `spcpt_gNXFxJ55T59nCGk5`


## Card 4 — question_and_answer (`fl_39Pq5w7T6qMptRqN`)

**FRONT**

In what three ways can a discrete probability distribution be presented?


**BACK**

As a **table**, listing each value against its probability.

As a **function**, giving $\text{P} ( X = x )$ by a formula, which is called a probability mass function.

Or as a **vertical line graph**, with the values along the horizontal axis and the probabilities as the heights.


Spec links: `spcpt_Gfcm92qtDBJvFpw2`


## Card 5 — fill_in_the_blanks (`fl_RMdDzQbP3Ps9NcRW`)

**FRONT**

Complete the property that every discrete probability distribution must have:

`\sum \text{P}(X = x) = \_\_\_\_\_\_`


**BACK**

The completed property is:

$\sum \text{P} ( X = x ) = 1$

The variable is certain to take one of its possible values, so the probabilities of all of them together must account for everything.

This is the equation you form whenever a distribution contains an unknown.


*Blanks: 0 — answers: []*

Spec links: `spcpt_Gfcm92qtDBJvFpw2`

Flags: fitb_no_blank_marker


## Card 6 — question_and_answer (`fl_Kc75Djp9dSP7p3hw`)

**FRONT**

A distribution is given by $\text{P} ( X = x ) = k x^{2}$ for $x = - 3 , - 1 , 2 , 4$. How do you find $k$?


**BACK**

Work out each probability in terms of $k$, then set their sum equal to 1 and solve.

Here the four probabilities are $9 k$, $k$, $4 k$ and $16 k$, so

$30 k = 1 , \text{so} k = \frac{1}{30}$

Writing the distribution out as a table first makes the sum much harder to get wrong.


Spec links: `spcpt_Gfcm92qtDBJvFpw2`


## Card 7 — question_and_answer (`fl_KZftWgWHKVGrqFd2`)

**FRONT**

How do you find $\text{P} ( X \leq 3 )$ from a probability distribution table?


**BACK**

Pick out every value in the table that is **at most 3**, and add their probabilities together.

Only values the variable can actually take contribute anything, so a number that is not in the table has probability zero and is simply ignored.

Remember to include the smallest value, which is easy to skip over.


Spec links: `spcpt_BzMXR87dNgwF3Dfv`


## Card 8 — fill_in_the_blanks (`fl_VQw9nfqjsQNhkM5k`)

**FRONT**

Fill in the inequality each phrase translates to, for a discrete random variable:

at most $k$ becomes `\_\_\_\_\_\_`

fewer than $k$ becomes `\_\_\_\_\_\_`

at least $k$ becomes `\_\_\_\_\_\_`


**BACK**

The completed translations are:

at most $k$ becomes $X \leq k$

fewer than $k$ becomes $X < k$

at least $k$ becomes $X \geq k$

The difference between **at most** and **fewer than** is whether $k$ itself is counted, and for a discrete variable that changes the answer.


*Blanks: 0 — answers: []*

Spec links: `spcpt_BzMXR87dNgwF3Dfv`

Flags: fitb_no_blank_marker


## Card 9 — question_and_answer (`fl_kDCydwQsbn5xfWd4`)

**FRONT**

Why does $\text{P} ( X > k ) = 1 - \text{P} ( X \leq k )$, and when is it worth using?


**BACK**

Every value the variable can take is either at most $k$ or greater than $k$, never both and never neither, so the two probabilities account for everything and add to 1.

It is worth using whenever there are fewer unwanted values than wanted ones, since it replaces a long sum with a short one.

The matching pair is $\text{P} ( X \geq k ) = 1 - \text{P} ( X < k )$, and mixing the two up is what the strict and weak inequalities are there to warn you about.


Spec links: `spcpt_BzMXR87dNgwF3Dfv`


## Card 10 — question_and_answer (`fl_VwxBK9kHrGDr2ySS`)

**FRONT**

How do you find $\text{P} ( X^{2} < 5 )$ when $X$ can take the values $- 3 , - 1 , 2$ and $4$?


**BACK**

Test each value in turn, keep the ones that satisfy the condition, and add their probabilities.

Here $( - 1 )^{2} = 1$ and $2^{2} = 4$ are below 5, while $( - 3 )^{2} = 9$ and $4^{2} = 16$ are not, so the answer is $\text{P} ( X = - 1 ) + \text{P} ( X = 2 )$.

Testing each value one at a time matters because a **negative** value can satisfy a condition on $X^{2}$, which solving an inequality in your head is likely to miss.


Spec links: `spcpt_BzMXR87dNgwF3Dfv`


## Card 11 — keyword_definition (`fl_zTCMZTMTh4CjwxQb`)

**FRONT**

Define **expected value**.


**BACK**

The **expected value** of a random variable, written $\text{E} ( X )$, is its **mean**.

It is the value that the average of a large number of observations of $X$ would be expected to settle near.

It need not be a value that $X$ can actually take: a fair die has expected value 3.5.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 12 — fill_in_the_blanks (`fl_9qmvKF5MszSPbZfd`)

**FRONT**

Fill in the two expectation formulae for a discrete random variable:

`\text{E}(X) = \sum \_\_\_\_\_\_ \text{P}(X = x)`

`\text{E}(X^{2}) = \sum \_\_\_\_\_\_ \text{P}(X = x)`


**BACK**

The completed formulae are:

$\text{E} ( X ) = \sum x \text{P} ( X = x )$

$\text{E} ( X^{2} ) = \sum x^{2} \text{P} ( X = x )$

In each case you weight the quantity you are averaging by the probability of getting it, and add.

Notice that the probabilities are untouched: it is only the thing being averaged that gets squared.


*Blanks: 0 — answers: []*

Spec links: `spcpt_ZMNyvHd7JK6WfHTm`

Flags: fitb_no_blank_marker


## Card 13 — question_and_answer (`fl_YsMDq4ssQS9vj6Xm`)

**FRONT**

How would you find `\text{E}\left(\frac{1}{X}\right)` for a discrete random variable?


**BACK**

Apply the function to each value of $X$, multiply each result by that value's probability, and add.

So it is $\sum \frac{1}{x} \text{P} ( X = x )$, worked out value by value.

The same pattern gives $\text{E}$ of any function of $X$, and it is the only safe route, because applying the function to the mean instead does not give the same answer.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 14 — true_or_false (`fl_pgBn8JTTg9hhGpHy`)

**FRONT**

**True or False?**

$\text{E} ( X^{2} )$ is the same as $\text{E} ( X )$ squared.


**BACK**

**False.**

The mean of the squares is not the square of the mean.

So, **for example**, if $X$ is $- 1$ or $1$ with equal chance, its mean is 0, so squaring the mean gives 0; but every value squares to 1, so the mean of the squares is 1.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 15 — question_and_answer (`fl_gfTwtRF6HQNJnYD5`)

**FRONT**

A distribution has $\text{E} ( X ) = 4 . 9$ and $\text{E} ( X^{2} ) = 27 . 7$. What are its variance and standard deviation?


**BACK**

The variance is

$27 . 7 - 4 . 9^{2} = 27 . 7 - 24 . 01 = 3 . 69$

and the standard deviation is $\sqrt{3.69} = 1 . 92$ to 3 significant figures.

The order matters: square the mean and subtract it, rather than subtracting first and squaring afterwards.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 16 — question_and_answer (`fl_CjgfwjwyfhsKtCCH`)

**FRONT**

A variable takes the values 1, 5 and 9 with probabilities 0.3, 0.4 and 0.3. What is $\text{E} ( X )$, and why is no calculation needed?


**BACK**

It is **5**.

Both the values and their probabilities are **symmetrical** about 5, so the weighting either side of it balances exactly and the mean sits at the centre.

Spotting a symmetrical distribution saves the whole calculation, and it also tells you the mean and the median are equal.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`


## Card 17 — question_and_answer (`fl_pdsXyfCRHwjs6WkF`)

**FRONT**

Why must $\text{E} ( X )$ always lie between the smallest and largest values that $X$ can take?


**BACK**

Because it is a **weighted average** of those values, and the weights are probabilities that add up to 1.

An average built that way cannot escape the range of the things being averaged, however uneven the weights are.

That makes it a quick check on any expectation you calculate: an answer outside the range means an arithmetic slip.


Spec links: `spcpt_ZMNyvHd7JK6WfHTm`

