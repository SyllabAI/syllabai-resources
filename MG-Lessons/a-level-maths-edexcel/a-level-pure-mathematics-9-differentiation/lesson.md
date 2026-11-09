# a-level-pure-mathematics-9-differentiation — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 4 check questions (source: MathsGenie lessons)_

## Gradient at a point

A straight line has a constant gradient, but a curve changes gradient from point to point. The derivative, written $\frac{dy}{dx}$ or $f'(x)$, gives the gradient of the tangent at a chosen point.

![Graph of a parabola with a secant line and a tangent line](../assets/001-9af3b0c0-3871-4cf8-8dbe-b04b1d615676.jpeg)

From first principles, the derivative is defined by the following limit formula:
$$
f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
$$
This process starts with the gradient of a secant and lets the gap shrink to zero until the secant becomes a tangent.

For $f(x)=x^2+5x$, we first form and simplify the difference quotient:
$$
\frac{f(x+h)-f(x)}{h} = \frac{x^2+2xh+h^2+5x+5h-(x^2+5x)}{h} = 2x+h+5
$$
By letting $h\to 0$, the remaining $h$ term disappears, giving the derivative $f'(x)=2x+5$.

## Power rule and standard results

Before differentiating, rewrite roots and fractions as powers, such as $\sqrt{x}=x^{\frac{1}{2}}$ and $\frac{1}{x^2}=x^{-2}$. This puts the function in a form where the power rule works directly.

The key rule is $$\frac{d}{dx}(x^n)=nx^{n-1}$$ and other standard results include $\frac{d}{dx}(e^x)=e^x$, $\frac{d}{dx}(\ln x)=\frac{1}{x}$, $\frac{d}{dx}(\sin x)=\cos x$, and $\frac{d}{dx}(\cos x)=-\sin x$. For trigonometric functions, angles must be in radians.

As a quick example, if $y=3x^4-2x^{-2}+x^{\frac{1}{2}}$, then differentiate term by term to get $$\frac{dy}{dx}=12x^3+4x^{-3}+\frac{1}{2}x^{-\frac{1}{2}}$$ This same idea also lets you find second derivatives by differentiating again.

## Chain rule for composite functions

A composite function is a function inside another function, such as $(x^2+4)^3$ or $e^{x^2}$. The chain rule says differentiate the outside, keep the inside unchanged, then multiply by the derivative of the inside: $$\frac{dy}{dx}=f'(g(x))g'(x)$$

For $y=(x^2+4)^3$, the outside function is "cube" and the inside is $x^2+4$. So: $$\frac{dy}{dx}=3(x^2+4)^2\cdot 2x=6x(x^2+4)^2$$

For $z=e^{x^2}$, the outside derivative stays exponential, but the inside $x^2$ contributes another factor of $2x$. That is why: $$\frac{dz}{dx}=e^{x^2}\cdot 2x=2xe^{x^2}$$

## Product rule and quotient rule

Use the product rule when two expressions involving $x$ are multiplied, and the quotient rule when one is divided by another. The rules are
$$\frac{d}{dx}(uv)=u'v+uv'$$
and
$$\frac{d}{dx}\left(\frac{u}{v}\right)=\frac{u'v-uv'}{v^2}$$

For $y=2xe^x$, let $u=2x$ and $v=e^x$. Then $u'=2$ and $v'=e^x$, so the derivative is calculated as follows:
$$\frac{dy}{dx}=2e^x+2xe^x=2e^x(x+1)$$
This result is found by substituting our values into the product rule formula.

For $z=\frac{\ln(x^2+1)}{2x+3}$, let $u=\ln(x^2+1)$ and $v=2x+3$. Then $u'=\frac{2x}{x^2+1}$ and $v'=2$, so the quotient rule gives:
$$\frac{dz}{dx}=\frac{\frac{2x}{x^2+1}(2x+3)-2\ln(x^2+1)}{(2x+3)^2}$$
Note how the denominator $v^2$ is simply the original denominator squared.

## Tangents and normals

A tangent has the same gradient as the curve at a point, while a normal is perpendicular to the tangent. Once you know a point $(x_1,y_1)$ and gradient $m$, use the straight-line form $y-y_1=m(x-x_1)$.

For $y=\frac{4}{2x+1}$ at $x=1$, first find the point $P=\left(1,\frac{4}{3}\right)$. Rewrite the function as $y=4(2x+1)^{-1}$, then find the derivative:
$$\frac{dy}{dx}=4(-1)(2x+1)^{-2}\cdot 2=-\frac{8}{(2x+1)^2}$$

At $x=1$, the tangent gradient is $-\frac{8}{9}$, so the normal gradient is its negative reciprocal, $\frac{9}{8}$. The normal equation is therefore:
$$y-\frac{4}{3}=\frac{9}{8}(x-1)$$

## Stationary points and their nature

![Three sketches showing a local maximum, a local minimum, and a stationary point of inflection, each with a horizontal tangent](../assets/002-73ed1e91-89c5-42cd-ab86-d55430e95ee6.jpeg)
A stationary point occurs where $\frac{dy}{dx}=0$, so the tangent is horizontal. To classify it, use the second derivative: if $y''>0$ it is a local minimum, if $y''<0$ it is a local maximum, and if $y''=0$ you need a sign test on $\frac{dy}{dx}$.

For $y=x^3-3x^2+2$, first differentiate: $y'=3x^2-6x=3x(x-2)$. So the stationary points occur at $x=0$ and $x=2$.

Differentiate again to get $y''=6x-6$. At $x=0$, $y''=-6$ so there is a local maximum, while at $x=2$, $y''=6$ so there is a local minimum; if the sign of $\frac{dy}{dx}$ stays the same on both sides, the stationary point is an inflection instead.

## Implicit and parametric differentiation

Implicit equations mix $x$ and $y$ together, so every time you differentiate a $y$ term you must multiply by $\frac{dy}{dx}$. For example, $\frac{d}{dx}(y^2)=2y\frac{dy}{dx}$ and $\frac{d}{dx}(xy)=x\frac{dy}{dx}+y$.

From $x^2+xy+2y^2=23$, differentiating gives $2x+x\frac{dy}{dx}+y+4y\frac{dy}{dx}=0$. Collecting the derivative terms gives $(x+4y)\frac{dy}{dx}=-(2x+y)$, so at $(3,2)$ the gradient is $-\frac{8}{11}$.

For parametric curves, if $x=x(t)$ and $y=y(t)$ then
$$\frac{dy}{dx}=\frac{\frac{dy}{dt}}{\frac{dx}{dt}}$$

Provided $\frac{dx}{dt}\neq 0$. For example, if $x=3\cos t$ and $y=2\sin t$, then $\frac{dy}{dx}=\frac{2\cos t}{-3\sin t}=-\frac{2}{3}\cot t$.

## Check yourself

1. What does $\frac{dy}{dx}$ represent at a point on a curve?

   - The average gradient over the whole curve

   - The gradient of the tangent at that point ✔

   - The $y$-coordinate of the point

   - The area under the curve

   _Explanation:_ B is correct because the derivative gives the instantaneous rate of change, which is the gradient of the tangent at that point. A is the common wrong answer because average gradient describes a secant over an interval, not the gradient at one exact point.

2. Differentiate $y=e^{x^2}$.

   - $$e^{x^2}$

   - $$2xe^{x^2}$ ✔

   - $$xe^{x^2}$

   - $$2x^2e^{x^2}$

   _Explanation:_ B is correct because the chain rule keeps the outside as $e^{x^2}$ and multiplies by the derivative of the inside, which is $2x$. A is the common wrong answer because it differentiates the outside but forgets the inside derivative.

3. If the tangent gradient at a point is $-\frac{8}{9}$, what is the normal gradient?

   - $$\frac{8}{9}$

   - $$\frac{9}{8}$ ✔

   - $$-\frac{9}{8}$

   - $$-\frac{8}{9}$

   _Explanation:_ B is correct because perpendicular gradients are negative reciprocals, and the negative reciprocal of $-\frac{8}{9}$ is $\frac{9}{8}$. C is a common wrong answer because it takes the reciprocal but forgets that the sign must also change.

4. Stretch: A curve has $\frac{dy}{dx}=(x-2)^2(x+1)$. What kind of stationary point is at $x=2$?

   - Local maximum

   - Local minimum

   - Stationary point of inflection ✔

   - Impossible to tell

   _Explanation:_ C is correct because $\frac{dy}{dx}=0$ at $x=2$, but the factor $(x-2)^2$ does not change sign, so the sign of $\frac{dy}{dx}$ stays positive on both sides when $x$ is near 2. D is the common wrong answer if you stop when a standard test seems inconclusive, but a sign test on $\frac{dy}{dx}$ does tell you the nature.
