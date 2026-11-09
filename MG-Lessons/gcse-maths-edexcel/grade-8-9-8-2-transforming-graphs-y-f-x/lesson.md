# grade-8-9-8-2-transforming-graphs-y-f-x — lesson

_Lane: `gcse-maths-edexcel` · grade 8 · 7 content steps · 3 check questions (source: MathsGenie lessons)_

## Original graph and the big rule

![Graph showing original curve y=f(x) with transformed curves y=f(x)+2, y=-f(x), y=f(x-3) and y=f(-x) on labelled axes and matching key points marked](../assets/001-b2699c19-2af8-4cdd-8175-ea9fe40ed16a.jpeg)

Treat $y=f(x)$ as the original graph. If $f(a)=b$, then the graph passes through $(a,b)$, so transformations can be tracked by moving old points to new positions.

Outside changes happen after the function gives an output, so they change $y$-coordinates. Inside changes happen to the input, so they change $x$-coordinates, and horizontal shifts work in the opposite direction.

Mark a few key points such as intercepts and turning points first. Move those points, then redraw the same overall shape.

## Outside $f(x)$ means vertical change

If a number is outside the function, it acts on the output. Keep the $x$-coordinates the same and change only the $y$-coordinates.

For $y=f(x)+a$, a point $(p,q)$ moves to $(p,q+a)$. Positive $a$ moves the graph up and negative $a$ moves it down.

For $y=kf(x)$, a point $(p,q)$ moves to $(p,kq)$. If $k<0$, the graph is also reflected in the $x$-axis, so on $y=-2f(x)$ the point $(1,4)$ becomes $(1,-8)$.

## Inside the bracket means horizontal change

If the change is inside the bracket, it affects the input before the function acts. So the $y$-coordinates stay the same and the $x$-coordinates move.

The sign is opposite for shifts: $y=f(x-5)$ moves right 5, while $y=f(x+4)$ moves left 4. A safe method is to solve the bracket equal to the old input.

Example: if $(-1,2)$ is on $y=f(x)$, then on $y=f(x-4)$ solve $x-4=-1$. This gives $x=3$, so the new point is $(3,2)$.

## Multiplying inside changes $x$ by division

For $y=f(kx)$, the multiplier is inside the bracket, so it changes the inputs. To find the new point, divide the old $x$-coordinate by $k$ and keep the $y$-coordinate the same.

So $y=f(2x)$ halves every $x$-coordinate, and $y=f(-x)$ reflects the graph in the $y$-axis. A negative inside changes the sign of $x$, not $y$.

Worked example: if $(-4,3)$, $(0,-1)$ and $(6,2)$ lie on $y=f(x)$, then on $y=f(-2x)$ they become $(2,3)$, $(0,-1)$ and $(-3,2)$. The graph is reflected in the $y$-axis and compressed horizontally by scale factor $\frac{1}{2}$.

## Quick decision rules

When you read a transformed equation, first decide whether the change is outside $f$ or inside it. Outside means change $y$ directly, while inside means change $x$ instead.

Reflections give a quick check. In $y=-f(x)$ the $y$-values change sign, so the mirror line is the $x$-axis, while in $y=f(-x)$ the $x$-values change sign, so the mirror line is the $y$-axis.

## A point map for combined transformations

For a graph like $y=af(bx+c)+d$, track one old point $(p,q)$ at a time. Solve $bx+c=p$ to find the new $x$-coordinate, then calculate $aq+d$ to find the new $y$-coordinate.

This point map avoids guessing the order of transformations. It is especially useful for turning points and intercepts.

Worked example: suppose $(2,-1)$ is a turning point on $y=f(x)$ and the new graph is $y=3f(2x-4)+5$. The old input is 2, so solve $2x-4=2$, then $2x=6$, so $x=3$.

The old output is -1, so the new output is $3(-1)+5=2$. The turning point moves to $(3,2)$.

## Working backwards from two graphs

Sometimes you are shown the original graph and the transformed graph and must write the equation. Match a key point on the original to the same feature on the new graph, then compare the change in $x$ and the change in $y$ separately.

If a point has moved 5 units right with the same shape, write $x-5$ inside the bracket. If it has moved 2 units down, write $-2$ outside the function.

For example, if a vertex moves from $(0,0)$ to $(5,-2)$ with the same shape, the transformed graph is $y=f(x-5)-2$.

Always check the shape before you finish. A mirror image means a reflection, and a wider or narrower graph means a scale factor is needed as well.

## Check yourself

1. If $f(-2)=5$, which point lies on $y=f(x)$?

   - $$(-2,5)$ ✔

   - $$(5,-2)$

   - $$(-2,-5)$

   - $$(2,5)$

   _Explanation:_ Because the input becomes the $x$-coordinate and the output becomes the $y$-coordinate. The common wrong answer $(5,-2)$ swaps them, but $f(-2)=5$ means $x=-2$ and $y=5$.

2. The graph of $y=f(x+4)$ is obtained from $y=f(x)$ by

   - translating 4 units left ✔

   - translating 4 units right

   - translating 4 units up

   - reflecting in the $y$-axis

   _Explanation:_ The $+4$ is inside the bracket, so the horizontal shift works oppositely and the graph moves left 4. The common wrong answer is "right 4", but that would be $y=f(x-4)$.

3. If $(6,2)$ lies on $y=f(x)$, which point lies on $y=f(-2x)$?

   - $$(-3,2)$ ✔

   - $$(3,2)$

   - $$(-12,2)$

   - $$(12,2)$

   _Explanation:_ The $-2$ is inside the bracket, so divide the old $x$-coordinate by $-2$ and keep $y$ the same, giving $6 \div -2 = -3$. The common wrong answer $(3,2)$ divides by 2 but forgets the reflection in the $y$-axis caused by the negative sign.
