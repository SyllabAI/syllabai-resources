# Mark Schemes — Programming Paradigms
**20. Further Programming** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (15 questions)


### Q1
Original pseudocode outputs: **40, 30, 20** **[1]**

Changed pseudocode outputs: **50, 40, 30** **[1]**

In an imperative language the statements are a sequence of commands that are carried out in the order they are written **[1]**

Each assignment changes the value of the variable `Stock`, so the output depends on whether it runs before or after the assignment. The same statements in a different order give a different result **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for original outputs 40, 30, 20 (all three, in this order)
> 
> **1 mark** for changed outputs 50, 40, 30 (all three, in this order)
> 
> **Explanation, any two from:**
> 
> - statements are a sequence of commands / instructions
> - carried out in the order they are written / given
> - each statement changes something in the program run // the value of `Stock` changes after line 05 runs
> - the output shows the value of the variable at the moment the `OUTPUT` statement runs, so the order of statements decides the result
> 
> **[2 marks]**
> 
> Do not accept 20 as the only output for the original pseudocode: `OUTPUT` is inside the loop, so it runs three times

> **[exam-tip]**
> Two errors are common. First, students put the `OUTPUT` outside the loop in their head and give one value. Line 06 is before `NEXT Day`, so it runs on every pass. Second, students say the final value of `Stock` changes. It does not: it is 20 in both versions. What changes is the value that each `OUTPUT` sees, because the statements run in a different order.

### Q2
- It uses variables, `Balance` and `Week`, whose values are changed by assignment statements, for example `Balance ← Balance + 20.00` **[1]**
- The statements are a sequence of commands carried out in the order they are written: `Balance` is set to 100.00 before the loop starts, and it is output only after the loop ends **[1]**
- It relies on repetition: the `FOR` loop repeats the assignment four times **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - Uses variables (`Balance` / `Week`) …
> - … that are changed using assignment statements (`Balance ← Balance + 20.00`)
> - Relies on repetition / iteration (the `FOR` loop)
> - The statements are a sequence of commands …
> - … carried out in the order written / given (for example, `Balance` is set before the loop and output after it)
> - Each line changes something in the program run (for example, `Balance` goes from 100.00 to 120.00 on the first pass)
> 
> **[3 marks]**
> 
> Accept a characteristic stated on its own, without a link to the code, for example "uses variables" or "relies on iteration"

> **[exam-tip]**
> The question says "how this pseudocode shows", so quote the part of the code that shows each point where you can: "the `FOR` loop repeats the addition four times" is a clearer answer than "uses iteration". The mistake that loses marks is describing a characteristic of a different paradigm, such as facts, rules or goals, which this code does not show.

### Q3
| Label | Opcode | Operand | Mark |
|---|---|---|---|
|   | `LDM` | `#100` | **[1]** |
|   | `STO` | `Hundred` | **[1]** |
|   | `LDI` | `Ptr` | **[1]** |
|   | `SUB` | `Hundred` | **[1]** |
|   | `ADD` | `Bonus` | **[1]** |
|   | `STO` | `Score` |   |
|   | `END` |   |   |
| `Hundred:` | `#100` |   |   |
| `Ptr:` |   |   |   |
| `Bonus:` |   |   |   |
| `Score:` |   |   | **[1]** |

For example, if `Ptr` holds 450, address 450 holds 160 and `Bonus` holds 15, then `LDI Ptr` loads 160. Subtracting 100 gives 60, adding 15 gives 75, and 75 is stored in `Score`.

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for `LDM #100` seen
> 
> **1 mark** for storing the constant at a labelled address, for example `STO Hundred`, with that label (`Hundred:`) placed away from the program code
> 
> **1 mark** for `LDI Ptr`
> 
> **1 mark** for `SUB` with the labelled address of the constant, for example `SUB Hundred`
> 
> **1 mark** for `ADD Bonus`
> 
> **1 mark** for `STO Score`, with `Ptr:`, `Bonus:` and `Score:` labelled away from the program code
> 
> Accept any label name for the constant, for example `Const:` or `C100:`
> 
> Accept `ADD Bonus` before `SUB Hundred`, as long as `LDI Ptr` comes first. The result is the same
> 
> Accept the data area without `#100` beside the constant's label, because `STO` puts 100 there when the program runs
> 
> Accept the answer without `END`
> 
> Do not accept `LDD Ptr` for the third mark. That loads the address held in `Ptr`, not the value stored at that address
> 
> Do not accept `SUB #100`. `SUB` in the given instruction set takes an address only, which is why the constant must be stored first
> 
> Do not accept labels placed inside the program code, where the processor would try to run them as instructions

> **[exam-tip]**
> Students lose the most marks by writing `LDD Ptr`. `Ptr` holds an address, not the value you want. `LDD` would load that address itself, for example 450, and the whole calculation would be wrong. `LDI` goes to `Ptr`, reads the address, then loads the value stored there.
> 
> "Use only the given instruction set" means the table printed in the question, not every instruction you have learned. The full instruction set has `SUB #n`, but this table does not, so the constant has to be stored at a labelled address before it can be subtracted. Put every label in a data area after `END`, so the processor never runs it as an instruction.

### Q4
| Statement | True | False |
|---|---|---|
| Variables are changed by assignment statements. | **✓** |   |
| The program is written as a set of facts and rules. |   | **✓** |
| The statements are carried out in the order they are written. | **✓** |   |
| The programmer states what the result must be, not how to find it. |   | **✓** |
| Repetition is carried out using iteration, such as a loop. | **✓** |   |

All five rows correct **[2]**

**[2 marks]**

> **[mark-scheme]**
> **2 marks** for all five rows correct
> 
> **1 mark** for four rows correct
> 
> Do not award a mark for a row with both boxes ticked

> **[exam-tip]**
> Rows 2 and 4 describe the declarative paradigm, not the imperative one. Students often tick row 4 as true because they think every program must state its result. In an imperative language the programmer writes how to get the result, as a sequence of commands. Stating what is wanted, without the steps, is the declarative approach.

### Q5
(i)

The term wants(M, S) finds a sport S that member M wants to learn. **[1]**

The term qualified(C, S) uses the same variable S, so coach C must be qualified to teach that sport. **[1]**

The term NOT injured(M) excludes any member who is injured. **[1]**

All the operators and punctuation are correct, with exactly three terms. **[1]**

(ii) Who = chen, bilal **[1]**

(iii) Tariq is injured (clause 17), so NOT injured(tariq) is false and the rule can never succeed for him. **[1]**

**[6 marks]**

> **[mark-scheme]**
> **(i)**
> 
> **1 mark** for `wants(M, S)`
> 
> **1 mark** for `qualified(C, S)`, using the same variable for the sport as in the first mark point
> 
> **1 mark** for `injured(M)` inside a `NOT`
> 
> **1 mark** for all Boolean operators and punctuation correct (allow `,` for `AND`), with the correct number of terms and no additional lines of code
> 
> Example answers:
> 
> Accept the terms in any order
> 
> Accept any capitalised variable name for the sport, if the same name is used in both terms
> 
> Accept the rule with or without a full stop at the end
> 
> Do not award the fourth mark if extra terms are added, for example `coach(C)` or `member(M)`. The rule statement gives exactly three conditions
> 
> Do not award the second mark if the two sport variables differ, for example `wants(M, S)` and `qualified(C, T)`
> 
> **(ii)**
> 
> **1 mark** for chen, bilal
> 
> Accept the names in either order
> 
> Do not accept ana. Ana is qualified to teach swimming only, and Lena wants to learn judo
> 
> **(iii)**
> 
> **1 mark** for: Tariq is injured // `injured(tariq)` is a fact, so the `NOT injured(M)` condition fails
> 
> Do not accept "no coach is qualified to teach judo". Chen and Bilal are both qualified to teach judo

> **[exam-tip]**
> The sport does not appear in the head of the rule, but you still need a variable for it. Use the same variable, for example S, in both terms. If you write wants(M, S) and qualified(C, T), the two sports are not linked, and every coach would be matched with Lena, including Ana, who teaches only swimming.
> 
> In (iii), check every condition before you blame the facts. Two coaches are qualified to teach judo, so the goal fails because of the NOT condition, not because of the qualified facts.

### Q6
Program A is imperative (procedural):

- The programmer writes a sequence of commands that says **how** to find the students, and the commands are carried out in the order they are written **[1]**
- It uses repetition: the `FOR` loop checks each element of the array in turn, and the variable `Index` is given a new value on each pass **[1]**

Program B is declarative:

- The program is a set of facts, and the programmer only states **what** is needed, as the goal `member(X, chess)` **[1]**
- The programmer writes no loop and no steps; the query is used to satisfy the goal and the language finds every value of `X` that matches **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Program A (imperative), any two from:**
> 
> - A sequence of commands / statements
> - Carried out in the order they are written
> - The programmer states how to solve the problem (step by step)
> - Uses variables (`Index`) that are changed as the program runs
> - Relies on repetition / iteration (the `FOR` loop)
> 
> **[2 marks]**
> 
> **Program B (declarative), any two from:**
> 
> - The program is a set of facts (and rules)
> - The programmer states what is needed, not how to do it
> - Uses a query / goal
> - The language finds the values that satisfy the goal // no loop or order of steps is written by the programmer
> 
> **[2 marks]**
> 
> Maximum 2 marks for Program A and maximum 2 marks for Program B. Each point must be about the given program or the paradigm it shows
> 
> Do not accept "Program B is faster" or "Program B is shorter": neither is a characteristic of the paradigm

> **[exam-tip]**
> The command word is explain, and the question asks for a difference, so you need points about both programs. Students often write four points about Program A and nothing about Program B, which limits them to 2 marks. A good pair of points is: "Program A says how to find the students, step by step" and "Program B only says what is wanted, as a goal".

### Q7
(i)

This goal is one term, with the variable Stay in the room position. **[1]**

(It returns Stay = jade, opal.)

(ii)

The first term finds the rooms on the first floor. **[1]**

The second term, using the same variable Quiet, keeps only the rooms that also have a garden view. **[1]**

(It returns Quiet = pearl.)

**[3 marks]**

> **[mark-scheme]**
> **(i)**
> 
> **1 mark** for `roomtype(Stay, double)`
> 
> **(ii)**
> 
> **1 mark** for `floor(Quiet, first)`
> 
> **1 mark** for `view(Quiet, garden)` joined to the first term by a comma
> 
> Accept `AND` in place of the comma
> 
> Accept the two terms in either order
> 
> Accept a full stop at the end of either goal
> 
> Do not award the second mark in (ii) if the two terms use different variables, for example `floor(Quiet, first), view(Room, garden)`. The goal no longer requires one room to meet both conditions
> 
> Do not accept a goal that uses a constant in place of the variable, for example `roomtype(jade, double)`

> **[exam-tip]**
> The variable name is given in the question, so use it exactly as printed. It starts with a capital letter. A lower-case word such as quiet is a constant, not a variable, so the goal would search for a room called quiet.
> 
> In (ii), the same variable must appear in both terms. That is what links the conditions together, so the goal finds a room that is on the first floor **and** has a garden view.

### Q8
| Description | Programming paradigm |
|---|---|
| Each instruction has an opcode and an operand. The operand can use immediate, direct or indirect addressing. | **Low-level** **[1]** |
| The program is written as a set of facts and rules. A query is used to satisfy a goal. | **Declarative** **[1]** |
| Data and the methods that use the data are grouped together in a class. Objects are created as instances of the class. | **Object-oriented** **[1]** |
| Variables are changed by assignment statements. The statements are a sequence of commands that are carried out in the order they are written. | **Imperative (procedural)** **[1]** |

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each correct row
> 
> Row 1: low-level. Accept assembly / assembly language
> 
> Row 2: declarative
> 
> Row 3: object-oriented. Accept OOP
> 
> Row 4: imperative. Accept procedural

> **[exam-tip]**
> Row 4 is the one students most often get wrong. They see "sequence of commands" and write "low-level", because assembly code is also a list of instructions. Look for the words "variables" and "assignment statements": those describe an imperative (procedural) high-level language. The low-level row is the one that mentions an opcode, an operand and addressing.

### Q9
| Label | Opcode | Operand | Mark |
|---|---|---|---|
|   | `LDR` | `#3` | **[1]** |
|   | `LDX` | `Temps` | **[1]** |
|   | `ADD` | `Temps` | **[1]** |
|   | `STO` | `Sum` | **[1]** |
|   | `END` |   |   |

`LDR #3` puts 3 in the IX. The first reading is at offset 0 from `Temps`, so the fourth reading is at offset 3.

The code loads the value at 200 + 3 = 203, which is 26. It then adds the contents of address 200, which is 18. The value 44 is stored in `Sum`.

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `LDR #3`
> 
> **1 mark** for `LDX Temps` after the IX has been set
> 
> **1 mark** for `ADD Temps` to add the first reading
> 
> **1 mark** for `STO Sum` as the final store, with the sum of the first and fourth readings in the ACC
> 
> Accept the absolute address 200 in place of the label `Temps`, and 205 in place of `Sum`
> 
> Accept code that loads the first reading with `LDD Temps`, stores it with `STO Sum`, then uses `LDR #3`, `LDX Temps`, `ADD Sum` and `STO Sum`. Award the same four marks
> 
> Accept the answer without `END`
> 
> Do not accept `LDR #4`. That uses address 204 and adds the fifth reading
> 
> Do not accept `LDD 203` to load the fourth reading. That is direct addressing, and the question requires indexed addressing
> 
> Do not accept `LDD Temps` followed straight away by `LDX Temps` with nothing stored in between. `LDX` overwrites the ACC, so the first reading is lost

> **[exam-tip]**
> The most common error is `LDR #4` for the fourth reading. The IX holds an offset from the label, not a position number. The first reading is at `Temps` + 0, so the fourth reading is at `Temps` + 3.
> 
> The second error is order. There is only one general purpose register. Every load instruction replaces what is in the ACC, and this instruction set has no instruction to add an indexed value. So load the indexed value first, then use `ADD` for the value you can reach directly.

### Q10
A declarative program states what the problem is, not how to solve it, so there is no sequence of steps for the computer to follow. **[1]**

The program is made up of facts, such as `parent(maya, ravi).` in clause 01, and rules, such as `grandparent(G, C)` in clause 04. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - The program instructs the computer what needs to be done, instead of how to do it
> - The program is written using facts and rules (for example the `parent` facts and the `grandparent` rule)
> - A goal / query is satisfied by matching it against the facts and rules
> - A declarative language can be logical or functional
> 
> **[2 marks]**
> 
> Accept an answer that makes the facts and rules point in general terms, without quoting the program
> 
> Do not accept "the statements are carried out in the order they are written". That describes an imperative (procedural) language
> 
> Do not accept "it uses variables" on its own. Imperative programs use variables too

> **[exam-tip]**
> Students often write one vague line, such as "it says what, not how", and stop. That earns one mark at most. For the second mark, name the parts of the program: facts, rules, and the goal that is satisfied by using them.
> 
> Read the program you are given. Clause 04 is a rule because it contains `IF`; clauses 01 to 03 are facts because they are simply stated as true.

### Q11
Example 1: **Low-level** (assembly language) **[1]**

Example 2: **Object-oriented** (OOP) **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for Example 1: low-level
> 
> **1 mark** for Example 2: object-oriented
> 
> Accept assembly / assembly language for Example 1
> 
> Accept OOP for Example 2
> 
> Do not accept machine code for Example 1: the instructions are written as an opcode and an operand in text, which is assembly language, not binary machine code
> 
> Do not accept high-level for Example 2: high-level describes a type of language, not a programming paradigm

> **[exam-tip]**
> Many students write "high-level language" for code like Example 2. That is not a paradigm. The clue is the structure: a class, a private attribute and a constructor called `NEW` are object-oriented features. In Example 1, each line is an opcode such as `LDM` or `STO` with an operand, which tells you it is low-level code.

### Q12
> **[mark-scheme]**
> One mark for each correctly completed clause (Max 4)
> 
> `20 person(carlos).`
> 
> `21 hobby(cycling).`
> 
> `22 enjoys(carlos, cycling).`
> 
> `23 dislikes(carlos, music).`
> **[mark-scheme]**
> `P = toby, nina`
> **[mark-scheme]**
> One mark per mark point (Max 4)
> 
> - person(N)
> - hobby(H)
> - dislikes(N, H)
> - all logical operators correct with no additional code (see example answers)
> 
> Example answers:
> 
> might_enjoy(N, H)
> 
> `IF person(N) AND hobby(H) AND NOT dislikes(N, H)`
> 
> `might_enjoy(N, H)`
> 
> `IF NOT dislikes(N, H), person(N), hobby(H)`

### Q13
> **[mark-scheme]**
> One mark for each correctly completed clause (Max 3)
> 
> (`22) student(anthony).`
> 
> `(23) choice1(anthony, history).`
> 
> `(24) choice2(anthony, geography).`
> **[mark-scheme]**
> `X = tomaz, pietre, nico`
> **[mark-scheme]**
> One mark per mark point (Max 4)
> 
> - student(N)
> - subject(S)
> - choice1(N, S)
> - all logical operators correct with no additional code (see example
> 
> answers)
> 
> Example answers:
> 
> `may_choose_subject(N, S)`
> 
> `IF student(N) AND subject(S) AND NOT choice1(N, S)`
> 
> `may_choose_subject(N, S)`
> 
> `IF NOT choice1(N, S), student(N), subject(S)`

### Q14
> **[mark-scheme]**
> One mark for each correctly completed clause (Max 4)
> 
> Example answer
> 
> `(25) client(jane).`
> 
> `(26) activity(surfing).`
> 
> `(27) choice(jane, surfing).`
> 
> `(28) done(jane, sailing).`
> **[mark-scheme]**
> `(List =) frankie, erik, henry`
> **[mark-scheme]**
> One mark per mark point (Max 4)
> 
> MP1 `client(C)`
> 
> MP2 `activity(A)`
> 
> MP3 `done(C, A)`
> 
> MP4 all correct Boolean operators and punctuation (allow , for AND). There must be the correct number of terms and
> 
> no additional lines of code
> 
> Example answers
> 
> `may_choose_activity(C, A)`
> 
> `IF`
> 
> `client(C) AND activity(A) AND NOT done(C, A).`
> 
> `client(C), activity(A), NOT (done(C, A)).`

### Q15
> **[mark-scheme]**
> One mark for each correctly completed clause (Max 3)
> 
> - 23) feature(sliding_doors).
> - (24) available(sliding_doors, minivan).
> - (25) unavailable(sliding_doors, hatchback).
> **[mark-scheme]**
> `(Options =) sunroof, reversing_camera`
**One **mark per mark point (**Max 4**)

MP1 `feature(F)`

MP2 `bodystyle(B)`

MP3 `unavailable(F, B)`

MP4 all correct Boolean operators and punctuation (allow , for AND) and no additional lines of code

Example answers

`may_choose_option(F, B)`

`IF`

`feature(F) AND bodystyle(B) AND NOT unavailable(F, B).`

`feature(F), bodystyle(B), NOT unavailable(F, B).`
