# Mark Schemes — Language Translators
**5. System Software** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (19 questions)


### Q1
Benefit: the company only has to produce and maintain one file, **[1]** because the partially compiled file is interpreted when it is run and so works on all three operating systems. **[1]**

Drawback: every customer's computer must have the interpreting software installed, **[1]** and part of the translation then happens every time the program is run, so the program takes longer to run than a fully compiled executable file. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Max 2 marks** for the benefit and **max 2 marks** for the drawback.
> 
> Benefit, **1 mark** for each point:
> 
> - Only one file has to be produced // only one file has to be maintained and updated
> - ... because the partially compiled file is interpreted when it is run, so it works on all three operating systems
> - A change to the program only has to be made and translated once, not three times
> - The machine code is generated at run time, so the code is optimised for the processor it is running on
> 
> Drawback, **1 mark** for each point:
> 
> - The customer's computer must have the interpreting software installed
> - ... so the program will not run on a computer that does not have it
> - Part of the translation happens every time the program is run
> - ... so the program takes longer to run than a fully compiled executable file
> 
> Do not credit two benefits or two drawbacks. The maximum for each side is 2 marks.
> 
> Do not accept "Method B is easier" without saying what is easier and why.

> **[exam-tip]**
> Read the tariff and the wording together. Four marks split as one benefit and one drawback means two marks are available on each side, so develop each point with a "because" rather than writing four separate one-line advantages. Two benefits and no drawback caps you at 2 marks however good they are.
> 
> The drawback students miss is that Method B still needs a translator on the customer's computer. Method A does not. That is the trade the company is really making.

### Q2
The compiled file is not the machine code of one particular processor, so it is not tied to a single type of computer. **[1]**

Each type of computer has its own interpreter, which translates the compiled file when the program is run. **[1]**

The machine code is therefore generated at run time for whichever processor the program is running on, so the company does not need to produce a separately compiled version for each type of computer. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each point, **max 3**:
> 
> - The compiled file is not the machine code of one particular processor
> - Each type of computer has its own interpreter for the compiled file
> - The compiled file is interpreted when the program is run
> - ... so the machine code is generated at run time for that processor
> - The company only has to produce and supply one file rather than one for each type of computer
> 
> Accept "platform" in place of "type of computer".
> 
> Do not accept "Java runs on any computer" on its own. The answer must say why.
> 
> Do not accept "the file is compiled for each computer". Nothing is recompiled by the customer.

> **[exam-tip]**
> "It works on any computer" is a statement, not an explanation, and it earns nothing. An "explain" question wants the mechanism, so give the two halves: the compiled file is not machine code for one processor, and an interpreter on each computer finishes the translation while the program runs.
> 
> Be careful with the word compile in your last sentence. The customer's computer interprets the file; it does not compile it again.

### Q3
The source code is first compiled into a form that is not the machine code of any one processor. **[1]**

That compiled code is then interpreted when the program is run, so the machine code is generated at run time. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - The source code is compiled first
> - ... into a form that is not the machine code of one particular processor
> - The compiled code is then interpreted when the program is run
> - ... so the machine code is generated at run time
> - Translation is therefore completed in two stages, one before the program is run and one while it runs
> 
> **[2 marks]**
> 
> Do not accept "the whole program is compiled into machine code and then run". If the program were fully compiled there would be nothing left to interpret.
> 
> Do not accept an answer that only gives a benefit, such as "it can be used on different platforms". The question asks what happens, not why it is useful.

> **[exam-tip]**
> The word students drop is "interpreted". Many answers say the program is compiled and then run, which describes ordinary compilation and earns one mark at most. Say clearly that the compiled code is interpreted while the program runs.
> 
> Two stages, two marks. Write one sentence about the compiling stage and one about the interpreting stage and you have the answer.

### Q4
A compiler should be used.

A compiler produces an executable file, **[1]** so each control unit can run the program even though it has no translator software installed. **[1]**

The program is translated once, before it is installed, so no translation takes place while the program is running. **[1]**

Only the executable file is installed on the control units, not the source code, **[1]** so customers cannot read or change the program code. **[1]**

**[5 marks]**

> **[mark-scheme]**
> No mark is given for the choice. **1 mark** for each justification point, **max 5**:
> 
> - A compiler produces an executable file
> - ... so the control unit can run the program without any translator installed
> - ... whereas an interpreter would have to be installed on all 200 control units
> - The program is translated once, before it is installed
> - ... so no translation takes place while the program is running
> - ... so the program does not need memory for a translator while it runs
> - Only the executable file is installed, not the source code
> - ... so the customer cannot read, change or copy the program code
> - The program is complete, so the real-time error correction an interpreter offers is no longer needed
> - The compiler produces a full error report, so all errors can be found before the program is installed on 200 units
> 
> Marks are only available for a justification of the compiler. A justification of the interpreter earns 0.
> 
> Do not accept "compiled code always runs faster" on its own. It must be linked to a reason, for example that the program is translated once before it is run so no translating happens while it runs.
> 
> Do not accept "it is easier to debug" as a justification here. The program is already finished.

> **[exam-tip]**
> The marks in a "justify" question are in the justification, not in the choice, so never stop at "a compiler". Work through the facts you were given, one at a time: no translator installed, small memory, and code that must stay hidden. Each of those gives you a separate justification point.
> 
> "Compiled code runs faster" is the answer examiners see most and credit least. Add the reason and it becomes a mark: the whole program is translated before it is run, so no time is spent translating while it is running.

### Q5
A compiler translates the whole program in one go, before any of it is run, and produces an executable file. **[1]**

An interpreter translates one statement at a time and executes each statement immediately after translating it. **[1]**

The executable file produced by the compiler can be run without the compiler being present, but the interpreter has to translate the program again every time it is run, so the interpreter must be present each time. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Max 3 marks**, with at least **1 mark** from each list.
> 
> Compiler:
> 
> - Translates the whole program in one go // translates all of the source code before any of it is run
> - Produces an executable file // produces object code that is saved
> - The program is translated once, and the executable file can then be run many times
> - The compiler is not needed when the program is run
> - Produces a full error report after translating
> 
> Interpreter:
> 
> - Translates one statement at a time
> - Executes each statement immediately after translating it
> - The program is translated again every time it is run
> - The interpreter must be present whenever the program is run
> - Stops at the first error and reports it
> 
> **[3 marks]**
> 
> Do not accept "a compiler is faster" without saying what is faster and why.
> 
> Do not accept "an interpreter translates line by line" on its own for both marks. The interpreter mark also needs the execution point, that each statement is executed as it is translated.

> **[exam-tip]**
> A "compare" question needs both sides. Answers that describe only the compiler cannot reach full marks, however detailed they are. Write a point about the compiler, then the matching point about the interpreter.
> 
> The point students most often leave out is that an interpreter executes each statement as well as translating it. A compiler only translates. That single difference explains why the compiler produces a file you can run later and the interpreter does not.

### Q6
The customer must have the interpreter installed, otherwise the program will not run. **[1]**

The program is translated every time it is run, so translation takes time on every run. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - The customer must have the interpreter installed in order to run the program
> - The program has to be translated every time it is run // it is not translated once and then reused
> - ... so the program takes longer to run than a compiled executable file
> - The source code has to be supplied to the customer
> - ... so the customer can read, change or copy the program code
> 
> **[2 marks]**
> 
> Do not accept "the interpreter reports only one error at a time" or "errors can be corrected in real time". Those describe an interpreter during development, and neither is a drawback of supplying a finished program.
> 
> Do not accept "an interpreter is slower" without saying why it is slower.

> **[exam-tip]**
> Students revise the list of interpreter advantages and then write the same points here with the word "not" added. That does not work. The advantages of an interpreter, stopping at the first error and letting you correct it immediately, belong to the programmer writing the code. This question is about the customer running a finished program.
> 
> If you write that the program is slower, add the reason: it is translated again every time it is run.

### Q7
| Program | Translator | Reason |
|---|---|---|
| Program 1 | **Assembler** **[1]** | **It is the only translator that converts an assembly language program into machine code.** **[1]** |
| Program 2 | **Interpreter** **[1]** | **It translates and executes one statement at a time and stops at the first error, so the programmer can correct the error and see the effect immediately.** **[1]** |
| Program 3 | **Compiler** **[1]** | **It produces an executable file, so the customer can run the program without having a translator installed.** **[1]** |

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for each correct translator and **1 mark** for a matching reason.
> 
> Accept for the Program 1 reason: the program is not written in a high-level language, so a compiler or an interpreter cannot be used // it translates the assembly language program into machine code that the robot arm controller can execute
> 
> Accept for the Program 2 reason: only one error is reported at a time, so there are no dependent errors to sort out // a partially written program can be translated and tested
> 
> Accept for the Program 3 reason: the source code is not supplied, so the customer cannot read or change it // the program is translated once rather than every time the customer runs it
> 
> A reason mark can only be awarded if the translator named in the same row is correct.
> 
> Do not accept "it is faster" on its own for any row.
> 
> Do not accept "an interpreter is slower" as the reason for Program 3, because a reason must say what the compiler gives the customer.

> **[exam-tip]**
> Each reason must fit the program described in that row, not translators in general. "A compiler is better" earns nothing. "It produces an executable file so the customer does not need a translator installed" earns the mark because it uses the detail in the question, that the program is sold to customers.
> 
> Program 1 catches students out because they are thinking about compilers and interpreters. Look at the language first. Assembly language means assembler, whatever the program is for.

### Q8
The processor in the washing machine can only execute instructions that are in machine code. **[1]**

Assembly language is a low-level language written in a text form, so the processor cannot execute it directly. **[1]**

The assembler translates the assembly language program into machine code, which is then loaded and run by the washing machine. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each point, **max 3**:
> 
> - The processor can only execute machine code
> - Assembly language cannot be executed by the processor directly
> - The assembler translates the assembly language program into machine code
> - ... so the translated program can be loaded and run by the washing machine
> 
> Accept "object code" in place of "machine code".
> 
> Accept "each assembly language instruction is translated into one machine code instruction" for the third point.
> 
> Do not accept "so the computer can understand it" on its own. The answer must name machine code.
> 
> Do not accept a description of the first pass and second pass of the assembler. That is not what this question asks for.

> **[exam-tip]**
> Two answers lose marks here every year. The first is "so the computer can understand it", which is too vague to credit. Name machine code and say that this is the only form the processor can execute.
> 
> The second is a description of the two passes of a two-pass assembler. That is a different question. This one asks why the assembler is needed at all, so keep your answer on what the processor can and cannot run.

### Q9
(i) Assembler **[1]**

(ii) Compiler **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for assembler
> 
> **1 mark** for compiler
> 
> Accept "assembler software" for (i)
> 
> Do not accept compiler or interpreter for (i). Only an assembler translates a program written in assembly language
> 
> Do not accept interpreter for (ii). An interpreter does not produce an executable file, and it must be present every time the program is run

> **[exam-tip]**
> The most common error here is writing "compiler" for the assembly language program. A compiler and an interpreter both take a high-level language as their input. Assembly language is a low-level language, and the assembler is the only translator that handles it.
> 
> Read part (ii) for the words "executable file". Those two words rule the interpreter out on their own.

### Q10
| Problem | IDE feature |
|---|---|
| The programmer types a keyword incorrectly and wants the mistake to be shown on the screen straight away, before the program is run. | **Dynamic syntax check** **[1]** |
| The programmer cannot remember the exact name of a built-in function and wants the IDE to offer the possible names while the name is being typed. | **Context-sensitive prompt** **[1]** |
| The program is now several thousand lines long and the programmer wants to hide the sections of code that they are not working on. | **Expand and collapse code blocks** **[1]** |
| A variable holds the wrong value, and the programmer wants the program to stop running at a chosen line so that the value can be checked at that point. | **Breakpoint** **[1]** |
| The programmer wants the current values of several variables to be displayed on the screen while the program runs. | **Report window** **[1]** |

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for row 1: dynamic syntax check. Accept "syntax check as the code is typed" or "dynamic syntax checking". Accept "prettyprint", because Cambridge credits pretty-printing as colour-coding keywords "so the user can identify any errors"
> 
> **1 mark** for row 2: context-sensitive prompt. Accept "auto-complete" or "auto-completion"
> 
> **1 mark** for row 3: expand and collapse code blocks. Accept "collapse code blocks" or "expand/collapse blocks". Do not accept "comments", because commenting out a block removes it from the program instead of hiding it on the screen
> 
> **1 mark** for row 4: breakpoint. Do not accept "single stepping", because single stepping runs the program one statement at a time from the start rather than stopping it at a line the programmer chooses
> 
> **1 mark** for row 5: report window. Accept "watch window", "variable watch window" or "variable window". Do not accept "breakpoint", because a breakpoint halts the program and it is the report window that displays the values

> **[exam-tip]**
> Rows 4 and 5 are where marks are lost, because the three debugging features get mixed up. A breakpoint decides where the program stops, single stepping decides how fast it moves, and the report window is the only one of the three that actually displays the contents of the variables. Learn them as three different jobs, not as three names for debugging.
> 
> The syllabus groups IDE features under four purposes: coding, initial error detection, presentation and debugging. When a question describes a problem, decide which of those four purposes it belongs to first. That narrows five possible answers down to one or two.

### Q11
Keywords are displayed in a different colour from the rest of the code. **[1]**

Strings, comments and identifiers are each given their own colour, so the separate parts of a statement can be told apart. **[1]**

A keyword that has been typed incorrectly is not coloured, so the programmer notices the mistake as it is made. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - Keywords are displayed in a different colour / font / style from the rest of the code
> - Strings, comments, identifiers and other parts of the code are shown in different colours so they can be told apart
> - A keyword typed incorrectly is not coloured or highlighted, so the mistake is noticed as it is made
> - The code is easier to read, so the programmer can find their way around a long program more quickly
> 
> **[3 marks]**
> 
> Accept "syntax highlighting" as an alternative name, but write prettyprint, which is the term used in the syllabus
> 
> Do not accept "it corrects the spelling of a keyword", because prettyprint changes how the code is displayed and never changes the code itself
> 
> Do not accept "it checks the code against the rules of the language", which is a dynamic syntax check and not prettyprint

> **[exam-tip]**
> "It makes the code look nice" earns nothing. Say what prettyprint does to the code on the screen, which is colour, and then say what the programmer gains from it.
> 
> Keep prettyprint apart from a dynamic syntax check. Prettyprint is a presentation feature, so it changes how correct code is displayed. It does not test a statement against the rules of the language.

### Q12
Each statement is checked against the rules of the programming language as the code is being typed. **[1]**

Any statement that does not follow the rules is underlined or highlighted, so the programmer sees the error before the program is run. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the check happening while the code is entered, e.g. each statement is checked against the rules (syntax) of the language as it is typed
> 
> **1 mark** for how the error is shown, e.g. the statement that breaks the rules is underlined / highlighted / coloured, so the error is seen before the program is run
> 
> Accept "the grammar of the language" or "the rules of the language" in place of syntax
> 
> Accept "flags", "marks" or "displays an error message beside the line" in place of underlines or highlights
> 
> Do not accept "it produces a list of all the errors at the end of translation", which describes a compiler's error report and not a dynamic check
> 
> Do not accept "it finds logic errors", because a syntax check only tests the rules of the language
> 
> Do not accept "it corrects the error", because the IDE shows the error and the programmer repairs it

> **[exam-tip]**
> The mark that goes missing here is the one hidden in the word "dynamic". The examiner wants to see that the checking happens as you type, not when you press run. Put "as the code is being entered" somewhere in your answer and that mark is safe.
> 
> Keep syntax errors and logic errors apart. A dynamic syntax check cannot tell you that you have written a plus sign where you needed a minus sign, because that statement still obeys the rules of the language.

### Q13
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2** for each feature).
> 
> Context-sensitive prompts:
> 
> - As the code is being written
> - …the options to complete the statement are shown
> 
> Single stepping:
> 
> - allows the programmer to execute the program one line at a time
> - …so that the effects of each statement can be seen

### Q14
> **[mark-scheme]**
> **1 mark **for each bullet point (**max 4**)
> 
> - easier to debug the program
> - … because it translates line-by-line and stops when an error is found whereas the compiler translates all the program at the same time
> - … only reporting one error at a time
> - … which allows the error to be corrected in real time whereas the program would need to be corrected and recompiled
> - ... and the program can restart at same point when error occurred with a compiler the program needs to be re-run
> - The effect of any changes made by the programmer can be seen immediately with a compiler the effects can only be seen after re-running
> - A partially completed program can be translated / tested on its own a compiler cannot translate a partial program
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - Partially compiled programs can be used on different platforms as they are interpreted when run
> - Code is optimised for the CPU as machine code is generated at run time
> - Source code does not need recompiling so more efficient to run
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - Prettyprint
> - Expand/collapse code blocks
> - Auto indentation / formatting
> 
> **1 mark** for each bullet point (**max 2**)
> 
> - Single stepping
> - Breakpoints
> - Report window
> - Variable expressions

### Q15
> **[mark-scheme]**
> For example:
> 
> - Set a breakpoint at the start of / within Lookup, to stop execution at a given statement
> - then use single stepping to execute one statement / instruction at a time
> - to display the value of variables using a watch window
> 
> One mark for each:
> 
> **MP1 **Order starting with a breakpoint **and **an explanation – ‘stop execution <u>at this statement / line’</u>
> 
> **MP2 **Explanation of single stepping – execute ‘line by line’ / statements
> 
> **MP3 **Explanation of watch window – displaying the value of <u>variable(s)</u>
> **[mark-scheme]**
> Features include:
> 
> **MP1 **Editor
> 
> **MP2 **<u>Auto</u>- (syntax) complete / <u>auto </u>correction // identify undeclared variables(s)
> 
> **MP3 **Prettyprint / <u>auto</u>-indentation / <u>auto</u> (structure) highlighter
> 
> **MP4 **<u>Dynamic</u> syntax checking
> 
> **MP5 **Expand / collapse code blocks
> 
> **MP6 **Context sensitive prompts
> 
> **Max 2 marks**

### Q16
> **[mark-scheme]**
> **1 mark** each to **max 2**:
> 
> - Creates an executable file
> - … so the code can be tested multiple times without having to recompile
> - … so** repeated testing** takes less time
> **[mark-scheme]**
> **1 mark** for identification of each feature and **1 mark** for matching description:
> 
> e.g.
> 
> *For coding:*
> 
> | IDE feature | Description |
> |---|---|
> | Context-sensitive prompts | **Gives suggestions** for code as the user types instead of having to write/remember the code |
> | **Auto**-correct | Corrects spelling mistakes so that user has fewer errors to correct |
> 
> *For presentation:*
> 
> | IDE feature | Description |
> |---|---|
> | Pretty-printing | Colour code keywords so the user can identify any errors |
> | Expand/collapse (code) blocks | The user can hide code that they are not currently working on |
> 
> *For debugging:*
> 
> | IDE feature | Description |
> |---|---|
> | Single stepping | Run the code **one line at a time** // shows the effect of each line of code |
> | Breakpoints | Stop the code running at a set point to check the flow/variable contents |

### Q17
> **[mark-scheme]**
> **1 mark** each to **max 2**:
> 
> - The interpreter will stop when an error is found
> - ... so the error can be corrected in real-time, and the result of changes seen immediately
> - Only one error is displayed at a time
> - … so fewer errors to correct simultaneously and no dependent errors
> **[mark-scheme]**
> **1 mark **each to **max 3**:
> 
> - Program can be distributed without source code
> - ... so it cannot be edited/stolen/plagiarised
> - Users do not require the translator to run the program
> - … so time is not spent retranslating by user

### Q18
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 4**)
> 
> e.g.
> 
> - Single stepping
> - Run the program one line at a time
> - … and check the variable contents / program flow // show the effect of each line of code
> - Set breakpoints
> - … run the code up to a set line
> - ... and then check the status
> - Variable/report watch window
> - … view how the data changes as the program is running

### Q19
> **[mark-scheme]**
> (i)** 1 mark** for correct name, **1 mark **for matching description
> 
> - Expand/collapse code blocks…
> - … sections of source code that are part of the same block can be expanded to see the content or collapsed so that the overall code is seen
> - Auto-indentation // auto-formatting...
> - ... automatically indents/formats code as the user types so that the structure is clear // aids readability
> 
> (ii) **1 mark** for correct name, **1 mark **for matching description
> 
> - Breakpoints …
> - … stops the code running on a set line to view the current status/variable contents/program flow
> - Report window // variable watch window …
> - … shows the values in variables/data structures and how they change when each line is run
