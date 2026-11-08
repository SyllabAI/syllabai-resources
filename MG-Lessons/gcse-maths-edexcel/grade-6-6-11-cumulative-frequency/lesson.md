# grade-6-6-11-cumulative-frequency — lesson

_Lane: `gcse-maths-edexcel` · grade 6 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## What cumulative frequency means

Frequency tells you how many values are in one class interval, such as $5 < t \le 10$. Cumulative frequency is the running total as you move through the classes from smallest to largest.

If the frequencies are $7$, $11$ and $13$, the cumulative frequencies are $7$, $18$ and $31$. A quick check is that the final cumulative frequency should equal the total number of data values.

## Worked example: making a cumulative frequency table

Suppose 42 people have times in seconds with class frequencies $7$, $11$, $13$, $8$ and $3$ for the intervals $0 < t \le 5$, $5 < t \le 10$, $10 < t \le 15$, $15 < t \le 20$ and $20 < t \le 25$. Start the cumulative frequency with the first frequency, so the first total is $7$.

Keep adding each new frequency to the total so far. Each value includes all the classes before it.
$$
7,\quad 7+11=18,\quad 18+13=31,\quad 31+8=39,\quad 39+3=42
$$

So the cumulative frequencies are up to $5$: $7$, up to $10$: $18$, up to $15$: $31$, up to $20$: $39$, and up to $25$: $42$. The last value is $42$, which matches the total number of people, so the additions are consistent.

## Plotting a cumulative frequency graph

![Cumulative frequency graph of time in seconds for 42 people with points at 0,0; 5,7; 10,18; 15,31; 20,39; 25,42 and a smooth increasing curve](../assets/001-17f96729-2465-4d22-9889-5b4326b33f02.jpeg)

To draw a cumulative frequency graph, put the variable on the horizontal axis and cumulative frequency on the vertical axis. Plot each upper boundary against its cumulative frequency, not the midpoint of the class.

Also include the starting point at the lowest boundary with cumulative frequency 0. For the example table, the plotted points are $(0,0)$, $(5,7)$, $(10,18)$, $(15,31)$, $(20,39)$ and $(25,42)$.

Join the points with a smooth increasing curve. The graph cannot go down because cumulative frequency never decreases.

## Estimating the median and quartiles

![Cumulative frequency graph for 60 batteries with dashed guide lines from 15, 30 and 45 on the cumulative frequency axis to estimates 22, 31 and 41 on the lifetime axis](../assets/002-4e4252fe-767e-493d-a60c-ffd25a01331e.jpeg)

If the total frequency is $N$, read the lower quartile at $N/4$, the median at $N/2$ and the upper quartile at $3N/4$. Start on the cumulative frequency axis at these values, move across to the curve, then drop down to the horizontal axis.

For $N=60$, the positions are $$Q_1: \frac{60}{4}=15,\qquad \text{median}: \frac{60}{2}=30,\qquad Q_3: \frac{3\times 60}{4}=45$$ These are positions in the data, not values on the horizontal axis yet.

From the graph, you might estimate $22$, $31$ and $41$ minutes for $Q_1$, the median and $Q_3$. Then the interquartile range is $$\text{IQR}=41-22=19$$ Because the data is grouped and the curve is drawn, these readings are estimates.

## From cumulative frequency to box plots

A box plot uses five values: minimum, $Q_1$, median, $Q_3$ and maximum. Once you have estimated these from a cumulative frequency graph, you can plot them on a number line.

For example, if the five-number summary is $4$, $10$, $14$, $21$, $30$, draw a box from 10 to 21. Draw a median line at 14, and remember it does not have to sit in the middle of the box. Then draw whiskers from 4 to 10 and from 21 to 30.

When comparing two box plots, a higher median means a higher typical value. A smaller IQR means the middle 50% is less spread out, so the data is more consistent.

## Check yourself

1. Which statement best describes cumulative frequency?

   - The running total of the frequencies ✔

   - The number in one class interval

   - The middle value of a class interval

   - The width of a class interval

   _Explanation:_ Cumulative frequency is a running total, so A is correct. The most common wrong answer is B, but that is just the ordinary frequency for one class, not the total built up so far.

2. For the example above, which point should not be plotted?

   - $$(10,18)$

   - $$(12.5,18)$ ✔

   - $$(25,42)$

   - $$(0,0)$

   _Explanation:_ B is correct because $12.5$ is the midpoint of the class $10 < t \le 15$, and cumulative frequency graphs use upper boundaries instead. A common wrong answer is D, but $(0,0)$ should be included as the starting point at the lowest boundary.

3. Class A has median $46$ and IQR $18$. Class B has median $52$ and IQR $9$. Which comparison is correct?

   - Class B generally scored higher and was more consistent ✔

   - Class A generally scored higher and was more consistent

   - Class B generally scored higher but was less consistent

   - Both classes had the same typical score

   _Explanation:_ Class B has the higher median, so its typical value is higher. It also has the smaller IQR, so its middle $50\%$ is less spread out. The most common wrong answer is C, which forgets that a smaller IQR means more consistency, not less.
