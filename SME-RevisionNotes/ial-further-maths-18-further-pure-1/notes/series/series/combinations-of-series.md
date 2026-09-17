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

  - `sum from r equals 1 to n of r equals 1 half n open parentheses n plus 1 close parentheses`
  - `sum from r equals 1 to n of r squared equals 1 over 6 n open parentheses n plus 1 close parentheses open parentheses 2 n plus 1 close parentheses`
  - `sum from r equals 1 to n of r cubed equals 1 fourth n squared open parentheses n plus 1 close parentheses squared`
- **Coefficients **of $r$, $r^{2}$ and $r^{3}$ can come out of the sum

  - `sum from r equals 1 to n of open parentheses a r cubed plus b r squared plus c r plus d close parentheses equals a sum from r equals 1 to n of r cubed space plus b sum from r equals 1 to n of r squared plus c sum from r equals 1 to n of r plus d n`
  
    - **Constants **are **multiplied** by $n$
  - You may have to **expand** expressions in $r$
  
    - `sum from r equals 1 to n of open parentheses r plus 3 close parentheses open parentheses r plus 4 close parentheses equals sum from r equals 1 to n of open parentheses r squared plus 7 r plus 12 close parentheses`
- It is often possible to **factorise final** **answers**, in particular taking out:

  - fractional coefficients
  - $n$
  - `open parentheses n plus 1 close parentheses`
- You may be required to write series as the **difference of two sums**

  - `sum from r equals 5 to 10 of r equals sum from r equals 1 to 10 of r minus sum from r equals 1 to 4 of r`

> **Exam Hint**
> Exam questions often refer to these three formulae as the "standard summation formulae".

> **Worked Example**
> (a)  Using standard summation formulae, show that
> 
> `sum from r equals 1 to n of open parentheses r minus 1 close parentheses r open parentheses r plus 1 close parentheses equals 1 fourth open parentheses n minus 1 close parentheses n open parentheses n plus 1 close parentheses open parentheses n plus 2 close parentheses`
> 
> > *Expand and simplify the left-hand side*
> 
> `table row cell open parentheses r minus 1 close parentheses r open parentheses r plus 1 close parentheses end cell equals cell r open parentheses r squared minus 1 close parentheses end cell row blank equals cell r cubed minus r end cell end table`
> 
> > *Substitute in the formulae *`sum from r equals 1 to n of r cubed equals 1 fourth n squared open parentheses n plus 1 close parentheses squared`* and *`sum from r equals 1 to n of r equals 1 half n open parentheses n plus 1 close parentheses`
> 
> `table row cell sum from r equals 1 to n of open parentheses r cubed minus r close parentheses end cell equals cell sum from r equals 1 to n of r cubed minus sum from r equals 1 to n of r end cell row blank equals cell 1 fourth n squared open parentheses n plus 1 close parentheses squared minus 1 half n open parentheses n plus 1 close parentheses end cell end table`* *
> 
> > *Factorise out the quarter, *$n$* and *`open parentheses n plus 1 close parentheses`* then simplify*
> 
> `table row cell sum from r equals 1 to n of open parentheses r cubed minus r close parentheses end cell equals cell 1 fourth n open parentheses n plus 1 close parentheses open square brackets n open parentheses n plus 1 close parentheses minus 2 close square brackets end cell row blank equals cell 1 fourth n open parentheses n plus 1 close parentheses open parentheses n squared plus n minus 2 close parentheses end cell end table`
> 
> > *Factorise the quadratic on the right-hand side *
> 
> `table row cell sum from r equals 1 to n of open parentheses r cubed minus r close parentheses end cell equals cell equals 1 fourth n open parentheses n plus 1 close parentheses open parentheses n plus 2 close parentheses open parentheses n minus 1 close parentheses end cell row blank blank blank end table`
> 
> > *Rearrange into the form asked for by the question*
> 
> `table row cell sum from r equals 1 to n of open parentheses r minus 1 close parentheses r open parentheses r plus 1 close parentheses end cell equals cell 1 fourth open parentheses n minus 1 close parentheses n open parentheses n plus 1 close parentheses open parentheses n plus 2 close parentheses end cell end table`
> 
> (b)  Hence find the value of
> 
> $0\times1\times2+1\times2\times3+2\times3\times4+...+20\times21\times22$
> 
> > *It helps to write out the first few terms in the series *`table row blank blank cell sum from r equals 1 to n of open parentheses r minus 1 close parentheses r open parentheses r plus 1 close parentheses end cell end table`
> 
> `table row blank blank cell open parentheses 1 minus 1 close parentheses cross times 1 cross times open parentheses 1 plus 1 close parentheses space space plus space space open parentheses 2 minus 1 close parentheses cross times 2 cross times open parentheses 2 plus 1 close parentheses space space plus space space open parentheses 3 minus 1 close parentheses cross times 3 cross times open parentheses 3 plus 1 close parentheses space space plus... end cell row blank equals cell 0 cross times 1 cross times 2 space space plus space space 1 cross times 2 cross times 3 space space plus space space 2 cross times 3 cross times 4 space space plus... end cell end table`
> 
> > *The question stops at 20 x 21 x 22*
> *This is actually the 21*<sup>*st*</sup>* term (not the 20*<sup>*th*</sup>* term)*
> *To find the sum of the first 21 terms, substitute *$n=21$* into part (a)*
> 
> `table row cell sum from r equals 1 to 21 of open parentheses r minus 1 close parentheses r open parentheses r plus 1 close parentheses end cell equals cell 1 fourth open parentheses 21 minus 1 close parentheses cross times 21 cross times open parentheses 21 plus 1 close parentheses open parentheses 21 plus 2 close parentheses end cell row blank equals cell 1 fourth cross times 20 cross times 21 cross times 22 cross times 23 end cell end table`
> 
> **Final answer:** **53130**
> 
> (c)  If `sum from r equals 1 to n of open parentheses r minus 1 close parentheses r open parentheses r plus 1 close parentheses equals 10 space sum from r equals 1 to n of r squared`, find $n$.
> 
> > *Substitute the answer from part (a) into the left-hand side*
> *Substitute the standard formula *`sum from r equals 1 to n of r squared equals 1 over 6 n open parentheses n plus 1 close parentheses open parentheses 2 n plus 1 close parentheses`* into the right-hand side*
> 
> `table row cell 1 fourth open parentheses n minus 1 close parentheses n open parentheses n plus 1 close parentheses open parentheses n plus 2 close parentheses end cell equals cell 10 cross times 1 over 6 n open parentheses n plus 1 close parentheses open parentheses 2 n plus 1 close parentheses end cell end table`* *
> 
> > *Cancel the terms *$n$* and *`open parentheses n plus 1 close parentheses`* from both sides*
> *It also helps to multiply both sides by 12 to remove fractions*
> 
> `3 table row blank blank cell open parentheses n minus 1 close parentheses open parentheses n plus 2 close parentheses end cell end table table row blank equals blank end table table row blank blank 20 end table table row blank blank cell open parentheses 2 n plus 1 close parentheses end cell end table`
> 
> > *Expand, then form and solve a quadratic in *`equation`
> 
> `table row cell 3 open parentheses n squared plus n minus 2 close parentheses end cell equals cell 40 n plus 20 end cell row cell 3 n squared minus 37 n minus 26 end cell equals 0 row cell open parentheses 3 n plus 2 close parentheses open parentheses n minus 13 close parentheses end cell equals 0 row n equals cell negative 2 over 3 space space or space space n equals 13 end cell end table`
> 
> > $n$* must be a positive integer (as it is used in sigma notation, *`sum from r equals 1 to n of`*)*
> 
> $n=13$
