## Bit Manipulation

* Binary numbers can be multiplied or divided by shifting
* Left shift (LSL #n)
  * Bits are shifted to the left to multiply
  * E.g. to multiply by four, all digits shift two places to left
* Right shift (LSR #n)
  * Bits are shifted to the right to divide
  * E.g. to divide by four, all digits shift two places to right
* Logical shift: zeros replace the vacated bit position
* Arithmetic shift: Used to carry out multiplication and division of signed integers represented by bits in the accumulator by ensuring that the sign-bit (usually the MSB) is the same after the shift.
* Cyclic shift: the bit that is removed from one end by the shift is added to the other end.

**Bit Masking**

- Each bit can represent an individual flag.
- ∴ by altering the bits, flags could be operated upon.
- Bit manipulation operations:
  - Masking: an operation that defines which bits you want to keep and which bits you want to clear.
  - Masking to 1: The OR operation is used with a 1.
  - Masking to 0: The AND operation is used with a 0.
  - Matching: an operation that allows the accumulator to compare the value it contains to the given value in order to change the state of the status register.
- Practical applications of Bit Masking:
  - Setting an individual bit position:
    - Mask the content of the register with a mask pattern which has 0 in the ‘mask out’ positions and 1 in the ‘retain’ positions.
    - Set the result with the match pattern by using the AND command with a direct address.
  - Testing one or more bits:
    - Mask the content of the register with a mask pattern which has 0 in the ‘mask out’ positions and 1 in the ‘retain’ positions.
    - Compare the result with the match pattern by using the CMP command or by “Checking the pattern”.
  - Checking the pattern
    - Use AND operation to mask bits and obtain resultant.
    - Now subtract matching bit pattern from resultant.
     The final ‘non-zero’ result confirms the patterns are not the same else vice versa.



