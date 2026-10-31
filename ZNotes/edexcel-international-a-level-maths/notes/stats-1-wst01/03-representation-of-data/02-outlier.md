## Outliers

* An outlier is an extreme value that lies far away from the rest of the data.

* An outlier is usually either greater than $Q_3$    \+ k($Q_3-Q_1$) or less than $Q_1$   -k($Q_3-Q_1$)

  * $Q_3$ and $Q_1$ are the upper and lower quartiles

  * $\boxed {IQR = Q_3 - Q_1}$

    **Note:** Different exam questions will state different definitions of an outlier. You must read the specific rule given in the question.

### Example Question:

A data set has $Q_1 $= 12, $Q_3$= 20. A data point is 33. Check if 33 is an outlier using the 1.5 $\times $IQR rule.

### Answer

* Step 1: The IQR= 20-12=8

* Step 2: Upper Boundary: $Q_3$\+(1.5 $\times$ IQR) = 20\+(1.5 $\times$ 8) = 20\+12=32

* Step 3: Compare: 33\> 32 so it is an outlier

### **Anomalies**

* **Anomaly**: An outlier that is clearly an error (example: a faulty equipment reading)

* **Cleaning Data:** The process of identifying and removing anomalies from a data set

* Example of an anomaly: in a data set of student ages, there is a value of 120 (this is most likely to be a mistype), Temperature is unusually cold for 1 day where every other day is hot