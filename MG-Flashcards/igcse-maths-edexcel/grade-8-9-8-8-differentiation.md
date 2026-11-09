# Differentiation Flashcards

_Lane: `igcse-maths-edexcel` · grade 8 · 21 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** What does the derivative $\frac{dy}{dx}$ represent on a curve?

**Back:** The gradient function (the gradient at any point).

**Choices:**

- The gradient function (the gradient at any point). ✔
  - _why:_ The derivative gives the gradient of the curve as a function of $x$, so substituting a particular $x$-value gives the curve’s gradient at that point.
- The equation of the curve (the value of $y$ at any point).
  - _why:_ This confuses the original function with its derivative. The derivative is the gradient function, which gives the gradient of the curve at any chosen point.
- The area function (the area beneath any point).
  - _why:_ Area beneath a curve is associated with integration, not differentiation. The derivative represents the gradient function, giving the curve’s gradient at any point.
- The coordinate function (the coordinates of every point).
  - _why:_ The original equation determines coordinates on the curve. Its derivative instead gives the gradient function, which specifies the gradient at each point.

## Card 2 — `basic`

**Front:** State the power rule for differentiating $y=ax^n$.

**Back:** $$\frac{dy}{dx} = anx^{n-1}$

**Choices:**

- $$\frac{dy}{dx} = anx^{n-1}$ ✔
  - _why:_ The power rule multiplies the coefficient by the original power and then reduces the power by one, giving $\frac{dy}{dx}=anx^{n-1}$.
- $$\frac{dy}{dx} = ax^{n-1}$
  - _why:_ This reduces the power correctly but forgets to multiply the coefficient by $n$. The full power rule is $\frac{dy}{dx}=anx^{n-1}$.
- $$\frac{dy}{dx} = anx^n$
  - _why:_ This multiplies by the power but fails to reduce the exponent by one. Applying both steps gives $\frac{dy}{dx}=anx^{n-1}$.
- $$\frac{dy}{dx} = (n-1)ax^{n-1}$
  - _why:_ This incorrectly multiplies by the new exponent $n-1$. The coefficient must be multiplied by the original exponent $n$, giving $\frac{dy}{dx}=anx^{n-1}$.

## Card 3 — `basic`

**Front:** What is the derivative of a constant (e.g., 11)?

**Back:** Zero

**Choices:**

- Zero ✔
  - _why:_ A constant does not change as $x$ changes, so its rate of change and therefore its derivative are both zero.
- One
  - _why:_ One is the derivative of $x$, not of a constant. Since a constant has no change as $x$ varies, its derivative is zero.
- Eleven
  - _why:_ This leaves the example constant unchanged instead of differentiating it. A constant such as $11$ has no rate of change, so its derivative is zero.
- Undefined
  - _why:_ A constant function has a well-defined horizontal graph with gradient zero everywhere. Therefore, its derivative is zero rather than undefined.

## Card 4 — `basic`

**Front:** What is the derivative of a linear term such as $7x$?

**Back:** $$7$

**Choices:**

- $$7$ ✔
  - _why:_ Using the power rule, $7x$ is $7x^1$, so its derivative is $7\times1x^0=7$.
- $$7x$
  - _why:_ This leaves the term unchanged. Differentiating $7x=7x^1$ reduces the exponent to zero, so the derivative is the constant $7$.
- $$x$
  - _why:_ This incorrectly removes the coefficient rather than the variable. The gradient of $y=7x$ is constant and equal to $7$, so its derivative is $7$.
- $$0$
  - _why:_ Zero is the derivative of a constant term, but $7x$ changes with $x$. Its constant gradient is $7$, so the derivative is $7$.

## Card 5 — `cloze`

**Front:** To differentiate a term like $\frac{1}{x}$, first rewrite it as $\text{[...]}$.

**Back:** To differentiate a term like $\frac{1}{x}$, first rewrite it as $\boxed{x^{-1}}$.

**Choices:**

- $$x^{-1}$ ✔
  - _why:_ A reciprocal can be written using a negative exponent: $\frac{1}{x}=x^{-1}$. This form allows the power rule to be applied directly.
- $$x^1$
  - _why:_ A positive exponent gives $x^1=x$, not its reciprocal. Since moving $x$ from the denominator changes the exponent’s sign, $\frac{1}{x}=x^{-1}$.
- $$x^{-2}$
  - _why:_ The exponent $-2$ represents $\frac{1}{x^2}$, not $\frac{1}{x}$. A single factor of $x$ in the denominator becomes $x^{-1}$.
- $$-x^{-1}$
  - _why:_ Moving $x$ from the denominator creates a negative exponent, not a negative coefficient. Therefore $\frac{1}{x}$ is rewritten as $x^{-1}$.

## Card 6 — `basic`

**Front:** Differentiate the term $x^{-1}$.

**Back:** $$-x^{-2}$ (or $-\frac{1}{x^2}$)

**Choices:**

- $$-x^{-2}$ (or $-\frac{1}{x^2}$) ✔
  - _why:_ The power rule multiplies by the exponent $-1$ and subtracts one from it, so $\frac{d}{dx}(x^{-1})=-x^{-2}$.
- $$x^{-2}$ (or $\frac{1}{x^2}$)
  - _why:_ This reduces the exponent correctly but loses the negative multiplier from the original power. The derivative is $-x^{-2}$, equivalent to $-\frac{1}{x^2}$.
- $$-x^{-1}$ (or $-\frac{1}{x}$)
  - _why:_ This multiplies by $-1$ but fails to subtract one from the exponent. The new exponent is $-2$, giving $-x^{-2}$.
- $$-2x^{-3}$ (or $-\frac{2}{x^3}$)
  - _why:_ This applies the power rule as though the original term were $x^{-2}$. Starting from exponent $-1$ gives coefficient $-1$ and exponent $-2$, so the derivative is $-x^{-2}$.

## Card 7 — `basic`

**Front:** What is the required condition for a stationary point?

**Back:** $$\frac{dy}{dx} = 0$

**Choices:**

- $$\frac{dy}{dx} = 0$ ✔
  - _why:_ At a stationary point, the tangent is horizontal, so its gradient is zero. Since the derivative gives the tangent’s gradient, $\frac{dy}{dx}=0$.
- $$\frac{dy}{dx} = 1$
  - _why:_ A derivative of $1$ describes a tangent rising with gradient one, not a stationary point. Stationary points require a horizontal tangent, so $\frac{dy}{dx}=0$.
- $$\frac{dy}{dx} = y$
  - _why:_ This incorrectly equates the gradient with the curve’s vertical coordinate. A stationary point is identified by a zero tangent gradient, so $\frac{dy}{dx}=0$.
- $$\frac{d^2y}{dx^2} = 0$
  - _why:_ The second derivative can help classify curvature but does not give the required stationary-point condition. The first derivative must equal zero: $\frac{dy}{dx}=0$.

## Card 8 — `basic`

**Front:** Describe the tangent at a stationary point.

**Back:** It is horizontal (gradient is zero).

**Choices:**

- It is horizontal (gradient is zero). ✔
  - _why:_ A stationary point occurs where the derivative is zero. Since the derivative is the tangent’s gradient, the tangent at that point must be horizontal.
- It is vertical (gradient is undefined).
  - _why:_ A vertical tangent has an undefined gradient and is not the defining feature of a stationary point. At a stationary point, the tangent is horizontal with gradient zero.
- It is diagonal (gradient is one).
  - _why:_ A gradient of one means the curve is increasing, so the point is not stationary. A stationary point has a horizontal tangent with gradient zero.
- It is horizontal (gradient is undefined).
  - _why:_ This correctly identifies the tangent’s direction but gives the wrong gradient. A horizontal tangent has gradient zero, while an undefined gradient describes a vertical tangent.

## Card 9 — `basic`

**Front:** How do you find the $y$-coordinate of a stationary point once you have the $x$-coordinate?

**Back:** Substitute the $x$-value into the original equation for $y$.

**Choices:**

- Substitute the $x$-value into the original equation for $y$. ✔
  - _why:_ The original equation links each $x$-coordinate to its corresponding $y$-coordinate, so substituting the stationary point’s $x$-value gives its exact $y$-coordinate.
- Substitute the $x$-value into the differentiated equation for $y$.
  - _why:_ The differentiated equation gives the gradient, not the curve’s $y$-coordinate. Substitute the known $x$-value into the original equation for $y$ instead.
- Substitute the $x$-value into the second derivative for $y$.
  - _why:_ The second derivative helps determine the nature of a stationary point, but it does not give its $y$-coordinate. Use the original equation for $y$.
- Substitute zero into the original equation for $y$.
  - _why:_ Setting the derivative equal to zero finds the stationary point’s $x$-coordinate; it does not mean $x=0$. Substitute the calculated $x$-value into the original equation.

## Card 10 — `basic`

**Front:** What inequality is used to find where a curve has a negative gradient?

**Back:** $$\frac{dy}{dx} < 0$

**Choices:**

- $$\frac{dy}{dx} < 0$ ✔
  - _why:_ A negative gradient means the derivative is less than zero. Solving $\frac{dy}{dx}<0$ therefore identifies the $x$-values for which the curve is decreasing.
- $$\frac{dy}{dx} > 0$
  - _why:_ A derivative greater than zero represents a positive gradient, so the curve is increasing. A negative gradient is found using $\frac{dy}{dx}<0$.
- $$\frac{dy}{dx} = 0$
  - _why:_ Setting the derivative equal to zero finds stationary points, where the gradient is neither positive nor negative. Negative gradients satisfy $\frac{dy}{dx}<0$.
- $$\frac{dy}{dx} \leq 0$
  - _why:_ Using a non-strict inequality incorrectly includes points where the gradient is zero. For a genuinely negative gradient, the required inequality is $\frac{dy}{dx}<0$.

## Card 11 — `basic`

**Front:** Why are strict inequalities used when finding a range for negative gradients?

**Back:** At the endpoints, the gradient is zero, not negative.

**Choices:**

- At the endpoints, the gradient is zero, not negative. ✔
  - _why:_ The endpoints are roots of the derivative, so the gradient equals zero there. They must be excluded because the question requires a negative, rather than non-positive, gradient.
- At the endpoints, the gradient is positive, not negative.
  - _why:_ The endpoints occur where the derivative crosses or touches the $x$-axis, so the gradient is zero there, not positive. This is why strict inequalities exclude them.
- At the endpoints, the gradient is undefined, not negative.
  - _why:_ For a differentiable curve, the gradient remains defined at these endpoints and equals zero. Strict inequalities are used because zero is not a negative value.
- At the endpoints, the gradient is constant, not negative.
  - _why:_ The key issue is not that the gradient is constant, but that it equals zero at the endpoints. Therefore, the endpoints are excluded using strict inequalities.

## Card 12 — `basic`

**Front:** If $\frac{dy}{dx}$ is an upward-opening quadratic, where is the gradient negative?

**Back:** Between the two roots.

**Choices:**

- Between the two roots. ✔
  - _why:_ An upward-opening quadratic lies below the $x$-axis between its two distinct roots. Therefore, $\frac{dy}{dx}<0$ between those roots, giving a negative gradient.
- Outside the two roots.
  - _why:_ Outside the roots, an upward-opening derivative is above the $x$-axis, so the gradient is positive. It is negative between the two roots.
- At the two roots.
  - _why:_ At the roots of $\frac{dy}{dx}$, the derivative equals zero, so these are stationary points. The gradient is negative between the roots, not at them.
- Beyond the larger root.
  - _why:_ Beyond the larger root, an upward-opening quadratic derivative is positive. Its negative values occur below the $x$-axis, between the two roots.

## Card 13 — `basic`

**Front:** In particle motion, how is velocity ($v$) calculated from displacement ($s$)?

**Back:** $$v = \frac{ds}{dt}$

**Choices:**

- $$v = \frac{ds}{dt}$ ✔
  - _why:_ Velocity is the rate of change of displacement with respect to time. Differentiating $s$ with respect to $t$ therefore gives $v=\frac{ds}{dt}$.
- $$v = \frac{dt}{ds}$
  - _why:_ This reverses the derivative and gives time change per unit displacement, not velocity. Velocity is displacement change per unit time, so $v=\frac{ds}{dt}$.
- $$v = \frac{d^2s}{dt^2}$
  - _why:_ Differentiating displacement twice gives acceleration, not velocity. Velocity is obtained after one differentiation with respect to time: $v=\frac{ds}{dt}$.
- $$v = \frac{dv}{dt}$
  - _why:_ The derivative of velocity with respect to time is acceleration. To calculate velocity from displacement, differentiate $s$ once: $v=\frac{ds}{dt}$.

## Card 14 — `basic`

**Front:** In particle motion, how is acceleration ($a$) calculated from velocity ($v$)?

**Back:** $$a = \frac{dv}{dt}$

**Choices:**

- $$a = \frac{dv}{dt}$ ✔
  - _why:_ Acceleration is the rate of change of velocity with respect to time. Differentiating the velocity function therefore gives $a=\frac{dv}{dt}$.
- $$a = \frac{dt}{dv}$
  - _why:_ This reverses the derivative and measures time change per unit velocity. Acceleration is velocity change per unit time, so $a=\frac{dv}{dt}$.
- $$a = \frac{ds}{dt}$
  - _why:_ The derivative of displacement with respect to time is velocity, not acceleration. Acceleration is found by differentiating velocity: $a=\frac{dv}{dt}$.
- $$a = \frac{d^2v}{dt^2}$
  - _why:_ Differentiating velocity twice gives the rate of change of acceleration, sometimes called jerk. Acceleration requires only one differentiation: $a=\frac{dv}{dt}$.

## Card 15 — `basic`

**Front:** What is the physical condition for a particle to be instantaneously at rest?

**Back:** Velocity is zero ($v=0$).

**Choices:**

- Velocity is zero ($v=0$). ✔
  - _why:_ A particle is instantaneously at rest when its instantaneous velocity is zero. Its acceleration may still be non-zero, so it may begin moving again immediately.
- Acceleration is zero ($a=0$).
  - _why:_ Zero acceleration means velocity is not changing at that instant, but the particle could still be moving at constant velocity. Rest requires velocity to be zero.
- Displacement is zero ($s=0$).
  - _why:_ Zero displacement only means the particle is at the chosen origin; it may be passing through that point at speed. Instantaneous rest requires $v=0$.
- Time is zero ($t=0$).
  - _why:_ The value $t=0$ marks the chosen starting time and says nothing by itself about motion. A particle is instantaneously at rest when $v=0$.

## Card 16 — `basic`

**Front:** How do you find acceleration from a displacement equation?

**Back:** Differentiate twice with respect to $t$.

**Choices:**

- Differentiate twice with respect to $t$. ✔
  - _why:_ Differentiating displacement once with respect to time gives velocity, and differentiating again gives acceleration. Thus, $a=\frac{d^2s}{dt^2}$.
- Differentiate once with respect to $t$.
  - _why:_ One differentiation of displacement gives velocity rather than acceleration. Differentiate a second time with respect to $t$ to obtain $a=\frac{d^2s}{dt^2}$.
- Integrate twice with respect to $t$.
  - _why:_ Integration moves from acceleration towards velocity and displacement, so it is the reverse process. To find acceleration from displacement, differentiate twice with respect to $t$.
- Integrate once with respect to $t$.
  - _why:_ Integrating displacement does not produce acceleration. Acceleration is the second derivative of displacement, so the displacement equation must be differentiated twice with respect to $t$.

## Card 17 — `cloze`

**Front:** A [ ___ ] is a straight line that touches a curve at one point and has the same direction as the curve at that point.

**Back:** A tangent is a straight line that touches a curve at one point and has the same direction as the curve at that point.

**Choices:**

- tangent ✔
  - _why:_ A tangent touches a curve at a particular point and follows the curve’s direction there, so it has the same gradient at the point of contact.
- normal
  - _why:_ A normal also meets the curve at a point, but it is perpendicular to the tangent there. The line with the same direction as the curve is the tangent.
- secant
  - _why:_ A secant passes through two points on a curve rather than matching its direction at one point. The line described is a tangent.
- chord
  - _why:_ A chord is a line segment joining two points on a curve. A straight line touching at one point and sharing the curve’s direction is a tangent.

## Card 18 — `cloze`

**Front:** A tangent is a straight line that touches a curve at one point and has the same [ ___ ] as the curve at that point.

**Back:** A tangent is a straight line that touches a curve at one point and has the same direction as the curve at that point.

**Choices:**

- direction ✔
  - _why:_ At the point of contact, a tangent points in the same direction as the curve. Equivalently, the tangent and curve have the same gradient there.
- position
  - _why:_ A tangent shares the curve’s direction at the point of contact, not its position as a general property. Its gradient matches the curve’s gradient there.
- curvature
  - _why:_ The tangent is straight, so its curvature does not match that of a curved graph. It instead has the same direction as the curve at the contact point.
- length
  - _why:_ Length is not the defining shared property and a tangent line may extend indefinitely. It is the direction, or gradient, that matches at the contact point.

## Card 19 — `cloze`

**Front:** A negative power like $x^{-2}$ means the term belongs in the [ ___ ].

**Back:** A negative power like $x^{-2}$ means the term belongs in the denominator.

**Choices:**

- denominator ✔
  - _why:_ The negative-index rule gives $x^{-n}=\frac{1}{x^n}$. Therefore, $x^{-2}=\frac{1}{x^2}$, placing the corresponding positive power in the denominator.
- numerator
  - _why:_ Placing $x^2$ in the numerator would represent $x^2$, not $x^{-2}$. By the negative-index rule, $x^{-2}=\frac{1}{x^2}$, so it belongs in the denominator.
- coefficient
  - _why:_ A coefficient is a numerical multiplier and does not determine whether a power is above or below a fraction bar. A negative power places the term in the denominator.
- index
  - _why:_ The index is the power itself, such as $-2$, rather than a part of a fraction. Rewriting with a positive index places $x^2$ in the denominator.

## Card 20 — `basic`

**Front:** Differentiate $y = 5x^4 - 3x^2$.

**Back:** $$\frac{dy}{dx} = 20x^3 - 6x$

**Choices:**

- $$\frac{dy}{dx} = 20x^3 - 6x$ ✔
  - _why:_ Using $\frac{d}{dx}(ax^n)=anx^{n-1}$ gives $\frac{d}{dx}(5x^4)=20x^3$ and $\frac{d}{dx}(-3x^2)=-6x$, producing the stated derivative.
- $$\frac{dy}{dx} = 5x^3 - 3x$
  - _why:_ This reduces each power but fails to multiply each coefficient by the original power. Applying the power rule correctly gives $\frac{dy}{dx}=20x^3-6x$.
- $$\frac{dy}{dx} = 20x^4 - 6x^2$
  - _why:_ This multiplies the coefficients by the powers but fails to reduce each power by one. The power rule gives $\frac{dy}{dx}=20x^3-6x$.
- $$\frac{dy}{dx} = 20x^3 - 3x$
  - _why:_ The first term is differentiated correctly, but differentiating $-3x^2$ requires multiplying $-3$ by $2$. The correct second term is $-6x$, giving $20x^3-6x$.

## Card 21 — `basic`

**Front:** In motion questions, why might you reject a solution like $t = -3$?

**Back:** Time $t$ must be greater than or equal to zero ($t \geq 0$).

**Choices:**

- Time $t$ must be greater than or equal to zero ($t \geq 0$). ✔
  - _why:_ If $t$ measures elapsed time from the start of the model, it cannot be negative. Valid solutions therefore satisfy $t\geq0$, so $t=-3$ is rejected.
- Time $t$ must be less than or equal to zero ($t \leq 0$).
  - _why:_ This reverses the valid domain for elapsed time. Time measured from the start must satisfy $t\geq0$, which is why the negative solution $t=-3$ is rejected.
- Time $t$ must be equal to zero ($t = 0$).
  - _why:_ Time need not equal zero; positive values can also represent valid moments after the motion begins. The required condition is $t\geq0$, so $t=-3$ is invalid.
- Time $t$ must be greater than or equal to negative three ($t \geq -3$).
  - _why:_ This bound would incorrectly allow $t=-3$, even though it represents a time before the model begins. Elapsed time must instead satisfy $t\geq0$.
