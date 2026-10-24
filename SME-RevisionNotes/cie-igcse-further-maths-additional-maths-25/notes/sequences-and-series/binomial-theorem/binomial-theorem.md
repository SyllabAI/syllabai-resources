---
note_id: "rn_277Qgfb6dxbykZ48"
title: "Binomial Theorem"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/sequences-and-series/binomial-theorem/binomial-theorem
path: sequences-and-series/binomial-theorem/binomial-theorem
updated_at: "2026-07-02T08:19:38.512Z"
spec_point_ids: ["spcpt_pwBvmphGXzWcW2xh", "spcpt_Rzg2QGvB2x64zyTp"]
spec_point_codes: []
guided_study: false
---

# Binomial Theorem

## Binomial Expansion

> **Spec point** — `spcpt_pwBvmphGXzWcW2xh`

## Binomial expansion

### What is the Binomial Expansion?

- The **binomial theorem (**also known as the binomial expansion) gives a method for expanding a **two-term** expression in a bracket raised to a power
- To expand a bracket with a two-term expression in:

  - First choose the most appropriate parts of the expression to assign to *a *and *b*
  - Then use the formula for the binomial theorem:

`( a + b ) ^ n = a ^ n + _ ( n 1 ) a ^ n - 1 b + _ ( n 2 ) a ^ n - 2 b ^2 + horizontal ellipsis + ( n r ) a _ ^ n - r b _ ^ r + horizontal ellipsis + b ^ n`

- where $n$ is a positive integer and  $( n
r ) = \frac{n factorial}{( n - r ) \text{factorial} r factorial}$

  - You may also see $( n
 r )$  written as `C _ r _ _ ^ n` or `C _ n _ r`
- You will usually be asked to find the first three or four terms of an expansion

### What is Pascal’s Triangle?

- Pascal’s triangle is a way of arranging the binomial coefficients and neatly shows how they are formed

  - Each term is formed by adding the two terms above it
  - The first row has just the number 1
  - Each row begins and ends with a number 1
  - From the third row the terms in between the 1s are the sum of the two terms above it

![Pascal's Triangle](../../../assets/c1d5880eaf55-4-1-1-binomial-expansion-notes-diagram-3-1024x86.png)

### How does Pascal’s Triangle relate to the binomial expansion?

- Pascal’s triangle is an alternative way of finding the binomial coefficients, $( n
r )$

  - It can be useful for finding for smaller values of $n$ without a calculator
  - However for larger values of $n$ it is slow and prone to arithmetic errors

- Taking the first row as the 0th row, $( 0
0 ) = 1$, each row corresponds to the $n^{th}$* *row and the term within that row corresponds to the $r^{th}$* *term

  - The first term, which will be a 1, will be the 0th term
- In the non-calculator exam Pascal's triangle can be helpful if you need to get the coefficients of an expansion quickly, provided the value of *n *is not too big

### How do I find the coefficient of a single term?

- Most of the time you will be asked to find the coefficient of a term, rather than carry out the whole expansion
- Use the formula for the general term

$( n
r ) a^{n - r} b^{r}$

- The question will give you the power of *x* of the term you are looking for

  - Use this to choose which value of *r * you will need to use in the formula
  - This will depend on where the *x *is in the bracket
  - The laws of indices can help you decide which value of *r  *to use:
  
    - For $(a+bx)^{n}$* *to find the coefficient of $x^{r}$* *use $a^{n-r}(bx)^{r}$
    - For $(a+bx^{2})^{n}$ to find the coefficient of $x^{r}$* *use <sup>* *</sup>$a^{n-\frac{r}{2}}(bx^{2})^{\frac{r}{2}}$
    - For $(a+\frac{b}{x})^{n}$ look at how the powers will cancel out to decide which value of $r$ to use
  - So for $( 3 x + \frac{2}{x} )^{8}$ to find the coefficient of $x^{2}$ use the term with $r=3$ and to find the constant term use the term with $r=4$
  
    - There are a lot of variations of this so it is usually easier to see this by inspection of the powers
- You may also be given the coefficient of a particular term and asked to find an unknown in the brackets

  - Use the laws of indices to choose the correct term and then use the binomial theorem formula to form and solve and equation

> **Exam Hint**
> - Binomial expansion questions can get messy, use separate lines to keep your working clear and always put terms in brackets

> **Worked Example**
> Find the first three terms in the expansion of $(3-2x)^{5}$, in ascending powers of $x$. Simplify the coefficient of each term.
> 
> > *Identify the values of **a**,** b **and** n.*
> 
> $a=3,b=-2x,n=5$
> 
> > *Substitute values into the formula for (**a** + **b**)*<sup>*n*</sup>*. The question asks for ascending powers of **x**, so start with the constant term, **a*<sup>*n*</sup>*. *`stretchy ( a + b stretchy ) ^ n = a ^ n + _ ( n > 1 ) a ^ n - 1 b + _ ( n > 2 ) a ^ n - 2 b ^2 + horizontal ellipsis + ( n > r ) a _ ^ n - r b _ ^ r + horizontal ellipsis + b ^ n`*.*
> 
> > *Pay attention to the negative term for **b. *
> 
> $\begin{gathered} ( 3 - 2 x )^{5} & = 3^{5} + ( 5
> 1 ) ( 3 )^{5 - 1 } ( - 2 x ) + ( 5
> 2 ) ( 3 )^{5 - 2 } ( - 2 x )^{2} + \text{horizontal} \text{ellipsis} \\ = 243 + ( 5 ) ( 81 ) ( - 2 x ) + ( 10 ) ( 27 ) ( 4 x^{2} ) \\ = 243 + ( 405 ) ( - 2 x ) + 270 ( 4 x^{2} ) \end{gathered}$
> 
> $(3-2x)^{5}=243-810x+1080x^{2}+...$

## Applications of Binomial Expansion

> **Spec point** — `spcpt_Rzg2QGvB2x64zyTp`

## Applications of binomial expansion

### What are binomial expansions used for?

- Binomial expansions are used to expand brackets

  - Normally in the form (a + b)<sup>n</sup>
- You will most likely be asked to find the first few terms
- Look out for whether you should give your answer in **ascending** or **descending **powers of *x*

  - For **ascending **powers start with the constant term, *a*<sup>*n*</sup>
  - For **descending **powers start with the term with *x *in
  
    - You may wish to swap *a* and *b* over so that you can follow the general formula given in the formula book
- If you are not writing the full expansion you can either

  - show that the sequence continues by putting an ellipsis (…) after your final term
  - or show that the terms you have found are an approximation of the full sequence by using the sign for approximately equals to (≈) ** ** ![The Binomial Expansion can be used to find the first few terms of an expansion](assets/bd9d9b335124-4-1-1-binomial-expansion-notes-diagram-6.png)

- You may be asked to find the coefficient of a particular term

** **

![The Binomial Expansion can be used to find the coefficient of a particular term](../../../assets/7a9cc7086d6c-4-1-1-binomial-expansion-notes-diagram-7.png)

- You may be asked to solve a problem to find an unknown

![Settin up and solving equations with the binomial expansion](../../../assets/fb3551b19d99-4-1-1-binomial-expansion-notes-diagram-8.png)
