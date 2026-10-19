# Exam Questions — Programming Basics
**11. Programming** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 14 questions across 1 sets


## Exam Questions (14 questions)


### Q1 — hard — 4 marks

**Q1** [4 marks]

A program calculates the average of a set of test marks. The marks have already been added together.

The program should:

- input the total of all the marks and the number of marks
- calculate the average mark, which may have a fractional part
- set `Valid` to `TRUE` only when the average is 40 or more and 100 or less
- set `Top` to `TRUE` when the average is 90 or more
- build a message that joins the text `"Average mark: "` to the average
- output the message.

The pseudocode below contains four errors. Each error is caused by the incorrect use of an operator. Line numbers are for reference only.

Identify each error and state the correction required.

### Q2 — medium — 3 marks

**Q2** [3 marks]

A cinema has 200 seats, numbered 1 to 200.

A program stores the number of a seat in the `INTEGER` variable `SeatNum`, and whether that seat has already been booked in the `BOOLEAN` variable `Booked`.

A seat may be reserved only when all three of the following are true:

- the seat number is an even number
- the seat has not already been booked
- the seat number is either less than 50 or greater than 150.

Write a single pseudocode condition that evaluates to `TRUE` only when a seat may be reserved.

Use only the operators given on the insert.

### Q3 — easy — 2 marks

**Q3** [2 marks]

A program controls the entry barrier at a car park. It uses the `INTEGER` variables `Count` and `Limit`.

Two conditions in the program are written as follows.

Condition 1: `(Count > Limit) OR (Count = Limit)`

Condition 2: `NOT (Count >= Limit)`

Write each condition in its simplest form.

Each answer must use one comparison operator only.

### Q4 — very_hard — 5 marks

**Q4** [5 marks]

A program calculates the cost of the water that a household has used in one month.

The program already contains this declaration:

The identifier `UnitCost` holds the cost in dollars of one unit of water. A water meter always shows a whole number of units.

The program must:

- declare every variable that it uses
- prompt for and input the meter reading taken at the start of the month
- prompt for and input the meter reading taken at the end of the month
- calculate the number of units used, which is the reading at the end minus the reading at the start
- calculate the total cost, which is the number of units used multiplied by the cost of one unit
- output the total cost together with a suitable message.

Write pseudocode for the program.

You do not need to check that the readings are valid. You must not declare `UnitCost` again.

### Q5 — medium — 4 marks

**Q5** [4 marks]

A program manages the loan of books in a public library.

Complete the identifier table for four of the values that the program stores.

| Example value | Explanation | Variable name | Data type |
|---|---|---|---|
| "Kigali" | The city in which the library branch is located |   |   |
| TRUE | A value that shows whether the book is on loan at the moment |   |   |
| 14/03/2026 | The day on which the book must be returned |   |   |
| 2.75 | The fine in dollars charged for each day a book is returned late |   |   |

### Q6 — easy — 2 marks

**Q6** [2 marks]

A program prints address labels for a delivery company.

Two of the values used by the program never change while the program runs:

- the character that is printed in every empty position on a label, which is the asterisk character
- the width of one label in centimetres, which is 4.5

Write a pseudocode statement to declare each of these two values.

Choose a suitable identifier for each one.

### Q7 — medium — 4 marks

**Q7** [4 marks]

Other variables in the program have example values as shown:

| **Variable** | **Value** |
|---|---|
| `Active` | `TRUE` |
| `Fraction` | `0.2` |
| `Code` | `"Ab12345"` |

Complete the table by evaluating each expression using the example values.

| **Expression** | **Evaluates to** |
|---|---|
| `Fraction >= 0.2 AND NOT Active` |   |
| `INT((Fraction * 100) + 13.3)` |   |
| `STR_TO_NUM(MID(Code, 4, 2)) + 5` |   |
| `LENGTH("TRUE" & Code)` |   |

*Source: November 2023 9618/23 Q1B*


### Q8 — medium — 4 marks

**Q8** [4 marks]

Other variables in the program have example values as shown:

| **Variable** | **Example value** |
|---|---|
| `Total` | `124.00` |
| `DepRate` | `2.00` |
| `Description` | `"AB12345:Cleaning Brush (small)"` |

Complete the table by evaluating each expression using the example values.

| **Expression** | **Evaluates to** |
|---|---|
| `(Total * DepRate) + 1.5` |   |
| `RIGHT(Description, 7)` |   |
| `(LENGTH(Description) - 8) > 16` |   |
| `NUM_TO_STR(INT(DepRate * 10)) & '%'` |   |

*Source: November 2023 9618/22 Q1B*


### Q9 — medium — 4 marks

**Q9** [4 marks]

Refer to the [insert](https://cdn.savemyexams.com/uploads/2025/11/28487-9618_s24_in_23.pdf) for the list of pseudocode functions and operators.

Four of the expressions used in the program are represented by pseudocode in the table.

Complete each pseudocode expression with a function or operator so that it evaluates to the value shown.

Any functions and operators used must be defined in the **insert.**

| **Pseudocode expression** | **Evaluates to** |
|---|---|
| `........................................ ("Random", 2, 3)` | `"and"` |
| `5 + ........................................ (10/11/2023)` | `15` |
| `........................................ ("45000")` | `TRUE` |
| `(20 ........................................ 3) + 1` | `3` |

*Source: June 2024 9618/23 Q1B*


### Q10 — medium — 4 marks

**Q10** [4 marks]

Program variables have data types as follows:

| **Variable** | **Data type** |
|---|---|
| MyChar | CHAR |
| MyString | STRING |
| MyInt | INTEGER |

Complete the table by filling in each gap with a function (from the insert) so that each expression is valid.

| **Expression** |
|---|
| `MyInt `$\leftarrow$`.......................................... (3.1415926)` |
| `MyChar `$\leftarrow$`.......................................... ("Elwood", 3, 1)` |
| `MyString `$\leftarrow$`....................................... ( ....................................... (27.509))` |
| `MyInt `$\leftarrow$`....................................... ( ........................................ ("ABC123", 3))` |

*Source: June 2024 9618/22 Q1B*


### Q11 — medium — 2 marks

**Q11** [2 marks]

An algorithm has three steps. It will:

1. repeatedly input a pair of numeric values `A` and `B`
2. count the number of pairs that are input until `A` has been greater than `B` 10 times
3. output the number of pairs that were input.

Step 1 of the algorithm is changed.

A variable `ThisSequence` is used to enter a sequence of 10 pairs of numeric values, using a single input statement.

Following the input of `ThisSequence` the revised algorithm will extract the pairs of numbers.

Describe the variable `ThisSequence` and how the numbers are extracted.

*Source: June 2024 9618/21 Q2B*


### Q12 — medium — 8 marks

**Q12** [4 marks]

Refer to the [insert ](https://cdn.savemyexams.com/uploads/2025/11/40523-9618_s24_in_21.pdf)for the list of pseudocode functions and operators.

An algorithm is developed in pseudocode before being coded in a programming language.

The following table shows four valid pseudocode assignment statements. Complete the table by giving an appropriate data type to declare each of the variables `A, B, C` and `D.`

| **Assignment statement** | **Data type** |
|---|---|
| `A `$\leftarrow$`LEFT(MyName, 1)` |   |
| `B `$\leftarrow$` Total * 2` |   |
| `C `$\leftarrow$`INT(ItemCost) / 3` |   |
| `D `$\leftarrow$`"Odd OR Even"` |   |

*Source: June 2024 9618/21 Q1A*


**Q12** [4 marks]

Other variables in the program have example values as shown:

| **Variable** | **Value** |
|---|---|
| `Sorted` | `False` |
| `Tries` | `9` |
| `ID` | `"ZGAC001"` |

Complete the table by evaluating each expression, using the example values.

| **Expression** | **Evaluates to** |
|---|---|
| `Tries < 10 AND NOT Sorted` |   |
| `Tries MOD 4` |   |
| `TO_LOWER(MID(ID, 3, 1))` |   |
| `LENGTH(ID & "xx") >= Tries` |   |

*Source: June 2024 9618/21 Q1B*


### Q13 — medium — 3 marks

**Q13** [3 marks]

Evaluate each expression in the table by using the data value `100` for the variable `Index` and `True` for the variable `Available`.

Write ‘ERROR’ if the expression contains an error.

| **Expression** | **Evaluates to** |
|---|---|
| `Available AND NOT(Index > 100)` |   |
| `Index MOD 30` |   |
| `NUM_TO_STR(Index + "33")` |   |

*Source: November 2024 9618/23 Q1C*


### Q14 — medium — 4 marks

**Q14** [4 marks]

Refer to the [insert](https://cdn.savemyexams.com/uploads/2025/11/33139-9618_w24_in_21.pdf) for the list of pseudocode functions and operators.

A program will calculate the tax payable based on the cost of an item.

Calculations will occur at many places in the program and these involve the use of one of three tax rates.

Tax rate values represent a percentage. For example, a tax rate value of 5.23 represents 5.23%. In this case, the tax payable on an item costing \$100 would be \$5.23.

Tax rate values are used at several places within the program. One example is given in pseudocode as follows:

`HighRate `$\leftarrow$` FALSE `
`CASE OF ItemCost `
`   <= 50  : TaxRate `$\leftarrow$` 3.75   // tax rate of 3.75% `
`   <= 200 : TaxRate `$\leftarrow$` 5.23   // tax rate of 5.23% `
`   > 200  : TaxRate `$\leftarrow$` 6.25   // tax rate of 6.25% `
`            HighRate `$\leftarrow$` TRUE `
`ENDCASE `
`TaxPayable `$\leftarrow$` ItemCost * TaxRate // tax payable`

During the design of the program, tax rate values have been used wherever they are needed as shown in the pseudocode example above. Tax rates do not change while the program runs.

(i) Identify a more appropriate way of representing the tax rate values in the final program.

[1]

(ii) Describe the benefits of your answer to part **(b)(i)** with reference to this program.

[3]

*Source: November 2024 9618/21 Q1BI,BII*

