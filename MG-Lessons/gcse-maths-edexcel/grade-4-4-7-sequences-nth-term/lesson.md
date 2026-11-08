# grade-4-4-7-sequences-nth-term — lesson

_Lane: `gcse-maths-edexcel` · grade 4 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Sequence basics

A sequence is an ordered list of numbers, so position matters. Each number is a term, and the position tells you whether it is first, second, third, and so on.

A term-to-term rule tells you how to move from one term to the next, such as "add 4". An nth-term rule, such as $4n + 1$, gives the term at position $n$ directly.

When you meet a new sequence, check the gaps between consecutive terms. Do not just use the first gap, because some sequences have changing gaps.

## Using an nth-term formula

The letter $n$ means the position number, and in GCSE questions the first term is usually when $n=1$. To find a term, substitute the position into the formula.

For the nth term $5n + 2$, substitute $n=1$ and $n=2$. This gives the first two terms:
$$5(1) + 2 = 7$$
$$5(2) + 2 = 12$$

To check whether 37 is in the sequence, set the formula equal to 37 and solve the equation:
$$5n + 2 = 37$$
$$5n = 35$$
$$n = 7$$

Because $n=7$ is a positive whole number, 37 is a term in the sequence. If you get a decimal, fraction, or negative value for $n$, the number is not a term.

## Finding the nth term of an arithmetic sequence

![Aligned table comparing positions 1 to 5 for the arithmetic sequence 8, 13, 18, 23, 28 with the values of 5n, arrows showing a common difference of +5, and a label showing each term is +3 more so the nth term is 5n + 3](../assets/001-6b3805ba-0f64-46e9-a1d4-3967c2df642e.jpeg)

To find the $n$th term of an arithmetic sequence, start by working out the common difference. For the sequence $8, 13, 18, 23, 28$, the difference is $+5$, so the rule begins with $5n$.

$$5n$ gives $5, 10, 15, 20, 25$.

Each term in the sequence is $3$ more than this, so the $n$th term is $5n + 3$.

Check the rule:

- When $n = 1$, $5(1) + 3 = 8$
- When $n = 2$, $5(2) + 3 = 13$

These match the sequence, so the rule works.

## Decreasing arithmetic sequences

If a sequence goes down by the same amount each time, the common difference is negative. For $26, 22, 18, 14, 10$, the common difference is $-4$.

Start with $-4n$, which gives $-4, -8, -12, -16, -20$. Each actual term is $30$ more than that, so the nth term is $-4n + 30$.

Check it before you finish. When $n=1$, $-4n + 30 = 26$, and when $n=2$, $-4n + 30 = 22$, so the rule matches.

## A stretch: square nth terms

Not every nth term is linear. If the rule contains $n^2$, square the position first and then add or subtract.

For the rule $n^2 + 5$, substitute small values of $n$ to build the sequence. The first three terms are:
$$1^2 + 5 = 6$$
$$2^2 + 5 = 9$$
$$3^2 + 5 = 14$$

To check whether 54 is in the sequence, solve the equation for $n$. The working is:
$$n^2 + 5 = 54$$
$$n^2 = 49$$
$$n = 7$$

Since $n=7$ is a positive whole number, 54 is a term in the sequence. A common mistake is to stop at 49 and forget to account for the constant term.

## Check yourself

1. In an nth-term rule such as $5n + 2$, what does $n$ represent?

   - The first term

   - The position number ✔

   - The common difference

   - The total number of terms

   _Explanation:_ $$n$ stands for the position, so $n=1$ gives the first term, $n=2$ gives the second term, and so on. The most common wrong answer is "the first term", but the first term is the result after substituting $n=1$, not what $n$ means.

2. What is the nth term of the sequence $12, 16, 20, 24, \ldots$?

   - $$4n + 12$

   - $$4n + 8$ ✔

   - $$12n + 4$

   - $$4n - 8$

   _Explanation:_ The common difference is 4, so start with $4n$. The values of $4n$ begin 4, 8, 12, 16, so every actual term is 8 more, giving $4n + 8$. The most common wrong answer is $4n + 12$, which comes from adding the first term as the adjustment instead of comparing the sequence with $4n$.

3. Stretch: Which number is in the sequence with nth term $n^2 + 5$?

   - 49

   - 54 ✔

   - 58

   - 64

   _Explanation:_ 54 is correct because $7^2 + 5 = 49 + 5 = 54$. The most common wrong answer is 49, which comes from forgetting the $+5$ after squaring. Subtract 5 first, then check whether the result is a square number.
