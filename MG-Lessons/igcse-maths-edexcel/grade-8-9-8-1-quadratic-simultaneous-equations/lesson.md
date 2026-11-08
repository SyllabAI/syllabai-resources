# grade-8-9-8-1-quadratic-simultaneous-equations — lesson

_Lane: `igcse-maths-edexcel` · grade 8 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Line meets curve

![Coordinate graph of a circle centred at the origin and a line crossing it at two points labelled negative 3 comma negative 1 and 1 comma 3](../assets/001-c1ba8341-b0e7-46b6-bd16-008e802f37ee.jpeg)

Simultaneous equations are solved together, so each answer must satisfy both equations. With a quadratic and a line, you are usually finding the points where a straight line meets a curve.

On a graph, the intersections are the solutions, written as coordinate pairs such as $(x,y)$. A line can cut the curve twice, touch it once, or miss it completely, so quadratic simultaneous equations can have two, one, or no real solutions.

## The substitution method

Start by rearranging the linear equation so one variable is the subject, usually $y$ or $x$. Then replace that variable in the quadratic equation with a bracketed expression.

For example, if $x - y = 3$, write $y = x - 3$ first. Then $x^2 + y^2 = 29$ becomes $x^2 + (x - 3)^2 = 29$, and the brackets matter because the whole expression is squared.

After expanding and simplifying, solve the quadratic in one variable. Finally, substitute each root back into the linear equation to find the matching second coordinate and write answers as pairs.

Do not split or combine squares incorrectly. For example, $x^2 + y^2$ is not $(x + y)^2$, so careful substitution and expansion are essential.

## Worked example that factorises

Solve

$$
x^2 + y^2 = 10
$$

$$
y = x + 2
$$

Because the second equation already gives $y$, substitute it straight into the quadratic equation.

This gives

$$
x^2 + (x + 2)^2 = 10
$$

$$
x^2 + x^2 + 4x + 4 = 10
$$

Expand carefully before collecting like terms. Keep the bracket around $x + 2$ until after it has been squared.

Collect terms and simplify to

$$
2x^2 + 4x - 6 = 0
$$

$$
x^2 + 2x - 3 = 0
$$

Now factorise the quadratic. This gives

$$
(x + 3)(x - 1) = 0
$$

so $x = -3$ or $x = 1$.

Use the line equation to find the matching $y$-values. If $x = -3$, then $y = -1$, and if $x = 1$, then $y = 3$, so the solutions are $(-3,-1)$ and $(1,3)$.

## When the quadratic does not factorise nicely

Solve the following system of equations, giving your answers to 3 significant figures. We have a quadratic circle equation and a linear equation:

$$x^2 + y^2 = 18$$

$$2x + y = 4$$

First, rearrange the linear equation to $y = 4 - 2x$. Substitute this expression into the quadratic equation and expand the brackets to simplify into a standard form:

$$x^2 + (4 - 2x)^2 = 18$$

$$x^2 + 16 - 16x + 4x^2 = 18$$

$$5x^2 - 16x - 2 = 0$$

This equation does not factorise neatly, so we use the quadratic formula with $a = 5$, $b = -16$, and $c = -2$:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{16 \pm \sqrt{296}}{10}$$

This yields $x \approx 3.320465$ or $x \approx -0.120465$.

Substitute each $x$ value into $y = 4 - 2x$ to find $y \approx -2.64093$ or $y \approx 4.24093$. Rounded to 3 significant figures, the solutions are $(3.32, -2.64)$ and $(-0.120, 4.24)$. Note that the zero in $-0.120$ is significant because it follows a non-zero digit in a decimal.

## Stretch example with a minus sign and a fraction

Not every quadratic simultaneous equation is a circle. Solve the following equations algebraically:
$$
2x^2 - y^2 = 1
$$
$$
3x + 2y = 1
$$
First rearrange the linear equation to get $y = \frac{1 - 3x}{2}$.

Substitute this into the quadratic equation. Because of the fraction, multiplying through by 4 makes the algebra cleaner. This gives:
$$
2x^2 - \left(\frac{1 - 3x}{2}\right)^2 = 1
$$
$$
8x^2 - (1 - 3x)^2 = 4
$$

Now expand the square carefully. The minus sign in front applies to the whole bracket:
$$
8x^2 - (1 - 6x + 9x^2) = 4
$$
$$
-x^2 + 6x - 1 = 4
$$
Bring everything to one side and multiply by $-1$ to make the $x^2$ term positive, giving $x^2 - 6x + 5 = 0$.

Now factorise: $(x - 1)(x - 5) = 0$, which gives $x = 1$ or $x = 5$. Substitute back into $y = \frac{1 - 3x}{2}$ to find $y = -1$ or $y = -7$. The final solutions are $(1,-1)$ and $(5,-7)$.

## Check yourself

1. Why can a quadratic simultaneous equation have two coordinate-pair solutions?

   - Because a line can intersect a quadratic curve at two points ✔

   - Because a quadratic always gives two y-values for every x

   - Because you solve the linear equation first and stop

   - Because $x^2 + y^2$ can be rewritten as $(x + y)^2$

   _Explanation:_ A is correct because each solution is an intersection that satisfies both equations, and there can be two intersections. B is the common wrong choice, but it describes the quadratic on its own, not points that also lie on the line.

2. If a calculator gives $x \approx -0.120465$, how should this be written to 3 significant figures?

   - $$-0.12$

   - $$-0.120$ ✔

   - $$-0.121$

   - $$-0.100$

   _Explanation:_ B is correct because the first three significant digits are 1, 2 and 0, so the trailing zero must be kept. A is the common wrong choice because it gives only 2 significant figures, even though it has two decimal places.

3. After substitution, which result shows that there are no real coordinate-pair solutions?

   - The discriminant is negative ✔

   - The discriminant is positive

   - One root is zero

   - The line has been rearranged to make $y$ the subject

   _Explanation:_ A is correct because a negative discriminant means the quadratic formula would need the square root of a negative number, so there are no real intersection points. B is the common wrong choice, but a positive discriminant actually means two real roots.
