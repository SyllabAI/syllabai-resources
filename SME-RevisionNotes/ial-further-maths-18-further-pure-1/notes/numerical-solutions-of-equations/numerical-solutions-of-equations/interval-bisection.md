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
- For example, if $\mathrm{f} ( 1 ) < 0$ and $\mathrm{f} ( 2 ) > 0$ and $\mathrm{f} ( x )$ is continuous

  - Then a root must lie in $[ 1 , 2 ]$
  - Find the **midpoint **of the interval
  
    - $x=1.5$
  - Check the **sign **at the midpoint
  
    - For example, $\mathrm{f} ( 1.5 ) < 0$
  - Write down the **half-interval **that has the **sign change**
  
    - $\mathrm{f} ( 1 ) < 0$, $\mathrm{f} ( 1.5 ) < 0$ and $\mathrm{f} ( 2 ) > 0$
    - So $[ 1.5 , 2 ]$ has the sign change
- The process can be **repeated**

  - For example, if $\mathrm{f} ( 1.75 ) > 0$ then $[ 1.5 , 1.75 ]$ contains the sign change

### How do I use interval bisection to estimate a root?

- If a root lies in the interval $[ 1 , 2 ]$, then the **first approximation **of the root, $x_{1}$, is simply the **midpoint**

  - $x_{1}=1.5$
- The **second approximation**, $x_{2}$, requires using Interval Bisection once

  - For example, giving $[ 1.5 , 2 ]$
  - Then find the **midpoint**
  
    - $x_{2}=1.75$
  - And so on

> **Exam Hint**
> Read the question carefully to see if an approximation to the root is required, or the interval containing the root is required.

> **Worked Example**
> The equation $x^{3}+x-16=0$ has a root in the interval $[ 2.1 , 2.9 ]$.
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
> $\begin{gathered} \mathrm{f} ( 2.1 ) & = - 4.639 < 0 \\ \mathrm{f} ( 2.9 ) & = 11.289 > 0 \end{gathered}$
> 
> > *Find the midpoint of the interval*
> 
> $x=\frac{2.1+2.9}{2}=2.5$
> 
> > *Find the sign of *$\mathrm{f} ( x )$* at *$x=2.5$
> 
> $\mathrm{f} ( 2.5 ) = 2.125 > 0$
> 
> > *Find the new halved interval containing the sign change*
> *Check the signs: *$\mathrm{f} ( 2.1 ) < 0$*, *$\mathrm{f} ( 2.5 ) > 0$* and *$\mathrm{f} ( 2.9 ) > 0$
> 
> $[ 2.1 , 2.5 ]$
> 
> > *Repeat the process*
> *Find the midpoint of the interval*
> 
> $x=\frac{2.1+2.5}{2}=2.3$
> 
> > *Find the sign of *$\mathrm{f} ( x )$* at *$x=2.3$
> 
> $\mathrm{f} ( 2.3 ) = - 1.533 < 0$
> 
> > *Find the new halved interval containing the sign change*
> *Check the signs: *$\mathrm{f} ( 2.1 ) < 0$*, *$\mathrm{f} ( 2.3 ) < 0$* and *$\mathrm{f} ( 2.5 ) > 0$
> 
> $[ 2.3 , 2.5 ]$
