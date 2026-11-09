# grade-6-6-11-sector-areas-and-arc-lengths — lesson

_Lane: `igcse-maths-edexcel` · grade 6 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Parts of a sector

![Labelled sector with centre O, two radii marked r, central angle theta, arc length L and shaded sector area A](../assets/001-9ddae9cc-79e2-4346-9d57-105b258fb483.jpeg)

A sector is a slice of a circle made by two radii and an arc. If the angle at the centre is $\theta$, then the sector is the fraction $\frac{\theta}{360}$ of the whole circle.

Start from the full circle formulae $C = 2\pi r$ and $A = \pi r^2$. Then multiply by the same fraction $\frac{\theta}{360}$ to get arc length or sector area.

Be careful with units. Area is in square units such as square centimetres, but arc length and perimeter are in units such as cm.

## Area of a sector

To find the area of a sector, multiply the area of the full circle by the fraction of the circle. In this formula, $r$ is the radius and $\theta$ is the central angle measured in degrees.

$$$A = \frac{\theta}{360}\times \pi r^2$$

If $r = 8$ cm and $\theta = 150^\circ$, we calculate the exact area by substituting these values: $$A = \frac{150}{360}\times \pi \times 8^2 = \frac{80\pi}{3}$$

Rounding only at the final step, we find $\frac{80\pi}{3} \approx 83.8$ square centimetres to 3 significant figures. This same formula works for major sectors where $\theta$ is greater than $180^\circ$.

## Arc length and perimeter

Arc length is a fraction of the full circumference. It is measured in length units such as cm, rather than square units. The general formula is:
$$L = \frac{\theta}{360}\times 2\pi r$$

For example, if $r = 12$ cm and $\theta = 135^\circ$, the calculation is:
$$L = \frac{135}{360}\times 2\pi \times 12 = \frac{3}{8}\times 24\pi = 9\pi$$
This results in an arc length of $9\pi$ cm.

The perimeter of a sector is the sum of the curved arc length plus the two straight radii that bound the shape. Be careful not to forget either radius:
$$P = L + 2r$$

Consider a sector with $r = 5.4$ cm and $\theta = 80^\circ$. First, find the arc length $L = \frac{80}{360}\times 2\pi \times 5.4 = 2.4\pi$. Then, calculate the total perimeter $P = 2.4\pi + 10.8 \approx 18.3$ cm to 3 significant figures.

## Shaded regions by subtraction

![Composite diagram of a 90 degree sector of radius 10 cm with an internal semicircle of diameter 10 cm and the remaining region shaded](../assets/002-4600c1eb-06a1-4727-9f11-837074f2f871.jpeg)

Many shaded-region questions are really subtraction questions. Find the larger area first, then subtract the smaller shape inside it.

Here the sector area is:

$$A_{\text{sector}} = \frac{90}{360} \times \pi \times 10^2 = 25\pi$$

The semicircle has a diameter of 10 cm, so its radius is 5 cm and its area is calculated as:

$$A_{\text{semi}} = \frac{1}{2} \times \pi \times 5^2 = \frac{25\pi}{2}$$

Now subtract to find the remaining region:

$$A_{\text{shaded}} = 25\pi - \frac{25\pi}{2} = \frac{25\pi}{2}$$

The same idea works with rectangles, semicircles, and sectors: calculate each piece carefully, then combine them.

## When the angle is missing

Sometimes the angle is not given, but the radius and arc length are. In these cases, you can find the area using the shortcut:

$$A = \frac{1}{2}rL$$

where $L$ is the arc length.

This works because area and arc length use the same fraction of the full circle. If you substitute the expression $L = \frac{\theta}{360} \times 2\pi r$ into the standard area formula, it simplifies directly to this shortcut.

Example: if $r = 8$ cm and $L = 5\pi$ cm, then:

$$A = \frac{1}{2} \times 8 \times 5\pi = 20\pi$$

So the sector area is $20\pi$ square centimetres.

## Check yourself

1. A sector has central angle $135^\circ$. What fraction of the full circle is the sector?

   - $$\frac{3}{8}$ ✔

   - $$\frac{3}{4}$

   - $$\frac{5}{8}$

   - $$\frac{135}{180}$

   _Explanation:_ A full circle is $360^\circ$, so the fraction is $\frac{135}{360} = \frac{3}{8}$. The common wrong answer $\frac{3}{4}$ comes from comparing $135^\circ$ with $180^\circ$ instead of with the full $360^\circ$.

2. A sector has radius 5.4 cm and angle $80^\circ$. What is its perimeter to 3 significant figures?

   - 18.3 ✔

   - 7.54

   - 10.8

   - 13.2

   _Explanation:_ First find the arc length: $L = \frac{80}{360}\times 2\pi \times 5.4 = 2.4\pi \approx 7.54$ cm. Then add the two radii, so $P = 7.54 + 10.8 \approx 18.3$ cm; the common wrong answer 7.54 is just the arc length with the straight sides forgotten. Hint: Perimeter means every outside edge.

3. Stretch: A sector has radius 9 cm and arc length $6\pi$ cm. What is its area?

   - $$27\pi$ ✔

   - $$54\pi$

   - $$15\pi$

   - $$3\pi$

   _Explanation:_ Hint: The angle is missing, so use the radius and the arc length directly. Use the shortcut $A = \frac{1}{2}rL = \frac{1}{2}\times 9\times 6\pi = 27\pi$ square centimetres. The common wrong answer $54\pi$ comes from multiplying $9\times 6\pi$ but forgetting the factor of $\frac{1}{2}$.
