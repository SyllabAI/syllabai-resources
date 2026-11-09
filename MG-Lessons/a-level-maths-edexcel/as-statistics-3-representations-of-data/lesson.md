# as-statistics-3-representations-of-data — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Grouped data and true class widths

Data are often grouped into class intervals, and the frequency tells you how many observations lie in each class. When the variable is continuous and values have been rounded, the written class labels are not the exact boundaries.

If data are measured to the nearest whole number, move half a unit either side to get the true class boundaries. So the class 10-14 really runs from $9.5$ to $14.5$, giving class width $14.5 - 9.5 = 5$.

A common mistake is to subtract the labels instead of the boundaries. For example, the class 14-20 has width $20.5 - 13.5 = 7$, not $6$.

## Histograms use area

![Histogram with a tall narrow bar and a short wide bar labelled with equal areas to show equal frequency](../assets/001-a1b570ed-b6f9-40e3-9329-8adca2735a06.jpeg)
A histogram is used for grouped continuous data. Because class widths can be different, the important quantity is bar area, not just height.

The vertical axis shows frequency density, where
$$\text{frequency density} = \frac{\text{frequency}}{\text{class width}}$$

Rearranging this formula allows us to calculate frequency using the area of each bar:
$$\text{frequency} = \text{class width} \times \text{frequency density}$$

So width matters every time you compare bars. A tall narrow bar and a short wide bar can show the same frequency if their areas are equal. This area-based logic is also used when estimating probabilities or percentages from a histogram.

## Worked example with separate scales

Suppose the class 9-13 has frequency $12$ and is drawn $2 \, \text{cm}$ wide and $3 \, \text{cm}$ high. We want to determine the dimensions of the bar for the class 14-20, which has a frequency of $21$.

First, use true boundaries to calculate width. The class 9-13 has a width of $13.5 - 8.5 = 5$. Since it is drawn $2 \, \text{cm}$ wide, the horizontal scale is $\frac{2}{5} = 0.4 \, \text{cm per unit}$.

The class 14-20 has a width of $20.5 - 13.5 = 7$, so its drawn width is $7 \times 0.4 = 2.8 \, \text{cm}$. For the height, the first bar has a frequency density of $\frac{12}{5} = 2.4$. A density of $2.4$ is drawn as $3 \, \text{cm}$, meaning the vertical scale is $\frac{3}{2.4} = 1.25 \, \text{cm per density unit}$.

Now find the second bar's density: $\frac{21}{7} = 3$. Its drawn height is $3 \times 1.25 = 3.75 \, \text{cm}$. It is crucial to calculate horizontal and vertical scales separately to ensure the area remains proportional to frequency.

## Box plots, quartiles and outliers

![Annotated box plot with minimum 8, Q1 15, median 22, Q3 29, whisker to 33 and outlier at 56](../assets/002-80f7dc7a-94ac-44d8-8e8c-5ca7651d12eb.jpeg)
A box plot summarises a distribution using the minimum, $Q_1$, median, $Q_3$ and maximum or largest non-outlier. The box runs from $Q_1$ to $Q_3$, so it contains the middle $50\%$ of the data.

$$$\text{IQR} = Q_3 - Q_1$$

The interquartile range measures spread in the middle half of the data. When there is an odd number of values, do not include the median in both halves when finding $Q_1$ and $Q_3$.

To test for outliers, use the fences $Q_1 - 1.5 \times \text{IQR}$ and $Q_3 + 1.5 \times \text{IQR}$. Whiskers stop at the smallest and largest values that are not outliers, and any outliers are plotted separately.

## Worked example from ordered data

Consider the ordered data $8, 12, 15, 18, 20, 22, 24, 25, 29, 33, 56$. There are $11$ values, so the median is the 6th value, which is $22$.

The lower half is $8, 12, 15, 18, 20$, so $Q_1 = 15$. The upper half is $24, 25, 29, 33, 56$, so $Q_3 = 29$ and the IQR is $29 - 15 = 14$.

The lower fence is $15 - 1.5 \times 14 = -6$, and the upper fence is $29 + 1.5 \times 14 = 50$. Since $56 > 50$, the value $56$ is an outlier.

The whiskers do not go to the outlier. They go to the smallest and largest non-outliers, which are $8$ and $33$, and the outlier is shown separately as a cross.

## Choosing the right summary statistics

If a distribution is roughly symmetrical and has no major outliers, the mean and standard deviation are useful summaries. For summary data, you may use:

$$$\bar{x} = \frac{\sum x}{n}$$
and
$$s = \sqrt{\frac{\sum x^2}{n} - \bar{x}^2}$$

These measures use all the data values, so they respond to changes across the whole distribution. That is helpful when the shape is fairly regular.

If the data are skewed or contain outliers, the median and IQR are usually better. They are resistant measures, so extreme values have much less effect.

## Check yourself

1. A variable is measured to the nearest whole number. What is the true class width of 14-20?

   - 6

   - 7 ✔

   - 6.5

   - 5

   _Explanation:_ The true boundaries are $13.5$ and $20.5$, so the width is $20.5 - 13.5 = 7$. The most common wrong answer is $6$, which comes from subtracting the class labels and ignoring the half-unit boundaries.

2. A class 9-13 has frequency $12$ and is drawn $2$ cm wide and $3$ cm high. What should the height of the bar for class 14-20 with frequency $21$ be?

   - $$2.8$ cm

   - $$3.75$ cm ✔

   - $$4.2$ cm

   - $$5.25$ cm

   _Explanation:_ The first class has true width $5$, so its density is $\frac{12}{5} = 2.4$. A density of $2.4$ is drawn as $3$ cm, so the vertical scale is $1.25$ cm per density unit; the second class has width $7$, density $\frac{21}{7} = 3$, and height $3 \times 1.25 = 3.75$ cm. The most common wrong answer is $2.8$ cm, which is the correct width of the bar, not its height.

3. Group A has median $13$, IQR $6$, and high outliers at $25$ and $27$. Group B has median $14$, IQR $6$, and no outliers. Which statement best compares them?

   - Group A is typically faster, but it has some unusually long times ✔

   - Group B is faster because its maximum is lower

   - The groups have the same typical time because their IQRs are equal

   - Group A is more consistent because its median is lower

   _Explanation:_ Group A has the lower median, so its typical time is lower and therefore faster. Both groups have the same IQR, so their middle $50\%$ have similar spread, but only Group A has high outliers. The most common wrong answer is C, which confuses spread with centre: equal IQR does not mean equal typical value.

4. A box plot of journey times is strongly right-skewed and shows two large high outliers. Which pair of summary statistics is most suitable?

   - Mean and standard deviation

   - Median and interquartile range ✔

   - Mean and range

   - Mode and standard deviation

   _Explanation:_ The median and IQR are less affected by skewness and extreme values, so they describe the typical journey time and spread more reliably here. The most common wrong answer is mean and standard deviation, but both can be pulled upward by the large outliers.
