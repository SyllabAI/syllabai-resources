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

- The **general binomial expansion** lets us write `open parentheses 1 plus x close parentheses to the power of n` as a **binomial series**

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

  - `open parentheses 1 plus x close parentheses to the power of n equals 1 plus n x plus fraction numerator n open parentheses n minus 1 close parentheses over denominator 2 factorial end fraction x squared plus... plus fraction numerator n open parentheses n minus 1 close parentheses... open parentheses n minus r plus 1 close parentheses over denominator r factorial end fraction x to the power of r plus... space space space space for space open vertical bar x close vertical bar less than 1 comma space n element of straight rational numbers`
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

- Usually you will be asked to **expand** something **in the form **`open parentheses p plus q x close parentheses to the power of n`
- But the formula **only works** if the constant term is a 1

  - So start by pulling out a **factor** of $p$
  
    - `open parentheses p plus q x close parentheses to the power of n equals open parentheses p open parentheses 1 plus q over p x close parentheses close parentheses to the power of n equals p to the power of n open parentheses 1 plus q over p x close parentheses to the power of n`
  - Then **expand**  `open parentheses 1 plus q over p x close parentheses to the power of n`
  
    - **Substitute** $\frac{q}{p}x$ everywhere that $x$ is in the formula
    - The **interval of convergence** becomes   `open vertical bar p over q x close vertical bar less than 1`
  - Don't forget to **multiply** everything by $p^{n}$ again at the end!
- Be sure you can recognise a **negative** or **fractional** power

  - The expression may be in the **denominator** of a fraction
  
    - `1 over open parentheses p plus q x close parentheses to the power of k equals open parentheses p plus q x close parentheses to the power of negative k end exponent`
  - Or inside a **square root**
  
    - `square root of p plus q x end root equals open parentheses p plus q x close parentheses to the power of 1 half end exponent`
  - Or be written as a **more complex root**
  
    - `m-th root of open parentheses p plus q x close parentheses to the power of k end root equals open parentheses p plus q x close parentheses to the power of k over m end exponent`

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
> `fraction numerator 1 over denominator square root of 9 minus 3 x end root end fraction equals open parentheses 9 minus 3 x close parentheses to the power of negative 1 half end exponent`
> 
> > *Now pull out a factor to make the constant term inside the brackets a 1*
> 
> `table row cell open parentheses 9 minus 3 x close parentheses to the power of negative 1 half end exponent end cell equals cell open parentheses 9 to the power of negative 1 half end exponent close parentheses open parentheses 1 minus 3 over 9 x close parentheses to the power of negative 1 half end exponent end cell row blank equals cell 1 third open parentheses 1 minus x over 3 close parentheses to the power of negative 1 half end exponent end cell end table`
> 
> > *Now use the binomial series formula to expand *`open parentheses 1 minus x over 3 close parentheses to the power of negative 1 half end exponent`
> 
> > *Use *$n=\frac{1}{2}$* and substitute  *$-\frac{x}{3}$* everywhere that *$x$* appears in the formula*
> 
> > `table row cell open parentheses 1 minus x over 3 close parentheses to the power of negative 1 half end exponent end cell equals cell 1 plus open parentheses negative 1 half close parentheses open parentheses negative x over 3 close parentheses plus fraction numerator open parentheses negative 1 half close parentheses open parentheses negative 1 half minus 1 close parentheses over denominator 2 factorial end fraction open parentheses negative x over 3 close parentheses squared plus fraction numerator open parentheses negative 1 half close parentheses open parentheses negative 1 half minus 1 close parentheses open parentheses negative 1 half minus 2 close parentheses over denominator 3 factorial end fraction open parentheses negative x over 3 close parentheses cubed plus... end cell row blank equals cell 1 plus 1 over 6 x plus fraction numerator open parentheses negative 1 half close parentheses open parentheses negative 3 over 2 close parentheses over denominator 2 end fraction open parentheses x squared over 9 close parentheses plus fraction numerator open parentheses negative 1 half close parentheses open parentheses negative 3 over 2 close parentheses open parentheses negative 5 over 2 close parentheses over denominator 6 end fraction open parentheses negative x cubed over 27 close parentheses plus... end cell row blank equals cell 1 plus 1 over 6 x plus fraction numerator open parentheses 3 over 4 close parentheses over denominator 2 end fraction open parentheses x squared over 9 close parentheses plus fraction numerator open parentheses negative 15 over 8 close parentheses over denominator 6 end fraction open parentheses negative x cubed over 27 close parentheses plus... end cell row blank equals cell 1 plus 1 over 6 x plus open parentheses 3 over 8 close parentheses open parentheses x squared over 9 close parentheses plus open parentheses negative 5 over 16 close parentheses open parentheses negative x cubed over 27 close parentheses plus... end cell row blank equals cell 1 plus 1 over 6 x plus 1 over 24 x squared plus 5 over 432 x cubed plus... end cell end table`
> 
> *Now don't forget to multiply by *$\frac{1}{3}$* (factorised out earlier) to get the final answer!*
> 
> `fraction numerator 1 over denominator square root of 9 minus 3 x end root end fraction equals 1 third open parentheses table attributes columnalign right center left columnspacing 0px end attributes row blank blank cell 1 plus 1 over 6 x plus 1 over 24 x squared plus 5 over 432 x cubed plus... end cell end table close parentheses`
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
