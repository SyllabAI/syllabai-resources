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

`open parentheses a plus b close parentheses to the power of n equals a to the power of n plus blank open parentheses straight n
1 close parentheses a to the power of n minus 1 space end exponent b space plus blank open parentheses n
2 close parentheses a to the power of n minus 2 space end exponent b squared space plus horizontal ellipsis space plus space open parentheses n
r close parentheses a blank to the power of n minus r end exponent space b blank to the power of r space end exponent plus space horizontal ellipsis space plus space b to the power of n`

- where $n$ is a positive integer and  `open parentheses n
r close parentheses equals fraction numerator n factorial over denominator open parentheses n minus r close parentheses factorial r factorial end fraction`

  - You may also see `open parentheses n
  r close parentheses`  written as `scriptbase straight C subscript r end scriptbase presubscript blank presuperscript n` or `straight C presubscript space n end presubscript subscript r`
- You will usually be asked to find the first three or four terms of an expansion

### What is Pascal’s Triangle?

- Pascal’s triangle is a way of arranging the binomial coefficients and neatly shows how they are formed

  - Each term is formed by adding the two terms above it
  - The first row has just the number 1
  - Each row begins and ends with a number 1
  - From the third row the terms in between the 1s are the sum of the two terms above it

![Pascal's Triangle](../../../assets/c1d5880eaf55-4-1-1-binomial-expansion-notes-diagram-3-1024x86.png)

### How does Pascal’s Triangle relate to the binomial expansion?

- Pascal’s triangle is an alternative way of finding the binomial coefficients, `open parentheses n
r close parentheses`

  - It can be useful for finding for smaller values of $n$ without a calculator
  - However for larger values of $n$ it is slow and prone to arithmetic errors

- Taking the first row as the 0th row, `open parentheses 0
0 close parentheses space equals space 1`, each row corresponds to the $n^{th}$* *row and the term within that row corresponds to the $r^{th}$* *term

  - The first term, which will be a 1, will be the 0th term
- In the non-calculator exam Pascal's triangle can be helpful if you need to get the coefficients of an expansion quickly, provided the value of *n *is not too big

### How do I find the coefficient of a single term?

- Most of the time you will be asked to find the coefficient of a term, rather than carry out the whole expansion
- Use the formula for the general term

`open parentheses n
r close parentheses space a to the power of n minus r end exponent space b to the power of r`

- The question will give you the power of *x* of the term you are looking for

  - Use this to choose which value of *r * you will need to use in the formula
  - This will depend on where the *x *is in the bracket
  - The laws of indices can help you decide which value of *r  *to use:
  
    - For $(a+bx)^{n}$* *to find the coefficient of $x^{r}$* *use $a^{n-r}(bx)^{r}$
    - For $(a+bx^{2})^{n}$ to find the coefficient of $x^{r}$* *use <sup>* *</sup>$a^{n-\frac{r}{2}}(bx^{2})^{\frac{r}{2}}$
    - For $(a+\frac{b}{x})^{n}$ look at how the powers will cancel out to decide which value of $r$ to use
  - So for `open parentheses 3 x blank plus 2 over x close parentheses to the power of 8` to find the coefficient of $x^{2}$ use the term with $r=3$ and to find the constant term use the term with $r=4$
  
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
> > *Substitute values into the formula for (**a** + **b**)*<sup>*n*</sup>*. The question asks for ascending powers of **x**, so start with the constant term, **a*<sup>*n*</sup>*. *`stretchy left parenthesis a plus b stretchy right parenthesis to the power of n equals a to the power of n plus blank open parentheses n
> 1 close parentheses a to the power of n minus 1 space end exponent b space plus blank open parentheses n
> 2 close parentheses a to the power of n minus 2 space end exponent b squared space plus horizontal ellipsis space plus space open parentheses n
> r close parentheses a blank to the power of n minus r end exponent space b blank to the power of r space end exponent plus space horizontal ellipsis space plus space b to the power of n`*.*
> 
> > *Pay attention to the negative term for **b. *
> 
> `table row cell stretchy left parenthesis 3 minus 2 x stretchy right parenthesis to the power of 5 end cell equals cell 3 to the power of 5 plus blank open parentheses 5
> 1 close parentheses stretchy left parenthesis 3 stretchy right parenthesis to the power of 5 minus 1 space end exponent stretchy left parenthesis negative 2 x stretchy right parenthesis space plus blank open parentheses 5
> 2 close parentheses stretchy left parenthesis 3 stretchy right parenthesis to the power of 5 minus 2 space end exponent stretchy left parenthesis negative 2 x stretchy right parenthesis squared space plus horizontal ellipsis space end cell row blank equals cell 243 space plus space stretchy left parenthesis 5 stretchy right parenthesis stretchy left parenthesis 81 stretchy right parenthesis stretchy left parenthesis negative 2 x stretchy right parenthesis space plus space stretchy left parenthesis 10 stretchy right parenthesis stretchy left parenthesis 27 stretchy right parenthesis stretchy left parenthesis 4 x squared stretchy right parenthesis end cell row blank equals cell space 243 space plus space stretchy left parenthesis 405 stretchy right parenthesis stretchy left parenthesis negative 2 x stretchy right parenthesis space plus space 270 stretchy left parenthesis 4 x squared stretchy right parenthesis end cell end table`
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
