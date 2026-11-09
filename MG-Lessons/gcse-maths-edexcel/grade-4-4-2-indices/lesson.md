# grade-4-4-2-indices — lesson

_Lane: `gcse-maths-edexcel` · grade 4 · 6 content steps · 2 check questions (source: MathsGenie lessons)_

## What an index means

![Annotated summary showing 5 cubed with base and index labelled and boxes for the multiply, divide and power of a power index laws](../assets/001-7e998024-1b1f-42ed-90c7-696764d4a65b.jpeg)

An index tells you how many times a base is multiplied by itself. In $5^3$, the 5 is the base and the 3 is the index.

$$5^3 = 5 \times 5 \times 5 = 125$, so a power is a quick way to write repeated multiplication. The summary diagram also previews the three laws you will use most often.

## The core laws for same bases

Most index questions start by checking whether the bases are the same. If the base matches, the base itself stays the same and only the indices change.

For multiplication, add the indices, and for division, subtract them.

$$a^m \times a^n = a^{m+n} \qquad \frac{a^m}{a^n} = a^{m-n}$$

These rules work because repeated factors either combine or cancel. A single letter has an invisible power of 1, meaning $d^{10} \div d^6 = d^4$ and $m^3 \times m = m^4$.

## Worked example with coefficients and letters

When numbers and letters are mixed, deal with the coefficient first and then each variable separately. Simplify $4m^3n^2 \times 6mn^5$.

Multiply the coefficients to get $4 \times 6 = 24$. For the $m$ terms, remember $m = m^1$, so $m^3 \times m = m^{3+1} = m^4$.

Now add the indices on the $n$ terms: $n^2 \times n^5 = n^7$. So the final answer is $24m^4n^7$.

## Powers outside brackets

When a power is outside brackets, it applies to every factor inside. For a single base, $(a^m)^n = a^{mn}$, so you multiply the indices.

Now simplify $(3a^2b)^3$. First cube the coefficient to get $3^3 = 27$, then multiply the index on $a$ so $(a^2)^3 = a^6$.

Finally, $b$ has an invisible index of 1, so $(b^1)^3 = b^3$. Therefore $(3a^2b)^3 = 27a^6b^3$, and the coefficient must be powered as well.

## Zero powers and negative powers

Any non-zero base to the power of 0 equals 1. So $7^0 = 1$ and $x^0 = 1$ as long as the base is not 0.

A negative index means take the reciprocal. The rule is: 

$$a^{-n} = \frac{1}{a^n}$$

For example, $2^{-4} = \frac{1}{2^4} = \frac{1}{16}$. If you need a final value, rewrite the answer with positive indices.

## Missing indices and matching bases

Sometimes you simplify first and then match the indices. In $y^3 \times y^a = y^8$, same-base multiplication gives $y^{3+a} = y^8$.

So $3 + a = 8$, which means $a = 5$. A missing index can even turn out to be negative after you solve the equation.

If numbers are involved, rewrite them using the same base before applying a law. For example, $16 \times 4^6 = 4^2 \times 4^6 = 4^8$ because $16 = 4^2$.

## Check yourself

1. Simplify $d^{10} \div d^6$.

   - $$d^4$ ✔

   - $$d^{16}$

   - $$d^{60}$

   - $$d^{-4}$

   _Explanation:_ The bases are both $d$, so for division you subtract the indices: $10 - 6 = 4$. A common wrong answer is $d^{16}$, but adding the indices only works for multiplication. Hint: Same base and division means subtract.

2. Given $\frac{x^5}{x^a} = x^7$, what is $a$?

   - 2

   - -2 ✔

   - 12

   - -12

   _Explanation:_ Dividing same-base powers means subtract the indices, so the left side becomes $x^{5-a}$. Matching powers gives $5 - a = 7$, so $a = -2$; a common wrong answer is 2 from solving the equation with the wrong sign.
