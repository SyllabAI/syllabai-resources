# as-pure-mathematics-6-2-equation-of-a-circle — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 4 check questions (source: MathsGenie lessons)_

## Circle as a distance rule

![Coordinate diagram of a circle with centre C(a,b), radius r to a point P(x,y), and a tangent at T meeting the radius at 90 degrees](../assets/001-04d4db14-bc43-4f17-b6f8-be7270ccd459.jpeg)

A circle is the set of all points a fixed distance from a fixed point. The fixed point is the centre and the fixed distance is the radius. In coordinates, a circle with centre $(a,b)$ and radius $r$ has equation:

$$$(x-a)^2+(y-b)^2=r^2$$

This is just the distance formula written so every point $(x,y)$ is exactly $r$ units from the centre. Be careful with signs inside the brackets: the centre is the opposite of what you see there. A tangent touches the circle at exactly one point and is perpendicular to the radius at that point.

## From a centre and a point

If you know the centre and one point on the circle, use the distance formula from the centre to that point. When you are writing the equation, it is usually quickest to find $r^2$ directly.

Example: the centre is $(2,-3)$ and the circle passes through $(5,1)$. Then $$r^2=(5-2)^2+(1-(-3))^2=3^2+4^2=25$$ so you have the radius information you need without taking a square root.

Now substitute the centre and $r^2$ into the centre-radius form: $$(x-2)^2+(y+3)^2=25$$ Notice the sign change in $y+3$, because the centre coordinate is $-3$.

## Expanded form to centre-radius form

Expanded equations do not show the centre immediately. To recover it, group the $x$ terms and the $y$ terms, then complete the square in each variable.

For $$x^2+y^2+6x-8y=11$$ first write $$(x^2+6x)+(y^2-8y)=11$$ Work one variable at a time, then complete the square to get $$(x+3)^2-9+(y-4)^2-16=11$$

Now move the constants to the right: $$(x+3)^2+(y-4)^2=36$$ So the centre is $(-3,4)$ and the radius is $6$. If the right-hand side were negative, there would be no real circle.

## Finding an unknown constant first

Sometimes a circle equation contains an unknown constant such as $k$. If a point lies on the circle, its coordinates must satisfy the equation, so substitute them before you complete the square.

Suppose $x^2+y^2+2x-4y+k=0$ passes through $(3,5)$. Substituting the coordinates gives: $$3^2+5^2+2(3)-4(5)+k=0$$ From this calculation, we find that $20+k=0$, which implies $k=-20$.

Now replace $k$ and complete the square: $$(x+1)^2-1+(y-2)^2-4-20=0$$ $$(x+1)^2+(y-2)^2=25$$ Consequently, the centre of the circle is $(-1,2)$ and the radius is $5$.

## Equation from a diameter

If you know the endpoints of a diameter, the centre is the midpoint of those points. For the points $A(-4,6)$ and $B(8,-2)$, the midpoint calculation is:
$$\left(\frac{-4+8}{2},\frac{6+(-2)}{2}\right)=(2,2)$$

Once the centre is found, you can calculate $r^2$ by finding the squared distance from the centre to either endpoint. Using point $A(-4,6)$ and the centre $(2,2)$, we find:
$$r^2=(-4-2)^2+(6-2)^2=36+16=52$$

Substitute the centre and $r^2$ into the standard form to get the final circle equation:
$$(x-2)^2+(y-2)^2=52$$
This method is often quicker than finding the full diameter length and then halving it.

## Intersections with a line

A point where a line meets a circle must satisfy both equations simultaneously. To find these points, substitute the line equation into the circle equation and solve the resulting quadratic equation for $x$ or $y$.

For the circle $$(x-2)^2+(y+1)^2=25$$ and the line $y=2x-3$, note that $y+1=2x-2$. Substituting this into the circle equation gives: $$(x-2)^2+(2x-2)^2=25$$

Expand and collect like terms to reach the standard quadratic form: $$5x^2-12x-17=0$$ Factorising this quadratic equation yields: $$(5x-17)(x+1)=0$$

Solving for $x$ gives $x=\frac{17}{5}$ or $x=-1$. Substituting these values back into $y=2x-3$ gives the intersection points $\left(\frac{17}{5},\frac{19}{5}\right)$ and $(-1,-5)$. Keep exact fractions unless the question asks for decimals.

## Tangents to a circle

![Circle with centre (1,4), point P(-2,0), radius to P, and tangent at P drawn perpendicular to the radius](../assets/002-9e7e3fe0-3d11-4fab-8d2a-b1dbb472f0e4.jpeg)

At the point where a tangent touches the circle, the radius and tangent are perpendicular. This means you should find the radius gradient first, then take the negative reciprocal to find the tangent gradient.

For a circle with centre $(1,4)$ and point $P(-2,0)$ on the circumference, the radius gradient is:
$$m_{\text{radius}}=\frac{0-4}{-2-1}=\frac{-4}{-3}=\frac{4}{3}$$
So the tangent gradient is:
$$m_{\text{tangent}}=-\frac{3}{4}$$

Using the point-slope form through $P(-2,0)$, we find the equation of the tangent line:
$$y-0=-\frac{3}{4}(x+2)$$
$$4y=-3x-6$$
$$3x+4y+6=0$$
If the radius is horizontal, the tangent is vertical, and if the radius is vertical, the tangent is horizontal.

## Check yourself

1. A circle has centre $(-2,3)$ and radius $4$. Which equation is correct?

   - $$(x+2)^2+(y-3)^2=16$ ✔

   - $$(x-2)^2+(y+3)^2=16$

   - $$(x+2)^2+(y-3)^2=4$

   - $$(x-2)^2+(y+3)^2=4$

   _Explanation:_ The correct equation uses opposite signs inside the brackets and $r^2=4^2=16$. The common wrong answer is B, which copies the centre signs directly instead of reversing them inside $(x-a)$ and $(y-b)$. Hint: Write the model $(x-a)^2+(y-b)^2=r^2$ first.

2. What are the centre and radius of $x^2+y^2-10x+4y-11=0$?

   - Centre $(5,-2)$, radius $2\sqrt{10}$ ✔

   - Centre $(-5,2)$, radius $2\sqrt{10}$

   - Centre $(5,-2)$, radius $40$

   - Centre $(5,2)$, radius $\sqrt{40}$

   _Explanation:_ Completing the square gives $(x-5)^2+(y+2)^2=40$, so the centre is $(5,-2)$ and the radius is $\sqrt{40}=2\sqrt{10}$. The common wrong answer is B, which forgets that the centre coordinates have opposite signs to the brackets.

3. The points $A(-4,6)$ and $B(8,-2)$ are endpoints of a diameter. Which is the equation of the circle?

   - $$(x-2)^2+(y-2)^2=52$ ✔

   - $$(x-2)^2+(y-2)^2=104$

   - $$(x+2)^2+(y+2)^2=52$

   - $$(x-2)^2+(y-2)^2=13$

   _Explanation:_ The midpoint of the diameter is $(2,2)$, and the radius squared from that centre to either endpoint is $52$. The common wrong answer is B, which treats the full diameter as if it were the radius.

4. Stretch: The circle $(x-2)^2+(y+1)^2=25$ meets the line $y=2x-3$ at two points. Which pair is correct?

   - $$\left(\frac{17}{5},\frac{19}{5}\right)$ and $(-1,-5)$ ✔

   - $$\left(\frac{17}{5},\frac{2}{5}\right)$ and $(-1,-4)$

   - $$\left(\frac{17}{5},\frac{19}{5}\right)$ and $(-1,5)$

   - $$\left(\frac{5}{17},\frac{19}{5}\right)$ and $(1,-5)$

   _Explanation:_ Solving after substitution gives $x=\frac{17}{5}$ or $x=-1$, and then $y=2x-3$ gives $\frac{19}{5}$ and $-5$. The common wrong answer is C, which makes a sign error when substituting $x=-1$ into $y=2x-3$.
