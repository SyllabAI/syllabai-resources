# Further Probability

Course: cie-a-level-maths-20-probability-and-statistics-1 · Section: Probability

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/flashcards/probability/further-probability/


## Card 1 — keyword_definition (`fl_6WZNRJfJnqhvzHy9`)

**FRONT**

Define the **empty set**.


**BACK**

The **empty set** is the set with no elements in it at all, and it is written $\emptyset$.

In probability it is what you get when two events cannot both happen: their intersection contains no outcomes, so it is the empty set.

It is worth having a symbol for, because "the intersection is empty" is a statement about the events themselves rather than about any particular experiment.


Spec links: `spcpt_g5pddg4MDHhfn69F`


## Card 2 — fill_in_the_blanks (`fl_8V6phfWKznqZFf9P`)

**FRONT**

Fill in the missing symbol in each result, watching what happens between the two sides:

`\left(A \cup B\right)' = A' \_\_\_\_\_\_ B'`

`\left(A \cap B\right)' = A' \_\_\_\_\_\_ B'`


**BACK**

The completed results are:

`\left(A \cup B\right)' = A' \cap B'`

`\left(A \cap B\right)' = A' \cup B'`

The union and the intersection **swap over** when the complement is taken, which is the part that catches people out.

In words, "neither $A$ nor $B$" is the same as "not $A$ and not $B$", while "not both" is the same as "not $A$ or not $B$".


*Blanks: 0 — answers: []*

Spec links: `spcpt_g5pddg4MDHhfn69F`

Flags: fitb_no_blank_marker


## Card 3 — question_and_answer (`fl_BhPZ27dqCXSdZWyn`)

**FRONT**

How does shading tell you which region an expression such as $S ' \cap D$ describes?


**BACK**

Shade the first set, shade the second in a different colour, then take the region shaded **twice** for an intersection and every region shaded **at all** for a union.

So for $S ' \cap D$ you shade everything outside $S$, then shade $D$, and the answer is the part of $D$ that lies outside $S$.

With several symbols in one expression this is far more reliable than trying to read it in one go.


Spec links: `spcpt_g5pddg4MDHhfn69F`


## Card 4 — question_and_answer (`fl_5JX8CK6nGKPWVvfd`)

**FRONT**

What does the vertical bar in `\text{P}(A \vert B)` mean?


**BACK**

It means "**given that**", so `\text{P}(A \vert B)` is the probability that $A$ happens given that $B$ has already happened.

Being told that $B$ happened shrinks the sample space to $B$ alone, so you are no longer asking how likely $A$ is out of everything, but how likely it is out of the cases where $B$ happened.

Phrases such as "of those who" and "among the ones that" mean the same thing without using the word "given".


Spec links: `spcpt_FzzVfjwhkyjcBrzK`


## Card 5 — fill_in_the_blanks (`fl_g3s8C85QG2JwnyTR`)

**FRONT**

Fill in the formula for a conditional probability:

`\text{P}(A \vert B) = \frac{\text{P}(A \cap B)}{\_\_\_\_\_\_}`


**BACK**

The completed formula is:

`\text{P}(A \vert B) = \frac{\text{P}(A \cap B)}{\text{P}(B)}`

The event you are **given** goes underneath, because it is the new sample space you are working inside.

Rearranged, the same result gives the multiplication form `\text{P}(A \cap B) = \text{P}(B) \times \text{P}(A \vert B)`, which is the more useful direction when the intersection is what you are after.


*Blanks: 0 — answers: []*

Spec links: `spcpt_FzzVfjwhkyjcBrzK`

Flags: fitb_no_blank_marker


## Card 6 — question_and_answer (`fl_Khs68sWxXc7zBsdH`)

**FRONT**

If $A$ and $B$ are independent, what is `\text{P}(A \vert B)`, and why?


**BACK**

It is just $\text{P} ( A )$.

Independence means that $B$ happening has no effect on how likely $A$ is, so being told that $B$ happened tells you nothing new and leaves the probability where it was.

This gives a second way of testing independence, by checking whether `\text{P}(A \vert B)` and $\text{P} ( A )$ come out the same.


Spec links: `spcpt_FzzVfjwhkyjcBrzK`


## Card 7 — question_and_answer (`fl_sy4pJvJ9xrFFVNm3`)

**FRONT**

In `\text{P}\left(\left(A \cap B\right) \vert \left(A \cup B\right)\right)`, what does the numerator `\text{P}\left(\left(A \cap B\right) \cap \left(A \cup B\right)\right)` simplify to, and why?


**BACK**

It simplifies to $\text{P} ( A \cap B )$, because every outcome that is in both events is certainly in at least one of them, so intersecting with the union throws nothing away.

With regions of $0 . 2$, $0 . 2$, $0 . 3$ and $0 . 3$ that leaves $\frac{0.2}{0.7} = \frac{2}{7}$.

Spotting that one set sits entirely inside another is what turns a forbidding expression into an easy one.


Spec links: `spcpt_FzzVfjwhkyjcBrzK`


## Card 8 — question_and_answer (`fl_Rdvms6RJCjYHJRMK`)

**FRONT**

How do the cells of a two-way table for two events correspond to the regions of a Venn diagram?


**BACK**

The four inner cells are the four regions $A \cap B$, $A ' \cap B$, $A \cap B '$ and $A ' \cap B '$.

The Total row and Total column give the events themselves, $A$, $A '$, $B$ and $B '$, and the grand total is the whole sample space.

A two-way table is therefore the same information in a different shape, so either can be used on the same question.


Spec links: `spcpt_jwXsq7gMvT7TxSpP`


## Card 9 — true_or_false (`fl_HB7V343vNqCcn85p`)

**FRONT**

**True or False?**

On a two-way table, the number of pets that are dogs **or** are fed wet food is the dog total added to the wet-food total.


**BACK**

**False.**

The 28 pets that are dogs **and** are fed wet food sit inside the dog total and inside the wet-food total, so adding the two totals counts them twice over.

That shared cell has to come off once, giving $47 + 47 - 28 = 66$ out of the 80 pets.


Spec links: `spcpt_jwXsq7gMvT7TxSpP`


## Card 10 — question_and_answer (`fl_snQzyqMycDQyjhp9`)

**FRONT**

On a two-way table, how do you find the probability that a pet is fed raw food **given** that it is a dog?


**BACK**

Work inside the dog row only, so the denominator becomes the dog total rather than the grand total.

With 8 of the 47 dogs fed raw food, the probability is $\frac{8}{47}$.

A two-way table makes conditioning easy to see, because the row or column you are told about is literally the only part of the table you use.


Spec links: `spcpt_jwXsq7gMvT7TxSpP`


## Card 11 — question_and_answer (`fl_7MkNWDq5xMgsvTFg`)

**FRONT**

How do you find `\text{P}(A \vert B)` from a completed Venn diagram?


**BACK**

Add up the regions inside $B$ to get the denominator, then take as the numerator only the part of that which is also inside $A$.

The grand total plays no part at all, because being told $B$ has happened restricts you to $B$'s regions and nothing else.

Shading $B$ first and then $A$ makes it visible: the answer is the doubly shaded part over the singly shaded part.


Spec links: `spcpt_FZtYScDC38fJ2CY2`


## Card 12 — fill_in_the_blanks (`fl_yPmhYCdsy7XrWVqm`)

**FRONT**

On a Venn diagram, the bubble for $B$ lies entirely inside the bubble for $A$. Fill in the two gaps:

Whenever event $B$ happens, event $A$ also `\_\_\_\_\_\_`.

`\text{P}(A \vert B) = \_\_\_\_\_\_`


**BACK**

The completed statements are:

Whenever event $B$ happens, event $A$ also **happens**.

`\text{P}(A \vert B) = 1`

Restricted to $B$, every single outcome is also inside $A$, so the conditional probability is certain.

The reverse does not follow: $A$ can perfectly well happen without $B$, so `\text{P}(B \vert A)` is not 1.


*Blanks: 0 — answers: []*

Spec links: `spcpt_FZtYScDC38fJ2CY2`

Flags: fitb_no_blank_marker


## Card 13 — true_or_false (`fl_Sn8mW8Kv8RrjBKvF`)

**FRONT**

**True or False?**

On a Venn diagram for three events, $\text{P} ( A \cap B )$ is the number written in the region where $A$ and $B$ overlap but $C$ does not.


**BACK**

**False.**

The region where all three events happen is also inside $A$ and inside $B$, so it belongs to $A \cap B$ too and has to be added in.

With $0 . 16$ in the first of those regions and $0 . 1$ in the one where all three overlap, $\text{P} ( A \cap B ) = 0 . 26$.


Spec links: `spcpt_FZtYScDC38fJ2CY2`


## Card 14 — question_and_answer (`fl_VbSTV7RnnghdsV3G`)

**FRONT**

Three events $A$, $B$ and $C$ are such that $A$ and $C$ cannot both happen. How is that shown on a Venn diagram?


**BACK**

The bubbles for $A$ and $C$ are drawn so that they do not overlap each other, while both may still overlap $B$.

The diagram then has six regions instead of the usual eight, because the region for $A$ and $C$ together, and the region where all three happen, do not exist.

Drawing the shape correctly at the start is what stops you looking for values that were never going to be there.


Spec links: `spcpt_FZtYScDC38fJ2CY2`


## Card 15 — question_and_answer (`fl_zdPcbgBFkcn5XvCv`)

**FRONT**

How do you fill in a three-event Venn diagram when the question gives you probabilities in set notation?


**BACK**

Put each given straight into the region it names, so an intersection goes into the overlap it describes and a complement of a union goes outside all the bubbles.

Then work outwards by subtraction: $\text{P} ( A ' )$ gives you $\text{P} ( A )$, and taking away the parts of $A$ you have already filled leaves the region belonging to $A$ alone.

Whatever is missing from a total of 1 fills the last region, which also checks everything you have done.


Spec links: `spcpt_FZtYScDC38fJ2CY2`


## Card 16 — question_and_answer (`fl_tykzgVqx2XR6Y5NX`)

**FRONT**

How do you find `\text{P}(A' \vert C')` from a Venn diagram?


**BACK**

The event you are given is $C '$, so the denominator is everything outside $C$, which is $1 - \text{P} ( C )$.

The numerator is the part of that which is also outside $A$, so you add up only the regions lying outside **both** bubbles.

With $\text{P} ( C ) = 0 . 45$ and those regions totalling $0 . 3$, the answer is $\frac{0.3}{0.55} = \frac{6}{11}$.


Spec links: `spcpt_FZtYScDC38fJ2CY2`


## Card 17 — question_and_answer (`fl_qzmTYg5fBxH83C6n`)

**FRONT**

A probability question could be drawn as a Venn diagram, a tree diagram or a two-way table. What decides which one fits?


**BACK**

Use a **tree diagram** when one event follows another, such as drawing two beads without replacing the first, because a tree is what shows the second event's probabilities changing.

Use a **two-way table** when the items are classified in two ways at once, such as a year group split by gender and by chosen sport.

A **Venn diagram** suits most other cases, and is the natural choice when the question is written in set notation to begin with.


Spec links: `spcpt_FZtYScDC38fJ2CY2`


## Card 18 — question_and_answer (`fl_fJFNpbvXn8BKR7FW`)

**FRONT**

On a tree diagram, what does the number written on a branch of the **second** experiment actually represent?


**BACK**

It is a **conditional** probability: the probability of that second outcome **given** the first outcome you travelled through to reach it, written `\text{P}(B \vert A)`.

That is exactly why the upper set of second branches can carry different numbers from the lower set.

A tree diagram therefore displays conditional probabilities directly, which no other diagram does.


Spec links: `spcpt_qqShgKnf3SR5y4KX`


## Card 19 — question_and_answer (`fl_k5xrWDdJKPnfh75X`)

**FRONT**

On a tree diagram for events $F$ and $W$, which complete paths make up $F ' \cap W$, and which make up $F \cup W$?


**BACK**

$F ' \cap W$ is the single path that goes through $F '$ and then through $W$.

$F \cup W$ is three of the four paths: every one except the path that goes through $F '$ and then $W '$, since that is the only path on which neither event happens.

Translating the set notation into paths before calculating anything is what keeps a wordy question straight.


Spec links: `spcpt_qqShgKnf3SR5y4KX`


## Card 20 — true_or_false (`fl_v8JkFgSKrSKXr5J5`)

**FRONT**

**True or False?**

Every "given that" probability in a question can be read straight off a branch of the tree diagram.


**BACK**

**False.**

Only conditionals of the form "second outcome given first outcome" appear as branch labels, because that is the order the tree is built in.

A reversed one such as `\text{P}(F \vert W)`, where $W$ is the second event, is nowhere on the diagram and has to be worked backwards from the completed paths.


Spec links: `spcpt_qqShgKnf3SR5y4KX`


## Card 21 — question_and_answer (`fl_TGgTTHty5TMpG5k2`)

**FRONT**

The probability along a complete path is the product of its branch labels. Given that $\text{P} ( F ' \cap W ) = 0 . 15$ and $\text{P} ( F ' ) = 0 . 25$, what is the branch label for $W$ after $F '$?


**BACK**

It is $0 . 6$, found by dividing:

$\frac{0.15}{0.25} = 0 . 6$

That label is `\text{P}(W \vert F')`, the probability of $W$ given that $F '$ happened.

A path probability given in a question is nearly always meant to be divided like this, because it is one step further on than the branch you actually need.


Spec links: `spcpt_qqShgKnf3SR5y4KX`


## Card 22 — fill_in_the_blanks (`fl_Bcvw5yqQMz6zPGWW`)

**FRONT**

Fill in the missing path so that the probability of the second event is complete:

`\text{P}(B) = \text{P}(A \cap B) + \_\_\_\_\_\_`


**BACK**

The completed result is:

$\text{P} ( B ) = \text{P} ( A \cap B ) + \text{P} ( A ' \cap B )$

Event $B$ can be reached along two paths, one through $A$ and one through $A '$, and there is no third way to get there.

Adding them is what turns branch information into a probability for the second event on its own, which a tree never shows you directly.


*Blanks: 0 — answers: []*

Spec links: `spcpt_qqShgKnf3SR5y4KX`

Flags: fitb_no_blank_marker


## Card 23 — question_and_answer (`fl_GHDh9s59xnyyB8Hr`)

**FRONT**

How do you find `\text{P}(F' \vert W')` from a tree diagram?


**BACK**

Find $\text{P} ( F ' \cap W ' )$ by multiplying along that one path, find $\text{P} ( W ' )$ by adding both paths that end in $W '$, then divide the first by the second.

With $0 . 1$ on the path and $0 . 15 + 0 . 1 = 0 . 25$ for $W '$ altogether, the answer is $\frac{0.1}{0.25} = 0 . 4$.

The conditioning event is the one on the **second** set of branches here, which is why the calculation runs backwards along the tree.


Spec links: `spcpt_qqShgKnf3SR5y4KX`


## Card 24 — question_and_answer (`fl_ThK2jgG66DFDYKWt`)

**FRONT**

A tree diagram has three possible outcomes at each of three experiments. How many complete paths does it have, and what does that mean for using it?


**BACK**

It has $3 \times 3 \times 3 = 27$ complete paths, because the number of outcomes at each stage multiplies.

With that many, listing every path and its probability is not practical, so you identify only the paths the question actually asks about and work out those.

This is why a tree stops being the best diagram once there are more than two or three outcomes per event.


Spec links: `spcpt_qqShgKnf3SR5y4KX`


## Card 25 — fill_in_the_blanks (`fl_yDPRZJ9VTh9Nf8mZ`)

**FRONT**

Fill in the missing term in the addition formula:

`\text{P}(A \cup B) = \text{P}(A) + \text{P}(B) - \_\_\_\_\_\_`


**BACK**

The completed formula is:

$\text{P} ( A \cup B ) = \text{P} ( A ) + \text{P} ( B ) - \text{P} ( A \cap B )$

Adding $\text{P} ( A )$ and $\text{P} ( B )$ counts the outcomes where both events happen **twice**, once inside each event, so they have to be taken off once.

On a Venn diagram this is the region shaded twice over, which is where the formula comes from.


*Blanks: 0 — answers: []*

Spec links: `spcpt_4XqYGqKNNWgv2SVd`

Flags: fitb_no_blank_marker


## Card 26 — true_or_false (`fl_k4sV7d8Mq5Phc3rJ`)

**FRONT**

**True or False?**

The addition formula holds for any two events, whether or not they are mutually exclusive.


**BACK**

**True.**

Unlike the two rules that come with conditions attached to them, this one carries no condition at all.

The subtracted term takes care of whatever overlap the two events happen to have, so nothing has to be checked before using it.


Spec links: `spcpt_4XqYGqKNNWgv2SVd`


## Card 27 — question_and_answer (`fl_rZYbkBbTDGt2Mzhv`)

**FRONT**

A question gives $\text{P} ( A )$, $\text{P} ( B )$ and $\text{P} ( A \cup B )$, and asks for $\text{P} ( A \cap B )$. How do you get it?


**BACK**

Rearrange the addition formula to

$\text{P} ( A \cap B ) = \text{P} ( A ) + \text{P} ( B ) - \text{P} ( A \cup B )$

The two arrangements look almost identical, differing only in which of the union and the intersection is on the left.

So write down which of the two the question has actually given you before you substitute anything.


Spec links: `spcpt_4XqYGqKNNWgv2SVd`


## Card 28 — question_and_answer (`fl_D3Z7JtGBKHgkHCMy`)

**FRONT**

Why is the addition formula not needed when two events are mutually exclusive?


**BACK**

Because mutually exclusive events share no outcomes at all, so nothing has been counted twice and the term being subtracted is zero.

The formula then collapses to the simpler rule that the probabilities just add.

That simpler rule is a special case of the addition formula rather than a separate result, which is why you only ever need to remember one of them.


Spec links: `spcpt_4XqYGqKNNWgv2SVd`


## Card 29 — question_and_answer (`fl_r2DmWxrz8jGZ57wX`)

**FRONT**

Most probability questions can be answered from a diagram. When is a formula the more practical route?


**BACK**

When the question gives you probabilities and nothing that would fill a diagram, so there are no regions or branches to read anything off.

That happens whenever you are told the probabilities of **combined** events, such as a union or an intersection, without being told how the individual outcomes split up.

A diagram can often be built afterwards, once a formula has supplied the missing value.


Spec links: `spcpt_4XqYGqKNNWgv2SVd`


## Card 30 — question_and_answer (`fl_Qq9YYJSyYzxDPt28`)

**FRONT**

The probability that the first match runs long is 0.15, that both of the first two do is 0.06, and that at least one of them does is 0.32. What is the probability that the second runs long?


**BACK**

It is $0 . 23$.

"At least one" is the union and "both" is the intersection, so substituting into the addition formula gives

$0 . 32 = 0 . 15 + \text{P} ( M_{2} ) - 0 . 06$

Turning the wording into unions and intersections is the whole difficulty in a question like this, and once that is done it is a single equation.


Spec links: `spcpt_4XqYGqKNNWgv2SVd`

