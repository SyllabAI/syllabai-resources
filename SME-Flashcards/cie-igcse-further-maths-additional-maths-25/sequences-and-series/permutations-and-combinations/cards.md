# Permutations & Combinations

Course: cie-igcse-further-maths-additional-maths-25 · Section: Sequences & Series

Source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/flashcards/sequences-and-series/permutations-and-combinations/


## Card 1 — question_and_answer (`fl_w7CxvJy5rP8DTqB6`)

**FRONT**

How many ways can $n$ different objects be arranged in a row?


**BACK**

There are $n \times ( n - 1 ) \times ( n - 2 ) \times \dots \times 2 \times 1$ ways.

The count drops by one each time because every object you place is no longer available for the next position.


Spec links: `spcpt_jYCdPVrS3gNFw5JW`


## Card 2 — question_and_answer (`fl_F7wZ2fkQffj87wj9`)

**FRONT**

How many distinct arrangements are there of the letters in MATHS?


**BACK**

There are $5 \times 4 \times 3 \times 2 \times 1 = 120$.

Five different letters can go first, then four remain for the second place, and so on down to one.


Spec links: `spcpt_jYCdPVrS3gNFw5JW`


## Card 3 — keyword_definition (`fl_ZkzzCTDbfHwpw8tJ`)

**FRONT**

Define $n$ **factorial**.


**BACK**

$n !$ means $n \times ( n - 1 ) \times ( n - 2 ) \times \dots \times 2 \times 1$, for any non-negative integer $n$.

It is an operation like $+$ or $\times$, and it is exactly the number of ways of arranging $n$ different objects.


Spec links: `spcpt_8R5wf3qRTj6JYQj3`


## Card 4 — true_or_false (`fl_VVNDTK3DfdYd4sz2`)

**FRONT**

**True or False?**

$0 ! = 1$


**BACK**

**True.**

There is exactly **one** way to arrange nothing at all, namely the empty arrangement, so the count is 1 rather than 0.

The factorial of a negative number, by contrast, is simply not defined.


Spec links: `spcpt_8R5wf3qRTj6JYQj3`


## Card 5 — fill_in_the_blanks (`fl_c4kQ3vK7hB2HXqv2`)

**FRONT**

Complete these factorial results:

`\frac{n!}{(n-1)!} = \_\_\_\_\_\_`

`\frac{n!}{(n-2)!} = \_\_\_\_\_\_`


**BACK**

The completed results are:

$\frac{n!}{(n-1)!} = n$

$\frac{n!}{(n-2)!} = n ( n - 1 )$

Everything from $( n - 1 )$ downwards cancels, leaving only the factors at the top end.


*Blanks: 0 — answers: []*

Spec links: `spcpt_8R5wf3qRTj6JYQj3`

Flags: fitb_no_blank_marker


## Card 6 — question_and_answer (`fl_FscYWDjd9BGmp6jj`)

**FRONT**

Simplify $\frac{7!}{4!}$ by cancelling.


**BACK**

Writing both out in full, everything from 4 downwards is common to the top and bottom:

$\frac{7\times6\times5\times4\times3\times2\times1}{4\times3\times2\times1} = 7 \times 6 \times 5$

Dividing a large factorial by a smaller one always collapses like this, so never work the two out separately.


Spec links: `spcpt_8R5wf3qRTj6JYQj3`


## Card 7 — fill_in_the_blanks (`fl_RgFDHCfggWY6Jbqm`)

**FRONT**

Complete the formula for the number of permutations of $r$ objects chosen from $n$:

`{}^{n}\text{P}_{r} = \_\_\_\_\_\_`


**BACK**

The completed formula is:

`{}^{n}\text{P}_{r} = \frac{n!}{(n-r)!}`

A permutation counts arrangements, so the **order** of the $r$ chosen objects matters.


*Blanks: 0 — answers: []*

Spec links: `spcpt_VkKccRJhrmwPw7tM`

Flags: fitb_no_blank_marker


## Card 8 — question_and_answer (`fl_ns5wVXX2bWCJz9Fs`)

**FRONT**

Why is arranging 3 out of 5 objects the same as $\frac{5!}{2!}$?


**BACK**

Counting directly gives $5 \times 4 \times 3$, since there are five choices, then four, then three.

Dividing $5 !$ by $2 !$ cancels the $2 \times 1$ at the bottom end, leaving exactly $5 \times 4 \times 3$.


Spec links: `spcpt_VkKccRJhrmwPw7tM`


## Card 9 — question_and_answer (`fl_Rb63jzc9f9Bnv5yB`)

**FRONT**

How do you count arrangements where two items must stay together?


**BACK**

Treat the two as **stuck together** into a single item, and arrange that block with everything else.

Then arrange the two items **within** the block separately, and multiply the two counts together.


Spec links: `spcpt_VkKccRJhrmwPw7tM`


## Card 10 — true_or_false (`fl_wv8gy73F5ccN5wQG`)

**FRONT**

**True or False?**

"All three items must be separated" means the same as "the three items cannot all be together".


**BACK**

**False.**

"Cannot all be together" still allows two of them to sit side by side, so you find it by subtracting the all-together arrangements from the total.

"Completely separated" is stricter: lay out the other items first and slot these into the gaps between them.


Spec links: `spcpt_VkKccRJhrmwPw7tM`


## Card 11 — keyword_definition (`fl_9RTsxJc3brRRfmHD`)

**FRONT**

Define a **combination**.


**BACK**

A **combination** is a selection of $r$ objects from $n$ in which the **order does not matter**.

That is the whole difference from a permutation, where a different order counts as a different arrangement.


Spec links: `spcpt_Mtg25yFQFXdCDYdC`


## Card 12 — question_and_answer (`fl_P4sH92J9GTr9q2VP`)

**FRONT**

Choosing 2 letters from A, B and C gives 6 permutations but only 3 combinations. Why?


**BACK**

Because AB and BA are two different **arrangements** but the same **selection**.

Each combination has been counted twice over, so dividing the 6 permutations by 2 gives 3 combinations.


Spec links: `spcpt_Mtg25yFQFXdCDYdC`


## Card 13 — fill_in_the_blanks (`fl_tJ6DDNbqy634xFXm`)

**FRONT**

Complete the formula for the number of combinations of $r$ objects from $n$:

`{}^{n}\text{C}_{r} = \_\_\_\_\_\_`


**BACK**

The completed formula is:

`{}^{n}\text{C}_{r} = \frac{n!}{(n-r)!\,r!}`

It is also written `\binom{n}{r}` and read as **n choose r**.


*Blanks: 0 — answers: []*

Spec links: `spcpt_Mtg25yFQFXdCDYdC`

Flags: fitb_no_blank_marker


## Card 14 — question_and_answer (`fl_JvYMgDrMp4yJqGZF`)

**FRONT**

Why does the combination formula divide by $r !$?


**BACK**

Because `{}^{n}\text{P}_{r}` counts every selection once for each way of ordering it, and there are $r !$ such orderings.

Dividing by $r !$ removes that duplication, which is why `{}^{n}\text{C}_{r} = \frac{{}^{n}\text{P}_{r}}{r!}`.


Spec links: `spcpt_Mtg25yFQFXdCDYdC`


## Card 15 — question_and_answer (`fl_CXXt5QMy54c3FSnZ`)

**FRONT**

What are `{}^{n}\text{C}_{n}` and `{}^{n}\text{C}_{0}`, and why?


**BACK**

Both equal **1**.

There is only one way to choose all $n$ objects, and only one way to choose none of them.

Working these out from the formula also shows why $0 !$ has to be 1.


Spec links: `spcpt_Mtg25yFQFXdCDYdC`


## Card 16 — true_or_false (`fl_5X9h5TD4sZrMJj8b`)

**FRONT**

**True or False?**

`{}^{n}\text{C}_{r} = {}^{n}\text{C}_{n-r}`


**BACK**

**True.**

Choosing which $r$ objects to **take** is the same decision as choosing which $n - r$ to **leave behind**.

This symmetry is a useful shortcut, since `{}^{20}\text{C}_{18}` is much quicker worked as `{}^{20}\text{C}_{2}`.


Spec links: `spcpt_Mtg25yFQFXdCDYdC`


## Card 17 — question_and_answer (`fl_FfrGWbdn86QKKByy`)

**FRONT**

Why is `{}^{n}\text{C}_{r}` also called a **binomial coefficient**?


**BACK**

Because the same numbers appear as the coefficients when a two-term bracket is raised to a power.

So the quantity that counts selections is exactly the quantity that multiplies each term of a binomial expansion.


Spec links: `spcpt_Mtg25yFQFXdCDYdC`


## Card 18 — question_and_answer (`fl_cB9G5HvnpTqKHpPN`)

**FRONT**

How do you tell whether a question is about permutations or combinations?


**BACK**

Ask whether the **order matters**: if rearranging the same objects gives a genuinely different outcome, it is a permutation.

Guessing first, second and third prize is a permutation, while naming the top three scorers in any order is a combination.


Spec links: `spcpt_5CR4bZZmb6VNWxVT`


## Card 19 — fill_in_the_blanks (`fl_jGHhbSB5W8nwQT3m`)

**FRONT**

Fill in the type each set of keywords points to:

**arrange**, **order**, **sequence** suggest `\_\_\_\_\_\_`.

**select**, **choose**, **group** suggest `\_\_\_\_\_\_`.


**BACK**

The completed sentences are:

**arrange**, **order**, **sequence** suggest **permutations**.

**select**, **choose**, **group** suggest **combinations**.

Keywords are a strong hint rather than a guarantee, so check the context as well.


*Blanks: 0 — answers: []*

Spec links: `spcpt_5CR4bZZmb6VNWxVT`

Flags: fitb_no_blank_marker


## Card 20 — question_and_answer (`fl_kYP9nyzh65YkJVmy`)

**FRONT**

When do you multiply your options, and when do you add them?


**BACK**

**Multiply** when you need one thing **and** another, since every choice of the first pairs with every choice of the second.

**Add** when you need one thing **or** another, since those are separate cases that do not combine.


Spec links: `spcpt_5CR4bZZmb6VNWxVT`


## Card 21 — question_and_answer (`fl_Zdrsh6qzvD4MfXX4`)

**FRONT**

A four-digit PIN is built from ten digits. How does the count change if digits may be repeated?


**BACK**

With repetition allowed every position still has all ten options, giving $10 \times 10 \times 10 \times 10$.

Without repetition the options fall away each time, giving $10 \times 9 \times 8 \times 7$, so check this before choosing any formula.


Spec links: `spcpt_5CR4bZZmb6VNWxVT`


## Card 22 — question_and_answer (`fl_XRBfhHJ2vrdKKxfb`)

**FRONT**

A password is 2 letters from A to E followed by 3 digits from 0 to 9, with no repeats. How many are there?


**BACK**

Order matters in a password, so each part is a permutation: `{}^{5}\text{P}_{2}` for the letters and `{}^{10}\text{P}_{3}` for the digits.

You need letters **and** digits, so multiply:

$( 5 \times 4 ) \times ( 10 \times 9 \times 8 ) = 14400$


Spec links: `spcpt_5CR4bZZmb6VNWxVT`


## Card 23 — question_and_answer (`fl_fh3KqQScj5ZBJKkz`)

**FRONT**

How do you handle a restriction such as "at least one yellow and no more than three reds"?


**BACK**

Break it into every case that satisfies the restriction, such as one yellow with three reds, then two yellows with two reds, and so on.

**Multiply** within each case, because both conditions must hold, then **add** the cases together, because any one of them will do.


Spec links: `spcpt_5CR4bZZmb6VNWxVT`


## Card 24 — true_or_false (`fl_GNTHHBPtXcc6tTvg`)

**FRONT**

**True or False?**

A question asking "how many ways" is always a combinations question.


**BACK**

**False.**

"How many ways" is used for both types, so it settles nothing on its own.

Look instead for whether order matters, or for the stronger keywords such as **arrange** against **choose**.


Spec links: `spcpt_5CR4bZZmb6VNWxVT`

