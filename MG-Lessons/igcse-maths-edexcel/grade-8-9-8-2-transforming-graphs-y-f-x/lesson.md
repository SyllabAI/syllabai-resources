# grade-8-9-8-2-transforming-graphs-y-f-x — lesson

_Lane: `igcse-maths-edexcel` · grade 8 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Start with the original graph

![Coordinate graph showing original curve y=f(x), an upward shift y=f(x)+2, and a right shift y=f(x-3), with matching points marked](../assets/001-96d0df0e-1044-44d1-bd57-dcff80b0e046.jpeg)
The graph $y=f(x)$ is the original function. If the graph contains the point $(3,6)$, then when the input is 3 the output is 6, so $f(3)=6$.

A transformation moves every point on the graph to a new position. The key idea is: changes outside the bracket affect the $y$-values, while changes inside the bracket affect the $x$-values and usually do the opposite.

A quick memory trick is "outside does what it says, inside does the opposite". We will track coordinates so each transformation has a clear rule.

## Outside the bracket changes $y$

In $y=f(x)+a$, add $a$ to every $y$-value, so the graph moves up or down without changing shape. In $y=af(x)$, multiply every $y$-value by $a$, so the graph gets taller, shorter, or reflected.

Worked example: take the point $(2,-3)$ on $y=f(x)$ and transform it to $y=2f(x)+5$. The $x$-coordinate stays as 2, then the $y$-coordinate changes in order: $2 \times (-3)+5=-1$.

So the image of $(2,-3)$ is $(2,-1)$. If the multiplier is negative, such as in $y=-f(x)$, the graph is reflected in the $x$-axis.

## Inside the bracket changes $x$

In $y=f(x-a)$, the graph moves right by $a$, and in $y=f(x+a)$, the graph moves left by $a$. Because the change is inside the bracket, the transformation affects the $x$-coordinates and the direction is opposite to the sign you see.

In $y=f(kx)$, divide each $x$-coordinate by $k$. For example, the point $(8,3)$ on $y=f(x)$ becomes $(4,3)$ on $y=f(2x)$ because $8 \div 2=4$, which pulls the graph closer to the $y$-axis.

Worked example: the point $(1,5)$ on $y=f(x)$ moves on $y=f(x-4)$. Since the $-4$ is inside the bracket, we do the opposite to the $x$-coordinate: $1+4=5$. The $y$-value remains unchanged, so the new point is $(5,5)$.

## Reflections and combined transformations

For a point on $y=f(x)$, the coordinates change in different ways under different transformations.

If $(1,3)$ lies on $y=f(x)$, then:
- on $y=2f(x)$ it becomes $(1,6)$;
- on $y=f(2x)$ it becomes $(\frac{1}{2},3)$, so this is a horizontal compression by scale factor $\frac{1}{2}$;
- on $y=-f(x)$ it becomes $(1,-3)$;
- on $y=f(-x)$ it becomes $(-1,3)$.

A minus sign outside the bracket reflects the graph in the $x$-axis, changing $(x,y)$ to $(x,-y)$. A minus sign inside the bracket reflects it in the $y$-axis, changing $(x,y)$ to $(-x,y)$.

You can also combine transformations. If $(4,5)$ lies on $y=f(x)$, then on $y=2f(x-3)-7$ the $x$-coordinate becomes $4+3=7$ and the $y$-coordinate becomes $2 \times 5 - 7 = 3$.

So the new point is $(7,3)$. A safe method is to deal with the transformations inside the bracket for the $x$-coordinate first, then apply the outside changes to determine the $y$-coordinate.

## Writing the transformation clearly

In an exam, name the type of transformation, then give the direction or axis, and finally the number of units or scale factor. Good descriptions are "translation 5 units left", "reflection in the $y$-axis", or "horizontal compression by scale factor $\frac{1}{4}$".

Be precise with inside multipliers. The graph $y=f(4x)$ is not a stretch by 4; it is a horizontal compression by scale factor $\frac{1}{4}$ because every $x$-value is divided by 4.

If you are unsure, pick a clear point and track it. If the point moves closer to the $y$-axis, you are dealing with a horizontal compression.

## Check yourself

1. If the graph $y=f(x)$ passes through $(3,6)$, what is $f(3)$?

   - 6 ✔

   - 3

   - 9

   - $$-6$

   _Explanation:_ The point $(3,6)$ means input 3 gives output 6, so $f(3)=6$. The common wrong answer 3 is the $x$-coordinate, but $f(3)$ asks for the matching $y$-value.

2. Which description is correct for $y=f(x+5)$?

   - A translation 5 units left ✔

   - A translation 5 units right

   - A translation 5 units up

   - A horizontal stretch by scale factor 5

   _Explanation:_ The $+5$ is inside the bracket, so it affects the $x$-values in the opposite direction. The common wrong answer is "right 5" because students read the sign literally, but inside transformations reverse the direction.

3. How should you describe the transformation from $y=f(x)$ to $y=f(4x)$?

   - A horizontal stretch by scale factor 4

   - A horizontal compression by scale factor $\frac{1}{4}$ ✔

   - A vertical stretch by scale factor 4

   - A translation 4 units right

   _Explanation:_ In $f(4x)$, the 4 is inside the bracket, so it affects the $x$-values oppositely: each $x$-value is divided by 4. The common wrong answer "stretch by 4" forgets the inside-opposite rule.
