# as-pure-mathematics-1-algebraic-expressions — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 4 check questions (source: MathsGenie lessons)_

## Expressions, terms and like terms

An algebraic expression is a mathematical phrase made from numbers, letters and operations, but it has no equals sign to solve. In $3x^2 - 5x + 1$, the terms are $3x^2$, $-5x$ and $1$.

A coefficient is the number multiplying a variable, so $3$ is the coefficient of $x^2$ in $3x^2$. Like terms have exactly the same variable part, so $4x^2$ and $-7x^2$ combine but $4x$ and $4x^2$ do not.

To simplify means to rewrite an expression in an equivalent but cleaner form. In this lesson, you will do that with index laws, exponential rewriting, factorising, expanding and rationalising surds.

## Index laws for simplifying powers

An index tells you how many times a base is used as a factor. When bases match, the index laws help you simplify expressions without changing their value.

$$$a^m \times a^n = a^{m+n}, \quad \frac{a^m}{a^n} = a^{m-n}, \quad (a^m)^n = a^{mn}.$$

These laws work because you are counting repeated factors of the same base. Negative and fractional indices are just extensions of the same idea. Use $a^{-n} = \frac{1}{a^n}$ and $a^{\frac{1}{n}} = \sqrt[n]{a}$, so a negative fractional index means reciprocal first, then root or power.

## Worked example with a negative fractional index

To simplify $\left(\frac{125x^6}{8y^3}\right)^{-\frac{2}{3}}$, deal with the negative sign first. A negative index means take the reciprocal, so
$$\left(\frac{125x^6}{8y^3}\right)^{-\frac{2}{3}} = \left(\frac{8y^3}{125x^6}\right)^{\frac{2}{3}}.$$

Now interpret the power $\frac{2}{3}$ as "cube root, then square". This gives
$$\left(\frac{8y^3}{125x^6}\right)^{\frac{2}{3}} = \left(\frac{2y}{5x^2}\right)^2.$$

Finally square the numerator and denominator:
$$\left(\frac{2y}{5x^2}\right)^2 = \frac{4y^2}{25x^4}.$$
So the simplified form is $\frac{4y^2}{25x^4}$.

## Common base or substitution?

![Flowchart showing how to solve exponential equations by rewriting with a common base or by using a substitution](../assets/001-2163ec5f-6a38-4b5e-835b-cfa2a4e7904e.jpeg)

When the unknown is in the index, look for structure before doing any algebra. If both sides can be written with the same base, rewrite them and equate the indices.

If you see $a^x$ and $a^{2x}$ together, let $y = a^x$ to make a quadratic. For example, we can rewrite an exponential term to match a specific base:

$$$27^{2x-1} = (3^3)^{2x-1} = 3^{6x-3}.$$

The key move in these transformations is multiplying the indices using index laws, rather than multiplying the base.

## Worked example using substitution

Solve $4^x - 10(2^x) + 16 = 0$ by letting $y = 2^x$. Then $4^x = (2^2)^x = (2^x)^2 = y^2$, so the equation becomes
$$y^2 - 10y + 16 = 0.$$

Factorise the quadratic:
$$y^2 - 10y + 16 = (y - 2)(y - 8).$$
So $y = 2$ or $y = 8$.

Now substitute back using $y = 2^x$. This gives $2^x = 2$ or $2^x = 8$, so $x = 1$ or $x = 3$.

Always check the meaning of your substitution at the end. Since $2^x > 0$ for all real $x$, any negative value of $y$ would be rejected.

## Factorise completely and expand carefully

To factorise completely, start by taking out the highest common factor. Then look for special patterns such as a difference of two squares.

For $6x - 24x^3$, first take out $6x$: $$6x - 24x^3 = 6x(1 - 4x^2).$$ Now use $1 - 4x^2 = 1^2 - (2x)^2 = (1 - 2x)(1 + 2x)$.

So the full factorisation is $$6x - 24x^3 = 6x(1 - 2x)(1 + 2x).$$ When expanding, work in the opposite direction: simplify any repeated bracket first and then multiply through carefully.

## Surds and rationalising denominators

A surd is an irrational root left in exact form, such as $\sqrt{2}$. To rationalise a denominator, remove the surd from the bottom by multiplying by a suitable expression.

For a denominator like $3 - \sqrt{2}$, use its conjugate $3 + \sqrt{2}$. This process involves multiplying the numerator and denominator by the conjugate as shown below:
$$\frac{4 + \sqrt{2}}{3 - \sqrt{2}} \times \frac{3 + \sqrt{2}}{3 + \sqrt{2}}$$

Now expand the top and bottom: $$(4 + \sqrt{2})(3 + \sqrt{2}) = 14 + 7\sqrt{2}, \quad (3 - \sqrt{2})(3 + \sqrt{2}) = 9 - 2 = 7.$$ By dividing the terms by $7$, the final simplified answer is $2 + \sqrt{2}$.

## Check yourself

1. Which pair are like terms?

   - $$4x^2$ and $-7x^2$ ✔

   - $$3x$ and $3x^2$

   - $$5a$ and $5b$

   - $$2xy$ and $2x$

   _Explanation:_ $$4x^2$ and $-7x^2$ have exactly the same variable part, so only the coefficients differ. A common mistake is choosing $3x$ and $3x^2$, but their powers of $x$ are different, so they are not like terms.

2. What is the best first step when simplifying $\left(\frac{16a^4}{b^2}\right)^{-\frac{1}{2}}$?

   - Rewrite it as $\left(\frac{b^2}{16a^4}\right)^{\frac{1}{2}}$ ✔

   - Rewrite it as $\left(\frac{16a^4}{b^2}\right)^{\frac{1}{2}}$

   - Rewrite it as $\frac{1}{16a^4b^2}$

   - Rewrite it as $\left(\frac{4a^2}{b}\right)^{-1}$

   _Explanation:_ The negative sign means take the reciprocal first, so the correct first move is to invert the fraction and change the power to positive $\frac{1}{2}$. The common wrong answer is B because it keeps the same fraction and simply ignores the negative index.

3. Stretch: Solve $9^x - 10(3^x) + 9 = 0$.

   - $$x = 1$ or $x = 3$

   - $$x = 0$ or $x = 2$ ✔

   - $$x = -1$ or $x = 1$

   - No real solutions

   _Explanation:_ Let $y = 3^x$, so $9^x = (3^x)^2 = y^2$. Then $y^2 - 10y + 9 = (y - 1)(y - 9)$, so $y = 1$ or $y = 9$, giving $x = 0$ or $x = 2$. The common wrong answer is A because it treats the values of $y$ as if they were already values of $x$.

4. Which is the complete factorisation of $6x - 24x^3$?

   - $$6x(1 - 2x)(1 + 2x)$ ✔

   - $$6x(1 - 4x^2)$

   - $$6(x - 4x^3)$

   - $$6x(1 - 4x)^2$

   _Explanation:_ After taking out the highest common factor $6x$, the bracket $1 - 4x^2$ is remaining. This is a difference of two squares, which can be further factorised into $(1 - 2x)(1 + 2x)$. Option B is incorrect because it is not the *complete* factorisation.
