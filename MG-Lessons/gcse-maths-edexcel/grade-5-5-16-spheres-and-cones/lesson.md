# grade-5-5-16-spheres-and-cones — lesson

_Lane: `gcse-maths-edexcel` · grade 5 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Key measurements first

![Cone and sphere with radius, diameter, vertical height and slant height labelled](../assets/001-6cac7887-e493-44ca-a337-6e96d6577822.jpeg)

A sphere is perfectly round, and a cone has a circular base and a single point. In both shapes, the radius $r$ is the key measurement, while a cone also uses vertical height $h$ and sometimes slant height $l$.

The diameter goes all the way across a circle or sphere, so $d = 2r$ and $r = \frac{d}{2}$. Most sphere and cone formulas use $r$, so always halve the diameter first if that is what the diagram gives you.

Volume measures the space inside a shape, and surface area measures the outside. For cones, volume uses the vertical height but surface area uses the slant height.

## Volume of cones and spheres

Volume is the space inside a 3D shape. For these solids, use the following formulas:
$$V_{\text{cone}} = \frac{1}{3}\pi r^2 h$$
$$V_{\text{sphere}} = \frac{4}{3}\pi r^3$$

A hemisphere is half a sphere, so its volume is $\frac{2}{3}\pi r^3$. In this worked example, a cone has height 18 cm and diameter 10 cm. First find the radius: $r = \frac{10}{2} = 5 \text{ cm}$.

Now substitute the values into the cone formula:
$$V = \frac{1}{3}\pi \times 5^2 \times 18 = 150\pi$$
This gives $V \approx 471.239$, so the volume is $471 \text{ cm}^3$ to 3 significant figures.

## Surface area of spheres and hemispheres

Surface area is the outside area of a 3D shape. For a sphere, because the whole surface is curved, the area is calculated using this formula:

$$$A_{\text{sphere}} = 4\pi r^2$$

For a solid hemisphere, take half the sphere's curved area, $2\pi r^2$, then add the flat circular base, $\pi r^2$. That gives: $$A_{\text{total hemisphere}} = 3\pi r^2$$

Worked example: if $r = 7 \text{ cm}$, then $$A = 3\pi \times 7^2 = 147\pi$$ So the total surface area is $147\pi \text{ cm}^2$, not $98\pi \text{ cm}^2$.

## Cone surface area and slant height

![Cone cross-section with radius 6 cm, height 8 cm and slant height 10 cm forming a right-angled triangle](../assets/002-d999896f-d6a4-4166-9058-b4e9a70cc590.jpeg)
For a cone, the curved surface area is $$A_{\text{curved}} = \pi r l$$ and the total surface area of a solid cone is $$A_{\text{total}} = \pi r l + \pi r^2$$

This formula uses the slant height $l$, not the vertical height $h$. Worked example: a cone has diameter 12 cm and vertical height 8 cm. First find $r = 6 \text{ cm}$, then use Pythagoras in the cross-section:
$$l^2 = h^2 + r^2 = 8^2 + 6^2 = 100$$

So we find $l = 10 \text{ cm}$ and calculate the area as: $$A = \pi \times 6 \times 10 + \pi \times 6^2 = 96\pi$$ The total surface area is $96\pi \text{ cm}^2$, and using $8$ instead of $10$ would underestimate the curved part.

## Compound solids and displaced water

A compound solid is made by joining simpler 3D shapes. To find its volume, split it into parts, work out each volume, and add them. For example, consider a cone sitting on a hemisphere, both with diameter 8 cm and a cone height of 9 cm.

With $r=4$, the cone volume is $48\pi$ and the hemisphere volume is $\frac{128}{3}\pi$, so: $$V_{\text{total}} = 48\pi + \frac{128}{3}\pi = \frac{272}{3}\pi$$ This gives the compound solid a volume of $\frac{272}{3}\pi \text{ cm}^3$.

If a solid sinks fully in water, it displaces its own volume. The rise in the water level can be found using the relationship: $$\text{rise} = \frac{\text{volume of solid}}{\text{area of container base}}$$

Using this formula, a sphere of radius 3 cm in a 12 cm by 10 cm container raises the water level by $\frac{36\pi}{120} \approx 0.942 \text{ cm}$.

## Working backwards from volume

Sometimes the volume is given and you need the radius. Start with the sphere formula

$$V = \frac{4}{3}\pi r^3$$

then rearrange so $r^3$ is on its own.

Worked example: a cube of side $6 \text{ cm}$ has volume $6^3 = 216 \text{ cm}^3$. If a sphere has the same volume, then

$$\frac{4}{3}\pi r^3 = 216$$

so $r^3 = \frac{162}{\pi}$.

Now use a cube root to solve for the radius:

$$r = \sqrt[3]{\frac{162}{\pi}} \approx 3.72$$

So the radius is $3.72 \text{ cm}$ to 3 significant figures.

## Check yourself

1. A cone has base diameter 14 cm and vertical height 20 cm. Which values should be used for $r$ and $h$ in $V = \frac{1}{3}\pi r^2 h$?

   - $$r=7,\ h=20$ ✔

   - $$r=14,\ h=20$

   - $$r=7,\ h=10$

   - $$r=14,\ h=10$

   _Explanation:_ The formula needs the radius and the vertical height, so halve 14 to get $r=7$ and keep $h=20$. The most common mistake is B, which uses the diameter as the radius and makes the volume far too large.

2. A solid hemisphere has radius 5 cm. What is its total surface area in terms of $\pi$?

   - $$50\pi \text{ cm}^2$

   - $$75\pi \text{ cm}^2$ ✔

   - $$100\pi \text{ cm}^2$

   - $$25\pi \text{ cm}^2$

   _Explanation:_ For a solid hemisphere, total surface area is $3\pi r^2$, so $3\pi \times 5^2 = 75\pi$. The most common mistake is selecting $50\pi$, which calculates only the curved part $2\pi r^2$ and forgets the flat circular base $\pi r^2$.

3. A sphere of radius 3 cm sinks fully into a rectangular tank with base 12 cm by 10 cm. What is the rise in water level, to 3 significant figures?

   - 0.300 cm

   - 0.942 cm ✔

   - 1.13 cm

   - 9.42 cm

   _Explanation:_ The sphere's volume is $V = \frac{4}{3}\pi \times 3^3 = 36\pi \text{ cm}^3$, and the tank base area is $12 \times 10 = 120 \text{ cm}^2$, so the rise is $36\pi/120 \approx 0.942 \text{ cm}$. The most common mistake is option A, which drops the $\pi$ from the sphere volume and uses $36/120$ instead.

4. A cube has side length 6 cm. A sphere has the same volume. What is the sphere's radius to 3 significant figures?

   - 3.72 cm ✔

   - 4.09 cm

   - 7.18 cm

   - 13.7 cm

   _Explanation:_ The cube volume is $6^3 = 216 \text{ cm}^3$, so solve $\frac{4}{3}\pi r^3 = 216$ to get $r^3 = \frac{162}{\pi}$ and $r \approx 3.72 \text{ cm}$. The most common mistake is B, which forgets the $\frac{4}{3}$ factor and uses $V = \pi r^3$ instead.
