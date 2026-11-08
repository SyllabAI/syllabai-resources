# grade-4-4-1-compound-interest-and-depreciation — lesson

_Lane: `gcse-maths-edexcel` · grade 4 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## From percentages to multipliers

![Side-by-side timeline showing £1000 growing by 5% each year with multiplier 1.05 and £1000 depreciating by 10% each year with multiplier 0.90 over 3 years](../assets/001-c129a010-40c4-4106-97a8-925c4374c0fc.jpeg)

The starting amount is 100% of itself, so an increase uses a multiplier bigger than 1 and a decrease uses a multiplier smaller than 1. For example, a 6% increase uses $1.06$, while a 6% decrease uses $0.94$.

To build a multiplier, rewrite the new percentage as a decimal. So 8% increase means $108\% = 1.08$, and 25% decrease means $75\% = 0.75$. Compound interest and depreciation both use these multipliers again and again over time.

## Compound interest formula

Compound interest means each year's interest is added to the account, then next year's interest is worked out on the new balance. With a fixed annual rate of $r\%$, the multiplier is $1 + \frac{r}{100}$. If the starting amount is $P$, the final amount is $A$, and the money stays invested for $n$ years, use the formula below.

$$$A = P\left(1 + \frac{r}{100}\right)^n$$

The power $n$ shows the multiplier is used once per year. If the question asks for total interest, subtract the starting amount from the final amount after finding $A$. Note that 4 years at 3% is not the same as one 12% increase.

## Worked example: final amount and total interest

Ravi invests £3600 for 4 years at 2.5% compound interest per annum. The yearly multiplier is $1.025$ because $100\% + 2.5\% = 102.5\%$. Set up the calculation below:

$$$A = 3600 \times 1.025^4$$

Using the full calculator value gives $A = 3973.72640625$. Round only at the end, so the final amount is £3973.73. If the question asks for total interest, subtract the original £3600 to get £373.73.

## Depreciation and changing rates

Depreciation means a value goes down over time, so the multiplier is below 1. A fixed decrease of $r\%$ per year uses the formula shown below.

$$$A = P\left(1 - \frac{r}{100}\right)^n$$

If the percentage changes from year to year, do not add or combine the percentages. Use one multiplier for each year, such as $0.75$ for a 25% fall followed by $0.90$ for a 10% fall.

For a scooter worth £1800 that loses 25% in year 1 and 10% in each of the next two years, the calculation $1800 \times 0.75 \times 0.90^2 = 1093.50$ is used. Thus, the scooter is worth £1093.50 after 3 years.

## Comparing saving options fairly

When comparing savings options, calculate the final amount for each one and then compare. Do not just compare the percentages, because simple and compound interest are different methods.

Leah invests £7000 for 5 years. Option A gives 2.4% compound interest, so $7000 \times 1.024^5 = 7881.30$.

Option B gives 2.5% simple interest, so the interest each year is $0.025 \times 7000 = 175$. Over 5 years that is £875, so the final amount is £7875 and Option A is better.

## Finding the number of years

Sometimes the unknown is $n$, the number of years. At GCSE, a reliable method is to try whole-number powers on your calculator until the value matches or first passes the target.

For £3000 growing at 2% per year, try $3000 \times 1.02^5 = 3312.24$. Then try $3000 \times 1.02^6 = 3378.49$, so the investment has grown for 6 years.

For depreciation, compare powers with a threshold such as half the original value. For example, $0.85^4 = 0.522\ldots$ is still above $0.5$, but $0.85^5 = 0.443\ldots$ is below it.

## Check yourself

1. A value decreases by 7%. Which multiplier should you use?

   - 0.93 ✔

   - 1.07

   - 0.07

   - 1.70

   _Explanation:_ A 7% decrease means the item keeps 93% of its value, and $93\% = 0.93$. The common wrong answer B is the multiplier for a 7% increase, not a decrease.

2. Ravi's investment from the worked example ends at $£3973.73$. What is the total interest?

   - $$£373.73$ ✔

   - $$£3973.73$

   - $$£360.00$

   - $$£90.13$

   _Explanation:_ Total interest is the extra money earned, so subtract the starting amount: $£3973.73 - £3600 = £373.73$. The common wrong answer B is the final amount, not the interest.

3. Stretch: Sam invests £4000 for 4 years. Option A pays 3% compound interest per annum. Option B pays 3% simple interest per annum. Which statement is correct?

   - Option A gives £4502.04 and beats Option B by £22.04 ✔

   - Option B gives £4502.04 and beats Option A by £22.04

   - Both options give £4480

   - Option A gives £4480 because $3\% \times 4 = 12\%$

   _Explanation:_ Option A uses repeated multiplication, so $4000 \times 1.03^4 = 4502.04$. Option B adds £120 each year to reach £4480; the common wrong answer D treats compound interest as one 12% increase, which ignores compounding.
