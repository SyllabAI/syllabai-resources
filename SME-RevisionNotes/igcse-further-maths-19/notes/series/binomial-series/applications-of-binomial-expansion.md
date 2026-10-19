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

  - Rewrite as a **product**,  `fraction numerator 1 plus x over denominator 3 plus 2 x end fraction equals open parentheses 1 plus x close parentheses open parentheses 3 plus 2 x close parentheses to the power of negative 1 end exponent`

- Find the **binomial expansion** of  `open parentheses 3 plus 2 x close parentheses to the power of negative 1 end exponent`

`open parentheses 3 plus 2 x close parentheses to the power of negative 1 end exponent equals 1 third minus 2 over 9 x plus 4 over 27 x squared minus 8 over 81 x cubed plus...`

- Note this has only been expanded up to the $x^{3}$ **term**
- **Multiply **that expansion by** **`open parentheses 1 plus x close parentheses` and simplify

**            **`table row cell open parentheses 1 plus x close parentheses open parentheses 3 plus 2 x close parentheses to the power of negative 1 end exponent end cell equals cell open parentheses 1 plus x close parentheses open parentheses 1 third minus 2 over 9 x plus 4 over 27 x squared minus 8 over 81 x cubed plus... close parentheses end cell row blank equals cell 1 third minus 2 over 9 x plus 4 over 27 x squared minus 8 over 81 x cubed plus 1 third x minus 2 over 9 x squared plus 4 over 27 x 3 minus 8 over 81 x to the power of 4 plus... end cell row blank equals cell 1 third plus 1 over 9 x minus 2 over 27 x squared plus 4 over 81 x cubed minus 8 over 81 x to the power of 4 plus... end cell row blank equals cell 1 third plus 1 over 9 x minus 2 over 27 x squared plus 4 over 81 x cubed minus... end cell end table`

- This is only **valid** up to the $x^{3}$ term
- To get **more terms** we would have to start with more terms for `open parentheses 3 plus 2 x close parentheses to the power of negative 1 end exponent`
- $-\frac{8}{81}x^{4}$ is **not** the correct $x^{4}$ term for `table row blank blank cell open parentheses 1 plus x close parentheses open parentheses 3 plus 2 x close parentheses to the power of negative 1 end exponent end cell end table` as there are more $x^{4}$ terms that were not found
- Use the **same process** to find the expansion for something like  $\frac{1-2x}{\sqrt{2+3x}}$

  - Rewrite as a **product**,  `fraction numerator 1 minus 2 x over denominator square root of 2 plus 3 x end root end fraction equals open parentheses 1 minus 2 x close parentheses open parentheses 2 plus 3 x close parentheses to the power of negative 1 half end exponent`
  - Find the** binomial expansion** of  `open parentheses 2 plus 3 x close parentheses to the power of negative 1 half end exponent`
  - **Multiply** the expansion by `open parentheses 1 minus 2 x close parentheses` and simplify

### How can I use the binomial expansion to estimate a value?

- The binomial expansion can be used to find **estimates **or** approximations**

  - When `open vertical bar x close vertical bar less than 1`, higher powers of $x$* *will be **very small**
  - So even the **first 3 or 4 terms** of an expansion can form a good approximation
  - The **more terms used** the **closer** the approximation will be to the true value
  
    - Also the **closer to zero** $x$is, the **better** the approximation will be
- For example, find an **approximation** for $\sqrt{0.96}$ using the expansion of `open parentheses 1 minus x close parentheses to the power of 1 half end exponent`

  - **Compare** the value you are approximating to the expression being expanded
  
    - $(1-x)^{\frac{1}{2}}=0.96^{\frac{1}{2}}$
  - Find the **value of **$x$* *to use by solving the appropriate equation
  
    - `table attributes columnalign right center left columnspacing 0px end attributes row blank blank blank row cell 1 space minus space x space end cell equals cell space 0.96 end cell row cell space x space end cell equals cell space 0.04 end cell end table`

- **Substitute** this value of $x$ into the binomial expansion of `open parentheses 1 minus x close parentheses to the power of 1 half end exponent`

  - `open parentheses 1 minus x close parentheses to the power of 1 half end exponent equals 1 minus 1 half x minus 1 over 8 x squared minus...`
  - So `square root of 0.96 end root almost equal to 1 minus 1 half open parentheses 0.04 close parentheses minus 1 over 8 blank open parentheses 0.04 close parentheses squared equals 0.9798`
  - The true value of $\sqrt{0.96}$ is  $0.97979589...$
- On the exam this is often used to approximate **square roots**

  - It can also be used to approximate **other things**
  - For example approximate the **fraction** $\frac{8}{125}$ using the binomial expansion of `1 over open parentheses 3 minus x close parentheses cubed`
  
    - `1 over open parentheses 3 minus x close parentheses cubed equals 8 over 125 space space space rightwards double arrow space space space fraction numerator 1 over denominator 3 minus x end fraction equals 2 over 5 space space space rightwards double arrow space space space x equals 0.5`
    - So substitute $x=0.5$ into the expansion
- Always check that the value of $x$ is within the **interval of convergence **for the expansion

  - If $x$ is **outside** the interval of convergence then the approximation is **not reliable**

### How can I use the binomial expansion with calculus?

- A complete binomial expansion is **exactly equal** to the function it represents

- This means that it is valid to **differentiate** or **integrate** a binomial expansion

  - These will always be **powers of** $x$** **derivatives or integrals

- For example, the function  `straight f open parentheses x close parentheses equals fraction numerator 1 plus x over denominator 3 plus 2 x end fraction`

  - We saw above that  `table row cell fraction numerator 1 plus x over denominator 3 plus 2 x end fraction end cell equals cell 1 third plus 1 over 9 x minus 2 over 27 x squared plus 4 over 81 x cubed minus... end cell end table`
  - We can **differentiate **that:
  
    - `straight f to the power of apostrophe open parentheses x close parentheses equals 1 over 9 minus 4 over 27 x plus 4 over 27 x squared minus...`
  - Or **integrate** it
  
    - `integral straight f open parentheses x close parentheses space straight d x space equals space integral table row blank blank cell open parentheses 1 third plus 1 over 9 x minus 2 over 27 x squared plus 4 over 81 x cubed minus... close parentheses end cell end table space straight d x space equals 1 third x plus 1 over 18 x squared minus 2 over 81 x cubed plus 1 over 81 x to the power of 4 minus... plus c`
- This can be used to find **estimates** or **approximations**

  - For example to estimate `integral subscript 0 superscript 0.5 end superscript space fraction numerator 1 plus x over denominator 3 plus 2 x end fraction d x`
  - **Integrate** the binomial expansion (as we just did above)
  
    - `integral subscript 0 superscript 0.5 end superscript space fraction numerator 1 plus x over denominator 3 plus 2 x end fraction d x almost equal to open square brackets 1 third x plus 1 over 18 x squared minus 2 over 81 x cubed plus 1 over 81 x to the power of 4 close square brackets subscript 0 superscript 0.5 end superscript equals 77 over 432 equals 0.178240...`
    - The true value of the integral is 0.178079...
- Always check that any values of $x$ you use are within the **interval of convergence **for the expansion

  - This includes the **integration limits** if you are approximating a definite integral
  - If any $x$ values are **outside** the interval of convergence then the approximation is **not reliable**

### How can I find the percentage error of an approximation?

- Use the following formula

  - `percentage space error equals open parentheses fraction numerator v subscript E minus v subscript A over denominator v subscript E end fraction close parentheses cross times 100 percent sign`
  
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
> > *Find the value of *$x$*you need to use*
> 
> `table row cell fraction numerator 1 over denominator square root of 9 minus 3 x end root end fraction end cell equals cell fraction numerator 1 over denominator square root of 10 end fraction end cell row cell 9 minus 3 x end cell equals 10 row cell 3 x end cell equals cell negative 1 end cell row x equals cell negative 1 third end cell end table`
> 
> > *That is within the interval of convergence  *$-3<x<3$*, so we can use it to find approximation*
> 
> > *Substitute it into the expansion*
> 
> `fraction numerator 1 over denominator square root of 10 end fraction almost equal to 1 third plus 1 over 18 open parentheses negative 1 third close parentheses plus 1 over 72 open parentheses negative 1 third close parentheses squared equals 1 third minus 1 over 54 plus 1 over 648 equals 205 over 648`
> 
> $\frac{1}{\sqrt{10}}\approx\frac{205}{648}$
> 
> (b) Find the percentage error, to 3 decimal places, of your approximation from the actual value.
> 
> > *Use  *`percentage space error equals open parentheses fraction numerator v subscript E minus v subscript A over denominator v subscript E end fraction close parentheses cross times 100 percent sign`
> 
> > *Make sure the exact value is in the denominator!*
> 
> `percentage space error equals open parentheses fraction numerator begin display style fraction numerator 1 over denominator square root of 10 end fraction end style minus begin display style 205 over 648 end style over denominator begin display style fraction numerator 1 over denominator square root of 10 end fraction end style end fraction close parentheses cross times 100 equals negative 0.041191...`
> 
> > *That is negative because the approximated value is greater than the exact value*
> 
> > *Percentage errors are usually given as positive numbers, so remove the minus sign*
> 
> > *Round to 3 decimal places*
> 
> `bold 0 bold. bold 041 bold percent sign bold space begin bold style stretchy left parenthesis 3 space d. p. stretchy right parenthesis end style`
