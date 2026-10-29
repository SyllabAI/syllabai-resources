---
note_id: "rn_GDy4XcxmvwF6mCMV"
title: "Other Sequences"
source: https://www.savemyexams.com/igcse/maths/cie/25/extended/revision-notes/algebra-and-sequences/sequences/types-of-sequences
path: algebra-and-sequences/sequences/types-of-sequences
updated_at: "2026-08-27T12:04:53.474Z"
spec_point_ids: ["spcpt_TrK3QG8J9HsdDRWC"]
spec_point_codes: []
guided_study: true
---

# Other Sequences

## Types of Sequences

> **Spec point** — `spcpt_TrK3QG8J9HsdDRWC`

## Types of Sequences

### What are common types of sequences?

- Sequences can follow any rule, but common sequences are

  - **Linear**
  
    - *n*th term = $an+b$
  - **Quadratic**
  
    - *n*th term = $an^{2}+bn+c$
  - **Cubic**
  
    - *n*th term = $an^{3}+bn^{2}+cn+d$
  - **Exponential **(**Geometric**)
  
    - *n*th term = $a\timesr^{n}$ or $a\timesr^{n-1}$
- Sequences may also be formed using common numbers

  - **Prime numbers**
  
    - 2, 3, 5, 7, 11, ...
  - **Triangular numbers**
  
    - 1, 3, 6, 10, 15, ...

### What is a cubic sequence?

- A **cubic **sequence has an ***n *****th term formula** that involves ***n***<sup>**3**</sup>
- The **third differences** are **constant **(the same)

  - These are the differences between the second differences
  - For example,   4, 25, 82, 193, 376, 649, ...
  1st Differences:  21, 57, 111, 183, 273, ... 2nd Differences:   36,  54,  72,   90, ...
  3rd Differences:      18,    18,   18, ...

### How do I find the n<sup>th</sup> term formula for a simple cubic sequence?

- The sequence with the *n* th term formula of** *****n***<sup>**3**</sup> is the **cube numbers **

  - 1, 8, 27, 64, 125, ...
  
    - From 1<sup>3</sup>, 2<sup>3</sup>, 3<sup>3</sup>, 4<sup>3</sup>, ...
- Finding the ***n *****th term formula** of other cubic sequences comes from **comparing** them to the cube numbers, *n*<sup>3</sup>

  - 2, 9, 28, 65, 126, ... has the formula *n*<sup>3 </sup>+ 1
  
    - Each term is one more than the cube numbers
  - 2, 16, 54, 128, 250, ...  has the formula 2*n*<sup>3</sup>
  
    - Each term is double a cube number
  - 8, 27, 64, 125, ... has the formula (n+1)<sup>3</sup>
  
    - They are the cube numbers starting from 2<sup>3</sup>
- You can also use **third differences** to help find the *n* th term $an^{3}+bn^{2}+cn+d$

  - The value of *a*  is $\frac{1}{6}$ of the **third** difference
  
    - e.g. the third difference of 8, 23, 62, 137, 260, ... is 12
  - You can then subtract *an*<sup>3</sup> from the sequence and find the *n*th term of the differences
  
    - e.g. (8, 23, 62, 137, 260, ...) - (2, 16, 54, 128, 250, ... ) is (6, 7, 8, 9, 10, ...) which has *n*th term *n* + 5
    - So the nth term is 2*n*<sup>3</sup> + *n* + 5

### What is an exponential (geometric) sequence?

- An **exponential (geometric) sequence** is one where you **multiply each term **by the **same number** to get the **next term**

  - E.g. 3, 6, 12, 24, 48, ... is exponential because:
  
    - terms are **multiplied** by 2 each time
    - 2 is called the **common ratio** (or **constant multiplier**)
    - You can find this by dividing any term by the term immediately before, 6 ÷ 3 or 12 ÷ 6 or 24 ÷ 12 etc

### How do I find the n<sup>th</sup> term formula for a simple exponential sequence?

- The sequence with the *n* th term formula of** *****r***<sup>***n***</sup> is the **powers **of *r*

  - e.g. 2, 4, 8, 16, 32, ... has formula 2<sup>*n*</sup>
- Finding the ***n *****th term formula** of other exponential sequences comes from **comparing** them to the powers of the multiplier, *r*<sup>*n*</sup>

  - 6, 12, 24, 48, 96, ... has the formula 3× *2*<sup>*n*</sup>
  
    - Each term is three times more than a power of 2
  - 4, 8, 16, 32, 64, ... has the formula 2<sup>*n*</sup><sup>+1</sup>
  
    - Each term is a power of 2 starting at 2<sup>2</sup>
- If the common ratio satisfies

  - $r>1$ then the sequence **increases**
  - $0<r<1$ then the sequence **decreases**
  
    - E.g. $r=\frac{1}{2}$

### How can sequences be made harder?

- You may be given a **fraction **with **two different sequences** on the top and bottom

  - E.g. $\frac{3}{1},\frac{5}{8},\frac{7}{27},\frac{9}{64},...$
  
    - The **numerators **are the **linear **sequence $2n+1$
    - The **denominators **are the **cube **numbers, $n^{3}$
    - So the *n* th term formula is $\frac{2n+1}{n^{3}}$
- You may be asked to find ** combinations** of two different sequences

  - E.g. if sequence *U* is the prime numbers and sequence *V* has the *n* th term formula $4n^{2}$, find the sequence *U* + *V*
  
    - *U* = 2, 3, 5, 7, ... and *V* = 4, 16, 36, 64, ...
    - *U* + *V* = (2 + 4), (3 + 16), (5 + 36), (7 + 64), ... = 6, 19, 41, 71, ...
- Other problems involving **setting up and solving equations**

  - This may lead to a pair of **simultaneous equations**

> **Worked Example**
> (a) Find the formula for the *n*<sup>th</sup> term of the sequence 5, 19, 57, 131, 253, 435, ...
> 
> **Answer:**
> 
> > *See if the sequence is linear, quadratic or cubic by finding the first, second or third differences*
> 
> > *The first differences are*
> 
> *14, 38, 74, 122, 182*
> 
> > *These are not constant, so find the second differences*
> 
> *24, 36, 48, 60*
> 
> > *These are not constant, so find the third differences*
> 
> *12, 12, 12*
> 
> > *Compare 5, 19, 57, 131, 253, 435, ... to the cube numbers 1, 8, 27, 64, 125, ...*
> 
> > *Double the cube numbers*
> 
> *2, 16, 54, 128, 250, ...*
> 
> > *Add 3*
> 
> *5, 19, 57, 131, 253, ...*
> 
> > *The cube numbers (with **n*<sup>*th*</sup> *term formula* $n^{3}$*) are doubled then 3 is added*
> 
> **The ****n**<sup>**th**</sup>** term formula is **$2n^{3}+3$
> 
> (b) Find the formula for the *n*<sup>th</sup> term of the sequence 4, 20, 100, 500, 2500, ...
> 
> **Answer:**
> 
> > *Seeing if the first, second or third differences are constant does not work*
> 
> > *The numbers are increasing very fast, suggesting it could be exponential*
> *Check to see if each term is multiplied by the same number each time*
> 
> $4\times5=20,20\times5=100,100\times5=500,500\times5=2500,...$
> 
> > *Each term is multiplied by 5 (the "common ratio") to get the next, so it is exponential*
> *Compare the sequence to the sequence 5*<sup>*n*</sup>
> 
> *Sequence: 4, 20, 100, 500, 2500, ...*
> *5**<sup>*n*</sup>**: 5, 25, 125, 625, 3125, ...*
> 
> > *You need to divide the powers of 5 by 5 and multiply by 4 to get the sequence*
> 
> **Final answer:** **The ****n**<sup>**th**</sup>** term formula is **$\frac{4}{5}\times5^{n}$** or **$4\times5^{n-1}$** **
> 
> (c) Write down the formula for the *n*<sup>th</sup> term of the sequence
> 
> $\frac{5}{4},\frac{19}{20},\frac{57}{100},\frac{131}{500},\frac{253}{2500},...$
> 
> **Answer:**
> 
> > *This sequence is a fraction formed by dividing the sequence in part (a) by the sequence in part (b)*
> *Divide their **n*<sup>*th*</sup> *term formulas*
> 
> **Final answer:** **The ****n**<sup>**th**</sup>** term formula is **$\frac{2n^{3}+3}{4\times5^{n-1}}$

> **Worked Example**
> The first three terms of an exponential sequence are shown below
> 
> $x-12xx^{2}$
> 
> By forming and solving an equation, find the common ratio, $r$, given that  $x\neq0$.
> 
> **Answer:**
> 
> > *As this is an exponential sequence, each term is multiplied by the common ratio,* $r$*, to get the next term*
> 
> > *Consider the first two terms*
> 
> $\begin{gathered} ( x - 1 ) \times r & = 2 x \\ r = \frac{2 x}{x - 1} \end{gathered}$
> 
> > *Considering the next two terms*
> 
> $\begin{gathered} 2 x \times r & = x^{2} \\ r = \frac{x^{2}}{2 x} \end{gathered}$
> 
> > *This is a pair of simultaneous equations*
> *They can be solved by substituting one into the other (replacing* $r$*)*
> 
> $\frac{2x}{x-1}=\frac{x^{2}}{2x}$
> 
> > *Multiply both sides by* $2x$
> 
> $\frac{4x^{2}}{x-1}=x^{2}$
> 
> > *Multiply both sides by* $x-1$*, and expand*
> 
> $4 x^{2} = x^{2} ( x - 1 )
> 4 x^{2} = x^{3} - x^{2}$
> 
> > *Subtract* $4x^{2}$ *from both sides and factorise*
> 
> $0 = x^{3} - 5 x^{2}
> 0 = x^{2} ( x - 5 )$
> 
> > *Solve*
> 
> $\begin{gathered} x^{2} & = 0 \end{gathered}$ *so* $\begin{gathered} x = 0 \end{gathered}$
> *or*
> $\begin{gathered} ( x - 5 ) & = 0 \end{gathered}$ *so* $\begin{gathered} x = 5 \end{gathered}$
> 
> > *You are told* $x\neq0$ *so* $x=5$
> *Substitute this into the original sequence,* $x-1,2x,x^{2}$
> 
> $( 5 - 1 ) , 2 ( 5 ) , 5^{2}
> = 4 , 10 , 25$* *
> 
> > *Find the common ratio* $r$ *(for example, by dividing a term by its previous term)*
> 
> $\frac{10}{4}=2.5$
> 
> **Final answer:** **r ****= 2.5**
