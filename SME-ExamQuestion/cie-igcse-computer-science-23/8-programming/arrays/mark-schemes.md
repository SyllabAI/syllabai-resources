# Mark Schemes — Arrays
**8. Programming** · Cambridge (CIE) IGCSE computer-science (0478 & 0984)


## Exam Questions (7 questions)


### Q1
The provided solutions are just two of many possible solutions; as long as your code **effectively addresses the problem**, it is equally valid and can receive full marks.

**Pseudocode**

`// Procedures to be called`

`PROCEDURE CheckDetails(StudID : INTEGER)`

`    DECLARE Name, Class : STRING // local variables`

`    Valid ← FALSE`

`    IF StudID < 0 OR StudID > TotalStudents`

`      THEN`

`        OUTPUT "Invalid Student ID"`

`      ELSE`

`        OUTPUT "Please Enter Student Name "`

`        INPUT Name`

`        OUTPUT "Please Enter Class "`

`        INPUT Class`

`        IF Name <> StudentData[StudID,1] OR Class <> StudentData[StudID,2]`

`          THEN`

`            OUTPUT "Invalid name or class"`

`          ELSE`

`            Valid ← TRUE`

`        ENDIF`

`      ENDIF`

`ENDPROCEDURE`

`PROCEDURE DisplayGrades(StudID : INTEGER)`

`    OUTPUT "Current average grade: ", Grades[StudID,1]`

`    OUTPUT "Minimum threshold: ", Grades[StudID,2]`

`    OUTPUT "Highest assignment score: ", Grades[StudID,3]`

`ENDPROCEDURE`

`PROCEDURE UpdateAverage(StudID : INTEGER)`

`    DECLARE NewGrade : REAL // local variable`

`    REPEAT`

`        OUTPUT "Please enter new average grade (0-100) "`

`        INPUT NewGrade`

`        IF NewGrade < 0 OR NewGrade > 100`

`          THEN`

`            OUTPUT "Grade must be between 0 and 100"`

`        ENDIF`

`        IF NewGrade < Grades[StudID,2]`

`          THEN`

`            OUTPUT "Warning: Grade below minimum threshold"`

`        ENDIF`

`        IF NewGrade >= 0 AND NewGrade <= 100`

`          THEN`

`            Grades[StudID,1] ← NewGrade`

`            OUTPUT "Average grade updated successfully"`

`        ENDIF`

`    UNTIL NewGrade >= 0 AND NewGrade <= 100`

`ENDPROCEDURE`

`PROCEDURE AddAssignment(StudID : INTEGER)`

`    DECLARE Score : REAL // local variable`

`    REPEAT`

`        OUTPUT "Please enter assignment score (0-100) "`

`        INPUT Score`

`        IF Score < 0 OR Score > 100`

`          THEN`

`            OUTPUT "Score must be between 0 and 100"`

`        ENDIF`

`    UNTIL Score >= 0 AND Score <= 100`

`    IF Score > Grades[StudID,3]`

`      THEN`

`        Grades[StudID,3] ← Score`

`        OUTPUT "New highest assignment score recorded"`

`      ELSE`

`        OUTPUT "Assignment score recorded"`

`    ENDIF`

`ENDPROCEDURE`

`// Main program`

`DECLARE StudentID, Choice : INTEGER`

`DECLARE Valid, Exit : BOOLEAN`

`OUTPUT "Please enter student ID "`

`INPUT StudentID`

`CheckDetails(StudentID)`

`IF Valid`

`  THEN`

`    REPEAT`

`      OUTPUT "Menu"`

`      OUTPUT "1. display grades"`

`      OUTPUT "2. update average grade"`

`      OUTPUT "3. add assignment score"`

`      OUTPUT "4. exit"`

`      OUTPUT "Please choose 1, 2, 3 or 4"`

`      INPUT Choice`

`      CASE OF Choice`

`        1 : DisplayGrades(StudentID)`

`        2 : UpdateAverage(StudentID)`

`        3 : AddAssignment(StudentID)`

`        4 : Exit ← TRUE`

`        OTHERWISE OUTPUT "Invalid choice"`

`      ENDCASE`

`    UNTIL Choice = 4`

`  ELSE`

`    OUTPUT "Access denied"`

`ENDIF`

**Python**

> **[mark-scheme]**
> You must include the following in your solution to achieve a maximum score:
> 
> 1. **Techniques:**
> 2. Check student ID and authentication (**iteration** and **validation**, **selection**, **input**, **output**)
> 3. Display menu and make a selection (**output**, **input** and **selection**)
> 4. Perform actions selected (use of **arrays** and **procedures** with **parameters**)
> 
> 1. **Data Structures:**
> 
> required names shown underlined must be used as given in the scenario
> 
> 1. **Arrays or lists**: `StudentData, Grades`
> 2. **Variables**: `TotalStudents, StudentID`

> **[exam-tip]**
> - **All criteria** stated for the scenario have been covered by the use of **appropriate** programming techniques
> - The data structures used **store all the data that is required** by the scenario
> - **All** the data structures used have **meaningful names**
> - Solution **logically performs** **all the tasks** given in the scenario

### Q2
**Example 15 mark solution:**

**Data structures required:**

The names <u>underlined</u> must match those given in the scenario:

Arrays or lists: <u>**Clubs[]**</u>**, **<u>**Statistics[]**</u>, `Points[]`, `TieIndex[]`

Variables:` `<u>**Matches**</u>, `Won, Drawn, Lost, Counter, Maximum, TieCheck, OutLoop, Max, Count`

**Requirements (techniques):**

- **One**

  - Input and store number of matches, cricket club names, number of matches won, drawn and lost.
  - Validation of number of matches played and matches won, lost and drawn against number of matches played (with prompts, iteration, storing data in variables, validation, 1D and 2D arrays).
- **Two**

  - Calculate and store the number of points for each cricket club.
  Finding the index of the array with the highest score / highest score
  (calculation, finding the maximum, iteration).
- **Three**

  - Identifying cricket clubs with highest number of points and whether there is a tie for the top position.
  - Output with appropriate messages (iteration, selection and output)

> **[mark-scheme]**
> **7-9 Marks**
> 
> - The range of programming techniques used is appropriate to the problem.
> - All criteria stated for the scenario have been covered by the use of appropriate programming techniques, check the list of techniques needed.
> - The data structures chosen are appropriate and store all the data required.
> - The data structures used store all the data required by the scenario.
> 
> **5-6 Marks**
> 
> - The program has been fully commented.
> - Suitable identifiers with names meaningful to their purpose have been used throughout.
> - All of the data structures used have meaningful names.
> - The program is in a logical order
> - The solution is accurate.
> - Solution logically performs all the tasks given in the scenario. Ignore minor syntax errors.
> - The solution meets all the requirements given in the question.
> - Solution performs all the tasks given in the scenario.
> 
> **Total: [15 marks]**

### Q3
The provided solutions are just two of many possible solutions; as long as your code **effectively addresses the problem**, it is equally valid and can receive full marks.

**Pseudocode**

`// Procedures to be called PROCEDURE CheckDetails(AccID : INTEGER) `
`    DECLARE Name, Password : STRING // local variables `
`    Valid  FALSE `
`    IF AccID <0 OR AccID > Size `
`      THEN `
`        OUTPUT "Invalid Account Number" `
`      ELSE `
`        OUTPUT "Please Enter Name " `
`        INPUT Name `
`        OUTPUT "Please Enter Password " `
`        INPUT Password `
`        IF Name <> Account[AccID,1] OR Password <> Account[AccID,2] `
`          THEN `
`            OUTPUT "Invalid name or password" `
`          ELSE`
`            Valid  True `
`         ENDIF `
`      ENDIF `
`ENDPROCEDURE `
`PROCEDURE Balance(AccID : INTEGER) `
`     OUTPUT "Your balance is ", AccDetails[AccID,1] `
`ENDPROCEDURE `

`PROCEDURE WithDrawal(AccID : INTEGER) `
`    DECLARE Amount : REAL // local variable `
`    REPEAT `
`       OUTPUT "Please enter amount to withdraw " `
`       INPUT Amount `
`       IF Amount > AccDetails[AccID,3] `
`         THEN `
`           OUTPUT "Amount greater than withdrawal limit" `
`       ENDIF `
`       IF Amount > AccDetails[AccID,2] + AccDetails[AccID,1] `
`          THEN `
`            OUTPUT "Amount greater than cash available" `
`       ENDIF `
`       IF Amount <= AccDetails[AccID,3] AND Amount < AccDetails[AccID,2] + AccDetails[AccID,1] `
`          THEN `
`            AccDetails[AccID,1]  AccDetails[AccID,1] - Amount `
`       ENDIF `
`   UNTIL Amount<= AccDetails[AccID,3] AND Amount > AccDetails[AccID,2] + AccDetails[AccID,1] AND Amount > 0 `
`ENDPROCEDURE `

`PROCEDURE Deposit(AccID : INTEGER) `
`    DECLARE Amount : REAL // local variable `
`    REPEAT `
`      OUTPUT "Please enter a positive amount to deposit " `
`      INPUT Amount `
`  UNTIL Amount >0 AccDetails[AccID,1]  AccDetails[AccID,1] + Amount`
`ENDPROCEDURE `
`// Declarations of global variables for information – not required in candidate responses `
`DECLARE AccountNumber, Choice : INTEGER `
`DECLARE Valid, Exit : BOOLEAN `

`OUTPUT "Please enter your account number " `
`INPUT AccountNumber `
`CheckDetails(AccountNumber) `

`IF Valid `
`  THEN `
`    REPEAT `
`      OUTPUT "Menu" `
`      OUTPUT "1. display balance" `
`      OUTPUT "2. withdraw money" `
`      OUTPUT "3. deposit money" `
`      OUTPUT "4. exit" `
`      OUTPUT "please choose 1, 2, 3 or 4" `
`      INPUT Choice `
`      CASE OF Choice `
`        1 : Balance(AccountNumber) `
`        2 : Withdrawal(AccountNumber) `
`        3 : Deposit(AccountNumber) `
`        4 : Exit  TRUE `
`        OTHERWISE OUTPUT "Invalid choice" `
`      ENDCASE `
`   UNTIL Choice = 4 `
`  ELSE `
`   OUTPUT "Invalid account number " `
`ENDIF`

**Python**

> **[mark-scheme]**
> You must include the following in your solution to achieve a maximum score:
> 
> 1. **Techniques:**
> 
>   1. Check account number and password (**iteration **and **validation**, **selection**, **input**, **output**)
>   2. Display menu and make a selection (**output**, **input** and **selection**)
>   3. Perform actions selected (use of **arrays **and **procedures **with **parameters**)
> 2. **Data Structures:** required names shown underlined must be used as given in the scenario
> 
>   1. **Arrays or lists**: `Account, AccDetails`
>   2. **Variables**: `Size, AccountNumber`

> **[exam-tip]**
> - **All criteria** stated for the scenario have been covered by the use of **appropriate** programming techniques
> - The data structures used **store all the data that is required** by the scenario
> - **All** the data structures used have **meaningful names**
> - Solution** logically performs** **all the tasks **given in the scenario

### Q4
The provided solutions are just two of many possible solutions; as long as your code **effectively addresses the problem**, it is equally valid and can receive full marks.

**Pseudocode**

`// meaningful identifiers and appropriate data structures for `
`// all data required `
`DECLARE Days : ARRAY[1:7] OF STRING `
`DECLARE Readings : ARRAY[1:7, 1:24] OF REAL `
`DECLARE AverageTemp : ARRAY[1:7] OF REAL `
`DECLARE WeekLoop : INTEGER `
`DECLARE DayLoop : INTEGER `
`DECLARE InTemp : REAL`
`DECLARE TotalDayTemp : REAL `
`DECLARE TotalWeekTemp : REAL `
`DECLARE AverageWeekTemp : REAL `
`// initial population of Days[] array `
`// input and a loop are also acceptable `
`Days[1]`$\leftarrow$` "Sunday" `
`Days[2] `$\leftarrow$`  "Monday" `
`Days[3] `$\leftarrow$`  "Tuesday" `
`Days[4] `$\leftarrow$`  "Wednesday" `
`Days[5] `$\leftarrow$`  "Thursday" `
`Days[6] `$\leftarrow$`  "Friday" `
`Days[7] `$\leftarrow$`  "Saturday" `
`// input temperatures inside nested loop `
`FOR WeekLoop `$\leftarrow$`  1 TO 7 `
`      TotalDayTemp`$\leftarrow$`  0 `
`      FOR DayLoop `$\leftarrow$`  1 TO 24 `
`          OUTPUT "Enter temperature ", DayLoop, " for ", Days[WeekLoop]`
`          INPUT InTemp `
`// validation of input for between -20 and +50 inclusive `
`          WHILE InTemp < -20.0 OR InTemp > 50.0 DO `
`            OUTPUT "Your temperature must be between -20.0 and +50.0 inclusive. Please try again" `
`            INPUT InTemp `
`          ENDWHILE `
`          Readings[WeekLoop, DayLoop] `$\leftarrow$`  InTemp `
`// totalling of temperatures during the day `
`          TotalDayTemp `$\leftarrow$`  TotalDayTemp + ROUND(InTemp, 1) `
`       NEXT DayLoop `
`// average temperature for the day `
`       AverageTemp[WeekLoop] `$\leftarrow$`  ROUND(TotalDayTemp / 24,1) NEXT WeekLoop `
`// calculate the average temperature for the week `
`TotalWeekTemp`$\leftarrow$`  0 `
`FOR WeekLoop `$\leftarrow$` 1 TO 7 TotalWeekTemp `$\leftarrow$` TotalWeekTemp + AverageTemp[WeekLoop] `
`NEXT WeekLoop `
`AverageWeekTemp `$\leftarrow$`  ROUND(TotalWeekTemp / 7,1) `
`// outputs in Celsius and Fahrenheit `
`FOR WeekLoop `$\leftarrow$`  1 TO 7 `
`    OUTPUT "The average temperature on ", Days[WeekLoop], " was ", AverageTemp[WeekLoop], " Celsius and ",      `
`        ROUND(AverageWeekTemp  9 / 5 + 32), 1, " Fahrenheit" `
`NEXT WeekLoop `
`OUTPUT "The average temperature for the week was ", AverageWeekTemp," Celsius and ", ROUND(AverageWeekTemp  9 / 5 + 32, 1)," Fahrenheit"`

**Python**

> **[mark-scheme]**
> You **must **include the following in your solution to achieve a maximum score:
> 
> 1. **Techniques**:
> 
>   1. Input and store hourly temperatures and validation of input temperatures for each day (with **prompts**, **range check** and (**nested**)**iteration**)
>   2. Calculate, round to one decimal place and store daily average temperatures and calculate the weekly average temperature rounded to one decimal place (**iteration**, **totalling** and **rounding**)
>   3. Convert all average temperatures to Fahrenheit (to one decimal place) and output the average temperatures in both Celsius and Fahrenheit. Output with appropriate messages. (**output **and **rounding**)
> 2. **Data structures: **
> The names underlined must match those given in the scenario
> 
>   1. **Arrays or lists:** `Days[], Readings[], AverageTemp[]`
>   2. **Variables: **`WeekLoop, DayLoop, InTemp, TotalDayTemp, TotalWeekTemp, AverageWeekTemp`

> **[exam-tip]**
> - **All criteria** stated for the scenario have been covered by the use of **appropriate** programming techniques
> - The data structures used **store all the data that is required** by the scenario
> - **All** the data structures used have **meaningful names**
> - Solution** logically performs** **all the tasks **given in the scenario

### Q5
Indexing could be used by:

- using a counter to index the array **[1 mark]**
- … so that the same code can be repeatedly used to check every element **OR** every element can be checked in a loop **[1 mark]**

### Q6
A one-dimensional array is described as:

Any **two **of the following:

- a list / one column of items **[1 mark]**
- … of the same data type **[1 mark]**
- … stored under a single identifier **[1 mark]**
- … with a single index to identify each element **[1 mark]**

**One **mark for an example of a declaration

- example e.g. `DECLARE MyArray[1:10] OF INTEGER `**[1 mark]**

### Q7
**Final answer:** **The correct answer is ****A**

- **A **is correct as an array is described as a data structure used to store a collection of data of the same data type **[1 mark]**
- **B **is incorrect as a constant is an identifier set once in the lifetime of a program
- **C **is incorrect as a function is a sub program that returns a value
- **D **is incorrect as a variable is an identifier that can change in the lifetime of a program
