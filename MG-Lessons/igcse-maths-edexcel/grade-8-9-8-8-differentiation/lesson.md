# grade-8-9-8-8-differentiation — lesson

_Lane: `igcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Gradient and derivative

![Graph of a curve with an upward tangent labeled positive gradient, a horizontal tangent labeled stationary point, and a downward tangent labeled negative gradient](../assets/001-3830ca49-9f32-4e3a-8fe7-dcc9ab6ee391.jpeg)

The gradient of a straight line is constant, but the gradient of a curve changes from point to point. To find the gradient at one exact point, we draw a tangent and measure the gradient of that tangent.

The derivative, written $\frac{dy}{dx}$, tells you the gradient of the curve at each value of $x$. A positive derivative means the curve rises, a zero derivative means a horizontal tangent, and a negative derivative means the curve falls.

## The power rule

The power rule is the main rule you use at IGCSE: if $y = ax^n$, then $\frac{dy}{dx} = anx^{n-1}$. To apply this, multiply the coefficient by the current power and then reduce the exponent by 1.

Differentiate $y = 5x^4 - 3x^2 + 7x - 11$ term by term. Each term is handled separately before the results are combined:
$$5x^4 \to 20x^3, \qquad -3x^2 \to -6x, \qquad 7x \to 7, \qquad -11 \to 0$$

So the derivative is
$$\frac{dy}{dx} = 20x^3 - 6x + 7$$
A constant term disappears during differentiation because its gradient is always zero.

## Reciprocal terms

Reciprocal terms are easiest if you rewrite them with negative powers first. For example, $\frac{1}{x} = x^{-1}$ and $\frac{3}{x} = 3x^{-1}$.

Differentiate $y = 4x^2 + \frac{1}{x}$ by first writing $y = 4x^2 + x^{-1}$. Then apply the power rule to both terms.

$$$\frac{dy}{dx} = 8x - x^{-2} = 8x - \frac{1}{x^2}$$

A negative power does not mean the term is negative. It means the term belongs in the denominator, so $x^{-2} = \frac{1}{x^2}$.

## Worked example: finding a stationary point

A stationary point happens when the gradient is zero, so we solve $\frac{dy}{dx} = 0$. For the function $y = 4x^2 + \frac{1}{x}$, we first find the derivative: $$\frac{dy}{dx} = 8x - \frac{1}{x^2}$$

Next, set the derivative to zero and solve for $x$. Multiply by $x^2$ to clear the fraction and simplify the resulting cubic equation: $$8x - \frac{1}{x^2} = 0 \Rightarrow 8x^3 - 1 = 0 \Rightarrow x^3 = \frac{1}{8} \Rightarrow x = \frac{1}{2}$$

Finally, substitute $x = \frac{1}{2}$ into the original equation, not the derivative, to find the $y$-coordinate: $$y = 4\left(\frac{1}{2}\right)^2 + \frac{1}{\frac{1}{2}} = 1 + 2 = 3$$ Therefore, the stationary point is $\left(\frac{1}{2}, 3\right)$.

## Where a curve has negative gradient

To find where a curve has negative gradient, differentiate and solve $\frac{dy}{dx} < 0$. For the function $y = x^3 - 3x^2 - 9x + 6$, we first calculate the derivative:

$$$\frac{dy}{dx} = 3x^2 - 6x - 9$$

Next, we solve the inequality $3x^2 - 6x - 9 < 0$. Factorising the quadratic reveals its roots, and since the $x^2$ coefficient is positive, the graph opens upwards:

$$$3x^2 - 6x - 9 < 0 \Rightarrow 3(x - 3)(x + 1) < 0$$

The solution to the inequality is $-1 < x < 3$. The endpoints are excluded from the result because the gradient is exactly zero at those specific points.

## Differentiation in motion

In motion questions, displacement is usually $s$, velocity is usually $v$, and acceleration is usually $a$. If $s$ is given in terms of time $t$, then $v = \frac{ds}{dt}$ and $a = \frac{dv}{dt}$.

For $s = t^3 - 4t^2 - 3t + 6$, differentiate once to get velocity. A particle is instantaneously at rest when $v = 0$. $$v = 3t^2 - 8t - 3$$

So solve $$3t^2 - 8t - 3 = 0 \Rightarrow (3t + 1)(t - 3) = 0$$ giving $t = -\frac{1}{3}$ or $t = 3$. If $t \ge 0$, only $t = 3$ is valid, and differentiating again gives $$a = 6t - 8$$

## Check yourself

1. What does $\frac{dy}{dx}$ tell you at a point on a curve?

   - The gradient of the tangent at that point ✔

   - The $y$-coordinate of the point

   - The average gradient between two different points

   - The area under the curve

   _Explanation:_ The derivative at a point is the gradient of the tangent at that point, so A is correct. A common mistake is C, but that is an average gradient between two points, not the instantaneous gradient at one point. Hint: Think about what a tangent tells you.

2. Differentiate $y = 2x^3 + \frac{3}{x}$.

   - $$6x^2 + \frac{3}{x^2}$

   - $$6x^2 - \frac{3}{x^2}$ ✔

   - $$6x - \frac{3}{x^2}$

   - $$6x^2 - \frac{3}{x}$

   _Explanation:_ Rewrite $\frac{3}{x}$ as $3x^{-1}$, so its derivative is $-3x^{-2} = -\frac{3}{x^2}$. A common mistake is option A, which forgets that differentiating $x^{-1}$ gives a negative sign.

3. Stretch: If $\frac{dy}{dx} = (x-4)(x+2)$, for which values of $x$ is the gradient negative?

   - $$x < -2$ or $x > 4$

   - $$-2 < x < 4$ ✔

   - $$x \le -2$ or $x \ge 4$

   - $$x = -2$ or $x = 4$

   _Explanation:_ The roots are $x = -2$ and $x = 4$, and the positive coefficient means the quadratic is below the axis between the roots, so the gradient is negative on $-2 < x < 4$. A common mistake is A, which would be true for a downward-opening quadratic, and the endpoints are excluded because there the gradient is zero.
