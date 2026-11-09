# as-pure-mathematics-14-exponentials-and-logarithms — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 4 check questions (source: MathsGenie lessons)_

## Exponentials and inverse logs

![Graphs of y = e^x and y = ln x with the line y = x showing the inverse relationship](../assets/001-8f2b869e-e6ed-4392-855c-4c43458c3411.jpeg)

An exponential function has the variable in the power, like $y=3^x$ or $y=e^x$. For AS Maths the base is positive and not equal to 1.

A logarithm undoes an exponential: $\log_a b=c$ means $a^c=b$. That is why $y=e^x$ and $y=\ln x$ are inverse functions, reflected in the line $y=x$.

If you can rewrite both sides of an equation with the same base, you can solve by equating powers. For example, $2^{x+1}=64$ becomes $2^{x+1}=2^6$. Then $x+1=6$, so $x=5$.

## Solving when bases do not match

When bases do not match, use logarithms. The natural logarithm is $\ln x=\log_e x$, where $e\approx 2.718$.

To solve $5^x=18$, take natural logs of both sides and use the power law. This brings the unknown down from the exponent: $$\ln(5^x)=\ln 18 \Rightarrow x\ln 5=\ln 18$$

Then divide by $\ln 5$ and evaluate: $$x=\frac{\ln 18}{\ln 5}\approx 1.80$$ A common mistake is to write $\ln(18 \div 5)$, but logs do not work like that.

## Using the log laws

The three fundamental log laws are:
$$
\log_a(MN)=\log_a M+\log_a N,\quad \log_a\left(\frac{M}{N}\right)=\log_a M-\log_a N,\quad \log_a(M^p)=p\log_a M
$$
These laws apply to multiplication, division, and powers, but they do not apply to addition or subtraction inside the logarithm's argument.

Using these rules, the expression $2\log_a(x+3)-\log_a 7$ can be condensed into a single logarithm:
$$
\log_a\left(\frac{(x+3)^2}{7}\right)
$$
It is important to remember that the argument of a log must be positive, so in this case, we require $x > -3$.

To solve $2\log_2 x-\log_2 5=3$, we first combine the logs and then convert the equation to exponential form:
$$
\log_2\left(\frac{x^2}{5}\right)=3 \Rightarrow \frac{x^2}{5}=2^3
$$
This simplifies to $x^2=40$, giving $x=2\sqrt{10}$. We reject the negative root $x=-2\sqrt{10}$ because the original equation requires $x>0$.

## Natural log equations

For any logarithm, the argument must be positive. When solving an equation involving $\ln(3x-2)$, we must first recognize that $3x-2 > 0$ for the expression to be defined.

To solve $\ln(3x-2)=1$, exponentiate both sides with base $e$. This operation undoes the natural logarithm: $$3x-2=e$$

Isolating $x$ provides the final answer: $$x=\frac{e+2}{3}$$ This solution is valid because substituting it back into the original log function results in $3x-2=e$, and since $e > 0$, the domain requirement is satisfied.

## Substitution with exponential terms

Some equations contain both $e^y$ and $e^{-y}$. To solve these, we can let $u=e^y$, noting that $u>0$ and $e^{-y}=\frac{1}{u}$.

For the equation $3e^y+10e^{-y}=11$, we substitute $u$ and multiply through by $u$. This process turns the expression into a quadratic equation:

$$$3u+\frac{10}{u}=11 \Rightarrow 3u^2-11u+10=0$$

Factorising the quadratic gives $(3u-5)(u-2)=0$, so $u=\frac{5}{3}$ or $u=2$. Converting back to the original variable gives $y=\ln\left(\frac{5}{3}\right)$ or $y=\ln 2$.

## Growth models

Models of the form $P=Ae^{kt}$ have initial value $A$ because $P(0)=A$. The sign of $k$ tells you whether the model grows or decays.

Consider the model $P=60e^{0.07t}$ where $t$ is in weeks. The initial population is 60 and the rate of growth is given by the derivative: $$\frac{dP}{dt}=4.2e^{0.07t}$$

At $t=10$, the rate is $4.2e^{0.7}\approx 8.46$ plants per week. This value represents the instantaneous rate of change of the population at that specific time.

To find when the population exceeds 300, solve $60e^{0.07t}>300$, which simplifies to $e^{0.07t}>5$. Taking logs gives $t>\frac{\ln 5}{0.07}\approx 22.99$, and you would round up to 23 if a whole number of weeks is required.

## Graphs, range, and tangents

![Graph of $y = e^{x+2} - 4$ showing asymptote, intercepts, and tangent at the y-intercept](../assets/002-2c70753a-1e4d-45a9-9780-224273e1d9de.jpeg)

The graph of $y=e^{x+2}-4$ is the curve $y=e^x$ shifted left 2 units and down 4 units. Its horizontal asymptote is $y=-4$, meaning the range of the function is $y>-4$.

The $y$-intercept is found by setting $x=0$, giving the point $A(0, e^2-4)$. To find the $x$-intercept, we set $e^{x+2}=4$, which leads to $x+2 = \ln 4$, resulting in the coordinate $B(\ln 4-2, 0)$.

By differentiating, we find $f'(x)=e^{x+2}$, so the gradient at the intercept $A$ is $e^2$. Using the point-gradient form, the equation of the tangent at $A$ is:

$$y-(e^2-4)=e^2x$$

## Check yourself

1. Solve $2^{x+1}=64$.

   - $$5$ ✔

   - $$6$

   - $$32$

   - $$64$

   _Explanation:_ Because $64=2^6$, the bases match and you equate powers to get $x+1=6$. The common wrong answer $6$ comes from spotting the exponent on 64 but forgetting to subtract 1.

2. Which expression is equivalent to $2\log_a(x+3)-\log_a 7$?

   - $$\log_a\left(\frac{(x+3)^2}{7}\right)$ ✔

   - $$\log_a\left((x+3)^2-7\right)$

   - $$\log_a\left(\frac{x+6}{7}\right)$

   - $$2\log_a\left(\frac{x+3}{7}\right)$

   _Explanation:_ A is correct because the power law squares the whole argument and the subtraction law turns subtraction of logs into division. The common wrong answer B treats subtraction of logs as subtraction inside the argument, but $\log A-\log B=\log\left(\frac{A}{B}\right)$, not $\log(A-B)$.

3. Which is the exact solution set of $3e^y+10e^{-y}=11$?

   - $$y=\ln\left(\frac{5}{3}\right)$ or $y=\ln 2$ ✔

   - $$y=\frac{5}{3}$ or $y=2$

   - $$y=\ln\left(\frac{3}{5}\right)$ or $y=-\ln 2$

   - $$y=\ln\left(\frac{5}{3}\right)$ only

   _Explanation:_ After the substitution $u=e^y$, you solve for $u$ first and then return to $y$ by taking logs, so the answers are $y=\ln\left(\frac{5}{3}\right)$ and $y=\ln 2$. The common wrong answer B forgets to undo the substitution and leaves the values of $u$ instead of the values of $y$.

4. Which statement about $f(x)=e^{x+2}-4$ is correct?

   - The range is $y>-4$ ✔

   - The horizontal asymptote is $y=4$

   - The y-intercept is $(0,e^2+4)$

   - The x-intercept is $(2-\ln 4,0)$

   _Explanation:_ A is correct because $e^{x+2}$ is always positive, so $e^{x+2}-4$ is always greater than $-4$. The common wrong answer D comes from rearranging $x+2=\ln 4$ incorrectly: the correct step is $x=\ln 4-2$.
