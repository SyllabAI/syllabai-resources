---
note_id: "rn_CsZKPc9xv4ZdybMg"
title: "Binomial Expansion"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/series/binomial-series/binomial-expansion
path: series/binomial-series/binomial-expansion
updated_at: "2024-10-20T08:04:32.843Z"
spec_point_ids: ["spcpt_3hw656HdGSpfGzT2"]
spec_point_codes: []
guided_study: false
---

# Binomial Expansion

## Binomial Expansion

> **Spec point** — `spcpt_3hw656HdGSpfGzT2`

## Binomial Expansion

### What is the Binomial Expansion?

- The **binomial expansion **gives a method for expanding a **two-term** expression in a bracket raised to a power

  - For example  $( a + b )^{n}$
  - You may also see it referred to as the binomial theorem
  - In this note $n$ will be a **positive integer**
  
    - See the 'General Binomial Expansion' revision note for the general case
- To **expand** a bracket with a two-term expression in it:

  - Determine what $a$* *and $b$ are for your example
  - Then use the **formula** **for the binomial expansion**
  
    - $( a + b )^{n = a^{n} + ( \begin{gathered} n \\ 1 \end{gathered} ) a^{n} - 1 } b + \ldots + ( \begin{gathered} n \\ r \end{gathered} ) a^{n - r} b^{r} + \ldots + b^{n}$
  - $( \begin{gathered} n \\ r \end{gathered} )$  in the formula is known as the **binomial coefficient**
  
    - $( \begin{gathered} n \\ r \end{gathered} ) = \frac{n factorial}{r \text{factorial} ( n - r ) factorial} = \frac{n ( n - 1 )... ( n - r + 1 )}{r factorial}$
    - $n!$ ("$n$ factorial") is defined by $n!=1\times2\times3\times...\timesn$
    - You may also see $( \begin{gathered} n \\ r \end{gathered} )$  written as `C _ r _ _ ^ n`
    - Your **calculator** should be able to calculate $( \begin{gathered} n \\ r \end{gathered} )$ for you
    - Or you can use **Pascal's triangle** (see the next section)
- To get **all the terms**

  - **Start** with $r=0$
  - Then use  $r=1$, $r=2$,...  **until **you get up to** **$r=n$
  - So there will always be $n+1$ **terms** in the full expansion
- This version of the binomial expansion formula is **not** on the exam **formula sheet**

  - But it is a special case of the Binomial Series formula for $( 1 + x )^{n}$ which is on the formula sheet
  - See the 'General Binomial Expansion' revision note
- When expanding something like $( p + q x )^{n}$ you may only be asked to find the **first few terms** of an expansion

  - Check whether the question wants **ascending** or **descending **powers of *x*
  
    - For **ascending **powers start with the constant term, $p^{n}$
    - For **descending **powers start with the term with $x$*,* $( q x )^{n}$
    - Choosing $a$ and $b$ appropriately will make it easier to follow the formula above
- If you are **not writing the full expansion** you can either

  - show that the series continues by putting an **ellipsis** (…) after your final term
  - or show that the terms you have found are an **approximation** of the full series by using the 'approximately equals' sign (≈)

### Finding binomial coefficients using Pascal's triangle

- **Pascal’s triangle** is a way of arranging (and finding!) the binomial coefficients

  - The **first row** has just the number 1
  - Each row **begins and ends** **with a 1**
  - Starting in the **third row**
  
    - Each other terms is the **sum** of the two terms immediately above it

![Pascal's Triangle](../../../assets/c1d5880eaf55-4-1-1-binomial-expansion-notes-diagram-3-1024x86.png)

- Pascal’s triangle is an alternative way of finding the **binomial coefficients** $( \begin{gathered} n \\ r \end{gathered} )$  (also written `C _ r _ _ ^ n` )

  - It can be useful for finding the values of the coefficients without a calculator
  
    - Most useful for smaller values of $n$
    - For larger values of $n$ it is slow and prone to arithmetic errors

- Taking the first row as corresponding to $n=0$,

  - each row gives the binomial coefficient values for the corresponding value of $n$
  - within a row the values run from $r=0$ to $r=n$
  - e.g. from the 6<sup>th</sup> row of the table ($n=5$):
  
    - $( a + b )^{5} = a^{5} + 5 a^{4} b + 10 a^{3} b^{2} + 10 a^{2} b^{3} + 5 a b^{4} + b^{5}$

### How do I find the coefficient of a single term?

- You may just be asked to find the **coefficient of a single term**, rather than the whole expansion
- Use the formula for the **general term**

  - $( \begin{gathered} n \\ r \end{gathered} ) a^{n - r} b^{r}$

- To find a **particular power of **$x$** term** in an expansion

  - Choose which **value of **$r$* * you will need to use in the formula
  - The **laws of indices** can help you decide which value of $r$*  *to use:
  
    - For $(p+qx)^{n}$,*  *to find the coefficient of $x^{2}$* *let  $a=p,b=qx$ and use $r=2$
    - For $(p+qx^{2})^{n}$,  to find the coefficient of $x^{2}$* *let  $a=p,b=qx^{2}$ and use $r=1$
    - For something like $( p x + \frac{q}{x} )^{n}$, you need to consider how the powers will cancel each other
    
      - `equation`E.g. for $( p x + \frac{q}{x} )^{6}$ , to find the coefficient of $x^{2}$ let $a=px,b=\frac{q}{x}$ and user $r=2$
      - Because then $x^{n - r} ( \frac{1}{x} )^{r = x^{6} - 2 } ( \frac{1}{x} )^{2 } = x^{4} ( \frac{1}{x^{2}} ) = x^{2}$
    - There are a lot of variations, so **practice** is better than trying to memorise formulae for $r$!
- If you know the **coefficient** of a particular term, you can use it to find an **unknown** in the brackets

  - Use the **laws of indices** to choose the correct term
  - Then use the **general term** formula to form and solve an equation

> **Exam Hint**
> - Binomial expansion questions can get messy
> 
>   - Use separate lines to keep your working clear
>   - And always put terms in brackets

> **Worked Example**
> Using the binomial expansion, find the complete expansion of  $( x + y )^{4}$.
> 
> > *Use the formula with* $a=x$*,* $b=y$ *and* $n=4$
> $r$ *will run from 0 to 4, so there will be 5 terms*
> 
> $( x + y )^{4} = ( \begin{gathered} 4 \\ 0 \end{gathered} ) x^{4} + ( \begin{gathered} 4 \\ 1 \end{gathered} ) x^{3} y + ( \begin{gathered} 4 \\ 2 \end{gathered} ) x^{2} y^{2} + ( \begin{gathered} 4 \\ 3 \end{gathered} ) x y^{3} + ( \begin{gathered} 4 \\ 4 \end{gathered} ) y^{4}$
> 
> > *Now just work out the values of the binomial coefficients*
> *You can use the formula, your calculator or Pascal's triangle*
> 
> > *Note that* $( \begin{gathered} 4 \\ 0 \end{gathered} ) = ( \begin{gathered} 4 \\ 4 \end{gathered} ) = 1$
> *That's why we usually don't bother writing the binomial coefficients for the first and last terms of an expansion!*
> 
> > $(x+y)^{4}=x^{4}+4x^{3}y+6x^{2}y^{2}+4xy^{3}+y^{4}$* *

> **Worked Example**
> Find the first three terms, in ascending powers of $x$, in the expansion of $(3-2x)^{5}$.
> 
> > *For ascending powers of* $x$ *we want to start with the constant term*
> 
> > *So we want to use the formula with* $a=3$*,* $b=-2x$*, and* $n=5$
> 
> > *For the first three terms (constant term,* $x$ *term  and* $x^{2}$ *term) we want* $r$ *from 0 to 2*
> 
> > *Substitute those values into the formula*
> 
> $( 3 - 2 x )^{5} = ( 3 )^{5} + ( \begin{gathered} 5 \\ 1 \end{gathered} ) ( 3 )^{4} ( - 2 x ) + ( \begin{gathered} 5 \\ 2 \end{gathered} ) ( 3 )^{3} ( - 2 x )^{2} +...$
> 
> > *Find the value of the binomial coefficients and bring the powers inside the brackets*
> *Be careful with the minus signs!*
> 
> > * *$( 3 - 2 x )^{5} = 243 + ( 5 ) ( 81 ) ( - 2 x ) + ( 10 ) ( 27 ) ( 4 x^{2} ) +...$
> 
> > *Expand the remaining brackets and write down the final answer*
> 
> $(3-2x)^{5}=243-810x+1080x^{2}+...$
