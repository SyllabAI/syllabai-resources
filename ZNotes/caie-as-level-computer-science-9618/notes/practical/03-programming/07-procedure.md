## Procedure

**Procedure:** subroutine that performs a specific task without returning a value

* **Procedure without parameters:**

| PROCEDURE <identifier><statement(s)>ENDPROCEDURE | def identifier():statement(s) |
|----|----|

* When a procedure has a parameter, the function can either pass it by either reference or value
* **Pass by value:** data copied into procedure so variable not changed outside procedure

`PROCEDURE <identifier> (BYVALUE <param>: <datatype>)`

`<statement(s)>`

`ENDPROCEDURE`

`def identifier(param):`

`statement(s)`

* **Pass by reference:** link to variable provided so variable changed after going through procedure *(not in Python)*

`PROCEDURE <identifier> (BYREF <param>: <datatype>)`

`<statement(s)>`

`ENDPROCEDURE`

* **Calling a procedure:**

| CALL <identifier>() | Identifier() |
|----|----|



