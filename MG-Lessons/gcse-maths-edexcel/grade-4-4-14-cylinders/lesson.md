# grade-4-4-14-cylinders — lesson

_Lane: `gcse-maths-edexcel` · grade 4 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Parts and circle facts

![Labelled cylinder showing radius, diameter, height, and the curved surface unwrapped into a rectangle of width 2πr and height h](../assets/001-d6ccbc59-7493-45ea-8da6-837e6add5cfa.jpeg)

A cylinder is a 3D solid with two equal, parallel circular faces and one curved surface. The key measurements are radius $r$, diameter $d$, and height $h$, with $d = 2r$.

Two circle facts come up again and again: area $A = \pi r^2$ and circumference $C = 2\pi r$. If the question gives the diameter, halve it before substituting into any cylinder formula.

The curved surface can be unwrapped into a rectangle. Its width is the circumference $2\pi r$ and its height is $h$, which is why surface area involves $2\pi rh$.

## Volume of a cylinder

Volume tells you how much space is inside the cylinder, so the units are cubic. The formula is the area of the circular base multiplied by the height:
$$V = \pi r^2h$$

Example: a cylinder has diameter $8 \, \text{cm}$ and height $13 \, \text{cm}$. First find the radius, then substitute:
$$r = 8 \div 2 = 4 \, \text{cm}$$
$$V = \pi \times 4^2 \times 13 = 208\pi \, \text{cm}^3$$

If a decimal is required, only round on the final line. Here
$$208\pi = 653.451\ldots$$
so the volume is $653.5 \, \text{cm}^3$ to 1 decimal place, or $208\pi \, \text{cm}^3$ in terms of $\pi$.

## Total surface area of a closed cylinder

Surface area is the total area on the outside of a solid. For a closed cylinder, we calculate this by adding the areas of the top circle, the bottom circle, and the curved side surface.

The two circles provide $2\pi r^2$, while the curved side area is the circumference multiplied by height, $2\pi rh$. This results in the following formula: $$\text{TSA} = 2\pi r^2 + 2\pi rh$$

Consider a cylinder with diameter $10 \, \text{cm}$ ($r=5$) and height $14 \, \text{cm}$. The calculation for total surface area is as follows: $$\text{TSA} = 2\pi \times 5^2 + 2\pi \times 5 \times 14 = 50\pi + 140\pi = 190\pi \, \text{cm}^2$$

This results in approximately $596.902$, or $597 \, \text{cm}^2$ when rounded to 3 significant figures. Remember that you only omit a circle's area if the problem specifically states the cylinder is open.

## Half-cylinders

![Semi-cylinder cut lengthways with radius, diameter, length, half curved surface, two semi-circular ends, and flat rectangular face labelled](../assets/002-23e98fae-c124-4865-a75f-f732257e65e3.jpeg)

A semi-cylinder is half a cylinder cut lengthways. If the length is $L$, its volume is half the usual cylinder volume:

$$$V = \frac{1}{2}\pi r^2L$$

Surface area is more careful because there are three outside parts. The half-curved surface is $\pi rL$, the two semi-circular ends make one full circle area $\pi r^2$, and the cut face is a rectangle of area $2rL$.

$$$\text{TSA} = \pi rL + \pi r^2 + 2rL$$

The flat rectangle $2rL$ is the part students most often forget.

## Working backwards

Sometimes you are given the volume and must find a missing radius or height. Use $V = \pi r^2h$, substitute what you know, and solve step by step.

Example: a cylinder has volume $490\pi \, \text{m}^3$ and height $10 \, \text{m}$. To find the radius, start with this equation: $$490\pi = \pi r^2 \times 10$$

Dividing by $10\pi$ isolates $r^2$, resulting in $r^2 = 49$. Then square root both sides to find the final value: $$r = 7 \, \text{m}$$

If you stop at $r^2 = 49$, you have not found the radius yet. Always perform that final square root calculation to finish the problem.

## Units, paint and filling

In real life, filling questions usually require calculating volume, while painting questions usually require surface area. Always ensure every length measurement is in the same unit before you begin your calculations, and keep in mind that $1 \, \text{litre} = 1000 \, \text{cm}^3$.

Consider an example with 4 closed tanks, each with a diameter of $50 \, \text{cm}$ and a height of $1.5 \, \text{m}$. First, convert $50 \, \text{cm}$ to $0.5 \, \text{m}$ to get a radius of $0.25 \, \text{m}$. Since the tanks are closed, we must include both circular ends in the surface area:
$$\text{TSA} = 2\pi(0.25)^2 + 2\pi(0.25)(1.5) = 0.875\pi \, \text{m}^2 = 2.748\ldots \, \text{m}^2$$

For 4 tanks, the total area is $4 \times 2.748\ldots = 10.995\ldots \, \text{m}^2$. If one pot of paint covers $3 \, \text{m}^2$, we calculate the number of pots needed:
$$10.995\ldots \, \text{m}^2 \div 3 \, \text{m}^2/\text{pot} = 3.665\ldots \, \text{pots}$$
Since 3 pots are not enough to finish the job, you must round up to 4 pots.

## Check yourself

1. A cylinder has diameter 14 cm. What radius should you use in the formula?

   - 7 cm ✔

   - 14 cm

   - 28 cm

   - 49 cm

   _Explanation:_ A is correct because the radius is half the diameter, so $14 \div 2 = 7$. The most common wrong answer is B, which uses the diameter directly and would make the final volume or surface area much too large.

2. Which expression gives the total surface area of a closed cylinder with radius 3 cm and height 8 cm?

   - $$2\pi \times 3^2 + 2\pi \times 3 \times 8$ ✔

   - $$\pi \times 3^2 \times 8$

   - $$2\pi \times 3^2 + \pi \times 3 \times 8$

   - $$2\pi \times 6 \times 8$

   _Explanation:_ A is correct because total surface area is two circles plus the curved side, so $2\pi r^2 + 2\pi rh$. The most common wrong answer is B, which is the volume formula and measures the space inside the cylinder, not the area on the outside.

3. A semi-cylinder has radius 4 cm and length 12 cm. What is its total surface area?

   - $$(64\pi + 96) \, \text{cm}^2$ ✔

   - $$(48\pi + 96) \, \text{cm}^2$

   - $$64\pi \, \text{cm}^2$

   - $$96\pi \, \text{cm}^2$

   _Explanation:_ A is correct because the half-curved surface is $48\pi$, the two semi-circular ends make $16\pi$, and the flat rectangle is $8 \times 12 = 96$, giving $64\pi + 96$. The most common wrong answer is C, which forgets the flat rectangular face created by the cut.
