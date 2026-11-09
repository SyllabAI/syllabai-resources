# as-statistics-box-plots — lesson

_Lane: `a-level-maths-edexcel` · grade — · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## What a box plot shows

![Annotated horizontal box plot showing outliers, whiskers, quartiles, and median](../assets/001-0d8065e7-91ec-4d71-a9f8-7f794e35745c.jpeg)
A box plot summarises a data set on a number line using the lower quartile $Q_1$, the median, the upper quartile $Q_3$, and the whiskers. The whiskers reach the smallest and largest non-outlier values, while any outliers are plotted separately as crosses.

The box from $Q_1$ to $Q_3$ contains the middle 50% of the data. Roughly 25% of the values lie in each section: below $Q_1$, between $Q_1$ and the median, between the median and $Q_3$, and above $Q_3$.

## Finding the median and quartiles

Always put raw data in ascending order before doing anything else. For the weekly call times 18, 22, 34, 37, 50, 52, 53, 56, 61, 78, 112, the values are already ordered.

There are 11 values, so the median is the 6th value, which is 52. Because 11 is odd, this middle value is not included again when finding the quartiles.

The lower half is 18, 22, 34, 37, 50, so $Q_1 = 34$. The upper half is 53, 56, 61, 78, 112, so $Q_3 = 61$.

## IQR and outlier fences

The interquartile range measures the spread of the middle 50% of the data. This range is calculated using the first and third quartiles:
$$\text{IQR} = Q_3 - Q_1$$

For the call-time data, $\text{IQR} = 61 - 34 = 27$. To test for outliers, we calculate boundaries known as fences.

$$$\text{lower fence} = Q_1 - 1.5 \times \text{IQR}$$
$$\text{upper fence} = Q_3 + 1.5 \times \text{IQR}$$
Here $1.5 \times 27 = 40.5$, so the calculated fences are $-6.5$ and $101.5$.

A value is an outlier only if it is smaller than the lower fence or greater than the upper fence; a value exactly on a fence is not an outlier. Therefore 112 is an outlier, while 78 is still a non-outlier and stays at the end of the whisker.

## Drawing the box plot

![Worked example horizontal box plot for the call-time data with box from 34 to 61, median 52, whiskers at 18 and 78, and an outlier cross at 112](../assets/002-07ac90d9-0ab0-4f40-93a8-a0d61064ed05.jpeg)

For the call-time data, draw the box from $Q_1 = 34$ to $Q_3 = 61$ and place the median line at 52. The lower whisker goes to 18 because 18 is the smallest non-outlier value.

The value 112 is not used as the end of the whisker because it is an outlier. The upper whisker stops at 78, which is the largest non-outlier value.

Choose a scale that includes every important value, such as 0 to 120 with equal intervals. Consistent spacing matters just as much as the correct quartiles.

## Reading and comparing box plots

When a question asks for the value by which 75% have finished, it is asking for $Q_3$. For example, if a puzzle-time box plot has $Q_3 = 18$ minutes, then 75% finished by 18 minutes.

When comparing two box plots, use the medians for typical value and the IQRs for consistency. If Group A has median 13 and $Q_1 = 10$, $Q_3 = 18$, then its IQR is $18 - 10 = 8$.

If Group B has median 15 and $Q_1 = 12$, $Q_3 = 17$, then its IQR is $17 - 12 = 5$. Group A is typically faster because its median is lower, but Group B is more consistent because its IQR is smaller. If Group A also has outliers, mention them as unusually slow times in context.

## Check yourself

1. On a box plot, which value is the point by which 75% of the data lie at or below?

   - $$Q_1$

   - the median

   - $$Q_3$ ✔

   - the maximum value

   _Explanation:_ $$Q_3$ is the upper quartile, so 75% of the data are at or below it. The most common wrong answer is the median, but the median only marks 50% of the data.

2. If $Q_1 = 20$ and $Q_3 = 44$, which value is an outlier?

   - 80

   - 81 ✔

   - 68

   - -16

   _Explanation:_ The IQR is $44 - 20 = 24$, so the fences are $20 - 1.5 \times 24 = -16$ and $44 + 1.5 \times 24 = 80$. A value must be greater than 80 or smaller than -16 to be an outlier, so 81 is the only outlier; 80 is the common wrong answer because it is on the fence, not beyond it.

3. Stretch: Group A has median $13$, IQR $8$, and outliers at $28$ and $29$ minutes. Group B has median $15$, IQR $5$, and no outliers. Which is the best comparison?

   - Group A is typically faster, but Group B is more consistent ✔

   - Group B is typically faster because its IQR is smaller

   - Group A is more consistent because its median is lower

   - The groups have the same spread because both have box plots

   _Explanation:_ The median compares typical value, so Group A is faster because $13$ is lower than $15$. A smaller IQR shows greater consistency, not a faster typical time.
