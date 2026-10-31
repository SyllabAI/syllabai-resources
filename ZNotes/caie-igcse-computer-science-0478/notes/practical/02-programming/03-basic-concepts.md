## Basic Concepts

When writing the steps required to solve a problem, the following concepts need to be used and understood:

* Sequence
* Selection
* Iteration
* Counting and totalling
* String handling
* Use of operators.

### **Sequence**

The ordering of the steps in an algorithm is very important. An incorrect order can lead to incorrect results and/or extra steps that are not required by the task.

### **Selection**

Selection is a very useful technique, allowing different routes through the steps of a program. The code of this is explained in the notes of previous chapters.

### **Iteration**

As explained in the previous chapter, we already

### **Totalling and Counting**

As explained in the previous chapter, we already

### **String Handling**

* Strings are used to store text and can contain various characters.
* An empty string has no characters, while the programming language specifies the maximum number of characters allowed.
* Characters in a string can be identified by their position number, starting from either zero or one, depending on the programming language.
* String handling is an important aspect of programming.
* In IGCSE Computer Science, you will need to write algorithms and programs for the following string methods:
  * Length: Determines the number of characters in a string, including spaces.
  * Substring: Extracts a portion of a string.
  * Upper: Converts all letters in a string to uppercase.
  * Lower: Converts all letters in a string to lowercase.
* These string manipulation methods are commonly provided in programming languages through library routines.

**Finding the length of a string:**

```javascript
LENGTH("Text Here")

LENGTH(Variable)
```

**Extracting a substring from a string:**

```javascript
SUBSTRING("Computer Science", 10, 7)
// returns the next 7 values starting from the 10th value of the string "Computer Science" i.e. "Science"
SUBSTRING(Variable, Position, Length)
```

**Converting a string to upper case**

```javascript
UCASE("Text here")

UCASE(Variable)
```

**Converting a string to lowercase**

```javascript
LCASE("Text Here")

LCASE(Variable)
```

### **Arithmetic, Logical and Boolean Operators**

As explained in the previous chapter, we already

### **Use of Nested Statements**

* Selection and iteration statements can be nested, meaning one statement can be placed inside another.
* Nested statements help reduce code duplication and simplify testing of programs.
* Different types of constructs can be nested within each other, such as selection statements within condition-controlled loops or loops within other loops.

### **Procedures and Functions**

Procedures and functions are defined at the start of the code.

* Procedure- A subroutine that does not return a value to the program that called it.

* Function- A subroutine that returns a single value to the program

* Parameter -A value that is passed into a subroutine when it is called.

**Procedures without parameters:**

```javascript
PROCEDURE ProcedureName ()
 [Commands]
ENDPROCEDURE
//Calling/running the procedure
CALL ProcedureName()
```

**The procedure with parameters:**

```javascript
PROCEDURE ProcedureName (ParameterName : ParameterDatatype)
 [Commands]
ENDPROCEDURE
//Calling/running the procedure
CALL ProcedureName (ParameterValue)
```

**Function:**

```
FUNCTION FunctionName (ParameterName : ParameterDatatype) RETURNS DataTypeOfValueReturned
 [Commands]
 RETURN ValueToBeReturned
ENDFUNCTION
```

* When defining procedures and functions, the **header** is the first statement in the definition.
* The header includes:
  * The name of the procedure or function.
  * Parameters passed to the procedure or function, along with their data types.
  * The data type of the return value for a function.
* Procedure calls are standalone statements.
* Function calls are made as part of an expression, typically on the right-hand side.

### **Local and Global Variable**

* Any part of a program can use a global variable – its scope covers the whole program

* A local variable can only be used by the part of the program it is declared in – its scope is restricted to that part of the program.

**Note: Any variables/arrays made in this procedure and functions will be local and cannot be used out of these. To be made available all over the program, they must be declared globally in the following way.**

```javascript
DECLARE [VariableName] : DataType AS GLOBAL
```