# as-pure-mathematics-9-trigonometric-ratios — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 3 check questions (source: MathsGenie lessons)_

## Naming sides and basic ratios

Right-angled triangle relative to angle $\theta$:

```
          θ
          o
         /|
        / |
       /  | adjacent
      /   |
     /    |
    o-----o
     opposite
```

Trigonometric ratios link an angle to side lengths. In a right-angled triangle, the side names depend on the chosen angle $\theta$.

With $\theta$ at the top vertex and the right angle at the bottom-right corner:
- the vertical side next to $\theta$ is the **adjacent** side
- the sloping longest side is the **hypotenuse**
- the bottom horizontal side across from $\theta$ is the **opposite** side

Each ratio compares a different pair of sides. The memory aid is SOH CAH TOA.

$$$
\begin{aligned}
\sin \theta &= \frac{\text{opposite}}{\text{hypotenuse}} \\
\cos \theta &= \frac{\text{adjacent}}{\text{hypotenuse}} \\
\tan \theta &= \frac{\text{opposite}}{\text{adjacent}}
\end{aligned}
$$

Keep your calculator in degree mode for this lesson. For non-right-angled triangles, angle $A$ is opposite side $a$, angle $B$ is opposite side $b$, and angle $C$ is opposite side $c$. Marking opposite pairs first helps you choose the correct formula later.

## Worked example: finding a side in a right-angled triangle

Suppose a right-angled triangle has hypotenuse $13 \, \text{cm}$ and angle $28^{\circ}$, and we want the side opposite the angle. Because we know opposite and hypotenuse, sine is the correct ratio.

To begin, write the equation using the sine ratio: $$\sin 28^{\circ} = \frac{x}{13}$$ Then, multiply both sides by 13 to rearrange the equation and isolate the unknown side: $$x = 13 \sin 28^{\circ}$$

Now evaluate the expression using degree mode on your calculator. $$x \approx 6.10 \, \text{cm}$$ Following this calculation, we find the opposite side is approximately $6.1 \, \text{cm}$.

## Choosing between the main triangle formulas

For non-right-angled triangles, label opposite pairs before you do any calculation. Then choose the formula: the sine rule needs an opposite pair, the cosine rule uses two sides with the included angle or all three sides, and the area formula uses two sides with the included angle.

Example: sides $14 \, \text{cm}$ and $9 \, \text{cm}$ include an angle of $35^\circ$, so the sine area formula applies. Substitute carefully: $$\text{Area} = \frac{1}{2} \times 14 \times 9 \times \sin 35^\circ = 63 \sin 35^\circ$$

$$$\text{Area} \approx 36.1 \, \text{cm}^2$$ A common mistake is using an angle that is not between the two sides.

## Worked example: cosine rule for a missing side

In triangle $PQR$, let $PQ = 10 \, \text{cm}$, $PR = 7 \, \text{cm}$ and angle $QPR = 65^\circ$. The unknown side $QR$ is opposite the known angle, so it goes on the left of the cosine rule.

Substitute the given values into the formula and calculate the right-hand side: $$QR^2 = 10^2 + 7^2 - 2 \times 10 \times 7 \times \cos 65^\circ$$ This calculation gives: $$QR^2 \approx 89.83$$

Now take the square root of both sides to find the side length. $$QR \approx 9.48 \, \text{cm}$$ So the third side is approximately $9.48 \, \text{cm}$.

## Sine rule and the two possible angles

Use the sine rule when you know an opposite angle-side pair. In triangle $ABC$, if $A = 35^\circ$, $BC = 8 \, \text{cm}$ and $AB = 12 \, \text{cm}$, then side $BC$ is opposite $A$ and side $AB$ is opposite $C$.

Write $$\frac{\sin C}{12} = \frac{\sin 35^\circ}{8}$$ so $$\sin C = \frac{12 \sin 35^\circ}{8} \approx 0.8604$$ The calculator gives one angle, $C \approx 59.4^\circ$.

Sine takes the same value at two angles between $0^\circ$ and $180^\circ$, so the second possibility is $180^\circ - 59.4^\circ = 120.6^\circ$. Therefore $B = 180^\circ - 35^\circ - C$ is either $85.6^\circ$ or $24.4^\circ$.

## Exact values from an identity

The identity $$\sin^2 \theta + \cos^2 \theta = 1$$ lets you find one ratio if you know the other. If $\theta$ is acute, both sine and cosine are positive.

For example, if $\sin \theta = \frac{2}{3}$, start by substituting into the identity. $$\left(\frac{2}{3}\right)^2 + \cos^2 \theta = 1$$ This simplifies to $$\cos^2 \theta = 1 - \frac{4}{9} = \frac{5}{9}$$

Take the positive square root because the angle is acute. So $$\cos \theta = \frac{\sqrt{5}}{3}$$

## Sketching sine and cosine graphs

![Graph of y equals sin x and y equals sin x plus 1 from 0 degrees to 360 degrees with key points marked](../assets/001-c18e807e-d9a3-4516-a24b-6d496f5533bb.jpeg)

From $0^\circ$ to $360^\circ$, $y = \sin x$ passes through $(0^\circ,0)$, $(90^\circ,1)$, $(180^\circ,0)$, $(270^\circ,-1)$ and $(360^\circ,0)$. The graph $y = \sin x + 1$ has the same shape, but every point is moved up by 1.

$$y = \cos x$ starts at (0°,1), then passes through (90°,0) and (180°,-1).

It then goes through (270°,0) and ends at (360°,1).

For a sketch, plot the five key $x$-values first and then join them with a smooth curve. A number outside the bracket changes vertical position, while a change inside the bracket shifts the graph horizontally.

## Check yourself

1. For an angle $\theta$ in a right-angled triangle, which ratio compares opposite and hypotenuse?

   - $$\sin \theta$ ✔

   - $$\cos \theta$

   - $$\tan \theta$

   - $$\frac{1}{\tan \theta}$

   _Explanation:_ $$\sin \theta$ is opposite over hypotenuse, so it matches the side pair in the question. The most common wrong answer is $\cos \theta$, but cosine uses adjacent over hypotenuse.

2. Triangle $ABC$ has $b = 7 \, \text{cm}$, $c = 10 \, \text{cm}$ and included angle $A = 65^\circ$. Which method should be used first to find side $a$?

   - Sine rule

   - Cosine rule ✔

   - Pythagoras

   - Area formula

   _Explanation:_ The cosine rule is correct because two sides and the included angle are given, and you want the third side. The most common wrong answer is the sine rule, but there is no complete opposite angle-side pair yet.

3. A calculation gives $\sin C = 0.8604$ in a triangle. Which extra angle must also be checked?

   - $$59.4^\circ$

   - $$120.6^\circ$ ✔

   - $$30.6^\circ$

   - $$149.4^\circ$

   _Explanation:_ If one solution is $59.4^\circ$, the second sine angle is $180^\circ - 59.4^\circ = 120.6^\circ$. Sine has the same value at $\theta$ and $180^\circ - \theta$. The most common wrong answer is $59.4^\circ$, which is only the primary calculator output rather than the secondary angle to check.
