# grade-6-6-1-recurring-decimals-to-fractions — lesson

_Lane: `igcse-maths-edexcel` · grade 6 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Reading recurring decimal notation

A fraction is another way of writing a division, so some fractions give terminating decimals and others give recurring decimals. A recurring decimal has a digit or block of digits that repeats forever.

A dot over one digit means that digit repeats, so $0.\dot{7}=0.777\dots$. Two dots mark the first and last digit of the repeating block, so $0.\dot{3}\dot{6}=0.363636\dots$.

Be careful with mixed decimals like $0.2\dot{4}\dot{9}=0.2494949\dots$. The 2 does not repeat; only the block 49 repeats. In long division, if the same remainder appears again, the decimal will start repeating from that point.

## The algebra cancellation trick

To turn a recurring decimal into a fraction, let the decimal be $x$. Then multiply by powers of 10 until the recurring tails line up exactly.

If there are $n$ non-recurring digits and the repeating block has length $r$, compare $10^{n+r}x$ with $10^n x$. Subtracting removes the infinite tail because the recurring parts are identical.

For a pure recurring decimal with a 2-digit block, compare $100x$ and $x$. For a mixed recurring decimal like $0.3\dot{8}$, compare $100x$ and $10x$ because one digit is non-recurring and one digit recurs.

## Worked example: pure recurring decimal

For a pure recurring decimal, the repeat starts immediately after the decimal point. Let $x=0.666\ldots$, so $10x=6.666\ldots$.

Subtract the first equation from the second to eliminate the recurring digits. $$10x-x=6.666\ldots-0.666\ldots$$ $$9x=6$$ The matching recurring parts cancel out perfectly.

Now divide by 9 to solve for $x$ and simplify the fraction. $$x=\frac{6}{9}=\frac{2}{3}$$ So $0.\dot{6}=\frac{2}{3}$.

## Worked example: one non-recurring digit

![Aligned equations for x equals 0.3888 recurring, 10x equals 3.8888 recurring, and 100x equals 38.8888 recurring, with matching recurring tails cancelling to give 90x equals 35](../assets/001-55fb0d5c-a778-4b7b-88bf-ff6127213f91.jpeg)
Now convert $0.3\dot{8}$, which means $0.3888\dots$. Let $x=0.3888\dots$.

One digit is non-recurring, so first multiply by 10.
$$10x=3.8888\ldots$$
One full recurring digit later, multiply by 100.
$$100x=38.8888\ldots$$

Now the tails match, so subtract.
$$100x-10x=38.8888\ldots-3.8888\ldots$$
$$90x=35$$
Using $10x$ and $x$ would not make the tails identical.

Solve and simplify.
$$x=\frac{35}{90}=\frac{7}{18}$$
So $0.3\dot{8}=\frac{7}{18}$.

## Whole numbers and longer repeats

A whole number before the decimal point does not change the method. Keep the whole number inside $x$ and work with the entire decimal.

Consider the decimal $3.2\dot{6}\dot{3}=3.263636\ldots$. Since there is 1 non-recurring digit and a 2-digit recurring block, let $x=3.263636\ldots$ and compare $1000x$ and $10x$.

Write the two equations to align the decimals: $$1000x=3263.636363\ldots$$ $$10x=32.636363\ldots$$ Now the recurring tails match exactly.

Subtract and solve to find the final value: $$990x=3231$$ $$x=\frac{3231}{990}=\frac{359}{110}$$ Note that leaving the answer as an improper fraction is perfectly acceptable.

## Calculations with recurring decimals

When a question asks you to multiply or divide recurring decimals, convert each one to a fraction first. This is quicker and avoids messy infinite decimals.

For $0.4\dot{2}$, let $x=0.4222\ldots$.
$$100x=42.222\ldots$$
$$10x=4.222\ldots$$
Subtracting these equations gives $90x=38$.

This result gives $x=\frac{19}{45}$. Using $0.\dot{3}=\frac{1}{3}$, we can now divide using fractions:
$$0.4\dot{2}\div 0.\dot{3}=\frac{19}{45}\div\frac{1}{3}=\frac{19}{45}\times 3=\frac{19}{15}$$

Dividing by a fraction means multiplying by its reciprocal. Always simplify the final answer if you can.

## Check yourself

1. In $0.2\dot{4}\dot{9}$, which part repeats forever?

   - 49 ✔

   - 249

   - 94

   - 2

   _Explanation:_ The dots show the first and last digits of the recurring block, so the repeating part is 49. The common wrong answer 249 includes the non-recurring 2, but only the dotted digits repeat.

2. What is $0.\dot{5}$ as a fraction in simplest form?

   - $$\frac{5}{9}$ ✔

   - $$\frac{1}{2}$

   - $$\frac{5}{10}$

   - $$\frac{9}{5}$

   _Explanation:_ Since $0.\dot{5}=0.555\dots$, letting $x=0.555\dots$ gives $10x=5.555\dots$, so subtracting gives $9x=5$ and therefore $x=\frac{5}{9}$. The common wrong answer $\frac{1}{2}$ comes from confusing recurring $0.555\dots$ with terminating $0.5$. Hint: One recurring digit straight after the decimal often leads to ninths.

3. If $x=3.263636\ldots$, which pair should you compare and subtract?

   - $$1000x$ and $10x$ ✔

   - $$100x$ and $x$

   - $$1000x$ and $x$

   - $$100x$ and $10x$

   _Explanation:_ There is 1 non-recurring digit and a 2-digit recurring block, so you need $10^{1+2}x$ and $10^1x$, which are $1000x$ and $10x$. The common wrong choice $100x$ and $10x$ does not line up the full recurring block 63, so the tails will not match exactly.
