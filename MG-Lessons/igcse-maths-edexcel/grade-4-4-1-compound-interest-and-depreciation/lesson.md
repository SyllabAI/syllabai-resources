# grade-4-4-1-compound-interest-and-depreciation — lesson

_Lane: `igcse-maths-edexcel` · grade 4 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## From percentages to multipliers

![Flow diagram showing a starting value multiplied each year by 1.03 for compound interest and by 0.90 for depreciation, with one path rising and the other falling](../assets/001-47178c62-0f92-4ea6-b4d1-1984e73a7ccb.jpeg)

A percentage multiplier turns a percentage change into a single number you multiply by. An increase of $r\%$ uses $1+\frac{r}{100}$, while a decrease of $r\%$ uses $1-\frac{r}{100}$.

So $5\%$ interest means multiply by $1.05$, and $12\%$ depreciation means multiply by $0.88$. Compound interest and depreciation are repeated multipliers, not repeated adding or subtracting.

## The compound interest formula

Compound interest means interest is added, and next year's interest is worked out on the new larger balance. The starting amount is called the principal, and per annum means per year.

If the annual rate is $r\%$ for $n$ years, the formula calculates the final balance after compounding. $$A = P\left(1+\frac{r}{100}\right)^n$$ Here $A$ is the final amount, $P$ is the principal, and $n$ is the number of years.

If a question asks for total interest, calculate the final amount first and then subtract the starting amount. Keep full calculator values until the final rounding to the nearest penny.

## Worked example: growing savings

Example: £2700 is invested for 4 years at 3% compound interest per annum. First, turn the 3% interest rate into the decimal multiplier $1.03$.

Substitute these values into the compound interest formula: 

$$A = 2700 \times 1.03^4$$

This calculation means we multiply the principal by the multiplier $1.03$ four times.

Using a calculator gives: 

$$A = 2700 \times 1.03^4 = 3038.873787$$

So the final amount in the account is £3038.87 to the nearest penny.

## Depreciation and repeated decreases

Depreciation means an item loses value over time. If something depreciates by 14% each year, it keeps 86% of its value, so the multiplier is $0.86$.

When the same depreciation rate repeats, use the following formula to find the total value: $$A = P\left(1-\frac{r}{100}\right)^n$$ The multiplier represents the percentage left, not the percentage lost.

If the rate changes from year to year, do not use one power. Instead, multiply the principal by each individual year's multiplier in the order given.

## Worked example: mixed percentage changes

A painting is worth £4000. Its value increases by 6% in year 1, then decreases by 10% in year 2, so the multipliers are $1.06$ and $0.90$.

Apply the first change to the starting value to find the updated value after the first year:
$$
4000 \times 1.06 = 4240
$$

Then apply the second change to the new value, not the original £4000 value. To decrease the value by 10% in the second year:
$$
4240 \times 0.90 = 3816
$$

So the painting is worth £3816 after 2 years. It is important to note that you cannot combine the changes as a simple 4% decrease because the calculations are sequential.

## Finding the number of years

Sometimes the starting amount, rate, and final amount are known, but the number of years is not. At this level, you can often test powers of the multiplier until you match the amount or pass the target.

For £4800 invested at 2% compound interest, suppose the final amount is £5299.59. To find the time $n$, we start by writing: $$4800 \times 1.02^n = 5299.59$$

Divide both sides by 4800 to isolate the power: $$1.02^n \approx 1.10408$$ This shows what power of $1.02$ you need to solve for through trial and improvement.

Now try testing powers of $1.02$ on a calculator: $$1.02^5 \approx 1.10408$$ Since this matches, we find $n=5$. For a depreciation question such as 'when will the value be less than half?', compare powers of the depreciation multiplier with $0.5$.

## Check yourself

1. An item depreciates by $18\%$ in one year. Which multiplier should you use?

   - $$0.18$

   - $$0.82$ ✔

   - $$1.18$

   - $$0.92$

   _Explanation:_ The correct multiplier is $0.82$ because $18\%$ depreciation means $82\%$ of the value is left. A common mistake is $0.18$, but that is the percentage lost, not the percentage kept.

2. Using the worked example above, what is the total interest earned after 4 years?

   - £$338.87$ ✔

   - £$3038.87$

   - £$81.00$

   - £$324.00$

   _Explanation:_ The final amount is £$3038.87$, so the interest is £$3038.87$ minus £$2700$, which is £$338.87$. A common mistake is choosing £$3038.87$, but that is the balance in the account, not the interest earned. Hint: Interest means how much extra money was gained.

3. An investor can choose between two 5-year options. Option A pays 2.5% compound interest per annum. Option B pays 2.6% simple interest per annum. Which statement is correct?

   - Option A is better, because £100 would grow to about £113.14 ✔

   - Option B is better, because 2.6 is bigger than 2.5

   - They are equal, because the rates are almost the same

   - Option B is better, because simple interest compounds faster

   _Explanation:_ Compare both options using £100. Option A gives $100 \times 1.025^{5} \approx 113.14$, while Option B gives simple interest of $2.6\% \times 5 = 13\%$, so £113.00. A common mistake is choosing Option B just because 2.6 is bigger than 2.5, but compounding over 5 years makes Option A slightly better.
