# Mark Schemes — Identifying Errors
**7. Algorithm Design & Problem-Solving** · Cambridge (CIE) IGCSE computer-science (0478 & 0984)


## Exam Questions (5 questions)


### Q1
The lines that contain errors are:

- **Line 4**        `WHILE Number <= 99 OR Number >= 1001 `**[1 mark]**
- **Line 7 **       `Num[Index] ← Number `**[1 mark]**
- **Line 9**        `NEXT Index `**[1 mark]**
- **Line 10**     `PRINT Count `**[1 mark]**

> **[mark-scheme]**
> - One mark for each error identified plus suggested correction

### Q2
The three errors in the pseudocode are:

** Line 07**` Total `$\leftarrow$` Total + Number * Counter `

- … *should be *`Total `$\leftarrow$`  Total + Number[Counter] * Counter `**[1 mark]**

**Line 08**` IF Number[Counter] = 0 `

- … should be `IF Number[Counter] = -1` **OR**  `IF Number[Counter] < 0 `**[1 mark]**

**Line 16**` FOR Counter `$\leftarrow$`  0 TO 5 `

- … should be `FOR Counter `$\leftarrow$`  1 TO 5 `**[1 mark]**

### Q3
The four errors in the pseudocode are:

**Line 04**

- `IF Number < 0 `

  - should be `IF Number > 0` **[1 mark]**

**Line 10 or 'line 01 and line 02'**

- `Exit ← 1 `**OR**` 'Exit ← 1 `**AND  **`WHILE Exit <> 0' `

  - should be` Exit ← 0 `**OR**  `Exit ← 0 `**and  **`WHILE Exit = 0 `**[1 mark]**

**Line 13**

- `ENDIF `

  - should be` ENDWHILE `**[1 mark]**

**Line 14**

- `OUTPUT "The total value of your numbers is ", Number `

  - should be` OUTPUT "The total value of your numbers is ", Total `**[1 mark]**

> **[exam-tip]**
> **Correct algorithm:**

### Q4
The three errors in the pseudocode are:

**line 8** / `PassCheck `$\leftarrow$`TRUE `

- … correction `PassCheck `$\leftarrow$`FALSE `**[1 mark]**

**line 12** /` IF Password <> Password `

- …` `correction `IF Password2 <> Password `**OR**` IF Password <> Password2 `**[1 mark]**

**line 18** / `UNTIL PassCheck OR Attempt <> 3 `

- … correction `UNTIL PassCheck OR Attempt = 3 / UNTIL PassCheck OR Attempt >= 3 `**[1 mark]**

### Q5
The four errors in the pseudocode are:

`Numbers `

- … should be `Number `**[1 mark]**

`IF Number > 100`

- … should be `IF Number >= 100` **[1 mark]**

`INPUT Number` missing from inside the loop

- … insert `INPUT Number` after the `ENDIF `statement **[1 mark]**

The final `OUTPUT Number` is not needed

- … remove it **[1 mark]**
The pseudocode statement would be:

- ` IF Number >= 100 AND Number <= 200 `
- both ends of the range and correct inequality symbols **[1 mark]**
- `AND `**OR**  nested IFs **[1 mark]**
