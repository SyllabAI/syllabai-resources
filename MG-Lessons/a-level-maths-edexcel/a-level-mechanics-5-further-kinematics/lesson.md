# a-level-mechanics-5-further-kinematics — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 3 check questions (source: MathsGenie lessons)_

## Motion with $\mathbf{i}$ and $\mathbf{j}$ components

Further kinematics describes motion in a plane using unit vectors $\mathbf{i}$ and $\mathbf{j}$. In many questions $\mathbf{i}$ is east and $\mathbf{j}$ is north, so $3\mathbf{i}-4\mathbf{j}$ means 3 units east and 4 units south.

A position vector tells you where a particle is relative to the origin, and displacement is final position minus initial position. Velocity is displacement per unit time, while speed is the magnitude of the velocity vector.

For constant velocity, work component by component and then combine the results. The basic model is

$$$\mathbf{r}=\mathbf{r}_0+\mathbf{v}t$$

where $\mathbf{r}_0$ is the initial position vector and $t$ is time.

## Worked example: velocity, speed and bearing

![Coordinate diagram with east as the i-axis and north as the j-axis, showing a boat at noon at (4,-3), at 3 p.m. at (-8,12), the displacement arrow between them, a north-west velocity arrow, and a bearing of about 321 degrees marked from north.](../assets/001-e318aca6-8e8c-4252-a40a-da9e5c3f2ccd.jpeg)

Suppose a boat is at $4\mathbf{i}-3\mathbf{j}$ km at noon and at $-8\mathbf{i}+12\mathbf{j}$ km at 3 p.m. The sketch shows the motion is in the north-west quadrant, so the bearing must be just below $360^{\circ}$.

First find displacement and divide by 3 hours:

$$(-8\mathbf{i}+12\mathbf{j})-(4\mathbf{i}-3\mathbf{j})=-12\mathbf{i}+15\mathbf{j}$$

so

$$\mathbf{v}=\frac{-12\mathbf{i}+15\mathbf{j}}{3}=-4\mathbf{i}+5\mathbf{j} \, \text{km h}^{-1}.$$

Dividing by 3 hours turns km into $\text{km h}^{-1}$ and is a good point to check the signs of both components.

The speed is the magnitude of the velocity:

$$|\mathbf{v}|=\sqrt{(-4)^2+5^2}=\sqrt{41} \, \text{km h}^{-1}.$$

The angle west of north is $\tan^{-1}\left(\frac{4}{5}\right)\approx 38.7^{\circ}$, so the bearing is about $321^{\circ}$.

Now write the position vector after $t$ hours:

$$\mathbf{r}=(4\mathbf{i}-3\mathbf{j})+t(-4\mathbf{i}+5\mathbf{j})=(4-4t)\mathbf{i}+(5t-3)\mathbf{j}.$$

That single equation lets you find the boat's position at any later time.

## Constant acceleration as a vector

With constant acceleration, the usual SUVAT equations work component by component as vector equations. Two key ones are:
$$
\mathbf{v}=\mathbf{u}+\mathbf{a}t
$$
and
$$
\mathbf{r}=\mathbf{r}_0+\mathbf{u}t+\frac{1}{2}\mathbf{a}t^2
$$

If a question says the particle moves in the direction $3\mathbf{i}+4\mathbf{j}$, that gives only a ratio of components. To turn it into a velocity with speed $20 \, \text{m s}^{-1}$, first use the unit vector:
$$
20\left(\frac{3}{5}\mathbf{i}+\frac{4}{5}\mathbf{j}\right)=12\mathbf{i}+16\mathbf{j}
$$

The common mistake is to use $3\mathbf{i}+4\mathbf{j}$ itself as the velocity vector. Always check whether you have been given a direction, a speed, or a full velocity vector before beginning your calculations.

## Worked example: constant acceleration

A particle starts at the origin, initially moves in the direction $3\mathbf{i}+4\mathbf{j}$ with speed $20 \, \text{m s}^{-1}$, and after 5 seconds has velocity $-5\mathbf{i}+18\mathbf{j} \, \text{m s}^{-1}$. First convert the direction and speed into the initial velocity:
$$
\mathbf{u}=20\left(\frac{3}{5}\mathbf{i}+\frac{4}{5}\mathbf{j}\right)=12\mathbf{i}+16\mathbf{j}.
$$

Now use $\mathbf{v}=\mathbf{u}+\mathbf{a}t$ and rearrange to solve for acceleration:
$$
\mathbf{a}=\frac{(-5\mathbf{i}+18\mathbf{j})-(12\mathbf{i}+16\mathbf{j})}{5}=-\frac{17}{5}\mathbf{i}+\frac{2}{5}\mathbf{j} \, \text{m s}^{-2}.
$$
Subtract first and divide second, so each component stays organised.

For position after 5 seconds, use $\mathbf{r}=\mathbf{r}_0+\mathbf{u}t+\frac{1}{2}\mathbf{a}t^2$ with $\mathbf{r}_0=\mathbf{0}$:
$$
\mathbf{r}(5)=(12\mathbf{i}+16\mathbf{j})(5)+\frac{1}{2}\left(-\frac{17}{5}\mathbf{i}+\frac{2}{5}\mathbf{j}\right)(25)=\frac{35}{2}\mathbf{i}+85\mathbf{j} \, \text{m}.
$$
So after 5 seconds the particle is $\frac{35}{2}$ m east and 85 m north of the origin.

## Direction tests and minimum speed

Moving in the direction $\mathbf{i}+2\mathbf{j}$ means the velocity is a positive multiple of that vector. For $\mathbf{v}=(4t-8)\mathbf{i}+(3t+1)\mathbf{j}$, set the component ratio using:

$$$3t+1=2(4t-8).$$

Solving gives $t=\frac{17}{5}$. You should then check that the $\mathbf{i}$ component is positive, because a negative multiple would point in the opposite direction.

To find minimum speed, minimise $V^2$ instead of $V$ because the square root is unnecessary. In this example, the expression for squared speed is:

$$$V^2=(4t-8)^2+(3t+1)^2=25t^2-58t+65$$

Differentiating and solving for zero gives the time of minimum speed:

$$$\frac{d}{dt}(V^2)=50t-58=0 \Rightarrow t=\frac{29}{25}.$$

In constant acceleration questions, minimum speed also occurs when velocity is perpendicular to acceleration. This provides a useful check provided that time lies in the allowed interval.

## Relative motion and collisions

![Coordinate diagram with boat A starting at (6,0) and boat B starting at (0,9), their straight-line paths and velocity arrows, and the collision marked at (-9,12) after 3 hours.](../assets/002-3815d96d-3797-45d3-bb54-e7d7bd0f18c1.jpeg)

Relative position tells you where one particle is seen from another. The diagram shows the two straight-line paths crossing at the collision point.

If $\mathbf{r}_{B/A}=\mathbf{r}_B-\mathbf{r}_A$, then a collision occurs when $\mathbf{r}_{B/A}=\mathbf{0}$. Here
$$\mathbf{r}_A=(6-5t)\mathbf{i}+4t\mathbf{j},\qquad \mathbf{r}_B=-3t\mathbf{i}+(9+t)\mathbf{j}.$$
So
$$\mathbf{r}_{B/A}=\mathbf{r}_B-\mathbf{r}_A=(2t-6)\mathbf{i}+(9-3t)\mathbf{j}.$$
The relative position vector tells you where boat $B$ is from boat $A$ at any time.

Set both components equal to zero:
$$2t-6=0,\qquad 9-3t=0.$$
Both give $t=3$, so the boats collide 3 hours after noon at
$$\mathbf{r}_A(3)=-9\mathbf{i}+12\mathbf{j} \, \text{km}.$$
Checking only one component would miss the key condition that both coordinates must match together.

## Variable kinematics with calculus

When position, velocity or acceleration varies with time, differentiate or integrate each component separately. The core rules are:
$$
\mathbf{v}=\frac{d\mathbf{r}}{dt}
$$
and
$$
\mathbf{a}=\frac{d\mathbf{v}}{dt}.
$$

If $\mathbf{r}_P=(2t^2+3t-1)\mathbf{i}+(t^2+9t+4)\mathbf{j}$, then the velocity and acceleration are found by differentiating:
$$
\mathbf{v}_P=(4t+3)\mathbf{i}+(2t+9)\mathbf{j},
\qquad
\mathbf{a}_P=4\mathbf{i}+2\mathbf{j}.
$$
Differentiate the $\mathbf{i}$ and $\mathbf{j}$ parts exactly as you would in one dimension.

If $\mathbf{a}_Q=(6t-2)\mathbf{i}+4t\mathbf{j}$, integrate to get the velocity vector:
$$
\mathbf{v}_Q=(3t^2-2t+C)\mathbf{i}+(2t^2+D)\mathbf{j}.
$$
Using the given boundary condition $\mathbf{v}_Q(2)=8\mathbf{i}+10\mathbf{j}$ allows us to solve for the constants $C=0$ and $D=2$.

Integrate again and use the initial position $\mathbf{r}_Q(0)=\mathbf{i}-3\mathbf{j}$ to find the position vector:
$$
\mathbf{r}_Q=(t^3-t^2+1)\mathbf{i}+\left(\frac{2}{3}t^3+2t-3\right)\mathbf{j}.
$$
Constants appear every time you integrate, so always use the given conditions to fix them.

## Check yourself

1. A particle moves from $2\mathbf{i}+5\mathbf{j}$ m to $-4\mathbf{i}+\mathbf{j}$ m in 2 s. What is its velocity vector?

   - $$-3\mathbf{i}-2\mathbf{j}$ ✔

   - $$-6\mathbf{i}-4\mathbf{j}$

   - $$3\mathbf{i}+2\mathbf{j}$

   - $$\sqrt{13}$

   _Explanation:_ The displacement is $(-4\mathbf{i}+\mathbf{j})-(2\mathbf{i}+5\mathbf{j})=-6\mathbf{i}-4\mathbf{j}$, and dividing by 2 s gives $-3\mathbf{i}-2\mathbf{j}$. Option B is the common mistake because it is the displacement, not the velocity, so the time division has been missed.

2. A particle moves in the direction $3\mathbf{i}+4\mathbf{j}$ with speed $15 \, \text{m s}^{-1}$. What is its velocity?

   - $$9\mathbf{i}+12\mathbf{j}$ ✔

   - $$3\mathbf{i}+4\mathbf{j}$

   - $$45\mathbf{i}+60\mathbf{j}$

   - $$12\mathbf{i}+9\mathbf{j}$

   _Explanation:_ The direction vector has magnitude 5, so the unit direction is $\frac{3}{5}\mathbf{i}+\frac{4}{5}\mathbf{j}$, and multiplying by 15 gives $9\mathbf{i}+12\mathbf{j}$. Option B is the common wrong answer because it keeps the direction ratio but ignores the required speed. Hint: Scale a unit vector, not the raw direction vector.

3. For $\mathbf{v}=(4t-8)\mathbf{i}+(3t+1)\mathbf{j}$ with $t\ge 0$, when is the speed minimum?

   - $$\frac{17}{5}$

   - $$\frac{29}{25}$ ✔

   - $$\frac{5}{17}$

   - $$\frac{8}{3}$

   _Explanation:_ Minimise $V^2=(4t-8)^2+(3t+1)^2=25t^2-58t+65$, so $\frac{d}{dt}(V^2)=50t-58=0$ gives $t=\frac{29}{25}$. Option A is the common wrong answer because it comes from the direction condition, not from minimising the speed. Hint: Use $V^2$, not $V$.
