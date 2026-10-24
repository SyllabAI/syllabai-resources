---
note_id: "rn_8HVwNyQy685GYRFq"
title: "Stationary Points & Turning Points"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/calculus/applications-of-differentiation/stationary-points-and-turning-points
path: calculus/applications-of-differentiation/stationary-points-and-turning-points
updated_at: "2024-10-16T10:15:14.760Z"
spec_point_ids: ["spcpt_y4d7RdjSk7WhHRYx", "spcpt_C9Nq7TX52PN6xJPk"]
spec_point_codes: []
guided_study: false
---

# Stationary Points & Turning Points

## Stationary Points & Turning Points

> **Spec point** — `spcpt_y4d7RdjSk7WhHRYx`

## Stationary Points & Turning Points

### What is the difference between a stationary point and a turning point?

- A **stationary point** is a point at which the **derivative** of a function is equal to zero

  - The **tangent** to the curve of the function is **horizontal** (gradient = 0)
- A **turning point** is a point at which

  - the **derivative** of a function is equal to zero
  - AND the derivative **changes sign** (from negative to positive, or positive to negative)
  
    - i.e. the curve changes from **‘going upwards’** to **‘going downwards’** (or vice versa)
  - Turning points will either be **(local) minimum** or **(local)** **maximum** points
- All **turning points** are also **stationary points**

  - But not all **stationary points **are **turning points**

### How do I find stationary points and turning points?

- For the function $y=f(x)$, **stationary points** can be found using the following process
- **STEP 1**
Find the **derivative,**$\frac{dy}{dx}=f'(x)$
- **STEP 2**
**Solve** the equation $f^{'}(x)=0$

  - The solution(s) are the $x$**-coordinate(s)** of any stationary points
  
    - Remember, 'stationary points' includes turning points
- **STEP 3**
Find the corresponding $y$**-coordinates** (if necessary)

  - **Substitute** each$x$-coordinate(s) into$f(x)$
  - If the question only asks for the $x$-coordinates, you can skip this step!
- More work is needed to find if a **stationary point** is a **turning point**

  - i.e. if it is a **(local) maximum** or **(local) minimum**
  - See the following note

## Testing for Local Minimum & Maximum Points

> **Spec point** — `spcpt_C9Nq7TX52PN6xJPk`

## Testing for Local Minimum & Maximum Points

### What are local minimum and maximum points?

- Local **minimum** and **maximum** points are two types of **stationary** point

  - The **derivative** at stationary points equals **zero**
  
    - i.e. $f'(x)=0$
  - But **not all** points with a zero derivative are maximum or minimum points
- A **local** **minimum** point,$(x,f(x))$

  - will have the **lowest** value of $f(x)$ in the **local** vicinity of the $x$ value
  - But $\mathrm{f} ( x )$ may reach a **lower** value further away
- A **local** **maximum** point, $(x,f(x))$

  - will have the **highest** value of $f(x)$ in the **local** vicinity of the $x$ value
  - But $\mathrm{f} ( x )$ may reach a **higher** value further away
- A **global** **maximum** (or **global minimum**) point

  - has the **highest** (or **lowest)** value of$f(x)$ for **all values** of$x$ in the domain of $f$
  
    - A **global** maximum (or minimum) may not be a **local** maximum (or minimum)
    - and vice versa
  - **Not all** functions have a global maximum (or minimum)
  
    - e.g. some functions tend to $\pm$infinity as $x$ tends to $\pm$infinity
    - or as $x$ approaches some other value (vertical asymptotes)

### How can I use the derivative to identify local minimum & maximum points?

- The **nature** of a **stationary point** can be determined using the **derivative**
- For the function$f(x)$ …
- **STEP 1**
**Find** $f^{'}(x)$ and **solve** $f^{'}(x)=0$

  - The solutions are the the $x$-coordinates of any **stationary points**
- **STEP 2**
Find the **sign of the derivative** just either side of each stationary point

  - i.e. evaluate $f^{'}(x-h)$ and $f^{'}(x+h)$ for small$h$
  
    - Choose a convenient value for $h$
    - Just make sure you don't 'jump over' any other stationary points!

- At a **local minimum point**

  - the **derivative** changes from **negative** to **positive**
  - $f^{'}(x-h)<0,f^{'}(x)=0,f^{'}(x+h)>0$
- At a **local maximum point**

  - the **derivative** changes from **positive** to **negative**
  - $f^{'}(x-h)>0,f^{'}(x)=0,f^{'}(x+h)<0$ ![Stationary points of a cubic graph](assets/005827484d4a-7-2-4-stationary-points-incr-decr-min-max.png)
- If the derivative does **not change sign** at the point

  - (i.e. if it is positive on both sides or negative on both sides)
  - then the point is **not** a local minimum or a local maximum
  - But it is still a **stationary point** if $\mathrm{f}^{'} ( x ) = 0$ there

### What is the second derivative?

- It is possible to differentiate a function **more than once**

  - If you differentiate $y = \mathrm{f} ( x )$, you find its **(first) derivative**  $\frac{ \mathrm{d} y}{ \mathrm{d} x} = \mathrm{f}^{'} ( x )$
  
    - e.g. the (first) derivative of $2x^{3}$ is $6x^{2}$
  - Then you can differentiate the derivative **again** to find the **second derivative  **$\frac{ \mathrm{d}^{2} y}{ \mathrm{d} x^{2}} = \mathrm{f}^{''} ( x )$
  
    - e.g. the derivative of $6x^{2}$ is $12x$
    - so the second derivative of $2x^{3}$ is $12x$
- The **second derivative** can be used to test the **nature** of a **stationary point**

### How can I use the second derivative to identify local minimum & maximum points?

- **STEP 1**
**Find** $f^{'}(x)$ and **solve** $f^{'}(x)=0$

  - The solutions are the the $x$-coordinates of any **stationary points**
- **STEP 2**
Find the **second derivative** $\mathrm{f}^{''} ( x )$

  - Do this by differentiating $\mathrm{f}^{'} ( x )$ from Step 1
- **STEP 3**
Find the **value** of $\mathrm{f}^{''} ( x )$ at each of the **stationary points**

  - i.e., by **substituting** the $x$-coordinate of each point into $\mathrm{f}^{''} ( x )$

- **If ** $f^{''}(x)>0$

  - then the stationary point is a **local minimum**
- **If  **$f^{''}(x)<0$

  - then the stationary point is a **local maximum**
- **If  **$f^{''}(x)=0$

  - then the test **does not tell you anything**
  - the stationary point may be a **local maximum**, a **local minimum**, or **neither**
  - In this case, use the **first derivative test** instead

> **Exam Hint**
> - Don't just assume that a zero derivative corresponds to a maximum or minimum point
> 
>   - Especially if a question asks you to justify that a point is a maximum or minimum
> - The second derivative test is usually much quicker for identifying maximum and minimum points
> 
>   - But it is good to understand how to use the first derivative test as well
> - Your calculator may be able to show graphs of functions
> 
>   - You can use this to check your work

> **Worked Example**
> Find the coordinates and determine the nature of any stationary points on the graph of $y=f(x)$, where $f$ is the function defined by  $f(x)=2x^{3}-3x^{2}-36x+25$.
> 
> > *Start by finding *$\mathrm{f}^{'} ( x )$
> 
> $\mathrm{f}^{'} ( x ) = 6 x^{2} - 6 x - 36$
> 
> > *Solve *$\mathrm{f}^{'} ( x ) = 0$* to find the *$x$*-coordinates of any stationary points*
> 
> $\begin{gathered} 6 x^{2} - 6 x - 36 & = 0 \\ 6 ( x^{2} - x - 6 ) & = 0 \\ x^{2} - x - 6 & = 0 \\ ( x - 3 ) ( x + 2 ) & = 0 \end{gathered}$
> 
> $x=-2\mathrm{or}x=3$
> 
> > *Substitute into *$\mathrm{f} ( x )$* to find the corresponding *$y$*-coordinates*
> 
> $\begin{gathered} \mathrm{f} ( - 2 ) & = 2 ( - 2 )^{3} - 3 ( - 2 )^{2} - 36 ( - 2 ) + 25 \\ = - 16 - 12 + 72 + 25 \\ = 69 \end{gathered}$
> 
> $\begin{gathered} \mathrm{f} ( 3 ) & = 2 ( 3 )^{3} - 3 ( 3 )^{2} - 36 ( 3 ) + 25 \\ = 54 - 27 - 108 + 25 \\ = - 56 \end{gathered}$
> 
> > *So the stationary points are *$( - 2. 69 )$* and *$( 3 , - 56 )$
> 
> > *Method 1: using the second derivative to test the points*
> 
> > *Differentiate *$\mathrm{f}^{'} ( x )$* to find the second derivative *$\mathrm{f}^{''} ( x )$
> 
> $\begin{gathered} \mathrm{f}^{''} ( x ) & = \frac{ \mathrm{d} }{ \mathrm{d} x} ( 6 x^{2} - 6 x - 36 ) \\ = 12 x - 6 \end{gathered}$
> 
> > *Now substitute in the *$x$*-coordinates of the two stationary points*
> *This will give the value of the second derivative at those points*
> 
> $\mathrm{f}^{''} ( - 2 ) = 12 ( - 2 ) - 6 = - 30 < 0$
> 
> > *That is less than zero, so *$( - 2 , 69 )$* is a local maximum point*
> 
> $\mathrm{f}^{''} ( 3 ) = 12 ( 3 ) - 6 = 30 > 0$
> 
> > *That is greater than zero, so *$( 3 , - 56 )$* is a local minimum point*
> 
> > *Method 2: using the first derivative to test the points*
> 
> > *Test the values of *$\mathrm{f}^{'} ( x )$* at either side of the stationary points*
> *(Note that, where applicable, *$x=0$* is a very convenient test value!)*
> 
> $\begin{gathered} \mathrm{f}^{'} ( - 3 ) & = 6 ( - 3 )^{2} - 6 ( - 3 ) - 36 \\ = 54 + 18 - 36 \\ = 36 \\ > 0 \end{gathered}$
> 
> $\begin{gathered} \mathrm{f}^{'} ( 0 ) & = 6 ( 0 )^{2} - 6 ( 0 ) - 36 \\ = 0 + 0 - 36 \\ = - 36 \\ < 0 \end{gathered}$
> 
> $\begin{array}{rcl} \mathrm{f}^{'} ( 4 ) & = 6 ( 4 )^{2} - 6 ( 4 ) - 36 \\ = 96 - 24 - 36 \\ = 36 \\ > 0 \end{array}$
> 
> > *At  *$( - 2 , 69 )$*  the derivative changes from positive to negative, so that is a local maximum point*
> 
> > *At  *$( 3 , - 56 )$*  the derivative changes from negative to positive, so that is a local minimum point*
> 
> > *Note that for this function both stationary points are also turning points*
> 
> **Final answer:** $(-2,69)$**  is a local maximum point**
> 
> **Final answer:** $(3,-56)$**  is a local minimum point **
