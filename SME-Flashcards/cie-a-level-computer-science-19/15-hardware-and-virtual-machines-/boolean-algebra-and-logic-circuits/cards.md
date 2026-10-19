# Boolean Algebra & Logic Circuits

Course: cie-a-level-computer-science-19 · Section: 15. Hardware & Virtual Machines

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/15-hardware-and-virtual-machines-/boolean-algebra-and-logic-circuits/


## Card 1 — keyword_definition (`fl_YYFJSmCqMxmhpDyT`)

**FRONT**

Define **half adder**.


**BACK**

A half adder is a **basic digital circuit** that performs the **addition of two single bit numbers**.


Spec links: `spcpt_YPzqqCF8T2nQfgs7`


## Card 2 — question_and_answer (`fl_mXk5HbGytTVHXptC`)

**FRONT**

What are the inputs and outputs of a half adder?


**BACK**

Two inputs, **A** and **B**, and two outputs, **Carry out (Cout)** and **Sum (S)**.


Spec links: `spcpt_YPzqqCF8T2nQfgs7`


## Card 3 — question_and_answer (`fl_6BKr9hmskH6P9wMQ`)

**FRONT**

Which gate produces the Sum in a half adder?


**BACK**

An **XOR** gate, so `S = A XOR B`.


Spec links: `spcpt_YPzqqCF8T2nQfgs7`


## Card 4 — fill_in_the_blanks (`fl_Xj85GMWjNS6JYYZQ`)

**FRONT**

In a half adder, the Sum output is A <u>**        **</u> B.


**BACK**

In a half adder, the Sum output is A **XOR** B.


*Blanks: 1 — answers: []*

Spec links: `spcpt_YPzqqCF8T2nQfgs7`

Flags: blank_answer_mismatch


## Card 5 — question_and_answer (`fl_m9kmMWGSWSGfTks9`)

**FRONT**

Which gate produces the Carry in a half adder?


**BACK**

An **AND** gate, so `Cout = A AND B`.


Spec links: `spcpt_YPzqqCF8T2nQfgs7`


## Card 6 — question_and_answer (`fl_RZCdRn7ffrgByXhS`)

**FRONT**

In a half adder, what are Cout and S when A = 0 and B = 1?


**BACK**

`0 + 1 = 1`, which is `01` in two bits, so **Cout = 0 and S = 1**.


Spec links: `spcpt_YPzqqCF8T2nQfgs7`


## Card 7 — question_and_answer (`fl_BddFzmm25X4WjY8K`)

**FRONT**

In a half adder, what are Cout and S when A = 1 and B = 1?


**BACK**

`1 + 1 = 2`, which is `10` in two bits, so **Cout = 1 and S = 0**.


Spec links: `spcpt_YPzqqCF8T2nQfgs7`


## Card 8 — question_and_answer (`fl_xSKfr6Zxn5rPs3b6`)

**FRONT**

What is the quick way to build the half adder truth table?


**BACK**

For each row, **add A and B together** and write the answer as a **2-bit binary number** in the Cout and S columns.


Spec links: `spcpt_YPzqqCF8T2nQfgs7`


## Card 9 — true_or_false (`fl_9tVX2HqY9RpfWDYf`)

**FRONT**

**True or False?**

A half adder can add three bits.


**BACK**

**False.**

A half adder adds **two single-bit numbers**. It is a **full adder** that handles three bits.


Spec links: `spcpt_YPzqqCF8T2nQfgs7`


## Card 10 — keyword_definition (`fl_PrWS5vtCWP3jZ2bx`)

**FRONT**

Define **full adder**.


**BACK**

A full adder **extends the half adder to handle the addition of three bits**.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 11 — question_and_answer (`fl_dgcBzdssVBbfdpV9`)

**FRONT**

What are the inputs and outputs of a full adder?


**BACK**

Three inputs, **A**, **B** and **carry in (Cin)**, and two outputs, **carry out (Cout)** and **sum (S)**.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 12 — question_and_answer (`fl_SHVfRpgvRwRt7FwF`)

**FRONT**

What does the Sum output of a full adder provide?


**BACK**

The **XOR of the inputs A, B and Cin**.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 13 — question_and_answer (`fl_3zz6qm7tjsYgD8yD`)

**FRONT**

When is the Carry output of a full adder TRUE?


**BACK**

When **at least two of the inputs** A, B and Cin are TRUE.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 14 — true_or_false (`fl_X8QJcBBBydJBvyR9`)

**FRONT**

**True or False?**

In a full adder, Cout is 1 only when all three inputs are 1.


**BACK**

**False.**

Cout is TRUE when **at least two** of the three inputs are TRUE.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 15 — fill_in_the_blanks (`fl_rpqBQNCGx7JX7SRF`)

**FRONT**

In a full adder the three inputs are added, so the answer can be 0, 1, 2 or <u>**        **</u>.


**BACK**

In a full adder the three inputs are added, so the answer can be 0, 1, 2 or **3**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_kp7Pr7pTdrdvZrP9`

Flags: blank_answer_mismatch


## Card 16 — question_and_answer (`fl_bKTmG6tB44D85Kkn`)

**FRONT**

In a full adder, what are Cout and S when A = 0, B = 1 and Cin = 1?


**BACK**

`0 + 1 + 1 = 2`, which is `10` in binary, so **Cout = 1 and S = 0**.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 17 — question_and_answer (`fl_z7Mdf9k2qQYcj5sV`)

**FRONT**

In a full adder, what are Cout and S when A = 1, B = 1 and Cin = 1?


**BACK**

`1 + 1 + 1 = 3`, which is `11` in binary, so **Cout = 1 and S = 1**.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 18 — question_and_answer (`fl_nMznBywjWV8GF9c9`)

**FRONT**

What can a full adder be built from?


**BACK**

**Two half adders** and an **OR gate**.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 19 — question_and_answer (`fl_jPdRj6gH7TdW9PFT`)

**FRONT**

What are the inputs to the first half adder in a full adder?


**BACK**

**A** and **B**.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 20 — question_and_answer (`fl_r9y4mVtyPrt7JXSm`)

**FRONT**

What are the inputs to the second half adder in a full adder?


**BACK**

**Sum1**, the output of the first half adder's XOR gate, and **Cin**.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 21 — question_and_answer (`fl_kWrGm92j7h5qT8hW`)

**FRONT**

How is the final Cout produced in a full adder?


**BACK**

**Carry1** and **Carry2** are connected to the inputs of an **OR gate**, and the output of that gate is the final Cout.


Spec links: `spcpt_kp7Pr7pTdrdvZrP9`


## Card 22 — question_and_answer (`fl_YZTwFCS26D7kZpzP`)

**FRONT**

What are SR and JK flip flops used for?


**BACK**

They are **digital memory components used in sequential circuits**, storing **1 bit of data**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 23 — fill_in_the_blanks (`fl_ZVBmyW5D8c9MchTw`)

**FRONT**

A flip flop stores <u>**        **</u> bit of data.


**BACK**

A flip flop stores **1** bit of data.


*Blanks: 1 — answers: []*

Spec links: `spcpt_whKGvzDcpchQ4bgY`

Flags: blank_answer_mismatch


## Card 24 — question_and_answer (`fl_cZcgyMtxK7qxFSBS`)

**FRONT**

Name three uses of flip flops.


**BACK**

**Counters**, **control systems** and **synchronous logic**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 25 — keyword_definition (`fl_qgmdHY9z6tWf5FNv`)

**FRONT**

Define **bistable circuit**.


**BACK**

A bistable circuit has **two stable states**. It responds to clock signals and is often edge-triggered.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 26 — question_and_answer (`fl_JDMCRhwDKCQtDWkr`)

**FRONT**

On which clock edge are flip flops typically triggered?


**BACK**

The **rising edge**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 27 — question_and_answer (`fl_kyTW7dVdSJhJ53yD`)

**FRONT**

What does SR stand for?


**BACK**

**Set** and **Reset**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 28 — question_and_answer (`fl_PFwrKFd8YjvttzPd`)

**FRONT**

Which gates is an SR flip flop commonly built from in exams?


**BACK**

**NOR** gates.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 29 — question_and_answer (`fl_5DfWXNTFZ5XwMNmG`)

**FRONT**

Name the inputs and outputs of an SR flip flop.


**BACK**

Inputs are **S (Set)**, **R (Reset)** and **CLK (Clock)** when edge-triggered. Outputs are **Q**, the current stored value, and **NOT(Q)**, its inverse.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 30 — question_and_answer (`fl_RP9PdBcwjczRCbT3`)

**FRONT**

In a NOR-based SR flip flop, what happens when S = 0 and R = 0?


**BACK**

**No change.** The flip flop holds its current value, which is memory mode.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 31 — question_and_answer (`fl_HnQ66B4KkbwsCX8n`)

**FRONT**

In an SR flip flop, what happens when S = 0 and R = 1?


**BACK**

**Reset.** Q becomes **0**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 32 — question_and_answer (`fl_4nnG6d2qWqSMKr9D`)

**FRONT**

In an SR flip flop, what happens when S = 1 and R = 0?


**BACK**

**Set.** Q becomes **1**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 33 — question_and_answer (`fl_YwDcj42FNChq3F3Z`)

**FRONT**

In a NOR-based SR flip flop, what happens when S = 1 and R = 1?


**BACK**

It **forces Q = 0**. Both Q and NOT(Q) are driven to 0.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 34 — true_or_false (`fl_2NKXwDxywvvVbhzc`)

**FRONT**

**True or False?**

In a NOR-based SR flip flop, S = 1 and R = 1 is an invalid state.


**BACK**

**False.**

In **NOR-based** designs it forces **Q = 0**. It is in **NAND-based** designs that this state is undefined.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 35 — question_and_answer (`fl_HnBxhVXth5BP2Qdx`)

**FRONT**

An SR flip flop has S = 1, R = 0 and Q = 1. S then changes to 0.

What happens to Q?


**BACK**

The flip flop enters **memory mode**, so **Q stays at 1**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 36 — question_and_answer (`fl_4C7WG6x7phgxpRY3`)

**FRONT**

Why is the JK flip flop more versatile than the SR flip flop?


**BACK**

It **solves the problem of the SR's illegal state** by using that condition to toggle, and it uses a **clock** to control the exact timing of changes.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 37 — fill_in_the_blanks (`fl_JQCfQtGZHqzXqPkT`)

**FRONT**

The JK flip flop uses a <u>**          **</u> to control the exact timing of changes.


**BACK**

The JK flip flop uses a **clock** to control the exact timing of changes.


*Blanks: 1 — answers: []*

Spec links: `spcpt_whKGvzDcpchQ4bgY`

Flags: blank_answer_mismatch


## Card 38 — question_and_answer (`fl_N59cSVgHqFfyYFJv`)

**FRONT**

In a JK flip flop, what happens when J = 0 and K = 0?


**BACK**

**No change.** This is memory or hold mode.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 39 — question_and_answer (`fl_x4DDRf4C6KY7PdT7`)

**FRONT**

In a JK flip flop, what happens when J = 0 and K = 1?


**BACK**

**Reset.** Q becomes **0**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 40 — question_and_answer (`fl_NKNVmydVmyB4Vnwd`)

**FRONT**

In a JK flip flop, what happens when J = 1 and K = 0?


**BACK**

**Set.** Q becomes **1**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 41 — question_and_answer (`fl_NcN2brSNPF7zqbQ5`)

**FRONT**

In a JK flip flop, what happens when J = 1 and K = 1?


**BACK**

It **toggles** the output, so Q becomes **NOT(Q)**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 42 — true_or_false (`fl_VdCJwRMF9K8k4HfS`)

**FRONT**

**True or False?**

J = 1 and K = 1 resets the JK flip flop.


**BACK**

**False.**

It **toggles** the output, so Q becomes NOT(Q).


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 43 — question_and_answer (`fl_zq5WC5qr6KfZCfwk`)

**FRONT**

What is an SR flip flop typically used for?


**BACK**

**Simple memory** and **control circuits**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 44 — question_and_answer (`fl_Qh6FdvxK3QFd6gbf`)

**FRONT**

What is a JK flip flop typically used for?


**BACK**

**Toggles**, **counters** and **frequency dividers**.


Spec links: `spcpt_whKGvzDcpchQ4bgY`


## Card 45 — keyword_definition (`fl_6NFNwzFbdd9bkWhf`)

**FRONT**

Define **Boolean algebra**.


**BACK**

Boolean algebra is a **mathematical system used to manipulate Boolean values**, allowing complex expressions to be made simpler.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 46 — question_and_answer (`fl_DjZZMRZrZDDggRGY`)

**FRONT**

How does Boolean algebra compare with Karnaugh maps?


**BACK**

It is a **more powerful simplification method**, and can simplify expressions that Karnaugh maps cannot.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 47 — question_and_answer (`fl_GBDg52dgZ3btcsSb`)

**FRONT**

What is `X AND 0`?


**BACK**

**0**. An AND only outputs 1 when **both** inputs are 1, so anything ANDed with 0 is 0 whatever X is.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 48 — question_and_answer (`fl_MGNWb4799SZXTVSF`)

**FRONT**

What is `X AND 1`?


**BACK**

**X**. The output is whatever the value of X is.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 49 — true_or_false (`fl_fPjtYzkj5ZQG6QRQ`)

**FRONT**

**True or False?**

`X AND 1` evaluates to 1.


**BACK**

**False.**

`X AND 1 = X`, so the output is **whatever the value of X is**.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 50 — question_and_answer (`fl_7SxCGKd7WZkcjH9c`)

**FRONT**

What is `NOT X AND X`?


**BACK**

**0**. X and NOT X always hold **opposite values**, so one input is always 0, and an AND with a 0 input gives 0.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 51 — question_and_answer (`fl_Pwt5Mhmq2CZjmM4P`)

**FRONT**

What is `X OR 0`?


**BACK**

**X**. An OR outputs 1 if **either** input is 1, so ORing with 0 leaves the output as whatever X is.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 52 — question_and_answer (`fl_YV39332RkvcnmGg8`)

**FRONT**

What is `X OR 1`?


**BACK**

**1**. An OR outputs 1 if **either** input is 1, so a 1 input forces the output to 1 whatever X is.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 53 — question_and_answer (`fl_FhZHSyRx2Rz8p4WC`)

**FRONT**

What is `NOT X OR X`?


**BACK**

**1**. X and NOT X always hold **opposite values**, so one input is always 1, and an OR with a 1 input gives 1.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 54 — question_and_answer (`fl_yvK66Y7qn5ZQjNnB`)

**FRONT**

Which symbols represent AND in Boolean notation?


**BACK**

`A · B`, or simply `AB`.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 55 — fill_in_the_blanks (`fl_vcZpfZVTzZ8hMDgv`)

**FRONT**

In Boolean notation the dot for AND is often <u>**              **</u>, so `AB` means A AND B.


**BACK**

In Boolean notation the dot for AND is often **omitted**, so `AB` means A AND B.


*Blanks: 1 — answers: []*

Spec links: `spcpt_qB5xbpNWQFbdXBMW`

Flags: blank_answer_mismatch


## Card 56 — question_and_answer (`fl_8TjpT4gb6yTZqfFy`)

**FRONT**

Which symbol represents OR in Boolean notation?


**BACK**

`A + B`. The plus sign means OR, so `A + B` reads as A OR B.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 57 — question_and_answer (`fl_SpBDkYMqjrqQ2xmj`)

**FRONT**

How is NOT written in Boolean notation?


**BACK**

As `¬A`, as `A'`, or as a **line drawn above** the variable.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 58 — question_and_answer (`fl_jHg7y5mg3Sq8KrrS`)

**FRONT**

What does a line drawn above a variable or expression mean?


**BACK**

The value is **inverted or negated**. It is the **NOT** of that value.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 59 — question_and_answer (`fl_WFc663NV5TVCjvJm`)

**FRONT**

What does `(A + B)·C` mean?


**BACK**

Do **A OR B first**, then AND the result with C.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 60 — question_and_answer (`fl_JH2zWkHGgnKM3j99`)

**FRONT**

What does `A · B̅` mean?


**BACK**

**A AND (NOT B)**. B is negated before the AND operation.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 61 — question_and_answer (`fl_VjxNtJdsrs9k53SR`)

**FRONT**

When an expression has multiple horizontal lines, what is negated?


**BACK**

The **whole expression**, not just one part of it.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 62 — question_and_answer (`fl_86XDjtKcbk9sYbns`)

**FRONT**

Which line do you apply De Morgan's Law to first?


**BACK**

The **outermost** line.


Spec links: `spcpt_qB5xbpNWQFbdXBMW`


## Card 63 — question_and_answer (`fl_R4w2bzNPzZrjxq7T`)

**FRONT**

State De Morgan's first law.


**BACK**

**NOT (A AND B)** is equivalent to **(NOT A) OR (NOT B)**.


Spec links: `spcpt_tg2CcHpVKFFNPG6V`


## Card 64 — question_and_answer (`fl_HhH7ngtHJF6c5vSB`)

**FRONT**

State De Morgan's second law.


**BACK**

**NOT (A OR B)** is equivalent to **(NOT A) AND (NOT B)**.


Spec links: `spcpt_tg2CcHpVKFFNPG6V`


## Card 65 — question_and_answer (`fl_fdgxw6NgM4wQyZPf`)

**FRONT**

When applying De Morgan's Law, what happens to the operator?


**BACK**

It **changes**: AND becomes OR, and OR becomes AND. Both terms are then **negated**.


Spec links: `spcpt_tg2CcHpVKFFNPG6V`


## Card 66 — question_and_answer (`fl_Ps4YPCxXKnyqT8gY`)

**FRONT**

Simplify `NOT(A AND B)`.


**BACK**

**(NOT A) OR (NOT B)**


Spec links: `spcpt_tg2CcHpVKFFNPG6V`


## Card 67 — true_or_false (`fl_VnQ7ZrW8N2ws3H6z`)

**FRONT**

**True or False?**

Applying De Morgan's Law to NOT(A OR B) gives (NOT A) OR (NOT B).


**BACK**

**False.**

It gives **(NOT A) AND (NOT B)**. The operator changes when the law is applied.


Spec links: `spcpt_tg2CcHpVKFFNPG6V`


## Card 68 — question_and_answer (`fl_rrdQ8NS7bZs83kkF`)

**FRONT**

What are De Morgan's Laws particularly useful for?


**BACK**

**Rewriting logic circuits using only NAND or NOR gates**.


Spec links: `spcpt_tg2CcHpVKFFNPG6V`


## Card 69 — fill_in_the_blanks (`fl_PpcCy9TCC6P2QFJJ`)

**FRONT**

De Morgan's Laws allow a circuit to be implemented using only NAND or <u>**        **</u> gates.


**BACK**

De Morgan's Laws allow a circuit to be implemented using only NAND or **NOR** gates.


*Blanks: 1 — answers: []*

Spec links: `spcpt_tg2CcHpVKFFNPG6V`

Flags: blank_answer_mismatch


## Card 70 — question_and_answer (`fl_GcMCXgVdQybyRkGh`)

**FRONT**

Give two reasons to use De Morgan's Laws.


**BACK**

They make **circuit design more efficient and cost-effective**, and they are essential where **NAND or NOR logic is cheaper or faster** to implement.


Spec links: `spcpt_tg2CcHpVKFFNPG6V`


## Card 71 — question_and_answer (`fl_K3hVyCPb4DcXxnBf`)

**FRONT**

Where are De Morgan's Laws commonly used?


**BACK**

In **microprocessor** and **memory device** design, for example flash drives.


Spec links: `spcpt_tg2CcHpVKFFNPG6V`


## Card 72 — keyword_definition (`fl_Q7BmKmKgr4gvsY8y`)

**FRONT**

Define **Karnaugh map**.


**BACK**

A Karnaugh map is a tool used for **simplifying Boolean algebra expressions**, offering a **visual method of grouping together expressions with common factors**.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 73 — question_and_answer (`fl_KTG3rc7SQxdjJjYT`)

**FRONT**

What makes a Karnaugh map useful?


**BACK**

The format of the map makes it **easy to identify and eliminate redundant terms**.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 74 — question_and_answer (`fl_qJVQkbnksgPf7bst`)

**FRONT**

Where are Karnaugh maps used?


**BACK**

In **digital logic design**, such as simplifying the logic of digital circuits.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 75 — question_and_answer (`fl_tH5ZYgJ3tvHnpp6d`)

**FRONT**

What are the four steps of using a Karnaugh map?


**BACK**

**Create the map**, **group the 1s**, **simplify each group**, then **combine the group expressions with OR** to get the final simplified expression.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 76 — question_and_answer (`fl_bVfFnTNv692ntwDT`)

**FRONT**

What does each cell in a Karnaugh map correspond to?


**BACK**

A **term in the Boolean expression**. Cells are filled with 1s and 0s corresponding to the **output of that term**.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 77 — question_and_answer (`fl_2wXkbxM7xf5RbX6W`)

**FRONT**

How do you fill in a Karnaugh map from an expression?


**BACK**

Split the expression at each **OR** into subterms, then put a **1 in every cell where that subterm would be TRUE**.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 78 — question_and_answer (`fl_BP5gQ7Dns22kntmS`)

**FRONT**

When mapping `A OR B` on a two-variable Karnaugh map, which cells get a 1?


**BACK**

Every cell where **A is 1**, and every cell where **B is 1**.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 79 — question_and_answer (`fl_svYfs3KC4pxZNZRM`)

**FRONT**

What shape must each group on a Karnaugh map be?


**BACK**

A **rectangle**.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 80 — fill_in_the_blanks (`fl_s8WGDYm6s4GNs6pn`)

**FRONT**

Groups on a Karnaugh map must be <u>**                      **</u> in shape.


**BACK**

Groups on a Karnaugh map must be **rectangular** in shape.


*Blanks: 1 — answers: []*

Spec links: `spcpt_v5FF96rrRjkm65jk`

Flags: blank_answer_mismatch


## Card 81 — question_and_answer (`fl_NnBph2KypX8jm5Rs`)

**FRONT**

What sizes can a Karnaugh map group be?


**BACK**

The size must be a **power of 2**, so a group contains **8, 4, 2 or 1** ones.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 82 — true_or_false (`fl_ZcxCFbHHvsFPCPDV`)

**FRONT**

**True or False?**

Karnaugh map groups must have exactly 4 cells.


**BACK**

**False.**

A group's size must be a **power of 2**, so it can contain **8, 4, 2 or 1** ones.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 83 — question_and_answer (`fl_rgQPvWWzJStVBpmZ`)

**FRONT**

How large should Karnaugh map groups be?


**BACK**

**As large as possible**.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 84 — true_or_false (`fl_XKk9pHCFwPdxTrVm`)

**FRONT**

**True or False?**

A cell on a Karnaugh map can only belong to one group.


**BACK**

**False.**

**Groups can overlap**, so a cell can be part of multiple groups.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 85 — question_and_answer (`fl_wd4pYnFbvD6nWb9g`)

**FRONT**

What happens at the edges of a Karnaugh map?


**BACK**

The grid **wraps round in all directions**, so groups can wrap round.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 86 — question_and_answer (`fl_gwnfZYfMZsDhxnQQ`)

**FRONT**

How do you write the simplified expression for a group?


**BACK**

It consists of the **variables that remain constant** in all the terms in that group.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 87 — fill_in_the_blanks (`fl_vvYpKqTmzhk9HPQV`)

**FRONT**

The simplified expression for a group consists of the variables that remain <u>**                **</u>.


**BACK**

The simplified expression for a group consists of the variables that remain **constant**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_v5FF96rrRjkm65jk`

Flags: blank_answer_mismatch


## Card 88 — question_and_answer (`fl_CmdYYSJvPS72cMxb`)

**FRONT**

If a variable changes within a group, what happens to it?


**BACK**

It is **eliminated** from that group's term, because only the variables that stay constant are kept.


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 89 — question_and_answer (`fl_PQ9JKmYGgZvPtRMY`)

**FRONT**

In a group where A is 1 in every cell, and B and C both change, what does the group represent?


**BACK**

**A**


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 90 — question_and_answer (`fl_PNhWG5hQhBrFqKSW`)

**FRONT**

In a group where B is 0 in every cell, and A and C both change, what does the group represent?


**BACK**

**NOT B**


Spec links: `spcpt_v5FF96rrRjkm65jk`


## Card 91 — question_and_answer (`fl_gHzq45XRGb7rxhvZ`)

**FRONT**

How do you build the final simplified expression?


**BACK**

**Combine the simplified expressions from each group using OR operations**.


Spec links: `spcpt_v5FF96rrRjkm65jk`

