# grade-6-6-13-similar-shapes-area-and-volume — lesson

_Lane: `igcse-maths-edexcel` · grade 6 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What changes in similar solids?

![Two similar solids with matching lengths labelled k, and labels showing area scale factor k squared and volume scale factor k cubed](../assets/001-95937b79-7261-4de0-8aef-4ecaaa75701c.jpeg)

Two 3D shapes are similar if they have the same shape and all corresponding lengths are in the same ratio. The multiplier between matching lengths is called the linear scale factor, $k$.

Lengths scale once, areas scale twice, and volumes scale three times. So:
$$
\text{length scale factor} = k,\qquad \text{area scale factor} = k^2,\qquad \text{volume scale factor} = k^3
$$
This tells you which multiplier to use.

Corresponding lengths must match like with like, such as radius with radius or height with height. If you are given area and need a length, square root the area scale factor, and if you are given volume and need a length, cube root the volume scale factor. Always check whether you are going from smaller to larger or from larger to smaller.

## Worked example: surface area of a larger cone

Suppose two similar cones have radii 5 cm and 15 cm, and the smaller cone has total surface area 70 cm². We start by identifying the corresponding lengths to find the scale factor.

The linear scale factor $k$ from the smaller cone to the larger cone is calculated as:
$$
k = \frac{15}{5} = 3
$$

To find the surface area, square the linear scale factor to get the area scale factor. Applying this to the smaller area gives us:
$$
k^2 = 3^2 = 9, \qquad 70 \times 9 = 630
$$

The larger cone has a surface area of $630 \, \text{cm}^2$. It is important to remember that area does not scale linearly; multiplying by 3 instead of 9 is a common error.

## Worked example: volume of a larger cylinder

Now look at volume, which is 3D, so it scales with the cube of the linear scale factor. Suppose similar cylinders have lengths 4 cm and 6 cm, and the smaller cylinder has volume $80 \text{ cm}^3$.

The linear scale factor is $k = \frac{6}{4} = \frac{3}{2}$. To find the volume scale factor, we cube this value to account for the three dimensions: $$k^3 = \left(\frac{3}{2}\right)^3 = \frac{27}{8}$$

Now multiply the smaller volume by $\frac{27}{8}$: $$80 \times \frac{27}{8} = 270$$ The larger cylinder has volume $270 \, \text{cm}^3$. Remember that squaring the scale factor is a common error reserved for area.

## Working backwards from area to length

Sometimes the question gives areas but asks for a missing length. In that case, find the area scale factor first, then square root it to recover the linear scale factor.

Consider similar cones with surface areas $30 \, \text{cm}^2$ and $120 \, \text{cm}^2$. The area scale factor for these shapes is:
$$\frac{120}{30} = 4$$

The linear scale factor is $k = \sqrt{4} = 2$. If the smaller cone has height 5 cm, the larger cone has a height of $5 \times 2 = 10$ cm. This demonstrates why moving from area to length requires a square root.

## From surface area to volume

A common exam question gives the surface areas of two similar solids and the volume of one of them. To solve this, the route is to find the area ratio, take the square root to find the linear scale factor $k$, and then cube $k$ for the volume ratio.

Suppose solids X and Y have surface areas $500 \, \text{cm}^2$ and $1125 \, \text{cm}^2$, and X has volume $1600 \, \text{cm}^3$. First find the area scale factor and then the linear scale factor:

$$\frac{1125}{500} = 2.25,\qquad k = \sqrt{2.25} = 1.5$$

Now find the volume scale factor and apply it to find the volume of Y:

$$k^3 = 1.5^3 = 3.375,\qquad 1600 \times 3.375 = 5400$$

So Y has volume $5400 \, \text{cm}^3$. Do not cube $2.25$ directly, because $2.25$ is an area scale factor, not a length scale factor.

## Frustums by subtraction

![Large cone, small removed cone, and resulting frustum with heights and diameters labelled to show frustum volume by subtraction](../assets/002-6560e14b-957a-4397-80b6-b8666a6e50ea.jpeg)
A frustum is what remains when the top of a cone is cut off parallel to the base. Because the cut is parallel to the base, the small cone is similar to the large cone.

In the example, the large cone has height 9 cm and diameter 12 cm, so its radius is 6 cm. The small cone has height 3 cm and diameter 4 cm, so its radius is 2 cm.

Use $V = \frac{1}{3}\pi r^2 h$ for each cone:
$$
V_{\text{large}} = \frac{1}{3}\pi \times 6^2 \times 9 = 108\pi,\qquad V_{\text{small}} = \frac{1}{3}\pi \times 2^2 \times 3 = 4\pi
$$
Both volumes are in cubic centimetres.

Now subtract:
$$
108\pi - 4\pi = 104\pi
$$
So the frustum volume is $104\pi \, \text{cm}^3$. Always halve a diameter first, because the formula uses radius.

## Check yourself

1. If the linear scale factor is 3, what is the surface area scale factor?

   - 3

   - 9 ✔

   - 6

   - 27

   _Explanation:_ Surface area uses $k^2$, so with $k = 3$ the scale factor is $3^2 = 9$. A common wrong answer is 3, which treats area like a length instead of squaring the scale factor.

2. Two similar solids have heights $3\text{ cm}$ and $6\text{ cm}$. The smaller solid has volume $50\text{ cm}^3$. What is the volume of the larger solid?

   - 100 cm³

   - 200 cm³

   - 400 cm³ ✔

   - 800 cm³

   _Explanation:_ The linear scale factor is $6 \div 3 = 2$, so the volume scale factor is $2^3 = 8$. Then $50 \times 8 = 400$. A common wrong answer is 200, which comes from squaring instead of cubing. Remember: Volume is 3D, so use the cube factor.

3. Two similar solids have surface areas in the ratio 9:25. The smaller solid has volume 216 cm³. What is the volume of the larger solid?

   - 600 cm³

   - 1000 cm³ ✔

   - 1500 cm³

   - 2160 cm³

   _Explanation:_ The area ratio 9:25 gives the length ratio 3:5, so the volume ratio is 27:125 and the larger volume is $216 \times \frac{125}{27} = 1000$. A common wrong answer is 600, which comes from multiplying by the area ratio $\frac{25}{9}$ instead of square-rooting first.
