# grade-7-7-6-algebraic-fractions — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Algebraic fractions and excluded values

An algebraic fraction is a fraction where the numerator, the denominator, or both contain algebraic expressions. It behaves like an ordinary fraction, so the denominator can never be zero.

Any value of $x$ that makes the denominator zero is called an excluded value. To find excluded values, look only at the denominator and factorise it:

$$$x^2-4=(x-2)(x+2)$$

So $\frac{x+3}{x^2-4}$ has excluded values $x=2$ and $x=-2$. Even if a factor cancels later, those values still stay excluded because they made the original denominator zero.

## Factorise before you cancel

Use this order every time:

1. Factorise the numerator and denominator fully.
2. Find any excluded values by setting the original denominator equal to $0$.
3. Rewrite the fraction in factor form.
4. Cancel common factors only.
5. Write the simplified answer.

You can cancel common factors, but you cannot cancel just the $x$ from a sum such as $x+6$.

Here is a worked example with $\frac{x^2+6x}{x^2+8x+12}$. First factorise both parts:
$$x^2+6x=x(x+6)$$
$$x^2+8x+12=(x+2)(x+6)$$

Now find the excluded values from the original denominator:
$$(x+2)(x+6)=0$$
so $x \neq -2$ and $x \neq -6$.

Then rewrite the fraction using factors and cancel the common factor:
$$\frac{x^2+6x}{x^2+8x+12}=\frac{x(x+6)}{(x+2)(x+6)}=\frac{x}{x+2}$$
The factor $(x+6)$ cancels because it multiplies both the numerator and the denominator.

## Patterns that help you factorise

One factor pattern appears again and again in algebraic fractions: the difference of two squares. This pattern is expressed by the formula: $$a^2-b^2=(a-b)(a+b)$$ It often creates a bracket that can be used to cancel terms in a fraction.

For example, we can simplify an expression by factorising the denominator: $$\frac{x+7}{x^2-49}=\frac{x+7}{(x-7)(x+7)}=\frac{1}{x-7}$$ Once we factorise $x^2-49$, the $(x+7)$ term in the numerator and denominator can be removed.

The excluded values still come from the original denominator, even after simplification. In the example above, $x \neq 7$ and $x \neq -7$ are both necessary constraints even though the $(x+7)$ bracket was cancelled.

A classic trap is attempting to simplify $\frac{x+4}{x+7}$ by crossing out the $x$. You cannot cancel the $x$ because it is part of an addition, not a whole factor multiplied across the top and bottom.

## Dividing using a reciprocal

To divide by a fraction, multiply by its reciprocal. After that, treat the question as a simplification problem: factorise and cancel common factors.

Example: $$\frac{x+3}{x-5} \div \frac{x^2+5x+6}{x^2-5x}=\frac{x+3}{x-5}\times\frac{x^2-5x}{x^2+5x+6}$$ Now factorise the expressions that can be factorised: $x^2-5x=x(x-5)$ and $x^2+5x+6=(x+2)(x+3)$.

Substitute the factors and cancel: $$\frac{x+3}{x-5}\times\frac{x(x-5)}{(x+2)(x+3)}=\frac{x}{x+2}$$ Here $x\neq 5$ and $x\neq 0$ from the original denominators. Also $x\neq -2$ and $x\neq -3$ because the fraction you divide by must not be zero.

## Solving equations by clearing denominators

When an equation contains algebraic fractions, write the excluded values first. Then multiply every term by a common denominator to remove all the fractions.

For the equation $$\frac{8}{x+2}+\frac{6}{x+5}=1$$ the excluded values are $x\neq -2$ and $x\neq -5$. Multiplying every term by $(x+2)(x+5)$ clears the denominators: $$8(x+5)+6(x+2)=(x+2)(x+5)$$

Expanding both sides and rearranging gives: $$14x+52=x^2+7x+10$$ $$x^2-7x-42=0$$

The quadratic $x^2-7x-42=0$ does not factorise over the integers, so use the quadratic formula: $$x=\frac{-(-7)\pm\sqrt{(-7)^2-4(1)(-42)}}{2(1)}=\frac{7\pm\sqrt{217}}{2}$$ So $x=\frac{7+\sqrt{217}}{2}$ or $x=\frac{7-\sqrt{217}}{2}$. Since neither solution is an excluded value, both answers are valid.

## Ratios and proportions

A ratio statement such as $A:B=C:D$ can be rewritten as $\frac{A}{B}=\frac{C}{D}$. Once it is written as a fraction equation, you solve it by cross multiplying.

For the following proportion:
$$\frac{x+2}{2x}=\frac{x+3}{3x-1}$$
Cross multiplying the terms gives $$(x+2)(3x-1)=2x(x+3)$$

This turns the ratio into an ordinary quadratic equation when you expand:
$$3x^2+5x-2=2x^2+6x$$
Rearranging the equation gives $$x^2-x-2=0$$

Finally, factorising gives $(x-2)(x+1)=0$. So $x=2$ or $x=-1$, and both are valid because they do not make the original denominators $2x$ or $3x-1$ equal to zero.

## Check yourself

1. What are the excluded values of $\frac{x+5}{x^2-9}$?

   - $$x=3$ and $x=-3$ ✔

   - $$x=9$ only

   - $$x=3$ only

   - No excluded values

   _Explanation:_ The denominator factorises as $x^2-9=(x-3)(x+3)$, so it is zero when $x=3$ or $x=-3$. Option C is the common mistake of solving only one factor and forgetting that both brackets can make the denominator zero.

2. Why can $\frac{x+4}{x+7}$ not be simplified by cancelling $x$?

   - Because $x$ is not a factor of the whole numerator and denominator ✔

   - Because only numbers can cancel

   - Because the denominator would become zero

   - Because $x$ must stay in the numerator

   _Explanation:_ You can only cancel factors, and in $\frac{x+4}{x+7}$ the $x$ is part of a sum, not a separate factor. Option B is the common wrong idea because algebraic factors can cancel too, but only when the whole expression is a factor, such as $(x+3)$. Hint: Ask yourself whether $x$ is multiplying or adding.

3. Stretch: After multiplying every term in $\frac{3}{x}+\frac{2}{x+1}=1$ by $x(x+1)$, which equation is correct?

   - $$3(x+1)+2x=x(x+1)$ ✔

   - $$3+2=1$

   - $$3x+2(x+1)=x+1$

   - $$3(x+1)+2x=1$

   _Explanation:_ Multiplying by $x(x+1)$ clears both denominators on the left and turns the $1$ on the right into $x(x+1)$. Option D is the very common mistake of forgetting to multiply the $1$ by the common denominator as well.
