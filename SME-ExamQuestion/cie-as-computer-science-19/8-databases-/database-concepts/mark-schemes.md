# Mark Schemes — Database Concepts
**8. Databases** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (9 questions)


### Q1
> **[mark-scheme]**
> **1 mark** for both 1:M relationships as follows:
> 
> ![Diagram showing "COURSE_SCHEDULE" linked to "TUTOR" and "COURSE_INFORMATION" with arrows indicating relationships between the boxes.](assets/002-diagram-showing-course-schedule-linked-to-tutor-.png)

### Q2
> **[mark-scheme]**
> **1 mark** for each term (**max 3**)
> 
> Entity:
> 
> - An object about which data can be stored
> 
> Primary key:
> 
> - The **unique** attribute / combination of attributes used to identify the **record / tuple **
> 
> Referential integrity:
> 
> - Makes sure that if data is changed in one place the change is reflected in all related records - cascading update/delete
> - Makes sure that data that does not exist cannot be referenced
> - Ensures that every foreign key has a **corresponding** primary key // A logical dependency of a foreign key on a primary key
> - Ensures that the data in the database is consistent / up to date
> - Prevents records from being added/deleted/modified incorrectly
> - Makes sure any queries return accurate and complete results
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 4**)
> 
> - Identify repeating groups of attributes ...
> - ... Subject and SubjectCode
> - Ensure each field is atomic
> - ... StudentName should be split into e.g. FirstName and LastName
> - Identify the primary key for the table

### Q3
> **[mark-scheme]**
> **1 mark** for each correct relationship or relationships
> 
> - 1:M between CUSTOMER and SHOP_ORDER
> - 1:M between SUPPLIER and ITEM
> - 1:M between SHOP_ORDER and ORDER_ITEM **and** M:1 between ORDER_ITEM and ITEM
> 
> ![Diagram showing relationships: SHOP_ORDER to CUSTOMER, ORDER_ITEM to SHOP_ORDER and ITEM, ITEM to SUPPLIER, forming an interconnected system.](assets/004-diagram-showing-relationships-shop-order-to-cust.png)
> **[mark-scheme]**
> **1 mark** for each bullet point **(max 3) **
> 
> - Reduced data **redundancy **
> - Improved data integrity / consistency / referential integrity
> - Allows for views / improved privacy
> - Allows for program-data independence
> - Complex queries can be executed

### Q4
> **[mark-scheme]**
> **1 mark** for:
> 
> many to 1 // there are many performances of each show
> **[mark-scheme]**
> **1 mark** each to **max 5**:
> 
> e.g.
> 
> - CUSTOMER table identified with suitable Primary Key and appropriate name
> - … and other suitable fields including name and email
> - BOOKING TABLE identified with suitable Primary Key and appropriate name
> - … that stores the Primary Key of the CUSTOMER table as a Foreign Key to join with CUSTOMER table
> - … and stores the Primary Key of the PERFORMANCE table as a Foreign Key to join with PERFORMANCE table
> - A linking table between Table 2 and SEAT with suitable Primary Key and appropriate name
> - … that includes the Primary Key of Table 2 as a Foreign Key to join with Table 2
> - … that stores the SeatID.

### Q5
> **[mark-scheme]**
> **1 mark** for:
> 
> 1-to-many
> **[mark-scheme]**
> **1 mark **each to **max 5**:
> 
> - STUDENT table identified with suitable Primary Key
> - A linking table between STUDENT and EXAM with suitable Primary Key and appropriate name
> - … that includes the Primary Key of the STUDENT table as a Foreign Key to join with STUDENT
> - ... and includes the Primary Key of the EXAM table as a Foreign Key to join with EXAM
> - A linking table between STUDENT and EXAM_QUESTION with suitable Primary Key and appropriate name
> - … that includes the Primary Key of Table 2 as a Foreign Key to join with Table 2
> - … that stores the ExamQuestionID and the mark for that question

### Q6
> **[mark-scheme]**
> **1 mark** each:
> 
> - User table with the username as the Primary Key
> - … containing at least email address, date of birth / age and rating
> - Quiz table with Quiz ID or date or file name as the Primary Key.
> - … containing at least the other field(s) not used as the PK
> - A joining table with an appropriate name including at least fields for user identification, quiz identification and score
> - … with an appropriate Primary Key
> - ... and Foreign Keys matching the Primary Keys of the other two tables
> 
> `USER(Username, Email, DateOfBirth, Rating) `
> `QUIZ(QuizID, Date, Filename)  `
> `USER_QUIZ(Username, QuizID, Score)`

### Q7
> **[mark-scheme]**
> **1 mark **each:
> 
> - Foreign key: `BatchID`, table `BATCH `
> - Foreign key: `CustomerID`, table `CUSTOMER`
> **[mark-scheme]**
> **1 mark **for each bullet point each (max 4)
> 
> e.g.
> 
> - Ice cream table with an appropriate name
> - … containing type, flavour, size, selling price
> - … with suitable primary key
> - … foreign key identified in BATCH that links to the primary key in `ICECREAM `
> 
> Example table definitions – not example answer:
> 
> `BATCH(BatchID, IceCreamID, EndDate) `
> `ICE_CREAM(IceCreamID, Type, Flavour, Size, SellingPrice)`
> **[mark-scheme]**
> **1 mark** for each definition
> 
> Entity:
> 
> - A real-life object that is represented as a table
> 
> Attribute:
> 
> - An item of data about an entity

### Q8
> **[mark-scheme]**
> **1 mark** each to **max 3 **
> 
> e.g.
> 
> - There is reduced data redundancy // less repeated data
> - … because each item of data is only stored once
> - Data consistency is maintained // Data integrity is improved
> - … changes in one table will automatically update in another
> - ... linked data cannot be entered differently in two tables
> - Program-data independence is ensured
> - … changes to the data do not require programs to be re-written // queries are not dependent on the structure of the data
> - Complex queries are easier to run
> - Different views can be provided
> - …. so users can only see specific aspects of the database
> - Multiple concurrent access is possible
> - ... through record locking
> **[mark-scheme]**
> **1 mark** each to **max 6**
> 
> - `CUSTOMER `to `JOB `is 1 to many
> - … implemented by Primary Key in `CUSTOMER` is Foreign Key in `JOB  `
> - `EMPLOYEE` to `LOGIN_DATA` is 1 to 1
> - … implemented by Primary Key in `EMPLOYEE `is Foreign Key in `LOGIN_DATA `
> - `JOB` to `JOB_EMPLOYEE` is 1 to many
> - … implemented by Primary Key in `JOB `is Foreign Key in `JOB_EMPLOYEE `
> - `EMPLOYEE` to `JOB_EMPLOYEE` is 1 to many
> - … implemented by Primary Key in `EMPLOYEE` is Foreign Key in `JOB_EMPLOYEE`

### Q9
> **[mark-scheme]**
> 1 mark for limitation and 2 marks for corresponding explanation
> 
> e.g.
> 
> Data redundancy // data duplication
> 
> - Separate linked tables are used
> - Data items are stored once so reduces data duplication / data redundancy
> 
> Data inconsistency / Poor data integrity
> 
> - Data changed once in one place will automatically update elsewhere
> - Linked data cannot be entered differently in two tables
> - Referential integrity can be enforced
> 
> The data structure used depends on the application
> 
> - Changes to the data structure are managed by the DBMS
> - … and queries are not dependent on the structure of the data
> - … and changes to the data do not require programs to be re-written
> **[mark-scheme]**
> **1 mark** for each correct relation
> 
> ![Diagram showing entities: REPAIR_PART, PART, REPAIR, and CUSTOMER, interconnected with lines indicating relationships between them.](assets/006-diagram-showing-entities-repair-part-part-repair.png)
> **[mark-scheme]**
> **1 mark** for each correct definition
> 
> | **Database** **Term** | **Definition** |
> |---|---|
> | Referential integrity | All duplicate entries of data between tables are consistent // all foreign keys are matched to an appropriate primary key |
> | Candidate key | A field that could be a primary key but is not // an attribute or smallest set of attributes in a table where no tuple has the same value |
> | Tuple | A row / record in a table // one instance of an entity in a table |
