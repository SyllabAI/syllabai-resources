# as-statistics-4-correlation — lesson

_Lane: `a-level-maths-edexcel` · grade — · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Paired data and scatter graphs

![Four scatter plots showing strong positive, weak positive, strong negative, and no clear correlation](../assets/001-a7eb3d7e-c2ae-4435-80ea-ad999e8731b0.jpeg)

Correlation uses bivariate data, which means two measurements are recorded in pairs for each case. A scatter graph plots each pair as one point so you can look for a relationship.

Put the explanatory variable on the horizontal axis and the response variable on the vertical axis. Label both axes with the variable and the unit, such as Height (cm) and Weight (kg).

We do not join the points on a scatter graph. Instead, we study the overall pattern to decide whether the variables seem related.

## Direction, strength, and the correlation coefficient

Positive correlation means that larger values of one variable tend to go with larger values of the other. Negative correlation means that larger values of one variable tend to go with smaller values of the other.

Strong correlation has points close to an imaginary straight line, while weak correlation has points more widely scattered. In exam answers, say both the direction and the strength, then link it to the context.

The product moment correlation coefficient is written as $r$, where

$$-1 \le r \le 1$$

Values close to 1 or -1 show strong linear correlation, while values close to 0 show little or no linear correlation. A value near 0 does not rule out a curved relationship.

## Causation and outliers

Correlation shows association, but it does not prove that one variable causes the other. Two variables may move together because of a third factor, such as hot weather affecting both ice cream sales and suncream sales.

An outlier is a value far from the rest of the pattern, and a single outlier can change how strong the correlation looks. One common rule is to calculate the interquartile range (IQR) to establish boundaries.

$$$\text{IQR} = Q_3 - Q_1$$

Then use the boundaries $Q_1 - 1.5 \times \text{IQR}$ and $Q_3 + 1.5 \times \text{IQR}$. An outlier is not automatically a mistake; it may be a genuine extreme value, so you should comment on its effect before deciding whether it should be ignored.

## Worked example: using a regression line

![Scatter graph of height against weight with regression line, interpolation at 176 cm, and extrapolation beyond the data range](../assets/002-be5ecfdf-221e-40cc-8a2a-a6179d95b741.jpeg)

A regression line is a straight-line model, often written as $y = a + bx$. Suppose the regression line for weight $w$ on height $h$ is $w = 1.31h - 157$.

To estimate the weight of a player who is 176 cm tall, substitute $h = 176$ because height is the explanatory variable.

$$$w = 1.31 \times 176 - 157 = 230.56 - 157 = 73.56$$

So the estimated weight is about $73.6 \, \text{kg}$. The line predicts weight from height, so using it this way is correct. The gradient 1.31 means that each extra 1 cm of height increases the predicted weight by about $1.31 \, \text{kg}$. Because 176 cm is within the observed height range, this estimate is interpolation and is usually more reliable than extrapolation.

## Reliability of estimates

Estimates are most reliable when the points show a strong linear pattern and the new value lies within the original data range. Predicting inside the range is called interpolation, and predicting outside it is called extrapolation.

Extrapolation is risky because the relationship may not continue in the same way beyond the observed data. Serious outliers or a changed context can also make the line less trustworthy.

Also check the direction of the model. If the equation is weight on height, you should not rearrange it to predict height from weight unless the question specifically supports that choice.

## Check yourself

1. A coach wants to use height to estimate weight for players. Which setup is best for the scatter graph?

   - Height on the horizontal axis and weight on the vertical axis ✔

   - Weight on the horizontal axis and height on the vertical axis

   - Put both variables on the same axis

   - Use a bar chart instead of a scatter graph

   _Explanation:_ A is correct because height is the explanatory variable and weight is the response variable being predicted. B is the most common wrong answer because swapping the axes reverses the prediction direction and can lead to the wrong interpretation or the wrong regression equation.

2. A calculator gives $r = -0.82$ for distance from the coast and average annual rainfall. What is the best interpretation?

   - Strong negative linear correlation ✔

   - Weak negative linear correlation

   - Strong positive linear correlation

   - No correlation

   _Explanation:_ A is correct because the negative sign shows that rainfall tends to decrease as distance from the coast increases, and $0.82$ is close to 1 in size so the linear relationship is strong. B is the most common wrong answer because students notice the negative sign but forget that values close to $-1$ indicate strong, not weak, correlation.

3. A regression line was built using player heights from $168 \text{ cm}$ to $194 \text{ cm}$. Which use of the line is most reliable?

   - Estimate the weight of a player who is $170 \text{ cm}$ tall ✔

   - Estimate the weight of a player who is $205 \text{ cm}$ tall

   - Rearrange the equation to estimate height from weight

   - Assume every estimate from the line is exact

   _Explanation:_ Option A is correct because $170 \text{ cm}$ lies within the original height range ($168$ to $194 \text{ cm}$), making this an interpolation which is generally reliable. Option B involves a value outside the range ($205 \text{ cm}$), which is extrapolation and less reliable. Option C is incorrect because a regression of $Y$ on $X$ cannot simply be rearranged to predict $X$ from $Y$ accurately.
