# as-statistics-2-measures-of-location-and-spread — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## What these measures tell you

A measure of location tells you where a data set is centred. Common examples are the mean, median and quartiles, and they help answer "what is a typical value?".

A measure of spread tells you how much the values vary. Common examples are the range, interquartile range and standard deviation, so a good summary usually includes one location measure and one spread measure.

For raw data, the key formulas are $$ \bar{x}=\frac{\sum x}{n}, \qquad \text{IQR}=Q_3-Q_1 $$ The mean uses every value, while the median and quartiles depend on the ordered positions in the data.

## Worked example with raw data

Twelve runners record these 400 m times in seconds: 46.3, 45.0, 45.8, 47.1, 45.6, 46.0, 45.4, 46.8, 45.9, 45.5, 46.2, 45.7. Add all 12 times and divide by 12 to get the mean: $$\bar{x}=\frac{551.3}{12}=45.941\ldots \approx 45.9$$

For the median and quartiles, order the data first. The ordered times are 45.0, 45.4, 45.5, 45.6, 45.7, 45.8, 45.9, 46.0, 46.2, 46.3, 46.8, 47.1.

There are 12 values, so the median is halfway between the 6th and 7th values. That gives $$\text{median}=\frac{45.8+45.9}{2}=45.85$$

The lower half is the first 6 values and the upper half is the last 6 values. So $$Q_1=\frac{45.5+45.6}{2}=45.55,\qquad Q_3=\frac{46.2+46.3}{2}=46.25$$

## Standard deviation from summary statistics

A standard deviation tells you how far the data typically lie from the mean. For AS questions using a whole data set or summary totals, use
$$
\text{sd}=\sqrt{\frac{\sum x^2}{n}-\bar{x}^2}
$$
where $\sum x^2$ means square each value, then add.

If $n=80$, $\sum x=3440$ and $\sum x^2=163200$, start by finding the mean. This gives
$$
\bar{x}=\frac{3440}{80}=43
$$

Now substitute into the formula and simplify inside the square root first. So
$$
\text{sd}=\sqrt{\frac{163200}{80}-43^2}=\sqrt{2040-1849}=\sqrt{191}=13.82\ldots
$$
so the standard deviation is about 13.8.

Sometimes you are given $S_{xx}$ instead of $\sum x^2$. Then use
$$
S_{xx}=\sum x^2-\frac{(\sum x)^2}{n}, \qquad \text{sd}=\sqrt{\frac{S_{xx}}{n}}
$$
This is the same spread calculation written in a more convenient form.

## Estimating mean and standard deviation from grouped data

When data are grouped into classes, the exact values are unknown. Use each class midpoint as a representative value, so the results obtained are estimates.

Consider plant heights in the classes $120<h\le130$, $130<h\le140$, $140<h\le150$, $150<h\le160$, $160<h\le180$ with frequencies 5, 12, 20, 9, 4. The midpoints are 125, 135, 145, 155, and 170.

Using these midpoints, we can calculate the sum of frequencies times values and the estimated mean: $$\sum fx=5(125)+12(135)+20(145)+9(155)+4(170)=7220,\qquad \bar{x}=\frac{7220}{50}=144.4$$

To estimate the standard deviation, square the midpoint rather than the frequency. In this example, $\sum fx^2 = 1049150$: $$\text{sd}\approx \sqrt{\frac{1049150}{50}-144.4^2}=11.47\ldots \approx 11.5$$

## Estimating the grouped median by interpolation

![Cumulative frequency graph of plant heights with the 25th value projected to the curve and down to an estimated median of 144 cm](../assets/001-be66cf19-5002-43ed-a34d-8a5357d6aa75.jpeg)
For the same plant data, the total frequency is 50, so the median is the 25th value. The cumulative frequencies are 5, 17, 37, 46, 50, so the 25th value lies in the class $140<h\le150$.

To calculate the estimate, use the formula:
$$\text{median}=L+\frac{\frac{n}{2}-c}{f}\times w$$
Here $L=140$, $c=17$, $f=20$ and $w=10$, because 17 values are below the median class and the class width is 10.

Substituting the specific values into the formula gives:
$$\text{median}=140+\frac{25-17}{20}\times 10=144$$
This is an estimate, and if the classes come from rounded data you should use the real class boundaries for the value of $L$.

## How coding changes location and spread

Coding makes awkward numbers easier to handle by applying a linear transformation. For example, if $x=\frac{t-20}{2}$, then the original variable can be recovered using the formula:
$$
t=2x+20
$$

In general, if $t=ax+b$, then location measures such as the mean, median and quartiles are multiplied by $a$ and then shifted by $b$. Spread measures such as the interquartile range and standard deviation are multiplied by $|a|$ only, because adding a constant does not change the spread of the data.

For coded data with a median of $14.2$ and a standard deviation of $8.1$, we transform each measure separately using $t = 2x + 20$:
$$
\text{median of }t=2(14.2)+20=48.4,\qquad \text{sd of }t=2(8.1)=16.2
$$

It is a common mistake to apply the constant shift to every statistic. Remember that you do not add $20$ to the standard deviation, as the width of the distribution remains unaffected by shifting the entire set of data points.

## Check yourself

1. Which pair contains one measure of location and one measure of spread?

   - mean and standard deviation ✔

   - median and lower quartile

   - range and interquartile range

   - mean and median

   _Explanation:_ Mean is a measure of location and standard deviation is a measure of spread, so A mixes centre with variation correctly. The common wrong answer B is wrong because the lower quartile is also a location measure: it marks a position in the ordered data rather than the width of the spread.

2. A survey of 70 staff gives $n=70$, $\sum x=1890$ and $S_{xx}=5670$. What is the standard deviation?

   - 9 ✔

   - 81

   - 27

   - 5670

   _Explanation:_ Use $\text{sd}=\sqrt{\frac{S_{xx}}{n}}=\sqrt{\frac{5670}{70}}=\sqrt{81}=9$. The common wrong answer 81 comes from calculating $\frac{S_{xx}}{n}$ correctly but forgetting to take the square root at the end.

3. In the interpolation calculation above, what does $c$ equal?

   - 17 ✔

   - 20

   - 25

   - 37

   _Explanation:_ $$c$ is the cumulative frequency before the median class, so $c=17$. The common wrong answer 20 is the frequency of the median class, which is $f$, not $c$.

4. A coded variable satisfies $x=\frac{t-10}{5}$. If the mean of $x$ is 6.4 and the standard deviation of $x$ is 1.8, which pair gives the mean and standard deviation of $t$?

   - 42 and 9 ✔

   - 42 and 19

   - 32 and 9

   - 6.4 and 1.8

   _Explanation:_ Rearranging gives $t=5x+10$, so the mean becomes $5(6.4)+10=42$ and the standard deviation becomes $5(1.8)=9$. The common wrong answer B adds 10 to the standard deviation, but shifting every value by 10 does not change spread. Hint: Undo the coding first, then treat location and spread separately.
