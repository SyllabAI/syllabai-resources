# Exam Questions — Bit Manipulation
**4. Processor Fundamentals** · Cambridge (CIE) AS computer-science (9618)
> Source: [https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/) · 7 questions across 1 sets


## Exam Questions (7 questions)


### Q1 — medium — 3 marks

**Q1** [3 marks]

The following table shows another part of the instruction set for the same processor.

| Instruction | Explanation |   |
|---|---|---|
| **Opcode** | Operand |   |
| `AND` | `Bn` | Bitwise AND operation of the contents of ACC with the operand |
| `XOR` | `Bn` | Bitwise XOR operation of the contents of ACC with the operand |
| `LSR` | `#n` | Bits in ACC are shifted logically n places to the right. Zeros are introduced on the left hand end |
| # denotes a denary number, e.g. #123 <br>B denotes a binary number, e.g. B01001101 |   |   |

(i) The current contents of the ACC are:

| 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 |
|---|---|---|---|---|---|---|---|

Show the contents of the ACC after the execution of the following instruction.

`AND B10100101`

(1)

(ii) The current contents of the ACC are:

| 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 |
|---|---|---|---|---|---|---|---|

Show the contents of the ACC after the execution of the following instruction.

`LSR #3`

(1)

(iii)  The current contents of the ACC are:

| 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 |
|---|---|---|---|---|---|---|---|

Show the contents of the ACC after the execution of the following instruction.

`XOR B00100101`

(1)

*Source: Nov 2023 9618/11 Q8C*


### Q2 — medium — 1 marks

**Q2** [1 mark]

The processor includes these bit manipulation instructions:

| Instruction | Explanation |   |
|---|---|---|
| Opcode | Operand |   |
| `AND` | `#n / Bn / &n` | Bitwise AND operation of the contents of ACC with the operand |
| `AND` | `<address>` | Bitwise AND operation of the contents of ACC with the contents of <address> |
| `XOR` | `#n / Bn / &n` | Bitwise XOR operation of the contents of ACC with the operand |
| `XOR` | `<address>` | Bitwise XOR operation of the contents of ACC with the contents of <address> |
| `OR` | `#n / Bn / &n` | Bitwise OR operation of the contents of ACC with the operand |
| `OR` | `<address>` | Bitwise OR operation of the contents of ACC with the contents of <address> |
| `LSL` | `#n` | Bits in ACC are shifted logically n places to the left. Zeros are introduced on the right-hand end |
| `LSR` | `#n` | Bits in ACC are shifted logically n places to the right. Zeros are introduced on the left-hand end |
| <address> can be an absolute or a symbolic address<br># denotes a denary number, e.g. #123 <br>B denotes a binary number, e.g. B01001010<br>& denotes a hexadecimal number, e.g. &4A |   |   |

The current contents of memory are shown:

| **Address** | Data |
|---|---|
| **100** | 00001101 |
| **101** | 10111110 |
| **102** | 11110011 |
| **103** | 00110111 |
| **104** | 00000000 |

The current content of the ACC is shown:

| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
|---|---|---|---|---|---|---|---|

Complete the table by writing the content of the ACC after each instruction has run.

The binary number 11111111 is reloaded into the ACC before each instruction is run.

| **Instruction number** | Instruction | ACC content |
|---|---|---|
| **1** | `LSL #2` |   |
| **2** | `XOR 100` |   |
| **3** | `AND 103` |   |

*Source: June 2024 9618/13 Q3B*


### Q3 — medium — 3 marks

**Q3** [3 marks]

The processor includes these bit manipulation instructions:

| Instruction | Explanation |   |
|---|---|---|
| Opcode | Operand |   |
| `AND` | `#n/Bn/&n` | Bitwise AND operation of the contents of ACC with the operand |
| `AND` | `<address>` | Bitwise AND operation of the contents of ACC with the contents of <address> |
| `XOR` | `#n/Bn/&n` | Bitwise XOR operation of the contents of ACC with the operand |
| `XOR` | `<address>` | Bitwise XOR operation of the contents of ACC with the contents of <address> |
| `OR` | `#n/Bn/&n` | Bitwise OR operation of the contents of ACC with the operand |
| `OR` | `<address>` | Bitwise OR operation of the contents of ACC with the contents of <address> |
| <address> can be an absolute or a symbolic address<br># denotes a denary number, e.g. #123 <br>B denotes a binary number, e.g. B01001010<br>& denotes a hexadecimal number, e.g. &4A |   |   |

The current contents of memory are shown:

| **Address** | Data |
|---|---|
| **25** | 11000110 |
| **26** | 11100001 |
| **27** | 10000001 |
| **28** | 11001101 |
| **29** | 00001111 |

The current content of the ACC is shown:

| 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 |
|---|---|---|---|---|---|---|---|

Complete the table by writing the content of the ACC after each program has run.

The binary number 01000110 is reloaded into the ACC before each program is run.

| **Program number** | Code | ACC content |
|---|---|---|
| **1** | `XOR 29` |   |
| **2** | `AND #29` |   |
| **3** | `OR B11111111` |   |

*Source: June 2024 9618/12 Q5B*


### Q4 — medium — 3 marks

**Q4** [3 marks]

The processor includes these bit manipulation instructions:

| Instruction | Explanation |   |
|---|---|---|
| Opcode | Operand |   |
| `AND` | `#n/Bn/&n` | Bitwise AND operation of the contents of ACC with the operand |
| `AND` | `<address>` | Bitwise AND operation of the contents of ACC with the contents of <address> |
| `XOR` | `#n/Bn/&n` | Bitwise XOR operation of the contents of ACC with the operand |
| `XOR` | `<address>` | Bitwise XOR operation of the contents of ACC with the contents of <address> |
| `OR` | `#n/Bn/&n` | Bitwise OR operation of the contents of ACC with the operand |
| `OR` | `<address>` | Bitwise OR operation of the contents of ACC with the contents of <address> |
| <address> can be an absolute or a symbolic address<br># denotes a denary number, e.g. #123 <br>B denotes a binary number, e.g. B01001010<br>& denotes a hexadecimal number, e.g. &4A |   |   |

The current contents of memory are shown:

| Address | Data |
|---|---|
| **30** | 01110101 |
| **31** | 11111111 |
| **32** | 00000000 |
| **33** | 11001100 |
| **34** | 10101010 |

The current content of the ACC is shown:

| 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
|---|---|---|---|---|---|---|---|

Complete the table by writing the content of the ACC after each program has run.

The binary number 10011010 is reloaded into the ACC before each program is run.

| Program number | Code | ACC content |
|---|---|---|
| 1 | `AND 31` |   |
| 2 | `XOR B01001111` |   |
| 3 | `OR #30` |   |

*Source: June 2024 9618/11 Q4B*


### Q5 — medium — 2 marks

**Q5** [2 marks]

Describe the difference between a right logical binary shift and a right arithmetic binary shift.

*Source: Nov 2024 9618/13 Q8C*


### Q6 — medium — 3 marks

**Q6** [3 marks]

The instruction set also includes these bit manipulation instructions:

| Instruction | Explanation |   |
|---|---|---|
| Opcode | Operand |   |
| `AND` | `#n/Bn/&n` | Bitwise AND operation of the contents of ACC with the operand |
| `AND` | `<address>` | Bitwise AND operation of the contents of ACC with the contents of <address> |
| `XOR` | `#n/Bn/&n` | Bitwise XOR operation of the contents of ACC with the operand |
| `XOR` | `<address>` | Bitwise XOR operation of the contents of ACC with the contents of <address> |
| `OR` | `#n/Bn/&n` | Bitwise OR operation of the contents of ACC with the operand |
| `OR` | `<address>` | Bitwise OR operation of the contents of ACC with the contents of <address> |
| <address> can be an absolute or a symbolic address<br># denotes a denary number, e.g. #123 <br>B denotes a binary number, e.g. B01001010<br>& denotes a hexadecimal number, e.g. &4A |   |   |

Explain how bit manipulation can be used to clear the data in an 8-bit register.

Write the bit manipulation instruction that will be used.

*Source: Nov 2024 9618/13 Q7B*


### Q7 — medium — 6 marks

**Q7** [6 marks]

The instruction set also includes these bit manipulation instructions:

| Instruction | **Explanation** |   |
|---|---|---|
| Opcode | Operand |   |
| `AND` | `#n/Bn/&n` | BitwiseAND operation of the contents ofACC with the operand |
| `AND` | `<address>` | Bitwise AND operation of the contents of ACC with the contents of <address> |
| `XOR` | `#n/Bn/&n` | Bitwise XOR operation of the contents ofACC with the operand |
| `XOR` | `<address>` | Bitwise XOR operation of the contents of ACC with the contents of <address> |
| `OR` | `#n/Bn/&n` | Bitwise OR operation of the contents ofACC with the operand |
| `OR` | `<address>` | Bitwise OR operation of the contents of ACC with the contents of <address> |
| `LSL` | `#n` | Bits in ACC are shifted logically n places to the left. Zeros are introduced on the right-hand end |
| `LSR` | `#n` | Bits in ACC are shifted logically n places to the right. Zeros are introduced on the left-hand end |
| <address> can be an absolute or a symbolic address<br># denotes a denary number, e.g. #123 <br>B denotes a binary number, e.g. B01001010<br>& denotes a hexadecimal number, e.g. &4A |   |   |

The current content of the ACC is shown:

| ACC | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|

The table has three sets of instructions. The binary number 10011010 is reloaded into the ACC before each set of instructions is run.

Complete the table by writing the content of the ACC after each set of instructions has run.

|   | Instructions | ACC content |
|---|---|---|
| 1 | `LSL #2` |   |
| 2 | `ADD #5`<br>`AND #30` |   |
| 3 | `OR B11110010`<br>`INC ACC` |   |

(3)

(ii)  Explain how bit manipulation can be used to test whether the binary number stored in the ACC represents an odd denary number.

Write the bit manipulation instruction that will be used.

(3)

*Source: Nov 2024 9618/12 Q8B*

