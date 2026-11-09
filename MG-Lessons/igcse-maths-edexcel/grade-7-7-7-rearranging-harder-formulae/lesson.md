# grade-7-7-7-rearranging-harder-formulae — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## The core idea

![Flowchart showing m = n + kp with forward operations multiply by p and add n, and reverse operations subtract n and divide by p to isolate k](../assets/001-91a3ce33-8c81-424c-bb27-e843dfc78d60.jpeg)

Rearranging a harder formula means isolating one variable so the final line has $x$ on its own on one side. The safest idea is balance: whatever you do to one side, you must do to the other side.

Work backwards through the operations using inverse operations. Undo addition before multiplication, and clear fractions before you try to collect terms.

A good exam check is simple: the target letter should appear once, on its own, and nowhere else. If it still appears on both sides, you have more rearranging to do.

## Worked example with inverse operations

Start with the operation furthest from the target letter. In $m=n+kp$, the $n$ is added after $kp$ is formed, so subtract $n$ first.

Subtracting $n$ from both sides results in:
$$m-n=kp$$
We then divide both sides by $p$ to isolate the target variable.

$$$k=\frac{m-n}{p}$$
Thinking in inverse operations is safer than talking about moving terms across, as it helps prevent sign errors.

## Squares and half-terms

If the target letter is squared, isolate the squared part before taking the square root. In pure algebra you usually need $\pm$, although for a length or time the negative root may be rejected.

From $R^2=P^2+5qt$, subtract $5qt$ first:
$$R^2-5qt=P^2$$
Then square root both sides:
$$P=\pm\sqrt{R^2-5qt}$$

If a term has a coefficient like $\frac{1}{2}$, clear that fraction before dividing by other factors. Do not divide by $t^2$ first, because the $\frac{1}{2}$ applies to the whole product.

From $d=wt+\frac{1}{2}nt^2$, first isolate the half-term:
$$d-wt=\frac{1}{2}nt^2$$
Multiply by 2 and then divide by $t^2$:
$$2(d-wt)=nt^2$$
$$n=\frac{2(d-wt)}{t^2}$$

## Collect, factorise, divide

If the target letter appears in two places, collect those terms together before you try to divide. Dividing too early often traps the target letter in another term.

For $x(4+a)=b(x+1)$, expand both sides first:
$$4x+ax=bx+b$$
Now subtract $bx$ from both sides to group the terms containing $x$ on one side:
$$4x+ax-bx=b$$

Factorise $x$ from the left-hand side:
$$x(4+a-b)=b$$
Now divide by the bracket to isolate the subject:
$$x=\frac{b}{4+a-b}$$

## Clearing algebraic fractions

When the target letter is in a numerator and a denominator, clear the fraction first. If one fraction equals another, the same idea becomes multiplying by both denominators, which is often called cross-multiplying.

From $p=\frac{6+2qx}{2x-5}$, multiply both sides by $2x-5$: $$p(2x-5)=6+2qx$$ Then expand the bracket: $$2px-5p=6+2qx$$

Collect the $x$ terms on one side and the other terms on the other side: $$2px-2qx=6+5p$$ Factorise $2x$: $$2x(p-q)=6+5p$$

Now divide by $2(p-q)$: $$x=\frac{6+5p}{2(p-q)}$$ You also need hidden restrictions such as $2x-5\neq0$ and $p-q\neq0$ so you never divide by zero.

## Reciprocal formulae

Reciprocal formulae look awkward, but the method is very regular. Isolate the reciprocal containing the target, combine the other fractions, then take the reciprocal at the end.

For $\frac{1}{x}=\frac{1}{y}+\frac{1}{z}$, subtract $\frac{1}{z}$ from both sides:
$$\frac{1}{y}=\frac{1}{x}-\frac{1}{z}$$

Now combine the fractions:
$$\frac{1}{y}=\frac{z}{xz}-\frac{x}{xz}=\frac{z-x}{xz}$$

Take the reciprocal of both sides:
$$y=\frac{xz}{z-x}$$
This only makes sense when the denominators are non-zero, so $x\neq0$, $z\neq0$, and $z-x\neq0$.

## Check yourself

1. When you have successfully made $x$ the subject of a formula, what must be true?

   - $$x$ is alone on one side and does not appear on the other ✔

   - $$2x$ is alone on one side

   - $$x$ appears on both sides

   - the formula has no fractions

   _Explanation:_ A is correct because the subject of a formula is the variable isolated by itself. B is the most common wrong idea because $x$ is still being multiplied by 2, so it is not fully isolated. Hint: The subject is the variable written by itself.

2. Make $P$ the subject of $R^2=P^2+5qt$. Which answer is correct?

   - $$P=\sqrt{R^2-5qt}$

   - $$P=\pm\sqrt{R^2-5qt}$ ✔

   - $$P=R^2-5qt$

   - $$P=\pm(R^2-5qt)$

   _Explanation:_ B is correct because after subtracting $5qt$ you have $P^2=R^2-5qt$, and square-rooting gives two roots unless context says only positive values are allowed. A is the most common wrong answer because it forgets the negative root.

3. What is the best first step when rearranging $p=\frac{6+2qx}{2x-5}$ to make $x$ the subject?

   - Divide both sides by $2q$

   - Multiply both sides by $2x-5$ ✔

   - Subtract 6 from both sides

   - Take the reciprocal of both sides

   _Explanation:_ B is correct because clearing the denominator removes the fraction containing $x$. A is the most common wrong answer because dividing by $2q$ leaves the denominator $2x-5$ untouched.
