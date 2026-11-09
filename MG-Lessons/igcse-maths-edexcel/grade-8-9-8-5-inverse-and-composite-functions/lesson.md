# grade-8-9-8-5-inverse-and-composite-functions — lesson

_Lane: `igcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Functions, inputs and outputs

A function gives exactly one output for each allowed input. The allowed inputs are called the domain, and the outputs you can get are called the range.

Function notation tells you what to substitute into the rule. If $f(x)=3x-2$, then $f(5)=3(5)-2=13$.

When the input is negative, keep it in brackets so the sign stays correct. For example, if $h(x)=2x-7$, then $h(-4)=2(-4)-7$.

## Domains and excluded values

Not every algebraic rule accepts every real number as an input. Two common restrictions involve division by zero and square roots of negative numbers.

For $p(x)=\frac{6}{x-3}$, the denominator cannot be 0, so $x-3 \neq 0$ and $x \neq 3$. That means 3 must be excluded from the domain.

For $q(x)=\sqrt{15-x}$, the expression inside the root must be non-negative, so $15-x \ge 0$. Solving gives $x \le 15$, so the domain is all real numbers up to and including 15.

## What an inverse function does

![Graph of a function and its inverse reflected in the line y=x, with points (2,5) and (5,2) labelled](../assets/001-46105baf-cb9c-4dce-896a-d034b47e9269.jpeg)

An inverse function reverses the original rule, so inputs and outputs swap over. If $f(2)=5$, then $f^{-1}(5)=2$.

On a graph, $f$ and $f^{-1}$ are reflections in the line $y=x$ because each point $(a,b)$ becomes $(b,a)$. This means the domain of $f$ becomes the range of $f^{-1}$, and the range of $f$ becomes the domain of $f^{-1}$.

A function must be one-to-one before its inverse is also a function. This is why quadratics often need a restricted domain, and it is also why $f^{-1}(x)$ does not mean $\frac{1}{f(x)}$.

## Worked example: inverse of a linear function

For $f(x)=\frac{4x-7}{3}$, start by writing the rule with $y$. This makes the inverse steps easier to follow.
$$
y=\frac{4x-7}{3}
$$

Swap $x$ and $y$, because the inverse reverses inputs and outputs. Then start rearranging.
$$
x=\frac{4y-7}{3}
$$

Multiply by 3 and then add 7, so $3x=4y-7$ and $3x+7=4y$. Dividing by 4 gives
$$
y=\frac{3x+7}{4}
$$

Now rename $y$ as $f^{-1}(x)$. You can check it by seeing that $f(f^{-1}(x))=x$.
$$
f^{-1}(x)=\frac{3x+7}{4}
$$

## Worked example: inverse of a quadratic

A quadratic is not one-to-one across all real numbers, because different inputs can give the same output. For example, $2^2=4$ and $(-2)^2=4$, so we must restrict the domain first.

Suppose $g(x)=x^2+10x+7$ with domain $x \ge -5$. Completing the square gives
$$
g(x)=(x+5)^2-18
$$
This shows the turning point is at $(-5,-18)$.

Write $y=(x+5)^2-18$ and solve for $x$. Rearranging gives $y+18=(x+5)^2$, and because $x \ge -5$ we take the positive square root and get
$$
x=-5+\sqrt{y+18}
$$

Replace $y$ with $x$ to write the inverse. The domain of $g^{-1}$ is $x \ge -18$, and its range is all real values greater than or equal to -5.
$$
g^{-1}(x)=-5+\sqrt{x+18}
$$

## Composite functions: do the inside first

A composite function means one function is done after another. The notation $fg(x)$ means $f(g(x))$, so you read it from right to left and evaluate the inner function first.

If $f(x)=\frac{3}{x-2}$ and $g(x)=x+5$, then we calculate $fg(1)$ by starting with $g$. First $g(1)=6$, and then $f(6)=\frac{3}{6-2}=\frac{3}{4}$.

$$$fg(1)=f(g(1))$$

Order matters because $gf(1)$ means something different. Here $f(1)=-3$, so $gf(1)=g(-3)=2$, which is not the same value as $\frac{3}{4}$.

## Check yourself

1. For $q(x)=\sqrt{15-x}$, which domain is correct?

   - $$x \le 15$ ✔

   - $$x \ge 15$

   - $$x \neq 15$

   - All real values of $x$

   _Explanation:_ Inside a square root must be non-negative, so $15-x \ge 0$ and therefore $x \le 15$. The common wrong answer $x \ge 15$ comes from solving the inequality in the wrong direction after moving the $x$ term.

2. The function $g(x)=x^2+10x+7$ has domain $x \ge -5$. Which is $g^{-1}(x)$?

   - $$-5+\sqrt{x+18}$ ✔

   - $$-5-\sqrt{x+18}$

   - $$-5\pm\sqrt{x+18}$

   - $$\sqrt{x-18}-5$

   _Explanation:_ Completing the square gives $g(x)=(x+5)^2-18$, and the restricted domain $x \ge -5$ means we must choose the positive square-root branch. The common wrong answer $-5\pm\sqrt{x+18}$ ignores the domain restriction and gives two outputs for one input, so it is not a function.

3. If $f(x)=2x+1$ and $g(x)=x^2$, what is $fg(3)$?

   - 19 ✔

   - 49

   - 7

   - 18

   _Explanation:_ Apply $g$ first, so $g(3)=9$, and then apply $f$, giving $f(9)=19$. The common wrong answer 49 comes from doing $f$ first and finding $gf(3)$ instead.
