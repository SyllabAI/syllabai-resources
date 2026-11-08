# grade-5-5-14-gradient-of-a-line — lesson

_Lane: `gcse-maths-edexcel` · grade 5 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## What gradient means

![Coordinate grids showing a positive line with rise 6 and run 2 and a negative line with fall 6 and run 2](../assets/001-76fa7564-799d-471d-a2e5-b51b25831469.jpeg)

Gradient tells you how steep a straight line is. It compares how much the line goes up or down with how much it goes across.

From left to right, a line that goes up has a positive gradient and a line that goes down has a negative gradient. The bigger the size of the gradient, the steeper the line.

The key idea is rise over run. $$m=\frac{\text{change in }y}{\text{change in }x}$$ Here $m$ means gradient, with the change in $y$ on top and the change in $x$ on the bottom.

## Finding gradient from a grid

On a coordinate grid, choose two exact points where the line crosses grid intersections. Then count the run, which is the change in $x$, and the rise, which is the change in $y$.

For the line through $(0,0)$ and $(2,6)$, the run is $2$ and the rise is $6$. So $$m=\frac{6}{2}=3$$

For the line through $(0,4)$ and $(2,-2)$, the run is $2$ but the rise is $-6$ because the line goes down. So $$m=\frac{-6}{2}=-3$$

## Using the formula with two coordinates

If you know two coordinates, you do not need a graph. Use the formula below and keep the subtraction order consistent on the top and bottom: $$m=\frac{y_2-y_1}{x_2-x_1}$$

For $(3,2)$ and $(7,10)$, substitute carefully: $$m=\frac{10-2}{7-3}=\frac{8}{4}=2$$ The line goes up $2$ for every $1$ across.

Negative coordinates need extra care. For $(-4,1)$ and $(2,4)$, the bottom calculation is $2-(-4)=6$, not $-2$. You can start with either point, but do not swap the order halfway through.

## Finding a missing coordinate

Sometimes the gradient is given and one coordinate contains a letter. Use the same gradient formula, then solve the equation you create.

Example: the line through $(1,-2)$ and $(5,k)$ has gradient $3$. Start by substituting these values into the gradient formula: $$3=\frac{k-(-2)}{5-1}$$

Simplify the fraction first to get $$3=\frac{k+2}{4}$$ Next, multiply both sides by $4$ to get $12=k+2$.

Subtract $2$ from both sides, so $k=10$. This is still a gradient problem, but the final step is just solving an equation.

## Special cases and quick checks

A horizontal line has gradient $0$ because the $y$-values are equal, so the change in $y$ is $0$. For example, using $(1,4)$ and $(6,4)$ gives

$$$m=\frac{0}{5}=0$$

A vertical line has undefined gradient because the $x$-values are equal, so the change in $x$ is $0$. Division by $0$ is not allowed, so a line like $x=3$ has no numerical gradient.

In an exam, do three quick checks at the end. Did you put the $y$-change on top, keep the subtraction order consistent, and choose the correct sign?

## Check yourself

1. A line slopes down as you move from left to right. What must be true about its gradient?

   - It is positive

   - It is negative ✔

   - It is zero

   - It is undefined

   _Explanation:_ The gradient is negative because $x$ increases while $y$ decreases, so the change in $y$ is negative. The common wrong answer C confuses a downward line with a flat line, but gradient $0$ only happens when the line does not go up or down at all.

2. What is the gradient of the line through $(-4,1)$ and $(2,4)$?

   - $$\frac{1}{2}$ ✔

   - $$2$

   - $$-\frac{1}{2}$

   - $$6$

   _Explanation:_ Using $m=\frac{y_2-y_1}{x_2-x_1}$ gives $m=\frac{4-1}{2-(-4)}=\frac{3}{6}=\frac{1}{2}$. The common wrong answer B comes from swapping the changes and calculating $\frac{6}{3}$, but gradient is change in $y$ over change in $x$, not the other way round. Hint: Put the $y$-change on top.

3. Which line has an undefined gradient?

   - $$y=-2$

   - $$x=4$ ✔

   - The line through $(0,0)$ and $(4,2)$

   - The line through $(1,5)$ and $(3,5)$

   _Explanation:_ $$x=4$ is a vertical line, so the change in $x$ is $0$ and the gradient is undefined. The common wrong answer A is horizontal, which has gradient $0$ because the change in $y$ is $0$ instead.
