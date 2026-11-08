# grade-7-7-5-factorising-harder-quadratics — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Why these quadratics are harder

Factorising means rewriting an expression as a product of brackets. When the quadratic starts with $x^2$, the first terms in the brackets are usually just $x$ and $x$. Harder quadratics like $2x^2+7x+3$ need a method because the first terms in the brackets are no longer obvious.

![Flow diagram of factorising $3x^2+14x+8$ by finding $ac=24$, choosing 12 and 2, splitting the middle term, grouping, and getting $(3x+2)(x+4)$](../assets/001-6021a7f2-a76b-4c5d-8538-1c97499270f3.jpeg)

For a quadratic of the form $ax^2+bx+c$, multiply the leading coefficient by the constant term. Then find two numbers that multiply to that result and add to the middle coefficient. Split the middle term using those numbers, factorise in pairs, and look for the repeated bracket.

## Worked example: positive terms

To factorise $3x^2+14x+8$, identify $a=3$, $b=14$, and $c=8$. Then $ac=24$, so the pair we need is $12$ and $2$ because $12 \times 2 = 24$ and $12+2=14$.

Split the middle term first.
$$
3x^2+14x+8=3x^2+12x+2x+8
$$

Then factorise each pair.
$$
3x^2+12x+2x+8=3x(x+4)+2(x+4)
$$

The repeated bracket is $x+4$, so factorise it out.
$$
3x(x+4)+2(x+4)=(3x+2)(x+4)
$$
A quick expansion check gives $3x^2+14x+8$, so the factorisation is correct.

## Signs with a negative constant

Signs matter just as much as the product. In $2x^2+x-15$, $ac=-30$, so the split numbers must have opposite signs and add to $1$.

The correct pair is $6$ and $-5$. Keep each sign attached to its term when you split. $$2x^2+x-15=2x^2+6x-5x-15=2x(x+3)-5(x+3)$$

Now take out the repeated bracket. $$2x(x+3)-5(x+3)=(2x-5)(x+3)$$ Choosing $5$ and $-6$ is the common mistake because they add to $-1$, not $1$.

## From factorising to solving

If the question says solve, you must go beyond brackets and find the roots. For the equation $4x^2+4x-15=0$, we identify that $ac=-60$ and find the useful factor pair $10$ and $-6$.

$$$4x^2+4x-15=4x^2+10x-6x-15=2x(2x+5)-3(2x+5)=(2x-3)(2x+5)$$

Now use the zero product property: if $AB=0$, then $A=0$ or $B=0$. Setting each bracket to zero, $2x-3=0$ or $2x+5=0$, gives the roots $x=\frac{3}{2}$ or $x=-\frac{5}{2}$.

## Common factor first

Sometimes the first job is to take out a common factor. In $6x^2-24$, both terms share $6$, so start with
$$6x^2-24=6(x^2-4)$$

The bracket still factorises because $x^2-4$ is a difference of two squares. That is the pattern $a^2-b^2=(a-b)(a+b)$.
$$x^2-4=x^2-2^2=(x-2)(x+2)$$

So the fully factorised form is
$$6x^2-24=6(x-2)(x+2)$$
Always check whether the bracket can factorise again.

## Two-variable quadratics

The same method works with two variables. In $3x^2-13xy+4y^2$, treat $xy$ like the middle term and use $a=3$, $b=-13$, $c=4$, so $ac=12$.

The split numbers are $-12$ and $-1$. Splitting the middle term and grouping gives: $$3x^2-13xy+4y^2=3x^2-12xy-xy+4y^2=3x(x-4y)-y(x-4y)$$

The repeated bracket is $x-4y$, which leads to the final factorised form: $$3x^2-13xy+4y^2=(3x-y)(x-4y)$$ Notice that the brackets must contain $y$ because the last term is $4y^2$.

## Check yourself

1. For $2x^2+7x+3$, which pair of numbers should you use to split the middle term?

   - $$6$ and $1$ ✔

   - $$3$ and $2$

   - $$7$ and $0$

   - $$-6$ and $-1$

   _Explanation:_ Correct because $a \times c = 2 \times 3 = 6$, and the numbers must multiply to $6$ and add to $7$. Option B is the common mistake because it multiplies to $6$ but adds to $5$, so it does not recreate the middle term.

2. Which pair of numbers should you use to split the middle term in $4x^2-11x-3$?

   - $$-12$ and $1$ ✔

   - $$-3$ and $4$

   - $$-4$ and $3$

   - $$-6$ and $-2$

   _Explanation:_ Here $ac = 4 \times (-3) = -12$, so the numbers must multiply to $-12$ and add to $-11$, which only $-12$ and $1$ do. Option B is the common wrong choice because it has the right product but adds to $1$, so the sign of the middle term is wrong.

3. Which is the fully factorised form of $6x^2-24$?

   - $$6(x-2)(x+2)$ ✔

   - $$6(x^2-4)$

   - $$2(3x^2-12)$

   - $$(3x-6)(2x+4)$

   _Explanation:_ The correct answer first takes out the common factor $6$ and then factorises $x^2-4$ as a difference of two squares. Option B is the common wrong answer because it starts correctly but stops too early, so the expression is not fully factorised.

4. Which is the correct factorisation of $6x^2+11xy-10y^2$?

   - $$(3x-2y)(2x+5y)$ ✔

   - $$(3x+2y)(2x-5y)$

   - $$(6x-5y)(x+2y)$

   - $$(3x-5y)(2x+2y)$

   _Explanation:_ Expanding A gives $6x^2+15xy-4xy-10y^2 = 6x^2+11xy-10y^2$, so it matches exactly. Option B is the common wrong one because it gives $6x^2-11xy-10y^2$, so the middle term has the wrong sign.
