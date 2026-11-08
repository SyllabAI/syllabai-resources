# grade-7-7-16-histograms — lesson

_Lane: `gcse-maths-edexcel` · grade 7 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What a histogram shows

![Histogram with four touching bars of unequal widths over 0 to 4, 4 to 9, 9 to 15 and 15 to 25, with frequency density heights labelled](../assets/001-24294d11-f9ec-44fe-bb4f-718445ee4551.jpeg)
A histogram is used for grouped continuous data such as time, length, or mass. Unlike an ordinary bar chart, the class intervals can have different widths, so the width of each bar matters.

In a histogram, frequency is shown by the area of a bar, not by height alone. That is why the vertical axis is usually frequency density rather than frequency.

The bars touch because the intervals join up with no gaps. For example, $0 \le t < 5$ includes 0 up to but not including 5, so a value of exactly 5 goes in the next class.

## Class intervals and class widths

The class width is the upper boundary minus the lower boundary. In $0 \le t < 5$, the width is $5 - 0 = 5$, and a value of exactly 5 goes into the next class.

For $0 \le t < 3$, $3 \le t < 8$, $8 \le t < 14$, and $14 \le t < 24$, the widths are $3$, $5$, $6$, and $10$. Writing these widths down first makes later calculations much easier.

## Frequency density is the bar height

The vertical axis on a histogram is usually frequency density, often shortened to f.d. This tells you how much frequency there is per unit of class width.

Use
$$\text{frequency density}=\frac{\text{frequency}}{\text{class width}}$$
to find the height of a bar. Rearranging gives
$$\text{frequency}=\text{class width}\times\text{frequency density}$$
when you need the frequency from a bar.

For $2 \le t < 8$ with frequency 18, the class width is $8 - 2 = 6$. So the frequency density is $18 \div 6 = 3$, so the bar height is 3, not 18.

## Worked example: complete the missing values

A table gives $0 \le t < 4$ frequency 10, $4 \le t < 9$ frequency density 1.4, $9 \le t < 15$ frequency density 1.5, and $15 \le t < 25$ frequency 12. First find the class widths: $4$, $5$, $6$, and $10$.

For the classes with known frequencies, divide by the width to get the bar heights:
$$
\begin{aligned}
\text{f.d. for }0 \le t < 4 &= \frac{10}{4}=2.5\\
\text{f.d. for }15 \le t < 25 &= \frac{12}{10}=1.2
\end{aligned}
$$
These are the heights of those two bars.

For the classes with known frequency densities, multiply by the width to get the frequencies:
$$
\begin{aligned}
\text{frequency for }4 \le t < 9 &= 5 \times 1.4=7\\
\text{frequency for }9 \le t < 15 &= 6 \times 1.5=9
\end{aligned}
$$
These are the missing frequencies.

So the completed rows are frequency 10 and frequency density 2.5, frequency 7 and frequency density 1.4, frequency 9 and frequency density 1.5, and frequency 12 and frequency density 1.2. Draw touching bars across the correct intervals, with heights $2.5$, $1.4$, $1.5$, and $1.2$ on the frequency density axis.

## Estimating from part of a bar

![Histogram bar from 10 to 20 with a highlighted sub-interval from 12 to 18 and height 2.5](../assets/002-d1827ecd-04a1-421f-b748-da5807ca8499.jpeg)
Sometimes you only want part of a class interval, such as $12 \le t < 18$ inside the bar $10 \le t < 20$. You use the same frequency density within that bar and assume the data is spread evenly through the class.

The smaller interval has width $18 - 12 = 6$. So the estimated frequency is
$$
6 \times 2.5 = 15
$$
The estimate is 15.

This is only an estimate because the real data might not be perfectly even inside the class. The method works by taking the area of just the highlighted part of the bar.

## Common mistakes and exam checks

Read the vertical axis carefully. If it says frequency density, a bar with width 10 and height 2 has frequency $10 \times 2 = 20$.

Write each class width beside the interval before you calculate. This stops two common errors: drawing all bars the same width and using raw frequency as the bar height.

Bars should touch because the data is continuous. If you use only part of a bar, say that the answer is an estimate.

## Check yourself

1. Why does a histogram use area rather than just height to show frequency?

   - Because class widths can be different, so frequency must depend on width and height ✔

   - Because all histogram bars have the same width

   - Because frequency density is always the same as frequency

   - Because continuous data cannot be counted

   _Explanation:_ Histograms can have unequal class widths, so height alone would not fairly show how much data is in a class. The common wrong answer is B, but that describes ordinary bar charts, not histograms. For example, compare a class from 15 to 25 with a class from 4 to 9; their widths differ significantly.

2. A class interval $4 \le x < 10$ has frequency 15. What is the frequency density?

   - 2.5 ✔

   - 15

   - 6

   - 90

   _Explanation:_ The class width is $10 - 4 = 6$, so the frequency density is $15 \div 6 = 2.5$. The common wrong answer is B, which treats the frequency as if it were the bar height.

3. A class interval $20 \le x < 35$ has frequency 24. Estimate the frequency for $26 \le x < 31$.

   - 5

   - 8 ✔

   - 16

   - 24

   _Explanation:_ The full class width is $35 - 20 = 15$, so the frequency density is $24 \div 15 = 1.6$. The smaller interval has width 5, so the estimate is $5 \times 1.6 = 8$; the common wrong answer C comes from using the wrong fraction of the class.
