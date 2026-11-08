# grade-5-5-12-data — lesson

_Lane: `igcse-maths-edexcel` · grade 5 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Typical value and spread

![Ordered scores on a number line with a matching box plot labelled $Q_1 = 18$, median $= 20$, $Q_3 = 22$, and IQR $= 4$](../assets/001-5a777774-29ab-48f1-837e-cc332660fb99.jpeg)
When we describe data, we usually want one number for a typical value and one number for spread. Typical values include the mean and median, while spread can be shown by the range or the interquartile range.

Quartiles split ordered data into four parts. $Q_1$ is the middle of the lower half, $Q_3$ is the middle of the upper half, and
$$
\text{IQR} = Q_3 - Q_1
$$

The range uses the whole data set:
$$
\text{range} = \text{highest} - \text{lowest}
$$
A smaller IQR means the middle half of the data is less spread out, so the results are more consistent.

## Worked example: finding the interquartile range

Suppose the scores are 19, 15, 21, 18, 24, 21, 16, 22, 20, 18, 25. First put them in order: 15, 16, 18, 18, 19, 20, 21, 21, 22, 24, 25. There are 11 values, so the median is the 6th value, which is 20.

Do not include this median when you split the data into lower and upper halves. The lower half is 15, 16, 18, 18, 19, so $Q_1 = 18$. The upper half is 21, 21, 22, 24, 25, so $Q_3 = 22$.

Now subtract the quartiles: $$\text{IQR} = Q_3 - Q_1 = 22 - 18 = 4$$ So the middle half of the scores is spread over 4 points.

## Comparing two groups

When you compare two groups, make two separate comments. Use the median to describe the typical score, and use the IQR to describe spread or consistency.

Example: Red Class has median 31 and IQR 15. Blue Class has median 28.5 and IQR 8. Red Class has the higher typical score because $31 > 28.5$.

Blue Class has the smaller IQR, so Blue Class is more consistent. A larger IQR does not mean a group did better; it only means the results are more spread out.

## Combined means

For mean questions, think about totals first. The key formula used to navigate these problems is: 
$$\text{total} = \text{mean} \times \text{number of values}$$

Example: 24 students are in Group A and 36 are in Group B. The mean for all 60 students is 70.4, and Group A has mean 73.4. First find the totals for the whole set and the known group: 
$$70.4 \times 60 = 4224$$
and
$$73.4 \times 24 = 1761.6$$

Subtract to get Group B's total: $$4224 - 1761.6 = 2462.4$$. Now divide by the 36 students in Group B: $$2462.4 \div 36 = 68.4$$. So Group B's mean is 68.4. Avoid averaging the two means directly, as groups with different sizes must be weighted.

## Combined range

For a combined range, you need the overall lowest value and the overall highest value. If a group gives you a lowest value and a range, first work out its highest value.

Example: Group A has lowest 41 and range 54, so its highest value is $$41 + 54 = 95$$. Group B has lowest 36 and range 52, so its highest value is $$36 + 52 = 88$$.

The overall lowest value is 36 and the overall highest value is 95. This allows us to calculate: $$\text{combined range} = 95 - 36 = 59$$

Do not add the two ranges together. Range depends only on the extreme values of the combined data set, not the sum of individual ranges.

## Check yourself

1. In an ordered data set with 11 values, which value is the median?

   - The 5th value

   - The 6th value ✔

   - The mean of the 5th and 6th values

   - The 7th value

   _Explanation:_ With 11 values, the middle position is $(11+1)/2 = 6$, so the median is the 6th value. A common wrong answer is A, because students count the 5 values below the middle but forget that the middle value itself is the 6th one.

2. Red Class has median 31 and IQR 15. Blue Class has median 28.5 and IQR 8. Which comparison is correct?

   - Red Class has the higher typical score, and Blue Class is more consistent ✔

   - Blue Class has the higher typical score, and Blue Class is more consistent

   - Red Class has the higher typical score, and Red Class is more consistent

   - Blue Class has the higher typical score, and Red Class is more consistent

   _Explanation:_ Red Class has the higher typical score because its median is larger: $31 > 28.5$. Blue Class is more consistent because its IQR is smaller: $8 < 15$. A common wrong answer is C, which mixes up typical score with consistency and assumes the class with the higher median must also be more consistent.

3. Group A has lowest 12 and range 20. Group B has lowest 8 and range 17. What is the combined range?

   - 20

   - 24 ✔

   - 29

   - 37

   _Explanation:_ Group A's highest value is $12 + 20 = 32$ and Group B's highest value is $8 + 17 = 25$. The overall lowest value is 8 and the overall highest value is 32, so the combined range is $32 - 8 = 24$. A common wrong answer is A, which just chooses the larger given range instead of using the overall lowest and highest values.
