# Mark Schemes — Object-Oriented Programming
**20. Further Programming** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (42 questions)


### Q1
- Procedure header `Move(Distance : INTEGER)`, the same identifier and parameter as in `Robot`, and `ENDPROCEDURE` **[1]**
- Battery needed calculated as the distance, doubled when the load is greater than 0 **[1]**
- Battery needed compared with the battery level obtained using `GetBattery()` **[1]**
- If there is not enough battery, "Battery too low" output and the robot not moved **[1]**
- Otherwise, the parent's method called with `SUPER.Move(Distance)` **[1]**
- ... and when the load is greater than 0, a further `Distance` units taken from the battery using `SetBattery()` **[1]**

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for `PROCEDURE Move(Distance : INTEGER)` ... `ENDPROCEDURE`
> 
> **1 mark** for the battery needed: `Distance` when `Load` is 0, twice `Distance` when `Load` is greater than 0
> 
> **1 mark** for comparing the battery needed with `GetBattery()`, so that a move needing exactly the remaining battery is allowed
> 
> **1 mark** for outputting "Battery too low" with no change to the position or the battery
> 
> **1 mark** for calling `SUPER.Move(Distance)` when there is enough battery
> 
> **1 mark** for, only when loaded, `SetBattery(GetBattery() - Distance)` or equivalent
> 
> Accept `GetBattery()` and `SetBattery()` with or without `SUPER.` in front
> 
> Accept `CALL` in front of a procedure call
> 
> Accept the extra battery taken before `SUPER.Move(Distance)` is called, provided it is inside the branch where there is enough battery
> 
> Accept the comparison written the other way round, and a `NOT` of the opposite test, if the logic is the same
> 
> A declaration of the local variable is not required
> 
> Do not award the fifth mark for `Move(Distance)` without `SUPER.`. Inside the redefined method this calls the `Move()` in `CarrierRobot` again, not the one in `Robot`
> 
> Do not award the fifth or sixth mark for `Position ← Position + Distance` or any assignment to `Battery` inside `CarrierRobot`. Both attributes are private to `Robot`
> 
> Do not award the third mark if the battery level is compared with `Distance` in every case. A loaded robot needs twice the distance

> **[exam-tip]**
> `Position` and `Battery` belong to `Robot` and are private, so `CarrierRobot` cannot change them itself. There is also no method to set the position. The only way to move the robot is to call the parent's version with `SUPER.Move(Distance)`. That call also takes 1 unit per metre from the battery, so a loaded robot only needs one more `Distance` taken off.
> 
> Many students write `Move(Distance)` without `SUPER.`, which calls the redefined method again and never finishes. Others check the battery against `Distance` for every robot. Test your answer: a loaded robot with 20 units of battery moving 10 metres needs exactly 20, so it moves and its battery becomes 0. Moving 1 more metre then outputs "Battery too low".

### Q2
Function header with the same identifier as the method in `PhonePlan`, no parameters, `RETURNS REAL`, and `ENDFUNCTION` **[1]**

The base price found by calling the parent's method, `SUPER.GetMonthlyCost()` **[1]**

The extra users multiplied by 8.50, added to the base price, and the result returned **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `FUNCTION GetMonthlyCost() RETURNS REAL` ... `ENDFUNCTION`
> 
> **1 mark** for using `SUPER.GetMonthlyCost()` to obtain the base price
> 
> **1 mark** for adding `ExtraUsers` multiplied by 8.50 and returning the result
> 
> Accept the header with or without `PUBLIC`
> 
> Accept the calculation stored in a local variable which is then returned
> 
> Do not accept `BasePrice` used directly inside `FamilyPlan` for the second mark. `BasePrice` is a private attribute of `PhonePlan`
> 
> Do not accept `GetMonthlyCost()` without `SUPER.` for the second mark. Inside the redefined method, this calls the method in `FamilyPlan` again, not the one in `PhonePlan`
> 
> Do not award the first mark for a different identifier, such as `GetFamilyCost()`. That adds a new method; it does not redefine the existing one

> **[exam-tip]**
> A redefined method must use exactly the same identifier as the method in the parent class. If you name it differently, a `FamilyPlan` object still runs the version in `PhonePlan` and returns only the base price.
> 
> The most common error is writing `RETURN BasePrice + ExtraUsers * 8.50`. It looks correct, but `BasePrice` is private to `PhonePlan`, so `FamilyPlan` cannot use it. Ask the parent class for it with `SUPER.GetMonthlyCost()`. For a plan created as `NEW FamilyPlan("Home", 20.00, 3)`, the method returns 20.00 + 25.50 = 45.50.

### Q3
The first two lines, `URGENT` then `Fire drill`, in that order **[1]**

The last line, `Meeting at 10` **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `URGENT` followed by `Fire drill` as the first two lines
> 
> **1 mark** for `Meeting at 10` as the third and last line
> 
> Accept the values with or without quotation marks
> 
> Do not award the first mark for `Fire drill` on its own. `M2` is an `UrgentMessage` object, so the redefined `Show()` runs and outputs `URGENT` first
> 
> Do not award the first mark for `Fire drill` before `URGENT`. The redefined method outputs `URGENT` before it calls `SUPER.Show()`

> **[exam-tip]**
> `M1` is a `Message` object, so `M1.Show()` runs the version in `Message` and outputs only the text. `M2` is an `UrgentMessage` object, so `M2.Show()` runs the redefined version in `UrgentMessage`.
> 
> The line `SUPER.Show()` runs the parent class's version of `Show()` from inside the redefined one. That is how `UrgentMessage` can output the private `Text` it cannot access directly. Follow the statements in the order they are written, and write the outputs in the order the main program calls them: `M2` is shown before `M1`.

### Q4
| Method call | Class whose version runs |
|---|---|
| `MyDrum.PlayNote()` | **Drum** |
| `MyDrum.Tune()` | **Instrument** |
| `MyViolin.PlayNote()` | **Violin** |
| `MyViolin.Tune()` | **StringInstrument** |
| `MyGuitar.PlayNote()` | **Instrument** |
| `MyGuitar.Tune()` | **StringInstrument** |

Start at the object's own class. If the method is redefined there, that version runs. If not, move up to the parent class and check again. **[3]**

**[3 marks]**

> **[mark-scheme]**
> **3 marks** for all six rows correct
> 
> **2 marks** for four or five rows correct
> 
> **1 mark** for two or three rows correct
> 
> Correct answers, in order: `Drum`, `Instrument`, `Violin`, `StringInstrument`, `Instrument`, `StringInstrument`
> 
> Do not accept `Guitar` for either `MyGuitar` row. `Guitar` does not redefine `PlayNote()` or `Tune()`
> 
> Do not accept `Instrument` for `MyViolin.Tune()` or `MyGuitar.Tune()`. The nearest class above them that redefines `Tune()` is `StringInstrument`

> **[exam-tip]**
> The most common error is jumping straight to the top class. For `MyViolin.Tune()`, `Violin` has no `Tune()`, so look one level up. `StringInstrument` has redefined `Tune()`, so its version runs and you stop there. You never reach `Instrument`.
> 
> The other error is writing the object's own class for every row. `MyGuitar` is a `Guitar`, but `Guitar` redefines nothing, so every method it calls comes from a class above it.

### Q5
`GetArea()` has been redefined in `Rectangle` and in `Circle`. This is polymorphism. **[1]**

The area of each shape is calculated in a different way. A rectangle uses its width and height, and a circle uses its radius, so the single version in `Shape` cannot work for both. **[1]**

When `GetArea()` is called, the version in the object's own class runs. A `Circle` object runs the `GetArea()` written in `Circle`, and a `Rectangle` object runs the one written in `Rectangle`. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `GetArea()` is redefined in each derived class // this is polymorphism
> 
> **1 mark** for the area is calculated differently for each type of shape // the method in `Shape` does not use `Width`, `Height` or `Radius`
> 
> **1 mark** for the same method call runs a different version depending on the class of the object // an object uses the version in its own class, not the version in `Shape`
> 
> Accept "overridden" for "redefined"
> 
> Do not accept "`Rectangle` and `Circle` do not inherit `GetArea()`, so it must be written again". They do inherit it; they replace what it does
> 
> Do not accept "so that `Rectangle` and `Circle` can use `GetArea()`". They can already use it through inheritance, as they use `GetColour()`

> **[exam-tip]**
> Compare `GetArea()` with `GetColour()`. A colour is found in the same way for every shape, so `GetColour()` is inherited and not changed. An area is not, so `GetArea()` is redefined. Apart from `Constructor()`, which every class has, a method that appears again in a derived class box has been redefined there.
> 
> A common wrong answer is that the derived classes "need" `GetArea()` so they can use it. They could already use it. The reason for writing it again is to change what it does.

### Q6
Polymorphism allows a method defined in a parent class to be redefined in a derived class. **[1]**

The same method then behaves differently depending on which class the object was instantiated from. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for a method (in a parent class) is redefined in a derived class // methods can be redefined for derived classes
> 
> **1 mark** for the same method takes on different behaviours depending on which class is instantiated // the same method call gives a different result for objects of different classes
> 
> Accept "overridden" for "redefined"
> 
> Accept "base class" or "super class" for "parent class"
> 
> Do not accept "an object can take many forms" on its own. The answer must say what changes (the method) and what the change depends on (the class of the object)
> 
> Do not accept a description of inheritance, for example "a derived class gets all the methods of its parent class", for either mark

> **[exam-tip]**
> Students often mix up polymorphism and inheritance, because both involve a parent class and a derived class. Inheritance means the derived class receives the parent's attributes and methods. Polymorphism means the derived class redefines one of those methods, so the same method does something different.
> 
> Both marks need the word **method**. An answer about objects "taking many forms" does not say what is different, so it scores zero.

### Q7
- Class header with `INHERITS Car`, and `ENDCLASS` **[1]**
- Two private attributes, battery capacity as `REAL` and charge level as `INTEGER` **[1]**
- Constructor header `NEW` with a `STRING` and a `REAL` parameter, and `ENDPROCEDURE` **[1]**
- Parent constructor called with `SUPER.NEW`, passing the registration **[1]**
- ... and the value `"Electric"` for the fuel type **[1]**
- Battery capacity set from its parameter and charge level set to 100 **[1]**

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for `CLASS ElectricCar INHERITS Car` ... `ENDCLASS`
> 
> **1 mark** for two `PRIVATE` attribute declarations: battery capacity `REAL`, charge level `INTEGER`
> 
> **1 mark** for `PROCEDURE NEW(... : STRING, ... : REAL)` ... `ENDPROCEDURE`, with exactly two parameters
> 
> **1 mark** for `SUPER.NEW(...)` with the registration parameter as the first argument ...
> 
> **1 mark** for ... `"Electric"` as the second argument
> 
> **1 mark** for both assignments: battery capacity from the parameter and `ChargeLevel ← 100`
> 
> Accept any sensible identifiers, used consistently
> 
> Accept the constructor header with or without `PUBLIC`, and `New` for `NEW`
> 
> Do not accept `FuelType ← "Electric"` written inside `ElectricCar` for the fifth mark. `FuelType` is a private attribute of `Car`, so its value must be passed to the constructor of `Car`
> 
> Do not accept a constructor with a third parameter for the fuel type; the fuel type is fixed, not supplied
> 
> Do not award the attribute mark if `Registration`, `FuelType` or `Mileage` are declared again in `ElectricCar`

> **[exam-tip]**
> The constructor of `Car` needs two values, but an `ElectricCar` is only given one of them. The derived class supplies the missing one itself, so the call is `SUPER.NEW(GivenRegistration, "Electric")`. Many students write `SUPER.NEW(GivenRegistration)` and lose the mark.
> 
> Do not declare `Registration`, `FuelType` or `Mileage` again in `ElectricCar`. They are inherited from `Car`, and the constructor of `Car` already sets `Mileage` to 0.

### Q8
| Attribute | Class in which it is declared | Value |
|---|---|---|
| `Name` | **Product** | **"Yoghurt"** |
| `Price` | **Product** | **1.25** |
| `ShelfLife` | **Food** | **7** |
| `Temperature` | **ChilledFood** | **4** |

The constructor of `ChilledFood` calls the constructor of `Food` with the value 7, and the constructor of `Food` calls the constructor of `Product` with the name and the price. **[4]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `Name` holds `"Yoghurt"` and `Price` holds 1.25
> 
> **1 mark** for `ShelfLife` holds 7
> 
> **1 mark** for `Temperature` holds 4
> 
> **1 mark** for all four "declared in" entries correct: `Product`, `Product`, `Food`, `ChilledFood`
> 
> Accept `Yoghurt` without quotation marks
> 
> Do not accept `ChilledFood` in the "declared in" column for `Name`, `Price` or `ShelfLife`. The object has these attributes through inheritance, but they are declared in the parent classes
> 
> Do not accept "no value" or "unknown" for `ShelfLife`. The value 7 is passed up by `SUPER.NEW(GivenName, GivenPrice, 7)`

> **[exam-tip]**
> Follow each `SUPER.NEW` call up to the parent's constructor and match the arguments to the parameters by position. The third argument, 7, becomes `GivenDays` in `Food`, so `ShelfLife` is 7 even though the statement that creates `Snack` never mentions it.
> 
> Students often write `ChilledFood` for every row in the middle column because `Snack` is a `ChilledFood` object. The object has all four attributes, but each one is declared in only one class.

### Q9
The declaration of Registration as PRIVATE with the data type STRING **[1]**

The declaration of HoursStayed as PRIVATE with the data type REAL **[1]**

The declaration of Paid as PRIVATE with the data type BOOLEAN **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `PRIVATE Registration : STRING`
> 
> **1 mark** for `PRIVATE HoursStayed : REAL`
> 
> **1 mark** for `PRIVATE Paid : BOOLEAN`
> 
> Accept the three declarations in any order
> 
> Each identifier must be exactly the identifier used in the constructor's assignment statements
> 
> Do not accept `GivenReg` or `GivenHours` as an attribute identifier. These are the parameters of the constructor
> 
> Do not accept `PUBLIC` or `DECLARE` in place of `PRIVATE`

> **[exam-tip]**
> The constructor tells you everything you need. The attribute is the identifier on the left of each `←`. Its data type comes from what is assigned to it: the parameter's data type, or the kind of value, such as `FALSE`, which is a `BOOLEAN`.
> 
> The most common mistake is to declare the parameters, such as GivenReg, as the attributes. A parameter only exists while the constructor runs. The attribute is what the object keeps afterwards.

### Q10
The first gap is the keyword INHERITS **[1]**

The second gap is SUPER.NEW, which calls the constructor of the parent class **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `INHERITS`
> 
> **1 mark** for `SUPER.NEW`
> 
> Accept `SUPER.New`
> 
> Do not accept `EXTENDS`, `Inherits Account` written as a separate line, or brackets such as `SavingsAccount(Account)`. These are forms from Java, Visual Basic and Python, not the Cambridge pseudocode
> 
> Do not accept `SUPER.Account` or `Account.NEW`. In pseudocode every constructor is called `NEW`, and the parent's constructor is called with the keyword `SUPER`

> **[exam-tip]**
> In Cambridge pseudocode the constructor is always a procedure called `NEW`, in every class. So the parent's constructor is `SUPER.NEW`, not `SUPER` followed by the parent's class name. Students who program in Java often write the class name here.
> 
> Only the account number is passed up. The balance is set to 0 inside the constructor of `Account`, so `SavingsAccount` does not set it again.

### Q11
The declaration of NumberOfPages as PRIVATE with the data type INTEGER **[1]**

The declaration of OnLoan as PRIVATE with the data type BOOLEAN **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `PRIVATE NumberOfPages : INTEGER`
> 
> **1 mark** for `PRIVATE OnLoan : BOOLEAN`
> 
> Each mark needs all three parts: the keyword `PRIVATE`, the identifier and the correct data type
> 
> Do not accept `DECLARE` in place of `PRIVATE`: the question asks for the access level
> 
> Do not accept `PUBLIC`
> 
> Do not accept a declaration with no data type, for example `PRIVATE OnLoan`
> 
> Do not accept `REAL` for NumberOfPages, or `STRING` for OnLoan

> **[exam-tip]**
> An attribute declaration has the same shape as a variable declaration. The access level replaces `DECLARE`, then you write the identifier, a colon and the data type. Students who program in Java or Python often write something like private boolean onLoan or give a starting value with an equals sign. Neither is Cambridge pseudocode.
> 
> Do not leave out the data type. In the exam a declaration without one earns no mark.

### Q12
| `Staff` |   |
|---|---|
| `StaffID : STRING`<br>`Name : STRING`<br>`DateJoined : DATE`<br>`HourlyRate : REAL` |   |
| `Constructor()`<br>`GetName()`<br>`SetHourlyRate()` |   |
| ↑ inherits from `Staff` | ↑ inherits from `Staff` |
| `Pilot` | `CabinCrew` |
| `FlyingHours : INTEGER` | `FirstAidCertificate : BOOLEAN` |
| `Constructor()` | `Constructor()`<br>`AssignSection()` |

- `Staff` has an attribute for the hourly rate with data type `REAL` **[1]**
- `Staff` has a method to edit the hourly rate, for example `SetHourlyRate()` **[1]**
- `Pilot` has an attribute for the flying hours with data type `INTEGER` **[1]**
- `CabinCrew` has an attribute for the first-aid certificate with data type `BOOLEAN` **[1]**
- Both `Pilot` and `CabinCrew` inherit from `Staff` (both arrows point to `Staff`) **[1]**

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for `Staff` has an hourly rate attribute with data type `REAL`
> 
> **1 mark** for `Staff` has a method to edit the hourly rate
> 
> **1 mark** for `Pilot` has a flying hours attribute with data type `INTEGER`
> 
> **1 mark** for `CabinCrew` has a first-aid certificate attribute with data type `BOOLEAN`
> 
> **1 mark** for both `Pilot` and `CabinCrew` shown inheriting from `Staff`
> 
> Accept any sensible identifier without spaces, for example `PayRate`, `EditPayRate()`, `ChangeRate()`, `HoursFlown`, `HasFirstAid`
> 
> Accept the data type written with or without a space before the colon
> 
> Do not accept `INTEGER` for the hourly rate, because the rate contains cents
> 
> Do not award either hourly rate mark if the attribute or its method is placed in `Pilot` or `CabinCrew` instead of `Staff`
> 
> Do not award the inheritance mark if either arrow points from `Staff` to a derived class

> **[exam-tip]**
> Ask one question for each item of data: is it stored for EVERY member of staff, or only for one type? The hourly rate is stored for everyone, so it belongs in the parent class `Staff`. Students often put it in each derived class, which repeats code that inheritance is meant to remove.
> 
> The arrow points from the derived class up to the parent class, as in Cambridge's own class inheritance diagrams. Do not copy `StaffID` or the hourly rate into the derived class boxes; they are inherited and are not written again.

### Q13
One mark for each of the following:

- Declaring and inputting the ID and the price **[1]**
- Creating `ThisTicket` with `NEW Ticket` and the arguments in the correct order **[1]**
- Testing whether the price is greater than 100.0, inside a complete `IF` structure **[1]**
- Calling `SetPrice` with 90% of the current price **[1]**
- Calling `SellTicket()` on `ThisTicket` **[1]**
- Outputting the ID and price using `GetTicketID()` and `GetPrice()` **[1]**

**[6 marks]**

For example, an input price of 120.0 is reduced to 108.0. An input price of exactly 100.0 is not reduced.

> **[mark-scheme]**
> **1 mark** for declaring two variables of appropriate types and inputting the ID and the price into them
> 
> **1 mark** for `ThisTicket ← NEW Ticket(InID, InPrice)`, with the ID argument before the price argument
> 
> **1 mark** for a test that the price is greater than 100.0, in a complete `IF` ... `ENDIF` structure
> 
> **1 mark** for `ThisTicket.SetPrice()` called with 90% of the price, inside the `IF`
> 
> **1 mark** for `ThisTicket.SellTicket()`
> 
> **1 mark** for an `OUTPUT` of `ThisTicket.GetTicketID()` and `ThisTicket.GetPrice()`
> 
> Accept the input variable in the test, for example `InPrice > 100.0`
> 
> Accept any equivalent reduction as the argument to `SetPrice`, for example multiplying by 90 and dividing by 100, or subtracting 10% of the input price
> 
> Accept `SellTicket()` called before or after the price is reduced
> 
> Accept `New` for `NEW`
> 
> Accept `CALL` in front of a procedure method call
> 
> Do not accept `ThisTicket.Price` anywhere in the main program. `Price` is `PRIVATE`, so it can only be accessed through `GetPrice()` and `SetPrice()`
> 
> Do not accept outputting `InPrice` for the final price. The input variable is not changed when the object's price is reduced
> 
> Do not accept a test of greater than or equal to 100.0. The stem says greater than

> **[exam-tip]**
> The most common error is to change the price in a local variable and never call `SetPrice`. The object's own `Price` attribute is then still the full price, and `GetPrice()` returns it. When a class provides a setter, the change must go through it.
> 
> Every method call needs the object's identifier in front of it. `SellTicket()` on its own, or `Ticket.SellTicket()`, does not say which ticket is sold. Write `ThisTicket.SellTicket()`.

### Q14
| Data stored | Example value | Identifier | Data type |
|---|---|---|---|
| the number of hours the court is booked for | 1.5 | **HoursBooked** | **REAL** |
| whether or not the booking has been paid for | FALSE | **Paid** | **BOOLEAN** |
| the date the court is booked for (dd/mm/yyyy) | 14/03/2026 | **BookingDate** | **DATE** |
| the telephone number of the customer | 0061412555019 | **CustomerTelephone** | **STRING** |

An attribute for the hours booked with data type REAL **[1]**

An attribute for whether the booking has been paid for with data type BOOLEAN **[1]**

An attribute for the booking date with data type DATE **[1]**

An attribute for the telephone number with data type STRING **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each attribute with a sensible identifier and the correct data type, in any order
> 
> Accept any sensible identifier, for example `Hours`, `IsPaid`, `DateBooked`, `Telephone`
> 
> Do not accept an identifier that contains a space, such as Booking Date, or that starts with a digit. A 9618 identifier may contain only letters, digits and the underscore, and must start with a letter
> 
> Do not accept `INTEGER` for the telephone number. It is never used in a calculation, and as an integer the leading zeros in 0061412555019 would be lost
> 
> Do not accept `STRING` for the booking date. `DATE` is the data type for a calendar date
> 
> Do not accept `INTEGER` for the hours booked: 1.5 has a fractional part

> **[exam-tip]**
> The telephone number is the row most students get wrong. It is made of digits, so it looks like an `INTEGER`. Ask two questions: will the program ever do arithmetic with it, and does it matter if a leading 0 disappears? The answers are no and yes, so it is a `STRING`. Cambridge gives telephone numbers the data type `STRING` in its own OOP questions.
> 
> Also check each identifier. Students often copy the wording from the table, for example "Booking Date", and a space inside an identifier is not allowed. Join the words, with a capital letter at the start of each one.

### Q15
| Attribute | Data type | Description |
|---|---|---|
| MembershipLevel | STRING | the level of membership, for example "Gold" |
| MonthlyFee | **REAL** | the fee paid each month in dollars and cents, for example 29.50 |
| HasLocker | **BOOLEAN** | whether or not the member rents a locker |
| VisitsThisMonth | **INTEGER** | the number of times the member has visited the club this month |

REAL for MonthlyFee **[1]**

BOOLEAN for HasLocker **[1]**

INTEGER for VisitsThisMonth **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `REAL` for MonthlyFee
> 
> **1 mark** for `BOOLEAN` for HasLocker
> 
> **1 mark** for `INTEGER` for VisitsThisMonth
> 
> Do not accept `INTEGER` for MonthlyFee: 29.50 has a fractional part
> 
> Do not accept `STRING` or `CHAR` for HasLocker: the attribute only ever holds one of two logical values
> 
> Do not accept `REAL` for VisitsThisMonth: a number of visits is always a whole number

> **[exam-tip]**
> Use only the six data types from the Cambridge pseudocode: `INTEGER`, `REAL`, `CHAR`, `STRING`, `BOOLEAN` and `DATE`. Students who program in Python or Java often write float or int here. The mark scheme is written in the 9618 names, so answer with those.
> 
> For a yes/no item like HasLocker, some students write `STRING` so they can store "Yes" or "No". That works in a program, but it is not the most appropriate type. If the data can only be true or false, the answer is `BOOLEAN`.

### Q16
| Attribute or method | Yes or No |
|---|---|
| `WingSpan` | **Yes** |
| `WaterType` | **No** |
| `DateArrived` | **Yes** |
| `GetName()` | **Yes** |
| `GetWaterType()` | **No** |
| `GetWingSpan()` | **Yes** |

`Parrot` has everything declared in `Bird`, plus everything `Bird` inherits from `Animal`. It has nothing from `Fish`. **[3]**

**[3 marks]**

> **[mark-scheme]**
> **3 marks** for all six rows correct
> 
> **2 marks** for four or five rows correct
> 
> **1 mark** for two or three rows correct
> 
> Correct answers: `WingSpan` Yes, `WaterType` No, `DateArrived` Yes, `GetName()` Yes, `GetWaterType()` No, `GetWingSpan()` Yes
> 
> Accept a tick for Yes and a cross for No

> **[exam-tip]**
> The two derived classes do not share with each other. `Bird` and `Fish` both inherit from `Animal`, but a `Bird` object gets nothing from `Fish`. Students who see `GetWaterType()` on the same diagram often mark it Yes by mistake.
> 
> A derived class box lists only its NEW attributes and methods. The inherited ones, such as `DateArrived` and `GetName()`, are not written again, but the object still has them.

### Q17
The attributes and methods that are defined in the parent class `Person` **[1]**

are made available to (reused by) the derived class `Student`, so `Student` does not need to declare them again **[1]**

`Student` can also add its own extra attributes and methods.

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the attributes / properties and methods contained in the parent class / super class / base class (`Person`) ...
> 
> **1 mark** for ... are made available to / reused by another class / the derived class (`Student`)
> 
> Accept "a new class (`Student`) is defined that has all the attributes and methods of an existing class (`Person`)" for both marks
> 
> Accept subclass or child class for derived class, and superclass for parent class
> 
> Do not accept an answer with the direction reversed (`Person` inherits from `Student`)
> 
> Do not accept an answer about objects inheriting from a class. Inheritance is a relationship between two classes; an object is an instance of a class

> **[exam-tip]**
> Many students get the direction wrong. The derived class receives the attributes and methods; the parent class gives them. Check your sentence: `Student` inherits from `Person`, so `Student` gets what `Person` has, never the other way round.
> 
> Do not describe inheritance as a class passing things to its objects. Creating an object from a class is instantiation, not inheritance.

### Q18
An attribute is a data item (a property) that is defined in a class **[1]**

Each attribute is declared with a data type, for example STRING or INTEGER **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - A data item / a property / a variable ...
> - ... that is defined in a class / that belongs to a class
> - ... that is given a data type
> - Each object (instance) of the class stores its own value for the attribute
> 
> **[2 marks]**
> 
> Accept "characteristics" for the data type point, as CIE does
> 
> Do not accept "a column in a table" or "a field in a record" on its own. That is the meaning of attribute in a relational database, not in OOP
> 
> Do not accept a description of a method, for example "a procedure or function that the object can carry out"

> **[exam-tip]**
> The word attribute has two meanings on this course. In databases it is a column in a table. In OOP it is a data item stored in a class. Students who revise databases just before this question often write the database meaning and lose both marks. Say "in a class" in your answer.
> 
> A second common slip is to describe what an object does, such as "it calculates the total". That is a method. An attribute stores data; a method acts on that data.

### Q19
| Member | Access level | Justification |
|---|---|---|
| Health | PRIVATE | It must be hidden, so it can only be accessed and changed by the class's own methods |
| TakeDamage() | PUBLIC | The main program, outside the class, must be able to call it |
| GetHealth() | PUBLIC | The main program must call it to get the value of the PRIVATE attribute Health |
| CheckHealth() | PRIVATE | It is only called by another method of the class, so code outside the class does not need it |

One mark for each correct row **[4]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `Health`: `PRIVATE`, because it is hidden // can only be accessed by the class's own methods
> 
> **1 mark** for `TakeDamage()`: `PUBLIC`, because it is called from outside the class // by the main program
> 
> **1 mark** for `GetHealth()`: `PUBLIC`, because the main program uses it to return // read the value of `Health`
> 
> **1 mark** for `CheckHealth()`: `PRIVATE`, because it is only called from inside the class // by `TakeDamage()`
> 
> Each mark needs both the correct access level and a matching justification
> 
> Do not accept `PUBLIC` for `Health`. Code outside the class could then change it without using `TakeDamage()`
> 
> Do not accept `PUBLIC` for `CheckHealth()`, including the reason "it is a method". No code outside the class needs to call it, and methods can be `PRIVATE` as well as `PUBLIC`

> **[exam-tip]**
> Many students think every method must be `PUBLIC`. The Cambridge pseudocode allows `PRIVATE` methods too. Ask one question for each member: does code outside the class need to use it? If not, make it `PRIVATE`.
> 
> Write a justification for every row. An access level on its own, with no reason, does not score.

### Q20
First output: **250** **[1]**

Second output: **300** **[1]**

Third output: **550** **[1]**

**[3 marks]**

The two objects hold separate values. `TankB` reaches 350 after the second fill, but 350 is greater than its capacity of 300, so `Fill` sets its level to 300. `TankA` then gains 300 and moves from 250 to 550, which is within its capacity of 600.

> **[mark-scheme]**
> **1 mark** for 250
> 
> **1 mark** for 300
> 
> **1 mark** for 550
> 
> Follow through the third mark from an incorrect second output: 250 + (second output), up to a maximum of 600. For example, a second output of 350 leads to 600
> 
> Do not accept 450 for the first output. That adds the 200 filled into `TankB` to `TankA`

> **[exam-tip]**
> Keep a separate running value for each object as you trace. Students who keep one value for "the tank" add every `Fill` together and give 450 as the first output. `TankA.Fill(250)` changes only `TankA`.
> 
> Watch the call inside the brackets on the last `Fill` line. `TankB.GetLevel()` is evaluated first, and it returns the level of `TankB` after the cap, 300, not the 150 that was last filled.

### Q21
Function header for `AddWater` with an `INTEGER` parameter and `RETURNS INTEGER` **[1]**

Correct test for water that does not fit **[1]**

If it does not fit: the extra litres are calculated before `Level` is set to `Capacity`, and that value is returned **[1]**

If it fits: `Amount` is added to `Level` and 0 is returned **[1]**

Procedure header for `Drain` with an `INTEGER` parameter, and `ENDPROCEDURE` **[1]**

`Level` is set to 0 if the amount is greater than `Level`, otherwise the amount is subtracted from `Level` **[1]**

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for `FUNCTION AddWater` with one `INTEGER` parameter, `RETURNS INTEGER` and `ENDFUNCTION`
> 
> **1 mark** for a correct test for water that does not all fit, for example `Level + Amount > Capacity`
> 
> **1 mark** for, when the water does not fit, returning `Level + Amount - Capacity` calculated from the value of `Level` before it is changed, and setting `Level` to `Capacity`
> 
> **1 mark** for, when the water fits, adding `Amount` to `Level` and returning 0
> 
> **1 mark** for `PROCEDURE Drain` with one `INTEGER` parameter and `ENDPROCEDURE`
> 
> **1 mark** for setting `Level` to 0 when the amount is greater than `Level`, otherwise subtracting the amount from `Level`
> 
> Accept `Amount > Capacity - Level` as the test in `AddWater`
> 
> Accept `Level + Amount >= Capacity` as the test in `AddWater`, because a tank that ends exactly full then returns 0 from either branch
> 
> Accept a `RETURN` statement inside each branch in place of a local variable, provided `Level` is updated before the `RETURN` is executed
> 
> Accept `Amount >= Level` as the test in `Drain`, because both branches then give 0
> 
> Do not award the third mark if `Level` is set to `Capacity` first and the overflow is then calculated from the new `Level`. That always returns `Amount`

> **[exam-tip]**
> Order matters in `AddWater`. If you write `Level ← Capacity` first and then calculate the overflow as `Level + Amount - Capacity`, the answer is always `Amount`. Work out the overflow while `Level` still holds the old value.
> 
> Always trace your method with real numbers. With a capacity of 500 and a level of 350, adding 400 litres should set `Level` to 500 and return 250.

### Q22
Line 1 creates the object, with the arguments in the same order as the constructor's parameters: room first, then watts. **[1]**

Line 2 calls the method `SwitchOn()` on the object `DeskLamp`. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `DeskLamp ← NEW Lamp("Office", 40)`, with the room before the watts
> 
> **1 mark** for `DeskLamp.SwitchOn()`
> 
> Accept `New` for `NEW`
> 
> Accept `CALL DeskLamp.SwitchOn()`
> 
> Do not accept `NEW Lamp(40, "Office")`. The arguments must match the order and data types of the parameters `GivenRoom : STRING, GivenWatts : INTEGER`
> 
> Do not accept `DeskLamp ← Lamp("Office", 40)` without `NEW`
> 
> Do not accept `Lamp.SwitchOn()`. The method must be called on the object, not the class
> 
> Do not accept `DeskLamp.IsOn ← TRUE`. `IsOn` is `PRIVATE`, so it cannot be changed from outside the class

> **[exam-tip]**
> The question gives the power before the room, but the constructor's header takes the room first. Students who copy the order of the question write `NEW Lamp(40, "Office")` and lose the mark. Always read the parameter list of `NEW` before you write the arguments.
> 
> The second common error is calling the method on the class name. `Lamp` is the template; `DeskLamp` is the object that is switched on.

### Q23
Line 02 calls the setter `SetStock()` to change the stock level **[1]**

The new value passed to `SetStock()` is the value returned by the getter `GetStock()`, minus 3 **[1]**

Line 03 uses `GetStock()` and `GetPrice()` in place of the attributes **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for calling `Item.SetStock(...)` to update the stock
> 
> **1 mark** for passing `Item.GetStock() - 3` as the parameter
> 
> **1 mark** for `Item.GetStock() * Item.GetPrice()` in the output line
> 
> Accept the stock value stored in a variable first, for example:
> 
> Accept the output line using a variable that holds the result of `Item.GetStock() * Item.GetPrice()`
> 
> Do not accept any answer that still uses `Item.Stock` or `Item.Price` directly. These attributes are `PRIVATE`
> 
> Do not accept `Item.SetStock(-3)`. This sets the stock level to minus 3, it does not reduce it by 3

> **[exam-tip]**
> A common error is to fix the left-hand side of line 02 and forget the right-hand side, giving `Item.SetStock(Item.Stock - 3)`. Every use of a `PRIVATE` attribute outside the class is a problem, including the ones that only read it.
> 
> Also check the new value, not just the method name. `SetStock()` replaces the stored value with its parameter, so the parameter must be the new stock level, not the change.

### Q24
- Memory is allocated for a new object (instance) of the class `FuelPump` **[1]**
- The constructor `NEW` of the class `FuelPump` is called, and the values `3` and `"Diesel"` are passed to it as parameters **[1]**
- The constructor assigns these values to the attributes of the new object, `Pump3` **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - Memory is allocated for a new object / instance of `FuelPump`
> - The constructor / `NEW` procedure of `FuelPump` is called / executed
> - `3` and `"Diesel"` are passed to the constructor as parameters / arguments
> - The constructor assigns these values to the attributes of the new object // sets the initial values of the object's attributes
> - The new object can then be referred to using the identifier `Pump3`
> 
> **[3 marks]**
> 
> Do not accept "the class `FuelPump` is created / defined". The class already exists; this statement creates an object from it
> 
> Do not accept "`Pump3` inherits from `FuelPump`". Inheritance is a relationship between classes, not between an object and its class

> **[exam-tip]**
> Many students answer this by describing the class: its attributes and methods. That earns nothing, because the class was defined before this line ran. Describe the sequence of events for this one statement: memory for the object, the constructor runs, the values are passed in and stored in the attributes.
> 
> Use the actual values from the stem. "The values are passed in" is weaker than "`3` and `"Diesel"` are passed to the constructor".

### Q25
Procedure header with one `INTEGER` parameter, and `ENDPROCEDURE` **[1]**

Checking that the new rating is from 1 to 5, including both 1 and 5 **[1]**

Assigning the parameter to `Rating` only when the check is passed **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for a `PROCEDURE` header named `SetRating` with one parameter of type `INTEGER`, and `ENDPROCEDURE`
> 
> **1 mark** for a condition that accepts 1 to 5 inclusive and rejects every other value
> 
> **1 mark** for assigning the parameter to `Rating` inside the selection statement only
> 
> Accept the condition written with `> 0` and `< 6`, joined by `AND`
> 
> Accept the parameter passed `BYVAL`
> 
> Do not accept `OR` in place of `AND`. The condition is then true for every value
> 
> Do not award the third mark if `Rating` is assigned before the check or outside the `IF`

> **[exam-tip]**
> Test your condition with the boundary values 1 and 5, and with 0 and 6. The words "from 1 to 5 inclusive" mean that 1 and 5 are both valid, so the comparisons must include them.
> 
> A setter changes the private attribute; it does not need to return anything. Write it as a `PROCEDURE`, and assign to the attribute itself, not to a new local variable.

### Q26
Line 03 **[1]**

`TestMark` is declared `PRIVATE`, so it can only be accessed by the class's own methods. Line 03 tries to access it directly from outside the class **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for line 03
> 
> **1 mark** for `TestMark` is `PRIVATE` // hidden, so it can only be accessed using the class's own methods // cannot be accessed from outside the class
> 
> Do not accept line 02 or line 04. Both use `PUBLIC` methods of the class, which is allowed
> 
> Do not accept "line 03 has a syntax error" without the reason. The mark is for linking the error to the `PRIVATE` attribute

> **[exam-tip]**
> Some students pick line 02 because it changes the mark. Changing an attribute is allowed, as long as it happens through a method of the class. Line 02 calls the `PUBLIC` method `SetTestMark()`, so encapsulation is kept. Line 03 reaches past the methods and uses the attribute itself.
> 
> Check the keyword in front of each member. If neither `PUBLIC` nor `PRIVATE` is shown, assume the member is public.

### Q27
Function header with no parameters and `RETURNS REAL` **[1]**

Returning the value of `Reading`, and `ENDFUNCTION` **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for a `FUNCTION` header named `GetReading()` with `RETURNS REAL`
> 
> **1 mark** for `RETURN Reading` and `ENDFUNCTION`
> 
> Accept the header without `PUBLIC`. Methods are public unless stated otherwise
> 
> Do not accept `OUTPUT Reading` in place of `RETURN Reading`. That displays the value but does not give it back to the calling code
> 
> Do not accept a `PROCEDURE`, or `RETURNS INTEGER`

> **[exam-tip]**
> The most common mistake is to write `OUTPUT Reading`. A getter does not print anything. It hands the value back to the code that called it, so it must use `RETURN`.
> 
> Check that the `RETURNS` data type matches the attribute. `Reading` is `REAL`, so the getter returns `REAL`.

### Q28
| Method | Type of method | Reason from the code |
|---|---|---|
| NEW | **constructor** | It is the procedure named `NEW`. It sets the starting values of all three attributes when an `Account` object is created |
| GetBalance | **getter** | It only returns the value of the attribute `Balance`. It does not change any attribute |
| SetOwnerName | **setter** | It updates the attribute `OwnerName` with the value passed in the parameter `NewName` |
| Withdraw | **none of these** | It returns `TRUE` or `FALSE`, not the value of an attribute, and it changes `Balance` by subtracting the amount |

One mark for each correct row, with both the type and a reason **[4]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for `NEW`: constructor, because it is named `NEW` // it sets the initial values of the attributes // it is used when an object is created
> 
> **1 mark** for `GetBalance`: getter, because it returns the value of the attribute / property `Balance` (and changes nothing)
> 
> **1 mark** for `SetOwnerName`: setter, because it updates / assigns a new value to the attribute / property `OwnerName` from its parameter
> 
> **1 mark** for `Withdraw`: none of these, because it returns a `BOOLEAN` result rather than an attribute's value // because it changes `Balance` by calculation rather than assigning a value passed in
> 
> The type alone, with no reason, does not score
> 
> Accept for `Withdraw`: "a method that acts on / updates the attributes", provided it is not called a getter or a setter
> 
> Do not accept "getter" for `Withdraw` because "it is a function that returns a value". A getter returns the value of an attribute; `Withdraw` returns a success flag and also changes `Balance`
> 
> Do not accept "setter" for `NEW` because "it sets the attributes". The method that sets the attributes when the object is created is the constructor

> **[exam-tip]**
> Do not decide the type from the header alone. Many students call every `FUNCTION` a getter and every `PROCEDURE` a setter. Read the body. A getter only returns an attribute. A setter only stores a new value from its parameter in an attribute.
> 
> `Withdraw` is the method most students get wrong. It returns a value and it changes an attribute, so it does both jobs at once and is neither a getter nor a setter.

### Q29
`Game12` is an **instance** of the class `Match`. **[1]**

The process of creating `Game12` from the class `Match` is called **instantiation**. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for instance
> 
> Accept object
> 
> **1 mark** for instantiation
> 
> Accept instantiating // creating an instance (of the class)
> 
> Do not accept constructor for the second mark. The constructor is the method that runs during instantiation; it is not the name of the process
> 
> Do not accept inheritance for either mark. Inheritance is a relationship between two classes, not between a class and one of its objects

> **[exam-tip]**
> Read the statement from right to left. The name after `NEW` is the class, which already exists. The identifier on the left of the arrow, `Game12`, is the new object.
> 
> A common slip is to write "constructor" in the second gap. The constructor is the procedure `NEW` inside the class. Instantiation is the whole process of making the object, and calling the constructor is one step of it.

### Q30
If `LastReading` is made `PUBLIC`, it is no longer hidden inside the class, so encapsulation is broken **[1]**

Any code outside the class could then access `LastReading` directly, and change its value, without using the class's own methods **[1]**

Instead, `LastReading` should stay `PRIVATE` and a `PUBLIC` getter, for example `GetLastReading()`, should be added to the class. The outside code calls this method to return the value, so the attribute is still only accessed through the class's own methods **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - The attribute would no longer be hidden // encapsulation would be broken
> - Code outside the class could access // change `LastReading` directly, not through the class's methods
> - Keep `LastReading` as `PRIVATE` and add a getter // a method that returns the value of `LastReading`
> - The getter only returns the value, so outside code can read `LastReading` but cannot change it directly
> 
> **[3 marks]**
> 
> Accept any sensible getter name, for example `GetReading()`
> 
> Do not accept "add a setter" as the change needed. A setter updates a value, it does not return it

> **[exam-tip]**
> Students often write "it makes the data less secure" and stop. That is too vague for a mark. Say exactly what goes wrong: code outside the class could access and change the attribute without going through the class's methods.
> 
> The second part needs a getter, not a setter. A getter returns the value of an attribute; a setter updates it. Mixing these two up is the most common way to lose the last mark.

### Q31
`GetPrice()` is the getter and `SetPrice()` is the setter **[1]**

The getter returns the value of the attribute `Price` to the code that called it, so it must be a function that returns a `REAL` value **[1]**

The setter updates the value of `Price` using the value passed in the parameter `NewPrice`. It does not need to return a value, so it is a procedure **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for identifying `GetPrice()` as the getter and `SetPrice()` as the setter (both needed)
> 
> **1 mark** for the getter returns / fetches the value of the attribute / property, so it is a function
> 
> **1 mark** for the setter updates / changes the value of the attribute / property and does not return a value, so it is a procedure
> 
> Accept for the third mark: the setter is given the new value as a parameter and only assigns it
> 
> Do not accept "`SetPrice()` sets up the `Ticket` object". Creating the object is the job of the constructor, not the setter
> 
> Do not accept "a function is used because it has brackets". Both methods have brackets

> **[exam-tip]**
> A common error is to say that a setter "returns the new price". It returns nothing. It only changes the attribute, which is why it is a `PROCEDURE`.
> 
> Look at the header for evidence. `RETURNS REAL` shows that the method gives a value back. The `RETURNS` type of a getter matches the data type of the attribute it returns.

### Q32
A method is a procedure or a function that is defined inside a class **[1]**

It carries out an action (a behaviour) of the object by using or changing the object's attributes, for example adding to `SeatsBooked` when a seat is booked **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - A procedure / function / subroutine / programmed instructions...
> - ...that is defined in / belongs to a class
> - ...that implements a behaviour of the object // an action the object can perform
> - ...that acts on / uses / updates the attributes / properties of the object
> 
> **[2 marks]**
> 
> Do not accept "a variable or data item stored in the class". That describes an attribute (property), not a method

> **[exam-tip]**
> Many students mix up methods and attributes. An attribute is data the object stores, such as `SeatsBooked`. A method is code the object runs, such as a procedure that books a seat.
> 
> "A method is a way of doing something" earns no marks. Say that it is a procedure or a function, and say that it belongs to a class.

### Q33
- Class header `CLASS Room` and `ENDCLASS` **[1]**
- Five attributes declared `PRIVATE` **[1]**
- Correct data types for all five attributes **[1]**
- Constructor header `PUBLIC PROCEDURE NEW` with three parameters and their data types, closed with `ENDPROCEDURE` **[1]**
- Room number, room type and nightly rate assigned from the parameters **[1]**
- Occupied set to `FALSE` and guest name set to an empty string **[1]**

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for `CLASS Room` and `ENDCLASS`
> 
> **1 mark** for five attributes, each declared `PRIVATE`
> 
> **1 mark** for correct data types: number `INTEGER`, type `STRING`, rate `REAL`, occupied `BOOLEAN`, guest name `STRING`
> 
> **1 mark** for the constructor header, a `PROCEDURE` named `NEW` with three parameters and their data types, and `ENDPROCEDURE`
> 
> **1 mark** for three assignments from the parameters to the matching attributes. The identifiers on the left must match the attribute declarations
> 
> **1 mark** for occupied set to `FALSE` and guest name set to `""`
> 
> Accept `STRING` for the room number
> 
> Accept the constructor without the keyword `PUBLIC`, because the Pseudocode Guide assumes methods are public unless stated
> 
> Do not accept `REAL` for the room number or `INTEGER` for the nightly rate
> 
> Do not accept a parameter with the same identifier as its attribute, for example `RoomNumber ← RoomNumber`, because the assignment does not show which value is stored where
> 
> Do not accept `Occupied ← "FALSE"` or `Occupied ← 0`

> **[exam-tip]**
> The last mark is the one most often lost. Students assign the three parameters and stop, leaving the occupied flag and the guest name with no value. Read the question for every attribute the constructor must set, not only the ones passed in as parameters.
> 
> Give each parameter a different identifier from its attribute. Cambridge's own examples use names such as `GivenName` for the parameter and `Name` for the attribute, so the assignment `Name ← GivenName` is clear.

### Q34
The attributes `TicketID` and `Price` and the methods `NEW()` and `GetPrice()` are put together inside one class, as a single unit **[1]**

The attributes are declared `PRIVATE`, so they are hidden and cannot be accessed directly by code outside the class **[1]**

The methods are declared `PUBLIC`, so the attributes can only be accessed through the class's own methods. For example, other code must call `GetPrice()` to find the price of a ticket **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for attributes and methods put together in the class // as a single unit
> 
> **1 mark** for the attributes are `PRIVATE` so they are hidden // cannot be accessed from outside the class
> 
> **1 mark** for the attributes can only be accessed using the class's own (`PUBLIC`) methods, for example `GetPrice()` // `NEW()`
> 
> Accept properties or data for attributes
> 
> Do not accept "the attributes are secure" on its own. The answer must say they are hidden, or that they cannot be accessed from outside the class

> **[exam-tip]**
> The command word is explain, and the question says "in the class `Ticket`". Point to the code: name the `PRIVATE` attributes and name a `PUBLIC` method that gives access to them. A general definition of encapsulation that never mentions this class usually earns only one mark.

### Q35
Line 05: `PUBLIC PROCEDURE NEW(Code : STRING, ParcelWeight : REAL)` **[1]**

Line 07: `Weight ← ParcelWeight` **[1]**

Line 08: `Delivered ← FALSE` **[1]**

Line 09: `ENDPROCEDURE` **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each correct line number with its corrected line, max 4
> 
> **1 mark** for line 05: the constructor must be named `NEW`
> 
> **1 mark** for line 07: the parameter must be assigned to the declared attribute `Weight`
> 
> **1 mark** for line 08: `FALSE` is a Boolean value and must not be in quotation marks
> 
> **1 mark** for line 09: the constructor is a procedure, so it closes with `ENDPROCEDURE`
> 
> A line number on its own, with no correction, does not earn the mark
> 
> Do not accept declaring a new attribute for `ParcelMass` as the correction for line 07. The class would then hold two weight attributes and `Weight` would never be given a value

> **[exam-tip]**
> Line 07 is the error students most often miss, because the line looks correct on its own. Always check that every identifier on the left of an assignment in the constructor matches an attribute declared at the top of the class.
> 
> On line 08, `"FALSE"` is a string of five characters, not a Boolean value. The attribute `Delivered` is declared as `BOOLEAN`, so it must be given `TRUE` or `FALSE` without quotation marks.

### Q36
Encapsulation is putting the attributes (properties) and the methods together inside a class, as a single unit, so that the values of the attributes are hidden inside the class **[1]**

The keyword is `PRIVATE` **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for either of:
> 
> - Putting properties / attributes / data and methods inside a class // together as a single unit
> - Ensuring data is hidden by keeping the values of the attributes inside the class
> 
> **1 mark** for `PRIVATE`
> 
> Accept the keyword in lower case
> 
> Do not accept `PUBLIC`: a `PUBLIC` attribute can be accessed by code outside the class
> 
> Do not accept "a blueprint or template for creating objects" for the first mark. That describes a class, not encapsulation

> **[exam-tip]**
> Many students define encapsulation as "a class is a template for objects". That is the definition of a class, and it scores nothing here. Your answer must mention the attributes and methods being kept together, or the data being hidden inside the class.

### Q37
A: `WeatherStation` and D: `ENDCLASS` **[1]**

B: `NEW` and C: `ENDPROCEDURE` **[1]**

The completed class is:

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for A `WeatherStation` and D `ENDCLASS`
> 
> **1 mark** for B `NEW` and C `ENDPROCEDURE`
> 
> Accept `New` for B
> 
> Do not accept `WeatherStation` for B. In 9618 pseudocode the constructor is always a procedure named `NEW`, not a procedure named after the class
> 
> Do not accept `ENDFUNCTION` for C, because the constructor was opened as a `PROCEDURE`

> **[exam-tip]**
> Students who program in Java often write the class name in gap B, because a Java constructor has the same name as its class. The Cambridge pseudocode rule is different: constructors are procedures with the name `NEW`, whatever the class is called.
> 
> Check that every opening keyword has its matching closing keyword, in the right order. The constructor closes with `ENDPROCEDURE` inside the class, and only then does `ENDCLASS` close the class.

### Q38
| Screening |
|---|
| `FilmTitle : STRING`<br>`ScreenNumber : INTEGER`<br>`ScreeningDate : DATE`<br>`TicketPrice : REAL`<br>`SeatsAvailable : INTEGER` |
| `Constructor()`<br>`GetSeatsAvailable()`<br>`SetTicketPrice(NewPrice : REAL)`<br>`SellTickets(NumberSold : INTEGER)` |

- Three attributes with sensible identifiers and correct data types **[1]**
- All five attributes with correct data types **[1]**
- A constructor **[1]**
- A getter for the seats available and a setter for the ticket price, with a `REAL` parameter **[1]**
- A method to reduce the seats available, with an `INTEGER` parameter for the number sold **[1]**

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for three attributes with sensible identifiers and correct data types
> 
> **1 mark** for all five attributes with correct data types: title `STRING`, screen number `INTEGER`, date `DATE`, price `REAL`, seats available `INTEGER`
> 
> **1 mark** for a constructor, for example `Constructor()` or `NEW()`
> 
> **1 mark** for a getter that returns the seats available and a setter that changes the ticket price, the setter having a parameter of data type `REAL`
> 
> **1 mark** for a method to reduce the seats available, with a parameter of data type `INTEGER` for the number of tickets sold
> 
> Accept any sensible identifiers. Accept `STRING` for the screen number
> 
> Accept the parameters of the constructor listed in full, for example `Constructor(Title : STRING, Screen : INTEGER, ...)`
> 
> Do not accept `INTEGER` for the ticket price, because the price can have a fractional part (7.50)
> 
> Do not accept data types that are not 9618 pseudocode types, such as `float`, `int` or `Currency`

> **[exam-tip]**
> Read the example values in the question before you choose a data type. A price of 7.50 has a fractional part, so it must be `REAL`. The most common lost mark here is `TicketPrice : INTEGER`.
> 
> Check every method that changes an attribute. A setter needs a parameter to receive the new value, so `SetTicketPrice()` with empty brackets does not show where the new price comes from. A getter only returns a value, so it does not need one.

### Q39
The class `Book` is defined only once, but 3000 objects are created from it. **[1]**

The class is the template, and each object is an instance of the class `Book`, with its own values for the attributes, for example its own title. **[1]**

No memory is allocated when the class is defined, but memory is allocated to each of the 3000 objects when it is created. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - The class is defined once, but many (3000) objects are created from it
> - The class is a template / blueprint // each object is an instance of the class
> - Each object holds its own values for the attributes that the class defines
> - The class is defined, but each object is declared / created / instantiated (using the constructor)
> - Memory is not allocated when the class is defined, but each object is allocated memory when it is created
> - The objects can be manipulated / changed by the program (for example when a book is borrowed), but the class cannot
> 
> **[3 marks]**
> 
> Each point must relate the class to the objects. A definition of "class" and a separate definition of "object" with no link between them scores a maximum of 1 mark

> **[exam-tip]**
> The command word is explain, and the question asks for a relationship. Students often write one line defining a class and one line defining an object, and stop. Each point needs both sides: what is true of the class, and what is true of the objects.
> 
> The memory point is the one most students miss. The class itself takes no memory for attribute values; each of the 3000 objects does.

### Q40
A class is a template (blueprint) from which objects are created. **[1]**

It defines the attributes (with their data types) and the methods that each object of the class will have. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for a template / blueprint from which objects are created // objects are instances of the class
> 
> **1 mark** for it contains / defines the attributes (properties) and the methods
> 
> Accept "properties" or "data items" for attributes, and "procedures and functions" for methods
> 
> Do not accept "a class is an object" or "a class is a group of objects". A class is the definition; the objects are made from it

> **[exam-tip]**
> Many students write that a class "is an object". It is not. The class is written once, as a definition, and the program then creates as many objects from it as it needs.
> 
> A class is sometimes compared with a record, because both group data items together. The difference is that a class also contains methods, so name the methods in your answer, not only the data.

### Q41
**One **mark per mark point (Max 3)

MP1 Attributes/properties …

MP2 … with their data types // … are variables bound to the class

MP3 Methods …

MP4 … that are subroutines / functions / procedures that act upon the attributes

MP5 Getters/setters …

MP6 … are methods that can fetch / update the contents of attributes

MP7 A constructor …

MP8 … that is used to create instances / objects of this class.
One mark per mark point (Max 3)

MP1 A class is only defined once but many objects can be created from that class // A class is a template / blueprint from  which objects are created // An object is an instance of a class

MP2 No memory is allocated when a class is defined, but objects are allocated memory space whenever they are created

MP3 A class cannot be manipulated as it is not available in the memory, but objects can be manipulated

MP4 A class is defined but an object is declared / created / instantiated.

MP5 A class can use inheritance. An object cannot.

### Q42
> **[mark-scheme]**
> To ensure that the attributes are only accessible using the class’s own methods/within the class.
**One **mark per mark point (Max 5)

MP1 Two correct attributes with sensible names and correct data types.

MP2 Constructor present.

MP3 Two correct setters with exact names and appropriate parameters and data types.

MP4 Two correct getters with appropriate names.

MP5 Name assigned to pet name getter matches the attribute.

| Pet |   |
|---|---|
| `PetID` | `: STRING` |
| `PetType` | `: STRING` |
| `OwnerTelephone` | `: STRING` |
| `DateRegistered` | `: DATE` |
| `PetName` | `: STRING` |
| `OwnerName` | `: STRING` |
| `Constructor()`<br><br>`SetPetID(APetID : STRING)`<br><br>`SetDateRegistered(RegDate : DATE)`<br><br>`GetPetName()`<br><br>`GetOwnerTelephone()` |   |
