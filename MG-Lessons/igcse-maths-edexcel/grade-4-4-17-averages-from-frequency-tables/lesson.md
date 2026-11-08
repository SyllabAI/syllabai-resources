# grade-4-4-17-averages-from-frequency-tables — lesson

_Lane: `igcse-maths-edexcel` · grade 4 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What a frequency table tells you

A frequency table is a compact way to show repeated data. If the value $2$ has a frequency of $5$, that means the number $2$ appears five times in the dataset.

For an exact frequency table, the mean is a weighted average because some values happen more often than others. Use the formula: $$\text{mean} = \frac{\sum (x \times f)}{\sum f}$$ where $x$ is the value and $f$ is the frequency.

The median is the middle value once the data is in order, and the mode is the most frequent value. Always find the total frequency first, because that tells you how many data values there are in the entire set.

## Worked example: mean from an exact table

A player scored the following points in 50 games. Add a new column for $xf$, which means score times frequency.

| Points $x$ | Frequency $f$ | $xf$ |
|---|---:|---:|
| 0 | 8 | 0 |
| 1 | 12 | 12 |
| 2 | 17 | 34 |
| 3 | 8 | 24 |
| 4 | 4 | 16 |
| 5 | 1 | 5 |

First check the total number of games, because that is the denominator for the mean.
$$\sum f = 8+12+17+8+4+1=50$$

Now add the weighted totals and divide.
$$\sum xf = 0+12+34+24+16+5=91$$
$$\text{mean} = \frac{91}{50} = 1.82$$

Do not just average 0, 1, 2, 3, 4 and 5 by themselves. The value 2 matters much more than 5 here, because 2 happened 17 times while 5 happened only once.

## Median and mode with cumulative frequency

A team played 38 games. The frequencies were as follows: 0 goals: frequency 6, cumulative frequency 6; 1 goal: frequency 15, cumulative frequency 21; 2 goals: frequency 10, cumulative frequency 31; 3 goals: frequency 7, cumulative frequency 38. For an even total, the median lies between the two middle positions.

With 38 games, the middle positions are the 19th and 20th values. The cumulative frequency reaches 21 at 1 goal, so both of these values are 1.

So the median is 1, and the mode is also 1 because 15 is the largest frequency. You can also find the total number of goals by multiplying each score by its frequency and adding: $0 \times 6 + 1 \times 15 + 2 \times 10 + 3 \times 7 = 56$.

## Grouped data and midpoints

![Number line of plant height class intervals from 140 to 200 with midpoint markers at 145, 155, 165, 175 and 190, showing the last class is wider](../assets/001-e5bf6633-c550-4ff0-ba34-f317637673eb.jpeg)

Grouped tables give intervals such as $140 < h \le 150$ instead of exact values. To estimate the mean, we pretend every value in a class sits at the midpoint of that interval.

The midpoint is halfway between the class boundaries. For $180 < h \le 200$, the midpoint is calculated as:

$$\frac{180+200}{2}=190$$

Note that the midpoint is 190, not 185, because this specific class is wider than the previous ones.

For grouped data, use midpoints $m$ instead of exact values. The formula is:

$$\text{estimated mean} = \frac{\sum (m \times f)}{\sum f}$$

This is only an estimate because the exact values inside each class are unknown to us.

## Worked example: estimated mean from grouped data

The heights of 60 plants are grouped below. Add a midpoint column and then multiply each midpoint by its frequency.

| Height | Frequency $f$ | Midpoint $m$ | $mf$ |
|---|---:|---:|---:|
| $140 < h \le 150$ | 5 | 145 | 725 |
| $150 < h \le 160$ | 11 | 155 | 1705 |
| $160 < h \le 170$ | 16 | 165 | 2640 |
| $170 < h \le 180$ | 18 | 175 | 3150 |
| $180 < h \le 200$ | 10 | 190 | 1900 |

Now add the two totals. The total frequency is 60, and the total of the $mf$ column is 10120.
$$\sum f = 60 \qquad \sum mf = 10120$$

Divide to estimate the mean height.
$$\text{estimated mean} = \frac{10120}{60} = 168.666\ldots \approx 168.7 \, \text{cm}$$

This answer is an estimate, not an exact mean. The real plant heights could be anywhere inside each class interval.

## Median class and percentages

A travel-time table for 100 people is shown below. For grouped data, the exact median is usually unknown, so we find the median class instead.

| Time (minutes) | Frequency | Cumulative frequency |
|---|---:|---:|
| $0 < t \le 10$ | 12 | 12 |
| $10 < t \le 20$ | 18 | 30 |
| $20 < t \le 30$ | 24 | 54 |
| $30 < t \le 40$ | 28 | 82 |
| $40 < t \le 50$ | 13 | 95 |
| $50 < t \le 60$ | 5 | 100 |

With 100 people, the middle positions are the 50th and 51st values. The cumulative frequency reaches 54 in the third class, so the median class is $20 < t \le 30$.

To find the percentage who travelled for more than 30 minutes, add the frequencies above 30 minutes:
$$28+13+5=46$$

Because the total is 100, the percentage is 46%; if the total were different, divide by the total frequency and multiply by 100.

## Check yourself

1. When finding the mean from an exact frequency table, what do you divide by?

   - The total frequency ✔

   - The number of rows

   - The largest frequency

   - The number of different values

   _Explanation:_ You divide by the total frequency because that is the total number of data values in the set. The most common wrong answer is B, but the number of rows only tells you how many categories are listed, not how many observations there are.

2. Scores $0, 1, 2$ and $3$ have frequencies $3, 4, 2$ and $1$. What is the median score?

   - 1 ✔

   - 1.5

   - 2

   - 5

   _Explanation:_ There are $10$ values, so the median is found from the $5^{th}$ and $6^{th}$ values. Both of those values are $1$, so the median is $1$; the most common wrong answer is $1.5$, but $1.5$ would only be correct if the $5^{th}$ and $6^{th}$ values were $1$ and $2$, which they are not.

3. A football team scored 54 goals in a season. Goals per game had frequencies 0 goals: 9, 1 goal: 13, 2 goals: $x$, 3 goals: 5, 4 or more goals: 0. What is $x$?

   - 10

   - 13 ✔

   - 15

   - 26

   _Explanation:_ The known goals contribute $0 \times 9 + 1 \times 13 + 3 \times 5 = 28$, so the 2-goal games contribute $54 - 28 = 26$ goals. Since each of those games adds 2 goals, $2x = 26$ and $x = 13$; the open-ended row does not matter because its frequency is 0, and the most common wrong answer is D, which confuses 26 goals with 26 games.
