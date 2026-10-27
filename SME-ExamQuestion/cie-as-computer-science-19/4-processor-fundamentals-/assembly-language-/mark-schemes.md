# Mark Schemes — Assembly Language
**4. Processor Fundamentals** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (7 questions)


### Q1
> **[mark-scheme]**
> **1 mark** for each bullet point
> 
> - `IN `- Input **and **output of data
> - `ADD `- Arithmetic operations
> - `JPE `- Unconditional and conditional instructions
> - `CMI `- Compare instructions
> **[mark-scheme]**
> **1 mark** for each set of shaded rows
> 
> ![Table with columns: Instruction Address, ACC, IX, Memory Address (100-111), and Output. Rows show numerical data and an 'A' at address 22.](assets/002-table-with-columns-instruction-address-acc-ix-me.png)

### Q2
> **[mark-scheme]**
> **1 mark** for:
> 
> - To create a symbol table
> **[mark-scheme]**
> (i) **1 mark **for each bullet point
> 
> - Data movement: e.g. LDR #50 // STO 201
> - Arithmetic operation: e.g. ADD 100 // INC IX
> - Conditional instruction: e.g. JPE 96
> 
> (ii)** 1 mark** for each bullet point (**max 2**)
> 
> Similarity:
> 
> - both load the contents of an address into the Accumulator
> 
> Difference:
> 
> - direct accesses the address given by the operand whereas indexed adds the contents of IX to the operand and accesses the data at that calculated address
> 
> (iii) **1 mark** for
> 
> - Indirect (addressing)
> - Relative (addressing)

### Q3
> **[mark-scheme]**
> **1 mark **for each correct answer:
> 
> | Program number | Instructions | ACC content |
> |---|---|---|
> | 1 | `LDM #50 `<br>`INC ACC `<br>`SUB #1` | **50** |
> | 2 | `LDI 51 `<br>`ADD 52` | **97** |
> | 3 | `LDR #2 `<br>`LDX 50 `<br>`DEC ACC` | **48** |
> | 4 | `LDD 52 `<br>`SUB 54 `<br>`INC ACC` | **44** |

### Q4
> **[mark-scheme]**
> **1 mark** for each correct answer:
> 
> | Program number | Instructions | ACC content |
> |---|---|---|
> | 1 | `LDI 15 `<br>`SUB #1` | **11** |
> | 2 | `LDD 14 `<br>`ADD 11` | **13** |
> | 3 | `LDM #11 `<br>`ADD #3 `<br>`SUB 16` | **2** |
> | 4 | `LDR #2`<br>`LDX 14 `<br>`ADD #2` | **14** |

### Q5
> **[mark-scheme]**
> **1 mark **for each correct answer:
> 
> | Program number | Instructions | ACC content |
> |---|---|---|
> | 1 | `LDD 20`<br>`ADD #2` | **4** |
> | 2 | `LDX 22` | **5** |
> | 3 | `LDI 25`<br>`INC ACC `<br>`SUB 22` | **1** |
> | 4 | `LDD 19`<br>`LDM #5`<br>`LDM #25` | **25** |

### Q6
> **[mark-scheme]**
> **1 mark **each:
> 
> |   | Instructions | ACC content |
> |---|---|---|
> | 1 | `LDD 50 `<br>`ADD #4 `<br>`ADD 54` | **158** |
> | 2 | `LDI 53 `<br>`DEC ACC `<br>`ADD 56` | **99** |
> | 3 | `LDM #55 `<br>`SUB #5` | **50** |

### Q7
> **[mark-scheme]**
> **1 mark** for each correct content of the ACC (4) 
> **1 mark** for correct IX column
> 
> |   | Instructions | ACC content | IX content |
> |---|---|---|---|
> | 1 | `LDM #19`<br>`DEC ACC` | **18** | **20** |
> | 2 | `LDD 23`<br>`ADD 19` | **40** | **20** |
> | 3 | `LDI 25`<br>`INC ACC` | **5** | **20** |
> | 4 | `LDR #21`<br>`LDX 2` | **15** | **21** |
