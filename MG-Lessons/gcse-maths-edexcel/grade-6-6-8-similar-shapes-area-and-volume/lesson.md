# grade-6-6-8-similar-shapes-area-and-volume — lesson

_Lane: `gcse-maths-edexcel` · grade 6 · 4 content steps · 3 check questions (source: MathsGenie lessons)_

## Similar solids and linear scale factor

![Small and large similar cylinder with matching radius and height labels, arrows showing how length, surface area, and volume scale, and a cone frustum formed by removing a small cone from a larger cone](../assets/001-36793d32-d311-4807-92ad-7b4ab1c9de59.jpeg)
Similar 3D shapes have the same shape but different sizes. Corresponding lengths are measurements in the same position, such as radius with radius or height with height.

The linear scale factor tells you how one length changes into its matching length. From shape A to shape B, we define the scale factor $k$ using the following formula:
$$k = \frac{\text{length on B}}{\text{matching length on A}}$$

Always label the direction before calculating, such as small to large. If a radius changes from 6 cm to 15 cm, then the linear scale factor is $k = \frac{15}{6} = \frac{5}{2}$.

## How area and volume scale

Surface area is measured in square units such as $\text{cm}^2$, while volume is measured in cubic units such as $\text{cm}^3$. If every corresponding length is multiplied by $k$, then surface area is multiplied by $k^2$ and volume by $k^3$.

Use this rule as a shortcut.
$$\text{surface area factor} = k^2 \qquad \text{volume factor} = k^3$$
Area depends on two lengths, while volume depends on three lengths.

If cylinder B is 3 times as tall as cylinder A, then the length scale factor from A to B is $3$. So the surface area scale factor is $3^2 = 9$ and the volume scale factor is $3^3 = 27$.

A common mistake is to use the length scale factor directly on area or volume. If a length doubles, the surface area becomes 4 times as big, not 2 times as big.

## Worked example: from surface area to volume

Two similar solids X and Y have surface areas $180 \, \text{cm}^2$ and $320 \, \text{cm}^2$. The volume of X is $540 \, \text{cm}^3$, and we want to find the volume of Y. First find the area scale factor from X to Y.

$$\frac{320}{180} = \frac{16}{9}$$

This is an area ratio, so do not cube it yet.

Now square root the area ratio to get the length scale factor $k$. Cubing this length factor gives the volume scale factor we need.

$$k = \sqrt{\frac{16}{9}} = \frac{4}{3}, \qquad \text{volume factor} = \left(\frac{4}{3}\right)^3 = \frac{64}{27}$$

Finally, multiply the volume of solid X by the calculated volume factor to find the volume of solid Y.

$$540 \times \frac{64}{27} = 1280$$

So the volume of Y is $1280 \, \text{cm}^3$.

## Worked example: frustum volume

![Large cone of height 9 cm and diameter 24 cm, small similar top cone of height 3 cm and diameter 8 cm, and the resulting frustum with subtraction of volumes shown](../assets/002-54d57440-ff41-4288-b748-ecf49ac66851.jpeg)

A frustum is the solid left when the top of a cone is cut off parallel to the base. To find its volume, subtract the small cone volume from the large cone volume.

In this example, the large cone has height 9 cm and diameter 24 cm, and the small cone has height 3 cm and diameter 8 cm. The formula uses radius, so first halve the diameters to get $r_{\text{large}} = 12$ and $r_{\text{small}} = 4$.

Use $V = \frac{1}{3}\pi r^2 h$ for each cone. These exact volumes are:

$$
V_{\text{large}} = \frac{1}{3}\pi \times 12^2 \times 9 = 432\pi, \qquad V_{\text{small}} = \frac{1}{3}\pi \times 4^2 \times 3 = 16\pi
$$

Now subtract the two volumes to find the remaining frustum:

$$
V_{\text{frustum}} = 432\pi - 16\pi = 416\pi
$$

So the exact volume of the frustum is $416\pi \, \text{cm}^3$.

## Check yourself

1. Two similar cones have base radii 6 cm and 15 cm. What is the scale factor from the smaller cone to the larger cone?

   - $$\frac{5}{2}$ ✔

   - $$\frac{2}{5}$

   - $$9$

   - $$21$

   _Explanation:_ The scale factor is larger radius divided by smaller radius, so $k = \frac{15}{6} = \frac{5}{2}$. The common wrong answer $\frac{2}{5}$ reverses the direction and would be the scale factor from larger to smaller.

2. Two similar solids have surface areas in the ratio $25:49$. What is the corresponding length ratio?

   - $$5:7$ ✔

   - $$25:49$

   - $$625:2401$

   - $$7:5$

   _Explanation:_ Surface area scales with $k^2$, so you square root the area ratio: $\sqrt{25:49} = 5:7$. The common wrong answer $25:49$ forgets that the area ratio already has the square built in.

3. Two similar solids have volumes in the ratio $27:125$. The surface area of the smaller solid is $54 \, \text{cm}^2$. What is the surface area of the larger solid?

   - $$150 \, \text{cm}^2$ ✔

   - $$250 \, \text{cm}^2$

   - $$90 \, \text{cm}^2$

   - $$54 \, \text{cm}^2$

   _Explanation:_ Cube root the volume ratio to get the length ratio $3:5$. Then square it to get the area ratio $9:25$, so the larger surface area is $54 \times \frac{25}{9} = 150$; the common wrong answer $250 \, \text{cm}^2$ uses the volume ratio directly on area.
