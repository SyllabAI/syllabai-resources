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
  - But `straight f open parentheses x close parentheses` may reach a **lower** value further away
- A **local** **maximum** point, $(x,f(x))$

  - will have the **highest** value of $f(x)$ in the **local** vicinity of the $x$ value
  - But `straight f open parentheses x close parentheses` may reach a **higher** value further away
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
  - But it is still a **stationary point** if `straight f to the power of apostrophe open parentheses x close parentheses equals 0` there

### What is the second derivative?

- It is possible to differentiate a function **more than once**

  - If you differentiate `y equals straight f open parentheses x close parentheses`, you find its **(first) derivative**  `fraction numerator straight d y over denominator straight d x end fraction equals straight f to the power of apostrophe open parentheses x close parentheses`
  
    - e.g. the (first) derivative of $2x^{3}$ is $6x^{2}$
  - Then you can differentiate the derivative **again** to find the **second derivative  **`fraction numerator straight d squared y over denominator straight d x squared end fraction equals straight f to the power of apostrophe apostrophe end exponent open parentheses x close parentheses`
  
    - e.g. the derivative of $6x^{2}$ is $12x$
    - so the second derivative of $2x^{3}$ is $12x$
- The **second derivative** can be used to test the **nature** of a **stationary point**

### How can I use the second derivative to identify local minimum & maximum points?

- **STEP 1**
**Find** $f^{'}(x)$ and **solve** $f^{'}(x)=0$

  - The solutions are the the $x$-coordinates of any **stationary points**
- **STEP 2**
Find the **second derivative** `straight f to the power of apostrophe apostrophe end exponent open parentheses x close parentheses`

  - Do this by differentiating `straight f to the power of apostrophe open parentheses x close parentheses` from Step 1
- **STEP 3**
Find the **value** of `straight f to the power of apostrophe apostrophe end exponent open parentheses x close parentheses` at each of the **stationary points**

  - i.e., by **substituting** the $x$-coordinate of each point into `straight f to the power of apostrophe apostrophe end exponent open parentheses x close parentheses`

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
> > *Start by finding *`straight f to the power of apostrophe open parentheses x close parentheses`
> 
> `straight f to the power of apostrophe open parentheses x close parentheses equals 6 x squared minus 6 x minus 36`
> 
> > *Solve *`straight f to the power of apostrophe open parentheses x close parentheses equals 0`* to find the *$x$*-coordinates of any stationary points*
> 
> `table row cell 6 x squared minus 6 x minus 36 end cell equals 0 row cell 6 open parentheses x squared minus x minus 6 close parentheses end cell equals 0 row cell x squared minus x minus 6 end cell equals 0 row cell open parentheses x minus 3 close parentheses open parentheses x plus 2 close parentheses end cell equals 0 end table`
> 
> $x=-2\mathrm{or}x=3$
> 
> > *Substitute into *`straight f open parentheses x close parentheses`* to find the corresponding *$y$*-coordinates*
> 
> `table row cell straight f open parentheses negative 2 close parentheses end cell equals cell 2 open parentheses negative 2 close parentheses cubed minus 3 open parentheses negative 2 close parentheses squared minus 36 open parentheses negative 2 close parentheses plus 25 end cell row blank equals cell negative 16 minus 12 plus 72 plus 25 end cell row blank equals 69 end table`
> 
> `table row cell straight f open parentheses 3 close parentheses end cell equals cell 2 open parentheses 3 close parentheses cubed minus 3 open parentheses 3 close parentheses squared minus 36 open parentheses 3 close parentheses plus 25 end cell row blank equals cell 54 minus 27 minus 108 plus 25 end cell row blank equals cell negative 56 end cell end table`
> 
> > *So the stationary points are *`open parentheses negative 2. space 69 close parentheses`* and *`open parentheses 3 comma space minus 56 close parentheses`
> 
> > *Method 1: using the second derivative to test the points*
> 
> > *Differentiate *`straight f to the power of apostrophe open parentheses x close parentheses`* to find the second derivative *`straight f to the power of apostrophe apostrophe end exponent open parentheses x close parentheses`
> 
> `table row cell straight f to the power of apostrophe apostrophe end exponent open parentheses x close parentheses end cell equals cell fraction numerator straight d over denominator straight d x end fraction open parentheses 6 x squared minus 6 x minus 36 close parentheses end cell row blank equals cell 12 x minus 6 end cell end table`
> 
> > *Now substitute in the *$x$*-coordinates of the two stationary points*
> *This will give the value of the second derivative at those points*
> 
> `straight f to the power of apostrophe apostrophe end exponent open parentheses negative 2 close parentheses equals 12 open parentheses negative 2 close parentheses minus 6 equals negative 30 less than 0`
> 
> > *That is less than zero, so *`open parentheses negative 2 comma space 69 close parentheses`* is a local maximum point*
> 
> `straight f to the power of apostrophe apostrophe end exponent open parentheses 3 close parentheses equals 12 open parentheses 3 close parentheses minus 6 equals 30 greater than 0`
> 
> > *That is greater than zero, so *`open parentheses 3 comma space minus 56 close parentheses`* is a local minimum point*
> 
> > *Method 2: using the first derivative to test the points*
> 
> > *Test the values of *`straight f to the power of apostrophe open parentheses x close parentheses`* at either side of the stationary points*
> *(Note that, where applicable, *$x=0$* is a very convenient test value!)*
> 
> `table row cell straight f to the power of apostrophe open parentheses negative 3 close parentheses end cell equals cell 6 open parentheses negative 3 close parentheses squared minus 6 open parentheses negative 3 close parentheses minus 36 end cell row blank equals cell 54 plus 18 minus 36 end cell row blank equals 36 row blank greater than 0 end table`
> 
> `table row cell straight f to the power of apostrophe open parentheses 0 close parentheses end cell equals cell 6 open parentheses 0 close parentheses squared minus 6 open parentheses 0 close parentheses minus 36 end cell row blank equals cell 0 plus 0 minus 36 end cell row blank equals cell negative 36 end cell row blank less than 0 end table`
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row cell straight f to the power of apostrophe open parentheses 4 close parentheses end cell equals cell 6 open parentheses 4 close parentheses squared minus 6 open parentheses 4 close parentheses minus 36 end cell row blank equals cell 96 minus 24 minus 36 end cell row blank equals 36 row blank greater than 0 end table`
> 
> > *At  *`open parentheses negative 2 comma space 69 close parentheses`*  the derivative changes from positive to negative, so that is a local maximum point*
> 
> > *At  *`open parentheses 3 comma space minus 56 close parentheses`*  the derivative changes from negative to positive, so that is a local minimum point*
> 
> > *Note that for this function both stationary points are also turning points*
> 
> **Final answer:** $(-2,69)$**  is a local maximum point**
> 
> **Final answer:** $(3,-56)$**  is a local minimum point **
