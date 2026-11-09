# as-pure-mathematics-7-3-the-factor-theorem — lesson

_Lane: `a-level-maths-edexcel` · grade — · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## From substitution to factors

A polynomial is an expression like $2x^3-5x^2-4x+3$. When you see $f(2)$, you substitute $x=2$ everywhere in the expression.

The factor theorem says that, for a polynomial $f(x)$, the bracket $x-a$ is a factor if and only if $f(a)=0$. This turns a division question into a substitution question.

The sign must be handled carefully. If the factor is $x+3$, then you test $x=-3$ because $x+3=x-(-3)$.

## Roots, factors, and the graph

![Cubic graph crossing the x-axis at negative 2, 1, and 3, with each root matched to factors x plus 2, x minus 1, and x minus 3](../assets/001-c92feab3-d2c7-4e31-95f4-dae278f05ef8.jpeg)

On a graph, roots are the $x$-values where the curve meets the $x$-axis. If the root is $x=a$, the matching factor is $x-a$.

A negative root reverses the sign in the factor. So root $x=-2$ gives factor $x+2$, not $x-2$.

Possible integer roots often come from the factors of the constant term when the coefficients are integers. They are only candidates, so you still must test them by substitution.

## Showing a bracket is a factor

To show that $x+2$ is a factor of $f(x)=2x^3+3x^2-8x-12$, first rewrite the bracket as $x-(-2)$. This tells us to test the specific value $x=-2$ using the Factor Theorem.

Substitute carefully into the function expression:
$$f(-2)=2(-2)^3+3(-2)^2-8(-2)-12$$
Work out the powers first to get $f(-2)=2(-8)+3(4)+16-12$.

Finally, simplify the remaining arithmetic:
$$f(-2)=-16+12+16-12=0$$
Since the result is zero, the factor theorem proves that $x+2$ is a factor of the polynomial.

## Worked example: factorising a cubic completely

Factorise $2x^3-3x^2-11x+6$ completely by testing sensible roots. Since the constant term is $6$, small candidates are $x=\pm 1,\pm 2,\pm 3,\pm 6$. We begin with two quick tests: $$f(2)=2(2)^3-3(2)^2-11(2)+6=-12,\qquad f(3)=2(3)^3-3(3)^2-11(3)+6=0$$

Since $f(3)=0$, $x-3$ is the linear factor we want. We then write the cubic in the form $(x-3)(Ax^2+Bx+C)$, which expands to $Ax^3+(B-3A)x^2+(C-3B)x-3C$.

Compare coefficients with $2x^3-3x^2-11x+6$ to get $A=2$, $B-3A=-3$, $C-3B=-11$, and $-3C=6$, so $A=2, B=3, C=-2$. This yields the complete factorisation: $$2x^3-3x^2-11x+6=(x-3)(2x^2+3x-2)=(x-3)(2x-1)(x+2)$$

## When the quadratic needs the formula

Suppose you want to solve $x^3+5x^2+x-7=0$. Testing $x=1$ gives $f(1)=1+5+1-7=0$, which confirms that $x-1$ is a factor according to the Factor Theorem.

Divide the polynomial to find the remaining quadratic factor. This results in the following expression: $$x^3+5x^2+x-7=(x-1)(x^2+6x+7)$$

The quadratic $x^2+6x+7$ does not factorise nicely over integers. Therefore, we must use the quadratic formula $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ with the coefficients $a=1$, $b=6$, and $c=7$.

This gives the final roots: $$x=\frac{-6\pm\sqrt{36-28}}{2}=\frac{-6\pm\sqrt{8}}{2}$$ Including the integer root, the three solutions are $x=1$, $x\approx -1.59$, and $x\approx -4.41$.

## Check yourself

1. For the possible factor $x+3$, which value should you substitute into $f(x)$?

   - $$-3$ ✔

   - $$3$

   - $$\frac{1}{3}$

   - $$-\frac{1}{3}$

   _Explanation:_ The correct test value is $-3$ because $x+3$ can be written as $x-(-3)$. The most common wrong answer is B, but substituting $3$ would test whether $x-3$ is a factor instead.

2. For $f(x)=x^3-4x^2-x+4$, you calculate $f(1)=0$. Which conclusion follows?

   - $$x-1$ is a factor ✔

   - $$x+1$ is a factor

   - $$x=-1$ is definitely the only root

   - The polynomial cannot be factorised further

   _Explanation:_ By the factor theorem, $f(1)=0$ means $x-1$ is a factor. The most common wrong answer is B, but root $x=1$ matches factor $x-1$, not $x+1$.

3. Let $f(x)=x^3+2x^2+px+q$. Given $f(2)=0$ and $f(-3)=10$, which pair of equations should you form first?

   - $$2p+q=-16$ and $-3p+q=19$ ✔

   - $$2p+q=16$ and $-3p+q=19$

   - $$2p+q=-16$ and $3p+q=19$

   - $$p+q=-16$ and $-3p+q=10$

   _Explanation:_ Substituting $x=2$ gives $8+8+2p+q=0$, so $2p+q=-16$. Substituting $x=-3$ gives $-27+18-3p+q=10$, so $-3p+q=19$. The most common wrong answer is option c because it forgets that the $px$ term becomes $-3p$ when $x=-3$. Hint: Use brackets carefully when substituting $-3$.
