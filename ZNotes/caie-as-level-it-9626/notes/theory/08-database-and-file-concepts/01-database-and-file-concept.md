# Database and File Concepts

* **Database:** a structured method for storing data in sets of
  tables.
* **Table:** a set of similar data.
* **Record:** a common word for entity.
* **Entity:** a set of data about one thing.
* **Field:** common word for attribute.
* **Database management software:** software used to manage a database.
* **Relationship:** the way in which two entities in two different tables are connected.
* **Primary Key:** a field that contains a unique identifier for a
  record.
* **Foreign key:** a field in a table that refers to the primary key
  in another table.
* **Normal form:** the extent to which a database has been normalised.
* **Index:** a list of keys or keywords that identify a unique record
* and can be used to search quickly and sort records.
* **Flat file:** a database stored in a single file.
* **Compound key:** two or more fields that form the primary key.
* **Referential integrity:** data in the foreign key of the table on the many sides of a relationship must exist in the primary key of the table on the one side of the relationship.
* **Query:** a question used to retrieve data from a database.
* **Parameter:** data used within the criteria for query.
* Data types include:
  * **String (text)**
  * **Numeric**
  * **Boolean**
  * **Date/time**
* Generic file formats enable data to be transferred between software.
  * They do not include any formatting and only include essential
    data.
  * .txt and .csv are generic file formats
* Indexed sequential(serial) access: data is accessed based on the sequential order in which it is sorted.
* Direct file access: Data is stored in a random order based on a hashing algorithm that determines its storage location, and the same is used to locate it during access.
* Data dictionary: a document/file that describes the structure of the
  data held within the database, known as metadata.
* Management information system (MIS): collects data from a database and presents it as reports and charts. These reports and graphs can be produced within the database system itself or may be part of another piece of software used to analyse the data.
* An MIS’ essential features:
  * Data is collated from databases and other sources
  * Data is interconnected from different sources
  * Data is analysed to provide the data that is required
  * Summary reports and charts
* When additional software is used to collate data from more than one
  database, it is often referred to as an Executive information system
  (EIS).
* **Data integrity:** The level of accuracy and reliability of data.
* **Data redundancy:** Data that is unnecessary.
* **Normalisation:** Organising data in a database reduces data redundancy and increases data integrity.
* **Unnormalised data:** Data that is unnormalised may have repeated entries and fields that are not atomic.
* **1NF:** A database in 1NF will not have any repeating fields, and all the fields in the database will be atomic.
* **2NF:** A database in 2NF will have the characteristics of 1NF. In addition, related fields will be separated into different tables, dependent on the primary key of the table.
* **3NF:** A database in 3NF will have the characteristics of 2NF. In
  addition, any fields that are not directly related to each other are
  given further separation into tables that only contain fields that
  are directly related.



