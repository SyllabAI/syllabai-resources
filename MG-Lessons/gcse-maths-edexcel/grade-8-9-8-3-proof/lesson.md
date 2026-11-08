# grade-8-9-8-3-proof — lesson

_Lane: `gcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What proof means

![Flowchart of algebraic proof with boxes labelled define n, write even odd and consecutive forms, substitute and simplify, factorise into target forms, and conclude](../assets/001-04e11e40-8db1-4f46-82c2-7f6159044d5a.jpeg)

In proof, checking a few examples is not enough. We use a letter such as $n$ to stand for any allowed integer, so the argument works for every case.

Standard forms matter. Even numbers are $2n$, odd numbers are $2n+1$, and consecutive integers can be written as $n$ and $n+1$.

Before you start, decide the target form you want to reach, such as $2k+1$, $6k$, $k^2$, or $8k+2$. A good proof follows a clear chain: define the general number, substitute, simplify, factorise if needed, and conclude. The last sentence must explain why the remaining part is an integer.

## Worked example: consecutive integers

To prove a result about two consecutive integers, let the smaller integer be $n$. Then the next integer is $n+1$, which keeps the proof general. Add the two expressions and simplify.

$$$n+(n+1)=2n+1$$

The result is now in the form $2k+1$. Since $2n$ is even for every integer $n$, $2n+1$ is always odd. Therefore, the sum of two consecutive integers is always odd.

## Worked example: three consecutive even integers

For consecutive even integers, start with an even number on purpose. A safe general form is $2n$, $2n+2$, and $2n+4$.

Add the three expressions and collect like terms.
$$
2n+(2n+2)+(2n+4)=6n+6
$$
Now the common factor of 6 is visible.

Factorise completely.
$$
6n+6=6(n+1)
$$
Since $n+1$ is an integer, the sum is always a multiple of 6. Therefore, three consecutive even integers always add to a number divisible by 6.

## Expand, simplify, then factorise

Some proof questions use brackets and powers to hide the answer. The safest method is to expand first, simplify second, and then factorise last. For $(4n+3)^2-(4n-3)^2$, you should expand each square individually before you subtract.

$$$
(4n+3)^2=16n^2+24n+9
$$
$$
(4n-3)^2=16n^2-24n+9
$$

Expanding separately avoids losing the minus sign in front of the second bracket. If the question asks for a multiple of 12, your final line should look like $12k$. After subtraction, we want a factor of 12 to appear clearly.

## Finishing the divisibility proof

Now subtract carefully.
$$
(16n^2+24n+9)-(16n^2-24n+9)=48n
$$
The $16n^2$ terms cancel, and the outside minus turns $-24n$ into $+24n$.

Next factorise the result.
$$
48n=12(4n)
$$
Since $4n$ is an integer, the expression is always a multiple of 12. Therefore, $(4n+3)^2-(4n-3)^2$ is always divisible by 12.

A quick check is
$$
(a+b)^2-(a-b)^2=4ab
$$
Here $a=4n$ and $b=3$, so
$$
4ab=4 \times 4n \times 3=48n
$$
which matches the full proof.

## Worked example: proving a square number

If the target is a square number, do not stop at an expanded expression like $n^2+10n+25$. You want a single bracket squared, because that shows the value is $k^2$ for some integer $k$.

Consider $(n+5)(n+4)+(n+5)$. Both terms contain $n+5$, so factorise that common factor first. $$(n+5)(n+4)+(n+5)=(n+5)(n+4+1)$$

Now simplify inside the bracket and rewrite the product as a square. $$(n+5)(n+4+1)=(n+5)(n+5)=(n+5)^2$$ Since $n+5$ is an integer, the expression is always a square number.

## Check yourself

1. Which algebraic form always represents an odd integer?

   - $$2n+1$ ✔

   - $$2n$

   - $$n+1$

   - $$n+2$

   _Explanation:_ $$2n+1$ is one more than an even number, so it is always odd. The common wrong answer is $n+1$, but if $n=3$ then $n+1=4$, which is even.

2. Why is $n$, $n+2$, $n+4$ not a safe starting point for proving something about three consecutive even integers?

   - The numbers are not 2 apart

   - The numbers might not all be even ✔

   - You must always use a different letter for each number

   - Factorising will no longer work

   _Explanation:_ $$n$, $n+2$, $n+4$ are 2 apart, but they are only guaranteed to be even if $n$ is even. The common wrong answer is A, but the spacing is fine; the problem is the missing guarantee that the numbers are even.

3. The sum $(2n+1)^2+(2n+3)^2$ simplifies to $8n^2+16n+10$. Which line completes the proof that it is 2 more than a multiple of 8?

   - $$8(n^2+2n+1)+2$ ✔

   - $$8(n^2+2n+1)$

   - $$2(4n^2+8n+5)$

   - $$(2n+2)^2+6$

   _Explanation:_ To prove “2 more than a multiple of 8”, the expression must be written as $8k+2$, and A does exactly that with $k=n^2+2n+1$. The common wrong answer is B because it shows a multiple of 8, but it misses the extra 2 that the question asks for.
