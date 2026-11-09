# grade-5-11-sohcahtoa-trigonometry — lesson

_Lane: `igcse-maths-edexcel` · grade 5 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Start with the right-angled triangle

![Right-angled triangle labelled opposite, adjacent and hypotenuse relative to angle theta](../assets/001-8fda46c2-5724-42f5-87c9-c799270a0132.jpeg)

A right-angled triangle has one angle of $90^\circ$, usually shown by a small square. The longest side, opposite the right angle, is always the hypotenuse.

The other two side names depend on the angle you choose. Relative to angle $\theta$, the side across from it is the opposite side, and the side next to it that is not the hypotenuse is the adjacent side.

A common mistake is thinking adjacent means "the bottom side". It really means "next to the chosen angle", so opposite and adjacent can swap if you use a different angle.

## SOHCAHTOA and choosing the ratio

SOHCAHTOA is a memory aid that links an angle in a right-angled triangle to a pair of sides. Write the three ratios like this.

$$$\sin \theta = \frac{\text{opposite}}{\text{hypotenuse}}$$
$$\cos \theta = \frac{\text{adjacent}}{\text{hypotenuse}}$$
$$\tan \theta = \frac{\text{opposite}}{\text{adjacent}}$$

Choose the ratio from the two sides you know or need. Opposite and hypotenuse means sine, adjacent and hypotenuse means cosine, and opposite and adjacent means tangent. Do not choose the ratio from where the side sits on the page. Choose it from the labels relative to the angle.

## Worked example: finding a missing side

Example: a right-angled triangle has angle $35^\circ$, opposite side $20 \, \text{cm}$, and hypotenuse $x$. Because we are using opposite and hypotenuse, we choose sine.

$$$\sin 35^\circ = \frac{20}{x}$$ Rearrange carefully by multiplying both sides by $x$, then dividing by $\sin 35^\circ$. This gives $$x \sin 35^\circ = 20$$

$$$x = \frac{20}{\sin 35^\circ}$$ Now use the calculator in degrees mode. $$x = 34.9 \, \text{cm}$$ This result is logical because the hypotenuse should always be longer than the opposite side.

## Worked example: finding a missing angle

When the angle is missing, you still start with SOHCAHTOA. For example, if the adjacent side is $16 \, \text{cm}$ and the hypotenuse is $24 \, \text{cm}$ for angle $x$, you would identify cosine as the relevant ratio.

$$$\cos x = \frac{16}{24}$$ To find the angle, work backwards with the inverse button rather than the ordinary cosine button. Inverse cosine means "the angle whose cosine is this number".

$$$x = \cos^{-1}\left(\frac{16}{24}\right)$$ In degrees mode, $x = 48.2^\circ$. Keep the full calculator value until the final line, then round for your final answer.

## Letters and hidden right triangles

In diagrams with letters, $AB$ means the side joining points $A$ and $B$. For an angle such as $\angle ABC$, the middle letter tells you the vertex, so the angle is at point $B$.

Here is a hidden-triangle example without needing a picture. Suppose trapezium $ABCD$ has $A$ at the bottom left, $B$ at the top left, $C$ at the top right, and $D$ at the bottom right. The parallel vertical sides are $AB = 6\,\text{m}$ and $CD = 4\,\text{m}$, and the bottom side $AD$ is horizontal and $15\,\text{m}$ long. The top side $BC$ slopes down from $B$ to $C$. If $E$ is the point on $AB$ that is level with $C$, then triangle $BEC$ is right-angled, with
$$BE = 6 - 4 = 2\,\text{m} \quad \text{and} \quad EC = 15\,\text{m}.$$

The small angle to the horizontal is $\angle BCE$, because it is the angle between the sloping side $BC$ and the horizontal side $CE$. In right triangle $BEC$,
$$\tan(\angle BCE) = \frac{BE}{EC} = \frac{2}{15}$$
so
$$\angle BCE = \tan^{-1}\left(\frac{2}{15}\right) = 7.6^\circ.$$

If the question asks for the angle between the sloping side $BC$ and the vertical side $BA$, that angle is $\angle ABC$. Because $BA$ is vertical and $CE$ is horizontal, they are perpendicular, so these angles are complementary:
$$\angle ABC = 90^\circ - \angle BCE = 90^\circ - 7.6^\circ = 82.4^\circ.$$

## Check yourself

1. Which side is always opposite the right angle in a right-angled triangle?

   - The hypotenuse ✔

   - The adjacent side

   - The opposite side

   - The shortest side

   _Explanation:_ The hypotenuse is always opposite the $90^\circ$ angle and is always the longest side. The most common wrong answer is C because "opposite" sounds like it should mean opposite the right angle, but opposite is named relative to the angle you are focusing on.

2. A triangle has angle $35^{\circ}$, opposite side $20 \, \text{cm}$, and hypotenuse $x$. Which calculation finds $x$?

   - $$\frac{20}{\sin 35^{\circ}}$ ✔

   - $$20 \sin 35^{\circ}$

   - $$\frac{20}{\cos 35^{\circ}}$

   - $$\tan^{-1}\left(\frac{20}{35}\right)$

   _Explanation:_ Using opposite and hypotenuse means sine, so $\sin 35^{\circ} = \frac{20}{x}$ and rearranging gives $x = \frac{20}{\sin 35^{\circ}}$. The most common wrong answer is B because students multiply by $\sin 35^{\circ}$ instead of dividing, which would make the hypotenuse smaller than 20 cm. Hint: Start from SOH, not from memory of the final formula.

3. In the trapezium example, after finding $\theta = 7.6^\circ$, what should you do next to get the angle between the sloping top and the longer vertical side?

   - Calculate $90^\circ - 7.6^\circ$ ✔

   - Calculate $90^\circ + 7.6^\circ$

   - Calculate $180^\circ - 7.6^\circ$

   - Stop, because $7.6^\circ$ is already the required angle

   _Explanation:_ The tangent calculation found the angle to the horizontal dashed line. To get the angle with the longer vertical side, use the complementary angle: $90^\circ - 7.6^\circ = 82.4^\circ$. The shorter vertical side would give the obtuse angle $90^\circ + 7.6^\circ = 97.6^\circ$.
