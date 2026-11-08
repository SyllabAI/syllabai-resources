# a-level-pure-mathematics-5-radians — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What is a radian?

![Circle sector with centre O, radii labelled r, arc labelled s, central angle theta, and note that s = r gives 1 radian](../assets/001-5a7db7f3-8278-4de3-bdd1-e44478e5ed81.jpeg)

Radians measure angle by comparing two lengths in the same circle. A central angle of 1 radian is formed when the arc length equals the radius.

If the arc length is $s$ and the radius is $r$, then the angle in radians is
$$
\theta = \frac{s}{r}
$$
This makes radians a natural unit for circle problems, because the geometry is built straight into the angle measure.

A full turn has circumference $2\pi r$, so dividing by the radius gives a full-turn angle of $2\pi$. That means
$$
360^\circ = 2\pi \, \text{rad}, \qquad 180^\circ = \pi \, \text{rad}
$$

## Converting between degrees and radians

To convert degrees to radians, multiply by $\frac{\pi}{180}$. To convert radians to degrees, multiply by $\frac{180}{\pi}$.

For example, $40^\circ$ becomes
$$
40 \times \frac{\pi}{180} = \frac{2\pi}{9}
$$
So $40^\circ = \frac{2\pi}{9} \, \text{rad}$.

This conversion matters because formulas such as $s = r\theta$ and $A = \frac{1}{2} r^2\theta$ assume $\theta$ is in radians. If a question gives degrees, convert before substituting.

## Arc length, sector area, and perimeter

When $\theta$ is in radians, the main sector formulas are short and direct. Use
$$
s = r\theta, \qquad A = \frac12 r^2\theta, \qquad P = 2r + s
$$
where $s$ is arc length, $A$ is sector area, and $P$ is sector perimeter.

Take $r = 9 \, \text{cm}$ and $\theta = 1.2$ rad as an example. The arc length is calculated by multiplying the radius and the angle:
$$
s = r\theta = 9 \times 1.2 = 10.8 \, \text{cm}
$$

The area uses the square of the radius, and the perimeter adds two radii to the arc length. So:
$$
A = \frac12 \times 9^2 \times 1.2 = 48.6 \, \text{cm}^2, \qquad P = 2\times 9 + 10.8 = 28.8 \, \text{cm}
$$

## Chords and minor segments

![Circle with centre O, radii OA and OB labelled 6 cm, chord AB labelled 8 cm, midpoint M on the chord, central angle theta, and the minor segment shaded](../assets/002-311b1f0d-0566-421b-8910-bc69ffbe3551.jpeg)

A chord is a straight line joining two points on the circumference, and a minor segment is the smaller region between that chord and its arc. To find a segment area, think sector minus triangle.

In the diagram, $r = 6 \, \text{cm}$ and the chord is $8 \, \text{cm}$. Halving the chord gives a right triangle with opposite side $4$ and hypotenuse $6$, so
$$
\sin\left(\frac{\theta}{2}\right) = \frac{4}{6} = \frac{2}{3}
$$
and therefore
$$
\theta = 2\arcsin\left(\frac{2}{3}\right) \approx 1.459
$$

The triangle part uses $A_{\text{triangle}} = \frac{1}{2} r^2\sin\theta$, so the minor segment area is
$$
A_{\text{segment}} = \frac{1}{2} r^2(\theta - \sin\theta)
$$
Using $r = 6$ and the unrounded value of $\theta$ gives
$$
A_{\text{segment}} \approx 8.38 \, \text{cm}^2
$$

## Small angle approximations

For very small angles, trig functions can be replaced by simpler expressions, but only if the angle is measured in radians. The standard approximations are
$$
\sin x \approx x, \qquad \tan x \approx x, \qquad \cos x \approx 1 - \frac{x^2}{2}
$$

For example, to approximate $\tan(3x)\cos(2x)$, replace each trig function first. This gives
$$
\tan(3x)\cos(2x) \approx 3x\left(1 - \frac{(2x)^2}{2}\right) = 3x(1 - 2x^2)
$$

Now expand carefully, because the algebra is where most slips happen. The product becomes
$$
3x(1 - 2x^2) = 3x - 6x^3
$$
so when $x = 0.1$, the estimate is $0.294$.

## Stretch: solving an approximate equation

A good stretch skill is turning a trig equation into something simpler by approximating first. If $\theta$ is small, the equation $2\cos\theta + (\sin\theta + 1)^2 = 20\tan\theta$ becomes much easier.

Approximate the left-hand side and simplify carefully. The middle terms cancel: $$ \begin{aligned} 2\cos\theta + (\sin\theta + 1)^2 &\approx 2\left(1 - \frac{\theta^2}{2}\right) + (\theta + 1)^2 \\ &= 2 - \theta^2 + \theta^2 + 2\theta + 1 \\ &= 3 + 2\theta \end{aligned} $$

On the right, $20\tan\theta \approx 20\theta$, so solve a linear equation instead. You get $$ 3 + 2\theta = 20\theta \Rightarrow 18\theta = 3 \Rightarrow \theta = \frac16 \approx 0.167 $$

## Check yourself

1. Which statement defines 1 radian?

   - The central angle subtended by an arc equal in length to the radius ✔

   - The central angle subtended by an arc equal in length to the diameter

   - Any angle equal to $\frac{\pi}{180}$

   - The angle in a quarter turn

   _Explanation:_ A radian is defined by comparing arc length with radius, so 1 radian is the angle made when arc length equals radius. The common wrong answer is using the diameter, but that would make the arc twice as long as required. Think about the formula $\theta = \frac{s}{r}$.

2. A sector has radius $5 \, \text{cm}$ and angle $60^\circ$. What is its arc length?

   - $$300 \, \text{cm}$

   - $$\frac{5\pi}{3} \, \text{cm}$ ✔

   - $$60\pi \, \text{cm}$

   - $$25\pi \, \text{cm}^2$

   _Explanation:_ Convert $60^\circ$ to $\frac{\pi}{3}$ rad first, then use $s = r\theta = 5 \times \frac{\pi}{3} = \frac{5\pi}{3} \, \text{cm}$. The common wrong answer is A, which comes from using $\theta = 60$ directly in $s = r\theta$, but that formula only works when the angle is in radians.

3. For small $x$, which is the best approximation to $\cos(2x)$?

   - $$1 - \frac{x^2}{2}$

   - $$1 - 2x^2$ ✔

   - $$2x$

   - $$1 - 4x^2$

   _Explanation:_ Start from $\cos u \approx 1 - \frac{u^2}{2}$ and substitute $u = 2x$, giving $1 - \frac{(2x)^2}{2} = 1 - \frac{4x^2}{2} = 1 - 2x^2$. The common wrong answer is A, which forgets to substitute the doubled angle before simplifying.
