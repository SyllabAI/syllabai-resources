# grade-7-7-5-factorising-harder-quadratics — lesson

_Lane: `gcse-maths-edexcel` · grade 7 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## The key idea

When the coefficient of $x^2$ is 1, you can often factorise by inspection. When it is not 1, as in $2x^2 + 7x + 3$, splitting the middle term is the reliable method.

For an expression of the form $ax^2 + bx + c$, first check for a common factor. If there is none, multiply $a$ and $c$, then find two numbers that multiply to $ac$ and add to $b$.

## Worked example

![Flowchart showing how 2x^2 + 7x + 3 is split, grouped, and factorised into (2x + 1)(x + 3)](../assets/001-37fa6399-b057-46b7-89b6-1e7fb4e2d930.jpeg)
This flowchart shows the split-the-middle method on $2x^2 + 7x + 3$. Notice that the middle term is rewritten, not the whole expression changed.

In this example, $a = 2$, $b = 7$, and $c = 3$, so $ac = 6$. The numbers 6 and 1 multiply to 6 and add to 7, so we split the $7x$ term into $6x + x$.

Split and group the terms to begin factorising:
$$2x^2 + 7x + 3 = 2x^2 + 6x + x + 3 = 2x(x + 3) + 1(x + 3)$$
Now both pairs of terms contain the same common bracket $(x + 3)$.

Finally, take out the common bracket to finish the expression:
$$2x^2 + 7x + 3 = (2x + 1)(x + 3)$$
A quick expansion check gives $2x^2 + 6x + x + 3 = 2x^2 + 7x + 3$.

## Getting the signs right

Negative signs matter just as much as the numbers. If $c$ is negative, the two split numbers must have opposite signs because their product is negative.

Factorise $4x^2 - 11x - 3$ by first calculating $ac = 4 \times (-3) = -12$. The numbers $-12$ and 1 multiply to $-12$ and add to $-11$, so split $-11x$ as $-12x + x$.

Now split and group: $$4x^2 - 11x - 3 = 4x^2 - 12x + x - 3 = 4x(x - 3) + 1(x - 3)$$ So the factorisation is $(4x + 1)(x - 3)$.

## Solving by factorising

If a quadratic equation equals zero, first factorise it and then use the zero product property. A product is zero only when at least one factor is zero.

For $3x^2 + 10x - 8 = 0$, calculate $ac = 3 \times (-8) = -24$. The numbers 12 and $-2$ multiply to $-24$ and add to 10, so split $10x$ as $12x - 2x$.

Split and factorise:
$$3x^2 + 10x - 8 = 3x^2 + 12x - 2x - 8 = 3x(x + 4) - 2(x + 4) = (3x - 2)(x + 4)$$
Then solve $3x - 2 = 0$ or $x + 4 = 0$ to get $x = \frac{2}{3}$ or $x = -4$.

## Common factor first

When a question says "factorise fully", check for a common factor before using any other pattern. This step makes the expression smaller, easier to work with, and helps you avoid missing easy marks.

For the expression $3x^2 - 75$, we should take out the common factor of 3 first:
$$3x^2 - 75 = 3(x^2 - 25)$$
The bracket is now in the form of a difference of two squares.

Apply the identity $A^2 - B^2 = (A - B)(A + B)$ using $A = x$ and $B = 5$. The final factorised expression is:
$$3x^2 - 75 = 3(x - 5)(x + 5)$$

## Two variables and pattern spotting

The same split-the-middle method works with terms like $xy$ and $y^2$. Treat the middle term as the $xy$ term and match like terms carefully. For $2x^2 + 11xy + 5y^2$, use $ac = 2 \times 5 = 10$ to split $11xy$ into $10xy + xy$.

$$$2x^2 + 11xy + 5y^2 = 2x^2 + 10xy + xy + 5y^2 = 2x(x + 5y) + y(x + 5y) = (2x + y)(x + 5y)$$

Also watch for perfect-square quadratics. These follow a recognizable pattern where the first and last terms are squares, and the middle term is twice the product of their square roots.

$$$x^2 - 8xy + 16y^2 = x^2 - 2(x)(4y) + (4y)^2 = (x - 4y)^2$$

## Check yourself

1. For $2x^2 + 7x + 3$, which pair of numbers should you use to split the middle term?

   - 6 and 1 ✔

   - 3 and 2

   - 7 and 3

   - -6 and -1

   _Explanation:_ Multiply $a$ and $c$ to get $2 \times 3 = 6$, then find numbers that add to $7$. So 6 and 1 are correct. The most common wrong answer is 3 and 2 because they multiply to 6 but only add to 5.

2. Which factorisation is correct for $4x^2 - 11x - 3$?

   - $$(4x + 1)(x - 3)$ ✔

   - $$(4x - 1)(x + 3)$

   - $$(2x - 3)(2x + 1)$

   - $$(4x - 3)(x + 1)$

   _Explanation:_ Expanding A gives $4x^2 - 12x + x - 3 = 4x^2 - 11x - 3$. The most common wrong answer is B because it uses the right numbers but the signs give $4x^2 + 11x - 3$ instead.

3. Which is the fully factorised form of $3x^2 - 75$?

   - $$3(x - 5)(x + 5)$ ✔

   - $$(3x - 5)(x + 5)$

   - $$3(x^2 - 25)$

   - $$(x - 5)(x + 5)$

   _Explanation:_ First take out the common factor 3, then use difference of two squares on $x^2 - 25$. The most common wrong answer is C because it is only partly factorised, so it is not fully factorised.

4. Which is the correct factorisation of $2x^2 + 11xy + 5y^2$?

   - $$(2x + y)(x + 5y)$ ✔

   - $$(2x + 5y)(x + y)$

   - $$(x + 5y)^2$

   - $$(2x + y)(x + y)$

   _Explanation:_ Expanding A gives $2x^2 + 10xy + xy + 5y^2 = 2x^2 + 11xy + 5y^2$. The most common wrong answer is B because its middle terms are $2xy$ and $5xy$, which add to only $7xy$. Hint: Expand the middle terms if two answers look similar.
