# Numerical Methods Flashcards

_Lane: `a-level-maths-edexcel` · grade — · 23 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** State the two conditions required for a sign change between $x=a$ and $x=b$ to guarantee at least one root.

**Back:** The function $f(x)$ is continuous on $[a,b]$$f(a)$ and $f(b)$ have opposite signs

**Choices:**

- The function $f(x)$ is continuous on $[a,b]$$f(a)$ and $f(b)$ have opposite signs ✔
  - _why:_ The Intermediate Value Theorem applies when the function is continuous on the whole interval and the endpoint values have opposite signs, forcing the graph to cross the x-axis.
- The function $f(x)$ is discontinuous on $[a,b]$$f(a)$ and $f(b)$ have opposite signs
  - _why:_ Opposite endpoint signs alone are insufficient because a discontinuity could jump from positive to negative without crossing the x-axis. Continuity on $[a,b]$ is also required.
- The function $f(x)$ is continuous on $[a,b]$$f(a)$ and $f(b)$ have the same sign
  - _why:_ Continuity is necessary, but equal endpoint signs do not force a crossing. The required endpoint condition is that $f(a)$ and $f(b)$ have opposite signs.
- The function $f(x)$ is continuous on $(a,b)$$f(a)$ and $f(b)$ are equal
  - _why:_ Having equal endpoint values does not guarantee a root, even when the function is continuous. The endpoints must have opposite signs so the graph is forced through zero.

## Card 2 — `cloze`

**Front:** The sign-change test can only be used to guarantee a root if the function has no [ ___ ] (it is continuous).

**Back:** The sign-change test can only be used to guarantee a root if the function has no jumps or breaks (it is continuous).

**Choices:**

- jumps or breaks ✔
  - _why:_ A sign change guarantees a root only under continuity. Jumps or breaks can let a function move between opposite signs without actually taking the value zero.
- turning points
  - _why:_ Turning points do not necessarily prevent continuity; a continuous curve may have many turning points. Jumps or breaks are the features that invalidate the sign-change guarantee.
- negative values
  - _why:_ Negative values can occur in a continuous function and do not stop the graph crossing zero. The relevant obstruction is a jump or break in the function.
- vertical asymptotes
  - _why:_ A vertical asymptote indicates a discontinuity, but excluding only asymptotes does not exclude all jumps or breaks. Continuity requires no discontinuities throughout the interval.

## Card 3 — `basic`

**Front:** Does a lack of sign change between $f(a)$ and $f(b)$ prove that no root exists in the interval $[a,b]$? Why?

**Back:** No. The curve could touch the x-axis or cross it an even number of times.

**Choices:**

- No. The curve could touch the x-axis or cross it an even number of times. ✔
  - _why:_ No sign change means the test is inconclusive, not that there is no root. The curve could touch the x-axis or cross it an even number of times.
- Yes. A root requires $f(a)$ and $f(b)$ to have opposite signs.
  - _why:_ A root can exist even without an endpoint sign change, for example when the curve touches the x-axis. The correct answer is no because roots can also occur an even number of times.
- Yes. The curve stays entirely above or entirely below the x-axis.
  - _why:_ The endpoint signs do not determine every possible crossing inside the interval. The correct answer is no because the curve may touch the x-axis or cross it an even number of times.
- No. The function must be discontinuous somewhere in the interval.
  - _why:_ A lack of sign change does not imply the curve is discontinuous. The correct answer is no because a continuous curve can touch the axis or cross it an even number of times.

## Card 4 — `cloze`

**Front:** A sign change between $f(a)$ and $f(b)$ proves the existence of at least [ ___ ] in that interval.

**Back:** A sign change between $f(a)$ and $f(b)$ proves the existence of at least one root in that interval.

**Choices:**

- one root ✔
  - _why:_ For a continuous function, opposite signs at the endpoints force the graph to pass through $y=0$ at least once, so there is at least one root in the interval.
- two roots
  - _why:_ A sign change guarantees an odd number of crossings, but it does not guarantee at least two roots; the graph may cross the x-axis exactly once.
- one stationary point
  - _why:_ A turning point is not necessarily on the x-axis and is unrelated to the sign-change conclusion. The guaranteed object is at least one root.
- one maximum value
  - _why:_ The Intermediate Value Theorem guarantees that the function reaches zero, not that it reaches a maximum. The correct conclusion is the existence of at least one root.

## Card 5 — `basic`

**Front:** What is the first step in using a numerical method to find the $x$-coordinate of a stationary point?

**Back:** Set the first derivative to zero: $\frac{dy}{dx} = 0$.

**Choices:**

- Set the first derivative to zero: $\frac{dy}{dx} = 0$. ✔
  - _why:_ A stationary point has a horizontal tangent, so its gradient is zero. The first step is therefore to differentiate and solve the equation $rac{dy}{dx}=0$.
- Set the function to zero: $y = 0$.
  - _why:_ Setting the function itself to zero finds x-intercepts, not generally stationary points. Stationary points are found by setting the first derivative, $rac{dy}{dx}$, to zero.
- Set the second derivative to zero: $\frac{d^2y}{dx^2} = 0$.
  - _why:_ The second derivative helps classify a stationary point after it has been found. The initial condition for locating it is $rac{dy}{dx}=0$.
- Set the first derivative to one: $\frac{dy}{dx} = 1$.
  - _why:_ A stationary point requires zero gradient, not a gradient of one. The equation to solve first is $rac{dy}{dx}=0$, before any classification is attempted.

## Card 6 — `cloze`

**Front:** In fixed-point iteration, the solutions are found at the intersection of the graphs $\text{[...]}$ and $y = g(x)$.

**Back:** In fixed-point iteration, the solutions are found at the intersection of the graphs $\boxed{y = x}$ and $y = g(x)$.

**Choices:**

- $$y = x$ ✔
  - _why:_ Fixed points satisfy $x=g(x)$, so their coordinates lie on both $y=x$ and $y=g(x)$. The solutions are therefore found at the intersections of these graphs.
- $$y = -x$
  - _why:_ The graph $y=-x$ represents reflection in the origin rather than the fixed-point condition. Fixed points require the input and output to be equal, giving $y=x$.
- $$y = f(x)$
  - _why:_ The original function $f(x)$ is not generally the graph used to display the fixed-point iteration. The relevant comparison is between $y=x$ and $y=g(x)$.
- $$y = x^2$
  - _why:_ The parabola $y=x^2$ does not express the fixed-point condition for a general iteration. Fixed points occur where $x=g(x)$, represented by $y=x$.

## Card 7 — `cloze`

**Front:** In fixed-point iteration, the solutions are found at the intersection of the graphs $y = x$ and $\text{[...]}$.

**Back:** In fixed-point iteration, the solutions are found at the intersection of the graphs $y = x$ and $\boxed{y = g(x)}$.

**Choices:**

- $$y = g(x)$ ✔
  - _why:_ A fixed point satisfies $x=g(x)$, meaning its y-coordinate equals its x-coordinate. Hence it lies on $y=x$ as well as on the iteration graph $y=g(x)$.
- $$y = f(x)$
  - _why:_ The graph $y=f(x)$ belongs to the original function, not necessarily to the rearranged iteration formula. Fixed-point solutions are found by intersecting $y=x$ with $y=g(x)$.
- $$y = -g(x)$
  - _why:_ The line $y=-g(x)$ reverses the output values and does not represent the iteration formula. The required graph is exactly $y=g(x)$.
- $$y = x + g(x)$
  - _why:_ The graph $y=x+g(x)$ is not the iteration function and would give a different intersection equation. Fixed-point iteration uses the graph $y=g(x)$.

## Card 8 — `basic`

**Front:** When using an iteration formula like $x_{n+1}=g(x_n)$, why should you use the calculator's 'ANS' key?

**Back:** To maintain full accuracy and avoid rounding errors between steps.

**Choices:**

- To maintain full accuracy and avoid rounding errors between steps. ✔
  - _why:_ The ANS key carries the calculator's unrounded previous result into the next iteration. This preserves full accuracy and prevents rounding errors from accumulating through repeated steps.
- To round each answer consistently between steps.
  - _why:_ Rounding each iterate before using it loses precision and can cause later values to drift. The ANS key is used to retain the previous unrounded result.
- To guarantee that the iteration converges to a root.
  - _why:_ The ANS key does not make the iteration converge; convergence depends on the iteration function and starting value. It mainly prevents intermediate rounding errors.
- To differentiate the iteration formula automatically between steps.
  - _why:_ Using ANS does not calculate the derivative or replace the iteration formula. It transfers the previous full-precision output into the next calculation.

## Card 9 — `basic`

**Front:** To prove a root is $0.673$ to 3 decimal places, what interval of $x$ values must you test for a sign change?

**Back:** $$[0.6725, 0.6735]$

**Choices:**

- $$[0.6725, 0.6735]$ ✔
  - _why:_ Rounding to three decimal places gives a half-unit tolerance of $0.0005$. Therefore, the lower and upper rounding bounds are $0.6725$ and $0.6735$.
- $$[0.672, 0.674]$
  - _why:_ Using $0.001$ on either side makes the interval too wide. Three-decimal-place rounding requires half of $0.001$, giving the correct interval $[0.6725, 0.6735]$.
- $$[0.673, 0.674]$
  - _why:_ These are adjacent three-decimal values rather than the rounding bounds. The required endpoints lie halfway between them, so the correct interval is $[0.6725, 0.6735]$.
- $$[0.6725, 0.6734]$
  - _why:_ The upper endpoint has been truncated instead of placed halfway between $0.673$ and $0.674$. The correct upper bound is $0.6735$, giving $[0.6725, 0.6735]$.

## Card 10 — `cloze`

**Front:** To prove a root $\alpha$ is correct to a given accuracy, you must show a sign change occurs between the [ ___ ] of that rounded value.

**Back:** To prove a root $\alpha$ is correct to a given accuracy, you must show a sign change occurs between the upper and lower bounds of that rounded value.

**Choices:**

- upper and lower bounds ✔
  - _why:_ Every number that rounds to the stated value lies between its upper and lower bounds. Opposite signs at these endpoints prove that a root lies within the required accuracy interval.
- two nearest integers
  - _why:_ The nearest integers are unrelated to the specified rounding accuracy and usually create a much wider interval. The sign change must be shown between the upper and lower bounds.
- midpoint and upper bound
  - _why:_ A midpoint and one bound cover only part of the interval containing all values that round to the result. Both the upper and lower bounds must be tested.
- rounded value and error
  - _why:_ The rounded value and its error do not themselves form the two endpoints of the rounding interval. The required endpoints are the upper and lower bounds.

## Card 11 — `basic`

**Front:** What condition for the gradient $g'(x)$ usually guarantees that a fixed-point iteration will converge?

**Back:** $$|g'(x)| < 1$ near the root.

**Choices:**

- $$|g'(x)| < 1$ near the root. ✔
  - _why:_ When $|g'(x)|<1$, the iteration mapping contracts distances near the fixed point. Successive approximations therefore tend to move closer to the root.
- $$|g'(x)| > 1$ near the root.
  - _why:_ A gradient magnitude greater than one magnifies small errors, so successive iterates generally move away from the fixed point. Convergence usually requires $|g'(x)|<1$ near the root.
- $$g'(x) < 1$ near the root.
  - _why:_ A derivative below one without an absolute value may still have magnitude greater than one, such as $g'(x)=-2$. The required condition is $|g'(x)|<1$.
- $$g'(x) > 0$ near the root.
  - _why:_ A positive gradient alone does not ensure contraction because it could exceed one. The usual convergence condition controls the magnitude: $|g'(x)|<1$ near the root.

## Card 12 — `cloze`

**Front:** If $|g'(x)| > 1$ near a root, the fixed-point iteration is likely to [ ___ ].

**Back:** If $|g'(x)| > 1$ near a root, the fixed-point iteration is likely to diverge.

**Choices:**

- diverge ✔
  - _why:_ A gradient magnitude greater than one magnifies deviations from the fixed point at each iteration. Consequently, successive approximations are likely to move away rather than approach the root.
- converge
  - _why:_ Convergence is normally expected when $|g'(x)|1$, errors grow, so the iteration is likely to diverge.
- stabilise
  - _why:_ A negative derivative can make iterates alternate, but $|g'(x)|>1$ makes the size of their errors grow rather than stabilise. The iteration is therefore likely to diverge.
- remain constant
  - _why:_ Iterates remain constant only if an iterate is already exactly at a fixed point. In general, $|g'(x)|>1$ amplifies errors and makes the iteration diverge.

## Card 13 — `basic`

**Front:** What are the two types of diagrams used to visualize fixed-point iteration?

**Back:** Cobweb diagramsStaircase diagrams

**Choices:**

- Cobweb diagramsStaircase diagrams ✔
  - _why:_ Cobweb diagrams are used when the iteration alternates across the line $y=x$, while staircase diagrams show a step-like approach. Both visualise repeated applications of $x_{n+1}=g(x_n)$.
- Tangent diagramsNormal diagrams
  - _why:_ Tangent and normal lines describe local geometry of curves, not the standard graphical forms of fixed-point iteration. Those forms are cobweb diagrams and staircase diagrams.
- Trapezium diagramsMidpoint diagrams
  - _why:_ Trapezium and midpoint refer to numerical integration rules rather than fixed-point iteration diagrams. Iterative movement between $y=g(x)$ and $y=x$ is shown by cobweb or staircase diagrams.
- Bisection diagramsInterval diagrams
  - _why:_ Bisection and interval methods locate roots using sign-changing intervals, but they are not the two standard fixed-point diagrams. These are cobweb diagrams and staircase diagrams.

## Card 14 — `basic`

**Front:** State the Newton-Raphson formula for finding a root of $f(x)=0$.

**Back:** $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$

**Choices:**

- $$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ ✔
  - _why:_ The tangent at $x_n$ has gradient $f'(x_n)$, and its $x$-intercept is obtained by subtracting the correction $rac{f(x_n)}{f'(x_n)}$ from $x_n$.
- $$x_{n+1} = x_n + \frac{f(x_n)}{f'(x_n)}$
  - _why:_ The tangent’s $x$-intercept requires subtracting the correction, not adding it. Newton-Raphson therefore uses $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$.
- $$x_{n+1} = x_n - \frac{f'(x_n)}{f(x_n)}$
  - _why:_ This reverses the Newton correction fraction. Solving the tangent equation for its $x$-intercept gives the function value divided by the derivative, so $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$.
- $$x_{n+1} = x_n - \frac{f(x_{n+1})}{f'(x_n)}$
  - _why:_ Newton-Raphson evaluates both the function and its derivative at the current approximation $x_n$. Using $f(x_{n+1})$ makes the update implicit rather than the Newton-Raphson formula.

## Card 15 — `cloze`

**Front:** The Newton-Raphson method works by finding where the [ ___ ] to the curve at $x_n$ intersects the $x$-axis.

**Back:** The Newton-Raphson method works by finding where the tangent to the curve at $x_n$ intersects the $x$-axis.

**Choices:**

- tangent ✔
  - _why:_ Newton-Raphson replaces the curve locally with its tangent at the current estimate. The tangent’s intersection with the $x$-axis supplies the next estimate $x_{n+1}$.
- secant
  - _why:_ A secant uses two points and leads to the secant method, not standard Newton-Raphson. Newton-Raphson uses the tangent at the single current estimate $x_n$.
- normal
  - _why:_ The normal is perpendicular to the tangent and does not produce the Newton-Raphson update. The method follows the tangent at $x_n$ to the $x$-axis.
- chord
  - _why:_ A chord joins two points on the curve and is associated with two-point root-finding approaches. Newton-Raphson instead uses the tangent at the current estimate.

## Card 16 — `cloze`

**Front:** The Newton-Raphson method works by finding where the tangent to the curve at $x_n$ intersects the [ ___ ].

**Back:** The Newton-Raphson method works by finding where the tangent to the curve at $x_n$ intersects the $x$-axis.

**Choices:**

- $$x$-axis ✔
  - _why:_ A root of $f(x)=0$ lies on the $x$-axis. Newton-Raphson therefore uses the tangent’s $x$-axis intersection as the next approximation to the root.
- $$y$-axis
  - _why:_ The curve’s intersection with the $y$-axis corresponds to $x=0$, not generally to a root. Newton-Raphson takes the tangent’s intersection with the $x$-axis.
- line $y=x$
  - _why:_ The line $y=x$ is used to visualise fixed-point iteration $x_{n+1}=g(x_n)$. Newton-Raphson instead finds where the tangent intersects the $x$-axis.
- curve $y=f(x)$
  - _why:_ The tangent already meets the original curve at $x_n$, so that intersection supplies no new approximation. The next estimate comes from its intersection with the $x$-axis.

## Card 17 — `basic`

**Front:** Under what specific condition will the Newton-Raphson method fail numerically?

**Back:** When $f'(x_n) = 0$ (the gradient is zero / stationary point).

**Choices:**

- When $f'(x_n) = 0$ (the gradient is zero / stationary point). ✔
  - _why:_ Newton-Raphson divides by $f'(x_n)$ when calculating the next iterate. If the gradient is zero, the formula involves division by zero and cannot produce a numerical value.
- When $f(x_n) = 0$ (the iterate is already a root).
  - _why:_ Having $f(x_n)=0$ means the current iterate is already an exact root, so no further iteration is needed. Failure occurs when $f'(x_n)=0$, because the formula then divides by zero.
- When $f''(x_n) = 0$ (the curvature is zero / inflection point).
  - _why:_ Zero curvature does not itself make the standard Newton-Raphson calculation undefined. Numerical failure occurs when $f'(x_n)=0$, since the derivative appears in the denominator.
- When $f'(x_n) = 1$ (the gradient is non-zero).
  - _why:_ A gradient of one gives a valid, non-zero denominator, so the next iterate can be calculated. The method fails numerically when $f'(x_n)=0$.

## Card 18 — `basic`

**Front:** Why does the Newton-Raphson method fail if $f'(x_n) = 0$?

**Back:** The formula requires division by the derivative; division by zero is undefined.

**Choices:**

- The formula requires division by the derivative; division by zero is undefined. ✔
  - _why:_ Newton-Raphson uses $x_{n+1}=x_n-f(x_n)/f'(x_n)$. If $f'(x_n)=0$, its quotient has a zero denominator, so the next iterate is undefined.
- The formula requires multiplication by the derivative; multiplying by zero prevents convergence.
  - _why:_ The derivative is used as a divisor, not as a multiplying factor. When $f'(x_n)=0$, division by the derivative is undefined, so no next iterate can be calculated.
- The formula requires taking the square root of the derivative; square roots of zero are undefined.
  - _why:_ Newton-Raphson does not take the square root of the derivative, and the square root of zero is defined. It fails because it divides by the zero derivative.
- The formula requires division by the function value; division by zero is undefined.
  - _why:_ The function value is the numerator, while the derivative is the denominator. A zero derivative therefore causes undefined division, whereas a zero function value indicates a root.

## Card 19 — `cloze`

**Front:** When using numerical methods involving trigonometry in calculus, the calculator must be in [ ___ ] mode.

**Back:** When using numerical methods involving trigonometry in calculus, the calculator must be in radians mode.

**Choices:**

- radians ✔
  - _why:_ Calculus formulas for trigonometric derivatives, such as the derivative of $sin x$ being $cos x$, assume angles are measured in radians. Numerical calculations must therefore use radians mode.
- degrees
  - _why:_ Degrees introduce an additional conversion factor into trigonometric derivatives, so standard calculus formulas do not apply directly. The calculator must be set to radians mode.
- gradians
  - _why:_ Gradians divide a full turn into 400 units and introduce a conversion factor in differentiation. Standard trigonometric calculus and its numerical methods require radians mode.
- turns
  - _why:_ Turns are not the angular unit assumed by standard trigonometric derivative formulas. Those formulas are valid in their usual form only when the calculator uses radians.

## Card 20 — `basic`

**Front:** How is the Newton-Raphson formula modified to find a stationary point of $y=f(x)$?

**Back:** $$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}$

**Choices:**

- $$x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)}$ ✔
  - _why:_ A stationary point satisfies $f'(x)=0$. Applying Newton-Raphson to the function $f'(x)$ gives derivative $f''(x)$ and hence the stated iteration.
- $$x_{n+1} = x_n - rac{f(x_n)}{f'(x_n)}$
  - _why:_ This is the ordinary Newton-Raphson formula for solving $f(x)=0$, so it locates roots of the original function rather than stationary points where $f'(x)=0$.
- $$x_{n+1} = x_n + rac{f'(x_n)}{f''(x_n)}$
  - _why:_ Applying Newton-Raphson to $f'(x)=0$ requires subtracting the correction term. Using addition moves in the opposite direction and does not give the required iteration formula.
- $$x_{n+1} = x_n - rac{f''(x_n)}{f'(x_n)}$
  - _why:_ The Newton-Raphson correction is the target function divided by its derivative. For $f'(x)=0$, that means $f'(x_n)/f''(x_n)$, not the inverted quotient.

## Card 21 — `basic`

**Front:** A question asks for a root to 3 decimal places. When can you stop iterating?

**Back:** When two successive iterates round to the same value to 3 decimal places.

**Choices:**

- When two successive iterates round to the same value to 3 decimal places. ✔
  - _why:_ Matching rounded values for two consecutive approximations indicates that the iteration has stabilised at the requested precision. Both iterates therefore support the same 3-decimal-place answer.
- When two successive iterates round to the same value to 3 significant figures.
  - _why:_ Three significant figures and three decimal places are different accuracy requirements, especially for values away from one. The successive iterates must agree when rounded to 3 decimal places.
- When two successive iterates differ by less than 0.001.
  - _why:_ A difference below $0.001$ does not guarantee equal rounding to 3 decimal places because the values could lie on opposite sides of a rounding boundary. Their rounded values must match.
- When the first iterate can be rounded to 3 decimal places.
  - _why:_ Every finite calculator value can be rounded, so rounding one iterate alone gives no evidence of convergence. Two successive iterates must round to the same 3-decimal-place value.

## Card 22 — `cloze`

**Front:** Polynomials, exponentials, and sines are [ ___ ] everywhere, but logarithms are only continuous on their valid domains ($x > 0$) domain.

**Back:** Polynomials, exponentials, and sines are continuous everywhere, but logarithms are only continuous on their valid domains ($x > 0$) domain.

**Choices:**

- continuous ✔
  - _why:_ These functions have no breaks, jumps or gaps for real inputs in their domains. Logarithms are likewise continuous wherever defined, but their real domain requires $x>0$.
- discontinuous
  - _why:_ Polynomials, exponentials and sines are not discontinuous on the real line; they have no breaks there. The required property is continuous, with logarithms restricted to $x>0$.
- undefined
  - _why:_ Polynomials, exponentials and sine functions are defined for every real input, so describing them as undefined everywhere reverses the fact. The missing term is continuous.
- periodic
  - _why:_ Only sine among the listed functions is periodic; general polynomials and exponentials do not repeat at fixed intervals. All three are instead continuous everywhere.

## Card 23 — `cloze`

**Front:** Polynomials, exponentials, and sines are continuous everywhere, but [ ___ ] are only continuous on their valid domains ($x > 0$) domain.

**Back:** Polynomials, exponentials, and sines are continuous everywhere, but logarithms are only continuous on their valid domains ($x > 0$) domain.

**Choices:**

- logarithms ✔
  - _why:_ Real logarithmic functions require a positive argument, so their domain is $x>0$. They are continuous at every point within that valid domain.
- square roots
  - _why:_ Square-root functions are continuous on $xge 0$, including at zero, so $x>0$ is not their complete valid domain. The stated restriction belongs to logarithms.
- reciprocal functions
  - _why:_ A basic reciprocal function is defined and continuous for both positive and negative inputs, excluding zero. The domain $x>0$ instead characterises real logarithms.
- cosines
  - _why:_ Cosine functions are defined and continuous for every real value, just like sine functions. Logarithms are the functions restricted to the positive real domain $x>0$.
