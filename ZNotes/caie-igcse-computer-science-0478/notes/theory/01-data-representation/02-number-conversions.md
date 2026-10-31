## Number Conversions

### **Converting Binary to Denary**

* Place the binary value in columns of 2 raised to the power of the number of values from the right starting from 0. e.g. For binary value 11101110, place it in a table like this:


|128|64|32|16|8|4|2|1|
|:---|:---|:---|:---|:---|:---|:---|:---|
|1|1|1|0|1|1|1|0|

* As can be seen it starts from 1 and then goes to 128 from right to left
* Now values with 1 are to be added together, giving the final answer, as for the example, it is 128     + 64 + 32 + 8 + 4 + 2 = 238

### **Converting Denary to Binary**

* Take the value and successively divide it by 2, creating a table like follows:


|2|142||||
|:---|:---|:---|:---|:---|
|2|71|Remainder:|0|2^0|
|2|35|Remainder:|1|2^1|
|2|17|Remainder:|1|2^2|
|2|8|Remainder:|1|2^3|
|2|4|Remainder:|0|2^4|
|2|2|Remainder:|0|2^5|
|2|1|Remainder:|0|2^6|
||0|Remainder:|1|2^7|

* Note that when the value itself is not divisible by 2, it is divided by the previous value of the current number and 1 is added to the remainder column for that specific number, this remainder is known as the modulus
* When you reach 0, the remainder has to be read from bottom to top giving us the binary value ( as in this case, it is 1 0 0 0 1 1 1 0 )
* A quick check you can do after conversion. If the LSB is 1, then the denary value should be odd. If the LSB is 0, the number is even.

### **Converting Hexadecimal to Binary**

* Each hex digit is one binary nibble

* Separate each value from each other and convert them to denary, refer to the tabler under 1.1 (Hexadecimal, aka Hex)

* Each separate denary value to be converted to binary

* All the binary values to be merged together

  e.g.

```
Hexadecimal : 2    1    F    D 
Denary      : 2    1    15   13
Binary      : 0010 0001 1111 1101

Final Answer: 0010000111111101
```

### **Converting Binary to Hexadecimal**

* Divide the binary value into groups of 4 nibbles starting from the right. If at the end, the last division is less than 4, add 0s until it reaches 4
* For each group, find the denary value as shown above, and then convert each denary value to its corresponding hexadecimal value (if less than 10, then itself, else, 10 is A, 11 is B, 12 is C, 13 is D, 14 is E and 15 is F).
* Put all the hexadecimal values in order to get the final answer

```
Given Value : 1 0 0 0 0 1 1 1 1 1 1 1 0 1
When grouped: 10 0001 1111 1101

After 2 values added to left: 0010 0001 1111 1101

After Conversion to Denary: 2 1 15 13

Hexadecimal: 21FD
```

### **Converting Hexadecimal to Denary**

* Convert the value to binary as shown above, and then convert the final answer to denary

### **Converting Denary to Hexadecimal**

* Convert the value to binary, and then convert it to hexadecimal as explained above