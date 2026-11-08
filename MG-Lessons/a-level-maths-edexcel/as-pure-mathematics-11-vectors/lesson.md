# as-pure-mathematics-11-vectors — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Vectors in component form

A scalar has size only, but a vector has size and direction. In AS Maths, two-dimensional vectors are usually written using $\mathbf{i}$ and $\mathbf{j}$.

$$\mathbf{i}$ means 1 unit in the positive horizontal direction, and $\mathbf{j}$ means 1 unit in the positive vertical direction. So $4\mathbf{i}-3\mathbf{j}$ means 4 units right and 3 units down.

Read $a\mathbf{i}+b\mathbf{j}$ as instructions: move $a$ horizontally and $b$ vertically. A negative component means move in the opposite direction.

## Position vectors and vectors between points

![Coordinate plane showing position vectors OA and OB and displacement AB between A(4,-2) and B(-3,6)](../assets/001-f425ed9b-f38a-4f25-bfa8-9d6ce2964c07.jpeg)

A position vector tells you where a point is relative to the origin $O$. To find the vector from $A$ to $B$, subtract the starting position vector from the finishing position vector.

$$$
\vec{AB}=\vec{OB}-\vec{OA}
$$

Order matters when calculating displacement, because the vector $\vec{BA}$ points in the exact opposite direction of $\vec{AB}$.

If $A$ has position vector $4\mathbf{i}-2\mathbf{j}$ and $B$ has position vector $-3\mathbf{i}+6\mathbf{j}$, then:

$$\vec{AB}=(-3\mathbf{i}+6\mathbf{j})-(4\mathbf{i}-2\mathbf{j})=-7\mathbf{i}+8\mathbf{j}$$

When simplifying, only combine $\mathbf{i}$ terms with $\mathbf{i}$ terms, and $\mathbf{j}$ terms with $\mathbf{j}$ terms.

## Magnitude and length

The magnitude of a vector is its length, written $|\mathbf{v}|$. If a vector is given in terms of unit vectors as $\mathbf{v}=a\mathbf{i}+b\mathbf{j}$, its magnitude is calculated using the following formula:

$$$ |\mathbf{v}|=\sqrt{a^2+b^2} $$

For example, if $\mathbf{v}=-7\mathbf{i}+8\mathbf{j}$, we calculate the magnitude by squaring the components: $$ |\mathbf{v}|=\sqrt{(-7)^2+8^2}=\sqrt{49+64}=\sqrt{113} $$ So the length is $\sqrt{113}$, which is approximately $10.6$.

If a question provides the magnitude, there may be two possible answers for a missing component. For instance, the equation $|5\mathbf{i}+k\mathbf{j}|=13$ leads to $25+k^2=169$, which simplifies to $k^2=144$ and gives $k=\pm 12$.

## Adding vectors and resultants

When vectors act together, add their components separately. This gives the resultant vector, which has the same overall effect as all the original vectors together.

For $\mathbf{F}_1=-2\mathbf{i}+6\mathbf{j}$, $\mathbf{F}_2=7\mathbf{i}-4\mathbf{j}$, and $\mathbf{F}_3=3\mathbf{i}+5\mathbf{j}$, the resultant is:
$$\mathbf{R}=(-2+7+3)\mathbf{i}+(6-4+5)\mathbf{j}=8\mathbf{i}+7\mathbf{j}$$
Simply add the $\mathbf{i}$ parts together and the $\mathbf{j}$ parts together to find the new components.

If the resultant and one vector are known, you can work backwards. Compare the horizontal components and vertical components separately to find the missing vector.

## Velocity vectors, speed and bearing

![Compass diagram with north and east axes, a south-east velocity vector with components 6 east and 8 south, and the bearing marked about 143 degrees](../assets/002-5031e854-29bd-404f-b1b7-0fae3a92d0f9.jpeg)
A velocity vector tells you both speed and direction. If $\mathbf{i}$ is east and $\mathbf{j}$ is north, then speed is the magnitude of the vector and bearing is measured clockwise from north.

For velocity $(6\mathbf{i}-8\mathbf{j}) \, \text{m s}^{-1}$,
$$
\text{speed}=\sqrt{6^2+(-8)^2}=10 \, \text{m s}^{-1}
$$
The signs show 6 east and 8 south, so the motion is in the south-east quadrant.

The angle below east is
$$
\theta=\tan^{-1}\left(\frac{8}{6}\right)\approx 53.1^\circ
$$
Bearings start from north, so
$$
\text{bearing}=90^\circ+53.1^\circ\approx 143^\circ
$$

## Vectors in triangles

In a triangle, vectors between vertices still follow start-to-finish subtraction. If two vectors start from the same point, subtract them to get the side joining their endpoints.

For example, the vector $\vec{BC}$ can be found using the relationship $\vec{BC}=\vec{AC}-\vec{AB}$. If $\vec{AB}=6\mathbf{i}-2\mathbf{j}$ and $\vec{AC}=9\mathbf{i}+4\mathbf{j}$, then:
$$
\vec{BC}=(9\mathbf{i}+4\mathbf{j})-(6\mathbf{i}-2\mathbf{j})=3\mathbf{i}+6\mathbf{j}
$$

You can find side lengths using magnitude in exactly the same way. For the vector $\vec{AB}$ defined previously, the length is calculated as:
$$
|\vec{AB}|=\sqrt{6^2+(-2)^2}=\sqrt{40}=2\sqrt{10}
$$

## Check yourself

1. What does the vector $4\mathbf{i}-3\mathbf{j}$ represent?

   - 4 units right and 3 units down ✔

   - 4 units left and 3 units up

   - 3 units right and 4 units down

   - 4 units right and 3 units up

   _Explanation:_ The $\mathbf{i}$ component gives horizontal movement and the $\mathbf{j}$ component gives vertical movement, so $4\mathbf{i}-3\mathbf{j}$ means 4 right and 3 down. The common wrong answer is D, which ignores the negative sign on the $\mathbf{j}$ component.

2. Given that $|5\mathbf{i}+k\mathbf{j}|=13$, what are the possible values of $k$?

   - $$12$ only

   - $$-12$ only

   - $$\pm 12$ ✔

   - $$\pm 8$

   _Explanation:_ Using $13^2=5^2+k^2$ gives $169=25+k^2$, so $k^2=144$ and therefore $k=\pm 12$. The common wrong answer is A, which forgets that squaring removes the sign. Hint: Square the magnitude equation.

3. A velocity vector is $-5\mathbf{i}+2\mathbf{j}$, where $\mathbf{i}$ is east and $\mathbf{j}$ is north. Which interval must its bearing lie in?

   - Between $0^{\circ}$ and $90^{\circ}$

   - Between $90^{\circ}$ and $180^{\circ}$

   - Between $180^{\circ}$ and $270^{\circ}$

   - Between $270^{\circ}$ and $360^{\circ}$ ✔

   _Explanation:_ A negative $\mathbf{i}$ component means west and a positive $\mathbf{j}$ component means north, so the vector points north-west. Bearings in the north-west quadrant lie between $270^{\circ}$ and $360^{\circ}$, while the common wrong answer A forgets the west component and assumes north-east.

4. In triangle $ABC$, $\vec{AB}=6\mathbf{i}-2\mathbf{j}$ and $\vec{AC}=9\mathbf{i}+4\mathbf{j}$. What is $\vec{BC}$?

   - $$3\mathbf{i}+6\mathbf{j}$ ✔

   - $$-3\mathbf{i}-6\mathbf{j}$

   - $$15\mathbf{i}+2\mathbf{j}$

   - $$-15\mathbf{i}-2\mathbf{j}$

   _Explanation:_ Use $\vec{BC}=\vec{AC}-\vec{AB}$, so the components are $(9-6)\mathbf{i}$ and $(4-(-2))\mathbf{j}$, giving $3\mathbf{i}+6\mathbf{j}$. The common wrong answer is B, which reverses the subtraction and actually gives $\vec{CB}$.
