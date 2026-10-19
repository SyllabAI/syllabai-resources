# Assembly Language

Course: cie-a-level-computer-science-19 · Section: 4. Processor Fundamentals

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/4-processor-fundamentals-/assembly-language-/


## Card 1 — keyword_definition (`fl_ypKy8qvD4fFyq6vk`)

**FRONT**

Define **machine code**.


**BACK**

Machine code is a **first-generation language**, written in **binary code**, whose instructions are **directly executable by the processor**.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 2 — keyword_definition (`fl_3QckDMkbzB4CYB93`)

**FRONT**

Define **assembly code**.


**BACK**

Assembly code is a **second-generation language** written using **mnemonics**, abbreviated text commands that let programmers write **human-readable programs corresponding almost exactly to machine code**.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 3 — question_and_answer (`fl_gwWZdfGVS2qST6Rh`)

**FRONT**

How many machine code instructions does one assembly instruction translate to?


**BACK**

**One** — one assembly language instruction translates to **one machine code instruction**.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 4 — keyword_definition (`fl_JhM4PKFJtPn4DW5r`)

**FRONT**

Define **instruction set**.


**BACK**

An instruction set is a list of **all the commands that can be processed by a CPU**, each with a **binary code** which is the machine code.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 5 — question_and_answer (`fl_2t5HN4rsm66rdPR4`)

**FRONT**

What is the opcode?


**BACK**

The **part of an instruction that tells the CPU what operation to perform** — short for **operation code**.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 6 — question_and_answer (`fl_4cfZHgBdfDjRRBMf`)

**FRONT**

What is the operand?


**BACK**

The **data or memory address the opcode will work with**, giving the extra detail the CPU needs — often a memory address, a value or a label.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 7 — question_and_answer (`fl_9xw8PYkwgTNjcxbc`)

**FRONT**

What does LDM #n do?


**BACK**

**Immediate addressing** — it **loads the number n into the accumulator**.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 8 — question_and_answer (`fl_4szCGtTxnFr27SHj`)

**FRONT**

What does LDD <address> do?


**BACK**

**Direct addressing** — it **loads the contents of the location at the given address into the ACC**.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 9 — question_and_answer (`fl_D27YQvxwd7zfrdRK`)

**FRONT**

What does LDI <address> do?


**BACK**

**Indirect addressing** — it **uses the value at the given address as a new address**, and loads the contents of that into the ACC.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 10 — question_and_answer (`fl_VtNgxC9tyQcZ8N2b`)

**FRONT**

What does LDX <address> do?


**BACK**

**Indexed addressing** — it uses **address plus the index register** to get the final address, and loads the contents into the ACC.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 11 — question_and_answer (`fl_tHCpyFMDzM2TRXc8`)

**FRONT**

What is the difference between LDM #n and LDR #n?


**BACK**

**LDM** loads the number n into the **accumulator**, while **LDR** loads it into the **index register (IX)**.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 12 — question_and_answer (`fl_gGqV55hQHt7q4hC9`)

**FRONT**

What is the difference between JPE and JPN?


**BACK**

**JPE** jumps to the address if the previous compare result was **true (equal)**; **JPN** jumps if it was **false (not equal)**.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 13 — fill_in_the_blanks (`fl_H4XqRS2mpSBkY2bV`)

**FRONT**

In the 9618 instruction set, <u>**      **</u> denotes a denary number, B denotes binary and & denotes hexadecimal.


**BACK**

In the 9618 instruction set, **#** denotes a denary number, B denotes binary and & denotes hexadecimal.


*Blanks: 1 — answers: []*

Spec links: `spcpt_PfZ6VmBkxyXVhWZd`

Flags: blank_answer_mismatch


## Card 14 — question_and_answer (`fl_r2sBb3jnBKy7bdtn`)

**FRONT**

What do IN and OUT do?


**BACK**

**IN** takes input from the keyboard and stores its **ASCII value in the ACC**; **OUT** outputs to the screen the **character stored in the ACC**.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 15 — true_or_false (`fl_9rPY7JTPQ8dmqWBP`)

**FRONT**

**True or False?**

Assembly code can be executed directly by the processor.


**BACK**

**False.**

Assembly **needs to be translated into machine code** before the computer can execute it; only **machine code** is directly executable.


Spec links: `spcpt_PfZ6VmBkxyXVhWZd`


## Card 16 — keyword_definition (`fl_vPhFVJgm82DSryKD`)

**FRONT**

Define **two-pass assembler**.


**BACK**

A two-pass assembler **translates assembly language into machine code in two stages**, scanning the source code **twice**.


Spec links: `spcpt_znNKGg967WWw9MNQ`


## Card 17 — question_and_answer (`fl_Jy9DmBR6gJzFyhZh`)

**FRONT**

What happens in the first pass of a two-pass assembler?


**BACK**

It **identifies all labels and records their memory addresses**, building a **symbol table**, but does **not translate the instructions yet**.


Spec links: `spcpt_znNKGg967WWw9MNQ`


## Card 18 — question_and_answer (`fl_mKfz3QRBfrXRCNkT`)

**FRONT**

What happens in the second pass of a two-pass assembler?


**BACK**

It **replaces the labels with the correct memory addresses** in the machine code, ensuring the final machine code is accurate and ready to execute.


Spec links: `spcpt_znNKGg967WWw9MNQ`


## Card 19 — question_and_answer (`fl_6TBRyXdBhMmVkSpP`)

**FRONT**

What does a two-pass assembler produce, and what is needed to run it?


**BACK**

It produces an **object program** that can be stored, loaded and run later; another utility called a **loader** is needed to execute it.


Spec links: `spcpt_znNKGg967WWw9MNQ`


## Card 20 — fill_in_the_blanks (`fl_4bxZmHCn599hXQPS`)

**FRONT**

The first pass of a two-pass assembler builds a <u>**                    **</u> table of labels and their addresses.


**BACK**

The first pass of a two-pass assembler builds a **symbol** table of labels and their addresses.


*Blanks: 1 — answers: []*

Spec links: `spcpt_znNKGg967WWw9MNQ`

Flags: blank_answer_mismatch


## Card 21 — question_and_answer (`fl_9cFNGBgYXmT8VsJf`)

**FRONT**

Why is a second pass needed at all?


**BACK**

Because a label may be **used before it is defined**, so the assembler must first record **every label's address** before it can substitute the correct addresses.


Spec links: `spcpt_znNKGg967WWw9MNQ`


## Card 22 — keyword_definition (`fl_5JCgPYd3mVRPt9Rk`)

**FRONT**

Define **trace table**.


**BACK**

A trace table is a table used to **manually track the values of variables as a program runs**, following the flow of the program **line by line**.


Spec links: `spcpt_Sw7xjscGJpcy44GB`


## Card 23 — question_and_answer (`fl_dxYnw9XsP8wpvvF9`)

**FRONT**

Name four uses of a trace table.


**BACK**

To **understand how a program works**, to **debug errors in the logic**, to **predict outputs** before running the program, and to **check variable values at each step**.


Spec links: `spcpt_Sw7xjscGJpcy44GB`


## Card 24 — question_and_answer (`fl_T3n7v7h6wrFpQWdG`)

**FRONT**

In a trace, what does LOAD X do to the accumulator?


**BACK**

It sets **ACC = memory[X]**.


Spec links: `spcpt_Sw7xjscGJpcy44GB`


## Card 25 — question_and_answer (`fl_tnXg6R2rZQJgM9N3`)

**FRONT**

In a trace, what does ADD X do to the accumulator?


**BACK**

It sets **ACC = ACC + memory[X]**.


Spec links: `spcpt_Sw7xjscGJpcy44GB`


## Card 26 — question_and_answer (`fl_XDyfXbdYWmvRbBHk`)

**FRONT**

In a trace, what does STORE X do?


**BACK**

It sets **memory[X] = ACC**.


Spec links: `spcpt_Sw7xjscGJpcy44GB`


## Card 27 — question_and_answer (`fl_tZkMH4VBp3kfmzcx`)

**FRONT**

Trace LOAD A, ADD B, STORE C, HALT where A = 4 and B = 2. What are ACC and C at the end?


**BACK**

**ACC = 6 and C = 6** — LOAD A puts 4 in the ACC, ADD B makes it 6, and STORE C writes 6 into C.


Spec links: `spcpt_Sw7xjscGJpcy44GB`


## Card 28 — question_and_answer (`fl_YWgyCSH4HwYWPqqZ`)

**FRONT**

What is a program's object code, in the context of assembly?


**BACK**

The **machine code output** by the assembler, which can be **stored, loaded and run later**.


Spec links: `spcpt_znNKGg967WWw9MNQ`


## Card 29 — true_or_false (`fl_GhQQn465tHG26m3d`)

**FRONT**

**True or False?**

A two-pass assembler translates each instruction into machine code during the first pass.


**BACK**

**False.**

The first pass only **assigns memory addresses to labels**; translation into machine code happens in the **second pass**.


Spec links: `spcpt_znNKGg967WWw9MNQ`


## Card 30 — question_and_answer (`fl_jfg6JMJvDj3cyRGc`)

**FRONT**

Name the five categories of assembly language instruction.


**BACK**

**Data movement**, **input and output of data**, **arithmetic operations**, **unconditional and conditional instructions**, and **compare instructions**.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 31 — question_and_answer (`fl_cbPd3cxvSwn74T7m`)

**FRONT**

What is the difference between LOAD A and STORE B?


**BACK**

**LOAD A** loads the value stored at memory location A **into the accumulator**; **STORE B** stores the value **from the accumulator into memory location B**.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 32 — question_and_answer (`fl_QpmpzR9TDxsJzzT9`)

**FRONT**

What does MOV A, B do?


**BACK**

It **copies the value from register or memory A to register or memory B**.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 33 — question_and_answer (`fl_yVKdmTqcw8PctFnf`)

**FRONT**

What do CLEAR ACC and DATA do?


**BACK**

**CLEAR ACC** clears the accumulator, setting it to 0; **DATA** declares a **constant or data value**.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 34 — question_and_answer (`fl_7ZPqZJZt9z5Jfst6`)

**FRONT**

What do IN and OUT do?


**BACK**

**IN** takes input from a user or input device and **stores it in the accumulator**; **OUT** outputs the **value in the accumulator** to a screen or output device.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 35 — question_and_answer (`fl_9vQkx9mGnMHC8yb4`)

**FRONT**

What do ADD A and SUB B do?


**BACK**

**ADD A** adds the value at memory location A **to the accumulator**; **SUB B** subtracts the value at memory location B **from the accumulator**.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 36 — question_and_answer (`fl_4zG4XBnjKQ2mN3bN`)

**FRONT**

What do INC and DEC do?


**BACK**

**INC increments the accumulator by 1** and **DEC decrements the accumulator by 1**.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 37 — fill_in_the_blanks (`fl_nHMFV4gMx3spBDg6`)

**FRONT**

<u>**        **</u> jumps to a label **unconditionally**, without testing anything first.


**BACK**

**JMP** jumps to a label **unconditionally**, without testing anything first.


*Blanks: 1 — answers: []*

Spec links: `spcpt_Yr56xgwmtZfJRwFS`

Flags: blank_answer_mismatch


## Card 38 — question_and_answer (`fl_cBc6HgxyQdVcjZVz`)

**FRONT**

What is the difference between JZ and JNZ?


**BACK**

**JZ** jumps to the label if the accumulator **is zero**; **JNZ** jumps if the accumulator is **not zero**.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 39 — question_and_answer (`fl_9hvdWtn6pwxpfyrw`)

**FRONT**

What does JC do?


**BACK**

It **jumps to the label if the carry flag is set**.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 40 — question_and_answer (`fl_q6hbcFRJpCcvqQJS`)

**FRONT**

What does HLT do?


**BACK**

It **stops the program**, halting execution.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 41 — question_and_answer (`fl_Zgd9D2WzSw7Hknb7`)

**FRONT**

What is the difference between CMP A and TEST A?


**BACK**

**CMP A compares the accumulator with the value at memory location A**, while **TEST A performs a logical AND** between the accumulator and A, **setting flags with no output**.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 42 — true_or_false (`fl_r7DpcMN86mzHyVhS`)

**FRONT**

**True or False?**

The TEST instruction produces an output value like ADD does.


**BACK**

**False.**

TEST performs a logical AND and **sets flags, with no output** — it is used to check a condition, not to produce a result.


Spec links: `spcpt_Yr56xgwmtZfJRwFS`


## Card 43 — keyword_definition (`fl_K5T22dq7fjQJGjH7`)

**FRONT**

Define **addressing method**.


**BACK**

An addressing method is a way in which an **instruction in assembly language or machine code can access data stored in memory**.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`


## Card 44 — question_and_answer (`fl_qrh6frR8HbpFzxgD`)

**FRONT**

Name the five main addressing methods.


**BACK**

**Immediate**, **direct**, **indirect**, **indexed** and **relative**.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`


## Card 45 — question_and_answer (`fl_DqBK5jSCbrMP3bmZ`)

**FRONT**

What is immediate addressing?


**BACK**

The **operand is a constant value included directly in the instruction**.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`


## Card 46 — question_and_answer (`fl_swXzD9phpK4RJxqY`)

**FRONT**

What is direct addressing?


**BACK**

The **exact memory address of the operand is given in the instruction**.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`


## Card 47 — question_and_answer (`fl_FFRnrtzmy8HWmwGF`)

**FRONT**

What is indirect addressing?


**BACK**

A **register contains the memory address of the operand**.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`


## Card 48 — question_and_answer (`fl_sJDCkDTfNkChNSgD`)

**FRONT**

What is indexed addressing?


**BACK**

It uses a **base register and an index to calculate the memory address**.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`


## Card 49 — question_and_answer (`fl_KTgnGp4tvWzNkFVr`)

**FRONT**

What is relative addressing, and what is it used for?


**BACK**

The operand is an **offset relative to the current instruction address**, and it is used in **branching**.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`


## Card 50 — question_and_answer (`fl_DKxZPX6DfPs2Dt9k`)

**FRONT**

In indexed addressing, if the base register holds 0050h and the index holds 1000h, which address is used?


**BACK**

**1050h**, because the base and the index are **added together** to give the effective address.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`


## Card 51 — question_and_answer (`fl_W25P35JQfT6CStb3`)

**FRONT**

What is the key difference between direct and indirect addressing?


**BACK**

In **direct** addressing the instruction gives the **address of the operand itself**; in **indirect** addressing a **register holds that address**, so there is an extra step to reach the data.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`


## Card 52 — fill_in_the_blanks (`fl_XSfrhNqFbwKHKFRV`)

**FRONT**

In <u>**                    **</u> addressing the operand is a constant value written into the instruction itself.


**BACK**

In **immediate** addressing the operand is a constant value written into the instruction itself.


*Blanks: 1 — answers: []*

Spec links: `spcpt_9s6ft5c2ryVvfNMH`

Flags: blank_answer_mismatch


## Card 53 — question_and_answer (`fl_dG948RbZFxZyxd8S`)

**FRONT**

What does an instruction like JMP +5 do?


**BACK**

It tells the program to **jump forward 5 instructions from the current line**, using **relative addressing**.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`


## Card 54 — true_or_false (`fl_Db2tbz5QMDnJ3bqy`)

**FRONT**

**True or False?**

In immediate addressing the value in the instruction is treated as a memory address.


**BACK**

**False.**

In immediate addressing the operand **is the constant value itself**; it is **direct** addressing where the value given is a **memory address**.


Spec links: `spcpt_9s6ft5c2ryVvfNMH`

