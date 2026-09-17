---
note_id: "rn_KnR42njGpmYbrQbP"
title: "Interval Bisection"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/numerical-solutions-of-equations/numerical-solutions-of-equations/interval-bisection
path: numerical-solutions-of-equations/numerical-solutions-of-equations/interval-bisection
updated_at: "2024-04-04T16:40:11.063Z"
spec_point_ids: ["spcpt_rS66jWdV6BtkFBXm"]
spec_point_codes: []
guided_study: false
---

# Interval Bisection

## Interval Bisection

> **Spec point** — `spcpt_rS66jWdV6BtkFBXm`

## Interval Bisection

### What is interval bisection?

- **Interval Bisection** means **splitting** an **interval** containing a root into two **halves** and using a **sign change** **test** to find out which half contains the **root**
- For example, if `straight f open parentheses 1 close parentheses less than 0` and `straight f open parentheses 2 close parentheses greater than 0` and `straight f open parentheses x close parentheses` is continuous

  - Then a root must lie in `open square brackets 1 comma space 2 close square brackets`
  - Find the **midpoint **of the interval
  
    - $x=1.5$
  - Check the **sign **at the midpoint
  
    - For example, `straight f open parentheses 1.5 close parentheses less than 0`
  - Write down the **half-interval **that has the **sign change**
  
    - `straight f open parentheses 1 close parentheses less than 0`, `straight f open parentheses 1.5 close parentheses less than 0` and `straight f open parentheses 2 close parentheses greater than 0`
    - So `open square brackets 1.5 comma space 2 close square brackets` has the sign change
- The process can be **repeated**

  - For example, if `straight f open parentheses 1.75 close parentheses greater than 0` then `open square brackets 1.5 comma space 1.75 close square brackets` contains the sign change

### How do I use interval bisection to estimate a root?

- If a root lies in the interval `open square brackets 1 comma space 2 close square brackets`, then the **first approximation **of the root, $x_{1}$, is simply the **midpoint**

  - $x_{1}=1.5$
- The **second approximation**, $x_{2}$, requires using Interval Bisection once

  - For example, giving `open square brackets 1.5 comma space 2 close square brackets`
  - Then find the **midpoint**
  
    - $x_{2}=1.75$
  - And so on

> **Exam Hint**
> Read the question carefully to see if an approximation to the root is required, or the interval containing the root is required.

> **Worked Example**
> The equation $x^{3}+x-16=0$ has a root in the interval `open square brackets 2.1 comma space 2.9 close square brackets`.
> 
> Use interval bisection to find an interval of width 0.2 that contains the root.
> 
> > *Find the width of the interval given in the question*
> 
> $2.9-2.1=0.8$
> 
> > *Interval bisection halves the width*
> *To get a width of 0.2, interval bisection is needed twice*
> *Find the signs of the interval end-points*
> 
> `table row cell straight f open parentheses 2.1 close parentheses end cell equals cell negative 4.639 less than 0 end cell row cell straight f open parentheses 2.9 close parentheses end cell equals cell 11.289 greater than 0 end cell end table`
> 
> > *Find the midpoint of the interval*
> 
> $x=\frac{2.1+2.9}{2}=2.5$
> 
> > *Find the sign of *`straight f open parentheses x close parentheses`* at *$x=2.5$
> 
> `straight f open parentheses 2.5 close parentheses equals 2.125 greater than 0`
> 
> > *Find the new halved interval containing the sign change*
> *Check the signs: *`straight f open parentheses 2.1 close parentheses less than 0`*, *`straight f open parentheses 2.5 close parentheses greater than 0`* and *`straight f open parentheses 2.9 close parentheses greater than 0`
> 
> `open square brackets 2.1 comma space 2.5 close square brackets`
> 
> > *Repeat the process*
> *Find the midpoint of the interval*
> 
> $x=\frac{2.1+2.5}{2}=2.3$
> 
> > *Find the sign of *`straight f open parentheses x close parentheses`* at *$x=2.3$
> 
> `straight f open parentheses 2.3 close parentheses equals negative 1.533 less than 0`
> 
> > *Find the new halved interval containing the sign change*
> *Check the signs: *`straight f open parentheses 2.1 close parentheses less than 0`*, *`straight f open parentheses 2.3 close parentheses less than 0`* and *`straight f open parentheses 2.5 close parentheses greater than 0`
> 
> `open square brackets 2.3 comma space 2.5 close square brackets`
