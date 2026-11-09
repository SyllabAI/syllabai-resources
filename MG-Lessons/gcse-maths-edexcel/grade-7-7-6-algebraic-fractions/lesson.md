# grade-7-7-6-algebraic-fractions — lesson

_Lane: `gcse-maths-edexcel` · grade 7 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## What algebraic fractions are

![Worked example showing an algebraic fraction factorised from (x^2+6x)/(x^2+8x+12) to x(x+6)/((x+2)(x+6)) and then simplified to x/(x+2), with the common factor x+6 highlighted](../assets/001-a7a20d42-5854-4196-9e98-276b9ab1b7a6.jpeg)

An algebraic fraction is a fraction whose numerator, denominator, or both contain algebra. The top is called the numerator and the bottom is called the denominator.

They follow the same rules as ordinary fractions, but you can only cancel common factors. You must not cancel part of a sum such as the $x$ in $x+4$.

That is why factorising comes first. Useful patterns are:

$$3x^2+9x = 3x(x+3)$$

$$x^2+7x+10 = (x+5)(x+2)$$

$$x^2-25 = (x-5)(x+5)$$

## Worked example: simplify fully

Start by factorising the numerator and denominator completely. Here the numerator has a common factor, and the denominator is a difference of two squares.
$$4x^2+16x=4x(x+4)$$
$$x^2-16=(x-4)(x+4)$$

Now rewrite the fraction using those factors. This is the step that reveals what can really cancel.
$$\frac{4x^2+16x}{x^2-16}=\frac{4x(x+4)}{(x-4)(x+4)}$$

Cancel the common factor and write the simpler form. The original denominator still tells you that $x \neq 4$ and $x \neq -4$.
$$\frac{4x(x+4)}{(x-4)(x+4)}=\frac{4x}{x-4}$$

## Writing a requested form

Sometimes a question asks for a specific form such as $\frac{ax+b}{x+c}$. Here $a$, $b$, and $c$ are integers, and you find them after simplifying.

Factorise the numerator and denominator completely before proceeding to the next step:
$$
2x^2+11x+5=(2x+1)(x+5)
$$
$$
x^2+6x+5=(x+1)(x+5)
$$

Then cancel the common factor from the fraction to simplify it:
$$
\frac{2x^2+11x+5}{x^2+6x+5}=\frac{(2x+1)(x+5)}{(x+1)(x+5)}
$$
$$
\frac{2x+1}{x+1}
$$

Now match the result to the requested form $\frac{ax+b}{x+c}$. Comparing the coefficients, we find that $a=2$, $b=1$, and $c=1$.

## Dividing algebraic fractions

To divide algebraic fractions, multiply by the reciprocal of the second fraction. Keep the first fraction, change division to multiplication, and flip the second fraction.

Factorise every part before you flip anything. That makes the factors that will cancel much easier to spot.

$$2x+4=2(x+2)$$

$$x^2+5x+6=(x+2)(x+3)$$

$$x^2-3x=x(x-3)$$

Now rewrite the division as multiplication by the reciprocal. After cancelling the common factors, the result is shown below.

$$\frac{2x+4}{x-3}\div\frac{x^2+5x+6}{x^2-3x}=\frac{2(x+2)}{x-3}\times\frac{x(x-3)}{(x+2)(x+3)}$$

$$\frac{2x}{x+3}$$

## Solving fraction equations

When an equation contains algebraic fractions, start by writing any excluded values. Then multiply every term by a common denominator to clear the fractions.

For $\frac{3}{x+2}+\frac{4}{x+7}=1$, the excluded values are $x \neq -2$ and $x \neq -7$. Multiplying every term by $(x+2)(x+7)$ removes the fractions. $$3(x+7)+4(x+2)=(x+2)(x+7)$$

Expand, collect terms, and factorise the quadratic. The solutions are valid if they are not excluded. $$7x+29=x^2+9x+14$$ $$x^2+2x-15=0$$ $$(x+5)(x-3)=0$$ So $x=-5$ or $x=3$, and both are valid because neither is excluded.

## Turning ratios into fraction equations

A ratio statement $A:B=C:D$ can be rewritten as $\frac{A}{B}=\frac{C}{D}$. That turns a ratio question into a fraction equation you can solve by cross multiplying.

For $(x+4):(x+1)=(x+8):(3x+2)$, first write it as a fraction equation and note the excluded values. Then cross multiply.
$$\frac{x+4}{x+1}=\frac{x+8}{3x+2},\quad x \neq -1,\quad x \neq -\frac{2}{3}$$
$$(x+4)(3x+2)=(x+8)(x+1)$$

After expanding and collecting terms, factorise as usual. Then solve and check the excluded values.
$$3x^2+14x+8=x^2+9x+8$$
$$2x^2+5x=0$$
$$x(2x+5)=0$$
So $x=0$ or $x=-\frac{5}{2}$, and both are allowed.

## Check yourself

1. Which simplification is valid?

   - After factorising, $\frac{x+4}{x^2-16}$ simplifies to $\frac{1}{x-4}$ ✔

   - $$\frac{x+4}{x^2-16}$ simplifies to $\frac{1}{x-16}$

   - $$\frac{x^2+6x}{x^2+8x+12}$ simplifies to $\frac{x+6}{x+12}$

   - $$\frac{3x^2+9x}{x^2+5x+6}$ simplifies to $\frac{3x}{x+6}$

   _Explanation:_ A is correct because $x^2-16=(x-4)(x+4)$, so the whole factor $x+4$ cancels and leaves $\frac{1}{x-4}$. The common wrong answer B comes from cancelling terms inside a subtraction, but you may only cancel complete factors.

2. After simplifying $\frac{2x^2+11x+5}{x^2+6x+5}$ into the form $\frac{ax+b}{x+c}$, which values are correct?

   - $$a=2$, $b=11$, $c=6$

   - $$a=2$, $b=1$, $c=1$ ✔

   - $$a=1$, $b=2$, $c=1$

   - $$a=5$, $b=1$, $c=5$

   _Explanation:_ B is correct because the fraction simplifies to $\frac{2x+1}{x+1}$, so the values come from the simplified numerator and denominator. The common wrong answer A reads off coefficients from the original quadratics, but the question asks for the final form after cancelling. Hint: Compare with $\frac{ax+b}{x+c}$ only after simplifying.

3. Simplify fully $\frac{x+4}{x-1}\div\frac{x^2+3x+2}{x^2-1}$.

   - $$\frac{x+2}{x+4}$

   - $$\frac{x+4}{x+2}$ ✔

   - $$\frac{(x+4)(x-1)}{x+2}$

   - $$\frac{x+4}{x-1}$

   _Explanation:_ B is correct because $x^2+3x+2=(x+1)(x+2)$ and $x^2-1=(x-1)(x+1)$, so you multiply by the reciprocal of the second fraction and then cancel the common factors. The common wrong answer A comes from flipping the wrong fraction or flipping the final answer instead of only the second fraction.

4. In the ratio equation $(x+4):(x+1)=(x+8):(3x+2)$, what are the possible values of $x$?

   - $$-1$ and $-\frac{2}{3}$

   - $$0$ only

   - $$0$ and $-\frac{5}{2}$ ✔

   - $$-\frac{5}{2}$ only

   _Explanation:_ C is correct because rewriting as fractions and cross multiplying gives $x(2x+5)=0$, so $x=0$ or $x=-\frac{5}{2}$. The common wrong answer A lists the excluded values, but those are rejected because they make a denominator zero.
