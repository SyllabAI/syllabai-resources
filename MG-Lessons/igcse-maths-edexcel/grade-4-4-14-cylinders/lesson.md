# grade-4-4-14-cylinders — lesson

_Lane: `igcse-maths-edexcel` · grade 4 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Cylinder basics

A cylinder is a 3D shape with two equal, parallel circular faces joined by one curved surface. The key measurements are radius $r$, diameter $d$, and height $h$.

If a question gives the diameter, halve it before using any formula with $r$. For circles, $d = 2r$, area $A = \pi r^2$, and circumference $C = 2\pi r$.

These circle facts feed directly into cylinder formulas. Volume is measured in cubic units such as $cm^3$, while surface area is measured in square units such as $cm^2$.

## Volume of a cylinder

Volume tells you how much space is inside the cylinder. It is the area of the circular base multiplied by the height, using the formula:

$$V = \pi r^2h$$

For example, consider a cylinder with a diameter of $8$ cm and a height of $11.5$ cm. First, we calculate the radius by dividing the diameter by two:

$$r = \frac{8}{2} = 4$$

Now substitute the radius and height into the volume formula:

$$V = \pi \times 4^2 \times 11.5 = 184\pi$$

If a decimal is needed, $184\pi \approx 578.053$, so the volume is $578.1$ cm³ to 1 decimal place.

If the question asks for the answer in terms of $\pi$, stop at $184\pi$ cm³. Do not turn $\pi$ into a decimal unless the question specifically asks you to.

## Total surface area from the net

![Net of a closed cylinder showing two circles and a rectangle with width 2πr and height h](../assets/001-56109000-5866-493f-8b8e-7e22c720d9ec.jpeg)

A closed cylinder can be opened into a net with two circles and one rectangle. The rectangle has height $h$ and width equal to the circumference, so its width is $2\pi r$.

So the total surface area of a closed cylinder is

$$\text{TSA} = 2\pi r^2 + 2\pi rh$$

The first part is the two circular ends, and the second part is the curved surface.

Example: if $r = 3$ cm and $h = 9.5$ cm, then

$$\text{TSA} = 2\pi \times 3^2 + 2\pi \times 3 \times 9.5 = 18\pi + 57\pi = 75\pi$$

So the total surface area is $75\pi$ cm², which is about $235.6$ cm².

If the cylinder is open at the top or bottom, leave out that missing circle. Always check whether the shape is closed before choosing the formula.

## Semi-cylinders and combined solids

![Semi-cylinder showing half curved surface, flat rectangular face, two semicircular ends, radius r, and length L](../assets/002-1bac3859-ff71-447e-b3c4-7c4f7b7d50cc.jpeg)

A semi-cylinder is half of a cylinder cut lengthways. For volume, take half the full-cylinder formula, so:

$$V = \frac{1}{2}\pi r^2L$$

where $L$ is the length.

For surface area, count every exposed face carefully. You need half the curved surface, the flat rectangular face, and two semicircular ends, so:

$$\text{TSA} = \pi rL + 2rL + \pi r^2$$

If $r = 10$ cm and $L = 40$ cm, then the volume is calculated as:

$$V = \frac{1}{2}\pi \times 10^2 \times 40 = 2000\pi$$

Thus, the volume is about $6.28 \times 10^3$ cm³.

For the same semi-cylinder, the total surface area is:

$$\text{TSA} = \pi \times 10 \times 40 + 2 \times 10 \times 40 + \pi \times 10^2 = 500\pi + 800$$

This results in a total surface area of about $2.37 \times 10^3$ cm². For a combined solid, split it into simple parts and add the volumes.

## Working backwards

Sometimes you are given the volume or surface area and must find a missing radius or height. Write the formula first, substitute the known values, and then solve the equation step by step.

Example: a cylinder has volume $288\pi$ m³ and height $8$ m. Start with
$$V = \pi r^2h$$
so
$$288\pi = \pi r^2 \times 8$$

Now divide by $\pi$ to simplify the equation:
$$288 = 8r^2$$
Then divide by $8$ to get $r^2 = 36$.

Finally, take the positive square root:
$$r = 6$$
Use the positive value because a radius cannot be negative.

## Units, litres, and practical answers

Practical questions often mix units, so convert before substituting. Two useful facts are $1\,\text{m} = 100\,\text{cm}$ and $1\,\text{L} = 1000\,\text{cm}^3$.

Example: a cylindrical tank has radius $10$ cm and height $60$ cm. Its volume is $$V = \pi \times 10^2 \times 60 = 6000\pi$$ so the tank holds $6000\pi\,\text{cm}^3$.

To change $\text{cm}^3$ into litres, use a conversion factor: $$6000\pi\,\text{cm}^3 \times \frac{1\,\text{L}}{1000\,\text{cm}^3} = 6\pi\,\text{L}$$ The $\text{cm}^3$ units cancel, leaving litres.

At $1.5$ L per minute, the filling time is $6\pi \div 1.5 \approx 12.6$ minutes. To the nearest minute, the tank fills in $13$ minutes.

## Check yourself

1. A cylinder has diameter 12 cm. What radius should you use in $V = \pi r^2h$?

   - 6 cm ✔

   - 12 cm

   - 24 cm

   - 3 cm

   _Explanation:_ The radius is half the diameter, so $r = 12 \div 2 = 6$ cm. The most common wrong answer is 12 cm because it uses the diameter directly in a formula that needs the radius.

2. A closed cylinder has radius 5 cm and height 13 cm. What is its total surface area in terms of $\pi$?

   - $$180\pi$ cm² ✔

   - $$155\pi$ cm²

   - $$130\pi$ cm²

   - $$50\pi$ cm²

   _Explanation:_ For a closed cylinder, $\text{TSA} = 2\pi r^2 + 2\pi rh = 2\pi \times 5^2 + 2\pi \times 5 \times 13 = 50\pi + 130\pi = 180\pi$ cm². The most common wrong answer is $155\pi$ cm² because it includes only one circular end instead of two.

3. A solid is made from a cuboid of volume $108$ $m^3$ and a half-cylinder of volume $18\pi$ $m^3$ on top. What is the total volume to 3 significant figures?

   - $$126$ $m^3$

   - $$165$ $m^3$ ✔

   - $$164.5$ $m^3$

   - $$56.5$ $m^3$

   _Explanation:_ Add the two volumes first: $108 + 18\pi \approx 164.549$. Rounded to 3 significant figures, this is $165$ $m^3$. The most common wrong answer is $126$ $m^3$ because it treats $18\pi$ as just 18 and forgets the factor of $\pi$. Hint: Work with the exact value $108 + 18\pi$ before rounding.

4. Four closed cylindrical tanks each have diameter $50$ cm and height $1.2$ m. One pot of paint covers $3$ m². How many pots are needed?

   - 3

   - 4 ✔

   - 9

   - 10

   _Explanation:_ Convert $50$ cm to $0.5$ m, so the radius is $0.25$ m. One tank has surface area about $2.278$ m², so four tanks need about $9.112$ m². Then $9.112 \div 3 \approx 3.037$, so you must buy 4 pots. The most common wrong answer is 3 because practical buying questions must round up, not down.
