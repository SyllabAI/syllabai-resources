# grade-6-6-4-repeated-percentage-change — lesson

_Lane: `gcse-maths-edexcel` · grade 6 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Multipliers first

![Flow diagram showing £100 becoming £110, £121, and £133.10 under three successive multipliers of 1.10, with overall multiplier 1.10^3 labelled](../assets/001-c34cae33-7b78-4a98-8607-2d17bc1ed211.jpeg)

A repeated percentage change means the same kind of percentage change happens more than once, each time on the new amount. The quickest method is to turn the percentage into a multiplier.

For an increase of $p\%$, use $1+\frac{p}{100}$. For a decrease of $p\%$, use $1-\frac{p}{100}$. For example, a 12% increase gives a multiplier of $1.12$, while a 12% decrease gives $0.88$.

If the same multiplier $m$ happens $n$ times, the overall multiplier is $m^n$. That is why repeated percentage change is really about multipliers, powers, and sometimes roots.

## Same change repeated

Repeated changes are not found by adding the percentages. A 12% increase each hour means multiply by $1.12$ each hour.

If the starting population is $P$, then after 3 hours it is $P \times 1.12^3$. Calculate the power first:
$$1.12^3 = 1.404928$$
So the final population is about $1.405$ times the original.

To turn the multiplier back into a percentage increase, subtract 1 and multiply by 100.
$$\left(1.404928 - 1\right)\times 100 = 40.4928$$
So the total increase is about 40.5%, not 36%.

## Different changes in a row

When different percentage changes happen one after another, multiply the multipliers in order. Do not add the percentages unless the question says both are taken from the original amount.

To test '15% off, then another 20% off', start with £100. The calculation is: $$100 \times 0.85 \times 0.80 = 68$$ This result shows that the overall multiplier for both changes is $0.68$.

A final price of £68 from £100 means a 32% decrease. The common wrong answer is 35%, which comes from adding 15 and 20 instead of compounding them.

## Compound interest backwards

Compound interest uses the same multiplier idea, because each year's interest is added before the next year's interest is worked out. The general model is
$$\text{final amount} = \text{starting amount} \times m^n$$
where $m$ is the yearly multiplier.

Aisha has £5624.32 after 3 years at 4% compound interest. Let the starting amount be $A$, so
$$A \times 1.04^3 = 5624.32$$

Divide by $1.04^3$ to undo the repeated increase. Then
$$A = \frac{5624.32}{1.04^3} = 5000$$
so Aisha invested £5000.

## Finding the repeated rate

Sometimes you know the total change but not the equal rate each time. In that case, an $n$th root undoes the power.

Suppose a colony grows by 75% over 5 years at a constant rate. The overall multiplier is $1.75$, so if the yearly multiplier is $m$ then:
$$m^5 = 1.75$$

Take the fifth root to find the one-year multiplier:
$$m = \sqrt[5]{1.75} \approx 1.1184$$
This means a yearly increase of 11.84%, so the rate is 11.8% to 1 decimal place.

## Length, area, and volume

![Split-panel diagram showing a square with side multiplier 1.06 leading to area multiplier 1.06^2, and a cube with side multiplier k leading to volume multiplier k^3](../assets/002-a5de5a91-e020-47c4-98d6-d24003692344.jpeg)
When every length changes by multiplier $k$, area changes by $k^2$ and volume changes by $k^3$. Working backwards means using a square root for area or a cube root for volume.

If a circle's radius increases by 6%, the radius multiplier is $1.06$. Its area multiplier is
$$1.06^2 = 1.1236$$
so the area increases by 12.36%.

If a cube's volume increases by 20%, the volume multiplier is $1.20$. The side length multiplier is
$$\sqrt[3]{1.20} \approx 1.06266$$
so the side length increases by about 6.27%.

## Check yourself

1. What is the multiplier for a $12\%$ increase?

   - 1.12 ✔

   - 0.88

   - 1.20

   - 0.12

   _Explanation:_ A $12\%$ increase means $112\%$ of the original, so the multiplier is $1.12$. The common wrong answer $0.88$ is the multiplier for a $12\%$ decrease, because it leaves $88\%$ of the original.

2. A price is reduced by $10\%$ and then increased by $10\%$. What is the overall change?

   - No change

   - 1% decrease ✔

   - 1% increase

   - 20% increase

   _Explanation:_ Start with $£100$: after a $10\%$ decrease it becomes $£90$, and after a $10\%$ increase it becomes $£99$, so the overall change is a $1\%$ decrease. The common wrong answer "no change" comes from cancelling $+10\%$ and $-10\%$, but the second change is applied to the smaller amount.

3. Stretch: A machine is worth 40% of its original value after 6 years, falling by the same percentage each year. What is the yearly percentage decrease, to 2 d.p.?

   - 10.00%

   - 14.16% ✔

   - 40.00%

   - 60.00%

   _Explanation:_ Hint: First find the multiplier that remains each year. Being worth 40% overall means an overall multiplier of $0.40$, so the yearly multiplier is $\sqrt[6]{0.40} \approx 0.85837$. That is a yearly decrease of $1 - 0.85837 = 0.14163$, so about 14.16%; the common wrong answers 40% and 60% confuse the total change with the equal yearly change.
