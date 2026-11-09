# grade-4-4-9-pythagoras — lesson

_Lane: `igcse-maths-edexcel` · grade 4 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Right-angled triangles and the hypotenuse

![Labelled right-angled triangle with sides a and b as shorter sides and side c as the hypotenuse opposite the right angle](../assets/001-cf895e71-50a3-42fb-a212-0757350f4f2c.jpeg)

Pythagoras' theorem only works in a right-angled triangle. The hypotenuse is opposite the right angle. It is always the longest side.

If the shorter sides are $a$ and $b$ and the hypotenuse is $c$, then:
$$
c^2 = a^2 + b^2
$$
This is the key formula you will use.

Before substituting numbers, mark the $90^\circ$ angle and identify $c$ first. Do not choose the hypotenuse just because it looks longest; it must be opposite the right angle.

## When to add and when to subtract

If the missing side is the hypotenuse, add the squares of the two shorter sides. Then take a square root at the end.

For a missing hypotenuse $x$, write:
$$
x^2 = a^2 + b^2
$$
The answer should come out longer than either shorter side.

If the missing side is one of the shorter sides, subtract the known shorter side square from the hypotenuse square. The hypotenuse square is always the biggest square in the equation.

For a missing shorter side $x$, write:
$$
x^2 = c^2 - a^2
$$
Square first, then subtract, so use $15^2 - 8^2$, not $(15 - 8)^2$.

## Worked example: finding the hypotenuse

A right-angled triangle has shorter sides 7.2 cm and 9.6 cm. Let the hypotenuse be $x$. Because $x$ is opposite the right angle, it is the hypotenuse. That means we add the squares of the shorter sides:

$$$x^2 = 7.2^2 + 9.6^2$$
Now square each number and add:
$$x^2 = 51.84 + 92.16 = 144$$
This gives an exact square, which makes the last step simple.

Take the square root to find the side itself:
$$x = \sqrt{144} = 12$$
So the hypotenuse is $12 \, \text{cm}$, which is longer than both shorter sides.

## Worked example: finding a shorter side

A right-angled triangle has hypotenuse 15 cm and one shorter side 8 cm. Let the missing shorter side be $x$. Start with Pythagoras and then rearrange because $x$ is not the hypotenuse:

$$$15^2 = 8^2 + x^2$$ So we need to subtract $8^2$ from $15^2$. Now calculate the square difference:

$$$x^2 = 15^2 - 8^2 = 225 - 64 = 161$$ Square first, then subtract, not the other way around. Take the square root at the end:

$$$x = \sqrt{161} = 12.688\ldots$$ So the missing side is $12.7 \, \text{cm}$ to 1 decimal place.

## Spotting hidden right-angled triangles

![Composite diagram](../assets/002-6688d39e-ca69-4fae-923d-71b5f2b18044.jpeg)

Many questions hide a right-angled triangle inside a bigger shape. Look for diagonals, heights, and wall-floor corners.

In a rectangle, the diagonal is the hypotenuse. In an isosceles triangle, drawing the height from the top vertex bisects the base and makes two right-angled triangles.

A ladder against a wall forms a right-angled triangle. Convert units first, for example: 80 cm = 0.8 m.

## A two-step Pythagoras problem

Some questions need Pythagoras twice. First find a shared side, then use it in a second right-angled triangle.

In the first triangle, the hypotenuse is $20 \, \text{m}$ and one shorter side is $12 \, \text{m}$. If the shared side is $s$, then: $$s^2 = 20^2 - 12^2 = 400 - 144 = 256$$

So $s = \sqrt{256} = 16$. In the second triangle, use $16 \, \text{m}$ and $9 \, \text{m}$ as the shorter sides: $$x^2 = 16^2 + 9^2 = 337$$

Finally, $$x = \sqrt{337} = 18.357\ldots$$ so the final hypotenuse is $18.4 \, \text{m}$ to 3 significant figures. Keep the unrounded calculator value until the last step.

## Check yourself

1. Which statement correctly identifies the hypotenuse?

   - It is the side opposite the right angle ✔

   - It is the side that looks longest

   - It is any side touching the right angle

   - It is the shortest side

   _Explanation:_ The hypotenuse is defined by position, so A is correct because it is opposite the $90^\circ$ angle. Option B is a common mistake because a drawing can be misleading; you must find the right angle first, not guess by appearance.

2. A right-angled triangle has shorter sides 5 cm and 12 cm. What is the hypotenuse?

   - 13 cm ✔

   - 17 cm

   - 169 cm

   - 7 cm

   _Explanation:_ Use $c^2 = 5^2 + 12^2 = 25 + 144 = 169$, so $c = \sqrt{169} = 13$. Option B is the common mistake of adding $5 + 12$ instead of adding the squares and then square-rooting.

3. An isosceles triangle has equal sides 13 cm and base 10 cm. What is the perpendicular height?

   - 12 cm ✔

   - 8.3 cm

   - 5 cm

   - 18 cm

   _Explanation:_ The height splits the 10 cm base into two 5 cm halves, so $h^2 = 13^2 - 5^2 = 169 - 25 = 144$ and $h = 12$. Option B is the common mistake from using the whole base 10 instead of halving it first.

4. A rectangle has side lengths in the ratio $3:4$ and a diagonal of 10 cm. What is the longer side?

   - 6 cm

   - 8 cm ✔

   - 10 cm

   - 12 cm

   _Explanation:_ Let the sides be $3k$ and $4k$. Then $10^2 = (3k)^2 + (4k)^2 = 25k^2$, so $5k = 10$ and $k = 2$, giving longer side $4k = 8$. Option A is the common mistake of finding the shorter side $3k$ and stopping there.
