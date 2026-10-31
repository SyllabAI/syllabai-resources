## Reverse Polish Notation (RPN)

**Reverse Polish notation (RPN):** An unambiguous method for representing an expression left to right without needing rules of precedence or brackets.

### Advantages

- No brackets or precedence of operators needed
- Simpler to evaluate
- No need for backtracking in evaluation as the operators appear in the order required for computation and can be evaluated from left to right

### Uses with a Stack

- RPN expression is read left to right
- As values are read numbers are pushed into the stack.
- If an operator is read the last two values in the stack are popped, the operation is performed on them, and the result is pushed back onto the stack.
- Repeated until the end of the expression is reached.

### Example

$(a – b) * (a + c) / 7 \phantom{FFF} \leftrightarrow \phantom{FFF}  ab-ac+*7/$

$a b / 4 * a b + - \phantom{FFF} \leftrightarrow \phantom{FFF} (a/b)*4-(a+b)$