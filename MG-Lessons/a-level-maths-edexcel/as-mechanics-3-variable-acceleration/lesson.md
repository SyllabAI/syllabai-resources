# as-mechanics-3-variable-acceleration — lesson

_Lane: `a-level-maths-edexcel` · grade — · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## The calculus chain

![Diagram linking displacement s(t), velocity v(t), and acceleration a(t) with differentiation arrows forwards and integration arrows backwards](../assets/001-ea70dfc1-8363-4aef-a192-1130dc690602.jpeg)

In constant acceleration questions you could use SUVAT, but with variable acceleration the acceleration changes with time, so SUVAT usually does not apply. Instead, calculus links displacement, velocity and acceleration.

Displacement $s$ is measured in $\text{m}$, velocity $v$ in $\text{m s}^{-1}$, and acceleration $a$ in $\text{m s}^{-2}$. The key chain is

$$v = \frac{ds}{dt}, \qquad a = \frac{dv}{dt}$$

Moving from $s$ to $v$ to $a$ means differentiate. Moving backwards means integrate, and every integration brings a constant that must be found from given conditions.

## Worked example: from acceleration to velocity

Suppose $a = 6t - 12$ and initially $v = 9 \, \text{m s}^{-1}$. Since $a = \frac{dv}{dt}$, we integrate to find the velocity expression:
$$v = \int (6t - 12)\,dt = 3t^2 - 12t + C$$

Initially means $t = 0$. To find the constant $C$, substitute $v = 9$ and $t = 0$ into the expression:
$$9 = 3(0)^2 - 12(0) + C$$

So $C = 9$, giving the particular velocity function:
$$v = 3t^2 - 12t + 9$$

Forgetting the constant of integration $+C$ is the most common error in variable acceleration problems, and it stops you from finding the correct specific velocity function.

## From velocity to displacement

If velocity is known, use $v = \frac{ds}{dt}$ and integrate to recover displacement. The condition might be at $t = 0$ or at any later time, so read the wording carefully.

Example: if $v = 5t - 3$ and $s = 52$ when $t = 4$, then $$s = \int (5t - 3)\,dt = \frac{5}{2}t^2 - 3t + C$$

Use the condition at $t = 4$. Substitute into the expression: $$52 = \frac{5}{2}(4)^2 - 3(4) + C = 28 + C$$ So $C = 24$, hence $s = \frac{5}{2}t^2 - 3t + 24$, and $s(8) = 160 \, \text{m}$.

## Distance versus displacement

For $v = 12 - 2t^2$, useful points for a velocity-time sketch are $(0,12)$, $(2,4)$, $(\sqrt{6},0)$, and $(4,-20)$. So the graph starts above the axis, crosses once, and then lies well below the axis by $t = 4$. Displacement over a time interval is the signed area under this graph, while total distance is the total area with any part below the axis counted positively.

On $0 \le t \le 4$, solve $12 - 2t^2 = 0$ to find when the particle is instantaneously at rest. This gives $t = \sqrt{6}$, and because $v$ changes from positive to negative there, the particle turns around at that time.

Take the start point as the origin, so $s(0) = 0$. Integrating gives
$$
s(t) = 12t - \frac{2}{3}t^3 + C
$$
Using $s(0) = 0$ gives $C = 0$, so
$$
s(t) = 12t - \frac{2}{3}t^3
$$
Then $s(\sqrt{6}) = 8\sqrt{6}$ and $s(4) = \frac{16}{3}$.

So the particle first travels $8\sqrt{6}$ units out to the turning point, then travels back
$$
8\sqrt{6} - \frac{16}{3}
$$
units. Therefore the total distance is
$$
8\sqrt{6} + \left(8\sqrt{6} - \frac{16}{3}\right) = 16\sqrt{6} - \frac{16}{3} \approx 33.9
$$
The final displacement is $s(4) - s(0) = \frac{16}{3}$ because the motion after $t = \sqrt{6}$ is in the negative direction.

## Differentiate displacement directly

Sometimes the question starts with displacement, not acceleration. Then you move forwards along the chain by differentiating once for velocity and twice for acceleration.

If $x = t^3 - 12t^2 + 45t$, then $$v = \frac{dx}{dt} = 3t^2 - 24t + 45$$ So the initial velocity is $v(0) = 45 \, \text{m s}^{-1}$.

Differentiate again: $$a = \frac{dv}{dt} = 6t - 24$$ Setting $a = 0$ gives $t = 4 \, \text{s}$. Do not mix up 'when velocity is zero' with 'when acceleration is zero' because they answer different questions.

## Check yourself

1. A particle has acceleration $a = 4t - 8$ and you are told its velocity when $t = 0$. What is the correct method to find $v$?

   - Differentiate $4t - 8$

   - Integrate $4t - 8$ and use the given velocity to find the constant ✔

   - Use SUVAT because acceleration is linear

   - Set $s = \int (4t - 8)\,dt$

   _Explanation:_ Velocity comes from $v = \int a \, dt + C$, then the condition at $t = 0$ fixes $C$. The most common wrong choice is A, but differentiating acceleration gives its rate of change, not the velocity.

2. A particle has $v = 5t - 3$ and $s = 52$ when $t = 4$. Which displacement function is correct?

   - $$s = \frac{5}{2}t^2 - 3t + 24$ ✔

   - $$s = \frac{5}{2}t^2 - 3t - 24$

   - $$s = 5t^2 - 3t + 24$

   - $$s = \frac{5}{2}t^2 - 3 + 24$

   _Explanation:_ Integrating gives $\frac{5}{2}t^2 - 3t + C$, and substituting $t = 4$, $s = 52$ gives $C = 24$. The most common wrong choice is C, which forgets that the integral of $5t$ is $\frac{5}{2}t^2$, not $5t^2$.

3. A particle starts from rest. For $0 \le t \le 3$, $a = 3t - t^2$, and for $t > 3$, $a = \frac{18}{t^2}$. Which expression correctly finds $v(6)$?

   - $$v(6) = \int_0^6 \frac{18}{t^2}\,dt$

   - $$v(6) = \int_0^3 (3t - t^2)\,dt + \int_3^6 \frac{18}{t^2}\,dt$ ✔

   - $$v(6) = \int_0^6 (3t - t^2)\,dt$

   - $$v(6) = \int_3^6 (3t - t^2)\,dt + \int_0^3 \frac{18}{t^2}\,dt$

   _Explanation:_ B is correct because you must work interval by interval: the first integral gives the velocity gained up to $t = 3$, and the second adds the extra change from $t = 3$ to $t = 6$. The most common wrong choice is A, which uses the $t > 3$ rule outside its interval and ignores the velocity already gained by $t = 3$. Hint: The value at the join, $t = 3$, becomes the starting value for the next interval.
