## Finding the Mean and Standard Deviation of 2 Combined Datasets

* We can find the Mean and Standard Deviation of 2 combined datasets if we are given the Mean and Standard Deviation of both original datasets

For Example:

* Dataset 1

  * Mean: 50

  * Standard Deviation: 4

  * Total Values: 20

* Dataset 2

  * Mean: 60

  * Standard Deviation: 6

  * Total Values: 30

### Finding the Combined Mean:

* To find the Combined Mean, we must first find the Combined Total of both datasets

* To do so, we will multiply the mean by the Total Number of Values for each dataset, and then add them.

  * $(50 \times 20)+(60 \times 30)$

  * $= 1000 + 1800$

  * $= 2800$

* Next, we must find the Total Number of Values:

  * $20 + 30$

  * $= 50$

* Finally, we can divide the Combined Total by the Combined Total Number of Values:

  * $\frac{2800}{50}$

  * $= 56$

* Hence, the Combined Mean is 56

### Finding the Mean Using the Combined Mean:

* We may also use the Combined mean to find the Mean of a dataset, given that the mean of the second dataset is also available to us.

* For Example:

  * Dataset 1

    * Mean: 50

    * Total Values: 20

  * Dataset 2

    * Mean: $x$

    * Total Values: 30

  * Combined Mean

    * 44

* The formula for finding the Combined Mean is:

  * $\bar{x}_c = \frac{\bar{x}_1 \times y_1 + (\bar{x}_2 \times y_2)}{y_1 + y_2}$

* Where:

  * $\bar{x}_1$ = Mean of Dataset 1

  * $\bar{x}_2$ = Mean of Dataset 2

  * $y_1$ = No. of Values in Dataset 1

  * $y_2$ = No. of Values in Dataset 2

  * $\bar{x}_c$ = Combined Mean

* We can rearrange the formula to:

  * ${\bar{x}_2 =\frac{\bar{x}_c(y_1+y_2)-y_1\bar{x}_1}{y_2}}$

* Hence:

  * $\bar{x}_2 =\frac{\bar{x}_c(y_1+y_2)-y_1\bar{x}_1}{y_2}$

  * $\bar{x}_2 =\frac{44(20+30)-(20 \times 50}{30})$

  * $\bar{x}_2 = 40$

### Finding the Standard Deviation:

* To find the Standard Deviation, we need the value of $fx^2$

* To understand how to find the Value of $fx^2$, we must rearrange the original formula for standard deviation.

* (Mean is represented by $\overline{x}$)

  * $\sigma = \sqrt{\frac{fx^2}{f} - (\frac{fx}{f})^2}$

  * $\sigma^2 = \frac{fx^2}{f} - (\frac{fx}{f})^2$

  * $\sigma^2 = \frac{fx^2}{f} - \overline{x}^2$

  * $\sigma^2 + \overline{x}^2 = \frac{fx^2}{f}$

  * $f(\sigma^2 + \overline{x}^2) = fx^2$

* Now we have a formula to find the value of $fx^2$ for each set of data.

* Dataset 1:

  * $f(\sigma^2 + \overline{x}^2) = fx^2$

  * $20(4^2 + 50^2) = fx^2$

  * $20(2516) = fx^2$

  * $50320 = fx^2$

* Dataset 2:

  * $f(\sigma^2 + \overline{x}^2) = fx^2$

  * $30(6^2 + 60^2) = fx^2$

  * $30(3636) = fx^2$

  * $109080 = fx^2$

* Now that we have the value for $fx^2$ for both the datasets, we can add them to get the combined value of $fx^2$

  * $50320 + 109080$

  * $159400$

* Finally, we can input the rest of the values in the original formula to obtain the combined Standard Deviation.

  * $\sqrt{\frac{fx^2}{f} - (\frac{fx}{f})^2}$

  * $\sqrt{\frac{159400}{50} - (56)^2}$

  * $= 7.21$