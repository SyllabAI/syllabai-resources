# Data Representation

## User-defined data types

- A data type constructed by the programmer using primitive data types.
- User-defined data types are used to create new data types that help to extend the flexibility of a programming language as the programmer can create data types based on the application’s requirements.
- Importance of user-defined data types:
  - Code organization- Helps structure and group related data logically, making programs easier to read and maintain.

  - Reusability- Once defined, the data type can be reused multiple times, reducing redundant code and improving efficiency.
- Examples include:
  - Record
  - Set
  - Class
  - Object

### **Composite User-Defined Data Types**

Composite user-defined data types have a definition referencing at least one other type.

- **Record:** A composite data type that is a collection of related items which may or may not have different data types

  ```vb
  TYPE TBook // Example
    DECLARE Name : STRING 
    DECLARE Isbn : INTEGER 
  ENDTYPE
  
  DECLARE Book1: TBook // Creating a variable
  Book1.Name = "To Kill a Mockingbird" // Accessing properties
  ```

- **Set:** A set stores a finite number of unique items in no particular order allowing the program to apply mathematical operations defined in set theory.

  ```vb
  TYPE <set-name> = SET OF <type> //Declaration
  DEFINE <var-name> (value1,value2,value3,...) : <set-name>
  
  TYPE Numbers = SET OF INTEGERS
  DEFINE EvenNumbers (2,4,6,8,10) : Numbers
  ```

- **Classes:** In object-oriented programming (OOP), a class is the base for creating objects. It has methods and properties.

  ```vb
  // Class definition
  CLASS Bird
      PRIVATE Name: STRING
      PUBLIC PROCEDURE NEW(pName: STRING)
          Name ← pName
      ENDPROCEDURE
  ENDCLASS
  
  // Implementing inheritance
  CLASS FlyingBird IMPLEMENTS Bird
      // Class info...
  ENDCLASS
  
  // Creating an object
  <name> ← NEW <class_name>(<parameter1>, <parameter2>, ...)
  MyPet ← NEW Bird("Kiwi")
  ```

### **Non-Composite Data Type**

Data types that can be defined without referencing another type.

String and Char are both non-composite built-in types

Examples include:

- Integers

- Booleans

- Strings

- **Enumerated Data Type:** A user defined non-composite data type that contains an ordered list of all possible values.

  ```vb
  TYPE <name> : (<value1>, <value2>, ...)
  TYPE Days: (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday)
  TYPE Numbers: (1..10) // Inclusive
  DECLARE Today: Days // Declaration
  Today ← Sunday
  Today ← Today + 1 // Value is now Monday
  ```

- **Pointer Data Type:** A user defined non-composite data type that is used to reference a memory location.

  ```vb
  TYPE <Name> = ^<Type>
  
  // Declaring a pointer type
  TYPE PIntPointer: ^INTEGER
  // Declaring a pointer variable
  DECLARE MyPointer: PIntPointer
  
  MyPointer^ ← 3 // Sets the value at the address to 
  MyPointer ← 3 // Pointer points to value at the address 3
  MyPointer ← @<variable_name> // Makes pointer point to value stored at the address of the variable
  ```