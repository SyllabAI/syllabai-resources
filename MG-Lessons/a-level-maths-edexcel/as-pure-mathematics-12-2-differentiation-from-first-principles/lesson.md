# as-pure-mathematics-12-2-differentiation-from-first-principles — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Average and instantaneous gradient

![Graph of a curve $y=f(x)$ with points at $x$ and $x+h$, a secant line through both points, and a tangent at $x$](../assets/001-c52cbfe3-051e-48a1-83a7-37a63ebd366e.jpeg)

A straight line has one constant gradient, but a curve changes steepness from point to point. The gradient between two points on a curve is the average gradient, found from the secant or chord joining them.

At one exact point, we want the instantaneous gradient instead. That is the gradient of the tangent to the curve at that point.

## Building the formula

Take one point at input $x$ and a nearby point at input $x+h$, where $h$ is a small change in $x$. Their average gradient is
$$
\frac{f(x+h)-f(x)}{h}
$$

As $h$ gets closer to 0, the secant approaches the tangent. That limiting value is the derivative, written $f'(x)$ or $\frac{dy}{dx}$.

$$$
f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
$$
This is called differentiating from first principles. Do not substitute $h=0$ at the start, because the denominator would still be zero.

## Warm-up: a linear function

Let $f(x)=6x$ and start with the general definition of the derivative:
$$f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$$

First, find the expression for $f(x+h)=6(x+h)=6x+6h$. Substitute this into the difference quotient:
$$f'(x)=\lim_{h\to 0}\frac{(6x+6h)-6x}{h}=\lim_{h\to 0}\frac{6h}{h}$$

The $6x$ terms cancel exactly. Now cancel the common factor of $h$ and take the limit to find the result:
$$f'(x)=\lim_{h\to 0}6=6$$
So the derivative of $6x$ is 6 at every point.

## Expanding brackets correctly

Most first-principles mistakes are algebra mistakes. You need accurate expansions before you can cancel $h$.

The key expansions to know are $$(x+h)^2=x^2+2xh+h^2$$ and $$(x+h)^3=x^3+3x^2h+3xh^2+h^3$$

These are the patterns you should know by heart. After subtracting $f(x)$, every remaining term should contain a factor of $h$. If one term does not, check your expansion or your subtraction signs.

## Worked example: quadratic from first principles

Let $f(x)=3x^2$ and start with the definition of the derivative from first principles:
$$
f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
$$
In this specific case, we have the term $f(x+h)=3(x+h)^2$.

Expand the expression carefully to avoid algebraic errors:
$$
f(x+h)=3(x^2+2xh+h^2)=3x^2+6xh+3h^2
$$
Now substitute this back into the limit definition, keeping brackets around the part you subtract to manage the signs.

$$$
f'(x)=\lim_{h\to 0}\frac{(3x^2+6xh+3h^2)-3x^2}{h}
=\lim_{h\to 0}\frac{6xh+3h^2}{h}
$$
Every term in the numerator now has a factor of $h$, which allows us to factor it out and simplify the fraction.

Factor and cancel the common $h$ terms:
$$
f'(x)=\lim_{h\to 0}\frac{h(6x+3h)}{h}
=\lim_{h\to 0}(6x+3h)
=6x
$$
Only now is it safe to let $h\to 0$. This proves that the derivative of $3x^2$ is $6x$ using the first principles method.

## Cubic proof and the power rule

For $f(x)=4x^3$, start in the same way as previous examples, but apply the cubic expansion. Since $(x+h)^3=x^3+3x^2h+3xh^2+h^3$, we determine the expanded form of the function:
$$f(x+h)=4x^3+12x^2h+12xh^2+4h^3$$

Substitute and simplify using the limit definition of the derivative. As shown below, every term in the simplified numerator contains $h$, which allows us to factor it out:
$$f'(x)=\lim_{h\to 0}\frac{(4x^3+12x^2h+12xh^2+4h^3)-4x^3}{h} =\lim_{h\to 0}\frac{12x^2h+12xh^2+4h^3}{h}$$

Cancel the $h$ in the denominator and take the limit. The pattern shows that if $f(x)=ax^3$, then $f'(x)=3ax^2$, which aligns with the shortcut power rule:
$$f'(x)=\lim_{h\to 0}(12x^2+12xh+4h^2)=12x^2$$

You can use the general rule $\frac{d}{dx}(x^n)=nx^{n-1}$ to check your final answer. However, if an exam specifies finding the derivative "from first principles," the full limit method must be shown as your primary solution.

## Check yourself

1. For the curve $y=x^2$, what is the average gradient between $x=2$ and $x=5$?

   - 7 ✔

   - 21

   - 3

   - 5

   _Explanation:_ At $x=2$, $y=4$, and at $x=5$, $y=25$, so the average gradient is $\frac{25-4}{5-2}=\frac{21}{3}=7$. A very common wrong answer is 21, which is just the change in $y$ and forgets to divide by the change in $x$.

2. Why must you simplify or cancel the factor of $h$ before setting $h=0$ in first principles?

   - Because otherwise the denominator would be zero ✔

   - Because $x$ would also become 0

   - Because limits remove any denominator automatically

   - Because $h$ and $x$ must always be equal

   _Explanation:_ A is right because the original quotient has $h$ in the denominator, so setting $h=0$ too early would mean dividing by zero. C is the common misconception: limits do not magically cancel denominators, so you still have to simplify the algebra first.

3. In the quadratic proof for $f(x)=3x^2$, what is the simplified numerator after subtracting $f(x)$?

   - $$6xh+3h^2$ ✔

   - $$3x^2+6xh+3h^2$

   - $$6x+3h$

   - $$6xh$

   _Explanation:_ A is right because the $3x^2$ from $f(x+h)$ and the $3x^2$ from $f(x)$ cancel, leaving only terms with $h$. B is the common wrong answer when you forget to subtract the whole of $f(x)$.
