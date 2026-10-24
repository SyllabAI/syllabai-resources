---
note_id: "rn_ncFNDyPfbMRFdmZW"
title: "General Binomial Expansion"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/series/binomial-series/general-binomial-expansion
path: series/binomial-series/general-binomial-expansion
updated_at: "2024-10-20T08:06:05.125Z"
spec_point_ids: ["spcpt_SgDCdWKMBvfBRt2R"]
spec_point_codes: []
guided_study: false
---

# General Binomial Expansion

## General Binomial Expansion

> **Spec point** — `spcpt_SgDCdWKMBvfBRt2R`

## General Binomial Expansion

### What is the general binomial expansion?

- The **general binomial expansion** lets us write $( 1 + x )^{n}$ as a **binomial series**

  - It is valid for **any **$n\inℚ$
  
    - $ℚ$ is the set of all **rational numbers**
    - So $n$ can be **negative** or a **fraction**
  - If $n$ is a **positive integer**
  
    - Then the series has a **finite** number of terms
    - For this case see the '**Binomial Expansion**' revision note

- If $n\inℚ$ is **not a positive integer**

  - Then the series has an infinite number of terms
  - I.e. 'it goes on forever'
  - An exam question will only ask for the first few terms of the expansion

- A general binomial expansion is found using the binomial series **formula**

  - $( 1 + x )^{n} = 1 + n x + \frac{n ( n - 1 )}{2 factorial} x^{2} +... + \frac{n ( n - 1 )... ( n - r + 1 )}{r factorial} x^{r} +... \text{for} \left| x \right| < 1 , n \in \mathbb{Q}$
  - This formula is on the exam **formula sheet**
  
    - So you don't need to **remember** it
    - But you do need to know how to **use** it
- The expansion is only **valid** for `open vertical bar x close vertical bar less than 1`

  - This means $-1<x<1$
  - This is known as the **interval of convergence**
  - For values of $x$ **inside** the interval of convergence
  
    - the (infinite) expansion on the right-hand side of the formula
    - is **exactly equal** to the function on the left-hand side

### How do I use the binomial series formula?

- Usually you will be asked to **expand** something **in the form **$( p + q x )^{n}$
- But the formula **only works** if the constant term is a 1

  - So start by pulling out a **factor** of $p$
  
    - $( p + q x )^{n} = ( p ( 1 + \frac{q}{p} x ) )^{n} = p^{n} ( 1 + \frac{q}{p} x )^{n}$
  - Then **expand**  $( 1 + \frac{q}{p} x )^{n}$
  
    - **Substitute** $\frac{q}{p}x$ everywhere that $x$ is in the formula
    - The **interval of convergence** becomes   `open vertical bar p over q x close vertical bar less than 1`
  - Don't forget to **multiply** everything by $p^{n}$ again at the end!
- Be sure you can recognise a **negative** or **fractional** power

  - The expression may be in the **denominator** of a fraction
  
    - $\frac{1}{( p + q x )^{k = ( p + q x )^{-k}} }$
  - Or inside a **square root**
  
    - $\sqrt{p + q x} = ( p + q x )^{1 \frac{1}{2}}$
  - Or be written as a **more complex root**
  
    - $\sqrt[m]{ ( p + q x ) ^{k}} = ( p + q x ) ^{\frac{k}{m}}$

> **Exam Hint**
> - Remember the formula is on the formula sheet
> - Be especially careful with
> 
>   - negative numbers
>   - subtracting 1 from fractions
> - Use brackets to separate things out
> - Don't rush!

> **Worked Example**
> (a) Expand  $\frac{1}{\sqrt{9-3x}}$  in ascending powers of $x$ up to and including the term in $x^{3}$ and simplifying each term as far as possible.
> 
> > *Start by rewriting using laws of indices*
> 
> $\frac{1}{ \sqrt{9 - 3 x} } = ( 9 - 3 x )^{- 1 \frac{1}{2}}$
> 
> > *Now pull out a factor to make the constant term inside the brackets a 1*
> 
> $\begin{gathered} ( 9 - 3 x )^{- 1 \frac{1}{2}} & = ( 9^{- 1 \frac{1}{2}} ) ( 1 - \frac{3}{9} x )^{- 1 \frac{1}{2}} \\ = 1 \frac{1}{3} ( 1 - \frac{x}{3} )^{- 1 \frac{1}{2}} \end{gathered}$
> 
> > *Now use the binomial series formula to expand *$( 1 - \frac{x}{3} )^{- 1 \frac{1}{2}}$
> 
> > *Use *$n=\frac{1}{2}$* and substitute  *$-\frac{x}{3}$* everywhere that *$x$* appears in the formula*
> 
> > `| ( 1 - x / 3 ) ^ - 1 half | = 1 + ( - 1 half ) ( - x / 3 ) + (( - 1 half ) ( - 1 half - 1 ))/(2 factorial) ( - x / 3 ) ^2 + (( - 1 half ) ( - 1 half - 1 ) ( - 1 half - 2 ))/(3 factorial) ( - x / 3 ) ^3 +... | | _ = 1 + 1 / 6 x + (( - 1 half ) ( - 3 / 2 ))/(2) ( x ^2 / 9 ) + (( - 1 half ) ( - 3 / 2 ) ( - 5 / 2 ))/(6) ( - x ^3 / 27 ) +... | | _ = 1 + 1 / 6 x + (( 3 / 4 ))/(2) ( x ^2 / 9 ) + (( - 15 / 8 ))/(6) ( - x ^3 / 27 ) +... | | _ = 1 + 1 / 6 x + ( 3 / 8 ) ( x ^2 / 9 ) + ( - 5 / 16 ) ( - x ^3 / 27 ) +... | | _ = 1 + 1 / 6 x + 1 / 24 x ^2 + 5 / 432 x ^3 +... | |`
> 
> *Now don't forget to multiply by *$\frac{1}{3}$* (factorised out earlier) to get the final answer!*
> 
> $\frac{1}{ \sqrt{9 - 3 x} } = 1 \frac{1}{3} ( \begin{array}{rcl} 1 + \frac{1}{6} x + \frac{1}{24} x^{2} + \frac{5}{432} x^{3} +... \end{array} )$
> 
> $\frac{1}{\sqrt{9-3x}}=\frac{1}{3}+\frac{1}{18}x+\frac{1}{72}x^{2}+\frac{5}{1296}x^{3}+...$
> 
> (b) Find the interval of convergence for the expansion in part (a).
> 
> > *Remember that we used  *$-\frac{x}{3}$* in place of *$x$* when we used the binomial series formula*
> 
> > *We also need to substitute  *$-\frac{x}{3}$* into the standard convergence interval  *`open vertical bar x close vertical bar less than 1`
> 
> `open vertical bar negative x over 3 close vertical bar less than 1
> 1 third open vertical bar x close vertical bar less than 1
> minus 1 less than 1 third x less than 1`
> 
> $-3<x<3$
