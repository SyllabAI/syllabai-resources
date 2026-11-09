# grade-7-7-13-the-cosine-rule — lesson

_Lane: `gcse-maths-edexcel` · grade 7 · 7 content steps · 4 check questions (source: MathsGenie lessons)_

## Spotting the opposite side and the included angle

![Triangle ABC with angle A highlighted, side a opposite angle A, and sides b and c meeting at the included angle](../assets/001-e390e1b9-2e41-4ce2-9f63-3ad732abdd06.jpeg)

The Cosine Rule is used in a non-right-angled triangle when you know two sides and the included angle, or when you know all three sides. It is the right choice when Pythagoras and SOHCAHTOA do not fit.

In triangle $ABC$, side $a$ is opposite angle $A$, side $b$ is opposite angle $B$, and side $c$ is opposite angle $C$. The included angle is the angle between the two known sides.

## The Cosine Rule for a missing side

When you know two sides and the included angle, the missing side opposite that angle is found with the Cosine Rule:
$$a^2 = b^2 + c^2 - 2bc\cos A$$

Here $a$ is opposite angle $A$, and $b$ and $c$ are the sides that meet at angle $A$. This looks a bit like Pythagoras, but the extra term adjusts for triangles that are not right-angled.

If $A = 90^\circ$, then $\cos 90^\circ = 0$, so the rule reduces to $a^2 = b^2 + c^2$. For GCSE questions, ensure your calculator is in degrees mode and remember to square root the result of $a^2$ at the end.

## Worked example: finding a side

![Scalene triangle with sides 12 cm and 9 cm meeting at a 100 degree angle, and the opposite side labelled x](../assets/002-1c9d2b51-97c2-4308-b556-16261066e0ca.jpeg)
A triangle has sides 12 cm and 9 cm with an included angle of $100^\circ$. Let the opposite side be $x$.

Substitute into the Cosine Rule and keep the full calculator value at this stage.
$$
\begin{aligned}
x^2 &= 12^2 + 9^2 - 2 \times 12 \times 9 \cos 100^\circ \\
x^2 &= 144 + 81 - 216\cos 100^\circ \\
x^2 &\approx 262.508
\end{aligned}
$$
This gives the value of $x^2$, not $x$.

Now square root to get the actual side length.
$$
x = \sqrt{262.508\ldots} \approx 16.2
$$
So the third side is 16.2 cm to 1 decimal place.

## The Cosine Rule for a missing angle

When all three sides are known, rearrange the Cosine Rule to find an angle. The side being subtracted is always the side opposite the angle you want.

$$$\cos A = \frac{b^2 + c^2 - a^2}{2bc}$$

After you find the cosine value, use inverse cosine to get the angle. Remember to round only at the final step of your calculation.

$$$A = \cos^{-1}\left(\frac{b^2 + c^2 - a^2}{2bc}\right)$$ A common mistake is subtracting the wrong side in the numerator. Always label the opposite side first, then substitute.

## Worked example: finding an angle

We want the angle between the 14 cm and 15 cm sides, so the opposite side is 22 cm. That makes $a = 22$, $b = 14$, and $c = 15$.

Substitute into the rearranged formula and simplify the fraction first.
$$
\cos A = \frac{14^2 + 15^2 - 22^2}{2 \times 14 \times 15} = \frac{-63}{420} = -0.15
$$
A negative cosine tells you the angle will be obtuse.

Now use inverse cosine.
$$
A = \cos^{-1}(-0.15) \approx 98.6^\circ
$$
So the angle between the 14 cm and 15 cm sides is $98.6^\circ$ to 3 significant figures.

## Stretch: algebraic side lengths

Sometimes the side lengths are expressions such as $x+1$ and $2x+1$. You still use the Cosine Rule in exactly the same way, then expand and solve the equation. For example, if the included angle is $60^\circ$ and the opposite side is $\sqrt{91}$, start with:

$$$91 = (x+1)^2 + (2x+1)^2 - 2(x+1)(2x+1)\cos 60^\circ$$

Because $\cos 60^\circ = \frac{1}{2}$, the last term simplifies to $(x+1)(2x+1)$. After expanding, you get $91 = 3x^2 + 3x + 1$, so $3x^2 + 3x - 90 = 0$. The solutions are $x = -6$ or $x = 5$, but only $x = 5$ is valid because side lengths must be positive.

## Area first, then perimeter

Sometimes a perimeter question hides the angle first. If two sides and the area are known, use the area formula below to find the included angle.

$$$ \text{Area} = \frac{1}{2}ab\sin C $$

For sides 15 m and 13 m with area 78 m², solve $78 = \frac{1}{2} \times 15 \times 13 \sin C$. This gives $\sin C = 0.8$, so because the angle is acute, $C \approx 53.130^\circ$. Then use the Cosine Rule for the third side.

$$$ x^2 = 15^2 + 13^2 - 2 \times 15 \times 13 \cos 53.130\ldots^\circ \approx 160 $$

So $x \approx 12.649$, and the perimeter is about 40.6 m to 3 significant figures.

## Check yourself

1. A triangle has $AB = 6$ cm, $AC = 8$ cm and angle $BAC = 50^\circ$. Which side is opposite the $50^\circ$ angle?

   - BC ✔

   - AB

   - AC

   - You cannot tell without more information

   _Explanation:_ Angle $BAC$ is at vertex $A$, so the side opposite it is $BC$. A common wrong answer is C because $AC$ appears in the angle name, but $AC$ forms the angle rather than lying across from it.

2. In the worked example, a student stops after getting $x^2 = 262.508$ and writes "the side is 262.5 cm". What should they do next?

   - Square root 262.508 and then round ✔

   - Round 262.508 to 263 and stop

   - Use $\cos^{-1}(262.508)$

   - Double 262.508 because two sides were known

   _Explanation:_ The Cosine Rule for a side gives $x^2$, so you must square root to get the side length. A common wrong answer is B, but rounding before square rooting still leaves you with $x^2$, not $x$.

3. Which line is correct after using $\cos 60^\circ = \frac{1}{2}$ in the algebraic example?

   - $$91 = (x+1)^2 + (2x+1)^2 - (x+1)(2x+1)$ ✔

   - $$91 = (x+1)^2 + (2x+1)^2 + (x+1)(2x+1)$

   - $$91 = (x+1)^2 + (2x+1)^2 - 2(x+1)(2x+1)$

   - $$\sqrt{91} = (x+1)^2 + (2x+1)^2 - (x+1)(2x+1)$

   _Explanation:_ Since the rule starts with the square of the opposite side, $\left(\sqrt{91}\right)^2 = 91$, and the factor $2\cos 60^\circ$ becomes $1$. A common wrong answer is C, but that forgets that $\cos 60^\circ = \frac{1}{2}$ cancels the 2.

4. In the area-and-perimeter example, why does the word "acute" matter?

   - Because $\sin C = 0.8$ gives two possible angles, and "acute" chooses the smaller one ✔

   - Because the Cosine Rule only works in acute triangles

   - Because the area formula only works for acute angles

   - Because an acute angle makes the perimeter equal the area

   _Explanation:_ When you use inverse sine, both an acute and an obtuse angle can have the same sine value. A common wrong answer is B, but the Cosine Rule works for any triangle, including obtuse ones.
