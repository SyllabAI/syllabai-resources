## Translation Software

### Interpreter

* An interpreter reads line by line and checks statements for errors, if no errors are found it is executed otherwise a report is made and the interpreter stops execution. It is easier for debugging.

* A compiler does not run the code line by line but rather at the end of translation.

### Lexical Analysis

- Characters are converted from strings into tokens.
- Comments are removed.
- Symbol table stores identifiers and keywords.
- White spaces are removed
- Keyword table stores the reserved words used and the matching operators.

**Tokens:** Strings with an assigned meaning

### Syntax Analysis

A parse tree is generated for Backus-Naur Form and syntax errors are reported.

### Code generation

Object code is generated.

### Code Optimization

Code is optimized to improve time for execution.