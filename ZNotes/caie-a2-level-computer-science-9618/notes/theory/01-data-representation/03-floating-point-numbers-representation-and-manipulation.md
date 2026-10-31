## Floating-point numbers, representation and manipulation

### Floating point representation

- **Mantissa:** Represents the numbers. If we increase the bits allocated to the mantissa, we increase accuracy.

- **Exponent:** Represents the number of times the decimal place needs to move. If we increase the bits allocated to exponent, we increase the range.

  $$M \times 2^E$$

  $$M = \text{Mantissa}$$

  $$E = \text{Exponent}$$

### Converting from Binary Digit to Positive Float

$$\textrm{Mantissa} =  01101000\textrm{Exponent} =  0011$$

1. Write the binary number with the decimal point

$$0\cdot1101$$

2. Multiply with 2 to the power of the exponent (Move the decimal point the same number of places as the exponent)

$$0\cdot1101 \textrm{ x } 2^3 \0110\cdot1$$

3. Convert to decimal by multiplying

$$ (4\times 1) + (2 \times 1) + (\frac{1}{2} \times 1)$$

Therefore the answer is 6.5

### Converting from Float to Binary Digit

$$6.5$$

* Make the float into an integer by multiplying by factors of 2
  tilt it becomes a whole number.

  $$6.5 = \frac{13}{2}$$

* Now multiply the denominator by multiples of 2 till it is
  larger than the numerator.

  $$\frac{13}{2} \xrightarrow{\boxed{1}} \quad \frac{13}{4} \xrightarrow{\boxed{2}} \quad \frac{13}{8} \xrightarrow{\boxed{3}} \quad \frac{13}{16}$$

* So we get exponent as 3 which in binary is 0011. Now for mantissa, we slowly split $\frac{13}{16}$ into factors of $\frac{1}{2}$.

  $$\frac{13}{16} = \frac{1}{16} + \frac{12}{16} = \frac{1}{16} + \frac{6}{8} = \frac{1}{16} + \frac{3}{4} = \frac{1}{16} + \frac{1}{4} + \frac{2}{4} = \frac{1}{16} + \frac{1}{4} + \frac{1}{2}$$

* Put these back into the mantissa table

  Mantissa: 01101000

  Exponent: 0011

### Converting from Binary Digit to Negative Float

By taking two’s compliment on a postive binary float, converts it gets converted into the negative float.

- Do not take two’s compliment of the exponent.

$$ 01110000\phantom{F}0010\rightarrow 10010000\phantom{F}0010 $$

+3.5 became -3.5

### Normalization

For a positive binary digit, the first two bits need to be different. (Removing extra zeros before in between the decimal and the first 1 digit).

$$ 0\cdot0110000 \phantom{FF} 0011 \rightarrow \0\cdot1100000 \phantom{FF} 0010$$

Benefits:

- Avoids two of the same number being represented differently.
- Maximizes the potential precision.
- Allows us to store the maximum range of numbers in the minimum number of bits.

**Negative binary numbers**

* For negative binary digit, the first bit needs to be 1.

* The mantissa are shifted until we arrive at 1.0, then the exponent must be changed to reflect the change.

  For example:

1\.1101100  --> 1010

1\.0110000  --> 1000

Unlike positive normalisation, the number of changes are subtracted from the exponent.

### Important values


|Largest positive number|0111 1111    0111|
|:---|:---|
|Smallest positive number|0000 0001    1000|
|Smallest normalized positive number|0100 0000    1000|
|Largest magnitude negative number|1000 0000    0111|

### Errors

- **Rounding Error:** When numbers can’t be represented be represented exactly in binary, an approximate value is used which is either more or less than the needed value. When these numbers are then used in operations, the inaccuracies get added to the point where they are visible in the final answer. Like 0.1 + 0.2 = 0.3000000000004
- **Underflow:** Underflow occurs when a number is too close to zero to be accurately represented in binary, leading to a loss of precision.
- **Overflow:** Overflow happens when a number's magnitude exceeds the limit that can be represented in a given number of bits.