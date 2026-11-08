# as-pure-mathematics-6-circles — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Standard form of a circle

![Coordinate diagram of a circle with centre C(a,b), point P(x,y), radius r, and the standard equation labelled](../assets/001-f7b1dcac-f736-47c7-a936-f446a79cf73b.jpeg)
A circle is the set of all points a fixed distance from one centre. If the centre is $(a,b)$ and the radius is $r$, then

$$$
(x-a)^2+(y-b)^2=r^2
$$
This is called the standard form of a circle.

The signs inside the brackets are the opposite of the centre coordinates, so $(x+4)^2$ means an $x$-coordinate of $-4$. The number on the right is $r^2$, not $r$.

Every point $(x,y)$ on the circle is exactly $r$ units from the centre, which is why the distance formula leads to the standard equation. For example, $(x+4)^2+(y-1)^2=9$ has centre $(-4,1)$ and radius $3$.

## From a centre and a point

A circle has centre $(3,-1)$ and passes through $P(7,2)$. Start by putting the centre into standard form:
$$
(x-3)^2+(y+1)^2=r^2
$$
This leaves only the value of $r^2$ to find.

Because $P$ lies on the circle, the radius is the distance from $(3,-1)$ to $(7,2)$. It is quicker to calculate $r^2$ directly:
$$
r^2=(7-3)^2+(2-(-1))^2=4^2+3^2=25
$$

Substitute this value into the standard form to finish the equation. The circle is
$$
(x-3)^2+(y+1)^2=25
$$

## Using the endpoints of a diameter

If $A(-3,5)$ and $B(9,-1)$ are the endpoints of a diameter, the centre is the midpoint of $AB$. So
$$\left(\frac{-3+9}{2},\frac{5+(-1)}{2}\right)=(3,2)$$
This midpoint value of $(3,2)$ is the centre of the circle.

Now use the distance from the centre to one endpoint to get $r^2$. Using $A(-3,5)$ and the calculated centre gives
$$r^2=(-3-3)^2+(5-2)^2=36+9=45$$
Using $r^2$ directly avoids an unnecessary square root during the calculation.

Put the centre and $r^2$ into standard form. The resulting equation of the circle is
$$(x-3)^2+(y-2)^2=45$$

## Completing the square to reveal centre and radius

Expanded equations hide the centre and radius, so complete the square in $x$ and $y$ separately. For the following equation, first group the terms as $x^2+4x+y^2-10y=7$: 

$$x^2+y^2+4x-10y=7$$

Now complete each square: $x^2+4x=(x+2)^2-4$ and $y^2-10y=(y-5)^2-25$. Substituting these back into the original equation gives: 

$$(x+2)^2-4+(y-5)^2-25=7$$

Move the constants to the right-hand side to reach the standard form:

$$(x+2)^2+(y-5)^2=36$$

So the centre is $(-2,5)$ and the radius is $6$, with the sign inside each bracket reversed when you read the centre.

## Intersections between a circle and a line

To find where a line meets a circle, substitute the line equation into the circle equation. This turns the problem into a quadratic, and the number of real roots tells you how many intersection points there are.

For the circle with centre $(2,3)$ and radius $5$, the equation is $(x-2)^2+(y-3)^2=25$. If the line is $y=x+2$, then substituting into the circle equation gives:
$$
(x-2)^2+(x-1)^2=25
$$

Expand and solve the quadratic by simplifying the terms:
$$
2x^2-6x-20=0
$$
$$
x^2-3x-10=0
$$
$$
(x-5)(x+2)=0
$$

So $x=5$ or $x=-2$. Using the linear equation $y=x+2$, we find the corresponding $y$-values to get the intersection points $(5,7)$ and $(-2,0)$.

## Tangents and perpendicular gradients

![Coordinate diagram of a circle with centre (-1,2), point A(4,4), a radius to A, and a tangent at A meeting at a right angle](../assets/002-76ea92e7-9160-4216-a14e-b0689e9fa6e1.jpeg)

A tangent touches a circle at exactly one point, and the radius to that point of contact is perpendicular to the tangent. For non-vertical lines, that means the tangent gradient is the negative reciprocal of the radius gradient.

For a circle with centre $(-1,2)$ and point of contact $A(4,4)$, the radius gradient is
$$m_{\text{radius}}=\frac{4-2}{4-(-1)}=\frac{2}{5}$$
So the tangent gradient is $-\frac{5}{2}$.

Use point-gradient form through $A(4,4)$:
$$y-4=-\frac{5}{2}(x-4)$$
Rearranging gives the equation of the tangent line:
$$5x+2y-28=0$$

## Check yourself

1. What are the centre and radius of $(x+4)^2+(y-1)^2=9$?

   - Centre $(-4,1)$, radius $3$ ✔

   - Centre $(4,1)$, radius $3$

   - Centre $(-4,-1)$, radius $9$

   - Centre $(4,-1)$, radius $9$

   _Explanation:_ Standard form is $(x-a)^2+(y-b)^2=r^2$, so $x+4$ means $a=-4$, $y-1$ means $b=1$, and $r=\sqrt{9}=3$. B is the common sign mistake because you must reverse the sign inside each bracket to get the centre.

2. What is the centre and radius of $x^2+y^2-8x+6y=12$?

   - Centre $(4,-3)$, radius $\sqrt{37}$ ✔

   - Centre $(-4,3)$, radius $\sqrt{37}$

   - Centre $(4,-3)$, radius $37$

   - Centre $(-4,-3)$, radius $6$

   _Explanation:_ Completing the square gives $(x-4)^2+(y+3)^2=37$, so the centre is $(4,-3)$ and the radius is $\sqrt{37}$. B is the common sign mistake because $(y+3)^2$ means the centre has $y=-3$, not $y=3$, and C forgets that $37$ is $r^2$, not $r$.

3. A circle has centre $(-1,2)$ and point of contact $A(4,4)$. What is the gradient of the tangent at $A$?

   - $$\frac{2}{5}$

   - $$-\frac{2}{5}$

   - $$-\frac{5}{2}$ ✔

   - $$\frac{5}{2}$

   _Explanation:_ The radius from $(-1,2)$ to $(4,4)$ has gradient $\frac{2}{5}$, so the tangent must have gradient $-\frac{5}{2}$ because perpendicular gradients are negative reciprocals. A is the common wrong answer because it uses the radius gradient itself instead of the tangent gradient.
