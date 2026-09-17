---
note_id: "rn_NkYrY2NgnrdJh3R2"
title: "Inverse Functions"
source: https://www.savemyexams.com/igcse/maths/edexcel/a-modular/24/higher-unit-2/revision-notes/functions-graphs-and-differentiation/functions/inverse-functions
path: functions-graphs-and-differentiation/functions/inverse-functions
updated_at: "2026-01-29T16:06:52.357Z"
spec_point_ids: ["spcpt_TZkZ5ZK4bRYdjnGY"]
spec_point_codes: []
guided_study: false
---

# Inverse Functions

## Inverse Functions

> **Spec point** — `spcpt_TZkZ5ZK4bRYdjnGY`

## Inverse functions

### What is an inverse function?

- An** inverse function **does the** opposite (reverse) operation** of the function it came from

  - E.g. If a function “doubles the number then adds 1”
  - Then its inverse function “subtracts 1, then halves the result”
  
    - The same inverse operations are used when solving an equation or rearranging a formula
- An inverse function performs the **inverse operations** in the **reverse** **order**

### What notation is used for inverse functions?

- The inverse function of `straight f open parentheses x close parentheses` is written as $f^{-1}(x)=\dots$ or  `straight f to the power of negative 1 end exponent colon space x rightwards arrow from bar horizontal ellipsis`

  - For example, if $f(x)=2x+1$
  - The inverse function is $f^{-1}(x)=\frac{x-1}{2}$  or `straight f to the power of negative 1 end exponent colon space x rightwards arrow from bar fraction numerator x minus 1 over denominator 2 end fraction`
- If `straight f open parentheses a close parentheses equals b` then `straight f to the power of negative 1 end exponent open parentheses b close parentheses equals a`

  - For example
  
    - `straight f open parentheses 3 close parentheses equals 2 cross times 3 plus 1 equals 7` (inputting 3 into $f$ gives 7)
    - `straight f to the power of negative 1 end exponent open parentheses 7 close parentheses equals fraction numerator 7 minus 1 over denominator 2 end fraction equals 3`  (inputting 7 into $f^{-1}$ gives back 3)

### How do I find an inverse function algebraically?

- The **process** for finding an inverse function is as follows:

  - **Write** the function as $y=...$
  
    - E.g. The function $f(x)=2x+1$ becomes $y=2x+1$
  - **Swap** the $x$s and $y$s to get $x=\dots$
  
    - E.g. $x=2y+1$
    - The letters change but no terms move
  - **Rearrange **the expression to **make **$y$** the subject **again
  
    - E.g. $x=2y+1$ becomes $x-1=2y$ so $y=\frac{x-1}{2}$
  - **Replace** $y$** **with $f^{-1}(x)=\dots$(or `straight f to the power of negative 1 end exponent colon space x rightwards arrow from bar horizontal ellipsis`)
  
    - E.g. `straight f to the power of negative 1 end exponent open parentheses x close parentheses equals fraction numerator x minus 1 over denominator 2 end fraction`
    - This is the inverse function
    - $y$** should not appear** in the final answer

### How are inverse functions and composite functions related?

- The **composite function** of $f$ followed by $f^{-1}$ (or the other way round) **cancels out**

  - `ff to the power of negative 1 end exponent open parentheses x close parentheses equals straight f to the power of negative 1 end exponent straight f open parentheses x close parentheses equals x`
  
    - If you apply a function to *x*, then apply its inverse function, you get back *x*
    - Whatever happened to *x* gets** undone**
    - f and f<sup>-1</sup>** cancel each other out **when applied together
- For example, solve `straight f to the power of negative 1 end exponent open parentheses x close parentheses equals 5` where `straight f open parentheses x close parentheses equals 2 to the power of x`

  - Finding the inverse function `straight f to the power of negative 1 end exponent open parentheses x close parentheses` algebraically in this case is tricky
  
    - (It is impossible if you haven't studied logarithms!)
  - Instead, you can take $f$ of both sides of `straight f to the power of negative 1 end exponent open parentheses x close parentheses equals 5` and use the fact that $\mathrm{ff}^{-1}$ cancel each other out:
  
    - `table row cell ff to the power of negative 1 end exponent open parentheses x close parentheses end cell equals cell straight f open parentheses 5 close parentheses end cell end table` which cancels to `x equals straight f open parentheses 5 close parentheses` giving $x=2^{5}=32$

### How do I find the domain and range of an inverse function?

- The **domain **of an** inverse function** has exactly the same values as the **range** of the **original function**

  - E.g. If `straight f open parentheses x close parentheses equals fraction numerator 3 over denominator x plus 1 end fraction` has a range of `straight f open parentheses x close parentheses greater than 5`
  
    - then its inverse function, `straight f to the power of negative 1 end exponent open parentheses x close parentheses equals 3 over x minus 1`, has the domain $x>5$
    - Remember to always write domains in terms of $x$
- The** range **of an** inverse function** has exactly the same values as the **domain **of the** original function**

  - E.g. If `straight f open parentheses x close parentheses equals fraction numerator 3 over denominator x plus 1 end fraction` has a domain of $x<-1$
  
    - then its inverse function, `straight f to the power of negative 1 end exponent open parentheses x close parentheses equals 3 over x minus 1`, has the range `straight f to the power of negative 1 end exponent open parentheses x close parentheses less than negative 1`
    - Remember to always write ranges in terms of their function, `straight f to the power of negative 1 end exponent open parentheses x close parentheses`

> **Worked Example**
> A function `straight f open parentheses x close parentheses equals 5 minus 3 x`has the domain $-2<x\leq7$.
> 
> (a) Use algebra to find `straight f to the power of negative 1 end exponent open parentheses x close parentheses`.
> 
> **Answer:**
> 
> > *Write the function in the form *$y=5-3x$* and then swap the *$x$* and *$y$
> 
> $y=5-3x\,x=5-3y$
> 
> > *Rearrange **the expression to make *$y$* the subject again*
> 
> `table row x equals cell 5 minus 3 y end cell row cell space x plus 3 y end cell equals 5 row cell 3 y end cell equals cell 5 minus x end cell row y equals cell fraction numerator 5 minus x over denominator 3 end fraction end cell end table`
> 
> > *Rewrite the answer using inverse function notation*
> 
> $f^{-1}(x)=\frac{5-x}{3}$
> 
> (b) Find the domain of `straight f to the power of negative 1 end exponent open parentheses x close parentheses`.
> 
> **Answer:**
> 
> > *The domain of the inverse function is the range of the original function*
> 
> > *Find the range of *`straight f open parentheses x close parentheses`* by first finding *`straight f open parentheses negative 2 close parentheses`* and *`straight f open parentheses 7 close parentheses`
> 
> `table row cell straight f open parentheses negative 2 close parentheses end cell equals cell 5 minus 3 open parentheses negative 2 close parentheses equals 5 plus 6 equals 11 end cell row cell straight f open parentheses 7 close parentheses end cell equals cell 5 minus 3 open parentheses 7 close parentheses equals 5 minus 21 equals negative 16 end cell end table`
> 
> > *The graph of *$y=5-3x$* is a straight line with a negative gradient*
> *Between **x** = -2 and **x** = 7 the graph decreases from a height of 11 to a height of -16*
> 
> *The range of *`straight f open parentheses x close parentheses`* is *`negative 16 less or equal than straight f open parentheses x close parentheses less than 11`
> 
> *Note that the inequality is "equal to" at x = 7, f(x) = -16*
> (*this is the opposite order of "equal to" in the domain)*
> 
> > *The domain of *`straight f to the power of negative 1 end exponent open parentheses x close parentheses`* takes the same values as range of *`straight f open parentheses x close parentheses`
> *Write down the domain of *`straight f to the power of negative 1 end exponent open parentheses x close parentheses`* *
> *(Remember that domains are always written in terms of *$x$*)*
> 
> $-16\leqx<11$

### How do I find the inverse of a quadratic function?

- You need to rewrite the quadratic expression by **completing the square**

  - E.g. if `straight f open parentheses x close parentheses equals x squared plus 4 x minus 3` then rewrite it as `straight f open parentheses x close parentheses equals open parentheses x plus 2 close parentheses squared minus 7`
- Follow the **same process** to find the inverse

  - E.g. `y equals open parentheses x plus 2 close parentheses squared minus 7`
  
    - Swap: `x equals open parentheses y plus 2 close parentheses squared minus 7`
    - Rearrange: $y=-2\pm\sqrt{x+7}$
- Use the **domain of the quadratic function** to decide whether to use the plus or minus root

  - The domain of the quadratic is the range of the inverse
  - E.g. suppose the domain of `straight f open parentheses x close parentheses` is $x\leq-2$
  
    - Then `straight f to the power of negative 1 end exponent open parentheses x close parentheses equals negative 2 minus square root of x plus 7 end root`
  - E.g. suppose the domain `straight f open parentheses x close parentheses` is $x\geq-2$
  
    - Then `straight f to the power of negative 1 end exponent open parentheses x close parentheses equals negative 2 plus square root of x plus 7 end root`

> **Worked Example**
> Let `straight f colon x rightwards arrow from bar 2 x squared minus 12 x plus 1` for $x\geq3$
> 
> (a) Express the inverse function $f^{-1}$ in the form `straight f to the power of negative 1 end exponent colon x rightwards arrow from bar...`
> 
> **Answer**:
> 
> > *Complete the square for the quadratic expression*
> 
> `2 open parentheses x squared minus 6 x close parentheses plus 1
> 2 open square brackets open parentheses x minus 3 close parentheses squared minus 9 close square brackets plus 1
> 2 open parentheses x minus 3 close parentheses squared minus 18 plus 1
> 2 open parentheses x minus 3 close parentheses squared minus 17`
> 
> > *Set the function equal to *$y$* and then swap *$x$* and *$y$
> 
> `y equals 2 open parentheses x minus 3 close parentheses squared minus 17
> x equals 2 open parentheses y minus 3 close parentheses squared minus 17`
> 
> > *Rearrange to make *$y$* the subject*
> 
> `table row cell open parentheses y minus 3 close parentheses squared end cell equals cell fraction numerator x plus 17 over denominator 2 end fraction end cell row cell y minus 3 end cell equals cell plus-or-minus square root of fraction numerator x plus 17 over denominator 2 end fraction end root end cell row y equals cell 3 plus-or-minus square root of fraction numerator x plus 17 over denominator 2 end fraction end root end cell end table`
> 
> > *The domain of the quadratic function is the range of the inverse*
> 
> - *Therefore *$y\geq3$
> - *Take the positive root*
> 
> > *Write in the required format*
> 
> `straight f to the power of negative 1 end exponent colon x rightwards arrow from bar 3 plus square root of fraction numerator x plus 17 over denominator 2 end fraction end root`
> 
> (b) State the domain of $f^{-1}$
> 
> **Answer**:
> 
> > *Find the range of *$f$
> 
> *When *$x\geq3$*, *`open parentheses x minus 3 close parentheses squared greater or equal than 0`* so *`2 open parentheses x minus 3 close parentheses squared minus 17 greater or equal than negative 17`
> 
> `straight f open parentheses x close parentheses greater or equal than negative 17`
> 
> > *The range of a function is the domain of its inverse*
> 
> - *Write the domain in terms of *$x$
> 
> $x\geq-17$
