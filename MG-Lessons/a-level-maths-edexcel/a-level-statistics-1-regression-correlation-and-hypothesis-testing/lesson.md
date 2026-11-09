# a-level-statistics-1-regression-correlation-and-hypothesis-testing — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Scatter diagrams and paired data

![Scatter diagrams showing an upward trend with a regression line and a downward trend, with axes labelled temperature and sales, and experience and task time](../assets/001-9a7a919c-f93f-4903-b11d-33b521cd7cb7.jpeg)

Bivariate data means each point comes from a matched pair of values, such as temperature and sales from the same day. In a scatter diagram, we place the explanatory variable on the horizontal axis as $x$ and the response variable on the vertical axis as $y$.

When points rise from left to right, the correlation is positive; when they fall, it is negative. If the points lie close to a straight pattern, the linear correlation is strong, and if they are spread out, it is weak.

A scatter diagram helps you judge the relationship visually before performing any complex calculations. While it can suggest a trend, a scatter diagram does not by itself prove that changes in one variable cause changes in the other.

## PMCC and what it tells you

The product moment correlation coefficient, or PMCC, is written $r$ for a sample and always satisfies $-1 \le r \le 1$. Values near 1 show strong positive linear correlation, values near -1 show strong negative linear correlation, and values near 0 show little or no linear correlation.

The sign of $r$ gives direction, while the size of $|r|$ gives strength. A value near 0 only means there is no clear straight-line pattern, so the data could still follow a curve.

The PMCC has no units, and swapping $x$ and $y$ does not change its value. In hypothesis testing we use $\rho$ for the population correlation coefficient, while $r$ is the sample value compared with a critical value.

## Regression lines in context

The regression line of $y$ on $x$ is used to predict $y$ from $x$, and it is written
$$y = a + bx$$
Here $b$ is the gradient and $a$ is the intercept.

Suppose a café models daily sales $S$ from temperature $t$ using
$$S = 4800 + 135t$$
The gradient 135 means predicted sales rise by about £135 for each extra 1°C. If the sample PMCC is $r=0.69$, the positive linear correlation is moderately strong, so the straight-line model is fairly sensible.

At $t=12$, substitute into the line:
$$S = 4800 + 135(12) = 6420$$
So the model predicts sales of about £6420 at 12°C.

The intercept 4800 is the predicted sales when $t=0$, but that may not be meaningful if the data were collected only in summer. Using the model at a temperature outside the original data range is extrapolation and is less reliable.

## Worked PMCC hypothesis test

Suppose 10 paired observations give a sample PMCC of $r=0.67$, and we want to test for positive correlation at the 5% level. The hypotheses are $$H_0:\rho = 0,\qquad H_1:\rho > 0$$ because the question is specifically about positive correlation.

With $n=10$ pairs, the 5% one-tailed critical value from the PMCC table is 0.549. For a one-tailed positive test, compare $r$ directly with the critical value, whereas a two-tailed test uses $|r|$.

Since $$0.67 > 0.549$$ the sample value lies in the critical region and we reject $H_0$. The result is statistically significant at the 5% level.

There is sufficient evidence at the 5% level of positive correlation between the variables. This does not prove causation; it only says the sample gives enough evidence of a positive linear relationship in the population.

## Using logarithms to straighten a curve

![Curved cooling scatter plot beside a straight-line transformed plot after taking log10 of temperature](../assets/002-46102c63-9c8f-409c-9233-a8d5aacbcb5e.jpeg)

Some data follow a curved pattern, so an ordinary straight regression line is not a good model. A logarithmic transformation can turn certain curved relationships into straight-line ones.

For an exponential model
$$y = ab^x$$
taking base-10 logs gives
$$\log_{10}y = \log_{10}a + x\log_{10}b$$

If we set $Y=\log_{10}y$, the transformed regression line has the form $Y=A+Bx$ with $a=10^{A}$ and $b=10^{B}$.

For a power model
$$y = ax^b$$
taking logs gives
$$\log_{10}y = \log_{10}a + b\log_{10}x$$
So a straight-line model for $Y=\log_{10}y$ against $X=\log_{10}x$ supports a power relationship.

## Worked example: from log line to exponential model

Suppose $Y=\log_{10}w$ and the regression line is $$Y = 1.99 - 0.031t$$ To match an exponential model $w=ab^t$, compare it with $\log_{10}w=\log_{10}a+t\log_{10}b$.

This comparison gives the following values: $$\log_{10}a = 1.99,\qquad \log_{10}b = -0.031$$ So we now undo the base-10 logs to find $a$ and $b$.

Undo the logs: $$a = 10^{1.99} \approx 97.7,\qquad b = 10^{-0.031} \approx 0.931$$ So the exponential model is $$w = 97.7(0.931)^t$$

The value of $a$ is the predicted temperature when $t=0$, so the model starts at about 97.7°C. Because $b<1$, the model describes exponential decay, which fits a cooling process. If the transformed PMCC is closer to $\pm 1$ than the original PMCC, that supports using the transformed model.

## Check yourself

1. A researcher uses study time to help predict test score. The scatter diagram rises fairly tightly from left to right. Which statement is best?

   - Put study time on the $x$-axis, test score on the $y$-axis, and describe fairly strong positive linear correlation ✔

   - Put test score on the $x$-axis because it is the variable being predicted

   - Describe the relationship as negative correlation because one variable causes the other to change

   - Describe the relationship as strong negative linear correlation

   _Explanation:_ Study time is the explanatory variable, so it goes on the $x$-axis, and test score is the response variable, so it goes on the $y$-axis. The upward, fairly tight pattern shows fairly strong positive linear correlation. The common wrong answer is B: the response variable is predicted from the explanatory variable, so it belongs on the $y$-axis, not the $x$-axis.

2. A regression line is fitted using temperatures between 18°C and 28°C. What is the best comment on using it to predict sales at 35°C?

   - It is interpolation, so the prediction is usually reliable

   - It is extrapolation, so the prediction may be much less reliable ✔

   - It is impossible because regression lines can only predict when $x=0$

   - It proves that temperature causes sales to increase

   _Explanation:_ 35°C is outside the observed range 18°C to 28°C, so this is extrapolation and the straight-line pattern may not continue there. The common wrong answer is A: interpolation only happens inside the range of the original data.

3. If $X=\log_{10}x$, $Y=\log_{10}y$, and the regression line is $Y=0.25-0.16X$, which power model matches the line?

   - $$y=0.25x^{-0.16}$

   - $$y=1.78x^{-0.16}$ ✔

   - $$y=1.78x^{0.16}$

   - $$y=10^{-0.16}x^{0.25}$

   _Explanation:_ Comparing $Y=0.25-0.16X$ with $\log_{10}y=\log_{10}a+b\log_{10}x$ gives $\log_{10}a=0.25$ and $b=-0.16$, so $a=10^{0.25}\approx 1.78$. The common wrong answer is A: the intercept in the log equation is $\log_{10}a$, not $a$ itself.
