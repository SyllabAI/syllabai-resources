# as-pure-mathematics-4-graphs-and-transformations — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Reading a graph

A graph of $y=f(x)$ shows all points $(x,y)$ that satisfy the rule. In sketch questions, your first aim is to find the key features you can label exactly.

An x-intercept happens where $y=0$, so it also gives a root or zero of $f(x)$. A y-intercept happens where $x=0$, so you find it by substituting $x=0$.

An asymptote is a line that a curve approaches without meeting. For polynomials, roots and intercepts usually drive the sketch; for reciprocal graphs, asymptotes matter just as much.

## Worked example: sketching a factorised cubic

To sketch $y=(x+2)(x-1)(3-x)$, set each factor to zero.
$$
x+2=0 \Rightarrow x=-2, \quad x-1=0 \Rightarrow x=1, \quad 3-x=0 \Rightarrow x=3
$$
So the x-intercepts are $(-2,0)$, $(1,0)$ and $(3,0)$.

Now find the y-intercept by substituting $x=0$.
$$
y=(0+2)(0-1)(3-0)=-6
$$
So the curve crosses the y-axis at $(0,-6)$.

The leading term is $x \cdot x \cdot (-x)=-x^3$, so this cubic goes up on the left and down on the right. Draw a smooth curve through the four labelled points, crossing the x-axis at each simple root. If a factor were repeated, such as $(x-2)^2$, the graph would usually touch the x-axis there instead of crossing.

## Function notation and the main transformations

![Base graph with four labelled transformations: up by 2, right by 2, reflection in the x-axis, and horizontal compression, with the note outside affects y-values and inside affects x-values](../assets/001-32398ce6-65dc-4744-b651-7db226f6d597.jpeg)
Writing $y=f(x)$ means the y-value comes from a rule applied to $x$. A transformation moves, reflects or stretches that graph.

Changes outside the function act on y-values: $f(x)+a$ shifts up by $a$, $-f(x)$ reflects in the x-axis, and $af(x)$ multiplies all y-values by $a$.

Changes inside the function act on x-values in the opposite way: $f(x-a)$ moves right by $a$, $f(-x)$ reflects in the y-axis, and $f(ax)$ gives a horizontal scale factor of $\frac{1}{a}$.

The minus sign inside is the common trap. For $y=f(x-3)$, every point moves 3 units to the right, not left.

## Quadratics, completing the square, and minimum points

A quadratic in completed-square form shows its turning point directly. For the function $f(x)=x^2+6x+11$, we can complete the square to find the vertex:

$$$f(x)=x^2+6x+11=(x+3)^2-9+11=(x+3)^2+2$$

Since $(x+3)^2 \ge 0$, the smallest possible value for the expression occurs when $x=-3$. Thus, the minimum point of the graph $y=f(x)$ is $(-3,2)$.

We can track this point under transformations instead of re-sketching. For $y=2f(x)$ the y-values double, giving $(-3,4)$, and for $y=f(2x)$ the x-values halve, giving $\left(-\frac{3}{2},2\right)$.

## Reciprocal graphs and asymptotes

![Graph of y equals 2 over x minus 1 plus 3 with dashed asymptotes x equals 1 and y equals 3, and intercepts labelled at one third comma zero and zero comma one](../assets/002-c3e6696b-2464-4b51-bdde-24f3bcade919.jpeg)

The basic reciprocal graph $y=\frac{1}{x}$ has asymptotes $x=0$ and $y=0$. In $y=\frac{2}{x-1}+3$, the whole graph shifts right by 1 and up by 3, so the asymptotes become $x=1$ and $y=3$.

Find the y-intercept by substituting $x=0$.
$$y=\frac{2}{0-1}+3=1$$
So the curve passes through $(0,1)$.

Find the x-intercept by setting $y=0$.
$$0=\frac{2}{x-1}+3 \Rightarrow -3=\frac{2}{x-1} \Rightarrow -3(x-1)=2 \Rightarrow x=\frac{1}{3}$$
So the x-intercept is $\left(\frac{1}{3},0\right)$.

Sketch two branches that approach the asymptotes without touching them. The right-hand branch lies above $y=3$, while the left-hand branch passes through both intercepts and drops sharply near $x=1$.

## Solving equations and inequalities from sketches

A sketch answers algebra questions as well as drawing ones. Solving $f(x)=0$ means reading the x-intercepts, while solving $f(x)>0$ or $f(x)\le 0$ means checking where the graph sits above or on and below the x-axis.

For $f(x)=(x+1)(x-2)^2$, the roots are $x=-1$ and $x=2$, with $x=2$ repeated. The graph crosses at $x=-1$ but only touches at $x=2$, and its positive leading term means it is down on the left and up on the right.

So $f(x)\le 0$ for $x\le -1$ and also at $x=2$. The same idea works for intersections: the real solutions of $f(x)=g(x)$ are the x-values where the two graphs meet.

## Check yourself

1. For the graph $y=f(x)$, which statement is always true?

   - At a root, $y=0$ ✔

   - At a y-intercept, $y=0$

   - Every asymptote is horizontal

   - Every cubic has three distinct x-intercepts

   _Explanation:_ A root means $f(x)=0$, so the point lies on the x-axis and has $y=0$. B is the most common wrong answer because students mix up the axes; at the y-intercept, $x=0$, not $y=0$.

2. The point $(4,-1)$ lies on $y=f(x)$. Which point lies on $y=f(x-3)$?

   - $$(1,-1)$

   - $$(7,-1)$ ✔

   - $$(4,2)$

   - $$(-4,-1)$

   _Explanation:_ $$f(x-3)$ shifts the graph 3 units to the right, so you add 3 to the x-coordinate and keep the y-coordinate the same. A is the common wrong answer because students follow the minus sign literally instead of remembering that inside changes work in the opposite direction.

3. What are the asymptotes of $y=\frac{3}{x+5}-1$?

   - $$x=-5$ and $y=-1$ ✔

   - $$x=5$ and $y=-1$

   - $$x=-5$ and $y=1$

   - $$x=0$ and $y=0$

   _Explanation:_ The vertical asymptote comes from the denominator, so $x+5=0$ gives $x=-5$, and the outside $-1$ moves the horizontal asymptote to $y=-1$. B is the common wrong answer because students forget that inside changes work in the opposite direction, so $x+5$ means left 5, not right 5. Hint: Set the denominator equal to zero first.
