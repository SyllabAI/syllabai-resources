# Exam Questions — Object-Oriented Programming
**20. Further Programming** · Cambridge (CIE) A-LEVEL computer-science (9618)
> Source: [https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/](https://www.savemyexams.com/a-level/computer-science/cie/19/topic-questions/) · 42 questions across 1 sets


## Exam Questions (42 questions)


### Q1 — very_hard — 6 marks

**Q1** [6 marks]

A warehouse uses robots to move goods. The program is written using Object-Oriented Programming (OOP). The class `Robot` is shown.

A robot uses 1 unit of battery for each metre it moves.

The class `CarrierRobot` inherits from `Robot`. A carrier robot can carry a load, measured in kilograms. Part of the class is shown.

The method `Move()` must be redefined in `CarrierRobot` so that:

- when `Load` is 0, the robot uses 1 unit of battery for each metre, in the same way as a `Robot`
- when `Load` is greater than 0, the robot uses 2 units of battery for each metre
- if the battery level is less than the battery needed for the whole move, the robot does not move and the method outputs "Battery too low".

The attributes of `Robot` are private, so they cannot be accessed directly from `CarrierRobot`.

Write pseudocode for the method `Move()` in the class `CarrierRobot`.

### Q2 — medium — 3 marks

**Q2** [3 marks]

A mobile phone company uses a program written using Object-Oriented Programming (OOP). The class `PhonePlan` is shown.

The class `FamilyPlan` inherits from `PhonePlan`. Part of the class is shown.

The monthly cost of a family plan is the base price plus 8.50 for each extra user.

The method `GetMonthlyCost()` must be redefined in `FamilyPlan` to return this monthly cost.

Write pseudocode for the method `GetMonthlyCost()` in the class `FamilyPlan`.

### Q3 — easy — 2 marks

**Q3** [2 marks]

A messaging program is written using Object-Oriented Programming (OOP). The class `Message` is shown.

The class `UrgentMessage` inherits from `Message`. It redefines the method `Show()`.

The main program runs these statements. Each `OUTPUT` statement displays its value on a new line.

Write the output from the main program.

### Q4 — hard — 3 marks

**Q4** [3 marks]

A music teaching app is written using Object-Oriented Programming (OOP). The class inheritance diagram is shown.

In each class box the class name is at the top, then the attributes, then the methods. Every class has its own `Constructor()`. Any other method listed in a derived class box has been redefined in that class.

| `Instrument` |   |   |
|---|---|---|
| `Name : STRING` |   |   |
| `Constructor()`<br>`GetName()`<br>`PlayNote()`<br>`Tune()` |   |   |
| ↑ inherits from `Instrument` | ↑ inherits from `Instrument` |   |
| `StringInstrument` | `Drum` |   |
| `NumberOfStrings : INTEGER` | `Diameter : REAL` |   |
| `Constructor()`<br>`Tune()` | `Constructor()`<br>`PlayNote()` |   |
| ↑ inherits from `StringInstrument` | ↑ inherits from `StringInstrument` |   |
| `Violin` | `Guitar` |   |
| `BowLength : REAL` | `IsElectric : BOOLEAN` |   |
| `Constructor()`<br>`PlayNote()` | `Constructor()` |   |

Three objects are created:

- `MyDrum` from the class `Drum`
- `MyViolin` from the class `Violin`
- `MyGuitar` from the class `Guitar`

Complete the table. For each method call, write the name of the class whose version of the method runs.

| Method call | Class whose version runs |
|---|---|
| `MyDrum.PlayNote()` |   |
| `MyDrum.Tune()` |   |
| `MyViolin.PlayNote()` |   |
| `MyViolin.Tune()` |   |
| `MyGuitar.PlayNote()` |   |
| `MyGuitar.Tune()` |   |

### Q5 — medium — 3 marks

**Q5** [3 marks]

A drawing program is written using Object-Oriented Programming (OOP). The class inheritance diagram shows a parent class `Shape` and two derived classes, `Rectangle` and `Circle`.

In each class box the class name is at the top, then the attributes, then the methods.

| `Shape` |   |
|---|---|
| `Colour : STRING`<br>`PositionX : INTEGER`<br>`PositionY : INTEGER` |   |
| `Constructor()`<br>`GetColour()`<br>`GetArea()` |   |
| ↑ inherits from `Shape` | ↑ inherits from `Shape` |
| `Rectangle` | `Circle` |
| `Width : REAL`<br>`Height : REAL` | `Radius : REAL` |
| `Constructor()`<br>`GetArea()` | `Constructor()`<br>`GetArea()` |

The method `GetColour()` is not listed in `Rectangle` or in `Circle`, but objects of both classes can still use it.

The method `GetArea()` is listed in all three class boxes.

Explain why `GetArea()` is listed again in `Rectangle` and in `Circle`.

### Q6 — easy — 2 marks

**Q6** [2 marks]

In Object-Oriented Programming (OOP), a parent class can have one or more derived classes.

Define the term **polymorphism**.

### Q7 — very_hard — 6 marks

**Q7** [6 marks]

A garage program uses object-oriented programming. The class `Car` is declared as follows. Its other methods are not shown.

A new class `ElectricCar` inherits from `Car`. It needs:

- a private attribute for the battery capacity, for example 57.5
- a private attribute for the charge level, stored as a whole-number percentage
- a constructor that takes the registration and the battery capacity as its only parameters.

When an `ElectricCar` object is created:

- the fuel type is always set to `"Electric"`
- the charge level is set to 100.

Write pseudocode for the class `ElectricCar`. You only need to write the attributes and the constructor.

### Q8 — medium — 4 marks

**Q8** [4 marks]

A shop program uses object-oriented programming. Three of its classes are shown.

The class `Product`:

The class `Food`:

The class `ChilledFood`:

This statement is executed:

The object `Snack` has four attributes.

Complete the table to show, for each attribute, the class in which it is declared and the value it holds after the statement has been executed.

| Attribute | Class in which it is declared | Value |
|---|---|---|
| `Name` |   |   |
| `Price` |   |   |
| `ShelfLife` |   |   |
| `Temperature` |   |   |

### Q9 — medium — 3 marks

**Q9** [3 marks]

A car park program uses object-oriented programming (OOP). The class `ParkingTicket` has three attributes. All three attributes are PRIVATE.

The constructor has already been written:

Complete the pseudocode by writing the three attribute declarations.

### Q10 — easy — 2 marks

**Q10** [2 marks]

A bank program uses object-oriented programming. The class `Account` is declared as follows.

The class `SavingsAccount` inherits from `Account`. Its constructor must call the constructor of `Account` to set the account number.

Complete the pseudocode for the class `SavingsAccount`.

### Q11 — easy — 2 marks

**Q11** [2 marks]

A library program uses object-oriented programming (OOP). The class `Book` has these two attributes:

- `NumberOfPages` stores the number of pages in the book
- `OnLoan` stores whether or not the book is currently borrowed.

Both attributes must be declared as PRIVATE.

Write the pseudocode declaration for each attribute.

### Q12 — hard — 5 marks

**Q12** [5 marks]

An airline is writing a program to manage its staff using object-oriented programming.

The following data are stored for every member of staff:

- staff ID
- name
- date joined
- hourly rate of pay, in dollars and cents (can be edited).

There are two types of staff, and each type needs its own class.

- A pilot records the total number of whole hours they have flown.
- A cabin crew member records whether they hold a first-aid certificate or not. A cabin crew member also has a method to assign them to a section of the aircraft.

Complete the class inheritance diagram to show the attributes, methods and inheritance. In each class box the class name is at the top, then the attributes, then the methods. Use the middle row of the diagram to show the inheritance.

| `Staff` |   |
|---|---|
| `StaffID : STRING`<br>`Name : STRING`<br>`DateJoined : DATE`<br>................................ |   |
| `Constructor()`<br>`GetName()`<br>................................ |   |
| ................................ | ................................ |
| `Pilot` | `CabinCrew` |
| ................................ | ................................ |
| `Constructor()` | `Constructor()`<br>`AssignSection()` |

### Q13 — very_hard — 6 marks

**Q13** [6 marks]

A concert venue sells tickets using a program written with Object-Oriented Programming (OOP). The class `Ticket` is shown.

Write pseudocode for the main program to:

- take as input a ticket ID and a price
- create a `Ticket` object called `ThisTicket` using the input values
- reduce the price of `ThisTicket` by 10% if its price is greater than 100.0
- sell `ThisTicket`
- output the ticket ID and the final price of `ThisTicket`.

The main program must use the methods of the class to access the attributes of `ThisTicket`.

### Q14 — hard — 4 marks

**Q14** [4 marks]

A sports centre is writing a program using object-oriented programming (OOP). The class `CourtBooking` stores the details of one booking of a tennis court.

The class has the attribute BookingRef, of data type STRING. It needs four more attributes, one for each item of data in the table. An example value is given for each item.

Complete the table. For each attribute, write a suitable identifier and the most appropriate data type.

| Data stored | Example value | Identifier | Data type |
|---|---|---|---|
| the number of hours the court is booked for | 1.5 | .................... | .................... |
| whether or not the booking has been paid for | FALSE | .................... | .................... |
| the date the court is booked for (dd/mm/yyyy) | 14/03/2026 | .................... | .................... |
| the telephone number of the customer | 0061412555019 | .................... | .................... |

### Q15 — medium — 3 marks

**Q15** [3 marks]

A sports club program uses object-oriented programming (OOP). The class `Member` stores the details of one club member.

The table shows some of the attributes of `Member`. One row has been completed for you.

| Attribute | Data type | Description |
|---|---|---|
| MembershipLevel | STRING | the level of membership, for example "Gold" |
| MonthlyFee | .................... | the fee paid each month in dollars and cents, for example 29.50 |
| HasLocker | .................... | whether or not the member rents a locker |
| VisitsThisMonth | .................... | the number of times the member has visited the club this month |

Complete the table by writing the most appropriate data type for each attribute.

### Q16 — medium — 3 marks

**Q16** [3 marks]

A zoo uses an object-oriented program to keep records of its animals. The class inheritance diagram shows a parent class `Animal` and two derived classes, `Bird` and `Fish`.

In each class box the class name is at the top, then the attributes, then the methods.

| `Animal` |   |
|---|---|
| `AnimalID : STRING`<br>`Name : STRING`<br>`DateArrived : DATE` |   |
| `Constructor()`<br>`GetName()` |   |
| ↑ inherits from `Animal` | ↑ inherits from `Animal` |
| `Bird` | `Fish` |
| `WingSpan : REAL`<br>`CanFly : BOOLEAN` | `WaterType : STRING` |
| `Constructor()`<br>`GetWingSpan()` | `Constructor()`<br>`GetWaterType()` |

An object `Parrot` is created from the class `Bird`.

Complete the table. Write **Yes** if `Parrot` has the attribute or method. Write **No** if it does not.

| Attribute or method | Yes or No |
|---|---|
| `WingSpan` |   |
| `WaterType` |   |
| `DateArrived` |   |
| `GetName()` |   |
| `GetWaterType()` |   |
| `GetWingSpan()` |   |

### Q17 — easy — 2 marks

**Q17** [2 marks]

A school system is written using object-oriented programming. It has a class `Person` and a class `Student`.

The class `Student` inherits from the class `Person`.

Describe what is meant by **inheritance**, using these two classes in your answer.

### Q18 — easy — 2 marks

**Q18** [2 marks]

In object-oriented programming (OOP), a class is made up of attributes and methods.

Describe what is meant by an **attribute** in OOP.

### Q19 — hard — 4 marks

**Q19** [4 marks]

A game uses an object-oriented program. The class `Character` has these members:

- `Health`, an integer attribute that stores the character's health points
- `TakeDamage(Amount : INTEGER)`, a procedure that the main program calls each time the character is hit. It subtracts `Amount` from `Health` and then calls `CheckHealth()`
- `GetHealth()`, a function that the main program calls to display the character's health points
- `CheckHealth()`, a procedure that sets another attribute, `IsActive`, to `FALSE` when `Health` is 0 or less. It is only called by `TakeDamage()`

The value of `Health` must only be changed by `TakeDamage()`.

Complete the table. For each member, write the access level `PUBLIC` or `PRIVATE` and justify your choice.

| Member | Access level | Justification |
|---|---|---|
| Health |   |   |
| TakeDamage() |   |   |
| GetHealth() |   |   |
| CheckHealth() |   |   |

### Q20 — medium — 3 marks

**Q20** [3 marks]

A program that monitors water tanks is written using Object-Oriented Programming (OOP). The class `Tank` is shown.

The main program is:

State the **three** values output by the main program, in order.

### Q21 — very_hard — 6 marks

**Q21** [6 marks]

A water supply company uses the class `WaterTank`. Part of the class is shown:

The attributes `Capacity` and `Level` are both measured in litres.

Two more public methods are needed. Each method takes one parameter, the number of litres. The parameter is always a positive integer.

- `AddWater()` adds water to the tank. If all the water fits, `Level` increases by the number of litres and the method returns 0. If it does not all fit, the tank is filled to `Capacity` and the method returns the number of litres that did not fit.
- `Drain()` removes water from the tank. `Level` must never fall below 0. This method does not return a value.

Write pseudocode for the methods `AddWater()` and `Drain()`.

### Q22 — easy — 2 marks

**Q22** [2 marks]

A program to control the lights in an office is written using Object-Oriented Programming (OOP). The class `Lamp` is shown.

Write pseudocode statements in the main program to:

- create an object called `DeskLamp` with a power of 40 watts, for the room "Office"
- switch `DeskLamp` on.

### Q23 — medium — 3 marks

**Q23** [3 marks]

A shop uses an object-oriented program to manage its stock. Part of the class `Product` is shown. The attributes must be available only through the methods of the class.

This code is written in the main program, outside the class. It records the sale of 3 items and then outputs the total value of the remaining stock.

Lines 02 and 03 break encapsulation.

Write the pseudocode to replace lines 02 and 03 so that they perform the same task without breaking encapsulation.

### Q24 — medium — 3 marks

**Q24** [3 marks]

A program for a fuel station is written using Object-Oriented Programming (OOP). The class `FuelPump` has a constructor that takes a pump number and a fuel type.

The main program executes this statement:

Describe what happens when this statement is executed.

### Q25 — medium — 3 marks

**Q25** [3 marks]

A hotel review program uses the class `Review`. The class contains this attribute declaration:

A valid rating is a whole number from 1 to 5 inclusive.

Write pseudocode for the public setter method `SetRating()`. The method:

- takes the new rating as a parameter
- updates `Rating` only if the new rating is valid
- leaves `Rating` unchanged if the new rating is not valid.

### Q26 — easy — 2 marks

**Q26** [2 marks]

A teacher uses an object-oriented program to store students' test marks. Part of the class `Student` is shown.

This code is written in the main program, outside the class. Line numbers are shown for reference.

Identify the line number that breaks encapsulation, and give the reason.

### Q27 — easy — 2 marks

**Q27** [2 marks]

A weather station program uses the class `Sensor`. The class contains this attribute declaration:

Code outside the class must be able to find the current value of `Reading`.

Write pseudocode for the public getter method `GetReading()`.

### Q28 — hard — 4 marks

**Q28** [4 marks]

A bank uses a program written using Object-Oriented Programming (OOP). Part of the class `Account` is shown.

Complete the table. For each method, write **constructor**, **getter** or **setter**, or write **none of these**. Give a reason from the code for each answer.

| Method | Type of method | Reason from the code |
|---|---|---|
| NEW |   |   |
| GetBalance |   |   |
| SetOwnerName |   |   |
| Withdraw |   |   |

### Q29 — easy — 2 marks

**Q29** [2 marks]

A program for a football league is written using Object-Oriented Programming (OOP). The class `Match` has a constructor with two parameters.

This statement is executed:

Complete the **two** sentences about this statement.

`Game12` is an ............................................ of the class `Match`.

The process of creating `Game12` from the class `Match` is called ............................................

### Q30 — hard — 3 marks

**Q30** [3 marks]

A weather station uses an object-oriented program. The class diagram for `Sensor` is shown. All the attributes are `PRIVATE` and all the methods are `PUBLIC`. The method `TakeReading()` reads the sensor and stores the result in `LastReading`.

| Sensor |
|---|
| `SensorID : STRING`<br>`Location : STRING`<br>`LastReading : REAL` |
| `Constructor(GivenID : STRING, GivenLocation : STRING)`<br>`SetLocation(NewLocation : STRING)`<br>`TakeReading()`<br>`GetSensorID()`<br>`GetLocation()` |

Code outside the class now needs to output the value of `LastReading`. A programmer suggests changing the declaration of `LastReading` from `PRIVATE` to `PUBLIC`.

Explain why this change is **not** appropriate, and describe what the programmer should do instead.

### Q31 — medium — 3 marks

**Q31** [3 marks]

A program uses the class `Ticket`. Part of the class is shown. The bodies of the two methods are not shown.

Identify which method is the getter and which method is the setter. Explain why one method is written as a function and the other as a procedure.

### Q32 — easy — 2 marks

**Q32** [2 marks]

An airline uses a program written using Object-Oriented Programming (OOP). The class `Flight` stores the attributes `FlightNumber`, `Destination` and `SeatsBooked`. The class also contains several methods.

Describe what is meant by a **method** in a class.

### Q33 — very_hard — 6 marks

**Q33** [6 marks]

A hotel booking program uses a class, `Room`.

The class has these attributes:

- the room number, for example 214
- the room type, for example "Double"
- the nightly rate, for example 85.50
- whether the room is occupied
- the name of the guest in the room.

All attributes must be available only through the methods of the class.

When a `Room` object is created, the constructor is given the room number, the room type and the nightly rate. A new room is always unoccupied and has no guest, so the constructor sets the room to unoccupied and the guest name to an empty string.

Write pseudocode to declare the class `Room`, its attributes and its constructor. Do **not** write any other methods.

### Q34 — medium — 3 marks

**Q34** [3 marks]

A cinema uses an object-oriented program to sell tickets. Part of the class `Ticket` is shown.

Explain how encapsulation is used in the class `Ticket`.

### Q35 — medium — 4 marks

**Q35** [4 marks]

A delivery company uses a class, `Parcel`. A programmer has written this pseudocode to declare the class and its constructor. The line numbers are for reference only.

The pseudocode contains **four** errors.

Identify the line number of each error and write the corrected line.

### Q36 — easy — 2 marks

**Q36** [2 marks]

Encapsulation is one of the features of Object-Oriented Programming (OOP).

State what is meant by **encapsulation**, and identify the pseudocode keyword used in a class so that an attribute can only be accessed by the class's own methods.

### Q37 — easy — 2 marks

**Q37** [2 marks]

A weather program uses a class, `WeatherStation`. The pseudocode for the class is shown. Four parts are missing and are labelled A, B, C and D.

Complete the pseudocode by writing the missing item for each label.

### Q38 — hard — 5 marks

**Q38** [5 marks]

A cinema wants a program to manage ticket sales. Each film showing is called a screening. The program will use a class, `Screening`.

Draw a class diagram for `Screening`, to include:

- attributes and data types for the film title, the screen number, the date of the screening, the ticket price (for example 7.50) and the number of seats still available
- a method to create a `Screening` object and set its attributes
- a method to return the number of seats still available
- a method to change the ticket price
- a method to reduce the number of seats still available by the number of tickets sold.

### Q39 — medium — 3 marks

**Q39** [3 marks]

A library program is written using Object-Oriented Programming (OOP).

The program has one class, `Book`. When the program runs, it creates a separate `Book` object for each of the 3000 books in the library.

Explain the relationship between the class `Book` and the 3000 `Book` objects.

### Q40 — easy — 2 marks

**Q40** [2 marks]

Define the term **class** in Object-Oriented Programming (OOP).

### Q41 — medium — 4 marks

**Q41** [3 marks]

Objects and classes form the basic structure of Object‑Oriented Programming (OOP).

Outline the structure of a class.

*Source: Nov 2024 9618/32 Q10A*


**Q41** [1 mark]

Give **three **differences between an object and a class.

*Source: Nov 2024 9618/32 Q10B*


### Q42 — medium — 10 marks

**Q42** [5 marks]

A veterinary surgery wants to create a class for individual pets. 
Some of the attributes required in the class are listed in the table.

| Attribute | Data type | Description |
|---|---|---|
| PetID | STRING | unique ID assigned at registration |
| PetType | STRING | type of pet assigned at registration |
| OwnerTelephone | STRING | telephone number of owner assigned at registration |
| DateRegistered | DATE | date of registration |

State **one **reason why the attributes would be declared as PRIVATE.

*Source: Nov 2024 9618/31 Q9A*


**Q42** [5 marks]

Complete the class diagram for `Pet`, to include:

- an attribute and data type for the name of the pet
- an attribute and data type for the name of the owner
- a method to create a Pet object and set attributes at the time of registration
- a method to assign a pet ID
- a method to assign the date of registration
- a method to return the pet name
- a method to return the owner’s telephone number.

| Pet |   |
|---|---|
| PetID | : STRING |
| PetType | : STRING |
| OwnerTelephone | : STRING |
| DateRegistered | : DATE |
| ...................................................................... | : ...........................<br><br>: ........................... |
| .......................................................................................................................................................................................................................................................................................................................................... |   |

*Source: Nov 2024 9618/31 Q9B*

