# Mark Schemes — Bit Manipulation
**4. Processor Fundamentals** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (13 questions)


### Q1
The mask `01100000` is used. It holds a 1 in the window position and a 1 in the motion position, and 0 everywhere else. **[1]**

A bitwise AND is carried out between the contents of the status register and the mask. **[1]**

The AND clears every other bit to 0, so the result holds only the two bits being tested and the six sensors outside this test cannot affect it. **[1]**

Both sensors have been triggered only when the result is equal to the mask `01100000`. With the register holding `01001010` the result is `01000000`. This is not 0, but it is not equal to the mask either, so only the window sensor has been triggered and no full alarm is raised. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the mask `01100000`
> 
> **1 mark** for a bitwise AND between the status register and the mask
> 
> **1 mark** for the AND clearing all the other bits to 0 // isolating the two bits being tested
> 
> **1 mark** for comparing the result with the mask, both sensors are triggered only if the result equals `01100000`
> 
> Accept for the fourth mark the worked example, `01001010` AND `01100000` gives `01000000`, which is not equal to the mask, so only one sensor has been triggered
> 
> Accept the mask written with a space, `0110 0000`
> 
> Do not accept OR or XOR for the second mark. OR would set the two bits rather than test them, and would destroy the sensor readings
> 
> Do not accept "if the result is not 0 then both sensors have been triggered". A result of `01000000` is not 0 and only one sensor has been triggered

> **[exam-tip]**
> The trap here is the last step. A single-bit test can stop at "is the result 0 or not", but a two-bit test cannot: `01000000` is not 0 and yet only one of the two sensors is on. When a mask holds more than one 1, compare the result with the mask itself, not with 0.
> 
> Take the mask straight from the place-value row rather than counting bit positions in your head. Window sits at 64 and motion sits at 32, so the mask is `01100000`.

### Q2
**(a)** Mask: `00100000` **[1]**

**(b)** Bitwise OR **[1]**

**(c)** Control register after the operation: `01101010` **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `00100000`
> 
> **1 mark** for OR // bitwise OR // the instruction `OR B00100000`
> 
> **1 mark** for `01101010`
> 
> Accept for (a) the mask written with a space, `0010 0000`
> 
> Do not accept AND for (b). ANDing with `00100000` would switch every other device off and would leave the fan off as well
> 
> Do not accept XOR for (b). XOR would switch the fan on here, but it toggles rather than sets, so it would switch the fan off again if the fan were already on
> 
> Do not accept `11011111` for (a), this is the mask for clearing the fan bit rather than setting it

> **[exam-tip]**
> Match the operation to the job before you build the mask. To set a bit and leave everything else alone you need OR with a mask holding a 1 in that one position and 0 everywhere else, because ORing any bit with 0 leaves it unchanged. To clear a bit you need AND with a mask holding a 0 in that position and 1 everywhere else.
> 
> Students often reach for AND because the phrase "bit mask" makes them think of AND. Read what the question wants to happen to the other seven devices, then check your answer by looking at them: in `01101010` the pump, lamp and mister are still on, exactly as they were.

### Q3
| Instruction | ACC contents after the instruction |
|---|---|
| `AND B00001111` | **00001101** **[1]** |
| `OR B10000000` | **11101101** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `00001101`
> 
> **1 mark** for `11101101`
> 
> Accept the bits written with a space, `0000 1101` and `1110 1101`
> 
> Do not accept `00001111` for the first row, this is the mask copied out rather than the result
> 
> Do not accept `00000000` for the second row, this is an AND applied where an OR was asked for
> 
> Do not accept `10001101` for the second row, this comes from applying the second instruction to the result of the first instead of reloading the ACC with `01101101`
> 
> Do not accept an answer with more or fewer than 8 bits

> **[exam-tip]**
> Write the two patterns one above the other in the answer space and work down column by column. The most common error is to carry the operation over from the previous row, so keep telling yourself what each one does: `AND` gives a 1 only when both bits are 1, so it clears bits, while `OR` gives a 1 when either bit is 1, so it sets bits and can never turn a 1 into a 0.
> 
> Note that the ACC is reloaded with `01101101` before each instruction. Do not feed the answer from the first row into the second.

### Q4
**(a)** Contents of the register after the shift: `10100100` **[1]**

**(b)** Before the shift: 105. After the shift: 164. **[1]**

**(c)** A left logical shift only multiplies by 2 for each place while every 1 bit stays inside the register. Here the bit with place value 64 is shifted out of the left-hand end and is lost. **[1]**

The correct product is 4 x 105 = 420, and 420 is larger than 255, which is the largest unsigned value an 8-bit register can hold. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `10100100`
> 
> **1 mark** for both denary values, 105 before and 164 after
> 
> **1 mark** for a 1 bit being shifted out of the left-hand end of the register and lost // the bit with place value 64 has nowhere to move to
> 
> **1 mark** for 420 being too large for the register // an 8-bit register holds a maximum unsigned value of 255
> 
> Accept for the third mark: the bit with place value 64 would need place value 256 after the shift
> 
> Accept for the fourth mark: 4 x 105 given as 420, or the working `105 x 4`, or the word overflow used correctly
> 
> Do not accept "the shift was carried out incorrectly", the shift itself is correct
> 
> Do not accept 420 as the answer to part (b), the register holds 164

> **[exam-tip]**
> The rule "a left shift of one place doubles the value" is only safe while nothing falls off the end. Before you use it, look at the leftmost bits of the starting pattern. Shifting `01101001` left by 2 pushes a 1 out of the register, so the doubling rule breaks and the answer 164 is not 4 x 105.
> 
> A quick check saves the marks: work out the product first. If it is bigger than 255 on an 8-bit register, the shift cannot give it, and part of your explanation is already written for you.

### Q5
**(a)** Right logical shift, 2 places: `00110010` **[1]**

**(b)** Right arithmetic shift, 2 places: `11110010` **[1]**

**(c)** A right arithmetic shift copies the sign bit into the Most Significant Bit (MSB), so a negative number stays negative. A right logical shift puts a 0 into the MSB, which turns the negative value into a positive one. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `00110010`
> 
> **1 mark** for `11110010`
> 
> **1 mark** for the sign bit being copied into the MSB by the arithmetic shift, so the sign is kept
> 
> Accept for (c): a logical shift inserts a 0 into the MSB, so the number is no longer negative
> 
> Accept for (c): the point made with the values, the arithmetic shift gives -14 and the logical shift gives +50
> 
> Do not accept `11110010` as the answer to (a), or `00110010` as the answer to (b)
> 
> Do not accept "the arithmetic shift leaves the number unchanged", the value is still divided by 4

> **[exam-tip]**
> Students often fill the left-hand end with a 0 out of habit and then write the same answer twice. The only difference between the two shifts is what enters at the left, so decide that first: a logical shift always brings in a 0, an arithmetic shift always brings in a copy of the bit already in the MSB. Here the MSB is a 1, so two 1s enter and the answer starts `1111`.
> 
> Say "copies the sign bit", not "keeps the number the same". An arithmetic right shift still divides the value, it just keeps the sign correct while doing it.

### Q6
**(a)** Contents of the ACC after the shift: `01011000` **[1]**

**(b)** Denary value after the shift: 88 **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `01011000`
> 
> **1 mark** for 88
> 
> Accept the bits written with a space, `0101 1000`
> 
> Do not accept `00000101`, which is a right shift instead of a left shift
> 
> Do not accept an answer with more or fewer than 8 bits, such as `0101100000`
> 
> Do not accept 5 or 44

> **[exam-tip]**
> The two mistakes here are direction and width. On a left logical shift the bits move towards the most significant end and the zeros come in at the right-hand end, so `00010110` becomes `01011000` and not `00000101`. Read the words "left" and "right" in the question before you write anything.
> 
> The register does not get wider. It holds 8 bits before the shift and 8 bits after it, so never add extra columns to make room for the bits you have moved.

### Q7
> **[mark-scheme]**
> (i) 0000 0101
> 
> (ii) 0000 0010
> 
> (iii) 1101 0010

### Q8
> **[mark-scheme]**
> **1 mark** for each correct answer:
> 
> | **Instruction number** | Instruction | ACC content |
> |---|---|---|
> | **1** | `LSL #2` | **1111 1100** |
> | **2** | `XOR 100` | **1111 0010** |
> | **3** | `AND 103` | **0011 0111** |

### Q9
> **[mark-scheme]**
> **1 mark for** each correct answer:
> 
> | **Program number** | Code | ACC content |
> |---|---|---|
> | **1** | `XOR 29` | **0100 1001** |
> | **2** | `AND #29` | **0000 0100** |
> | **3** | `OR B11111111` | **1111 1111** |

### Q10
> **[mark-scheme]**
> **1 mark** for each correct answer:
> 
> | Program number | Code | ACC content |
> |---|---|---|
> | 1 | `AND 31` | **1001 1010** |
> | 2 | `XOR B01001111` | **1101 0101** |
> | 3 | `OR #30` | **1001 1110** |

### Q11
**1 mark** each:

- A logical shift moves all bits to the right and inserts zeros in the appropriate leftmost bits
- An arithmetic shift moves all bits to the right but copies the sign bit into the Most Significant Bit (MSB)

### Q12
> **[mark-scheme]**
> **1 mark** for each bullet point for the explanation
> 
> **1 mark** for correct instruction
> 
> - A bit manipulation operation is required to set all the bits to zero
> - Compare the result of the masking with 0
> - … the result of comparison will be true if the register is cleared
> - AND B00000000 / #00 / &00

### Q13
> **[mark-scheme]**
> (i) **1 mark** each correct content of ACC
> 
> |   | Instructions | ACC content |
> |---|---|---|
> | 1 | `LSL #2` | **0110 1000** |
> | 2 | `ADD #5`<br>`AND #30` | **0001 1110** |
> | 3 | `OR B11110010`<br>`INC ACC` | **1111 1011** |
> 
> (ii)** 1 mark** each to **max 2** for explanation
> 
> - An odd binary number will have a 1 in the Least Significant Bit (LSB)
> - A bit manipulation operation is required to access/mask only the LSB and clear all the others
> - Compare the result of the masking with denary 1
> - … the result of the comparison will be true if the number is odd
> 
> **1 mark** for correct instruction
> 
> - AND B00000001 // AND #1 // AND &01
