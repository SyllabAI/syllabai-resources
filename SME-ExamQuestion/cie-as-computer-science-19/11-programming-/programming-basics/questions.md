# Exam Questions — Programming Basics
**11. Programming** · Cambridge (CIE) AS computer-science (9618)
> Source: [https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/as/computer-science/cie/19/topic-questions/) · 8 questions across 1 sets


## Exam Questions (8 questions)


### Q1 — medium — 4 marks

**Q1** [4 marks]

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


### Q2 — medium — 4 marks

**Q2** [4 marks]

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


### Q3 — medium — 4 marks

**Q3** [4 marks]

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


### Q4 — medium — 4 marks

**Q4** [4 marks]

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


### Q5 — medium — 2 marks

**Q5** [2 marks]

An algorithm has three steps. It will:

1. repeatedly input a pair of numeric values `A` and `B`
2. count the number of pairs that are input until `A` has been greater than `B` 10 times
3. output the number of pairs that were input.

Step 1 of the algorithm is changed.

A variable `ThisSequence` is used to enter a sequence of 10 pairs of numeric values, using a single input statement.

Following the input of `ThisSequence` the revised algorithm will extract the pairs of numbers.

Describe the variable `ThisSequence` and how the numbers are extracted.

*Source: June 2024 9618/21 Q2B*


### Q6 — medium — 8 marks

**Q6** [4 marks]

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


**Q6** [4 marks]

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


### Q7 — medium — 3 marks

**Q7** [3 marks]

Evaluate each expression in the table by using the data values shown in part **(b)**.

Write ‘ERROR’ if the expression contains an error.

| **Expression** | **Evaluates to** |
|---|---|
| `Available AND NOT(Index > 100)` |   |
| `Index MOD 30` |   |
| `NUM_TO_STR(Index + "33")` |   |

*Source: November 2024 9618/23 Q1C*


### Q8 — medium — 4 marks

**Q8** [4 marks]

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

(ii) Describe the benefits of your answer to part **(i)** with reference to this program.

[3]

*Source: November 2024 9618/21 Q1BI,BII*

