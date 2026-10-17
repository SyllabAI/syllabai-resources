---
note_id: "rn_9FDb37nSVHprWVZ3"
title: "Definite Integrals"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/calculus/integration/definite-integrals
path: calculus/integration/definite-integrals
updated_at: "2026-07-02T08:19:38.534Z"
spec_point_ids: ["spcpt_D8yXJgjNvHXZ9KQk"]
spec_point_codes: []
guided_study: false
---

# Definite Integrals

## Definite Integrals

> **Spec point** — `spcpt_D8yXJgjNvHXZ9KQk`

## Definite integration

### What is definite integration?

- **Definite** **Integration** occurs in an alternative version of the Fundamental Theorem of Calculus
- This version of the Theorem is the one referred to by most textbooks/websites

![Fundamental Theorem of Calculus using definite integration](../../../assets/c6af3891d5d1-8-1-3-notes-fig1.png)

- **a** and **b** are called limits

  - **a** is the lower limit
  - **b** is the upper limit
- **f’(x)** is the **derivative** of **f(x)**
- The value can be **positive, zero** or **negative**

### Why do I not need to include a constant of integration for definite integration?

![Example of the constant of integration cancelling out](../../../assets/04e6ace23b39-8-1-3-notes-fig2.png)

- “**+c**” would appear in both **f(a)** and **f(b)**

  - Since we then calculate **f(b)** – **f(a)** they cancel each other out
  - So “**+c**” is not included with definite integration

### How do I find a definite integral?

- **STEP 1**

  - Give the integral a name (if it does not already have one)
  
    - This saves you having to rewrite the whole integral every time!
- **STEP 2**

  - If necessary rewrite the integral into a more easily *integrable* form
  
    - Not all functions can be integrated directly
- **STEP 3**

  - Integrate without applying the limits
  
    - Notation: use square brackets [ ] with limits placed after the end bracket
- **STEP 4**

  - Substitute the limits into the function and calculate the answer
  
    - Substitute the top limit first
    - Then substitute the bottom limit
    - Subtract the second value from the first

![Example of definite integration](../../../assets/8355b475572a-8-1-3-notes-fig3.png)

### What are the special properties of definite integrals?

- Some of these have been encountered already and some may seem obvious …

  - taking **constant** factors outside the integral
  
    - `integral subscript a superscript b k straight f left parenthesis x right parenthesis space straight d x equals k integral subscript a superscript b straight f left parenthesis x right parenthesis space straight d x` where$k$ is a constant
    - useful when fractional and/or negative values involved
  - integrating term by term
  
    - `space integral subscript a superscript b left square bracket straight f left parenthesis x right parenthesis plus straight g left parenthesis x right parenthesis right square bracket space straight d x equals integral subscript a superscript b straight f left parenthesis x right parenthesis space straight d x plus integral subscript a superscript b straight g left parenthesis x right parenthesis space straight d x`
    - the above works for subtraction of terms/functions too
  - equal upper and lower limits
  
    - `integral subscript a superscript a straight f left parenthesis x right parenthesis space d x equals 0`
    - on evaluating, this would be a value subtracted from itself!
  - swapping limits gives the same, but negative, result
  
    - `integral subscript a superscript b straight f left parenthesis x right parenthesis space straight d x equals negative integral subscript b superscript a straight f left parenthesis x right parenthesis space straight d x`
    - compare 8 subtract 5 say, with 5 subtract 8 …
  - splitting the interval
  
    - `space integral subscript a superscript b straight f left parenthesis x right parenthesis space straight d x equals integral subscript a superscript c straight f left parenthesis x right parenthesis space straight d x plus integral subscript c superscript b straight f left parenthesis x right parenthesis space straight d x` where$a\leqc\leqb$
    - this is particularly useful for areas under multiple curves or areas under the$x$-axis

> **Exam Hint**
> - Look out for questions that ask you to find an **indefinite** integral in one part (so “**+c**” needed), then in a later part use the same integral as a **definite** integral (where “**+c**” is not needed)

> **Worked Example**
> Find the value of
> 
> `integral subscript 2 superscript 4 3 x left parenthesis x squared minus 2 right parenthesis space straight d x`
> 
> **Answer:**
> 
> > *Start by expanding the brackets inside the integral*
> 
> `integral subscript 2 superscript 4 open parentheses 3 x cubed minus 6 x close parentheses space straight d x`
> 
> > *Integrate as usual (here it's a 'powers of *$x$*' integration)*
> 
> > *Write the answer in square brackets with the integration limits outside*
> 
> `table row cell integral subscript 2 superscript 4 open parentheses 3 x cubed minus 6 x close parentheses space straight d x end cell equals cell open square brackets 3 open parentheses fraction numerator x to the power of 3 plus 1 end exponent over denominator 3 plus 1 end fraction close parentheses minus 6 open parentheses fraction numerator x to the power of 1 plus 1 end exponent over denominator 1 plus 1 end fraction close parentheses close square brackets subscript 2 superscript 4 end cell row blank equals cell open square brackets 3 over 4 x to the power of 4 minus 3 x squared close square brackets subscript 2 superscript 4 end cell end table`
> 
> > *Now substitute 4 into that function *
> *And subtract from it the function with 2 substituted in*
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row cell open square brackets 3 over 4 x to the power of 4 minus 3 x squared close square brackets subscript 2 superscript 4 end cell equals cell open parentheses 3 over 4 open parentheses 4 close parentheses to the power of 4 minus 3 open parentheses 4 close parentheses squared close parentheses minus open parentheses 3 over 4 open parentheses 2 close parentheses to the power of 4 minus 3 open parentheses 2 squared close parentheses close parentheses end cell row blank equals cell open parentheses 192 minus 48 close parentheses minus open parentheses 12 minus 12 close parentheses end cell row blank equals cell 144 minus 0 end cell row blank equals 144 end table`
> 
> `Error converting from MathML to accessible text.`
