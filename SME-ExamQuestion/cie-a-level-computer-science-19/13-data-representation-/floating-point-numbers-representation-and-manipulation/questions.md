# Exam Questions — Floating-point Numbers, Representation & Manipulation
**13. Data Representation** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 21 questions across 1 sets


## Exam Questions (21 questions)


### Q1 — hard — 4 marks

**Q1** [4 marks]

A computer system stores real numbers using binary floating-point representation with:

- 12 bits for the mantissa
- 4 bits for the exponent
- two's complement form for both the mantissa and the exponent.

**Mantissa**

| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|

**Exponent**

| 0 | 1 | 1 | 0 |
|---|---|---|---|

A student calculates the denary value of this number as -13. The student's answer is not correct.

Calculate the correct denary value of the number and identify the mistake the student has made.

Show your working.

### Q2 — medium — 3 marks

**Q2** [3 marks]

A computer system stores real numbers using binary floating-point representation with:

- 10 bits for the mantissa
- 6 bits for the exponent
- two's complement form for both the mantissa and the exponent.

Calculate the denary value of the given normalised binary floating-point number.

Show your working.

**Mantissa**

| 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|

**Exponent**

| 1 | 1 | 1 | 1 | 1 | 1 |
|---|---|---|---|---|---|

### Q3 — easy — 2 marks

**Q3** [2 marks]

A computer system stores real numbers using binary floating-point representation with:

- 8 bits for the mantissa
- 8 bits for the exponent
- two's complement form for both the mantissa and the exponent.

Calculate the denary value of the given normalised binary floating-point number.

Show your working.

**Mantissa**

| 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|

**Exponent**

| 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
|---|---|---|---|---|---|---|---|

### Q4 — hard — 4 marks

**Q4** [4 marks]

Two computer systems store real numbers using binary floating-point representation.

System 1 uses:

- 10 bits for the mantissa
- 6 bits for the exponent
- two's complement form for both the mantissa and the exponent.

System 2 uses:

- 12 bits for the mantissa
- 4 bits for the exponent
- two's complement form for both the mantissa and the exponent.

Calculate the normalised binary floating-point representation of +45.5 in each of these two systems.

Show your working.

**System 1 mantissa**

|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|

**System 1 exponent**

|   |   |   |   |   |   |
|---|---|---|---|---|---|

**System 2 mantissa**

|   |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|

**System 2 exponent**

|   |   |   |   |
|---|---|---|---|

### Q5 — medium — 3 marks

**Q5** [3 marks]

A computer system stores real numbers using binary floating-point representation with:

- 10 bits for the mantissa
- 6 bits for the exponent
- two's complement form for both the mantissa and the exponent.

Calculate the normalised binary floating-point representation of -0.34375 in this system.

Show your working.

**Mantissa**

|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|

**Exponent**

|   |   |   |   |   |   |
|---|---|---|---|---|---|

### Q6 — easy — 2 marks

**Q6** [2 marks]

A computer system stores real numbers using binary floating-point representation with:

- 8 bits for the mantissa
- 8 bits for the exponent
- two's complement form for both the mantissa and the exponent.

Write the normalised binary floating-point representation of +5.5 in this system.

**Mantissa**

|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|

**Exponent**

|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|

### Q7 — hard — 4 marks

**Q7** [4 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 10 bits for the mantissa
- 6 bits for the exponent
- two's complement form for both the mantissa and the exponent.

A negative number is stored in this system as shown.

**Mantissa**

| 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|

**Exponent**

| 0 | 0 | 0 | 1 | 0 | 1 |
|---|---|---|---|---|---|

Explain why this number is not normalised, write its normalised representation, and explain what a computer system gains by storing floating-point numbers in normalised form.

### Q8 — medium — 3 marks

**Q8** [3 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 10 bits for the mantissa
- 6 bits for the exponent
- two's complement form for both the mantissa and the exponent.

A number is stored in this system as shown. The number is not normalised.

**Mantissa**

| 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|

**Exponent**

| 0 | 0 | 0 | 1 | 1 | 1 |
|---|---|---|---|---|---|

Write the normalised floating-point representation of this number.

Show your working.

### Q9 — easy — 2 marks

**Q9** [2 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 10 bits for the mantissa
- 6 bits for the exponent
- two's complement form for both the mantissa and the exponent.

A number is stored in this system with the following mantissa.

**Mantissa**

| 1 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 1 |
|---|---|---|---|---|---|---|---|---|---|

State why this number is not normalised, and state the first two bits that the mantissa of any normalised negative number must have.

### Q10 — hard — 4 marks

**Q10** [4 marks]

Two computer systems each store real numbers in a total of 16 bits, using floating-point representation with two's complement form for both the mantissa and the exponent. The systems allocate the 16 bits differently.

| System | Bits for the mantissa | Bits for the exponent |
|---|---|---|
| X | 8 | 8 |
| Y | 12 | 4 |

Explain the effect that this difference has on the numbers each system can store. Give the exponent range of each system in your answer.

### Q11 — medium — 3 marks

**Q11** [3 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 12 bits for the mantissa
- 4 bits for the exponent
- two's complement form for both the mantissa and the exponent.

Calculate the largest positive denary value and the most negative denary value that can be stored in this system.

Show your working.

### Q12 — easy — 2 marks

**Q12** [2 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 10 bits for the mantissa
- 6 bits for the exponent
- two's complement form for both the mantissa and the exponent.

State the largest exponent and the smallest exponent, in denary, that can be stored in this system.

### Q13 — hard — 4 marks

**Q13** [4 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 10 bits for the mantissa
- 6 bits for the exponent
- two's complement form for both the mantissa and the exponent.

A sensor reading has the denary value +86.4375. Written in binary, this value is `1010110.0111`. The reading cannot be stored exactly in this system.

A programmer suggests changing the system so that the mantissa uses 12 bits and the exponent uses 4 bits, keeping the total of 16 bits unchanged.

Explain why the reading cannot be stored exactly in the original system, and what effect the programmer's change would have.

### Q14 — medium — 3 marks

**Q14** [3 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 12 bits for the mantissa
- 4 bits for the exponent
- two's complement form for both the mantissa and the exponent.

The value +9.25 can be stored exactly in this system. The value +9.20 cannot.

Explain why.

### Q15 — easy — 2 marks

**Q15** [2 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 12 bits for the mantissa
- 4 bits for the exponent
- two's complement form for both the mantissa and the exponent.

A program stores the denary value +26.802734375. Written in binary, this value is `11010.110011011`.

Describe the reason why this value cannot be stored accurately in this system.

### Q16 — medium — 6 marks

**Q16** [3 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 10 bits for the mantissa
- 6 bits for the exponent
- two’s complement form for both the mantissa and the exponent.

Write the normalised floating-point representation of -96.75 in this system.

Show your working.

**Mantissa**

|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|

**Exponent**

|   |   |   |   |   |   |
|---|---|---|---|---|---|

*Source: Nov 2023 9618/32 Q1A*


**Q16** [3 marks]

Explain why a binary representation is sometimes only an approximation to the real number it represents.

*Source: Nov 2023 9618/32 Q1B*


### Q17 — medium — 5 marks

**Q17** [3 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 12 bits for the mantissa
- 4 bits for the exponent
- two’s complement form for both the mantissa and the exponent.

Write the normalised floating-point representation of +65.25 in this system.

Show your working.

**Mantissa**

|   |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|

**Exponent**

|   |   |   |   |
|---|---|---|---|

*Source: Nov 2023 9618/31 Q1A*


**Q17** [2 marks]

Explain the problem that will occur in storing the normalised floating-point representation of +65.20 in this system.

*Source: Nov 2023 9618/31 Q1B*


### Q18 — medium — 5 marks

**Q18** [2 marks]

Describe the effect of changing the allocation of bits used for the mantissa and for the exponent in a floating-point number with a fixed total number of bits.

*Source: June 2024 9618/32 Q1A*


**Q18** [3 marks]

Real numbers are stored in a computer, using floating-point representation with:

- 12 bits for the mantissa
- 4 bits for the exponent
- two’s complement form for both the mantissa and exponent.

Calculate the normalised floating-point representation of +54.8125 in this system.

Show your working.

**Mantissa**

|   |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|

**Exponent**

|   |   |   |   |
|---|---|---|---|

*Source: June 2024 9618/32 Q1B*


### Q19 — medium — 6 marks

**Q19** [3 marks]

Real numbers are stored in a computer system using floating-point representation with:

- 10 bits for the mantissa
- 6 bits for the exponent
- two’s complement form for both the mantissa and the exponent.

Calculate the denary value of the given normalised floating-point number.

Show your working.

**Mantissa**

| 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|---|

**Exponent**

| 0 | 0 | 1 | 0 | 0 | 1 |
|---|---|---|---|---|---|

*Source: June 2024 9618/31 Q1A*


**Q19** [3 marks]

Calculate the normalised floating-point representation of –102.75 in this system. Show your working.

**Mantissa**

|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|

**Exponent**

|   |   |   |   |   |   |
|---|---|---|---|---|---|

*Source: June 2024 9618/31 Q1B*


### Q20 — medium — 6 marks

**Q20** [2 marks]

Numbers are stored in a computer using binary floating‑point representation with:

- 12 bits for the mantissa
- 4 bits for the exponent
- two’s complement form for both the mantissa and the exponent.

Calculate the denary value of the given normalised binary floating‑point number.

Show you working.

**Mantissa**

| 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|

**Exponent**

| 0 | 1 | 1 | 1 |
|---|---|---|---|

*Source: Nov 2024 9618/32 Q4A*


**Q20** [4 marks]

Calculate the normalised binary floating‑point representation of – 49.1875 in this system.

Show your working.

**Mantissa**

|   |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|

**Exponent**

|   |   |   |   |
|---|---|---|---|

*Source: Nov 2024 9618/32 Q4B*


### Q21 — medium — 6 marks

**Q21** [3 marks]

Numbers are stored in a computer using binary floating-point representation with:

- 10 bits for the mantissa
- 6 bits for the exponent
- two’s complement form for both the mantissa and the exponent.

Calculate the normalised binary floating-point representation of +201.125 in this system.

Show your working.

**Mantissa**

|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|

**Exponent**

|   |   |   |   |   |   |
|---|---|---|---|---|---|

*Source: Nov 2024 9618/31 Q1A*


**Q21** [3 marks]

Calculate the denary value of the given normalised binary floating-point number.

Show your working.

**Mantissa**

| 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
|---|---|---|---|---|---|---|---|---|---|

**Exponent**

| 0 | 0 | 0 | 1 | 0 | 1 |
|---|---|---|---|---|---|

*Source: Nov 2024 9618/31 Q1B*

