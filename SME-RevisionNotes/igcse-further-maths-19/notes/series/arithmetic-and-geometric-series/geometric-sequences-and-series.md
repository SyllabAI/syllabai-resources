---
note_id: "rn_FZpnT8cqx43f5NVT"
title: "Geometric Sequences & Series"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/series/arithmetic-and-geometric-series/geometric-sequences-and-series
path: series/arithmetic-and-geometric-series/geometric-sequences-and-series
updated_at: "2024-10-20T08:03:27.513Z"
spec_point_ids: ["spcpt_b5KzyjnFxRygqtmk", "spcpt_c8RQZfhSvPzK9dGS", "spcpt_DqNff4JYrm6vQjyS"]
spec_point_codes: []
guided_study: false
---

# Geometric Sequences & Series

## Geometric Sequences

> **Spec point** — `spcpt_b5KzyjnFxRygqtmk`

## Geometric Sequences

### What is a geometric sequence?

- In a **geometric sequence**, there is a **common ratio **between consecutive terms in the sequence

  - This means each term is **multiplied** by a common ratio to get the **next term**
- The **first term** of the sequence is denoted by $a$
- The common ratio is denoted by $r$

  - For example, 2, 6, 18, 54, 162, … is a sequence with the rule *‘start at two and multiply each number by three’*
  
    - The **first term, **$a$***,***** **is 2
    - The **common ratio, **$r$**, **is 3
- A geometric sequence can be

  - **increasing **(*r* > 1), or
  - **decreasing **(0 < *r *< 1)
- If the common ratio is a **negative number** the terms will alternate between positive and negative values

  - For example, 1, -4, 16, -64, 256, … is a sequence with the rule *‘start at one and multiply each number by negative four’*
  
    - The **first term, **$a$***,***** **is 1
    - The **common ratio, **$r$**, **is -4
- **Terms** in a geometric sequence can be referred to

  - by the letter $u$* *with
  - a subscript corresponding to its place in the sequence
  
    - e.g.  $u_{1}=a$ is the first term, $u_{9}$ is the ninth term, $u_{n}$ is the $n$<sup>th</sup> term, etc.

## Geometric Series

> **Spec point** — `spcpt_c8RQZfhSvPzK9dGS`

## Geometric Series

### What is a geometric series?

- When the terms of a **geometric sequence** are added together, that is known as a **geometric series**

  - The **terms** (1st term, 2nd term, 3rd term, etc.) are **exactly the same** in the sequence and series
  - But with the series we're most interested in what happens when the terms are **added together**

### How do I find a term in a geometric series?

- The $n^{th}$<sup>*** ***</sup>**term formula** for a geometric series is

$u_{n}=ar^{n-1}$

- Where $a$* *is the **first term**, and $r$ is the **common ratio**
- This is **not **given on the exam **formula sheet**, so make sure you know it
- The formula allows you to find **any term** in the geometric series

  - **Enter** the values of $a$, $r$ and $n$ and calculate the value of $u_{n}$
- Sometimes you will be **given a term** and asked to f**ind **$a$** or **$r$

  - **Substitute** the information you have into the formula and solve the equation
- Sometimes you will be **given two or more consecutive terms** and asked to **find both **$a$** and **$r$

  - Find the **common ratio** by **dividing** a term by the one immediately before it
  
    - $r=\frac{u_{n+1}}{u_{n}}$
  - **Substitute** this and one of the terms into the formula to find the **first term**
- Sometimes you may be **given a term along with **$a$** and **$r$ and asked to **find the value of **$n$

  - You can solve this using **logarithms** on your calculator

### How do I find the sum of a geometric series?

- A **geometric series** is the sum of the terms in a **geometric sequence**

  - For the geometric sequence 2, 6, 18, 54, … the geometric series is 2 + 6 + 18 + 54 + …
- Use the following **formula** to find the sum of the first *n* terms of a geometric series:

$S_{n}=\frac{a(1-r^{n})}{1-r}$

- $a$<sub>* *</sub>is the **first term**
- $r$ is the **common ratio**
- The formula is given on the exam **formula sheet**

  - So you don't need to remember it
  - But you do need to know how to use it!
- If $r>1$ the following **rearrangement** of the formula might be more convenient:

$S_{n}=\frac{a(r^{n}-1)}{r-1}$

- This version is **not** on the formula sheet
- The formula sheet version will always work as well
- A question will often **give you the sum of a certain number of terms** and ask you to **find the values of **$a$**, **$r$** or **$n$

  - **Substitute** the information you have into the formula and solve the equation

> **Exam Hint**
> - The formula for the **sum** of a geometric series is on the exam formula sheet
> 
>   - But the *n*<sup>th</sup> term formula is **not** on the formula sheet
> - You will sometimes need to use logarithms to answer geometric series questions
> 
>   - Make sure you are confident doing this
>   - And know how your calculator handles logarithms

> **Worked Example**
> The sixth term of a geometric series is 486 and the seventh term is 1458.
> 
> Find
> 
> (a) the common ratio of the series
> 
> > *Find the common ratio by dividing a term by the term immediately before it*
> *Here *$r=\frac{7^{\mathrm{th}}\mathrm{term}}{6^{\mathrm{th}}\mathrm{term}}$
> 
> $r=\frac{1458}{486}$
> 
> $r=3$
> 
> (b) the first term of the series.
> 
> > *Use the **n*<sup>*th*</sup>* term formula  *$u_{n}=ar^{n-1}$
> 
> > *For the 6*<sup>*th*</sup>* term, we know  *$u_{6}=486$*,  *$r=3$*  and  *$n=6$
> 
> $\begin{gathered} 486 = a \times 3^{( 6 - 1 )} \\ 486 = a \times 3^{5} \\ 486 = 243 a \\ a = \frac{486}{243} \end{gathered}$
> 
> $a=2$

> **Worked Example**
> The first term of a geometric series is 25, and the common ratio is 0.8.
> 
> Find the value of the fifth term, as well as the sum of the first 5 terms.
> 
> > *To find the fifth term, use the **n*<sup>*th*</sup>* term formula  *$u_{n}=ar^{n-1}$
> *Here  *$n=5$*,  *$a=25$*  and  *$r=0.8$* *
> 
> $\begin{gathered} \frac{1}{5} \text{term} & = 25 \times 0.8^{( 5 - 1 )} \\ = 25 \times 0.8^{4} \end{gathered}$
> 
> > $\mathrm{fifth} \mathrm{term}=10.24$
> 
> *To find the sum of the first 5 terms, use the sum of a geometric series formula  *$S_{n}=\frac{a(1-r^{n})}{1-r}$
> *Again,  *$a=25$*  and  *$r=0.8$* *
> 
> $S_{5} = \frac{25 ( 1 - 0.8^{5} )}{1 - 0.8}$
> 
> > *Use your calculator to work this out  *
> 
> $S_{5}=84.04$

## Sum to Infinity

> **Spec point** — `spcpt_DqNff4JYrm6vQjyS`

## Sum to Infinity

### What is the sum to infinity of a geometric series?

- The **sum to infinity** is the sum of **all the terms** in a geometric series

  - $u_{1}+u_{2}+u_{3}+...$  'all the way to infinity'
- **As **$n$** increases** the terms of a geometric series may

  - move **further away** from zero
  
    - if  $r>1$  or  $r<-1$
  - stay **the same distance away** from zero
  
    - if  $r=1$  or  $r=-1$
  - get **closer and closer** to zero
  
    - if  $-1<r<1$
- If the terms are **getting closer to zero** then the series is said to **converge**

- This means that the **sum of the series** will approach a finite 'limiting value'
- As $n$ increases, the sum of the terms will get **closer and closer** to the limiting value
- The limiting value is the **sum to infinity** of the series

  - It is denoted by $S_{\infty}$

### How do I calculate the sum to infinity?

- First you need to consider the **value of **$r$

  - If  $\left| r \right| < 1$  then the sequence **converges**
  
    - `open vertical bar r close vertical bar less than 1`**  **is the same as   $-1<r<1$
    - In this case the sum to infinity can be calculated
  - If  `open vertical bar r close vertical bar greater or equal than 1`  then the sequence **does not converge**
  
    - `open vertical bar r close vertical bar greater or equal than 1`  is the same as  $r\leq-1$  or  $r\geq1$
    - In this case the sum to infinity cannot be calculated
- If $\vert r \vert < 1$, then the sum **converges** to a finite value given by the formula

`S _ inf = (a)/(1 - r) , _ | r | less than 1`

- $a$ is the **first term**
- $r$ is the **common ratio**
- The formula is given on the exam **formula sheet**

  - So you don't need to remember it
  - But you do need to know how to use it!

> **Exam Hint**
> - Always check the `open vertical bar r close vertical bar less than 1` condition before calculating a sum to infinity
> 
>   - Marks may depend on showing this in your working

> **Worked Example**
> The first three terms of a geometric sequence are  $6,2,\frac{2}{3}$.  Show that the sum to infinity of the series exists, and then find the sum to infinity.
> 
> > *To show the sum to infinity exists we need to know the value of the common ratio *$r$
> 
> > *We can find this by dividing a term by the term immediately before it *
> 
> $r=\frac{2}{6}=\frac{1}{3}$
> 
> > *This satisfies *`open vertical bar r close vertical bar less than 1`*, so the series converges and the sum to infinity exists*
> 
> $\text{stretchy} \mid r \text{stretchy} \mid < 1$*, ***so the series converges**
> 
> > *Now use the sum to infinity formula  *$S_{\infty}=\frac{a}{1-r}$
> 
> > *Here  *$a=6$*  and  *$r=\frac{1}{3}$
> 
> `| S _ inf | = (6)/(1 - 1 third) | | _ = (6)/(( 2 / 3 )) | | _ = 6 x 3 / 2 | |`
> 
> $S_{\infty}=9$
