# Differentiation Flashcards

_Lane: `a-level-maths-edexcel` · grade — · 20 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** What does the derivative $\frac{dy}{dx}$ represent geometrically?

**Back:** The gradient of the curve at a specific point.

**Choices:**

- The gradient of the curve at a specific point. ✔
  - _why:_ The derivative gives the instantaneous rate at which y changes with x, which geometrically is the gradient of the tangent to the curve at that point.
- The y-coordinate of the curve at a specific point.
  - _why:_ The y-coordinate gives the height of the curve, not its steepness. The derivative represents the gradient of the curve at a specific point.
- The equation of the tangent to the curve at a specific point.
  - _why:_ The tangent is a line touching the curve, whereas the derivative gives its steepness. The correct interpretation is the gradient of the curve at a specific point.
- The distance from the origin to the curve at a specific point.
  - _why:_ The derivative is not the distance from the origin to the curve. It measures local steepness, namely the gradient of the curve at a specific point.

## Card 2 — `cloze`

**Front:** The definition of the derivative from first principles is $f'(x) = \lim_{h \to 0} \text{[...]}$.

**Back:** The definition of the derivative from first principles is $f'(x) = \lim_{h \to 0} \boxed{\frac{f(x+h) - f(x)}{h}}$.

**Choices:**

- $$\frac{f(x+h) - f(x)}{h}$ ✔
  - _why:_ The difference quotient compares the change in function value with the change in input, then the limit makes that input change tend to zero, giving the derivative.
- $$\frac{f(x) - f(x+h)}{h}$
  - _why:_ Reversing the numerator changes the sign of the quotient, giving the negative derivative. The correct first-principles quotient is $\frac{f(x+h) - f(x)}{h}$.
- $$\frac{f(x+h) - f(x)}{h^2}$
  - _why:_ Dividing by $h^2$ gives the wrong scaling and does not produce the derivative limit. The denominator must be the first power, $\frac{f(x+h) - f(x)}{h}$.
- $$\frac{f'(x+h) - f'(x)}{h}$
  - _why:_ Using $f'(x+h)$ introduces the derivative before it has been defined, so it is circular. First principles uses function values: $\frac{f(x+h) - f(x)}{h}$.

## Card 3 — `basic`

**Front:** What unit of measurement must be used for angles in standard trigonometric derivatives?

**Back:** Radians.

**Choices:**

- Radians. ✔
  - _why:_ The standard derivative formulae for sine, cosine and the other trigonometric functions assume the angle is measured in radians.
- Degrees
  - _why:_ Degree measures introduce a conversion factor into trigonometric derivatives, so the standard formulae are not valid unchanged. The required unit is Radians.
- Revolutions
  - _why:_ A revolution is an angular amount rather than the unit assumed by the standard derivative formulae. Angles must be measured in Radians.
- Gradians
  - _why:_ Gradians use a different scale from the one built into standard trigonometric derivatives. The required angular measure is Radians.

## Card 4 — `basic`

**Front:** Differentiate $\tan x$.

**Back:** $$\sec^2 x$

**Choices:**

- $$\sec^2 x$ ✔
  - _why:_ The derivative of $\tan x$ is $\sec^2 x$, obtained from the quotient rule or from $\tan x = \frac{\sin x}{\cos x}$.
- $$\sec x \tan x$
  - _why:_ This is the derivative of $\sec x$, not $\tan x$. Differentiating $\tan x$ gives $\sec^2 x$.
- $$-\csc^2 x$
  - _why:_ The negative cosecant-square result belongs to differentiating $\cot x$. The derivative of $\tan x$ is $\sec^2 x$.
- $$\csc^2 x$
  - _why:_ This expression is the derivative of $\cot x$ with the sign omitted, not the derivative of tangent. For $\tan x$, the result is $\sec^2 x$.

## Card 5 — `basic`

**Front:** Differentiate $a^x$ where $a > 0$.

**Back:** $$a^x \ln a$

**Choices:**

- $$a^x \ln a$ ✔
  - _why:_ Writing $a^x = e^{x\ln a}$ and applying the chain rule gives $a^x\ln a$, which is valid for positive $a$.
- $$xa^{x-1}$
  - _why:_ This applies the power rule for $x^a$, incorrectly treating the variable base and constant exponent as the roles in $a^x$. The derivative is $a^x \ln a$.
- $$a^{x-1} \ln a$
  - _why:_ Reducing the exponent by one is another power-rule error. An exponential retains $a^x$ and gains the factor $\ln a$, giving $a^x \ln a$.
- $$a^x$
  - _why:_ The factor $\ln a$ is missing, so this would only work when $a=e$. In general, differentiating $a^x$ gives $a^x \ln a$.

## Card 6 — `basic`

**Front:** What does the second derivative $\frac{d^2y}{dx^2}$ represent?

**Back:** The rate of change of the gradient.

**Choices:**

- The rate of change of the gradient. ✔
  - _why:_ The first derivative is the gradient, so differentiating it again measures how quickly that gradient changes as x changes.
- The gradient of the curve.
  - _why:_ The first derivative, not the second, gives the gradient itself. The second derivative represents the rate of change of the gradient.
- The rate of change of the function.
  - _why:_ The function's rate of change is represented by the first derivative. A second derivative measures the rate of change of the gradient.
- The value of the gradient.
  - _why:_ The second derivative does not simply report the gradient's value; it reports how that gradient varies. Its meaning is the rate of change of the gradient.

## Card 7 — `basic`

**Front:** Outline the mechanism of the Chain Rule for $y=f(g(x))$.

**Back:** Differentiate the outside function, leave the inside unchanged, then multiply by the derivative of the inside.

**Choices:**

- Differentiate the outside function, leave the inside unchanged, then multiply by the derivative of the inside. ✔
  - _why:_ The chain rule differentiates the outer operation first, retains the inner expression during that step, and multiplies by the inner expression's derivative.
- Differentiate the inside function, leave the outside unchanged, then multiply by the derivative of the inside.
  - _why:_ This reverses the chain rule's order: the outer function must be differentiated first while the inside remains unchanged. The correct sequence is outside, inside, then multiply.
- Differentiate the outside function, leave the inside unchanged, then add the derivative of the inside.
  - _why:_ Adding derivatives is a common confusion with the product rule. The chain rule requires differentiating the outside, retaining the inside, then multiplying by the inner derivative.
- Differentiate the outside function, leave the inside unchanged, then divide by the derivative of the inside.
  - _why:_ Leaving the inner function unchanged throughout omits the essential inner derivative factor. The chain rule requires differentiating the outside, leaving the inside briefly unchanged, then multiplying.

## Card 8 — `basic`

**Front:** State the Product Rule for $\frac{d}{dx}(uv)$.

**Back:** $$u'v + uv'$

**Choices:**

- $$u'v + uv'$ ✔
  - _why:_ The product rule differentiates the first factor while retaining the second, then retains the first and differentiates the second, so both contributions are included.
- $$u'v'$
  - _why:_ Differentiating both factors simultaneously omits the two product-rule contributions with one factor retained. The correct result is $u'v + uv'$.
- $$uv$
  - _why:_ This is just the original product, with neither factor differentiated. The product rule gives $u'v + uv'$.
- $$u'v + u'v'$
  - _why:_ The second term differentiates both factors instead of retaining $u$ while differentiating $v$. The correct formula is $u'v + uv'$.

## Card 9 — `basic`

**Front:** State the Quotient Rule for $\frac{d}{dx}(\frac{u}{v})$.

**Back:** $$\frac{u'v - uv'}{v^2}$

**Choices:**

- $$\frac{u'v - uv'}{v^2}$ ✔
  - _why:_ The quotient rule differentiates the numerator and denominator in a cross-product subtraction, then divides by the square of the original denominator.
- $$\frac{u'v + uv'}{v^2}$
  - _why:_ This uses addition instead of the required subtraction. The quotient rule is $\frac{u'v - uv'}{v^2}$, with the numerator terms subtracted in that order.
- $$\frac{u'v - uv'}{v}$
  - _why:_ This fails to square the denominator, a common quotient-rule slip. The correct derivative is $\frac{u'v - uv'}{v^2}$.
- $$\frac{uv' - u'v}{v^2}$
  - _why:_ This reverses the numerator subtraction, giving the negative of the required derivative. The quotient rule is $\frac{u'v - uv'}{v^2}$.

## Card 10 — `basic`

**Front:** If a tangent has a gradient of $m$, what is the gradient of the normal?

**Back:** $$-\frac{1}{m}$ (the negative reciprocal).

**Choices:**

- $$-\frac{1}{m}$ (the negative reciprocal). ✔
  - _why:_ A tangent and its normal are perpendicular, so their gradients have product $-1$. Therefore, a tangent gradient of $m$ gives a normal gradient of $-\frac{1}{m}$.
- $$\frac{1}{m}$ (the reciprocal).
  - _why:_ Taking only the reciprocal misses the negative sign required for perpendicular lines. The normal’s gradient is $-\frac{1}{m}$, the negative reciprocal of $m$.
- $$-m$ (the negative gradient).
  - _why:_ Changing only the sign does not generally produce a perpendicular gradient. The normal’s gradient must be the negative reciprocal, $-\frac{1}{m}$.
- $$m$ (the same gradient).
  - _why:_ Using the same gradient would make the normal parallel to the tangent rather than perpendicular. Its gradient is $-\frac{1}{m}$.

## Card 11 — `basic`

**Front:** What is the requirement for a point to be stationary?

**Back:** $$\frac{dy}{dx} = 0$

**Choices:**

- $$\frac{dy}{dx} = 0$ ✔
  - _why:_ At a stationary point, the tangent is horizontal, so its gradient is zero. Since $\frac{dy}{dx}$ gives the tangent’s gradient, the requirement is $\frac{dy}{dx}=0$.
- $$\frac{dy}{dx} = 1$
  - _why:_ A gradient of one means the tangent rises at $45^\circ$ and is not horizontal. A stationary point requires $\frac{dy}{dx}=0$.
- $$\frac{d^2y}{dx^2} = 0$
  - _why:_ Setting the second derivative to zero does not define a stationary point; it concerns changes in gradient. Stationarity specifically requires $\frac{dy}{dx}=0$.
- $$y = 0$
  - _why:_ The condition $y=0$ identifies an intercept with the $x$-axis, not necessarily a stationary point. Stationarity requires the gradient condition $\frac{dy}{dx}=0$.

## Card 12 — `basic`

**Front:** How is a stationary point classified if $\frac{d^2y}{dx^2} > 0$?

**Back:** Local minimum

**Choices:**

- Local minimum ✔
  - _why:_ A positive second derivative means the gradient is increasing through the stationary point, so the curve is concave upwards and the point is a local minimum.
- Local maximum
  - _why:_ A local maximum has a negative second derivative because the curve is concave downwards. A positive second derivative at a stationary point indicates a local minimum.
- Stationary inflection
  - _why:_ A stationary point of inflection is not identified by a strictly positive second derivative. The positive value shows upward curvature, classifying the point as a local minimum.
- Non-stationary inflection
  - _why:_ A non-stationary inflection has a non-zero first derivative and changing concavity. Here the point is stationary with positive second derivative, so it is a local minimum.

## Card 13 — `basic`

**Front:** How is a stationary point classified if $\frac{d^2y}{dx^2} < 0$?

**Back:** Local maximum

**Choices:**

- Local maximum ✔
  - _why:_ A negative second derivative means the gradient is decreasing through the stationary point, so the curve is concave downwards and the point is a local maximum.
- Local minimum
  - _why:_ A local minimum has a positive second derivative because the curve is concave upwards. A negative second derivative at a stationary point indicates a local maximum.
- Stationary inflection
  - _why:_ A stationary point of inflection is not identified by a strictly negative second derivative. The negative value shows downward curvature, classifying the point as a local maximum.
- Non-stationary inflection
  - _why:_ A non-stationary inflection does not have zero gradient, whereas this is already a stationary point. Its negative second derivative classifies it as a local maximum.

## Card 14 — `basic`

**Front:** What must you do to classify a stationary point if $\frac{d^2y}{dx^2} = 0$?

**Back:** Check the sign of $\frac{dy}{dx}$ on both sides of the point.

**Choices:**

- Check the sign of $\frac{dy}{dx}$ on both sides of the point. ✔
  - _why:_ When the second derivative test is inconclusive, inspect the first derivative around the point. A change from negative to positive gives a minimum, while positive to negative gives a maximum.
- Check the value of $\frac{d^2y}{dx^2}$ at the point again.
  - _why:_ The second derivative’s value at the point is already known to be zero, so repeating that check cannot classify it. Instead, check the sign of $\frac{dy}{dx}$ on both sides.
- Check the sign of $y$ on both sides of the point.
  - _why:_ Whether $y$ is positive or negative describes the curve’s position relative to the axis, not its turning behaviour. Check the sign of $\frac{dy}{dx}$ on both sides.
- Assume it is a stationary point of inflection.
  - _why:_ A zero second derivative makes the test inconclusive and does not automatically imply an inflection. The sign of $\frac{dy}{dx}$ on both sides must be checked.

## Card 15 — `cloze`

**Front:** In implicit differentiation, $\frac{d}{dx}(y^2) = \text{[...]}$.

**Back:** In implicit differentiation, $\frac{d}{dx}(y^2) = \boxed{2y \frac{dy}{dx}}$.

**Choices:**

- $$2y \frac{dy}{dx}$ ✔
  - _why:_ Because $y$ is a function of $x$, the chain rule applies: differentiating $y^2$ gives $2y$, multiplied by the inner derivative $\frac{dy}{dx}$.
- $$2y$
  - _why:_ This treats $y$ as though it were the independent variable and omits the chain-rule factor. Implicit differentiation gives $2y\frac{dy}{dx}$.
- $$y^2 \frac{dy}{dx}$
  - _why:_ The power rule reduces the exponent from two to one; it does not leave $y^2$ unchanged. The correct derivative is $2y\frac{dy}{dx}$.
- $$2x \frac{dy}{dx}$
  - _why:_ This incorrectly differentiates as though the squared variable were $x$. Since $y$ depends on $x$, the chain rule gives $2y\frac{dy}{dx}$.

## Card 16 — `cloze`

**Front:** Using the product rule on an implicit term, $\frac{d}{dx}(xy) = \text{[...]}$.

**Back:** Using the product rule on an implicit term, $\frac{d}{dx}(xy) = \boxed{x \frac{dy}{dx} + y}$.

**Choices:**

- $$x \frac{dy}{dx} + y$ ✔
  - _why:_ Applying the product rule gives $x\frac{dy}{dx}+y\frac{dx}{dx}$. Since $\frac{dx}{dx}=1$, this simplifies to $x\frac{dy}{dx}+y$.
- $$x \frac{dy}{dx}$
  - _why:_ This omits the second product-rule term obtained by differentiating $x$. Since $\frac{dx}{dx}=1$, the full derivative is $x\frac{dy}{dx}+y$.
- $$y \frac{dy}{dx} + x$
  - _why:_ This attaches $\frac{dy}{dx}$ to the wrong product-rule term. Differentiating $y$ supplies $\frac{dy}{dx}$, so the derivative is $x\frac{dy}{dx}+y$.
- $$\frac{dy}{dx} + y$
  - _why:_ This loses the factor $x$ when differentiating $y$. The product rule preserves the undifferentiated factor, giving $x\frac{dy}{dx}+y$.

## Card 17 — `basic`

**Front:** State the formula for parametric differentiation $\frac{dy}{dx}$.

**Back:** $$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}$

**Choices:**

- $$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}$ ✔
  - _why:_ For parametric equations, the chain rule gives $\frac{dy}{dx}=\frac{dy}{dt}\frac{dt}{dx}$. Since $\frac{dt}{dx}=\frac{1}{dx/dt}$, this produces the stated quotient.
- $$\frac{dy}{dx} = \frac{\frac{dx}{dt}}{\frac{dy}{dt}}$
  - _why:_ This reverses the quotient and therefore gives $\frac{dx}{dy}$. Parametric differentiation requires dividing $\frac{dy}{dt}$ by $\frac{dx}{dt}$.
- $$\frac{dy}{dx} = \frac{dy}{dt}\frac{dx}{dt}$
  - _why:_ The parametric derivatives must be divided, not multiplied. Applying the chain rule correctly gives $\frac{dy}{dx}=\frac{dy/dt}{dx/dt}$.
- $$\frac{dy}{dx} = \frac{dy}{dt} + \frac{dx}{dt}$
  - _why:_ Adding the derivatives does not eliminate the parameter $t$ correctly. The chain rule instead requires the quotient $\frac{dy/dt}{dx/dt}$.

## Card 18 — `basic`

**Front:** Differentiate $y = e^{x^2}$.

**Back:** $$2xe^{x^2}$

**Choices:**

- $$2xe^{x^2}$ ✔
  - _why:_ Using the chain rule, differentiating the outer exponential leaves $e^{x^2}$, while differentiating the inner function $x^2$ gives the multiplier $2x$.
- $$e^{x^2}$
  - _why:_ This omits the derivative of the inner function $x^2$. The chain rule supplies a factor of $2x$, so the derivative is $2xe^{x^2}$.
- $$2xe^x$
  - _why:_ This differentiates the exponent incorrectly by replacing $x^2$ with $x$. The exponential remains $e^{x^2}$ and is multiplied by $2x$, giving $2xe^{x^2}$.
- $$x^2e^{x^2}$
  - _why:_ This multiplies by the original inner function rather than its derivative. Since $\frac{d}{dx}(x^2)=2x$, the chain rule gives $2xe^{x^2}$.

## Card 19 — `basic`

**Front:** How is a stationary point of inflection identified using a sign test?

**Back:** The gradient $\frac{dy}{dx}$ has the same sign on both sides of the point.

**Choices:**

- The gradient $\frac{dy}{dx}$ has the same sign on both sides of the point. ✔
  - _why:_ At a stationary point of inflection, the gradient is zero at the point but does not change sign, so the function continues increasing or decreasing through it.
- The gradient $\frac{dy}{dx}$ has the opposite sign on both sides of the point.
  - _why:_ Opposite gradient signs indicate a change between increasing and decreasing, which identifies a local maximum or minimum. At a stationary inflection, the gradient has the same sign on both sides.
- The gradient $\frac{dy}{dx}$ is equal to zero on both sides of the point.
  - _why:_ A gradient cannot be described as zero throughout both sides merely because it is zero at the stationary point. The required test is that its sign remains the same across the point.
- The gradient $\frac{dy}{dx}$ has the same value on both sides of the point.
  - _why:_ Equal gradient values on either side are not required and generally do not occur. A stationary point of inflection is identified when the gradient retains the same sign across the point.

## Card 20 — `basic`

**Front:** Differentiate $y = \cos x$.

**Back:** $$-\sin x$

**Choices:**

- $$-\sin x$ ✔
  - _why:_ The standard trigonometric derivative is $\frac{d}{dx}(\cos x)=-\sin x$. The negative sign reflects that cosine decreases immediately to the right of $x=0$.
- $$\sin x$
  - _why:_ This misses the negative sign in the standard derivative of cosine. Since cosine initially decreases from its maximum at $x=0$, its derivative is $-\sin x$.
- $$\cos x$
  - _why:_ This incorrectly treats cosine as unchanged by differentiation. The standard trigonometric derivative is $\frac{d}{dx}(\cos x)=-\sin x$.
- $$-\cos x$
  - _why:_ Negating the original function is not the differentiation rule for cosine. Differentiation changes cosine to negative sine, so the correct result is $-\sin x$.
