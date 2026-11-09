# grade-3-3-1-error-intervals — lesson

_Lane: `gcse-maths-edexcel` · grade 3 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## The basic idea

![Number line showing the error interval for 6.8 to 1 decimal place, with a filled dot at 6.75, an open dot at 6.85, and 6.8 in the centre](../assets/001-c69553b8-d4c8-48f6-baea-1a4f1a9a4ce3.jpeg)

An error interval shows the range of original values that could have produced a rounded answer. If a number rounds to $6.8$ to 1 decimal place, the actual value could be anywhere from $6.75$ up to, but not including, $6.85$.

The smallest boundary is the lower bound and the largest boundary is the upper bound. For normal rounding, we write the interval with $\le$ on the left and $<$ on the right, because the upper boundary would round to the next value.

A quick method is to find the step size, then take half of it. This method works for ordinary rounding, not truncation.

$$$r - \frac{s}{2} \le x < r + \frac{s}{2}$$

## Correct to the nearest whole unit

When a measurement is correct to the nearest whole unit, the step size is $1$. That means the half-step is $0.5$.

Worked example: a sack has a mass of 18 kg, correct to the nearest kg. Subtract $0.5$ for the lower bound and add $0.5$ for the upper bound.

$$$18 - 0.5 = 17.5,\qquad 18 + 0.5 = 18.5$$

If $m$ is the mass in kg, the error interval is $17.5 \le m < 18.5$. We do not include $18.5$ because $18.5$ kg rounds to 19 kg.

## Rounded to decimal places

For decimal places, the step size depends on the place value of the last kept digit. To 1 decimal place the step is $0.1$, and to 2 decimal places the step is $0.01$.

Worked example: $x$ rounds to $1.34$ to 2 decimal places. The last kept digit is in the hundredths place, so the half-step is $0.005$.

$$$1.34 - 0.005 = 1.335,\qquad 1.34 + 0.005 = 1.345$$

So the error interval is $1.335 \le x < 1.345$. The most common mistake is writing $\le$ on both sides, but $1.345$ rounds to $1.35$.

## Significant figures

For significant figures, count from the first non-zero digit, not from the decimal point. After you find the last significant figure, use its place value to get the step size.

Example 1: if a number rounds to $0.472$ to 3 significant figures, the third significant figure is in the thousandths place. The step size is $0.001$, so the half-step is $0.0005$ and the interval is $0.4715 \le x < 0.4725$.

Example 2: if a number rounds to $7000$ to 1 significant figure, the 7 is in the thousands place. The step size is $1000$, so the half-step is $500$ and the interval is $6500 \le x < 7500$.

## Truncation is different

![Two number lines comparing rounding and truncation for 4.73 to 2 decimal places, with 4.725 to 4.735 for rounding and 4.73 to 4.74 for truncation](../assets/002-c875123b-8d3a-45bb-9931-1a36be85b5c3.jpeg)

Truncation means cutting digits off without rounding up. So if a positive number is truncated to 2 decimal places and shown as $4.73$, the actual value starts at $4.73$.

The next possible hundredth after $4.73$ is $4.74$, so the interval is $4.73 \le x < 4.74$. Do not use a half-step for truncation.

This is different from rounding to 2 decimal places, which would give $4.725 \le x < 4.735$. In exams, underline whether the question says rounded, correct to the nearest, or truncated before you calculate.

## Check yourself

1. A number rounds to $6.8$ to 1 decimal place. Which error interval is correct?

   - $$6.75 \le x < 6.85$ ✔

   - $$6.8 \le x < 6.9$

   - $$6.75 < x \le 6.85$

   - $$6.7 \le x < 6.9$

   _Explanation:_ To 1 decimal place, the step size is $0.1$, so the half-step is $0.05$. That gives $6.75 \le x < 6.85$; the common wrong answer $6.8 \le x < 6.9$ treats rounding like truncation and misses values such as $6.76$.

2. $$y$ rounds to $9.6$ to 1 decimal place. Which interval is correct?

   - $$9.55 \le y < 9.65$ ✔

   - $$9.5 \le y < 9.7$

   - $$9.59 \le y < 9.61$

   - $$9.6 \le y < 9.7$

   _Explanation:_ To 1 decimal place, the step size is $0.1$ and the half-step is $0.05$, so the bounds are $9.55$ and $9.65$. The common wrong answer $9.6 \le y < 9.7$ is a truncation-style interval, not a rounding interval.

3. A positive number is truncated to 2 decimal places and the result is $4.73$. Which interval is correct?

   - $$4.73 \le x < 4.74$ ✔

   - $$4.725 \le x < 4.735$

   - $$4.70 \le x < 4.76$

   - $$4.73 < x \le 4.74$

   _Explanation:_ Truncation keeps the given digits and cuts off the rest, so the smallest possible value is exactly $4.73$ and the next hundredth is $4.74$. The common wrong answer $4.725 \le x < 4.735$ is the interval for rounding to 2 decimal places, not truncating.
