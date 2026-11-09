# grade-7-7-11-finding-the-area-of-any-triangle — lesson

_Lane: `gcse-maths-edexcel` · grade 7 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## From base and height to sine

You already know that triangle area can be found with $A = \frac{1}{2}\times \text{base}\times \text{height}$. In this sketch, $CQ = a$ is the base and $CP = b$.

```text
         P
        /|
       / |
    b /  | h
     /   |
    /    |
   C-----D------Q
   <------ a ------>
```

Angle $C$ is between sides $a$ and $b$. Dropping a perpendicular from $P$ to the base at $D$ gives the height $PD = h$. In right triangle $CPD$, $\sin C = \frac{PD}{CP} = \frac{h}{b}$, so $h = b\sin C$. Substituting that into the usual area formula gives

$$$A = \frac{1}{2}ah = \frac{1}{2}a(b\sin C) = \frac{1}{2}ab\sin C$$

So when two sides and their included angle are known, use $A = \frac{1}{2}ab\sin C$. More generally, for any two sides $x$ and $y$ with included angle $\theta$, $A = \frac{1}{2}xy\sin\theta$. The angle in the formula must be the one directly between the two sides you choose. Area answers should be given in squared units such as $\text{cm}^2$ or $\text{m}^2$.

## Worked example: finding an area

A triangle has sides $14 \, \text{cm}$ and $11 \, \text{cm}$ with an included angle of $115^\circ$. Because the angle is between the given sides, the sine area formula works straight away.

Substitute into the formula. This simplifies to $A = 77\sin 115^\circ$.

$$$A = \frac{1}{2}\times 14\times 11\times \sin 115^\circ$$

In degree mode, this gives $A = 69.785\ldots$. Rounded to 1 decimal place, the area is $69.8 \, \text{cm}^2$.

## Working backwards to find an angle

![Acute and obtuse triangles with sides 12 cm and 15 cm showing angles 53.1 degrees and 126.9 degrees have the same sine value](../assets/001-f338103a-c159-48ea-9c4a-4cd48dfb5d4f.jpeg)

Sometimes the area and two sides are known, but the included angle is missing. Start from the same formula and rearrange until sine is on its own.

The key rearrangement is below. Once you have the sine value, use inverse sine on the calculator.

$$A = \frac{1}{2}ab\sin x$$

$$\sin x = \frac{2A}{ab}$$

A positive sine value can match both an acute angle and an obtuse angle because $\sin x = \sin(180^\circ - x)$. If the diagram shows an obtuse angle, use $180^\circ$ minus the calculator angle.

## Worked example: finding an obtuse angle

The triangle has area $72 \, \text{cm}^2$ and sides $12 \, \text{cm}$ and $15 \, \text{cm}$, with included angle $x$. Start by substituting into the formula.

$$$72 = \frac{1}{2}\times 12\times 15\times \sin x$$

Simplify to $72 = 90\sin x$, then divide by 90 to get $\sin x = 0.8$. Using inverse sine gives the calculator angle $53.130\ldots^{\circ}$.

Because the diagram says the included angle is obtuse, use $180^{\circ} - 53.130\ldots^{\circ} = 126.869\ldots^{\circ}$. So $x = 126.9^{\circ}$ to 1 decimal place.

## Algebraic sides and ratios

If side lengths contain algebra, use the same area formula and solve the resulting equation. For sides $x$ and $x+2$ with included angle 60° and area 12√3 cm², start with:

$$$12√3 = (1/2) × x(x+2) × sin(60°)$$

Use the exact value of the sine:

$$sin(60°) = √3 / 2$$

Then the equation becomes:

$$12√3 = x(x+2) × √3 / 4$$

So $x(x+2)=48$ and $x^2+2x-48=0$, giving the positive solution $x=6$.

Ratios are handled in the same way. If two sides are in the ratio $3:2$, write them as $3k$ and $2k$, solve for $k$, and then give the actual side length asked for.

## Check yourself

1. In $A = \frac{1}{2}ab\sin C$, what must $C$ be?

   - The angle directly between sides $a$ and $b$ ✔

   - Any angle in the triangle

   - The largest angle in the triangle

   - The angle opposite side $a$

   _Explanation:_ $$C$ must be the included angle because the formula comes from turning one side into a perpendicular height using sine. The most common wrong answer is "any angle", but a non-included angle does not create the correct height directly.

2. A calculator gives $x = \sin^{-1}(0.8)=53.1^{\circ}$. The triangle's included angle is marked obtuse. What is $x$ to 1 decimal place?

   - $$53.1^{\circ}$

   - $$126.9^{\circ}$ ✔

   - $$36.9^{\circ}$

   - $$233.1^{\circ}$

   _Explanation:_ The correct answer is $126.9^{\circ}$ because an obtuse angle with the same sine is found by $180^{\circ} - 53.1^{\circ}$. The most common wrong answer is $53.1^{\circ}$, but that is just the acute angle your calculator gives first. Hint: Supplementary angles have the same sine.

3. Two sides of a triangle meet at $30^\circ$. Their lengths are in the ratio $3:2$, and the area is $54 \, \text{cm}^2$. What is the shorter side?

   - $$6 \, \text{cm}$

   - $$12 \, \text{cm}$ ✔

   - $$18 \, \text{cm}$

   - $$24 \, \text{cm}$

   _Explanation:_ Let the sides be $3k$ and $2k$. Then $54 = \frac{1}{2}(3k)(2k)\sin 30^\circ = \frac{3}{2}k^2$, so $k=6$ and the shorter side is $2k=12 \, \text{cm}$. The most common wrong answer is $6 \, \text{cm}$, but 6 is the value of $k$, not the shorter side itself.
