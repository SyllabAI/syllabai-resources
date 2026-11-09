# a-level-mechanics-2-forces-and-friction — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 3 check questions (source: MathsGenie lessons)_

## Forces, particles, and equilibrium

A force is a push or pull measured in newtons, N. In the particle model, we ignore the size and shape of the object so every force can be drawn from one point.

Common forces are weight $mg$ vertically downward, where $g = 9.8 \, \text{m s}^{-2}$, tension along a taut string, normal reaction perpendicular to a surface, and friction parallel to a surface. Friction always opposes motion or the tendency to move.

A particle is in equilibrium when its acceleration is zero, so the resultant force is zero. In two perpendicular directions, we write:

$$$ \sum F_x = 0, \qquad \sum F_y = 0 $$

## Resolving forces at an angle

![Free-body diagram of a particle attached to a wall by a string at 30 degrees to the vertical with tension, a horizontal 18 N force, and weight labelled](../assets/001-b58c07ca-b193-42a4-bb3b-519729906001.jpeg)

The safest way to resolve a force is to sketch the right-angled triangle made by its components.

If the angle is given relative to the vertical, the vertical component uses the cosine function and the horizontal component uses the sine function.

In this example, the 18 N force is horizontal, so balance horizontally first:

$$T\sin 30^\circ = 18$$

Hence $T = \frac{18}{\sin 30^\circ} = 36$. So the tension is 36 N.

Now balance vertically:

$$W = T\cos 30^\circ = 36\cos 30^\circ \approx 31.2$$

So the weight is about 31.2 N. The key idea is to match sine or cosine to the side next to the given angle.

## Friction and limiting equilibrium

Friction acts parallel to a surface and opposes actual motion or possible motion. Its size is not automatically fixed; it adjusts to whatever value is needed up to a maximum.

The maximum available friction is controlled by the normal reaction: $$F_{\text{friction}} \le \mu R$$ Here $\mu$ is the coefficient of friction and $R$ is the normal reaction.

Only at the point of slipping, or while sliding, do we use $$F_{\text{friction}} = \mu R$$ A pull angled upward reduces $R$, while a push angled downward increases $R$.

## Worked example: pulling a rough block

A 20 kg block rests on a rough horizontal floor with $\mu = 0.3$, and a force $P$ pulls at $25^\circ$ above the horizontal. Because the block is on the point of sliding, the friction is limiting and the weight is $20g = 196$ N.

Resolve vertically first:
$$
R + P\sin 25^\circ = 196
$$
so
$$
R = 196 - P\sin 25^\circ
$$
The upward pull reduces the normal reaction, so it also reduces friction.

Now resolve horizontally:
$$
P\cos 25^\circ = 0.3R = 0.3(196 - P\sin 25^\circ)
$$
Hence
$$
P(\cos 25^\circ + 0.3\sin 25^\circ) = 58.8
$$
and $P \approx 56.9$ N. That is the pull needed to make the block start to slide.

## Inclined planes: resolve along and into the slope

![Free-body diagram of a block on a rough plane inclined at 28 degrees, showing weight 12 N, normal reaction, friction up the plane, and weight components 12 sin 28 degrees down the plane and 12 cos 28 degrees into the plane](../assets/002-0e60182e-6811-4ef5-b31c-31ab63a0cfaf.jpeg)

On an inclined plane, horizontal and vertical axes usually make the algebra messier. Resolve parallel and perpendicular to the plane, so the weight splits into $mg\sin\theta$ down the plane and $mg\cos\theta$ into the plane.

For a block of weight 12 N on a plane at $28^\circ$ that is about to slide down, the perpendicular balance gives
$$
R = 12\cos 28^\circ
$$
Because it is about to move down the plane, friction acts up the plane and is limiting.

Along the plane,
$$
\mu R = 12\sin 28^\circ
$$
So
$$
\mu(12\cos 28^\circ) = 12\sin 28^\circ \Rightarrow \mu = \tan 28^\circ \approx 0.532
$$
The 12 cancels because both components came from the same weight.

## Moving on a rough slope

If the block is moving, use Newton's second law along the plane instead of setting the forces to zero. Friction still acts against the motion, so a block sliding down the plane has friction up the plane.

Suppose a 3 kg block slides down a plane where $\tan\theta = 0.75$ and $\mu = 0.2$. Since $0.75 = \frac{3}{4}$, a 3-4-5 triangle gives $\sin\theta = \frac{3}{5}$ and $\cos\theta = \frac{4}{5}$.

Perpendicular to the plane, $R = mg\cos\theta$, so the friction is $0.2mg\cos\theta$. Down the plane, we apply $F=ma$: $$mg\sin\theta - 0.2mg\cos\theta = ma$$

Solving for acceleration gives: $$a = g(\sin\theta - 0.2\cos\theta) = 9.8\left(\frac{3}{5} - 0.2 \times \frac{4}{5}\right) = 4.312$$ The acceleration is about $4.31 \, \text{m s}^{-2}$ down the plane, and the mass cancels out.

## Will it move or stay at rest?

Sometimes no acceleration is given, and you must decide whether a block starts to move. Compare the driving force with the maximum possible friction.

For a block on a slope with no other force, the driving component is $mg\sin\theta$ and the largest friction available is $\mu mg\cos\theta$. If $mg\sin\theta > \mu mg\cos\theta$, it slides down; otherwise it can stay at rest.

Example: a 10 N brick sits on a $30^\circ$ plane with $\mu = 0.7$. Here $10\sin 30^\circ = 5$ N, while the maximum friction is $0.7 \times 10\cos 30^\circ \approx 6.06$ N, so friction is large enough to prevent motion.

## Check yourself

1. Which statement must be true for a particle in equilibrium?

   - The resultant force is zero ✔

   - All the forces are equal in size

   - No forces act on the particle

   - The weight always equals the normal reaction

   _Explanation:_ A is correct because equilibrium means zero acceleration, so the resultant force must be zero. B is the most common wrong answer, but forces can have different sizes as long as their components balance.

2. A block is resting on a rough floor and is not about to move. Which statement is always true?

   - The friction force equals $\mu R$

   - The friction force can be less than $\mu R$ ✔

   - The normal reaction equals $\mu R$

   - The friction force acts vertically upward

   _Explanation:_ B is correct because friction adjusts up to its maximum value and only equals $\mu R$ at the limit of motion or while sliding. A is the most common wrong answer because students often use $F = \mu R$ too early.

3. A plane is inclined at angle $\theta$ to the horizontal. Which expression gives the component of weight down the plane?

   - $$mg\sin\theta$ ✔

   - $$mg\cos\theta$

   - $$\mu mg\cos\theta$

   - $$R\sin\theta$

   _Explanation:_ A is correct because the component parallel to the slope is $mg\sin\theta$. B is the most common wrong answer because $mg\cos\theta$ is the component perpendicular to the plane.
