# Mark Schemes — Polynomials
**Algebra & Functions** · Cambridge (CIE) A-LEVEL maths (9709)


## Exam Questions (65 questions)


### Q1
Both $( x - 2 )$ and $( x + 3 )$ are factors, so their product $( x - 2 ) ( x + 3 ) = x^{2} + x - 6$ divides $\text{f} ( x )$; divide to find the remaining quadratic

$x^{4} - 9 x^{3} + 9 x^{2} + 85 x - 150 = ( x^{2} + x - 6 ) ( x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$b + 1 = - 9 \Rightarrow b = - 10$

Compare the constant term

$- 6 c = - 150 \Rightarrow c = 25$

These give the quadratic factor

$\text{f} ( x ) = ( x^{2} + x - 6 ) ( x^{2} - 10 x + 25 )$

Factorise both quadratics; the second is a perfect square

$\text{f} ( x ) = ( x - 2 ) ( x + 3 ) ( x - 5 )^{2}$

**[A1]**

Set each factor to zero; the repeated factor $( x - 5 )^{2}$ gives a point where the curve touches the axis, the others where it crosses

$\text{crosses at} ( - 3 , 0 ) \text{and} ( 2 , 0 ) , \text{touches at} ( 5 , 0 )$

**[B1]**

Find the $y$-intercept by substituting $x = 0$

$( 0 , - 150 )$

**[B1]**

The coefficient of $x^{4}$ is positive, so the curve falls from the upper left and rises to the upper right; draw it crossing at $- 3$ and $2$ and touching at $5$

![Sketch of a positive quartic that crosses the x-axis at (-3, 0) and (2, 0), touches the x-axis at (5, 0), and crosses the y-axis at (0, -150). The curve comes down from upper left, dips below the axis between -3 and 2, rises to touch at (5, 0), then rises again. Not drawn to scale](assets/001-sketch-of-a-positive-quartic-that-crosses-the-x-.png)

**[B1]**

> **[exam-tip]**
> The squared factor $( x - 5 )^{2}$ is the key: a repeated root means the curve *touches* the $x$-axis there rather than crossing it. Miss that and your sketch has the wrong shape even with every coordinate correct.

> **[mark-scheme]**
> **M1**: Using the product $( x - 2 ) ( x + 3 )$ as a quadratic factor and dividing (or comparing coefficients) to find the remaining quadratic.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x - 2 ) ( x + 3 ) ( x - 5 )^{2}$.
> 
> **B1**: All three $x$-axis points correct: crosses at $( - 3 , 0 )$ and $( 2 , 0 )$, touches at $( 5 , 0 )$.
> 
> **B1**: The $y$-intercept $( 0 , - 150 )$.
> 
> **B1**: Correct positive-quartic shape, crossing at the two single roots and touching (not crossing) at the repeated root. A curve that crosses at $( 5 , 0 )$ does not earn this mark.

### Q2
Look for a factor; testing $x = - 2$ gives $4 ( - 8 ) + 17 ( 4 ) + 20 ( - 2 ) + 4 = 0$, so $( x + 2 )$ is a factor. Divide it out, writing the cubic as $( x + 2 )$ multiplied by an unknown quadratic

$4 x^{3} + 17 x^{2} + 20 x + 4 = ( x + 2 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 4$

Compare the constant term

$2 c = 4 \Rightarrow c = 2$

Compare the coefficient of $x^{2}$

$2 a + b = 17 \Rightarrow b = 9$

These give the quadratic factor

$4 x^{3} + 17 x^{2} + 20 x + 4 = ( x + 2 ) ( 4 x^{2} + 9 x + 2 )$

**[A1]**

Factorise the quadratic; $4 \times 2 = 8$, and $8$ and $1$ multiply to $8$ and add to $9$

$4 x^{2} + 9 x + 2 = ( 4 x + 1 ) ( x + 2 )$

Combine, noting that $( x + 2 )$ now appears twice

$4 x^{3} + 17 x^{2} + 20 x + 4 = ( 4 x + 1 ) ( x + 2 )^{2}$

**[A1]**

> **[mark-scheme]**
> **M1**: Finding a factor (e.g. $( x + 2 )$) and dividing to reach a quadratic factor, or comparing coefficients.
> 
> **A1**: Correct quadratic factor $4 x^{2} + 9 x + 2$.
> 
> **A1**: Fully factorised $( 4 x + 1 ) ( x + 2 )^{2}$, in any order. The square must be shown, so $( 4 x + 1 ) ( x + 2 )$ alone is not fully factorised.
From part (a) the factors give the $x$-axis behaviour: a crossing where $4 x + 1 = 0$ and a touch where $( x + 2 )^{2} = 0$

`\text{crosses at } \left(-\frac{1}{4}, 0\right), \text{ touches at } (-2, 0)`

Find the $y$-intercept by substituting $x = 0$, then draw a positive cubic through these points

$( 0 , 4 )$

![Sketch of a positive cubic that touches the x-axis at (-2, 0), crosses it at (negative one quarter, 0), and crosses the y-axis at (0, 4). The curve rises from lower left to touch at (-2, 0), dips slightly, then rises through the crossing and continues up to the right](assets/002-sketch-of-a-positive-cubic-that-touches-the-x-ax.png)

**[B1 B1]**

> **[mark-scheme]**
> **B1**: All axis points correct and labelled: touches at $( - 2 , 0 )$, crosses at `\left(-\frac{1}{4}, 0\right)`, $y$-intercept $( 0 , 4 )$.
> 
> **B1**: Correct positive-cubic shape, touching (not crossing) at $( - 2 , 0 )$ and crossing at `\left(-\frac{1}{4}, 0\right)`. Follow through from part (a)'s factors.

### Q3
To find where the curve crosses the $x$-axis, factorise the cubic; the crossings do not depend on the factor of $\frac{1}{4}$

Test values to find a factor: $x = 2$ gives $( 2 )^{3} - 5 ( 2 )^{2} - 12 ( 2 ) + 36 = 0$, so $( x - 2 )$ is a factor

$x^{3} - 5 x^{2} - 12 x + 36 = ( x - 2 ) ( x^{2} + b x + c )$

Compare the coefficient of $x^{2}$

$b - 2 = - 5 \Rightarrow b = - 3$

Compare the constant term

$- 2 c = 36 \Rightarrow c = - 18$

Factorise the quadratic $x^{2} - 3 x - 18$; $- 6$ and $3$ multiply to $- 18$ and add to $- 3$

$x^{3} - 5 x^{2} - 12 x + 36 = ( x - 2 ) ( x - 6 ) ( x + 3 )$

**[M1]**

The curve crosses the $x$-axis where each factor is zero

$( - 3 , 0 ) ,  ( 2 , 0 ) ,  ( 6 , 0 )$

**[A1]**

Find the cubic's $y$-intercept; because $4 y = 36$ at $x = 0$, divide by $4$

$( 0 , 9 )$

**[B1]**

Rearrange the line to $y = 6 - x$; it has negative gradient and crosses the axes at $( 6 , 0 )$ and $( 0 , 6 )$

**[B1]**

Find the intersections by setting $6 - x = \frac{1}{4} ( x^{3} - 5 x^{2} - 12 x + 36 )$ and clearing the fraction

$24 - 4 x = x^{3} - 5 x^{2} - 12 x + 36$

$x^{3} - 5 x^{2} - 8 x + 12 = 0$

**[M1]**

To solve, factorise; $x = 6$ is already known to lie on both graphs, so $( x - 6 )$ is a factor. Divide by it, writing the cubic as $( x - 6 )$ times a quadratic

$x^{3} - 5 x^{2} - 8 x + 12 = ( x - 6 ) ( x^{2} + b x + c )$

Compare the coefficient of $x^{2}$

$b - 6 = - 5 \Rightarrow b = 1$

Compare the constant term

$- 6 c = 12 \Rightarrow c = - 2$

Factorise the quadratic $x^{2} + x - 2$; $2$ and $- 1$ multiply to $- 2$ and add to $1$

$( x - 6 ) ( x - 1 ) ( x + 2 ) = 0 \Rightarrow x = 6 ,  1 ,  - 2$

**[A1]**

Substitute each into the line $y = 6 - x$ to get the intersection points

$( 6 , 0 ) ,  ( 1 , 5 ) ,  ( - 2 , 8 )$

**[A1]**

Draw both graphs on one diagram: a positive cubic through its three crossings and $y$-intercept, and the descending line, meeting at the three intersection points

![Sketch of a positive cubic and a descending straight line on the same diagram. The cubic crosses the x-axis at (-3, 0), (2, 0) and (6, 0) and the y-axis at (0, 9). The line y = 6 - x crosses the x-axis at (6, 0) and the y-axis at (0, 6). The two graphs meet at (-2, 8), (1, 5) and (6, 0)](assets/003-sketch-of-a-positive-cubic-and-a-descending-stra.png)

**[B1 B1]**

> **[exam-tip]**
> Two things may trip people here. First, the cubic is written as $4 y = \dots$, so every $y$-value is a quarter of the cubic expression, making the $y$-intercept $9$, not $36$.
> 
> Secondly the point $( 6 , 0 )$ does three things: it is a crossing of the cubic, the $x$-intercept of the line, and one of the three intersections. Spotting that gives you a factor of the intersection cubic for free.

> **[mark-scheme]**
> **M1**: Factorising the cubic $x^{3} - 5 x^{2} - 12 x + 36$.
> 
> **A1**: Correct cubic crossings $( - 3 , 0 )$, $( 2 , 0 )$, $( 6 , 0 )$.
> 
> **B1**: The cubic's $y$-intercept $( 0 , 9 )$, with the division by $4$ applied.
> 
> **B1**: The line drawn correctly with negative gradient, crossing at $( 6 , 0 )$ and $( 0 , 6 )$.
> 
> **M1**: Setting the two expressions equal and reaching $x^{3} - 5 x^{2} - 8 x + 12 = 0$.
> 
> **A1**: Factorising and solving for all three $x$-values $6 , 1 , - 2$.
> 
> **A1**: All three intersection points $( 6 , 0 )$, $( 1 , 5 )$, $( - 2 , 8 )$ as coordinate pairs.
> 
> **B1**: Correct positive-cubic shape drawn on the same diagram as the line.
> 
> **B1**: A fully correct diagram with both graphs, all axis crossings and all three intersections labelled.

### Q4
Test values to find a factor of the cubic: $x = 1$ gives $( 1 )^{3} - 3 ( 1 )^{2} - 6 ( 1 ) + 8 = 0$, so $( x - 1 )$ is a factor

Divide by $( x - 1 )$, writing the cubic as $( x - 1 )$ multiplied by an unknown quadratic

$x^{3} - 3 x^{2} - 6 x + 8 = ( x - 1 ) ( x^{2} + b x + c )$

Compare the coefficient of $x^{2}$

$b - 1 = - 3 \Rightarrow b = - 2$

Compare the constant term

$- c = 8 \Rightarrow c = - 8$

Factorise the quadratic $x^{2} - 2 x - 8$; $- 4$ and $2$ multiply to $- 8$ and add to $- 2$

$x^{3} - 3 x^{2} - 6 x + 8 = ( x - 1 ) ( x - 4 ) ( x + 2 )$

**[M1]**

Set each factor to zero to find where the curve crosses the $x$-axis

$( - 2 , 0 ) ,  ( 1 , 0 ) ,  ( 4 , 0 )$

**[A1]**

Find the cubic's $y$-intercept by substituting $x = 0$

$( 0 , 8 )$

**[B1]**

For $y = \frac{3}{x^{2}}$, note that $x^{2} > 0$ for all $x \neq 0$, so the graph lies entirely above the $x$-axis in two branches, with the $y$-axis ($x = 0$) and the $x$-axis as asymptotes; draw it on the same diagram as the cubic

![Sketch of a positive cubic and the reciprocal curve y = 3 over x squared on the same diagram. The cubic crosses the x-axis at (-2, 0), (1, 0) and (4, 0) and the y-axis at (0, 8). The reciprocal curve has two branches, both above the x-axis, approaching the y-axis as a vertical asymptote and the x-axis as a horizontal asymptote. The two graphs cross three times, twice on the left branch and once on the far right](assets/004-sketch-of-a-positive-cubic-and-the-reciprocal-cu.png)

**[B1]**

> **[mark-scheme]**
> **M1**: Factorising the cubic $x^{3} - 3 x^{2} - 6 x + 8$.
> 
> **A1**: Correct cubic crossings $( - 2 , 0 )$, $( 1 , 0 )$ and $( 4 , 0 )$, with a correct positive-cubic shape.
> 
> **B1**: The $y$-intercept $( 0 , 8 )$ labelled.
> 
> **B1**: A correct $y = \frac{3}{x^{2}}$: two branches, both above the $x$-axis, with the $y$-axis and $x$-axis as asymptotes, drawn on the same diagram.
Divide both sides by $x^{2}$; this is valid because $x = 0$ is not a solution (the left-hand side would be $0$, not $3$)

$x^{3} - 3 x^{2} - 6 x + 8 = \frac{3}{x^{2}}$

The two sides are exactly the two graphs from part (a)

![Sketch of a positive cubic and the reciprocal curve y = 3 over x squared on the same diagram. The cubic crosses the x-axis at (-2, 0), (1, 0) and (4, 0) and the y-axis at (0, 8). The reciprocal curve has two branches, both above the x-axis, approaching the y-axis as a vertical asymptote and the x-axis as a horizontal asymptote. The two graphs cross three times, twice on the left branch and once on the far right](assets/004-sketch-of-a-positive-cubic-and-the-reciprocal-cu.png)

The number of solutions is the number of times those graphs cross

$3$

**[B1]**

> **[mark-scheme]**
> **B1**: $3$, following from a correct part (a) sketch. The count follows through from the candidate's own diagram; award the mark if their sketch clearly shows that many intersections and the reasoning (divide by $x^{2}$, read off the graphs) is sound, even if their graph is slightly inaccurate.

### Q5
Look for a factor; testing $x = - 2$ gives $3 ( - 8 ) + 2 ( 4 ) - 3 ( - 2 ) + 10 = 0$, so $( x + 2 )$ is a factor. Divide it out

$3 x^{3} + 2 x^{2} - 3 x + 10 = ( x + 2 ) ( 3 x^{2} - 4 x + 5 )$

**[M1]**

Check whether the quadratic factor gives further crossings by evaluating its discriminant

$b^{2} - 4 a c = ( - 4 )^{2} - 4 ( 3 ) ( 5 ) = 16 - 60 = - 44$

Since the discriminant is negative, $3 x^{2} - 4 x + 5$ has no real roots, so the only crossing is where $x + 2 = 0$

$( - 2 , 0 )$

**[A1]**

Find the $y$-intercept by substituting $x = 0$

$( 0 , 10 )$

**[B1]**

The coefficient of $x^{3}$ is positive, so the curve rises from lower left to upper right, crossing the axis only at $( - 2 , 0 )$

![Sketch of a positive cubic crossing the x-axis once at (-2, 0) and the y-axis at (0, 10). To the right of the crossing the curve has a shallow local maximum and local minimum but both stay above the x-axis, so there are no further crossings](assets/005-sketch-of-a-positive-cubic-crossing-the-x-axis-o.png)

**[B1]**

> **[exam-tip]**
> A positive cubic can cross the $x$-axis once, twice or three times. Once you have one factor, check the quadratic that is left: a negative discriminant means it never reaches the axis, so there is exactly one crossing.

> **[mark-scheme]**
> **M1**: Finding the factor $( x + 2 )$ and dividing to reach the quadratic factor $3 x^{2} - 4 x + 5$.
> 
> **A1**: Establishing $( - 2 , 0 )$ as the only $x$-axis crossing, supported by showing the quadratic factor has a negative discriminant (or equivalent reasoning that it has no real roots).
> 
> **B1**: The $y$-intercept $( 0 , 10 )$.
> 
> **B1**: Correct positive-cubic shape crossing the $x$-axis exactly once, at $( - 2 , 0 )$. A sketch showing extra crossings does not earn this mark.

### Q6
The graphs meet where their $y$-values are equal, so set the two expressions equal

$x^{3} - x^{2} - 4 x + 4 = 2 x + 4$

**[M1]**

Rearrange so that one side is zero; the constant terms cancel

$x^{3} - x^{2} - 6 x = 0$

**[A1]**

Every term has a factor of $x$, so take it out and factorise the quadratic

$x ( x^{2} - x - 6 ) = 0$

$x ( x - 3 ) ( x + 2 ) = 0$

**[M1]**

Set each factor to zero to get the three $x$-values

$x = 0 ,  3 ,  - 2$

Substitute each into the line $y = 2 x + 4$, which is the simpler of the two equations

$( 0 , 4 ) ,  ( 3 , 10 ) ,  ( - 2 , 0 )$

**[A1]**

> **[exam-tip]**
> Substitute back into the line rather than the cubic, as it is far less work and both must give the same answer.

> **[mark-scheme]**
> **M1**: Setting the two expressions for $y$ equal to each other.
> 
> **A1**: Correct simplified cubic equal to zero, $x^{3} - x^{2} - 6 x = 0$.
> 
> **M1**: Taking out the factor of $x$ and factorising the resulting quadratic (or otherwise solving for all three roots).
> 
> **A1**: All three points $( 0 , 4 )$, $( 3 , 10 )$ and $( - 2 , 0 )$, as coordinate pairs. Accept them in any order. $x$-values alone, without the matching $y$-values, do not score this mark.
The line $y = 2 x + 4$ has gradient $2$; it crosses the axes at $( - 2 , 0 )$ and $( 0 , 4 )$

**[B1]**

To find where the curve crosses the $x$-axis, factorise the cubic by grouping the terms in pairs

$x^{3} - x^{2} - 4 x + 4 = x^{2} ( x - 1 ) - 4 ( x - 1 )$

Take out the common factor of $( x - 1 )$

$= ( x - 1 ) ( x^{2} - 4 )$

Factorise the difference of two squares

$= ( x - 1 ) ( x - 2 ) ( x + 2 )$

The curve crosses the $x$-axis where each factor is zero

$( - 2 , 0 ) ,  ( 1 , 0 ) ,  ( 2 , 0 )$

**[B1]**

Find the curve's $y$-intercept by substituting $x = 0$

$( 0 , 4 )$

**[B1]**

The coefficient of $x^{3}$ is positive, so the curve rises from lower left to upper right; draw both graphs on one diagram and mark the three intersection points found in part (a)

![Sketch of a positive cubic and a straight line on the same diagram. The cubic crosses the x-axis at (-2, 0), (1, 0) and (2, 0) and the y-axis at (0, 4). The straight line crosses the x-axis at (-2, 0) and the y-axis at (0, 4). The two graphs meet at (-2, 0), (0, 4) and (3, 10)](assets/006-sketch-of-a-positive-cubic-and-a-straight-line-o.png)

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Correct straight line with positive gradient, crossing at $( - 2 , 0 )$ and $( 0 , 4 )$.
> 
> **B1**: The curve's three $x$-axis crossings $( - 2 , 0 )$, $( 1 , 0 )$ and $( 2 , 0 )$, correct and labelled.
> 
> **B1**: The curve's $y$-intercept $( 0 , 4 )$, correct and labelled.
> 
> **B1**: Correct shape of a positive cubic, drawn on the same diagram as the line.
> 
> **B1**: All three intersection points $( - 2 , 0 )$, $( 0 , 4 )$ and $( 3 , 10 )$ labelled, following through from part (a). The first two coincide with the axis crossings already labelled, so a single label at each of those points is enough.

### Q7
Since $( x + 1 )$ is a factor, divide the cubic by it; write it as $( x + 1 )$ multiplied by an unknown quadratic

$x^{3} - 4 x^{2} + x + 6 = ( x + 1 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 1$

Compare the constant term

$c = 6$

Compare the coefficient of $x^{2}$

$a + b = - 4 \Rightarrow b = - 5$

These give the quadratic factor

$x^{3} - 4 x^{2} + x + 6 = ( x + 1 ) ( x^{2} - 5 x + 6 )$

Factorise the quadratic, using two numbers that multiply to $6$ and add to $- 5$, namely $- 2$ and $- 3$

$x^{3} - 4 x^{2} + x + 6 = ( x + 1 ) ( x - 2 ) ( x - 3 )$

**[A1]**

Set each factor to zero to find where the curve crosses the $x$-axis

$( - 1 , 0 ) ,  ( 2 , 0 ) ,  ( 3 , 0 )$

**[B1]**

Find the $y$-intercept by substituting $x = 0$

$y = ( 0 + 1 ) ( 0 - 2 ) ( 0 - 3 ) = 6$

$( 0 , 6 )$

The coefficient of $x^{3}$ is positive, so the curve rises from lower left to upper right; draw it through the four points

![Sketch of a positive cubic crossing the x-axis at (-1, 0), (2, 0) and (3, 0), and crossing the y-axis at (0, 6), with a local maximum just to the right of the y-axis and a local minimum between x = 2 and x = 3](assets/007-sketch-of-a-positive-cubic-crossing-the-x-axis-a.png)

**[B1]**

> **[mark-scheme]**
> **M1**: Writing the cubic as $( x + 1 ) ( a x^{2} + b x + c )$ and comparing coefficients, or dividing by $( x + 1 )$ by long division.
> 
> **A1**: Fully factorised $( x + 1 ) ( x - 2 ) ( x - 3 )$, factors in any order.
> 
> **B1**: All three $x$-axis crossings $( - 1 , 0 )$, $( 2 , 0 )$ and $( 3 , 0 )$, correct and labelled.
> 
> **B1**: Correct positive-cubic shape through those crossings with the $y$-intercept $( 0 , 6 )$ labelled. Stationary points are not required, as the question says.

### Q8
By the factor theorem, $( x + 3 )$ is a factor exactly when $\text{f} ( - 3 ) = 0$, so evaluate $\text{f} ( - 3 )$

$\text{f} ( - 3 ) = 6 ( - 3 )^{3} + 23 ( - 3 )^{2} + 11 ( - 3 ) - 12$

$= - 162 + 207 - 33 - 12 = 0$

$\text{f} ( - 3 ) = 0 \text{, so} ( x + 3 ) \text{is a factor}$

**[B1]**

Now divide $\text{f} ( x )$ by $( x + 3 )$; write $\text{f} ( x )$ as $( x + 3 )$ multiplied by an unknown quadratic

$6 x^{3} + 23 x^{2} + 11 x - 12 = ( x + 3 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 6$

Compare the constant term

$3 c = - 12 \Rightarrow c = - 4$

Compare the coefficient of $x^{2}$

$3 a + b = 23 \Rightarrow b = 5$

These give the quadratic factor

$\text{f} ( x ) = ( x + 3 ) ( 6 x^{2} + 5 x - 4 )$

Factorise the quadratic; $6 \times ( - 4 ) = - 24$, and $8$ and $- 3$ multiply to $- 24$ and add to $5$

$6 x^{2} + 5 x - 4 = ( 2 x - 1 ) ( 3 x + 4 )$

$\text{f} ( x ) = ( x + 3 ) ( 2 x - 1 ) ( 3 x + 4 )$

**[A1]**

> **[mark-scheme]**
> **B1**: Substituting $x = - 3$ and reaching $0$, which shows $( x + 3 )$ is a factor. A written conclusion is good practice but is not required for the mark; an arithmetic slip loses it even if the last line reads $0$.
> 
> **M1**: Writing $\text{f} ( x ) = ( x + 3 ) ( a x^{2} + b x + c )$ and comparing coefficients, or dividing by $( x + 3 )$ by long division.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x + 3 ) ( 2 x - 1 ) ( 3 x + 4 )$, factors in any order. Accept the equivalent `3(x+3)(2x-1)\left(x+\frac{4}{3}\right)` or similar, provided it multiplies back to $\text{f} ( x )$.
Set each factor from part (a) to zero to find where the curve crosses the $x$-axis

`(-3, 0), \; \left(-\frac{4}{3}, 0\right), \; \left(\frac{1}{2}, 0\right)`

**[B1]**

Find the $y$-intercept by substituting $x = 0$

$y = ( 0 + 3 ) ( 2 ( 0 ) - 1 ) ( 3 ( 0 ) + 4 ) = - 12$

$( 0 , - 12 )$

**[B1]**

The coefficient of $x^{3}$ is positive, so the curve rises from lower left to upper right; draw it through the four points

![Sketch of a positive cubic crossing the x-axis at (-3, 0), (negative four thirds, 0) and (one half, 0), and crossing the y-axis at (0, -12), with a local maximum between x = -3 and x = negative four thirds and a local minimum between x = negative four thirds and x = one half](assets/008-sketch-of-a-positive-cubic-crossing-the-x-axis-a.png)

**[B1 B1]**

> **[mark-scheme]**
> **B1**: All three $x$-axis crossings $( - 3 , 0 )$, `\left(-\frac{4}{3}, 0\right)` and `\left(\frac{1}{2}, 0\right)`, correct and labelled. Follow through from part (a)'s factors.
> 
> **B1**: The $y$-intercept $( 0 , - 12 )$, correct and labelled.
> 
> **B1**: Correct shape of a positive cubic (down to the left, up to the right).
> 
> **B1**: A fully correct curve crossing the axis at all three points, with a local maximum then a local minimum in the right places.

### Q9
By the factor theorem, $( x + 2 )$ is a factor exactly when the value at $x = - 2$ is zero, so evaluate it there

$2 ( - 2 )^{3} - 3 ( - 2 )^{2} - 11 ( - 2 ) + 6 = - 16 - 12 + 22 + 6 = 0$

**[B1]**

Since the result is zero, the factor theorem confirms the factor

$( x + 2 ) \text{is a factor}$

> **[mark-scheme]**
> **B1**: Substituting $x = - 2$ and reaching $0$, which shows $( x + 2 )$ is a factor. A written conclusion is good practice but not required. The working must be correct throughout — an arithmetic slip loses the mark even if the last line reads $0$.
Since $( x + 2 )$ is a factor, divide the cubic by it; write it as $( x + 2 )$ multiplied by an unknown quadratic

$2 x^{3} - 3 x^{2} - 11 x + 6 = ( x + 2 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 2$

Compare the constant term

$2 c = 6 \Rightarrow c = 3$

Compare the coefficient of $x^{2}$

$2 a + b = - 3 \Rightarrow b = - 7$

These give the quadratic factor

$2 x^{3} - 3 x^{2} - 11 x + 6 = ( x + 2 ) ( 2 x^{2} - 7 x + 3 )$

Factorise the quadratic

$( x + 2 ) ( 2 x - 1 ) ( x - 3 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing the cubic as $( x + 2 ) ( a x^{2} + b x + c )$ and comparing coefficients, or dividing by $( x + 2 )$ by long division.
> 
> **A1**: Fully factorised $( x + 2 ) ( 2 x - 1 ) ( x - 3 )$, factors in any order.
The coefficient of $x^{3}$ is positive, so the curve rises from lower left to upper right

Set each factor to zero to find where the curve crosses the $x$-axis

$( - 2 , 0 ) ,  ( \frac{1}{2} , 0 ) ,  ( 3 , 0 )$

**[B1]**

Find the $y$-intercept by substituting $x = 0$

$y = ( 0 + 2 ) ( 2 ( 0 ) - 1 ) ( 0 - 3 ) = 6$

$( 0 , 6 )$

**[B1]**

Draw a positive cubic passing through these four points

![Sketch of a positive cubic crossing the x-axis at (-2, 0), (one half, 0) and (3, 0), and crossing the y-axis at (0, 6), with a local maximum between x = -2 and x = one half and a local minimum between x = one half and x = 3](assets/009-sketch-of-a-positive-cubic-crossing-the-x-axis-a.png)

**[B1 B1]**

> **[mark-scheme]**
> **B1**: The three $x$-axis crossings $( - 2 , 0 )$, $( \frac{1}{2} , 0 )$ and $( 3 , 0 )$, correct and labelled.
> 
> **B1**: The $y$-intercept $( 0 , 6 )$, correct and labelled.
> 
> **B1**: Correct shape of a positive cubic (up to the right, down to the left).
> 
> **B1**: A fully correct curve crossing the axis at all three points with a local maximum then a local minimum.

### Q10
Apply the factor theorem: $( x - 2 )$ is a factor exactly when $\text{f} ( 2 ) = 0$, so evaluate $\text{f} ( 2 )$

$\text{f} ( 2 ) = ( 2 )^{3} - 2 ( 2 )^{2} - 4 ( 2 ) + 8$

**[M1]**

Work out the arithmetic

$8 - 8 - 8 + 8 = 0$

$\text{f} ( 2 ) = 0 \text{, so} ( x - 2 ) \text{is a factor}$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = 2$ into $\text{f} ( x )$.
> 
> **A1**: Reaching $\text{f} ( 2 ) = 0$ with no errors, which is sufficient to show the factor. A written conclusion is good practice but is not required for the mark.
Since $( x - 2 )$ is a factor, divide $\text{f} ( x )$ by it; write $\text{f} ( x )$ as $( x - 2 )$ multiplied by an unknown quadratic

$x^{3} - 2 x^{2} - 4 x + 8 = ( x - 2 ) ( x^{2} + b x + c )$

**[M1]**

Compare the constant term

$- 2 c = 8 \Rightarrow c = - 4$

Compare the coefficient of $x^{2}$

$b - 2 = - 2 \Rightarrow b = 0$

These give the quadratic factor

$\text{f} ( x ) = ( x - 2 ) ( x^{2} - 4 )$

Factorise the difference of two squares

$\text{f} ( x ) = ( x - 2 ) ( x - 2 ) ( x + 2 ) = ( x - 2 )^{2} ( x + 2 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Dividing $\text{f} ( x )$ by $( x - 2 )$ (long division or inspection) to obtain the quadratic factor $x^{2} - 4$.
> 
> **A1**: Fully factorised $( x - 2 )^{2} ( x + 2 )$, accepting $( x - 2 ) ( x - 2 ) ( x + 2 )$, in any order.
The coefficient of $x^{3}$ is positive, so the curve rises from lower left to upper right

The repeated factor $( x - 2 )^{2}$ gives a point where the curve touches the axis, and $( x + 2 )$ a point where it crosses

$( 2 , 0 ) \text{and} ( - 2 , 0 )$

**[B1]**

Find the $y$-intercept by substituting $x = 0$

$y = ( 0 - 2 )^{2} ( 0 + 2 ) = 8$

$( 0 , 8 )$

**[B1]**

Draw a positive cubic through these points, touching the $x$-axis at $( 2 , 0 )$

![Sketch of a positive cubic touching the x-axis at (2, 0), crossing the x-axis at (-2, 0), and crossing the y-axis at (0, 8), with a local maximum between x = -2 and x = 2 and a local minimum at (2, 0)](assets/010-sketch-of-a-positive-cubic-touching-the-x-axis-a.png)

**[B1]**

> **[mark-scheme]**
> **B1**: Both $x$-axis points, $( - 2 , 0 )$ crossing and $( 2 , 0 )$ touching, correct.
> 
> **B1**: $y$-intercept $( 0 , 8 )$.
> 
> **B1**: Correct positive cubic shape that touches at $( 2 , 0 )$ and crosses at $( - 2 , 0 )$.

### Q11
(i)

The divisor is the expression the polynomial is divided by

$x - 2$

**[B1]**

(ii)

The quotient is the polynomial part of the result

$A x + B$

**[B1]**

(iii)

The remainder is the constant left over, sitting on top of the divisor

$C$

**[B1]**

> **[mark-scheme]**
> **B1**: Divisor $x - 2$.
> 
> **B1**: Quotient $A x + B$.
> 
> **B1**: Remainder $C$.
**Method 1 - Long Division**

Divide $x^{2} - 8 x - 20$ by $( x - 2 )$ to find the quotient and remainder

![Long division tableau dividing x squared minus 8x minus 20 by x minus 2, giving quotient x minus 6 and remainder minus 32](assets/011-long-division-tableau-dividing-x-squared-minus-8.png)

**[M1]**

Match the quotient $x - 6$ to $A x + B$ and the remainder to $C$

$x^{2} - 8 x - 20 = ( x - 2 ) ( x - 6 ) - 32$

$A = 1 ,  B = - 6 ,  C = - 32$

**[A1 A1 A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $x^{2} - 8 x - 20$ by $( x - 2 )$, by any valid method.
> 
> **A1**: $A = 1$.
> 
> **A1**: $B = - 6$.
> 
> **A1**: $C = - 32$. The quotient and remainder must be identified correctly; swapping them loses the accuracy marks.

**Method 2 - Inspection**

Expand the given identity so the coefficients can be compared

$x^{2} - 8 x - 20 = ( x - 2 ) ( A x + B ) + C$

**[M1]**

Compare the coefficients of $x^{2}$

$A = 1$

**[A1]**

Compare the coefficients of $x$

$B - 2 A = - 8 \Rightarrow B = - 6$

**[A1]**

Compare the constant terms

$C - 2 B = - 20 \Rightarrow C = - 32$

**[A1]**

$A = 1 ,  B = - 6 ,  C = - 32$

> **[mark-scheme]**
> **M1**: Writing $x^{2} - 8 x - 20 = ( x - 2 ) ( A x + B ) + C$ and comparing coefficients.
> 
> **A1**: $A = 1$.
> 
> **A1**: $B = - 6$.
> 
> **A1**: $C = - 32$.

### Q12
**Method 1 - Remainder Theorem**

By the remainder theorem, the remainder on dividing by $( x + 4 )$ is the value of the polynomial at $x = - 4$, so evaluate it there

$( - 4 )^{3} - 7 ( - 4 ) - 6$

**[M1]**

Work out the arithmetic

$- 64 + 28 - 6$

$- 42$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the remainder theorem, substituting $x = - 4$ into the polynomial (or commencing long division by $( x + 4 )$).
> 
> **A1**: Correct remainder $- 42$. A bare value with no substitution or division seen does not score.

**Method 2 - Long Division**

Divide the polynomial by $( x + 4 )$, writing the missing $x^{2}$ term as $0 x^{2}$ so that the columns line up; the number left at the foot of the division is the remainder

![Long division tableau dividing x cubed minus 7x minus 6 by x plus 4, giving quotient x squared minus 4x plus 9 and a remainder of minus 42](assets/012-long-division-tableau-dividing-x-cubed-minus-7x-.png)

**[M1]**

The final line of the division is the remainder

$- 42$

**[A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $x^{3} - 7 x - 6$ by $( x + 4 )$ and working through to the constant left at the foot.
> 
> **A1**: Correct remainder $- 42$.

### Q13
**Method 1 - Long Division**

Set the division out as a bus-stop, dividing the cubic by $( x + 2 )$ and working down through the powers of $x$, subtracting at each stage

![Long division tableau dividing x cubed plus 6x squared plus 11x plus 6 by x plus 2, with quotient x squared plus 4x plus 3 written above, each subtracted line shown in brackets with its underline, and a final remainder of zero](assets/013-long-division-tableau-dividing-x-cubed-plus-6x-s.png)

**[M1]**

The final subtraction leaves zero, so there is no remainder, and the quotient is read from the top of the tableau

$x^{2} + 4 x + 3$

**[A1 A1]**

> **[mark-scheme]**
> **M1**: Beginning a correct division of $x^{3} + 6 x^{2} + 11 x + 6$ by $( x + 2 )$, by any valid method, and reaching a leading quotient term $x^{2}$.
> 
> **A1**: Correct quotient $x^{2} + 4 x + 3$.
> 
> **A1**: Zero remainder, confirming that $( x + 2 )$ divides exactly.

**Method 2 - Inspection**

Since a cubic divided by a linear expression leaves a quadratic, write the cubic as the divisor multiplied by an unknown quadratic

$x^{3} + 6 x^{2} + 11 x + 6 = ( x + 2 ) ( x^{2} + b x + c )$

**[M1]**

Expand the right hand side and compare the coefficients of $x^{2}$ to find $b$

$b + 2 = 6 \Rightarrow b = 4$

**[A1]**

Compare the constant terms to find $c$

$2 c = 6 \Rightarrow c = 3$

The coefficient of $x$ then agrees as a check, since $c + 2 b = 3 + 8 = 11$, so the division is exact

$x^{2} + 4 x + 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $x^{3} + 6 x^{2} + 11 x + 6 = ( x + 2 ) ( x^{2} + b x + c )$ and comparing coefficients (an equally valid method of division).
> 
> **A1**: Correct $b = 4$.
> 
> **A1**: Correct $c = 3$, giving quotient $x^{2} + 4 x + 3$ with zero remainder.

### Q14
Since $\text{f} ( 3 ) = 0$, substitute $x = 3$ into $\text{f} ( x )$ and set the result to zero

$9 + 3 a + b = 0$

**[M1]**

Do the same with $\text{f} ( - 8 ) = 0$, giving two simultaneous equations

$3 a + b = - 9$

$- 8 a + b = - 64$

**[A1]**

Subtract the equations to eliminate $b$

$11 a = 55 \Rightarrow a = 5$

**[M1]**

Substitute $a = 5$ back to find $b$

$b = - 9 - 3 ( 5 ) = - 24$

$a = 5 ,  b = - 24$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = 3$ (or $x = - 8$) into $\text{f} ( x )$ and equating to zero. Substituting without equating to zero does not score.
> 
> **A1**: Two correct equations, e.g. $3 a + b = - 9$ and $- 8 a + b = - 64$.
> 
> **M1**: Solving the simultaneous equations. The factor method also scores here: writing $\text{f} ( x ) = ( x - 3 ) ( x + 8 )$ and comparing with $x^{2} + a x + b$.
> 
> **A1**: Both correct values $a = 5$ and $b = - 24$. The working must be shown; a bare answer does not score.

### Q15
Define the cubic as a function so the factor theorem can be applied

$\text{f} ( x ) = x^{3} - x^{2} - 14 x + 24$

The factor theorem says $( x - 2 )$ is a factor exactly when $\text{f} ( 2 ) = 0$, so substitute $x = 2$

$\text{f} ( 2 ) = ( 2 )^{3} - ( 2 )^{2} - 14 ( 2 ) + 24$

**[M1]**

Work out the arithmetic

$\text{f} ( 2 ) = 8 - 4 - 28 + 24 = 0$

Because the result is zero, the factor theorem confirms the factor

$( x - 2 ) \text{is a factor of} \text{f} ( x )$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = 2$ into $\text{f} ( x )$, showing the substituted expression $( 2 )^{3} - ( 2 )^{2} - 14 ( 2 ) + 24$.
> 
> **A1**: Correctly reaching $\text{f} ( 2 ) = 0$ with no errors, which is sufficient to show the factor. A written conclusion is good practice but is not required for the mark; an arithmetic slip loses it even if the last line reads $0$.

### Q16
Since $x = \frac{1}{2}$ is a root, the factor theorem gives `\text{f}\left(\dfrac{1}{2}\right) = 0`, so substitute $x = \frac{1}{2}$

`2\left(\dfrac{1}{2}\right)^3 + (p^2 + 1)\left(\dfrac{1}{2}\right)^2 - 11\left(\dfrac{1}{2}\right) + 4 = 0`

**[M1]**

Multiply every term by $4$ to clear the fractions

$1 + ( p^{2} + 1 ) - 22 + 16 = 0$

**[A1]**

Collect the terms into an equation in $p$

$p^{2} - 4 = 0$

**[M1]**

Solve, remembering that a squared term gives two roots

$p = \pm 2$

**[A1]**

> **[mark-scheme]**
> **M1**: Using `\text{f}\left(\dfrac{1}{2}\right) = 0` and substituting $x = \frac{1}{2}$ into the cubic.
> 
> **A1**: Correct equation after clearing fractions, such as $1 + p^{2} + 1 - 22 + 16 = 0$.
> 
> **M1**: Rearranging to $p^{2} = 4$ (or $p^{2} - 4 = 0$).
> 
> **A1**: Both values $p = \pm 2$. Both are required; a single value is not enough.

### Q17
Divide the polynomial by $( x - 2 )$; a zero remainder is exactly the condition for a factor

![Long division tableau dividing 2x cubed plus 3x squared minus 18x plus 8 by x minus 2, giving quotient 2x squared plus 7x minus 4 and a remainder of zero](assets/014-long-division-tableau-dividing-2x-cubed-plus-3x-.png)

**[M1]**

Read off the quotient, with a remainder of zero

$2 x^{3} + 3 x^{2} - 18 x + 8 = ( x - 2 ) ( 2 x^{2} + 7 x - 4 )$

**[A1]**

Since the remainder is zero, $( x - 2 )$ is a factor

$( x - 2 ) \text{is a factor}$

**[A1]**

> **[mark-scheme]**
> **M1**: A valid method, either commencing division of $2 x^{3} + 3 x^{2} - 18 x + 8$ by $( x - 2 )$, or evaluating $\text{f} ( 2 )$ by the factor theorem.
> 
> **A1**: Correct division, with quotient $2 x^{2} + 7 x - 4$ and zero remainder (or $\text{f} ( 2 ) = 0$).
> 
> **A1**: Concluding from the zero remainder that $( x - 2 )$ is a factor. Reaching the zero with no errors is sufficient; a written conclusion is good practice but not required.

### Q18
Since $( x + 1 )$ is a factor, write $\text{f} ( x )$ as $( x + 1 )$ multiplied by an unknown quadratic

$x^{3} - 5 x^{2} + 3 x + 9 = ( x + 1 ) ( x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{2}$ to find $b$

$b + 1 = - 5 \Rightarrow b = - 6$

Compare the constant terms to find $c$, giving the quadratic factor $x^{2} - 6 x + 9$

$c = 9$

**[A1]**

Factorise the quadratic; it is a perfect square, since $- 3$ and $- 3$ multiply to $9$ and add to $- 6$

$x^{2} - 6 x + 9 = ( x - 3 )^{2}$

**[M1]**

Combine the factors

$\text{f} ( x ) = ( x + 1 ) ( x - 3 )^{2}$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( x + 1 ) ( x^{2} + b x + c )$ and comparing coefficients, or dividing by $( x + 1 )$ by long division.
> 
> **A1**: Correct quadratic factor $x^{2} - 6 x + 9$.
> 
> **M1**: Factorising the quadratic into $( x - 3 )^{2}$ or $( x - 3 ) ( x - 3 )$.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x + 1 ) ( x - 3 )^{2}$.
The coefficient of $x^{3}$ is positive, so the curve rises from the lower left to the upper right

The factor $( x + 1 )$ gives a point where the curve crosses the $x$-axis, and the repeated factor $( x - 3 )^{2}$ gives a point where it touches the $x$-axis

$( - 1 , 0 ) \text{and} ( 3 , 0 )$

**[B1]**

Find the $y$-intercept by substituting $x = 0$

$y = ( 0 + 1 ) ( 0 - 3 )^{2} = 9$

$( 0 , 9 )$

**[B1]**

Draw a positive cubic passing through these points, touching the $x$-axis at $( 3 , 0 )$

![Sketch of a positive cubic that crosses the x-axis at (-1, 0), touches the x-axis at (3, 0), and crosses the y-axis at (0, 9), with a local maximum between x = -1 and x = 3 and a local minimum at (3, 0)](assets/015-sketch-of-a-positive-cubic-that-crosses-the-x-ax.png)

**[B1]**

> **[mark-scheme]**
> **B1**: Both $x$-axis points, $( - 1 , 0 )$ crossing and $( 3 , 0 )$ touching, correct and labelled.
> 
> **B1**: $y$-intercept $( 0 , 9 )$ correct and labelled.
> 
> **B1**: Correct positive cubic shape that crosses at $( - 1 , 0 )$ and touches at $( 3 , 0 )$.

### Q19
A root at $x = - 2$ means $( x + 2 )$ is a factor, so write $\text{f} ( x )$ as $( x + 2 )$ multiplied by an unknown quadratic

$x^{3} - 3 x^{2} - 8 x + 4 = ( x + 2 ) ( x^{2} + b x + c )$

**[M1]**

Expand and compare the coefficients of $x^{2}$ to find $b$

$b + 2 = - 3 \Rightarrow b = - 5$

**[A1]**

Compare the constant terms to find $c$

$2 c = 4 \Rightarrow c = 2$

**[A1]**

Test whether the quadratic factor $x^{2} - 5 x + 2$ factorises: its discriminant $( - 5 )^{2} - 4 ( 1 ) ( 2 ) = 17$ is not a perfect square, so it has no rational factors and will not factorise further

$\text{f} ( x ) = ( x + 2 ) ( x^{2} - 5 x + 2 )$

**[B1]**

> **[exam-tip]**
> Not every cubic breaks into three linear factors. Once the quadratic factor has a non-square discriminant, it has no rational factors, so leaving it as a quadratic is the fully factorised answer.

> **[mark-scheme]**
> **M1**: Using the root to write $\text{f} ( x ) = ( x + 2 ) ( x^{2} + b x + c )$ and compare coefficients, or dividing by $( x + 2 )$ by long division.
> 
> **A1**: Correct $b = - 5$.
> 
> **A1**: Correct $c = 2$, giving the quadratic factor $x^{2} - 5 x + 2$.
> 
> **B1**: Stating $\text{f} ( x ) = ( x + 2 ) ( x^{2} - 5 x + 2 )$ and recognising the quadratic does not factorise further.

### Q20
Since $( x - 4 )$ is a factor, the factor theorem gives $\text{f} ( 4 ) = 0$, so substitute $x = 4$ and set the result equal to zero

$( 4 )^{3} - k ( 4 )^{2} - 4 ( 4 ) + 16 = 0$

**[M1]**

Work out the arithmetic and collect the terms

$64 - 16 k - 16 + 16 = 0$

$64 - 16 k = 0$

**[A1]**

Solve for $k$

$k = 4$

**[A1]**

> **[mark-scheme]**
> **M1**: Using $\text{f} ( 4 ) = 0$ and substituting $x = 4$ into the cubic.
> 
> **A1**: Correct simplified equation $64 - 16 k = 0$, or equivalent.
> 
> **A1**: $k = 4$.

### Q21
Substitute $x = 1$ into the polynomial

$\text{f} ( 1 ) = ( 1 )^{3} - 4 ( 1 )^{2} - 7 ( 1 ) + 10 = 0$

**[M1]**

Since $\text{f} ( 1 ) = 0$, the factor theorem gives a factor

$( x - 1 ) \text{is a factor}$

**[A1]**

> **[mark-scheme]**
> **M1**: Evaluating $\text{f} ( 1 )$, showing the substitution.
> 
> **A1**: Obtaining $\text{f} ( 1 ) = 0$ and stating the factor $( x - 1 )$, which the question asks for.
**Method 1 - Long Division**

Divide $\text{f} ( x )$ by $( x + 2 )$

![Long division tableau dividing x cubed minus 4x squared minus 7x plus 10 by x plus 2, giving quotient x squared minus 6x plus 5 and remainder zero](assets/016-long-division-tableau-dividing-x-cubed-minus-4x-.png)

**[M1]**

Read the quotient from the top of the tableau; the remainder is zero

$x^{2} - 6 x + 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $\text{f} ( x )$ by $( x + 2 )$, by any valid method, reaching a partial quotient of the form $x^{2} + k x$.
> 
> **A1**: Correct quotient $x^{2} - 6 x + 5$ with zero remainder.

**Method 2 - Inspection**

Write $\text{f} ( x )$ as $( x + 2 )$ multiplied by an unknown quadratic

$x^{3} - 4 x^{2} - 7 x + 10 = ( x + 2 ) ( x^{2} + p x + q )$

**[M1]**

Compare the coefficients of $x^{2}$ to find $p$

$p + 2 = - 4 \Rightarrow p = - 6$

Compare the constant terms to find $q$

$2 q = 10 \Rightarrow q = 5$

$x^{2} - 6 x + 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( x + 2 ) ( x^{2} + p x + q )$ and comparing coefficients.
> 
> **A1**: Correct quotient $x^{2} - 6 x + 5$.
Factorise the quadratic quotient from part (b)

$x^{2} - 6 x + 5 = ( x - 1 ) ( x - 5 )$

**[M1 A1]**

Combine with the factor $( x + 2 )$ and match the required form

$\text{f} ( x ) = ( x + 2 ) ( x - 1 ) ( x - 5 )$

$a = 2 ,  b = - 1 ,  c = - 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Attempting to factorise $x^{2} - 6 x + 5$ into two linear factors.
> 
> **A1**: Correct factors $( x - 1 ) ( x - 5 )$.
> 
> **A1**: Writing $\text{f} ( x ) = ( x + 2 ) ( x - 1 ) ( x - 5 )$, giving $a = 2 , b = - 1 , c = - 5$. The factors may be in any order.

### Q22
Take out the common factor of $x$ first

$2 x^{3} + 7 x^{2} - 4 x = x ( 2 x^{2} + 7 x - 4 )$

**[M1]**

Factorise the quadratic, checking it expands to the required form

$\text{f} ( x ) = x ( 2 x - 1 ) ( x + 4 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Taking out the common factor $x$ to reach $x ( 2 x^{2} + 7 x - 4 )$.
> 
> **A1**: Factorising the quadratic to reach the given $x ( 2 x - 1 ) ( x + 4 )$. Because the result is given, the factorisation must be shown.
A fraction is zero only where its numerator is zero, provided the denominator is not, so solve $\text{f} ( x ) = 0$ with $x \neq - 1$

$x ( 2 x - 1 ) ( x + 4 ) = 0$

**[M1]**

Set each factor to zero; none of the roots is $- 1$, so all are valid

$x = - 4 ,  0 ,  \frac{1}{2}$

**[A1]**

> **[mark-scheme]**
> **M1**: Setting $\text{f} ( x ) = 0$ from the factorised form (or otherwise), using that the fraction is zero when its numerator is.
> 
> **A1**: All three solutions $x = - 4 , 0 , \frac{1}{2}$, in any order. None is excluded, since none equals $- 1$.

### Q23
**Method 1 - Remainder Theorem**

By the remainder theorem, the remainder on dividing by $( x - 3 )$ is the value of the polynomial at $x = 3$, so evaluate it there

$( 3 )^{3} + 2 ( 3 )^{2} - 5 ( 3 ) + 8$

**[M1]**

Work out the arithmetic

$27 + 18 - 15 + 8$

$38$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the remainder theorem, substituting $x = 3$ into the polynomial (or commencing long division by $( x - 3 )$).
> 
> **A1**: Correct remainder $38$. A bare value with no substitution or division seen does not score.

**Method 2 - Long Division**

Divide the polynomial by $( x - 3 )$; the number left at the foot of the division is the remainder

![Long division tableau dividing x cubed plus 2x squared minus 5x plus 8 by x minus 3, giving quotient x squared plus 5x plus 10 and a remainder of 38](assets/017-long-division-tableau-dividing-x-cubed-plus-2x-s.png)

**[M1]**

The final line of the division is the remainder

$38$

**[A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $x^{3} + 2 x^{2} - 5 x + 8$ by $( x - 3 )$ and working through to the constant left at the foot.
> 
> **A1**: Correct remainder $38$.

### Q24
(i)

Split the middle term using two numbers that multiply to $4 \times ( - 15 ) = - 60$ and add to $- 4$, namely $- 10$ and $6$

$4 x^{2} - 4 x - 15 = 4 x^{2} + 6 x - 10 x - 15$

**[M1]**

Factorise in pairs, then take out the common bracket

$2 x ( 2 x + 3 ) - 5 ( 2 x + 3 )$

$( 2 x + 3 ) ( 2 x - 5 )$

**[A1]**

(ii)

First take out the common factor of $x$

$3 x^{3} + 11 x^{2} - 4 x = x ( 3 x^{2} + 11 x - 4 )$

**[M1]**

Factorise the quadratic, using two numbers that multiply to $3 \times ( - 4 ) = - 12$ and add to $11$, namely $- 1$ and $12$

`x(3x^2 - x + 12x - 4) = x[x(3x - 1) + 4(3x - 1)]`

$x ( 3 x - 1 ) ( x + 4 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Splitting the middle term of $4 x^{2} - 4 x - 15$ into $+ 6 x$ and $- 10 x$, or otherwise attempting two factors.
> 
> **A1**: Correct $( 2 x + 3 ) ( 2 x - 5 )$, in either order.
> 
> **M1**: Taking out the common factor $x$ from $3 x^{3} + 11 x^{2} - 4 x$ to reach $x ( 3 x^{2} + 11 x - 4 )$.
> 
> **A1**: Fully correct $x ( 3 x - 1 ) ( x + 4 )$, factors in any order.

### Q25
A root at $x = 3$ means $( x - 3 )$ is a factor, so write $\text{f} ( x )$ as $( x - 3 )$ multiplied by an unknown quadratic

$x^{3} - 5 x^{2} - 2 x + 24 = ( x - 3 ) ( x^{2} + b x + c )$

**[M1]**

Expand the right hand side and compare the coefficients of $x^{2}$ to find $b$

$b - 3 = - 5 \Rightarrow b = - 2$

**[A1]**

Compare the constant terms to find $c$

$- 3 c = 24 \Rightarrow c = - 8$

**[A1]**

The quadratic factor is $x^{2} - 2 x - 8$; factorise it by finding two numbers that multiply to $- 8$ and add to $- 2$, namely $- 4$ and $2$

$x^{2} - 2 x - 8 = ( x - 4 ) ( x + 2 )$

**[M1 A1]**

Combine all three linear factors

$\text{f} ( x ) = ( x - 3 ) ( x - 4 ) ( x + 2 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the given root to write $\text{f} ( x ) = ( x - 3 ) ( x^{2} + b x + c )$ and compare coefficients, or dividing $\text{f} ( x )$ by $( x - 3 )$ by long division.
> 
> **A1**: Correct $b = - 2$ (equivalently, the $x^{2}$ term of the quotient).
> 
> **A1**: Correct $c = - 8$, giving the quadratic factor $x^{2} - 2 x - 8$.
> 
> **M1**: Attempting to factorise the quadratic into two linear factors.
> 
> **A1**: Correct factors $( x - 4 ) ( x + 2 )$.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x - 3 ) ( x - 4 ) ( x + 2 )$. The factors may be in any order.

### Q26
Since $( x + 1 )$ is a factor, the factor theorem gives $\text{f} ( - 1 ) = 0$, so substitute $x = - 1$

$( - 1 )^{4} + a ( - 1 )^{3} - 13 ( - 1 )^{2} - 38 ( - 1 ) - 4 b = 0$

**[M1]**

Simplify to a linear equation in $a$ and $b$

$1 - a - 13 + 38 - 4 b = 0$

$a + 4 b = 26$

**[A1]**

Since $( x + 2 )$ is also a factor, $\text{f} ( - 2 ) = 0$, so substitute $x = - 2$

$( - 2 )^{4} + a ( - 2 )^{3} - 13 ( - 2 )^{2} - 38 ( - 2 ) - 4 b = 0$

**[M1]**

Simplify to a second linear equation

$16 - 8 a - 52 + 76 - 4 b = 0$

$2 a + b = 10$

**[A1]**

Multiply the second equation by $4$ so the $b$ terms match, then subtract the first to eliminate $b$

$8 a + 4 b = 40$

$7 a = 14 \Rightarrow a = 2$

Substitute $a = 2$ back into $2 a + b = 10$

$b = 10 - 4 = 6$

$a = 2 ,  b = 6$

**[A1]**

> **[mark-scheme]**
> **M1**: Using $\text{f} ( - 1 ) = 0$ (or dividing by $( x + 1 )$ and equating the remainder to zero), substituting $x = - 1$.
> 
> **A1**: A correct first equation in any equivalent form, e.g. $a + 4 b = 26$ or $1 - a - 13 + 38 - 4 b = 0$.
> 
> **M1**: Using $\text{f} ( - 2 ) = 0$ (or dividing by $( x + 2 )$), substituting $x = - 2$.
> 
> **A1**: A correct second equation in any equivalent form, e.g. $2 a + b = 10$.
> 
> **A1**: Solving the equations simultaneously to obtain both $a = 2$ and $b = 6$. Both values are required, and the simultaneous working must be shown.

### Q27
Substitute $x = - 1$ and $x = - 2$ into $\text{f} ( x )$ and show each gives zero

$\text{f} ( - 1 ) = 2 + 15 - 10 - 105 + 98 = 0$

$\text{f} ( - 2 ) = 32 + 120 - 40 - 210 + 98 = 0$

**[B1]**

> **[mark-scheme]**
> **B1**: Both $\text{f} ( - 1 ) = 0$ and $\text{f} ( - 2 ) = 0$ shown, with the substitutions seen. As both results are given, the working must be seen for each.
From part (a), $( x + 1 )$ and $( x + 2 )$ are both factors, so their product $( x + 1 ) ( x + 2 ) = x^{2} + 3 x + 2$ is a factor; divide $\text{f} ( x )$ by it, writing $\text{f} ( x )$ as $( x^{2} + 3 x + 2 )$ multiplied by an unknown quadratic

$2 x^{4} - 15 x^{3} - 10 x^{2} + 105 x + 98 = ( x^{2} + 3 x + 2 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{4}$

$a = 2$

Compare the constant term

$2 c = 98 \Rightarrow c = 49$

Compare the coefficient of $x^{3}$

$3 a + b = - 15 \Rightarrow b = - 21$

These give the quadratic factor

$\text{f} ( x ) = ( x^{2} + 3 x + 2 ) ( 2 x^{2} - 21 x + 49 )$

**[A1]**

Factorise the quadratic $2 x^{2} - 21 x + 49$; $2 \times 49 = 98$, and $- 14$ and $- 7$ multiply to $98$ and add to $- 21$

$2 x^{2} - 21 x + 49 = ( 2 x - 7 ) ( x - 7 )$

**[M1 A1]**

Write $\text{f} ( x )$ fully factorised

$\text{f} ( x ) = ( x + 1 ) ( x + 2 ) ( 2 x - 7 ) ( x - 7 )$

**[A1]**

Set each factor to zero to solve $\text{f} ( x ) = 0$

$x = - 1 ,  - 2 ,  \frac{7}{2} ,  7$

**[A1 A1]**

> **[mark-scheme]**
> **M1**: Using $( x + 1 ) ( x + 2 ) = x^{2} + 3 x + 2$ as a factor and dividing (or comparing coefficients).
> 
> **A1**: Correct quadratic quotient $2 x^{2} - 21 x + 49$.
> 
> **M1**: Attempting to factorise $2 x^{2} - 21 x + 49$ into two linear factors.
> 
> **A1**: Correct factors $( 2 x - 7 ) ( x - 7 )$.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x + 1 ) ( x + 2 ) ( 2 x - 7 ) ( x - 7 )$.
> 
> **A1**: Two correct solutions.
> 
> **A1**: All four solutions $x = - 1 , - 2 , \frac{7}{2} , 7$ and no extras.

### Q28
Here $2 x + 1 = 0$ at $x = - \frac{1}{2}$, so by the remainder theorem the remainder is the value of the polynomial there

`8\left(-\frac{1}{2}\right)^3 + 6\left(-\frac{1}{2}\right)^2 - \left(-\frac{1}{2}\right) - 2 = -1 + \frac{3}{2} + \frac{1}{2} - 2`

**[M1]**

$- 1$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = - \frac{1}{2}$ into $8 x^{3} + 6 x^{2} - x - 2$.
> 
> **A1**: Correct remainder $- 1$.
Again $2 x + 1 = 0$ at $x = - \frac{1}{2}$, so evaluate the polynomial there

`6\left(-\frac{1}{2}\right)^2 - \left(-\frac{1}{2}\right) - 2 = \frac{3}{2} + \frac{1}{2} - 2`

**[M1]**

$0$

**[A1]**

> **[exam-tip]**
> A remainder of $0$ is not a mistake: it means $( 2 x + 1 )$ divides exactly, so it is a factor. Compare with part (a), where the same divisor gave a remainder of $- 1$, so this zero is telling you something specific about this polynomial.

> **[mark-scheme]**
> **M1**: Substituting $x = - \frac{1}{2}$ into $6 x^{2} - x - 2$ (or dividing by $( 2 x + 1 )$).
> 
> **A1**: Correct remainder $0$.

### Q29
Every term has a common factor of $x y$, so take that out first

$x^{5} y - x y^{5} = x y ( x^{4} - y^{4} )$

**[M1]**

$x^{4} - y^{4}$ is a difference of two squares, $( x^{2} )^{2} - ( y^{2} )^{2}$

$= x y ( x^{2} - y^{2} ) ( x^{2} + y^{2} )$

**[A1]**

$x^{2} - y^{2}$ is itself a difference of two squares; $x^{2} + y^{2}$ does not factorise over the reals, so leave it

$x y ( x - y ) ( x + y ) ( x^{2} + y^{2} )$

**[A1]**

> **[mark-scheme]**
> **M1**: Taking out the common factor $x y$ to reach $x y ( x^{4} - y^{4} )$.
> 
> **A1**: One correct difference-of-squares step, reaching $x y ( x^{2} - y^{2} ) ( x^{2} + y^{2} )$.
> 
> **A1**: Fully factorised $x y ( x - y ) ( x + y ) ( x^{2} + y^{2} )$, factors in any order. The $x^{2} + y^{2}$ must be present and left unfactorised, since it has no real factors, so "completely" means stopping there. Splitting $x^{2} + y^{2}$ further loses this mark.

### Q30
The factor $( 2 x - 5 )$ is zero at $x = \frac{5}{2}$, so by the factor theorem `\text{f}\left(\frac{5}{2}\right) = 0`

`2\left(\frac{5}{2}\right)^3 + k\left(\frac{5}{2}\right)^2 - 11\left(\frac{5}{2}\right) - 60 = 0`

**[M1]**

Work out the arithmetic and solve for $k$

$\frac{125}{4} + \frac{25k}{4} - \frac{55}{2} - 60 = 0 \Rightarrow \frac{25k}{4} = \frac{225}{4}$

$k = 9$

**[A1]**

Substitute $k = 9$ and divide by $( 2 x - 5 )$; write $\text{f} ( x )$ as $( 2 x - 5 )$ multiplied by an unknown quadratic

$2 x^{3} + 9 x^{2} - 11 x - 60 = ( 2 x - 5 ) ( x^{2} + b x + c )$

**[M1]**

Compare the constant term

$- 5 c = - 60 \Rightarrow c = 12$

Compare the coefficient of $x^{2}$

$- 5 + 2 b = 9 \Rightarrow b = 7$

Factorise the quadratic

$x^{2} + 7 x + 12 = ( x + 3 ) ( x + 4 )$

$\text{f} ( x ) = ( 2 x - 5 ) ( x + 3 ) ( x + 4 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the factor theorem at $x = \frac{5}{2}$, substituting into $\text{f} ( x )$ and equating to zero. The fractional substitution must be seen.
> 
> **A1**: $k = 9$.
> 
> **M1**: Substituting $k = 9$ and dividing by $( 2 x - 5 )$ (or comparing coefficients) to reach the quadratic factor $x^{2} + 7 x + 12$.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( 2 x - 5 ) ( x + 3 ) ( x + 4 )$, factors in any order.

### Q31
**Method 1 - Long Division**

Divide by $( 2 x - 1 )$, writing the missing $x^{3}$ and $x$ terms as $0 x^{3}$ and $0 x$ so the columns line up

![Long division tableau dividing 4x to the fourth plus zero x cubed minus 37x squared plus zero x plus 9 by 2x minus 1, giving quotient 2x cubed plus x squared minus 18x minus 9 and remainder zero](assets/018-long-division-tableau-dividing-4x-to-the-fourth-.png)

**[M1]**

Read the quotient from the top of the tableau; the remainder is zero

$2 x^{3} + x^{2} - 18 x - 9$

**[A1 A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $4 x^{4} - 37 x^{2} + 9$ by $( 2 x - 1 )$, by any valid method, dividing $4 x^{4}$ by $2 x$ to start the quotient with $2 x^{3}$.
> 
> **A1**: A correct partial quotient (at least $2 x^{3} + x^{2}$).
> 
> **A1**: Fully correct quotient $2 x^{3} + x^{2} - 18 x - 9$ with zero remainder.

**Method 2 - Inspection**

Write the quartic as $( 2 x - 1 )$ multiplied by an unknown cubic

$4 x^{4} - 37 x^{2} + 9 = ( 2 x - 1 ) ( a x^{3} + b x^{2} + c x + d )$

**[M1]**

Compare coefficients term by term, from $x^{4}$ down to the constant

$2 a = 4 \Rightarrow a = 2$

$- a + 2 b = 0 \Rightarrow b = 1$

$- b + 2 c = - 37 \Rightarrow c = - 18$

$- c + 2 d = 0 \Rightarrow d = - 9$

$2 x^{3} + x^{2} - 18 x - 9$

**[A1 A1]**

> **[mark-scheme]**
> **M1**: Writing $4 x^{4} - 37 x^{2} + 9 = ( 2 x - 1 ) ( a x^{3} + b x^{2} + c x + d )$ and comparing coefficients.
> 
> **A1**: At least two coefficients correct.
> 
> **A1**: Fully correct quotient $2 x^{3} + x^{2} - 18 x - 9$.

### Q32
The factor $( a x - 2 )$ is zero at $x = \frac{2}{a}$, so by the factor theorem evaluate the quadratic there and check it is zero

`3a\left(\frac{2}{a}\right)^2 + (a-6)\left(\frac{2}{a}\right) - 2`

**[M1]**

Work out each term

$= \frac{12}{a} + 2 - \frac{12}{a} - 2 = 0$

**Final answer:** **The value is **$0$**, so **$( a x - 2 )$** is a factor**

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = \frac{2}{a}$ into the quadratic (or writing it as $( a x - 2 ) ( 3 x + 1 )$ and expanding to verify).
> 
> **A1**: Reaching $0$ with no errors, which shows $( a x - 2 )$ is a factor. A written conclusion is good practice but is not required for the mark.
Part (a) shows $( a x - 2 )$ is a factor, so divide the quadratic by it to find the other factor

$3 a x^{2} + ( a - 6 ) x - 2 = ( a x - 2 ) ( 3 x + 1 )$

Setting each factor to zero gives the two roots $x = \frac{2}{a}$ and $x = - \frac{1}{3}$

**[M1]**

The given root $x = - \frac{1}{a-4}$ must equal one of these; equating it to $- \frac{1}{3}$

$- \frac{1}{a-4} = - \frac{1}{3}$

$a - 4 = 3 \Rightarrow a = 7$

**[M1]**

Equating it instead to $\frac{2}{a}$

$- \frac{1}{a-4} = \frac{2}{a}$

$- a = 2 ( a - 4 )$

$- a = 2 a - 8$

$3 a = 8 \Rightarrow a = \frac{8}{3}$

Both values give a genuine root of the quadratic, so

**Final answer:** $a = 7$** or **$a = \frac{8}{3}$

**[A1]**

> **[mark-scheme]**
> **M1**: Dividing by $( a x - 2 )$ to obtain the other factor $( 3 x + 1 )$, and hence the roots $x = \frac{2}{a}$ and $x = - \frac{1}{3}$.
> 
> **M1**: Equating $- \frac{1}{a-4}$ to a root and solving for $a$ (either case).
> 
> **A1**: Both $a = 7$ and $a = \frac{8}{3}$. Giving only $a = 7$ (equating to $- \frac{1}{3}$ alone) is incomplete and scores M1 M1 A0, since $x = - \frac{1}{a-4}$ can equally be the root $\frac{2}{a}$, which gives $a = \frac{8}{3}$.

### Q33
**Method 1 - Remainder Theorem**

The factor $( 2 x + 3 )$ is zero at $x = - \frac{3}{2}$, so the remainder is `\text{f}\left(-\frac{3}{2}\right)`

`\text{f}\left(-\frac{3}{2}\right) = 6\left(-\frac{3}{2}\right)^4 + 7\left(-\frac{3}{2}\right)^3 - 27\left(-\frac{3}{2}\right)^2 - 28\left(-\frac{3}{2}\right) + 12`

**[M1]**

Work out the arithmetic

$= \frac{243}{8} - \frac{189}{8} - \frac{243}{4} + 42 + 12 = 0$

$0$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the remainder theorem, substituting $x = - \frac{3}{2}$ into $\text{f} ( x )$ (or commencing long division by $( 2 x + 3 )$).
> 
> **A1**: Correct remainder $0$. (A remainder of $0$ also shows $( 2 x + 3 )$ is a factor, which is used implicitly in part (b).)

**Method 2 - Long Division**

Divide $\text{f} ( x )$ by $( 2 x + 3 )$; the constant left at the foot is the remainder

![Long division tableau dividing 6x to the fourth plus 7x cubed minus 27x squared minus 28x plus 12 by 2x plus 3, giving quotient 3x cubed minus x squared minus 12x plus 4 and a remainder of zero](assets/019-long-division-tableau-dividing-6x-to-the-fourth-.png)

**[M1]**

The final line of the division is the remainder

$0$

**[A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $\text{f} ( x )$ by $( 2 x + 3 )$ and working through to the constant at the foot.
> 
> **A1**: Correct remainder $0$.
Since $( x + 2 )$ is a factor, divide $\text{f} ( x )$ by it; write $\text{f} ( x )$ as $( x + 2 )$ multiplied by an unknown cubic

$6 x^{4} + 7 x^{3} - 27 x^{2} - 28 x + 12 = ( x + 2 ) ( a x^{3} + b x^{2} + c x + d )$

**[M1]**

Compare the coefficient of $x^{4}$

$a = 6$

Compare the coefficient of $x^{3}$

$2 a + b = 7 \Rightarrow b = - 5$

Compare the constant term

$2 d = 12 \Rightarrow d = 6$

Compare the coefficient of $x$

$2 c + d = - 28 \Rightarrow c = - 17$

These give the cubic factor

$\text{f} ( x ) = ( x + 2 ) ( 6 x^{3} - 5 x^{2} - 17 x + 6 )$

**[A1]**

From part (a), $( 2 x + 3 )$ is also a factor (the remainder was $0$), so divide the cubic by it

$6 x^{3} - 5 x^{2} - 17 x + 6 = ( 2 x + 3 ) ( 3 x^{2} - 7 x + 2 )$

**[M1]**

Factorise the quadratic; $3 \times 2 = 6$, and $- 6$ and $- 1$ multiply to $6$ and add to $- 7$

$3 x^{2} - 7 x + 2 = ( 3 x - 1 ) ( x - 2 )$

**[A1]**

Combine all four linear factors

$\text{f} ( x ) = ( x + 2 ) ( 2 x + 3 ) ( 3 x - 1 ) ( x - 2 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Dividing $\text{f} ( x )$ by $( x + 2 )$ (or comparing coefficients) to begin reducing the quartic.
> 
> **A1**: Correct cubic factor $6 x^{3} - 5 x^{2} - 17 x + 6$.
> 
> **M1**: Using $( 2 x + 3 )$ from part (a), or otherwise, to reduce the cubic to a quadratic factor.
> 
> **A1**: Correct quadratic factor $3 x^{2} - 7 x + 2$, or its factors $( 3 x - 1 ) ( x - 2 )$.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x + 2 ) ( 2 x + 3 ) ( 3 x - 1 ) ( x - 2 )$, factors in any order.

### Q34
Since $( 3 x + 1 )$ is a factor, write $\text{f} ( x )$ as $( 3 x + 1 )$ multiplied by an unknown cubic

$3 x^{4} + x^{3} - 12 x^{2} - 49 x - 15 = ( 3 x + 1 ) ( a x^{3} + b x^{2} + c x + d )$

**[M1]**

Expanding $( 3 x + 1 ) ( a x^{3} + b x^{2} + c x + d )$ gives $3 a x^{4} + ( 3 b + a ) x^{3} + ( 3 c + b ) x^{2} + ( 3 d + c ) x + d$; compare each coefficient with $\text{f} ( x )$

$3 a = 3 \Rightarrow a = 1$

$3 b + a = 1 \Rightarrow b = 0$

$d = - 15$

$3 d + c = - 49 \Rightarrow c = - 4$

$\text{f} ( x ) = ( 3 x + 1 ) ( x^{3} - 4 x - 15 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( 3 x + 1 ) ( a x^{3} + b x^{2} + c x + d )$ and comparing coefficients, or dividing by $( 3 x + 1 )$.
> 
> **A1**: Correct $a = 1 , b = 0 , c = - 4 , d = - 15$, giving $\text{f} ( x ) = ( 3 x + 1 ) ( x^{3} - 4 x - 15 )$. The $b = 0$ (no $x^{2}$ term in the cubic) must be correct.
From part (a), $\text{f} ( x ) = ( 3 x + 1 ) ( x^{3} - 4 x - 15 )$. Since $( x - 3 )$ is a factor of $\text{f} ( x )$ but not of $( 3 x + 1 )$, it must be a factor of the cubic; divide the cubic by it, writing the missing $x^{2}$ term as $0 x^{2}$

$x^{3} + 0 x^{2} - 4 x - 15 = ( x - 3 ) ( x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{2}$

$b - 3 = 0 \Rightarrow b = 3$

Compare the constant term

$- 3 c = - 15 \Rightarrow c = 5$

These give the quadratic factor

$x^{3} - 4 x - 15 = ( x - 3 ) ( x^{2} + 3 x + 5 )$

**[A1]**

Check whether the quadratic factorises further by its discriminant

$b^{2} - 4 a c = 3^{2} - 4 ( 1 ) ( 5 ) = 9 - 20 = - 11$

**[M1]**

Since the discriminant is negative, $x^{2} + 3 x + 5$ has no real factors, so the full factorisation is

$\text{f} ( x ) = ( 3 x + 1 ) ( x - 3 ) ( x^{2} + 3 x + 5 )$

**[A1 A1]**

> **[mark-scheme]**
> **M1**: Using $( x - 3 )$ as a factor of the cubic $x^{3} - 4 x - 15$ and dividing (or comparing coefficients).
> 
> **A1**: Correct quadratic factor $x^{2} + 3 x + 5$.
> 
> **M1**: Testing the quadratic factor for further factorisation (discriminant, or an equivalent argument that it has no real roots).
> 
> **A1**: Recognising $x^{2} + 3 x + 5$ is irreducible (negative discriminant), so it is left as a quadratic.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( 3 x + 1 ) ( x - 3 ) ( x^{2} + 3 x + 5 )$, factors in any order.
Set the fully factorised form to zero; a product is zero when one of its factors is zero

$( 3 x + 1 ) ( x - 3 ) ( x^{2} + 3 x + 5 ) = 0$

The two linear factors give real roots, while $x^{2} + 3 x + 5 = 0$ has discriminant $- 11 < 0$ from part (b), so contributes none

**Final answer:** **The only real roots are **$x = - \frac{1}{3}$** and **$x = 3$**, so **$\text{f} ( x ) = 0$** has exactly two real roots**

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Identifying the two real roots $x = - \frac{1}{3}$ and $x = 3$ from the linear factors.
> 
> **B1**: Concluding "exactly 2" by explicitly ruling out the quadratic factor via its negative discriminant. Both the two real roots and the reason the quadratic gives none are needed, because this is a "show" part, so the count must be justified, not just stated.

### Q35
The expression is a quadratic in $x^{2}$; writing $y = x^{2}$ turns it into $9 y^{2} - 40 y + 16$

$9 x^{4} - 40 x^{2} + 16 = 9 ( x^{2} )^{2} - 40 ( x^{2} ) + 16$

**[M1]**

By the factor theorem in $y$, test $y = \frac{4}{9}$ (that is, $x^{2} = \frac{4}{9}$)

`9\left(\frac{4}{9}\right)^2 - 40\left(\frac{4}{9}\right) + 16 = \frac{16}{9} - \frac{160}{9} + \frac{144}{9} = 0`

**Final answer:** **so **$( 9 x^{2} - 4 )$** is a factor**

**[A1]**

The quadratic in $y$ therefore factorises completely as $( 9 y - 4 ) ( y - 4 )$; replacing $y$ with $x^{2}$ and setting the result equal to zero

$9 x^{4} - 40 x^{2} + 16 = ( 9 x^{2} - 4 ) ( x^{2} - 4 ) = 0$

**[M1]**

Factorise each difference of two squares and solve

$( 3 x - 2 ) ( 3 x + 2 ) ( x - 2 ) ( x + 2 ) = 0$

$x = \frac{2}{3} ,  - \frac{2}{3} ,  2 ,  - 2$

**[A1 A1]**

> **[mark-scheme]**
> **M1**: Recognising the expression as a quadratic in $x^{2}$ (substitution $y = x^{2}$ or working directly in $x^{2}$).
> 
> **A1**: Showing $( 9 x^{2} - 4 )$ is a factor, by evaluating at $x^{2} = \frac{4}{9}$ or by dividing.
> 
> **M1**: Reaching the fully factorised $( 9 x^{2} - 4 ) ( x^{2} - 4 )$, or dividing $9 x^{4} - 40 x^{2} + 16$ by $( 9 x^{2} - 4 )$ to obtain $x^{2} - 4$.
> 
> **A1**: Two correct solutions.
> 
> **A1**: All four solutions $x = \pm \frac{2}{3} , \pm 2$ and no extras. Accept decimals $\pm 0 . 667$.

### Q36
Write out the division identity, dividend $= ( \text{divisor} ) ( \text{quotient} ) + \text{remainder}$

`2x^3 + (a+b)x^2 + (a-b)x - 3 = (x+4)\left(2x^2 + (2a+3)x + (2b-5)\right) + c`

**[M1]**

Expand the right hand side and collect like terms

$= 2 x^{3} + ( 2 a + 11 ) x^{2} + ( 8 a + 2 b + 7 ) x + ( 8 b - 20 + c )$

Compare the coefficient of $x^{2}$

$2 a + 11 = a + b \Rightarrow b = a + 11$

Compare the coefficient of $x$

$8 a + 2 b + 7 = a - b \Rightarrow 7 a + 3 b = - 7$

Substitute $b = a + 11$ and solve for $a$

$7 a + 3 ( a + 11 ) = - 7$

$a = - 4 ,  b = 7$

**[M1 A1]**

Compare the constant terms to find $c$

$8 b - 20 + c = - 3 \Rightarrow 8 ( 7 ) - 20 + c = - 3$

$c = - 39$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing the division identity dividend $= ( x + 4 ) ( \text{quotient} ) + c$ and expanding the product.
> 
> **M1**: Comparing coefficients of $x^{2}$ and $x$ to form two simultaneous equations in $a$ and $b$.
> 
> **A1**: Both $a = - 4$ and $b = 7$.
> 
> **A1**: $c = - 39$, from comparing the constant terms.

### Q37
Since $3$ is a root, $( x - 3 )$ is a factor; divide the cubic by it, writing it as $( x - 3 )$ multiplied by an unknown quadratic

$2 x^{3} - x^{2} - 11 x - 12 = ( x - 3 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 2$

Compare the constant term

$- 3 c = - 12 \Rightarrow c = 4$

Compare the coefficient of $x^{2}$

$- 3 a + b = - 1 \Rightarrow b = 5$

These give the quadratic factor

$2 x^{3} - x^{2} - 11 x - 12 = ( x - 3 ) ( 2 x^{2} + 5 x + 4 )$

**[A1]**

Any further real root must come from $2 x^{2} + 5 x + 4 = 0$; test whether that has real roots using its discriminant

$b^{2} - 4 a c = 5^{2} - 4 ( 2 ) ( 4 ) = 25 - 32 = - 7$

**[M1]**

Since the discriminant is negative, $2 x^{2} + 5 x + 4 = 0$ has no real roots, so the only real root of the cubic is $x = 3$

**Final answer:** **The discriminant is **$- 7 < 0$**, so there are no other real roots**

**[A1]**

> **[mark-scheme]**
> **M1**: Using $( x - 3 )$ as a factor and dividing (or comparing coefficients) to reach the quadratic factor.
> 
> **A1**: Correct quadratic factor $2 x^{2} + 5 x + 4$.
> 
> **M1**: Computing the discriminant of the quadratic factor.
> 
> **A1**: Concluding from the negative discriminant that the quadratic has no real roots, so the cubic has no real root other than $x = 3$. A conclusion in words is required here, because this is a "prove" question, so the negative discriminant must be explicitly linked to "no other real roots".

### Q38
Write out the required identity, noting that the left hand side has no constant term

$3 x^{3} + 16 x^{2} - 22 x + 0 = ( 3 x + 1 ) ( a x^{2} + b x + c ) + d$

**[M1]**

Compare the coefficient of $x^{3}$

$3 a = 3 \Rightarrow a = 1$

**[A1]**

Compare the coefficient of $x^{2}$

$3 b + a = 16 \Rightarrow b = 5$

Compare the coefficient of $x$

$3 c + b = - 22 \Rightarrow c = - 9$

**[A1]**

Compare the constant terms; the left hand side has none, so the two must cancel

$c + d = 0 \Rightarrow d = 9$

$3 x^{3} + 16 x^{2} - 22 x = ( 3 x + 1 ) ( x^{2} + 5 x - 9 ) + 9$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing the identity $3 x^{3} + 16 x^{2} - 22 x = ( 3 x + 1 ) ( a x^{2} + b x + c ) + d$ and comparing coefficients, or dividing $3 x^{3} + 16 x^{2} - 22 x$ by $( 3 x + 1 )$ by long division.
> 
> **A1**: $a = 1$.
> 
> **A1**: $b = 5$ and $c = - 9$.
> 
> **A1**: $d = 9$, with the full identity stated. Accept the values listed separately rather than substituted back in.

### Q39
**Method 1 - Remainder Theorem**

The remainder on dividing by $( x - 3 )$ is the value of $\text{f} ( x )$ at $x = 3$

$\text{f} ( 3 ) = ( 3 )^{3} - 28 ( 3 ) + 48 = 27 - 84 + 48$

**[M1]**

$- 9$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the remainder theorem, substituting $x = 3$ into $\text{f} ( x )$ (or commencing long division by $( x - 3 )$).
> 
> **A1**: Correct remainder $- 9$. A bare value with no substitution or division seen does not score.

**Method 2 - Long Division**

Divide $\text{f} ( x )$ by $( x - 3 )$, writing the missing $x^{2}$ term as $0 x^{2}$ so that the columns line up; the number left at the foot of the division is the remainder

![Long division tableau dividing x cubed plus zero x squared minus 28x plus 48 by x minus 3, giving quotient x squared plus 3x minus 19 and a remainder of minus 9](assets/020-long-division-tableau-dividing-x-cubed-plus-zero.png)

**[M1]**

The final line of the division is the remainder

$- 9$

**[A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $\text{f} ( x )$ by $( x - 3 )$ and working through to the constant at the foot.
> 
> **A1**: Correct remainder $- 9$.
Since $( x + 6 )$ is a factor, divide $\text{f} ( x )$ by it; write $\text{f} ( x )$ as $( x + 6 )$ multiplied by an unknown quadratic

$x^{3} + 0 x^{2} - 28 x + 48 = ( x + 6 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 1$

Compare the constant term

$6 c = 48 \Rightarrow c = 8$

Compare the coefficient of $x^{2}$

$6 a + b = 0 \Rightarrow b = - 6$

These give the quadratic factor

$\text{f} ( x ) = ( x + 6 ) ( x^{2} - 6 x + 8 )$

**[A1]**

Factorise the quadratic, using two numbers that multiply to $8$ and add to $- 6$, namely $- 2$ and $- 4$

$x^{2} - 6 x + 8 = ( x - 2 ) ( x - 4 )$

**[M1]**

Combine the factors

$\text{f} ( x ) = ( x + 6 ) ( x - 2 ) ( x - 4 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( x + 6 ) ( a x^{2} + b x + c )$ and comparing coefficients, or dividing by $( x + 6 )$. The missing $x^{2}$ term must be handled as $0 x^{2}$.
> 
> **A1**: Correct quadratic factor $x^{2} - 6 x + 8$.
> 
> **M1**: Factorising the quadratic into two linear factors.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x + 6 ) ( x - 2 ) ( x - 4 )$, factors in any order.

### Q40
The factor $( 4 x - 3 )$ is zero at $x = \frac{3}{4}$, so by the factor theorem evaluate $\text{f} ( x )$ there and check it is zero

`\text{f}\left(\frac{3}{4}\right) = 4\left(\frac{3}{4}\right)^3 - 7\left(\frac{3}{4}\right)^2 - 21\left(\frac{3}{4}\right) + 18`

**[M1]**

Work out the arithmetic

$= \frac{27}{16} - \frac{63}{16} - \frac{63}{4} + 18 = 0$

`\text{f}\left(\frac{3}{4}\right) = 0 \text{, so } (4x-3) \text{ is a factor}`

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = \frac{3}{4}$ into $\text{f} ( x )$. The fractional substitution must be seen.
> 
> **A1**: Reaching $0$ with no errors, which shows $( 4 x - 3 )$ is a factor. A written conclusion is good practice but is not required for the mark; an arithmetic slip loses it even if the last line reads $0$.
Since $( 4 x - 3 )$ is a factor, divide $\text{f} ( x )$ by it; write $\text{f} ( x )$ as $( 4 x - 3 )$ multiplied by an unknown quadratic

$4 x^{3} - 7 x^{2} - 21 x + 18 = ( 4 x - 3 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$4 a = 4 \Rightarrow a = 1$

Compare the constant term

$- 3 c = 18 \Rightarrow c = - 6$

Compare the coefficient of $x^{2}$

$- 3 a + 4 b = - 7 \Rightarrow b = - 1$

These give the quadratic factor

$\text{f} ( x ) = ( 4 x - 3 ) ( x^{2} - x - 6 )$

**[A1]**

Factorise the quadratic, using two numbers that multiply to $- 6$ and add to $- 1$, namely $- 3$ and $2$

$x^{2} - x - 6 = ( x - 3 ) ( x + 2 )$

**[M1]**

Combine the factors

$\text{f} ( x ) = ( 4 x - 3 ) ( x - 3 ) ( x + 2 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( 4 x - 3 ) ( a x^{2} + b x + c )$ and comparing coefficients, or dividing by $( 4 x - 3 )$.
> 
> **A1**: Correct quadratic factor $x^{2} - x - 6$.
> 
> **M1**: Factorising the quadratic into two linear factors.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( 4 x - 3 ) ( x - 3 ) ( x + 2 )$, factors in any order.
Set each factor to zero; each gives a root of $\text{f} ( x ) = 0$

$x = \frac{3}{4} ,  3 ,  - 2$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Two correct roots.
> 
> **B1**: All three roots $x = \frac{3}{4} , 3 , - 2$ and no extras. Accept $0 . 75$ for $\frac{3}{4}$, and accept them in any order.

### Q41
Any division can be written as $\frac{\text{dividend}}{\text{divisor}} = \text{quotient} + \frac{\text{remainder}}{\text{divisor}}$, so the divisor is whatever sits underneath the remainder term

$\text{The remainder term is} \frac{4}{x+1} \text{, so the divisor} \text{g} ( x ) \text{is} x + 1$

**[B1]**

> **[mark-scheme]**
> **B1**: Identifying that in the standard division form the divisor appears as the denominator of the remainder term, and that here that denominator is $( x + 1 )$. Accept any wording carrying that idea, for example "the remainder is written over the thing you divided by". Simply asserting "because it is the denominator" with no link to the division form is enough at this level, but a bare "it looks right" is not.
Take $\text{g} ( x ) = x + 1$ and multiply every term by it to clear the fractions

$\text{f} ( x ) = ( x + 1 ) ( 2 x + 3 ) - 4$

**[M1]**

Expand and simplify

$\text{f} ( x ) = 2 x^{2} + 5 x + 3 - 4$

$\text{f} ( x ) = 2 x^{2} + 5 x - 1$

**[A1]**

> **[mark-scheme]**
> **M1**: Multiplying through by $( x + 1 )$ to reach $\text{f} ( x ) = ( x + 1 ) ( 2 x + 3 ) - 4$.
> 
> **A1**: Correct $\text{f} ( x ) = 2 x^{2} + 5 x - 1$.
**Final answer:** **The equation only fixes the ratio **$\frac{\text{f}(x)}{\text{g}(x)}$**, so multiplying both functions by the same non-zero factor leaves that ratio unchanged**

**[B1]**

**Final answer:** **For example, doubling both gives a different pair of functions satisfying the same equation**

$\text{f} ( x ) = 4 x^{2} + 10 x - 2 \text{and} \text{g} ( x ) = 2 x + 2$

**[B1]**

> **[mark-scheme]**
> **B1**: Explaining that only the ratio of $\text{f} ( x )$ to $\text{g} ( x )$ is determined, so both may be multiplied by the same non-zero factor. Accept "any common multiple of both works" or equivalent.
> 
> **B1**: A correct concrete example, i.e. any pair $k ( 2 x^{2} + 5 x - 1 )$ and $k ( x + 1 )$ with $k \neq 1$. A common polynomial factor is equally acceptable, e.g. $\text{f} ( x ) = ( 2 x^{2} + 5 x - 1 ) ( x - 3 )$ with $\text{g} ( x ) = ( x + 1 ) ( x - 3 )$. The example must actually be stated; the explanation alone does not earn this mark.

### Q42
The factor $( 4 x - 5 )$ is zero at $x = \frac{5}{4}$, so by the factor theorem the polynomial is zero there

`4\left(\frac{5}{4}\right)^3 - 9\left(\frac{5}{4}\right)^2 + a\left(\frac{5}{4}\right) + 30 = 0`

**[M1]**

Work out the arithmetic and solve for $a$

$\frac{125}{16} - \frac{225}{16} + \frac{5a}{4} + 30 = 0$

$\frac{5a}{4} = - \frac{95}{4}$

$a = - 19$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the factor theorem at $x = \frac{5}{4}$, substituting into the cubic and equating to zero. The fractional substitution must be seen.
> 
> **A1**: $a = - 19$.
Substitute $a = - 19$ from part (a), then divide by the known factor $( 4 x - 5 )$; write the cubic as $( 4 x - 5 )$ multiplied by an unknown quadratic

$4 x^{3} - 9 x^{2} - 19 x + 30 = ( 4 x - 5 ) ( p x^{2} + q x + r )$

**[M1]**

Compare the coefficient of $x^{3}$

$4 p = 4 \Rightarrow p = 1$

Compare the constant term

$- 5 r = 30 \Rightarrow r = - 6$

Compare the coefficient of $x^{2}$

$- 5 p + 4 q = - 9 \Rightarrow q = - 1$

These give the quadratic factor

$4 x^{3} - 9 x^{2} - 19 x + 30 = ( 4 x - 5 ) ( x^{2} - x - 6 )$

Factorise the quadratic, using two numbers that multiply to $- 6$ and add to $- 1$, namely $- 3$ and $2$

$( 4 x - 5 ) ( x - 3 ) ( x + 2 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $a = - 19$ and writing the cubic as $( 4 x - 5 ) ( p x^{2} + q x + r )$, comparing coefficients or dividing by $( 4 x - 5 )$. Follow through from part (a)'s value of $a$.
> 
> **A1**: Fully factorised $( 4 x - 5 ) ( x - 3 ) ( x + 2 )$, factors in any order.

### Q43
Since $( 2 x - 3 )$ is a factor, write $\text{f} ( x )$ as $( 2 x - 3 )$ multiplied by an unknown quadratic

$6 x^{3} - 19 x^{2} + 11 x + 6 = ( 2 x - 3 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$2 a = 6 \Rightarrow a = 3$

Compare the constant term

$- 3 c = 6 \Rightarrow c = - 2$

Compare the coefficient of $x^{2}$

$- 3 a + 2 b = - 19 \Rightarrow b = - 5$

$\text{f} ( x ) = ( 2 x - 3 ) ( 3 x^{2} - 5 x - 2 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( 2 x - 3 ) ( a x^{2} + b x + c )$ and comparing coefficients, or dividing by $( 2 x - 3 )$.
> 
> **A1**: Correct $a = 3 , b = - 5 , c = - 2$, giving $\text{f} ( x ) = ( 2 x - 3 ) ( 3 x^{2} - 5 x - 2 )$.
Factorise the quadratic from part (a); $3 \times ( - 2 ) = - 6$, and $- 6$ and $1$ multiply to $- 6$ and add to $- 5$

$3 x^{2} - 5 x - 2 = ( 3 x + 1 ) ( x - 2 )$

**[M1 A1]**

Combine with the factor from part (a)

$\text{f} ( x ) = ( 2 x - 3 ) ( 3 x + 1 ) ( x - 2 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Attempting to factorise $3 x^{2} - 5 x - 2$ into two linear factors.
> 
> **A1**: Correct factors $( 3 x + 1 ) ( x - 2 )$.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( 2 x - 3 ) ( 3 x + 1 ) ( x - 2 )$, factors in any order. Follow through from part (a)'s quadratic.
Set each factor to zero; each gives a root of $\text{f} ( x ) = 0$

$x = \frac{3}{2} ,  - \frac{1}{3} ,  2$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Two correct roots.
> 
> **B1**: All three roots $x = \frac{3}{2} , - \frac{1}{3} , 2$ and no extras. Accept decimals $1 . 5$ and $- 0 . 333 \dots$, and accept them in any order.

### Q44
Since $( x + 4 )$ is a factor, the factor theorem gives $\text{f} ( - 4 ) = 0$, so substitute $x = - 4$

$p ( - 4 )^{3} + ( 5 p + 1 ) ( - 4 )^{2} + 5 q ( - 4 ) - 2 q - 2 = 0$

**[M1]**

Expand and collect like terms

$- 64 p + 80 p + 16 - 20 q - 2 q - 2 = 0$

$16 p - 22 q = - 14$

Divide through by $2$ to obtain the first equation

$8 p - 11 q = - 7$

**[A1]**

When $\text{f} ( x )$ is divided by $( x + 1 )$ the remainder is $- 12$, so by the remainder theorem $\text{f} ( - 1 ) = - 12$

$p ( - 1 )^{3} + ( 5 p + 1 ) ( - 1 )^{2} + 5 q ( - 1 ) - 2 q - 2 = - 12$

**[M1]**

Expand and collect like terms to obtain the second equation

$- p + 5 p + 1 - 5 q - 2 q - 2 = - 12$

$4 p - 7 q = - 11$

**[A1]**

Solve the two equations simultaneously; doubling the second gives $8 p - 14 q = - 22$, so subtracting eliminates $p$

$( 8 p - 11 q ) - ( 8 p - 14 q ) = - 7 - ( - 22 )$

$3 q = 15 \Rightarrow q = 5$

Substitute back into the second equation to find $p$

$4 p - 7 ( 5 ) = - 11 \Rightarrow 4 p = 24$

$p = 6 ,  q = 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the factor theorem, substituting $x = - 4$ into $\text{f} ( x )$ and equating to zero. Dividing by $( x + 4 )$ and equating the constant remainder to zero is equally acceptable.
> 
> **A1**: A correct simplified equation in $p$ and $q$, e.g. $8 p - 11 q = - 7$ or the unsimplified $16 p - 22 q = - 14$.
> 
> **M1**: Using the remainder theorem, substituting $x = - 1$ into $\text{f} ( x )$ and equating to $- 12$. Dividing by $( x + 1 )$ and equating the constant remainder to $- 12$ is equally acceptable.
> 
> **A1**: A correct simplified equation in $p$ and $q$, e.g. $4 p - 7 q = - 11$.
> 
> **A1**: Both $p = 6$ and $q = 5$, from correct working throughout. There is no follow-through here: if either equation is wrong, this mark is lost even if the wrong pair is then solved perfectly.

### Q45
The factor $( 2 x + 1 )$ is zero at $x = - \frac{1}{2}$, so by the factor theorem evaluate $\text{f} ( x )$ there and check it is zero

`\text{f}\left(-\frac{1}{2}\right) = 4\left(-\frac{1}{2}\right)^3 - 7\left(-\frac{1}{2}\right) - 3`

**[M1]**

Work out the arithmetic

$= - \frac{1}{2} + \frac{7}{2} - 3 = 0$

`\text{f}\left(-\frac{1}{2}\right) = 0 \text{, so } (2x+1) \text{ is a factor}`

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = - \frac{1}{2}$ into $\text{f} ( x )$. The fractional substitution must be seen; substituting $x = \frac{1}{2}$ or $x = - 1$ scores nothing.
> 
> **A1**: Reaching $0$ with no errors, which shows $( 2 x + 1 )$ is a factor. A written conclusion is good practice but is not required for the mark; an arithmetic slip loses it even if the last line reads $0$.
Since $( 2 x + 1 )$ is a factor, divide $\text{f} ( x )$ by it; write $\text{f} ( x )$ as $( 2 x + 1 )$ multiplied by an unknown quadratic

$4 x^{3} + 0 x^{2} - 7 x - 3 = ( 2 x + 1 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$2 a = 4 \Rightarrow a = 2$

Compare the constant term

$c = - 3$

Compare the coefficient of $x^{2}$

$a + 2 b = 0 \Rightarrow b = - 1$

These give the quadratic factor

$\text{f} ( x ) = ( 2 x + 1 ) ( 2 x^{2} - x - 3 )$

**[A1]**

Factorise the quadratic; $2 \times ( - 3 ) = - 6$, and $- 3$ and $2$ multiply to $- 6$ and add to $- 1$

$2 x^{2} - x - 3 = ( 2 x - 3 ) ( x + 1 )$

**[M1]**

Combine the factors

$\text{f} ( x ) = ( 2 x + 1 ) ( 2 x - 3 ) ( x + 1 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( 2 x + 1 ) ( a x^{2} + b x + c )$ and comparing coefficients, or dividing by $( 2 x + 1 )$. The missing $x^{2}$ term must be handled as $0 x^{2}$.
> 
> **A1**: Correct quadratic factor $2 x^{2} - x - 3$.
> 
> **M1**: Factorising the quadratic into two linear factors.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( 2 x + 1 ) ( 2 x - 3 ) ( x + 1 )$, factors in any order.
Set each factor to zero; each gives a root of $\text{f} ( x ) = 0$

$x = - \frac{1}{2} ,  \frac{3}{2} ,  - 1$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Two correct roots.
> 
> **B1**: All three roots $x = - \frac{1}{2} , \frac{3}{2} , - 1$ and no extras. Accept decimals $- 0 . 5$ and $1 . 5$, and accept them in any order.

### Q46
**Method 1 - Long Division**

Divide the cubic by $( x - 5 )$, writing the missing $x^{2}$ term as $0 x^{2}$ so that the columns line up

![Long division tableau dividing x cubed plus zero x squared minus 19x minus 30 by x minus 5, giving quotient x squared plus 5x plus 6 and remainder zero](assets/021-long-division-tableau-dividing-x-cubed-plus-zero.png)

**[M1]**

Read the quotient from the top of the tableau; the remainder is zero

$x^{2} + 5 x + 6$

**[A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $x^{3} - 19 x - 30$ by $( x - 5 )$, by any valid method, reaching a partial quotient of the form $x^{2} + k x$.
> 
> **A1**: Correct quotient $x^{2} + 5 x + 6$, with zero remainder. Accept the factorised $( x + 2 ) ( x + 3 )$.

**Method 2 - Inspection**

Write the cubic as $( x - 5 )$ multiplied by an unknown quadratic

$x^{3} - 19 x - 30 = ( x - 5 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 1$

Compare the constant term

$- 5 c = - 30 \Rightarrow c = 6$

Compare the coefficient of $x^{2}$

$- 5 a + b = 0 \Rightarrow b = 5$

$x^{2} + 5 x + 6$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $x^{3} - 19 x - 30 = ( x - 5 ) ( a x^{2} + b x + c )$ and comparing coefficients.
> 
> **A1**: Correct quotient $x^{2} + 5 x + 6$.

### Q47
Any division can be written as $\text{dividend} = ( \text{divisor} ) ( \text{quotient} ) + \text{remainder}$, so write that identity out

$x^{3} + a x^{2} + 4 x - 1 = ( x + 2 ) ( x^{2} - 4 x + 12 ) + b$

**[M1]**

Expand the right hand side

$= x^{3} - 4 x^{2} + 12 x + 2 x^{2} - 8 x + 24 + b$

$= x^{3} - 2 x^{2} + 4 x + 24 + b$

Compare the coefficient of $x^{2}$

$a = - 2$

**[A1]**

Compare the constant terms

$24 + b = - 1$

$b = - 25$

**[A1]**

> **[exam-tip]**
> Once you have expanded, the coefficient of $x$ comes out as $4$ on both sides without you having used it. That is a free check that you multiplied out correctly, so glance at it before writing down your answers.

> **[mark-scheme]**
> **M1**: Writing the division identity $x^{3} + a x^{2} + 4 x - 1 = ( x + 2 ) ( x^{2} - 4 x + 12 ) + b$ and expanding the product. Accept an equivalent route, such as dividing $x^{3} + a x^{2} + 4 x - 1$ by $( x + 2 )$ and matching the given quotient.
> 
> **A1**: $a = - 2$.
> 
> **A1**: $b = - 25$.

### Q48
Every term has a factor of $x$, so take that out first

$15 x^{3} + 19 x^{2} - 10 x = x ( 15 x^{2} + 19 x - 10 )$

**[M1]**

Factorise the quadratic; $15 \times ( - 10 ) = - 150$, and $25$ and $- 6$ multiply to $- 150$ and add to $19$

$15 x^{2} + 19 x - 10 = ( 5 x - 2 ) ( 3 x + 5 )$

Combine with the common factor

$x ( 5 x - 2 ) ( 3 x + 5 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Taking out the common factor of $x$ to reach $x ( 15 x^{2} + 19 x - 10 )$, or otherwise beginning a valid factorisation.
> 
> **A1**: Fully factorised $x ( 5 x - 2 ) ( 3 x + 5 )$, factors in any order. The $x$ must be there: "completely" means all three factors, so $( 5 x - 2 ) ( 3 x + 5 )$ on its own does not score.

### Q49
Since $\text{f} ( 2 ) = 0$, substitute $x = 2$ and set the result to zero

$8 + 4 r + 2 s - 30 = 0$

**[M1]**

Simplify to obtain the first equation

$2 r + s = 11$

**[A1]**

Since $\text{f} ( - 3 ) = - 240$, substitute $x = - 3$ and set the result to $- 240$

$- 27 + 9 r - 3 s - 30 = - 240$

**[M1]**

Simplify to obtain the second equation

$3 r - s = - 61$

**[A1]**

Add the two equations to eliminate $s$

$5 r = - 50 \Rightarrow r = - 10$

**[M1]**

Substitute back into the first equation to find $s$

$2 ( - 10 ) + s = 11$

$r = - 10 ,  s = 31$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = 2$ into $\text{f} ( x )$ and equating to zero.
> 
> **A1**: Correct first equation, e.g. $2 r + s = 11$.
> 
> **M1**: Substituting $x = - 3$ into $\text{f} ( x )$ and equating to $- 240$.
> 
> **A1**: Correct second equation, e.g. $3 r - s = - 61$.
> 
> **M1**: Solving the two equations simultaneously by elimination or substitution.
> 
> **A1**: Both $r = - 10$ and $s = 31$.
From part (a), $\text{f} ( 2 ) = 0$, so $( x - 2 )$ is a factor; divide $\text{f} ( x )$ by it, writing $\text{f} ( x )$ as $( x - 2 )$ times an unknown quadratic

$x^{3} - 10 x^{2} + 31 x - 30 = ( x - 2 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 1$

Compare the constant term

$- 2 c = - 30 \Rightarrow c = 15$

Compare the coefficient of $x^{2}$

$- 2 a + b = - 10 \Rightarrow b = - 8$

These give the quadratic factor

$\text{f} ( x ) = ( x - 2 ) ( x^{2} - 8 x + 15 )$

Factorise the quadratic, using two numbers that multiply to $15$ and add to $- 8$, namely $- 3$ and $- 5$

$x^{2} - 8 x + 15 = ( x - 3 ) ( x - 5 )$

**[A1]**

Combine the factors

$\text{f} ( x ) = ( x - 2 ) ( x - 3 ) ( x - 5 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Using $( x - 2 )$ as a factor and comparing coefficients (or dividing) to reach $x^{2} - 8 x + 15$.
> 
> **A1**: Correct factors $( x - 3 ) ( x - 5 )$.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x - 2 ) ( x - 3 ) ( x - 5 )$, factors in any order. Follow through from part (a)'s values of $r$ and $s$.

### Q50
The factor $( 5 x - 2 )$ is zero at $x = \frac{2}{5}$, so by the factor theorem evaluate the cubic there and check it is zero

`25\left(\frac{2}{5}\right)^3 + 55\left(\frac{2}{5}\right)^2 - 56\left(\frac{2}{5}\right) + 12`

**[M1]**

Work out the arithmetic

$= \frac{8}{5} + \frac{44}{5} - \frac{112}{5} + \frac{60}{5} = 0$

$\text{The value is} 0 \text{, so} ( 5 x - 2 ) \text{is a factor}$

**[A1]**

Now divide the cubic by $( 5 x - 2 )$; write it as $( 5 x - 2 )$ multiplied by an unknown quadratic

$25 x^{3} + 55 x^{2} - 56 x + 12 = ( 5 x - 2 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$5 a = 25 \Rightarrow a = 5$

Compare the constant term

$- 2 c = 12 \Rightarrow c = - 6$

Compare the coefficient of $x^{2}$

$- 2 a + 5 b = 55 \Rightarrow b = 13$

These give the quadratic factor

$25 x^{3} + 55 x^{2} - 56 x + 12 = ( 5 x - 2 ) ( 5 x^{2} + 13 x - 6 )$

Factorise the quadratic; $5 \times ( - 6 ) = - 30$, and $15$ and $- 2$ multiply to $- 30$ and add to $13$

$5 x^{2} + 13 x - 6 = ( 5 x - 2 ) ( x + 3 )$

**[A1]**

The factor $( 5 x - 2 )$ appears twice, so write the cubic in its fully factorised form and set each distinct factor to zero

$( 5 x - 2 )^{2} ( x + 3 ) = 0$

$x = \frac{2}{5} ,  - 3$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = \frac{2}{5}$ into the cubic. The fractional substitution must be seen.
> 
> **A1**: Reaching $0$ with no errors, which shows $( 5 x - 2 )$ is a factor. A written conclusion is good practice but is not required for the mark; an arithmetic slip loses it even if the last line reads $0$.
> 
> **M1**: Writing the cubic as $( 5 x - 2 ) ( a x^{2} + b x + c )$ and comparing coefficients, or dividing by $( 5 x - 2 )$.
> 
> **A1**: Correct quadratic factor $5 x^{2} + 13 x - 6$, or the fully factorised $( 5 x - 2 )^{2} ( x + 3 )$.
> 
> **A1**: Both solutions $x = \frac{2}{5}$ and $x = - 3$, and no extras. Accept $0 . 4$ for $\frac{2}{5}$. Do not penalise a candidate for giving only two solutions, because there are only two. Listing $\frac{2}{5}$ twice is condoned.

### Q51
Expand the first two brackets

$( 3 x + y ) ( 2 x - 3 y ) = 6 x^{2} - 7 x y - 3 y^{2}$

**[M1]**

Multiply the result by the third bracket and collect like terms

$( 6 x^{2} - 7 x y - 3 y^{2} ) ( x - 2 y ) = 6 x^{3} - 19 x^{2} y + 11 x y^{2} + 6 y^{3}$

$a = 6 ,  b = - 19 ,  c = 11 ,  d = 6$

**[A1]**

> **[mark-scheme]**
> **M1**: Expanding to reach a correct product of two of the brackets, then multiplying by the third.
> 
> **A1**: All four values correct: $a = 6 , b = - 19 , c = 11 , d = 6$.

### Q52
(i)

**Method 1 - Long Division**

Divide $4 x^{3} + 6 x^{2} - 7 x + 2$ by $( x - 2 )$

![Long division tableau dividing 4x cubed plus 6x squared minus 7x plus 2 by x minus 2, giving quotient 4x squared plus 14x plus 21 and a remainder of 44](assets/022-long-division-tableau-dividing-4x-cubed-plus-6x-.png)

**[M1]**

Read the quotient from the top of the tableau and the remainder from the foot

$\text{quotient} 4 x^{2} + 14 x + 21 , \text{remainder} 44$

**[A1 A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $\text{f} ( x )$ by $( x - 2 )$, by any valid method, reaching a partial quotient of the form $4 x^{2} + k x$.
> 
> **A1**: Correct quotient $4 x^{2} + 14 x + 21$.
> 
> **A1**: Correct remainder $44$. Stating the quotient and remainder the wrong way round earns a maximum of 2 of these 3 marks.

**Method 2 - Inspection**

Write the cubic as $( x - 2 )$ multiplied by an unknown quadratic plus a remainder, then compare coefficients

$4 x^{3} + 6 x^{2} - 7 x + 2 = ( x - 2 ) ( a x^{2} + b x + c ) + d$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 4$

Compare the coefficient of $x^{2}$

$- 2 a + b = 6 \Rightarrow b = 14$

Compare the coefficient of $x$

$- 2 b + c = - 7 \Rightarrow c = 21$

Compare the constant term

$- 2 c + d = 2 \Rightarrow d = 44$

$\text{quotient} 4 x^{2} + 14 x + 21 , \text{remainder} 44$

**[A1 A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( x - 2 ) ( a x^{2} + b x + c ) + d$ and comparing coefficients.
> 
> **A1**: Correct quotient $4 x^{2} + 14 x + 21$.
> 
> **A1**: Correct remainder $44$.

(ii)

Use the quotient and remainder from part (i) directly

$4 x^{3} + 6 x^{2} - 7 x + 2 = ( x - 2 ) ( 4 x^{2} + 14 x + 21 ) + 44$

**[B1]**

> **[mark-scheme]**
> **B1**: Correct identity, following from part (i): $( x - 2 ) ( 4 x^{2} + 14 x + 21 ) + 44$, or equivalently $a = 4 , b = 14 , c = 21 , d = 44$.

### Q53
The factor $( 2 x - 3 )$ is zero at $x = \frac{3}{2}$, so by the factor theorem evaluate the cubic there and check it is zero

`2\left(\frac{3}{2}\right)^3 - 13\left(\frac{3}{2}\right)^2 + 23\left(\frac{3}{2}\right) - 12`

**[M1]**

Work out the arithmetic

$= \frac{27}{4} - \frac{117}{4} + \frac{69}{2} - 12 = 0$

$\text{The value is} 0 \text{, so} ( 2 x - 3 ) \text{is a factor}$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = \frac{3}{2}$ into the cubic.
> 
> **A1**: Reaching $0$ with no errors, which shows $( 2 x - 3 )$ is a factor. A written conclusion is good practice but is not required for the mark; an arithmetic slip loses it even if the last line reads $0$.
Since $( 2 x - 3 )$ is a factor, divide the cubic by it; write it as $( 2 x - 3 )$ multiplied by an unknown quadratic

$2 x^{3} - 13 x^{2} + 23 x - 12 = ( 2 x - 3 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$2 a = 2 \Rightarrow a = 1$

Compare the constant term

$- 3 c = - 12 \Rightarrow c = 4$

Compare the coefficient of $x^{2}$

$- 3 a + 2 b = - 13 \Rightarrow b = - 5$

These give the quadratic factor

$2 x^{3} - 13 x^{2} + 23 x - 12 = ( 2 x - 3 ) ( x^{2} - 5 x + 4 )$

Factorise the quadratic

$( 2 x - 3 ) ( x - 1 ) ( x - 4 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing the cubic as $( 2 x - 3 ) ( a x^{2} + b x + c )$ and comparing coefficients, or dividing by $( 2 x - 3 )$.
> 
> **A1**: Fully factorised $( 2 x - 3 ) ( x - 1 ) ( x - 4 )$, factors in any order.
Set each factor to zero; each gives a solution

$x = \frac{3}{2} ,  1 ,  4$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Two correct solutions.
> 
> **B1**: All three solutions $x = \frac{3}{2} , 1 , 4$ and no extras.

### Q54
**Method 1 - Remainder Theorem**

The remainder on dividing by $( x - 2 )$ is the value of $\text{f} ( x )$ at $x = 2$

$\text{f} ( 2 ) = 2 ( 2 )^{3} - ( 2 )^{2} - 16 ( 2 ) + 15 = 16 - 4 - 32 + 15$

**[M1]**

$- 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the remainder theorem, substituting $x = 2$ into $\text{f} ( x )$ (or commencing long division by $( x - 2 )$).
> 
> **A1**: Correct remainder $- 5$.

**Method 2 - Long Division**

Divide $\text{f} ( x )$ by $( x - 2 )$; the constant left at the foot is the remainder

![Long division tableau dividing 2x cubed minus x squared minus 16x plus 15 by x minus 2, giving quotient 2x squared plus 3x minus 10 and a remainder of minus 5](assets/023-long-division-tableau-dividing-2x-cubed-minus-x-.png)

**[M1]**

$- 5$

**[A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $\text{f} ( x )$ by $( x - 2 )$ and working through to the constant at the foot.
> 
> **A1**: Correct remainder $- 5$.
Since $( x + 3 )$ is a factor, divide $\text{f} ( x )$ by it; write $\text{f} ( x )$ as $( x + 3 )$ multiplied by an unknown quadratic

$2 x^{3} - x^{2} - 16 x + 15 = ( x + 3 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 2$

Compare the constant term

$3 c = 15 \Rightarrow c = 5$

Compare the coefficient of $x^{2}$

$3 a + b = - 1 \Rightarrow b = - 7$

These give the quadratic factor

$\text{f} ( x ) = ( x + 3 ) ( 2 x^{2} - 7 x + 5 )$

**[A1]**

Factorise the quadratic

$2 x^{2} - 7 x + 5 = ( 2 x - 5 ) ( x - 1 )$

**[M1]**

Combine the factors

$\text{f} ( x ) = ( x + 3 ) ( 2 x - 5 ) ( x - 1 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( x + 3 ) ( 2 x^{2} + b x + c )$ and comparing coefficients, or dividing by $( x + 3 )$.
> 
> **A1**: Correct quadratic factor $2 x^{2} - 7 x + 5$.
> 
> **M1**: Factorising the quadratic into two linear factors.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x + 3 ) ( 2 x - 5 ) ( x - 1 )$, factors in any order.

### Q55
Make $\text{f} ( x )$ the subject by multiplying every term by $( x + 2 )$

$\text{f} ( x ) = ( x + 2 ) ( 3 x + 4 ) - 2$

**[M1]**

Expand and simplify

$\text{f} ( x ) = 3 x^{2} + 10 x + 8 - 2$

$\text{f} ( x ) = 3 x^{2} + 10 x + 6$

**[A1]**

> **[mark-scheme]**
> **M1**: Multiplying through by $( x + 2 )$ to reach $\text{f} ( x ) = ( x + 2 ) ( 3 x + 4 ) - 2$.
> 
> **A1**: Correct $\text{f} ( x ) = 3 x^{2} + 10 x + 6$.

### Q56
When $\text{f} ( x )$ is divided by $( x - 2 )$ the remainder is $7$, so by the remainder theorem $\text{f} ( 2 ) = 7$

$16 - 20 + 2 a + b = 7$

**[M1]**

Rearrange to obtain the first equation

$2 a + b = 11$

**[A1]**

Since $( 2 x + 3 )$ is a factor, `\text{f}\left(-\frac{3}{2}\right) = 0`

`2\left(-\frac{3}{2}\right)^3 - 5\left(-\frac{3}{2}\right)^2 + a\left(-\frac{3}{2}\right) + b = 0`

**[M1]**

Multiply through by $2$ and rearrange to obtain the second equation

$3 a - 2 b = - 36$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the remainder theorem $\text{f} ( 2 ) = 7$ (or dividing by $( x - 2 )$ and equating the constant remainder to $7$).
> 
> **A1**: Correctly reaching the given $2 a + b = 11$ with no errors.
> 
> **M1**: Using `\text{f}\left(-\frac{3}{2}\right) = 0` (the fractional substitution must be seen, or divide by $( 2 x + 3 )$).
> 
> **A1**: Correctly reaching the given $3 a - 2 b = - 36$ with no errors. As both results are given, the working must be fully correct.
Solve the two equations simultaneously; from the first equation $b = 11 - 2 a$, so substitute into the second

$3 a - 2 ( 11 - 2 a ) = - 36$

**[M1]**

$7 a = - 14 \Rightarrow a = - 2$

$a = - 2 ,  b = 15$

**[A1]**

> **[mark-scheme]**
> **M1**: Solving the simultaneous equations from part (a) by elimination or substitution.
> 
> **A1**: Both $a = - 2$ and $b = 15$. The simultaneous working must be shown; a bare answer from a calculator does not score.

### Q57
The factor $( 2 x - 1 )$ is zero at $x = \frac{1}{2}$, so by the factor theorem the polynomial is zero there

`2\left(\frac{1}{2}\right)^3 + \left(\frac{1}{2}\right)^2 - 25\left(\frac{1}{2}\right) + a = 0`

**[M1]**

Work out the arithmetic and solve for $a$

$\frac{1}{4} + \frac{1}{4} - \frac{25}{2} + a = 0$

$a = 12$

**[A1]**

> **[mark-scheme]**
> **M1**: Using the factor theorem at $x = \frac{1}{2}$, substituting into the cubic and equating to zero.
> 
> **A1**: $a = 12$.

### Q58
Write the numerator as the divisor times the quotient plus the remainder

$x^{2} + a x - 5 = ( x + 1 ) ( x + 3 ) + d$

**[M1]**

Expand the right hand side

$x^{2} + a x - 5 = x^{2} + 4 x + 3 + d$

Compare the coefficient of $x$ and the constant term

$a = 4 ,  d = - 8$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $x^{2} + a x - 5 = ( x + 1 ) ( x + 3 ) + d$ and comparing coefficients (or dividing and matching).
> 
> **A1**: Both $a = 4$ and $d = - 8$.

### Q59
Since $\text{f} ( 2 ) = 0$, substitute $x = 2$ and set the result to zero

$8 + 36 + 2 r + s = 0$

**[M1]**

This gives the first equation

$2 r + s = - 44$

**[A1]**

Since $\text{f} ( - 1 ) = - 54$, substitute $x = - 1$

$- 1 + 9 - r + s = - 54$

**[M1]**

This gives the second equation

$- r + s = - 62$

**[A1]**

Subtract the second equation from the first to eliminate $s$

$3 r = 18 \Rightarrow r = 6$

**[M1]**

Substitute back to find $s$

$s = - 44 - 2 ( 6 ) = - 56$

$r = 6 ,  s = - 56$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = 2$ into $\text{f} ( x )$ and equating to zero.
> 
> **A1**: Correct first equation, e.g. $2 r + s = - 44$.
> 
> **M1**: Substituting $x = - 1$ into $\text{f} ( x )$ and equating to $- 54$.
> 
> **A1**: Correct second equation, e.g. $- r + s = - 62$.
> 
> **M1**: Solving the two equations simultaneously.
> 
> **A1**: Both $r = 6$ and $s = - 56$.
From part (a), $\text{f} ( 2 ) = 0$, so $( x - 2 )$ is a factor; divide $\text{f} ( x )$ by it, writing $\text{f} ( x )$ as $( x - 2 )$ times an unknown quadratic

$x^{3} + 9 x^{2} + 6 x - 56 = ( x - 2 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 1$

Compare the constant term

$- 2 c = - 56 \Rightarrow c = 28$

Compare the coefficient of $x^{2}$

$- 2 a + b = 9 \Rightarrow b = 11$

These give the quadratic factor

$\text{f} ( x ) = ( x - 2 ) ( x^{2} + 11 x + 28 )$

Factorise the quadratic

$x^{2} + 11 x + 28 = ( x + 4 ) ( x + 7 )$

**[A1]**

Combine the factors

$\text{f} ( x ) = ( x - 2 ) ( x + 4 ) ( x + 7 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Using $( x - 2 )$ as a factor and comparing coefficients (or dividing) to reach $x^{2} + 11 x + 28$.
> 
> **A1**: Correct factors $( x + 4 ) ( x + 7 )$.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x - 2 ) ( x + 4 ) ( x + 7 )$.

### Q60
(i)

The divisor is the expression the polynomial is divided by

$x - 3$

**[B1]**

(ii)

The quotient is the polynomial part of the result

$x + 11$

**[B1]**

(iii)

The remainder is the numerator of the term written over the divisor

$29$

**[B1]**

> **[mark-scheme]**
> **B1**: Divisor $x - 3$.
> 
> **B1**: Quotient $x + 11$.
> 
> **B1**: Remainder $29$.
(i)

The highest power of $x$ in $x^{2} + 8 x - 4$ is $2$

$2$

**[B1]**

(ii)

The highest power of $x$ in $x - 3$ is $1$

$1$

**[B1]**

(iii)

**Final answer:** **When a polynomial is divided, the degree of the quotient is the degree of the dividend minus the degree of the divisor**

$2 - 1 = 1$

**Final answer:** **so the quotient has degree **$1$

**[B1]**

> **[mark-scheme]**
> **B1**: Degree $2$.
> 
> **B1**: Degree $1$.
> 
> **B1**: Explaining that the quotient's degree is the dividend's degree minus the divisor's degree, $2 - 1 = 1$.

### Q61
By the factor theorem, $( x + 2 )$ is a factor exactly when $\text{f} ( - 2 ) = 0$, so evaluate $\text{f} ( - 2 )$

$\text{f} ( - 2 ) = 4 ( - 2 )^{3} + 4 ( - 2 )^{2} - 23 ( - 2 ) - 30$

**[M1]**

Work out the arithmetic

$= - 32 + 16 + 46 - 30 = 0$

$\text{f} ( - 2 ) = 0 \text{, so} ( x + 2 ) \text{is a factor}$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = - 2$ into $\text{f} ( x )$.
> 
> **A1**: Reaching $\text{f} ( - 2 ) = 0$ with no errors, which shows the factor. A written conclusion is good practice but is not required for the mark; an arithmetic slip loses it even if the last line reads $0$.
Since $( x + 2 )$ is a factor, divide $\text{f} ( x )$ by it; write $\text{f} ( x )$ as $( x + 2 )$ multiplied by an unknown quadratic

$4 x^{3} + 4 x^{2} - 23 x - 30 = ( x + 2 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$a = 4$

Compare the constant term

$2 c = - 30 \Rightarrow c = - 15$

Compare the coefficient of $x^{2}$

$2 a + b = 4 \Rightarrow b = - 4$

These give the quadratic factor

$\text{f} ( x ) = ( x + 2 ) ( 4 x^{2} - 4 x - 15 )$

**[A1]**

Factorise the quadratic

$4 x^{2} - 4 x - 15 = ( 2 x - 5 ) ( 2 x + 3 )$

**[M1]**

Combine the factors

$\text{f} ( x ) = ( x + 2 ) ( 2 x - 5 ) ( 2 x + 3 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( x + 2 ) ( 4 x^{2} + b x + c )$ and comparing coefficients, or dividing by $( x + 2 )$.
> 
> **A1**: Correct quadratic factor $4 x^{2} - 4 x - 15$.
> 
> **M1**: Factorising the quadratic into two linear factors.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( x + 2 ) ( 2 x - 5 ) ( 2 x + 3 )$, factors in any order.
Set each factor to zero; each gives a root of $\text{f} ( x ) = 0$

$x = - 2 ,  \frac{5}{2} ,  - \frac{3}{2}$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Two correct roots.
> 
> **B1**: All three roots $x = - 2 , \frac{5}{2} , - \frac{3}{2}$ and no extras.

### Q62
Substitute $x = \frac{2}{3}$ into $\text{f} ( x )$ and show the result is zero

`3\left(\frac{2}{3}\right)^3 - 5\left(\frac{2}{3}\right)^2 - 4\left(\frac{2}{3}\right) + 4`

**[M1]**

Work out each term

$= \frac{8}{9} - \frac{20}{9} - \frac{8}{3} + 4 = 0$

**[A1]**

> **[mark-scheme]**
> **M1**: Substituting $x = \frac{2}{3}$ into $\text{f} ( x )$.
> 
> **A1**: Showing the terms sum to $0$. As the result is given, the working must be seen.
Since `\text{f}\left(\frac{2}{3}\right) = 0`, there is a factor with a root at $x = \frac{2}{3}$

$( 3 x - 2 )$

**[B1]**

> **[mark-scheme]**
> **B1**: The factor $( 3 x - 2 )$. Accept `3\left(x - \frac{2}{3}\right)` or equivalent.
Divide $\text{f} ( x )$ by the factor from part (b), writing $\text{f} ( x )$ as $( 3 x - 2 )$ multiplied by an unknown quadratic

$3 x^{3} - 5 x^{2} - 4 x + 4 = ( 3 x - 2 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$3 a = 3 \Rightarrow a = 1$

Compare the constant term

$- 2 c = 4 \Rightarrow c = - 2$

Compare the coefficient of $x^{2}$

$- 2 a + 3 b = - 5 \Rightarrow b = - 1$

These give the quadratic factor

$\text{f} ( x ) = ( 3 x - 2 ) ( x^{2} - x - 2 )$

Factorise the quadratic

$x^{2} - x - 2 = ( x - 2 ) ( x + 1 )$

**[A1]**

Combine the factors

$\text{f} ( x ) = ( 3 x - 2 ) ( x - 2 ) ( x + 1 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( 3 x - 2 ) ( x^{2} + b x + c )$ and comparing coefficients, or dividing by $( 3 x - 2 )$.
> 
> **A1**: Correct quadratic factor $x^{2} - x - 2$.
> 
> **A1**: Fully factorised $( 3 x - 2 ) ( x - 2 ) ( x + 1 )$, factors in any order.
Set each factor to zero

$x = \frac{2}{3} ,  2 ,  - 1$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Two correct solutions.
> 
> **B1**: All three solutions $x = \frac{2}{3} , 2 , - 1$.

### Q63
Take out the common factor of $3 x$ first

$3 x^{3} - 51 x^{2} + 126 x = 3 x ( x^{2} - 17 x + 42 )$

**[M1]**

Factorise the quadratic, using two numbers that multiply to $42$ and add to $- 17$, namely $- 3$ and $- 14$

$3 x ( x - 3 ) ( x - 14 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Taking out the common factor $3 x$ to reach $3 x ( x^{2} - 17 x + 42 )$.
> 
> **A1**: Fully factorised $3 x ( x - 3 ) ( x - 14 )$, factors in any order.

### Q64
Since $( 2 x + 1 )$ is a factor, write $\text{f} ( x )$ as $( 2 x + 1 )$ multiplied by a quadratic and expand to compare coefficients

$2 x^{3} - 3 x^{2} - 72 x - 35 = ( 2 x + 1 ) ( a x^{2} + b x + c )$

**[M1]**

Compare the coefficient of $x^{3}$

$2 a = 2 \Rightarrow a = 1$

Compare the constant term

$c = - 35$

Compare the coefficient of $x^{2}$

$2 b + a = - 3 \Rightarrow b = - 2$

$\text{f} ( x ) = ( 2 x + 1 ) ( x^{2} - 2 x - 35 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $\text{f} ( x ) = ( 2 x + 1 ) ( a x^{2} + b x + c )$ and comparing coefficients (or dividing by $( 2 x + 1 )$).
> 
> **A1**: Correct $a = 1 , b = - 2 , c = - 35$, giving $\text{f} ( x ) = ( 2 x + 1 ) ( x^{2} - 2 x - 35 )$.
Factorise the quadratic, using two numbers that multiply to $- 35$ and add to $- 2$, namely $- 7$ and $5$

$x^{2} - 2 x - 35 = ( x - 7 ) ( x + 5 )$

**[M1 A1]**

Combine with the factor from part (a)

$\text{f} ( x ) = ( 2 x + 1 ) ( x - 7 ) ( x + 5 )$

**[A1]**

> **[mark-scheme]**
> **M1**: Attempting to factorise $x^{2} - 2 x - 35$ into two linear factors.
> 
> **A1**: Correct factors $( x - 7 ) ( x + 5 )$.
> 
> **A1**: Fully factorised $\text{f} ( x ) = ( 2 x + 1 ) ( x - 7 ) ( x + 5 )$, factors in any order.
$\text{f} ( x ) = ( 2 x + 1 ) ( x - 7 ) ( x + 5 )$

Set each factor to zero; each gives a root of $\text{f} ( x ) = 0$

$x = - \frac{1}{2} ,  7 ,  - 5$

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Two correct roots.
> 
> **B1**: All three roots $x = - \frac{1}{2} , 7 , - 5$ and no extras.

### Q65
**Method 1 - Long Division**

Divide the cubic by $( x - 7 )$, working down through the powers of $x$

![Long division tableau dividing x cubed minus 6x squared minus 9x plus 14 by x minus 7, giving quotient x squared plus x minus 2 and remainder zero](assets/024-long-division-tableau-dividing-x-cubed-minus-6x-.png)

**[M1]**

Read the quotient from the top of the tableau; the remainder is zero

$x^{2} + x - 2$

**[A1]**

> **[mark-scheme]**
> **M1**: Commencing division of $x^{3} - 6 x^{2} - 9 x + 14$ by $( x - 7 )$, by any valid method, reaching a partial quotient of the form $x^{2} + k x$.
> 
> **A1**: Correct quotient $x^{2} + x - 2$, with zero remainder.

**Method 2 - Inspection**

Write the cubic as $( x - 7 )$ multiplied by an unknown quadratic

$x^{3} - 6 x^{2} - 9 x + 14 = ( x - 7 ) ( x^{2} + b x + c )$

**[M1]**

Compare the coefficients of $x^{2}$ to find $b$

$b - 7 = - 6 \Rightarrow b = 1$

Compare the constant terms to find $c$

$- 7 c = 14 \Rightarrow c = - 2$

$x^{2} + x - 2$

**[A1]**

> **[mark-scheme]**
> **M1**: Writing $x^{3} - 6 x^{2} - 9 x + 14 = ( x - 7 ) ( x^{2} + b x + c )$ and comparing coefficients.
> 
> **A1**: Correct quotient $x^{2} + x - 2$.
