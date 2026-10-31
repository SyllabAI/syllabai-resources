## Binary Calculations

* Binary values are not added the way denary values are added, as when adding 1 and 1, we cannot write two because it doesn’t exist in binary.

### **Points to Note:**

* 0 + 0 = 0
* 1 + 0 / 0 + 1 = 1
* 1 + 1 = 0  (1 carry)
* 1 + 1 + 1 = 1 (1 carry)

### **Overflow**

* When adding two values, if the solution exceeds the limit of given values, e.g., the solution has 9 bits, but the question had 8 bits per value, the 9th bit (most left bit) is called overflow.
* This indicates that the memory doesn’t have enough space to store the answer to the addition done in the previous part.

### **Steps to add Two Values (With Example - with overflow)**

* The values we will add are  1 1 0 1 1 1 0 and 1 1 0 1 1 1 1 0

* This solutions represents an overflow

  1. Convert both the bytes into 8 bits (add zero to the left-hand side to match them).

     e.g., 1 1 0 1 1 1 0 would become 0 1 1 0 1 1 1 0

  2. Add the values as follows with the points given above


|**Carry**|1|1|1|1|1|1|1|||
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|**Byte** **1**||0|1|1|0|1|1|1|0|
|**Byte 2**||1|1|0|1|1|1|1|0|
||OVERFLOW|||||||||
|**Solution**|1|0|1|0|0|1|1|0|0|

**Note:** We move from RHS to LHS, and when adding values, we use the rules given above. If the bit crosses the limit (overflows), we put the value in brackets, denoting it is overflow.

iii. The solution would now be  (1) 0 1 0 0 1 1 0 0

### **Steps to add Two Values (With Example - Without overflow)**

* The values we will add are **00101100** and **00010110**

* This solution **does not represent an overflow**

  1\. Convert both the bytes into 8 bits

  (e.g., if any number has fewer bits, add zeros to the left-hand side to match them).
  → 00101100 and 00010110

  2\. Add the values as follows with the points given above

  #|
  ||
  
  Carry

  |
  

  |
  

  |
  
  1

  |
  

  |
  
  1

  |
  

  |
  

  |
  

  ||
  |#
  
  #|
  ||
  
  Byte 1

  |
  
  0

  |
  
  ```
    0     
  ```

  |
  
  1

  |
  
  ```
   0     
  ```

  |
  
  1

  |
  
  ```
    1    
  ```

  |
  
  ```
      0   
  ```

  |
  
  0

  ||
  |#
  
  #|
  ||
  
  Byte 2

  |
  
  ```
  0     
  ```

  |
  
  ```
   0      
  ```

  |
  
  0

  |
  
  ```
  1      
  ```

  |
  
  0

  |
  
  ```
  1      
  ```

  |
  
  ```
   1      
  ```

  |
  
  0

  ||
  |#
  
  #|
  ||
  
  Solution

  |
  
  0

  |
  
  ```
  0        
  ```

  |
  
  1

  |
  
  ```
  1      
  ```

  |
  
  0

  |
  
  ```
   0     
  ```

  |
  
  ```
   1
  ```

  ||
  |#
  

**Note:**
We move from **right-hand side (RHS)** to **left-hand side (LHS)** when adding bits.
If the carry exceeds the leftmost bit and cannot fit into the 8-bit limit, **overflow occurs**.
In this example, the result still fits within **8 bits**, so **no overflow** occurs.

### **Logical Shifts**

* The logical shift means moving a binary value to the left or the right
* When doing a logical shift, keep in mind that the bit being emptied is going to become 0 and the bit that over/underflows will disappear.

### **Explanation with Example**

* **Shifting 10101010 - 1 place left:**

  1. The furthest bit in the direction to be logically shifted is removed ( in this case, one at the LHS is removed) - ==(if it were two places, 2 bits would have been removed)==
  2. Every bit is moved in given places to the given direction ( every bit is moved one place to the left in this case, and the leftover bit in the right is marked 0, so **10101010** would become **01010100**)

### **Two’s Complement (Binary Numbers)**

* Two’s complement is a method used to represent negative values in binary. Here, the MSB ( Most Significant Bit) is replaced from 128 to -128; thus, the range of values in a two’s complement byte is -128 to 127

### **Converting Binary Values to Two’s Complement**

* Firstly, write the binary value and locate the first one from the right; e.g., 0010011 would have the first one at the third position from the right.
* Now, switch every value to the left of the first one located above (not switching the one), e.g., the value in our example becomes 10010100, which is the two’s complement of itself.

### **Converting negative values to two complement**

* Find the binary equivalent of the value ignoring the - sign
* Ensure that the MSB is 0. If it is not, pad Zero (0) bits to the left to have groups of 4 or 8, ensuring that the first bit is always a zero (as it is a positive number)
* Convert the binary value to two’s complement

### **Converting Two’s Complement Value to Denary:**

* We do it the same way as a normal value is converted from binary to denary; we only replace 128 with -12,8 e.g., for 1011101,0 we do the:


|-128|64|32|16|8|4|2|1|
|:---|:---|:---|:---|:---|:---|:---|:---|
|1|0|1|1|1|0|1|0|

-128 + 32 + 16 + 8 + 2 = -70