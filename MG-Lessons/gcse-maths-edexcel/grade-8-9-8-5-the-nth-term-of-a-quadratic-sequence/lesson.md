# grade-8-9-8-5-the-nth-term-of-a-quadratic-sequence — lesson

_Lane: `gcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Spotting a quadratic sequence

![Difference table for the sequence 7, 15, 27, 43 showing first differences +8, +12, +16 and constant second differences +4, +4](../assets/001-d1b7884b-b35b-4ad2-9ef8-88262f8190a6.jpeg)

A sequence is a list of numbers following a rule, and the position of each term is called the term number $n$. The nth term is a formula that gives the value of a term for any chosen position.

Linear sequences have constant first differences, but quadratic sequences have constant second differences. In the diagram, the gaps between the gaps stay the same, so the sequence is quadratic.

## The $2a$ rule

Quadratic nth terms usually have the form $an^2 + bn + c$. The constant second difference is $2a$, so halving the second difference gives the coefficient of $n^2$.

If the second difference is 6, the formula starts with $3n^2$. If the second difference is -4, it starts with $-2n^2$, so the sign matters as well.

## Extending the pattern

The sequence $3, 8, 15, 24$ has first differences $5, 7, 9$, so the second difference is 2. Because that second difference is constant, keep increasing the first differences by 2.

$$$5,\quad 7,\quad 9,\quad 11,\quad 13$$

Add the new differences to the last term: $24 + 11 = 35$ and $35 + 13 = 48$. So the next two terms are 35 and 48.

## Worked example: finding the nth term

For the sequence $7, 15, 27, 43$, the first differences are $8, 12, 16$ and the second differences are $4, 4$. Since $4 = 2a$, the coefficient of $n^2$ is $a = 2$.

Start with $2n^2$ and list its first four values.
$$2,\quad 8,\quad 18,\quad 32$$
These are the values to subtract from the original terms.

Subtracting gives the leftover sequence below.
$$7 - 2 = 5,\quad 15 - 8 = 7,\quad 27 - 18 = 9,\quad 43 - 32 = 11$$
This leftover sequence increases by 2 each time, so its nth term is $2n + 3$.

Combine the quadratic and linear parts to get $2n^2 + 2n + 3$. A quick check gives 7 when $n = 1$ and 15 when $n = 2$, so the formula is consistent.

## When the second difference is negative

The sequence $18, 15, 10, 3$ has first differences $-3, -5, -7$ and constant second differences of $-2$. Halving this second difference gives $a = -1$, which indicates the nth term formula begins with $-n^2$.

The first four values of the sequence $-n^2$ are shown below:
$$-1,\quad -4,\quad -9,\quad -16$$
Subtracting these from the original sequence terms leaves a constant result:
$$19,\quad 19,\quad 19,\quad 19$$

Since this leftover value is constant, it contributes a simple $+19$ to the expression. The final nth term is $-n^2 + 19$. A common mistake is writing $n^2 + 19$, but that would result in a positive second difference rather than a negative one.

## Finding the term number

Sometimes you know the nth term and want the position of a particular value. Set the formula equal to that value and rearrange so one side is 0.

For $n^2 + 2n + 5 = 85$, move 85 across to get $n^2 + 2n - 80 = 0$. Then factorise:

$$$(n + 10)(n - 8) = 0$$

So $n = -10$ or $n = 8$. Only positive whole numbers can be term numbers, so the value 85 is the 8th term.

## Check yourself

1. Why is the sequence $6, 10, 16, 24$ quadratic?

   - The first differences are constant

   - The second differences are constant ✔

   - Every term is even

   - The terms are increasing

   _Explanation:_ The first differences are $4, 6, 8$, so they are not constant. The second differences are $2, 2$, which is the key sign of a quadratic sequence. A common wrong answer is A, but constant first differences would mean the sequence is linear, not quadratic.

2. The sequence $4, 11, 22, 37, \dots$ is quadratic. What is the next term?

   - 52

   - 54

   - 56 ✔

   - 60

   _Explanation:_ The first differences are $7, 11, 15$, so the second difference is 4. The next first difference is $19$, so the next term is $37 + 19 = 56$. A common wrong answer is A, which repeats the difference of 15 instead of increasing it by 4.

3. What is the nth term of the sequence $18, 15, 10, 3$?

   - $$n^2 + 19$

   - $$-n^2 + 19$ ✔

   - $$-n^2 - 19$

   - $$n^2 - 19$

   _Explanation:_ The first differences are $-3, -5, -7$, so the second difference is $-2$ and therefore $a = -1$. Using $-n^2$ leaves a constant 19, so the full formula is $-n^2 + 19$. A common wrong answer is A, but $n^2 + 19$ would have second difference $+2$, not $-2$.
