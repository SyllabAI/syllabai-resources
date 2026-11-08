# as-statistics-histograms — lesson

_Lane: `a-level-maths-edexcel` · grade — · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## What a histogram shows

![Histogram with unequal class widths labelled to show class width, frequency density, and that area represents frequency](../assets/001-ed1e6118-11d8-4e6e-b314-0d5d460c6867.jpeg)

A histogram is used for grouped numerical data, especially when class widths are different. The bars touch because the data are continuous or treated as continuous.

In a histogram, the area of each bar represents the frequency, not usually the height alone. That is why a wide class with the same frequency as a narrow class must have a shorter bar.

Use the key relationships $\text{frequency} = \text{class width} \times \text{frequency density}$ and:

$$\text{frequency density} = \frac{\text{frequency}}{\text{class width}}$$

These formulas let you move between a frequency table and the histogram.

## Finding class widths for rounded data

When data are measured to the nearest whole number, use class boundaries or count the whole-number values in the class. So the class 9-13 really runs from 8.5 to 13.5, giving width $13.5 - 8.5 = 5$.

For example, 4-8 has width 5, 9-12 has width 4, 13-19 has width 7, and 20-22 has width 3. Either count the included whole numbers or use boundaries.

A very common mistake is to do $20 - 14 = 6$ for the class 14-20. The correct width is 7 because it includes 14, 15, 16, 17, 18, 19 and 20.

## Worked example: completing a frequency-density table

Suppose times measured to the nearest second are grouped as 1-3, 4-7, 8-10, 11-15 and 16-20 with frequencies 6, 16, 9, missing and 5. First find the class widths: 3, 4, 3, 5 and 5.

The bar for 11-15 has frequency density 2.8, so use $\text{frequency} = \text{class width} \times \text{frequency density}$. The missing frequency is $5 \times 2.8 = 14$.

Now calculate the other densities with $\text{frequency density} = \frac{\text{frequency}}{\text{class width}}$. They are $6/3 = 2$, $16/4 = 4$, $9/3 = 3$ and $5/5 = 1$, so the histogram heights are 2, 4, 3, 2.8 and 1.

## Worked example: using one drawn bar

Suppose the classes are 4-8, 9-13, 14-20 and 21-24 with frequencies 10, 12, 21 and 8. In the histogram, the 9-13 bar is 2.4 cm wide and 3 cm high, and we want the size of the 14-20 bar.

The reference class 9-13 has actual width 5, so the horizontal scale is $2.4/5 = 0.48 \, \text{cm per unit}$. Since 14-20 has width 7, its drawn width is $7 \times 0.48 = 3.36 \, \text{cm}$.

Now find the density of the reference class: $12/5 = 2.4$. If density 2.4 is drawn as 3 cm, the vertical scale is $3/2.4 = 1.25 \, \text{cm per density unit}$.

The class 14-20 has density $21/7 = 3$, so its drawn height is $3 \times 1.25 = 3.75 \, \text{cm}$. Widths come from class width, but heights come from frequency density, so never use one scale for the other.

## Estimating probabilities from histogram areas

To estimate a probability from a histogram, use estimated frequency over total frequency. Because area represents frequency, whole bars count fully and part of a bar gives the matching fraction of its frequency.

![Histogram-style diagram showing a dashed line at 10 seconds and the shaded part of the 9-10 class used to estimate frequency under 10](../assets/002-2088098c-7b86-4907-afd0-7cd2f1f5afde.jpeg)

For classes 1-4, 5-8, 9-10, 11-15 and 16-20 with frequencies 4, 20, 12, 15 and 9, the total frequency is $4 + 20 + 12 + 15 + 9 = 60$. The full classes under 10 seconds contribute $4 + 20 = 24$.

The class 9-10 has boundaries 8.5 to 10.5, so its width is 2. The part under 10 runs from 8.5 to 10, so its width is 1.5 and its estimated frequency is $(1.5/2) \times 12 = 9$.

That gives $24 + 9 = 33$ people under 10 seconds, so $P(T < 10) = 33/60 = 0.55$. This is only an estimate because we assume values are spread evenly within the class 9-10.

## Check yourself

1. In a histogram with unequal class widths, which feature tells you the frequency of a class?

   - The area of the bar ✔

   - The height of the bar

   - The midpoint of the class

   - The left class boundary

   _Explanation:_ A is correct because $\text{area} = \text{class width} \times \text{frequency density}$, which gives the frequency. B is the most common wrong answer because students confuse histograms with bar charts, where height itself represents frequency.

2. A class has frequency 24 and class width 6. What is its frequency density?

   - 4 ✔

   - 24

   - 6

   - 0.25

   _Explanation:_ A is correct because $\text{frequency density} = 24/6 = 4$. B is the most common wrong answer because students sometimes use frequency itself as the bar height, which is not correct for a histogram.

3. The times are grouped as 1-4: 4, 5-8: 20, 9-10: 12, 11-15: 15, 16-20: 9, measured to the nearest second. Estimate $P(T < 12)$.

   - 0.55

   - 0.60

   - 0.675 ✔

   - 0.75

   _Explanation:_ C is correct because the total is 60, the first three classes give 36, and in the class 11-15 only the part from 10.5 to 12 is used. That is $1.5/5$ of the class, so the extra estimated frequency is $(1.5/5) \times 15 = 4.5$, giving $(36 + 4.5)/60 = 0.675$. D is the most common wrong answer because it includes all of the 11-15 class instead of only the part below 12.
