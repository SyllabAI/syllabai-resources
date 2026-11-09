# a-level-pure-mathematics-7-trigonometry-and-modelling — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 2 check questions (source: MathsGenie lessons)_

## Intervals, periods and reference angles

![Unit circle with quadrants labelled, reference angle alpha in quadrant I, matching angle 2π-alpha in quadrant IV, and cosine positive shown in quadrants I and IV](../assets/001-daf45abd-e2f1-4478-a402-682aaf98c172.jpeg)

Trigonometric equations repeat, so the interval tells you how many solutions to look for. Before using inverse trig, check whether the question is in degrees or radians and match your calculator mode.

The period is the angle length before a function repeats. Sine and cosine repeat every $360^\circ$ or $2\pi$, while tangent repeats every $180^\circ$ or $\pi$.

If $\cos\theta=0.25$ on $0\leq\theta<2\pi$, first find the reference angle $\alpha=\cos^{-1}(0.25)\approx1.318$. Cosine is positive in quadrants I and IV, so $\theta=\alpha$ or $\theta=2\pi-\alpha$, giving $\theta=1.318, 4.965$.

## Double-angle and triple-angle identities

A trig identity is true for every value where both sides are defined, so it is different from solving an equation. Starting from the compound-angle formulae, replacing $B$ by $A$ gives the double-angle identities.

The versions you use most often are below. Choose the form that matches the trig function already in your equation, because that keeps the algebra shorter.

$$\sin 2A = 2\sin A\cos A$$
$$\cos 2A = \cos^2 A-\sin^2 A = 2\cos^2 A-1 = 1-2\sin^2 A$$
$$\tan 2A = \frac{2\tan A}{1-\tan^2 A}$$

The triple-angle identities are especially useful when an equation looks cubic in $\sin x$ or $\cos x$. They let you replace a messy expression with a single trig function before solving.

$$\sin 3x \equiv 3\sin x - 4\sin^3 x,\qquad \cos 3x \equiv 4\cos^3 x - 3\cos x$$

## Worked example: a triple-angle equation

To solve $3\sin\theta-4\sin^3\theta=0.6$ for $0^{\circ}\leq\theta\leq180^{\circ}$, recognise the left-hand side as a triple-angle identity. It becomes
$$
\sin 3\theta = 0.6
$$

Let $u=3\theta$. Then the interval triples to $0^{\circ}\leq u\leq540^{\circ}$. The reference angle is $\sin^{-1}(0.6)=36.9^{\circ}$, and since sine is positive in quadrants I and II, the solutions are $u=36.9^{\circ},\ 143.1^{\circ},\ 396.9^{\circ},\ 503.1^{\circ}$.

Now divide every solution by 3 to return to $\theta$. This gives
$$
\theta=12.3^{\circ},\ 47.7^{\circ},\ 132.3^{\circ},\ 167.7^{\circ}
$$
The enlarged interval is what stops you missing the two answers from the second cycle.

## R-form and one-wave rewriting

R-form rewrites $a\sin x+b\cos x$ as one shifted wave. If you choose $R\sin(x-\alpha)$, expand first so the signs are visible: $$R\sin(x-\alpha)=R\cos\alpha\sin x-R\sin\alpha\cos x$$

For $\sin x-\sqrt{3}\cos x+4$, match coefficients with $R\sin(x-\alpha)+4$. This gives $$R\cos\alpha=1,\qquad R\sin\alpha=\sqrt{3}$$ so $R=2$ and $\alpha=60^{\circ}$.

Hence $$\sin x-\sqrt{3}\cos x+4=2\sin(x-60^{\circ})+4$$ This single-wave form makes maxima, minima, and solutions much easier to read. The range is $2\leq y\leq6$, and solving $2\sin(x-60^{\circ})+4=5$ on $0^{\circ}\leq x<360^{\circ}$ gives $x=90^{\circ},\ 210^{\circ}$.

## Trig models for daily cycles

![Graph of daily temperature model over 0 to 24 hours with sinusoidal curve, midline at 10, amplitude 5, and maximum near t=11.5 h at 15°C](../assets/002-935bf65b-84b7-4d6f-8e7f-074014e50510.jpeg)

A trigonometric model fits repeating data using parameters like midline, amplitude, period, and phase shift. In a daily temperature model, the term $15t$ indicates the angle increases by $15^\circ$ per hour, resulting in a period of $\frac{360}{15}=24$ hours.

Consider the model $\theta=10+4\sin((15t-120)^\circ)+3\cos((15t-120)^\circ)$. By letting $u=(15t-120)^\circ$ and combining the two waves using the identity $4\sin u+3\cos u=5\sin(u+36.9^\circ)$, we can simplify the expression for the model.

$$$\theta=10+5\sin((15t-83.1)^\circ)$$

With a midline of 10 and an amplitude of 5, the temperature oscillates between 5 and 15. The first maximum occurs when the sine argument is $90^\circ$, meaning $15t-83.1=90$, which yields $t=11.54$ hours, or approximately 11:33.

## Reciprocal functions and proof strategy

Reciprocal trig functions often appear in proof or modelling questions. Remember $\sec x=\frac{1}{\cos x}$ and $\csc x=\frac{1}{\sin x}$, so each is undefined when its denominator is zero.

In an identity proof, start with the more complicated side and simplify it. For example, the left-hand side becomes $$ \sec x-\cos x=\frac{1}{\cos x}-\cos x=\frac{1-\cos^2 x}{\cos x} $$

Now use $1-\cos^2 x\equiv\sin^2 x$ to get $\frac{\sin^2 x}{\cos x}=\sin x\tan x$. Do not move terms across as if you were solving an equation, and keep domain restrictions in mind when cancelling.

## Check yourself

1. When solving $\sin 3\theta = 0.6$ for $0^\circ\leq\theta\leq180^\circ$, which interval must you use for $u=3\theta$?

   - $$0^\circ\leq u\leq180^\circ$

   - $$0^\circ\leq u\leq360^\circ$

   - $$0^\circ\leq u\leq540^\circ$ ✔

   - $$0^\circ\leq u\leq60^\circ$

   _Explanation:_ Because the substitution $u=3\theta$ multiplies every value in the interval by 3, the correct interval is $0^\circ$ to $540^\circ$. The most common wrong answer is A, which keeps the original interval and misses the solutions coming from later repeats of the sine curve.

2. For the model $\theta=10+5\sin((15t-83.1)^\circ)$, when does the first maximum temperature occur?

   - 05:33

   - 11:33 ✔

   - 12:00

   - 17:33

   _Explanation:_ A maximum happens when the sine value is 1, so set $15t-83.1=90$ and solve to get $t=11.54$ hours, which is about 11:33. The most common wrong answer is C, which ignores the phase shift and assumes the peak is at noon just because the model is over 24 hours.
