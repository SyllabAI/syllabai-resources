## Statistical Tests & Calculation

* Statistically significant: it is an idea that the (observed) results
  are caused by an outside

  factor (not due to chance).

* P \< 0.05: it is an idea that 0.05 means that there is less than 5%
  chance of obtaining the (observed) results by chance.

* Bar chart shows discontinuous/discrete/qualitative/categoric data.

* Chi square test is used for data which is categoric/discrete.

* Pearson’s linear correlation test is suitable when (both sets of)
  data are continuous and (are approximately) normally distributed; a
  scatter graph or data suggests a linear correlation. 5 or more
  paired observations are required to carry out this test.


|Statistics|Criteria|Formulae|Interpretation|
|:---|:---|:---:|:---|
|t-test|2 sets of normal, continuous quantitative data (\>5 readings)|$ t = \frac{\left\| \overline{x} - \ \overline{y} \right\|}{\sqrt{\frac{s_{x}^{2}}{n_{x}} + \frac{s_{y}^{2}}{n_{y}}\ }} $|$v = n_x + n_y -2$|
||**null and alternate hypothesis →**|$h_0 = t < CV$|$h_1 = t > CV$|
|||||
|$x^2 - test$|2 sets of discrete/nominal data|$ \chi^{2} = \ \sum_{}^{}\frac{{(O - E)}^{2}}{E} $|*$*v = (n − 1)^2$|
||**null and alternate hypothesis →**|$h_0 = X^2 < CV$|$h_1 = X^2 > CV$|
|||||
|Pearson’s linear correlation|2 sets of normal, discrete quantitative data(\>5 readings)|$ r = \ \frac{\sum_{}^{}\text{xy} - n(\overline{x})(\overline{y})}{n(s_{x})(s_{y})} $|-1 : (-) relation. 0 : no relation. \+1 : (\+) relation|
|Spearman’s rank correlation|2 sets of discrete/ordinal, normal data (10-30 readings)|$r_s = 1 - \frac{6 \sum D^2}{n(n^2 - 1)} \quad$|\+1: strong positive correlation. -1: strong negative correlation. 0: no correlation|
|Simpson’s index of diversity|Population data|$D = 1 - \ \sum_{}^{} ( \frac{n}{N})^{2}$|0 : not diverse. 1 : very diverse|
|Mark-release-capture|Population data|$ n = \ \frac{n_{1} \times n_{2}}{\text{n\ }(marked)} $|n = total population|
