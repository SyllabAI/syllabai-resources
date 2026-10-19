# Exam Questions — Program Testing & Maintenance
**12. Software Development** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 21 questions across 1 sets


## Exam Questions (21 questions)


### Q1 — hard — 5 marks

**Q1** [5 marks]

A sports club gives each member a fitness band that is based on a score.

The program contains the function:

The function returns:

- "LOW" if Score is in the range 0 to 39 inclusive
- "MID" if Score is in the range 40 to 74 inclusive
- "HIGH" if Score is in the range 75 to 100 inclusive
- "ERROR" for every other value of Score.

A junior developer tests the function using the three values 20, 55 and 90 only.

(i) State **one** reason why this test plan does not thoroughly test the function.

(1)

(ii) Complete the table by giving a test value and the expected return value for each aspect listed.

| Aspect to be tested | Test value | Expected return value |
|---|---|---|
| The largest Score that returns "LOW" |   |   |
| The smallest Score that returns "MID" |   |   |
| The largest Score that returns "HIGH" |   |   |
| The largest Score below the valid range |   |   |

(4)

### Q2 — medium — 4 marks

**Q2** [4 marks]

A program allows a user to type the number of items that they want to order. What the user types is stored as a string.

The program contains the function:

The function returns TRUE if Entry represents a whole number that is greater than 0 and less than or equal to 250. In every other case the function returns FALSE.

A test plan for the function uses the four test values shown.

Complete the table by giving the type of test data and the expected return value for each test value.

| Test value | Type of test data | Expected return value |
|---|---|---|
| "120" |   |   |
| "ten" |   |   |
| "0" |   |   |
| "250" |   |   |

### Q3 — easy — 2 marks

**Q3** [2 marks]

A program asks a user to type a room code.

A valid room code is exactly three characters:

- the first character is an upper-case letter
- the second and third characters are both digits.

For example, `B07` is a valid room code.

The program contains a function that checks whether the room code typed by the user is valid.

Give **two** different room codes that this function should reject. For each one, give the reason why you chose it.

Do not give the same reason twice.

### Q4 — hard — 4 marks

**Q4** [4 marks]

A company is developing a program that is built from several separate modules.

The table describes four testing activities that will be carried out.

Complete the table by writing the name of the testing method used in each activity.

| Activity | Name of testing method |
|---|---|
| A tester is given the program specification and a list of input values. The tester works out the expected output for each input, runs the program and compares each actual output with the expected output. The tester never sees the program code. |   |
| Each module has already been tested on its own. The modules are now combined and the combined program is tested as a whole. |   |
| One module has not yet been written. It is replaced by a simple module that returns a known value, so that testing of the rest of the program can continue. |   |
| The programmers at the company test the finished program themselves, before anyone outside the company is given a copy. |   |

### Q5 — medium — 3 marks

**Q5** [3 marks]

A program has been written and compiled. It compiles without errors, but when the program runs the total that it outputs is sometimes wrong.

A team will test the program using the walkthrough method.

Describe this method **and** explain how it can be used to identify the fault.

### Q6 — easy — 2 marks

**Q6** [2 marks]

A company has written a program that manages bookings for a sports centre.

Programmers at the company have tested the program themselves and have corrected every fault that they found.

The company now gives the program to a small number of people who manage other sports centres. These people will use the program in their own centres and report anything that does not work as they expect.

Identify this stage of testing **and** state one reason why the company carries it out.

### Q7 — hard — 4 marks

**Q7** [4 marks]

A program uses a global 1D array `Reading` containing 10 elements of type INTEGER. The first element has the index value 1.

The array holds these values:

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Value | 12 | 45 | 33 | 78 | 21 | 90 | 55 | 40 | 67 | 85 |

The program contains the function `CountHigh()`, which should return the number of elements in `Reading` that are greater than `Limit`.

The program runs and calls the function three times. The table shows each call, the value that should be returned, and the value that is actually returned.

| Call | Value that should be returned | Value actually returned |
|---|---|---|
| `CountHigh(50)` | 5 | 4 |
| `CountHigh(80)` | 2 | 1 |
| `CountHigh(95)` | 0 | 0 |

Identify the type of error in the function, explain how the results in the table show that it is this type of error, explain what is wrong with the function, and write the corrected statement.

### Q8 — medium — 3 marks

**Q8** [3 marks]

A program contains the procedure `CountDown()`. The procedure is written in pseudocode as follows:

The pseudocode is translated into program code and no errors are reported.

The procedure is called with the value 10. It outputs 10, 8, 6, 4 and 2, then outputs `Finished`, as expected.

The procedure is then called with the value 7. It outputs 7, 5, 3, 1, -1, -3 and continues to output values without end. `Finished` is never output and the program stops responding.

Explain why the program stops responding when the procedure is called with the value 7, identify the type of error this is, and write a corrected version of the `WHILE` statement.

### Q9 — easy — 2 marks

**Q9** [2 marks]

A programmer writes a program. The program contains three errors. Each error is of a different type.

The table describes what happens because of each error.

Complete the table by stating the type of error in each case. The first row has been completed as an example.

| What happens | Type of error |
|---|---|
| The program runs to the end. The average that it outputs is larger than the correct average. | Logic |
| The program code cannot be translated. A message reports that a closing quotation mark is missing from a string. |   |
| The program is translated and starts to run. It then stops before the end and displays a message, because the user has entered 0 as the divisor. |   |

### Q10 — hard — 4 marks

**Q10** [4 marks]

A program is used by a shop to record its sales. The program has been released and is in use.

Two changes are made to the program after its release.

**Change 1**

A new law in the country where the shop operates requires a tax code to be printed on every receipt. The program is changed so that it stores a tax code for each sale and prints the code on the receipt.

**Change 2**

When two members of staff use the program at the same time, the same sale is sometimes stored twice. The program is changed so that this no longer happens.

For each change, identify the type of maintenance and justify your answer.

### Q11 — medium — 3 marks

**Q11** [3 marks]

A program that stores the records of the members of a sports club has been released and is in use.

The program produces correct results. However, when a club has more than 500 members, the program takes about two minutes to produce a membership report.

The developer rewrites part of the code so that the report is produced in about ten seconds.

A student says that this is an example of corrective maintenance.

Explain why the student is incorrect and state the correct type of maintenance.

### Q12 — easy — 1 marks

**Q12** [1 mark]

A program that records parcel deliveries has been released and is in use.

Two months later, a user reports that the program displays a negative number of parcels when a delivery is cancelled.

The developer finds a fault in the code and changes the program so that the number of parcels is always correct.

State the type of maintenance that has been carried out on the program.

### Q13 — medium — 4 marks

**Q13** [3 marks]

A program is being designed in pseudocode.

The program contains a global 1D array `Data `of type string containing 200 elements.

The first element has the index value 1.

A procedure` Process()` is written to initialise the values in the array:

`PROCEDURE Process(Label : STRING)`

`    DECLARE Index : INTEGER`

`    Index 0`

`    INPUT Data[Index]`

`    WHILE Index < 200`

`        Index Index + 1`

`        CASE OF (Index MOD 2)`

`            0 : Data[Index] TO_UPPER(Label)`

`            1 : Data[Index] TO_LOWER(Label)`

`            OTHERWISE : OUTPUT "Alarm 1201"`

`        ENDCASE`

`    NEXT Index`

`    OUTPUT "Completed " & Index & " times"`

`ENDPROCEDURE`

The pseudocode contains **two **syntax errors and **one** other error.

Identify the errors.

*Source: June 2024 9618/22 Q5A(I)*


**Q13** [1 mark]

After correcting all syntax errors, the pseudocode is translated into program code which compiles without generating any errors.

When the program is executed it unexpectedly stops responding.

Identify the type of error that has occurred.

*Source: June 2024 9618/22 Q5B*


### Q14 — medium — 3 marks

**Q14** [3 marks]

A software developer follows a program development life cycle. The life cycle divides the development process into various stages.

A software developer has written modules `Test_A()` and `Test_B()`. These have been written but contain errors. These modules are called from several places in the main program and testing of the main program (integration testing) has to stop.

Identify a method that can be used to continue testing the main program **before **the errors in these modules have been corrected **and **describe how this would work.

*Source: Nov 2024 9618/23 Q5B*


### Q15 — medium — 3 marks

**Q15** [3 marks]

A program contains a global 1D array `Data `with 100 elements of type `INTEGER`.

The program contains a function `Process()` expressed in pseudocode as follows:

`FUNCTION Process(Number : INTEGER, Label : STRING) RETURNS STRING`

`    DECLARE Index, Count : INTEGER`

`    DECLARE ReturnValue : STRING`

`    Count INT(100 / Number)`

`    Index Data[Number]`

`    CASE OF (Index MOD 2)`

`        0 : ReturnValue TO_UPPER(RIGHT(Label, Count))`

`        1 : ReturnValue "****"`

`    ENDCASE`

`    RETURN RetVal`

`ENDFUNCTION`

Run-time errors can be generated in different ways. For example, a run-time error will be generated if a function is called with invalid parameters.

The pseudocode contains three statements that could generate a run-time error.

Write the **three **statements **and **explain how each could generate a run-time error

*Source: Nov 2024 9618/22 Q5A*


### Q16 — medium — 5 marks

**Q16** [5 marks]

A software developer follows a program development life cycle. The life cycle divides the development process into various stages.

The program contains a validation function.

(i) The function will:

- take an integer value as a parameter .
- return TRUE if the value is within the range 24 to 37, inclusive
- otherwise return FALSE.

Complete the table to define a test plan to thoroughly test the operation of the function.

| Type of test data | Test data value | Expected result |
|---|---|---|
| Normal | 30 | TRUE |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |

(4)

(ii)  The function is to be tested on its own. When it is shown to work correctly the function will be combined with other modules and testing will continue.

Identify the type of testing that this represents.

(1)

*Source: Nov 2024 9618/21 Q5B*


### Q17 — medium — 2 marks

**Q17** [2 marks]

A program includes the following assignment statement:

`Result ← STR_TO_NUM(x) / STR_TO_NUM(y)`

When the program evaluates the expression in the statement, it performs a calculation.

Variable `Result `is of type real and variables x and y are of type string.

Two checks are required before the calculation is performed:

Identify the type of error that could occur if these checks are **not** carried out **and **state a cause of this error.

*Source: Nov 2024 9618/21 Q4A*


### Q18 — medium — 2 marks

**Q18** [2 marks]

Refer to the [insert ](https://cdn.savemyexams.com/uploads/2025/11/33139-9618_w24_in_21.pdf)for the list of pseudocode functions and operators.

A program will calculate the tax payable based on the cost of an item.

Calculations will occur at many places in the program and these involve the use of one of three tax rates.

Tax rate values represent a percentage. For example, a tax rate value of 5.23 represents 5.23%. In this case, the tax payable on an item costing \$100 would be \$5.23.

Tax rate values are used at several places within the program. One example is given in pseudocode as follows:

`HighRate ← FALSE `

`CASE OF ItemCost `

`    <= 50 : TaxRate ← 3.75 // tax rate of 3.75% `

`    <= 200 : TaxRate ← 5.23 // tax rate of 5.23% `

`    > 200 : TaxRate ← 6.25 // tax rate of 6.25% `

`            HighRate ← TRUE `

`ENDCASE`

`TaxPayable ← ItemCost * TaxRate // tax payable`

The pseudocode contains a logical error.

Identify the error **and **suggest a correction.

*Source: Nov 2024 9618/21 Q1A*


### Q19 — medium — 2 marks

**Q19** [2 marks]

A program is being developed in pseudocode before being converted into a programming language.

The hardware that runs the program is changed and the program needs to be modified so that it works with the new hardware.

Identify the type of maintenance that this represents and give one other reason why this type of maintenance may be needed.

*Source: November 2023 9618/23 Q1D*


### Q20 — medium — 3 marks

**Q20** [3 marks]

A procedure `Count()` will:

1. input a value (all values will be positive integers) 
2. count the number of odd values and count the number of even values 
3. repeat from step 1 until the value input is 99 
4. output the two count values, with a suitable message.

The value 99 must not be counted

The procedure `Count() `is to be tested.

Typical test data would consist of odd and even values, for example:

23, 5, 64, 100, 2002, 1, 8, 900, 99

The purpose of this test would be to test a typical mix of even and odd values and check the totals.

Give** three** test data sequences that may be used to test **different **aspects of the procedure.

Do **not** include invalid data.

*Source: November 2023 9618/22 Q4B*


### Q21 — medium — 7 marks

**Q21** [3 marks]

An algorithm is designed to find the smallest numeric value from an input sequence and count how many numeric values have been input. 
An example of an input sequence is:

23, AB56, 17, 23ZW, 4, 10, END

Numeric input values are all integers and non-numeric input is ignored, except for the string "END" which is used to terminate the sequence.

The algorithm is expressed in pseudocode as shown:

`DECLARE NextInput : STRING `
`DECLARE Min, Count, Num : INTEGER `

`Min ← 999 `
`Count ← 0 `

`REPEAT `
`    INPUT NextInput `
`    IF IS_NUM(NextInput) = TRUE THEN `
`           Num ← STR_TO_NUM(NextInput) `
`           IF Num > Min THEN `
`                 Min ← Num `
`           ENDIF Count ← Count & 1 `
`    ENDIF `
`UNTIL NextInput ← "END" `

`OUTPUT "The minimum value is ", Min, " and the count was ", Count`

The pseudocode contains three errors due to the incorrect use of **operators. **

Identify each error **and **state the correction required.

*Source: November 2023 9618/21 Q5A*


**Q21** [4 marks]

The operator errors are corrected and the algorithm is tested as follows:

The input sequence:

` 18, 4, ONE, 27, 189, ERIC, 3, 65, END `

produces the output:

` The minimum value is 3 and the count was 6 `

The algorithm is tested with a different test data sequence. The sequence contains a mix of integer and non-numeric values. It is terminated correctly but the algorithm produces unexpected results.

(i) Explain the problem with the algorithm

[2]

(ii) Give a sequence of four test data values that could be input to demonstrate the problem.

Value 1 .............................................................................................................................. Value 2 .............................................................................................................................. Value 3 .............................................................................................................................. Value 4 ............................................................................................................................

[2]

*Source: November 2023 9618/21 Q5BI,BII*

