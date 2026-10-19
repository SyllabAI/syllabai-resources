# Basic Probability

Course: ial-maths-20-statistics-1 · Section: Probability

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-1/flashcards/probability/basic-probability/


## Card 1 — keyword_definition (`fl_86D6MPXrM4n8gK9Q`)

**FRONT**

Define **sample space**.


**BACK**

The sample space is the set of **all possible outcomes** of an experiment.

It can be written as a list or set out in a table, which helps when the outcomes are hard to picture. So, **for example**, for the products of two four-sided spinners, a grid of all 16 products is the sample space.


Spec links: `spcpt_bxWFJwqxDSR3cBsC`


## Card 2 — question_and_answer (`fl_qfFKm2SXJfQPf4K4`)

**FRONT**

What is the difference between an outcome and an event?


**BACK**

An **outcome** is a single result of an experiment, while an **event** is what you are interested in happening, which may be one outcome or a whole collection of them.

So, **for example**, for the products of two spinners, the event "the product is $- 2$" contains one outcome, but the event "the product is negative" contains six.


Spec links: `spcpt_bxWFJwqxDSR3cBsC`


## Card 3 — fill_in_the_blanks (`fl_ySJV4xsCqgcjydtt`)

**FRONT**

Complete the condition that this formula depends on:

$\text{P} ( \text{success} ) = \frac{\text{number of ways to get a success}}{\text{total number of outcomes}}$

The formula is only valid when all outcomes are `\_\_\_\_\_\_`.


**BACK**

The completed condition is:

The formula is only valid when all outcomes are **equally likely**.

This is easy to lose sight of, because the formula looks as though it always applies. Counting outcomes tells you nothing about probability unless each one is as likely as the next, so, **for example**, it cannot be used on a biased dice.


*Blanks: 1 — answers: ['equally likely', 'for example']*

Spec links: `spcpt_bxWFJwqxDSR3cBsC`

Flags: blank_answer_mismatch


## Card 4 — question_and_answer (`fl_Qc3tgVvBxsG4rWDp`)

**FRONT**

What do $\text{P} ( A )$, $\text{P} ( A ' )$ and $\text{P} ( X \leq 4 )$ each mean?


**BACK**

`\text{P} \left(A\right)` is the probability that event $A$ **happens**.

`\text{P} \left(A '\right)` is the probability that event $A$ **does not happen**, sometimes written `\text{P} \left(\bar{A}\right)`, and the two are linked by `\text{P} \left(A '\right) = 1 - \text{P} \left(A\right)`.

`\text{P} \left(X \leq 4\right)` is the probability that the quantity $X$ takes a value **less than or equal to** 4, so read the inequality sign carefully: "less than 4" would be `\text{P} \left(X < 4\right)` and means something different.


Spec links: `spcpt_bxWFJwqxDSR3cBsC`


## Card 5 — keyword_definition (`fl_q88kYQ5MvJVnFWyY`)

**FRONT**

Define **independent events**.


**BACK**

Independent events are events that **do not affect each other**, so the probability of one happening is unchanged by the outcome of the other.

For two independent events:

$\text{P} ( A \text{and} B ) = \text{P} ( A ) \times \text{P} ( B )$

So, **for example**, rolling a 6 on a dice and flipping heads on a coin are independent, and the probability of both is $\frac{1}{6} \times \frac{1}{2} = \frac{1}{12}$.


Spec links: `spcpt_xPq8dPj856nqvFQ3`


## Card 6 — question_and_answer (`fl_msdHnQbRQbXZC3yD`)

**FRONT**

In probability, which arithmetic operation does **and** call for, and which does **or** call for?


**BACK**

**And** calls for multiplication, and **or** calls for addition.

Independence is an *and* situation and uses $\times$, while mutual exclusivity is an *or* situation and uses $+$.

Rephrasing a wordy question in these terms is usually the quickest way in: "the probability of a prime number with heads" becomes "the probability of rolling a 2 **or** a 3 **or** a 5, **and** heads".


Spec links: `spcpt_xPq8dPj856nqvFQ3`


## Card 7 — keyword_definition (`fl_2wYFr78ZZ9St5qD2`)

**FRONT**

Define **mutually exclusive events**.


**BACK**

Mutually exclusive events are events that **cannot both happen at once**, so $\text{P} ( A \text{and} B ) = 0$.

For two mutually exclusive events:

$\text{P} ( A \text{or} B ) = \text{P} ( A ) + \text{P} ( B )$

So, **for example**, rolling a 5 and rolling a 6 on a single dice are mutually exclusive, and the probability of one or the other is $\frac{1}{6} + \frac{1}{6} = \frac{1}{3}$.


Spec links: `spcpt_xPq8dPj856nqvFQ3`


## Card 8 — true_or_false (`fl_8H2jb26q73Dznrw6`)

**FRONT**

**True or False?**

Two events that are mutually exclusive can also be independent.


**BACK**

**False.**

Mutually exclusive events can never be independent. If $A$ happens then $B$ cannot happen at all, so the outcome of $A$ has changed the probability of $B$ to zero, and independence requires it to be left untouched.

The formulae show it too: mutual exclusivity gives $\text{P} ( A \text{and} B ) = 0$, while independence would need $\text{P} ( A ) \times \text{P} ( B )$, which is not zero for events that can actually happen.


Spec links: `spcpt_xPq8dPj856nqvFQ3`


## Card 9 — question_and_answer (`fl_8kd297hZrqC6qnjm`)

**FRONT**

What is the difference between a theoretical probability and one based on experimental results?


**BACK**

A **theoretical** probability comes from the structure of the experiment itself, while an **experimental** one, also called a relative frequency, comes from what actually happened over a number of trials.

So, **for example**, the probability of each score on a fair dice is theoretical, but the probability of one football team beating another can only come from previous results.

Comparing the two is how you judge whether an experiment is **biased**: if the observed relative frequencies stay a long way from the theoretical values over many trials, that is evidence of bias.


Spec links: `spcpt_bxWFJwqxDSR3cBsC`


## Card 10 — question_and_answer (`fl_pYG8Bx8PpTytpKxr`)

**FRONT**

On a Venn diagram, what do the rectangle and the bubbles inside it represent?


**BACK**

The **rectangle** represents the **sample space**, meaning every possible outcome of the experiment, and each **bubble** inside it represents one **event**.

Always draw the rectangle. The bubbles show only the events you happen to be interested in, so without the rectangle there is nothing on the diagram representing the outcomes that fall outside all of them.


Spec links: `spcpt_YrhS9dcy42xvf5Qf`


## Card 11 — true_or_false (`fl_fTzGdnRcMKtCxNhh`)

**FRONT**

**True or False?**

You can tell whether two events are independent by looking at the shape of a Venn diagram.


**BACK**

**False.**

Independence cannot be seen in the shape of a Venn diagram at all: it depends on the numbers in the regions, and has to be checked by calculation.

**Mutual exclusivity can** be seen at a glance, which is what makes this confusing.

Two bubbles that do not overlap are mutually exclusive, because no outcome belongs to both.


Spec links: `spcpt_YrhS9dcy42xvf5Qf`


## Card 12 — question_and_answer (`fl_srg9Rq3brjRx6Dqw`)

**FRONT**

How do you use a Venn diagram to decide whether two events are independent?


**BACK**

Read the three probabilities you need straight off the Venn diagram, then test whether the independence formula holds:

`\text{P} \left(A \textrm{ }\text{and}\textrm{ } B\right) = \text{P} \left(A\right) \times \text{P} \left(B\right)`

The overlap gives `\text{P} \left(A \textrm{ }\text{and}\textrm{ } B\right)`, and `\text{P} \left(A\right)` is everything inside bubble $A$, **including** the overlap.

If the two sides are equal the events are independent, so an overlap of $\frac{7}{40}$ against a product of $\frac{9}{40}$ shows that they are not.


Spec links: `spcpt_YrhS9dcy42xvf5Qf`


## Card 13 — true_or_false (`fl_3h272WT3sYBkbcxY`)

**FRONT**

**True or False?**

If the bubble for event $B$ lies entirely inside the bubble for event $A$, then whenever $A$ happens, $B$ happens.


**BACK**

**False.**

Whenever $B$ happens $A$ happens, not the other way round. Every outcome in $B$ is also in $A$, but $A$ contains outcomes outside $B$ as well.

So, **for example**, if $A$ is "rolls an even number" and $B$ is "rolls a 6", then rolling a 6 guarantees an even number, but rolling an even number does not guarantee a 6.


Spec links: `spcpt_YrhS9dcy42xvf5Qf`


## Card 14 — question_and_answer (`fl_9hfP636knm34GsDy`)

**FRONT**

When you fill in a Venn diagram for three events, why do you start from the centre (i.e. where the three events all overlap) and work outwards?


**BACK**

You start in the centre because the figures a question gives you usually **overlap each other**.

If you are told that 8 people own both a console $P$ and a console $X$, that 8 **includes** anyone who owns all three, so the region for $P$ and $X$ only is 8 minus the number owning all three.

Filling in the centre first means every later region can be found by subtracting from a figure you already have. Working the other way round leaves you guessing.


Spec links: `spcpt_YrhS9dcy42xvf5Qf`


## Card 15 — fill_in_the_blanks (`fl_9YScCrbfgfrqFNTx`)

**FRONT**

Complete the two checks you should run on a finished Venn diagram:

If the diagram shows frequencies, they must add up to the `\_\_\_\_\_\_` number of people or items involved.

If it shows probabilities, they must add up to `\_\_\_\_\_\_`.


**BACK**

The completed checks are:

If the diagram shows frequencies, they must add up to the **total** number of people or items involved.

If it shows probabilities, they must add up to **1**.

Run both every time. They cost a few seconds and they catch a region left blank or counted twice, which is the commonest way these questions go wrong.


*Blanks: 1 — answers: ['total', '1']*

Spec links: `spcpt_YrhS9dcy42xvf5Qf`

Flags: blank_answer_mismatch


## Card 16 — true_or_false (`fl_Qv8Yc4J3BHWTCCSv`)

**FRONT**

**True or False?**

On a tree diagram, the branches for the second event always carry the same probabilities whichever branch you arrived along.


**BACK**

**False.**

On a tree diagram the second set of branches can carry different probabilities depending on which branch came before, and that is precisely what tree diagrams are good at showing.

So, **for example**, if an item is drawn and **not replaced**, what is left to draw from depends on what was taken first, so the two sets of second branches differ.

When the probabilities are the same either way, the two events are independent.


Spec links: `spcpt_Q9VkVVBtSYX8n8rN`


## Card 17 — question_and_answer (`fl_Fzd74DMV2h3pCMMq`)

**FRONT**

How do you find the probability of one complete path through a tree diagram?


**BACK**

The probability of a complete path is the **product of the probabilities labelling its branches**.

Where the second event depends on the first, the number on the second branch is already the probability of that event **given what has just happened**, so multiplying the labels is correct even though the two events are not independent.

So, **for example**, a path whose branches are labelled $0 . 8$, $0 . 4$ and $0 . 8$ has probability $0 . 8 \times 0 . 4 \times 0 . 8 = 0 . 256$.


Spec links: `spcpt_Q9VkVVBtSYX8n8rN`


## Card 18 — true_or_false (`fl_RzJgvhy7qTHJj8Pz`)

**FRONT**

**True or False?**

Every branch of a tree diagram must lead on to the same number of later branches.


**BACK**

**False.**

A branch stops wherever the experiment stops, so some branches lead on and others do not.

So, **for example**, in a test that is retaken until it is passed, the **fail** branch leads on to another attempt but the **pass** branch does not, because there is nothing left to happen.


Spec links: `spcpt_Q9VkVVBtSYX8n8rN`


## Card 19 — question_and_answer (`fl_7r7hJ2hy9TvcSr5b`)

**FRONT**

Why are you allowed to add the probabilities of several complete paths through a tree diagram?


**BACK**

The complete paths through a tree diagram are **mutually exclusive**, so adding their probabilities never counts an outcome twice: the experiment ends up on exactly one path.

That is why a question asking for several different final outcomes becomes a sum.

Work out each path by multiplying along it, then add the paths you want.


Spec links: `spcpt_Q9VkVVBtSYX8n8rN`


## Card 20 — fill_in_the_blanks (`fl_hwZqRT6WC32twVyr`)

**FRONT**

A contestant has three attempts to hit a target, and wins by hitting it at least once. Rather than adding the three winning paths, complete the shortcut:

`\text{P}(\text{wins}) = 1 - \text{P}(\_\_\_\_\_\_)`


**BACK**

The completed shortcut is:

$\text{P} ( \text{wins} ) = 1 - \text{P} ( \text{misses all three} )$

There are three separate paths that win and only one that loses, so the subtraction replaces three multiplications and an addition with a single calculation.

Look for this whenever a question says **at least one**, because that phrasing almost always means the losing outcome is a single path.


*Blanks: 0 — answers: ['at least one']*

Spec links: `spcpt_Q9VkVVBtSYX8n8rN`

Flags: blank_answer_mismatch


## Card 21 — question_and_answer (`fl_XfDqn794zvTXBqj3`)

**FRONT**

What two checks are built into every tree diagram?


**BACK**

The probabilities on each **pair of branches** must add up to 1.

The probabilities of all the **final outcomes** must add up to 1.

Both are worth running, because they catch different mistakes: the first finds a branch labelled wrongly, and the second finds a path left out or multiplied wrongly.


Spec links: `spcpt_Q9VkVVBtSYX8n8rN`

