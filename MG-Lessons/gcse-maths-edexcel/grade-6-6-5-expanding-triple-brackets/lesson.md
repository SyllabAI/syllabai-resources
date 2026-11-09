# grade-6-6-5-expanding-triple-brackets — lesson

_Lane: `gcse-maths-edexcel` · grade 6 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## The big idea

![Flow diagram showing three brackets turning into a quadratic after expanding two brackets, then into a cubic after multiplying by the remaining bracket](../assets/001-8b4dbfc5-eb1f-4ef9-97bd-b0810fca4729.jpeg)

A triple bracket expression has three factors, such as $(x+1)(x+2)(x+3)$. The safest method is to turn it into a double-bracket question first.

Do not try to multiply all three brackets at once. Expand two brackets, simplify to a quadratic, then multiply that quadratic by the remaining bracket.

When three linear brackets are expanded, the final answer usually starts with an $x^3$ term. A quick check at the end is to write your answer in descending powers: $x^3$, then $x^2$, then $x$, then the constant.

## Quick recap of double brackets

Before triple brackets, you need to be confident with double brackets. Each term in one bracket multiplies each term in the other bracket.

For example,
$$
(x+6)(x-2)=x^2-2x+6x-12
$$
This is exactly the same multiplication idea you will use twice in a triple-bracket question.

Now collect the like terms.
$$
x^2-2x+6x-12=x^2+4x-12
$$
Be careful with signs because positive times negative gives a negative term.

## Fully worked example with three simple brackets

Let us expand $(x+3)(x+5)(x+2)$ step by step. First expand the first two brackets because they are simple.

$$(x+3)(x+5)=x^2+5x+3x+15$$

Now simplify that result before doing anything else. This turns the first part into a quadratic.

$$x^2+5x+3x+15=x^2+8x+15$$

So the question becomes $(x^2+8x+15)(x+2)$. You now multiply each term in the quadratic by both terms in $(x+2)$.

$$x^2(x+2)=x^3+2x^2,\quad 8x(x+2)=8x^2+16x,\quad 15(x+2)=15x+30$$

Put the pieces together and collect like terms. This is the point where students often miss a term, so keep every product visible.

$$x^3+2x^2+8x^2+16x+15x+30=x^3+10x^2+31x+30$$

The final answer is $x^3+10x^2+31x+30$. The leading term is $x^3$, which matches the expected highest power.

## Coefficients and negatives

Coefficients and negatives do not change the method, but they do make sign errors more likely. Choose the pair that looks simplest to expand first. For $(2x+3)(x-1)(x+4)$, starting with the simpler pair results in:
$$ (x-1)(x+4)=x^2+3x-4 $$

Next, use the chunking method by multiplying the remaining linear bracket $(2x+3)$ by the new quadratic. Calculate the products for both $2x$ and $3$ independently:
$$ 2x(x^2+3x-4)=2x^3+6x^2-8x $$
$$ 3(x^2+3x-4)=3x^2+9x-12 $$

Add the two lines and simplify carefully. Notice that $-8x+9x=x$, so the linear term is positive. The final expansion is:
$$ 2x^3+6x^2-8x+3x^2+9x-12=2x^3+9x^2+x-12 $$

## Squared brackets inside triple brackets

A squared bracket is just a repeated bracket. For example, $(x+4)(x-2)^2$ means $(x+4)(x-2)(x-2)$. When you see this notation, you should expand the repeated brackets first.

Expand the squared part: $$(x-2)(x-2)=x^2-2x-2x+4=x^2-4x+4$$ Avoid the common mistake of turning $(x-2)^2$ into just $x^2+4$; the middle term matters for the final result.

Now multiply by the remaining bracket: $$(x+4)(x^2-4x+4)=x^3-4x^2+4x+4x^2-16x+16$$ Every term in the linear bracket $(x+4)$ must multiply every term in the quadratic expression.

Collect like terms to finish: $$x^3-4x^2+4x+4x^2-16x+16=x^3-12x+16$$ In this case, the $x^2$ terms cancel completely, which shows that a missing power of $x$ in the final answer can still be correct.

## Show that questions and checking

In a "show that" question, expand one side carefully and compare your final line with the target expression. If it does not match, that means something in the algebra needs checking. A tidy start for $(2x-1)(x+3)(4x-5)$ is to expand the middle pair first.

$$$(x+3)(4x-5)=4x^2+7x-15$$ This leaves a linear bracket multiplying a quadratic. Now we can proceed to expand the remaining part of the expression in two manageable chunks.

$$$2x(4x^2+7x-15)=8x^3+14x^2-30x$$ $$-1(4x^2+7x-15)=-4x^2-7x+15$$ The coefficient of $x$ comes from combining $-30x$ and $-7x$ during the collection phase.

$$$8x^3+14x^2-30x-4x^2-7x+15=8x^3+10x^2-37x+15$$ Collect like terms carefully. Any claim with $-43x$ is wrong, even though the leading term and constant are correct.

## Check yourself

1. What is the safest first step when expanding $(x+1)(x+2)(x+3)$?

   - Expand two of the brackets first and simplify ✔

   - Multiply only the first terms to get $x^3$

   - Square each bracket separately

   - Add all the numbers inside the brackets

   _Explanation:_ A is correct because triple brackets are best handled in stages: first make a quadratic, then multiply by the last bracket. The common wrong answer is B, but multiplying only the first terms gives just the leading term and misses all the other terms in the expansion.

2. Which is the correct expansion of $(2x+3)(x-1)(x+4)$?

   - $$2x^3+9x^2+x-12$ ✔

   - $$2x^3+9x^2-x-12$

   - $$2x^3+7x^2+x-12$

   - $$2x^2+9x^2+x-12$

   _Explanation:_ A is correct because $(x-1)(x+4)=x^2+3x-4$, and multiplying by $(2x+3)$ gives $2x^3+6x^2-8x+3x^2+9x-12=2x^3+9x^2+x-12$. The common wrong answer is B, which comes from treating $-8x+9x$ as $-x$ instead of the correct result $x$. Hint: Expand the simpler pair first.

3. A student says $(2x-1)(x+3)(4x-5)=8x^3+10x^2-43x+15$. Which statement is correct?

   - The claim is true because the leading term is $8x^3$

   - The coefficient of $x$ should be $-37$, so the claim is false ✔

   - The constant term should be $-15$, so the claim is false

   - The highest power should be $x^2$, so the claim is false

   _Explanation:_ B is correct because $(x+3)(4x-5)=4x^2+7x-15$, and then $(2x-1)(4x^2+7x-15)$ gives $-30x-7x=-37x$. The common wrong answer is C, but the constant is actually $(-1)(-15)=+15$, so the constant term is not the problem.
