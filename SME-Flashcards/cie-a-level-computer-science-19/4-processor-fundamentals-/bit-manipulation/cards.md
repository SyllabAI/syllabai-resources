# Bit Manipulation

Course: cie-a-level-computer-science-19 · Section: 4. Processor Fundamentals

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/4-processor-fundamentals-/bit-manipulation/


## Card 1 — keyword_definition (`fl_3FNjz8JM2rBNkpQc`)

**FRONT**

Define **binary shift**.


**BACK**

A binary shift is an operation that **moves all the bits in a binary number left or right** by a certain number of positions.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 2 — question_and_answer (`fl_2bjrHZhZWK8ZvXdn`)

**FRONT**

What are binary shifts often used for?


**BACK**

**Fast multiplication or division by powers of 2**, or for **manipulating individual bits**.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 3 — question_and_answer (`fl_VGZVfBSNKcr25xsD`)

**FRONT**

Name the three main types of binary shift.


**BACK**

**Logical**, **arithmetic** and **cyclic**.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 4 — question_and_answer (`fl_kNmpv8w9fk9cC79d`)

**FRONT**

What does a logical shift fill the gap with, and what is it used for?


**BACK**

It fills the gap with **0s**, and is used for **unsigned binary numbers** or raw bit manipulation.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 5 — question_and_answer (`fl_8W2qg2xsn3XRkrMT`)

**FRONT**

What is 0000 1110 after a logical left shift of 2, in binary and denary?


**BACK**

**0011 1000**, which is **56** — the original 0000 1110 is 14, and each left shift doubles it.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 6 — question_and_answer (`fl_M9ZGJp2FJ6mhKHj7`)

**FRONT**

What is 1100 1000 after a logical right shift of 3, in binary and denary?


**BACK**

**0001 1001**, which is **25** — the original 1100 1000 is 200, and each right shift halves it.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 7 — question_and_answer (`fl_ZB4wbCTMf3xKHZDq`)

**FRONT**

What does an arithmetic right shift preserve, and why?


**BACK**

It **copies the sign bit (MSB) into the new leftmost bit**, so that **signed numbers in two's complement keep their sign**.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 8 — question_and_answer (`fl_9M7mHhnm59dkBwyp`)

**FRONT**

What is 1110 1000 after an arithmetic right shift of 3, in binary and denary?


**BACK**

**1111 1101**, which is **−3** — the original 1110 1000 is −24, and each arithmetic right shift divides by 2.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 9 — question_and_answer (`fl_zrR7R2cGrDW8tPdS`)

**FRONT**

How does an arithmetic left shift differ from a logical left shift?


**BACK**

It does **not differ** — an arithmetic left shift is the **same as a logical left shift**, shifting left with a 0 coming in.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 10 — question_and_answer (`fl_cw3Ss9fn2tPQCYHs`)

**FRONT**

What happens to the bits in a cyclic shift?


**BACK**

The bits are **rotated around** — **nothing is lost and no 0s are added** — because the bit that falls off one end is **reused at the other end**.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 11 — question_and_answer (`fl_2WRXCSRysPKM6Dg9`)

**FRONT**

What is 1011 0001 after a cyclic left shift of 3, in binary and denary?


**BACK**

**1000 1101**, which is **141** — the three leftmost bits 101 wrap around to the right side.


Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`


## Card 12 — fill_in_the_blanks (`fl_fkMQrMQHdQdj89zy`)

**FRONT**

Cyclic shifts do <u>**            **</u> preserve the sign bit, and are not equivalent to multiplying or dividing by powers of two.


**BACK**

Cyclic shifts do **not** preserve the sign bit, and are not equivalent to multiplying or dividing by powers of two.


*Blanks: 1 — answers: []*

Spec links: `spcpt_PwG2t8r8YrZZ4Hbd`

Flags: blank_answer_mismatch


## Card 13 — keyword_definition (`fl_X4QvPmvVxRtXyk3J`)

**FRONT**

Define **bit masking**.


**BACK**

Bit masking uses **binary patterns (masks)** to **test, set, clear or toggle specific bits without affecting the others**.


Spec links: `spcpt_524dyCyXXWhkGfNr`


## Card 14 — question_and_answer (`fl_dVsmH2GXKSG2ggNQ`)

**FRONT**

What is bitwise AND used for in device control?


**BACK**

To **test whether a specific bit is set to 1**, since it only returns 1 when **both the value and the mask have 1 in the same position** — useful for checking a device's status.


Spec links: `spcpt_524dyCyXXWhkGfNr`


## Card 15 — question_and_answer (`fl_n2zb4DW95gGGfmJn`)

**FRONT**

What is bitwise OR used for in device control?


**BACK**

To **set specific bits to 1**, since it returns 1 if **either the value or the mask has 1** — useful for **turning a device on** without changing the others.


Spec links: `spcpt_524dyCyXXWhkGfNr`


## Card 16 — question_and_answer (`fl_4JJmJr4FDrYWv4f3`)

**FRONT**

What is bitwise XOR used for in device control?


**BACK**

To **toggle or flip specific bits**, since it returns 1 if the bits are **different** — useful for switching a device from ON to OFF or back.


Spec links: `spcpt_524dyCyXXWhkGfNr`


## Card 17 — question_and_answer (`fl_HgSQ8dQV53wSCmfQ`)

**FRONT**

How can a single byte represent the state of several devices?


**BACK**

**Each bit** in the byte can represent the **state of a device or feature**, such as a light being on, a sensor being active, or an error being flagged.


Spec links: `spcpt_524dyCyXXWhkGfNr`


## Card 18 — true_or_false (`fl_WdK7gHTs2xRVXK5D`)

**FRONT**

**True or False?**

Applying a mask with bitwise AND changes the bits that the mask has 0s in.


**BACK**

**False.**

Masking tests, sets or toggles the targeted bits **without affecting the others** — an AND with a 0 in the mask simply returns 0 for that position, leaving the value untested there rather than altering the original.


Spec links: `spcpt_524dyCyXXWhkGfNr`

