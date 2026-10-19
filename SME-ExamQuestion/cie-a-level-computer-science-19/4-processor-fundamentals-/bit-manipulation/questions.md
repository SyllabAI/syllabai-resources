# Exam Questions — Bit Manipulation
**4. Processor Fundamentals** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 13 questions across 1 sets


## Exam Questions (13 questions)


### Q1 — hard — 4 marks

**Q1** [4 marks]

A building security system uses an 8-bit status register. Each bit reports one sensor. A bit is set to 1 when its sensor has been triggered and is 0 when it has not.

The table shows which sensor each bit reports.

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Sensor | front door | window | motion | smoke | heat | glass | gate | panic button |

The system must raise a full alarm only when the window sensor and the motion sensor have **both** been triggered.

Explain how bit masking is used to carry out this test. Your answer must include the 8-bit mask, the bitwise operation used, and how the result of the operation is interpreted.

Use the status register contents `01001010` as an example in your answer.

### Q2 — medium — 3 marks

**Q2** [3 marks]

An automated greenhouse is controlled by an 8-bit control register. Each bit controls one device. A bit set to 1 switches its device on. A bit set to 0 switches its device off.

The table shows which device each bit controls.

| Place value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|---|
| Device | alarm | pump | fan | heater | lamp | vent | mister | door |

The control register currently holds `01001010`.

The fan must be switched on. No other device may change state.

(a) Give the 8-bit mask that must be used.

(b) State the bitwise operation that must be used with this mask.

(c) Show the contents of the control register after the operation has been carried out.

### Q3 — easy — 2 marks

**Q3** [2 marks]

The table shows part of the instruction set for a processor. The processor has one general purpose register, the Accumulator (ACC).

| Instruction | Explanation |   |
|---|---|---|
| Opcode | Operand |   |
| AND | Bn | Bitwise AND operation of the contents of ACC with the operand |
| OR | Bn | Bitwise OR operation of the contents of ACC with the operand |

B denotes a binary number, for example `B01001010`.

The binary value `01101101` is loaded into the ACC before each instruction is executed.

Complete the table to show the contents of the ACC after each instruction has been executed.

| Instruction | ACC contents after the instruction |
|---|---|
| `AND B00001111` |   |
| `OR B10000000` |   |

### Q4 — hard — 4 marks

**Q4** [4 marks]

An 8-bit register holds an unsigned binary integer.

The register currently holds `01101001`.

A programmer wants to multiply the value in the register by 4. The programmer carries out a 2-place left logical shift on the register.

(a) Show the contents of the register after the shift.

(b) Give the denary value held in the register before the shift and after the shift.

(c) Explain why the shift has not multiplied the value by 4.

### Q5 — medium — 3 marks

**Q5** [3 marks]

An 8-bit register holds the two's complement binary integer `11001010`.

(a) Show the contents of the register after a 2-place right logical shift.

(b) Show the contents of the register after a 2-place right arithmetic shift.

(c) Explain why a right arithmetic shift is used instead of a right logical shift when the register holds a negative two's complement integer.

### Q6 — easy — 2 marks

**Q6** [2 marks]

A processor has one general purpose register, the Accumulator (ACC).

The ACC holds the unsigned binary integer `00010110`.

A 2-place left logical shift is carried out on the contents of the ACC.

(a) Show the contents of the ACC after the shift.

(b) Give the denary value held in the ACC after the shift.

### Q7 — medium — 3 marks

**Q7** [3 marks]

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


### Q8 — medium — 1 marks

**Q8** [1 mark]

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


### Q9 — medium — 3 marks

**Q9** [3 marks]

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


### Q10 — medium — 3 marks

**Q10** [3 marks]

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


### Q11 — medium — 2 marks

**Q11** [2 marks]

Describe the difference between a right logical binary shift and a right arithmetic binary shift.

*Source: Nov 2024 9618/13 Q8C*


### Q12 — medium — 3 marks

**Q12** [3 marks]

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


### Q13 — medium — 6 marks

**Q13** [6 marks]

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

