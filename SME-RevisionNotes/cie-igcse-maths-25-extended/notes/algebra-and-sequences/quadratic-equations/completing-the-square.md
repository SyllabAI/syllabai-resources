---
note_id: "rn_mrCKKkkm8y3CFH3r"
title: "Completing the Square"
source: https://www.savemyexams.com/igcse/maths/cie/25/extended/revision-notes/algebra-and-sequences/quadratic-equations/completing-the-square
path: algebra-and-sequences/quadratic-equations/completing-the-square
updated_at: "2026-01-20T16:02:38.638Z"
spec_point_ids: ["spcpt_HWGxmq9MtJxWfHyp", "spcpt_qqSKYggg8SJwzSNB"]
spec_point_codes: []
guided_study: true
---

# Completing the Square

## Completing the Square

> **Spec point** — `spcpt_HWGxmq9MtJxWfHyp`

## Completing the Square

### How can I rewrite the first two terms of a quadratic expression as the difference of two squares?

- Look at the quadratic expression *x*<sup>2</sup> + *bx* + *c *
- The first** two terms** can be written as the **difference of two squares** using the following rule

$x^{2}+bx$ is the same as $( x + p )^{2} - p^{2}$ where $p$ is **half** of $b$

- Check this is true by expanding the right-hand side

  - Is $x^{2}+2x$ the same as $( x + 1 )^{2} - 1^{2}$?
  
    - Yes: (*x* + 1)(*x* + 1) - 1<sup>2</sup> = *x*<sup>2</sup> + 2*x* + 1 - 1 = *x*<sup>2</sup> + 2*x*
- This works for **negative** values of *b* too

  - $x^{2}-20x$ can be written as $( x - 10 )^{2} - ( - 10 )^{2}$ which is $( x - 10 )^{2} - 100$
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
  - $a x^{2} + b x + c = a [ x^{2} + \frac{b}{a} x ] + c$
  
    - Use **square-shaped** **brackets** here to avoid confusion with round brackets later
- Then complete the square on the bit **inside** the brackets: $x^{2}+\frac{b}{a}x$

  - This gives $a [ ( x + p )^{2} - p^{2} ] + c$
  
    - where *p* is half of $\frac{b}{a}$
- Finally **multiply** this expression through by *a* (from outside the square brackets) and **add the c** on to the end

  - $a ( x + p )^{2} - a p^{2} + c$
  
    - This looks far more complicated than it is in practice!
  - Usually you are asked to give your final answer in the form  $a ( x + p )^{2} + q$
  - For example,  *y *= 4*x*<sup>2</sup> + 16*x* + 5
  
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

  - If $y = ( x + p )^{2} + q$ then the turning point is at $( - p , q )$
  
    - Notice the negative sign in the *x*-coordinate
    - This links to transformations of graphs
    - A translation of $y=x^{2}$ by *p* to the left and *q *up
  - If $y = a ( x + p )^{2} + q$ then the turning point is still at $( - p , q )$
  
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
> - To know if you have completed the square correctly, expand your answer to check

> **Worked Example**
> (a) By completing the square, find the coordinates of the turning point on the graph of $y=x^{2}+6x-11$.
> 
> **Answer:**
> 
> > *Find half of +6 (call this **p**)*
> 
> $p=\frac{6}{2}=3$
> 
> > *Write **x*<sup>*2*</sup>* + 6**x** in the form (**x** + **p**)*<sup>*2*</sup>* - **p*<sup>*2*</sup>
> 
> $x^{2}+6x$* is the same as *$( x + 3 )^{2} - 3^{2}$
> 
> > *Put this result into the equation of the curve*
> 
> $y = ( x + 3 )^{2} - 3^{2} - 11$
> 
> > *Simplify the numbers*
> 
> $y = ( x + 3 )^{2} - 20$
> 
> > *Use the fact that the turning point of *$y = ( x + p )^{2} + q$* is at *$( - p , q )$* *
> *Here **p** = 3 and **q **= -20*
> 
> **Final answer:** **turning point at (-3, -20)**
> 
> (b)  Write $-3x^{2}+12x+24$ in the form $a ( x + p )^{2} + q$.
> 
> **Answer:**
> 
> > *Factorise -3 out of the first two terms only*
> *Use square-shaped brackets*
> 
> $- 3 [ x^{2} - 4 x ] + 24$
> 
> > *Complete the square on the **x*<sup>*2*</sup>* - 4**x** inside the brackets*
> *Write in the form (**x** + **p**)*<sup>*2*</sup>* - **p*<sup>*2*</sup>* where **p** is half of -4*
> 
> $- 3 [ ( x - 2 )^{2} - ( - 2 )^{2} ] + 24$
> 
> > *Simplify the numbers inside the brackets*
> *(-2)*<sup>*2*</sup>* is 4*
> 
> $- 3 [ ( x - 2 )^{2} - 4 ] + 24$
> 
> *Multiply -3 by all the terms inside the square brackets*
> (*You do not multiply -3 by the 24)*
> 
> $- 3 ( x - 2 )^{2} + 12 + 24$
> 
> > *Simplify the numbers*
> 
> $- 3 ( x - 2 )^{2} + 36$
> 
> > *This is now in the form **a**(**x** + **p**)*<sup>*2*</sup>* + **q** where **a **= -3, **p** = -2 and **q** = 36*
> 
> $-3(x-2)^{2}+36$

## Solving by Completing the Square

> **Spec point** — `spcpt_qqSKYggg8SJwzSNB`

## Solving by Completing the Square

### How do I solve a quadratic equation by completing the square?

- To solve *x*<sup>2</sup> + *bx *+* c* = 0

  - **replace** the first two terms, ***x***<sup>**2**</sup>** + *****bx***, with **(*****x***** + *****p*****)**<sup>**2**</sup>** - *****p***<sup>**2**</sup> where ***p***** is half of *****b***
  - This is** completing the square**
  
    - *x*<sup>2</sup> + *bx *+* c* = 0 becomes (*x* + *p*)<sup>2</sup> - *p*<sup>2</sup> + *c *= 0
    - (where *p* is half of *b)*
  - rearrange this equation to **make *****x***** the subject** (using ±√)
- For example, solve *x*<sup>2</sup> + 10*x* + 9 = 0 by completing the square

  - *x*<sup>2</sup> + 10*x *becomes (*x* + 5)<sup>2</sup> - 5<sup>2</sup>
  - so* x*<sup>2</sup> + 10*x* + 9 = 0 becomes (*x* + 5)<sup>2</sup> - 5<sup>2 </sup>+ 9 = 0
  - make *x* the subject (using ±√)
  
    - (*x* + 5)<sup>2</sup> - 25<sup> </sup>+ 9 = 0
    - (*x* + 5)<sup>2</sup> = 16
    - *x* + 5 = ±√16
    - *x* + 5 = ±4
    - *x*  = -5 ±4
    - *x*  = -1 or *x*  = -9
- It also works with numbers that lead to **surds**

  - The answers found will be in **exact** (**surd**) form

> **Exam Hint**
> - When making *x* the subject to find the solutions, don't expand the squared bracket back out again!
> 
>   - Remember to use ±√ to get** two** solutions

### How do I solve by completing the square when there is a coefficient in front of the x<sup>2</sup> term?

- If the equation is *ax*<sup>2</sup> + *bx* + *c* = 0 with a **number** (other than 1)  **in front of *****x***<sup>**2**</sup>

  - you can **divide both sides by *****a**** *first (before completing the square)
  
    - For example  3*x*<sup>2</sup> + 12*x* + 9 = 0
    - Divide both sides by 3
    
      - *x*<sup>2</sup> + 4*x* + 3 = 0
    - Complete the square on this easier equation
- This trick **only** works when completing the square to **solve **a quadratic equation

  - i.e. it has an "=0" on the right-hand side
- **Don't** do this when using completing the square to rewrite a **quadratic expression** in a new form

  - i.e. when there is no "=0"
  - For that, you must **factorise out** the *a* (but not divide by it)
  
    - $a x^{2} + b x + c = a [ x^{2} + \frac{b}{a} x ] + c$ and so on

### How does completing the square link to the quadratic formula?

- The **quadratic formula** actually comes from **completing the square** to solve *ax*<sup>2</sup> + *bx* + *c* = 0

  - *a*, *b* and *c* are left as letters when completing the square
  
    - This makes it as general as possible
- You can see hints of this when you solve quadratics

  - For example, solving *x*<sup>2</sup> + 10*x* + 9 = 0
  
    - by completing the square, (*x* + 5)<sup>2</sup> = 16 so *x*  = -5 ± 4 (as above)
    - by the quadratic formula,  $x=\frac{-10\pm\sqrt{64}}{2}=-5\pm\frac{8}{2}$ = -5 ± 4 (the same structure)

> **Worked Example**
> Solve $2x^{2}-8x-24=0$ by completing the square.
> 
> **Answer:**
> 
> > *Divide both sides by 2 to make the quadratic start with **x*<sup>*2*</sup>* *
> 
> $x^{2}-4x-12=0$
> 
> > *Halve the middle number, -4, to get -2*
> *Replace the first two terms, **x*<sup>*2*</sup>* - 4**x**, with (**x** - 2)*<sup>*2*</sup>* - (-2)*<sup>*2*</sup>
> 
> $( x - 2 )^{2} - ( - 2 )^{2} - 12 = 0$
> 
> > *Simplify the numbers*
> 
> $\begin{array}{rcl} ( x - 2 )^{2} - 4 - 12 & = 0 \\ ( x - 2 )^{2} - 16 & = 0 \end{array}$
> 
> > *Add 16 to both sides*
> 
> $( x - 2 )^{2} = 16$
> 
> > *Take the square root of both sides*
> *Include the ± sign to get two solutions*
> 
> $x-2=\pm\sqrt{16}=\pm4$
> 
> > *Add 2 to both sides*
> 
> $x=2\pm4$
> 
> > *Work out each solution separately*
> 
> **Final answer:** **x**** = 6  or  ****x**** = -2**
