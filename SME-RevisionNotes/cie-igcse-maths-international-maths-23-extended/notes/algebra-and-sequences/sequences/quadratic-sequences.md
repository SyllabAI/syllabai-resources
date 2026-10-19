---
note_id: "rn_VV29xBKfZfsmGccF"
title: "Quadratic Sequences"
source: https://www.savemyexams.com/igcse/maths/cie/international-maths/23/extended/revision-notes/algebra-and-sequences/sequences/quadratic-sequences
path: algebra-and-sequences/sequences/quadratic-sequences
updated_at: "2026-01-20T17:19:13.491Z"
spec_point_ids: ["spcpt_6T579sqnsCTJJQVG"]
spec_point_codes: []
guided_study: true
---

# Quadratic Sequences

## Quadratic Sequences

> **Spec point** — `spcpt_6T579sqnsCTJJQVG`

## Quadratic Sequences

### What is a quadratic sequence?

- A **quadratic **sequence has an ***n *****th term formula** that involves ***n***<sup>**2**</sup>
- The **second differences** are **constant **(the same)

  - These are the differences between the first differences
  - For example,   3, 9, 19, 33, 51, …
  1st Differences: 6, 10, 14, 18, ... 2nd Differences:  4,   4,   4, ...

### How do I find the n<sup>th</sup> term formula for a simple quadratic sequence?

- The sequence with the *n*th term formula** *****n***<sup>**2**</sup> are the **square numbers **

  - 1, 4, 9, 16, 25, 36, 49, ...
  
    - From 1<sup>2</sup>, 2<sup>2</sup>, 3<sup>2</sup>, 4<sup>2</sup>, ...
- Some sequences are just the square numbers but with a **different starting number**

  - 16, 25, 36, 49, ... has the formula (*n* + 3)<sup>2</sup>
  
    - Substitute in *n* = 1, *n* = 2, *n* = 3 to see why
  - 0, 1, 4, 9, ... has the formula (*n* - 1)<sup>2</sup>
- Finding the ***n*****th term formula** comes from **comparing** sequences to the square numbers

  - 2, 5, 10, 17, 26, 37, 50, ... has the formula *n*<sup>2 </sup>+ 1
  
    - Each term is 1 more than the square numbers
  - 2, 8, 18, 32, 50, 72, 98, ... has the formula 2*n*<sup>2</sup>
  
    - Each term is double a square number
- It may be a simple **combination** of the above

  - For example, doubling then adding 1
  
    - 3, 9, 19, 33, 51, 73, 99, ... has the formula 2*n*<sup>2</sup> + 1
  - For example, subtracting 2 from square numbers starting with 4
  
    - 2, 7, 14, 23, ... has the formula (*n* + 1)<sup>2</sup> - 2

### How do I find the n<sup>th</sup> term formula for any quadratic sequence?

- **STEP 1**
Work out the **sequences **of **first **and **second differences**

  - e.g. for the sequence 1, 10, 23, 40, 61

| sequence | 1 | 10 | 23 | 40 | 61 |
|---|---|---|---|---|---|
| first difference |   | +9 | +13 | +17 | +21 |
| second difference |   |   | +4 | +4 | +4 |

- **STEP 2**
**Divide **the **second difference by 2** to find the coefficient of *n*<sup>2</sup>

  - e.g.  *a* = 4 ÷ 2 = 2
- **STEP 3**
Write out the **first three** or **four **terms of *an*<sup>2</sup> and **subtract **the terms from the **corresponding terms **of the given sequence

  - e.g. for the sequence 1, 10, 23, 40, 61

| sequence | 1 | 10 | 23 | 40 |
|---|---|---|---|---|
| 2*n*<sup>2</sup> | 2 | 8 | 18 | 32 |
| difference | -1 | 2 | 5 | 8 |

- **STEP 4**
Work out the ***n*****th term** of these **differences **to find the *bn* + *c *part of the formula

  - e.g. the *n*th term of -1, 2, 5, 8, ... is  *bn* + *c *= 3*n* − 4
- **STEP 5**
Find *an*<sup>*2*</sup>* *+* bn *+* c *by adding together this linear *n*th term to *an*<sup>2</sup> term

  - e.g.  *an*<sup>*2*</sup>* *+* bn *+* c *= 2*n*<sup>2</sup> + 3*n* − 4

> **Exam Hint**
> You must learn the square numbers from 1<sup>2</sup> to 15<sup>2</sup> .

> **Worked Example**
> For the sequence 6, 9, 14, 21, 30, ....
> 
> (a) Find a formula for the *n*<sup>th </sup>term.
> 
> **Answer:**
> 
> > *Find the first and second differences*
> 
> *Sequence:   6,   9,   14,   21,   30*
> *     First differences:   3,    5,     7,     9, ...           *
> *    Second differences:   2,    2,     2, ...   *
> 
> > *Halve the second difference, this is the value of **a** *
> *Write down the sequence **an*<sup>*2*</sup>
> *Compare this to the original sequence*
> 
> * Sequence:  6,   9,   14,   21,   30, ..*.     
> **           1n***<sup>2 </sup>**:  1,   4,   9,   16,   25,  ... * 
> *Differences: 5, 5, 5, 5, 5, ...*
> 
> > *Each term is 5 more than the terms in **n*<sup>*2*</sup>*, so add 5 to **n*<sup>*2*</sup>
> 
> **Final answer:** **n**<sup>**th**</sup>** term =**** n**<sup>**2**</sup>** + 5**
> 
> (b) Hence, find the 20<sup>th</sup> term of the sequence.
> 
> **Answer:**
> 
> > *Substitute **n** = 20 into **n*<sup>*2*</sup>* + 5*
> 
> *(20)**<sup>2</sup>** + 5 = 400 + 5*
> 
> **Final answer:** **The 20**<sup>**th**</sup>** term is 405**

> **Worked Example**
> For the sequence 5, 7, 11, 17, 25, ....
> 
> (a) Find a formula for the *n*<sup>th </sup>term.
> 
> **Answer:**
> *Start by finding the first and second differences*
> 
> *Sequence:   5,   7,   11,   17,   25*
> 
> *First differences:      2,    4,     6,      8, ...           *
> 
> *Second difference:     2,    2,     2, ...               *
> 
> > *Hence *
> 
> **a*** = 2 ÷ 2 = 1*
> 
> > *Now write down **an*<sup>*2*</sup>* (just **n*<sup>*2*</sup>* in this case as **a** = 1) and subtract the terms from the original sequence*
> 
> *sequence:   5,  7, 11, 17, ...*
> 
> **          an***<sup>2. </sup>**:  1,  4,  9,   16, ...*
> 
> * difference:  4,  3,  2,  1, ...   *
> 
> > *Work out the **n**th term of these differences to give you **bn** + **c*
> 
> **bn*** + ***c*** = −n + 5*
> 
> > *Add **an*<sup>*2*</sup>* and **bn** + **c **together to give you the **n*<sup>*th*</sup>* term of the sequence*
> 
> **Final answer:** **n**<sup>**th**</sup>** term =**** n**<sup>**2**</sup>** − ****n**** + 5**
> 
> (b) Hence find the 20<sup>th</sup> term of the sequence.
> 
> **Answer:**
> 
> *Substitute **n** = 20 into **n*<sup>*2*</sup>* − **n** + 5*
> 
> *(20)**<sup>2</sup>** − 20 + 5 = 400 − 15 *
> 
> **Final answer:** **20**<sup>**th**</sup>** term = 385**
