## Relational Database Modelling

* **Entity:** object/event which can be distinctly identified
* **Table:** contains a group of related entities in rows and columns
  called an entity set
* **Tuple:** a row or a record in a relational database
* **Attribute:** a field or column in a relational database
* **Primary key:** attribute or combination of them that uniquely
  define each tuple in relation
* **Candidate key**: attribute that can potentially be a primary key
* **Foreign key:** attribute or combination of them that relates 2
  different tables
* **Referential integrity:** prevents users or applications from
  entering inconsistent data
* **Secondary key:** candidate keys not chosen as the primary key
* **Indexing:** creating a secondary key on an attribute to provide
  fast access when searching on that attribute; indexing data must be
  updated when table data changes

  ## Advantages of Relational Database Modelling
* **Data Independence:** The database structure (schema) is separate from the application programs. Changes to the database layout do not break software functionality.
* **Controlled Redundancy:** Data is stored in one central location and referenced elsewhere using links, preventing unnecessary duplication.
* **Data Integrity:** Centralized updates ensure data consistency. Enforced validation rules (e.g., validation checks, foreign keys) maintain accuracy.
* **Centralized Security:** The Database Management System (DBMS) controls access rights, allowing specific users access to only specific tables or columns.
* **Data Sharing:** Multiple applications and users can access the same centralized data concurrently.
* **Concurrency Control:** The DBMS uses locking mechanisms to prevent data corruption when multiple users update data simultaneously.