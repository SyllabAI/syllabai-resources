# grade-5-5-6-solving-quadratics — lesson

_Lane: `igcse-maths-edexcel` · grade 5 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What is a quadratic?

![Graph of the parabola y = x^2 - x - 6 crossing the x-axis at -2 and 3, with roots and vertex labelled](../assets/001-100fbd8b-adab-4e98-b529-95b5a2b06981.jpeg)
A quadratic equation has highest power 2 and is usually written as $ax^2+bx+c=0$, where $a \neq 0$. In this lesson, we focus on forms like $x^2+bx+c=0$, where the coefficient of $x^2$ is 1 and factorising is usually the best method.

The graph of a quadratic is a parabola. Where it crosses the x-axis gives the solutions, also called roots.

If the expression can be written as two brackets, solving becomes much quicker. We will find the bracket numbers, then use the zero product rule to get the two answers.

## How factorising works

Factorising goes backwards from expanding double brackets. To factorise $x^2+bx+c$, find two numbers that multiply to $c$ and add to $b$. For example, $x^2+9x+20=(x+4)(x+5)$.

If $c$ is positive, the two bracket numbers have the same sign. If $b$ is positive they are both positive, and if $b$ is negative they are both negative.

If $c$ is negative, the signs are opposite. After factorising, use the zero product rule: if $(x+a)(x+b)=0$, then $x+a=0$ or $x+b=0$.

## Worked example with matching signs

Solve $u^2+8u+15=0$. We need two numbers that multiply to $15$ and add to $8$, so the pair is $3$ and $5$.

$$$
 u^2+8u+15=(u+3)(u+5)
 $$
So the equation becomes $(u+3)(u+5)=0$. Then set each bracket equal to zero.

$$$
 u+3=0 \quad \text{or} \quad u+5=0
 $$
So $u=-3$ or $u=-5$. If the question says solve, these values are the final answers.

## Worked example with opposite signs

Solve $x^2+2x-48=0$. Because the constant is negative, the two numbers must have opposite signs.

Factor pairs of $48$ are $1$ and $48$, $2$ and $24$, $3$ and $16$, $4$ and $12$, and $6$ and $8$. The pair that gives a total of $2$ is $8$ and $-6$.

$$$x^2+2x-48=(x+8)(x-6)$$

So the equation becomes $(x+8)(x-6)=0$. Now use the zero product rule to get $x=-8$ or $x=6$. Check the signs: $8 \times (-6)=-48$ and $8+(-6)=2$.

## Check your factorisation

A quick way to check a factorisation is to expand the brackets again. The middle term comes from adding the two bracket numbers, and the constant comes from multiplying them.

$$$(x-8)(x+3)=x^2+3x-8x-24=x^2-5x-24$$

So $x^2-5x-24=(x-8)(x+3)$ is correct. If your expansion does not match the original quadratic, the factorisation is wrong.

A common mistake is choosing the right pair but the wrong signs, such as $(x+8)(x-3)$. That gives $x^2+5x-24$, so the product is right but the middle term is not.

## Fast exam strategy

In an exam, first look at the sign of the constant term. This tells you whether the bracket numbers should have the same sign or opposite signs.

Then test factor pairs until their sum matches the middle coefficient, including its sign. For $x^2-10x+16$, the target sum is $-10$, not $10$.

After solving, substitute mentally if you can. Do not divide by a bracket like $(x-2)$ or $(x+5)$ to try to simplify $(x-2)(x+5)=0$, because a factor could be zero. Instead, set each bracket equal to zero separately.

## Check yourself

1. Which of these is a quadratic equation?

   - $$3x+7=0$

   - $$x^2-4x+1=0$ ✔

   - $$x^3+x=0$

   - $$\frac{1}{x}+2=0$

   _Explanation:_ A quadratic equation has highest power 2, so $x^2-4x+1=0$ is the only quadratic here. The common wrong choice $x^3+x=0$ is cubic because its highest power is 3.

2. Solve $p^2-7p+12=0$.

   - $$p=-3$ or $p=-4$

   - $$p=3$ or $p=4$ ✔

   - $$p=2$ or $p=6$

   - $$p=-2$ or $p=-6$

   _Explanation:_ Factorise as $(p-3)(p-4)=0$, so $p=3$ or $p=4$. The common wrong answer $p=-3$ or $p=-4$ comes from copying the bracket numbers without solving $p-3=0$ and $p-4=0$.

3. Which factorisation is correct for $x^2-5x-24$?

   - $$(x-8)(x+3)$ ✔

   - $$(x+8)(x-3)$

   - $$(x-8)(x-3)$

   - $$(x+8)(x+3)$

   _Explanation:_ $$(x-8)(x+3)$ multiplies to $-24$ and adds to $-5$, so it is correct. The common wrong choice $(x+8)(x-3)$ still multiplies to $-24$ but its middle term is $+5x$, not $-5x$.
