# Exam Questions — Arrays
**8. Programming** · Cambridge (CIE) IGCSE computer-science (0478 & 0984)
> Source: [https://www.savemyexams.com/igcse/computer-science/cie/23/topic-questions/](https://www.savemyexams.com/igcse/computer-science/cie/23/topic-questions/) · 7 questions across 1 sets


## Exam Questions (7 questions)


### Q1 — hard — 15 marks

**Q1** [15 marks]

A two-dimensional (2D) array `StudentData[]` contains student information for a school management system.

A 2D array `Grades[]` has three columns containing the following academic details:

- column one stores the current average grade – the student's overall percentage score, for example 78.5
- column two stores the minimum grade threshold – the lowest percentage required to pass the course, for example 40.0
- column three stores the maximum assignment score – the highest score achieved on any single assignment, for example 95.0

A student's average grade can fall below the minimum threshold (failing status) but appropriate warnings must be displayed.

For example, a student with a minimum threshold of 40.0 must have an average grade of at least 40.0 to maintain passing status.

Suitable messages must be displayed for grade updates, for example if a new grade would cause the student to fail or if an invalid grade is entered.

The student ID gives the index of each student's data held in the two arrays. For example, student ID 15's details would be held in:

`StudentData[15,1]` and `StudentData[15,2]` for name and class

`Grades[15,1]`, `Grades[15,2]` and `Grades[15,3]` for academic data

The variable TotalStudents contains the number of registered students.

The arrays and variable TotalStudents have already been set up and the data stored.

**Write a program** that meets the following requirements:

- checks the student ID exists and the name and class entered by the user match the name and class stored in `StudentData[]` before any action can take place
- displays a menu showing the four actions available for the user to choose from:

- **display grades**
- **update average grade**
- **add assignment score**
- **exit**

- allows an action to be chosen and completed. Each action is completed by a procedure with a parameter of the student ID.

You **must use** pseudocode or program code and add comments to explain how your code works. All inputs and outputs must contain **suitable messages**.

You only need to declare any local arrays and local variables that you use.

You **do not** need to declare and initialise the data in the global arrays `StudentData[]` and `Grades[]` and the variable TotalStudents.

### Q2 — hard — 15 marks

**Q2** [15 marks]

The one-dimensional (1D) array `Clubs[]` is used to store the names of 12 cricket clubs in a local sports league.

The two-dimensional (2D) array `Statistics[][]` is used to store, for each cricket club, the number of:

- matches won
- matches drawn
- matches lost.

The 1D array `Points[]` is used to store the total number of points each cricket club has been awarded.

The position of any cricket club’s data is the same in all three arrays. For example, the data in index 2 of `Statistics[]` and index 2 of `Points[]` belongs to the cricket club in index 2 of `Clubs[]`.

The variable `Matches` stores the number of matches played by each team. Each team plays the same number of matches.

Points are awarded for:

- a win – 12 points
- a draw – 5 points
- a loss – 0 points.

**Write a program that meets the following requirements:**

- allows the number of matches played to be input and stored, with a maximum of 22 matches
- validates the number of matches played
- allows the names of the cricket clubs to be input and stored
- allows the number of matches won, drawn and lost to be input and stored for each team
- validates the number of matches won, drawn or lost against the number of matches played
- asks the user to re-enter the number of matches won, drawn or lost if the total does not match the number of matches played
- calculates and stores the total number of points for each club
- finds the cricket club or clubs with the highest number of points
- outputs the name or names of the winning club or clubs, the number of wins and the total number of points awarded.

You **must use** pseudocode or program code and add comments to explain how your code works.

You **do not** need to declare any arrays or variables; you may assume that this has already been done.

All inputs and outputs **must **contain suitable messages.

*Source: June 2024 0478/21 Q10*


### Q3 — hard — 15 marks

**Q3** [15 marks]

A two-dimensional (2D) array `Account[]` contains account holders’ names and passwords for a banking program.

A 2D array `AccDetails[] `has three columns containing the following details:

- column one stores the balance – the amount of money in the account, for example 250.00
- column two stores the overdraft limit – the maximum total amount an account holder can borrow from the bank after the account balance reaches 0.00, for example 100.00
- column three stores the withdrawal limit – the amount of money that can be withdrawn at one time, for example 200.00

The amount of money in a bank account can be negative (overdrawn) but not by more than the overdraft limit.
For example, an account with an overdraft limit of 100.00 must have a balance that is greater than or equal to –100.00

Suitable error messages must be displayed if a withdrawal cannot take place, for example if the overdraft limit or the size of withdrawal is exceeded.

The bank account ID gives the index of each account holder’s data held in the two arrays. For example, account ID 20’s details would be held in:
`Account[20,1]` and `Account[20,2] AccDetails[20,1], AccDetails[20,2] `and `AccDetails[20,3]`

The variable Size contains the number of accounts

The arrays and variable Size have already been set up and the data stored

**Write a program** that meets the following requirements:

- checks the account ID exists and the name and password entered by the account holder match the name and password stored in` Account[] `before any action can take place
- displays a menu showing the four actions available for the account holder to choose from:

  - **display balance **
  - **withdraw money **
  - **deposit money **
  - **exit **

- allows an action to be chosen and completed. Each action is completed by a procedure with a parameter of the account ID.

You **must use** pseudocode or program code and add comments to explain how your code works. All inputs and outputs must contain** suitable messages**.

You only need to declare any local arrays and local variables that you use.

You **do not** need to declare and initialise the data in the global arrays `Account[]` and `AccDetails[]` and the variable Size

*Source: June 2023 0478/22 Q12*


### Q4 — hard — 15 marks

**Q4** [15 marks]

A one-dimensional (1D) array `Days[]` contains the **names of the days of the week**. A two-dimensional (2D) array `Readings[]` is used to **store 24 temperature readings**, taken once an hour, for each of the seven days of the week. A 1D array `AverageTemp[] `is used to **store the average temperature** for each day of the week.

The position of any day’s data is the same in all three arrays. For example, if Wednesday is in index 4 of `Days[]`, Wednesday’s temperature readings are in index 4 of `Readings[] `and Wednesday’s average temperature is in index 4 of `AverageTemp[]`

The temperature readings are in **Celsius **to **one decimal place**. Temperatures can only be from **–20.0°C to +50.0°C inclusive**.

**Write a program** that meets the following requirements:

- input and validate the hourly temperatures for one week
- calculate and store the average temperature for each day of the week
- calculate the average temperature for the whole week
- convert all the average temperatures from Celsius to Fahrenheit by using the formula Fahrenheit = Celsius * 9/5 + 32
- output the average temperature in Celsius and in Fahrenheit for each day
- output the overall average temperature in Celsius and in Fahrenheit for the whole week.

You must use **pseudocode **or** program code** and **add comments to explain** how your code works.

You do **not **need to declare any arrays, variables or constants; you may assume that this has already been done.

All inputs and outputs **must **contain suitable messages.

All data output **must **be rounded to one decimal place

You will need to **initialise **and **populate **the array` Days[]` at the start of the program

*Source: June 2023 0478/21 Q11*


### Q5 — hard — 2 marks

**Q5** [2 marks]

**Explain **how indexing could be used to search for a value stored in a one-dimensional array.

*Source: June 2022 0478/22 Q3B*


### Q6 — medium — 3 marks

**Q6** [3 marks]

**Describe** a one-dimensional array.

Include **an example** of an array declaration.

*Source: June 2022 0478/22 Q3A*


### Q7 — easy — 1 marks

**Q7** [1 mark]

**Tick (✓) one box** to show the name of the data structure used to store a collection of data of the same data type.

*Source: June 2023 0478/21 Q2A*

