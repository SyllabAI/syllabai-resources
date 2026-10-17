# Exam Questions — Identifying Errors
**7. Algorithm Design & Problem-Solving** · Cambridge (CIE) IGCSE computer-science (0478 & 0984)
> Source: [https://www.savemyexams.com/igcse/computer-science/cie/23/topic-questions/](https://www.savemyexams.com/igcse/computer-science/cie/23/topic-questions/) · 5 questions across 1 sets


## Exam Questions (5 questions)


### Q1 — hard — 4 marks

**Q1** [4 marks]

This section of program code asks for 80 numbers between 100 and 1000 inclusive to be entered. The pseudocode checks that the numbers are in the correct range and then stores the valid numbers in an array. It counts how many of the numbers are larger than 500 and then outputs the result when finished.

**There are four lines of code **that **contain errors**.

**State **the line number for each error and **write** the correct code for that line.

*Source: Specimen 2023 0478/02 2B Q6*


### Q2 — medium — 3 marks

**Q2** [3 marks]

An algorithm has been written in pseudocode to calculate a check digit for a four-digit number. The algorithm then outputs the five-digit number including the check digit. The algorithm stops when –1 is input as the fourth digit.

**Identify the three errors** in the pseudocode and **suggest a correction **for each error.

*Source: June 2023 0478/22 Q7B*


### Q3 — medium — 4 marks

**Q3** [4 marks]

An algorithm has been written in pseudocode to allow some numbers to be input. All the positive numbers that are input are totalled and this total is output at the end. An input of 0 stops the algorithm.

**Identify the four errors **in the pseudocode and **suggest a correction** for each error.

*Source: June 2023 0478/21 Q5A*


### Q4 — medium — 3 marks

**Q4** [3 marks]

An algorithm allows a user to input their password and checks that there are at least eight characters in the password. Then, the user is asked to re-input the password to check that both inputs are the same. The user is allowed three attempts at inputting a password of the correct length and a matching pair of passwords.

The pre-defined function `LEN(X) `returns the number of characters in the string, `X`

**Identify the three errors **in the pseudocode and **suggest a correction** to remove each error.

*Source: June 2022 0478/22 Q2A*


### Q5 — hard — 6 marks

**Q5** [4 marks]

An algorithm has been written in pseudocode to input some numbers. It only outputs any numbers that are greater than or equal to 100. The number 999 is not output and stops the algorithm.

`INPUT Number`
`WHILE Numbers <> 999 DO`
`   IF Number > 100`
`      THEN`
`         OUTPUT Number`
`   ENDIF`
`ENDWHILE`
`OUTPUT Number`

**Identify the four errors** in the pseudocode and **suggest corrections**.

*Source: Specimen 2023 Paper 2 Q5A*


**Q5** [2 marks]

**Extract:**

An algorithm has been written in pseudocode to input some numbers. It only outputs any numbers that are greater than or equal to 100. The number 999 is not output and stops the algorithm.

INPUT Number

WHILE Numbers <> 999 DO

   IF Number > 100

      THEN

         OUTPUT Number

   ENDIF

ENDWHILE

OUTPUT Number

The four errors in the pseudocode are:

Numbers 

- … should be Number

 IF Number > 100 

- … should be IF Number >= 100

INPUT Number missing from inside the loop

- … insert INPUT Number after the ENDIF statement

The final OUTPUT Number is not needed

- … remove it

**Write a pseudocode statement **to change the corrected algorithm to output all numbers between 100 and 200 inclusive.

You **do not **need to rewrite the whole algorithm

*Source: Specimen 2023 Paper 2 Q5B*

