# grade-7-7-10-the-sine-rule — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Opposite pairs and the sine rule

![Triangle ABC with angles A, B, C and opposite sides a, b, c colour matched](../assets/001-da2066ef-a40d-451e-8592-0c71008fa914.jpeg)
The sine rule is for non-right-angled triangles, so you do not need a $90^\circ$ angle. The key skill is spotting opposite pairs: an angle and the side directly across from it.

In triangle ABC, side $a$ is opposite angle $A$, side $b$ is opposite angle $B$, and side $c$ is opposite angle $C$. A complete opposite pair means you know both the side and its opposite angle.

$$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$$

Use it when you know one complete opposite pair and want another side or angle. Make sure the pair you use is directly opposite, not just touching.

## Worked example: finding a side

When finding a side, it is usually easiest to write the side lengths on top of the fractions. In this example, 12 cm is opposite $44^\circ$ and side $y$ is opposite $101^\circ$.

$$$\frac{y}{\sin 101^\circ} = \frac{12}{\sin 44^\circ}$$

$$$y = \frac{12 \sin 101^\circ}{\sin 44^\circ} = 16.96\ldots$$

So $y = 17.0 \, \text{cm}$ to 1 decimal place. Always ensure that your calculator is in degrees mode when performing these calculations.

## Worked example: finding an angle

When finding an angle, it is usually easier to put the sine terms on top. After you find the sine value, use $\sin^{-1}$ on your calculator.

If 8.1 cm is opposite $x$ and 12.6 cm is opposite $72^{\circ}$, start with the following ratio. This arrangement makes solving for the unknown angle easier: $$\frac{\sin x}{8.1} = \frac{\sin 72^{\circ}}{12.6}$$

Then multiply by 8.1 to find the value of $\sin x$. Keep the full decimal in your calculator for the final step to ensure accuracy: $$\sin x = \frac{8.1 \sin 72^{\circ}}{12.6} = 0.611\ldots$$

Now use inverse sine to calculate the final value: $$x = \sin^{-1}(0.611\ldots) = 37.7^{\circ}$$ So $x = 37.7^{\circ}$ to 3 significant figures, and you should only round at the end.

## Find an angle first, then use the sine rule

Sometimes the angle opposite the known side is not given, so the sine rule cannot start immediately. In that case, use the angle sum of a triangle first.

If $A = 36^\circ$, $B = 82^\circ$, and $AB = 7 \, \text{m}$, then side $AB$ is opposite angle $C$. We calculate the missing angle as: $$C = 180^\circ - 36^\circ - 82^\circ = 62^\circ$$

Now pair $AB = 7 \, \text{m}$ with $C = 62^\circ$, and pair $AC$ with $B = 82^\circ$. Using the sine rule: $$\frac{AC}{\sin 82^\circ} = \frac{7}{\sin 62^\circ}$$ Rearranging this gives $AC = 7.85 \, \text{m}$ to 3 significant figures.

## Applications: perimeter and area

Perimeter means the total distance around the triangle. In a sine rule perimeter question, find any missing sides first and add only at the end.

For example, if $AC = 14.2 \, \text{m}$, $B = 102^\circ$, and $C = 44^\circ$, then $A = 34^\circ$. Using the known pair $AC$ opposite $B$, you get $BC = \frac{14.2 \sin 34^\circ}{\sin 102^\circ} = 8.12\ldots \, \text{m}$ and $AB = \frac{14.2 \sin 44^\circ}{\sin 102^\circ} = 10.08\ldots \, \text{m}$.

The total perimeter is $14.2 + 8.12\ldots + 10.08\ldots = 32.4 \, \text{m}$ to 3 significant figures. For area, use the following formula with two sides and their included angle: $$\text{Area} = \frac{1}{2}ab\sin C$$

If $AB = 10 \, \text{m}$, $A = 76^\circ$, and $C = 44^\circ$, first find $B = 60^\circ$ and then use the sine rule to get $AC = \frac{10 \sin 60^\circ}{\sin 44^\circ} = 12.47\ldots \, \text{m}$. Then $\text{Area} = \frac{1}{2} \times 10 \times 12.47\ldots \times \sin 76^\circ = 60.5 \, \text{m}^2$ to 1 decimal place.

## Check for an obtuse angle

![Angle sketches showing 60 degrees and 120 degrees with equal sine values and matching heights](../assets/002-7f8a43b5-a435-4c06-82a2-40b8d60d7bb3.jpeg)

When you use inverse sine, the calculator gives the acute angle first. But $\sin \theta = \sin(180^\circ - \theta)$, so an obtuse angle can share the same sine value.

In a triangle, $AB = 11$ cm is opposite $C = 32^\circ$, and $AC = 18$ cm is opposite angle $B$. The sine rule gives:

$$\frac{\sin B}{18} = \frac{\sin 32^\circ}{11}$$

so $\sin B = \frac{18\sin 32^\circ}{11} \approx 0.867$.

Using inverse sine gives $60.1^\circ$, but if the question says that $B$ is obtuse, we must subtract this from $180^\circ$:

$$B = 180^\circ - 60.1^\circ = 119.9^\circ$$

Thus, $B = 119.9^\circ$ to 1 decimal place.

## Check yourself

1. In triangle ABC, which side-angle pair is matched correctly for the sine rule?

   - side $b$ and angle $B$ ✔

   - side $b$ and angle $A$

   - side $c$ and angle $A$

   - side $a$ and angle $C$

   _Explanation:_ In standard triangle notation, lower-case side $b$ is opposite upper-case angle $B$. The common wrong answer is B, because side $b$ may touch angle $A$, but the sine rule uses opposite pairs, not touching pairs.

2. In the angle example, which expression for $\sin x$ is correct?

   - $$\sin x = \frac{8.1 \sin 72^\circ}{12.6}$ ✔

   - $$\sin x = \frac{12.6 \sin 72^\circ}{8.1}$

   - $$\sin x = \frac{8.1}{12.6 \sin 72^\circ}$

   - $$\sin x = \frac{\sin 72^\circ}{8.1 \times 12.6}$

   _Explanation:_ Side 8.1 must stay paired with angle $x$ because they are opposite. The common wrong answer is B, which swaps the opposite pairs and even gives a value bigger than 1 for $\sin x$, which is impossible. Hint: Start from $\frac{\sin(\text{angle})}{\text{side}}$ when finding an angle.

3. In the area example, which expression gives the area after finding $AC = 12.47 \, \text{m}$?

   - $$\frac{1}{2} \times 10 \times 12.47 \times \sin 76^{\circ}$ ✔

   - $$\frac{1}{2} \times 10 \times 12.47 \times \sin 44^{\circ}$

   - $$\frac{1}{2} \times 10 \times 12.47 \times \sin 60^{\circ}$

   - $$\frac{1}{2} \times 10 \times 12.47 \div \sin 76^{\circ}$

   _Explanation:_ The area formula uses two sides and their included angle, and the included angle between $AB$ and $AC$ is $A = 76^{\circ}$. The common wrong answer is C because $60^{\circ}$ is an angle you found on the way, but it is not between sides $AB$ and $AC$. Hint: Ask yourself which angle lies between the two sides you are multiplying.

4. Triangle ABC has $AC = 18 \, \text{cm}$, $AB = 11 \, \text{cm}$, angle $C = 32^\circ$, and angle $B$ is obtuse. What is angle $B$ to 1 decimal place?

   - $$60.1^\circ$

   - $$119.9^\circ$ ✔

   - $$87.0^\circ$

   - $$147.9^\circ$

   _Explanation:_ Using the sine rule gives $\sin B = \frac{18 \sin 32^\circ}{11} = 0.867\ldots$. The common wrong answer is A because $\sin^{-1}(0.867\ldots)$ gives the acute angle first, but an obtuse angle must be the supplement, so $B = 180^\circ - 60.1^\circ = 119.9^\circ$.
