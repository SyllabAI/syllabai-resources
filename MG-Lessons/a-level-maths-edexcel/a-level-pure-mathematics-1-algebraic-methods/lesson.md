# a-level-pure-mathematics-1-algebraic-methods — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Identities and choosing a method

![Flowchart showing how to choose a partial fraction form by checking whether a fraction is proper, whether factors are distinct or repeated, and when to add a polynomial part](../assets/001-db9cca3e-a54a-4d81-8674-df65c881cc2c.jpeg)

Algebraic methods often turn one expression into another form that is easier to use. A key idea is an identity, written with $\equiv$, which is true for every allowed value of $x$, so you can compare coefficients or substitute convenient values.

For partial fractions, first decide whether the rational function is proper. Then match the denominator: distinct linear factors need one constant numerator each, such as $\frac{A}{x-a}+\frac{B}{x-b}$, while repeated factors need every power, such as $\frac{B}{x-a}+\frac{C}{(x-a)^2}$.

If the fraction is top-heavy, add a polynomial part before decomposing the rest. This decision at the start prevents the most common setup errors.

## Distinct linear factors

For $\frac{3x+11}{(x+2)(x+5)}$, the denominator has two distinct linear factors. To begin the partial fraction decomposition, we set up the following identity:
$$\frac{3x+11}{(x+2)(x+5)} \equiv \frac{A}{x+2}+\frac{B}{x+5}.$$

Multiply through by the full denominator $(x+2)(x+5)$ to clear the fractions. This results in a linear identity which we can use to solve for the unknown constants:
$$3x+11 \equiv A(x+5)+B(x+2).$$

Choose values of $x$ that make one term disappear to solve for the coefficients. Putting $x=-2$ gives $5=3A$, so $A=\frac{5}{3}$, and putting $x=-5$ gives $-4=-3B$, so $B=\frac{4}{3}$.

Finally, write the simplified form by substituting these constants back into the partial fraction structure. Recombining these terms gives back the original numerator $3x+11$:
$$\frac{3x+11}{(x+2)(x+5)} \equiv \frac{5}{3(x+2)}+\frac{4}{3(x+5)}.$$

## Repeated factors need every power

A repeated factor means you must include every power that appears in the partial fraction setup. For the fraction below, we provide terms for both $(x+2)$ and $(x+2)^2$:
$$\frac{4x+1}{(x-1)(x+2)^2} \equiv \frac{A}{x-1}+\frac{B}{x+2}+\frac{C}{(x+2)^2}$$

After multiplying through, you get the identity $4x+1 \equiv A(x+2)^2+B(x-1)(x+2)+C(x-1)$. Substituting $x=1$ gives $5=9A$ ($A=\frac{5}{9}$), and substituting $x=-2$ gives $-7=-3C$ ($C=\frac{7}{3}$).

Use any other convenient value, like $x=0$, to find the remaining constant. This gives $1=4A-2B-C = \frac{20}{9}-2B-\frac{7}{3}$, so $B=-\frac{5}{9}$ and the result is:
$$\frac{4x+1}{(x-1)(x+2)^2} \equiv \frac{5}{9(x-1)}-\frac{5}{9(x+2)}+\frac{7}{3(x+2)^2}$$

## Top-heavy fractions

A rational function is improper if the numerator degree is greater than or equal to the denominator degree. For the following example, we use a linear polynomial part because the numerator is one degree higher than the denominator:
$$\frac{2x^3+7x^2+3x+4}{(x+1)(x+3)} \equiv Ax+B+\frac{C}{x+1}+\frac{D}{x+3}.$$

To solve, multiply through by the denominator $(x+1)(x+3) = x^2+4x+3$:
$$2x^3+7x^2+3x+4 \equiv (Ax+B)(x+1)(x+3)+C(x+3)+D(x+1).$$
Comparing the coefficients of the highest powers gives $A=2$ and $4A+B=7$, which simplifies to $B=-1$.

Now substitute values to remove terms. At $x=-1$, $6=2C$ so $C=3$, and at $x=-3$, $4=-2D$ so $D=-2$. The final identity is:
$$\frac{2x^3+7x^2+3x+4}{(x+1)(x+3)} \equiv 2x-1+\frac{3}{x+1}-\frac{2}{x+3}.$$

## Proof by contradiction

![Flow diagram showing proof by contradiction as assume the opposite, use algebra or number facts, reach an impossible statement, and conclude the original claim is true](../assets/002-9066582f-4fc1-42bd-beac-71cc8241bc5b.jpeg) Proof by contradiction starts by assuming the statement you want is false. You then use algebra or number facts until the assumption forces something impossible, so the original statement must be true.

To show there are no integers $m$ and $n$ with $14m+21n=5$, assume such integers exist. Then $$14m+21n=7(2m+3n),$$ so the left-hand side is a multiple of 7 because $2m+3n$ is an integer.

The equation would then say that 5 is a multiple of 7, which is impossible. That contradiction proves no such integers $m$ and $n$ exist.

## Irrationality by contradiction

To prove $\sqrt{5}$ is irrational, assume the opposite and write it in lowest terms as $$\sqrt{5}=\frac{a}{b},$$ where $a$ and $b$ are coprime integers and $b\neq0$. Squaring gives $$a^2=5b^2.$$

Because 5 divides $a^2$, it divides $a$, so let $a=5k$ for some integer $k$. Substituting gives $$25k^2=5b^2 \Rightarrow b^2=5k^2,$$ so 5 divides $b$ as well.

Now both $a$ and $b$ are divisible by 5, which contradicts the fact that they were coprime. Lowest terms matters because the contradiction is exactly that the numerator and denominator share a common factor.

A similar idea proves that rational plus irrational is irrational. If $r+s$ were rational, then subtracting the rational number $r$ would make $s$ rational, which is impossible.

## Check yourself

1. Which statement is an identity?

   - $$x^2-1 \equiv (x-1)(x+1)$ ✔

   - $$2x+3=11$

   - $$x+4>0$

   - $$3x=3x+1$

   _Explanation:_ Option A is true for every value of $x$, making it an identity. In contrast, option B is an equation that is only true when $x=4$, and option D is a contradiction that is never true. An identity must hold for every allowed value of the variable.

2. Which is the correct starting form for $\frac{4x+1}{(x-1)(x+2)^2}$?

   - $$\frac{A}{x-1}+\frac{B}{(x+2)^2}$

   - $$\frac{A}{x-1}+\frac{B}{x+2}+\frac{C}{(x+2)^2}$ ✔

   - $$\frac{Ax+B}{(x-1)(x+2)^2}$

   - $$\frac{A}{x-1}+\frac{Bx+C}{x+2}$

   _Explanation:_ A repeated factor needs a term for every power, so both $\frac{B}{x+2}$ and $\frac{C}{(x+2)^2}$ are required. The common wrong choice A misses the $\frac{B}{x+2}$ term, so it cannot produce all possible numerators after recombining.

3. In the contradiction proof for $14m+21n=5$, what is the impossible statement?

   - $$m=n$

   - $$5$ is a multiple of 7 ✔

   - $$2m+3n=0$

   - $$14m+21n$ is odd

   _Explanation:_ Factoring gives $14m+21n=7(2m+3n)$, so the left-hand side must be divisible by 7. The common wrong choice C is not forced by the algebra; the contradiction is specifically that 5 would have to be divisible by 7.

4. Stretch: Let $r$ be rational and $s$ be irrational. If you assume $r+s$ is rational, what gives the contradiction?

   - $$(r+s)-r=s$ would be rational ✔

   - $$(r+s)+r$ must be irrational

   - $$rs$ must be rational

   - $$r$ must be irrational

   _Explanation:_ The difference of two rational numbers is rational, so from the assumption that $r+s$ is rational, subtracting $r$ would force $s$ to be rational. The common wrong choice C talks about a product, but the argument uses subtraction, not multiplication.
