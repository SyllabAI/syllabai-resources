# grade-6-6-10-spheres-and-cones — lesson

_Lane: `igcse-maths-edexcel` · grade 6 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Key measurements and cone formulae

![Labelled cone showing base radius, vertical height, slant height, and the right triangle inside the cone](../assets/001-dcc733b7-5182-4837-954b-022157733e8b.jpeg)

Spheres and cones are built from circles, so most formulae use the radius $r$. If a question gives the diameter $d$, convert first with $r = \frac{d}{2}$.

In a cone, the vertical height $h$ goes straight from the centre of the base to the apex, while the slant height $l$ runs up the outside edge. The main cone formulas are $V = \frac{1}{3}\pi r^2 h$ for volume and $A = \pi r l + \pi r^2$ for total surface area.

The radius, vertical height, and slant height form a right triangle, so $l^2 = r^2 + h^2$. Volume answers use cubic units such as $\text{cm}^3$, while surface area answers use square units such as $\text{cm}^2$.

## Worked example: cone volume from a diameter

A cone has height 15 cm and base diameter 12 cm. Start by changing diameter to radius, because the formula needs $r$.

$$$r = \frac{12}{2} = 6$$

Now substitute into the volume formula and simplify the exact value first. Leaving the answer in terms of $\pi$ keeps the working accurate.

$$$V = \frac{1}{3}\pi \times 6^2 \times 15 = 180\pi \, \text{cm}^3$$

If a decimal is required, round only at the end. Here $180\pi \approx 565$, so the volume is $565 \, \text{cm}^3$ to 3 significant figures.

## Worked example: total surface area of a cone

For surface area, first check whether you have the slant height. A solid cone has vertical height 12 cm and base diameter 18 cm, so its radius is $9$ cm and you must use Pythagoras.

$$$l^2 = 12^2 + 9^2 = 225$$
$$l = 15$$

Now add the curved surface area and the base area. Because the question asks for an exact answer, leave $\pi$ in the final line.

$$$A = \pi r l + \pi r^2 = \pi \times 9 \times 15 + \pi \times 9^2 = 216\pi \, \text{cm}^2$$

## Sphere and hemisphere formulae

![Labelled hemisphere showing radius, curved surface, and flat circular base](../assets/002-cc6f41f5-b6ac-41d5-b04a-cd18d9f483eb.jpeg)

A sphere uses the formulas $V = \frac{4}{3}\pi r^3$ and $A = 4\pi r^2$. A hemisphere is half of a sphere, so its volume is $V = \frac{2}{3}\pi r^3$.

For area, be careful about whether the flat circle is included. The curved surface area of a hemisphere is $2\pi r^2$, but the total surface area of a solid hemisphere is $2\pi r^2 + \pi r^2 = 3\pi r^2$.

If the question says "in terms of $\pi$", stop once the number part is simplified. Do not turn $\pi$ into a decimal unless the question asks for rounding.

## Reverse problems: finding the radius

Sometimes you know the volume and must work backwards. If a cube has side $6 \, \text{cm}$, its volume is $6^3 = 216 \, \text{cm}^3$, so a sphere with the same volume satisfies:

$$$\frac{4}{3}\pi r^3 = 216$$

Rearrange to isolate $r^3$. Because the radius is cubed, the final step will be a cube root, not a square root. $$r^3 = \frac{216 \times 3}{4\pi} = \frac{162}{\pi}$$

Now take the cube root and round at the end. The radius is about $3.72 \, \text{cm}$ to 3 significant figures. $$r = \sqrt[3]{\frac{162}{\pi}} \approx 3.72 \, \text{cm}$$

## Compound solids and water displacement

A compound solid is made from two or more shapes joined together. For volume calculations, you simply add the volumes of the individual parts, but for surface area, you must only count the faces visible on the outside. Consider a cone of radius $4$ cm and height $9$ cm sitting on top of a hemisphere of radius $4$ cm.

$$$V = \frac{1}{3}\pi \times 4^2 \times 9 + \frac{2}{3}\pi \times 4^3 = 48\pi + \frac{128}{3}\pi = \frac{272}{3}\pi \, \text{cm}^3$$

Water displacement also relies on the principle of volume. A fully submerged object displaces a volume of water equal to its own volume. In a rectangular container, this causes the water level to rise based on the base area (length $\times$ width):
$$\text{rise in water level} = \frac{\text{volume displaced}}{\text{base area}}$$

If a sphere of radius $3$ cm sinks into a $12$ cm by $10$ cm tank, the rise in water level is:
$$\text{rise} = \frac{\frac{4}{3}\pi \times 3^3}{12 \times 10} = \frac{36\pi}{120} \approx 0.942 \, \text{cm}$$
Always ensure the object is fully submerged and the container does not overflow when performing these calculations.

## Check yourself

1. A cone has diameter 10 cm and vertical height 12 cm. What is its slant height?

   - $$5 \, \text{cm}$

   - $$12 \, \text{cm}$

   - $$13 \, \text{cm}$ ✔

   - $$17 \, \text{cm}$

   _Explanation:_ The diameter is 10 cm, so the radius is $5$ cm. Using the Pythagorean theorem, the slant height is $l = \sqrt{5^2 + 12^2} = \sqrt{169} = 13$ cm. The common wrong answer $12$ cm is the vertical height, but the slant height is the length along the side of the cone. Hint: Convert the diameter to the radius before using Pythagoras.

2. A solid cone has radius 7 cm and vertical height 24 cm. What is its total surface area in terms of $\pi$?

   - $$175\pi \, \text{cm}^2$

   - $$217\pi \, \text{cm}^2$

   - $$224\pi \, \text{cm}^2$ ✔

   - $$625\pi \, \text{cm}^2$

   _Explanation:_ First find the slant height: $l = \sqrt{7^2 + 24^2} = 25$. Then $A = \pi r l + \pi r^2 = \pi \times 7 \times 25 + \pi \times 7^2 = 175\pi + 49\pi = 224\pi \, \text{cm}^2$. The common wrong answer $217\pi$ comes from using the vertical height 24 instead of the slant height 25 in $\pi r l$.

3. A sphere has the same volume as a cube of side length 8 cm. What is the radius of the sphere to 3 significant figures?

   - $$4.96 \, \text{cm}$ ✔

   - $$5.46 \, \text{cm}$

   - $$7.27 \, \text{cm}$

   - $$8.00 \, \text{cm}$

   _Explanation:_ The cube volume is $8^3 = 512 \, \text{cm}^3$. Solve $\frac{4}{3}\pi r^3 = 512$ to get $r^3 = \frac{384}{\pi}$, then take the cube root: $r = \sqrt[3]{\frac{384}{\pi}} \approx 4.96 \, \text{cm}$. The common wrong answer $8.00$ comes from taking the cube root of 512 and ignoring the factor $\frac{4}{3}\pi$.
