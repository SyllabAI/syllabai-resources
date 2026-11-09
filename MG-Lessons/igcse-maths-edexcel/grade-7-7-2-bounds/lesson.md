# grade-7-7-2-bounds — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What bounds mean

![Number line with 20.5 as a filled endpoint and 21.5 as an open endpoint for 21 cm to the nearest cm](../assets/001-0860621e-812f-4cd8-9d48-f3f94c13af21.jpeg)

A rounded measurement is not exact. If a length is given as 21 cm to the nearest cm, the true value lies in a continuous interval of possible values.

The lower bound is the smallest possible value, and the upper bound is the boundary at the top of the interval. For this example, we write $20.5 \le x < 21.5$.

The symbol $<$ is used at the top because 21.5 would round to 22, not 21. In bounds questions, write the interval first and then use it in the calculation.

## The half-unit rule

To find bounds, take half of the rounding unit.

Then subtract that half-unit to get the lower bound and add it to get the upper bound. Rounding to the nearest cm gives a half-unit of 0.5 cm, rounding to the nearest 5 m gives 2.5 m, and rounding to 2 decimal places gives 0.005.

Example: if a length is 130 m to the nearest 5 m, the half-unit is 2.5 m. Then $130 - 2.5 = 127.5$ and $130 + 2.5 = 132.5$. So the actual length is from 127.5 m up to but not including 132.5 m.

For significant figures, first find the place value of the last significant digit. If 3680 is correct to 3 significant figures, the last significant digit is in the tens place, so it was rounded to the nearest 10 and the half-unit is 5. Then $3680 - 5 = 3675$ and $3680 + 5 = 3685$. So the actual value is from 3675 up to but not including 3685.

## Bounds in perimeter and area

For positive lengths, making a measurement bigger makes perimeter, area, and circumference bigger. So upper bound questions use bigger lengths, and lower bound questions use smaller lengths.

A rectangle has length 38 cm to the nearest cm and width 7.4 cm to the nearest mm. Therefore $37.5 \le L < 38.5$ and $7.35 \le W < 7.45$ because nearest mm is nearest 0.1 cm.

The upper bound of the perimeter uses both upper values because perimeter is found by adding positive lengths. $$P_{\text{upper}} = 2(38.5 + 7.45) = 91.9$$ So the upper bound of the perimeter is 91.9 cm.

The lower bound of the area uses both lower values because we want the smallest possible product. $$A_{\text{lower}} = 37.5 \times 7.35 = 275.625$$ So the lower bound of the area is 275.625 $\text{cm}^2$.

## Products and quotients

For a product of positive quantities, the largest answer uses upper bounds and the smallest uses lower bounds. For a fraction, the denominator works the opposite way because a smaller denominator makes the quotient larger.

So for $v = \frac{s}{t}$, the upper bound uses the upper bound of $s$ and the lower bound of $t$. With $s = 5.42$ and $t = 1.37$ correct to 2 decimal places, the intervals are $5.415 \le s < 5.425$ and $1.365 \le t < 1.375$.

Now substitute the values that make the fraction as large as possible. $$v_{\text{upper}} = \frac{5.425}{1.365} = 3.974358\dots$$ So the upper bound is 3.974 to 3 decimal places.

## Pythagoras and subtraction

![Right-angled triangle labelled a, b, and c with a note that the lower bound of b uses lower c and upper a](../assets/002-322199bd-6155-4c48-ae1f-64fe589670fb.jpeg)

For positive lengths, squaring and square-rooting keep the order the same. The key change comes from the subtraction inside the formula $b = \sqrt{c^2 - a^2}$.

Suppose $a = 3.8$ cm to the nearest mm and $c = 9$ cm to the nearest cm. This results in the bounds $3.75 \le a < 3.85$ and $8.5 \le c < 9.5$. To find the lower bound of $b$, use the smallest hypotenuse and the largest value of $a$ because $a^2$ is being subtracted.

$$$
b_{\text{lower}} = \sqrt{8.5^2 - 3.85^2} = \sqrt{57.4275} = 7.577\ldots
$$

The result $7.577\ldots$ means the lower bound of $b$ is 7.6 cm when rounded to 1 decimal place.

## Choosing a suitable degree of accuracy

A suitable degree of accuracy is a rounding level for which every possible value gives the same rounded answer. To test this, calculate the lower and upper possible answers first.

If $p = \frac{F}{A}$, with $F = 31.42$ correct to 2 decimal places and $A = 5.18$ correct to 3 significant figures, then $31.415 \le F < 31.425$ and $5.175 \le A < 5.185$. The lower bound of $p$ uses lower $F$ and upper $A$, while the upper bound uses upper $F$ and lower $A$.

This gives $$p_{\text{lower}} = \frac{31.415}{5.185} = 6.0588\ldots$$ $$p_{\text{upper}} = \frac{31.425}{5.175} = 6.0724\ldots$$ To 2 decimal places these round differently, but to 2 significant figures both round to 6.1.

## Check yourself

1. A rod has length 21 cm to the nearest cm. Which interval is correct for its true length $x$?

   - $$20.5 \le x < 21.5$ ✔

   - $$20 < x < 22$

   - $$20.5 < x \le 21.5$

   - $$21 \le x < 22$

   _Explanation:_ $$21$ to the nearest cm means the rounding unit is 1, so the half-unit is 0.5 and the interval is $20.5 \le x < 21.5$. The most common wrong answer is C because students reverse the inclusive and exclusive ends, but 20.5 does round to 21 so it must be included, while 21.5 rounds to 22 so it must be excluded.

2. A rectangle has length 12 cm to the nearest cm and width 4.6 cm to the nearest mm. Which calculation gives the upper bound for its perimeter?

   - $$2(12.5 + 4.65)$ ✔

   - $$2(11.5 + 4.55)$

   - $$2(12.5 + 4.55)$

   - $$2(11.5 + 4.65)$

   _Explanation:_ Perimeter gets larger when either side gets larger, so the upper bound must use both upper bounds, giving $2(12.5 + 4.65)$. The most common wrong answer is C because students use the correct upper length but forget that the width must also be as large as possible.

3. A value is known to lie between $6.0588$ and $6.0724$. What is the greatest suitable degree of accuracy?

   - 3 decimal places

   - 2 decimal places

   - 2 significant figures ✔

   - 3 significant figures

   _Explanation:_ 2 significant figures is correct because both endpoints round to $6.1$, so every possible value in the interval gives the same answer. The most common wrong answer is 2 decimal places, but the endpoints round to $6.06$ and $6.07$, so that accuracy is not safe. Hint: Round both endpoints at each proposed accuracy.
