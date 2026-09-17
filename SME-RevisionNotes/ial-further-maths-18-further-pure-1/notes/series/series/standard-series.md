---
note_id: "rn_cVxMCGzqwMdvXpTx"
title: "Standard Series"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/series/series/standard-series
path: series/series/standard-series
updated_at: "2024-04-10T09:40:37.466Z"
spec_point_ids: ["spcpt_VBt5CyWqhyvcvTwD", "spcpt_qnKVvs82Wxy4pD6P", "spcpt_Dwkpk276tdPzYYpF"]
spec_point_codes: []
guided_study: false
---

# Standard Series

## Sums of Natural Numbers

> **Spec point** — `spcpt_VBt5CyWqhyvcvTwD`

## Sums of Natural Numbers

### What is sigma notation?

- **Sigma notation **represents **sums** as follows:`sum from r equals 1 to 5 of r equals 1 plus 2 plus 3 plus 4 plus 5`

  - $r$ counts in** integers** from the** lower limit **to the **upper limit**
- It works for **functions** of $r$

  - `sum from r equals 1 to 5 of open parentheses 3 r minus 1 close parentheses equals open parentheses 3 cross times 1 minus 1 close parentheses plus open parentheses 3 cross times 2 minus 1 close parentheses plus left parenthesis 3 cross times 3 minus 1 right parenthesis plus... plus open parentheses 3 cross times 5 minus 1 close parentheses`
- The sum of the **first **$n$** terms** has an upper limit of $n$

  - `sum from r equals 1 to n of r equals 1 plus 2 plus 3 plus... plus n`

### How do I write a series as the difference of two sums?

- When the **lower limit **is **not 1**, such as`sum from r equals 5 to 10 of r equals 5 plus 6 plus 7 plus... plus 10`, you can write it as the **difference** **between two sums**:

  - `sum from r equals 5 to 10 of r equals sum from r equals 1 to 10 of r minus sum from r equals 1 to 4 of r`
  - This is because`5 plus 6 plus 7 plus 8 plus 9 plus 10 equals open parentheses 1 plus 2 plus 3 plus 4 plus... plus 10 close parentheses minus open parentheses 1 plus 2 plus 3 plus 4 close parentheses`
  
    - The 1, 2, 3 and 4** cancel out**, leaving 5, 6, ..., 10
  - Be careful: the **upper limit **of the second** **sum is **one less** than the** lower limit** of the original sum!

### What properties of sigma notation do I need to know?

- You need to know the following rules:

  - `sum from r equals 1 to n of k equals k plus k plus... plus k equals k n`
  
    - The **sum** of a **constant** is the constant$\timesn$
  - `sum from r equals 1 to n of open parentheses a r plus b close parentheses equals a sum from r equals 1 to n of r space plus b n`
  
    - **Coefficients **of $r$* *can come **out **of the sum
    - **Constants **are **multiplied** by $n$

### What is the formula for the sum of the natural numbers?

- `sum from r equals 1 to n of r equals 1 plus 2 plus 3 plus... plus n` is the sum of the** natural numbers**

  - Natural numbers are **positive integers**
- It has the** standard formula**:

  - `sum from r equals 1 to n of r equals 1 half n open parentheses n plus 1 close parentheses`
  - You can work the formula out using **arithmetic series**
  
    - first term 1, common  difference 1
- You may use the formula in calculations **without proof**

> **Exam Hint**
> The formula for the sum of natural numbers is **not given** in the Formulae Booklet!

> **Worked Example**
> A sum of $n$ terms is given by `sum from r equals 1 to n of open parentheses 2 r plus 1 close parentheses`.
> 
> (a)  Using any standard summation formulae, show that `sum from r equals 1 to n of open parentheses 2 r plus 1 close parentheses equals n open parentheses n plus A close parentheses` where $A$  is a positive integer to be found.
> 
> > *Use the rule that *`sum from r equals 1 to n of open parentheses a r plus b close parentheses equals a sum from r equals 1 to n of r space plus b n`
> 
> `sum from r equals 1 to n of open parentheses 2 r plus 1 close parentheses equals 2 sum from r equals 1 to n of r space plus n`
> 
> > *Substitute in the formula  *`sum from r equals 1 to n of r equals 1 half n open parentheses n plus 1 close parentheses`* *
> 
> `sum from r equals 1 to n of open parentheses 2 r plus 1 close parentheses equals 2 open parentheses 1 half n open parentheses n plus 1 close parentheses close parentheses space plus n`
> 
> > *Expand and simplify*
> 
> `table row cell sum from r equals 1 to n of open parentheses 2 r plus 1 close parentheses end cell equals cell n open parentheses n plus 1 close parentheses plus n end cell row blank equals cell n squared plus 2 n end cell end table`
> 
> > *Factorise the right-hand side*
> 
> `table row cell sum from r equals 1 to n of open parentheses 2 r plus 1 close parentheses end cell equals cell n open parentheses n plus 2 close parentheses end cell end table`
> 
> > *Check it has the right form, *`n open parentheses n plus A close parentheses`
> 
> **Final answer:** `table row cell sum from r equals 1 to n of open parentheses 2 r plus 1 close parentheses end cell equals cell n open parentheses n plus 2 close parentheses end cell end table`** where **`table row A equals 2 end table`
> 
> (b)  Hence find the sum of the odd numbers from 3 to 81.
> 
> > *It often helps to write out the first few terms and the last term of the series*
> 
> `sum from r equals 1 to n of open parentheses 2 r plus 1 close parentheses equals open parentheses 2 cross times 1 plus 1 close parentheses plus open parentheses 2 cross times 2 plus 1 close parentheses plus open parentheses 2 cross times 3 plus 1 close parentheses plus... plus open parentheses 2 cross times n plus 1 close parentheses`
> 
> > *Simplify these terms*
> 
> `sum from r equals 1 to n of open parentheses 2 r plus 1 close parentheses equals 3 plus 5 plus 7 plus... plus open parentheses 2 n plus 1 close parentheses`
> 
> > *This is the sum of the odd numbers from 3 to *`open parentheses 2 n plus 1 close parentheses`
> *The question wants the sum of odd numbers from 3 to 81*
> *Use the last term to find *$n$
> 
> * *`table row cell 2 n plus 1 end cell equals 81 row cell 2 n end cell equals 80 row n equals 40 end table`
> 
> > *The sum of the first 40 terms gives the sum of odd numbers from 3 to 81*
> *Substitute *$n=40$* into the formula in part (a)*
> 
> `40 cross times open parentheses 40 plus 2 close parentheses`
> 
> **Final answer:** **1680**

## Sums of Squares

> **Spec point** — `spcpt_qnKVvs82Wxy4pD6P`

## Sums of Squares

### What is the formula for the sum of the squares of the natural numbers?

- `sum from r equals 1 to n of r squared equals 1 squared plus 2 squared plus 3 squared plus... plus n squared equals 1 plus 4 plus 9 plus... plus n squared` is the sum of the **squares** of the** natural numbers**
- It has it the** standard formula**:

  - `sum from r equals 1 to n of r squared equals 1 over 6 n open parentheses n plus 1 close parentheses open parentheses 2 n plus 1 close parentheses`
  - You may use the formula in calculations **without proof**
- Note that `sum from r equals 1 to n of open parentheses a r squared plus b close parentheses equals a sum from r equals 1 to n of r squared space plus b n`

  - **Coefficients **of* *$r^{2}$ can come **out **of the sum
  - **Constants **are **multiplied** by $n$

> **Exam Hint**
> This formula is given in the Formulae Booklet.

> **Worked Example**
> (a)  Evaluate `sum from r equals 1 to 30 of r squared`
> 
> > *Evaluate means "find the value of"*
> *This is the sum of the first 30 square numbers*
> *Substitute *$n=30$* into the formula *`sum from r equals 1 to n of r squared equals 1 over 6 n open parentheses n plus 1 close parentheses open parentheses 2 n plus 1 close parentheses`* *
> 
> `table row cell sum from r equals 1 to 30 of r squared end cell equals cell 1 over 6 cross times 30 cross times open parentheses 30 plus 1 close parentheses open parentheses 2 cross times 30 plus 1 close parentheses end cell row blank equals cell 1 over 6 cross times 30 cross times 31 cross times 61 end cell end table`* *
> 
> **Final answer:** **9455**
> 
> (b)  Show that `sum from r equals m plus 1 to 2 m of r squared space equals 1 over 6 m open parentheses P m plus 1 close parentheses open parentheses Q m plus 1 close parentheses` where $P<Q$  and where $P$ and $Q$ are prime numbers to be found.
> 
> > *The lower limit is not 1, so write it as the difference between two sums*
> *It can help to imagine simpler numbers, *`sum from r equals 5 to 10 of r squared equals sum from r equals 1 to 10 of r squared minus sum from r equals 1 to 4 of r squared`
> 
> `sum from r equals m plus 1 to 2 m of r squared equals sum from r equals 1 to 2 m of r squared minus sum from r equals 1 to m of r squared`
> 
> > *Now use the formula *`sum from r equals 1 to n of r squared equals 1 over 6 n open parentheses n plus 1 close parentheses open parentheses 2 n plus 1 close parentheses`* for each sum on the right*
> 
> `sum from r equals m plus 1 to 2 m of r squared equals 1 over 6 open parentheses 2 m close parentheses open parentheses 2 m plus 1 close parentheses open parentheses 4 m plus 1 close parentheses minus 1 over 6 m open parentheses m plus 1 close parentheses open parentheses 2 m plus 1 close parentheses`
> 
> *Factorise out*$\frac{1}{6}$* , *$m$ *and *`open parentheses 2 m plus 1 close parentheses`* then simplify*
> 
> `table row cell sum from r equals m plus 1 to 2 m of r squared end cell equals cell 1 over 6 m open parentheses 2 m plus 1 close parentheses open square brackets 2 open parentheses 4 m plus 1 close parentheses minus open parentheses m plus 1 close parentheses close square brackets end cell row blank equals cell 1 over 6 m open parentheses 2 m plus 1 close parentheses open parentheses 7 m plus 1 close parentheses end cell end table`
> 
> > *Check this is in the right form*
> *2 and 7 are prime numbers and 2 < 7*
> 
> **Final answer:** `table row cell sum from r equals m plus 1 to 2 m of r squared end cell equals cell 1 over 6 m open parentheses 2 m plus 1 close parentheses open parentheses 7 m plus 1 close parentheses end cell end table`** where **`table row P equals 2 end table`** and **`table row Q equals 7 end table`

## Sums of Cubes

> **Spec point** — `spcpt_Dwkpk276tdPzYYpF`

## Sums of Cubes

### What is the formula for the sum of the cubes of the natural numbers?

- `sum from r equals 1 to n of r cubed equals 1 cubed plus 2 cubed plus 3 cubed plus... plus n cubed equals 1 plus 8 plus 27 plus... plus n cubed` is the sum of the **cubes** of the** natural numbers**
- It has it the** standard formula**:

  - `sum from r equals 1 to n of r cubed equals 1 fourth n squared open parentheses n plus 1 close parentheses squared`
  - You may use the formula in calculations **without proof**
  - It is the **square** of the **formula** for the **sum **of the **natural numbers**
  
    - `open parentheses sum from r equals 1 to n of r close parentheses squared equals open parentheses 1 half n open parentheses n plus 1 close parentheses close parentheses squared equals 1 fourth n squared open parentheses n plus 1 close parentheses squared`
- Note that `sum from r equals 1 to n of open parentheses a r cubed plus b close parentheses equals a sum from r equals 1 to n of r cubed space plus b n`

  - **Coefficients **of $r^{3}$* *can come **out **of the sum
  - **Constants **are **multiplied** by $n$

> **Exam Hint**
> This formula is given in the Formulae Booklet.

> **Worked Example**
> (a)  Find $1^{3}+2^{3}+3^{3}+...+24^{3}$
> 
> > *This is the sum of the first 24 cube numbers*
> *Substitute *$n=24$* into the formula *`sum from r equals 1 to n of r cubed equals 1 fourth n squared open parentheses n plus 1 close parentheses squared`* *
> 
> `table row cell sum from r equals 1 to 24 of r cubed end cell equals cell 1 fourth cross times 24 squared cross times open parentheses 24 plus 1 close parentheses squared end cell row blank equals cell 1 fourth cross times 24 squared cross times 25 squared end cell end table`
> 
> **Final answer:** **90000**
> 
> (b)  Find and simplify a formula for the sum of the first $n$ even cube numbers.
> 
> > *The sum of even cube numbers is 2*<sup>*3*</sup>* + 4*<sup>*3*</sup>* + 6*<sup>*3*</sup>* + ...*
> *The first 5 would end on 10*<sup>*3*</sup>
> *The first *$n$* would end on *`open parentheses 2 n close parentheses cubed`
> 
> `2 cubed plus 4 cubed plus 6 cubed plus... plus open parentheses 2 n close parentheses cubed`* *
> 
> > *The standard formula is for *`sum from r equals 1 to n of r cubed`* *
> *To get just the even numbers, replace *$r$* with *$2r$
> 
> `sum from r equals 1 to n of open parentheses 2 r close parentheses cubed`
> 
> > *Cube the expression and use *`sum from r equals 1 to n of a r cubed equals a sum from r equals 1 to n of r cubed`
> 
> `table row cell sum from r equals 1 to n of open parentheses 2 r close parentheses cubed end cell equals cell sum from r equals 1 to n of 8 r cubed end cell row blank equals cell 8 sum from r equals 1 to n of r cubed end cell end table`
> 
> > *Now substitute in the standard formula *`sum from r equals 1 to n of r cubed equals 1 fourth n squared open parentheses n plus 1 close parentheses squared`* and simplify*
> 
> `table row cell sum from r equals 1 to n of open parentheses 2 r close parentheses cubed end cell equals cell 8 open parentheses 1 fourth n squared open parentheses n plus 1 close parentheses squared close parentheses end cell row blank equals cell 2 n squared open parentheses n plus 1 close parentheses squared end cell end table`
> 
> `table row blank blank cell 2 n squared open parentheses n plus 1 close parentheses squared end cell end table`
