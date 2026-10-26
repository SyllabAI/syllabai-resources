# Mark Schemes — Data Definition Language (DDL) & Data Manipulation Language (DML)
**8. Databases** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (8 questions)


### Q1
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

### Q2
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

### Q3
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

### Q4
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

### Q5
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

### Q6
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

### Q7
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

### Q8
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
