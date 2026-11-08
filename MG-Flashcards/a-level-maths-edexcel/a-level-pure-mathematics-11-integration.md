# Integration Flashcards

_Lane: `a-level-maths-edexcel` · grade — · 21 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** Why must a constant of integration $+c$ be added to indefinite integrals?

**Back:** Constants have a derivative of zero, so they are lost during differentiation and must be recovered.

**Choices:**

- Constants have a derivative of zero, so they are lost during differentiation and must be recovered. ✔
  - _why:_ Differentiating any constant gives zero, so different antiderivatives can differ by a constant while having the same derivative. The constant of integration represents this missing family of answers.
- Constants have a derivative of one, so they are lost during differentiation and must be recovered.
  - _why:_ A constant differentiates to zero, not one. Because differentiation removes the constant term entirely, an arbitrary constant must be included when finding the full family of antiderivatives.
- Constants have a derivative equal to themselves, so they are lost during differentiation and must be recovered.
  - _why:_ Constants do not differentiate to their own value; their derivative is zero. This is why differentiation cannot distinguish between antiderivatives that differ only by a constant.
- Constants have a derivative of zero, so they are lost during integration and must be recovered.
  - _why:_ The loss occurs when differentiating, not integrating. Since a constant differentiates to zero, indefinite integration must restore an arbitrary constant to include every possible antiderivative.

## Card 2 — `cloze`

**Front:** For $n \neq -1$, the general rule for integrating a power of $x$ is: $\int x^n\,dx = \text{[...]} + c$.

**Back:** For $n \neq -1$, the general rule for integrating a power of $x$ is: $\int x^n\,dx = \boxed{\frac{x^{n+1}}{n+1}} + c$.

**Choices:**

- $$\frac{x^{n+1}}{n+1}$ ✔
  - _why:_ The power rule increases the exponent by one and divides by the new exponent, giving $\frac{x^{n+1}}{n+1}$ when $n \neq -1$.
- $$\frac{x^n}{n}$
  - _why:_ This leaves the exponent unchanged and divides by the original exponent. The power rule instead increases the exponent to $n+1$ and divides by $n+1$.
- $$\frac{x^{n-1}}{n-1}$
  - _why:_ This applies the differentiation power rule in reverse incorrectly by decreasing the exponent. Integration increases the exponent by one, so the denominator must be $n+1$.
- $$(n+1)x^n$
  - _why:_ Multiplying by the new exponent is the differentiation rule, not the integration rule. Integration requires increasing the exponent and dividing by it, producing $\frac{x^{n+1}}{n+1}$.

## Card 3 — `basic`

**Front:** What is the integral of $\frac{1}{x}$ with respect to $x$?

**Back:** $$\ln|x|+c$

**Choices:**

- $$\ln|x|+c$ ✔
  - _why:_ The derivative of $\ln|x|$ is $\frac{1}{x}$ for $x \neq 0$, so the general integral is $\ln|x|+c$. The absolute value covers both positive and negative domains.
- $$\ln x+c$
  - _why:_ This works only for positive $x$ and omits the negative domain. The general antiderivative of $\frac{1}{x}$ is $\ln|x|+c$, valid wherever $x \neq 0$.
- $$\frac{1}{x^2}+c$
  - _why:_ Differentiating this expression gives $-\frac{2}{x^3}$, not $\frac{1}{x}$. The reciprocal function is the exceptional power case whose integral is logarithmic: $\ln|x|+c$.
- $$x\ln|x|+c$
  - _why:_ Using the product rule, the derivative is $\ln|x|+1$, so it does not produce $\frac{1}{x}$. The required antiderivative is $\ln|x|+c$.

## Card 4 — `basic`

**Front:** When integrating a linear bracket $(ax+b)^n$, what extra step must be taken after applying the power rule?

**Back:** Divide by the derivative of the bracket ($a$).

**Choices:**

- Divide by the derivative of the bracket ($a$). ✔
  - _why:_ The substitution $u=ax+b$ gives $du=a\,dx$, so the integral must be divided by $a$ after applying the power rule to account for the bracket's derivative.
- Multiply by the derivative of the bracket ($a$).
  - _why:_ The substitution introduces a factor of $a\,dx$, so the result needs division by $a$, not multiplication. Multiplying would make the derivative too large by a factor of $a^2$.
- Divide by the exponent of the bracket ($n$).
  - _why:_ The extra factor comes from differentiating the inside, whose derivative is $a$, not from the exponent. Therefore the result must be divided by $a$ after using the power rule.
- Subtract the derivative of the bracket ($a$).
  - _why:_ A linear inner function creates a multiplicative chain-rule factor, which is corrected by division. Subtracting $a$ does not undo this factor, so division by $a$ is required.

## Card 5 — `cloze`

**Front:** To integrate $\sin^2 x$, it must be replaced using the identity: $\sin^2 x = \text{[...]}$.

**Back:** To integrate $\sin^2 x$, it must be replaced using the identity: $\sin^2 x = \boxed{\frac{1-\cos 2x}{2}}$.

**Choices:**

- $$\frac{1-\cos 2x}{2}$ ✔
  - _why:_ The double-angle identity gives $\cos 2x=1-2\sin^2x$. Rearranging yields $\sin^2x=\frac{1-\cos 2x}{2}$, replacing the squared sine with integrable terms.
- $$\frac{1+\cos 2x}{2}$
  - _why:_ The plus form is the identity for $\cos^2x$, not $\sin^2x$. Rearranging the cosine double-angle identity gives $\sin^2x=\frac{1-\cos 2x}{2}$.
- $$1-\cos^2 2x$
  - _why:_ This confuses the half-angle identity with the Pythagorean identity and also uses the wrong angle. The required replacement is $\frac{1-\cos 2x}{2}$.
- $$\frac{1-\cos x}{2}$
  - _why:_ The half-angle identity contains $\cos 2x$, not $\cos x$. Omitting the doubled angle changes the function, so the correct expression is $\frac{1-\cos 2x}{2}$.

## Card 6 — `basic`

**Front:** What trigonometric identity is used to integrate $\cos^2 x$?

**Back:** $$\cos^2 x = \frac{1+\cos 2x}{2}$

**Choices:**

- $$\cos^2 x = \frac{1+\cos 2x}{2}$ ✔
  - _why:_ The double-angle identity $\cos 2x=2\cos^2x-1$ rearranges directly to $\cos^2x=\frac{1+\cos 2x}{2}$, making the square suitable for integration.
- $$\cos^2 x = \frac{1-\cos 2x}{2}$
  - _why:_ The minus form is the half-angle identity for $\sin^2x$. For cosine, rearranging $\cos 2x=2\cos^2x-1$ gives the plus sign.
- $$\cos^2 x = 1-\sin^2 2x$
  - _why:_ The Pythagorean identity uses the same angle, giving $1-\sin^2x$, not $1-\sin^2 2x$. For integration, the relevant half-angle form is $\frac{1+\cos 2x}{2}$.
- $$\cos^2 x = \frac{1+\cos x}{2}$
  - _why:_ The double-angle identity requires the angle $2x$ inside the cosine. Replacing it with $x$ produces a different function, so the correct identity contains $\cos 2x$.

## Card 7 — `cloze`

**Front:** The formula for integration by parts is: $\int u \frac{dv}{dx}\,dx = \text{[...]} - \int v \frac{du}{dx}\,dx$.

**Back:** The formula for integration by parts is: $\int u \frac{dv}{dx}\,dx = \boxed{uv} - \int v \frac{du}{dx}\,dx$.

**Choices:**

- $$uv$ ✔
  - _why:_ Integration by parts follows from the product rule: integrating $u\frac{dv}{dx}$ gives the product $uv$, then subtracts the integral involving the differentiated $u$.
- $$u\frac{du}{dx}$
  - _why:_ The product term must combine $u$ with its antiderivative component $v$, not with $\frac{du}{dx}$. The correct first term is $uv$, followed by the subtraction integral.
- $$v\frac{dv}{dx}$
  - _why:_ This repeats the differentiated component rather than forming the product of the chosen factors. Applying the product rule shows that the boundary product is $uv$.
- $$u+v$
  - _why:_ Integration by parts comes from the product rule, which creates a product rather than a sum. The first term is therefore $uv$, with the remaining integral subtracted.

## Card 8 — `cloze`

**Front:** The formula for integration by parts is: $\int u \frac{dv}{dx}\,dx = uv - \int \text{[...]}\,dx$.

**Back:** The formula for integration by parts is: $\int u \frac{dv}{dx}\,dx = uv - \int \boxed{v \frac{du}{dx}}\,dx$.

**Choices:**

- $$v \frac{du}{dx}$ ✔
  - _why:_ This is the remaining factor produced by integration by parts: choose one function as $u$ and integrate the other to obtain $v$, giving $uv - \int v\frac{du}{dx}\,dx$.
- $$u \frac{dv}{dx}$
  - _why:_ This repeats the original integrand rather than using the differentiated factor after applying the product rule. The required remaining factor is $v\frac{du}{dx}$.
- $$\frac{du}{dx}\frac{dv}{dx}$
  - _why:_ Differentiating both functions introduces an extra derivative and does not follow from the product rule. Integration by parts leaves one integrated factor and one differentiated factor: $v\frac{du}{dx}$.
- $$v \frac{dv}{dx}$
  - _why:_ The derivative must be taken of the function originally labelled $u$, not of the integrated function $v$. Therefore the remaining integrand is $v\frac{du}{dx}$.

## Card 9 — `basic`

**Front:** In the integral $\int x\sin x\,dx$, which term should be chosen as $u$ for integration by parts?

**Back:** $$u = x$

**Choices:**

- $$u = x$ ✔
  - _why:_ Choosing $u=x$ makes $du=dx$, while integrating $sin x$ is straightforward. Integration by parts then reduces the integral to simpler terms.
- $$u = \sin x$
  - _why:_ Choosing the trigonometric factor as $u$ does not simplify the integral, because differentiating it leaves a product involving $x$. The useful choice is $u=x$, giving $du=dx$.
- $$u = x\sin x$
  - _why:_ Choosing the entire integrand as $u$ leaves no helpful factor for $dv$ and makes differentiation more complicated. Instead, take $u=x$ so differentiation removes the algebraic factor.
- $$u = \cos x$
  - _why:_ Cosine is not a factor in the original integrand, so it cannot be selected directly as $u$. The algebraic factor $x$ should be chosen because it differentiates to $1$.

## Card 10 — `basic`

**Front:** When performing a definite integral by substitution, what must be done with the limits?

**Back:** Convert the $x$ limits into $u$ values using the substitution equation.

**Choices:**

- Convert the $x$ limits into $u$ values using the substitution equation. ✔
  - _why:_ After changing the variable of integration from $x$ to $u$, the bounds must also use $u$. Substituting each original $x$ limit into the substitution equation gives the new limits.
- Keep the $x$ limits unchanged after applying the substitution equation.
  - _why:_ Keeping limits expressed in $x$ while integrating with respect to $u$ mixes variables and is invalid. Each $x$ limit must be converted using the substitution equation.
- Convert the $u$ limits into $x$ values using the substitution equation.
  - _why:_ The substitution equation converts original $x$ bounds into new $u$ bounds, not the reverse. Both limits must be evaluated as $u$ values before applying them.
- Convert only the upper $x$ limit using the substitution equation.
  - _why:_ Changing only one bound leaves the definite integral with limits in different variables. Both the lower and upper $x$ limits must be converted into corresponding $u$ values.

## Card 11 — `basic`

**Front:** When must algebraic division be performed before using partial fractions for integration?

**Back:** When the degree of the numerator is greater than or equal to the degree of the denominator.

**Choices:**

- When the degree of the numerator is greater than or equal to the degree of the denominator. ✔
  - _why:_ Partial fractions require a proper rational expression. If the numerator’s degree is at least the denominator’s degree, division first produces a polynomial plus a proper fraction.
- When the degree of the numerator is less than the degree of the denominator.
  - _why:_ A fraction with a lower-degree numerator is already proper, so algebraic division is unnecessary. Division is required when the numerator’s degree is greater than or equal to the denominator’s.
- When the degree of the denominator is greater than or equal to the degree of the numerator.
  - _why:_ This reverses the condition for an improper rational expression. Algebraic division is needed when the numerator’s degree is greater than or equal to the denominator’s degree.
- When the degree of the numerator is exactly equal to the degree of the denominator.
  - _why:_ Equal degrees do require algebraic division, but the condition is not restricted to equality. Division is also needed whenever the numerator has a higher degree than the denominator.

## Card 12 — `basic`

**Front:** Why are modulus signs used in the result $\ln|x+a|$?

**Back:** To ensure the argument of the natural logarithm is positive, as $\ln$ is undefined for negative numbers.

**Choices:**

- To ensure the argument of the natural logarithm is positive, as $\ln$ is undefined for negative numbers. ✔
  - _why:_ The real natural logarithm requires a positive argument. The modulus makes both positive and negative values of $x+a$ contribute through their positive magnitude, excluding $x=-a$.
- To ensure the value of the natural logarithm is positive, as $\ln$ cannot produce negative numbers.
  - _why:_ A natural logarithm can have a negative value when its positive argument lies between $0$ and $1$. The modulus instead ensures that the logarithm’s argument is positive.
- To ensure the natural logarithm is continuous, as $\ln$ is undefined at stationary points.
  - _why:_ The modulus does not make the antiderivative continuous at $x=-a$; the integrand and logarithm are undefined there. It ensures the logarithm receives a positive argument.
- To ensure the constant of integration is unnecessary, as $\ln$ already includes all possible values.
  - _why:_ Modulus signs do not remove the arbitrary integration constant, which must still be included in an indefinite integral. Their purpose is to keep the logarithm’s argument positive.

## Card 13 — `basic`

**Front:** How is the area between an upper curve $y_1$ and a lower curve $y_2$ calculated?

**Back:** Integrate the difference: $\int (y_1 - y_2)\,dx$.

**Choices:**

- Integrate the difference: $\int (y_1 - y_2)\,dx$. ✔
  - _why:_ At each $x$-value, the vertical separation is the upper height minus the lower height. Integrating this non-negative difference across the relevant interval gives the enclosed area.
- Integrate the difference: $\int (y_2 - y_1)\,dx$.
  - _why:_ Reversing the subtraction makes the integrand negative wherever $y_1$ is above $y_2$, producing the negative of the required area. Subtract the lower curve from the upper curve.
- Integrate the sum: $\int (y_1 + y_2)\,dx$.
  - _why:_ Adding the curve heights measures their combined displacement from the axis, not the vertical separation between them. The required integrand is upper curve minus lower curve.
- Integrate the product: $\int (y_1y_2)\,dx$.
  - _why:_ Multiplying the two heights does not represent the vertical distance between the curves and gives inappropriate dimensions. Their separation is $y_1-y_2$, which must be integrated.

## Card 14 — `cloze`

**Front:** The formula for the area under a parametric curve is $A = \int \text{[...]}\,dt$.

**Back:** The formula for the area under a parametric curve is $A = \int \boxed{y(t) \frac{dx}{dt}}\,dt$.

**Choices:**

- $$y(t) \frac{dx}{dt}$ ✔
  - _why:_ For a parametrisation $x=x(t)$ and $y=y(t)$, substitute $dx=(dx/dt)dt$ into $A=\int y\,dx$. This gives the parametric area integrand $y(t)(dx/dt)$.
- $$y(t) \frac{dy}{dt}$
  - _why:_ Using $dy/dt$ corresponds to integrating $y\,dy$, not the area expression $\int y\,dx$. The required conversion is $dx=(dx/dt)dt$, giving $y(t)(dx/dt)$.
- $$x(t) \frac{dx}{dt}$
  - _why:_ The area under a curve is based on height $y$ multiplied by a horizontal change $dx$. Replacing the height with $x(t)$ does not represent $\int y\,dx$.
- $$y(t) \frac{dt}{dx}$
  - _why:_ Changing variables uses $dx=(dx/dt)dt$, so the derivative must not be inverted. The reciprocal $dt/dx$ gives the wrong scaling of each parametric interval.

## Card 15 — `basic`

**Front:** What makes a differential equation separable?

**Back:** It can be rearranged to isolate all $y$ terms on one side with $dy$ and all $x$ terms on the other with $dx$.

**Choices:**

- It can be rearranged to isolate all $y$ terms on one side with $dy$ and all $x$ terms on the other with $dx$. ✔
  - _why:_ Separation places every factor involving $y$ alongside $dy$ and every factor involving $x$ alongside $dx$. Each side can then be integrated independently in its own variable.
- It can be rearranged to combine all $x$ and $y$ terms on one side with $dy$ and leave only constants with $dx$.
  - _why:_ Having both variables on one side does not permit separate integration and is the opposite of separation. A separable equation must group $y$ terms with $dy$ and $x$ terms with $dx$.
- It can be rearranged so that the derivative is constant and all $x$ and $y$ terms appear on the same side.
  - _why:_ A constant derivative describes a particularly simple differential equation, but it is not the defining condition. Separability depends on rearranging variable factors onto opposite sides with their differentials.
- It can be rearranged into a linear form with all $y$ terms on one side and the derivative on the other side.
  - _why:_ Writing an equation in the standard linear form identifies a first-order linear equation, not necessarily a separable one. Separation specifically groups $y$ terms with $dy$ and $x$ terms with $dx$.

## Card 16 — `basic`

**Front:** Why does the trapezium rule produce an overestimate for concave-up curves?

**Back:** The straight chords of the trapezia lie above the actual curve.

**Choices:**

- The straight chords of the trapezia lie above the actual curve. ✔
  - _why:_ For a concave-up curve, each secant chord between adjacent points lies above the graph. The trapezia therefore include extra area, making their total an overestimate.
- The straight chords of the trapezia lie below the actual curve.
  - _why:_ Chords of a concave-up curve lie above, not below, the graph. If they lay below, the trapezium rule would underestimate rather than overestimate the area.
- The straight tangents of the trapezia lie above the actual curve.
  - _why:_ The trapezium rule uses secant chords joining endpoint values, not tangent lines. For concave-up curves these chords lie above the graph, creating the overestimate.
- The straight tangents of the trapezia lie below the actual curve.
  - _why:_ Tangent lines are not used to form the trapezia, and tangents to a concave-up curve generally lie below it. The overestimate comes from chords lying above the curve.

## Card 17 — `basic`

**Front:** When does the trapezium rule produce an underestimate of the area?

**Back:** When the curve is concave-down.

**Choices:**

- When the curve is concave-down. ✔
  - _why:_ For a concave-down curve, each joining chord lies below the curve, so the trapezia omit some of the region and underestimate the true area.
- When the curve is concave-up.
  - _why:_ For a concave-up curve, the joining chords lie above the curve, producing an overestimate. An underestimate occurs when the curve is concave-down.
- When the curve is a straight line.
  - _why:_ A straight-line graph has no curvature, so the trapezium rule gives its area exactly. An underestimate occurs for a concave-down curve.
- When the joining chords lie above the curve.
  - _why:_ Chords above the curve make the trapezia larger than the true region, giving an overestimate. For an underestimate, the curve must be concave-down.

## Card 18 — `basic`

**Front:** How should you handle a negative result when calculating area using a parametric integral?

**Back:** Take the absolute (positive) value or reverse the limits of integration.

**Choices:**

- Take the absolute (positive) value or reverse the limits of integration. ✔
  - _why:_ A definite integral gives signed area, so a negative result indicates orientation rather than negative geometric area. Taking its absolute value or reversing the limits makes the area positive.
- Keep the negative value because integration gives a signed area.
  - _why:_ A negative integral represents signed area, but geometric area must be non-negative. Take the absolute value of the result or reverse the integration limits.
- Square the negative result to make the calculated area positive.
  - _why:_ Squaring changes the magnitude and gives incorrect units, so it does not convert signed area correctly. Take the absolute value or reverse the limits instead.
- Change the sign of the parameter but keep the original limits.
  - _why:_ Changing the parameter’s sign does not generally reverse the direction in which the curve is traced. Take the absolute value or reverse the integration limits.

## Card 19 — `basic`

**Front:** What is the integral of $\sec^2(ax)$ with respect to $x$?

**Back:** $$\frac{1}{a}\tan(ax)+c$

**Choices:**

- $$\frac{1}{a}\tan(ax)+c$ ✔
  - _why:_ Since the derivative of $\tan(ax)$ is $a\sec^2(ax)$, multiplying by $\frac{1}{a}$ compensates for the chain-rule factor.
- $$\tan(ax)+c$
  - _why:_ This misses the reciprocal chain-rule factor. Differentiating $\tan(ax)$ introduces a factor of $a$, so the integral is $\frac{1}{a}\tan(ax)+c$.
- $$a\tan(ax)+c$
  - _why:_ This multiplies by the inner derivative instead of dividing by it. The reverse chain rule gives $\frac{1}{a}\tan(ax)+c$, not an additional factor of $a$.
- $$\frac{1}{a}\sec(ax)+c$
  - _why:_ The antiderivative involves tangent because $\frac{d}{dx}\tan(ax)=a\sec^2(ax)$. Therefore the correct result is $\frac{1}{a}\tan(ax)+c$.

## Card 20 — `basic`

**Front:** What are the three components of the trapezium rule formula?

**Back:** $\frac{h}{2}$ (half the strip width)The sum of the first and last ordinatesTwice the sum of the remaining interior ordinates

**Choices:**

- $\frac{h}{2}$ (half the strip width)The sum of the first and last ordinatesTwice the sum of the remaining interior ordinates ✔
  - _why:_ The trapezium rule multiplies half the common strip width by the two endpoint ordinates plus twice every interior ordinate, matching the areas of adjacent trapezia.
- $h$ (the full strip width)The sum of the first and last ordinatesTwice the sum of the remaining interior ordinates
  - _why:_ Using $h$ instead of $\frac{h}{2}$ doubles every trapezium’s calculated area. The correct outside factor is half the strip width.
- $\frac{h}{2}$ (half the strip width)Twice the sum of the first and last ordinatesThe sum of the remaining interior ordinates
  - _why:_ This reverses the endpoint and interior weights. Endpoints occur in one trapezium each, while interior ordinates occur in two, so only the interior sum is doubled.
- $\frac{h}{2}$ (half the strip width)The sum of the first and last ordinatesFour times the sum of the remaining interior ordinates
  - _why:_ A factor of four is associated with some terms in Simpson’s rule, not the trapezium rule. Every interior ordinate must instead have weight two.

## Card 21 — `basic`

**Front:** What is the derivative of $\operatorname{cosec}(ax)$?

**Back:** $$-a\operatorname{cosec}(ax)\cot(ax)$

**Choices:**

- $$-a\operatorname{cosec}(ax)\cot(ax)$ ✔
  - _why:_ The derivative of $\operatorname{cosec}(u)$ is $-\operatorname{cosec}(u)\cot(u)$. With $u=ax$, the chain rule supplies the additional factor $a$.
- $$a\operatorname{cosec}(ax)\cot(ax)$
  - _why:_ The derivative of cosecant has a negative sign. Applying the chain rule gives $-a\operatorname{cosec}(ax)\cot(ax)$, including both the minus sign and factor $a$.
- $$-\frac{1}{a}\operatorname{cosec}(ax)\cot(ax)$
  - _why:_ Differentiation multiplies by the inner derivative $a$ rather than dividing by it. The reciprocal factor is a reverse-chain-rule error associated with integration.
- $$-a\operatorname{cosec}^2(ax)$
  - _why:_ The expression $-a\operatorname{cosec}^2(ax)$ is the derivative of $\cot(ax)$. Differentiating cosecant instead gives $-a\operatorname{cosec}(ax)\cot(ax)$.
