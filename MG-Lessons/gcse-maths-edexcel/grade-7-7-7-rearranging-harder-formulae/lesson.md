# grade-7-7-7-rearranging-harder-formulae — lesson

_Lane: `gcse-maths-edexcel` · grade 7 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## The basic strategy

![Flowchart for rearranging harder formulae showing: choose the subject letter, undo operations from the outside in, and if the letter appears twice then collect terms, factorise and divide](../assets/001-6de3ed67-5e8e-4ad4-869f-f5c4e384d014.jpeg)

Rearranging a formula means making one chosen letter the subject. All the other letters are treated like fixed numbers while you use the balance rule to isolate your variable.

For harder formulae, look at what is happening to the subject and undo those operations from the outside in. If the subject appears more than once, collect those terms together before you try to factorise and divide.

## Worked example with a coefficient

Harder formulae often hide the subject inside a term like $\frac{1}{2}kt^2$. Start by isolating the whole term containing the subject, not just the letter.

$$D = nt + \frac{1}{2}kt^2$$

$$D - nt = \frac{1}{2}kt^2$$

Now remove the coefficient of $k$. Multiply both sides by $2$, then divide by $t^2$.

$$2(D - nt) = kt^2$$

$$k = \frac{2(D - nt)}{t^2}$$

The whole coefficient of $k$ is $\frac{1}{2}t^2$. A common mistake is to forget one part of that coefficient and stop at $2(D - nt) = k$.

## Squares and roots

If the subject is squared, first isolate the squared term. Only then use a square root.

$$q^2 = p^2 + 5rs$$

$$q^2 - 5rs = p^2$$

Square rooting both sides gives the subject. In pure algebra, remember that both positive and negative values can square to the same answer.

$$p = \pm\sqrt{q^2 - 5rs}$$

If the formula describes a length or speed, context may tell you to keep only the positive root. Without that context, missing the $\pm$ loses half the solution.

## When the subject appears twice

When the subject appears on both sides, you cannot isolate it until you collect those terms together. This usually means expand, move the subject terms to one side, and then factorise.

$$$y(4 + c) = d(y + 5)$$

Expand the brackets and collect the $y$ terms. This creates one equation with all the $y$ terms together.

$$4y + cy = dy + 5d$$

$$4y + cy - dy = 5d$$

Factorise out $y$, then divide by the bracket multiplying it. You cannot cancel $y$ at the start because the right-hand side is a sum, not a single factor.

$$y(4 + c - d) = 5d$$

$$y = \frac{5d}{4 + c - d}$$

## Clearing algebraic fractions

To clear an algebraic fraction, multiply both sides by the entire denominator. This turns the problem back into normal collecting and factorising.

$$a = \frac{5 + 3cy}{3y - 2}$$

$$a(3y - 2) = 5 + 3cy$$

Expand and then collect the $y$ terms on one side of the equation. Keep the whole denominator together until you multiply it through to avoid common errors.

$$3ay - 2a = 5 + 3cy$$

$$3ay - 3cy = 5 + 2a$$

Factorise and divide to isolate $y$. Also remember that the original denominator cannot be zero, so $3y - 2 \neq 0$.

$$y(3a - 3c) = 5 + 2a$$

$$y = \frac{5 + 2a}{3a - 3c}$$

## Reciprocal formulae

Reciprocal formulae look messy because every term is a fraction. A reliable method is to multiply every term by the product of all the denominators, assuming those denominators are non-zero.

$$$\frac{1}{p} = \frac{1}{q} + \frac{1}{r}$$

Multiply by $pqr$ to clear all the fractions in one step. This avoids dealing with separate fractions one at a time.

$$$qr = pr + pq$$
$$qr - pq = pr$$

Factorise and divide. Be careful with the order in $r - p$ because swapping it changes the sign of the answer.

$$$q(r - p) = pr$$
$$q = \frac{pr}{r - p}$$

## Check yourself

1. To make $k$ the subject of $w = r + kt$, what should you do first?

   - Divide both sides by $t$

   - Subtract $r$ from both sides ✔

   - Add $r$ to both sides

   - Multiply both sides by $k$

   _Explanation:_ You must first isolate the term containing $k$, so subtract $r$ to get $w - r = kt$. The common wrong answer A divides too early and leaves the added term $r$ mixed in with $k$.

2. Make $p$ the subject of $q^2 = p^2 + 5rs$.

   - $$p = \sqrt{q^2 - 5rs}$

   - $$p = \pm\sqrt{q^2 - 5rs}$ ✔

   - $$p = q^2 - 5rs$

   - $$p = \frac{q^2}{5rs}$

   _Explanation:_ First isolate $p^2$ to get $q^2 - 5rs = p^2$, then square root both sides, which gives two possible values. The common wrong answer A forgets the negative root, which matters unless context says $p$ must be positive.

3. Which is the correct rearrangement of $a = \frac{5 + 3cy}{3y - 2}$ to make $y$ the subject?

   - $$y = \frac{5 + 2a}{3a - 3c}$ ✔

   - $$y = \frac{5 - 2a}{3a - 3c}$

   - $$y = \frac{5 + 2a}{3a + 3c}$

   - $$y = \frac{a(3y - 2) - 5}{3c}$

   _Explanation:_ To make $y$ the subject, first clear the fraction: $a(3y - 2) = 5 + 3cy$. Expand the brackets: $3ay - 2a = 5 + 3cy$. Collect all terms involving $y$ on one side and constant terms on the other: $3ay - 3cy = 5 + 2a$. Factorise $y$ out: $y(3a - 3c) = 5 + 2a$. Finally, divide: $y = \frac{5 + 2a}{3a - 3c}$.
