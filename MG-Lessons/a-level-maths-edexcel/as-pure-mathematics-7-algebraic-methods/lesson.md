# as-pure-mathematics-7-algebraic-methods — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Polynomials, roots and the factor theorem

A polynomial in $x$ is an expression built from powers of $x$, such as $3x^3-2x+5$. A root is a value of $x$ that makes the polynomial 0, and a factor is an expression that divides it exactly.

The factor theorem is the key shortcut: $(x-a)$ is a factor of $f(x)$ exactly when $f(a)=0$. So if the factor is $(x+3)$, you test $x=-3$, because $x+3=0$ gives the root $x=-3$.

For integer polynomials, sensible first tests are small numbers. Often these are factors of the constant term divided by factors of the leading coefficient.

## Finding unknown coefficients from substitutions

If $f(x)=x^3+4x^2+px+q$ with $f(2)=0$, substitute $x=2$ carefully. This process turns a function condition into a linear equation in $p$ and $q$.

$$
8+16+2p+q=0 \Rightarrow 2p+q=-24
$$

Now use $f(-3)=10$. Be careful with signs, because $(-3)^2=9$ but $(-3)^3=-27$. This substitution provides our second linear equation.

$$
-27+36-3p+q=10 \Rightarrow -3p+q=1
$$

Subtract the second equation from the first to solve for the coefficients:

$$
(2p+q)-(-3p+q)=-24-1 \Rightarrow 5p=-25 \Rightarrow p=-5
$$

Then $2(-5)+q=-24$, so $q=-14$.

## Factorising a cubic completely

To factorise $f(x)=2x^3-5x^2-4x+12$, first test a likely root. Since
$$f(2)=2(2)^3-5(2)^2-4(2)+12=16-20-8+12=0,$$
the factor theorem tells us that $(x-2)$ is a factor.

At AS level, comparing coefficients is often cleaner than long division. Write
$$f(x)=(x-2)(Ax^2+Bx+C).$$
Expand the right-hand side:
$$ (x-2)(Ax^2+Bx+C)=Ax^3+(B-2A)x^2+(C-2B)x-2C. $$

Now compare coefficients with $2x^3-5x^2-4x+12$ to get $A=2$, $B=-1$, and $C=-6$. This gives us the following intermediate form:
$$f(x)=(x-2)(2x^2-x-6).$$

Factor the quadratic to finish:
$$2x^2-x-6=(2x+3)(x-2),$$
so the complete factorisation is $f(x)=(x-2)^2(2x+3)$.

## Solving cubics and counting real roots

![Cubic graph on labelled axes showing a blue curve crossing the x-axis at a simple root and touching then turning at a repeated root](../assets/001-b94cf151-3669-4a0f-889e-8d73012490f9.jpeg)
A simple root makes a cubic cross the $x$-axis, while a repeated root makes it touch the axis and turn. After you remove one linear factor, the remaining quadratic tells you whether the cubic has two more real roots, one repeated real root, or no more real roots.

For $r(x)=x^3+6x^2+4x-15$, test $x=-3$:
$$r(-3)=-27+54-12-15=0.$$
So $(x+3)$ is a factor and $$r(x)=(x+3)(x^2+3x-5).$$

Now solve the quadratic factor with the formula $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.$$ Here, $$x=\frac{-3\pm\sqrt{3^2-4(1)(-5)}}{2}=\frac{-3\pm\sqrt{29}}{2},$$ so the other two roots are $x\approx -4.19$ and $x\approx 1.19$.

Since $29>0$, the quadratic has two distinct real roots, so the cubic has three real roots altogether. If the quadratic factor had a negative discriminant instead, it would give no real roots, and only the linear factor would produce a real solution.

## Proofs, disproofs and counterexamples

A proof must cover every allowed case, not just a few examples that seem to fit. For parity proofs, write even integers as $2n$ and odd integers as $2n+1$.

To show that neighbouring odd integers always add to a multiple of 4, write them as $2n+1$ and $2n+3$. Then $$ (2n+1)+(2n+3)=4n+4=4(n+1),$$ which is a multiple of 4 because $n+1$ is an integer.

To disprove an "always" statement, one counterexample is enough. For example, the claim "$n^2-n+3$ is prime for every positive integer $n$" fails at $n=3$ because $$3^2-3+3=9,$$ and $9$ is not prime.

## Proving inequalities by completing the square

To prove an inequality, start by moving everything to one side to set the expression against zero:
$$x^2+6x-(2x-7)=x^2+4x+7.$$
Now the objective is to show that this resulting quadratic expression is always positive.

Complete the square for the expression:
$$x^2+4x+7=(x+2)^2+3.$$
A square is never negative, so we know that $(x+2)^2 \ge 0$ for all real values of $x$.

Therefore, $(x+2)^2+3 > 0$ for every real $x$, which means $x^2+6x > 2x-7$ is always true. This method is powerful because it turns a messy inequality into the sum of a square and a positive constant.

## Check yourself

1. If $(x+4)$ is a factor of $f(x)$, which value should you substitute into $f(x)$ to test it?

   - $$4$

   - $$-4$ ✔

   - $$\frac{1}{4}$

   - $$0$

   _Explanation:_ If $(x+4)$ is a factor, then $x+4=0$ so the root is $x=-4$, and the factor theorem says test $f(-4)$. The common wrong answer is A because students often forget that the sign changes when you solve $x+4=0$.

2. Which is the complete factorisation of $2x^3-5x^2-4x+12$?

   - $$(x-2)^2(2x+3)$ ✔

   - $$(x+2)^2(2x-3)$

   - $$(x-2)(x+2)(2x-3)$

   - $$(2x+3)^2(x-2)$

   _Explanation:_ After taking out $(x-2)$, the remaining quadratic is $2x^2-x-6=(2x+3)(x-2)$, so $(x-2)$ appears twice. A common wrong answer is B because it flips the signs and would make the tested root $x=-2$ instead of $x=2$.

3. Stretch: Which argument is a valid proof that $n^2+1$ is never a multiple of 4 for positive integers $n$?

   - Check $n=1,2,3,4$ and see the statement works each time.

   - Write $n=2k$ or $n=2k+1$, then show $n^2+1=4k^2+1$ or $4(k^2+k)+2$ ✔

   - Since $n^2$ is always a multiple of 4, $n^2+1$ cannot be.

   - Because prime numbers have odd squares.

   _Explanation:_ B handles every positive integer by splitting into even and odd cases. The common wrong answer is A because checking a few values may suggest a pattern, but it does not prove an "always" statement.
