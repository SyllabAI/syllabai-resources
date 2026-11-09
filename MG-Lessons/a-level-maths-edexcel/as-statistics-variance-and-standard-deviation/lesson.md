# as-statistics-variance-and-standard-deviation — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Why spread matters

![Two horizontal dot plots labelled Set A and Set B, both centred on mean 5, with Set A at 4, 5, 6 and Set B at 1, 5, 9 to show different spread](../assets/001-2f4b484b-877e-4bc6-b5d3-58feb5077e50.jpeg)

A measure of location, such as the mean, tells you where the data is centred. A measure of spread tells you how tightly the values cluster around that centre.

The two sets in the diagram both have mean $5$, but Set B is more spread out. Standard deviation measures the typical distance of values from the mean, so a larger standard deviation means more variation.

If there are $n$ data values, the mean is

$$\bar{x}=\frac{\sum x}{n}$$

We use this mean as the centre when discussing spread.

## Deviation, variance, and standard deviation

A deviation tells you how far a value is from the mean, so for a value $x$ it is $x-\bar{x}$. If you add all the deviations, they cancel to zero, so we square them instead. Variance is the mean of the squared deviations, so it uses squared units. Standard deviation is the square root of the variance, so it is back in the original units.

$$$s^2=\frac{\sum (x-\bar{x})^2}{n},\qquad s=\sqrt{\frac{\sum (x-\bar{x})^2}{n}}$$

In AS questions, the shortcut formula below is usually faster. Remember that this gives the variance first, so you must square root to get $s$.

$$$s^2=\frac{\sum x^2}{n}-\bar{x}^2$$

## Worked example: raw data setup

The six race times are $45.2$, $46.8$, $46.0$, $46.3$, $45.5$, and $45.0$ seconds. For raw data, start by finding $n$, $\sum x$, and $\sum x^2$.

Here the totals are shown below. These are the key calculator values to write down. $$n=6,\qquad \sum x=274.8,\qquad \sum x^2=12588.22$$

Now find the mean so you know the centre of the data. This will be used again in the variance formula. $$\bar{x}=\frac{274.8}{6}=45.8$$

## Worked example: raw data finish

Substitute the totals into the shortcut formula to get the variance. This is quicker than working from every deviation one by one.

$$$s^2=\frac{12588.22}{6}-45.8^2=0.396666\ldots$$

Now square root the variance to get the standard deviation. Quote the answer to 3 significant figures.

$$$s=\sqrt{0.396666\ldots}=0.6298\ldots \approx 0.630$$ So the standard deviation is $0.630$ seconds. If you stopped at $0.396666\ldots$, you would only have the variance.

## Grouped data: estimate using midpoints

When data is grouped into class intervals, the exact values are missing. We estimate each class by its midpoint and combine it with the frequency. Because midpoints replace the original values, the answers are estimates.

$$$\bar{x}=\frac{\sum fx}{\sum f},\qquad s^2=\frac{\sum fx^2}{\sum f}-\bar{x}^2$$

For the plant heights, $\sum f=50$, $\sum fx=7360$, and $\sum fx^2=1091100$. Applying the midpoints to the formula gives the following results: $$\bar{x}=\frac{7360}{50}=147.2,\qquad s=\sqrt{\frac{1091100}{50}-147.2^2}=12.4$$

The estimated standard deviation is 12.4 cm. For a class such as $160 < h \leq 180$, remember that the midpoint is $170$, rather than the boundaries $160$ or $180$.

## Coding: what changes and what stays the same

Coding makes awkward numbers easier to handle. If $T=a+bX$, then the mean and median of $T$ are found by applying the same transformation.

Spread only reacts to the scale factor. The shift $a$ does not change spread, but the standard deviation is multiplied by $|b|$ and the variance by $b^2$.

$$$s_T=|b|s_X$$

For example, if $x=\frac{t-12}{3}$, then $t=3x+12$. So a coded standard deviation of $7.81$ becomes $s_t=3\times 7.81=23.4$, and you do not add 12 to the standard deviation.

## Check yourself

1. Two data sets both have mean $12$. Set A is $11, 12, 13$ and Set B is $6, 12, 18$. Which statement is correct?

   - Set A has the larger standard deviation

   - Set B has the larger standard deviation ✔

   - The standard deviations are equal because the means are equal

   - Standard deviation cannot be compared without the median

   _Explanation:_ Set B is correct because its values are further from the mean $12$, so the deviations and squared deviations are larger. The common wrong answer is C, but having the same mean only tells you the centre, not the spread.

2. In the class $160 < h \leq 180$, which value should be used as $x$ in the grouped-data formula?

   - 160

   - 170 ✔

   - 180

   - 20

   _Explanation:_ 170 is correct because the midpoint is halfway between 160 and 180. The common wrong answer is A, but 160 is just the lower class boundary, not a representative value for the whole class.

3. Stretch: If $Y=4-2X$ and the variance of $X$ is $9$, what is the variance of $Y$?

   - 18

   - 9

   - 36 ✔

   - 13

   _Explanation:_ 36 is correct because multiplying by -2 multiplies the variance by $(-2)^2=4$, and the +4 shift does not change spread. The common wrong answer is A because it multiplies by 2 instead of squaring the scale factor.
