# Mark Schemes — SQL
**9. Databases** · Cambridge (CIE) IGCSE computer-science (0478 & 0984)


## Exam Questions (8 questions)


### Q1
- `SUM` **[1 mark]**
- `NumberInStock` **[1 mark]**
- `SoftDrinks` **[1 mark]**
- `Container` **[1 mark]**
- '`Can`' **[1 mark]**

### Q2
The completed SQL query would be:

- `SELECT Class, SUM(Score)`
`FROM students`
`GROUP BY Class`
`ORDER BY Class;`

- Correct use of `SELECT `statement** [1 mark]**
- Correct use of `SUM(Score)` to calculate total score **[1 mark]**
- Correct use of `FROM students `**[1 mark]**
- Correct use of `GROUP BY Class` to group results by class **[1 mark]**

> **[exam-tip]**
> Remember that `ORDER BY` only sorts rows — it is `GROUP BY` that aggregates values into one result per group.
> 
> Whenever you use an aggregate function like `SUM()` alongside another field, group by that field.
The completed SQL would be:

- `SELECT COUNT(*)` `FROM students` `WHERE Score > 75;`
- Correct use of `SELECT `statement with `COUNT(*)`  **[1 mark]**
- Correct use of `FROM students `**[1 mark]**
- Correct use of `WHERE` clause to filter scores greater than 75 **[1 mark]**

### Q3
The purpose of the SQL statements is to:

- Find the total number of minutes of music** [1 mark]**
- Find the total number of songs **[1 mark]**
- … available for the genre rock **[1 mark]**

### Q4
The completed SQL statement is:

- `SELECT TVCode, `**ScreenSize**`, `**Price\$**`,`
**FROM**` TVRange `
`WHERE SmartTV = `**YES**`;`

### Q5
The completed SQL query is:

- `SELECT CatNo, Title `

**FROM **`2018MOV `

`WHERE Genre1 = `**"Comedy"**`;`

### Q6
The output of the SQL statement would be:

- 03 Nov Acoustic Evening **[2 marks]**

> **[mark-scheme]**
> - **One** mark for correct content
> - **One** mark for correct field order
