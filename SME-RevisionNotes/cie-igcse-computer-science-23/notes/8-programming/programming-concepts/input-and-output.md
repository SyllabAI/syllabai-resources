---
note_id: "rn_957wFDRHscbD8VVJ"
title: "Input & Output"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/8-programming/programming-concepts/input-and-output
path: 8-programming/programming-concepts/input-and-output
updated_at: "2024-11-28T10:24:44.679Z"
spec_point_ids: ["spcpt_F6TdQnH2yysTzcG2"]
spec_point_codes: []
guided_study: true
---

# Input & Output

## Input & Output

> **Spec point** — `spcpt_F6TdQnH2yysTzcG2` · 3 Understand and use input and output 

## Input & Output

### What is an input?

- An input is** **a value that is** read from an input device **and then **processed **by a computer program
- Typical input devices include:

  - **Keyboards **- Typing text
  - **Mice **- Selecting item, clicking buttons
  - **Sensors **- Reading data from sensors such as temperature, pressure or motion
  - **Microphone **- Capturing audio, speech recognition
- Without inputs, programs are** not useful **as they can't i**nteract with the outside world **and always produce the **same result**
- In programming the **keyboard **is considered the **standard** for user input
- If the command '**INPUT**' is executed, a program will wait for the **user **to **type a sequence of characters**
- In other programming languages **different command words** can be used

#### Examples

| **Pseudocode (INPUT <identifier>)** | **Python** |
|---|---|
| `INPUT Name `<br><br>`IF Name ← "James" OR Name ← "Rob" THEN...` | `name=input("Enter your name: ")`<br><br>`if name == "James" or name == "Rob":` |

### What is an output?

- An output is a value **sent to an output device** from a computer program
- Typical output devices include:

  - **Monitor **- Displaying text, images or graphics
  - **Speaker **- Playing audio
  - **Printer **- Creating physical copies of documents or images
- In programming the **monitor **is considered the **standard** for user output
- If the command '**OUTPUT**' is executed, a program will output to the screen
- In other programming languages **different command words** can be used

#### Examples

| **Pseudocode (OUTPUT <identifier(s)>)** | **Python** |
|---|---|
| `INPUT Name `<br><br>`IF Name ← "James" OR Name ← "Rob" THEN`<br><br>`  OUTPUT "Great names!"` | `name=input("Enter your name: ")`<br><br>`if name == "James" or name == "Rob":`<br><br>`  print("Great names!")` |
| `INPUT Name `<br><br>`IF Name ← "James" OR Name ← "Rob" THEN`<br><br>`  OUTPUT "Love the name ", Name` | `name=input("Enter your name: ")`<br><br>`if name == "James" or name == "Rob":`<br><br>`  print("Love the name "+name)` |
