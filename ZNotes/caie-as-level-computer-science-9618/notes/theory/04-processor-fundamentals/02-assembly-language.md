## Assembly Language

* Assembly language: low-level programming language with instructions made up of an op code and an operand
* Machine code: code written in binary that uses the processor’s basic machine operations
* Relationship between machine and assembly language: every assembly language instruction (source code) translates into exactly one machine code instruction (object code)
* Symbolic addressing
  * Symbols used to represent operation codes
  * Labels can be used for addresses
* Absolute addressing: a fixed address in memory
* Assembler
  * Software that changes assembly language into machine code for the processor to understand
  * The assembler replaces all mnemonics and labels with their respective binary values (that are predefined before by the assembler software)
* One pass assembler
  * Assembler converts mnemonic source code into machine code in one sweep of program
  * Cannot handle code that involves forward referencing
* Two pass assembler: software makes 2 passes through the code
  * On the first pass:
    * Symbol table created to enter symbolic addresses and labels into specific addresses
    * All errors are suppressed
  * On the second pass:
    * Jump instructions access memory addresses via table
    * Whole source code translates into machine code
  * Error reported if they exist
* Grouping the Processor’s Instruction Set


|Op Code|Operand|Explanation|
|:---|:---|:---|
|Addressing|||
|LDM|#n|Immediate: Load n into ACC|
|LDD|<address>|Direct: load contents at address into the ACC|
|LDI|<address>|Indirect: load contents of address at given address into ACC|
|LDX|<address>|Indexed: load contents of given address + IR into ACC|
|Data Movement|||
|STO|<address>|Store contents of ACC into address|
|Arithmetic Operations|||
|ADD|<address>|Add contents of register to ACC|
|INC|<register>|Add 1 to contents of the register|
|Comparing|||
|CMP|<address>|Compare contents of ACC with that of given address|
|CMP|#n|Compare contents of ACC with n|
|Conditional Jumps|||
|JPE|<address>|Jump to address if compare TRUE|
|JPN|<address>|Jump to address if compare FALSE|
|Unconditional Jumps|||
|JMP|<address>|Jump to given address|
|I/O Data|||
|IN||Input any character and store ASCII value in ACC|
|OUT||Output character whose ASCII value is stored in ACC|
|Ending|||
|END||Return Control to operating system|

\#denotes immediate addressing

B denotes a binary number, e.g. B01001010
& denotes a hexadecimal number, e.g. &4A

* Modes of Addressing
  * Direct Addressing: loads contents at address into ACC
  * Indirect Addressing: The address to be used is at given address. Load contents of this second address to ACC
  * Indexed addressing: form the address to be used as <address> + the contents of the IR (Index Register)
  * Relative addressing: next instruction to be carried out is an offset number of locations away, relative to address of current instruction held in PC; allows for relocatable code
  * Conditional jump: has a condition that will be checked (like using an IF statements)
  * Unconditional jump: no condition to be followed, simply jump to the next instruction as specified