## Development and Testing

* Guarantees the system's functionality before it is put into use.
* Identification and removal of errors, thus improving system reliability and performance.

### **Test Designs**

* Test data structures, file structures, input formats, output formats, and validation routines
* Ensure all components function correctly and interact seamlessly

### **Test Strategies**

* Test each module: verify that the individual components function as intended
* Test each function: ensure all features work correctly
* Test the whole system: confirm overall system performance and integration

### **Test Plan**

* Test data: specific data used for testing purposes
* Expected outcomes: predicted results based on test data
* Actual outcomes: results obtained from testing
* Remedial action: steps taken to fix identified issues

### **Test Data Types**

*The following data types will be explained using the example of months in a year.*

* **Normal data:** valid and expected data values within the range of acceptability have an expected outcome. E.g., any whole number between 1 and 12.
* **Abnormal data:** invalid or unexpected data values. This can either be:
  * Data outside the range of acceptability or
  * Data that is the wrong data type
  * In this case, examples could be…
    * any value less than 1 (i.e. 0, -6, etc.)
    * any value greater than 12 (i.e. 13, 15, etc.)
    * letters or nun-numeric data (i.e. July, etc.)
    * non-integral values (i.e. 3.5, 4.2, etc.)
* **Extreme data:** values at the limits of acceptability (E.g. 1 or 12)

### **What is live data?**

* Data that has been used with the current system
* Hence, the results are already known



