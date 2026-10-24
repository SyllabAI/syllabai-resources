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

  - $\sum_{r = 1}^{5} ( 3 r - 1 ) = ( 3 \times 1 - 1 ) + ( 3 \times 2 - 1 ) + ( 3 \times 3 - 1 ) +... + ( 3 \times 5 - 1 )$
- The sum of the **first **$n$** terms** has an upper limit of $n$

  - `sum from r equals 1 to n of r equals 1 plus 2 plus 3 plus... plus n`

### How do I write a series as the difference of two sums?

- When the **lower limit **is **not 1**, such as`sum from r equals 5 to 10 of r equals 5 plus 6 plus 7 plus... plus 10`, you can write it as the **difference** **between two sums**:

  - `sum from r equals 5 to 10 of r equals sum from r equals 1 to 10 of r minus sum from r equals 1 to 4 of r`
  - This is because$5 + 6 + 7 + 8 + 9 + 10 = ( 1 + 2 + 3 + 4 +... + 10 ) - ( 1 + 2 + 3 + 4 )$
  
    - The 1, 2, 3 and 4** cancel out**, leaving 5, 6, ..., 10
  - Be careful: the **upper limit **of the second** **sum is **one less** than the** lower limit** of the original sum!

### What properties of sigma notation do I need to know?

- You need to know the following rules:

  - `sum from r equals 1 to n of k equals k plus k plus... plus k equals k n`
  
    - The **sum** of a **constant** is the constant$\timesn$
  - $\sum_{r = 1}^{n} ( a r + b ) = a \sum_{r = 1}^{n} r + b n$
  
    - **Coefficients **of $r$* *can come **out **of the sum
    - **Constants **are **multiplied** by $n$

### What is the formula for the sum of the natural numbers?

- `sum from r equals 1 to n of r equals 1 plus 2 plus 3 plus... plus n` is the sum of the** natural numbers**

  - Natural numbers are **positive integers**
- It has the** standard formula**:

  - $\sum_{r = 1}^{n} r = 1 \frac{1}{2} n ( n + 1 )$
  - You can work the formula out using **arithmetic series**
  
    - first term 1, common  difference 1
- You may use the formula in calculations **without proof**

> **Exam Hint**
> The formula for the sum of natural numbers is **not given** in the Formulae Booklet!

> **Worked Example**
> A sum of $n$ terms is given by $\sum_{r = 1}^{n} ( 2 r + 1 )$.
> 
> (a)  Using any standard summation formulae, show that $\sum_{r = 1}^{n} ( 2 r + 1 ) = n ( n + A )$ where $A$  is a positive integer to be found.
> 
> > *Use the rule that *$\sum_{r = 1}^{n} ( a r + b ) = a \sum_{r = 1}^{n} r + b n$
> 
> $\sum_{r = 1}^{n} ( 2 r + 1 ) = 2 \sum_{r = 1}^{n} r + n$
> 
> > *Substitute in the formula  *$\sum_{r = 1}^{n} r = 1 \frac{1}{2} n ( n + 1 )$* *
> 
> $\sum_{r = 1}^{n} ( 2 r + 1 ) = 2 ( 1 \frac{1}{2} n ( n + 1 ) ) + n$
> 
> > *Expand and simplify*
> 
> $\begin{gathered} \sum_{r = 1}^{n} ( 2 r + 1 ) & = n ( n + 1 ) + n \\ = n^{2} + 2 n \end{gathered}$
> 
> > *Factorise the right-hand side*
> 
> $\begin{gathered} \sum_{r = 1}^{n} ( 2 r + 1 ) & = n ( n + 2 ) \end{gathered}$
> 
> > *Check it has the right form, *$n ( n + A )$
> 
> **Final answer:** $\begin{gathered} \sum_{r = 1}^{n} ( 2 r + 1 ) & = n ( n + 2 ) \end{gathered}$** where **$\begin{gathered} A = 2 \end{gathered}$
> 
> (b)  Hence find the sum of the odd numbers from 3 to 81.
> 
> > *It often helps to write out the first few terms and the last term of the series*
> 
> $\sum_{r = 1}^{n} ( 2 r + 1 ) = ( 2 \times 1 + 1 ) + ( 2 \times 2 + 1 ) + ( 2 \times 3 + 1 ) +... + ( 2 \times n + 1 )$
> 
> > *Simplify these terms*
> 
> $\sum_{r = 1}^{n} ( 2 r + 1 ) = 3 + 5 + 7 +... + ( 2 n + 1 )$
> 
> > *This is the sum of the odd numbers from 3 to *$( 2 n + 1 )$
> *The question wants the sum of odd numbers from 3 to 81*
> *Use the last term to find *$n$
> 
> * *$\begin{gathered} 2 n + 1 & = 81 \\ 2 n & = 80 \\ n = 40 \end{gathered}$
> 
> > *The sum of the first 40 terms gives the sum of odd numbers from 3 to 81*
> *Substitute *$n=40$* into the formula in part (a)*
> 
> $40 \times ( 40 + 2 )$
> 
> **Final answer:** **1680**

## Sums of Squares

> **Spec point** — `spcpt_qnKVvs82Wxy4pD6P`

## Sums of Squares

### What is the formula for the sum of the squares of the natural numbers?

- $\sum_{r = 1}^{n} r^{2} = 1^{2} + 2^{2} + 3^{2} +... + n^{2} = 1 + 4 + 9 +... + n^{2}$ is the sum of the **squares** of the** natural numbers**
- It has it the** standard formula**:

  - $\sum_{r = 1}^{n} r^{2} = \frac{1}{6} n ( n + 1 ) ( 2 n + 1 )$
  - You may use the formula in calculations **without proof**
- Note that $\sum_{r = 1}^{n} ( a r^{2} + b ) = a \sum_{r = 1}^{n} r^{2} + b n$

  - **Coefficients **of* *$r^{2}$ can come **out **of the sum
  - **Constants **are **multiplied** by $n$

> **Exam Hint**
> This formula is given in the Formulae Booklet.

> **Worked Example**
> (a)  Evaluate $\sum_{r = 1}^{30} r^{2}$
> 
> > *Evaluate means "find the value of"*
> *This is the sum of the first 30 square numbers*
> *Substitute *$n=30$* into the formula *$\sum_{r = 1}^{n} r^{2} = \frac{1}{6} n ( n + 1 ) ( 2 n + 1 )$* *
> 
> $\begin{gathered} \sum_{r = 1}^{30} r^{2} & = \frac{1}{6} \times 30 \times ( 30 + 1 ) ( 2 \times 30 + 1 ) \\ = \frac{1}{6} \times 30 \times 31 \times 61 \end{gathered}$* *
> 
> **Final answer:** **9455**
> 
> (b)  Show that $\sum_{r = m + 1}^{2 m} r^{2} = \frac{1}{6} m ( P m + 1 ) ( Q m + 1 )$ where $P<Q$  and where $P$ and $Q$ are prime numbers to be found.
> 
> > *The lower limit is not 1, so write it as the difference between two sums*
> *It can help to imagine simpler numbers, *$\sum_{r = 5}^{10} r^{2} = \sum_{r = 1}^{10} r^{2} - \sum_{r = 1}^{4} r^{2}$
> 
> $\sum_{r = m + 1}^{2 m} r^{2} = \sum_{r = 1}^{2 m} r^{2} - \sum_{r = 1}^{m} r^{2}$
> 
> > *Now use the formula *$\sum_{r = 1}^{n} r^{2} = \frac{1}{6} n ( n + 1 ) ( 2 n + 1 )$* for each sum on the right*
> 
> $\sum_{r = m + 1}^{2 m} r^{2} = \frac{1}{6} ( 2 m ) ( 2 m + 1 ) ( 4 m + 1 ) - \frac{1}{6} m ( m + 1 ) ( 2 m + 1 )$
> 
> *Factorise out*$\frac{1}{6}$* , *$m$ *and *$( 2 m + 1 )$* then simplify*
> 
> $\begin{gathered} \sum_{r = m + 1}^{2 m} r^{2} & = \frac{1}{6} m ( 2 m + 1 ) [ 2 ( 4 m + 1 ) - ( m + 1 ) ] \\ = \frac{1}{6} m ( 2 m + 1 ) ( 7 m + 1 ) \end{gathered}$
> 
> > *Check this is in the right form*
> *2 and 7 are prime numbers and 2 < 7*
> 
> **Final answer:** $\begin{gathered} \sum_{r = m + 1}^{2 m} r^{2} & = \frac{1}{6} m ( 2 m + 1 ) ( 7 m + 1 ) \end{gathered}$** where **$\begin{gathered} P = 2 \end{gathered}$** and **$\begin{gathered} Q = 7 \end{gathered}$

## Sums of Cubes

> **Spec point** — `spcpt_Dwkpk276tdPzYYpF`

## Sums of Cubes

### What is the formula for the sum of the cubes of the natural numbers?

- $\sum_{r = 1}^{n} r^{3} = 1^{3} + 2^{3} + 3^{3} +... + n^{3} = 1 + 8 + 27 +... + n^{3}$ is the sum of the **cubes** of the** natural numbers**
- It has it the** standard formula**:

  - $\sum_{r = 1}^{n} r^{3} = 1 \frac{1}{4} n^{2} ( n + 1 )^{2}$
  - You may use the formula in calculations **without proof**
  - It is the **square** of the **formula** for the **sum **of the **natural numbers**
  
    - $( \sum_{r = 1}^{n} r )^{2} = ( 1 \frac{1}{2} n ( n + 1 ) )^{2} = 1 \frac{1}{4} n^{2} ( n + 1 )^{2}$
- Note that $\sum_{r = 1}^{n} ( a r^{3} + b ) = a \sum_{r = 1}^{n} r^{3} + b n$

  - **Coefficients **of $r^{3}$* *can come **out **of the sum
  - **Constants **are **multiplied** by $n$

> **Exam Hint**
> This formula is given in the Formulae Booklet.

> **Worked Example**
> (a)  Find $1^{3}+2^{3}+3^{3}+...+24^{3}$
> 
> > *This is the sum of the first 24 cube numbers*
> *Substitute *$n=24$* into the formula *$\sum_{r = 1}^{n} r^{3} = 1 \frac{1}{4} n^{2} ( n + 1 )^{2}$* *
> 
> $\begin{gathered} \sum_{r = 1}^{24} r^{3} & = 1 \frac{1}{4} \times 24^{2} \times ( 24 + 1 )^{2} \\ = 1 \frac{1}{4} \times 24^{2} \times 25^{2} \end{gathered}$
> 
> **Final answer:** **90000**
> 
> (b)  Find and simplify a formula for the sum of the first $n$ even cube numbers.
> 
> > *The sum of even cube numbers is 2*<sup>*3*</sup>* + 4*<sup>*3*</sup>* + 6*<sup>*3*</sup>* + ...*
> *The first 5 would end on 10*<sup>*3*</sup>
> *The first *$n$* would end on *$( 2 n )^{3}$
> 
> $2^{3} + 4^{3} + 6^{3} +... + ( 2 n )^{3}$* *
> 
> > *The standard formula is for *$\sum_{r = 1}^{n} r^{3}$* *
> *To get just the even numbers, replace *$r$* with *$2r$
> 
> $\sum_{r = 1}^{n} ( 2 r )^{3}$
> 
> > *Cube the expression and use *$\sum_{r = 1}^{n} a r^{3} = a \sum_{r = 1}^{n} r^{3}$
> 
> $\begin{gathered} \sum_{r = 1}^{n} ( 2 r )^{3} & = \sum_{r = 1}^{n} 8 r^{3} \\ = 8 \sum_{r = 1}^{n} r^{3} \end{gathered}$
> 
> > *Now substitute in the standard formula *$\sum_{r = 1}^{n} r^{3} = 1 \frac{1}{4} n^{2} ( n + 1 )^{2}$* and simplify*
> 
> $\begin{gathered} \sum_{r = 1}^{n} ( 2 r )^{3} & = 8 ( 1 \frac{1}{4} n^{2} ( n + 1 )^{2} ) \\ = 2 n^{2} ( n + 1 )^{2} \end{gathered}$
> 
> $\begin{gathered} 2 n^{2} ( n + 1 )^{2} \end{gathered}$
