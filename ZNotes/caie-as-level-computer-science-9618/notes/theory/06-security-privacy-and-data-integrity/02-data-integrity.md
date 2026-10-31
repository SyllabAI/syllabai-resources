## Data Integrity 

* Data validation and data verification help protect the integrity of data by checking whether the data entered is sensible and accurate, respectively. 
* Data Validation: checks if data entered is valid, but not its accuracy 
* Data Validation Methods 
  * Range check: data must be between a set of values 
  * Format check: data must follow correct pattern/order 
  * Length check: data must have exact no. of characters 
  * Presence check: checks if some data has been entered 
  * Existence check: data entered must exist 
  * Limit check: checks whether a value entered is within acceptable minimum and maximum values. 
  * Check digit: A digit is used as the answer to an arithmetic operation of other digits in data. If not matched, then data entered incorrectly 
* Data Verification: checks data entered is accurate during data entry and data transfer 
* Data Entry Verification Methods 
  * Visual Check: Person manually compares original data with that entered to check if correct 
  * Double Entry: Enter data into computer twice and compares. 
  * If differences found, go back to raw data to fix error 

**Data Transfer Verification Methods**

* Errors may occur when data moved in system. 
* Parity Check 
  * All data transmitted as bits 
  * Number of 1s in a byte must always be either an odd number or an even number 
  * Parity can be set either as even or odd 
  * E.g. two communicating devices decide there will always be an odd number of 1s. A byte is received that has even number of 1s so error occurred and receiving device would ask for it to be sent again 
  * Used also when data sent between parts of the CPU 
  * Not foolproof: if 2 bits are transposed, data accepted 
* Checksum Check 
  * Data sent from one place to another as block of bytes rather than individual bytes 
  * Computer adds together all bytes being sent 
  * Any bits lost at most-significant end as carry ignored so answer is an 8-bit number 
  * Checksum calculated before and after data sent 
  * If two bytes different, error occurred therefore block of bytes must be sent again



