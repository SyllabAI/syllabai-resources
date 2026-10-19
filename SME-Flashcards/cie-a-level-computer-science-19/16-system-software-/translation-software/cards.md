# Translation Software

Course: cie-a-level-computer-science-19 · Section: 16. System Software

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/16-system-software-/translation-software/


## Card 1 — keyword_definition (`fl_396W5z6ZtKSdvJ2V`)

**FRONT**

Define **interpreter**.


**BACK**

An interpreter is a type of translator that **executes high-level code line by line**.


Spec links: `spcpt_8VQwpnTM66wPN9h8`


## Card 2 — question_and_answer (`fl_8thHgPVn2BWZm9hn`)

**FRONT**

Does an interpreter produce a machine code file?


**BACK**

**No.** It does **not generate a standalone executable or machine code file**. Only immediate execution happens.


Spec links: `spcpt_8VQwpnTM66wPN9h8`


## Card 3 — true_or_false (`fl_NVNZ8FWNgzCKt4F8`)

**FRONT**

**True or False?**

An interpreter produces a standalone executable file.


**BACK**

**False.**

There is **no output file**. The code runs as it is interpreted.


Spec links: `spcpt_8VQwpnTM66wPN9h8`


## Card 4 — question_and_answer (`fl_R6GF6G32pNY82RnS`)

**FRONT**

How does an interpreter process source code?


**BACK**

The source code is **read, analysed and executed one line at a time**.


Spec links: `spcpt_8VQwpnTM66wPN9h8`


## Card 5 — question_and_answer (`fl_Dn9X2C3kkGvYHmzm`)

**FRONT**

What happens when an interpreter finds an error in a line?


**BACK**

**Execution stops**, and the **error is reported immediately**.


Spec links: `spcpt_8VQwpnTM66wPN9h8`


## Card 6 — question_and_answer (`fl_R9RS8nKy3XJf4P7s`)

**FRONT**

Why is interpreted execution slower?


**BACK**

Each line is **translated every time** the program runs.


Spec links: `spcpt_8VQwpnTM66wPN9h8`


## Card 7 — question_and_answer (`fl_2Q9bfFvt7XJdq3bm`)

**FRONT**

Why is an interpreter useful during development?


**BACK**

It is good for **testing and debugging** while coding.


Spec links: `spcpt_8VQwpnTM66wPN9h8`


## Card 8 — question_and_answer (`fl_r6s7qv3gnWKrM4vX`)

**FRONT**

Give two example uses of an interpreter.


**BACK**

**Educational tools**, such as Python shells or BASIC interpreters, and **rapid prototyping** where frequent changes are made.


Spec links: `spcpt_8VQwpnTM66wPN9h8`


## Card 9 — keyword_definition (`fl_bTCYWzCbRCDBpKNg`)

**FRONT**

Define **compilation**.


**BACK**

Compilation is a process that **translates a program written in a high-level programming language into machine code**.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 10 — question_and_answer (`fl_pWFCk4FbFBfnw6XT`)

**FRONT**

Why is compilation necessary?


**BACK**

Because **only machine code can be executed by a computer**.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 11 — question_and_answer (`fl_SmBPpnC7dm4Btcbh`)

**FRONT**

Name the four stages of compilation.


**BACK**

**Lexical analysis**, **syntax analysis**, **code generation** and **optimisation**.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 12 — question_and_answer (`fl_RZRxnSH9QKYfr3pV`)

**FRONT**

What does lexical analysis do?


**BACK**

It **identifies lexical 'tokens'** in the code, studying the **words or vocabulary** of the language.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 13 — question_and_answer (`fl_ZXqq7qWzzyNZhHkH`)

**FRONT**

Name the four types of token.


**BACK**

**Keywords**, **identifiers**, **operators** and **separators**.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 14 — question_and_answer (`fl_Rztv9BNqjkSZZSkD`)

**FRONT**

Give two examples of a keyword token.


**BACK**

`var`, `const`, `function`, `for`, `while` and `if`.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 15 — question_and_answer (`fl_m6P97Xw4sB2fQHSX`)

**FRONT**

Give two examples of a separator token.


**BACK**

`,`, `;`, `{`, `}`, `(` and `)`.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 16 — question_and_answer (`fl_gNwWPDY7CThtQzzd`)

**FRONT**

What is ignored during lexical analysis?


**BACK**

**Comments and whitespace**.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 17 — question_and_answer (`fl_wP7Yr6pCQygVKjkj`)

**FRONT**

What is the result of lexical analysis?


**BACK**

A **token table**.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 18 — question_and_answer (`fl_yV6tNkb9CdnJsRMg`)

**FRONT**

What does syntax analysis do?


**BACK**

It makes sure the tokens all **adhere to the syntax rules** of the programming language.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 19 — fill_in_the_blanks (`fl_2nyj8qbgnN6QMr5w`)

**FRONT**

A symbol such as <u>**        **</u> could be a valid token but not a valid character in a language, so it breaks the syntax rules.


**BACK**

A symbol such as **\$** could be a valid token but not a valid character in a language, so it breaks the syntax rules.


*Blanks: 1 — answers: []*

Spec links: `spcpt_3vWyRRTy5kDyk84q`

Flags: blank_answer_mismatch


## Card 20 — question_and_answer (`fl_S96BY53X4YkXkcmq`)

**FRONT**

Give two common syntax errors.


**BACK**

**Mismatched parentheses** and **missing semicolons**.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 21 — keyword_definition (`fl_RV58ZkKptjrQ7RRG`)

**FRONT**

Define **Abstract Syntax Tree (AST)**.


**BACK**

An AST is a **graph-based representation of the code being compiled**, created once the code has passed syntax analysis.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 22 — fill_in_the_blanks (`fl_Tt9ThJ2VkJvbsWnZ`)

**FRONT**

If the code passes syntax analysis, the compiler creates an <u>**                **</u> Syntax Tree.


**BACK**

If the code passes syntax analysis, the compiler creates an **Abstract** Syntax Tree.


*Blanks: 1 — answers: []*

Spec links: `spcpt_3vWyRRTy5kDyk84q`

Flags: blank_answer_mismatch


## Card 23 — question_and_answer (`fl_yZB4ZPSKMskfsMfN`)

**FRONT**

Why is an AST useful?


**BACK**

It is an **efficient way to represent the code** for the next stage of compilation.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 24 — question_and_answer (`fl_6tWQ3GDjTMzD6hvM`)

**FRONT**

What happens at the code generation stage?


**BACK**

It **takes the AST and traverses it** to generate **object code** that can be executed by the computer.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 25 — question_and_answer (`fl_VKSynQHT5Cf9V2j3`)

**FRONT**

What does the optimisation stage do?


**BACK**

It **modifies the code to make it more efficient without changing its functionality**.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 26 — true_or_false (`fl_z84xDrP7WMRr4F87`)

**FRONT**

**True or False?**

Optimisation changes what the program does.


**BACK**

**False.**

Optimisation makes the code more efficient **without changing its functionality**.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 27 — question_and_answer (`fl_JV7hYprp7qDcV2H9`)

**FRONT**

Give a common optimisation action.


**BACK**

**Removing duplicate code**. If an 'add' function is written twice in the source code, a sophisticated compiler includes it only once in the object code.


Spec links: `spcpt_3vWyRRTy5kDyk84q`


## Card 28 — keyword_definition (`fl_m7zpMCCBVTDHsXGB`)

**FRONT**

Define **syntax**.


**BACK**

Syntax is the set of **strict rules that define how code must be written**.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 29 — question_and_answer (`fl_cSZWHYghjVyBpvmY`)

**FRONT**

Do all programming languages share the same syntax?


**BACK**

**No.** Each language has its own syntax. For example, Python uses indentation and Java uses semicolons.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 30 — question_and_answer (`fl_S6S9Hd7w3wWDsjgb`)

**FRONT**

Why must syntax be precisely defined?


**BACK**

To **avoid ambiguity**, so that translators can correctly convert the program into a form the CPU can understand.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 31 — question_and_answer (`fl_BskmDTxRSdd8KZvD`)

**FRONT**

What are regular expressions used for?


**BACK**

To **describe simple patterns** in text or syntax, such as variable names or simple statements.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 32 — question_and_answer (`fl_q5S5v9c5HZQthrZP`)

**FRONT**

Why are regular expressions not always enough?


**BACK**

Some aspects of a programming language are **too complex** for regular expressions alone.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 33 — true_or_false (`fl_np5qCGX53kQvC7vy`)

**FRONT**

**True or False?**

Every aspect of a programming language can be described by regular expressions.


**BACK**

**False.**

Some aspects are **too complex**, which is why a **meta-language** such as BNF is needed.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 34 — keyword_definition (`fl_BmKjTJYVRGGrYSYB`)

**FRONT**

Define **meta-language**.


**BACK**

A meta-language is a **language used to describe the structure of another language**.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 35 — fill_in_the_blanks (`fl_tbr9WmHHPyJzQtyY`)

**FRONT**

When regular expressions are not enough, we use a <u>**                          **</u>.


**BACK**

When regular expressions are not enough, we use a **meta-language**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_gWsF6g49PnYds2Bw`

Flags: blank_answer_mismatch


## Card 36 — question_and_answer (`fl_hVfnCPmf6ZBts6cG`)

**FRONT**

Name two meta-languages.


**BACK**

**Backus-Naur Form (BNF)** and **syntax diagrams**.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 37 — question_and_answer (`fl_vBxqSvSy8mHpHgbZ`)

**FRONT**

What three things do meta-languages let you define?


**BACK**

**Full grammar rules**, **nested structures** and **hierarchical syntax**.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 38 — keyword_definition (`fl_kRSY5GMSBRgd46WD`)

**FRONT**

Define **Backus-Naur Form (BNF)**.


**BACK**

BNF is a **meta-language**, a way of writing rules that define the **syntax of programming languages or data structures**.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 39 — question_and_answer (`fl_jKCp54N98RxfbnjP`)

**FRONT**

Name three things BNF is used for.


**BACK**

To describe **formal grammar**, to define how statements and expressions are **structured**, and to ensure syntax rules are **unambiguous and machine-readable**.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 40 — keyword_definition (`fl_fvmgSCWmFM8ZBBvj`)

**FRONT**

Define **non-terminal** in BNF.


**BACK**

A non-terminal is a **category or component**, such as `<digit>` or `<identifier>`.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 41 — keyword_definition (`fl_Q86vg5RHMKj3RzC5`)

**FRONT**

Define **terminal** in BNF.


**BACK**

A terminal is an **actual value or symbol**, such as `0`, `1`, `+` or `if`.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 42 — true_or_false (`fl_SQhNdjGBHVMZXkTj`)

**FRONT**

**True or False?**

A terminal in BNF is a category such as `<digit>`.


**BACK**

**False.**

That is a **non-terminal**. A **terminal** is an actual value or symbol, such as `0` or `if`.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 43 — question_and_answer (`fl_992q8pdXtGqyHFJK`)

**FRONT**

What does `::=` mean in BNF?


**BACK**

**'Is defined as'.** It separates the name from its definition.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 44 — question_and_answer (`fl_FnTyQsnZTbMRYcvJ`)

**FRONT**

What does `|` mean in BNF?


**BACK**

**'Or'.** It gives alternative definitions.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 45 — question_and_answer (`fl_rkVnGKR7ybwYXFrP`)

**FRONT**

Write the BNF rule for `<digit>`.


**BACK**

`<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9`


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 46 — question_and_answer (`fl_Rb2GrDZYhrVmJNFZ`)

**FRONT**

What does `<number> ::= <digit> | <digit> <number>` define?


**BACK**

A number as **a single digit, or a digit followed by another number**, which gives one or more digits.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 47 — question_and_answer (`fl_wpXZC29CWbSjh4JG`)

**FRONT**

Why is the `<number>` rule recursive?


**BACK**

Because it **refers to itself**, which is how a definition of **one or more items** is written in BNF.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 48 — question_and_answer (`fl_XfC4rvTJJ6VTsMnz`)

**FRONT**

What does `<IDcode> ::= <number><letter> | <number><number>` define?


**BACK**

An IDcode as a **number followed by either a letter or another number**.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 49 — keyword_definition (`fl_nDcXDm37QjY2YPrC`)

**FRONT**

Define **syntax diagram**.


**BACK**

A syntax diagram is a **graphical representation of BNF**, using symbols that map directly to the structure of BNF.


Spec links: `spcpt_gWsF6g49PnYds2Bw`


## Card 50 — fill_in_the_blanks (`fl_cCwjFQHZ3X22yrkb`)

**FRONT**

On a syntax diagram, a terminal element is drawn in a <u>**            **</u>.


**BACK**

On a syntax diagram, a terminal element is drawn in a **circle**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_gWsF6g49PnYds2Bw`

Flags: blank_answer_mismatch


## Card 51 — keyword_definition (`fl_dxzBYbcqXg7y6vJH`)

**FRONT**

Define **Reverse Polish Notation (RPN)**.


**BACK**

RPN is a method of writing mathematical expressions where the **operator comes after the operands**.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 52 — question_and_answer (`fl_4VCnFZzkwcKPgPPr`)

**FRONT**

What is RPN also known as?


**BACK**

**Postfix notation**.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 53 — fill_in_the_blanks (`fl_cGHrm7TF32zvwbNC`)

**FRONT**

In RPN, the operator comes <u>**          **</u> the operands.


**BACK**

In RPN, the operator comes **after** the operands.


*Blanks: 1 — answers: []*

Spec links: `spcpt_52qhP4gsvByRBtJB`

Flags: blank_answer_mismatch


## Card 54 — question_and_answer (`fl_cwTMR2zCqVkTTNdk`)

**FRONT**

Write `3 + 4` in RPN.


**BACK**

`3 4 +`


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 55 — question_and_answer (`fl_JzyNkfCpXgJv89cr`)

**FRONT**

Give three reasons to use RPN.


**BACK**

**No need for brackets**, **easier for computers to evaluate using a stack**, and it is always **unambiguous**.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 56 — question_and_answer (`fl_5T7MtBkdhJpkHQTG`)

**FRONT**

What determines the order of operations in RPN?


**BACK**

**Position**, not parentheses.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 57 — true_or_false (`fl_cQDq7kN5rZcFm89B`)

**FRONT**

**True or False?**

RPN needs brackets to show precedence.


**BACK**

**False.**

RPN follows the evaluation order naturally, so there is **no need for brackets** or precedence rules.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 58 — question_and_answer (`fl_4Js87QpCZBkc258p`)

**FRONT**

Which data structure is used to evaluate RPN?


**BACK**

A **stack**.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 59 — question_and_answer (`fl_83N8DhfMmcPxg44j`)

**FRONT**

What are the four steps of evaluating an RPN expression?


**BACK**

**Read left to right**; **push numbers onto the stack**; when an **operator** is read, **pop the top two values**, **apply the operator** and **push the result back**; when the expression ends, the result is at the **top of the stack**.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 60 — question_and_answer (`fl_rTnDCnM9VMGhpGsX`)

**FRONT**

What happens when an operator is read?


**BACK**

The **top two values are popped** from the stack, the **operator is applied**, and the **result is pushed back** onto the stack.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 61 — true_or_false (`fl_XXbFS6bDfc5jc4Nr`)

**FRONT**

**True or False?**

In RPN, an operator is applied to the bottom two values of the stack.


**BACK**

**False.**

It is applied to the **top two values**, which are popped from the stack.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 62 — question_and_answer (`fl_kj672FrChZSwhYkw`)

**FRONT**

Where is the final result of an RPN evaluation found?


**BACK**

At the **top of the stack**.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 63 — question_and_answer (`fl_Yyhjd9nrpFyzrrr9`)

**FRONT**

Evaluate `3 4 + 2 x`.


**BACK**

Push 3, push 4, add to give **7**, push 2, multiply to give **14**. The result is **14**.


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 64 — question_and_answer (`fl_6tXxp69dSzpGGvSD`)

**FRONT**

In `3 4 + 2 x`, what is on the stack after the `+` has been read?


**BACK**

**7**


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 65 — question_and_answer (`fl_sQh8nHWqq6RG4PQN`)

**FRONT**

Convert `(7 - 2 + 8)` to RPN.


**BACK**

`7 2 - 8 +`


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 66 — question_and_answer (`fl_gD78fds877wpwkpc`)

**FRONT**

Convert `(9 - 5)` to RPN.


**BACK**

`9 5 -`


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 67 — question_and_answer (`fl_r7bZJP5NZWYbyn3N`)

**FRONT**

Convert `(7 - 2 + 8) / (9 - 5)` to RPN.


**BACK**

`7 2 - 8 + 9 5 - /`


Spec links: `spcpt_52qhP4gsvByRBtJB`


## Card 68 — question_and_answer (`fl_nCqQsyrnpwV8vQmC`)

**FRONT**

What is the method for converting an infix expression to RPN?


**BACK**

**Work from inside brackets out**, **convert each sub-expression**, and **add the operator after its operands**.


Spec links: `spcpt_52qhP4gsvByRBtJB`

