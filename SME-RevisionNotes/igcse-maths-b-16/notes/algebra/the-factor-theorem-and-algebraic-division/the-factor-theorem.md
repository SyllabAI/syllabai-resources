---
note_id: "rn_6JfgD9zknhMB3kJz"
title: "The Factor Theorem"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/algebra/the-factor-theorem-and-algebraic-division/the-factor-theorem
path: algebra/the-factor-theorem-and-algebraic-division/the-factor-theorem
updated_at: "2026-01-06T10:49:23.195Z"
spec_point_ids: ["spcpt_HBwF9SP8dhSGhZZk"]
spec_point_codes: []
guided_study: false
---

# The Factor Theorem

## Factor Theorem

> **Spec point** — `spcpt_HBwF9SP8dhSGhZZk`

## Factor Theorem

### What is the factor theorem?

- The **factor theorem** is used to find the linear **factors** of a function

  - This is closely related to finding the **roots** (or **solutions**) of a function or equation
- For a function `straight f open parentheses x close parentheses`, the **factor theorem** tells us that

  - If  `straight f open parentheses a close parentheses equals 0`, then `open parentheses x minus a close parentheses` is a factor of `straight f open parentheses x close parentheses`
  - If `open parentheses x minus a close parentheses` is a factor of `straight f open parentheses x close parentheses`, then  `straight f open parentheses a close parentheses equals 0`

### How do I use the factor theorem?

- Consider the  function `straight f open parentheses x close parentheses` where `open parentheses x minus a close parentheses` is a factor

  - Then by the factor theorem we know that `straight f open parentheses a close parentheses equals 0`
  
    - I.e., $x=a$ is a solution to the equation  `straight f open parentheses x close parentheses equals 0`
- Or consider the function `straight f open parentheses x close parentheses` where `straight f open parentheses a close parentheses equals 0`

  - Then by the factor theorem we know  that `open parentheses x minus a close parentheses` is a factor of `straight f open parentheses x close parentheses`
  - Therefore  $f(x)=(x-a)\timesQ(x)$
  
    - where `Q open parentheses x close parentheses` is a function that is also a factor of `straight f open parentheses x close parentheses`
  - Hence  `fraction numerator straight f left parenthesis x right parenthesis over denominator open parentheses x minus a close parentheses end fraction equals Q left parenthesis x right parenthesis`
  
    - I.e. `Q open parentheses x close parentheses` is the **quotient** when `straight f open parentheses x close parentheses` is divided by `open parentheses x minus a close parentheses`
    - And the **remainder** is equal to zero
- If the linear factor has a **coefficient of *****x**** *(other than 1) you must first factorise out the coefficient

  - For the linear factor  `left parenthesis b x blank – blank c right parenthesis blank equals b open parentheses x minus c over b close parentheses`
  
    - `straight f open parentheses c over b close parentheses equals 0`
    - `straight f open parentheses x close parentheses equals b open parentheses x minus c over b close parentheses cross times Q open parentheses x close parentheses equals open parentheses b x minus c close parentheses cross times Q open parentheses x close parentheses`

> **Exam Hint**
> Be careful with the minus sign in a factor `open parentheses x minus a close parentheses`.
> 
> - That means $a$ is a solution to `f open parentheses x close parentheses equals 0`, not $-a$ !
> 
> If you are looking for **integer** solutions to `straight f open parentheses x close parentheses equals 0`  (where `straight f open parentheses x close parentheses` is a polynomial)
> 
> - those solutions will always be factors of the constant term in `straight f open parentheses x close parentheses`

> **Worked Example**
> (a) Consider the function$f(x)=x^{3}-2x^{2}-x+2$. Given that $x=2$ is a solution to the equation `straight f open parentheses x close parentheses equals 0`, write down a linear factor of `straight f open parentheses x close parentheses`.
> 
> **Answer:**
> 
> > *By the factor theorem, if  *`straight f open parentheses a close parentheses equals 0`* then *`open parentheses x minus a close parentheses`* is a factor of *`straight f open parentheses x close parentheses`
> 
> > $x-2$* *
> 
> (b) Use the factor theorem to determine whether `open parentheses x plus 1 close parentheses` is a factor of $g(x)=2x^{3}+3x^{2}-x+5$.
> 
> **Answer:**
> 
> > *By the factor theorem, *`open parentheses x minus a close parentheses`* can only be a factor of *`straight g open parentheses x close parentheses`* if  *`straight g open parentheses a close parentheses equals 0`
> 
> > *But be careful, here *$a$* is equal to *$-1$*, not *$1$
> 
> `table row cell straight g open parentheses negative 1 close parentheses end cell equals cell 2 open parentheses negative 1 close parentheses cubed plus 3 open parentheses negative 1 close parentheses squared minus open parentheses negative 1 close parentheses plus 5 end cell row blank equals cell negative 2 plus 3 plus 1 plus 5 end cell row blank equals 7 end table`
> 
> **Final answer:** $g(-1)\neq0$**, so **$(x+1)$** is not a factor of **$g(x)$
> 
> (c) Given that `open parentheses 2 x minus 3 close parentheses` is a factor of `space straight h open parentheses x close parentheses equals 2 x cubed minus b x squared plus 7 x minus 6`, find the value of $b$.
> 
> **Answer:**
> 
> > `open parentheses 2 x minus 3 close parentheses equals 2 open parentheses x minus 3 over 2 close parentheses`*,  so *`open parentheses x minus 3 over 2 close parentheses`* is a factor of *`straight h open parentheses x close parentheses`
> 
> > *Therefore by the factor theorem, *`straight h open parentheses 3 over 2 close parentheses equals 0`
> 
> `table row cell space 2 open parentheses 3 over 2 close parentheses cubed minus b open parentheses 3 over 2 close parentheses squared plus 7 open parentheses 3 over 2 close parentheses minus 6 end cell equals 0 row cell 27 over 4 minus 9 over 4 b plus 21 over 2 minus 6 end cell equals 0 row cell 45 over 4 minus 9 over 4 b end cell equals 0 row cell 9 over 4 b end cell equals cell 45 over 4 end cell row b equals cell 4 over 9 cross times 45 over 4 end cell end table`
> 
> $b=5$
