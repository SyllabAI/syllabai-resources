---
note_id: "rn_4p2Z4pDwxgDD9QQ5"
title: "Combinations of Series"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/series/series/combinations-of-series
path: series/series/combinations-of-series
updated_at: "2024-04-10T09:42:27.278Z"
spec_point_ids: ["spcpt_43RTm6JtZxvK7VS3"]
spec_point_codes: []
guided_study: false
---

# Combinations of Series

## Combinations of Series

> **Spec point** — `spcpt_43RTm6JtZxvK7VS3`

## Combinations of Series

### How do I find combinations of series?

- Use the **three formulae**:

  - $\sum_{r = 1}^{n} r = 1 \frac{1}{2} n ( n + 1 )$
  - $\sum_{r = 1}^{n} r^{2} = \frac{1}{6} n ( n + 1 ) ( 2 n + 1 )$
  - $\sum_{r = 1}^{n} r^{3} = 1 \frac{1}{4} n^{2} ( n + 1 )^{2}$
- **Coefficients **of $r$, $r^{2}$ and $r^{3}$ can come out of the sum

  - $\sum_{r = 1}^{n} ( a r^{3} + b r^{2} + c r + d ) = a \sum_{r = 1}^{n} r^{3} + b \sum_{r = 1}^{n} r^{2} + c \sum_{r = 1}^{n} r + d n$
  
    - **Constants **are **multiplied** by $n$
  - You may have to **expand** expressions in $r$
  
    - $\sum_{r = 1}^{n} ( r + 3 ) ( r + 4 ) = \sum_{r = 1}^{n} ( r^{2} + 7 r + 12 )$
- It is often possible to **factorise final** **answers**, in particular taking out:

  - fractional coefficients
  - $n$
  - $( n + 1 )$
- You may be required to write series as the **difference of two sums**

  - $\sum_{r=5}^{10} r= \sum_{r=1}^{10} r− \sum_{r=1}^{4} r$

> **Exam Hint**
> Exam questions often refer to these three formulae as the "standard summation formulae".

> **Worked Example**
> (a)  Using standard summation formulae, show that
> 
> $\sum_{r = 1}^{n} ( r - 1 ) r ( r + 1 ) = 1 \frac{1}{4} ( n - 1 ) n ( n + 1 ) ( n + 2 )$
> 
> > *Expand and simplify the left-hand side*
> 
> $\begin{gathered} ( r - 1 ) r ( r + 1 ) & = r ( r^{2} - 1 ) \\ = r^{3} - r \end{gathered}$
> 
> > *Substitute in the formulae* $\sum_{r = 1}^{n} r^{3} = 1 \frac{1}{4} n^{2} ( n + 1 )^{2}$ *and* $\sum_{r = 1}^{n} r = 1 \frac{1}{2} n ( n + 1 )$
> 
> $\begin{gathered} \sum_{r = 1}^{n} ( r^{3} - r ) & = \sum_{r = 1}^{n} r^{3} - \sum_{r = 1}^{n} r \\ = 1 \frac{1}{4} n^{2} ( n + 1 )^{2} - 1 \frac{1}{2} n ( n + 1 ) \end{gathered}$* *
> 
> > *Factorise out the quarter,* $n$ *and* $( n + 1 )$ *then simplify*
> 
> $\begin{gathered} \sum_{r = 1}^{n} ( r^{3} - r ) & = 1 \frac{1}{4} n ( n + 1 ) [ n ( n + 1 ) - 2 ] \\ = 1 \frac{1}{4} n ( n + 1 ) ( n^{2} + n - 2 ) \end{gathered}$
> 
> > *Factorise the quadratic on the right-hand side*
> 
> $\begin{gathered} \sum_{r = 1}^{n} ( r^{3} - r ) & = = 1 \frac{1}{4} n ( n + 1 ) ( n + 2 ) ( n - 1 ) \\ \end{gathered}$
> 
> > *Rearrange into the form asked for by the question*
> 
> $\begin{gathered} \sum_{r = 1}^{n} ( r - 1 ) r ( r + 1 ) & = 1 \frac{1}{4} ( n - 1 ) n ( n + 1 ) ( n + 2 ) \end{gathered}$
> 
> (b)  Hence find the value of
> 
> $0\times1\times2+1\times2\times3+2\times3\times4+...+20\times21\times22$
> 
> > *It helps to write out the first few terms in the series* $\begin{gathered} \sum_{r = 1}^{n} ( r - 1 ) r ( r + 1 ) \end{gathered}$
> 
> $\begin{gathered} ( 1 - 1 ) \times 1 \times ( 1 + 1 ) + ( 2 - 1 ) \times 2 \times ( 2 + 1 ) + ( 3 - 1 ) \times 3 \times ( 3 + 1 ) +... \\ = 0 \times 1 \times 2 + 1 \times 2 \times 3 + 2 \times 3 \times 4 +... \end{gathered}$
> 
> > *The question stops at 20 x 21 x 22*
> *This is actually the 21*<sup>*st*</sup>*term (not the 20*<sup>*th*</sup> *term)*
> *To find the sum of the first 21 terms, substitute* $n=21$ *into part (a)*
> 
> $\begin{gathered} \sum_{r = 1}^{21} ( r - 1 ) r ( r + 1 ) & = 1 \frac{1}{4} ( 21 - 1 ) \times 21 \times ( 21 + 1 ) ( 21 + 2 ) \\ = 1 \frac{1}{4} \times 20 \times 21 \times 22 \times 23 \end{gathered}$
> 
> **Final answer:** **53130**
> 
> (c)  If $\sum_{r = 1}^{n} ( r - 1 ) r ( r + 1 ) = 10 \sum_{r = 1}^{n} r^{2}$, find $n$.
> 
> > *Substitute the answer from part (a) into the left-hand side*
> *Substitute the standard formula* $\sum_{r = 1}^{n} r^{2} = \frac{1}{6} n ( n + 1 ) ( 2 n + 1 )$ *into the right-hand side*
> 
> $\begin{gathered} 1 \frac{1}{4} ( n - 1 ) n ( n + 1 ) ( n + 2 ) & = 10 \times \frac{1}{6} n ( n + 1 ) ( 2 n + 1 ) \end{gathered}$* *
> 
> > *Cancel the terms* $n$ *and* $( n + 1 )$ *from both sides*
> *It also helps to multiply both sides by 12 to remove fractions*
> 
> $3 \begin{gathered} ( n - 1 ) ( n + 2 ) \end{gathered} \begin{gathered} = \end{gathered} \begin{gathered} 20 \end{gathered} \begin{gathered} ( 2 n + 1 ) \end{gathered}$
> 
> > *Expand, then form and solve a quadratic in* `equation`
> 
> $\begin{gathered} 3 ( n^{2} + n - 2 ) & = 40 n + 20 \\ 3 n^{2} - 37 n - 26 & = 0 \\ ( 3 n + 2 ) ( n - 13 ) & = 0 \\ n = - \frac{2}{3} \text{or} n = 13 \end{gathered}$
> 
> > $n$ *must be a positive integer (as it is used in sigma notation,* `SUM_ r = 1 to n of`*)*
> 
> $n=13$
