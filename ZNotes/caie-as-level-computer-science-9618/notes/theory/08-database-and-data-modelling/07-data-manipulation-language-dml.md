## Data Manipulation Language (DML)

* Query and maintenance of data done using this language – written in
  SQL

### Queries

* **Creating a query:**

  ```sql
  SELECT <field-name>
  FROM <table-name>
  WHERE <search-condition>
  ```

* **SQL Operators:**


|=|Equals to|
|:---|:---|
|>|Greater than|
|<|Less than|
|>=|Greater than or equal to|
|<=|Less than or equal to|
|<>|Not equal to|
|IS NULL|Check for null values|

* **Sort into ascending order:**

```sql
ORDER BY <field-name>
```

* **Arrange identical data into groups:**

```sql
GROUP BY <field-name>
```

* **Joining together fields of different tables:**

```sql
INNER JOIN
```

### Data Maintenance

* **Adding data to table:**

```sql
INSERT INTO <table-name>(field1, field2, field3)
VALUES (value1, value2, value3)
```

* **Deleting a record:**

```sql
DELETE FROM <table-name>
WHERE <condition>
```

* **Updating a field in a table:**

```sql
UPDATE <table-name>
SET <field-name> = <value>
WHERE <condition>
```