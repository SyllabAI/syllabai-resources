# as-pure-mathematics-12-differentiation — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## From gradient to derivative

![Curve on axes with tangent at point P, a rise-run triangle, and gradient dy/dx marked at x=a](../assets/001-39edcf0e-436c-421a-9d63-d90a5eeadb55.jpeg)
A straight line has one constant gradient, but a curve can have a different gradient at each point. To get the gradient at one point on a curve, we draw the tangent there.

The derivative is the rule that gives this gradient for every value of $x$. We write it as $\frac{dy}{dx}$ or $f'(x)$, and to differentiate means to find this derivative.

If $\frac{dy}{dx} > 0$, the curve is rising, and if $\frac{dy}{dx} < 0$, it is falling. If $\frac{dy}{dx} = 0$, the tangent is horizontal and the point is stationary.

## The power rule

Most AS differentiation starts with powers of $x$. For $ax^n$, multiply by the old power and then reduce the power by 1.

$$$\frac{d}{dx}(ax^n)=anx^{n-1}$$

A constant differentiates to 0, so a term like $-8$ disappears. Work term by term, and do not substitute an $x$-value until after differentiating.

For $y=3x^3-4x^2+6x-8$, the derivative is $$\frac{dy}{dx}=9x^2-8x+6$$ When $x=2$, the gradient is $9(2)^2-8(2)+6=36-16+6=26$.

## Roots, fractions, and second derivatives

The power rule works best when everything is written as a power of $x$. Useful rewrites are $\sqrt{x}=x^{1/2}$, $\frac{1}{x}=x^{-1}$, and $\frac{1}{x^{2}}=x^{-2}$.

For $y=6\sqrt{x}+\frac{4}{x}+7$, first rewrite the function as $y=6x^{1/2}+4x^{-1}+7$. Then differentiate once:
$$\frac{dy}{dx}=3x^{-1/2}-4x^{-2}$$

Differentiate again to get the second derivative:
$$\frac{d^{2}y}{dx^{2}}=-\frac{3}{2}x^{-3/2}+8x^{-3}$$
Negative powers are usually fine unless the question asks for fractions.

## Stationary points and their nature

![Cubic curve with stationary points labelled at (1,6) and (3,2), showing where the curve increases and decreases](../assets/002-1553a1c5-6bef-4dac-bb71-4690865bc98c.jpeg)
Stationary points happen where $\frac{dy}{dx}=0$. A positive derivative means the function is increasing, and a negative derivative means it is decreasing.

For the curve $y=x^3-6x^2+9x+2$, we find the stationary points by differentiating and factoring the result:
$$
\frac{dy}{dx}=3x^2-12x+9=3(x-1)(x-3)
$$
Setting $\frac{dy}{dx}=0$ gives the x-coordinates $x=1$ and $x=3$.

Next, we find the corresponding $y$-coordinates by substituting $x$ back into the original equation:
$$
y(1)=1-6+9+2=6,\qquad y(3)=27-54+27+2=2
$$
So the stationary points are located at $(1,6)$ and $(3,2)$.

To determine their nature, we differentiate again to find the second derivative:
$$
\frac{d^2y}{dx^2}=6x-12
$$
At $x=1$, $\frac{d^2y}{dx^2} = -6 < 0$, so $(1,6)$ is a local maximum. At $x=3$, $\frac{d^2y}{dx^2} = 6 > 0$, so $(3,2)$ is a local minimum.

## Tangents and normals

A tangent has the same gradient as the curve at a point. A normal is perpendicular to the tangent, so if the tangent gradient is $m$, the normal gradient is $-\frac{1}{m}$.

Use the line formula $y-b=m(x-a)$ once you know a point and a gradient. If the tangent gradient is $0$, the normal is vertical and has the equation $x=a$.

For $y=\frac{(2x+1)(x-3)}{x}$ at $x=-1$, first simplify the expression to $y=2x-5-3x^{-1}$ and differentiate: $$\frac{dy}{dx}=2+3x^{-2}$$

At $x=-1$, the tangent gradient is $2+3(-1)^{-2}=5$ and the $y$-coordinate is $y(-1)=-4$. The normal gradient is $-\frac{1}{5}$, giving $y+4=-\frac{1}{5}(x+1)$, which simplifies to $x+5y+21=0$.

## Optimisation with differentiation

Optimisation means finding the maximum or minimum value of a quantity. To do this, first write the quantity as a function of one variable, then differentiate and solve where the derivative is 0.

For $C=\frac{3200}{v}+2v+15$, rewrite as $C=3200v^{-1}+2v+15$ and differentiate:
$$\frac{dC}{dv}=-3200v^{-2}+2$$
Set this equal to 0 to find the turning point.

Solving gives
$$-\frac{3200}{v^2}+2=0 \Rightarrow v^2=1600 \Rightarrow v=40$$
We keep the positive root because speed cannot be negative.

Check with the second derivative:
$$\frac{d^2C}{dv^2}=6400v^{-3}$$
At $v=40$, this is positive, so the cost is a minimum. The minimum cost is $C=\frac{3200}{40}+2(40)+15=175$.

## Check yourself

1. Which statement best describes $\frac{dy}{dx}$ for $y=f(x)$?

   - The gradient of the curve at each value of $x$ ✔

   - The y-coordinate of the curve at each value of $x$

   - The average gradient between two points on the curve

   - The gradient of the normal at each value of $x$

   _Explanation:_ A is right because the derivative gives the instantaneous gradient of the curve at each value of $x$. The common wrong answer C is the average gradient between two points, which is a secant gradient, not the gradient at one point.

2. If $y=2\sqrt{x}+\frac{3}{x}$, what is $\frac{dy}{dx}$?

   - $$x^{-1/2}-3x^{-2}$ ✔

   - $$x^{-1/2}+3x^{-2}$

   - $$2x^{-1/2}-3x^{-1}$

   - $$x^{1/2}-3x^{-2}$

   _Explanation:_ A is right because $2x^{1/2}$ differentiates to $x^{-1/2}$ and $3x^{-1}$ differentiates to $-3x^{-2}$. The common wrong answer B forgets that differentiating $x^{-1}$ introduces a negative sign.

3. At the point $x=4$, a curve has tangent gradient 0. What is the equation of the normal?

   - $$y=4$

   - $$x=4$ ✔

   - $$y=0$

   - $$x=0$

   _Explanation:_ B is right because a tangent with gradient 0 is horizontal, so the perpendicular normal is vertical and has equation $x=4$. The common wrong answer A is another horizontal line, so it is not perpendicular to the tangent.

4. For $v>0$, a cost model is $C=\frac{1800}{v}+3v+30$. What speed minimises $C$?

   - $$10\sqrt{6}$ ✔

   - $$20\sqrt{6}$

   - $$10\sqrt{3}$

   - $$30$

   _Explanation:_ A is right because $\frac{dC}{dv}=-1800v^{-2}+3$, and setting this to 0 gives $v^2=600$, so $v=10\sqrt{6}$ for $v>0$. The common wrong answer D copies the earlier case with coefficient 2, but here the coefficient 3 changes the stationary value.
