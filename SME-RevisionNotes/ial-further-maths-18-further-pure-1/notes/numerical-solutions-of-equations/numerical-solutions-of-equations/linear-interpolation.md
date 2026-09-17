---
note_id: "rn_nnBDSgNV7PRX4wQF"
title: "Linear Interpolation"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/numerical-solutions-of-equations/numerical-solutions-of-equations/linear-interpolation
path: numerical-solutions-of-equations/numerical-solutions-of-equations/linear-interpolation
updated_at: "2024-04-04T17:00:44.619Z"
spec_point_ids: ["spcpt_vywmYvX3FQXf7n75"]
spec_point_codes: []
guided_study: false
---

# Linear Interpolation

## Linear Interpolation

> **Spec point** — `spcpt_vywmYvX3FQXf7n75`

## Linear Interpolation

### What is linear interpolation?

- **Linear interpolation** draws a **straight line** between the points *A* and *B* with coordinates  `open parentheses a comma space straight f open parentheses a close parentheses close parentheses` and `open parentheses b comma space straight f open parentheses b close parentheses close parentheses`, where $a<x<b$ is an interval containing a root to the equation `straight f open parentheses x close parentheses equals 0`

  - As `straight f open parentheses a close parentheses` and `straight f open parentheses b close parentheses` have **different signs**, *A *and *B* are on **either side **of the *x*-axis
  - The **approximation** to the root is  where this straight line **cuts the *****x*****-axis**
  
    - This is at the point *X* with coordinates `open parentheses x comma space 0 close parentheses`
    - Points *A, X *and *B* lie on the same straight line
- It helps to use the **gradient formula**

  - The gradient between `open parentheses x subscript 1 comma space y subscript 1 close parentheses` and `open parentheses x subscript 2 comma space y subscript 2 close parentheses` is $\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$

### How do I apply linear interpolation using gradients?

- This is best explained with an example
- If the root of `straight f open parentheses x close parentheses equals 0` lies in the interval `open square brackets 1 comma space 2 close square brackets` and `straight f open parentheses 1 close parentheses equals negative 5` and `straight f open parentheses 2 close parentheses equals 10`, then:

  - *A* is the point `open parentheses 1 comma space minus 5 close parentheses`
  - *B* is the point `open parentheses 2 comma space 10 close parentheses`
  - *X* is the point `open parentheses x comma space 0 close parentheses`
  
    - This is the *x*-intercept of the line *AB*
    - *A, X *and *B* lie on the same **straight line**
  - The **gradient **of ***AX*** equals the** gradient** of ***XB***
  
    - The** order** matters (not *BX*)
  - Use the **gradient formula** to set these equal
  
    - `fraction numerator 0 minus open parentheses negative 5 close parentheses over denominator x minus 1 end fraction equals fraction numerator 10 minus 0 over denominator 2 minus x end fraction` giving $\frac{5}{x-1}=\frac{10}{2-x}$
  - **Solve** the equation to find $x$
  
    - `5 open parentheses 2 minus x close parentheses equals 10 open parentheses x minus 1 close parentheses`
    - expand and solve to get $x=\frac{4}{3}$
- This process can be **repeated **to get the next approximation
- This gradient method does** not** require a** sketch**

### What other methods can I use to do linear interpolation?

- You can **sketch** the points *A*, *B* and *X* on a diagram and use **similar triangles** either side of the *x*-axis to find an **equation** in $x$

  - This leads to the same equation as the gradients above
- Or you can use **coordinate geometry** to find the **equation** of the **line *****AB***

  - Use `y minus y subscript 1 equals m open parentheses x minus x subscript 1 close parentheses`
  - Then find its ***x*****-intercept**
  
    - Substitute in $y=0$ and solve for $x$

> **Exam Hint**
> If the calculations involve lengthy decimals, you can use `straight f open parentheses a close parentheses` and `straight f open parentheses b close parentheses` to stand for their numbers  in your working!

> **Worked Example**
> The equation `straight f open parentheses x close parentheses equals 0` where `straight f open parentheses x close parentheses equals x cubed minus square root of x minus 2` has a root in the interval `open square brackets 1.4 comma space 1.5 close square brackets`.
> 
> Use linear interpolation once to find an approximation to the root, giving your answer to 3 decimal places.
> 
> > *Find *`straight f open parentheses 1.4 close parentheses`* and *`straight f open parentheses 1.5 close parentheses`
> 
> `table row cell straight f open parentheses 1.4 close parentheses end cell equals cell 1.4 cubed minus square root of 1.4 end root minus 2 equals negative 0.439215... end cell row cell straight f open parentheses 1.5 close parentheses end cell equals cell 1.5 cubed minus square root of 1.5 end root minus 2 equals 0.150255... end cell end table`
> 
> > *It is easier to write them as *`straight f open parentheses 1.4 close parentheses`* and *`straight f open parentheses 1.5 close parentheses`* for now*
> *Let **A**, **B** and **X** be the points *`open parentheses 1.4 comma space straight f open parentheses 1.4 close parentheses close parentheses`*, *`open parentheses 1.5 comma space straight f open parentheses 1.5 close parentheses close parentheses`* and *`open parentheses x comma space 0 close parentheses`
> *Use the gradient formula *$\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$* to find the gradient of **AX*
> 
> *gradient of ***AX ***is *`fraction numerator 0 minus straight f open parentheses 1.4 close parentheses over denominator x minus 1.4 end fraction`
> 
> > *Use the gradient formula *$\frac{y_{2}-y_{1}}{x_{2}-x_{1}}$* to find the gradient of **XB*
> 
> *gradient of ***XB ***is *`fraction numerator straight f open parentheses 1.5 close parentheses minus 0 over denominator 1.5 minus x end fraction`
> 
> > *Set the two gradients equal to each other*
> 
> `fraction numerator 0 minus straight f open parentheses 1.4 close parentheses over denominator x minus 1.4 end fraction equals fraction numerator straight f open parentheses 1.5 close parentheses minus 0 over denominator 1.5 minus x end fraction`
> 
> > *Simplify and cross multiply*
> 
> `table row cell fraction numerator negative straight f open parentheses 1.4 close parentheses over denominator x minus 1.4 end fraction end cell equals cell fraction numerator straight f open parentheses 1.5 close parentheses over denominator 1.5 minus x end fraction end cell row cell negative straight f open parentheses 1.4 close parentheses open parentheses 1.5 minus x close parentheses end cell equals cell straight f open parentheses 1.5 close parentheses open parentheses x minus 1.4 close parentheses end cell end table`
> 
> > *Expand and collect the *$x$* terms on the right-hand side*
> 
> `table row cell negative 1.5 straight f open parentheses 1.4 close parentheses plus straight f open parentheses 1.4 close parentheses x end cell equals cell straight f open parentheses 1.5 close parentheses x minus 1.4 straight f open parentheses 1.5 close parentheses end cell row cell 1.4 straight f open parentheses 1.5 close parentheses minus 1.5 straight f open parentheses 1.4 close parentheses end cell equals cell straight f open parentheses 1.5 close parentheses x minus straight f open parentheses 1.4 close parentheses x end cell end table`
> 
> > *Factorise out the *$x$*, then make *$x$* the subject*
> 
> `table row cell 1.4 straight f open parentheses 1.5 close parentheses minus 1.5 straight f open parentheses 1.4 close parentheses end cell equals cell x open square brackets straight f open parentheses 1.5 close parentheses minus straight f open parentheses 1.4 close parentheses close square brackets end cell row cell fraction numerator 1.4 straight f open parentheses 1.5 close parentheses minus 1.5 straight f open parentheses 1.4 close parentheses over denominator straight f open parentheses 1.5 close parentheses minus straight f open parentheses 1.4 close parentheses end fraction end cell equals x end table`
> 
> > *Substitute in  *`straight f open parentheses 1.4 close parentheses`* and *`straight f open parentheses 1.5 close parentheses`* from above*
> 
> `table row cell fraction numerator 1.4 cross times 0.150255... negative 1.5 cross times open parentheses negative 0.439215... close parentheses over denominator 0.150255... negative open parentheses negative 0.439215... close parentheses end fraction end cell equals x row cell 1.47451... end cell equals x end table`
> 
> > *Give your final answer to 3 decimal places*
> 
> **Final answer:** $1.475$** to 3 decimal places**
> 
> **If you did the working without **`straight f open parentheses 1.4 close parentheses`** and **`straight f open parentheses 1.5 close parentheses`**, keep lots of decimal places**
