# Mark Schemes — Bit Manipulation
**4. Processor Fundamentals** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (7 questions)


### Q1
> **[mark-scheme]**
> (i) 0000 0101
> 
> (ii) 0000 0010
> 
> (iii) 1101 0010

### Q2
> **[mark-scheme]**
> **1 mark** for each correct answer:
> 
> | **Instruction number** | Instruction | ACC content |
> |---|---|---|
> | **1** | `LSL #2` | **1111 1100** |
> | **2** | `XOR 100` | **1111 0010** |
> | **3** | `AND 103` | **0011 0111** |

### Q3
> **[mark-scheme]**
> **1 mark for** each correct answer:
> 
> | **Program number** | Code | ACC content |
> |---|---|---|
> | **1** | `XOR 29` | **0100 1001** |
> | **2** | `AND #29` | **0000 0100** |
> | **3** | `OR B11111111` | **1111 1111** |

### Q4
> **[mark-scheme]**
> **1 mark** for each correct answer:
> 
> | Program number | Code | ACC content |
> |---|---|---|
> | 1 | `AND 31` | **1001 1010** |
> | 2 | `XOR B01001111` | **1101 0101** |
> | 3 | `OR #30` | **1001 1110** |

### Q5
**1 mark** each:

- A logical shift moves all bits to the right and inserts zeros in the appropriate leftmost bits
- An arithmetic shift moves all bits to the right but copies the sign bit into the Most Significant Bit (MSB)

### Q6
> **[mark-scheme]**
> **1 mark** for each bullet point for the explanation
> 
> **1 mark** for correct instruction
> 
> - A bit manipulation operation is required to set all the bits to zero
> - Compare the result of the masking with 0
> - … the result of comparison will be true if the register is cleared
> - AND B00000000 / #00 / &00

### Q7
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
