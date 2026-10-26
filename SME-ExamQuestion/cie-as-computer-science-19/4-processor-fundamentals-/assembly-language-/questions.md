# Exam Questions — Assembly Language
**4. Processor Fundamentals** · Cambridge (CIE) AS computer-science (9618)
> Source: [https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/) · 7 questions across 1 sets


## Exam Questions (7 questions)


### Q1 — medium — 5 marks

**Q1** [4 marks]

The following table shows part of the instruction set for a processor. The processor has two registers, the Accumulator (ACC) and the Index Register (IX).

| **Instruction** | **Explanation** |   |
|---|---|---|
| Opcode | Operand |   |
| `LDD` | `<address>` | Direct addressing. Load the contents of the location at the given address to ACC |
| `LDX` | `<address>` | Indexed addressing. Form the address from <address> + the contents of the index register. Copy the contents of this calculated address to ACC |
| `LDR` | `#n` | Immediate addressing. Load the number n to IX |
| `STO` | `<address>` | Store the contents of ACC at the given address |
| `ADD` | `#n` | Add the denary number n to the ACC |
| `JMP` | `<address>` | Jump to the given address |
| `INC` | `<register>` | Add 1 to the contents of the register (ACC or IX) |
| `CMP` | `<address>` | Compare the contents of ACC with the contents of <address> |
| `CMI` | `<address>` | Indirect addressing. The address to be used is at the given address. Compare the contents of ACC with the contents of this second address |
| `JPE` | `<address>` | Following a compare instruction, jump to <address> if the compare was True |
| `IN` |   | Key in a character and store its ASCII value in ACC |
| `OUT` |   | Output to the screen the character whose ASCII value is stored in ACC |
| `END` |   | Return control to the operating system |
| <address> can be an absolute or a symbolic address<br># denotes a denary number, e.g. #123 |   |   |

The instructions in the processor’s instruction set can be grouped according to their function.

Identify the instruction group for each of the following opcodes.

`IN` .............................

`ADD `.........................

`JPE `...........................

`CMI` ...........................

*Source: Nov 2023 9618/12 Q9A*


**Q1** [1 mark]

The current contents of main memory and selected values from the ASCII character set are given on page 15.

Trace the program currently in memory using the trace table when the input is ‘1’.

![Table with computer instructions, memory addresses, and ASCII values. Includes instruction and output columns, memory values for addresses 100-111.](assets/001-table-with-computer-instructions-memory-addresse.png)

*Source: Nov 2023 9618/12 Q9B*


### Q2 — medium — 7 marks

**Q2** [1 mark]

Identify the purpose of the first pass of a two-pass assembler.

*Source: Nov 2023 9618/11 Q8A*


**Q2** [6 marks]

The following table shows part of the instruction set for a processor. The processor has two registers, the Accumulator (ACC) and the Index Register (IX).

| Instruction | Explanation |   |
|---|---|---|
| Opcode | Operand |   |
| `LDR` | `#n` | Immediate addressing. Load the number n to IX |
| `STO` | `<address>` | Store contents of ACC at the given address |
| `ADD` | `<address>` | Add the contents of the given address to the ACC |
| `INC` | `<register>` | Add 1 to the contents of the register (ACC or IX) |
| `CMP` | `#n` | Compare the contents of ACC with number n |
| `JPE` | `<address>` | Following a compare instruction, jump to <address> if the compare was True |
| `OUT` |   | Output to the screen the character whose ASCII value is stored in ACC |
| <address> can be an absolute or symbolic address<br><br># denotes a denary number, e.g. #123 |   |   |

(i) Give one example of an instruction that belongs to each of the following instruction groups.

Only use the instructions given in the table. Each instruction must have a suitable operand.

Data movement ...........................

Arithmetic operation ...................

Conditional instruction ................

(3)

(ii) The instruction` LDR #2` uses immediate addressing.

Give **one **similarity and **one **difference between direct addressing and indexed addressing.

(2)

(iii) Identify **one **other mode of addressing.

(1)

*Source: June 2024 9618/13 Q8B*


### Q3 — medium — 4 marks

**Q3** [4 marks]

The following table shows part of the instruction set for a processor. The processor has two registers: the Accumulator (ACC) and an Index Register (IX).

| **Instruction** | **Explanation** |   |
|---|---|---|
| **Opcode** | **Operand** |   |
| `LDM` | `#n` | Immediate addressing. Load the number n to ACC |
| `LDD` | `<address>` | Direct addressing. Load the contents of the location at the given address to ACC |
| `LDI` | `<address>` | Indirect addressing. The address to be used is at the given address. Load the contents of this second address to ACC |
| `LDX` | `<address>` | Indexed addressing. Form the address from <address> + the contents of the index register. Copy the contents of this calculated address to ACC |
| `LDR` | `#n` | Immediate addressing. Load the number n to IX |
| `ADD` | `#n/Bn/&n` | Add the number n to the ACC |
| `ADD` | `<address>` | Add the contents of the given address to the ACC |
| `SUB` | `#n/Bn/&n` | Subtract the number n from the ACC |
| `SUB` | `<address>` | Subtract the contents of the given address from the ACC |
| `INC` | `<register>` | Add 1 to the contents of the register (ACC or IX) |
| <address> can be an absolute or a symbolic address <br># denotes a denary number, e.g. #123 B <br>denotes a binary number, e.g. B01001010 <br>& denotes a hexadecimal number, e.g. &4A |   |   |

The current contents of memory are shown:

| Address | Data |
|---|---|
| **48** | 51 |
| **49** | 6 |
| **50** | 48 |
| **51** | 50 |
| **52** | 49 |
| **53** | 50 |
| **54** | 6 |

The current contents of the ACC and IX are shown:

| ACC | 2 |
|---|---|
| IX | 50 |

Complete the table by writing the content of the ACC after each program has run.

| Program number | Instructions | ACC content |
|---|---|---|
| 1 | `LDM #50 `<br>`INC ACC `<br>`SUB #1` |   |
| 2 | `LDI 51 `<br>`ADD 52` |   |
| 3 | `LDR #2 `<br>`LDX 50 `<br>`DEC ACC` |   |
| 4 | `LDD 52 `<br>`SUB 54 `<br>`INC ACC` |   |

*Source: June 2024 9618/13 Q3A*


### Q4 — medium — 4 marks

**Q4** [4 marks]

The following table shows part of the instruction set for a processor. The processor has two registers: the Accumulator (ACC) and an Index Register (IX).

| **Instruction** | **Explanation** |   |
|---|---|---|
| **Opcode** | **Operand** |   |
| `LDM` | `#n` | Immediate addressing. Load the number n to ACC |
| `LDD` | `<address>` | Direct addressing. Load the contents of the location at the given address to ACC |
| `LDI` | `<address>` | Indirect addressing. The address to be used is at the given address. Load the contents of this second address to ACC |
| `LDX` | `<address>` | Indexed addressing. Form the address from <address> + the contents of the index register. Copy the contents of this calculated address to ACC |
| `LDR` | `#n` | Immediate addressing. Load the number n to IX |
| `ADD` | `#n/Bn/&n` | Add the number n to the ACC |
| `ADD` | `<address>` | Add the contents of the given address to the ACC |
| `SUB` | `#n/Bn/&n` | Subtract the number n from the ACC |
| `SUB` | `<address>` | Subtract the contents of the given address from the ACC |
| `INC` | `<register>` | Add 1 to the contents of the register (ACC or IX) |
| <address> can be an absolute or a symbolic address <br># denotes a denary number, e.g. #123 B <br>denotes a binary number, e.g. B01001010 <br>& denotes a hexadecimal number, e.g. &4A |   |   |

The current contents of memory are shown:

| Address | Data |
|---|---|
| **10** | 1 |
| **11** | 3 |
| **12** | 5 |
| **13** | 11 |
| **14** | 10 |
| **15** | 16 |
| **16** | 12 |

The current contents of the ACC and IX are shown:

| ACC | 10 |
|---|---|
| IX | 0 |

Complete the table by writing the content of the ACC after each program has run.

| Program number | Instructions | ACC content |
|---|---|---|
| 1 | `LDI 15 `<br>`SUB #1` |   |
| 2 | `LDD 14 `<br>`ADD 11` |   |
| 3 | `LDM #11 `<br>`ADD #3 `<br>`SUB 16` |   |
| 4 | `LDR #2`<br>`LDX 14 `<br>`ADD #2` |   |

*Source: June 2024 9618/12 Q5A*


### Q5 — medium — 4 marks

**Q5** [4 marks]

The following table shows part of the instruction set for a processor. The processor has two registers: the Accumulator (ACC) and an Index Register (IX).

| **Instruction** | **Explanation** |   |
|---|---|---|
| **Opcode** | **Operand** |   |
| `LDM` | `#n` | Immediate addressing. Load the number n to ACC |
| `LDD` | `<address>` | Direct addressing. Load the contents of the location at the given address to ACC |
| `LDI` | `<address>` | Indirect addressing. The address to be used is at the given address. Load the contents of this second address to ACC |
| `LDX` | `<address>` | Indexed addressing. Form the address from <address> + the contents of the index register. Copy the contents of this calculated address to ACC |
| `LDR` | `#n` | Immediate addressing. Load the number n to IX |
| `ADD` | `#n/Bn/&n` | Add the number n to the ACC |
| `ADD` | `<address>` | Add the contents of the given address to the ACC |
| `SUB` | `#n/Bn/&n` | Subtract the number n from the ACC |
| `SUB` | `<address>` | Subtract the contents of the given address from the ACC |
| `INC` | `<register>` | Add 1 to the contents of the register (ACC or IX) |
| <address> can be an absolute or a symbolic address <br># denotes a denary number, e.g. #123 B <br>denotes a binary number, e.g. B01001010 <br>& denotes a hexadecimal number, e.g. &4A |   |   |

The current contents of memory are shown:

| Address | Data |
|---|---|
| **19** | 24 |
| **20** | 2 |
| **21** | 1 |
| **22** | 3 |
| **23** | 5 |
| **24** | 4 |
| **25** | 22 |

The current contents of the ACC and IX are shown:

| ACC | 12 |
|---|---|
| IX | 1 |

Complete the table by writing the content of the ACC after each program has run.

| Program number | Instructions | ACC content |
|---|---|---|
| 1 | `LDD 20`<br>`ADD #2` |   |
| 2 | `LDX 22` |   |
| 3 | `LDI 25`<br>`INC ACC `<br>`SUB 22` |   |
| 4 | `LDD 19`<br>`LDM #5`<br>`LDM #25` |   |

*Source: June 2024 9618/11 Q4A*


### Q6 — medium — 3 marks

**Q6** [3 marks]

The following table shows part of the instruction set for a processor. The processor has two registers, the Accumulator (ACC) and the Index Register (IX).

| **Instruction** | **Explanation** |   |
|---|---|---|
| **Opcode** | **Operand** |   |
| `LDM` | `#n` | Immediate addressing. Load the number n to ACC |
| `LDD` | `<address>` | Direct addressing. Load the contents of the location at the given address to ACC |
| `LDI` | `<address>` | Indirect addressing. The address to be used is at the given address. Load the contents of this second address to ACC |
| `LDX` | `<address>` | Indexed addressing. Form the address from <address> + the contents of the index register. Copy the contents of this calculated address to ACC |
| `LDR` | `#n` | Immediate addressing. Load the number n to IX |
| `ADD` | `#n/Bn/&n` | Add the number n to the ACC |
| `ADD` | `<address>` | Add the contents of the given address to the ACC |
| `SUB` | `#n/Bn/&n` | Subtract the number n from the ACC |
| `SUB` | `<address>` | Subtract the contents of the given address from the ACC |
| `INC` | `<register>` | Add 1 to the contents of the register (ACC or IX) |
| `DEC` | `<register>` | Subtract 1 from the contents of the register (ACC or IX) |
| <address> can be an absolute or a symbolic address <br># denotes a denary number, e.g. #123 B <br>denotes a binary number, e.g. B01001010 <br>& denotes a hexadecimal number, e.g. &4A |   |   |

The current contents of memory are shown:

| Address | Data |
|---|---|
| **50** | 54 |
| **51** | 55 |
| **52** | 50 |
| **53** | 52 |
| **54** | 100 |
| **55** | 25 |
| **56** | 50 |

The current contents of the ACC and IX are shown:

| ACC | 50 |
|---|---|
| IX | 45 |

Complete the table by writing the content of the ACC after each program has run.

|   | Instructions | ACC content |
|---|---|---|
| 1 | `LDD 50 `<br>`ADD #4 `<br>`ADD 54` |   |
| 2 | `LDI 53 `<br>`DEC ACC `<br>`ADD 56` |   |
| 3 | `LDM #55 `<br>`SUB #5` |   |

*Source: Nov 2024 9618/13 Q7A*


### Q7 — medium — 5 marks

**Q7** [5 marks]

The following table shows part of the instruction set for a processor. The processor has two registers, the Accumulator (ACC) and the Index Register (IX).

| **Instruction** | **Explanation** |   |
|---|---|---|
| **Opcode** | **Operand** |   |
| `LDM` | `#n` | Immediate addressing. Load the number n to ACC |
| `LDD` | `<address>` | Direct addressing. Load the contents of the location at the given address to ACC |
| `LDI` | `<address>` | Indirect addressing. The address to be used is at the given address. Load the contents of this second address to ACC |
| `LDX` | `<address>` | Indexed addressing. Form the address from <address> + the contents of the index register. Copy the contents of this calculated address to ACC |
| `LDR` | `#n` | Immediate addressing. Load the number n to IX |
| `ADD` | `#n/Bn/&n` | Add the number n to the ACC |
| `ADD` | `<address>` | Add the contents of the given address to the ACC |
| `SUB` | `#n/Bn/&n` | Subtract the number n from the ACC |
| `SUB` | `<address>` | Subtract the contents of the given address from the ACC |
| `INC` | `<register>` | Add 1 to the contents of the register (ACC or IX) |
| `DEC` | `<register>` | Subtract 1 from the contents of the register (ACC or IX) |
| <address> can be an absolute or a symbolic address <br># denotes a denary number, e.g. #123 B <br>denotes a binary number, e.g. B01001010 <br>& denotes a hexadecimal number, e.g. &4A |   |   |

The current contents of memory are shown:

| Address | Data |
|---|---|
| `19` | `25` |
| `20` | `23` |
| `21` | `2` |
| `22` | `4` |
| `23` | `15` |
| `24` | `50` |
| `25` | `22` |

The current contents of the ACC and IX are shown:

| ACC | 50 |
|---|---|
| IX | 20 |

Complete the table by writing the content of the ACC and the IX after each set of instructions has run.

|   | Instructions | ACC content | IX content |
|---|---|---|---|
| 1 | `LDM #19`<br>`DEC ACC` |   |   |
| 2 | `LDD 23`<br>`ADD 19` |   |   |
| 3 | `LDI 25`<br>`INC ACC` |   |   |
| 4 | `LDR #21`<br>`LDX 2` |   |   |

*Source: Nov 2024 9618/12 Q8A*

