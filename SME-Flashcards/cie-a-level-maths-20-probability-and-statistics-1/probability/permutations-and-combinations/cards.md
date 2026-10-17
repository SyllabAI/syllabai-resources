# Permutations & Combinations

Course: cie-a-level-maths-20-probability-and-statistics-1 · Section: Probability

Source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/flashcards/probability/permutations-and-combinations/


## Card 1 — keyword_definition (`fl_c4C9KtqxH45KD7HG`)

**FRONT**

Define **factorial**.


**BACK**

The **factorial** of a non-negative whole number $n$, written $n !$, is the result of multiplying $n$ by every whole number below it down to 1.

So, **for example**, $5 ! = 5 \times 4 \times 3 \times 2 \times 1 = 120$.

It is an operation in its own right, in the same way that $+$ and $\times$ are, and it is written after the number rather than before it.


Spec links: `spcpt_v9GnPyX4sbCvf8Ff`


## Card 2 — question_and_answer (`fl_tKSBfPfFr6csMfbm`)

**FRONT**

Why is the number of ways of arranging $n$ **different** objects in a row equal to $n !$?


**BACK**

Because the positions are filled one at a time: any of the $n$ objects can go first, $n - 1$ are left for the second position, $n - 2$ for the third, and so on until one object is left for the last.

The number of choices at each stage multiplies together, and that product is exactly the factorial of $n$.

This is why factorials appear everywhere in counting problems rather than only in this one.


Spec links: `spcpt_7gKmB69fTvMSjrvw`


## Card 3 — fill_in_the_blanks (`fl_PRCYWBbCzqh6pbHX`)

**FRONT**

Fill in the two gaps:

The value of $0 !$ is `\_\_\_\_\_\_`.

The factorial of a negative number is `\_\_\_\_\_\_`.


**BACK**

The completed statements are:

The value of $0 !$ is **1**.

The factorial of a negative number is **not defined**.

Zero objects can be arranged in exactly one way, which is to arrange nothing at all, whereas there is no way at all to arrange a negative number of objects.


*Blanks: 0 — answers: []*

Spec links: `spcpt_v9GnPyX4sbCvf8Ff`

Flags: fitb_no_blank_marker


## Card 4 — question_and_answer (`fl_DyZkDMC5GQ4gzrxt`)

**FRONT**

How do you simplify a fraction with a larger factorial on top and a smaller one underneath, such as $\frac{8!}{5!}$?


**BACK**

Write the larger factorial out only as far down as the smaller one reaches, because every factor from the smaller factorial downwards cancels.

That leaves

$\frac{8!}{5!} = 8 \times 7 \times 6$

and the same cancelling works whatever the two factorials are, which is what keeps the numbers manageable.


Spec links: `spcpt_v9GnPyX4sbCvf8Ff`


## Card 5 — question_and_answer (`fl_Fst6Vrzqv8QdvYtM`)

**FRONT**

When the objects being arranged in a row are not all different, what has to be done to $n !$, and why?


**BACK**

Divide by the factorial of the number of copies of each repeated object.

Each arrangement has been counted once for every way the identical copies could be swapped over, and all those swaps give the same-looking row.

So with one object repeated $r$ times the count is $\frac{n!}{r!}$, and with a second object repeated $s$ times it is $\frac{n!}{r!s!}$.


Spec links: `spcpt_7gKmB69fTvMSjrvw`


## Card 6 — true_or_false (`fl_Xgf7FSPyq76tsBgx`)

**FRONT**

**True or False?**

The word REVISE has six letters, so it has $6 ! = 720$ different arrangements.


**BACK**

**False.**

The two Es are identical, so REVISE has only **360** different-looking arrangements.

The answer 720 would be right only if all six letters were different, which is why checking for repeated letters is the first thing to do.


Spec links: `spcpt_7gKmB69fTvMSjrvw`


## Card 7 — fill_in_the_blanks (`fl_SZPz7KsxT4jGgVsg`)

**FRONT**

Fill in the two standard factorial results:

`\frac{n!}{\left(n - 1\right)!} = \_\_\_\_\_\_`

`\frac{n!}{\left(n - 2\right)!} = \_\_\_\_\_\_`


**BACK**

The completed results are:

`\frac{n!}{\left(n - 1\right)!} = n`

`\frac{n!}{\left(n - 2\right)!} = n \left(n - 1\right)`

Both follow from `n! = n \times \left(n - 1\right)!`, which lets you peel one factor at a time off the front of a factorial.

Results like these are what turn an equation containing factorials into an ordinary equation you can solve.


*Blanks: 0 — answers: []*

Spec links: `spcpt_v9GnPyX4sbCvf8Ff`

Flags: fitb_no_blank_marker


## Card 8 — keyword_definition (`fl_XKDPTsdWy9mBYrF3`)

**FRONT**

Define **permutation**.


**BACK**

A **permutation** is an arrangement of objects in which the **order** matters, so the same objects in a different order count as a different permutation.

It covers both arranging all $n$ of the objects and arranging only $r$ of them chosen from $n$.

So, **for example**, AB and BA are two different permutations of the letters A and B.


Spec links: `spcpt_89ps9KCVtj4YGq2C`


## Card 9 — fill_in_the_blanks (`fl_4PgmNbhP25cpZgKN`)

**FRONT**

Fill in the formula for the number of ways of arranging $r$ objects chosen from $n$ different objects:

`{}^{n}\text{P}_{r} = \frac{n!}{\_\_\_\_\_\_}`


**BACK**

The completed formula is:

`{}^{n}\text{P}_{r} = \frac{n!}{\left(n - r\right)!}`

The `\left(n - r\right)!` underneath cancels away the arrangements of the objects you did **not** choose, leaving only the $r$ positions you are filling.

So, **for example**, arranging 3 objects chosen from 5 gives $\frac{5!}{2!} = 5 \times 4 \times 3 = 60$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_89ps9KCVtj4YGq2C`

Flags: fitb_no_blank_marker


## Card 10 — question_and_answer (`fl_dGSGBp3MTv9z77ZN`)

**FRONT**

Besides arranging $r$ objects chosen from $n$, what else does `{}^{n}\text{P}_{r}` count?


**BACK**

It counts the ways of placing a **smaller** number of objects into a **larger** number of spaces, at most one object to a space.

So, **for example**, seating 5 people in a row of 10 empty chairs is `{}^{10}\text{P}_{5}`, because you are choosing which chairs get used and in which order.

Spotting this second reading is what makes the formula usable on problems that never mention choosing anything.


Spec links: `spcpt_89ps9KCVtj4YGq2C`


## Card 11 — question_and_answer (`fl_fGkZJ7N5S4WGhS9t`)

**FRONT**

How do you count the arrangements in which two or more particular items must **stay together**?


**BACK**

Treat the items that must stay together as a **single object**, and count the arrangements of the shorter list that results.

Then count the arrangements of those items **within** their block, and multiply the two counts together.

So, **for example**, the seven letters of ORANGES with the three vowels together give $5 ! \times 3 ! = 720$.


Spec links: `spcpt_89ps9KCVtj4YGq2C`


## Card 12 — true_or_false (`fl_8njgMGm865fgtnJG`)

**FRONT**

**True or False?**

Subtracting the arrangements in which three items are all together from the total leaves the arrangements in which the three items are all separated.


**BACK**

**False.**

What is left over also includes every arrangement in which exactly **two** of the three items are next to each other, since those were never subtracted.

"Not all together" and "all separated" are different conditions, and the subtraction answers only the first of them.


Spec links: `spcpt_89ps9KCVtj4YGq2C`


## Card 13 — question_and_answer (`fl_RZCKngH8FBbMH6Vv`)

**FRONT**

How do you count the arrangements in which several particular items must **all be separated** from one another?


**BACK**

First arrange all the **other** items, then count the gaps between them, remembering the gap before the first item and the gap after the last, so $k$ other items leave $k + 1$ gaps.

Then place the items that have to be kept apart into those gaps, at most one to a gap, and multiply the two counts together.

So, **for example**, ORANGES with its three vowels all separated gives `4! \times {}^{5}\text{P}_{3} = 1440`.


Spec links: `spcpt_89ps9KCVtj4YGq2C`


## Card 14 — question_and_answer (`fl_Z4qnjXvh7YkwRm4X`)

**FRONT**

The letters of BANANAS are arranged with the B and the S at the two ends. Why is the answer not simply the number of arrangements of the middle five letters?


**BACK**

Because the B and the S can also be swapped over, so each arrangement of the middle five letters occurs twice, once with the B first and once with the S first.

The count is therefore

$\frac{5!}{3!2!} \times 2 ! = 20$

Asking whether the items you pinned in place could be interchanged is the step most often left out.


Spec links: `spcpt_89ps9KCVtj4YGq2C`


## Card 15 — keyword_definition (`fl_4DRBzw3xmYMDHw7D`)

**FRONT**

Define **combination**.


**BACK**

A **combination** is a selection of $r$ objects from $n$ in which the **order** does not matter, so the same objects picked in a different order count only once.

So, **for example**, choosing two letters from CAB, the selections AB and BA are one combination although they are two permutations.

The number of combinations is written `{}^{n}\text{C}_{r}` and read "$n$ choose $r$".


Spec links: `spcpt_fVVc579xDmZm4X5t`


## Card 16 — fill_in_the_blanks (`fl_4xF42pXq6NJtFZwD`)

**FRONT**

Fill in the gap linking the two counting formulae:

`{}^{n}\text{C}_{r} = \frac{{}^{n}\text{P}_{r}}{\_\_\_\_\_\_}`


**BACK**

The completed link is:

`{}^{n}\text{C}_{r} = \frac{{}^{n}\text{P}_{r}}{r!}`

Every selection of $r$ objects has been counted once for each of the $r !$ orders those objects could have been picked in, so dividing removes the orderings and leaves the selections.

Writing `{}^{n}\text{P}_{r}` out in full then gives `{}^{n}\text{C}_{r} = \frac{n!}{r! \left(n - r\right)!}`.


*Blanks: 0 — answers: []*

Spec links: `spcpt_fVVc579xDmZm4X5t`

Flags: fitb_no_blank_marker


## Card 17 — true_or_false (`fl_qCwZJK8VrwTF7QrN`)

**FRONT**

**True or False?**

`{}^{n}\text{C}_{r}` always works out to a whole number, even though its formula is a fraction.


**BACK**

**True.**

It counts how many different selections there are, and there is no such thing as a fraction of a selection, so the division always comes out exactly.

A decimal answer is a reliable sign that the numbers have gone into the formula in the wrong places.


Spec links: `spcpt_fVVc579xDmZm4X5t`


## Card 18 — question_and_answer (`fl_j4Gv6vy9zJWyynnV`)

**FRONT**

Why does `{}^{n}\text{C}_{r}` always equal `{}^{n}\text{C}_{n - r}`?


**BACK**

Because choosing which $r$ objects to **take** is the same act as choosing which $n - r$ objects to **leave behind**, so the two counts cannot differ.

The formula agrees, since exchanging $r$ for $n - r$ simply swaps the two factorials underneath and leaves their product unchanged.

It is worth using, because it turns an awkward calculation into an easier one.


Spec links: `spcpt_fVVc579xDmZm4X5t`


## Card 19 — question_and_answer (`fl_3vP474xqVVcCPSpn`)

**FRONT**

When a selection has to meet several conditions, when do you **multiply** the separate counts and when do you **add** them?


**BACK**

Multiply when all the conditions have to hold at once, which is an **and**, and add when the selection could be made in one of several alternative ways, which is an **or**.

So, **for example**, taking exactly 3 pure and 2 statistics questions is a product, while taking either 5 pure or 5 statistics is a sum.

Deciding which word the question means before writing anything down is what keeps the two apart.


Spec links: `spcpt_fVVc579xDmZm4X5t`


## Card 20 — question_and_answer (`fl_T3TRwZMKyMWvMPQR`)

**FRONT**

Oscar picks 4 books from 4 fantasy, 5 historical fiction and 2 classics, and must take **at least two** fantasy books. How is that counted?


**BACK**

List every split that meets the condition, count each split as a product, and add the results.

Here he takes 2, 3 or 4 fantasy books, and once the fantasy count is fixed the other categories no longer matter, so the rest can be drawn from the 7 **non-fantasy** books:

`{}^{4}\text{C}_{2} \times {}^{7}\text{C}_{2} + {}^{4}\text{C}_{3} \times {}^{7}\text{C}_{1} + {}^{4}\text{C}_{4} \times {}^{7}\text{C}_{0} = 155`

Collapsing the categories the condition says nothing about turns six cases into three.


Spec links: `spcpt_fVVc579xDmZm4X5t`


## Card 21 — question_and_answer (`fl_Z49mGTkgymtvF9jd`)

**FRONT**

How do you count the ways of choosing objects when some of the objects available are **identical**?


**BACK**

Split the count into cases according to how many of the identical objects are taken, work out each case on its own, and add the results.

So, **for example**, choosing 4 letters from CHOOSE means handling zero Os, one O and two Os as three separate cases.

The identical objects have to be dealt with separately because the formula assumes the objects you are choosing from are all distinguishable.


Spec links: `spcpt_fVVc579xDmZm4X5t`

