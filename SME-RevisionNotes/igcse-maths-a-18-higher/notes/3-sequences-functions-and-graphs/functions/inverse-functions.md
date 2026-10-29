---
note_id: "rn_NkYrY2NgnrdJh3R2"
title: "Inverse Functions"
source: https://www.savemyexams.com/igcse/maths/edexcel/a/18/higher/revision-notes/3-sequences-functions-and-graphs/functions/inverse-functions
path: 3-sequences-functions-and-graphs/functions/inverse-functions
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

- The inverse function of $\mathrm{f} ( x )$ is written as $f^{-1}(x)=\dots$ or  `f ^ - 1 colon x ->from bar …`

  - For example, if $f(x)=2x+1$
  - The inverse function is $f^{-1}(x)=\frac{x-1}{2}$  or $\mathrm{f}^{- 1} : x \rightarrow \text{from} \text{bar} \frac{x - 1}{2}$
- If $\mathrm{f} ( a ) = b$ then $\mathrm{f}^{- 1} ( b ) = a$

  - For example
  
    - $\mathrm{f} ( 3 ) = 2 \times 3 + 1 = 7$ (inputting 3 into $f$ gives 7)
    - $\mathrm{f}^{- 1} ( 7 ) = \frac{7 - 1}{2} = 3$  (inputting 7 into $f^{-1}$ gives back 3)

### How do I find an inverse function algebraically?

- The **process** for finding an inverse function is as follows:

  - **Write** the function as $y=...$
  
    - E.g. The function $f(x)=2x+1$ becomes $y=2x+1$
  - **Swap** the $x$s and $y$s to get $x=\dots$
  
    - E.g. $x=2y+1$
    - The letters change but no terms move
  - **Rearrange **the expression to **make **$y$** the subject **again
  
    - E.g. $x=2y+1$ becomes $x-1=2y$ so $y=\frac{x-1}{2}$
  - **Replace** $y$** **with $f^{-1}(x)=\dots$(or `f ^ - 1 colon x ->from bar …`)
  
    - E.g. $\mathrm{f}^{- 1} ( x ) = \frac{x - 1}{2}$
    - This is the inverse function
    - $y$** should not appear** in the final answer

### How are inverse functions and composite functions related?

- The **composite function** of $f$ followed by $f^{-1}$ (or the other way round) **cancels out**

  - $ff^{- 1} ( x ) = \mathrm{f}^{- 1} \mathrm{f} ( x ) = x$
  
    - If you apply a function to *x*, then apply its inverse function, you get back *x*
    - Whatever happened to *x* gets** undone**
    - f and f<sup>-1</sup>** cancel each other out **when applied together
- For example, solve $\mathrm{f}^{- 1} ( x ) = 5$ where $\mathrm{f} ( x ) = 2^{x}$

  - Finding the inverse function $\mathrm{f}^{- 1} ( x )$ algebraically in this case is tricky
  
    - (It is impossible if you haven't studied logarithms!)
  - Instead, you can take $f$ of both sides of $\mathrm{f}^{- 1} ( x ) = 5$ and use the fact that $\mathrm{ff}^{-1}$ cancel each other out:
  
    - $\begin{gathered} ff^{- 1} ( x ) & = \mathrm{f} ( 5 ) \end{gathered}$ which cancels to $x = \mathrm{f} ( 5 )$ giving $x=2^{5}=32$

### How do I find the domain and range of an inverse function?

- The **domain **of an** inverse function** has exactly the same values as the **range** of the **original function**

  - E.g. If $\mathrm{f} ( x ) = \frac{3}{x + 1}$ has a range of $\mathrm{f} ( x ) > 5$
  
    - then its inverse function, $\mathrm{f}^{- 1} ( x ) = \frac{3}{x} - 1$, has the domain $x>5$
    - Remember to always write domains in terms of $x$
- The** range **of an** inverse function** has exactly the same values as the **domain **of the** original function**

  - E.g. If $\mathrm{f} ( x ) = \frac{3}{x + 1}$ has a domain of $x<-1$
  
    - then its inverse function, $\mathrm{f}^{- 1} ( x ) = \frac{3}{x} - 1$, has the range $\mathrm{f}^{- 1} ( x ) < - 1$
    - Remember to always write ranges in terms of their function, $\mathrm{f}^{- 1} ( x )$

> **Worked Example**
> A function $\mathrm{f} ( x ) = 5 - 3 x$has the domain $-2<x\leq7$.
> 
> (a) Use algebra to find $\mathrm{f}^{- 1} ( x )$.
> 
> **Answer:**
> 
> > *Write the function in the form* $y=5-3x$ *and then swap the* $x$ *and* $y$
> 
> $y=5-3x\,x=5-3y$
> 
> > *Rearrange **the expression to make *$y$ *the subject again*
> 
> $\begin{gathered} x = 5 - 3 y \\ x + 3 y & = 5 \\ 3 y & = 5 - x \\ y = \frac{5 - x}{3} \end{gathered}$
> 
> > *Rewrite the answer using inverse function notation*
> 
> $f^{-1}(x)=\frac{5-x}{3}$
> 
> (b) Find the domain of $\mathrm{f}^{- 1} ( x )$.
> 
> **Answer:**
> 
> > *The domain of the inverse function is the range of the original function*
> 
> > *Find the range of* $\mathrm{f} ( x )$ *by first finding* $\mathrm{f} ( - 2 )$ *and* $\mathrm{f} ( 7 )$
> 
> $\begin{gathered} \mathrm{f} ( - 2 ) & = 5 - 3 ( - 2 ) = 5 + 6 = 11 \\ \mathrm{f} ( 7 ) & = 5 - 3 ( 7 ) = 5 - 21 = - 16 \end{gathered}$
> 
> > *The graph of* $y=5-3x$ *is a straight line with a negative gradient*
> *Between **x** = -2 and **x** = 7 the graph decreases from a height of 11 to a height of -16*
> 
> *The range of* $\mathrm{f} ( x )$ *is* $- 16 \le \mathrm{f} ( x ) < 11$
> 
> *Note that the inequality is "equal to" at x = 7, f(x) = -16*
> (*this is the opposite order of "equal to" in the domain)*
> 
> > *The domain of* $\mathrm{f}^{- 1} ( x )$ *takes the same values as range of* $\mathrm{f} ( x )$
> *Write down the domain of* $\mathrm{f}^{- 1} ( x )$* *
> *(Remember that domains are always written in terms of* $x$*)*
> 
> $-16\leqx<11$

### How do I find the inverse of a quadratic function?

- You need to rewrite the quadratic expression by **completing the square**

  - E.g. if $\mathrm{f} ( x ) = x^{2} + 4 x - 3$ then rewrite it as $\mathrm{f} ( x ) = ( x + 2 )^{2} - 7$
- Follow the **same process** to find the inverse

  - E.g. $y = ( x + 2 )^{2} - 7$
  
    - Swap: $x = ( y + 2 )^{2} - 7$
    - Rearrange: $y=-2\pm\sqrt{x+7}$
- Use the **domain of the quadratic function** to decide whether to use the plus or minus root

  - The domain of the quadratic is the range of the inverse
  - E.g. suppose the domain of $\mathrm{f} ( x )$ is $x\leq-2$
  
    - Then $\mathrm{f}^{- 1} ( x ) = - 2 - \sqrt{x + 7}$
  - E.g. suppose the domain $\mathrm{f} ( x )$ is $x\geq-2$
  
    - Then $\mathrm{f}^{- 1} ( x ) = - 2 + \sqrt{x + 7}$

> **Worked Example**
> Let $\mathrm{f} : x \rightarrow \text{from} \text{bar} 2 x^{2} - 12 x + 1$ for $x\geq3$
> 
> (a) Express the inverse function $f^{-1}$ in the form $\mathrm{f}^{- 1} : x \rightarrow \text{from} bar...$
> 
> **Answer**:
> 
> > *Complete the square for the quadratic expression*
> 
> $2 ( x^{2} - 6 x ) + 1
> 2 [ ( x - 3 )^{2} - 9 ] + 1
> 2 ( x - 3 )^{2} - 18 + 1
> 2 ( x - 3 )^{2} - 17$
> 
> > *Set the function equal to* $y$ *and then swap* $x$ *and* $y$
> 
> $y = 2 ( x - 3 )^{2} - 17
> x = 2 ( y - 3 )^{2} - 17$
> 
> > *Rearrange to make* $y$ *the subject*
> 
> $\begin{gathered} ( y - 3 )^{2} & = \frac{x + 17}{2} \\ y - 3 & = \pm \sqrt{ \frac{x + 17}{2} } \\ y = 3 \pm \sqrt{ \frac{x + 17}{2} } \end{gathered}$
> 
> > *The domain of the quadratic function is the range of the inverse*
> 
> - *Therefore* $y\geq3$
> - *Take the positive root*
> 
> > *Write in the required format*
> 
> $\mathrm{f}^{- 1} : x \rightarrow \text{from} \text{bar} 3 + \sqrt{ \frac{x + 17}{2} }$
> 
> (b) State the domain of $f^{-1}$
> 
> **Answer**:
> 
> > *Find the range of* $f$
> 
> *When* $x\geq3$*,* $( x - 3 ) ^{2} \ge 0$ *so* $2 ( x - 3 ) ^{2} - 17 \ge - 17$
> 
> $\mathrm{f} ( x ) \ge - 17$
> 
> > *The range of a function is the domain of its inverse*
> 
> - *Write the domain in terms of* $x$
> 
> $x\geq-17$
