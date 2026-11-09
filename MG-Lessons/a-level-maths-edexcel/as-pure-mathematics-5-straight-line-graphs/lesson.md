# as-pure-mathematics-5-straight-line-graphs — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Gradient and line equations

![Straight line on coordinate axes with y-intercept at (0,3) and a gradient triangle showing rise -4 and run 2](../assets/001-195b327d-e549-4117-b1ed-9e321c6cd8d7.jpeg)

A straight line is described by how steep it is and where it crosses the $y$-axis. In the equation $y = mx + c$, $m$ represents the gradient and $c$ is the $y$-intercept.

From two points $(x_1, y_1)$ and $(x_2, y_2)$, the gradient is calculated by comparing the vertical change to the horizontal change. This is often summarized as the change in $y$ divided by the change in $x$.

$$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

It is essential to keep the subtraction order consistent for both the numerator and denominator. If you use $y_2 - y_1$ on top, you must use $x_2 - x_1$ on the bottom to ensure the correct sign.

These ideas also appear in linear models used to represent real-life situations. In a model such as $P = 0.6n + 40$, the gradient 0.6 is the rate of change and 40 is the starting value when $n = 0$.

## Worked example: equation through two points

Start with the points $(2, 7)$ and $(6, -1)$. First find the gradient $m$ using the change in $y$ over the change in $x$:
$$
m = \frac{-1 - 7}{6 - 2} = \frac{-8}{4} = -2
$$

Now use the slope-intercept form $y = mx + c$, so the line has the form $y = -2x + c$. Substitute the point $(2, 7)$ into this equation:
$$
7 = -2(2) + c
$$
This simplifies to $7 = -4 + c$, which gives a $y$-intercept of $c = 11$.

Therefore the final equation is:
$$
y = -2x + 11
$$
A quick check with the second point $(6, -1)$ gives $-2(6) + 11 = -1$, confirming the equation is correct.

## General form and intercepts

AS questions often ask for the answer in the form $ax + by + c = 0$, where $a$, $b$ and $c$ are integers. If you start with $y = mx + c$, clear any fractions first and then move every term to one side.

For example, $y = -\frac{1}{2}x + 3$ becomes $2y = -x + 6$ after multiplying through by 2. Rearranging gives
$$
x + 2y - 6 = 0
$$

Intercepts are found by setting one variable to zero. Set $y = 0$ for the $x$-intercept and set $x = 0$ for the $y$-intercept.

Those two intercepts can make a right triangle with the origin. Then use
$$
\frac{1}{2} \times \text{base} \times \text{height}
$$

## Parallel and perpendicular lines

Parallel lines have the same gradient, so they never meet. If one line is $y = -2x + 5$, every parallel line also has gradient $-2$.

Perpendicular lines meet at $90^{\circ}$, so their gradients are negative reciprocals. In symbols,

$$$m_1m_2 = -1$$

If a line is not already in $y = mx + c$ form, rearrange it before comparing. For example, $2x - y + 1 = 0$ becomes $y = 2x + 1$, so its gradient is 2 and a perpendicular line has gradient $-\frac{1}{2}$.

## Worked example: perpendicular bisector

![Line segment joining A(-4,1) and B(2,5) with midpoint M(-1,3) and its perpendicular bisector at right angles](../assets/002-ef77953a-9d4b-4074-850d-979702c1d5fa.jpeg)
To find a perpendicular bisector, you need the midpoint of the segment and a gradient at right angles to it. For points $A(-4, 1)$ and $B(2, 5)$:

$$$m_{AB} = \frac{5 - 1}{2 - (-4)} = \frac{4}{6} = \frac{2}{3}$$ so the perpendicular gradient is $-\frac{3}{2}$. Now find the midpoint $M$:
$$M = \left(\frac{-4 + 2}{2}, \frac{1 + 5}{2}\right) = (-1, 3)$$

Use the formula $y = mx + c$ with the perpendicular gradient $m = -\frac{3}{2}$ and the midpoint $(-1, 3)$. Substituting these values gives:
$$3 = -\frac{3}{2}(-1) + c$$
which results in $c = \frac{3}{2}$.

This results in the equation $y = -\frac{3}{2}x + \frac{3}{2}$. Multiply every term by 2 and rearrange into the general form $ax + by + c = 0$:
$$3x + 2y - 3 = 0$$

## Intersections of lines

At the point where two lines intersect, both equations are true at the same time. That means you can solve the equations simultaneously to find the shared coordinates.

For $2x - y + 1 = 0$ and $x + 3y - 14 = 0$, first rearrange the first line to $y = 2x + 1$. Substitute this expression into the second equation:

$$$x + 3(2x + 1) - 14 = 0$$
By expanding and simplifying, we find that $7x - 11 = 0$ and $x = \frac{11}{7}$.

$$$y = 2\left(\frac{11}{7}\right) + 1 = \frac{29}{7}$$
The intersection is $\left(\frac{11}{7}, \frac{29}{7}\right)$. Always substitute your answer back into both original equations as a final check.

## Check yourself

1. What is the gradient of the line through $(-1, 6)$ and $(5, -3)$?

   - $$-\frac{3}{2}$ ✔

   - $$\frac{3}{2}$

   - $$-\frac{2}{3}$

   - $$\frac{2}{3}$

   _Explanation:_ Use $m = \frac{y_2-y_1}{x_2-x_1} = \frac{-3-6}{5-(-1)} = \frac{-9}{6} = -\frac{3}{2}$. Option C is a very common mistake because it flips the fraction to change in $x$ over change in $y$.

2. The line $3x + 2y - 12 = 0$ meets the axes at $A$ and $B$. What is the area of triangle $AOB$?

   - 24

   - 12 ✔

   - 10

   - 6

   _Explanation:_ Set $y = 0$ to get $x = 4$, and set $x = 0$ to get $y = 6$. So the triangle has base 4 and height 6, giving area $\frac{1}{2} \times 4 \times 6 = 12$. Option A is the common wrong answer from using base $\times$ height and forgetting the $\frac{1}{2}$ for a triangle.

3. Which equation is perpendicular to $2x - y + 1 = 0$ and passes through $(2, 3)$?

   - $$x + 2y - 8 = 0$ ✔

   - $$2x - y - 1 = 0$

   - $$x - 2y + 4 = 0$

   - $$2x + y - 7 = 0$

   _Explanation:_ First rearrange $2x - y + 1 = 0$ to $y = 2x + 1$, so the gradient is 2. A perpendicular line has gradient $-\frac{1}{2}$, and using $(2, 3)$ gives $y = -\frac{1}{2}x + 4$, which rearranges to $x + 2y - 8 = 0$. Option B is the common wrong choice because it keeps the same gradient, so it is parallel, not perpendicular.

4. Where do the lines $2x - y + 1 = 0$ and $x + 3y - 14 = 0$ intersect?

   - $$\left(\frac{11}{7}, \frac{29}{7}\right)$ ✔

   - $$\left(\frac{11}{7}, \frac{22}{7}\right)$

   - $$\left(\frac{29}{7}, \frac{11}{7}\right)$

   - $$(11, 29)$

   _Explanation:_ Rearranging the first line gives $y = 2x + 1$. Substituting into the second gives $x + 3(2x + 1) - 14 = 0$, so $x = \frac{11}{7}$ and then $y = \frac{29}{7}$. Option B is a common mistake because it uses $2x$ but forgets to add the extra 1.
