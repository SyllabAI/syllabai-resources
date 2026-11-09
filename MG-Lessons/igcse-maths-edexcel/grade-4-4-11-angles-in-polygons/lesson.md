# grade-4-4-11-angles-in-polygons — lesson

_Lane: `igcse-maths-edexcel` · grade 4 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Interior angles and the triangle method

![Hexagon split into four triangles from one vertex, showing how a polygon can be divided into triangles to find the interior angle sum](../assets/001-21ef815e-7d9a-4c91-9886-6e7219f600be.jpeg)
A polygon is a flat 2D shape with straight sides, and a vertex is a corner. An interior angle is the angle inside the polygon at a vertex.

Three facts power most polygon questions: angles on a straight line add to $180^\circ$, angles around a point add to $360^\circ$, and angles in a triangle add to $180^\circ$. To find the total interior angle sum, split the polygon into triangles from one vertex.

An $n$-sided polygon makes $n - 2$ triangles, and each triangle has an angle sum of $180^\circ$. This gives the key formula for the total sum of all interior angles:

$$$
\text{sum of interior angles} = (n - 2)\times 180^\circ
$$

Do not confuse this with $360^\circ$, which is used for angles around a point and for the sum of exterior angles. Ensure you count the number of sides $n$ carefully before calculating.

## Worked example: a missing angle in a pentagon

A pentagon has 5 sides, so its interior angle sum is:
$$
(5 - 2)\times 180^{\circ} = 540^{\circ}
$$
This is the total for all five interior angles together.

Add the four known angles:
$$
102^{\circ} + 118^{\circ} + 93^{\circ} + 127^{\circ} = 440^{\circ}
$$
These known angles use up most of the total.

Subtract from the full sum to find the missing angle:
$$
x = 540^{\circ} - 440^{\circ} = 100^{\circ}
$$
Always find the polygon total first, then subtract the known angles.

## Regular polygons: interior and exterior angles

![Regular hexagon with an interior angle and adjacent exterior angle labelled, showing they form a straight line](../assets/002-47cda80e-cb3f-40e4-89b6-6272dd175c3a.jpeg)
A regular polygon has all sides equal and all interior angles equal. Once you know the total interior angle sum, you can divide by the number of sides to find the size of one interior angle.

For a regular polygon with $n$ sides, the size of each interior angle is calculated using this formula:
$$\text{each interior angle} = \frac{(n - 2)\times 180^\circ}{n}$$

At each vertex, the interior angle and exterior angle add to $180^\circ$ because they lie on a straight line. Since the exterior angles of any convex polygon add to $360^\circ$, we use this formula for regular shapes:
$$\text{each exterior angle} = \frac{360^\circ}{n}$$

For a regular decagon, the interior angle is found by:
$$\frac{(10 - 2)\times 180^\circ}{10} = 144^\circ$$
This means each interior angle is $144^\circ$. The matching exterior angle is calculated as $180^\circ - 144^\circ = 36^\circ$.

## Working backwards to find the number of sides

If you know each exterior angle of a regular polygon, use:
$$
n = \frac{360^\circ}{\text{each exterior angle}}
$$
This works because all the exterior angles together make one full turn.

If you are given an interior angle instead, first convert it using $180^\circ - \text{interior angle}$. Do not divide $360^\circ$ by the interior angle itself.

Example: if each interior angle is $160^\circ$, the exterior angle is $180^\circ - 160^\circ = 20^\circ$. So the number of sides is:
$$
\frac{360^\circ}{20^\circ} = 18
$$

## Polygons meeting at a point

![Triangle, decagon and unknown polygon P meeting at one point, with angles 60°, 144° and the remaining angle around the point shown](../assets/003-442dc6e1-1cbb-4763-b97d-586628c77bb8.jpeg)
When regular polygons meet at one point, the angles around that point add to $360^\circ$. Find the known interior angles first, then use the remaining angle for the unknown polygon.

A regular triangle has interior angle $60^\circ$, and a regular decagon has interior angle
$$
\frac{(10 - 2)\times 180^\circ}{10} = 144^\circ
$$
So polygon $P$ has interior angle
$$
360^\circ - 60^\circ - 144^\circ = 156^\circ
$$

Now convert to an exterior angle:
$$
180^\circ - 156^\circ = 24^\circ
$$
Then find the number of sides:
$$
\frac{360^\circ}{24^\circ} = 15
$$
so polygon $P$ is a 15-sided polygon.

## Irregular polygons and algebra

If a polygon is not regular, do not divide by the number of sides. Instead, find the interior angle sum, add the known angles, and use algebra for the unknown ones.

In a hexagon, the interior angle sum is
$$
(6 - 2) \times 180^\circ = 720^\circ
$$
If four angles are $118^\circ$, $132^\circ$, $126^\circ$, and $140^\circ$, they add to $516^\circ$.

That leaves $720^\circ - 516^\circ = 204^\circ$ for the two unknown angles $x$ and $2x$. So
$$
x + 2x = 204^\circ
$$
which simplifies to $3x = 204^\circ$.

Divide by 3 to get $x = 68^\circ$. By substituting this back into the expression for the larger angle, we find $2x = 136^\circ$.

## Check yourself

1. Which formula gives the sum of the interior angles of an $n$-sided polygon?

   - $$(n - 2)\times 180^\circ$ ✔

   - $$n\times 180^\circ$

   - $$(n - 2)\times 360^\circ$

   - $$360^\circ$

   _Explanation:_ A is correct because an $n$-sided polygon can be split into $n - 2$ triangles, and each triangle has angle sum $180^\circ$. D is the common wrong answer because $360^\circ$ is for angles around a point or for the total exterior angles, not for the interior angles of most polygons.

2. Each interior angle of a regular decagon is:

   - $$108^\circ$

   - $$144^\circ$ ✔

   - $$36^\circ$

   - $$162^\circ$

   _Explanation:_ First find the total interior sum, $(10 - 2)\times 180^\circ = 1440^\circ$, then divide by 10 because the polygon is regular, giving $144^\circ$. C is the common wrong answer because $36^\circ$ is the exterior angle, found from $360^\circ \div 10$. Note: Regular means all the interior angles are equal.

3. A regular square, a regular hexagon and a regular polygon $Q$ meet at one point. How many sides does $Q$ have?

   - 10

   - 12 ✔

   - 15

   - 30

   _Explanation:_ A square has interior angle $90^\circ$ and a regular hexagon has interior angle $120^\circ$, so the remaining angle is $360^\circ - 90^\circ - 120^\circ = 150^\circ$. The exterior angle of $Q$ is $180^\circ - 150^\circ = 30^\circ$, so $n = 360^\circ \div 30^\circ = 12$; D is the common wrong answer because $30^\circ$ is the exterior angle, not the number of sides.
