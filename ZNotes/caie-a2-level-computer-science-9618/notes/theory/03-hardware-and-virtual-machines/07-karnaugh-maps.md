## Karnaugh Maps

* **Karnaugh maps:** a method of obtaining a simplified Boolean algebra expression from a truth table. They minimize the number of logic circuits, thus making it more efficient.
* **Sum of products:** all the combinations that lead to 1 in the output.

### Methodology

* Try to look for trends in the output, thus predicting the presence of a term in the final expression
* Draw out a Karnaugh Map by filling in the truth table values into the table
* Select groups of ‘1’ bits in even quantities (2, 4, 6, etc.); if not possible, then consider a single input as a group
* Note: Karnaugh Maps wrap around columns
* Within each group, only the values that remain constant are retained

### Example

![](../../../assets/5d4d7cfc8be3-allimages86e19fef61b7cefe5624e11b.png)

1. Sum of Products

   $A\cdot \overline{B} \cdot \overline{C} + A \cdot B \cdot \overline{C} + A \cdot B \cdot C$

2. Fill in the map

![](../../../assets/fd5ae7e5e830-allimages0db1ad5241c78ae7db8b937d.png)

3. Circle the largest group containing an even number of 1s.

![](../../../assets/b08688e6169d-allimages6ae0f2902e7ea7266f45f7da.png)

4. Take the common values from both

   - In the first group, $A\cdot B$ is common
   - In the second group, $A\cdot \overline{C}$ is common

5. Write the simplified expression.

   $A \cdot \overline{C} + A \cdot B$