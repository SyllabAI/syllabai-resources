## Logic Gates & Circuit Design

**Logic Gates:** A component of a logical circuit that can perform a Boolean operation

* **AND Gate:** $A.B\  = \ X$

![](../../../assets/acc8119ef8b7-image005.png)


|**A**|**B**|**X**|
|:---|:---|:---|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

* **OR Gate:** $A + B = X$

![](../../../assets/5206353aca37-allimages892d1e4963f4090914b0b2d6.png)


|**A**|**B**|**Output**|
|:---|:---|:---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

* **NOT Gate:** $\overline{A}\  = \ X$

  ![](../../../assets/661dc656c8bf-allimagescbc96e1f7e65b093f8df0495.png)


|**A**|**Output**|
|:---|:---|
|0|1|
|1|0|

* **NAND Gate:** $\overline{A.B}\  = \ X$

![](../../../assets/0f8a762e4e97-allimages537149b017e3ecba0baa6c76.png)


|**A**|**B**|**Output**|
|:---|:---|:---|
|0|0|1|
|0|1|1|
|1|0|1|
|1|1|0|

* **NOR Gate:** $\overline{A + B} = X$

![](../../../assets/5206353aca37-allimages892d1e4963f4090914b0b2d6.png)


|**A**|**B**|**Output**|
|:---|:---|:---|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|0|

* **XOR Gate:** $A.\overline{B} + \overline{A}.B = X$

![](../../../assets/a34ae20d2017-image010.png)


|**A**|**B**|**Output**|
|:---|:---|:---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|0|

### Half-Adder

- A half adder adds two binary digits and outputs the sum (s) and their carry (c).

- A XOR gate acts like a half adder.

  <table>
  <thead>
  <tr>
  <th colspan=2><strong>Input</strong></th>
  <th colspan=2><strong>Output</strong></th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><strong>A</strong></td>
  <td><strong>B</strong></td>
  <td><strong>S</strong></td>
  <td><strong>C</strong></td>
  </tr>
  <tr>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  <td>0</td>
  </tr>
  <tr>
  <td>0</td>
  <td>1</td>
  <td>1</td>
  <td>0</td>
  </tr>
  <tr>
  <td>1</td>
  <td>0</td>
  <td>1</td>
  <td>0</td>
  </tr>
  <tr>
  <td>1</td>
  <td>1</td>
  <td>0</td>
  <td>1</td>
  </tr>
  </tbody>
  </table></td>
  </tr>
  </table>

  ### Full-Adder

  A full adder adds three binary digits and outputs the sum and their carry.

  ![](../../../assets/3ef5ff493f66-allimages4b788836eb0a331a22081def.png)

  - R is "Carry In"
  - J is "Carry Out"
  - K is "Sum"

  ![](../../../assets/538e7c79486f-allimages55f38799953aab828ca66c44.png)