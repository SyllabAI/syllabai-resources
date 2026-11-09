# grade-6-6-4-expanding-triple-brackets — lesson

_Lane: `igcse-maths-edexcel` · grade 6 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## The main method

![Flowchart showing the three brackets (x+3), (x+4), and (x+2) becoming a quadratic and then a cubic during expansion](../assets/001-cc174316-631b-4dc8-a899-41de609b4053.jpeg)

A triple bracket such as $(x+2)(x+5)(x-1)$ means three linear factors are being multiplied together. The safest method is to expand any two brackets first, simplify to a quadratic, then multiply by the remaining bracket.

If each bracket contains an $x$ term, the final answer is usually a cubic expression. You can start with any pair of brackets, but write the finished result in descending powers: $x^3$, then $x^2$, then $x$, then the constant.

## Worked example with positive terms

Expand and simplify $(x+3)(x+4)(x+2)$. Start by expanding the first two brackets to create a quadratic expression:

$$(x+3)(x+4)=x^2+4x+3x+12=x^2+7x+12$$

This leaves the quadratic result ready to be multiplied by the final bracket.

Now multiply the quadratic by the remaining bracket $(x+2)$. It is often easiest to split this into two separate distributions, first by $x$ and then by $2$:

$$x(x^2+7x+12)=x^3+7x^2+12x$$
$$2(x^2+7x+12)=2x^2+14x+24$$

Finally, add the results of the two distributions and collect like terms carefully. This process yields the final simplified cubic expression:

$$x^3+7x^2+12x+2x^2+14x+24=x^3+9x^2+26x+24$$

## Negative signs need care

Negative signs are where most slips happen. For $(x-4)(x+6)(x-1)$, expand the first two brackets first:
$$
(x-4)(x+6)=x^2+6x-4x-24=x^2+2x-24
$$
Now the last bracket is still waiting.

Next multiply the quadratic by $(x-1)$. The second row must be multiplication by $-1$, so every sign changes:
$$
x(x^2+2x-24)=x^3+2x^2-24x
$$
$$
-1(x^2+2x-24)=-x^2-2x+24
$$

Add the rows and collect like terms. This gives $(x-4)(x+6)(x-1)=x^3+x^2-26x+24$:
$$
x^3+2x^2-24x-x^2-2x+24=x^3+x^2-26x+24
$$

## Repeated brackets

$$(x-2)^2$ means $(x-2)(x-2)$, not $x^2+4$. For an expression like $(x+5)(x-2)^2$, we start by expanding the repeated pair first:
$$
(x-2)(x-2)=x^2-2x-2x+4=x^2-4x+4
$$

Now multiply the resulting quadratic by the remaining $(x+5)$. We can split this into multiplication by $x$ and multiplication by $5$:
$$
x(x^2-4x+4)=x^3-4x^2+4x
$$
$$
5(x^2-4x+4)=5x^2-20x+20
$$

Finally, add the rows and simplify by collecting like terms. The fully expanded form of $(x+5)(x-2)^2$ is $x^3+x^2-16x+20$:
$$
x^3-4x^2+4x+5x^2-20x+20=x^3+x^2-16x+20
$$

## Brackets with coefficients

The method stays the same when brackets contain terms like $2x$ or $3x$. A quick check for the leading term is to multiply only the x-terms: $2x \cdot x \cdot 3x = 6x^3$.

For $(2x+3)(x-1)(3x+2)$, expand the first two brackets first: $$(2x+3)(x-1)=2x^2-2x+3x-3=2x^2+x-3$$ This quadratic is the new expression you multiply by $(3x+2)$.

Now multiply by $(3x+2)$ using two rows. Then collect like terms to finish: $$3x(2x^2+x-3)=6x^3+3x^2-9x$$ $$2(2x^2+x-3)=4x^2+2x-6$$ $$6x^3+3x^2-9x+4x^2+2x-6=6x^3+7x^2-7x-6$$

## Show that questions

A show that question asks you to prove an identity. You must expand and simplify algebraically, because checking one value of $x$ does not prove something is true for all values.

For $(2x+1)(4x-3)(x-2)$, begin by expanding the first two brackets:
$$
(2x+1)(4x-3)=8x^2-6x+4x-3=8x^2-2x-3
$$
This gives the quadratic you need for the final multiplication.

Now multiply by $(x-2)$ and collect like terms. The left-hand side becomes the required cubic, so the identity is proved:
$$
x(8x^2-2x-3)=8x^3-2x^2-3x
$$
$$
-2(8x^2-2x-3)=-16x^2+4x+6
$$
$$
8x^3-2x^2-3x-16x^2+4x+6=8x^3-18x^2+x+6
$$

## Check yourself

1. When you expand $(x+2)(x-5)(x+1)$, what should the highest power in the final answer be?

   - $$x^3$ ✔

   - $$x^2$

   - $$x^4$

   - $$x$

   _Explanation:_ The x terms from all three brackets multiply to give $x \cdot x \cdot x = x^3$, so the final expression is cubic. The most common wrong answer is $x^2$, which happens if you stop after expanding only the first two brackets.

2. In the expansion of $(x^2+2x-24)(x-1)$, what is the correct second row?

   - $$-x^2-2x+24$ ✔

   - $$x^2+2x-24$

   - $$-x^2+2x+24$

   - $$x^2-2x+24$

   _Explanation:_ The second row comes from multiplying the whole quadratic by $-1$, so every term changes sign to give $-x^2-2x+24$. The most common wrong answer is $x^2+2x-24$, which forgets that the multiplier is negative.

3. What is the leading term of $(2x-1)(x+4)(3x+5)$?

   - $$6x^3$ ✔

   - $$6x^2$

   - $$5x^3$

   - $$3x^3$

   _Explanation:_ The leading term comes from multiplying the highest-power terms: $(2x)(x)(3x)=6x^3$. The most common wrong answer is $3x^3$, which misses the coefficient 2 from the first bracket.

4. Which method proves that $(2x+1)(4x-3)(x-2)=8x^3-18x^2+x+6$ for all values of $x$?

   - Expand and simplify the left-hand side until it matches the right-hand side ✔

   - Substitute $x=1$ and check both sides

   - Substitute $x=0$ and $x=2$ and check both sides

   - Compare only the $x^3$ terms on each side

   _Explanation:_ To prove an identity, you must show the two expressions are algebraically identical for every value of $x$, which is why full expansion works. The most common wrong answer is B, but checking one value only shows the statement is true in that single case.
