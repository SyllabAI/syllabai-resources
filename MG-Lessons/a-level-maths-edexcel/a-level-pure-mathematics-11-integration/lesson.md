# a-level-pure-mathematics-11-integration — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Integration as reverse differentiation

Integration reverses differentiation: if $F'(x)=f(x)$, then $\int f(x)\,dx = F(x)+c$. The constant $+c$ is essential because any constant disappears when you differentiate. Later, the same idea powers area problems, differential equations and numerical estimates.

For $n \neq -1$,
$$\int x^n\,dx = \frac{x^{n+1}}{n+1}+c$$
and the special case is
$$\int \frac{1}{x}\,dx = \ln|x|+c.$$
A linear bracket such as $ax+b$ needs a scale factor, so reverse the chain rule by dividing by the derivative of the bracket.

## Reverse chain rule in action

A very common mistake is forgetting the hidden derivative inside a bracket. Since $\frac{d}{dx}(5x-3)=5$, reversing the chain rule for $(5x-3)^{1/2}$ means dividing by 5.

For the first term, we apply the reverse chain rule: $$\int (5x-3)^{1/2}\,dx = \frac{1}{5}\cdot\frac{(5x-3)^{3/2}}{3/2} = \frac{2}{15}(5x-3)^{3/2}.$$ That extra factor of $\frac{1}{5}$ is what students most often miss.

For the second term: $$\int 2(4x+1)^{-3}\,dx = 2\cdot\frac{1}{4}\cdot\frac{(4x+1)^{-2}}{-2} = -\frac{1}{4}(4x+1)^{-2}.$$ Combining these, we find: $$\int \left((5x-3)^{1/2} + 2(4x+1)^{-3}\right)\,dx = \frac{2}{15}(5x-3)^{3/2} - \frac{1}{4}(4x+1)^{-2} + c.$$ Differentiate this result and both original terms reappear.

## Definite integrals and signed area

![Graph of y = x^3 - x with the region from x = -1 to 0 shaded above the x-axis as positive area and the region from x = 0 to 1 shaded below the x-axis as negative area, showing that a definite integral gives signed area](../assets/001-e8a07efe-bdca-4a09-8cdb-f169aceaae25.jpeg)
A definite integral adds up signed area between a curve and the $x$-axis. Area above the axis counts positive and area below counts negative, so equal positive and negative parts can cancel.

For definite integrals, the limits tell you where to start and finish, so there is no $+c$. A standard trig example is
$$
\int_0^{\frac{\pi}{2}} \cos^2 x\,dx = \int_0^{\frac{\pi}{2}} \frac{1+\cos 2x}{2}\,dx.
$$

Integrating term by term gives
$$
\left[\frac{x}{2}+\frac{\sin 2x}{4}\right]_0^{\frac{\pi}{2}} = \frac{\pi}{4}.
$$
Using the identity first is the key step.

## Substitution and changing limits

Substitution rewrites a hard integral in a simpler variable and is the reverse of the chain rule. For definite integrals, either change the limits straight away or change back to $x$ at the end, but never mix the two methods.

Consider the following integral example:
$$
I=\int_0^{\frac{\pi}{2}} \frac{\sin x}{1+\cos x}\,dx
$$
Let $u=1+\cos x$. Then $du=-\sin x\,dx$, so $\sin x\,dx=-du$, and the limits change from $x=0,\frac{\pi}{2}$ to $u=2,1$.

Now we substitute and evaluate the integral:
$$
I=\int_2^1 -\frac{1}{u}\,du = \int_1^2 \frac{1}{u}\,du = \left[\ln u\right]_1^2 = \ln 2.
$$
The minus sign is important because it is used to flip the limits.

## Integration by parts

Integration by parts reverses the product rule, so it is useful for products such as $x\sin x$ or $x e^x$. The formula is
$$\int u\frac{dv}{dx}\,dx = uv - \int v\frac{du}{dx}\,dx.$$

For
$$I=\int x\sin x\,dx,$$
choose $u=x$ so that differentiating simplifies it, and take $\frac{dv}{dx}=\sin x$. Then $\frac{du}{dx}=1$ and $v=-\cos x$.

Substituting gives
$$I = x(-\cos x) - \int (-\cos x)(1)\,dx = -x\cos x + \sin x + c.$$
A quick derivative check confirms the answer, and it also catches the common sign error.

## Partial fractions before integrating

When the integrand is a rational function, partial fractions can break it into simpler pieces whose antiderivatives you already know. This is especially useful when linear factors produce logarithms.

To solve an example like $\int \frac{3x}{(x+1)(x-2)} \,dx$, we first decompose the integrand. We write the fraction as: $$\frac{3x}{(x+1)(x-2)} = \frac{A}{x+1} + \frac{B}{x-2}$$ and multiply through by $(x+1)(x-2)$ to get $$3x = A(x-2) + B(x+1).$$

Comparing coefficients gives $A+B=3$ and $-2A+B=0$, so $A=1$ and $B=2$. Substituting these values allows us to integrate: $$\int \frac{3x}{(x+1)(x-2)}\,dx = \int \left(\frac{1}{x+1} + \frac{2}{x-2}\right)\,dx = \ln|x+1| + 2\ln|x-2| + c.$$ Modulus signs are used here because the linear factors inside the logarithms can be negative.

## Check yourself

1. Why does an indefinite integral need $+c$?

   - Because constants disappear when differentiated ✔

   - Because integration is only an approximation

   - Because the power rule always adds 1 to the answer

   - Because every integral must have limits

   _Explanation:_ $$+c$ is needed because differentiating any constant gives 0, so many different functions have the same derivative. The most common wrong answer is D, but limits are only used for definite integrals, not indefinite ones. Hint: Differentiate $x^2$, $x^2+3$ and $x^2-10$.

2. What is $\int_{-1}^{1} (x^3-x)\,dx$?

   - $$0$ ✔

   - $$\frac{1}{4}$

   - $$\frac{1}{2}$

   - $$1$

   _Explanation:_ The positive area from $-1$ to 0 and the negative area from 0 to 1 are equal in size, so the signed areas cancel and the integral is 0. The most common wrong answer is C, which adds the magnitudes of the areas instead of using signed area.

3. Stretch: Which is correct for $\int \ln x\,dx$?

   - $$x\ln x - x + c$ ✔

   - $$x\ln x + c$

   - $$\frac{(\ln x)^2}{2}+c$

   - $$x^2\ln x + c$

   _Explanation:_ Use integration by parts with $u=\ln x$ and $dv=dx$, so $du=\frac{1}{x}\,dx$ and $v=x$. This gives $x\ln x-\int 1\,dx = x\ln x-x+c$, while the common wrong answer B forgets the extra $-\int 1\,dx$ term and differentiates to $\ln x + 1$.
