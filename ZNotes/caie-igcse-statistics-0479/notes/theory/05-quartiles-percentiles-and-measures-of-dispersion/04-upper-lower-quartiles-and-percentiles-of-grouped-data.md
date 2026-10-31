## Upper & Lower Quartiles and Percentiles of Grouped Data

* Linear Interpolation is required to find the Upper and Lower Quartiles of a grouped dataset, similar to finding the Median of a dataset.

* Linear Interpolation is the method used to find estimated values between 2 known points, assuming that the change between the points is proportional.

  #|
  ||
  
  Time Taken (t)

  |
  
  No. of Students (f)

  |
  
  No. of Students (cf)

  ||
  ||
  
  0-10

  |
  
  3

  |
  
  3

  ||
  ||
  
  10-20

  |
  
  5

  |
  
  8

  ||
  ||
  
  20-30

  |
  
  2

  |
  
  10

  ||
  ||
  
  30-40

  |
  
  6

  |
  
  16

  ||
  ||
  
  40-50

  |
  
  11

  |
  
  27

  ||
  |#
  

* Above, we are given a set of grouped data regarding the time taken by students to complete an exam.

### How to find the Lower Quartile:

* First, we must divide the Cumulative Frequency into 4 quarters to find the **Lower Quartile (LQ)** Value:

  * $\frac{27}{4}$

  * $= 6.75$

* Next, we must find the class within which the LQ, the 6.75th value, lies.

  * This is the “10-20” class, as the cumulative frequency the class accounts for is “3-8”.

* Then, we will subtract the LQ value, 6.75, from the Cumulative frequency of the previous class

  * $6.75-3$

  * $= 3.75$

* We will then divide the value obtained from the previous step by the frequency of the class within which the LQ lies.

* This is done because our LQ is 4th out of the 5 values in the class, and data is spread evenly within a class in grouped data.

  * $\frac{3.75}{5}​$

* Then, we will find the class width of the LQ class by subtracting the Lower Class Boundary from the Upper Class Boundary.

  * $20 - 10$

  * $= 10$

* Next, we will identify the Lower Class Boundary of the LQ class

  * $10$

* We will put all this obtained information into a formula

  * $LQ = L + \left\[(\frac{\frac{N}{4} - CF}{f}\right\) \times w ]$

    * L is the Lower Class Boundary

    * $N$ is the total number of values

    * $CF$ is the cumulative frequency

    * $f$ is the frequency of the class

    * The fraction would be $\frac{3.75}{5}$, where we obtained the position of the LQ Value within the class containing the LQ value

    * The $w$ refers to the class width of the LQ class

* Hence, through these steps, our LQ would be

  * $LQ = 10 + \frac{3.75}{5} \times 10$

  * $LQ = 17.5$

### How to Find Upper Quartile of Grouped Data:

* To find the **Upper Quartile (UQ)**, we will use the same method as done for the LQ; however, we will slightly change the formula.

* $UQ = L + \left\[\frac{\frac{3N}{4} - CF}{f}\right\) \times w ]$

* First, we must divide the Cumulative Frequency into 4 quarters to find the UQ Value:

  * $\frac{3 \times 27}{4}$

  * $= 20.25$

* Next, we must find the class within which the UQ, 20.25th value, lies.

* This is the “40-50” class, as the cumulative frequency the class accounts for is “16-27”.

* Then, we will subtract the UQ value, 20.25, from the Cumulative frequency of the previous class

  * $20.25-16$

  * $= 4.25$

* We will then divide the value obtained from the previous step by the frequency of the class within which the UQ lies.

* This is done because our LQ is 4.25th out of the 11 values in the class, and data is spread evenly within a class in grouped data.

  * $\frac{4.25}{11}​$

* Then, we will find the class width of the UQ class by subtracting the Lower Class Boundary from the Upper Class Boundary.

  * $50 - 40$

  * $= 10$

* Next, we will identify the Lower Class Boundary of the UQ class

  * $10$

* We will put all this obtained information into a formula

* $UQ = L + \left\(\frac{\frac{3N}{4} - CF}{f}\right\) \times w ]$

  * L is the Lower Class Boundary

  * The fraction would be $\frac{4.25}{11}$, where we obtained the position of the LQ Value within the class containing the UQ value

  * The $w$ refers to the class width of the UQ class

* Hence, through these steps, our UQ would be

  * $UQ = 40 + \frac{4.25}{11} \times 10$

  * $UQ = 43.9$

### How to find the IQR of Grouped Data:

* Now that we have obtained the UQ and LQ of the dataset, we can find the IQR

  * $UQ - LQ$

  * $43.9 - 17.5$

  * $= 26.4$

### How to find Percentile Value in Grouped Data:

* Once again, a similar method will be adopted; however, instead of finding the $x$ value which represents a quartile, we will find the value which represents the percentile.

* For example, if we need to find the estimated value of the 35th Percentile of this data:

* Find the Value representing the 35th Percentile:

  * $\frac{35}{100} \times 27$

  * $= 9.45$

  * 9.45th Value

* Follow the same steps as done for the UQ and LQ

* At the end, we will be left with the following formula:

  * $= 20 + \frac{1.45}{2} \times 10$

  * $= 27.25$

* We may also be asked what Percentile a given value is at.

* For example, if we need to find the estimated percentile of 35 seconds:

* Find the Class which contains 35

  * 35 is present in the 30-40 class interval

* We can then input this value into the previous formula to obtain the position of 35 in the data.

* $10 + \frac{35-30}{10} \times 6$

* $= 13$

  * Now we know that 35 seconds is at the 13th position in the data, so we can put this in the formula for finding the percentile:

* $\frac{13}{27} \times 100$

* $= 48.15$