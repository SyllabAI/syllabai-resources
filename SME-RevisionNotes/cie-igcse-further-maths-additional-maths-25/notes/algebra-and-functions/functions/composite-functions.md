---
note_id: "rn_b6fxNBw2PGpd3Fn8"
title: "Composite Functions"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/algebra-and-functions/functions/composite-functions
path: algebra-and-functions/functions/composite-functions
updated_at: "2026-07-02T08:19:38.503Z"
spec_point_ids: ["spcpt_NbgkVjMb8tWmrx9b", "spcpt_22RwCmKzC8PNYndf"]
spec_point_codes: []
guided_study: false
---

# Composite Functions

## Composite Functions

> **Spec point** — `spcpt_NbgkVjMb8tWmrx9b`

## Composite functions

### What is a composite function?

- A **composite function **is where one function is applied after another function

![Composite function fg(x) applies g first then f](../../../assets/3dd120f9b69f-2-8-1-language-of-functions-notes-diagram-8.png)

- The ‘**output’** of one function will be the ‘**input’** of the next one
- Sometimes called **function-of-a-function**
- A composite function can be denoted

  - $\mathrm{fg}(x)$
  - $f(g(x))$
  - All of these mean “$f$ of $g(x)$”

![Composite functions as function machines](../../../assets/4da8ed2c98f3-2-8-2-composite-functions-notes-diagram-1.png)

### How do I work with composite functions?

![Notation for composite functions](../../../assets/6871fdd6407a-2-8-2-composite-functions-notes-diagram-2.png)

- **Recognise** the notation The order matters

  - $\mathrm{fg}(x)$ means **“f **of** g **of** x”**

  - First apply $g$* *to $x$* *to get $g(x)$
  - Then apply $f$ to `straight g open parentheses x close parentheses` to get $f(g(x))$
  - Always start with the function **closest to the variable**
  - $\mathrm{fg}(x)$ is not usually equal to $\mathrm{gf}(x)$

#### Special cases

- `fg open parentheses x close parentheses` and `gf open parentheses x close parentheses` are generally different but can sometimes be the same
- `ff open parentheses x close parentheses` is written as $f^{2}(x)$

  - Note that** trig functions** are **exceptions** to this rule
  
    - e.g. `sin squared open parentheses x close parentheses` means `open parentheses sin open parentheses x close parentheses close parentheses squared` not `sin open parentheses sin open parentheses x close parentheses close parentheses`
- For inverse functions, `ff to the power of negative 1 end exponent open parentheses x close parentheses equals straight f to the power of negative 1 end exponent straight f open parentheses x close parentheses equals x`

![In general fg is a different function to gf](../../../assets/4ee894a88c77-2-8-2-composite-functions-notes-diagram-3.png)

> **Worked Example**
> Two functions, `straight f open parentheses x close parentheses` and `straight g open parentheses x close parentheses` are
> 
> `straight f open parentheses x close parentheses equals x squared plus 3 x minus 2
> straight g open parentheses x close parentheses equals x plus 3`
> 
> a) Find `straight f open parentheses 3 close parentheses` and `straight g open parentheses 3 close parentheses`.
> 
> `table row cell straight f open parentheses 3 close parentheses end cell equals cell open parentheses 3 close parentheses squared plus 3 open parentheses 3 close parentheses minus 2 end cell row blank equals cell 9 plus 9 minus 2 end cell row blank equals 16 end table`
> 
> `straight g open parentheses 3 close parentheses equals 3 plus 3`
> 
> $f(3)=16,g(3)=6$
> 
> b) Find, in terms of $x$, `fg open parentheses x close parentheses`.
> 
> > $g$* is the first function to be applied ...*
> 
> `table row cell therefore fg open parentheses x close parentheses end cell equals cell straight f open square brackets x plus 3 close square brackets end cell row blank equals cell open parentheses x plus 3 close parentheses squared plus 3 open parentheses x plus 3 close parentheses minus 2 end cell row blank equals cell x squared plus 6 x plus 9 plus 3 x plus 9 minus 2 end cell end table`
> 
> $\mathrm{fg}(x)=x^{2}+9x+16$

## Domain & Range of Composite Functions

> **Spec point** — `spcpt_22RwCmKzC8PNYndf`

## Domain & range of composite functions

### How do I find the domain and range of composite functions?

- Use logic to determine the *domain* and *range* of a **composite function**
- For `fg open parentheses x close parentheses` the first function to be applied will be $g$

  - So, *at best*, the **domain** of `fg open parentheses x close parentheses` will be the **same** as the **domain** of `straight g open parentheses x close parentheses`
- However, for this to be the case, the range of `straight g open parentheses x close parentheses` must be contained within the domain of `straight f open parentheses x close parentheses`

  - If this is *not* the case, then **restrictions** on the **domain** of `fg open parentheses x close parentheses` will be required
- Similarly, *at best,* the **range** of `fg open parentheses x close parentheses` will be the same as the **range** of `straight f open parentheses x close parentheses`

  - But if the domain of `straight f open parentheses x close parentheses` has been affected, the range of `fg open parentheses x close parentheses` will also be affected

> **Exam Hint**
> - **Domain** and **range** are important in composite funcitons like `fg open parentheses x close parentheses`
> 
>   - the ‘output’ (range) of **g** **must** be in the domain of **f(x), s**o `fg open parentheses x close parentheses` could exist, but `gf open parentheses x close parentheses`** **may not (or not for some values of $x$)

> **Worked Example**
> Two functions, `straight f open parentheses x close parentheses` and `straight g open parentheses x close parentheses` are defined as follows
> 
> $f(x)=\frac{1}{x},0<x<1$
> 
> `straight g open parentheses x close parentheses equals x squared comma space space x greater than 1`
> 
> a) Write down the range of `straight f open parentheses x close parentheses` and the range of `straight g open parentheses x close parentheses`.
> 
> > *As the domain of *`straight f open parentheses x close parentheses`* is *$0<x<1$*, *$\frac{1}{x}$* will always be greater than 1,*
> 
> **Final answer:** **The range of **$f(x)$** is **$f>1$
> 
> > *The square of any value will be positive or zero, but here, *$x=0$* is not included in the domain for *`straight g open parentheses x close parentheses`*.*
> 
> **Final answer:** **The range of **$g(x)$** is **$g>1$
> 
> b) Use your answers to (a) to help explain why `fg open parentheses x close parentheses` does not exist.
> 
> **Final answer:** $g$** is the first function to be applied**** ****The range of **$g$** would need to be contained within the domain of **$f$** ****But the range of **$g$** is **$g>1$** which is outside the domain of **$f$** which is **$0<x<1$** **$\therefore\mathrm{fg}(x)$** does not exist**
> 
> c) Find the range of `gf open parentheses x close parentheses`,
> 
> > $f$* is the first function.  The range of *$f$* is *$f>1$*.  This is the same as the domain of *`straight g space open parentheses x greater than 1 close parentheses`*.*
> 
> **Final answer:** **The range of **$\mathrm{gf}$** is **$\mathrm{gf}>1$
