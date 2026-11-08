# a-level-pure-mathematics-6-trigonometric-functions — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Reciprocal functions and angle units

![Unit circle with x and y axes, quadrants I to IV, positive trig functions by quadrant, and a reference angle drawn in quadrant II](../assets/001-bd98a0a5-2f1d-4083-b30c-8fc2a12a9cde.jpeg)
Trig functions may use degrees or radians. If an interval contains $\pi$, use radians, but if it uses $180^\circ$ or $360^\circ$, use degrees.

On the unit circle, signs depend on quadrant. The memory aid All, Sin, Tan, Cos tells you which functions are positive in quadrants I, II, III, and IV, and a reference angle is the acute angle to the nearest horizontal axis.

The reciprocal functions are defined by the equations below.
$$\sec x=\frac{1}{\cos x},\qquad \csc x=\frac{1}{\sin x},\qquad \cot x=\frac{\cos x}{\sin x}$$
You may also see $\csc x$ written as $\operatorname{cosec} x$. Each reciprocal function is undefined when its denominator is zero.

## Worked example: solving a reciprocal equation

To solve $3\csc\theta=7$, rewrite it using the reciprocal definition. $$3\csc\theta=7 \Rightarrow \sin\theta=\frac{3}{7}$$

This turns the problem into an ordinary sine equation. Now find the reference angle in radian mode using the inverse sine function.

$$$\alpha=\arcsin\left(\frac{3}{7}\right)\approx 0.443$$ The calculator gives the acute angle first, which is the reference angle.

Since sine is positive in quadrants I and II, the solutions on $0\le \theta\le 2\pi$ are $\theta=\alpha$ and $\theta=\pi-\alpha$. Therefore $\theta\approx 0.443$ or $\theta\approx 2.70$ to 3 significant figures.

## Sketching reciprocal graphs

![Graphs of cosine and secant from 0 to 2pi with asymptotes at pi over 2 and 3pi over 2 and key points marked](../assets/002-97245307-58ac-4267-9b25-a400bc5db018.jpeg)

Reciprocal graphs inherit their vertical asymptotes from the zeros of the original function. For $y=\sec x$, draw asymptotes wherever $\cos x=0$.

On $0\le x\le 2\pi$, cosine is zero at $x=\frac{\pi}{2}$ and $x=\frac{3\pi}{2}$. The sec graph also passes through the points where cosine is $1$ or $-1$, so it includes $(0,1)$, $(\pi,-1)$, and $(2\pi,1)$.

Because $\sec x=\frac{1}{\cos x}$, its branches sit outside the strip $-1<y<1$, and you must never join the graph across an asymptote. The same idea works for $y=\csc x$ from $y=\sin x$, while $y=\cot x$ is reciprocal to tangent and repeats every $\pi$.

## The identities you need all the time

An identity is true for every allowed value of the variable, and we write this with $\equiv$. The fundamental identity is $$\sin^2 x+\cos^2 x=1$$

Divide by $\cos^2 x$ to connect tangent and secant. $$\tan^2 x+1=\sec^2 x$$ This is the best choice when an equation contains both $\tan$ and $\sec$.

Divide by $\sin^2 x$ to connect cotangent and cosecant. $$1+\cot^2 x=\csc^2 x$$ This is the best choice when an equation contains both $\cot$ and $\csc$.

## Worked example: turning trig into algebra

Solve $\tan^2 x+3\sec x-3=0$ for $0^\circ\le x\le 360^\circ$. Replace $\tan^2 x$ using $\tan^2 x=\sec^2 x-1$ to get:
$$\tan^2 x+3\sec x-3=0 \Rightarrow \sec^2 x+3\sec x-4=0$$

Now let $u=\sec x$ so the trig equation becomes a quadratic:
$$u^2+3u-4=0 \Rightarrow (u+4)(u-1)=0$$
Hence $\sec x=-4$ or $\sec x=1$.

Convert back to cosine: $\cos x=-\frac{1}{4}$ or $\cos x=1$. The reference angle for $\cos x=\frac{1}{4}$ is about $75.5^\circ$, allowing us to find the solutions in the second and third quadrants.

The cosine solutions are $104.5^\circ$ and $255.5^\circ$. Because the interval includes both endpoints, $\cos x=1$ gives the additional solutions $0^\circ$ and $360^\circ$.

## Transformed angles: inside angle first

If the inside angle is transformed, solve for that whole angle first. For example, to solve $\sec(2\theta-20^\circ)=-1.25$, we substitute $u=2\theta-20^\circ$ and calculate the transformed interval: $$-380^\circ\le u\le 340^\circ$$

Next, rewrite the reciprocal equation in cosine form to find the reference angle: $$\sec u=-1.25 \Rightarrow \cos u=-0.8$$ The reference angle is $\arccos(0.8)\approx 36.9^\circ$, which indicates that the solutions for $u$ lie in quadrants II and III.

Using $u=180^\circ\pm 36.9^\circ+360^\circ k$, find the values within the transformed interval: $-216.9^\circ, -143.1^\circ, 143.1^\circ, 216.9^\circ$. Finally, convert back with $\theta=\frac{u+20^\circ}{2}$ to find the final solutions: $\theta\approx -98.4^\circ, -61.6^\circ, 81.6^\circ, 118.4^\circ$.

## Check yourself

1. A trig equation is to be solved on $0\le x\le 2\pi$. Which calculator mode should you use?

   - Degrees

   - Radians ✔

   - Either degrees or radians

   - Statistics mode

   _Explanation:_ B is correct because intervals written with $\pi$ are in radians. The common wrong choice A gives answers measured in degrees, so your calculator values would be wrong even if your method was right.

2. For $y=\sec x$ on $0\le x\le 2\pi$, where are the vertical asymptotes?

   - $$x=0$ and $x=\pi$

   - $$x=\frac{\pi}{2}$ and $x=\frac{3\pi}{2}$ ✔

   - $$x=\frac{\pi}{4}$ and $x=\frac{5\pi}{4}$

   - There are no vertical asymptotes

   _Explanation:_ B is correct because $\sec x=\frac{1}{\cos x}$ is undefined where $\cos x=0$. The common wrong choice A gives the points where $\cos x=\pm 1$, so $\sec x=\pm 1$ and the graph is perfectly defined there.

3. Solve $\tan^2 x+3\sec x-3=0$ on $0^\circ\le x\le 360^\circ$. Which answer set is correct?

   - $$x=75.5^\circ,\ 284.5^\circ$

   - $$x=104.5^\circ,\ 255.5^\circ,\ 0^\circ,\ 360^\circ$ ✔

   - $$x=75.5^\circ,\ 104.5^\circ,\ 255.5^\circ$

   - $$x=104.5^\circ,\ 255.5^\circ$

   _Explanation:_ B is correct because $\cos x=-\frac{1}{4}$ gives quadrants II and III, so $104.5^\circ$ and $255.5^\circ$, and $\cos x=1$ gives both $0^\circ$ and $360^\circ$ on this closed interval. The common wrong choice D forgets that both endpoints are included.

4. When solving $\sec(2\theta-20^{\circ})=-1.25$ for $-180^{\circ}\le \theta\le 180^{\circ}$, what is the correct transformed interval after setting $u=2\theta-20^{\circ}$?

   - $$-360^{\circ}\le u\le 360^{\circ}$

   - $$-380^{\circ}\le u\le 340^{\circ}$ ✔

   - $$-200^{\circ}\le u\le 160^{\circ}$

   - $$-180^{\circ}\le u\le 180^{\circ}$

   _Explanation:_ B is correct because doubling the bounds gives $-360^{\circ}\le 2\theta\le 360^{\circ}$, then subtracting $20^{\circ}$ gives $-380^{\circ}\le u\le 340^{\circ}$. The common wrong choice C comes from subtracting $20^{\circ}$ but forgetting the factor of $2$ on $\theta$.
