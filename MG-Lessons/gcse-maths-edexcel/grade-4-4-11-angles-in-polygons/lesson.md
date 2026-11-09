# grade-4-4-11-angles-in-polygons — lesson

_Lane: `gcse-maths-edexcel` · grade 4 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Interior and exterior angles

![Pentagon with one interior angle inside, one exterior angle outside, and a straight line showing they add to 180°](../assets/001-77b629cc-7aa9-4c51-9331-b4cb62544e20.jpeg)
A polygon is a flat 2D shape with straight sides, and each corner is called a vertex. The angle inside the shape is an interior angle.

If you extend one side, the angle outside is an exterior angle. At one vertex, the interior and exterior angles form a straight line, so they add to $180^\circ$.

You also need three facts from earlier work: angles on a straight line add to $180^\circ$, angles around a point add to $360^\circ$, and angles in a triangle add to $180^\circ$. These facts are the building blocks for polygon questions.

## Interior angle sum of a polygon

![Regular hexagon split into four triangles from one vertex to show the interior angle sum formula](../assets/002-8c7f9439-d9c1-4653-8cfc-66f26d590f1b.jpeg)
You can find the interior angle sum of a polygon by splitting it into triangles from one vertex. An $n$-sided polygon always splits into $n - 2$ triangles.

Each triangle has an angle sum of $180^\circ$. Therefore, the total interior angle sum is calculated by multiplying the number of triangles by $180^\circ$:
$$\text{interior angle sum} = (n - 2)\times 180^\circ$$

This formula works for any polygon with $n$ sides. For example, a triangle has $180^\circ$, a pentagon $540^\circ$, and a hexagon $720^\circ$. Note that only quadrilaterals add to $360^\circ$, so do not use $360^\circ$ for every polygon.

## Worked example with an irregular polygon

Suppose a hexagon has interior angles $126^\circ$, $133^\circ$, $118^\circ$, $133^\circ$, $y^\circ$ and $2y^\circ$. Because it has 6 sides, its interior angle sum is: $$(6 - 2)\times 180^\circ = 720^\circ$$

That total is the starting point for the whole question. Add the known angles first: $$126^\circ + 133^\circ + 118^\circ + 133^\circ = 510^\circ$$

So the two missing angles must add to $720^\circ - 510^\circ = 210^\circ$. Now write an equation for the missing angles: $$y + 2y = 210^\circ$$

So $3y = 210^\circ$, which gives $y = 70^\circ$. The other missing angle is $2y = 140^\circ$. Do not divide by 6 here, because the polygon is irregular and its angles are not all equal.

## Angles in regular polygons

For any polygon, if you take one exterior angle at each vertex, they add to $360^\circ$. In a regular polygon, all exterior angles are equal, so each exterior angle is given by the following formula:

$$$\frac{360^\circ}{n}$$

At each vertex, the interior and exterior angles meet to form a straight line. Consequently, each interior angle can be found by subtracting the exterior angle from $180^\circ$.

For example, a regular nonagon has an exterior angle of $360^\circ \div 9 = 40^\circ$. Its interior angle is then calculated as $180^\circ - 40^\circ = 140^\circ$.

## Worked example: finding the number of sides

If a regular polygon has interior angle $156^\circ$, do not divide $360^\circ$ by 156. First find the exterior angle, because the exterior angles are the ones that add to $360^\circ$.

Work out the exterior angle: $$180^\circ - 156^\circ = 24^\circ$$ Then use the exterior-angle rule: $$n = \frac{360^\circ}{24^\circ} = 15$$

So the polygon has 15 sides. This method only works for regular polygons, where every exterior angle is the same.

## Regular polygons meeting at a point

![Square, regular hexagon, and regular 12-sided polygon meeting at a point with angles 90°, 120°, and 150° labelled](../assets/003-e982aab2-538a-4dd9-a23b-790c71ccee16.jpeg)
When regular polygons meet at a point, the angles touching the point are usually interior angles. Since these meet around a central point, those interior angles must add to $360^\circ$.

In the diagram, the square contributes $90^\circ$ and the regular hexagon contributes $120^\circ$. We can calculate the third interior angle by subtracting the known values from the total:
$$
360^\circ - 90^\circ - 120^\circ = 150^\circ
$$

Now change that interior angle into an exterior angle using $180^\circ - 150^\circ = 30^\circ$. This allows us to find the number of sides $n$ using the formula for exterior angles:
$$
n = \frac{360^\circ}{30^\circ} = 12
$$

So the third polygon is a 12-sided polygon. A common mistake is using exterior angles at the shared point, but remember that the angles around the point are actually inside the shapes.

## Check yourself

1. At one vertex of a polygon, the interior angle is $128^\circ$. What is the exterior angle at that same vertex?

   - $$52^\circ$ ✔

   - $$128^\circ$

   - $$232^\circ$

   - $$360^\circ$

   _Explanation:_ The interior and exterior angles at one vertex lie on a straight line, so they add to $180^\circ$. That gives $180^\circ - 128^\circ = 52^\circ$. A very common wrong answer is $232^\circ$, which comes from subtracting from $360^\circ$, but $360^\circ$ is for angles around a point, not for two adjacent angles on a straight line.

2. An irregular pentagon has interior angles $100^\circ$, $110^\circ$, $120^\circ$, $130^\circ$, and $x^\circ$. What is $x$?

   - $$80^\circ$ ✔

   - $$108^\circ$

   - $$72^\circ$

   - $$540^\circ$

   _Explanation:_ Hint: Find the total for a pentagon, then subtract the known angles. A pentagon has interior angle sum $540^\circ$. The known angles total $100^\circ + 110^\circ + 120^\circ + 130^\circ = 460^\circ$, so $x = 540^\circ - 460^\circ = 80^\circ$. The most common wrong answer is $108^\circ$, which comes from doing $540^\circ \div 5$ as if the pentagon were regular, but the question says it is irregular.

3. A regular polygon has interior angle $150^\circ$. How many sides does it have?

   - 12 ✔

   - 30

   - 6

   - 15

   _Explanation:_ First find the exterior angle: $180^\circ - 150^\circ = 30^\circ$. Then use $n = 360^\circ \div 30^\circ = 12$. The most common wrong answer is 30, but 30 is the exterior angle, not the number of sides.
