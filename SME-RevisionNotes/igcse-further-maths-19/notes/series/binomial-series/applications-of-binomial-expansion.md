---
note_id: "rn_JGSF7RD8MhMR45S9"
title: "Applications of Binomial Expansion"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/series/binomial-series/applications-of-binomial-expansion
path: series/binomial-series/applications-of-binomial-expansion
updated_at: "2024-10-20T08:07:34.937Z"
spec_point_ids: ["spcpt_mpQWyYQ6pCmyzryn"]
spec_point_codes: []
guided_study: false
---

# Applications of Binomial Expansion

## Applications of Binomial Expansion

> **Spec point** — `spcpt_mpQWyYQ6pCmyzryn`

## Applications of Binomial Expansion

### How can I use the binomial expansion with more complex expressions?

- You may be asked to find a **series expansion** for an expression like  $\frac{1+x}{3+2x}$

  - Rewrite as a **product**,  $\frac{1 + x}{3 + 2 x} = ( 1 + x ) ( 3 + 2 x )^{- 1}$

- Find the **binomial expansion** of  $( 3 + 2 x )^{- 1}$

$( 3 + 2 x )^{- 1} = 1 \frac{1}{3} - \frac{2}{9} x + \frac{4}{27} x^{2} - \frac{8}{81} x^{3} +...$

- Note this has only been expanded up to the $x^{3}$ **term**
- **Multiply **that expansion by** **$( 1 + x )$ and simplify

**            **$\begin{gathered} ( 1 + x ) ( 3 + 2 x )^{- 1} & = ( 1 + x ) ( 1 \frac{1}{3} - \frac{2}{9} x + \frac{4}{27} x^{2} - \frac{8}{81} x^{3} +... ) \\ = 1 \frac{1}{3} - \frac{2}{9} x + \frac{4}{27} x^{2} - \frac{8}{81} x^{3} + 1 \frac{1}{3} x - \frac{2}{9} x^{2} + \frac{4}{27} x 3 - \frac{8}{81} x^{4} +... \\ = 1 \frac{1}{3} + \frac{1}{9} x - \frac{2}{27} x^{2} + \frac{4}{81} x^{3} - \frac{8}{81} x^{4} +... \\ = 1 \frac{1}{3} + \frac{1}{9} x - \frac{2}{27} x^{2} + \frac{4}{81} x^{3} -... \end{gathered}$

- This is only **valid** up to the $x^{3}$ term
- To get **more terms** we would have to start with more terms for $( 3 + 2 x )^{- 1}$
- $-\frac{8}{81}x^{4}$ is **not** the correct $x^{4}$ term for $\begin{gathered} ( 1 + x ) ( 3 + 2 x )^{- 1} \end{gathered}$ as there are more $x^{4}$ terms that were not found
- Use the **same process** to find the expansion for something like  $\frac{1-2x}{\sqrt{2+3x}}$

  - Rewrite as a **product**,  $\frac{1 - 2 x}{ \sqrt{2 + 3 x} } = ( 1 - 2 x ) ( 2 + 3 x )^{- 1 \frac{1}{2}}$
  - Find the** binomial expansion** of  $( 2 + 3 x )^{- 1 \frac{1}{2}}$
  - **Multiply** the expansion by $( 1 - 2 x )$ and simplify

### How can I use the binomial expansion to estimate a value?

- The binomial expansion can be used to find **estimates **or** approximations**

  - When `open vertical bar x close vertical bar less than 1`, higher powers of $x$* *will be **very small**
  - So even the **first 3 or 4 terms** of an expansion can form a good approximation
  - The **more terms used** the **closer** the approximation will be to the true value
  
    - Also the **closer to zero** $x$is, the **better** the approximation will be
- For example, find an **approximation** for $\sqrt{0.96}$ using the expansion of $( 1 - x )^{1 \frac{1}{2}}$

  - **Compare** the value you are approximating to the expression being expanded
  
    - $(1-x)^{\frac{1}{2}}=0.96^{\frac{1}{2}}$
  - Find the **value of **$x$* *to use by solving the appropriate equation
  
    - $\begin{array}{rcl} \\ 1 - x & = 0.96 \\ x & = 0.04 \end{array}$

- **Substitute** this value of $x$ into the binomial expansion of $( 1 - x )^{1 \frac{1}{2}}$

  - $( 1 - x )^{1 \frac{1}{2}} = 1 - 1 \frac{1}{2} x - \frac{1}{8} x^{2} -...$
  - So $\sqrt{0.96} \approx 1 - 1 \frac{1}{2} ( 0.04 ) - \frac{1}{8} ( 0.04 )^{2} = 0.9798$
  - The true value of $\sqrt{0.96}$ is  $0.97979589...$
- On the exam this is often used to approximate **square roots**

  - It can also be used to approximate **other things**
  - For example approximate the **fraction** $\frac{8}{125}$ using the binomial expansion of $\frac{1}{( 3 - x )^{3}}$
  
    - $\frac{1}{( 3 - x )^{3}} = \frac{8}{125} \Leftrightarrow \frac{1}{3 - x} = \frac{2}{5} \Leftrightarrow x = 0.5$
    - So substitute $x=0.5$ into the expansion
- Always check that the value of $x$ is within the **interval of convergence **for the expansion

  - If $x$ is **outside** the interval of convergence then the approximation is **not reliable**

### How can I use the binomial expansion with calculus?

- A complete binomial expansion is **exactly equal** to the function it represents

- This means that it is valid to **differentiate** or **integrate** a binomial expansion

  - These will always be **powers of** $x$** **derivatives or integrals

- For example, the function  $\mathrm{f} ( x ) = \frac{1 + x}{3 + 2 x}$

  - We saw above that  $\begin{gathered} \frac{1 + x}{3 + 2 x} & = 1 \frac{1}{3} + \frac{1}{9} x - \frac{2}{27} x^{2} + \frac{4}{81} x^{3} -... \end{gathered}$
  - We can **differentiate **that:
  
    - $\mathrm{f}^{'} ( x ) = \frac{1}{9} - \frac{4}{27} x + \frac{4}{27} x^{2} -...$
  - Or **integrate** it
  
    - $\int \mathrm{f} ( x ) \mathrm{d} x = \int \begin{gathered} ( 1 \frac{1}{3} + \frac{1}{9} x - \frac{2}{27} x^{2} + \frac{4}{81} x^{3} -... ) \end{gathered} \mathrm{d} x = 1 \frac{1}{3} x + \frac{1}{18} x^{2} - \frac{2}{81} x^{3} + \frac{1}{81} x^{4} -... + c$
- This can be used to find **estimates** or **approximations**

  - For example to estimate $\int_{0}^{0.5} \frac{1 + x}{3 + 2 x} d x$
  - **Integrate** the binomial expansion (as we just did above)
  
    - $\int_{0}^{0.5} \frac{1 + x}{3 + 2 x} d x \approx [ 1 \frac{1}{3} x + \frac{1}{18} x^{2} - \frac{2}{81} x^{3} + \frac{1}{81} x^{4} ]_{0}^{0.5} = \frac{77}{432} = 0.178240...$
    - The true value of the integral is 0.178079...
- Always check that any values of $x$ you use are within the **interval of convergence **for the expansion

  - This includes the **integration limits** if you are approximating a definite integral
  - If any $x$ values are **outside** the interval of convergence then the approximation is **not reliable**

### How can I find the percentage error of an approximation?

- Use the following formula

  - $\text{percentage} \text{error} = ( \frac{v_{E} - v_{A} }{v_{E} } ) \times 100 \%$
  
    - $ν_{E}$  is the **exact value**
    - $ν_{A}$ is the **approximated value**
  - The exact value **must** be in the denominator!
- Percentage errors are usually given as **positive** values

  - If the formula gives you a **negative** value, you can just remove the minus sign
  - But you will usually get the marks for a correct **positive** or **negative** answer

> **Exam Hint**
> - When substituting values of $x$ into a binomial expansion
> 
>   - Always make sure they are within the interval of convergence
>   - If they are not then you may have made a mistake earlier in the question

> **Worked Example**
> The binomial expansion of  $\frac{1}{\sqrt{9-3x}}$ is $\frac{1}{3}+\frac{1}{18}x+\frac{1}{72}x^{2}+...$, with interval of convergence  $-3<x<3$.
> 
> (a) Use the expansion to estimate the value of $\frac{1}{\sqrt{10}}$, giving your answer as a fraction.
> 
> > *Find the value of* $x$*you need to use*
> 
> $\begin{gathered} \frac{1}{ \sqrt{9 - 3 x} } & = \frac{1}{ \sqrt{10} } \\ 9 - 3 x & = 10 \\ 3 x & = - 1 \\ x = - 1 \frac{1}{3} \end{gathered}$
> 
> > *That is within the interval of convergence* $-3<x<3$*, so we can use it to find approximation*
> 
> > *Substitute it into the expansion*
> 
> $\frac{1}{ \sqrt{10} } \approx 1 \frac{1}{3} + \frac{1}{18} ( - 1 \frac{1}{3} ) + \frac{1}{72} ( - 1 \frac{1}{3} )^{2} = 1 \frac{1}{3} - \frac{1}{54} + \frac{1}{648} = \frac{205}{648}$
> 
> $\frac{1}{\sqrt{10}}\approx\frac{205}{648}$
> 
> (b) Find the percentage error, to 3 decimal places, of your approximation from the actual value.
> 
> > *Use* $\text{percentage} \text{error} = ( \frac{v_{E} - v_{A} }{v_{E} } ) \times 100 \%$
> 
> > *Make sure the exact value is in the denominator!*
> 
> $\text{percentage} \text{error} = ( \frac{\frac{1}{ \sqrt{10} } - \frac{205}{648} }{\frac{1}{ \sqrt{10} }} ) \times 100 = - 0.041191...$
> 
> > *That is negative because the approximated value is greater than the exact value*
> 
> > *Percentage errors are usually given as positive numbers, so remove the minus sign*
> 
> > *Round to 3 decimal places*
> 
> $0 . 041 \% \text{begin} \text{style} \text{stretchy} ( 3 d. p. \text{stretchy} )$
