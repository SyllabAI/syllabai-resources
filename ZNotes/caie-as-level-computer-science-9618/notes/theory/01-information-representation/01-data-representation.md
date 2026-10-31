# Information Representation

## Data Representation

* The two fundamental characteristics of any number system are:
  * **A base:** The number of different digits that a system can use to represent numbers
  * **Place value:** The specific-value of a digit based on its position within a number
* **Denary** - Base 10
* **Binary Systems** - Base 2
  * Possible bits (binary digits): 0 and 1
  * All data and characters are represented in binary


|128|64|32|16|8|4|2|1|
|:---|:---|:---|:---|:---|:---|:---|:---|
|0|0|0|0|0|0|0|0|

* For example, 65 in binary is *01000001*

---

* **Denary vs. Binary prefixes:**


|Denary Prefix|Factor Value|Binary Prefix|Factor Value|
|:---|:---|:---|:---|
|kilo- (k)|×10<sup>3</sup>|kibi- (Ki)|×2<sup>10</sup>|
|mega- (M)|×10<sup>6</sup>|mebi- (Mi)|×2<sup>20</sup>|
|giga- (G)|×10<sup>9</sup>|gibi- (Gi)|×2<sup>30</sup>|
|tera- (T)|×10<sup>12</sup>|tebi- (Ti)|×2<sup>40</sup>|

* **Binary Coded Decimal (BCD)**
  * Binary representation where each positive denary digit is represented by a sequence of 4 bits (nibble).
  * Only certain digits are converted to BCD because particular digits represent a digit greater than 9.
  * For example, to represent 429 in BCD:
  * Convert each individual digit of the number to its binary equivalents -
    1. *4 = 0100*
    2. *2 = 0010*
    3. *9 = 1001*
  * Concatenate the 3 nibbles (4-bit group) in order to produce BCD: *0100 0010 1001*
* **Practical applications**
  * A string of digits on any electronic device displaying numbers (like in calculators)
  * Accurately measuring decimal fractions
  * Electronically coding denary numbers
* **Two’s Complement**
  * We can represent a negative number in binary by making the most significant bit (MSB) a sign bit, which indicates whether the number is positive or negative.

  * **Converting from negative denary to binary two’s complement (example -42):**

    1. Find the binary equivalent of the denary number (ignoring the negative sign) \| 42 = 101010
    2. Add extra 0 bits before the MSB, to format the binary number to 8 bits \| 00101010
    3. Convert binary number to one’s complement (flip the bits) \| 11010101
    4. Convert binary number to two’s complement (add 1) \|1010101 + 1 = 11010110

  * **Converting binary two’s complement into denary (example 11010110):**

    1. Flip all the bits \| 00101001
    2. Add 1 \| 00101010
    3. Convert binary to denary and put a negative sign) \| -42
* Maximum positive number in 8 bits: 127
* Maximum negative number in 8 bits: -128
* **Hexadecimal Systems - Base 16:**
  * Possible digits: 0 to 9 and A to F, where A to F represent denary digits 10 to 15
  * Practical applications:
    * Defining colours in HTML
    * Defining Media Access Control (MAC) addresses
    * Assembly languages and machine code
    * Debugging via memory dumps
  * Example - A5 in Denary = (16×10) + (1×5) *=* *165*
  * Example - 65 in Hexadecimal = 65÷16 = 4 \| Remainder 1 \| *∴ = 41*
* **Character Sets:**
  * A character set generally includes upper & lower case letters, number digits, punctuation marks, and other characters.
  * Character sets use different binary representations for each character via character encoding

---

* **Character Encoding Standards:**


|**ASCII**|**Extended ASCII**|**Unicode**|
|:---|:---|:---|
|Only the English alphabet can be represented|ASCII’s extension - Also includes most European languages’ alphabets|Superset for ASCII & extended ASCII - recognized by various global languages|
|Each character encoding takes up 7 bits, hence 128 possible characters|ASCII extended to 8 bits, hence 256 possible characters|It has an excellent range of characters, using 2 or 4 bytes per character|
|Smaller storage space||2 or 4 times more storage space per character|
