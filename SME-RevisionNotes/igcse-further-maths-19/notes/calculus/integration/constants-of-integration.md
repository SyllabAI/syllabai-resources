---
note_id: "rn_WsbpTp86wp3RBMs2"
title: "Constants of Integration"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/calculus/integration/constants-of-integration
path: calculus/integration/constants-of-integration
updated_at: "2024-10-16T10:42:11.036Z"
spec_point_ids: ["spcpt_Q2yPvWmbP3hFp5kM"]
spec_point_codes: []
guided_study: false
---

# Constants of Integration

## Finding the Constant of Integration

> **Spec point** — `spcpt_Q2yPvWmbP3hFp5kM`

## Finding the Constant of Integration

### What is the constant of integration?

- The **constant of integration** is the $c$ used when finding an **indefinite integral**

  - e.g. `integral open parentheses 3 x squared minus 5 close parentheses space straight d x equals x cubed minus 5 x plus c`
  - $c$ can be **any constant**
- **Integration** and **differentiation** are **inverse** operations

  - That means if you **differentiate** your answer to an **integral**...
  
    - ...it should turn back into the original **function you integrated**
  - The 'problem' is that the **derivative** **of a** **constant** is **zero**
  
    - `fraction numerator straight d over denominator straight d x end fraction open parentheses x cubed minus 5 x close parentheses equals 3 x squared minus 5`
    - `fraction numerator straight d over denominator straight d x end fraction open parentheses x cubed minus 5 x plus 7 close parentheses equals 3 x squared minus 5`
    - `fraction numerator straight d over denominator straight d x end fraction open parentheses x cubed minus 5 x minus 498 close parentheses equals 3 x squared minus 5`
  - So $x^{3}-5x$ plus or minus **any **constant** **is a valid solution to `integral open parentheses 3 x squared minus 5 close parentheses space straight d x`
- But consider the **graph** of $y=x^{3}-5x+c$

  - Different values of $c$ represent different vertical **translations** of the graph
  - If we know **one point** on that graph we can work out the value of $c$

### How do I find the constant of integration?

- On an exam you may be **given** a derivative $\frac{dy}{dx}$ or `straight f to the power of apostrophe open parentheses x close parentheses`

  - You can **integrate **that to find $y$ or `straight f open parentheses x close parentheses` in '$+c$' form
  
    - `integral fraction numerator straight d y over denominator straight d x end fraction straight d x equals y plus c`
    - `integral straight f to the power of apostrophe open parentheses x close parentheses space straight d x equals straight f open parentheses x close parentheses plus c`
- If you are **also** given a **point** on the graph of $y$ or of `y equals straight f open parentheses x close parentheses`

  - you can use this to **find the value** of $c$
  - **Substitute** the values you know into $y+c$ or `straight f open parentheses x close parentheses plus c`
  
    - Then **solve** for $c$
- The extra information doesn't **have** to be a point on a graph

  - As long as you know the value of `straight f open parentheses x close parentheses` for **one value** of $x$
  
    - you can substitute and solve to find $c$

> **Exam Hint**
> - An exam question probably won't tell you to 'find the constant of integration'
> 
>   - Instead you'll be given the derivative of a function
>   
>     - and one value of the function or a point on its graph
>   - Be sure to recognise this as a 'constant of integration' question!

> **Worked Example**
> The graph of $y=f(x)$ passes through the point $(3,-4)$.  The derivative of $f(x)$ is given by $f^{'}(x)=3x^{2}-4x-4$.
> 
> Find $f(x)$.
> 
> > *Integrate *`straight f to the power of apostrophe open parentheses x close parentheses`* to find *`straight f open parentheses x close parentheses`* in '*$+c$*' form*
> 
> `table row cell straight f open parentheses x close parentheses end cell equals cell integral open parentheses 3 x squared minus 4 x minus 4 close parentheses space straight d x end cell row blank equals cell 3 open parentheses fraction numerator x to the power of 2 plus 1 end exponent over denominator 2 plus 1 end fraction close parentheses minus 4 open parentheses fraction numerator x to the power of 1 plus 1 end exponent over denominator 1 plus 1 end fraction close parentheses minus 4 x plus c end cell row blank equals cell x cubed minus 2 x squared minus 4 x plus c end cell end table`
> 
> > *We also know the curve of *`y equals straight f open parentheses x close parentheses`* goes through *`open parentheses 3 comma space minus 4 close parentheses`
> 
> > *That means the function is equal to *$-4$* when *$x=3$
> 
> `open parentheses 3 close parentheses cubed minus 2 open parentheses 3 close parentheses squared minus 4 open parentheses 3 close parentheses plus c equals negative 4`
> 
> > *Solve for *$c$
> 
> `table row cell 27 minus 18 minus 12 plus c end cell equals cell negative 4 end cell row cell c minus 3 end cell equals cell negative 4 end cell row c equals cell negative 1 end cell end table`
> 
> $f(x)=x^{3}-2x^{2}-4x-1$
