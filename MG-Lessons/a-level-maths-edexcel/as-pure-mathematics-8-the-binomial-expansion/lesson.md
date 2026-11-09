# as-pure-mathematics-8-the-binomial-expansion — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What the binomial expansion is

![Pascal's triangle up to row 6 with row 5 highlighted and arrows showing powers of a decrease while powers of b increase](../assets/001-bb6fafae-f665-42f4-99ea-a4fd6c71ef44.jpeg)
A binomial is an expression with two terms, such as $a+b$ or $2-5x$. Expanding a binomial means multiplying it out and collecting like terms.

Writing in ascending powers of $x$ means starting with the constant, then $x$, then $x^2$, and so on. For a positive integer $n$, the finite binomial theorem is:

$$
(a+b)^n=\sum_{r=0}^{n}\binom{n}{r}a^{n-r}b^r
$$

The number $\binom{n}{r}$ is the binomial coefficient, and it gives the coefficient of the term containing $b^r$. Pascal's triangle gives the same coefficients row by row, so row 5 gives $1, 5, 10, 10, 5, 1$ for $(a+b)^5$.

As you move across the expansion, the power of $a$ goes down while the power of $b$ goes up. This pattern maintains a consistent total degree for every term in the series.

## Worked example with first three terms

To find the first three terms of $\left(2+\frac{x}{2}\right)^6$, identify $a=2$, $b=\frac{x}{2}$, and $n=6$. Because the question asks for the first three terms in ascending powers of $x$, you only need $r=0,1,2$.

The first two terms are
$$
T_{0}=\binom{6}{0}2^6=64,\qquad T_{1}=\binom{6}{1}2^5\left(\frac{x}{2}\right)=96x
$$
Notice that the $x$ term still includes the factor $2^5$, so you cannot just do $6\left(\frac{x}{2}\right)$.

For the quadratic term,
$$
T_{2}=\binom{6}{2}2^4\left(\frac{x}{2}\right)^2=60x^2
$$
So the first three terms are
$$
\left(2+\frac{x}{2}\right)^6=64+96x+60x^2+\cdots
$$

## Negative signs create alternating terms

If the second part of the binomial is negative, the signs alternate because odd powers of a negative quantity stay negative while even powers become positive. For $(2-5x)^7$, use $a=2$, $b=-5x$, and $n=7$.

The first three terms are:
$$
T_{0}=128,\qquad T_{1}=\binom{7}{1}2^6(-5x)=-2240x,\qquad T_{2}=\binom{7}{2}2^5(-5x)^2=16800x^2
$$
The $x^2$ term is positive because $(-5x)^2$ is positive.

The next term is $T_{3}=\binom{7}{3}2^4(-5x)^3=-70000x^3$. Thus, in ascending powers of $x$, the binomial expansion is:
$$
(2-5x)^7=128-2240x+16800x^2-70000x^3+\cdots
$$

## Using an expansion to estimate a power

Expansions are useful for numbers close to a convenient value. To estimate $1.04^8$, write it as $(1+4x)^8$ and solve $1+4x=1.04$, which gives $x=0.01$.

Expand only as far as you need: $$(1+4x)^8=1+8(4x)+\binom{8}{2}(4x)^2+\binom{8}{3}(4x)^3+\cdots=1+32x+448x^2+3584x^3+\cdots$$

Using a few terms works well because $x=0.01$ is small. Substitute $x=0.01$ into the truncated expansion: $$1+32(0.01)+448(0.01)^2+3584(0.01)^3=1.368384$$ So $1.04^8\approx 1.3684$ to 5 significant figures.

## Comparing coefficients without over-expanding

Suppose $f(x)=(ax+b)\left(2+\frac{x}{8}\right)^8$ and the first two terms are $40+72x$. Because we only need the constant and $x$ terms of $f(x)$, we only need the constant and $x$ terms of the binomial expansion to solve for the variables.

For the binomial, $$\left(2+\frac{x}{8}\right)^8=256+128x+\cdots$$ Multiplying by $(ax+b)$ gives $(ax+b)(256+128x+\cdots)$, so the constant term is $256b$. Therefore, $256b=40$ and $b=\frac{5}{32}$.

The coefficient of $x$ comes from $256ax$ and $128bx$. That gives the equation $$256a+128b=72$$ Substitute $b=\frac{5}{32}$ to get $256a+20=72$, so $a=\frac{13}{64}$. This is faster and safer than expanding every term in the product.

## Exam checks that save marks

Before expanding, identify the constant part, the $x$ part, and the power. If the question asks for the first three terms, use only $r=0,1,2$ and stop.

When a binomial is multiplied by another factor, keep only the terms that can affect the powers you need. After expanding, rewrite in ascending powers of $x$ and check the sign pattern if the $x$ part was negative.

A quick symmetry check also helps. For example, $$(3+x)^4+(3-x)^4=162+108x^2+2x^4$$ so the odd-power terms cancel and only even powers remain.

## Check yourself

1. In the expansion of $(a+b)^5$, what is the coefficient of $a^3b^2$?

   - $$10$ ✔

   - $$5$

   - $$20$

   - $$15$

   _Explanation:_ The term $a^3b^2$ corresponds to choosing 2 factors of $b$, so its coefficient is $\binom{5}{2}=10$. A common wrong answer is $5$, which is the coefficient of $a^4b$ or $ab^4$, not of $a^3b^2$. Hint: Match the power of $b$ to the value of $r$.

2. What is the coefficient of $x^2$ in the expansion of $(2-5x)^7$?

   - $$16800$ ✔

   - $$-16800$

   - $$-2240$

   - $$70000$

   _Explanation:_ The $x^2$ term is $\binom{7}{2}2^5(-5x)^2=16800x^2$, so the coefficient is positive $16800$. The common wrong answer $-16800$ comes from assuming the signs just keep alternating without checking that an even power of a negative is positive. Hint: Look at the power on $-5x$.

3. In the expansion of $(1+kx)^{10}$, the coefficient of $x^3$ is twice the coefficient of $x$, where $k \ne 0$. What is $k$?

   - $$\pm\frac{1}{\sqrt{6}}$ ✔

   - $$\pm\frac{1}{6}$

   - $$\frac{1}{\sqrt{6}}$

   - $$\pm\sqrt{6}$

   _Explanation:_ Hint: Write only the $x$ term and the $x^3$ term.

The coefficient of $x$ is $10k$ and the coefficient of $x^3$ is $120k^3$. So $120k^3=2(10k)$, and since $k \ne 0$ you can divide by $k$ to get $120k^2=20$, so $k^2=\frac{1}{6}$ and $k=\pm\frac{1}{\sqrt{6}}$. The common wrong answer $\pm\frac{1}{6}$ comes from forgetting to take the square root at the end.
