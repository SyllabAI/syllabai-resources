# Arrays

Course: cie-a-level-computer-science-19 · Section: 10. Data Types & Structures

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/10-data-types-and-structures-/arrays/


## Card 1 — keyword_definition (`fl_8dr3268BH6gBR2HH`)

**FRONT**

Define **array**.


**BACK**

An array is an **ordered, static set of elements** that can store only **one data type**.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 2 — question_and_answer (`fl_h2dpDMFGXzvk4gmw`)

**FRONT**

How is the position of each element in an array identified?


**BACK**

By the array's **index**.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 3 — fill_in_the_blanks (`fl_KbQr9KbVxxkY7rC5`)

**FRONT**

An array is an ordered, <u>**            **</u> set of elements.


**BACK**

An array is an ordered, **static** set of elements.


*Blanks: 1 — answers: []*

Spec links: `spcpt_z595zm7HJjPQnskj`

Flags: blank_answer_mismatch


## Card 4 — true_or_false (`fl_3zrSt3YsQqH7xKQ4`)

**FRONT**

**True or False?**

An array can store more than one data type.


**BACK**

**False.**

An array can store only **one data type**.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 5 — keyword_definition (`fl_vY4yy8sBZD4VqXRJ`)

**FRONT**

Define **lower bound (LB)**.


**BACK**

The lower bound is the array's **first element**.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 6 — keyword_definition (`fl_X4Jc2wYxcYcr74T6`)

**FRONT**

Define **upper bound (UB)**.


**BACK**

The upper bound is the array's **last element**.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 7 — question_and_answer (`fl_KX4S6CY4whcx9S4z`)

**FRONT**

What is the lower bound of an array typically?


**BACK**

Typically **0 or 1**, depending on the language being used.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 8 — fill_in_the_blanks (`fl_7YKS6HhNWPHgkqXV`)

**FRONT**

A one-dimensional array is also called a <u>**            **</u> array.


**BACK**

A one-dimensional array is also called a **linear** array.


*Blanks: 1 — answers: []*

Spec links: `spcpt_z595zm7HJjPQnskj`

Flags: blank_answer_mismatch


## Card 9 — question_and_answer (`fl_fM7JPkzpWpPkBCWw`)

**FRONT**

What must be included when declaring a 1D array in pseudocode?


**BACK**

The **lower bound**, the **upper bound** and the **data type**.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 10 — question_and_answer (`fl_9vwVGb7fj8hPFcPX`)

**FRONT**

What is the pseudocode syntax for declaring a 1D array?


**BACK**

`DECLARE <identifier> : ARRAY[LB:UB] OF <data type>`


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 11 — question_and_answer (`fl_9TpRkVTwcPD4pk9c`)

**FRONT**

Write pseudocode to declare a 1D array of five single characters called `Letters`.


**BACK**

`DECLARE Letters : ARRAY[0:4] OF CHAR`


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 12 — true_or_false (`fl_m68y9rR6jvptpgrT`)

**FRONT**

**True or False?**

`ARRAY[0:4]` holds four elements.


**BACK**

**False.**

It holds **five** elements, because the lower bound and upper bound are **both included**: indices 0, 1, 2, 3 and 4.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 13 — question_and_answer (`fl_pvGXQ3RWDsRGM7GY`)

**FRONT**

Write pseudocode to assign the character 'B' to the first element of `Letters`.


**BACK**

`Letters[0] ← 'B'`


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 14 — question_and_answer (`fl_QNS533xCm74f3RCP`)

**FRONT**

How can a 2D array be visualised?


**BACK**

As a **table**.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 15 — question_and_answer (`fl_8hddBHMPGRg4Q3mx`)

**FRONT**

How do you navigate through a 2D array?


**BACK**

First go **down the rows**, then **across the columns**, to find a position within the array.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 16 — question_and_answer (`fl_QfF26NZHMMv5WSCt`)

**FRONT**

Which four bounds must be declared for a 2D array?


**BACK**

The **lower and upper bounds for rows (LBR and UBR)**, and the **lower and upper bounds for columns (LBC and UBC)**.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 17 — question_and_answer (`fl_rgxfk7vS5pt92mZk`)

**FRONT**

What is the pseudocode syntax for declaring a 2D array?


**BACK**

`DECLARE <identifier> : ARRAY[LBR:UBR, LBC:UBC] OF <data type>`


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 18 — question_and_answer (`fl_4C32xPBRc2gHCrwC`)

**FRONT**

How many rows and columns does `ARRAY[0:2, 0:4]` create?


**BACK**

**3 rows** and **5 columns**.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 19 — question_and_answer (`fl_n9r9W96nJJQDJcyF`)

**FRONT**

In a 2D array reference, which index comes first?


**BACK**

The **row** comes first, then the **column**, written as `Identifier[row, column]`.


Spec links: `spcpt_z595zm7HJjPQnskj`


## Card 20 — keyword_definition (`fl_9WrqySKWKTmJwCpR`)

**FRONT**

Define **linear search**.


**BACK**

A linear search **starts with the first value** in a dataset and **checks every value one at a time** until all values have been checked.


Spec links: `spcpt_DTB8jjHzTdHVpnC2`


## Card 21 — true_or_false (`fl_XSdtcQPwDCn5KzRW`)

**FRONT**

**True or False?**

A linear search requires the data to be in order.


**BACK**

**False.**

A linear search can be performed **even if the values are not in order**.


Spec links: `spcpt_DTB8jjHzTdHVpnC2`


## Card 22 — question_and_answer (`fl_7JFqb6DKqkkS9VMD`)

**FRONT**

In which order are elements checked in a linear search on an array?


**BACK**

In order from the **lower bound** to the **upper bound**, until the item is found or the upper bound is reached.


Spec links: `spcpt_DTB8jjHzTdHVpnC2`


## Card 23 — question_and_answer (`fl_pZ8rjvWCMycVkj6M`)

**FRONT**

What are the four steps of a linear search?


**BACK**

Check the first value. **IF** it is the value you are looking for, **STOP**. **ELSE** move to the next value and check. **REPEAT UNTIL** all values have been checked.


Spec links: `spcpt_DTB8jjHzTdHVpnC2`


## Card 24 — question_and_answer (`fl_wwHpjKK59vtYbXvZ`)

**FRONT**

In the linear search example, what does the identifier `Found` store?


**BACK**

A **BOOLEAN** that tracks whether the target value has been found.


Spec links: `spcpt_DTB8jjHzTdHVpnC2`


## Card 25 — question_and_answer (`fl_BFCnKmDY3zW4z78c`)

**FRONT**

In the linear search example, what does the identifier `Index` store?


**BACK**

The **current position being checked** in the array.


Spec links: `spcpt_DTB8jjHzTdHVpnC2`


## Card 26 — fill_in_the_blanks (`fl_sTHg4jyNHSJhyqcS`)

**FRONT**

In the linear search, `Found` is initialised to <u>**          **</u> before the loop begins.


**BACK**

In the linear search, `Found` is initialised to **FALSE** before the loop begins.


*Blanks: 1 — answers: []*

Spec links: `spcpt_DTB8jjHzTdHVpnC2`

Flags: blank_answer_mismatch


## Card 27 — question_and_answer (`fl_9SFnmSNxy8B9YMfb`)

**FRONT**

Write the pseudocode condition that controls the linear search loop.


**BACK**

`WHILE Index <= 4 AND Found = FALSE DO`


Spec links: `spcpt_DTB8jjHzTdHVpnC2`


## Card 28 — question_and_answer (`fl_Bzs2MFMB6JydxtXX`)

**FRONT**

Why does the linear search use a `WHILE` loop rather than a `FOR` loop?


**BACK**

For **flexibility**, because a `WHILE` loop allows an **early exit** as soon as the item is found.


Spec links: `spcpt_DTB8jjHzTdHVpnC2`


## Card 29 — question_and_answer (`fl_69PND35DQjFxfbcX`)

**FRONT**

In the linear search, what happens to `Index` when the current element does not match the target?


**BACK**

`Index ← Index + 1`, which moves the search on to the next position.


Spec links: `spcpt_DTB8jjHzTdHVpnC2`


## Card 30 — keyword_definition (`fl_X92XwGWzknnnsNfh`)

**FRONT**

Define **bubble sort**.


**BACK**

A bubble sort **checks values in pairs**, starting at the beginning of a dataset, and **swaps them if they are not in the correct order**.


Spec links: `spcpt_SZCsB8JMfyN8zsRR`


## Card 31 — keyword_definition (`fl_h4hFcNp2jVVh6nTt`)

**FRONT**

Define **pass** in a bubble sort.


**BACK**

A pass is **one full run of comparisons from the beginning to the end** of the dataset.


Spec links: `spcpt_SZCsB8JMfyN8zsRR`


## Card 32 — question_and_answer (`fl_j6nryFVPFbs2qjtq`)

**FRONT**

When is a bubble sort finished?


**BACK**

When there are **no more swaps to make**.


Spec links: `spcpt_SZCsB8JMfyN8zsRR`


## Card 33 — question_and_answer (`fl_TkjCS4QwXv4PtMbd`)

**FRONT**

What are the steps of a bubble sort?


**BACK**

Compare the first two values. **IF** they are in the wrong order, **swap them**. Compare the next two values and repeat to the end of the dataset. **IF** any swaps were made, repeat from the start. **ELSE** stop, because the list is in the correct order.


Spec links: `spcpt_SZCsB8JMfyN8zsRR`


## Card 34 — question_and_answer (`fl_sG4Zdt9NJxGmPm6D`)

**FRONT**

A bubble sort starts with the dataset 5 2 4 1 6 3.

What is the dataset after pass 1?


**BACK**

**2 4 1 5 3 6**


Spec links: `spcpt_SZCsB8JMfyN8zsRR`


## Card 35 — question_and_answer (`fl_mVqX5TRHbNvQqv3m`)

**FRONT**

A bubble sort starts with the dataset 5 2 4 1 6 3.

How many passes are needed?


**BACK**

**Four** passes. Passes 1, 2 and 3 make swaps, and pass 4 makes no swaps, which confirms the list is sorted.


Spec links: `spcpt_SZCsB8JMfyN8zsRR`


## Card 36 — question_and_answer (`fl_wXN2T2khbZR8SyjS`)

**FRONT**

In the bubble sort pseudocode, what is the purpose of the `Swapped` variable?


**BACK**

It **indicates whether a swap occurred during a pass**, and is used to **optimise** the sort by leaving the loop early.


Spec links: `spcpt_SZCsB8JMfyN8zsRR`


## Card 37 — fill_in_the_blanks (`fl_rbvfGW8H95cnkqx6`)

**FRONT**

If no swaps were made on a pass, the bubble sort uses <u>**        **</u> to leave the loop early.


**BACK**

If no swaps were made on a pass, the bubble sort uses **EXIT** to leave the loop early.


*Blanks: 1 — answers: []*

Spec links: `spcpt_SZCsB8JMfyN8zsRR`

Flags: blank_answer_mismatch


## Card 38 — question_and_answer (`fl_pqSBJyrPH6j2fmJV`)

**FRONT**

In the bubble sort pseudocode, what is the purpose of the `Temp` variable?


**BACK**

It is a **temporary variable used for swapping two elements** in the array.


Spec links: `spcpt_SZCsB8JMfyN8zsRR`


## Card 39 — question_and_answer (`fl_KdBYnwc2TpbcmFPv`)

**FRONT**

Write the three pseudocode lines that swap two adjacent array elements.


**BACK**

`Temp ← Numbers[Index]`, then `Numbers[Index] ← Numbers[Index + 1]`, then `Numbers[Index + 1] ← Temp`


Spec links: `spcpt_SZCsB8JMfyN8zsRR`


## Card 40 — question_and_answer (`fl_ZbWjc8bb2MR2xrvh`)

**FRONT**

Write the comparison condition used in the bubble sort loop.


**BACK**

`IF Numbers[Index] > Numbers[Index + 1] THEN`


Spec links: `spcpt_SZCsB8JMfyN8zsRR`


## Card 41 — true_or_false (`fl_2M8Td5tWjCJgcJzT`)

**FRONT**

**True or False?**

In the bubble sort example the inner loop runs from 0 to 5.


**BACK**

**False.**

The inner loop runs `FOR Index ← 0 TO 4`. It compares `Numbers[Index]` with `Numbers[Index + 1]`, so going as far as 5 would read past the upper bound of the array.


Spec links: `spcpt_SZCsB8JMfyN8zsRR`

