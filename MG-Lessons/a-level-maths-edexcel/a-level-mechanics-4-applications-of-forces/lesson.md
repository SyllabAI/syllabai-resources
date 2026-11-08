# a-level-mechanics-4-applications-of-forces — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Force diagrams first

![Free-body diagram of a 5 kg block on a rough plane at angle theta with weight, normal reaction, friction, and resolved components labelled](../assets/001-934cc8fb-1593-4218-b653-2e08a2e795cc.jpeg)
A free-body diagram shows one body only, with every external force acting on it. In applications of forces, getting this sketch right usually decides the rest of the solution.

Weight has magnitude $mg$ and always acts vertically downward. The normal reaction is perpendicular to the surface, while friction acts along the surface opposing motion or the tendency to move.

On a plane inclined at angle $\theta$ to the horizontal, the weight components are $mg\sin\theta$ down the plane and $mg\cos\theta$ into the plane. Check with $\theta=0^\circ$: the down-slope component should be zero, so the sine term must go along the plane.

## Worked example on a rough plane

Consider a 5 kg particle resting on a rough plane where $\tan\theta=\frac{3}{4}$. Since it would tend to slide down the plane, friction acts up the plane.

Use the 3-4-5 triangle: $\sin\theta=\frac{3}{5}$ and $\cos\theta=\frac{4}{5}$. Perpendicular to the plane, equilibrium gives $R=5g\cos\theta = 5 \times 9.8 \times \frac{4}{5} = 39.2$.

So the normal reaction is 39.2 N, and the unit is newtons because $\text{kg} \times \text{m s}^{-2} = \text{N}$. Parallel to the plane, equilibrium gives $F=5g\sin\theta = 5 \times 9.8 \times \frac{3}{5} = 29.4$.

Therefore the frictional force is 29.4 N up the plane. If your algebra ever gives a negative friction, your assumed direction was the wrong way round.

## Equilibrium and moments

For rods, ladders and planks, equilibrium means no resultant force and no resultant turning effect. In symbols, we use $\sum F_x = 0$, $\sum F_y = 0$, and $\sum M = 0$.

The moment of a force about a point is force multiplied by perpendicular distance from the point to the line of action. Its unit is N m, and in equilibrium clockwise moments balance anticlockwise moments.

Choose the moment point wisely, usually at a hinge or a contact point with several unknown forces. Those forces then have zero perpendicular distance, so they disappear from the moment equation.

## Worked example: ladder on the point of slipping

![Free-body diagram of a 6 m ladder against a smooth wall and rough ground, with weight at midpoint, ground reaction, friction, wall reaction, and moment arms labelled](../assets/002-817bb86b-5d58-4883-87d3-20ddf64e18b5.jpeg)

A uniform 6 m ladder of mass 16 kg rests against a smooth wall, with rough ground and coefficient of friction $0.25$. On the point of slipping, the wall exerts only a horizontal reaction $H$, while the ground exerts a vertical reaction $R$ and friction $F$.

Resolve vertically first: $R = 16g$. Because the ladder is in limiting equilibrium, $F = \mu R = 0.25 \times 16g = 4g = 39.2$ N.

Resolve horizontally next: the only horizontal forces are $H$ and $F$, so $H = F = 39.2$ N. This is a common place to forget that a smooth wall cannot provide friction.

Take moments about the foot of the ladder so that $R$ and $F$ have zero moment. The wall reaction has perpendicular distance $6\sin\theta$ and the weight has perpendicular distance $3\cos\theta$, so $H(6\sin\theta)=16g(3\cos\theta)$, giving $\tan\theta=2$ and $\theta \approx 63.4^{\circ}$.

## Connected particles and pulleys

When particles are connected by a light inextensible string over a smooth pulley, the tension is the same on both sides and the accelerations have the same magnitude while the string is taut. Draw a separate force diagram for each particle before writing any equations.

Suppose a $2$ kg particle is on a rough $30^\circ$ plane and is connected to a hanging $3$ kg particle, with $\mu=0.25$ and the $3$ kg mass moving down. For the $2$ kg particle, take up the plane as positive, so friction acts down the plane and $R = 2g\cos30^\circ$.

Newton's second law gives $T-2g\sin30^\circ-0.25(2g\cos30^\circ)=2a$ for the particle on the plane and $3g-T=3a$ for the hanging particle. Add the equations to eliminate $T$, giving $a \approx 3.07 \, \text{m s}^{-2}$, then substitute back to get $T \approx 20.2$ N.

From rest over $1.6$ m, use $v^2=u^2+2as$ to get $v^2=2(3.07)(1.6)$, so $v \approx 3.14 \, \text{m s}^{-1}$. The force on the pulley is the resultant of two equal tensions with angle $60^\circ$ between them, because one string section is vertical and the other is parallel to a $30^\circ$ plane, so $P=T\sqrt{3}\approx35.0$ N.

## When the string goes slack

If a hanging mass hits the ground or the string becomes slack, the tension becomes zero immediately. You must stop using the old connected-particle equations and analyse the remaining body again.

Take a 2 kg particle on a rough plane with $\tan\theta=\frac{3}{4}$ and $\mu=\frac{5}{8}$ that has just come to rest after moving up the plane. With the string slack, the downhill component needed to hold it is $F_{\text{needed}}=2g\sin\theta=\frac{6g}{5}$ and the normal reaction is $R=2g\cos\theta=\frac{8g}{5}$.

The maximum possible friction is $F_{\max}=\mu R=\frac{5}{8}\times\frac{8g}{5}=g$. Since $g<\frac{6g}{5}$, friction is too small, so the particle does not remain at rest and slides down the plane.

## Check yourself

1. A particle rests on a rough plane at angle $\theta$. Which statement is correct?

   - The component of weight down the plane is $mg\sin\theta$ and the component into the plane is $mg\cos\theta$ ✔

   - The component of weight down the plane is $mg\cos\theta$ and the component into the plane is $mg\sin\theta$

   - Both components are $mg\cos\theta$

   - Both components are $mg\sin\theta$

   _Explanation:_ A is correct because the angle check at $\theta=0^{\circ}$ gives zero force down the plane and full weight into the plane. The most common wrong answer is B, which swaps sine and cosine and would wrongly predict a down-slope force of $mg$ on a horizontal surface. Hint: Test the expressions when $\theta=0^{\circ}$.

2. In the ladder example, why is taking moments about the foot especially useful?

   - It makes the weight have zero moment

   - It removes the ground reaction and friction from the moment equation ✔

   - It makes the wall smooth

   - It means horizontal equilibrium is no longer needed

   _Explanation:_ B is correct because both ground forces act through the foot, so their perpendicular distances are zero and they vanish from the moment equation. The most common wrong answer is A, but the weight acts at the midpoint of the ladder, not at the foot, so it still produces a moment.

3. A 2 kg particle on a rough plane has $\tan\theta=\frac{3}{4}$ and $\mu=\frac{5}{8}$. It has just come to rest after moving up the plane, and the string is now slack. What happens next?

   - It remains at rest because friction can always balance the component of weight

   - It slides down the plane because the maximum friction is less than the downhill component ✔

   - It continues up the plane because friction acts up the plane

   - It stays in equilibrium because the previous tension still acts

   _Explanation:_ B is correct because with the string slack, $T=0$, the required friction is $\frac{6g}{5}$, but the largest available friction is only $g$. The most common wrong answer is A, which forgets that friction is not any value you want; it is capped by $\mu R$. Hint: Compare $F_{\text{needed}}$ with $F_{\max}$.
