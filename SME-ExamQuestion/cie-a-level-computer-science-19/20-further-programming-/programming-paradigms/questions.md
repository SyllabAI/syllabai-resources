# Exam Questions — Programming Paradigms
**20. Further Programming** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 15 questions across 1 sets


## Exam Questions (15 questions)


### Q1 — hard — 4 marks

**Q1** [4 marks]

This pseudocode is written in an imperative (procedural) style.

A programmer swaps line 05 and line 06, so that the `OUTPUT` statement comes before the assignment inside the loop.

State the values output by the original pseudocode and by the changed pseudocode. Explain what this shows about imperative (procedural) programming.

### Q2 — medium — 3 marks

**Q2** [3 marks]

This pseudocode is written in an imperative (procedural) style.

Explain how this pseudocode shows **three** characteristics of imperative (procedural) programming.

### Q3 — hard — 6 marks

**Q3** [6 marks]

The table shows part of the instruction set for a processor. The processor has one general purpose register, the Accumulator (ACC).

| Label | Opcode | Operand | Explanation |
|---|---|---|---|
|   | `LDM` | `#n` | Load the number n to ACC |
|   | `LDD` | `<address>` | Load the contents of the given address to ACC |
|   | `LDI` | `<address>` | The address to be used is at the given address. Load the contents of this second address to ACC |
|   | `ADD` | `<address>` | Add the contents of the given address to the ACC |
|   | `SUB` | `<address>` | Subtract the contents of the given address from the ACC |
|   | `STO` | `<address>` | Store the contents of the ACC at the given address |
|   | `END` |   | Return control to the operating system |
| `<label>:` | `<data>` |   | Gives a symbolic address `<label>` to the memory location with the contents `<data>`. `<label>` can be used in place of `<address>` |

`#` denotes a denary number, for example `#123`.

A game program calculates a player's score.

Use only the given instruction set to write assembly language code to:

- load the constant 100 using immediate addressing, and store it in memory so that it can be used later
- load the value stored in the address contained in the variable `Ptr`
- subtract the constant 100 from this value
- add the value stored in the variable `Bonus`
- store the result in the variable `Score`.

Your answer must also give a symbolic address to each memory location that the code uses.

### Q4 — easy — 2 marks

**Q4** [2 marks]

Tick (✓) **one** box in each row to show whether the statement is true or false for an imperative (procedural) programming language.

| Statement | True | False |
|---|---|---|
| Variables are changed by assignment statements. |   |   |
| The program is written as a set of facts and rules. |   |   |
| The statements are carried out in the order they are written. |   |   |
| The programmer states what the result must be, not how to find it. |   |   |
| Repetition is carried out using iteration, such as a loop. |   |   |

### Q5 — hard — 6 marks

**Q5** [6 marks]

A declarative programming language is used to represent the coaches and members at a sports centre.

These clauses have the following meanings:

| Clause | Meaning |
|---|---|
| 01 | Ana is a coach. |
| 04 | Lena is a member. |
| 08 | Ana is qualified to teach swimming. |
| 13 | Lena wants to learn judo. |
| 17 | Tariq is injured. |

(i) C can coach M if M wants to learn a sport S, C is qualified to teach S and M is not injured.

Write this as a rule.

**[4]**

(ii) Using the variable Who, write the result returned by the goal:

Who = ........................................ **[1]**

(iii) State why the goal can_coach(Who, tariq) returns no result. **[1]**

### Q6 — hard — 4 marks

**Q6** [4 marks]

A school stores the name of each student and the club the student belongs to. Two programs are written to find the students who belong to the chess club.

Program A is written in pseudocode. The arrays already contain the data for five students.

Program B is written in a declarative programming language.

In Program B, the goal `member(X, chess)` returns `X = ana, wei, omar`

Explain how Program A and Program B show the difference between the imperative (procedural) paradigm and the declarative paradigm.

### Q7 — medium — 3 marks

**Q7** [3 marks]

A declarative programming language is used to represent the following facts about the rooms in a hotel.

These clauses have the following meanings:

| Clause | Meaning |
|---|---|
| 01 | Ruby is a single room. |
| 07 | Ruby is on the ground floor. |
| 14 | Jade has a sea view. |

Using the variable Room, the goal:

returns

(i) Write the goal, using the variable Stay, to find all the double rooms. **[1]**

(ii) Write the goal, using the variable Quiet, to find all the rooms that are on the first floor and have a garden view. **[2]**

### Q8 — medium — 4 marks

**Q8** [4 marks]

The table describes four programming paradigms.

Complete the table by writing the name of the programming paradigm for each description.

| Description | Programming paradigm |
|---|---|
| Each instruction has an opcode and an operand. The operand can use immediate, direct or indirect addressing. |   |
| The program is written as a set of facts and rules. A query is used to satisfy a goal. |   |
| Data and the methods that use the data are grouped together in a class. Objects are created as instances of the class. |   |
| Variables are changed by assignment statements. The statements are a sequence of commands that are carried out in the order they are written. |   |

### Q9 — medium — 4 marks

**Q9** [4 marks]

The table shows part of the instruction set for a processor. The processor has one general purpose register, the Accumulator (ACC), and an Index Register (IX).

| Opcode | Operand | Explanation |
|---|---|---|
| `LDD` | `<address>` | Direct addressing. Load the contents of the location at the given address to ACC |
| `LDX` | `<address>` | Indexed addressing. Form the address from `<address>` + the contents of the index register. Copy the contents of this calculated address to ACC |
| `LDR` | `#n` | Immediate addressing. Load the number n to IX |
| `ADD` | `<address>` | Add the contents of the given address to the ACC |
| `STO` | `<address>` | Store the contents of ACC at the given address |
| `END` |   | Return control to the operating system |

`<address>` can be an absolute or a symbolic address. `#` denotes a denary number, for example `#123`.

A weather station stores five temperature readings in consecutive memory locations. The first reading is at the address with the label `Temps`.

| Label | Address | Contents |
|---|---|---|
| Temps | 200 | 18 |
|   | 201 | 23 |
|   | 202 | 21 |
|   | 203 | 26 |
|   | 204 | 19 |
| Sum | 205 | 0 |

Use only the given instruction set to write assembly language code to:

- add the first reading and the fourth reading
- store the result in the variable `Sum`.

You must use indexed addressing to load the fourth reading.

### Q10 — easy — 2 marks

**Q10** [2 marks]

The following program is written in a declarative programming language.

Describe what is meant by a declarative programming language. Refer to the program in your answer.

### Q11 — easy — 2 marks

**Q11** [2 marks]

Two program code examples are shown.

Example 1

Example 2

Identify the programming paradigm used in each example.

### Q12 — medium — 9 marks

**Q12** [4 marks]

A declarative programming language is used to represent some facts about people and their hobbies.

`01 hobby(music).`

`02 hobby(caving).`

`03 hobby(climbing).`

`04 hobby(camping).`

`05 hobby(baking).`

`06 hobby(travelling).`

`07 person(toby).`

`08 person(natasha).`

`09 person(fatima).`

`10 person(joseph).`

`11 person(elijah).`

`12 person(nina).`

`13 enjoys(natasha, travelling).`

`14 enjoys(toby, climbing).`

`15 enjoys(nina, climbing).`

`16 enjoys(elijah, camping).`

`17 enjoys(fatima, baking).`

`18 enjoys(joseph, camping).`

`19 dislikes(toby, caving).`

These clauses have the meanings:

| Clause | Meaning |
|---|---|
| 01 | Music is a hobby |
| 07 | Toby is a person |
| 13 | Natasha enjoys travelling |
| 19 | Toby dislikes caving |

Carlos is a person who enjoys the hobby of cycling but does not like music.

Write additional clauses to represent this information.

20...........................

21...........................

22...........................

23...........................

*Source: Nov 2023 9618/32 Q11A*


**Q12** [1 mark]

Using the variable P, the goal:

` enjoys(P, camping)`

returns

` P = elijah, joseph`

Write the result returned by the goal:

`enjoys(P, climbing)`

` P = ....................`

*Source: Nov 2023 9618/32 Q11B*


**Q12** [4 marks]

N is a person who might enjoy H if H is a hobby and N does not dislike H.

Write this as a rule.

`might_enjoy(N, H)`

`IF .........................`

*Source: Nov 2023 9618/32 Q11C*


### Q13 — medium — 8 marks

**Q13** [3 marks]

A **declarative **programming language is used to represent subjects that students can choose to study.

Students must choose two subjects

`01 subject(mathematics).`

`02 subject(physics).`

`03 subject(chemistry).`

`04 subject(computer_science).`

`05 subject(geography).`

`06 subject(history).`

`07 subject(english).`

`08 subject(biology).`

`09 student(tomaz).`

`10 student(josephine).`

`11 student(elspeth).`

`12 student(nico).`

`13 student(teresa).`

`14 student(pietre).`

`15 choice1(tomaz, mathematics).`

`16 choice1(teresa, chemistry).`

`17 choice1(pietre, mathematics).`

`18 choice1(nico, mathematics).`

`19 choice1(elspeth, chemistry).`

`20 choice2(tomaz, computer_science).`

`21 choice2(nico, geography).`

These clauses have the meanings:

| Clause | Meaning |
|---|---|
| 01 | Mathematics is a subject. |
| 09 | Tomaz is a student. |
| 15 | Tomaz has chosen mathematics as his first choice. |
| 20 | Tomaz has chosen computer science as his second choice. |

Anthony is a student who would like to study history and geography.

Write additional clauses to represent this information.

22 ...........................................

23 ..........................................

24 ...........................................

*Source: Nov 2023 9618/31 Q11A*


**Q13** [1 mark]

Using the variable `X`, the goal:

`     choice1(X, chemistry)`

returns

`X = teresa, elspeth`

Write the result returned by the goal:

`     choice1(X, mathematics)`

` X =` .................

*Source: Nov 2023 9618/31 Q11B*


**Q13** [4 marks]

Students must choose two different subjects such that:

N may choose S, if N is a student and S is a subject and N has not chosen S as the first choice.

Write this as a rule.

`may_choose_subject(N, S)`

` IF .............................`

*Source: Nov 2023 9618/31 Q11C*


### Q14 — medium — 9 marks

**Q14** [4 marks]

A **declarative **programming language is used to allow clients to choose daily activities at the beach.

`01 activity(paddleboarding).`

`02 activity(sailing).`

`03 activity(rowing).`

`04 activity(kayaking).`

`05 activity(jetskiing).`

`06 client(stevie).`

`07 client(antonio).`

`08 client(henry).`

`09 client(eliza).`

`10 client(rebeka).`

`11 client(danny).`

`12 client(erik).`

`13 client(simone).`

`14 client(petra).`

`15 client(frankie).`

`16 choice(petra, rowing).`

`17 choice(frankie, sailing).`

`18 choice(erik, sailing).`

`19 choice(eliza, rowing).`

`20 choice(stevie, jetskiing).`

`21 choice(henry, sailing).`

`22 done(henry, jetskiing).`

`23 done(rebeka, jetskiing).`

`24 done(antonio, kayaking).`

These clauses have the meanings:

| Clause | Meaning |
|---|---|
| 01 | Paddle boarding is an activity |
| 06 | Stevie is a client. |
| 16 | Petra has chosen rowing |
| 22 | Henry has already done jet skiing. |

Jane is a client who would like to choose the activity surfing and she has already done sailing.

Write additional clauses to represent this information.

25 ...............................................................

26 ...................................................................

27..................................................................

28 ...............................................................

*Source: June 2024 9618/32 Q10A*


**Q14** [1 mark]

Using the variable `List`, the goal:

`    choice(List, rowing)`

returns

`    List = petra, eliza`

Write the result returned by the goal:

`    choice(List, sailing)`

` List =` ................................

*Source: June 2024 9618/32 Q10B*


**Q14** [4 marks]

`C` is a client who would like to choose `A` if `A` is an activity and `C` has not already done `A.`

Write this as a rule:

`may_choose_activity(C, A)`

`IF` ............................................

*Source: June 2024 9618/32 Q10C*


### Q15 — medium — 8 marks

**Q15** [3 marks]

A **declarative **programming language is used to represent the features that are available and the features that are unavailable on different body styles of a car.

`01 feature(sunroof).`

`02 feature(automatic_tailgate).`

`03 feature(heated_seats).`

`04 feature(extra_seats).`

`05 feature(reversing_camera).`

`06 feature(dashboard_camera).`

`07 feature(air_conditioning).`

`08 feature(heated_windscreen).`

`09 feature(satnav).`

`10 bodystyle(saloon).`

`11 bodystyle(hatchback).`

`12 bodystyle(estate).`

`13 bodystyle(minivan).`

`14 bodystyle(convertible).`

`15 available(sunroof, hatchback).`

`16 available(sunroof, minivan).`

`17 available(reversing_camera, hatchback).`

`18 available(extra_seats, minivan).`

`19 available(reversing_camera, saloon).`

`20 unavailable(sunroof, convertible).`

`21 unavailable(automatic_tailgate, saloon).`

`22 unavailable(extra_seats, hatchback).`

These clauses have the meanings:

| Clause | Meaning |
|---|---|
| `01` | Sunroof is a feature. |
| `10` | Saloon is a body style. |
| `15` | Sunroof is available on a hatchback. |
| `20` | Sunroof is unavailable on a convertible. |

Sliding doors is a feature that is available on a minivan but unavailable on a hatchback.

Write additional clauses to represent this information.

23........................................................................

24........................................................................

25........................................................................

*Source: June 2024 9618/31 Q8A*


**Q15** [1 mark]

Using the variable `Options`, the goal:

`      available(Options, saloon)`

returns

`Options = reversing_camera`

Write the result returned by the goal:

`      available(Options, hatchback)`

`Options =` ........................

*Source: June 2024 9618/31 Q8B*


**Q15** [4 marks]

`F` may be available for `B` if `F` is a feature and B is a body style and `F` is not unavailable for that body style.

Write this as a rule:

`may_choose_option(F, B)`

`IF `.........................................

*Source: June 2024 9618/31 Q8C*

