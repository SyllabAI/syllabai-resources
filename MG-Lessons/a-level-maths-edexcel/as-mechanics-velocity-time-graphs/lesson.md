# as-mechanics-velocity-time-graphs — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What a velocity-time graph shows

![Velocity-time graph with a rising section for positive acceleration, a horizontal section for constant velocity, a falling section for deceleration, and shaded area labelled as distance travelled](../assets/001-891b1475-7188-40ab-b51a-3979219d5225.jpeg)
A velocity-time graph plots velocity on the vertical axis against time on the horizontal axis. Its shape tells the story of a journey, such as speeding up, moving steadily, or slowing down.

The gradient, or slope, gives acceleration because it measures change in velocity per unit time. On any straight section, the acceleration is constant.
$$a = \frac{\Delta v}{\Delta t}$$

The area under the graph gives displacement. If the whole graph stays above the time axis, that area is also the total distance travelled.
$$\text{displacement} = \text{area under the velocity-time graph}$$

## Using the gradient

Suppose a tram moves from rest to $18 \, \text{m s}^{-1}$ uniformly in $30 \, \text{s}$. The phrase "from rest" tells you the starting velocity is $0 \, \text{m s}^{-1}$.

Use the gradient formula on that rising straight line. You divide the change in velocity by the time taken.

$$$a = \frac{18 - 0}{30} = 0.6 \, \text{m s}^{-2}$$

The units check out because $\text{m s}^{-1} \div \text{s} = \text{m s}^{-2}$. If the tram then continues at $18 \, \text{m s}^{-1}$ for another $20 \, \text{s}$, the graph is horizontal so the acceleration is $0 \, \text{m s}^{-2}$.

## Using area to find distance

When the graph stays above the time axis, distance travelled is the total area underneath it. Split the region into simple shapes such as triangles and rectangles before calculating.

A train reaches $22 \, \text{m s}^{-1}$ in $25 \, \text{s}$, travels at this speed for $40 \, \text{s}$, then slows to rest in $15 \, \text{s}$. The three sections have calculated areas:
$$A_1 = \frac{1}{2} \times 25 \times 22 = 275$$
$$A_2 = 40 \times 22 = 880$$
$$A_3 = \frac{1}{2} \times 15 \times 22 = 165$$

Each area value is measured in metres. Add the three areas to get the whole journey distance. This works because $\text{s} \times \text{m s}^{-1} = \text{m}$.
$$\text{distance} = 275 + 880 + 165 = 1320 \, \text{m}$$

## Sketching and interpreting carefully

A sketch does not need perfect scale, but it must show the correct shape and labels. Always mark the axes first, then add key times and key velocities.

If a car starts from rest, reaches speed $V$ in 8 s, keeps that speed for 12 s, then decelerates to rest in 5 s, the key points are $(0,0)$, $(8,V)$, $(20,V)$, and $(25,0)$. Join these with straight lines because each change is uniform.

If part of the graph goes below the time axis, the velocity there is negative. Its area counts as negative displacement, so for total distance you add the absolute values instead of letting areas cancel.

## Worked example, part 1

Now combine gradient and area in one problem. A train accelerates at $0.5 \, \text{m s}^{-2}$ for $40 \, \text{s}$, then travels at constant speed, then decelerates at $0.4 \, \text{m s}^{-2}$ to rest, and the stations are $3.1 \, \text{km}$ apart.

Convert the distance first so the units match the speeds and accelerations. Since $3.1 \, \text{km} = 3100 \, \text{m}$, the top speed after the first section is

$$$v = 0 + 0.5 \times 40 = 20 \, \text{m s}^{-1}$$

The first triangle has area $A_1 = \frac{1}{2} \times 40 \times 20 = 400 \, \text{m}$. To brake from $20 \, \text{m s}^{-1}$ to rest at $0.4 \, \text{m s}^{-2}$ takes

$$$t = \frac{20}{0.4} = 50 \, \text{s}$$

## Worked example, part 2

The braking section is another triangle, so its area is $$A_3 = \frac{1}{2} \times 50 \times 20 = 500 \, \text{m}$$. Subtract the two triangle distances from the total to find the constant-speed distance.

That leaves $$3100 - 400 - 500 = 2200 \, \text{m}$$ for the rectangular section. Because rectangle area is velocity times time, the cruising time is $$t_c = \frac{2200}{20} = 110 \, \text{s}$$.

Finally, add the three times together. The total time is $$40 + 110 + 50 = 200 \, \text{s}$$. This is sensible because the constant-speed section is the longest part of the journey.

## Check yourself

1. On a velocity-time graph, what does a horizontal section above the time axis mean?

   - Constant velocity and zero acceleration ✔

   - Velocity is increasing at a constant rate

   - The object is at rest

   - Distance travelled is zero

   _Explanation:_ A horizontal line has zero gradient, so the acceleration is zero, and if it is above the time axis the velocity is constant but not zero. The common wrong choice is C, because students often confuse a horizontal line with the time axis itself, but only a line on the time axis means the object is at rest.

2. A car travels at a constant velocity of $15 \, \text{m s}^{-1}$ for $12 \, \text{s}$. What distance is represented by this section on a velocity-time graph?

   - $$27 \, \text{m}$

   - $$90 \, \text{m}$

   - $$180 \, \text{m}$ ✔

   - $$15 \, \text{m s}^{-2}$

   _Explanation:_ A constant-velocity section is a rectangle, so distance is area = base $\times$ height = $12 \times 15 = 180 \, \text{m}$. The common wrong answer is B, which comes from using the triangle formula by mistake even though the section is rectangular. Hint: Constant velocity means a rectangle, not a triangle.

3. A car accelerates from rest to $V \, \text{m s}^{-1}$ in 8 s, travels at this speed for 36 s, then brakes to rest. The magnitude of the deceleration is twice the magnitude of the acceleration, and the total distance is 1008 m. What is $V$?

   - 18

   - 24 ✔

   - 28

   - 42

   _Explanation:_ During acceleration, $a = \frac{V}{8}$, so the braking deceleration magnitude is $\frac{V}{4}$ and the braking time is $\frac{V}{V/4} = 4$ s. The total area is $4V + 36V + 2V = 42V = 1008$, so $V = 24$; the common wrong answer 42 comes from finding the coefficient of $V$ but not actually solving for $V$.
