# Mark Schemes — Program Testing & Maintenance
**12. Software Development** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (21 questions)


### Q1
(i) All three values sit in the middle of a band, so no value at the edge of a band is tested. **[1]**

(ii)

| Aspect to be tested | Test value | Expected return value |
|---|---|---|
| The largest Score that returns "LOW" | **39** | **"LOW"** **[1]** |
| The smallest Score that returns "MID" | **40** | **"MID"** **[1]** |
| The largest Score that returns "HIGH" | **100** | **"HIGH"** **[1]** |
| The largest Score below the valid range | **-1** | **"ERROR"** **[1]** |

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for part (i), for either of:
> 
> - every test value is in the middle of a band, so no value at the edge of a band is tested
> - the return value "ERROR" is never produced, so that outcome is not tested
> 
> **1 mark** for row 1 of part (ii): 39 and "LOW"
> 
> **1 mark** for row 2 of part (ii): 40 and "MID"
> 
> **1 mark** for row 3 of part (ii): 100 and "HIGH"
> 
> **1 mark** for row 4 of part (ii): -1 and "ERROR"
> 
> Both cells in a row must be correct for that row to earn its mark.
> 
> Accept the return values written without quotation marks.
> 
> Do not accept 101 in row 4. That value is above the valid range, not below it.
> 
> Do not accept 0 in row 4. The valid range starts at 0, so 0 returns "LOW".
> 
> Do not accept "three tests are not enough" on its own in part (i), because the number of tests is not what is wrong with the plan.

> **[exam-tip]**
> The last row catches most students. The valid range starts at 0, so the largest score below it is -1. Nothing in the question says that a score cannot be negative, and "ERROR" exists precisely so that such values can be handled.
> 
> Values at the edge of a band must be exact. 39 and 40 sit either side of the LOW to MID edge, and only that pair proves that the function changes band in the right place. A value such as 38 or 45 tests nothing that 20 or 55 has not already tested.

### Q2
| Test value | Type of test data | Expected return value |
|---|---|---|
| "120" | **Normal** | **TRUE** **[1]** |
| "ten" | **Abnormal** | **FALSE** **[1]** |
| "0" | **Abnormal** | **FALSE** **[1]** |
| "250" | **Boundary** | **TRUE** **[1]** |

**[4 marks]**

> **[mark-scheme]**
> **1 mark** per row. Both the type and the expected return value must be correct for the row to earn its mark.
> 
> **1 mark** for row 1: Normal, TRUE
> 
> **1 mark** for row 2: Abnormal, FALSE
> 
> **1 mark** for row 3: Abnormal, FALSE. Accept Boundary or Extreme, because 0 is the largest value that is rejected at the lower end of the range
> 
> **1 mark** for row 4: Boundary, TRUE. Accept Extreme or Normal, because 250 is the largest value that is accepted
> 
> Do not accept Boundary or Extreme for row 2. The value "ten" does not represent a number at all, so it sits at no limit of the acceptable range.
> 
> Do not accept Normal for row 3, because 0 is outside the acceptable range.
> 
> Do not accept "accepted" or "rejected" in place of TRUE and FALSE, because the function returns a BOOLEAN.

> **[exam-tip]**
> Work out which end of the range each value sits on before you write anything. The rule here is not symmetrical: it says greater than 0, so 0 itself is rejected, and less than or equal to 250, so 250 itself is accepted. Students who read both limits as inclusive get row 3 wrong every time.
> 
> A value can honestly belong to more than one type and CIE credits the alternatives, but only where the value really does sit at a limit. Abnormal data is data that the program should reject, whether that is because it is the wrong kind of data, like "ten", or because it is outside the acceptable range, like "0".

### Q3
Room code 1: `b07` because the first character is a lower-case letter, not an upper-case letter. **[1]**

Room code 2: `B7` because the code is only two characters long, so it is too short. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for each room code that is paired with a reason that matches it. Max 2 marks.
> 
> The two answers must use different reasons. Accepted pairs:
> 
> - A lower-case first character, for example `b07`
> - A first character that is not a letter, for example `707`
> - A code that is too short, for example `B7`
> - A code that is too long, for example `B071`
> - A second or third character that is not a digit, for example `B0X` or `BB7`
> - An empty code
> 
> Do not accept `A00` or `Z99`, or any other code that follows all three rules, because the function should accept these
> 
> Do not accept a room code with no reason, or a reason with no room code
> 
> Do not accept two codes that fail for the same reason, for example `B7` and `B0`. Award 1 mark only

> **[exam-tip]**
> The marks are for testing different things, not for writing two odd-looking codes. Two codes that are both too short prove the same point and score once.
> 
> Check that the code you write really does break the rule you claim it breaks. `A00` and `Z99` look unusual but both follow the rule exactly, so the function should accept them.

### Q4
| Activity | Name of testing method |
|---|---|
| A tester is given the program specification and a list of input values. The tester works out the expected output for each input, runs the program and compares each actual output with the expected output. The tester never sees the program code. | **Black-box testing** **[1]** |
| Each module has already been tested on its own. The modules are now combined and the combined program is tested as a whole. | **Integration testing** **[1]** |
| One module has not yet been written. It is replaced by a simple module that returns a known value, so that testing of the rest of the program can continue. | **Stub testing** **[1]** |
| The programmers at the company test the finished program themselves, before anyone outside the company is given a copy. | **Alpha testing** **[1]** |

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for row 1: Black-box testing
> 
> **1 mark** for row 2: Integration testing
> 
> **1 mark** for row 3: Stub testing
> 
> **1 mark** for row 4: Alpha testing
> 
> Accept the method name written without the word "testing" in every row.
> 
> Accept "in-house testing" for row 4.
> 
> Do not accept "white-box testing" for row 1, because the tester cannot see the program code.
> 
> Do not accept "beta testing" for row 4, because no copy of the program has left the company.

> **[exam-tip]**
> Alpha and beta testing are told apart by who does the testing, not by when it happens. Alpha testing is done inside the company that wrote the program; beta testing is done by people outside it, before the program is sold.
> 
> Stub and integration testing are confused just as often. Integration testing combines modules that already work. Stub testing replaces a module that does not work yet, or has not been written yet, with a simple module that returns a known value.

### Q5
The program code is followed one line at a time, by hand, and a trace table is used. **[1]**

The value of every variable is written down each time it changes. **[1]**

The fault is shown when a variable is given a value that was not expected, or when the program follows a path that was not expected. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - The program code is checked one line at a time // a trace table is produced
> - The value of each variable is recorded as it changes
> - A fault is indicated when a variable is given an unexpected value
> - A fault is indicated when the program takes an unexpected path through the code // a fault in the logic of the program can be detected
> 
> **[3 marks]**
> 
> Accept, for the first marking point, that the code is reviewed by a group of people rather than by one person
> 
> Do not accept "the program is run and the output is checked". Nothing is executed in a walkthrough; the code is followed by hand

> **[exam-tip]**
> The most common answer here describes running the program and looking at what it prints. That is not a walkthrough and it scores nothing. In a walkthrough the code is never executed: a person follows it line by line and writes down what each variable holds.
> 
> Two of the three marks are for what you record and what an unexpected recorded value tells you, so do not stop at "you go through the code carefully".

### Q6
Stage: beta testing **[1]**

Reason: the program is tried by a small group of potential users, who use it in a real workplace and report any problems they find, so that those problems can be corrected before the program is sold. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the stage: Beta testing
> 
> **1 mark** for any one reason from:
> 
> - the testing is carried out by a small group of potential users
> - the users check that the program works as required // works in the real world
> - the users identify faults that the programmers did not find
> - the users feed back problems // suggestions for improvement
> - the problems that are found are corrected before the program is sold
> 
> Accept "beta" on its own for the stage mark.
> 
> Do not accept "user testing", "final testing" or "live testing" for the stage mark, as none of these is the name CIE uses.
> 
> Do not accept "so that the programmers can test it themselves" for the reason mark, because that testing has already happened.

> **[exam-tip]**
> Two details in the stem tell you which stage this is: the company has already finished testing the program itself, and the people who now have it are outside the company. That pair always means beta testing.
> 
> The reason mark is lost by writing "to find any errors", which is true of every stage of testing. Say who is doing the testing and what they do with what they find.

### Q7
The function contains a logic error. **[1]**

The program runs to the end and returns a value for every call, but the value returned is smaller than the value that should be returned. **[1]**

The `FOR` loop ends at index 9, so element 10 of `Reading` is never examined and is never counted. **[1]**

The corrected statement is: **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for Logic (error)
> 
> **1 mark** for the program runs to the end / returns a value every time, but the value returned is wrong / too small
> 
> **1 mark** for the loop does not examine the last element // element 10 is never tested // the loop ends one element early
> 
> **1 mark** for `FOR Index ← 1 TO 10`
> 
> Accept Logical error for the first mark
> 
> Accept an equivalent loop that examines indices 1 to 10 inclusive for the fourth mark
> 
> Do not accept Run-time error: the program does not stop, it completes every call and returns a value
> 
> Do not accept Syntax error: the pseudocode follows the rules of the language and would be translated with no errors reported
> 
> Do not accept the array index is out of range: no index outside 1 to 10 is used

> **[exam-tip]**
> The third call is the one to study. `CountHigh(95)` returns the right answer, because no element is greater than 95, so the element the loop misses would not have been counted anyway. One correct result never proves a function is correct.
> 
> When a loop is meant to cover a whole array, check its final value against the declared upper bound of the array rather than against a number that looks reasonable. Stopping one element early is the most common logic error on this paper, and it hides completely whenever the missing element would not have changed the answer.

### Q8
When `Start` is 7, `Value` takes only odd values (7, 5, 3, 1, -1 and so on), so `Value` is never exactly 0, the condition `Value <> 0` is never FALSE and the loop never ends. **[1]**

This is a run-time error. **[1]**

The corrected statement is: **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the terminating condition is never satisfied // `Value` steps past 0 // `Value` is only ever odd so it never equals 0 // the loop never ends
> 
> **1 mark** for Run-time (error)
> 
> **1 mark** for `WHILE Value > 0`
> 
> Accept `WHILE Value >= 1` for the third mark
> 
> Accept Run time or Runtime as spellings of Run-time
> 
> Do not accept `WHILE Value >= 0` : this changes the call that already works, because `CountDown(10)` would then output 0 as well
> 
> Do not accept Syntax error: the pseudocode was translated with no errors reported
> 
> Do not accept Logic error: the program never runs to the end, it is stuck in a loop that never ends and stops responding, and Cambridge treats a program that stops responding as a run-time error

> **[exam-tip]**
> The trap here is to answer logic error, because the mistake was made when the loop was written. Cambridge classifies a program that stops responding as a run-time error, so answer with the symptom described in the question, not with the stage at which the mistake was made.
> 
> A counter that changes by more than 1 should almost never be tested with `<>` or `=`, because it can step straight over the stopping value. Test it with `>` or `<` instead and the loop still ends even when the counter misses that value exactly.

### Q9
| What happens | Type of error |
|---|---|
| The program runs to the end. The average that it outputs is larger than the correct average. | Logic |
| The program code cannot be translated. A message reports that a closing quotation mark is missing from a string. | **Syntax** **[1]** |
| The program is translated and starts to run. It then stops before the end and displays a message, because the user has entered 0 as the divisor. | **Run-time** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for Syntax (error) in the second row
> 
> **1 mark** for Run-time (error) in the third row
> 
> Accept Run time or Runtime as spellings of Run-time
> 
> Do not accept Logic error in the second row: no program code is produced, so the program never runs and produces no output at all
> 
> Do not accept Syntax error in the third row: the program has already been translated successfully and has started to run

> **[exam-tip]**
> Students very often label anything that stops a program as a syntax error. Use the moment the fault appears to decide. If the translator refuses the code, it is a syntax error. If the program runs all the way through but gives the wrong answer, it is a logic error. If the program starts, then halts part way through, it is a run-time error.
> 
> A run-time error depends on the data. The same program can run perfectly for one set of inputs and stop for another, which is why a divisor of 0 is the standard example.

### Q10
**Change 1**

Adaptive maintenance. **[1]**

The program did not contain an error and it has not been made better for the user. It has been changed because a requirement outside the program, the law, has changed, and the program must now fit the new requirement. **[1]**

**Change 2**

Corrective maintenance. **[1]**

The program does not behave as it is supposed to, because one sale is stored twice. The fault was already in the program when it was released and has only been found in use, so the change puts an error right. **[1]**

**[4 marks]**

> **[mark-scheme]**
> One mark for each type and one mark for the matching justification.
> 
> **1 mark** for Change 1: Adaptive
> 
> **1 mark** for a justification of adaptive: the requirements have changed // the change is forced by a change in legislation // the program itself was not faulty
> 
> **1 mark** for Change 2: Corrective
> 
> **1 mark** for a justification of corrective: the program does not operate as expected // the program contains an error // the fault was present at release and has been found in use
> 
> Accept the legislation justification in Change 1 expressed as a change in the environment the program has to work in.
> 
> Do not accept perfective for Change 2, because the program was not working correctly before the change.
> 
> A justification mark is only available where the type named with it is correct.

> **[exam-tip]**
> Change 2 is written to look like an improvement, because the program works for one user at a time. Ask yourself one question first: does the program do what it is supposed to do? Here it does not, so the answer is corrective.
> 
> Where a question asks you to justify, a one word answer scores half the marks at most. Say what makes the change fit that type and, where you can, say why it does not fit one of the other two.

### Q11
Corrective maintenance is carried out when a program contains an error, so that it does not do what it is supposed to do. **[1]**

This program already produces the correct results, so there is no error to correct. It is only slow. **[1]**

The change makes a program that already works better, by improving its performance, so this is perfective maintenance. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for corrective maintenance is used when the program contains an error // when the program does not operate as expected
> 
> **1 mark** for the program gives correct results // there is no error in the program // the program is only slow
> 
> **1 mark** for the change improves the performance of a working program, so the type is perfective
> 
> Accept efficiency, speed or response time in place of performance.
> 
> Accept the third mark for naming perfective on its own, provided the first two marks have been earned.
> 
> Do not accept adaptive, because nothing outside the program has changed.

> **[exam-tip]**
> Students often treat anything that annoys a user as a bug. A program that gives the right answer slowly is not a faulty program, so putting the speed right is not corrective maintenance.
> 
> The command word is Explain, so naming perfective on its own will not score all three marks. You have to say what corrective maintenance actually is, and why this change does not match it.

### Q12
**Final answer:** **Corrective**

Corrective maintenance. **[1]**

**[1 mark]**

> **[mark-scheme]**
> **1 mark** for Corrective
> 
> Accept corrective on its own, without the word maintenance.
> 
> Do not accept perfective, because the program was not working correctly before the change.
> 
> Do not accept adaptive, because nothing has changed outside the program: the hardware, the software it runs with and the law are all the same.

> **[exam-tip]**
> Many students answer perfective here, because the program has been improved. Perfective maintenance is only used when the program already produces the correct results and is made better in some way. If a fault is put right, the answer is always corrective.
> 
> Only three types of maintenance are named in this syllabus: corrective, perfective and adaptive. Preventive maintenance is not one of them, so it will not earn a mark.

### Q13
> **[mark-scheme]**
> One mark per error:
> 
> Syntax:
> 
> 1. `NEXT Index `(should be `ENDWHILE`)
> 
> 2. '&' used to concatenate an integer (in `OUTPUT `statement)
> 
> Other:
> 
> 3. Accesses element outside range // Accesses element 0
> **[mark-scheme]**
> Run-time

### Q14
> **[mark-scheme]**
> One mark for method – two marks for the description
> 
> **MP1 **Stub testing
> 
> **MP2 **The modules `Test_A()`<u> and </u>`Test_B()`are replaced by dummy modules
> 
> **MP3 **... which return a known result // An output statement is displayed when called (to check it works) // gives expected output

### Q15
> **[mark-scheme]**
> **MP1**` Count ← INT(100 / Number)`
> Number could be zero (giving a divide by zero)
> 
> **MP2**` Index ← Data[Number]`
> Potential error: Value Number could be outside the range of array indices
> 
> **MP3 **`ReturnValue ← TO_UPPER(RIGHT(Label, Count))`
> Potential Error: Number to extract may be too big / negative / out of range for use in the RIGHT function // Label has insufficient characters
> 
> **MP4**` RETURN RetVal`
> Potential Error: There is no value to be returned // there is no variable named `RetVal`
> 
> Mark as follows:
> 1 mark for each statement <u>**and **</u>description
> **Max 3 marks**

### Q16
> **[mark-scheme]**
> (i) One mark per row
> 
> | Type of test data | Test data value | Expected result |
> |---|---|---|
> | Abnormal | 12 (< 23) | FALSE |
> | Abnormal / Boundary / Extreme | 23 | FALSE |
> | Boundary / Extreme | 24 | TRUE |
> | Boundary | 25 | TRUE |
> | Boundary | 36 | TRUE |
> | Boundary /Extreme | 37 | TRUE |
> | Abnormal / Boundary / Extreme | 38 | FALSE |
> | Abnormal | 99 (> 38) | FALSE |
> 
> **Max 4 marks**
> 
> (ii) Integration (testing)

### Q17
> **[mark-scheme]**
> One mark per point:
> 
> **Type**: Run-time error
> 
> **Cause**: A divide by zero operation is attempted // Attempt to convert a nonnumeric string to a number

### Q18
> **[mark-scheme]**
> One mark per point:
> 
> Error: The **calculation **of TaxPayable is incorrect
> 
> Correction: TaxPayable  (ItemCost * TaxRate) / 100

### Q19
> **[mark-scheme]**
> - **MP1**    Type: Adaptive
> - **MP2**   Reason: The (user) requirement(s) changes // to accommodate legislative changes

### Q20
> **[mark-scheme]**
> **One** mark per set, including stated purpose. Max 3 marks
> 
> Example answers:
> 
> 1   data set with (only) odd values, terminated with 99 
> 2   data set with (only) even values, terminated with 99 
> 3   data sets with same number of odd and even values, terminated with 99 
> 4   data sets with all even / all odd with just one odd/even value, terminated with 99 
> 5   data sets with no values just final 99 
> 6   data sets without (terminating) 99 // missing or incorrectly placed 99

### Q21
> **[mark-scheme]**
> - **MP1 **    `Num > Min` should be `Num < Min `
> - **MP2 **  `Count & 1 `should be `Count + 1 `
> - **MP3**` NextInput  "END"` should be `NextInput = "END"`
> **[mark-scheme]**
> (i)
> 
> - **MP1 **   If all the numeric input values are greater than 999 // If there are no numeric values in the sequence
> - **MP2**    then the minimum will be given as <u>**999 **</u>(and not one of the input values) (ii) Many possible correct answers, for example:
> - **MP1  **  Mixture non-numeric and numeric with 3 or 4 values - with all numerics 
> greater than 999 
> Examples: 1325, DOG, 7868, 7615 
> // SNAKE, 3478, SPIDER
> - **MP2**    Final value: END
