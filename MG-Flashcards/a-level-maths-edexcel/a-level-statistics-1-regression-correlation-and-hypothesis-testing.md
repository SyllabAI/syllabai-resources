# Regression, Correlation and Hypothesis Testing Flashcards

_Lane: `a-level-maths-edexcel` · grade — · 22 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** In bivariate data, what is the difference between the explanatory and response variables?

**Back:** The explanatory variable is used to predict the other variable ($x$-axis).The response variable is the variable being predicted ($y$-axis).

**Choices:**

- The explanatory variable is used to predict the other variable ($x$-axis).The response variable is the variable being predicted ($y$-axis). ✔
  - _why:_ The explanatory variable is treated as the predictor and plotted horizontally, while the response variable is the measured outcome and plotted vertically.
- The explanatory variable is the variable being predicted ($y$-axis).The response variable is used to predict the other variable ($x$-axis).
  - _why:_ This reverses the two roles. The explanatory variable is the predictor on the $x$-axis, while the response variable is the predicted outcome on the $y$-axis.
- The explanatory variable is used to predict the other variable ($y$-axis).The response variable is the variable being predicted ($x$-axis).
  - _why:_ The axis assignments have been swapped. By convention, the explanatory variable is plotted on the $x$-axis and the response variable on the $y$-axis.
- The explanatory variable is the variable being predicted ($x$-axis).The response variable is also the variable being predicted ($y$-axis).
  - _why:_ The variables do not both perform the same role. The explanatory variable predicts or explains changes, whereas the response variable is the outcome being predicted.

## Card 2 — `cloze`

**Front:** The product moment correlation coefficient ($r$) must always be between [ ___ ] and 1.

**Back:** The product moment correlation coefficient ($r$) must always be between -1 and 1.

**Choices:**

- -1 ✔
  - _why:_ A correlation coefficient lies in the closed interval from $-1$ to $1$. The value $-1$ represents a perfect negative linear correlation.
- 0
  - _why:_ Using $0$ as the lower bound wrongly excludes negative correlations. The PMCC ranges from $-1$ to $1$, with negative values representing negative linear correlation.
- -0.5
  - _why:_ The value $-0.5$ is a possible coefficient, not the minimum. The lower bound is $-1$, which represents perfect negative linear correlation.
- 1
  - _why:_ Using $1$ for both bounds would allow only perfect positive correlation. The PMCC can take any value from $-1$ to $1$.

## Card 3 — `cloze`

**Front:** The product moment correlation coefficient ($r$) must always be between -1 and [ ___ ].

**Back:** The product moment correlation coefficient ($r$) must always be between -1 and 1.

**Choices:**

- 1 ✔
  - _why:_ A correlation coefficient lies in the closed interval from $-1$ to $1$. The value $1$ represents a perfect positive linear correlation.
- 0
  - _why:_ Using $0$ as the upper bound wrongly excludes positive correlations. The PMCC ranges from $-1$ to $1$, with positive values representing positive linear correlation.
- 0.5
  - _why:_ The value $0.5$ is a possible coefficient, not the maximum. The upper bound is $1$, representing perfect positive linear correlation.
- 2
  - _why:_ A PMCC cannot exceed $1$. The value $2$ lies outside the permitted interval, whose upper endpoint is $1$.

## Card 4 — `basic`

**Front:** How do the sign and size of the PMCC ($r$) describe a relationship?

**Back:** The sign (+/-) indicates the direction.The size ($|r|$) indicates the strength of linear correlation.

**Choices:**

- The sign (+/-) indicates the direction.The size ($|r|$) indicates the strength of linear correlation. ✔
  - _why:_ The sign shows whether the variables tend to increase together or move oppositely. The magnitude $|r|$ measures how closely the points follow a linear pattern.
- The sign (+/-) indicates the strength.The size ($|r|$) indicates the direction of linear correlation.
  - _why:_ This reverses the interpretations. The sign determines the direction of the association, while the magnitude $|r|$ determines the strength of its linear correlation.
- The sign (+/-) indicates the direction.The size ($|r|$) indicates the causation of linear correlation.
  - _why:_ The sign does indicate direction, but magnitude does not establish causation. The value of $|r|$ measures the strength of linear correlation only.
- The sign (+/-) indicates the strength.The size ($|r|$) indicates the causation of linear correlation.
  - _why:_ The sign does not measure strength, and $|r|$ cannot show which variable causes the other. Sign gives direction, while magnitude gives linear strength.

## Card 5 — `basic`

**Front:** What happens to the PMCC if the explanatory and response variables are swapped?

**Back:** The value of the PMCC remains the same.

**Choices:**

- The value of the PMCC remains the same. ✔
  - _why:_ The PMCC formula is symmetric in the two variables, so interchanging $x$ and $y$ does not alter either its sign or magnitude.
- The value of the PMCC changes its sign.
  - _why:_ Swapping the variables does not reverse the direction of association. The PMCC formula treats both variables symmetrically, so its value remains the same.
- The value of the PMCC becomes its reciprocal.
  - _why:_ Taking a reciprocal is not part of swapping the variables; that misconception comes from gradients. Correlation is symmetric, so the PMCC remains unchanged.
- The value of the PMCC becomes equal to zero.
  - _why:_ Swapping variables does not destroy their association. Because correlation is symmetric in the two variables, the PMCC retains exactly the same value.

## Card 6 — `basic`

**Front:** What is the unit of measurement for the PMCC?

**Back:** The PMCC is dimensionless (it has no units).

**Choices:**

- The PMCC is dimensionless (it has no units). ✔
  - _why:_ The PMCC standardises covariance using both variables’ standard deviations. Their units cancel completely, leaving a pure number with no units.
- The PMCC is measured in units of the response variable.
  - _why:_ The PMCC does not inherit the response variable’s units. Standardisation cancels the units of both variables, so the coefficient is dimensionless.
- The PMCC is measured in the product of both variables’ units.
  - _why:_ Multiplying the variables’ units describes the units of covariance, not correlation. Dividing by both standard deviations makes the PMCC dimensionless.
- The PMCC is measured in percentage points.
  - _why:_ A percentage is sometimes used informally for proportions, but the PMCC is reported as a unitless number from $-1$ to $1$, not as a percentage.

## Card 7 — `cloze`

**Front:** The existence of correlation does not necessarily imply [ ___ ].

**Back:** The existence of correlation does not necessarily imply causation.

**Choices:**

- causation ✔
  - _why:_ A correlation may arise from coincidence, a lurking variable or reverse causality. It therefore shows association but does not by itself establish a causal link.
- association
  - _why:_ Correlation is itself a measure of association, so observed correlation does imply association. What it does not necessarily imply is causation between the variables.
- dependence
  - _why:_ A non-zero correlation indicates statistical dependence, although dependence can also exist without linear correlation. The unsupported conclusion from correlation is causation.
- covariance
  - _why:_ For variables with defined non-zero standard deviations, a non-zero PMCC corresponds to non-zero covariance. The conclusion that correlation cannot establish is causation.

## Card 8 — `basic`

**Front:** What does $r \approx 0$ indicate about the relationship between two variables?

**Back:** There is no linear correlation (though a non-linear relationship may still exist).

**Choices:**

- There is no linear correlation (though a non-linear relationship may still exist). ✔
  - _why:_ A PMCC near zero means there is little or no linear association. Curved or other non-linear patterns can nevertheless produce a coefficient near zero.
- There is no relationship of any kind (so the variables must be independent).
  - _why:_ A coefficient near zero rules out strong linear correlation, not every possible relationship. The variables may still follow a clear non-linear pattern.
- There is strong positive correlation (so both variables usually increase together).
  - _why:_ Strong positive linear correlation would require $r$ to be close to $1$. A value near zero instead indicates little or no linear correlation.
- There is strong negative correlation (so one variable decreases as the other increases).
  - _why:_ Strong negative linear correlation would require $r$ to be close to $-1$. A value near zero instead indicates little or no linear correlation.

## Card 9 — `basic`

**Front:** Interpret the gradient $b$ in the regression line $y = a + bx$.

**Back:** The predicted change in $y$ for every one-unit increase in $x$.

**Choices:**

- The predicted change in $y$ for every one-unit increase in $x$. ✔
  - _why:_ The gradient measures the expected change in the response variable $y$ when the explanatory variable $x$ increases by one unit.
- The predicted value of $y$ when the value of $x$ is zero.
  - _why:_ This describes the intercept rather than the gradient. The gradient $b$ is the predicted change in $y$ associated with a one-unit increase in $x$.
- The predicted change in $x$ for every one-unit increase in $y$.
  - _why:_ This reverses the roles of the variables. In the regression of $y$ on $x$, $b$ predicts the change in $y$ for each one-unit increase in $x$.
- The predicted value of $y$ when the value of $x$ is one.
  - _why:_ This confuses the gradient with a predicted coordinate. The gradient represents a change in $y$, not the predicted value of $y$ at $x=1$.

## Card 10 — `basic`

**Front:** When is the intercept $a$ in $y = a + bx$ considered a meaningful prediction?

**Back:** Only if a value of $x=0$ is within or near the range of the observed data and makes sense in context.

**Choices:**

- Only if a value of $x=0$ is within or near the range of the observed data and makes sense in context. ✔
  - _why:_ The intercept predicts $y$ at $x=0$, so it is meaningful only when zero is a realistic value supported by, or close to, the observed data.
- Only if the value of the intercept is positive and the fitted regression line has a positive gradient.
  - _why:_ A positive intercept does not automatically have a meaningful interpretation. Its relevance depends on whether $x=0$ is realistic and lies within or near the observed range.
- Only if the value of the PMCC is near $1$ and the observed data show strong correlation.
  - _why:_ A strong correlation does not make the intercept meaningful. The intercept predicts $y$ at $x=0$, so zero must be realistic and within or near the data range.
- Only if a value of $x=\bar{x}$ is within the range of the observed data and makes sense in context.
  - _why:_ The mean of $x$ is generally not zero and does not determine the intercept’s meaning. The relevant issue is whether $x=0$ is realistic and supported by the data.

## Card 11 — `basic`

**Front:** Why are predictions made via extrapolation considered unreliable?

**Back:** They use the model outside the range of the original data, where the trend may not continue.

**Choices:**

- They use the model outside the range of the original data, where the trend may not continue. ✔
  - _why:_ Extrapolation applies the fitted relationship beyond the observed values of the explanatory variable, where there is no evidence that the same pattern remains valid.
- They use the model inside the range of the original data, where the trend may not continue.
  - _why:_ Using the model within the observed range is interpolation, which is generally more reliable. Extrapolation is risky because it predicts outside that range, where the trend may change.
- They use a model that misses some points in the original data, so the trend cannot continue.
  - _why:_ Regression does not require every point to lie exactly on the line. Extrapolation is unreliable specifically because it extends the model beyond the observed data range.
- They use a model based on too few values in the original data, so the trend may not continue.
  - _why:_ A small sample can affect reliability, but it does not define extrapolation. Extrapolation means using the model outside the observed range, where its trend is unsupported.

## Card 12 — `cloze`

**Front:** In hypothesis testing for correlation, the symbol $\text{[...]}$ represents the population correlation coefficient, while $r$ represents the sample correlation coefficient.

**Back:** In hypothesis testing for correlation, the symbol $\boxed{\rho}$ represents the population correlation coefficient, while $r$ represents the sample correlation coefficient.

**Choices:**

- $$\rho$ ✔
  - _why:_ The Greek letter $\rho$ denotes the correlation coefficient for the entire population; it is the unknown parameter tested using evidence from a sample.
- $$r$
  - _why:_ The symbol $r$ denotes the PMCC calculated from sample data, not the population parameter. The population correlation coefficient is represented by $\rho$.
- $$\sigma$
  - _why:_ The symbol $\sigma$ conventionally denotes a population standard deviation, not correlation. The population correlation coefficient is represented by $\rho$.
- $$\mu$
  - _why:_ The symbol $\mu$ conventionally denotes a population mean, not correlation. The population correlation coefficient used in the hypotheses is $\rho$.

## Card 13 — `cloze`

**Front:** In hypothesis testing for correlation, the symbol $\rho$ represents the population correlation coefficient, while $\text{[...]}$ represents the sample correlation coefficient.

**Back:** In hypothesis testing for correlation, the symbol $\rho$ represents the population correlation coefficient, while $\boxed{r}$ represents the sample correlation coefficient.

**Choices:**

- $$r$ ✔
  - _why:_ The letter $r$ denotes the product moment correlation coefficient calculated from the sample and is used as evidence about the population coefficient $\rho$.
- $$\rho$
  - _why:_ The symbol $\rho$ denotes the population correlation coefficient, not the value calculated from a sample. The sample correlation coefficient is represented by $r$.
- $$r^2$
  - _why:_ The quantity $r^2$ is the coefficient of determination, not the sample correlation coefficient itself. The sample PMCC is represented by $r$.
- $$b$
  - _why:_ The symbol $b$ denotes the estimated gradient of a regression line, not the sample correlation coefficient. The sample PMCC is represented by $r$.

## Card 14 — `basic`

**Front:** State the null and alternative hypotheses for a two-tailed PMCC test at the population level.

**Back:** $H_0: \rho = 0$$H_1: \rho \neq 0$

**Choices:**

- $H_0: \rho = 0$$H_1: \rho \neq 0$ ✔
  - _why:_ The null hypothesis states that the population has no linear correlation, while the two-tailed alternative allows either a positive or a negative population correlation.
- $H_0: r = 0$$H_1: r \neq 0$
  - _why:_ Hypotheses must concern the population parameter $\rho$, not the observed sample statistic $r$. A two-tailed PMCC test uses $H_0: \rho=0$ and $H_1: \rho\neq0$.
- $H_0: \rho = 1$$H_1: \rho \neq 1$
  - _why:_ Zero, rather than one, represents no population correlation. The standard test therefore uses $H_0: \rho=0$, with the two-tailed alternative $H_1: \rho\neq0$.
- $H_0: \rho = 0$$H_1: \rho > 0$
  - _why:_ The alternative $\rho>0$ defines a one-tailed test for positive correlation. A two-tailed test must allow both directions, so its alternative is $\rho\neq0$.

## Card 15 — `cloze`

**Front:** To test for a negative correlation, the alternative hypothesis is $\text{[...]}$.

**Back:** To test for a negative correlation, the alternative hypothesis is $\boxed{H_1: \rho < 0}$.

**Choices:**

- $$H_1: \rho < 0$ ✔
  - _why:_ A negative population correlation means the population coefficient lies below zero, so the appropriate one-tailed alternative hypothesis is $H_1: \rho<0$.
- $$H_1: \rho > 0$
  - _why:_ The inequality $\rho>0$ tests for a positive correlation, reversing the required direction. A test for negative correlation uses $H_1: \rho<0$.
- $$H_1: \rho \neq 0$
  - _why:_ The condition $\rho\neq0$ tests for correlation in either direction and is therefore two-tailed. A specifically negative alternative is $H_1: \rho<0$.
- $$H_0: \rho < 0$
  - _why:_ The direction is suitable, but it has been assigned to the null hypothesis. The claim being tested for belongs in the alternative: $H_1: \rho<0$.

## Card 16 — `basic`

**Front:** How do you determine if a sample PMCC ($r$) is significant enough to reject $H_0$?

**Back:** Compare $r$ to the critical value from the table; reject $H_0$ if $r$ is in the critical region.

**Choices:**

- Compare $r$ to the critical value from the table; reject $H_0$ if $r$ is in the critical region. ✔
  - _why:_ Critical values define the outcomes sufficiently extreme under $H_0$. If the observed $r$ lies in that critical region, there is enough evidence to reject $H_0$.
- Compare $r$ to the critical value from the table; reject $H_0$ if $r$ is outside the critical region.
  - _why:_ This reverses the decision rule. Values outside the critical region are not sufficiently extreme, so $H_0$ is rejected only when $r$ lies inside the critical region.
- Compare $r$ to the significance level for the test; reject $H_0$ if $r$ is below the significance level.
  - _why:_ This confuses a correlation coefficient with a probability. The numerical significance level determines the table’s critical value; the observed $r$ is then compared with that critical value.
- Compare $\rho$ to the critical value from the table; reject $H_0$ if $\rho$ is in the critical region.
  - _why:_ The population coefficient $\rho$ is unknown, so it cannot be compared directly with the table. The sample statistic $r$ is compared with the critical value.

## Card 17 — `basic`

**Front:** When should a two-tailed test be used for correlation?

**Back:** When the question asks to test for any correlation without specifying a direction (positive or negative).

**Choices:**

- When the question asks to test for any correlation without specifying a direction (positive or negative). ✔
  - _why:_ A two-tailed test is appropriate when the alternative hypothesis allows correlation in either direction, so both sufficiently positive and sufficiently negative sample correlations can provide evidence against $H_0$.
- When the question asks to test for positive correlation and rules out a negative relationship.
  - _why:_ Specifying positive correlation gives the directional alternative $H_1: \rho > 0$, which requires a one-tailed test. A two-tailed test is used when either positive or negative correlation would count.
- When the question asks to test for negative correlation and rules out a positive relationship.
  - _why:_ Specifying negative correlation gives the directional alternative $H_1: \rho < 0$, so a one-tailed test is appropriate. A two-tailed test instead tests for correlation in either direction.
- When the question gives a small sample size without specifying the expected strength of correlation.
  - _why:_ The sample size affects the critical value, not whether the test has one or two tails. A two-tailed test is chosen when no direction of correlation is specified.

## Card 18 — `cloze`

**Front:** Taking logarithms of the exponential model $y = ab^x$ results in the linear form $$\text{[...]}$$.

**Back:** Taking logarithms of the exponential model $y = ab^x$ results in the linear form $$\boxed{\log y = \log a + x \log b}$$.

**Choices:**

- $$$\log y = \log a + x \log b$$ ✔
  - _why:_ Using $\log(ab^x)=\log a+\log(b^x)$ and the power rule $\log(b^x)=x\log b$ produces a linear equation with gradient $\log b$.
- $$$\log y = \log a + b \log x$$
  - _why:_ This is the linearisation of the power model $y=ax^b$, not the exponential model $y=ab^x$. For $y=ab^x$, the variable term is $x\log b$.
- $$$\log y = a + x \log b$$
  - _why:_ The logarithm must be applied to the multiplicative constant as well as the exponential term. Since $\log a$ is the intercept, the correct form is $\log y=\log a+x\log b$.
- $$$\log y = \log a + xb$$
  - _why:_ This fails to apply the logarithm to the base $b$. The power rule gives $\log(b^x)=x\log b$, so the correct variable term is $x\log b$.

## Card 19 — `cloze`

**Front:** Taking logarithms of the power model $y = ax^b$ results in the linear form $$\text{[...]}$$.

**Back:** Taking logarithms of the power model $y = ax^b$ results in the linear form $$\boxed{\log y = \log a + b \log x}$$.

**Choices:**

- $$$\log y = \log a + b \log x$$ ✔
  - _why:_ Taking logs gives $\log y=\log a+\log(x^b)$, and the power rule changes $\log(x^b)$ to $b\log x$. This is linear in $\log x$.
- $$$\log y = \log a + x \log b$$
  - _why:_ This form belongs to the exponential model $y=ab^x$, where $x$ is the exponent. For the power model, $\log(x^b)=b\log x$.
- $$$\log y = a + b \log x$$
  - _why:_ The constant multiplier $a$ must also be transformed when logarithms are taken. Its contribution is $\log a$, making the correct intercept $\log a$ rather than $a$.
- $$$\log y = \log a + bx$$
  - _why:_ The power rule does not remove the logarithm from $x$: $\log(x^b)=b\log x$, not $bx$. The correct linear variable is therefore $\log x$.

## Card 20 — `basic`

**Front:** If the regression line for transformed data is $\log_{10} y = A + Bx$, how are the constants $a$ and $b$ for the model $y = ab^x$ calculated?

**Back:** $a = 10^A$$b = 10^B$

**Choices:**

- $a = 10^A$$b = 10^B$ ✔
  - _why:_ Comparing $\log_{10}y=\log_{10}a+x\log_{10}b$ with $A+Bx$ gives $A=\log_{10}a$ and $B=\log_{10}b$. Applying inverse logs yields these values.
- $a = A$$b = B$
  - _why:_ The regression coefficients are logarithms of the model constants, not the constants themselves. Taking inverse base-10 logarithms gives $a=10^A$ and $b=10^B$.
- $a = 10^B$$b = 10^A$
  - _why:_ This interchanges the intercept and gradient. The intercept $A$ corresponds to $\log_{10}a$, while the gradient $B$ corresponds to $\log_{10}b$.
- $a = A^{10}$$b = B^{10}$
  - _why:_ Raising each coefficient to the tenth power confuses exponentiation with the inverse of a base-10 logarithm. The inverse transformation is $10^A$ and $10^B$.

## Card 21 — `basic`

**Front:** To test if a power model ($y = ax^b$) fits a dataset, what variables should be plotted on a scatter diagram to look for a straight line?

**Back:** $\log x$ and $\log y$.

**Choices:**

- $\log x$ and $\log y$. ✔
  - _why:_ Taking logarithms of $y=ax^b$ gives $\log y=\log a+b\log x$, which is linear with dependent variable $\log y$ and explanatory variable $\log x$.
- $x$ and $\log y$.
  - _why:_ Plotting $x$ against $\log y$ tests an exponential model because $\log y$ is then linear in $x$. A power model requires both variables to be logarithmically transformed.
- $\log x$ and $y$.
  - _why:_ Transforming only $x$ would test whether $y$ is linear in $\log x$, not whether $y=ax^b$. The power model becomes linear only after logging both variables.
- $x$ and $y$.
  - _why:_ A straight-line plot of the original variables supports a linear model rather than specifically a power model. Testing $y=ax^b$ requires plotting $\log x$ against $\log y$.

## Card 22 — `basic`

**Front:** What is the first step in a correlation hypothesis test?

**Back:** State the null hypothesis ($H_0: \rho = 0$) and the alternative hypothesis ($H_1$).

**Choices:**

- State the null hypothesis ($H_0: \rho = 0$) and the alternative hypothesis ($H_1$). ✔
  - _why:_ The hypotheses must be stated before calculations, using the population correlation coefficient $\rho$. The null asserts no population correlation, while $H_1$ reflects the direction specified by the question.
- Calculate the sample correlation coefficient ($r$) and compare it with the critical value.
  - _why:_ The sample coefficient is calculated only after the hypotheses have been defined. The first step is to state $H_0: \rho=0$ and the appropriate alternative hypothesis.
- State the null hypothesis ($H_0: r = 0$) and the alternative hypothesis ($H_1$).
  - _why:_ Hypotheses concern the unknown population coefficient $\rho$, not the observed sample statistic $r$. The first step is to state $H_0: \rho=0$ and the appropriate $H_1$.
- Look up the critical value using the sample size and the significance level.
  - _why:_ A critical value cannot be selected until the alternative hypothesis establishes whether the test is one-tailed or two-tailed. The hypotheses, beginning with $H_0: \rho=0$, must come first.
