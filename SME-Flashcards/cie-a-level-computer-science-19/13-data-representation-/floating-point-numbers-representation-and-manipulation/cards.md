# Floating-point Numbers, Representation & Manipulation

Course: cie-a-level-computer-science-19 · Section: 13. Data Representation

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/13-data-representation-/floating-point-numbers-representation-and-manipulation/


## Card 1 — keyword_definition (`fl_K3Wg7bSpMtHYpVvw`)

**FRONT**

Define **floating-point binary**.


**BACK**

Floating-point binary represents **real numbers in binary**: numbers with a fractional part, and numbers that are very large or very small.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 2 — question_and_answer (`fl_SkF2s9qhBTv58kqQ`)

**FRONT**

What is floating-point binary equivalent to in denary?


**BACK**

It works like **scientific notation, but in base 2**.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 3 — question_and_answer (`fl_cBPFwG4DYMVqfgVF`)

**FRONT**

How is a floating-point number written?


**BACK**

As a **mantissa multiplied by 2 to the power of an exponent**.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 4 — question_and_answer (`fl_BNhrYPNVwNGTb3qy`)

**FRONT**

In `3140 = 3.14 x 10^3`, which part is the mantissa and which is the exponent?


**BACK**

**3.14** is the mantissa, the significant digits. **3** is the exponent, how far to move the decimal point.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 5 — question_and_answer (`fl_f8RJx25SVWGPM7wV`)

**FRONT**

Give two reasons to use floating-point representation.


**BACK**

It represents a **much wider range** of numbers than fixed-point using the same number of bits, and the binary point can **float**, giving good **precision** for fractional values.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 6 — keyword_definition (`fl_6RtxpHjFJMSMGcYQ`)

**FRONT**

Define **mantissa**.


**BACK**

The mantissa holds the **significant bits** of the number. It is a **two's complement** number with the binary point **immediately after the leftmost bit**.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 7 — fill_in_the_blanks (`fl_JvyG5CNnVk96Wnfd`)

**FRONT**

In the mantissa, the binary point sits immediately after the <u>**                **</u> bit.


**BACK**

In the mantissa, the binary point sits immediately after the **leftmost** bit.


*Blanks: 1 — answers: []*

Spec links: `spcpt_dMzQRprWM4d9tk5Z`

Flags: blank_answer_mismatch


## Card 8 — keyword_definition (`fl_6vBvQP3yq2fRmwjj`)

**FRONT**

Define **exponent**.


**BACK**

The exponent is **how many places to move the binary point**, positive to move right and negative to move left. It is also stored in **two's complement**.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 9 — question_and_answer (`fl_NW5zBRy2RHZbJnB5`)

**FRONT**

Which parts of a floating-point number are stored in two's complement?


**BACK**

**Both** the mantissa and the exponent.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 10 — question_and_answer (`fl_MhWr5rcfWs8VxhnY`)

**FRONT**

What does the leftmost bit of the mantissa act as?


**BACK**

The **sign**: `0` means positive and `1` means negative.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 11 — question_and_answer (`fl_sQMW4X8ftjqcYbdK`)

**FRONT**

Convert +6.25 to a 12-bit mantissa and a 4-bit exponent.


**BACK**

`6.25 = 110.01`, normalised to `0.11001 x 2^3`. Mantissa `**011001000000**`, exponent `**0011**`.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 12 — question_and_answer (`fl_8y5BQvBCtXG4VV7C`)

**FRONT**

How do you find the mantissa of a negative floating-point number?


**BACK**

Work out the **positive mantissa first**, then take its **two's complement** by flipping the bits and adding 1.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 13 — true_or_false (`fl_6GSxzZQxRkxvK5nZ`)

**FRONT**

**True or False?**

To make a floating-point number negative you just change the sign bit.


**BACK**

**False.**

You must take the **two's complement of the whole positive mantissa**. Changing only the sign bit loses every mark on the conversion.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 14 — question_and_answer (`fl_RrzSBHWnrBDWzV9M`)

**FRONT**

The 12-bit mantissa for +6.25 is `011001000000`.

What is the mantissa for -6.25?


**BACK**

Flip the bits to `100110111111`, then add 1, giving `**100111000000**`.


Spec links: `spcpt_dMzQRprWM4d9tk5Z`


## Card 15 — keyword_definition (`fl_mjNPdPmXDNM7d76Y`)

**FRONT**

Define **normalisation** of a floating-point number.


**BACK**

A floating-point number is normalised when the **first two bits of the mantissa are different**.


Spec links: `spcpt_VCDty8T35dnZj3yF`


## Card 16 — question_and_answer (`fl_237hjGPTKNKQD7vp`)

**FRONT**

What do the first two bits of a normalised number look like?


**BACK**

`01` for a **positive** number, and `10` for a **negative** number.


Spec links: `spcpt_VCDty8T35dnZj3yF`


## Card 17 — true_or_false (`fl_vXYKJMMJfJgH4qGy`)

**FRONT**

**True or False?**

A normalised negative number starts `11`.


**BACK**

**False.**

A normalised negative number starts `**10**`. If it starts `11` it is not normalised, or sign-and-magnitude has been used by mistake.


Spec links: `spcpt_VCDty8T35dnZj3yF`


## Card 18 — question_and_answer (`fl_S2kxKwMB88nWshWM`)

**FRONT**

Why does normalising improve precision?


**BACK**

Removing **leading zeros** means the mantissa uses **all of its bits for significant figures**, giving the most accurate value possible for that number of bits.


Spec links: `spcpt_VCDty8T35dnZj3yF`


## Card 19 — question_and_answer (`fl_rJWGR3p6nyqTJJgJ`)

**FRONT**

Why does normalising give uniqueness?


**BACK**

Each number has **exactly one normalised form**, which makes comparison and arithmetic simpler.


Spec links: `spcpt_VCDty8T35dnZj3yF`


## Card 20 — question_and_answer (`fl_DZJRcmB9nd978PqH`)

**FRONT**

How do you adjust the exponent when normalising?


**BACK**

If the point moves **left**, **increase** the exponent. If the point moves **right**, **decrease** the exponent.


Spec links: `spcpt_VCDty8T35dnZj3yF`


## Card 21 — fill_in_the_blanks (`fl_qd9dxNG4P4WcMR9b`)

**FRONT**

When normalising, if the binary point moves left you <u>**                **</u> the exponent.


**BACK**

When normalising, if the binary point moves left you **increase** the exponent.


*Blanks: 1 — answers: []*

Spec links: `spcpt_VCDty8T35dnZj3yF`

Flags: blank_answer_mismatch


## Card 22 — question_and_answer (`fl_cCv4ttHsXFMznBzW`)

**FRONT**

Normalise the mantissa `0.0011` with exponent `+2`.


**BACK**

Move the point **2 places right** so the mantissa becomes `0.1100`, and **decrease the exponent by 2** to `0`. The value is unchanged.


Spec links: `spcpt_VCDty8T35dnZj3yF`


## Card 23 — question_and_answer (`fl_rkbc3SDGZXBv7Wh9`)

**FRONT**

How should the normalised form be written for CIE?


**BACK**

As `0.xxxxx x 2^n`, **not** `1.xxxxx x 2^n`, which is the IEEE form.


Spec links: `spcpt_VCDty8T35dnZj3yF`


## Card 24 — question_and_answer (`fl_Bmt87tsF5sP87yfJ`)

**FRONT**

What is the first step in converting denary to floating-point binary?


**BACK**

**Convert the magnitude to binary**, both the integer part and the fractional part.


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 25 — question_and_answer (`fl_8GHyKqCkqH64cvQ3`)

**FRONT**

Convert 5.25 to binary.


**BACK**

`5 = 101` and `0.25 = 0.01`, so `5.25 = 101.01`.


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 26 — question_and_answer (`fl_R9jnf9rnYhd5H9WW`)

**FRONT**

What is the second step in converting denary to floating-point binary?


**BACK**

**Normalise** into the form `0.xxxxx x 2^n`, moving the binary point until the first two bits differ.


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 27 — question_and_answer (`fl_VVYrPBgbGHmsvsZ9`)

**FRONT**

What does the number of places the binary point moves give you?


**BACK**

The **exponent**.


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 28 — question_and_answer (`fl_mJ65VXwszHhCXGhf`)

**FRONT**

Normalise `101.01`.


**BACK**

`0.10101 x 2^3`


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 29 — question_and_answer (`fl_6n5xGYRRrykpVZHR`)

**FRONT**

How do you build the positive mantissa?


**BACK**

Write `0`, then the **fraction bits**, then **pad with zeros on the right**.


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 30 — question_and_answer (`fl_NJkXCWD4fC83JnnD`)

**FRONT**

Give the 12-bit mantissa and 4-bit exponent for +5.25.


**BACK**

Mantissa `**010101000000**`, exponent `**0011**`.


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 31 — fill_in_the_blanks (`fl_yGPYkcmkG8SyCzVf`)

**FRONT**

The exponent is converted to <u>**          **</u> complement in the required number of bits.


**BACK**

The exponent is converted to **two's** complement in the required number of bits.


*Blanks: 1 — answers: []*

Spec links: `spcpt_NPkTzcxyQqKqymwn`

Flags: blank_answer_mismatch


## Card 32 — question_and_answer (`fl_74DV82ZvKj7PKs2K`)

**FRONT**

What extra step is needed if the number is negative?


**BACK**

Take the **two's complement of the whole positive mantissa**, by flipping the bits and adding 1.


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 33 — question_and_answer (`fl_fqHR2XNn48973NNT`)

**FRONT**

The 12-bit mantissa for +5.25 is `010101000000`.

Give the mantissa for -5.25.


**BACK**

Flip the bits to `101010111111`, then add 1, giving `**101011000000**`.


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 34 — question_and_answer (`fl_cTS9TPDxbVt6cRG7`)

**FRONT**

Does the exponent change when the number becomes negative?


**BACK**

**No.** The exponent is **unchanged**.


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 35 — question_and_answer (`fl_72tkQYfCSfYjkJZk`)

**FRONT**

How can you check that a negative mantissa is normalised?


**BACK**

It should **begin **`**10**`.


Spec links: `spcpt_NPkTzcxyQqKqymwn`


## Card 36 — question_and_answer (`fl_gDVMkFzjNrxZBYMd`)

**FRONT**

What is the first step in converting floating-point binary to denary?


**BACK**

**Read the exponent** and convert it from two's complement to denary.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 37 — question_and_answer (`fl_RfwkmMfRwwqvyhQz`)

**FRONT**

How do you tell the sign of a floating-point number?


**BACK**

Check the **first bit of the mantissa**: `0` means positive, `1` means negative.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 38 — question_and_answer (`fl_fqKn2pSg4rzk4t4T`)

**FRONT**

What do you do if the mantissa is negative?


**BACK**

Take its **two's complement** to find the **magnitude** of the fraction, then make the final answer negative.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 39 — fill_in_the_blanks (`fl_9jvFDTCzScJkS3gR`)

**FRONT**

To convert a negative mantissa to its magnitude, flip the bits and add <u>**        **</u>.


**BACK**

To convert a negative mantissa to its magnitude, flip the bits and add **1**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_VCY2SgXbSzFg7VCw`

Flags: blank_answer_mismatch


## Card 40 — question_and_answer (`fl_9wVNf6N93yxCT8Gk`)

**FRONT**

How do you apply the exponent?


**BACK**

**Move the binary point**: right if the exponent is positive, left if it is negative.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 41 — true_or_false (`fl_G7TNGchrDRxyHYsb`)

**FRONT**

**True or False?**

Only the mantissa is stored in two's complement.


**BACK**

**False.**

**Both** the mantissa and the exponent are stored in two's complement.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 42 — question_and_answer (`fl_ZhJ6VP2hNGHBw8NP`)

**FRONT**

Convert mantissa `010101000000`, exponent `0011` to denary.


**BACK**

Exponent is `+3`. First bit is `0`, so positive. Fraction is `0.10101`, and `0.10101 x 2^3 = 101.01`, which is **+5.25**.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 43 — question_and_answer (`fl_5kcjNp7pqBGFBPVy`)

**FRONT**

Convert mantissa `101011000000`, exponent `0011` to denary.


**BACK**

First bit is `1`, so negative. Two's complement gives `010101000000`, a fraction of `0.10101`. `0.10101 x 2^3 = 5.25`, so the answer is **-5.25**.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 44 — question_and_answer (`fl_zR6z22Nx6PYhHvPm`)

**FRONT**

Using the place-value check, what does the mantissa `1.01011` equal?


**BACK**

The leftmost bit carries a negative place value, so `-1 + 0.34375 = ``**-0.65625**`. With an exponent of 3 that gives `x 2^3 = -5.25`.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 45 — question_and_answer (`fl_q6ZWkq6yv4G2CBjr`)

**FRONT**

Convert 113.75 to binary.


**BACK**

`1110001.11`


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 46 — question_and_answer (`fl_xsg7dZYhczsxfBD4`)

**FRONT**

Normalise 113.75 and give the exponent.


**BACK**

`0.111000111 x 2^7`, so the binary point moves 7 places and the exponent is **7**.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 47 — question_and_answer (`fl_Tspfj8bRKhR6GxvH`)

**FRONT**

Give 113.75 with a 10-bit mantissa and a 6-bit exponent.


**BACK**

Mantissa `**0111000111**`, exponent `**000111**`.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 48 — question_and_answer (`fl_v59gjdMwrqxsFnJ3`)

**FRONT**

Give 113.75 with an 8-bit mantissa and an 8-bit exponent.


**BACK**

Mantissa `**01110001**`, exponent `**00000111**`. The mantissa is **truncated** to 8 bits, losing precision.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 49 — true_or_false (`fl_XsXD7TWbxK24t5Vd`)

**FRONT**

**True or False?**

A shorter mantissa stores the same value just as accurately.


**BACK**

**False.**

With fewer bits the mantissa is **truncated**, which **loses precision**.


Spec links: `spcpt_VCY2SgXbSzFg7VCw`


## Card 50 — question_and_answer (`fl_4fc3jVz6Nr2Xtm9x`)

**FRONT**

Why can real numbers not always be represented exactly in floating-point?


**BACK**

Floating-point binary has a **limited number of bits** for the mantissa and exponent, so many numbers can only be **approximated**.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 51 — true_or_false (`fl_3v3kNtdczGX4WhfZ`)

**FRONT**

**True or False?**

All real numbers can be stored exactly in floating-point binary.


**BACK**

**False.**

Not all real numbers can be represented **exactly**, only **approximated**.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 52 — question_and_answer (`fl_KvKGHjPSgPcJD6fF`)

**FRONT**

Give an example of a decimal that cannot be represented precisely in binary.


**BACK**

**0.1**, which in binary is `0.000110011001100...` recurring.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 53 — question_and_answer (`fl_g6M6nqH2ZQ8SWsJY`)

**FRONT**

What happens to a recurring binary value when memory is limited?


**BACK**

It must be **truncated or rounded**, which introduces **small errors**.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 54 — keyword_definition (`fl_rFSZjHtwPtFbRVwJ`)

**FRONT**

Define **rounding error**.


**BACK**

A rounding error is a **slight inaccuracy** caused when a real number **cannot be exactly represented in binary**.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 55 — question_and_answer (`fl_2jHfD5QRgdNzNnzx`)

**FRONT**

What is the consequence of rounding errors in a long calculation?


**BACK**

Calculations using approximated values may **accumulate errors**, so final results may be **slightly inaccurate**.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 56 — keyword_definition (`fl_T8nzPxWgnnDDxfst`)

**FRONT**

Define **underflow**.


**BACK**

Underflow occurs when a number is **too close to zero** to be stored in the available number of bits.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 57 — fill_in_the_blanks (`fl_wWqpwWMqMbnsZXwv`)

**FRONT**

Underflow occurs when a number is too close to <u>**        **</u> to be stored.


**BACK**

Underflow occurs when a number is too close to **zero** to be stored.


*Blanks: 1 — answers: []*

Spec links: `spcpt_CBTy9sh2hqRFjqVq`

Flags: blank_answer_mismatch


## Card 58 — question_and_answer (`fl_sMTrfQ8frPt3MKxf`)

**FRONT**

What causes underflow, in terms of the exponent?


**BACK**

The **exponent is too negative** to be stored.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 59 — question_and_answer (`fl_ydNQpvmCyP8Z6V9R`)

**FRONT**

What is a number stored as if underflow occurs?


**BACK**

It is **stored as 0**, which is a loss of precision.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 60 — fill_in_the_blanks (`fl_p8cDf3vjVvDwfKq4`)

**FRONT**

A very small number such as 1.2 x 10^-40 causes <u>**                    **</u>, because its exponent is too negative to store.


**BACK**

A very small number such as 1.2 x 10^-40 causes **underflow**, because its exponent is too negative to store.


*Blanks: 1 — answers: []*

Spec links: `spcpt_CBTy9sh2hqRFjqVq`

Flags: blank_answer_mismatch


## Card 61 — keyword_definition (`fl_NCnNYkY8yTCFyRMJ`)

**FRONT**

Define **overflow**.


**BACK**

Overflow occurs when a number is **too large** to fit in the allocated bits for the exponent or mantissa.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 62 — question_and_answer (`fl_ndp248FKtpPrqjRp`)

**FRONT**

What causes overflow, in terms of the exponent?


**BACK**

The **exponent is too positive** to be stored.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 63 — question_and_answer (`fl_bZ29GjtPK84zSDyQ`)

**FRONT**

A calculation produces 1.2 x 10<sup>50, but the maximum representable number is 1.2 x 10</sup>38.

What has occurred?


**BACK**

**Overflow**.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 64 — question_and_answer (`fl_JbQrJ4f9CgNQRBv6`)

**FRONT**

What are the consequences of overflow?


**BACK**

The program may **crash** or return an **infinity**, an **error**, or a **wraparound value**.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 65 — true_or_false (`fl_KYfbfPffPzRZvMcn`)

**FRONT**

**True or False?**

Underflow causes a program to crash.


**BACK**

**False.**

Underflow stores the value as **0**, causing a **loss of precision**. It is **overflow** that may crash the program or return an error.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 66 — question_and_answer (`fl_KM8SH4cvJBpjQpmD`)

**FRONT**

What is the difference between underflow and overflow?


**BACK**

**Underflow** is a number **too small to store**, which becomes **0**. **Overflow** is a number **too large to store**, giving an incorrect result or a program error.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`


## Card 67 — question_and_answer (`fl_csN84GkBtt38vJJW`)

**FRONT**

Where are underflow and overflow especially dangerous?


**BACK**

Underflow can affect accuracy in **scientific or financial calculations**. Overflow is especially dangerous in **loops or financial applications**.


Spec links: `spcpt_CBTy9sh2hqRFjqVq`

