---
note_id: "rn_BNqfQsXyDdbB42RM"
title: "Differentiation"
source: https://www.savemyexams.com/igcse/maths/cie/25/extended/revision-notes/coordinate-geometry-and-graphs/differentiation/differentiation
path: coordinate-geometry-and-graphs/differentiation/differentiation
updated_at: "2026-01-27T15:19:20.466Z"
spec_point_ids: ["spcpt_jZWNjy5cSsFsGdHp"]
spec_point_codes: []
guided_study: true
---

# Differentiation

## Differentiation

> **Spec point** — `spcpt_jZWNjy5cSsFsGdHp`

## Differentiation

### What is a gradient function?

- Recall that the **equation of a curve** gives the ***y*****-coordinate** of a point when you substitute in its* x*-coordinate

  - For example, $y=x^{2}+3x+5$
  
    - Substitute $x=2$ in to get $y=2^{2}+3\times2+5=15$
    - The point $( 2 , 15 )$ lies on the curve
- A **gradient function** gives the **gradient** of the curve at a point when you substitute in its *x*-coordinate

  - A gradient function is written as $\frac{dy}{dx}=...$
  
    - pronounced "d*y* by d*x*"
    - This refers to the change in *y *over change in *x*
  - For example, the gradient function $\frac{dy}{dx}=2x+3$
  
    - Substitute $x=2$ in to get $\frac{dy}{dx}=2\times2+3=7$
    - The gradient at the point where $x=2$ is 7
- The gradient function $\frac{dy}{dx}$ can also be called the **derivative** or **derived function**

### What is differentiation and how does it work?

- **Differentiation** is an **algebraic method** that changes the **equation **of a curve, $y=...$, into a **gradient function**, $\frac{dy}{dx}=...$
- To differentiate a power of $x$, **bring down the power** and** reduce the power by 1**

  - Differentiating $y=x^{5}$ gives $\frac{dy}{dx}=5x^{4}$
  - Differentiating $y=x^{8}$ gives $\frac{dy}{dx}=8x^{7}$
  - Differentiating $y=x^{n}$ gives $\frac{dy}{dx}=nx^{n-1}$
- Any **number **that is already **in front** of $x$ is** multiplied **by the power that was brought down

  - Differentiating $y=2x^{5}$ gives $\frac{dy}{dx}=2\times5x^{4}=10x^{4}$
  - Differentiating $y=\frac{1}{2}x^{8}$ gives $\frac{dy}{dx}=\frac{1}{2}\times8x^{7}=4x^{7}$
  - Differentiating $y=kx^{n}$ gives $\frac{dy}{dx}=knx^{n-1}$
- Be careful with **two special cases**:

  - Differentiating $y=kx$ gives $\frac{dy}{dx}=k$
  
    - The $x$ **disappears** leaving just a number
    - For example, $y=2x$ differentiates to $\frac{dy}{dx}=2$
    - This makes sense, the gradient of the straight line $y=2x$ is 2
  - Differentiating just a number (a **constant** term), $y=c$, gives $\frac{dy}{dx}=0$
  
    - **Numbers disappear!**
    - For example, $y=4$ differentiates to $\frac{dy}{dx}=0$
    - This makes sense, the gradient of the horizontal line $y=4$ is zero

![Image showing how the equation y = kx^n differentiates to dy/dx = knx^(n-1)](../../../assets/410d42648541-2-16-1-diff-basics-notes-fig5.png)

### How do I differentiate sums and differences of terms?

- The equation of a curve may include a number of different terms

  - You can differentiate each term **individually**
  
    - Differentiating $y=x^{5}+x^{8}$ gives $\frac{dy}{dx}=5x^{4}+8x^{7}$
    - Differentiating $y=4x^{3}-10x^{6}$ gives $\frac{dy}{dx}=12x^{2}-60x^{5}$
- Remember the two special cases of:

  - $kx$ differentiating to just $k$
  - and** constant **terms, $c$, differentiating to **zero**
  
    - E.g. differentiating $y=8x+1$ gives $\frac{dy}{dx}=8$

![Image showing the equation y = 3x^2 - 5x + 3 differentiates to dy/dx = 6x - 5](../../../assets/07ad8361eb7e-2-16-1-diff-basics-notes-fig6.png)

### How do I find the gradient of a curve using the gradient function?

- Find the ***x*****-coordinate** of the point on the curve you're interested in
- Use **differentiation** to turn the equation of the curve, $y=...$, into the gradient function, $\frac{dy}{dx}=...$
- **Substitute** the *x*-coordinate into the gradient function to find the gradient

  - The *y*-coordinate is not needed

![Image showing how the gradient of the curve y = 3x^2 - 2x at the point (2, 8), by differentiating the function and then substituting in x = 2. The gradient of the function at this (2, 8) is 10.](../../../assets/7b9667d2c57e-2-16-1-diff-basics-notes-fig7.png)

- If instead you are **given a gradient** and asked to find the ***x*****-coordinate**

  - set $\frac{dy}{dx}$ equal to that gradient and **solve** the equation

> **Exam Hint**
> Don't forget to write the left-hand sides of $y=...$ and $\frac{dy}{dx}=...$ to avoid mixing up the curve equation with the gradient function!

### How is the gradient function related to drawing tangents?

- The gradient of a curve changes as you move along the curve

  - To find the gradient at a particular point you can **draw a tangent **and find its **gradient **
  - This is a **graphical** method that is **not accurate**
  
    - It depends on how well you draw the tangent
- Instead, you can use **differentiation** to find the **gradient function**, then **substitute the x-coordinate** of the point into the gradient function to find the gradient

  - This is an **algebraic** method that is **exact**
- For example, to find the **gradient **of the curve $y=x^{3}-2x^{2}+6$ at the point *P* where $x=2$

  - either try to draw a tangent at $x=2$ and measure its gradient (see below)
  - or differentiate the equation to get $\frac{dy}{dx}=3x^{2}-4x$
  
    - Substitute in $x=2$ to get $\frac{dy}{dx}=3\times2^{2}-4\times2=4$
    - The gradient is 4

![Graph showing the curve with equation y = x^3 - 2x^2 + 6 and a tangent to the curve at a point P.](../../../assets/b5326219df38-2-16-1-diff-basics-notes-fig4.png)

> **Worked Example**
> A curve has the equation $y=x^{3}-3x^{2}-4x+1$.
> 
> (a) Find the gradient of the curve at the point $( 1 , - 5 )$.
> 
> > *Find the gradient function using differentiation*
> 
> $\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = 3 x^{2} - 3 \times 2 x - 4 + 0 \\ \frac{ \mathrm{d} y}{ \mathrm{d} x} & = 3 x^{2} - 6 x - 4 \end{gathered}$
> 
> > *Substitute *$x=1$* into the gradient function*
> 
> $\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = 3 \times 1^{2} - 6 \times 1 - 4 \\ = - 7 \end{gathered}$
> 
> > *The gradient when *$x=1$* is -7*
> *(The **y**-coordinate of the point is not needed)*
> 
> **Final answer:** **The gradient at **$(1,-5)$** is -7**
> 
> (b) Find the coordinates of the two points on the curve with a gradient of 5.
> 
> > *This is saying that *$\frac{dy}{dx}=5$
> *(This is not the same as substituting in *$x=5$*)*
> 
> > *Form an equation using *$\frac{dy}{dx}$* from above*
> 
> $3x^{2}-6x-4=5$
> 
> > *This is a quadratic equation*
> *Bring the terms to one side and solve (for example, by factorisation)*
> 
> $\begin{gathered} 3 x^{2} - 6 x - 9 & = 0 \\ x^{2} - 2 x - 3 & = 0 \\ ( x - 3 ) ( x + 1 ) & = 0 \\ x = 3 \text{or} x = - 1 \end{gathered}$
> 
> > *These are the *$x$*-coordinates of the two points on the curve with gradient 5*
> *Substitute *$x=3$* into *$y=x^{3}-3x^{2}-4x+1$* to find the *$y$*-coordinate of this point*
> 
> $\begin{gathered} y = 3^{3} - 3 \times 3^{2} - 4 \times 3 + 1 \\ = - 11 \end{gathered}$
> 
> > *Similarly, substitute *$x=-1$* into the equation for *$y$
> 
> $\begin{gathered} y = ( - 1 )^{3} - 3 \times ( - 1 )^{2} - 4 \times ( - 1 ) + 1 \\ = 1 \end{gathered}$
> 
> > *Write out the two sets of coordinates*
> 
> **Final answer:** **The points **$(3,-11)$** and **$(-1,1)$** have a gradient of 5**
