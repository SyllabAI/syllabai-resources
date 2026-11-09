# grade-7-7-12-the-sine-rule — lesson

_Lane: `gcse-maths-edexcel` · grade 7 · 7 content steps · 3 check questions (source: MathsGenie lessons)_

## Opposite pairs

![Triangle ABC with angles A, B, C and opposite sides BC, AC, AB colour coded to show opposite pairs](../assets/001-002d678d-dd9d-4451-bee2-15c7c34ad14c.jpeg)
The sine rule is usually used in non-right-angled triangles and links each angle to the side directly opposite it. Before you substitute anything, identify the matching side-angle pairs.

In triangle $ABC$, side $BC$ is opposite angle $A$, side $AC$ is opposite angle $B$, and side $AB$ is opposite angle $C$. If two angles are known, find the third first because $A + B + C = 180^\circ$.

## The formula and when to use it

Use the sine rule when you know one complete opposite pair and at least one more side or angle from another pair. If the triangle is right-angled and you are working with opposite, adjacent, and hypotenuse, SOHCAHTOA is often the better choice.

For a missing side, keep the side lengths on top:
$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$$

For a missing angle, many students prefer the equivalent form with sines on top:
$$\frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c}$$

Keep your calculator in degree mode because GCSE triangle questions use degrees unless told otherwise. The most common mistake is pairing an angle with a side that touches it instead of the side across from it.

## Worked example: finding a missing side

In triangle $DEF$, $DE = 14$ cm, angle $F = 101^\circ$, and angle $E = 37^\circ$. The complete opposite pair is $DE = 14$ cm with angle $F = 101^\circ$.

We want $DF$, which is opposite angle $E$. Let $DF = x$ and apply the Sine Rule ratio: $$\frac{x}{\sin 37^\circ} = \frac{14}{\sin 101^\circ}$$

Multiply by $\sin 37^\circ$ to make $x$ the subject: $$x = \frac{14\sin 37^\circ}{\sin 101^\circ} \approx 8.56$$ So $DF \approx 8.6$ cm to 1 decimal place, and it is best to round only at the end.

## Worked example: finding a missing angle

In triangle $GHI$, $GH = 9.5$ m, $GI = 7.0$ m, and angle $I = 72^\circ$. The full known pair is $GH = 9.5$ m opposite angle $I = 72^\circ$.

Side $GI = 7.0$ m is opposite angle $H$, so use the angle form: $$\frac{\sin H}{7.0} = \frac{\sin 72^\circ}{9.5}$$ This gives $$\sin H = \frac{7.0\sin 72^\circ}{9.5} \approx 0.701$$

Now use inverse sine: $$H = \sin^{-1}\left(\frac{7.0\sin 72^\circ}{9.5}\right) \approx 44.5^\circ$$ $\sin^{-1}$ means "find the angle", not "divide by sine".

## Using the sine rule for perimeter

Triangle $ABC$ has $AC = 10.4$ m, angle $B = 112^\circ$, and angle $C = 39^\circ$. Perimeter questions usually mean you must find missing sides first, so start with the angle sum to find $A = 29^\circ$.

The known pair is $AC = 10.4$ m opposite angle $B = 112^\circ$. Use this to find the other two side lengths, $AB$ and $BC$: $$AB = \frac{10.4\sin 39^\circ}{\sin 112^\circ} \approx 7.06$$ $$BC = \frac{10.4\sin 29^\circ}{\sin 112^\circ} \approx 5.44$$

Now add all three sides to find the total distance: $$P = 10.4 + 7.06 + 5.44 \approx 22.9$$ The perimeter is $22.9$ m. Note that rounding intermediate values too early can change the final answer.

## Using the sine rule before area

For any non-right-angled triangle, area can be found with
$$\text{Area} = \frac{1}{2}ab\sin C$$
Here, $C$ is the included angle between sides $a$ and $b$.

In triangle $LMN$, $LM = 12$ m, angle $L = 74^\circ$, and angle $N = 38^\circ$. First find $M = 68^\circ$, then use the known pair $LM = 12$ m opposite angle $N = 38^\circ$ to get
$$LN = \frac{12\sin 68^\circ}{\sin 38^\circ} \approx 18.07$$
So $LN \approx 18.07$ m.

Now use sides $LM$ and $LN$ with the included angle $L = 74^\circ$:
$$\text{Area} = \frac{1}{2} \times 12 \times 18.07 \times \sin 74^\circ \approx 104.2$$
So the area is $104.2 \, \text{m}^2$, and the sine rule was the bridge to the missing side.

## The obtuse angle twist

![Triangle showing two possible positions for point B when AC is 18 cm, AB is 12 cm and angle C is 32 degrees, giving acute and obtuse values of angle B](../assets/002-1c9ca99a-80f8-42de-99f9-934802e61d6f.jpeg)
Sometimes $\sin^{-1}$ gives the acute angle first, but a triangle question may need the obtuse one. This happens because $\sin \theta = \sin(180^\circ - \theta)$ for angles between $0^\circ$ and $180^\circ$.

Suppose $AC = 18$ cm, $AB = 12$ cm, and angle $C = 32^\circ$, with angle $B$ stated to be obtuse. The sine rule gives
$$\frac{\sin B}{18} = \frac{\sin 32^\circ}{12}$$
which simplifies to
$$\sin B = \frac{18\sin 32^\circ}{12} \approx 0.795$$

The calculator gives $B \approx 52.6^\circ$, but that is the acute possibility. Because the question says $B$ is obtuse, use
$$B = 180^\circ - 52.6^\circ = 127.4^\circ$$
so $B \approx 127^\circ$ to 3 significant figures.

## Check yourself

1. In triangle $PQR$, $PQ = 9$ cm, angle $P = 47^\circ$ and angle $R = 68^\circ$. Which is the complete opposite pair?

   - $$PQ = 9$ cm with angle $R = 68^\circ$ ✔

   - $$PQ = 9$ cm with angle $P = 47^\circ$

   - $$PQ = 9$ cm with angle $Q = 65^\circ$

   - $$PR = 9$ cm with angle $R = 68^\circ$

   _Explanation:_ $$PQ$ lies directly across from angle $R$, so $9$ cm pairs with $68^\circ$. The most common wrong answer is $PQ = 9$ cm with angle $P = 47^\circ$ because students match the side to the angle at the same vertex, but opposite means across the triangle.

2. Which equation correctly sets up the calculation for angle $H$ in the triangle from the worked example?

   - $$\frac{\sin H}{7.0} = \frac{\sin 72^{\circ}}{9.5}$ ✔

   - $$\frac{\sin H}{9.5} = \frac{\sin 72^{\circ}}{7.0}$

   - $$\frac{7.0}{\sin 72^{\circ}} = \frac{9.5}{\sin H}$

   - $$\sin H = \frac{9.5\sin 72^{\circ}}{7.0}$

   _Explanation:_ The correct setup matches each angle with its opposite side, so angle $H$ must pair with $7.0$ and angle $72^{\circ}$ must pair with $9.5$. The most common wrong answer is B because it swaps the side-angle pairs, which breaks the opposite matching. Hint: Check which side lies across from each angle.

3. Stretch: Triangle $ABC$ has $AC = 18$ cm, $AB = 12$ cm, angle $C = 32^\circ$, and angle $B$ is obtuse. What is angle $B$ to 3 significant figures?

   - $$52.6^\circ$

   - $$127^\circ$ ✔

   - $$95.4^\circ$

   - $$148^\circ$

   _Explanation:_ The sine rule gives $\sin B \approx 0.795$, so inverse sine first gives $52.6^\circ$. The most common wrong answer is $52.6^\circ$ because students stop at the calculator display, but the question says angle $B$ is obtuse, so the correct angle is $180^\circ - 52.6^\circ = 127.4^\circ$, which rounds to $127^\circ$.
