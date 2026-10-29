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

  - e.g. $\int ( 3 x^{2} - 5 ) \mathrm{d} x = x^{3} - 5 x + c$
  - $c$ can be **any constant**
- **Integration** and **differentiation** are **inverse** operations

  - That means if you **differentiate** your answer to an **integral**...
  
    - ...it should turn back into the original **function you integrated**
  - The 'problem' is that the **derivative** **of a** **constant** is **zero**
  
    - $\frac{ \mathrm{d} }{ \mathrm{d} x} ( x^{3} - 5 x ) = 3 x^{2} - 5$
    - $\frac{ \mathrm{d} }{ \mathrm{d} x} ( x^{3} - 5 x + 7 ) = 3 x^{2} - 5$
    - $\frac{ \mathrm{d} }{ \mathrm{d} x} ( x^{3} - 5 x - 498 ) = 3 x^{2} - 5$
  - So $x^{3}-5x$ plus or minus **any **constant** **is a valid solution to $\int ( 3 x^{2} - 5 ) \mathrm{d} x$
- But consider the **graph** of $y=x^{3}-5x+c$

  - Different values of $c$ represent different vertical **translations** of the graph
  - If we know **one point** on that graph we can work out the value of $c$

### How do I find the constant of integration?

- On an exam you may be **given** a derivative $\frac{dy}{dx}$ or $\mathrm{f}^{'} ( x )$

  - You can **integrate **that to find $y$ or $\mathrm{f} ( x )$ in '$+c$' form
  
    - $\int \frac{ \mathrm{d} y}{ \mathrm{d} x} \mathrm{d} x = y + c$
    - $\int \mathrm{f}^{'} ( x ) \mathrm{d} x = \mathrm{f} ( x ) + c$
- If you are **also** given a **point** on the graph of $y$ or of $y = \mathrm{f} ( x )$

  - you can use this to **find the value** of $c$
  - **Substitute** the values you know into $y+c$ or $\mathrm{f} ( x ) + c$
  
    - Then **solve** for $c$
- The extra information doesn't **have** to be a point on a graph

  - As long as you know the value of $\mathrm{f} ( x )$ for **one value** of $x$
  
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
> > *Integrate* $\mathrm{f}^{'} ( x )$ *to find* $\mathrm{f} ( x )$ *in '*$+c$*' form*
> 
> $\begin{gathered} \mathrm{f} ( x ) & = \int ( 3 x^{2} - 4 x - 4 ) \mathrm{d} x \\ = 3 ( \frac{x^{2 + 1} }{2 + 1} ) - 4 ( \frac{x^{1 + 1} }{1 + 1} ) - 4 x + c \\ = x^{3} - 2 x^{2} - 4 x + c \end{gathered}$
> 
> > *We also know the curve of* $y = \mathrm{f} ( x )$ *goes through* $( 3 , - 4 )$
> 
> > *That means the function is equal to* $-4$ *when* $x=3$
> 
> $( 3 )^{3} - 2 ( 3 )^{2} - 4 ( 3 ) + c = - 4$
> 
> > *Solve for* $c$
> 
> $\begin{gathered} 27 - 18 - 12 + c & = - 4 \\ c - 3 & = - 4 \\ c = - 1 \end{gathered}$
> 
> $f(x)=x^{3}-2x^{2}-4x-1$
