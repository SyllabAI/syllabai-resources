# a-level-pure-mathematics-8-parametric-equations — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## What parametric equations do

![Graph of the parametric curve x equals t plus 4 and y equals t squared plus 2, with vertex at (4,2), sample points for t equals -1, 0, and 2, and arrows showing direction as t increases](../assets/001-4bb70611-1c7b-4385-9cb9-7570c5f279ec.jpeg)

A parametric equation gives $x$ and $y$ separately in terms of a third variable, called a parameter, usually $t$ or $\theta$. Each value of the parameter gives one point, so the curve is traced in an order as the parameter changes.

For $x=t+2$ and $y=t^2-1$, substituting $t=-1,0,2$ gives the points $(1,0)$, $(2,-1)$, and $(4,3)$. As $t$ increases, the point moves through those points in that order.

## Eliminating the parameter

To eliminate the parameter, rearrange one equation so that the parameter is the subject, then substitute into the other equation. The aim is a Cartesian equation involving only $x$ and $y$.

If $x=t+4$ and $y=t^2+2$, we rearrange the first equation to get $t=x-4$. Substituting this into the second equation gives:

$$$y=(x-4)^2+2$$

This is an upward-opening parabola with vertex $(4,2)$. If $t$ is unrestricted, then $x$ can take any real value. Always watch the sign: from $x=t+4$, the correct rearrangement is $t=x-4$, not $x+4$.

## Intercepts and parameter restrictions

For an $x$-intercept, set $y=0$. For a $y$-intercept, set $x=0$, and work directly with the parameter instead of eliminating it if that is quicker.

For $x=\ln(t+2)$ and $y=t^2-9$ with $t>-2$, an $x$-intercept comes from $t^2-9=0$. This gives $t=3$ or $t=-3$, but $t=-3$ is not allowed, so the only $x$-intercept is $(\ln 5,0)$.

For the $y$-intercept, set $x=0$, so $\ln(t+2)=0$ and therefore $t=-1$. Then $y=(-1)^2-9=-8$, so the curve crosses the $y$-axis at $(0,-8)$.

## Recognising circles

A very common circle form is $x=a+r\cos\theta$ and $y=b+r\sin\theta$. In this form, the centre of the circle is $(a,b)$ and the radius is $r$.

So $x=3+4\cos\theta$ and $y=-2+4\sin\theta$ represent a circle with centre $(3,-2)$ and radius $4$. The constants outside the trig functions shift the graph, and the common coefficient of $\cos\theta$ and $\sin\theta$ gives the radius.

To eliminate $\theta$, rearrange to get $\frac{x-3}{4}=\cos\theta$ and $\frac{y+2}{4}=\sin\theta$. Using $\cos^2\theta+\sin^2\theta=1$ gives $\left(\frac{x-3}{4}\right)^2+\left(\frac{y+2}{4}\right)^2=1$, so the Cartesian form is $(x-3)^2+(y+2)^2=16$.

## When the curve is really a line segment

Sometimes the equations look curved, but the points lie on a straight line. If the parameter has a restricted interval, the graph is only a segment of that line.

For $x=\frac{1+6t}{t+1}$ and $y=\frac{3+t}{t+1}$ with $0\le t\le 4$, try a linear combination:
$$
2x+5y=\frac{2(1+6t)+5(3+t)}{t+1}=\frac{17+17t}{t+1}=17
$$
So every point lies on the line $2x+5y=17$.

Use the ends of the parameter interval to find the endpoints. At $t=0$, $(x,y)=(1,3)$, and at $t=4$, $(x,y)=\left(5,\frac{7}{5}\right)$.

The segment length is
$$
L=\sqrt{(5-1)^2+\left(\frac{7}{5}-3\right)^2}=\sqrt{16+\frac{64}{25}}=\frac{4\sqrt{29}}{5}
$$
Also check the denominator: $t+1\neq 0$ for $0\le t\le 4$, so the parametrization is valid throughout.

## Trig identities, domains, and intersections

With trig parametric equations, the key step is often to spot an identity. For $x=2+\cos t$ and $y=1+4\cos 2t$ with $0\le t\le 2\pi$, use $\cos 2t=2\cos^2 t-1$ and $\cos t=x-2$ to find the Cartesian equation.

$$$y=8(x-2)^2-3$$ Because $-1\le \cos t\le 1$, the possible $x$-values are restricted to $1\le x\le 3$, so you only sketch that specific part of the parabola.

To find intersections with another curve, substitute the parametric expressions for $x$ and $y$ into the target equation. For $x=4\cos t$ and $y=2\sqrt{3}\sin t$ meeting $x^2+y^2=13$, substitution gives $16\cos^2 t+12\sin^2 t=13$.

Using $\cos^2 t=1-\sin^2 t$ gives $\sin^2 t=\frac{3}{4}$. This leads to the four distinct intersection points: $(2,3)$, $(-2,3)$, $(-2,-3)$, and $(2,-3)$.

## Check yourself

1. For $x=t+2$ and $y=t^2-1$, which statement is correct as $t$ increases from $-1$ to $2$?

   - The curve passes through $(1,0)$, then $(2,-1)$, then $(4,3)$ ✔

   - The curve passes through $(4,3)$, then $(2,-1)$, then $(1,0)$

   - The curve passes through $(1,-1)$, then $(2,0)$, then $(4,3)$

   - The parameter tells you the gradient, not the position

   _Explanation:_ Each value of $t$ gives a point. At $t=-1,0,2$ the points are $(1,0)$, $(2,-1)$, and $(4,3)$, so that is the tracing order. The common wrong answer B lists the same points in reverse order and ignores that the curve is traced as $t$ increases.

2. For the curve $x=\ln(t+2),\ y=t^2-9,\ t>-2$, what is the $y$-intercept?

   - $$(\ln 5,0)$

   - $$(0,-8)$ ✔

   - $$(0,8)$

   - There is no $y$-intercept

   _Explanation:_ A $y$-intercept happens when $x=0$. Solving $\ln(t+2)=0$ gives $t=-1$, and then $y=-8$, so the point is $(0,-8)$. The common wrong answer A is the $x$-intercept, found by setting $y=0$ instead.

3. For the curve $x=\frac{1+6t}{t+1},\ y=\frac{3+t}{t+1},\ 0\le t\le 4$, why is the graph a line segment rather than the whole line $2x+5y=17$?

   - Because $0\le t\le 4$ only produces the points between the endpoint values ✔

   - Because any equation with a denominator must be curved

   - Because straight lines cannot be written parametrically

   - Because $2x+5y=17$ has only finitely many points

   _Explanation:_ The relation $2x+5y=17$ shows all points lie on a straight line, but the restricted parameter range gives only a finite part of that line. The common wrong answer B confuses the form of the parametrization with the shape of the graph.

4. For $x=2+\cos t,\ y=1+4\cos 2t,\ 0\le t\le 2\pi$, which Cartesian description is correct?

   - $$y=8(x-2)^2-3$ for $1\le x\le 3$ ✔

   - $$y=4(x-2)^2+1$ for $1\le x\le 3$

   - $$y=8(x-2)^2-3$ for all real $x$

   - $$y=8(x+2)^2-3$ for $1\le x\le 3$

   _Explanation:_ Since $\cos t=x-2$, the identity $\cos 2t=2\cos^2 t-1$ gives $y=1+4(2(x-2)^2-1)=8(x-2)^2-3$. The common wrong answer C finds the equation correctly but forgets that $\cos t$ can only lie between $-1$ and $1$, so $x$ must satisfy $1\le x\le 3$.
