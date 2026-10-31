## Trend Line and Moving Averages

* In order to identify the trend in a Time Series Graph, A line of best fit, known as the Trend Line, is drawn.

* The Trend Line passes through Moving Averages for the data set.

### Reasons for Finding the Moving Averages:

* Raw data contains many spikes and dips in values; moving averages are found to smooth the data out.

* Smoothing the data out by finding moving averages makes it easier to identify the trend.

### Calculating the Moving Averages:

* To calculate the Moving Averages, we must first identify the type of variation shown in the data.

* The type of variation depends on how frequently the pattern in the graph repeats itself.

* The graph we made before shows data recorded every three months.

* The pattern repeats itself every year

* Hence, the pattern repeats every 4 terms/intervals.

* $3 \text{months} \times 4 = \text{12 months/ 1 year}$

* So we need to find the 4-point moving average, as the pattern repeats every 4 data points.

* To find the 4-point moving average, we will find the mean of intervals 1-4, 2-5, 3-6, and so on.

* This is easier to do after organizing your data in a table.

#|
||

Term

|

Guests

|

4 Term Total

|

4 Term Moving Average

||
||

Jan-Mar

|

12

|

ㅤㅤㅤ

|

ㅤㅤㅤ

||
||

Apr-Jun

|

20

|

ㅤㅤㅤ

|

ㅤㅤㅤ

||
||

Jul-Sep

|

13

|

ㅤㅤㅤㅤ

|

ㅤㅤㅤ

||
||

Oct-Dec

|

40

|

$12+20+13+40=85$

|

$\frac{85}{4}=21.25$

||
||

Jan-Mar

|

13

|

$20+13+40+13=86$

|

$\frac{86}{4}=21.50$

||
||

Apr-Jun

|

17

|

$13+40+13+17=83$

|

$\frac{83}{4}=20.75$

||
||

Jul-Sep

|

8

|

$40+13+17+8=78$

|

$\frac{78}{4}=19.50$

||
||

Oct-Dec

|

56

|

$13+17+8+56=94$

|

$\frac{94}{4}=23.50$

||
||

Jan-Mar

|

10

|

$17+8+56+10=91$

|

$\frac{91}{4}=22.75$

||
||

Apr-Jun

|

23

|

$8+56+10+23=97$

|

$\frac{97}{4}=24.25$

||
||

Jul-Sep

|

11

|

$56+10+23+11=100$

|

$\frac{100}{4}=25.00$

||
||

Oct-Dec

|

50

|

$10+23+11+50=94$

|

$\frac{94}{4}=23.50$

||
|#

* **Important Note:**

  * The empty spaces in the table are intentional

  * To calculate the 4-point moving average, we need to add and find the average of 4 consecutive data points

  * For example:

    * Jan–Mar = 12

    * Apr–Jun = 20

    * Jul–Sep = 13

    * Oct–Dec = 40

  * The reason we have left the first 3 boxes empty is that we need 4 terms before we can calculate the first moving average.

  * So we start from the fourth row, using 4 values: 12, 20, 13, 40

  * The next moving average moves forward by one term, calculated in the 5th row and using the values: 20, 13, 40, 13

### Centred Moving Averages

* Usually, we would use the moving averages  found, plot them in the time series graph, and draw a line of best fit through them to get the Trend Line.

* However, as we have a moving average which is even-pointed (even number of intervals), we need to centre our moving averages so the moving averages represent the time they were taken at.

* If we do not centre our moving averages, our moving averages will not show the trend for the time they represent.

* If we have odd-pointed moving averages, we do not need to do this extra step as the averages will automatically be centred.

* To find the Centred Moving Averages, we will find the average of each 4-point moving average.

#|
||

Term

|

Guests

|

4 Term Moving Average

|

Centred 4 Term Moving Average

||
||

Jan-Mar

|

12

|

ㅤㅤㅤ

|

ㅤㅤㅤ

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

ㅤㅤㅤ

|

ㅤㅤㅤ

||
||

Apr-Jun

|

20

|

ㅤㅤㅤ

|

ㅤㅤㅤ

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

$\frac{85}{4}=21.25$

|

ㅤㅤㅤ

||
||

Jul-Sep

|

13

|

ㅤㅤㅤ

|

$\frac{21.25+21.50}{2}=\frac{42.75}{2}=21.375$

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

$\frac{86}{4}=21.50$

|

ㅤㅤㅤ

||
||

Oct-Dec

|

40

|

ㅤㅤㅤ

|

$\frac{21.50+20.75}{2}=\frac{42.25}{2}=21.125$

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

$\frac{83}{4}=20.75$

|

ㅤㅤㅤ

||
||

Jan-Mar

|

13

|

ㅤㅤㅤ

|

$\frac{20.75+19.50}{2}=\frac{40.25}{2}=20.125$

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

$\frac{78}{4}=19.50$

|

ㅤㅤㅤ

||
||

Apr-Jun

|

17

|

ㅤㅤㅤ

|

$\frac{19.50+23.50}{2}=\frac{43.00}{2}=21.500$

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

$\frac{94}{4}=23.50$

|

ㅤㅤㅤ

||
||

Jul-Sep

|

8

|

ㅤㅤㅤ

|

$\frac{23.50+22.75}{2}=\frac{46.25}{2}=23.125$

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

$\frac{91}{4}=22.75$

|

ㅤㅤㅤ

||
||

Oct-Dec

|

56

|

ㅤㅤㅤ

|

$\frac{22.75+24.25}{2}=\frac{47.00}{2}=23.500$

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

$\frac{97}{4}=24.25$

|

ㅤㅤㅤ

||
||

Jan-Mar

|

10

|

ㅤㅤㅤ

|

$\frac{24.25+25.00}{2}=\frac{49.25}{2}=24.625$

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

$\frac{100}{4}=25.00$

|

ㅤㅤㅤ

||
||

Apr-Jun

|

23

|

ㅤㅤㅤ

|

$\frac{25.00+23.50}{2}=\frac{48.50}{2}=24.250$

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

$\frac{94}{4}=23.50$

|

ㅤㅤㅤ

||
||

Jul-Sep

|

11

|

ㅤㅤㅤ

|

ㅤㅤㅤ

||
||

ㅤㅤㅤ

|

ㅤㅤㅤ

|

ㅤㅤㅤ

|

ㅤㅤㅤ

||
||

Oct-Dec

|

50

|

ㅤㅤㅤ

|

ㅤㅤㅤ

||
|#

* **Important Note:**
  * As we have an even number of data points, our moving average is calculated between 2 data points; for example, 21.25 is calculated between Apr-Jun and Jul-Sep, hence the blank spaces in the table.

  * We must centre the moving averages by calculating the arithmetic mean of every 2 averages so that they lie on the middle time interval/ are centred.

  * We do not face this issue when we have to calculate for an odd number of terms, as the moving averages would already be centred/ lie on the middle time interval.
* Now that we have obtained our centred moving averages, we can plot them on our graph and draw a line of best fit by eye to obtain the Trend Line.
* To draw the Trend Line by eye accurately, we must try to balance the line of best fit in a way that the moving averages are equally distributed on either side of the line.

![](https://images.znotes.org/allimages/77a08037f20641ec7342e6aa.webp =770x)