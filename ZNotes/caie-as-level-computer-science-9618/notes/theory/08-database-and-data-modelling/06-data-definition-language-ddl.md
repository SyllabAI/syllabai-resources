## Data Definition Language (DDL)

* Creation/modification of the database structure using this language
  * written in SQL
* **Creating a database:**

```sql
CREATE DATABASE <database-name>
```

* **Creating a table:**

```sql
CREATE TABLE <table-name> (…)
```

* **Changing a table:**

```sql
ALTER TABLE <table-name>
```

* **Adding a primary key:**

```sql
PRIMARY KEY (field)
ADD <field-name>:<data-type>
```

* **Adding a foreign key:**

```sql
FOREIGN KEY (field) REFERENCES <table>(field)
```

* **Example:**

```sql
CREATE DATABASE ‘Personnel.gdb’
CREATE TABLE Training
(EmpID INT NOT NULL,
CourseTitle VARCHAR(30) NOT NULL,
CourseDate Date NOT NULL,
PRIMARY KEY (EmpID, CourseDate),
FOREIGN KEY (EmpID) REFERENCES Employee(EmpID))
```



