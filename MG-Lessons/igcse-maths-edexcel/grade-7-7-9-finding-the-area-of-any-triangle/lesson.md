# grade-7-7-9-finding-the-area-of-any-triangle — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## From base and height to any triangle

![Triangle with base a, sloping side b, included angle theta at the base, and perpendicular height h dropped to the base](../assets/001-a3f92b8e-8b0a-4e0b-9229-843f69a19e31.jpeg)

You already know the triangle area formula $A=\frac{1}{2} \times \text{base} \times \text{height}$. That works when the height is the perpendicular distance to the base, even if the height is not already drawn.

In many exam questions, the perpendicular height is missing. Instead, you are given two sides and the included angle, which is the angle between those two sides.

The diagram shows how dropping a perpendicular creates a right-angled triangle inside the triangle. That right triangle lets us express the height using sine.

## Why the sine formula works

In the right-angled triangle inside the diagram, sine links the height to the sloping side: $\sin\theta=\frac{h}{b}$. So the perpendicular height is $h=b\sin\theta$.

Substitute this height into the usual area formula.
$$A=\frac12 \times a \times h=\frac12 \times a \times b\sin\theta$$
That gives the general rule $A=\frac12 ab\sin\theta$.

This formula works for acute, right, and obtuse included angles because triangle angles lie between $0^\circ$ and $180^\circ$ and sine stays positive there. Keep your calculator in degree mode unless the question says otherwise.

## Worked example with an obtuse angle

A triangle has sides 13 cm and 11 cm with included angle $120^\circ$. Use the sine formula directly because the angle is between the two known sides. Substitute the values to begin the calculation.

$$$A=\frac12 \times 13 \times 11 \times \sin 120^\circ$$

Using degree mode gives $A=61.9208\ldots$. Round only at the end, so the area is $61.9 \, \text{cm}^2$ to 1 decimal place. An obtuse angle works perfectly because $\sin 120^\circ$ is a positive value.

## Working backwards to find an angle

Sometimes the area is given and the angle is unknown. Rearrange the same formula to make $\sin x$ the subject, then use inverse sine to find the value of the missing angle.

For a triangle with sides 12 cm and 17 cm and an area of 80 cm², substitute the values into the formula: $$80=\frac12 \times 12 \times 17 \times \sin x$$ Since $\frac12 \times 12 \times 17=102$, this simplifies to the next step.

$$$\sin x=\frac{80}{102}=\frac{40}{51}$$ Now use $x=\sin^{-1}\left(\frac{40}{51}\right)$, giving $x=51.6^\circ$ to 1 decimal place. If the triangle shows an obtuse angle instead, calculate $180^\circ-51.6^\circ=128.4^\circ$.

## Algebraic side lengths

The method stays the same when the sides contain letters. After substituting into the area formula, you simplify and solve the resulting algebraic equation.

If the sides enclosing $60^\circ$ are $x$ and $x+6$, and the area is $18\sqrt{3}\,\text{cm}^2$, then $$18\sqrt{3} = \frac{1}{2} \times x \times (x+6) \times \sin 60^\circ.$$ Using the exact value $\sin 60^\circ = \frac{\sqrt{3}}{2}$ gives $$18\sqrt{3} = \frac{x(x+6)\sqrt{3}}{4}.$$

Divide by $\sqrt{3}$ and multiply by $4$ to get $$72 = x(x+6).$$ Rearranging this leads to the quadratic equation $$x^2 + 6x - 72 = 0.$$

This factorises to $$(x+12)(x-6) = 0.$$ We reject the negative solution $x=-12$ because a length cannot be negative, leaving the final result $x=6\,\text{cm}$.

## Stretch: using a side ratio

If side lengths are given in a ratio, use a common multiplier to represent them. For a ratio of $3:2$, we can write the side lengths as $3k$ and $2k$.

Suppose these sides enclose an angle of $30^\circ$ and the total area is $54 \, \text{cm}^2$. We can substitute these values into the area formula: $$54 = \frac{1}{2} \times 3k \times 2k \times \sin 30^\circ$$

Since $\sin 30^\circ = \frac{1}{2}$, the equation simplifies to $54 = \frac{3}{2}k^2$. This gives $k^2 = 36$, so $k = 6$. Therefore, the shorter side of the triangle is $2k = 12 \, \text{cm}$.

## Check yourself

1. In the formula $A=\frac{1}{2} ab\sin\theta$, what must $\theta$ represent?

   - The angle between sides $a$ and $b$ ✔

   - Any angle in the triangle

   - The largest angle in the triangle

   - The angle opposite the longest side

   _Explanation:_ $$\theta$ must be the included angle between the two sides used in the formula, because sine is turning one of those sides into the perpendicular height. The most common wrong choice is B, but using a non-included angle means the height is not $b\sin\theta$ for those same sides.

2. A triangle has sides 7 m and 12 m with included angle $38^\circ$. Which expression gives its area?

   - $$\frac12 \times 7 \times 12 \times \sin 38^\circ$ ✔

   - $$\frac12 \times 7 \times 12 \times \cos 38^\circ$

   - $$7 \times 12 \times \sin 38^\circ$

   - $$\frac12 \times (7+12) \times \sin 38^\circ$

   _Explanation:_ The correct formula is $A=\frac12 ab\sin\theta$, so you substitute the two sides and the included angle. The most common wrong choice is B, but cosine gives the adjacent component of a side, not the perpendicular height needed for area.

3. The equation $x^2+6x-72=0$ comes from a triangle area problem. Which value of $x$ is valid?

   - 6 ✔

   - -12

   - Both 6 and -12

   - 12

   _Explanation:_ Factoring gives $x=6$ or $x=-12$, but only $x=6$ can be a length. The most common wrong choice is -12 because it solves the algebra, yet it must be rejected in geometry since lengths cannot be negative. Hint: Solve first, then think about what $x$ represents.

4. Two sides of a triangle are in the ratio $4:3$ and enclose an angle of $30^\circ$. If the area is $48 \, \text{cm}^2$, what is the shorter side?

   - 4 cm

   - 8 cm

   - 12 cm ✔

   - 16 cm

   _Explanation:_ Let the sides be $4k$ and $3k$. Then $48=\frac{1}{2} \times 4k \times 3k \times \sin 30^\circ = 3k^2$, so $k=4$ and the shorter side is $3k=12 \, \text{cm}$. The most common wrong choice is 4 cm because 4 is the value of $k$, not the shorter side itself.
