# Further Probability

Course: ial-maths-20-statistics-1 · Section: Probability

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-1/flashcards/probability/further-probability/


## Card 1 — question_and_answer (`fl_XZ437fzQZXZP745q`)

**FRONT**

In set notation, what do $A \cap B$ and $A \cup B$ mean?


**BACK**

$A \cap B$ is the **intersection** of $A$ and $B$: the event that **both** of them happen, shown on a Venn diagram as the overlap between the two bubbles.

$A \cup B$ is the **union** of $A$ and $B$: the event that $A$ happens, or $B$ happens, **or both do**, shown as both bubbles together, including their overlap.

The union is the one to be careful with, because in everyday speech "or" usually means one or the other but not both.


Spec links: `spcpt_Gt3d7rKV2X8h4pwd`


## Card 2 — fill_in_the_blanks (`fl_fQSWWwF5kCmmfG3p`)

**FRONT**

Complete the two ways of rewriting the complement of a combined event, by filling in the missing set-notation symbol each time:

`\left(A \cup B\right)' = A' \_\_\_\_\_\_ B'`

`\left(A \cap B\right)' = A' \_\_\_\_\_\_ B'`


**BACK**

The completed statements are:

`\left(A \cup B\right)' = A' \cap B'`

`\left(A \cap B\right)' = A' \cup B'`

The operation **swaps** when the complement is taken. In words, "not ($A$ or $B$)" means neither of them happened, which is "not $A$" **and** "not $B$".

If you are not convinced, sketch a Venn diagram and shade each side.


*Blanks: 0 — answers: ['swaps', 'and']*

Spec links: `spcpt_Gt3d7rKV2X8h4pwd`

Flags: blank_answer_mismatch


## Card 3 — question_and_answer (`fl_fjXRdjXyKbN4w7Q5`)

**FRONT**

Two events are mutually exclusive. Written in set notation, what is their intersection?


**BACK**

The intersection of two mutually exclusive events is the **empty set**:

$A \cap B = \emptyset$

The empty set has no elements in it, so there is no outcome belonging to both events, and `\text{P} \left(A \cap B\right) = 0`.

On a Venn diagram the two bubbles do not overlap at all.


Spec links: `spcpt_Gt3d7rKV2X8h4pwd`


## Card 4 — keyword_definition (`fl_ZxRr7wSvFf5fsrDH`)

**FRONT**

Define **conditional probability**.


**BACK**

Conditional probability is the probability of an event when that probability **depends on the outcome of an earlier event**.

It is written with a vertical line, so `\text{P} \left(A \vert B\right)` is read as "the probability of $A$, **given that** $B$ has happened".

So, **for example**, a bag holds 6 white and 3 red buttons, and one is drawn and not replaced before a second is drawn:

`\text{P} \left(\text{2nd is white} \vert \text{1st is white}\right) = \frac{5}{8}`

because only 5 white buttons are left out of the 8 remaining.


Spec links: `spcpt_mpb85fVZSQGr3tkK`


## Card 5 — question_and_answer (`fl_BGBfn4RbZ8vDT86k`)

**FRONT**

When you work out `\text{P} \left(A \vert B\right)`, why do you divide by `\text{P} \left(B\right)` rather than by the total of the whole sample space?


**BACK**

Being told that $B$ has happened **reduces the sample space**: outcomes outside $B$ are no longer possible, so $B$ itself becomes the new whole.

The only part of $B$ that also gives $A$ is $A \cap B$, so

`\text{P} \left(A \vert B\right) = \frac{\text{P} \left(A \cap B\right)}{\text{P} \left(B\right)}`

This is why the denominator of a conditional probability is almost never the total of everything shown on a diagram.


Spec links: `spcpt_mpb85fVZSQGr3tkK`


## Card 6 — true_or_false (`fl_F8VhhPCWCS9XnZrh`)

**FRONT**

**True or False?**

Drawing two counters from a bag one at a time, without replacement, is mathematically the same as drawing both counters at once.


**BACK**

**True.**

Not replacing the first counter means the second is drawn from what is left, which is exactly the situation you are in if you take both together, and every pair of counters has the same probability either way.

This assumes you care only about **which** counters are drawn and not about the order they came out in, which is what these questions ask.

It is worth knowing, because a question about taking two counters at once can then be answered with a tree diagram and conditional probabilities.


Spec links: `spcpt_mpb85fVZSQGr3tkK`


## Card 7 — question_and_answer (`fl_wvPG37xQJg63qSw6`)

**FRONT**

If $A$ and $B$ are independent, what does `\text{P} \left(A | B\right)` simplify to, and why?


**BACK**

`\text{P} \left(A \vert B\right)` simplifies to `\text{P} \left(A\right)`, because independence means that $B$ happening has no effect on $A$, so being told $B$ has happened changes nothing.

The formula shows the same thing: for independent events `\text{P} \left(A \cap B\right) = \text{P} \left(A\right) \times \text{P} \left(B\right)`, so

`\text{P} \left(A \vert B\right) = \frac{\text{P} \left(A\right) \times \text{P} \left(B\right)}{\text{P} \left(B\right)} = \text{P} \left(A\right)`

The same argument gives `\text{P} \left(B \vert A\right) = \text{P} \left(B\right)`.


Spec links: `spcpt_mpb85fVZSQGr3tkK`


## Card 8 — fill_in_the_blanks (`fl_VNFFBkmBnDNShRgQ`)

**FRONT**

A two-way table has the outcomes of event $A$ across the columns and the outcomes of event $B$ down the rows. Complete what a single cell of the table holds:

`\text{the cell where the } A \text{ column meets the } B \text{ row holds } A \_\_\_\_\_\_ B`


**BACK**

The completed statement is:

$\text{the cell where the} A \text{column meets the} B \text{row holds} A \cap B$

Every cell of a two-way table is an **intersection**, so each one matches a region of a Venn diagram.

The **Total** row and **Total** column then give the events themselves: the total of the $A$ column is $A$, made up of $A \cap B$ and $A \cap B '$. The grand total in the corner is the whole sample space.


*Blanks: 0 — answers: ['intersection', 'Total', 'Total']*

Spec links: `spcpt_JT3NWnKdmfk6J6mh`

Flags: blank_answer_mismatch


## Card 9 — question_and_answer (`fl_S8zjmxszTq4F5z5n`)

**FRONT**

A two-way table records 47 dogs and 33 cats, and 8 of the dogs are fed raw food. To find the probability that a pet is fed raw food **given that it is a dog**, which total do you divide by?


**BACK**

Divide by the total for the **given** event only, which is the 47 dogs:

`\text{P} \left(\text{raw} | \text{dog}\right) = \frac{8}{47}`

Being told the pet is a dog rules out every cat, so the dog row becomes the whole sample space.

Dividing by the grand total of all 80 pets would answer a different question: the probability that a pet is **both** a dog and fed raw food, which is $\frac{8}{80}$.


Spec links: `spcpt_JT3NWnKdmfk6J6mh`


## Card 10 — question_and_answer (`fl_rX8jTGVjH5QDr8xG`)

**FRONT**

Several cells of a two-way table in a question are left blank. How do you fill them in?


**BACK**

Look for a row or a column with **only one value missing**, since that value must be the total minus everything else in the line.

Filling in one cell usually leaves another row or column with a single gap, so the table completes itself a cell at a time.

Check first that you have the grand total: it is often given in the wording of the question rather than printed in the table, and without it none of the totals can be worked out.


Spec links: `spcpt_JT3NWnKdmfk6J6mh`


## Card 11 — question_and_answer (`fl_fnZyppBm7DdVkrxS`)

**FRONT**

How do you use shading to read `\text{P} \left(A | B\right)` off a Venn diagram?


**BACK**

Shade the **given** event first, then shade the event you want on top of it.

So for `\text{P} \left(A \vert B\right)`, shade $B$, then shade $A \cap B$ over it, and the answer is

`\text{P} \left(A \vert B\right) = \frac{\text{double shading}}{\text{all shading}}`

Sketch a separate small copy of the diagram for each part of a question, since each part needs a different region shaded and two shadings on one diagram cannot be told apart.


Spec links: `spcpt_JfGQz47zpqCG2C9v`


## Card 12 — fill_in_the_blanks (`fl_hP6T8HvJphKfF6FP`)

**FRONT**

The given event in a conditional probability can itself be a combined event. Complete the formula:

`\text{P} \left(C | \left(A \cup B\right)'\right) = \frac{\text{P} \left(\_\_\_\_\_\_\right)}{\text{P} \left(\left(A \cup B\right)'\right)}`


**BACK**

The completed formula is:

`\text{P} \left(C | \left(A \cup B\right)'\right) = \frac{\text{P} \left(C \cap \left(A \cup B\right)'\right)}{\text{P} \left(\left(A \cup B\right)'\right)}`

Nothing changes: whatever is written after the vertical line is the given event, so it is what you shade first and it is the denominator. The numerator is the part of that region which is also $C$.

So, **for example**, if the region inside $C$ but outside both $A$ and $B$ has probability 0.15, and the region outside all three has probability 0.1, the answer is $\frac{0.15}{0.15+0.1} = \frac{3}{5}$.


*Blanks: 0 — answers: ['for example']*

Spec links: `spcpt_JfGQz47zpqCG2C9v`

Flags: blank_answer_mismatch


## Card 13 — question_and_answer (`fl_GGSptFzZJRfXWVZs`)

**FRONT**

Why do `\text{P} \left(A \vert B\right)` and `\text{P} \left(B \vert A\right)` usually come out different, when both are read from the same Venn diagram?


**BACK**

`\text{P} \left(A \vert B\right)` and `\text{P} \left(B \vert A\right)` have the **same numerator**, `\text{P} \left(A \cap B\right)`, which is the region shaded twice either way.

What changes is the **denominator**, because that is whichever event is given:

`\text{P} \left(A \vert B\right) = \frac{\text{P} \left(A \cap B\right)}{\text{P} \left(B\right)}`

`\text{P} \left(B \vert A\right) = \frac{\text{P} \left(A \cap B\right)}{\text{P} \left(A\right)}`

So swapping them changes the answer, unless `\text{P} \left(A\right)` and `\text{P} \left(B\right)` happen to be equal; reading the question carefully to see which event is the given one is what decides it.


Spec links: `spcpt_JfGQz47zpqCG2C9v`


## Card 14 — true_or_false (`fl_CM7McXPffSnhhVsP`)

**FRONT**

**True or False?**

`\text{P} \left(A' | B'\right) = 1 - \text{P} \left(A | B\right)`


**BACK**

**False.**

Complementing the event you **want** does give a subtraction from 1:

`\text{P} \left(A' | B\right) = 1 - \text{P} \left(A | B\right)`

since inside $B$ either $A$ happens or it does not.

But complementing the **given** event moves you into a different region of the diagram altogether. `\text{P} \left(A' | B'\right)` is worked out inside $B '$, which shares no outcomes with $B$, so it has to be found from scratch as `\frac{\text{P} \left(A' \cap B'\right)}{\text{P} \left(B'\right)}`.


Spec links: `spcpt_JfGQz47zpqCG2C9v`


## Card 15 — question_and_answer (`fl_7MKn2R4Rn4NzYcFZ`)

**FRONT**

On a Venn diagram for three events, which region is `\text{P} \left(\left(A \cup B \cup C\right)'\right)`?


**BACK**

`\left(A \cup B \cup C\right)'` is the region inside the rectangle but **outside all three bubbles**: the outcomes where none of the three events happens.

It is easy to overlook, because nothing is drawn there, but it is part of the sample space and it has to be filled in.

It is often the last value you work out, since every region on the diagram must total 1.


Spec links: `spcpt_JfGQz47zpqCG2C9v`


## Card 16 — question_and_answer (`fl_TrshrhSG6N9Sd9wM`)

**FRONT**

On a tree diagram, what does the number labelling a **second-experiment** branch represent?


**BACK**

The number on a second-experiment branch is a **conditional probability**: the probability of that outcome given the branch you arrived along.

So on a tree running from $A$ to $B$, the upper pair of second branches are labelled `\text{P} \left(B | A\right)` and `\text{P} \left(B' | A\right)`, and the lower pair are labelled `\text{P} \left(B | A'\right)` and `\text{P} \left(B' | A'\right)`.

That is why the two pairs can carry different numbers: they are conditional on different things.


Spec links: `spcpt_wDKP7rTqCr2Fj6QR`


## Card 17 — fill_in_the_blanks (`fl_NcdcWTN9mDfpMtXQ`)

**FRONT**

A tree diagram runs from event $A$ to event $B$. Complete the probability of the path along the top:

`\text{P} \left(A \cap B\right) = \text{P} \left(A\right) \times \text{P} \left(\_\_\_\_\_\_\right)`


**BACK**

The completed formula is:

`\text{P} \left(A \cap B\right) = \text{P} \left(A\right) \times \text{P} \left(B | A\right)`

This is the **multiplication formula**, and it is only what multiplying along the branches does, written out in notation: the first branch gives `\text{P} \left(A\right)` and the second gives `\text{P} \left(B | A\right)`.

Writing `\text{P} \left(A\right) \times \text{P} \left(B\right)` instead is correct **only** when the two events are independent.


*Blanks: 0 — answers: ['multiplication formula', 'only']*

Spec links: `spcpt_wDKP7rTqCr2Fj6QR`

Flags: blank_answer_mismatch


## Card 18 — question_and_answer (`fl_SNFtN2ySjN3X2fhX`)

**FRONT**

A question tells you that `\text{P} \left(F' \cap W\right) = 0.15`, where $F$ is the first event on a tree diagram and $W$ is the second. Where does that number belong on the diagram, and what can you get from it?


**BACK**

`\text{P} \left(F' \cap W\right)` is a **path** probability, not a branch label, so it belongs in the outcome column at the end of the path that goes $F '$ then $W$.

Since a path probability is the product of the branches along it, dividing by the first branch recovers the second:

`\text{P} \left(W | F'\right) = \frac{\text{P} \left(F' \cap W\right)}{\text{P} \left(F'\right)}`

So if `\text{P} \left(F'\right) = 0.25`, the missing branch label is $\frac{0.15}{0.25} = 0 . 6$.


Spec links: `spcpt_wDKP7rTqCr2Fj6QR`


## Card 19 — question_and_answer (`fl_b7fywGcHD7kx7xQX`)

**FRONT**

On a tree diagram with $A$ first and $B$ second, why can `\text{P} \left(B \vert A\right)` be read straight off the diagram while `\text{P} \left(A \vert B\right)` cannot?


**BACK**

A tree diagram is built in the order the events happen, so `\text{P} \left(B \vert A\right)` conditions on the **earlier** event and is exactly what a second branch is labelled with.

`\text{P} \left(A \vert B\right)` conditions on the **later** event, which runs against the way the diagram is drawn, so no branch carries it.

It has to be worked out instead, from

`\text{P} \left(A \vert B\right) = \frac{\text{P} \left(A \cap B\right)}{\text{P} \left(B\right)}`


Spec links: `spcpt_wDKP7rTqCr2Fj6QR`


## Card 20 — question_and_answer (`fl_fChbMCD7JxgnDJqm`)

**FRONT**

A tree diagram runs from $F$ to $W$, and all four path probabilities are known. How do you find `\text{P} \left(F | W'\right)`?


**BACK**

Divide the path you want by the total of **every** path that ends in $W '$:

`\text{P} \left(F \vert W '\right) = \frac{\text{P} \left(F \cap W '\right)}{\text{P} \left(F \cap W '\right) + \text{P} \left(F ' \cap W '\right)}`

The denominator is `\text{P} \left(W '\right)`, which is not written anywhere on the diagram: there are two routes to $W '$, through $F$ and through $F '$, and they cannot both happen, so their probabilities add.

So, **for example**, with `\text{P} \left(F \cap W '\right) = 0 . 15` and `\text{P} \left(F ' \cap W '\right) = 0 . 1`, the answer is $\frac{0.15}{0.25} = 0 . 6$; follow those two steps rather than memorising the formula, since the same logic works whichever way round the events are.


Spec links: `spcpt_wDKP7rTqCr2Fj6QR`


## Card 21 — question_and_answer (`fl_zrs9DBXz9br7wKCm`)

**FRONT**

In the addition formula `\text{P} \left(A \cup B\right) = \text{P} \left(A\right) + \text{P} \left(B\right) - \text{P} \left(A \cap B\right)`, why is the last term subtracted?


**BACK**

Adding `\text{P} \left(A\right)` and `\text{P} \left(B\right)` counts the **overlap twice**, because every outcome in $A \cap B$ lies inside both bubbles. Subtracting it once leaves every region of the union counted exactly once.

For **mutually exclusive** events there is no overlap, so `\text{P} \left(A \cap B\right) = 0` and the formula collapses to

`\text{P} \left(A \cup B\right) = \text{P} \left(A\right) + \text{P} \left(B\right)`


Spec links: `spcpt_jgKvwpptbcVFZqgq`


## Card 22 — fill_in_the_blanks (`fl_9YgZNZFRjgpsvz2s`)

**FRONT**

The formula booklet gives the addition formula, but not this rearrangement of it. Complete the rearrangement:

`\text{P} \left(A \cap B\right) = \text{P} \left(A\right) + \text{P} \left(B\right) - \text{P} \left(\_\_\_\_\_\_\right)`


**BACK**

The completed rearrangement is:

`\text{P} \left(A \cap B\right) = \text{P} \left(A\right) + \text{P} \left(B\right) - \text{P} \left(A \cup B\right)`

The intersection and the union simply swap places.

You need this form whenever a question gives you the **union** and asks about the **intersection**, or the other way round. So, **for example**, with `\text{P} \left(A\right) = 0.15`, `\text{P} \left(A \cap B\right) = 0.06` and `\text{P} \left(A \cup B\right) = 0.32`, it rearranges once more to give `\text{P} \left(B\right) = 0.06 - 0.15 + 0.32 = 0.23`.


*Blanks: 0 — answers: ['union', 'intersection', 'for example']*

Spec links: `spcpt_jgKvwpptbcVFZqgq`

Flags: blank_answer_mismatch


## Card 23 — question_and_answer (`fl_dX9QYSy5bBQg6Zcc`)

**FRONT**

How is the multiplication formula `\text{P} \left(A \cap B\right) = \text{P} \left(B\right) \times \text{P} \left(A | B\right)` related to the conditional probability formula?


**BACK**

The multiplication formula is the conditional probability formula rearranged: multiplying both sides of

`\text{P} \left(A \vert B\right) = \frac{\text{P} \left(A \cap B\right)}{\text{P} \left(B\right)}`

by `\text{P} \left(B\right)` gives it.

So there is one result here rather than two, and which form you write down depends only on which of the three probabilities is the one you are missing.

The letters are interchangeable, so `\text{P} \left(A \cap B\right) = \text{P} \left(A\right) \times \text{P} \left(B \vert A\right)` is equally valid.


Spec links: `spcpt_jgKvwpptbcVFZqgq`


## Card 24 — true_or_false (`fl_t8MQXnxTRcP5P97V`)

**FRONT**

**True or False?**

`\text{P} \left(A \cap B\right) = \text{P} \left(A\right) \times \text{P} \left(B\right)` can be used for any two events.


**BACK**

**False.**

That formula is the one for **independent** events: it says that $B$ happening makes no difference to $A$, which is a real condition and not something that holds automatically.

The version that works whatever the events is the multiplication formula:

`\text{P} \left(A \cap B\right) = \text{P} \left(A\right) \times \text{P} \left(B \vert A\right)`

The two agree exactly when `\text{P} \left(B \vert A\right) = \text{P} \left(B\right)`, and that is what independence means.


Spec links: `spcpt_jgKvwpptbcVFZqgq`


## Card 25 — question_and_answer (`fl_82nBzXQSSBJMpCvJ`)

**FRONT**

What structural difference decides whether a probability problem is best drawn as a tree diagram or as a Venn diagram?


**BACK**

What decides it is whether the events happen **one after another** or are properties of the **same single outcome**.

A **tree diagram** suits events in succession, because each set of branches can be conditional on the branch before it.

A **Venn diagram**, or a two-way table, suits events that can overlap, because one region can belong to more than one event at once.


Spec links: `spcpt_jgKvwpptbcVFZqgq`

