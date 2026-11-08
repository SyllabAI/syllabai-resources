# grade-8-9-8-7-sequences-higher — lesson

_Lane: `igcse-maths-edexcel` · grade 8 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Spotting arithmetic sequences

![Arithmetic sequence 4, 7, 10, 13, 16 with equal +3 jumps, and paired first-last terms showing the arithmetic series formula](../assets/001-c9055cea-085e-4763-8a85-27a35811627a.jpeg)

A sequence is an ordered list of numbers, where each number is called a term. In an arithmetic sequence, the gap between consecutive terms is always the same; this constant gap is called the common difference, $d$.

If the first term is $a$, then the term in position $n$ is written $T_n$. For an arithmetic sequence, the formula is $$T_n=a+(n-1)d$$ because you make one fewer jump than the term number.

For example, in the sequence $5, 8, 11, 14, \ldots$, the first term is $a=5$ and the common difference is $d=3$. This means the sequence grows by adding 3 to the previous term each time.

## Finding a far-away term

To find a later term, identify the first term and the common difference before using the formula. In the sequence $6, 10, 14, 18, 22, \ldots$, we have $a=6$ and $d=4$.

Now substitute these values into the general formula $$T_n=a+(n-1)d$$ to get $$T_{40}=6+(40-1)\times 4$$. Note that there are 39 jumps from the 1st term to the 40th term, not 40.

Simplify the arithmetic carefully to find the specific value: $$T_{40}=6+39\times 4=6+156=162$$ By following these steps, we find that the 40th term is 162.

## From sequence to series

A series is what you get when you add the terms of a sequence. For arithmetic sequences, the sum of the first $n$ terms is written $S_n$.

If you know the first term $a$, the last term $l$, and the number of terms $n$, use $$S_n=\frac{n}{2}(a+l)$$ This formula works because the sum of the first and last terms, the second and second-last, and so on, all result in the same total.

If you know $a$ and $d$ instead of the last term, use $$S_n=\frac{n}{2}\left(2a+(n-1)d\right)$$ This version follows the same logic, but replaces the last term $l$ with the expression for the $n^{th}$ term: $a+(n-1)d$.

## Worked example: sum of many terms

Suppose the sequence is $4, 7, 10, 13, 16, \ldots$ and we want the sum of the first 100 terms. Here $a=4$, $d=3$, and $n=100$.

Use the series formula: $$S_{100}=\frac{100}{2}\left(2\times 4+(100-1)\times 3\right)$$ Always simplify the bracket first so the arithmetic stays clear.

Now calculate: $$S_{100}=50(8+297)=50\times 305=15250$$ So the sum of the first 100 terms is 15250.

## Working backwards from two known terms

Sometimes you are given two terms instead of the first term and common difference. If the 6th term is 23 and the 14th term is 55, we can write the following equations: $$a+5d=23$$ and $$a+13d=55$$.

Subtract the equations to eliminate $a$: $$8d=32$$ so $$d=4$$. Then substitute back into $a+5d=23$ to get $$a+20=23$$ and so $$a=3$$.

Now you know the whole sequence and can calculate any term or sum. For example, the sum of the first 50 terms is: $$S_{50}=\frac{50}{2}\left(2\times 3+49\times 4\right)=25(6+196)=5050$$.

## Algebraic consecutive terms

For three consecutive terms in an arithmetic sequence, the two gaps must be equal. So if the terms are $x+4$, $3x-2$, and $4x+1$, start by writing $$ (3x-2)-(x+4)=(4x+1)-(3x-2) $$

Now simplify both sides: $$2x-6=x+3$$ so $$x=9$$. This gives the actual values of the three consecutive terms.

Finally, find the common difference by substituting back: $$d=(3x-2)-(x+4)=2x-6=12$$. In a prove question, do not stop at $x=9$; you must state the common difference as well.

## Check yourself

1. Which nth-term formula matches the sequence $12, 17, 22, 27, \ldots$?

   - $$12+5n$

   - $$12+5(n-1)$ ✔

   - $$5+12(n-1)$

   - $$12+4(n-1)$

   _Explanation:_ The first term is 12 and the common difference is 5, so the correct formula is $T_n=12+5(n-1)$. The most common wrong answer is A because it adds 5 even when $n=1$, which would give 17 as the first term instead of 12.

2. For an arithmetic sequence with $a=4$ and $d=3$, which expression gives $S_{20}$?

   - $$\frac{20}{2}(4+3)$

   - $$\frac{20}{2}(2\times 4+19\times 3)$ ✔

   - $$4+19\times 3$

   - $$\frac{20}{2}(2\times 4+20\times 3)$

   _Explanation:_ The correct formula is $S_n=\frac{n}{2}\left(2a+(n-1)d\right)$, so $S_{20}=\frac{20}{2}(2\times 4+19\times 3)$. The most common wrong answer is D because there are only 19 jumps from the 1st term to the 20th term, not 20. Hint: The bracket should contain $2a+(n-1)d$.

3. The 8th term of an arithmetic sequence is 29 and the 12th term is 45. What is the common difference?

   - 4 ✔

   - 16

   - 8

   - 29

   _Explanation:_ From the 8th term to the 12th term there are 4 jumps, and the total increase is $45 - 29 = 16$. So the common difference is $16 \div 4 = 4$. The most common wrong answer is B because it uses the total increase but forgets to divide by the number of jumps.

4. The expressions $2x+1$, $5x-4$, and $7x+2$ are consecutive terms of an arithmetic sequence. What is the common difference?

   - 11

   - 17

   - 28 ✔

   - 33

   _Explanation:_ Set the two gaps equal: $(5x-4)-(2x+1)=(7x+2)-(5x-4)$, so $3x-5=2x+6$ and therefore $x=11$. Then the common difference is $3x-5=28$. The most common wrong answer is A because 11 is the value of $x$, not the common difference.
