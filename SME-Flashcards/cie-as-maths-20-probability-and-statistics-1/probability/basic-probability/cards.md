# Basic Probability

Course: cie-as-maths-20-probability-and-statistics-1 · Section: Probability

Source: https://www.savemyexams.com/as/maths/cie/20/probability-and-statistics-1/flashcards/probability/basic-probability/


## Card 1 — keyword_definition (`fl_NvkXMRFZFpdvrcp6`)

**FRONT**

Define **event**.


**BACK**

An **event** is an outcome, or a **collection** of outcomes, of an experiment: it is whatever you are interested in happening.

So, **for example**, when two spinners are spun and their scores are multiplied, "the product is $- 2$" is an event containing one outcome, while "the product is negative" is an event containing six.

The word to watch is *collection*, because an event is very often more than one outcome and its outcomes then have to be counted rather than assumed.


Spec links: `spcpt_B8jpsFGFMWZ2ywS5`


## Card 2 — question_and_answer (`fl_Y94k2DDWzynYKd5Q`)

**FRONT**

In probability, does "$A$ **or** $B$" allow both events to happen?


**BACK**

**Yes.** "$A$ or $B$" means $A$ happens, or $B$ happens, **or both** happen.

It is written $A \cup B$ and is read as the **union** of $A$ and $B$.

Everyday English often uses "or" to mean one or the other but not both, which is why this is worth checking every time.


Spec links: `spcpt_B8jpsFGFMWZ2ywS5`


## Card 3 — fill_in_the_blanks (`fl_Q2gfDZJnWKvW7HT5`)

**FRONT**

A fair five-sided spinner shows 2, 5, 8, 10 and 11. Fill in the missing symbol and the missing probability:

`\text{P}(\text{odd} \_\_\_\_\_\_ \text{prime}) = \_\_\_\_\_\_`


**BACK**

The completed statement is:

$\text{P} ( \text{odd} \cap \text{prime} ) = \frac{2}{5}$

The word **and** is hidden inside "odd prime", because the number has to be odd **and** prime, which is the **intersection** $\cap$.

Only 5 and 11 lie in both events, so the probability is $\frac{2}{5}$, smaller than $\text{P} ( \text{prime} ) = \frac{3}{5}$, which counts the 2 as well.


*Blanks: 0 — answers: []*

Spec links: `spcpt_B8jpsFGFMWZ2ywS5`

Flags: fitb_no_blank_marker


## Card 4 — question_and_answer (`fl_5rymfmXpPFf3GBjd`)

**FRONT**

What does the notation $A '$ mean, and how do you find $\text{P} ( A ' )$?


**BACK**

$A '$ is the **complement** of $A$, the event that $A$ does **not** happen, and it is read "$A$ prime".

Its probability is

$\text{P} ( A ' ) = 1 - \text{P} ( A )$

This is one of the easiest results in probability to understand and one of the hardest to spot, because a question that looks awkward forwards is often straightforward backwards.


Spec links: `spcpt_B8jpsFGFMWZ2ywS5`


## Card 5 — question_and_answer (`fl_Ky9yW3BNnY2Bfv5t`)

**FRONT**

Why can you find the probability of rolling a six by counting outcomes, but not the probability that a football team wins?


**BACK**

Counting outcomes only gives a probability when **every outcome is equally likely**, which is true of a fair die and is not true of a football match.

A football result is estimated from **relative frequency** instead, meaning the proportion of times it has happened in previous matches between those teams.

The more results the estimate is based on the more reliable it is, and a large gap between a theoretical probability and a relative frequency is evidence of bias.


Spec links: `spcpt_B8jpsFGFMWZ2ywS5`


## Card 6 — question_and_answer (`fl_Kxwy6HMbNGZjnMG5`)

**FRONT**

What does it mean to say that two events are **independent**?


**BACK**

Two events are **independent** when the outcome of one has no effect on the probability of the other.

So, **for example**, "rolling a 6" and "flipping heads" are independent, because what the die does tells you nothing about what the coin does.

Independent events very often come from two separate experiments, which is a useful thing to look for in a question.


Spec links: `spcpt_7GngfWnfm7YxqRWm`


## Card 7 — fill_in_the_blanks (`fl_2nycdD55gnJCnnJw`)

**FRONT**

Each of these results only holds under a condition. Fill in the two conditions:

$\text{P} ( A \cap B ) = \text{P} ( A ) \times \text{P} ( B )$ holds when $A$ and $B$ are `\_\_\_\_\_\_`.

$\text{P} ( A \cup B ) = \text{P} ( A ) + \text{P} ( B )$ holds when $A$ and $B$ are `\_\_\_\_\_\_`.


**BACK**

The completed results are:

$\text{P} ( A \cap B ) = \text{P} ( A ) \times \text{P} ( B )$ holds when $A$ and $B$ are **independent**.

$\text{P} ( A \cup B ) = \text{P} ( A ) + \text{P} ( B )$ holds when $A$ and $B$ are **mutually exclusive**.

Neither result is true for every pair of events, so the condition has to be given in the question, or shown to be true, before the formula can be used.

A quick way to keep them apart: **and** goes with $\cap$ and multiplying, **or** goes with $\cup$ and adding.


*Blanks: 0 — answers: []*

Spec links: `spcpt_7GngfWnfm7YxqRWm`

Flags: fitb_no_blank_marker


## Card 8 — question_and_answer (`fl_NTP3B9BQXvcm52Xw`)

**FRONT**

What does it mean for two events to be **mutually exclusive**, and what is $\text{P} ( A \cap B )$?


**BACK**

**Mutually exclusive** events cannot both happen at the same time, so no outcome belongs to both of them.

That makes the intersection empty:

$\text{P} ( A \cap B ) = 0$

So, **for example**, "rolling a 5" and "rolling a 6" are mutually exclusive on a single roll of a die, because one roll cannot do both.


Spec links: `spcpt_7GngfWnfm7YxqRWm`


## Card 9 — true_or_false (`fl_hF64HXhMhWjgPbBY`)

**FRONT**

**True or False?**

Two events that are mutually exclusive can also be independent.


**BACK**

**False.**

If two events are mutually exclusive then one of them happening forces the probability of the other down to zero, and that is exactly the influence independence rules out.

The one exception is an event that was impossible to begin with, whose probability stays at zero whatever else happens.


Spec links: `spcpt_7GngfWnfm7YxqRWm`


## Card 10 — keyword_definition (`fl_krMSzPCnFc7zpgNq`)

**FRONT**

Define the **universal set** as it is used on a Venn diagram.


**BACK**

The **universal set** is every possible outcome of the experiment, and it is drawn as the **rectangle** enclosing the whole diagram.

It is labelled with a symbol just outside one corner, commonly $S$, $U$ or $ξ$, and there is no single standard choice.

Each **bubble** drawn inside the rectangle stands for one event and is labelled with that event's letter.


Spec links: `spcpt_KPTCzXxPJc56vjtQ`


## Card 11 — question_and_answer (`fl_GHwT7f4qcvRhpFYx`)

**FRONT**

What can the numbers written in the regions of a Venn diagram represent?


**BACK**

They are either **frequencies**, meaning how many items fall in that region, or **probabilities**.

The same diagram can be written either way, so, **for example**, regions holding 5, 8, 3 and 4 of the 20 people surveyed become $0 . 25$, $0 . 4$, $0 . 15$ and $0 . 2$.

Which of the two you are looking at decides what the values have to add up to, so it is worth settling first.


Spec links: `spcpt_KPTCzXxPJc56vjtQ`


## Card 12 — fill_in_the_blanks (`fl_pX3WBF3fsRZwKqvm`)

**FRONT**

Complete the check that the values on every Venn diagram must pass:

If the regions hold **frequencies**, they must add up to `\_\_\_\_\_\_`.

If the regions hold **probabilities**, they must add up to `\_\_\_\_\_\_`.


**BACK**

The completed check is:

If the regions hold **frequencies**, they must add up to **the total number of items surveyed**.

If the regions hold **probabilities**, they must add up to **1**.

Both say the same thing, which is that the regions between them account for every possible outcome and never count one twice.


*Blanks: 0 — answers: []*

Spec links: `spcpt_KPTCzXxPJc56vjtQ`

Flags: fitb_no_blank_marker


## Card 13 — question_and_answer (`fl_xc5PPYPJ3kfqrc7c`)

**FRONT**

On a Venn diagram for two events, which outcomes sit inside the rectangle but outside both bubbles, and why is that region needed?


**BACK**

They are the outcomes for which **neither** event happens, written $( A \cup B ) '$.

The region is needed because the bubbles cover only the events you happen to be interested in, and most experiments have outcomes falling into none of them.

Leaving it out is the usual reason a Venn diagram's values fail to reach the total.


Spec links: `spcpt_KPTCzXxPJc56vjtQ`


## Card 14 — question_and_answer (`fl_bxbvNJmW45tfzrWR`)

**FRONT**

A Venn diagram's four regions hold $x$, 8, $2 x$ and 5, and must account for all 40 people surveyed. What is $x$, and what does that make the $2 x$ region?


**BACK**

$x = 9$, so the $2 x$ region holds 18.

Adding the four regions and setting the sum equal to 40 gives

$x + 8 + 2 x + 5 = 40$

so $3 x = 27$.

Writing an unknown into a region and forming one equation from the total is the standard route whenever a question does not hand you every value.


Spec links: `spcpt_KPTCzXxPJc56vjtQ`


## Card 15 — question_and_answer (`fl_Sy7qkph4tmnptF4y`)

**FRONT**

On a Venn diagram for two events, which regions do you add to find the probability that **exactly one** of them happens?


**BACK**

You add the two "only" regions: the outcomes that are in $A$ but not in $B$, and the outcomes that are in $B$ but not in $A$.

The region where both events happen is deliberately left out, because "exactly one" rules out both happening.

That is what separates it from $\text{P} ( A \cup B )$, which does include that region.


Spec links: `spcpt_KPTCzXxPJc56vjtQ`


## Card 16 — true_or_false (`fl_y6Pb3SCTjMZN9DXm`)

**FRONT**

**True or False?**

A Venn diagram can be drawn for two events that can never happen at the same time.


**BACK**

**True.**

The two bubbles are simply drawn so that they do not overlap, or drawn overlapping with a $0$ written in the region where both events would happen.

A Venn diagram is a picture of what the events actually do, so an empty shared region is exactly how it shows that the two cannot both happen.


Spec links: `spcpt_KPTCzXxPJc56vjtQ`


## Card 17 — question_and_answer (`fl_4H3f2kbqRHqXwHsk`)

**FRONT**

There are two ways to read the probability that an event does **not** happen off a Venn diagram. What are they?


**BACK**

Add up the values in every region outside that event's bubble, which is every region where the event does not happen.

Or add up the values inside the bubble and subtract the total from 1.

Both must give the same answer, so doing one and checking with the other catches a misread region straight away.


Spec links: `spcpt_KPTCzXxPJc56vjtQ`


## Card 18 — true_or_false (`fl_Qv8Yc4J3BHWTCCSv`)

**FRONT**

**True or False?**

On a tree diagram, the branches for the second event always carry the same probabilities whichever branch you arrived along.


**BACK**

**False.**

On a tree diagram the second set of branches can carry different probabilities depending on which branch came before, and that is precisely what tree diagrams are good at showing.

So, **for example**, if an item is drawn and **not replaced**, what is left to draw from depends on what was taken first, so the two sets of second branches differ.

When the probabilities are the same either way, the two events are independent.


Spec links: `spcpt_Q9VkVVBtSYX8n8rN`


## Card 19 — question_and_answer (`fl_Fzd74DMV2h3pCMMq`)

**FRONT**

How do you find the probability of one complete path through a tree diagram?


**BACK**

The probability of a complete path is the **product of the probabilities labelling its branches**.

Where the second event depends on the first, the number on the second branch is already the probability of that event **given what has just happened**, so multiplying the labels is correct even though the two events are not independent.

So, **for example**, a path whose branches are labelled $0 . 8$, $0 . 4$ and $0 . 8$ has probability $0 . 8 \times 0 . 4 \times 0 . 8 = 0 . 256$.


Spec links: `spcpt_Q9VkVVBtSYX8n8rN`


## Card 20 — true_or_false (`fl_RzJgvhy7qTHJj8Pz`)

**FRONT**

**True or False?**

Every branch of a tree diagram must lead on to the same number of later branches.


**BACK**

**False.**

A branch stops wherever the experiment stops, so some branches lead on and others do not.

So, **for example**, in a test that is retaken until it is passed, the **fail** branch leads on to another attempt but the **pass** branch does not, because there is nothing left to happen.


Spec links: `spcpt_Q9VkVVBtSYX8n8rN`


## Card 21 — question_and_answer (`fl_7r7hJ2hy9TvcSr5b`)

**FRONT**

Why are you allowed to add the probabilities of several complete paths through a tree diagram?


**BACK**

The complete paths through a tree diagram are **mutually exclusive**, so adding their probabilities never counts an outcome twice: the experiment ends up on exactly one path.

That is why a question asking for several different final outcomes becomes a sum.

Work out each path by multiplying along it, then add the paths you want.


Spec links: `spcpt_Q9VkVVBtSYX8n8rN`


## Card 22 — fill_in_the_blanks (`fl_hwZqRT6WC32twVyr`)

**FRONT**

A contestant has three attempts to hit a target, and wins by hitting it at least once. Rather than adding the three winning paths, complete the shortcut:

`\text{P}(\text{wins}) = 1 - \text{P}(\_\_\_\_\_\_)`


**BACK**

The completed shortcut is:

$\text{P} ( \text{wins} ) = 1 - \text{P} ( \text{misses all three} )$

There are three separate paths that win and only one that loses, so the subtraction replaces three multiplications and an addition with a single calculation.

Look for this whenever a question says **at least one**, because that phrasing almost always means the losing outcome is a single path.


*Blanks: 0 — answers: []*

Spec links: `spcpt_Q9VkVVBtSYX8n8rN`

Flags: fitb_no_blank_marker


## Card 23 — question_and_answer (`fl_XfDqn794zvTXBqj3`)

**FRONT**

What two checks are built into every tree diagram?


**BACK**

The probabilities on each **pair of branches** must add up to 1.

The probabilities of all the **final outcomes** must add up to 1.

Both are worth running, because they catch different mistakes: the first finds a branch labelled wrongly, and the second finds a path left out or multiplied wrongly.


Spec links: `spcpt_Q9VkVVBtSYX8n8rN`

