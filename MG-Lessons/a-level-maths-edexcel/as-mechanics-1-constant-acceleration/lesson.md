# as-mechanics-1-constant-acceleration — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 4 check questions (source: MathsGenie lessons)_

## Motion quantities and signs

Constant acceleration means the velocity changes by equal amounts in equal time intervals. We usually model the object as a particle, so we only track its motion, not its size or shape.

The five SUVAT quantities are displacement $s$, initial velocity $u$, final velocity $v$, acceleration $a$, and time $t$. Displacement, velocity, and acceleration can be positive or negative because they depend on your chosen positive direction.

Before using any formula, convert speeds to m/s and distances to metres. A good habit is to choose the positive direction first and keep that sign convention all the way through.

## The SUVAT equations

The SUVAT equations work only when acceleration is constant. To solve kinematics problems, write down the values you know and then choose an equation containing just one unknown.

These are the five standard equations used for constant acceleration:
$$
\begin{aligned}
v &= u+at\\
s &= ut+\frac{1}{2}at^2\\
s &= vt-\frac{1}{2}at^2\\
s &= \frac{u+v}{2}t\\
v^2 &= u^2+2as
\end{aligned}
$$

The best first choice is usually the equation that avoids an extra unknown. If a speed is given in km/h, divide by 3.6 before substituting into SUVAT. For example, $18$ km/h = $5$ m/s and $54$ km/h = $15$ m/s.

## Worked example: find acceleration, then time

A particle starts from rest, travels 75 m, and reaches a speed of 30 m/s. The known values are $u=0$, $v=30$, and $s=75$.

Time is unknown, so start with the equation that does not contain $t$.

$$
\begin{aligned}
v^2 &= u^2 + 2as\\
30^2 &= 0^2 + 2a(75)\\
900 &= 150a\\
a &= 6
\end{aligned}
$$

This gives the acceleration directly.

Now use $v=u+at$ to find the time.

$$
\begin{aligned}
30 &= 0 + 6t\\
t &= 5
\end{aligned}
$$

This is quicker than starting with $s=ut+\frac{1}{2}at^2$, which would introduce two unknowns at once.

## Average velocity and the midpoint trap

When acceleration is constant, the average velocity is halfway between the initial and final velocities. This makes the equation $s=\frac{u+v}{2}t$ often the quickest way to solve problems without needing to calculate acceleration first.

For example, if a particle travels 96 m in 6 s and finishes at 20 m/s, we can solve for the initial velocity $u$ using the average velocity formula:
$$
\begin{aligned}
96 &= \frac{u+20}{2}\times 6\\
u &= 12
\end{aligned}
$$
In this case, the initial velocity is 12 m/s.

A common mistake is to think the midpoint of the distance happens at half the total time. Under acceleration this is not true, because equal time intervals do not cover equal distances when the velocity is changing.

Consider a car going from 4 m/s to 16 m/s in 6 s, covering 60 m total. Finding the time $t$ to reach the 30 m midpoint involves solving a quadratic equation:
$$
\begin{aligned}
30 &= 4t + \frac{1}{2}(2)t^2\\
0 &= t^2+4t-30\\
t &= -2+\sqrt{34}\approx 3.83
\end{aligned}
$$
The midpoint is reached after about 3.83 s, not at the 3 s mark.

## Vertical motion under gravity

![Ball thrown upward from 3 m above the ground with upward positive direction, launch velocity, top point, and downward gravity labelled](../assets/001-b02b8d2d-f502-4e51-8093-258471bb4b66.jpeg)

In vertical motion, choose a positive direction before writing any equations. If upwards is positive, gravity acts downward so $a=-g$.

At the highest point, the velocity is zero for an instant, but the acceleration is still downward. If the motion is freely under gravity, air resistance is ignored and you use $g=9.8$ unless the question states $10$. If you choose downwards as positive instead, then use $a=g$.

## Worked example: thrown up from a height

A ball is thrown vertically upwards at 14 m/s from 3 m above the ground, and take $g=10$. With upwards positive, $u=14$ and $a=-10$.

At the greatest height, $v=0$, so
$$
\begin{aligned}
0^2 &= 14^2 + 2(-10)s\\
0 &= 196-20s\\
s &= 9.8
\end{aligned}
$$
This is the extra height above the release point, so the greatest height above the ground is 12.8 m.

To reach the ground, the displacement from the release point is $-3$, so
$$
\begin{aligned}
-3 &= 14T + \frac{1}{2}(-10)T^2\\
-3 &= 14T - 5T^2\\
5T^2-14T-3 &= 0\\
T &= 3
\end{aligned}
$$
Take the positive root because time cannot be negative.

Finally, we calculate the velocity at impact:
$$
\begin{aligned}
v &= u+at\\
v &= 14-10(3) = -16
\end{aligned}
$$
The negative sign means the ball is moving downward, so the impact speed is 16 m/s.

## Velocity-time graphs

![Velocity-time graph with acceleration, constant velocity, deceleration, and shaded area under the graph](../assets/002-cf0a5251-97ff-4861-8f8f-2b193875b390.jpeg)

On a velocity-time graph, the gradient gives the acceleration. The area under a velocity-time graph gives the displacement. If the graph stays above the time axis, that area is also the total distance travelled.

Example: a train starts from rest and accelerates at $0.6 \text{ m/s}^{2}$ for $40 \text{ s}$, so:
$$
\begin{aligned}
v &= 0 + 0.6(40) = 24\\
t_{\text{decel}} &= \frac{24}{0.4} = 60
\end{aligned}
$$
So the top speed is $24 \text{ m/s}$ and the deceleration lasts $60 \text{ s}$.

The two triangular areas are $480 \text{ m}$ and $720 \text{ m}$, so together they account for $1200 \text{ m}$. For a total distance of $3 \text{ km} = 3000 \text{ m}$, the remaining $1800 \text{ m}$ is covered at $24 \text{ m/s}$:
$$
\begin{aligned}
\text{middle time} &= \frac{1800}{24} = 75\\
\text{total time} &= 40+75+60 = 175
\end{aligned}
$$
So the whole journey takes $175 \text{ s}$.

## Check yourself

1. Which statement is true for motion in a straight line?

   - Constant acceleration means constant speed

   - Displacement can be negative ✔

   - Speed is always equal to velocity

   - Distance can be negative

   _Explanation:_ Displacement is measured in a chosen direction, so it can be negative. The common wrong answer A mixes up acceleration with speed: under constant acceleration, the speed usually changes steadily rather than staying constant.

2. For the data $u=0$, $v=30$, $s=75$, which equation is the best first choice?

   - $$s=ut+\frac{1}{2}at^2$

   - $$v=u+at$

   - $$v^2=u^2+2as$ ✔

   - $$s=\frac{u+v}{2}t$

   _Explanation:_ $$v^2=u^2+2as$ is best because it uses only one unknown, $a$. The common wrong answer B looks familiar, but it contains both $a$ and $t$, so it cannot be solved on its own. Hint: Pick the equation with one unknown, not two.

3. A ball is thrown straight up, and upwards is taken as positive. What is true at the highest point?

   - $$v=0$ and $a=0$

   - $$v=0$ and $a=-g$ ✔

   - $$v=u$ and $a=0$

   - $$v=-u$ and $a=g$

   _Explanation:_ The ball's velocity is zero only for that instant at the top, but gravity still accelerates it downward, so $a=-g$. The common wrong answer A assumes zero velocity means zero acceleration, which is not true.

4. On a velocity-time graph, what does the area under the graph represent?

   - Acceleration

   - Displacement ✔

   - Final velocity

   - Time taken

   _Explanation:_ Area has units $(\text{m s}^{-1}) \times \text{s} = \text{m}$, so it represents displacement. The common wrong answer A confuses area with gradient, and it is the gradient that gives acceleration.
