# Mark Schemes — Language Translators
**5. System Software** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (7 questions)


### Q1
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

### Q2
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

### Q3
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

### Q4
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

### Q5
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

### Q6
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

### Q7
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
