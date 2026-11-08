# a-level-mechanics-3-projectiles — lesson

_Lane: `a-level-maths-edexcel` · grade — · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## The projectile model

![Projectile launched from the origin with axes, angle theta, initial velocity U, components U cos theta and U sin theta, parabolic path, and downward gravity arrow](../assets/001-972e5b1c-c4b7-41bb-bdf6-7d28a6a1f95f.jpeg)

A projectile is an object that moves only under gravity after it has been launched. In the standard model, air resistance is ignored, the object is treated as a particle, and the acceleration is constant: $g = 9.8 \, \text{m s}^{-2}$ vertically downward.

If the launch speed is $U$ at angle $\theta$ above the horizontal, resolve it into components. The horizontal component is $u_x = U\cos\theta$ and the vertical component is $u_y = U\sin\theta$.

Horizontal and vertical motion happen together, but you calculate them separately with the same time $t$. If the launch velocity is written as $a\mathbf{i} + b\mathbf{j}$, then $u_x = a$ and $u_y = b$.

## Core equations and a first worked example

Take upwards as positive and start at the launch point. Then the component equations for position and velocity are:
$$x = u_x t,\qquad y = u_y t - \frac{1}{2}gt^2$$
$$v_x = u_x,\qquad v_y = u_y - gt$$

Notice that $g$ appears only in the vertical equations. This indicates that gravity affects only vertical motion, leaving the horizontal component constant throughout the flight.

Example: a particle is projected at $18 \, \text{m s}^{-1}$ at $50^\circ$. We begin the solution by resolving the launch speed into its components:
$$u_x = 18\cos 50^\circ = 11.57,\qquad u_y = 18\sin 50^\circ = 13.79$$

After $2 \, \text{s}$, the horizontal velocity is still $v_x = 11.57$. The vertical velocity is $v_y = 13.79 - 9.8(2) = -5.81$, so $\mathbf{v} = 11.6\mathbf{i} - 5.81\mathbf{j} \, \text{m s}^{-1}$ and the negative $\mathbf{j}$ component shows the particle is moving downward.

## Greatest height, time of flight, and range

![Projectile launched from level ground and landing back on level ground, with angle theta, launch speed U, highest point labelled with vertical velocity zero, maximum height H, horizontal range R, and downward gravity arrow](../assets/002-178825a1-c911-4115-9890-2bf2bbbceb6c.jpeg)
At the greatest height, the vertical velocity is zero but the horizontal velocity is not. On level ground, you find the time of flight by setting the vertical displacement to zero and taking the non-zero value of $t$.

Suppose $U = 22 \, \text{m s}^{-1}$ and $\theta = 50^\circ$. Then $u_x = 22\cos 50^\circ = 14.14$ and $u_y = 22\sin 50^\circ = 16.85$. To find the height at the top point:
$$0 = 16.85^2 - 2(9.8)H$$
Solving this gives a maximum height of $H = 14.5 \, \text{m}$.

For a level-ground landing, we find the time of flight by setting the vertical displacement to zero:
$$0 = 16.85t - 4.9t^2 = t(16.85 - 4.9t)$$
The non-zero root is $t = 3.44 \, \text{s}$, which represents the total time the projectile is in the air.

The horizontal range is then $R = 14.14 \times 3.44 = 48.6 \, \text{m}$. Note that the shortcut $R = \frac{U^2\sin 2\theta}{g}$ works only when launch and landing heights are equal.

## Launching from a raised point

If a projectile starts at height $h$ above the ground, write its height above ground as $$y = h + u_y t - \frac{1}{2}gt^2$$ When it hits the ground, set $y = 0$.

Example: a particle is projected from $12 \, \text{m}$ above the ground with velocity $5\mathbf{i} + 8\mathbf{j} \, \text{m s}^{-1}$. Read off $u_x = 5$ and $u_y = 8$, then the extra height above the launch point is $H = \frac{8^2}{2(9.8)} = 3.27 \, \text{m}$, so the greatest height above the ground is $12 + 3.27 = 15.3 \, \text{m}$.

For landing, solve $$0 = 12 + 8t - 4.9t^2$$ which gives $t = 2.58 \, \text{s}$ when you take the positive root. The horizontal distance is then $x = 5(2.58) = 12.9 \, \text{m}$.

## Trajectory equation and collisions

Eliminate time using $t = \frac{x}{U\cos\theta}$. Then
$$y = x\tan\theta - \frac{gx^2}{2U^2\cos^2\theta}$$
which gives the trajectory relative to the launch point.

Example: at $45^\circ$, landing $60 \, \text{m}$ horizontally away and $10 \, \text{m}$ below the launch point gives
$$-10 = 60 - \frac{9.8(60^2)}{U^2}$$
so $U^2 = 504$ and $U = 22.4 \, \text{m s}^{-1}$.

For collisions, two projectiles must have the same horizontal position and the same vertical position at the same time. Choose a sensible origin and sign convention first, because a wrong sign in the horizontal direction is one of the most common errors.

## Check yourself

1. In the standard projectile model, which statement is correct after launch?

   - The horizontal acceleration is $0$. ✔

   - The vertical acceleration is $0$.

   - The acceleration always points along the direction of motion.

   - Both the horizontal and vertical accelerations have magnitude $g$.

   _Explanation:_ Gravity acts vertically downward, so there is no horizontal acceleration in the model. The common wrong answer is B, but the vertical motion definitely does accelerate because gravity is still acting.

2. At the greatest height of a projectile, which statement is true?

   - Both velocity components are zero.

   - The vertical velocity is zero but the horizontal velocity is unchanged. ✔

   - The horizontal velocity is zero but the vertical velocity is unchanged.

   - The acceleration is zero.

   _Explanation:_ At the top, only the vertical component becomes zero for an instant. The common wrong answer is A, but the projectile is still moving horizontally and gravity is still acting, so it has not come to rest. Hint: Think component by component, not about the overall motion as one number.

3. Ball P is at $(34.64, 0.4)$ after $2 \, \text{s}$. Ball Q starts at $(40, 0)$ and collides with P at that instant. Taking positive $x$ to the right, what must be the horizontal velocity component of Q?

   - $$2.68 \, \text{m s}^{-1}$

   - $$-2.68 \, \text{m s}^{-1}$ ✔

   - $$17.32 \, \text{m s}^{-1}$

   - $$-17.32 \, \text{m s}^{-1}$

   _Explanation:_ Q moves from $x = 40$ to $x = 34.64$ in $2 \, \text{s}$, so its horizontal displacement is $-5.36 \, \text{m}$ and its horizontal velocity component is $-5.36 \div 2 = -2.68 \, \text{m s}^{-1}$. The common wrong answer is A, which uses the correct magnitude but ignores the chosen positive direction. Hint: Use signed displacement divided by time.
