# Mark Schemes — Data Definition Language (DDL) & Data Manipulation Language (DML)
**8. Databases** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (17 questions)


### Q1
**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `SELECT GUEST.FullName` together with `COUNT(BOOKING.BookingID)`
> 
> **1 mark** for `AS NumberOfBookings`
> 
> **1 mark** for linking the two tables on the matching key field, either as `FROM GUEST INNER JOIN BOOKING ON GUEST.GuestID = BOOKING.GuestID` or as `FROM GUEST, BOOKING` with `WHERE GUEST.GuestID = BOOKING.GuestID`
> 
> **1 mark** for `GROUP BY GUEST.FullName;`
> 
> Accept `COUNT(BOOKING.GuestID)` or `COUNT(*)` in place of `COUNT(BOOKING.BookingID)`.
> 
> Accept `GROUP BY GUEST.GuestID, GUEST.FullName;`.
> 
> Accept `JOIN` written without the word `INNER`.
> 
> Do not accept a script with no `GROUP BY` clause. It returns one number for the whole table instead of one number for each guest.
> 
> Do not accept `SUM(BOOKING.BookingID)`. That adds the booking ID values together instead of counting the bookings.

> **[exam-tip]**
> `GROUP BY` is what turns one total into one total per guest. Whenever a question says for each, a `GROUP BY` is almost always needed, and the field you group by is the same field you list in the `SELECT` clause beside the aggregate.
> 
> When two tables are involved, write the table name in front of every field name, even where it is not strictly needed. `GuestID` on its own is ambiguous because it exists in both tables, and a separate mark is available for writing the link between the tables correctly.

### Q2
All four values are correct and in the same order as the fields. **[1]** The three text values are inside quotation marks and the Boolean value `TRUE` is not.

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `INSERT INTO GUEST`
> 
> **1 mark** for `VALUES` followed by brackets
> 
> **1 mark** for all four values correct and in the same order as the fields
> 
> Accept the shorter form `INSERT INTO GUEST VALUES(...)` with the field names left out, because a value is given for every field and the values are in table order.
> 
> Accept single quotation marks in place of double quotation marks.
> 
> Do not accept an `UPDATE GUEST SET ...` script. `UPDATE` changes a record that already exists; this question adds a new one.

> **[exam-tip]**
> Two forms of `INSERT INTO` are accepted. You may list the field names after the table name and then give the values in the same order, or you may leave the field names out. If you leave them out you must supply a value for every field and the values must be in exactly the table order, so listing the field names is the safer habit.
> 
> Quotation marks still matter. Text values go in quotation marks; numbers and the Boolean values `TRUE` and `FALSE` do not. Check the data type of each field before you decide.

### Q3
**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `SELECT RoomNumber` with `FROM ROOM` and the condition `WHERE MaxGuests >= 4`
> 
> **1 mark** for `ORDER BY RoomNumber;`
> 
> Accept `WHERE MaxGuests > 3`.
> 
> Accept `ORDER BY RoomNumber ASC;`.
> 
> Accept `ROOM.RoomNumber` and `ROOM.MaxGuests` with the table name written in front of the field name.
> 
> Do not accept `WHERE MaxGuests > 4`. That leaves out the rooms that sleep exactly four.
> 
> Do not accept `SELECT *`. The question asks for the room number only, not the whole record.

> **[exam-tip]**
> Four or more includes four, so the operator is `>=` and not `>`. Read the condition twice before you write it: more than four, four or more, and at least four do not all mean the same thing, and one wrong symbol loses the mark.
> 
> `SELECT` lists the fields you want returned. If the question names one field, list that one field. `SELECT *` returns the whole record and does not answer the question that was asked.

### Q4
(i)

(ii)

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `ALTER TABLE HIRE` in part (i)
> 
> **1 mark** for `ADD EndTime TIME;` with the field name and a suitable data type
> 
> **1 mark** for `ALTER TABLE HIRE` in part (ii)
> 
> **1 mark** for `ADD FOREIGN KEY(BicycleID) REFERENCES BICYCLE(BicycleID);`
> 
> Accept `ADD COLUMN EndTime TIME;` in part (i).
> 
> Accept the two clauses of either script written on one line.
> 
> Do not accept `CREATE TABLE HIRE` in either part. The table already exists, and changing the definition of an existing table uses `ALTER TABLE`.
> 
> Do not accept `ALTER TABLE BICYCLE` in part (ii). The foreign key is added to the table that holds the linking field, which is `HIRE`.

> **[exam-tip]**
> `ALTER TABLE` names the table you are changing, and for a foreign key that is always the table holding the linking field, never the table the key points to. Here `HIRE` holds `BicycleID`, so `HIRE` is altered and `BICYCLE` appears only after `REFERENCES`. Writing these the wrong way round is the most common error on this question type.
> 
> Learn the second line as one fixed pattern: `FOREIGN KEY(field) REFERENCES Table(Field)`. The name in the brackets after `REFERENCES` is the primary key of the other table, so the two field names are often the same word, but they do not have to be.

### Q5
**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `CREATE TABLE BICYCLE(` with a matching closing bracket, so that every field definition sits inside the brackets
> 
> **1 mark** for `BicycleID` as `CHARACTER(6)` and `Model` as `VARCHAR(n)`
> 
> **1 mark** for `DatePurchased` as `DATE` and `Electric` as `BOOLEAN`
> 
> **1 mark** for `PRIMARY KEY(BicycleID)`
> 
> Accept `VARCHAR(n)` for `BicycleID`, with any sensible length.
> 
> Accept `NOT NULL` on any field, and accept the script without it.
> 
> Accept keywords written in lower case or mixed case.
> 
> Do not accept `Electric` as `VARCHAR` or `CHARACTER`. The field holds only `TRUE` or `FALSE` and `BOOLEAN` is on the list of supported types.
> 
> Do not accept `DatePurchased` as `VARCHAR` or `INTEGER`. `DATE` is on the list of supported types.

> **[exam-tip]**
> Read the list of supported data types before you start writing, then choose only from that list. Marks are lost every session for storing a date as text, or a `TRUE` and `FALSE` field as text, when `DATE` and `BOOLEAN` were both printed in the question.
> 
> The other easy mark to lose is the bracket. `CREATE TABLE` opens a bracket after the table name, and every field definition goes inside it, including the `PRIMARY KEY` line. Close the bracket and finish with a semicolon.

### Q6
**[1 mark]**

> **[mark-scheme]**
> **1 mark** for `CREATE DATABASE CYCLE_HIRE;`
> 
> Accept the database name written in any case.
> 
> Accept the script without the closing semicolon.
> 
> Do not accept `CREATE TABLE CYCLE_HIRE;`. That creates a table inside a database, not the database itself.
> 
> Do not accept `CREATE DATABASE` with brackets, field names or data types after the name. There are no tables in the database yet.

> **[exam-tip]**
> This is a one line answer worth a whole mark, so learn the exact wording. Two keywords, the name, and nothing else.
> 
> `CREATE DATABASE` and `CREATE TABLE` are both Data Definition Language commands but they do different jobs. You create the database once, then you create a table inside it for each entity. Students who add field definitions to `CREATE DATABASE` have merged the two commands and lose the mark.

### Q7
`SUM` should be `COUNT`. The query needs the number of lessons, not the total of the ID values. **[1]**

The `FROM` clause names only one table. Both tables are used, so it should read `FROM STUDENT, LESSON` **[1]**

Silva is a text value, so it must be inside quotation marks: `WHERE STUDENT.LastName = "Silva"` **[1]**

`OR` should be `AND`. Both conditions have to be true at the same time. **[1]**

The corrected script is:

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `SUM` should be `COUNT`
> 
> **1 mark** for the second table is missing from the `FROM` clause // `FROM STUDENT, LESSON`
> 
> **1 mark** for the text value needs quotation marks // `LastName = "Silva"`
> 
> **1 mark** for `OR` should be `AND`
> 
> Accept single quotation marks in place of double quotation marks.
> 
> Accept `FROM STUDENT INNER JOIN LESSON ON STUDENT.StudentID = LESSON.StudentID` as the correction to the `FROM` clause, provided the link between the tables is then taken out of the `WHERE` clause.
> 
> Do not accept the script is missing a `GROUP BY` clause. The query returns one number for one named student, so no grouping is needed.
> 
> Do not accept the semicolon is missing. It is present.

> **[exam-tip]**
> `SUM` and `COUNT` are the pair that catches most students. `SUM` adds up the values held in a field, so `SUM(LessonID)` adds ID numbers together and produces a meaningless total. `COUNT` counts how many records match, which is what how many lessons is asking for.
> 
> When a query uses two tables, check three things every time: both table names appear in the `FROM` clause, the tables are linked on their matching key fields, and the conditions are joined with `AND`. An `OR` returns every record that meets either condition on its own, which usually returns almost the whole table.

### Q8
(i)

(ii)

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `UPDATE BOOK` together with `SET OnLoan = FALSE`
> 
> **1 mark** for `WHERE BookID = "B1044";`
> 
> **1 mark** for `DELETE FROM BOOK` together with `WHERE BookID = "B1043";`
> 
> Accept single quotation marks in place of double quotation marks.
> 
> Accept the clauses written on one line.
> 
> Do not accept an `UPDATE` script with no `WHERE` clause. It marks every book in the table as returned.
> 
> Do not accept a `DELETE` script with no `WHERE` clause. It removes every record in the table.

> **[exam-tip]**
> The mark lost most often here is the `WHERE` clause. `UPDATE BOOK SET OnLoan = FALSE;` is valid SQL, so it does not look wrong on the page, but it changes every record in the table. `DELETE FROM BOOK;` empties the table completely. Before you write either command, decide which records it should touch and write the `WHERE` clause that picks out exactly those records.
> 
> Note also that `DELETE FROM` removes a whole record, never one field. To clear a single value you use `UPDATE` and set that field to a new value.

### Q9
(i) Data Definition Language (DDL) **[1]**

(ii) Data Manipulation Language (DML) **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for Data Definition Language // `DDL`
> 
> **1 mark** for Data Manipulation Language // `DML`
> 
> Accept the initials on their own for either part.
> 
> Do not accept Structured Query Language or `SQL` for either part. SQL is the whole language, and the question asks for the two parts inside it.
> 
> Do not accept Database Management System or `DBMS`. That is the software that runs the language, not a part of the language.

> **[exam-tip]**
> The two names differ by one word, so they are easy to mix up. Link the middle word to the job it does. Definition builds the structure, so `CREATE DATABASE`, `CREATE TABLE` and `ALTER TABLE` are DDL. Manipulation works on the rows inside that structure, so `SELECT`, `INSERT INTO`, `UPDATE` and `DELETE FROM` are DML.
> 
> Writing SQL earns nothing here, because both parts of the question are already about SQL.

### Q10
> **[mark-scheme]**
> **1 mark** for each bullet point.
> 
> - `SELECT Count(CourseID) `
> - `AS NumOfCourses `
> - `FROM COURSE_SCHEDULE`
> - `WHERE DateStarted > "09/09/23"; `
> 
> `SELECT Count(CourseID) AS NumOfCourses FROM `
> `COURSE_SCHEDULE `
> `WHERE DateStarted > "09/09/23";`

### Q11
> **[mark-scheme]**
> (i)
> 
> **1 mark** for
> 
> `CREATE DATABASE SHOP`;
> 
> (ii)
> 
> **1 mark** for each line **(max 4) **
> 
> Either: 
> `SELECT SUM(Quantity) `
> `FROM ORDER_ITEM, SHOP_ORDER `
> `WHERE ORDER_ITEM.OrderNo = SHOP_ORDER.OrderNo `
> `AND SHOP_ORDER.CustomerID = 'HJ231';` 
> **OR **
> `SELECT SUM(Quantity) `
> `FROM ORDER_ITEM (INNER) JOIN SHOP_ORDER `
> `ON ORDER_ITEM.OrderNo = SHOP_ORDER.OrderNo `
> `WHERE SHOP_ORDER.CustomerID = 'HJ231';`

### Q12
> **[mark-scheme]**
> **1 mark** each for:
> 
> - Creating table PERFORMANCE with opening and closing brackets
> - Setting all four attributes with appropriate data types
> - Setting PerformanceID as primary key
> - Setting ShowID as foreign key referencing SHOW table
> 
> Example: 
> `CREATE TABLE PERFORMANCE( `
> `PerformanceID varchar NOT NULL, `
> `ShowID varchar, `
> `ShowDate Date, `
> `StartTime Time, `
> `PRIMARY KEY(PerformanceID), `
> `FOREIGN KEY(ShowID) REFERENCES SHOW(ShowID) `
> `);`
> **[mark-scheme]**
> **1 mark **each for:
> 
> - Selecting COUNT of an attribute in PERFORMANCE table with suitable name
> - FROM clause
> - Joining tables
> - Grouping by the title and selecting the title
> 
> Example 1: 
> `SELECT SHOW.Title, Count(PERFORMANCE.PerformanceID) `
> `AS NumberOfShowings `
> `FROM PERFORMANCE, SHOW `
> `WHERE PERFORMANCE.ShowID = SHOW.ShowID `
> `GROUP BY SHOW.Title; `
> 
> Example 2: 
> `SELECT SHOW.Title, Count(PERFORMANCE.PerformanceID) `
> `AS NumberOfShowings `
> `FROM PERFORMANCE INNER JOIN SHOW `
> `ON PERFORMANCE.ShowID = SHOW.ShowID `
> `GROUP BY SHOW.Title;`

### Q13
> **[mark-scheme]**
> **1 mark **each:
> 
> - Creating table EXAM with opening and closing brackets
> - All fields with appropriate data types and commas at end of lines
> - ExamID as primary key
> 
> Example:
> 
> `CREATE TABLE EXAM( `
> `ExamID varchar NOT NULL, `
> `Subject varchar, `
> `Level int, `
> `TotalMarks int, `
> `PRIMARY KEY(ExamID) `
> `);`
> **[mark-scheme]**
> **1 mark **each:
> 
> - Altering table EXAM_QUESTION
> - Linking ExamID to ExamID in EXAM
> 
> Example:
> `ALTER TABLE EXAM_QUESTION `
> `ADD FOREIGN KEY (ExamID) REFERENCES EXAM(ExamID);`

### Q14
> **[mark-scheme]**
> (i)
> 
> **1 mark** for each correct clause:
> 
> - Alter table EVENT
> - Adding foreign key as PlayerID referencing correct table
> 
> `ALTER TABLE EVENT `
> `ADD FOREIGN KEY(PlayerID)REFERENCES PLAYER(PlayerID);`
> 
> (ii)
> 
> **1 mark **each:
> 
> - Selecting PlayerID from EVENT
> - Counting EventID
> - Grouping by the PlayerID
> 
> Example: 
> `SELECT PlayerID, COUNT(EventID) `
> `FROM EVENT `
> `GROUP BY PlayerID;`

### Q15
> **[mark-scheme]**
> 1 mark each:
> 
> - `SELECT SUM(Quantity)`
> - `FROM SALE WHERE` and one correct condition
> - `AND` with remainder correct conditions
> 
> e.g. 
> `SELECT SUM(Quantity) `
> `FROM SALE `
> `WHERE CustomerID = "0034E" `
> `AND Date >= #01/01/2023# AND Date <= #31/12/2023#;`
> **[mark-scheme]**
> **1 mark** for each bullet point
> 
> - Create table `BATCH` with opening and closing brackets, all statements within brackets
> - `BatchID, Type` and `Flavour` as varchar or equivalent
> - …with suitable constraint(s)
> - `Size` as decimal, `SellingPrice` as currency, `EndDate` as date (or equivalent)
> - Primary key identified as `BatchID`
> 
> e.g.
> 
> `CREATE TABLE BATCH( `
> `     BatchID VARCHAR(6) NOT NULL,         `
> `     Type VARCHAR (20) NOT NULL, `
> `     Flavour VARCHAR (20) NOT NULL, `
> `     Size FLOAT, `
> `     SellingPrice CURRENCY, `
> `     EndDate DATE, `
> `     PRIMARY KEY(BatchID) );`

### Q16
> **[mark-scheme]**
> **1 mark **each
> 
> - Select SUM of Amount
> - From the correct table **and** one correct condition
> - Remaining correct condition
> 
> Example:
> 
> `SELECT SUM(Amount) `
> `FROM INVOICE `
> `WHERE Paid = "Y" `
> `AND DateSent >= #01/01/2023# AND DateSent <=`
> `#31/12/2023#`

### Q17
> **[mark-scheme]**
> **1 mark** for each bullet point
> 
> - Create table REPAIR_PART with opening and closing brackets, all statements inside the brackets
> - PartID and RepairNumber as varchar (or equivalent)
> - Quantity as integer
> - At least 1 appropriate constraint
> - Dual primary key
> 
> For example:
> 
> CREATE TABLE REPAIR_PART( 
>       PartID VARCHAR(20) NOT NULL, 
>       RepairNumber VARCHAR(4) NOT NULL, 
>       Quantity INT NOT NULL, 
>        PRIMARY KEY (PartID, RepairNumber) );
> 
> (iii)
> 
> **1 mark** for each bullet point
> 
> - Select SUM of AmountDue
> - From the correct table **and** one correct condition
> - Second correct condition
> 
> SELECT SUM(AmountDue) 
> FROM INVOICE 
> WHERE SupplierID = "JK675" AND Paid = FALSE;
