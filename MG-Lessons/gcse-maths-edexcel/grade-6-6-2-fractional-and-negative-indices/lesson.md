# grade-6-6-2-fractional-and-negative-indices — lesson

_Lane: `gcse-maths-edexcel` · grade 6 · 5 content steps · 2 check questions (source: MathsGenie lessons)_

## Extending the index laws

![Flow diagram showing that the denominator gives the root, the numerator gives the power, and a negative index means reciprocal](../assets/001-fce93033-1719-42db-ab8e-3d3b8a507641.jpeg)
In $a^n$, $a$ is the base and $n$ is the index. The diagram shows how a fractional index splits into a root and a power, while a negative index tells you to take a reciprocal.

The key laws are below.
$$a^m \cdot a^n = a^{m+n}, \qquad \frac{a^m}{a^n} = a^{m-n}, \qquad \left(a^m\right)^n = a^{mn}.$$

These work when the base is the same. These are not separate topics: they are all part of the same pattern of powers. A quick memory aid is denominator = root, numerator = power.

## Fractional indices are roots

A power of $\frac{1}{2}$ means square root, and a power of $\frac{1}{3}$ means cube root. More generally, for positive $a$, use this rule:

$$$a^{\frac{m}{n}} = \left(\sqrt[n]{a}\right)^m$$

The denominator tells you which root to take, and the numerator tells you which power to apply after that. Taking the root first is usually easier because it keeps the numbers smaller. For example:

$$$144^{\frac{1}{2}} = \sqrt{144} = 12, \qquad 216^{\frac{1}{3}} = \sqrt[3]{216} = 6.$$

At GCSE, when you evaluate a square root like $49^{\frac{1}{2}}$, you use the positive root. This is the standard convention used across all index and root problems.

## Worked example: positive and negative fractional indices

To evaluate $27^{\frac{2}{3}}$, use the denominator first. The denominator 3 gives the cube root and the numerator 2 tells you to square.

$$$27^{\frac{2}{3}} = \left(\sqrt[3]{27}\right)^2 = 3^2 = 9.$$

For $16^{-\frac{3}{2}}$, ignore the negative sign at first and work out the positive fractional power. Doing the positive part first keeps the method tidy.

$$$16^{\frac{3}{2}} = \left(\sqrt{16}\right)^3 = 4^3 = 64.$$ Now bring back the negative sign by taking the reciprocal: $$16^{-\frac{3}{2}} = \frac{1}{64}.$$ The common mistake is to stop at $64$ and forget the reciprocal.

## Fractions in brackets and variables

When the base is a fraction in brackets, the whole fraction is being powered. Keep the brackets in your working so you do not only change the top or the bottom.

For $\left(\frac{27}{64}\right)^{-\frac{2}{3}}$, do the positive power first:
$$\left(\frac{27}{64}\right)^{\frac{2}{3}} = \left(\sqrt[3]{\frac{27}{64}}\right)^2 = \left(\frac{3}{4}\right)^2 = \frac{9}{16}.$$

Then take the reciprocal, so $\left(\frac{27}{64}\right)^{-\frac{2}{3}} = \frac{16}{9}$. The same method works when applying these rules to algebraic expressions.

$$$\left(27x^6\right)^{\frac{2}{3}} = \left(\sqrt[3]{27x^6}\right)^2 = \left(3x^2\right)^2 = 9x^4.$$

Cube root first turns $27x^6$ into $3x^2$, and then squaring gives $9x^4$.

## Finding an unknown index

If an index is unknown, rewrite both sides using the same base. Once the bases match, compare the indices. For the example $9^n = 27$, we begin by writing $9 = 3^2$ and $27 = 3^3$.

$$$\left(3^2\right)^n = 3^3 \Rightarrow 3^{2n} = 3^3 \Rightarrow 2n = 3 \Rightarrow n = \frac{3}{2}.$$ This process effectively converts an unknown index question into a simple linear equation that is easy to solve.

The same idea helps when roots are hidden inside an expression. We can simplify such terms by converting every part of the expression to a power of the same base.

$$$2\sqrt{8} = 2^1 \cdot \left(2^3\right)^{\frac{1}{2}} = 2^1 \cdot 2^{\frac{3}{2}} = 2^{\frac{5}{2}}.$$ So if $2\sqrt{8} = 2^n$, comparing the indices reveals that the missing value is $n = \frac{5}{2}$.

## Check yourself

1. What is the value of $6^{-1}$?

   - $$-6$

   - $$\frac{1}{6}$ ✔

   - $$6$

   - $$\frac{1}{36}$

   _Explanation:_ $$a^{-1}$ means reciprocal, so $6^{-1} = \frac{1}{6}$. The most common wrong answer is $-6$, but the negative sign in the index does not make the value negative. Hint: Think "flip it", not "make it negative".

2. What is $64^{-\frac{2}{3}}$?

   - $$\frac{1}{16}$ ✔

   - $$16$

   - $$-16$

   - $$\frac{1}{8}$

   _Explanation:_ The cube root of $64$ is $4$, then $4^2 = 16$, and the negative index makes it reciprocal, so the answer is $\frac{1}{16}$. The most common wrong answer is $16$, which comes from doing the fractional power correctly but forgetting the reciprocal.
