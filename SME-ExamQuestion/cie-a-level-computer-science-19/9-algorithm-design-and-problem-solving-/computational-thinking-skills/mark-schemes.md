# Mark Schemes — Computational Thinking Skills
**9. Algorithm Design & Problem-solving** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (9 questions)


### Q1
`CheckBooking()` looks for a booking that matches the scanned passport and sends back `TRUE` or `FALSE`. **[1]** It is a function. **[1]**

`GetFreeSeats()` sends back the list of seats on that flight that have not yet been taken. **[1]** It is a function. **[1]**

`PrintBoardingPass()` prints the boarding pass for the chosen seat and sends nothing back. **[1]** It is a procedure. **[1]**

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for each description of an appropriate sub-problem of this scenario, up to a maximum of three
> 
> **1 mark** for each module correctly named as a procedure or a function, matching the description you have given, up to a maximum of three
> 
> Examples include:
> 
> Module: `CheckBooking()`. Use: finds the booking that matches the scanned passport and returns whether one was found. Type: function
> 
> Module: `GetFreeSeats()`. Use: returns the seats on the flight that are still free. Type: function
> 
> Module: `AllocateSeat()`. Use: records the seat the passenger has chosen against the booking. Type: procedure
> 
> Module: `PrintBoardingPass()`. Use: prints the boarding pass for the passenger. Type: procedure
> 
> Module: `PrintBagTag()`. Use: prints a tag for a bag the passenger is checking in. Type: procedure
> 
> Module: `CalculateBaggageCharge()`. Use: returns the amount owed for baggage above the free allowance. Type: function
> 
> The type mark is awarded on your own description. A module described as sending a value back is a function, and a module described as carrying out a task and sending nothing back is a procedure.
> 
> Do not award a type mark where no module description has been given.
> 
> Do not accept three modules that perform the same task under different names.

> **[exam-tip]**
> Give each module a name that says what it does, then one sentence on what it does, then the type. A name on its own earns nothing, and neither does a vague use such as "deals with the booking".
> 
> Decide the type from your own description, not from the size of the job. `PrintBoardingPass()` is the biggest task on this list and it is still a procedure, because it hands no value back. If your description says "returns" or "sends back", you have written a function.

### Q2
A smaller sub-problem is easier to understand and easier to solve than the whole problem at once. **[1]**

Small modules are easier to program, to test and to maintain than one large program. **[1]**

Different modules can be given to different programmers, so the modules can be written separately and at the same time. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for breaking a complex problem down makes it easier to understand or to solve, because each sub-problem is smaller
> 
> **1 mark** for smaller modules are easier to program, to test, to debug or to maintain
> 
> **1 mark** for different sub-problems can be given to different programmers, or to programmers with different expertise, so they can be solved separately
> 
> Accept, for any one mark, that a module can be reused when the same task is needed in several places in the program.
> 
> Accept, for any one mark, that the complexity of the program is reduced.
> 
> Do not accept the same benefit written twice in different words. "Easier to test" and "easier to debug" are one point, not two.
> 
> Do not accept "the program runs faster". Decomposition changes how the program is designed, not how quickly it executes.

> **[exam-tip]**
> Three marks means three different benefits. The easiest way to lose a mark here is to write "easier to write", "easier to test" and "easier to debug" as though they were three separate points. They are all the same idea, so examiners credit them once.
> 
> Reach for benefits from different stages instead: one about designing and understanding the problem, one about testing and maintaining the finished code, and one about how a team of programmers can share the work.

### Q3
Sub-problem 1: `FUNCTION` **[1]**

Sub-problem 2: `PROCEDURE` **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for Sub-problem 1: function
> 
> **1 mark** for Sub-problem 2: procedure
> 
> Accept the answers written in lower case, and accept the keywords `FUNCTION` and `PROCEDURE`.
> 
> Do not accept "subroutine", "module", "method" or "routine" for either answer. The question names the two types to choose between, so the answer must select one of them.

> **[exam-tip]**
> There is one test and only one: does the module send a value back to whatever called it? If it does, it is a function. If it just performs a task, it is a procedure.
> 
> Many students answer "function" for both, because both modules clearly do some work. Doing work is not the test. Sub-problem 2 does a great deal of work and still returns nothing, so it is a procedure.

### Q4
Data items:

Scooter ID **[1]**

User ID **[1]**

Date and time the hire started **[1]**

Date and time the hire ended **[1]**

Operations:

Calculate the length of the hire in minutes **[1]**

Calculate the cost of the hire **[1]**

**[6 marks]**

> **[mark-scheme]**
> **Any four from, one mark each, for the data items:**
> 
> - scooter ID
> - user ID
> - date and time the hire started
> - date and time the hire ended, or the number of minutes the scooter was used
> - parking point where the scooter was unlocked
> - parking point where the scooter was locked
> - cost of the hire
> - whether the payment for the hire was successful
> 
> **[4 marks]**
> 
> **Any two from, one mark each, for the operations:**
> 
> - check that the scooter is available before it is unlocked
> - unlock the scooter and start the hire
> - lock the scooter and end the hire
> - calculate the length of the hire from the start and end times
> - calculate the cost of the hire from the number of minutes used
> - take the payment from the user
> - update the stored location of the scooter
> 
> **[2 marks]**
> 
> Award the same point only once. "Date and time the hire ended" and "number of minutes used" are the same item and score one mark in total.
> 
> Accept details of the scooter, such as its ID or its type, as one data item.
> 
> Do not accept an operation written in the data list, or a data item written in the operation list.

> **[exam-tip]**
> An abstract model has two halves: the data the system holds and the operations the system performs on it. The marks here are split four and two, so write four nouns and then two verbs. Answers that give six data items and no operations throw away two marks.
> 
> The other frequent loss is repeating one item in two forms, such as "end time" and "minutes used". They come from the same fact, so only one of them is credited. Make each of your four items genuinely different.

### Q5
Abstraction keeps only the data that is needed to solve this problem and filters out the data that is not needed. **[1]**

The entry date and time and the exit date and time are kept, because the fee depends on how long the vehicle was parked. **[1]**

The vehicle colour, the vehicle make, the parking bay number and the driver's mobile phone number are left out of the model, because none of them changes the fee. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for stating the purpose of abstraction: only the data needed for the task is kept, or the data that is not needed for the task is filtered out
> 
> **1 mark** for naming data that is kept, with a reason: entry date and time and exit date and time, because the fee depends on the length of time parked
> 
> **1 mark** for naming data that is left out: vehicle colour, vehicle make, parking bay number or the driver's mobile phone number
> 
> Accept the number plate as data that is kept, because it is needed to match the entry record to the exit record for the same vehicle.
> 
> Accept "number of minutes parked" in place of the two date and time items.
> 
> Do not accept the second or third mark for an answer that only repeats the definition of abstraction. The question says to refer to the data given, so the item must be named.

> **[exam-tip]**
> This is a three-mark question, so one sentence defining abstraction cannot reach full marks. Give the definition once, then say which of the listed items you keep and which you throw away, and say why.
> 
> Students often keep the parking bay number because it feels like part of parking. Test every item against the one rule the question gives you: the fee depends only on the length of time. The bay number does not change the time, so it goes.

### Q6
Home address **[1]**

Date of birth **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from, one mark each:**
> 
> - email address
> - home address
> - date of birth
> - preferred language
> 
> **[2 marks]**
> 
> Do not accept passenger name, seat number, train number or travel date. Each of these is needed, either to choose the passengers travelling on that train on that date or to print the list.
> 
> Do not accept a general statement about abstraction. The question asks for items taken from the list given.

> **[exam-tip]**
> Read the description of the new module, not the description of the whole system. The system stores plenty of data that the ticketing company needs for other reasons, but this module only prints seat numbers and names, so anything that does not help to build that list is filtered out.
> 
> A common mistake is to name an item that the module does need, such as the train number, because it is not printed on the list. An item can still be essential even when it never appears in the output, if it is used to decide which records to include.

### Q7
> **[mark-scheme]**
> Examples include:
> 
> Module: `IdentifyMember() `
> Use: Identifies a club member who has expressed an interest in a given class
> 
> Module: `GetMemberPhoneNumber() `
> Use: Gets the mobile phone number of a member
> 
> Module: `CreateMessage() `
> Use: Generates a text message to a member
> 
> Module: `SendMessage() `
> Use: Sends a text message to a member in the waiting list
> 
> One mark for name **and** use
> 
> **Note: max 3 marks**

### Q8
> **[mark-scheme]**
> To make the solution easier to design / implement / solve

### Q9
> **[mark-scheme]**
> - Customer ID – to reference the other customer details
> - Email address – to send the email
> - Name – to personalise the email
> - Date of last visit – to select which customers should receive an email
> - Unique voucher code (or method of code generation) – to include in the email
> 
> Mark as follows:
> 
> One mark per item **and** justification
> 
> **Max 3 marks**
> **[mark-scheme]**
> Abstraction
