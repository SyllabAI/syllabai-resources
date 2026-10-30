---
note_id: "rn_Js4rWd72JRz7BzBj"
title: "Completing the Square"
source: https://www.savemyexams.com/igcse/maths/edexcel/a/18/higher/revision-notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square
path: 2-equations-formulae-and-identities/completing-the-square/completing-the-square
updated_at: "2026-01-27T15:03:08.666Z"
spec_point_ids: ["spcpt_9Stcxtj75Q3wpqJF"]
spec_point_codes: []
guided_study: false
---

# Completing the Square

## Completing the Square

> **Spec point** — `spcpt_9Stcxtj75Q3wpqJF`

## Completing the square

### How can I rewrite the first two terms of a quadratic expression as the difference of two squares?

- Look at the quadratic expression *x*<sup>2</sup> + *bx* + *c*
- The first** two terms** can be written as the **difference of two squares** using the following rule

$x^{2}+bx$ is the same as `(x+p)²−p²` where $p$ is **half** of $b$

- Check this is true by expanding the right-hand side

  - Is $x^{2}+2x$ the same as `(x+1)²−1²`?
  
    - Yes: (*x* + 1)(*x* + 1) - 1<sup>2</sup> = *x*<sup>2</sup> + 2*x* + 1 - 1 = *x*<sup>2</sup> + 2*x*
- This works for **negative** values of *b* too

  - $x^{2}-20x$ can be written as `(x−10)²−(−10)²` which is `(x−10)²−100`
  - A negative *b* does not change the sign at the end

### How do I complete the square?

- **Completing the square** is a way to rewrite a quadratic expression in a form containing a **squared bracket**
- To complete the square on *x*<sup>2</sup> + 10*x* + 9

  - Use the rule above to replace the first two terms, *x*<sup>2</sup> + 10*x, *with (*x* + 5)<sup>2</sup> - 5<sup>2</sup>
  - then add 9:  (*x* + 5)<sup>2</sup> - 5<sup>2 </sup>+ 9
  - **simplify** the **numbers**:  (*x* + 5)<sup>2</sup> - 25<sup> </sup>+ 9
  - answer: (*x* + 5)<sup>2</sup> - 16

### How do I complete the square when there is a coefficient in front of the x<sup>2</sup> term?

- You first need to take $a$ out as a **factor** of the *x*<sup>2</sup> and *x* terms only

  - **Factorise** the** first two terms**
  - $a x²+b x+c=a [ x²+b / a x ]+c$
  
    - Use **square-shaped** **brackets** here to avoid confusion with round brackets later
- Then complete the square on the bit **inside** the brackets: $x^{2}+\frac{b}{a}x$

  - This gives $a [ (x+p)²−p² ]+c$
  
    - where *p* is half of $\frac{b}{a}$
- Finally **multiply** this expression through by *a* (from outside the square brackets) and **add the c** on to the end

  - `a (x+p)²−a p²+c`
  
    - This looks far more complicated than it is in practice!
  - Usually you are asked to give your final answer in the form  `a (x+p)²+q`
  - For example,  *y* = 4*x*<sup>2</sup> + 16*x* + 5
  
    - Factorise out '*a*' on the right-hand side (use square brackets)
    
      - *y* = 4[*x*<sup>2</sup> + 4*x*] + 5
    - Replace *x*<sup>2</sup> + 4*x* with (*x* + 2)<sup>2</sup> - 2<sup>2</sup>  (because *p* = $\frac{4}{2}$ = 2)
    
      - *y* = 4[(*x* + 2)<sup>2</sup> - 2<sup>2</sup>] + 5
    - Simplify the terms inside the square brackets
    
      - *y* = 4[(*x* + 2)<sup>2</sup> - 4] + 5
    - Multiply everything inside the square brackets by 4
    
      - *y* = 4(*x* + 2)<sup>2</sup> - 16 + 5
    - Simplify to get the final answer
    
      - *y* = 4(*x* + 2)<sup>2</sup> - 11
- For quadratics like $-x^{2}+bx+c$, do the above but with *a* = -1

### How do I find the turning point by completing the square?

- Completing the square helps us find the **turning** **point** on a quadratic graph

  - If `y=(x+p)²+q` then the turning point is at `(−p comma q)`
  
    - Notice the negative sign in the *x*-coordinate
    - This links to transformations of graphs
    - A translation of $y=x^{2}$ by *p* to the left and *q* up
  - If `y=a (x+p)²+q` then the turning point is still at `(−p comma q)`
  
    - The *a* does **not change** the coordinates
    - The turning point is a minimum point if *a* > 0
    - or a maximum point if *a* < 0
- This can also help you **create the equation** of a quadratic when given the turning point

![Completing the square Notes Diagram 3, A Level & AS Level Pure Maths Revision Notes](../../../assets/70ae26731145-8467-completing-the-square-notes-diagram-3.png)

- It can also be used to **prove** or **show** results using the fact that any **squared term**, such as the squared bracket (*x* ± *p*)<sup>2</sup>, will always be **greater than or equal to 0**

  - You cannot square a number and get a negative value
  - The smallest a squared term can be is 0

![Completing the square Notes Diagram 4, A Level & AS Level Pure Maths Revision Notes](../../../assets/96ce1435039b-25538-completing-the-square-notes-diagram-4.png)

> **Exam Hint**
> To know if you have completed the square correctly, expand your answer to check.

> **Worked Example**
> (a) By completing the square, find the coordinates of the turning point on the graph of $y=x^{2}+6x-11$.
> 
> > *Find half of +6 (call this **p**)*
> 
> $p=\frac{6}{2}=3$
> 
> > *Write **x*<sup>*2*</sup>* + 6**x** in the form (**x** + **p**)*<sup>*2*</sup>* - **p*<sup>*2*</sup>
> 
> $x^{2}+6x$ *is the same as* `(x+3)²−3²`
> 
> > *Put this result into the equation of the curve*
> 
> `y=(x+3)²−3²−11`
> 
> > *Simplify the numbers*
> 
> `y=(x+3)²−20`
> 
> > *Use the fact that the turning point of* `y=(x+p)²+q` *is at* `(−p comma q)`* *
> *Here **p** = 3 and **q **= -20*
> 
> **Final answer:** **turning point at (-3, -20)**
> 
> (b)  Write $-3x^{2}+12x+24$ in the form `a (x+p)²+q`.
> 
> > *Factorise -3 out of the first two terms only*
> *Use square-shaped brackets*
> 
> $−3 [ x²−4x ]+24$
> 
> > *Complete the square on the **x*<sup>*2*</sup>* - 4**x** inside the brackets*
> *Write in the form (**x** + **p**)*<sup>*2*</sup>* - **p*<sup>*2*</sup>* where **p** is half of -4*
> 
> $−3 [ (x−2)²−(−2)² ]+24$
> 
> > *Simplify the numbers inside the brackets*
> *(-2)*<sup>*2*</sup> *is 4*
> 
> $−3 [ (x−2)²−4 ]+24$
> 
> *Multiply -3 by all the terms inside the square brackets*
> (*You do not multiply -3 by the 24)*
> 
> `−3 (x−2)²+12+24`
> 
> > *Simplify the numbers*
> 
> `−3 (x−2)²+36`
> 
> > *This is now in the form **a**(**x** + **p**)*<sup>*2*</sup>* + **q** where **a **= -3, **p** = -2 and **q** = 36*
> 
> $-3(x-2)^{2}+36$
