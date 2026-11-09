# grade-7-7-1-surds — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What counts as a surd?

A surd is an exact root that is irrational, such as $\sqrt{2}$ or $\sqrt{7}$. If the root evaluates to a whole number, then it is not a surd.

Check the square numbers first: 1, 4, 9, 16, 25, 36, 49, and so on. For example, $\sqrt{36}=6$ so it is not a surd, but $\sqrt{18}$ and $\sqrt{10}$ are surds because 18 and 10 are not perfect squares.

## Simplifying surds

To simplify a surd, look for the largest perfect-square factor inside the root. Then use $\sqrt{ab}=\sqrt{a}\sqrt{b}$ to pull the square factor out.

For $\sqrt{72}$, the best square factor is 36, so $$ \sqrt{72}=\sqrt{36\times 2}=6\sqrt{2} $$ Choosing the largest square factor keeps the answer fully simplified.

If there is already a coefficient, simplify the root first. For example, $$ 4\sqrt{45}=4\sqrt{9\times 5}=4(3\sqrt{5})=12\sqrt{5} $$ Do not split sums inside roots, so $\sqrt{9+16}\neq \sqrt{9}+\sqrt{16}$.

## Like surds and collecting terms

Like surds have the same root part, such as $3\sqrt{7}$ and $5\sqrt{7}$. You can only collect them after each surd has been simplified.

In $3\sqrt{48}+2\sqrt{75}$, simplify each root first:
$$
\sqrt{48}=4\sqrt{3},\qquad \sqrt{75}=5\sqrt{3}
$$
Now the surds are like surds because both contain $\sqrt{3}$.

Substitute back and collect the coefficients:
$$
3\sqrt{48}+2\sqrt{75}=3(4\sqrt{3})+2(5\sqrt{3})=12\sqrt{3}+10\sqrt{3}=22\sqrt{3}
$$
You would not combine $2\sqrt{3}$ and $7\sqrt{5}$ because the root parts are different.

## Expanding surd brackets

Expand brackets with surds just as you would in algebra: multiply every term in the first bracket by every term in the second. Remember that $\sqrt{a}\sqrt{a}=a$, so $(\sqrt{7})^2=7$.

For example,
$$
(2+\sqrt{7})(3-\sqrt{7})=6-2\sqrt{7}+3\sqrt{7}-7=-1+\sqrt{7}
$$
After expanding, collect the ordinary numbers and the like surds.

A pair like $a+\sqrt{b}$ and $a-\sqrt{b}$ are conjugates. Their product has no surd part, so
$$
(5+\sqrt{6})(5-\sqrt{6})=25-6=19
$$

## Rationalising the denominator

![Flowchart showing that a single surd denominator is rationalised by multiplying by the same surd, while a two-term denominator is rationalised by multiplying by the conjugate](../assets/001-2ab25cb7-b2c2-4f27-bbb1-853420a77497.jpeg)

To rationalise a denominator means to rewrite a fraction so there is no surd on the bottom. If the denominator has one term like $\sqrt{3}$, multiply by the same surd; if it has two terms like $3+\sqrt{2}$, multiply by its conjugate.

For a single surd denominator,
$$
\frac{12}{\sqrt{3}}\times\frac{\sqrt{3}}{\sqrt{3}}=\frac{12\sqrt{3}}{3}=4\sqrt{3}
$$
You must multiply the numerator and denominator by the same expression, otherwise you change the value.

For a two-term denominator, use the conjugate:
$$
\frac{10+\sqrt{2}}{3+\sqrt{2}}\times\frac{3-\sqrt{2}}{3-\sqrt{2}}=\frac{(10+\sqrt{2})(3-\sqrt{2})}{(3+\sqrt{2})(3-\sqrt{2})}=\frac{28-7\sqrt{2}}{7}=4-\sqrt{2}
$$
The denominator becomes a difference of two squares, so the surd disappears.

## Algebraic surds

The same rules work when letters are under square roots, as long as the quantities inside the roots are non-negative. In IGCSE questions, that is usually assumed unless the question says otherwise.

Conjugates still give a difference of two squares: $$(\sqrt{x}+\sqrt{y})(\sqrt{x}-\sqrt{y})=x-y$$ because $\sqrt{x}\sqrt{x}=x$ and $\sqrt{y}\sqrt{y}=y$.

Squaring a bracket still needs the middle term. For example, $$(3p+\sqrt{q})^2=(3p+\sqrt{q})(3p+\sqrt{q})=9p^2+6p\sqrt{q}+q$$

## Check yourself

1. Which expression is a surd?

   - $$\sqrt{36}$

   - $$\sqrt{18}$ ✔

   - $$\sqrt{81}$

   - $$\sqrt{49}$

   _Explanation:_ $$\sqrt{18}$ is irrational and cannot be simplified to an integer, so it is a surd. A common wrong choice is $\sqrt{36}$, but that equals 6 exactly, so it is not a surd.

2. Simplify $2\sqrt{12}+\sqrt{27}$.

   - $$5\sqrt{3}$

   - $$7\sqrt{3}$ ✔

   - $$2\sqrt{39}$

   - $$7\sqrt{12}$

   _Explanation:_ $$2\sqrt{12}=2(2\sqrt{3})=4\sqrt{3}$ and $\sqrt{27}=3\sqrt{3}$, so the total is $7\sqrt{3}$. A common wrong answer is $5\sqrt{3}$, which happens if you simplify $\sqrt{12}$ correctly but forget to multiply by the outside 2.

3. Simplify fully $\frac{6+\sqrt{5}}{2+\sqrt{5}}$.

   - $$7-4\sqrt{5}$

   - $$4\sqrt{5}-7$ ✔

   - $$8+\sqrt{5}$

   - $$4-\sqrt{5}$

   _Explanation:_ Multiply by the conjugate $2-\sqrt{5}$. The numerator becomes $7-4\sqrt{5}$ and the denominator becomes $4-5=-1$, so the whole fraction is $4\sqrt{5}-7$. A common wrong answer is $7-4\sqrt{5}$, which forgets to divide by the denominator $-1$.
