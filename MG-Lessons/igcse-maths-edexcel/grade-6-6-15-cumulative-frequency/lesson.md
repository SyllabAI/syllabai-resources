# grade-6-6-15-cumulative-frequency — lesson

_Lane: `igcse-maths-edexcel` · grade 6 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Upper bounds and running totals

Grouped data is split into class intervals such as $10 < t \le 20$. The upper bound is the right-hand end of the interval, so this class has upper bound 20.

Cumulative frequency is a running total of the frequencies as you move down the table. It tells you how many values are up to and including each upper bound.

On a cumulative frequency graph, plot upper bounds on the horizontal axis and cumulative frequency on the vertical axis. If classes are written as 10-19 or 20-29, first convert to class boundaries such as 9.5, 19.5, and 29.5.

## Worked example: building a cumulative frequency table

Suppose the intervals $0 < t \le 10$, $10 < t \le 20$, $20 < t \le 30$, $30 < t \le 40$ and $40 < t \le 50$ have frequencies 8, 16, 23, 18 and 7. Start the running total with the first class, so the first cumulative frequency is 8.

Keep adding the next frequency to the running total. That gives $8+16=24$, then $24+23=47$, then $47+18=65$, and finally $65+7=72$. The finished cumulative frequency row is shown below.

$$$8,\ 24,\ 47,\ 65,\ 72$$

So the cumulative frequencies are 8, 24, 47, 65 and 72, and the total number of values is 72.

## Drawing the cumulative frequency graph

![Cumulative frequency graph with time on the horizontal axis, cumulative frequency on the vertical axis, plotted upper-bound points, a smooth increasing curve, and guide lines for quartiles](../assets/001-336067a8-d560-4095-a0dc-31c1f2fc34fe.jpeg)

A cumulative frequency graph uses each upper bound as the $x$-value and the cumulative frequency as the $y$-value. For the table above, plot $(10, 8)$, $(20, 24)$, $(30, 47)$, $(40, 65)$ and $(50, 72)$.

Also plot the starting point $(0, 0)$ because before the first class, no data have been counted. Join the points with a smooth increasing curve, not separate bars or a zigzag line.

## Reading the median and quartiles

Read quartiles from the cumulative frequency axis first, not straight from the data axis. If the total frequency is 72, then read $Q_1$ at $72/4 = 18$, the median at $72/2 = 36$, and $Q_3$ at $3 \times 72 / 4 = 54$.

From each of these cumulative frequencies, move horizontally to the curve and then vertically down to the time axis. On the example graph, this gives about $Q_1 \approx 16$, median $\approx 25$, and $Q_3 \approx 34$ seconds.

These are estimates, so small differences are normal if the curve is hand drawn. Use a ruler for the guide lines and give a sensible value from your graph.

## More than, between, and interquartile range

Cumulative frequency gives the number of values less than or equal to a chosen value. If the graph shows a cumulative frequency of 65 at 40 seconds and the total frequency is 72, then the number taking more than 40 seconds is $72 - 65 = 7$.

To find how many values lie between two numbers, subtract the two cumulative frequencies. For example, if the graph shows 24 at 20 seconds and 65 at 40 seconds, then about $65 - 24 = 41$ values are between 20 and 40 seconds.

Once you have read $Q_1$ and $Q_3$ from the graph, the interquartile range measures the spread of the middle 50% of the data. It is calculated using the formula below and is less affected by extreme values than the full range:

$$\text{IQR} = Q_3 - Q_1$$

## From cumulative frequency to box plots

![Box plot on a horizontal scale with minimum 5, lower quartile 16, median 25, upper quartile 34, maximum 50, and the interquartile range marked](../assets/002-74213ac6-9a9f-418b-bdf0-7da9b0fb2fc2.jpeg)

A box plot summarises a data set using the minimum, $Q_1$, median, $Q_3$ and maximum. The box runs from $Q_1$ to $Q_3$, and the line inside the box marks the median.

If your cumulative frequency graph gives estimates such as $Q_1 = 16$, median $= 25$ and $Q_3 = 34$, you can combine these with the minimum and maximum to draw the box plot. The length of the box is the interquartile range, so a shorter box means the middle 50% is less spread out.

When comparing two box plots, mention both average and spread. A higher median means a higher typical value, while a smaller IQR means more consistency.

## Check yourself

1. For the class interval $10 < t \le 20$, which x-value should be plotted on a cumulative frequency graph?

   - 10

   - 15

   - 20 ✔

   - 30

   _Explanation:_ The correct x-value is 20 because cumulative frequency graphs use the upper bound of each class. A common wrong answer is 15, but 15 is the midpoint of the class, not the upper bound.

2. Why can a cumulative frequency graph never go downward?

   - Because upper bounds are always the midpoint of a class

   - Because the running total cannot decrease ✔

   - Because every class has frequency 1

   - Because the graph must be a straight line

   _Explanation:_ Each new cumulative frequency is the previous total plus the next frequency, so it stays the same or increases. A common wrong answer is D, but the curve does not have to be straight; it just has to be non-decreasing.

3. A cumulative frequency graph has total frequency 72. At 40 seconds, the cumulative frequency is 65. How many values are greater than 40 seconds?

   - 7 ✔

   - 65

   - 32

   - 72

   _Explanation:_ The graph gives 65 values at or below 40 seconds, so the number above 40 is $72 - 65 = 7$. The common wrong answer is 65, but that is the number up to 40 seconds, not greater than 40 seconds.

4. Class A has median 62 and IQR 18. Class B has median 70 and IQR 10. Which statement is correct?

   - Class A scored higher overall and was more consistent

   - Class B scored higher overall and was more consistent ✔

   - Class B scored lower overall but was more consistent

   - Both classes had the same spread because both have medians

   _Explanation:_ Class B has the higher median, so its typical score is higher, and Class B has the smaller IQR, so its middle $50\%$ is more consistent. A common wrong answer is A, but a larger IQR means more spread, not better performance.
