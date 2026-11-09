# a-level-pure-mathematics-10-numerical-methods — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Roots, continuity and sign changes

![Continuous curve crossing the x-axis between x equals 1 and x equals 1.5, with f(1) below the axis and f(1.5) above it](../assets/001-e0b8be38-b602-4a13-81dd-f69e77873efc.jpeg)

A root of $f(x)=0$ is an $x$ value where the graph has height 0, so it meets the $x$-axis. Numerical methods help when an equation mixes algebraic, exponential, logarithmic or trigonometric terms and exact solving is awkward.

If $f(x)$ is continuous on $[a,b]$ and $f(a)$ and $f(b)$ have opposite signs, there is at least one root between $a$ and $b$. This sign-change test proves existence of a root, but it does not prove there is exactly one.

In an exam, write the two endpoint values, state that the function is continuous, and then mention the sign change clearly. That full chain of reasoning is what justifies the interval.

## Fixed-point iteration

To use fixed-point iteration, rearrange an equation into the form $x=g(x)$ and then apply $x_{n+1}=g(x_n)$. Each new estimate is found by substituting the current estimate into the right-hand side.

For $e^{x+1}+x-6=0$, we rearrange to isolate $x$:

$$
\begin{aligned}
e^{x+1}+x-6&=0\\
e^{x+1}&=6-x\\
x+1&=\ln(6-x)\\
x&=\ln(6-x)-1
\end{aligned}
$$

This yields the iteration formula $x_{n+1}=\ln(6-x_n)-1$.

Starting with $x_0=0.5$ and keeping full calculator accuracy:

$$
\begin{aligned}
x_1&=\ln(6-0.5)-1=0.704748\dots\\
x_2&=\ln(6-0.704748\dots)-1=0.666811\dots\\
x_3&=\ln(6-0.666811\dots)-1=0.673949\dots
\end{aligned}
$$

The sequence of estimates suggests the root is near $0.674$.

## Proving a root to 3 decimal places

An iterate such as $0.673949\ldots$ suggests the root, but it does not prove the rounded answer. To prove $0.673$ to 3 decimal places, test the half-way values $0.6725$ and $0.6735$.

For the function $f(x)=e^{x+1}+x-6$, we calculate the function values at these interval boundaries to check for a sign change:

$$$
\begin{aligned}
f(0.6725)&=e^{1.6725}+0.6725-6=-0.00204\ldots\\
f(0.6735)&=e^{1.6735}+0.6735-6=0.00429\ldots
\end{aligned}
$$

The function is continuous for all real $x$, so the sign change shows there is a root between $0.6725$ and $0.6735$. Any number in that interval rounds to $0.673$ to 3 decimal places, which proves the root to that specific accuracy.

## Convergence and domain checks

A fixed-point iteration converges when the values move closer and closer to a fixed point. Graphically, the fixed point is where $y=g(x)$ meets $y=x$.

A useful local test is $|g'(\alpha)|<1$. For the specific function $g(x)=\ln(6-x)-1$, we calculate the derivative to check this condition:

$$$g'(x)=-\frac{1}{6-x}$$

Near $\alpha\approx 0.673$, the magnitude is about $0.19$, so convergence is likely. Always check the domain before iterating; here $x_n < 6$ must be satisfied or the logarithm becomes undefined.

## Newton-Raphson method

![Newton-Raphson tangents from x0 equals 1.5 to x1 and x2 on a cubic-like curve, approaching the root alpha on the x-axis](../assets/002-612cc674-1ed3-4389-8a33-428501b25014.jpeg)

Newton-Raphson uses tangents to improve a root estimate quickly. If $f(x)=0$, the iteration formula is
$$
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}
$$

For $f(x)=x^3+2x-5$, the derivative is $f'(x)=3x^2+2$. By substituting these expressions into the Newton-Raphson formula, we obtain the specific iteration:
$$
x_{n+1}=x_n-\frac{x_n^3+2x_n-5}{3x_n^2+2}
$$

Starting with an initial value of $x_0=1.5$, we calculate the sequence of approximations:
$$
\begin{aligned}
x_1&=1.342857\ldots\\
x_2&=1.328384\ldots\\
x_3&=1.328269\ldots
\end{aligned}
$$

Since $x_2$ and $x_3$ agree to 3 decimal places, the root is approximately $1.328$. Note that if $f'(x_n)=0$, the method breaks because the tangent is horizontal and the formula attempts to divide by zero.

## Newton-Raphson for stationary points

To find a stationary point numerically, first form an equation from the condition $\frac{dy}{dx}=0$. Then apply Newton-Raphson to that new function, not to the original $y$ itself.

For $y=x\sin x$, the derivative is: $$\frac{dy}{dx}=\sin x+x\cos x$$ On the interval $\frac{\pi}{2}<x<\pi$, we have $\cos x\neq 0$, so this problem reduces to finding the root of $F(x)=\tan x+x=0$.

Now use $F'(x)=\sec^2 x+1$ in the Newton-Raphson formula: $$x_{n+1}=x_n-\frac{F(x_n)}{F'(x_n)}$$

Starting with $x_0=2$ radians, we obtain: $$\begin{aligned} x_1&=2.0273\ldots \\ x_2&=2.0288\ldots \\ x_3&=2.0288\ldots \end{aligned}$$ The stationary point is approximately $x\approx 2.0288$.

## Check yourself

1. For a continuous function, if $f(2)=-3$ and $f(3)=5$, what is guaranteed?

   - There is at least one root between 2 and 3 ✔

   - There is exactly one root between 2 and 3

   - There is no root between 2 and 3

   - The root is at $x=2.5$

   _Explanation:_ Opposite signs at the endpoints and continuity guarantee at least one root in the interval. The common wrong answer is B, but a sign change does not rule out two or more crossings inside the interval.

2. For fixed-point iteration $x_{n+1}=g(x_n)$, which condition best suggests convergence near the fixed point $\alpha$?

   - $$|g'(\alpha)|<1$ ✔

   - $$g(\alpha)=\alpha$

   - $$|g'(\alpha)|>1$

   - $$g'(x)=0$ for every $x$

   _Explanation:_ The useful local test is $|g'(\alpha)|<1$, which means errors tend to shrink from one step to the next. The common wrong answer is B: $g(\alpha)=\alpha$ only tells you where the fixed point is, not whether nearby iterates move towards it.

3. In the stationary-point example with $F(x)=\tan x+x$, what is $F'(x)$?

   - $$\sec^2 x+1$ ✔

   - $$\tan x+1$

   - $$\sec x+1$

   - $$\cos^2 x+1$

   _Explanation:_ The derivative of $\tan x$ is $\sec^2 x$, so $F'(x)=\sec^2 x+1$. The common wrong answer is B because students often confuse the function $\tan x$ with its derivative.
