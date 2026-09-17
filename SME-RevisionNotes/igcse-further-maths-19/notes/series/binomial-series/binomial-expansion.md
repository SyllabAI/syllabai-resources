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

  - For example  `open parentheses a plus b close parentheses to the power of n`
  - You may also see it referred to as the binomial theorem
  - In this note $n$ will be a **positive integer**
  
    - See the 'General Binomial Expansion' revision note for the general case
- To **expand** a bracket with a two-term expression in it:

  - Determine what $a$* *and $b$ are for your example
  - Then use the **formula** **for the binomial expansion**
  
    - `open parentheses a plus b close parentheses to the power of n space equals space a to the power of n space plus space open parentheses table row n row 1 end table close parentheses space a to the power of n minus 1 space end exponent b space plus space horizontal ellipsis space plus space open parentheses table row n row r end table close parentheses space a to the power of n minus r end exponent b to the power of r space plus space horizontal ellipsis space plus space b to the power of n`
  - `open parentheses table row n row r end table close parentheses`  in the formula is known as the **binomial coefficient**
  
    - `open parentheses table row n row r end table close parentheses space equals space fraction numerator n factorial over denominator r factorial open parentheses n minus r close parentheses factorial end fraction space equals space fraction numerator n open parentheses n minus 1 close parentheses... open parentheses n minus r plus 1 close parentheses over denominator r factorial end fraction`
    - $n!$ ("$n$ factorial") is defined by $n!=1\times2\times3\times...\timesn$
    - You may also see `open parentheses table row n row r end table close parentheses`  written as `scriptbase straight C subscript r end scriptbase presubscript blank presuperscript n`
    - Your **calculator** should be able to calculate `open parentheses table row n row r end table close parentheses` for you
    - Or you can use **Pascal's triangle** (see the next section)
- To get **all the terms**

  - **Start** with $r=0$
  - Then use  $r=1$, $r=2$,...  **until **you get up to** **$r=n$
  - So there will always be $n+1$ **terms** in the full expansion
- This version of the binomial expansion formula is **not** on the exam **formula sheet**

  - But it is a special case of the Binomial Series formula for `open parentheses 1 plus x close parentheses to the power of n` which is on the formula sheet
  - See the 'General Binomial Expansion' revision note
- When expanding something like `open parentheses p plus q x close parentheses to the power of n` you may only be asked to find the **first few terms** of an expansion

  - Check whether the question wants **ascending** or **descending **powers of *x*
  
    - For **ascending **powers start with the constant term, $p^{n}$
    - For **descending **powers start with the term with $x$*, *`open parentheses q x close parentheses to the power of n`
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

- Pascal’s triangle is an alternative way of finding the **binomial coefficients** `open parentheses table row n row r end table close parentheses`  (also written `scriptbase straight C subscript r end scriptbase presubscript blank presuperscript n` )

  - It can be useful for finding the values of the coefficients without a calculator
  
    - Most useful for smaller values of $n$
    - For larger values of $n$ it is slow and prone to arithmetic errors

- Taking the first row as corresponding to $n=0$,

  - each row gives the binomial coefficient values for the corresponding value of $n$
  - within a row the values run from $r=0$ to $r=n$
  - e.g. from the 6<sup>th</sup> row of the table ($n=5$):
  
    - `open parentheses a plus b close parentheses to the power of 5 equals a to the power of 5 plus bold 5 a to the power of 4 b plus bold 10 a cubed b squared plus bold 10 a squared b cubed plus bold 5 a b to the power of 4 plus b to the power of 5`

### How do I find the coefficient of a single term?

- You may just be asked to find the **coefficient of a single term**, rather than the whole expansion
- Use the formula for the **general term**

  - `open parentheses table row n row r end table close parentheses space a to the power of n minus r end exponent space b to the power of r`

- To find a **particular power of **$x$** term** in an expansion

  - Choose which **value of **$r$* * you will need to use in the formula
  - The **laws of indices** can help you decide which value of $r$*  *to use:
  
    - For $(p+qx)^{n}$,*  *to find the coefficient of $x^{2}$* *let  $a=p,b=qx$ and use $r=2$
    - For $(p+qx^{2})^{n}$,  to find the coefficient of $x^{2}$* *let  $a=p,b=qx^{2}$ and use $r=1$
    - For something like `open parentheses p x plus q over x close parentheses to the power of n`, you need to consider how the powers will cancel each other
    
      - `equation`E.g. for `open parentheses p x plus q over x close parentheses to the power of 6` , to find the coefficient of $x^{2}$ let $a=px,b=\frac{q}{x}$ and user $r=2$
      - Because then `x to the power of n minus r end exponent space open parentheses 1 over x close parentheses to the power of r equals x to the power of 6 minus 2 space end exponent open parentheses 1 over x close parentheses to the power of 2 space end exponent equals x to the power of 4 open parentheses 1 over x squared close parentheses equals x squared
      space space`
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
> Using the binomial expansion, find the complete expansion of  `open parentheses x plus y close parentheses to the power of 4`.
> 
> > *Use the formula with *$a=x$*, *$b=y$* and *$n=4$
> $r$* will run from 0 to 4, so there will be 5 terms*
> 
> `open parentheses x plus y close parentheses to the power of 4 equals open parentheses table row 4 row 0 end table close parentheses x to the power of 4 plus open parentheses table row 4 row 1 end table close parentheses x cubed y plus open parentheses table row 4 row 2 end table close parentheses x squared y squared plus open parentheses table row 4 row 3 end table close parentheses x y cubed plus open parentheses table row 4 row 4 end table close parentheses y to the power of 4`
> 
> > *Now just work out the values of the binomial coefficients*
> *You can use the formula, your calculator or Pascal's triangle*
> 
> > *Note that  *`open parentheses table row 4 row 0 end table close parentheses equals open parentheses table row 4 row 4 end table close parentheses equals 1`
> *That's why we usually don't bother writing the binomial coefficients for the first and last terms of an expansion!*
> 
> > $(x+y)^{4}=x^{4}+4x^{3}y+6x^{2}y^{2}+4xy^{3}+y^{4}$* *

> **Worked Example**
> Find the first three terms, in ascending powers of $x$, in the expansion of $(3-2x)^{5}$.
> 
> > *For ascending powers of *$x$* we want to start with the constant term*
> 
> > *So we want to use the formula with *$a=3$*, *$b=-2x$*, and *$n=5$
> 
> > *For the first three terms (constant term, *$x$* term  and *$x^{2}$* term) we want *$r$* from 0 to 2*
> 
> > *Substitute those values into the formula*
> 
> `open parentheses 3 minus 2 x close parentheses to the power of 5 equals open parentheses 3 close parentheses to the power of 5 plus open parentheses table row 5 row 1 end table close parentheses open parentheses 3 close parentheses to the power of 4 open parentheses negative 2 x close parentheses plus open parentheses table row 5 row 2 end table close parentheses open parentheses 3 close parentheses cubed open parentheses negative 2 x close parentheses squared plus...`
> 
> > *Find the value of the binomial coefficients and bring the powers inside the brackets*
> *Be careful with the minus signs!*
> 
> > * *`open parentheses 3 minus 2 x close parentheses to the power of 5 equals 243 plus open parentheses 5 close parentheses open parentheses 81 close parentheses open parentheses negative 2 x close parentheses plus open parentheses 10 close parentheses open parentheses 27 close parentheses open parentheses 4 x squared close parentheses plus...`
> 
> > *Expand the remaining brackets and write down the final answer*
> 
> $(3-2x)^{5}=243-810x+1080x^{2}+...$
