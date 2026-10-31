## Calculating the least squares linear regression line

* The regression line of y on x has the form:

  * $y = mx + c $

  * $ y= a + bx$

    * * different textbooks use different constants

* The least squares regression line minimises the sum of the squares of the residuals of each data point

  ![](https://images.znotes.org/allimages/a8f5e81e567685fb9fb21038.webp =540x)

* Gradient: b = $\frac {S_{xy}}{S_{xx}}$

  * To find the gradient, add up (x-gap × y-gap) for every point, then divide that by the sum of each x-gap squared.

    * $S_{xx} = \sum x^2-\frac{\\(\sum x)^2}{n} $ (this is given in the formula booklet)
    * $S_{xy} = \sum xy-\frac{\sum x \sum y}{n} $ (this is given in the formula booklet)

* Intercept: a = $\overline {y} − b \overline {x}$   (mean of y minus b × mean of x)

**Example Questions:**

Find the equation of the least squares regression line y = a \+ bx for the following dataset containing (n = 3) data points:

#|
||

**x**

|

**y**

||
||

1

|

2

||
||

2

|

4

||
||

3

|

5

||
|#

**Anwer:**

Step 1:

#|
||

$\sum x = 6$

|

$\sum y = 11$

|

$\sum x^2 = 14$

|

$\sum xy = 25$

||
|#

Step 2:

$S_{xx}=14-\frac{6^2}{3}=14-\frac{36}{3}=14-12=2$

Step 3:

$S_{xy}=\sum xy-\frac{\sum x\sum y}{n}=25-\frac{6\times 11}{3}=25-\frac{66}{3}=25-22=3$

Step 3:

$b=\frac{S_{xy}}{S_{xx}}=\frac{3}{2}=1.5$

Step 4:

* $\bar{x} = \frac{\sum x}{n} = \frac{6}{3} = 2$

* $\bar{y} = \frac{\sum y}{n} = \frac{11}{3} \approx 3.67$

* $a={y}-b={x}=3.67-(1.5\times 2)=3.67-3=0.67$

The equation of the regression line is

$\boxed {y=0.67+1.5x}$

* **Only use the regression line to make predictions for values of the dependent variable that lie within the range of the given data (interpolation). Predicting outside this range (extrapolation) is unreliable.**