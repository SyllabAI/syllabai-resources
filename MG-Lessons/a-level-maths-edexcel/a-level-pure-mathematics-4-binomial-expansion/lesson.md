# a-level-pure-mathematics-4-binomial-expansion — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What binomial expansion means

A binomial has two terms, such as $1+3x$ or $9+6x$. Expanding a binomial means rewriting a power like $(1+u)^n$ as a series in ascending powers of $x$, starting with the constant term.

If $n$ is a positive integer, the expansion stops. In that case, the formula is:
$$(a+b)^n=\sum_{r=0}^{n}\binom{n}{r}a^{n-r}b^r$$

If $n$ is fractional or negative, the expansion is usually infinite. Then the first few terms are:
$$(1+u)^n=1+nu+\frac{n(n-1)}{2}u^2+\frac{n(n-1)(n-2)}{6}u^3+\cdots$$

It also helps to rewrite roots and reciprocals as powers first. For example, $\sqrt{1+6x}=(1+6x)^{\frac{1}{2}}$ and $\frac{1}{\sqrt{9+x}}=(9+x)^{-\frac{1}{2}}$.

## Worked example: finding a coefficient

For positive integer powers, the general term in $(3+2x)^7$ is $\binom{7}{r}3^{7-r}(2x)^r$. The power of $x$ is controlled by $r$, so choosing the right value of $r$ picks out the term we want.

To get the $x^5$ term, set $r=5$ to identify the specific part of the expansion. This results in the following expression: $$\binom{7}{5}3^{7-5}(2x)^5$$

Now simplify the coefficient only by calculating the product: $$\binom{7}{5}3^2 2^5=21\cdot 9\cdot 32=6048$$ So the $x^5$ term is $6048x^5$, and the coefficient is $6048$.

## Getting to standard form

![Flow diagram showing how (9+6x)^(-1/2) is factored, expanded, and given a validity range](../assets/001-b8bb994b-3a66-481c-be8f-971f230e7ac6.jpeg)

For fractional or negative powers, the formula is built for $(1+u)^n$, so a bracket like $(9+6x)^{-\frac{1}{2}}$ must be rearranged first. Factor out the constant term so the inside starts with 1.

$$$(9+6x)^{-\frac{1}{2}}=9^{-\frac{1}{2}}\left(1+\frac{2}{3}x\right)^{-\frac{1}{2}}=\frac{1}{3}\left(1+\frac{2}{3}x\right)^{-\frac{1}{2}}$$

Now $A=\frac{1}{3}$, $u=\frac{2}{3}x$, and $n=-\frac{1}{2}$. Once $u$ is identified, expand the bracket and then multiply by the outside factor $A$. Do not try to expand $9+6x$ directly as though it were $1+u$.

## Worked example: factoring first

Start from the standard form $(1+u)^n$ and substitute $u=\frac{2}{3}x$ and $n=-\frac{1}{2}$ into the first four terms. Keep the constant, $x$, $x^2$, and $x^3$ terms.
$$\left(1+\frac{2}{3}x\right)^{-\frac{1}{2}}=1+\left(-\frac{1}{2}\right)\left(\frac{2}{3}x\right)+\frac{\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)}{2}\left(\frac{2}{3}x\right)^2+\frac{\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)\left(-\frac{5}{2}\right)}{6}\left(\frac{2}{3}x\right)^3+\cdots$$

This simplifies to
$$\left(1+\frac{2}{3}x\right)^{-\frac{1}{2}}=1-\frac{x}{3}+\frac{x^2}{6}-\frac{5x^3}{54}+\cdots$$
Multiplying by $\frac{1}{3}$ gives
$$(9+6x)^{-\frac{1}{2}}=\frac{1}{3}-\frac{x}{9}+\frac{x^2}{18}-\frac{5x^3}{162}+\cdots$$

The expansion is valid while $|u|<1$. Here that means
$$\left|\frac{2}{3}x\right|<1 \Rightarrow |x|<\frac{3}{2}$$
so the range of validity is $-\frac{3}{2}<x<\frac{3}{2}$.

## Worked example: approximation

Binomial expansions are useful when $|u|$ is small, because higher powers get tiny very quickly. To estimate $\sqrt{8.8}$, we set $9-2x=8.8$, so $x=0.1$ and $\sqrt{8.8}=(9-2x)^{\frac{1}{2}}$.

Now factor the 9 and expand the expression using the binomial formula:
$$
(9-2x)^{\frac{1}{2}}=3\left(1-\frac{2x}{9}\right)^{\frac{1}{2}}
$$
Using the general expansion $(1+u)^{\frac{1}{2}}=1+\frac{1}{2}u-\frac{1}{8}u^2+\frac{1}{16}u^3+\cdots$, we get
$$
(9-2x)^{\frac{1}{2}}=3-\frac{x}{3}-\frac{x^2}{54}-\frac{x^3}{486}+\cdots
$$

Substitute $x=0.1$ into the series to find the numerical estimate:
$$
3-\frac{0.1}{3}-\frac{0.1^2}{54}-\frac{0.1^3}{486}=2.966479\ldots
$$
So $\sqrt{8.8}\approx 2.96648$ to 5 decimal places. Because $|u|=\frac{1}{45}$ is very small, the approximation is highly accurate.

## Worked example: multiplying expansions

Sometimes you expand one part and then multiply by another factor. For
$$\frac{1+x}{(1-2x)^2}=(1+x)(1-2x)^{-2}$$
expand the term $(1-2x)^{-2}$ first using the binomial series formula.

Using $n=-2$ and $u=-2x$, the expansion is:
$$(1-2x)^{-2}=1+4x+12x^2+32x^3+\cdots$$

Now multiply this series by $1+x$, ensuring you only keep terms that contribute up to $x^3$.
$$(1+x)(1+4x+12x^2+32x^3)=1+4x+12x^2+32x^3+x+4x^2+12x^3+\cdots$$

By collecting like terms, we get the final result:
$$\frac{1+x}{(1-2x)^2}=1+5x+16x^2+44x^3+\cdots$$
Any products resulting in $x^4$ or higher powers can be ignored for this specific expansion.

## Check yourself

1. In $(1-2x)^{-3}$, what are $u$ and $n$ when it is written as $(1+u)^n$?

   - $$u=-2x,\ n=-3$ ✔

   - $$u=1-2x,\ n=-3$

   - $$u=2x,\ n=-3$

   - $$u=-2x,\ n=3$

   _Explanation:_ The bracket must match $1+u$ exactly, so $1-2x=1+(-2x)$. That gives $u=-2x$ and the power is still $n=-3$. The common wrong answer C misses the negative sign inside the bracket. Hint: Compare the bracket term by term with $1+u$.

2. What is the range of validity for the expansion of $(9+6x)^{-\frac{1}{2}}$?

   - $$-\frac{3}{2}<x<\frac{3}{2}$ ✔

   - $$-\frac{2}{3}<x<\frac{2}{3}$

   - $$x>-\frac{3}{2}$

   - All real values of $x$

   _Explanation:_ After factoring, the bracket is $\left(1+\frac{2}{3}x\right)^{-\frac{1}{2}}$, so $u=\frac{2}{3}x$. For fractional or negative powers we need $|u|<1$, giving $\left|\frac{2}{3}x\right|<1$ and therefore $|x|<\frac{3}{2}$. The common wrong answer B comes from not solving the inequality fully for $x$.

3. The expansion of $\frac{a+bx}{\sqrt{4+x}}$ begins $2+x+\cdots$. What are $a$ and $b$?

   - $$a=4,\ b=\frac{5}{2}$ ✔

   - $$a=2,\ b=1$

   - $$a=4,\ b=2$

   - $$a=8,\ b=5$

   _Explanation:_ First expand $(4+x)^{-\frac{1}{2}}=\frac{1}{2}-\frac{x}{16}+\cdots$. Then $(a+bx)\left(\frac{1}{2}-\frac{x}{16}+\cdots\right)=\frac{a}{2}+\left(\frac{b}{2}-\frac{a}{16}\right)x+\cdots$. Matching with $2+x+\cdots$ gives $\frac{a}{2}=2$, so $a=4$, and then $\frac{b}{2}-\frac{1}{4}=1$, so $b=\frac{5}{2}$. The common wrong answer C forgets that the constant $a$ also contributes to the $x$ term through $a\left(-\frac{x}{16}\right)$.
