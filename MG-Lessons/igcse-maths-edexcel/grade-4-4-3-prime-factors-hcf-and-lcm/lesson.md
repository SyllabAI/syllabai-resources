# grade-4-4-3-prime-factors-hcf-and-lcm — lesson

_Lane: `igcse-maths-edexcel` · grade 4 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Factors, multiples and primes

A factor divides exactly into a number, while a multiple is a number in another number's times table. A prime number has exactly two factors, 1 and itself.

For example, $8$ is a factor of $56$ because $56 \div 8 = 7$. Also, $56$ is a multiple of $8$ because $8 \times 7 = 56$.

The number $1$ is not prime because it has only one factor. These ideas lead to HCF, the biggest shared factor, and LCM, the smallest shared multiple.

## Writing a number as a product of prime factors

![Factor tree for 84 showing 84 splitting to 12 and 7, 12 splitting to 3 and 4, and 4 splitting to 2 and 2, with prime leaves 2, 2, 3 and 7 highlighted](../assets/001-e468607e-b680-4206-bf60-a74f45548f53.jpeg)

A prime factorisation writes a number as a multiplication using only prime numbers. A factor tree helps you keep splitting until every branch ends with a prime.

For $84$, start with $84 = 12 \times 7$. Then split $12 = 3 \times 4$, and finally split $4 = 2 \times 2$.

Collect the prime leaves $2$, $2$, $3$ and $7$ and write them neatly as $84 = 2^2 \times 3 \times 7$. The exponent in $2^2$ shows repeated multiplication: $2 \times 2$.

## Finding the HCF

To find the Highest Common Factor (HCF), write each number as a product of prime factors. Keep only the prime factors that appear in both numbers. If a prime factor appears with different powers, use the smaller power.

For example, $72 = 2^3 \times 3^2$ and $108 = 2^2 \times 3^3$. The shared prime factors are $2^2$ and $3^2$, because both numbers contain at least two 2s and two 3s.

Multiply the shared factors:
$$2^2 \times 3^2 = 36$$
So the HCF is $36$. Because we used every shared prime factor, no larger common factor is possible.

In a Venn diagram, the HCF comes from the overlap. The extra $2$ from 72 and the extra $3$ from 108 are not included in the HCF. For the LCM, you would use all the prime factors from both numbers.

## Finding the LCM

For LCM, use every prime that appears in at least one of the numbers. If a prime has different powers, choose the largest power.

For $90$ and $126$, write $90 = 2 \times 3^2 \times 5$ and $126 = 2 \times 3^2 \times 7$. The primes you need are $2$, $3$, $5$ and $7$.

So $\text{LCM} = 2 \times 3^2 \times 5 \times 7 = 630$. This is the smallest number that is a multiple of both 90 and 126.

If a prime appears in only one number, it does not belong in the HCF, but it does belong in the LCM. That is why 5 and 7 are both included here.

## Repeated events use the LCM

When repeated events start together, the next time they happen together is found using the LCM of the intervals. After finding the LCM, add that amount of time to the start time.

For buses every 12 minutes and 18 minutes, write $12 = 2^2 \times 3$ and $18 = 2 \times 3^2$. Using the largest powers gives $\text{LCM} = 2^2 \times 3^2 = 36$.

If both buses leave at 8:15 am, they next leave together 36 minutes later at 8:51 am. Do not add 12 and 18, because 30 is not a multiple of both intervals.

## Working backwards from HCF and LCM

A reverse question gives you the HCF and LCM and asks for the original numbers. If two numbers have HCF 6, you can write them as $6a$ and $6b$, where $a$ and $b$ are coprime.

If the LCM is 180, divide by the HCF: $180 \div 6 = 30$. Now look for a coprime factor pair of 30, such as 5 and 6.

Multiply back by 6: $6 \times 5 = 30$ and $6 \times 6 = 36$. So one possible pair is 30 and 36.

Always check both conditions at the end. Here, $\text{HCF}(30,36) = 6$ and $\text{LCM}(30,36) = 180$.

## Check yourself

1. Which statement is true?

   - 1 is a prime number

   - 8 is a factor of 56 ✔

   - 56 is a factor of 8

   - 9 is a prime number

   _Explanation:_ 8 is a factor of 56 because $56 \div 8 = 7$, which is a whole number. A common wrong choice is A, but 1 is not prime because it has only one factor, not two.

2. What is the HCF of 48 and 60?

   - 12 ✔

   - 24

   - 240

   - 6

   _Explanation:_ HCF means shared primes with smallest powers. $48 = 2^4 \times 3$ and $60 = 2^2 \times 3 \times 5$, so the shared primes with the smallest powers are $2^2$ and $3$. That gives $2^2 \times 3 = 12$. A common wrong answer is 240, which is the LCM because it uses the largest powers and includes the 5.

3. Two alarms ring together at $9:00$ am. One rings every $8$ minutes and the other every $12$ minutes. When do they next ring together?

   - 9:20 am

   - 9:24 am ✔

   - 9:36 am

   - 10:36 am

   _Explanation:_ The LCM of $8$ and $12$ is $24$, so the next time together is $24$ minutes after $9:00$ am, which is $9:24$ am. A common wrong answer is $9:20$ am, which comes from adding the intervals even though $20$ is not a multiple of $12$.

4. Two numbers are both greater than 20. Their HCF is 6 and their LCM is 180. Which pair fits?

   - 24 and 45

   - 30 and 36 ✔

   - 18 and 60

   - 12 and 90

   _Explanation:_ $$30 = 2 \times 3 \times 5$ and $36 = 2^2 \times 3^2$, so the shared smallest powers give HCF $6$ and the largest powers give LCM $2^2 \times 3^2 \times 5 = 180$. A common wrong answer is 18 and 60 because it does have HCF 6 and LCM 180, but 18 is not greater than 20. Hint: Divide the LCM by the HCF, then use a coprime factor pair of the result.
