## Language Translators

* Assembler
  * Software that translates assembly language statements into machine code (binary) for execution
  * The mnemonics used translates into machine opcodes
  * Process simple because assembly language has a one-to-one relationship with machine code.
* Compiler and Interpreter


|Compiler|Interpreter|
|:---|:---|
|Translates a high-level language program to machine code.|Translates and executes a high-level language program, line-by-line.|
|Creates a .exe file which can be easily distributed.|No .exe file created.|
|Once compiled, .exe file does not need to be compiled again, resulting in faster execution.|Execution very slow – translated each time program run.|
|Reports all errors at the end of compilation: difficult to locate errors∴ development process long.|Debugging easier/faster, since it stops translating when it reaches an error. This allows real time error correction.|
|Only be produced when all errors are fixed.|Can run program any time, even before code finished.|
|Used when development is completed.|Used during development.|

* One Pass Assembler

  * A one-pass assembler is a type of assembler that processes the source code in a single scan. During this scan, it defines symbols and literals, storing them in the symbol and literal tables, respectively. It keeps track of the location counter to assign memory addresses to variables and instructions, processes pseudo-operations as they appear, and simultaneously translates the source code into machine code, effectively generating the object code while resolving addresses and symbolic references on the go.

* Two Pass Assembler

  * A two-pass assembler is a program that reads the source code twice to generate object code. In the first pass, it scans the code to define symbols, assign memory addresses, and gather information about literals and variables. In the second pass, it converts symbolic op-codes into their corresponding numeric op-codes, resolves symbol values, generates data for literals, and produces the final object code by fully translating the source code.

* Two-step translation

  * Java and some other high level language programs may require two-step translation, i.e., they will be partially compiled and partially interpreted
  * Java code first translated to bytecode by Java compiler
  * Bytecode finally interpreted by the Java Virtual Machine to produce machine code

* Integrated Development Environment (IDE) features

  * Coding
    * Context-sensitive prompts: Displays choice of keywords and available identifiers appropriate at current insertion point and provides choices in alphabetical order
    * Highlights undeclared/unassigned variable identifiers
  * Initial Error Detection
    * Dynamic syntax checks: Automatic checking and highlighting of syntax errors, as soon as line typed
    * Type checking & parameter checking
  * Presentation
    * Prettyprint: Automatic indentation and color-coding of keywords
    * Expand and Collapse code blocks: Saves excessive scrolling if collapsed, and easy to see global variable declarations and main program body when collapsed
  * Debugging
    * Single stepping: Executes program line-by-line to see the effect of each statement on variables
    * Breakpoints: Pauses program at a specific line to ensure program operates correctly up to that line
    * Variables/expressions Report Window: Monitors variables for comparing values.