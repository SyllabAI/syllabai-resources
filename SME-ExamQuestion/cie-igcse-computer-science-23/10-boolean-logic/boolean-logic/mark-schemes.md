# Mark Schemes — Boolean Logic
**10. Boolean Logic** · Cambridge (CIE) IGCSE computer-science (0478 & 0984)


## Exam Questions (11 questions)


### Q1
![Logic circuit diagram with NOT, OR, and AND gates, labelled inputs R, S, T, and output Z. Connections illustrate logic flow among the gates.](assets/002-logic-circuit-diagram-with-not-or-and-and-gates-.png)

- **Each **correct gate, with the correct input(s) as shown **[1 mark]**
| `R` | `S` | `T` | `Z` |
|---|---|---|---|
| `0` | `0` | `0` | `1` |
| `0` | `0` | `1` | `1` |
| `0` | `1` | `0` | `1` |
| `0` | `1` | `1` | `0` |
| `1` | `0` | `0` | `1` |
| `1` | `0` | `1` | `0` |
| `1` | `1` | `0` | `1` |
| `1` | `1` | `1` | `1` |

- Eight correct outputs **[4 marks]**
- Six or seven correct outputs **[3 marks]**
- Four or five correct outputs **[2 marks]**
- Two or three correct outputs **[1 marks]**

### Q2
The Boolean expression for the logic diagram can be expressed as:

- `P = (A AND B) OR (NOT C)` **OR  **`P = (A ^ B) V (¬C)`
- `(A AND B)` **[1 mark]**
- `(NOT C)` **[1 mark]**
- `(A AND B) OR (NOT C)` **[1 mark]**

> **[exam-tip]**
> Use parentheses to group each gate's output so the operator precedence is unambiguous
> 
> Match each gate exactly — an OR gate is an inclusive OR, not XOR

### Q3
The completed logic circuit is:

![Logic circuit diagram with inputs labeled A, B, and C. Includes NOT, AND, and OR gates leading to a single output labeled X.](assets/005-logic-circuit-diagram-with-inputs-labeled-a-b-an.png)

- Each correct logic gate with correct input(s) **[1 mark]**
The completed truth table is:

| **A** | **B** | **C** | **X** |
|---|---|---|---|
| 0 | 0 | 0 | **0** |
| 0 | 0 | 1 | **1** |
| 0 | 1 | 0 | **0** |
| 0 | 1 | 1 | **1** |
| 1 | 0 | 0 | **0** |
| 1 | 0 | 1 | **1** |
| 1 | 1 | 0 | **0** |
| 1 | 1 | 1 | **1** |

- 8 correct outputs **[4 marks]**
- 6/7 correct outputs **[3 marks]**
- 4/5 correct outputs **[2 marks]**
- 2/3 correct outputs **[1 mark]**

### Q4
The completed truth table is:

| **A** | **B** | **C** | **X** |
|---|---|---|---|
| 0 | 0 | 0 | **0** |
| 0 | 0 | 1 | **0** |
| 0 | 1 | 0 | **0** |
| 0 | 1 | 1 | **0** |
| 1 | 0 | 0 | **0** |
| 1 | 0 | 1 | **1** |
| 1 | 1 | 0 | **0** |
| 1 | 1 | 1 | **0** |

- 8 correct outputs **[4 marks]**
- 6/7 correct outputs **[3 marks]**
- 4/5 correct outputs **[2 marks]**
- 2/3 correct outputs **[1 mark]**

### Q5
The completed logic circuit is:

![Diagram of a logic circuit with three inputs (A, B, C) and one output (Z), showing an AND gate connected to two OR gates and a NOT gate.](assets/007-diagram-of-a-logic-circuit-with-three-inputs-a-b.png)

- Each correct gate, with the correct input(s) as shown **[1 mark]**
The completed truth table is:

| **A** | **B** | **C** | **X** |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

- Eight correct outputs **[4 marks]**
- Six or seven correct outputs **[3 marks]**
- Four or five correct outputs **[2 marks]**
- Two or three correct outputs **[1 mark]**

### Q6
The completed logic circuit is:

![Logic circuit with inputs A, B, and C. OR gate processes A and B, connecting to an AND gate. C and B inputs connect to an OR gate, then an inverter. Outputs connect to an AND gate.](assets/009-logic-circuit-with-inputs-a-b-and-c-or-gate-proc.png)

- Each correct logic gate with correct input(s) **[1 mark]**
The completed truth table is:

| **A** | **B** | **C** | **X** |
|---|---|---|---|
| 0 | 0 | 0 | **0** |
| 0 | 0 | 1 | **0** |
| 0 | 1 | 0 | **0** |
| 0 | 1 | 1 | **1** |
| 1 | 0 | 0 | **0** |
| 1 | 0 | 1 | **0** |
| 1 | 1 | 0 | **0** |
| 1 | 1 | 1 | **1** |

- 8 correct outputs **[4 marks]**
- 6/7 correct outputs **[3 marks]**
- 4/5 correct outputs **[2 marks]**
- 2/3 correct outputs **[1 mark]**

### Q7
The completed logic circuit would be:

![Logic circuit diagram with inputs A, B, and C, featuring AND, OR, and NOT gates, ultimately producing output X.](assets/011-logic-circuit-diagram-with-inputs-a-b-and-c-feat.png)

- Each correct** NOT gate** and **OR gate** with correct direction of input(s) **[4 marks]**
- Four correct** AND** gates **[3 marks]** 
or
- Three correct **AND **gates **[2 marks]** 
or
- Two correct **AND **gates with correct direction of inputs **[1 mark]**
The logic expression would be:

- `X = ((A AND NOT B AND NOT C) OR (A AND B AND C)) `
- `(A AND NOT B AND NOT C) `**[1 mark]**
- `OR `**[1 mark]**
- `(A AND B AND C)` **[1 mark]**

### Q8
The completed logic circuit would be:

![Logic circuit with inputs A, B, and C connected to AND, NOT, and OR gates. Output X is produced by an OR gate receiving signals from two AND gates.](assets/013-logic-circuit-with-inputs-a-b-and-c-connected-to.png)

- each correct gate, with the correct input(s) as shown** [1 mark]**
| **A** | **B** | **C** | **X** |
|---|---|---|---|
| 0 | 0 | 0 | **0** |
| 0 | 0 | 1 | **0** |
| 0 | 1 | 0 | **1** |
| 0 | 1 | 1 | **0** |
| 1 | 0 | 0 | **0** |
| 1 | 0 | 1 | **0** |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | **1** |

- Eight correct outputs **[4 marks]**
- Six or seven correct outputs **[3 marks]**
- Four or five correct outputs **[2 marks]**
- Two or three correct outputs **[1 mark]**

### Q9
![Diagram matching logic gates to their standard symbols: AND gate to its symbol; OR gate to its symbol; NAND gate to its symbol; NOT gate to its symbol.](assets/015-diagram-matching-logic-gates-to-their-standard-s.png)

### Q10
| **A** | **B** | **P** |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | **1 ****[1 mark]** |
| 1 | 0 | **1 ****[1 mark]** |
| 1 | 1 | 0 |
| **A** | **B** | **Q** |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| **1 ****[1 mark]** | 0 | **1 ****[1 mark]** |
| 1 | **1 ****[1 mark]** | **1 ****[1 mark]** |

**Final answer:** **[Total: 4 marks]**
