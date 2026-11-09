# grade-6-6-1-recurring-decimals-to-fractions — lesson

_Lane: `gcse-maths-edexcel` · grade 6 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Recurring decimals and dot notation

A recurring decimal has a digit or block that repeats forever. In dot notation, one dot above a digit means that single digit repeats, while dots above the first and last digits show a whole block repeats.

For example, $0.7\dot{2} = 0.7222\ldots$ but $0.\dot{2}1\dot{6} = 0.216216\ldots$. Our aim is to write these exact decimals as exact fractions, not rounded approximations.

## The cancel-the-tail method

The key trick is to call the recurring decimal $x$. Then multiply by a power of 10 so the same repeating tail appears in both equations.

For $x = 0.\dot{7}$, write $$x = 0.777\ldots \qquad 10x = 7.777\ldots$$

Subtracting the first equation from the second gives $$9x = 7.$$

Now divide by 9 to get $$x = \frac{7}{9}.$$ This works because the recurring tails were identical and canceled out during subtraction.

## When the repeat starts later

![Aligned equations for x equals 0.5333..., 10x equals 5.3333..., and 100x equals 53.3333..., showing subtraction to get 90x equals 48](../assets/001-3a16b2ee-08b2-4258-af30-fdd1155b0546.jpeg)

Sometimes there is a fixed digit before the repeat begins. Then you choose two shifted versions of $x$ so the recurring tails match exactly.

If $x = 0.5\dot{3}$, then

$$100x = 53.333\ldots \qquad 10x = 5.333\ldots$$

Subtracting gives

$$90x = 48$$

so

$$x = \frac{48}{90} = \frac{8}{15}. $$

In exams, $100x - 10x$ is the cleanest choice here. Using $10x - x$ can still work, but it leaves a decimal first and makes simplification easier to mess up.

## Longer blocks and whole number parts

Longer recurring blocks and numbers bigger than 1 work the same way. If there are $m$ non-recurring digits before a recurring block of $n$ digits, use $10^m x$ and $10^{m+n} x$.

For $x = 2.4\dot{3}\dot{6}$, there is 1 fixed decimal digit and a 2-digit recurring block, so use $10x$ and $1000x$. Then: $$10x = 24.3636\ldots \qquad 1000x = 2436.3636\ldots$$

Subtracting gives $990x = 2412$, resulting in: $$x = \frac{2412}{990} = \frac{134}{55}$$ Always finish by simplifying your final fraction to its simplest form.

## Calculations and recurring 9s

For any calculation, convert each recurring decimal to a fraction first. That keeps the answer exact and lets you use normal fraction rules.

For example, $0.1\dot{8} = \frac{17}{90}$ and $0.\dot{6} = \frac{2}{3}$. So

$$\frac{17}{90} \div \frac{2}{3} = \frac{17}{90} \times \frac{3}{2} = \frac{17}{60}.$$

Also remember the special case $0.\dot{9} = 1$. A tail of recurring 9s means the number is exactly equal to the next terminating decimal, so $1.2\dot{9} = 1.3$.

## Check yourself

1. What does $0.\dot{4}0\dot{5}$ mean?

   - $$0.405405405\dots$ ✔

   - $$0.450450450\dots$

   - $$0.45555\dots$

   - $$0.405555\dots$

   _Explanation:_ The dots above 4 and 5 mean the whole block 405 repeats, so the decimal is $0.405405405\dots$. The common wrong answer $0.450450450\dots$ treats 45 as the recurring block and misses the 0 in the middle.

2. For $x = 0.3\dot{7}$, which is the smallest standard pair of equations to subtract?

   - $$10x$ and $x$

   - $$100x$ and $10x$ ✔

   - $$1000x$ and $100x$

   - $$100x$ and $x$

   _Explanation:_ There is 1 non-recurring digit and 1 recurring digit, so the standard pair is $10^1 x$ and $10^{1+1} x$, which are $10x$ and $100x$. The common wrong answer $100x$ and $x$ skips the first shift; it can be forced to work, but it is not the smallest standard pair and usually leaves extra tidying.

3. Stretch: What is the exact value of $0.1\dot{8} \div 0.\dot{6}$?

   - $$\frac{17}{60}$ ✔

   - $$\frac{17}{135}$

   - $$\frac{60}{17}$

   - $$\frac{17}{90}$

   _Explanation:_ First convert to fractions: $0.1\dot{8} = \frac{17}{90}$ and $0.\dot{6} = \frac{2}{3}$. Then divide by multiplying by the reciprocal, so $\frac{17}{90} \times \frac{3}{2} = \frac{17}{60}$; the common wrong answer $\frac{17}{135}$ comes from multiplying by $\frac{2}{3}$ instead of flipping it to $\frac{3}{2}$.
