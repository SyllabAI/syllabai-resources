# Further Programming

## Programming Paradigms

A programming paradigm is a fundamental style of programming.

### Low Level

Low level programming means manipulating memory directly.

```nasm
Data Movement 
LDM <#n/Bn/&n> ; Loaded to ACC
LDD <address> ; Contents of address loaded to ACC
LDI <address> ; Contents of address of address loaded to ACC
LDX <address> ; Content of IX added to address to form a  new address and data from there is loaded to ACC
LDR <#n/Bn/&n> ; Loaded to IX
MOV <register> ; Move contents of ACC to <register>
STO <address> ; Store contents of ACC at <address> 
IN <> ; Store the ASCII value of the char in the ACC
OUT <> ; Output the character based on the ASCII value in  the ACC
 
Arithmetic Operations 
ADD <#n/Bn/&n> ; Add to ACC
SUB <#n/Bn/&n> ; Subtracts from ACC
INC <register> ; Increment register
DEC <register> ; Decrement register
 
Conditional and Unconditional Jumps 
JMP <address> ; Jump to given address
JPE <address> ; Jump if true after comparison
JPN <address> ; Jump if false after comparison
 
Comparison 
CMP <#n/Bn/&n> ; Checks if ACC is equal to value
CMI <address> ; Check if contents of address of the address is equal to ACC
```

- #‎‎‎‎ Represents a decimal number

- B Represents a binary number

- & Represents a hexadecimal number

**Addressing Modes**

- **Immediate:** The operand is the value used in the instruction.

- **Direct:** The value of the address is used in the instruction.

- **Indirect:** The operand stores an address that points to another address that stores the data.

- **Indexed:** The operand is added to the index and the data at the address is used.

- **Relative:** The operand is added to a set address to calculate where to read value from, offsets. It is used to allow for relocatable code as all addresses are base + offset.

### **Imperative**

Imperative programming involves writing a program as a sequence of steps that is executed by the processor, like pseudocode.

### Object Oriented

Object oriented programming is based on objects interacting with each other.

**Object:** An object is an instance of a class.

**Properties/Attributes/Fields:** The data items of the class. By setting properties to private it ensures they can only be accessed by the class and enforces encapsulation.

**Method:** The functions/procedures that are a part of a specific class.

**Class:** A data type that combines data structures and methods, which operate on that data structure, and serves as a template that is used to make objects.

**Inheritance:** The concept that all attributes and methods of the base class are passed on to the subclass.

**Polymorphism:** The concept that a method may behave differently for different classes in the hierarchy.

**Aggregation/Containment:** When one class contains another class within it.

**Encapsulation:** Encapsulation involves bundling variables (data) and methods within a class to restrict direct access to the variables.

**Getter:** A method to access the associated attribute.

**Setter:** A method to set the value of the associated attribute.

### Declarative

Declarative programming is fact oriented and there is no need to consider sequence of execution.

#### Fact

A clause without a body

```prolog
capitalCity(paris). /* Means Paris is a captial city */
capitalCity(paris). /* Running it a second time returns true because the database knowns Paris is a capital city */
```

#### Using Variables

```prolog
cityInCountry(paris, france). /*Means Paris is a city in France*/
cityInCountry(City, france). /*Retuns Paris*/
```

If a fact has more arguments but we only need one of them, you can replace the ones you don’t need with $\_$ (an anonymous variable).

#### Rules

```prolog
parent(fred, jack).
parent(fred, alia).
parent(fred, paul).
parent(dave, fred).
sibling(A,B) :- parent(P,B), parent(P,A), not(A=B). /*This is a rule that says if two kids are siblings if they share a parent*/
sibling(jack,X) /*Returns alia and paul*/
```