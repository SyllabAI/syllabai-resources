# grade-6-6-12-box-plots — lesson

_Lane: `gcse-maths-edexcel` · grade 6 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What a box plot shows

![Labeled box plot on a number line with minimum 8, lower quartile 18, median 27, upper quartile 39, maximum 52, and brackets showing range 44 and IQR 21](../assets/001-308b52a0-972c-48ac-8ea5-c6c5be5e1d47.jpeg)

A distribution is the way a set of data values is spread out. A box plot is a quick way to show that spread on a number line. It uses the five-number summary: minimum, lower quartile $Q_1$, median, upper quartile $Q_3$, and maximum.

The whiskers run from the box to the minimum and maximum. The box goes from $Q_1$ to $Q_3$, and the line inside the box marks the median.

To measure spread, use $\text{range} = \text{maximum} - \text{minimum}$ and $\text{IQR} = Q_3 - Q_1$. The IQR describes the middle 50% of the data, so it is often more useful than the range when comparing box plots.

## Sketching from the five-number summary

If the five values are given, first choose a sensible scale that includes them all. For plant heights with minimum 10 cm, $Q_1=26$ cm, median 34 cm, $Q_3=41$ cm, and maximum 54 cm, a scale from 0 cm to 60 cm works well.

Mark 10, 26, 34, 41, and 54 on the scale in that order. The order must always be minimum, $Q_1$, median, $Q_3$, maximum.

Draw the box from 26 to 41. Then draw a vertical line inside the box at 34 for the median.

Finally, draw whiskers from 26 back to 10 and from 41 up to 54. You now have the full box plot. A good exam habit is to write the five values above the scale before you draw.

## Find the missing value first

Sometimes one of the five values is missing, but the table gives the range or IQR instead. Do not start drawing yet; use the formula backwards first.

Example 1: the range is 96 g and the maximum is 183 g, so the minimum is $183-96=87$ g. The five values are then 87, 109, 132, 160, and 183.

Example 2: the IQR is 8 minutes and $Q_3=23$ minutes, so $Q_1=23-8=15$ minutes. After that, draw the box plot using 12, 15, 18, 23, and 29.

## From raw data to a box plot

When you start with raw data, put it in order first. For the ordered times 51, 53, 55, 55, 57, 58, 59, 61, 62, 63, 65, 66, 69, 71, 74, there are 15 values.

With 15 values, the median is the 8th value, so the median is 61. For an odd number of values, do not include this median again when finding the quartiles.

The lower half is 51, 53, 55, 55, 57, 58, 59, so $Q_1=55$. The upper half is 62, 63, 65, 66, 69, 71, 74, so $Q_3=66$.

The minimum is 51 and the maximum is 74. The five-number summary is therefore 51, 55, 61, 66, 74.

## Comparing two box plots

Comparison questions need two clear comments: one about the median and one about spread. The median tells you the typical value, and the IQR tells you how spread out the middle 50% is.

Suppose Class A has $Q_1=16$, median 21, and $Q_3=32$, while Class B has $Q_1=18$, median 24, and $Q_3=30$. Class B has the higher median, so Class B generally scored higher.

Now compare the IQRs: Class A has $32-16=16$ and Class B has $30-18=12$. Class B has the smaller IQR, so its scores were more consistent.

Always use the context. For scores, a higher median is better, but for times a lower median is better.

## From cumulative frequency to a box plot

![Cumulative frequency graph for 60 oranges with dashed lines from 15, 30, and 45 on the cumulative frequency axis to the curve and down to weights 123 g, 130 g, and 137 g](../assets/002-ae522347-8dc6-48ff-940e-7875aa0e5eb9.jpeg)
A cumulative frequency graph can also give the five-number summary for a box plot. Start with the total frequency $N$, then use $N/4$, $N/2$, and $3N/4$ to find the quartile positions on the cumulative frequency axis.

For 60 oranges, the quartile positions are $60/4=15$, $60/2=30$, and $3 \times 60 / 4 = 45$. Read across from 15, 30, and 45 to the curve, then down to the weight axis.

This gives about $Q_1=123$ g, median 130 g, and $Q_3=137$ g, with minimum 114 g and maximum 150 g. Those five values are enough to sketch the box plot. Do not start on the weight axis; quartile positions live on the cumulative frequency axis.

## Check yourself

1. A box plot has minimum 8, $Q_1=18$, median 27, $Q_3=39$, and maximum 52. What is the IQR?

   - 21 ✔

   - 44

   - 31

   - 12

   _Explanation:_ The IQR is $Q_3-Q_1=39-18=21$. A common wrong answer is 44, but that is the range because it uses maximum minus minimum instead.

2. The ordered data are 4, 7, 9, 12, 15, 18, 20, 22, 25, 29, 31. What is $Q_1$?

   - 9 ✔

   - 10.5

   - 12

   - 18

   _Explanation:_ There are 11 values, so the median is 18 and is not included again. The lower half is 4, 7, 9, 12, 15, whose middle value is 9. A common wrong answer is 10.5, which comes from incorrectly including the median 18 in the lower half.

3. Two box plots show delivery times. Company P has median $38$ minutes and IQR $12$ minutes. Company Q has median $34$ minutes and IQR $18$ minutes. Which statement is correct?

   - Company P is usually quicker and more consistent.

   - Company Q is usually quicker but less consistent ✔

   - Company Q is usually slower but more consistent.

   - Both companies are equally quick because the ranges are not given.

   _Explanation:_ Company Q has the lower median, so its typical delivery time is shorter, but its IQR is larger, so its times are less consistent. A common wrong answer is A because it notices Company P has the smaller IQR but forgets that for times, a lower median means quicker. Hint: For times, smaller is better.
