# grade-7-7-11-the-cosine-rule — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Included angle and opposite side

![Triangle labeled A, B and C with sides a, b and c, angle C highlighted as the included angle and side c shown opposite](../assets/001-75003d7d-32a2-46b9-8e3a-784e880f8897.jpeg)

The Cosine Rule works in any triangle, not only right-angled triangles. It is most useful when you know two sides and the included angle, or all three sides and want an angle.

In the diagram, angle $C$ lies between sides $a$ and $b$, so it is the included angle. Side $c$ is directly across from angle $C$, so it is the opposite side. To find the side opposite the included angle, use:

$$$c^2 = a^2 + b^2 - 2ab\cos C$$

If $C = 90^\circ$, then $\cos 90^\circ = 0$, so the rule reduces to Pythagoras.

## Worked example: finding a missing side

![Triangle with sides 12 cm and 9 cm enclosing a 105 degree angle, with the opposite side labeled x](../assets/002-526e06b6-6769-40b2-b122-e2c2b0d2b641.jpeg)

In this triangle, the known sides are 12 cm and 9 cm, and the included angle is $105^{\circ}$. The unknown side $x$ is opposite the $105^{\circ}$ angle, so we use the side form of the Cosine Rule.

Substitute the values carefully into the formula:
$$x^2 = 12^2 + 9^2 - 2 \times 12 \times 9 \times \cos 105^{\circ}$$
The formula gives $x^2$ first, so do not forget to take the square root at the end of the calculation.

Evaluating the calculation gives:
$$x^2 \approx 280.9$$
Taking the square root gives $x \approx 16.8 \, \text{cm}$ to 1 decimal place. This is sensible because an obtuse angle usually has a relatively long opposite side.

## Finding an angle from three sides

When all three sides are known, rearrange the Cosine Rule to find an angle. If side $c$ is opposite angle $C$, then

$$$\cos C = \frac{a^2 + b^2 - c^2}{2ab}$$

This version gives a cosine value first, not the angle itself. The side opposite the angle is the one being subtracted in the numerator. After calculating the fraction, use $\cos^{-1}$ and make sure your calculator is in degrees.

## Worked example: finding a missing angle

In triangle $ABC$, suppose $AB = 6 \, \text{m}$, $BC = 8 \, \text{m}$ and $AC = 9 \, \text{m}$. To find angle $B$, use the two sides touching $B$ and the side opposite $B$.

Substitute into the rearranged rule:
$$\cos B = \frac{6^2 + 8^2 - 9^2}{2 \times 6 \times 8} = \frac{19}{96} \approx 0.1979$$
Here, the 9 m side is subtracted because it is opposite angle $B$.

Now use inverse cosine:
$$B = \cos^{-1}(0.1979) \approx 78.6^{\circ}$$
So angle $B \approx 79^{\circ}$ to the nearest degree. If you get a small decimal like 1.37 instead, your calculator is probably in radians.

## Cosine Rule with algebra

Some harder questions use algebraic side lengths, but the structure of the rule stays the same. For sides $x + 1$ and $2x - 1$ with included angle $60^\circ$ and opposite side $\sqrt{63}$, start by squaring the opposite side so it becomes 63.

Substitute these values into the formula:
$$63 = (x + 1)^2 + (2x - 1)^2 - 2(x + 1)(2x - 1)\cos 60^\circ$$

Since $\cos 60^\circ = \frac{1}{2}$, this simplifies to $63 = 3x^2 - 3x + 3$. Rearranging and factoring then gives:
$$3x^2 - 3x - 60 = 0 \Rightarrow x^2 - x - 20 = 0 \Rightarrow (x - 5)(x + 4) = 0$$

So $x = 5$ or $x = -4$. We must reject $x = -4$ because it would result in negative side lengths; algebra answers in geometry must still describe a real triangle.

## Area first, then Cosine Rule

Sometimes the area formula helps you find the included angle before using the Cosine Rule. If $AB = 18.5 \, \text{m}$, $AC = 12.8 \, \text{m}$ and the area is $70 \, \text{m}^2$, then $$70 = \frac{1}{2} \times 18.5 \times 12.8 \times \sin A$$ and so $\sin A \approx 0.591$.

Because the angle at $A$ is acute, take $$A \approx \sin^{-1}(0.591) \approx 36.2^\circ$$ The word "acute" matters, because the same sine value could also match an obtuse angle.

Now use the Cosine Rule for the third side: $$BC^2 = 18.5^2 + 12.8^2 - 2 \times 18.5 \times 12.8 \times \cos 36.2^\circ$$ This gives $BC \approx 11.1 \, \text{m}$, so the perimeter is about $42.4 \, \text{m}$ to 3 significant figures.

## Check yourself

1. Which situation points straight to the Cosine Rule for finding a side?

   - You know two sides and the angle between them ✔

   - You know two angles and one side

   - You know two sides and a non-included angle

   - You know one side and one angle in a right-angled triangle

   _Explanation:_ A is correct because the side formula $c^2 = a^2 + b^2 - 2ab\cos C$ needs the two sides around the angle and the included angle itself. C is the most common wrong choice, but if the known angle is not between the known sides then the Sine Rule is usually the better starting point.

2. In a triangle with $AB = 6 \, \text{m}$, $BC = 8 \, \text{m}$ and $AC = 9 \, \text{m}$, which expression gives $\cos B$?

   - $$\frac{6^2 + 8^2 - 9^2}{2 \times 6 \times 8}$ ✔

   - $$\frac{6^2 + 9^2 - 8^2}{2 \times 6 \times 9}$

   - $$\frac{8^2 + 9^2 - 6^2}{2 \times 8 \times 9}$

   - $$\frac{9^2 - 6^2 - 8^2}{2 \times 6 \times 8}$

   _Explanation:_ A is correct because angle $B$ is between the 6 m and 8 m sides, and the 9 m side is opposite angle $B$, so $9^2$ is the term that gets subtracted. B is the most common wrong choice because it subtracts $8^2$, which treats the wrong side as opposite angle $B$.

3. An algebraic Cosine Rule question gives $x = 5$ or $x = -4$. Why is $x = -4$ rejected?

   - It makes at least one side length negative ✔

   - It changes $\cos 60^\circ$

   - It means the triangle is right-angled

   - Quadratic equations are only allowed one solution

   _Explanation:_ A is correct because triangle side lengths must be positive. D is the most common wrong idea, but quadratic equations can give two roots and you then reject any value that makes the geometry impossible.

4. In the area example, after finding $\sin A \approx 0.591$, why is $A \approx 36.2^\circ$ chosen rather than the obtuse alternative?

   - Because the question says angle $A$ is acute ✔

   - Because the Cosine Rule cannot be used with obtuse angles

   - Because $\sin^{-1}$ always gives the larger angle

   - Because the perimeter would otherwise be impossible to calculate

   _Explanation:_ A is correct because one sine value can match two different angles between $0^\circ$ and $180^\circ$, so the wording tells you which one fits. B is the most common wrong idea, but the Cosine Rule works for both acute and obtuse triangles.
