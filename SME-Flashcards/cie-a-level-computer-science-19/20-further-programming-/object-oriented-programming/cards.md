# Object-Oriented Programming

Course: cie-a-level-computer-science-19 · Section: 20. Further Programming

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/20-further-programming-/object-oriented-programming/


## Card 1 — keyword_definition (`fl_7wyQJ6P7ChBSDM8t`)

**FRONT**

Define **class**.


**BACK**

A class is a **blueprint used to create objects**, defining a structure for attributes (data) and methods (behaviour).


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 2 — keyword_definition (`fl_Zjr8Kp95yK6JS7gP`)

**FRONT**

Define **object**.


**BACK**

An object is an **instance of a class** with its own state and behaviour.


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 3 — keyword_definition (`fl_SZMW7KgvSwkTPRDD`)

**FRONT**

Define **attribute**.


**BACK**

An attribute is a **variable defined in a class**, also called a class variable.


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 4 — keyword_definition (`fl_ZTGyvdNR9rv8tKJ7`)

**FRONT**

Define **instance variable**.


**BACK**

An instance variable is an attribute **stored inside an individual object**.


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 5 — keyword_definition (`fl_DW83kkg9bCzzDCPt`)

**FRONT**

Define **method**.


**BACK**

A method is a **function defined within a class** that describes an object's behaviour.


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 6 — keyword_definition (`fl_9tjnMhsykgFnkhxg`)

**FRONT**

Define **instantiation**.


**BACK**

Instantiation is the process of **creating an object from a class**.


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 7 — keyword_definition (`fl_7MhTcGCQWfJTkDc5`)

**FRONT**

Define **identifier**.


**BACK**

An identifier is the **name used to refer to an object**.


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 8 — fill_in_the_blanks (`fl_rgqvMrWdKnsB8Vph`)

**FRONT**

A class defines a structure for <u>**                **</u>, which hold the data, and methods, which define the behaviour.


**BACK**

A class defines a structure for **attributes**, which hold the data, and methods, which define the behaviour.


*Blanks: 1 — answers: []*

Spec links: `spcpt_NRYKc3qkB8XSKVKf`

Flags: blank_answer_mismatch


## Card 9 — question_and_answer (`fl_dJrzfqdpjxJCktWW`)

**FRONT**

What is the difference between a prebuilt class and a custom class?


**BACK**

A prebuilt class is **provided by the language**, such as `String` or `Scanner` in Java, while a custom class is **defined by the programmer**, such as `Animal` or `Student`.


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 10 — question_and_answer (`fl_nCJGZXBDkJ52CnCF`)

**FRONT**

Give two examples of prebuilt Java classes.


**BACK**

Two prebuilt Java classes are `**String**` and `**Date**`, and `Random` and `Scanner` are also prebuilt.


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 11 — true_or_false (`fl_ZWx66cFNdPTpSHZ4`)

**FRONT**

**True or False?**

Every object created from the same class must hold the same attribute values.


**BACK**

**False.**

Each object created from a class has **its own unique values** for the attributes, so two `Student` objects can hold different names and dates of birth.


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 12 — question_and_answer (`fl_NMMyp5m3JRXJ8vMm`)

**FRONT**

State three attributes a `Student` class might contain.


**BACK**

A `Student` class might contain the attributes `**name**`, `**dateOfBirth**` and `**gender**`.


Spec links: `spcpt_NRYKc3qkB8XSKVKf`


## Card 13 — keyword_definition (`fl_gqmf92MwHd36nMvd`)

**FRONT**

Define **constructor**.


**BACK**

A constructor is the method **used to create the objects of a class**, setting the initial values of the attributes.


Spec links: `spcpt_SKCx699zkYg5wKhS`


## Card 14 — question_and_answer (`fl_JC4qFdnJv2MhDDqs`)

**FRONT**

A `Cars` class is written for a car sales program. State the five attributes it needs.


**BACK**

The five attributes are the **manufacturer**, **model**, **price**, **mileage** and **whether the car is preowned**.


Spec links: `spcpt_SKCx699zkYg5wKhS`


## Card 15 — question_and_answer (`fl_yZHC94QfFrBRQS9d`)

**FRONT**

Which data type would the `PreOwned` attribute of a `Cars` class use, and why?


**BACK**

It would use a **Boolean**, because a car either is or is not preowned.


Spec links: `spcpt_SKCx699zkYg5wKhS`


## Card 16 — question_and_answer (`fl_h4VB5StF4tvHyJkQ`)

**FRONT**

Name two methods that would be useful for a car object.


**BACK**

`**Accelerate**`, to make the car go faster, and `**honkHorn**`, to sound the horn.


Spec links: `spcpt_SKCx699zkYg5wKhS`


## Card 17 — fill_in_the_blanks (`fl_PYnpDZPJS2P8R3TT`)

**FRONT**

When a class is written so that its attributes cannot be accessed from outside it, those attributes are declared as <u>**                **</u>.


**BACK**

When a class is written so that its attributes cannot be accessed from outside it, those attributes are declared as **private**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_SKCx699zkYg5wKhS`

Flags: blank_answer_mismatch


## Card 18 — question_and_answer (`fl_XVySYm7zWCmKKkxG`)

**FRONT**

A `Vehicle` class has the attributes `ID`, `MaxSpeed`, `CurrentSpeed`, `IncreaseAmount` and `HorizontalPosition`. Which of these should the constructor set to 0 rather than take as a parameter?


**BACK**

`**CurrentSpeed**` and `**HorizontalPosition**` are set to 0, because a vehicle starts stationary at the origin, while `ID`, `MaxSpeed` and `IncreaseAmount` are passed in as parameters.


Spec links: `spcpt_SKCx699zkYg5wKhS`


## Card 19 — true_or_false (`fl_9yj52xRNhBDpMDD8`)

**FRONT**

**True or False?**

In Python, attribute declarations for a class are written as comments when answering an exam question.


**BACK**

**True.**

Python has no separate attribute declaration, so the exam requires the declarations to be **included as comments**, for example `#self.``<u>  </u>``MaxSpeed integer`.


Spec links: `spcpt_SKCx699zkYg5wKhS`


## Card 20 — question_and_answer (`fl_cyNvcGzytxKgM5dp`)

**FRONT**

What is the purpose of the `IncreaseAmount` attribute in the `Vehicle` class?


**BACK**

`IncreaseAmount` is the value **added to the current speed** each time the vehicle increases its speed.


Spec links: `spcpt_SKCx699zkYg5wKhS`


## Card 21 — keyword_definition (`fl_KNYp9WbgXJt2jbh7`)

**FRONT**

Define **object**.


**BACK**

An object is a **representation of a real-world entity**, such as a teacher, an aeroplane or a mobile phone.


Spec links: `spcpt_vbxKPQbQygRpCNDr`


## Card 22 — question_and_answer (`fl_PMqGMyD6jsrkNVbk`)

**FRONT**

What is the difference between a class and an object?


**BACK**

A class is a **blueprint that describes the properties and behaviours** of objects, while an object is a **specific instance created from that blueprint**, with its own unique values for the properties.


Spec links: `spcpt_vbxKPQbQygRpCNDr`


## Card 23 — keyword_definition (`fl_spJ2MSChdynNfzpk`)

**FRONT**

Define **constructor**.


**BACK**

A constructor is a **special method within a class that is automatically called when an object of that class is created**.


Spec links: `spcpt_vbxKPQbQygRpCNDr`


## Card 24 — question_and_answer (`fl_tbgpN3bGCkxg6CxK`)

**FRONT**

What do constructors typically define?


**BACK**

Constructors typically define the **initial values of the instance variables**.


Spec links: `spcpt_vbxKPQbQygRpCNDr`


## Card 25 — fill_in_the_blanks (`fl_CS6PsRJMpKZPm3kt`)

**FRONT**

As well as setting initial values, a constructor performs any necessary <u>**                **</u> to prepare the object for use.


**BACK**

As well as setting initial values, a constructor performs any necessary **setup** to prepare the object for use.


*Blanks: 1 — answers: []*

Spec links: `spcpt_vbxKPQbQygRpCNDr`

Flags: blank_answer_mismatch


## Card 26 — question_and_answer (`fl_GbsbYGgQ2XqrZrch`)

**FRONT**

Give three examples of real-world entities that could be modelled as objects.


**BACK**

A **teacher**, an **aeroplane** and a **mobile phone** could all be modelled as objects.


Spec links: `spcpt_vbxKPQbQygRpCNDr`


## Card 27 — true_or_false (`fl_3tSK7g4X4KcGn72q`)

**FRONT**

**True or False?**

Two objects created from the same class always share one set of property values.


**BACK**

**False.**

Each object is a separate instance with **its own unique values** for the properties.


Spec links: `spcpt_vbxKPQbQygRpCNDr`


## Card 28 — question_and_answer (`fl_tcCKXkj4CfMqjgDj`)

**FRONT**

In the `Person` class example, name the four attributes.


**BACK**

The four attributes are `**firstName**`, `**surname**`, `**dateOfBirth**` and `**hobbies**`.


Spec links: `spcpt_PMGDvYWx2Pj6bswW`


## Card 29 — fill_in_the_blanks (`fl_TnZr74RtW6XHmV6K`)

**FRONT**

In Java, an object is created from a class using the <u>**                **</u> keyword.


**BACK**

In Java, an object is created from a class using the **new** keyword.


*Blanks: 1 — answers: []*

Spec links: `spcpt_PMGDvYWx2Pj6bswW`

Flags: blank_answer_mismatch


## Card 30 — question_and_answer (`fl_2CQD65MrTPbG296s`)

**FRONT**

How many objects are instantiated in the `Person` example, and what are their identifiers?


**BACK**

**Two** objects are instantiated, with the identifiers `**person1**` and `**person2**`.


Spec links: `spcpt_PMGDvYWx2Pj6bswW`


## Card 31 — question_and_answer (`fl_BJg9JQzphJRMfV9k`)

**FRONT**

What values are passed in when `person1` is created?


**BACK**

`person1` is created with **"Bob"**, **"Jones"**, **"06/10/1981"** and **"E Sports"**.


Spec links: `spcpt_PMGDvYWx2Pj6bswW`


## Card 32 — question_and_answer (`fl_QXcc5nZ62VcR5NRq`)

**FRONT**

In Python, which method acts as the constructor for a class?


**BACK**

The `<u>**  **</u>``**init**``<u>**  **</u>` method acts as the constructor in Python.


Spec links: `spcpt_PMGDvYWx2Pj6bswW`


## Card 33 — true_or_false (`fl_MWPC3sjXJPVBT29Z`)

**FRONT**

**True or False?**

In the Java `Person` example, all four attributes are declared as private.


**BACK**

**True.**

Each attribute is declared with the `**private**` access modifier, so it cannot be accessed directly from outside the class.


Spec links: `spcpt_PMGDvYWx2Pj6bswW`


## Card 34 — question_and_answer (`fl_cjGvVt2MHdBPQXNb`)

**FRONT**

In Python, how does the constructor assign a parameter to an attribute of the object?


**BACK**

It uses the `**self**` keyword, for example `self.firstName = firstName`.


Spec links: `spcpt_PMGDvYWx2Pj6bswW`


## Card 35 — keyword_definition (`fl_5w739dBN75rJKkhS`)

**FRONT**

Define **method**.


**BACK**

A method is a **function associated with an object or class** that defines the behaviour and actions the object can perform.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 36 — question_and_answer (`fl_tr42cG6hqbrGn6ww`)

**FRONT**

What are the two main types of method?


**BACK**

The two main types of method are a **function** and a **procedure**.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 37 — question_and_answer (`fl_nBZ3bMgzcdsYcMw9`)

**FRONT**

What is the difference between a function and a procedure?


**BACK**

A function performs a task and **returns a value**, while a procedure performs a task but **does not return a value**.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 38 — true_or_false (`fl_CNYTb7PRC6XvcQpB`)

**FRONT**

**True or False?**

A procedure returns a value to the code that called it.


**BACK**

**False.**

A procedure performs a task but **does not return a value**, which is what distinguishes it from a function.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 39 — fill_in_the_blanks (`fl_k4xpsY9bSThVkFDV`)

**FRONT**

Because they are associated with objects rather than the class itself, these methods are called <u>**                **</u> methods.


**BACK**

Because they are associated with objects rather than the class itself, these methods are called **instance** methods.


*Blanks: 1 — answers: []*

Spec links: `spcpt_nxt9SD2gf3Z5xGsn`

Flags: blank_answer_mismatch


## Card 40 — question_and_answer (`fl_3WQY2WNJR6JSCxNw`)

**FRONT**

What notation does an object use to call a method from its class?


**BACK**

It uses **dot notation**, in the form `Objectname.Methodname`.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 41 — question_and_answer (`fl_2NRsRKQpvhPbR3Rb`)

**FRONT**

An object `jumboJet` has been created from the `aircraft` class. Write the statement that calls its take off method.


**BACK**

The statement is `**jumboJet.Takeoff()**`.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 42 — question_and_answer (`fl_wtvfxKg2PPKdCrXW`)

**FRONT**

Name the four methods of the `aircraft` class.


**BACK**

The four methods are **take off**, **land**, **bank left** and **bank right**.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 43 — question_and_answer (`fl_sv6kMbrVYSCMrvK8`)

**FRONT**

Name the four attributes held by each object of the `aircraft` class.


**BACK**

Each object holds a **manufacturer**, a **model**, a **passenger capacity** and a **maximum speed**.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 44 — question_and_answer (`fl_jppSjCKcxWdBfQzB`)

**FRONT**

Why is a class a good way to model aircraft, given that aircraft differ so much in design?


**BACK**

Although the designs differ, every aircraft **requires the same methods**, such as take off and landing, so one class can define that shared behaviour.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 45 — keyword_definition (`fl_tc6s8RVs39qbcGVC`)

**FRONT**

Define **public method**.


**BACK**

A public method is **accessible and can be invoked by any code within the same class or from any external class**.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 46 — keyword_definition (`fl_Ws3BH5zBTh7gqHQ2`)

**FRONT**

Define **private method**.


**BACK**

A private method is **only accessible within the same class** and cannot be invoked by external code or other classes.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 47 — true_or_false (`fl_TyH6ScbmCm8gG4f4`)

**FRONT**

**True or False?**

A private method can be invoked by code in a different class.


**BACK**

**False.**

A private method can only be called from **within its own class**.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 48 — question_and_answer (`fl_86yCBqQVZHSV4kBg`)

**FRONT**

Why must changes to public methods be made carefully?


**BACK**

Changes to public methods **may affect other parts of the codebase**, so they should be carefully designed, documented and kept backward compatible wherever possible.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 49 — question_and_answer (`fl_4DrD54N6JCc2BHwf`)

**FRONT**

Why is a private method easier to modify or refactor than a public one?


**BACK**

A private method has a **localised impact**, because it is only used internally within its own class.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 50 — question_and_answer (`fl_WVNgc8cfFwBz6Q33`)

**FRONT**

When would you make a method public?


**BACK**

When you want to **provide other parts of the program with access** to a particular functionality or behaviour of the object or class.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 51 — question_and_answer (`fl_cqtVhSm4dGykncFS`)

**FRONT**

When would you make a method private?


**BACK**

When it holds **internal implementation details** that should not be accessed or used by external code.


Spec links: `spcpt_nxt9SD2gf3Z5xGsn`


## Card 52 — fill_in_the_blanks (`fl_PdMNmnbMk7tCNS2d`)

**FRONT**

In Python, a method whose name begins with a single leading <u>**                **</u> is treated as private by convention.


**BACK**

In Python, a method whose name begins with a single leading **underscore** is treated as private by convention.


*Blanks: 1 — answers: []*

Spec links: `spcpt_Cv3J4Pp483HfxyS7`

Flags: blank_answer_mismatch


## Card 53 — question_and_answer (`fl_R8bQFzp3xzf6zMVv`)

**FRONT**

Does Python enforce private methods in the way Java does?


**BACK**

**No.** Python has **no explicit access modifier**, so a method marked as private can still be accessed from outside the class, but other developers should treat it as private and avoid doing so.


Spec links: `spcpt_Cv3J4Pp483HfxyS7`


## Card 54 — question_and_answer (`fl_bssVmKnqV5tRyKtc`)

**FRONT**

What does the statement `jumboJet = new aircraft("Boeing", "747", 416, 547)` do?


**BACK**

It **creates an object called **`**jumboJet**`** from the **`**aircraft**`** class**, giving it a manufacturer of Boeing, a model of 747, a capacity of 416 and a speed of 547.


Spec links: `spcpt_Cv3J4Pp483HfxyS7`


## Card 55 — keyword_definition (`fl_9tVstZHy64yZ95z6`)

**FRONT**

Define **attribute**.


**BACK**

An attribute is a **data member, or property, associated with an object or a class**.


Spec links: `spcpt_QWTDqxYwBJvHtwdr`


## Card 56 — question_and_answer (`fl_HCPjNpFhqYxGQFsV`)

**FRONT**

What do the attributes of a class define?


**BACK**

The attributes define the **state of an object**.


Spec links: `spcpt_QWTDqxYwBJvHtwdr`


## Card 57 — true_or_false (`fl_szXvn9c8d4gRfGrg`)

**FRONT**

**True or False?**

Every instance of a class must hold the same values for its attributes.


**BACK**

**False.**

Attributes can hold **different values for different instances** of the same class.


Spec links: `spcpt_QWTDqxYwBJvHtwdr`


## Card 58 — question_and_answer (`fl_mjbPsr6d5Wx64svR`)

**FRONT**

What data types can an attribute be?


**BACK**

An attribute can be any data type, including **integers**, **strings**, **Booleans** or even **other objects**.


Spec links: `spcpt_QWTDqxYwBJvHtwdr`


## Card 59 — fill_in_the_blanks (`fl_Jk34YSkKSR8D5YHk`)

**FRONT**

As well as a data type, attributes can be given different <u>**                **</u> rights.


**BACK**

As well as a data type, attributes can be given different **access** rights.


*Blanks: 1 — answers: []*

Spec links: `spcpt_QWTDqxYwBJvHtwdr`

Flags: blank_answer_mismatch


## Card 60 — question_and_answer (`fl_tGZKp5N53PHfQjVr`)

**FRONT**

A `Car` class has an attribute called `manufacturer` with private access and a String data type. What do those two things mean?


**BACK**

Private access means it **can only be accessed within the **`**Car**`** class**, and the String data type means the value it holds **must be text**.


Spec links: `spcpt_QWTDqxYwBJvHtwdr`


## Card 61 — question_and_answer (`fl_Jsw2fkHBZwk5QjRQ`)

**FRONT**

An object of the `Car` class is instantiated with the value "Ford". Which attribute holds that value?


**BACK**

The `**manufacturer**` attribute holds the value "Ford".


Spec links: `spcpt_QWTDqxYwBJvHtwdr`


## Card 62 — question_and_answer (`fl_PWTgCFSKYCXT3VWh`)

**FRONT**

How many attributes does a class usually have?


**BACK**

In most cases a class has **many different attributes**, so a single-attribute class is unusual.


Spec links: `spcpt_QWTDqxYwBJvHtwdr`


## Card 63 — question_and_answer (`fl_R5sbdzfrYJRMP43G`)

**FRONT**

Name the five attributes of the Java `Person` class.


**BACK**

The five attributes are `**name**`, `**age**`, `**gender**`, `**occupation**` and `**isMarried**`.


Spec links: `spcpt_9Mk8TpVF2qDYpJrn`


## Card 64 — question_and_answer (`fl_4Knf99BKZkwjqsXj`)

**FRONT**

In the Java `Person` class, which attribute is declared as a boolean, and which as an int?


**BACK**

`**isMarried**` is declared as a boolean and `**age**` is declared as an int.


Spec links: `spcpt_9Mk8TpVF2qDYpJrn`


## Card 65 — fill_in_the_blanks (`fl_WNTbvhVFvfWTH887`)

**FRONT**

In Python, attributes are defined using the <u>**                **</u> keyword, followed by the attribute name and its initial value.


**BACK**

In Python, attributes are defined using the **self** keyword, followed by the attribute name and its initial value.


*Blanks: 1 — answers: []*

Spec links: `spcpt_9Mk8TpVF2qDYpJrn`

Flags: blank_answer_mismatch


## Card 66 — true_or_false (`fl_kpTR93BPDRMSX5Fw`)

**FRONT**

**True or False?**

In the Java `Person` class, the attributes are declared as private.


**BACK**

**True.**

All five attributes are declared with the `**private**` access modifier.


Spec links: `spcpt_9Mk8TpVF2qDYpJrn`


## Card 67 — keyword_definition (`fl_4Yr7Nj3XfQsjPyxS`)

**FRONT**

Define **inheritance**.


**BACK**

Inheritance allows a class to **inherit the properties and behaviours, that is the attributes and methods, of another class**.


Spec links: `spcpt_DZTVTnD8468FWpMj`


## Card 68 — question_and_answer (`fl_w7DscZZWMt8Pw2XY`)

**FRONT**

How does inheritance promote code reuse?


**BACK**

A derived class can **inherit and use the existing code from the base class**, which avoids duplicating code and improves organisation and maintainability.


Spec links: `spcpt_DZTVTnD8468FWpMj`


## Card 69 — fill_in_the_blanks (`fl_TqG6bGwYZFbQZqZx`)

**FRONT**

Inheritance establishes an <u>**                **</u> relationship between the base class and the derived class.


**BACK**

Inheritance establishes an **IS-A** relationship between the base class and the derived class.


*Blanks: 1 — answers: []*

Spec links: `spcpt_DZTVTnD8468FWpMj`

Flags: blank_answer_mismatch


## Card 70 — question_and_answer (`fl_Z5wp7QtbzF5rcgSG`)

**FRONT**

A `Car` class is derived from a `Vehicle` class. State the IS-A relationship between them.


**BACK**

**A Car is a Vehicle**, so the `Car` class inherits the properties and behaviours associated with being a vehicle.


Spec links: `spcpt_DZTVTnD8468FWpMj`


## Card 71 — question_and_answer (`fl_wDGqqkgGhCHqVRcz`)

**FRONT**

Give two other names for the base class.


**BACK**

The base class is also known as the **parent class** or the **superclass**.


Spec links: `spcpt_DZTVTnD8468FWpMj`


## Card 72 — question_and_answer (`fl_V8N28gknkMMqhssK`)

**FRONT**

Give two other names for the derived class.


**BACK**

The derived class is also known as the **child class** or the **subclass**.


Spec links: `spcpt_DZTVTnD8468FWpMj`


## Card 73 — question_and_answer (`fl_mTBWvf3JV2YZQR26`)

**FRONT**

What is the role of the base class in an inheritance hierarchy?


**BACK**

The base class is the **blueprint or template from which the derived class inherits**, defining the common properties and behaviours shared among multiple derived classes.


Spec links: `spcpt_DZTVTnD8468FWpMj`


## Card 74 — true_or_false (`fl_XkS2TCJR8yhfRqrJ`)

**FRONT**

**True or False?**

A derived class can only use what it inherits, and cannot add anything of its own.


**BACK**

**False.**

A derived class inherits the attributes and methods of the base class, but it can also **add additional attributes and methods** of its own.


Spec links: `spcpt_DZTVTnD8468FWpMj`


## Card 75 — question_and_answer (`fl_s9FBSWNj6CJkkRgZ`)

**FRONT**

A `Car` class inherits from `Vehicle`. Name two attributes the `Car` class adds for itself.


**BACK**

The `Car` class adds `**IsInsured**`, which records whether the car is insured, and `**EngineCapacity**`, which records the size of the engine.


Spec links: `spcpt_DZTVTnD8468FWpMj`


## Card 76 — question_and_answer (`fl_2JjB6fPfKKjjHrrQ`)

**FRONT**

Name three methods a `Vehicle` base class might define.


**BACK**

`**TurnEngineOn()**`, `**TurnEngineOff()**` and `**SteerLeft()**` are all methods a `Vehicle` base class might define.


Spec links: `spcpt_DZTVTnD8468FWpMj`


## Card 77 — keyword_definition (`fl_Z8k7rbWZCV83qq2t`)

**FRONT**

Define the **super keyword**.


**BACK**

The super keyword is used within a subclass to **refer to the superclass and access its methods, attributes or constructors**.


Spec links: `spcpt_DZTVTnD8468FWpMj`


## Card 78 — fill_in_the_blanks (`fl_vZYCSJvrwbGSWf9N`)

**FRONT**

In Java, a derived class inherits from a base class using the keyword <u>**                **</u>.


**BACK**

In Java, a derived class inherits from a base class using the keyword **extends**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_XRj64GWyhZFKdc87`

Flags: blank_answer_mismatch


## Card 79 — question_and_answer (`fl_s9Dgrwkdchfnfx2T`)

**FRONT**

In Python, how does a class show that it inherits from another class?


**BACK**

The **parent class name is written in brackets after the child class name**, for example `class Car(Vehicle):`.


Spec links: `spcpt_XRj64GWyhZFKdc87`


## Card 80 — question_and_answer (`fl_tqy5WrtyJNMwMxFD`)

**FRONT**

Why does the constructor of a derived class call the constructor of its base class?


**BACK**

So that the **attributes belonging to the base class are initialised**, before the derived class sets its own additional attributes.


Spec links: `spcpt_XRj64GWyhZFKdc87`


## Card 81 — question_and_answer (`fl_T8JVZzH7nvsnbWPt`)

**FRONT**

A `Helicopter` class inherits from `Vehicle` and adds `VerticalPosition`, `VerticalChange` and `MaxHeight`. Which of these does the constructor set to 0?


**BACK**

`**VerticalPosition**` is initialised to 0, while `VerticalChange` and `MaxHeight` are set from the parameters passed in.


Spec links: `spcpt_XRj64GWyhZFKdc87`


## Card 82 — question_and_answer (`fl_jvG4vXCWtB2qhBnX`)

**FRONT**

The `Helicopter` constructor takes five parameters. Which three are passed straight up to the `Vehicle` constructor?


**BACK**

The **ID**, the **maximum speed** and the **increase amount** are passed up to the `Vehicle` constructor, because they belong to the parent class.


Spec links: `spcpt_XRj64GWyhZFKdc87`


## Card 83 — true_or_false (`fl_48qvQhQqMYd5Ch6J`)

**FRONT**

**True or False?**

The attributes a derived class declares for itself should be private.


**BACK**

**True.**

The `Helicopter` class declares `VerticalPosition`, `VerticalChange` and `MaxHeight` as **private**, in the same way the parent class declares its own attributes.


Spec links: `spcpt_XRj64GWyhZFKdc87`


## Card 84 — keyword_definition (`fl_CRMsnY8wd2GR74tH`)

**FRONT**

Define **encapsulation**.


**BACK**

Encapsulation is the practice of **grouping data (attributes) and methods (functions) together within a class**.


Spec links: `spcpt_PZ6sxctzBrrGQRFT`


## Card 85 — question_and_answer (`fl_zv9kwmnDFfYPjNh9`)

**FRONT**

How does encapsulation keep data secure?


**BACK**

It **controls access to the data using access modifiers** such as public and private, so the data cannot be accidentally modified or misused.


Spec links: `spcpt_PZ6sxctzBrrGQRFT`


## Card 86 — question_and_answer (`fl_HtcXbF823N6sXNmG`)

**FRONT**

State two benefits of encapsulation other than security.


**BACK**

It **organises code by keeping related data and methods together**, and it **promotes code reusability**, so the same class can be used in different parts of a program without rewriting it.


Spec links: `spcpt_PZ6sxctzBrrGQRFT`


## Card 87 — fill_in_the_blanks (`fl_Sn996Ybbm8Yvbm4p`)

**FRONT**

Encapsulation uses a concept called <u>**                **</u>, which reduces complexity by hiding the implementation details of the object.


**BACK**

Encapsulation uses a concept called **abstraction**, which reduces complexity by hiding the implementation details of the object.


*Blanks: 1 — answers: []*

Spec links: `spcpt_PZ6sxctzBrrGQRFT`

Flags: blank_answer_mismatch


## Card 88 — question_and_answer (`fl_djB5F8zNKNcbxmk9`)

**FRONT**

Why does hiding the internal details of a class help other programmers?


**BACK**

They can **use the methods and classes without having to understand how they have been constructed internally**.


Spec links: `spcpt_PZ6sxctzBrrGQRFT`


## Card 89 — true_or_false (`fl_hxz9NX3HkTC9CXzx`)

**FRONT**

**True or False?**

External code can access a private variable of a class directly.


**BACK**

**False.**

Private variables are **only accessible within the class itself**, and external code must interact with the class through its public methods.


Spec links: `spcpt_PZ6sxctzBrrGQRFT`


## Card 90 — keyword_definition (`fl_yNHnGH24fmm9pYGv`)

**FRONT**

Define **get method**.


**BACK**

A get method is used to **retrieve the value of an object's private attribute**, and is also known as a getter or accessor method.


Spec links: `spcpt_7FZjfQ7P4Tn8D2dq`


## Card 91 — keyword_definition (`fl_R8256Vmf9W5f7vTq`)

**FRONT**

Define **set method**.


**BACK**

A set method is used to **set the value of an object's private instance variable**, and is also known as a mutator method.


Spec links: `spcpt_7FZjfQ7P4Tn8D2dq`


## Card 92 — question_and_answer (`fl_bJvSGHV2jRb9r7DD`)

**FRONT**

What is the main purpose of a get method?


**BACK**

To provide **controlled access to the internal state of an object without allowing direct modification**.


Spec links: `spcpt_7FZjfQ7P4Tn8D2dq`


## Card 93 — question_and_answer (`fl_BXjT22w55xB6RDMb`)

**FRONT**

Why is extra code often written inside a set method?


**BACK**

To **enforce conditions or validations** before the attribute is updated, so that access is controlled.


Spec links: `spcpt_7FZjfQ7P4Tn8D2dq`


## Card 94 — question_and_answer (`fl_6cZZTRZw3pb4JZdm`)

**FRONT**

A `NumberUpdater` class has a private attribute `oldnumber` and a set method that rejects negative values. What happens if the method is passed -3?


**BACK**

`**oldnumber**`** is left unchanged**, because the method only updates the attribute when the new value is not less than zero.


Spec links: `spcpt_7FZjfQ7P4Tn8D2dq`


## Card 95 — fill_in_the_blanks (`fl_G4ZFbVGKNmSmTSdd`)

**FRONT**

Because attributes are declared private, external code must use the public <u>**                **</u> methods to read their values.


**BACK**

Because attributes are declared private, external code must use the public **get** methods to read their values.


*Blanks: 1 — answers: []*

Spec links: `spcpt_7FZjfQ7P4Tn8D2dq`

Flags: blank_answer_mismatch


## Card 96 — question_and_answer (`fl_ZGWXmPQGZySmS6TS`)

**FRONT**

How many parameters does a get method take, and what does it do with the attribute?


**BACK**

A get method takes **no parameters** and **returns the attribute without overwriting it**.


Spec links: `spcpt_7FZjfQ7P4Tn8D2dq`


## Card 97 — question_and_answer (`fl_6fMGkBKQfVcWFn5P`)

**FRONT**

The `Vehicle` class stores `CurrentSpeed` privately. Write, in words, what `GetCurrentSpeed()` must do.


**BACK**

It must **return the value held in the **`**CurrentSpeed**`** attribute**, taking no parameters and making no change to it.


Spec links: `spcpt_7FZjfQ7P4Tn8D2dq`


## Card 98 — true_or_false (`fl_FRYP4x7TgQk7g8s3`)

**FRONT**

**True or False?**

A set method returns the value of the attribute to the code that called it.


**BACK**

**False.**

A set method **updates** the attribute, while it is the get method that **returns** its value.


Spec links: `spcpt_7FZjfQ7P4Tn8D2dq`


## Card 99 — keyword_definition (`fl_K56QTxfYZ6xbpSyF`)

**FRONT**

Define **polymorphism**.


**BACK**

Polymorphism allows objects to **take on different forms or behaviours**, so different objects can share the same method name but work in different ways.


Spec links: `spcpt_nb6Kj8kq5CKfyjHF`


## Card 100 — question_and_answer (`fl_twW9rZJT96msbm4F`)

**FRONT**

State two benefits of using polymorphism.


**BACK**

Polymorphism makes code more **flexible** and more **reusable**, which also makes it easier to maintain.


Spec links: `spcpt_nb6Kj8kq5CKfyjHF`


## Card 101 — question_and_answer (`fl_YSdh2fQwYnXfCzgG`)

**FRONT**

How does polymorphism make a program more versatile?


**BACK**

Objects can be **treated as belonging to a common group even when they belong to different classes**, so the code adapts more easily to change.


Spec links: `spcpt_nb6Kj8kq5CKfyjHF`


## Card 102 — fill_in_the_blanks (`fl_VVPXJ3wdQRv4D3Kg`)

**FRONT**

The <u>**                **</u> keyword is used to provide a new implementation for a method that is already defined in the parent class.


**BACK**

The **override** keyword is used to provide a new implementation for a method that is already defined in the parent class.


*Blanks: 1 — answers: []*

Spec links: `spcpt_nb6Kj8kq5CKfyjHF`

Flags: blank_answer_mismatch


## Card 103 — question_and_answer (`fl_HFDpBxHmdt3Jkvr2`)

**FRONT**

A `Motorcycle` class and a `Car` class both inherit from `Vehicle` and neither redefines `startEngines()`. What is output when either object calls it?


**BACK**

Both output **"Engines Started!"**, because they inherit the same method from the base class.


Spec links: `spcpt_nb6Kj8kq5CKfyjHF`


## Card 104 — question_and_answer (`fl_8nM4wwxMdxD6Svqp`)

**FRONT**

A `Motorcycle` object calls `displayInfo()`, which is defined in both `Vehicle` and `Motorcycle`. What is output, and why?


**BACK**

**"I am a Motorcycle!"** is output, because the version in the object's own class **overrides** the `Vehicle` class method.


Spec links: `spcpt_nb6Kj8kq5CKfyjHF`


## Card 105 — question_and_answer (`fl_M7HVmdBvJKYfdnw8`)

**FRONT**

What does the declaration `Vehicle vehicle1 = new Car()` allow a programmer to do?


**BACK**

It allows an **array of type **`**Vehicle**`** to store both **`**Car**`** and **`**Motorcycle**`** objects**, rather than keeping them in separate data structures.


Spec links: `spcpt_nb6Kj8kq5CKfyjHF`


## Card 106 — question_and_answer (`fl_YQ5kcgMwgdydpXTy`)

**FRONT**

`vehicle1` is declared as type `Vehicle` but created as a `Car`. What does `vehicle1.displayInfo()` output?


**BACK**

It still outputs **"I am a Car!"**, because the version that runs depends on the object actually created, not the declared type.


Spec links: `spcpt_nb6Kj8kq5CKfyjHF`


## Card 107 — keyword_definition (`fl_TbG9Gw399JkTwXZq`)

**FRONT**

Define **run-time polymorphism**.


**BACK**

Run-time polymorphism happens when a subclass **overrides a method defined in a superclass, and the correct version is chosen at run-time rather than compile-time**.


Spec links: `spcpt_rk33CCQF8Gst9pyS`


## Card 108 — question_and_answer (`fl_vSQsjMKgmcPJMv8V`)

**FRONT**

In the `Animal`, `Dog` and `Cat` example, what does the `speak()` method in the `Animal` superclass contain?


**BACK**

It is **empty**, acting only as a placeholder for the subclasses to override.


Spec links: `spcpt_rk33CCQF8Gst9pyS`


## Card 109 — question_and_answer (`fl_4dyFRXYfXvfCK2xr`)

**FRONT**

`myDog` and `myCat` are passed in turn to `make_sound()`. What is output each time?


**BACK**

`make_sound(myDog)` outputs **Woof** and `make_sound(myCat)` outputs **Meow**.


Spec links: `spcpt_rk33CCQF8Gst9pyS`


## Card 110 — true_or_false (`fl_GXppH9bpgGgc4SDW`)

**FRONT**

**True or False?**

A separate version of `make_sound()` has to be written for each type of animal.


**BACK**

**False.**

One `make_sound()` accepts an object of type `Animal` and **calls the correct version of **`**speak()**` for whichever subclass was passed to it.


Spec links: `spcpt_rk33CCQF8Gst9pyS`


## Card 111 — fill_in_the_blanks (`fl_CWRy8Rj7KqdQzP6Y`)

**FRONT**

In run-time polymorphism the method call is resolved based on the actual <u>**                **</u> of the object.


**BACK**

In run-time polymorphism the method call is resolved based on the actual **type** of the object.


*Blanks: 1 — answers: []*

Spec links: `spcpt_rk33CCQF8Gst9pyS`

Flags: blank_answer_mismatch


## Card 112 — question_and_answer (`fl_HrkH77Q3cWtZGRhb`)

**FRONT**

In Java, what marks a method as overriding one in its superclass?


**BACK**

The `**@Override**` annotation is written above the method header.


Spec links: `spcpt_rk33CCQF8Gst9pyS`


## Card 113 — question_and_answer (`fl_Rx59qSnfJj5y3BpH`)

**FRONT**

The `Helicopter` class overrides `IncreaseSpeed()` from `Vehicle`. State the three things the overriding method must do.


**BACK**

It **adds the vertical change to the vertical position**, **adds **`**IncreaseAmount**`** to the current speed**, and **adds the updated current speed to the horizontal position**.


Spec links: `spcpt_rk33CCQF8Gst9pyS`


## Card 114 — question_and_answer (`fl_kydzhgJJwXZwKzhv`)

**FRONT**

What two limits must the `Helicopter` version of `IncreaseSpeed()` enforce?


**BACK**

The vertical position **cannot exceed the maximum height**, and the current speed **cannot exceed the maximum speed**.


Spec links: `spcpt_rk33CCQF8Gst9pyS`


## Card 115 — true_or_false (`fl_PV2NR3qrWHvtkd2J`)

**FRONT**

**True or False?**

The `Helicopter` version of `IncreaseSpeed()` takes no parameters.


**BACK**

**True.**

An overriding method keeps the **same header as the method it overrides**, and `IncreaseSpeed()` has no parameters.


Spec links: `spcpt_rk33CCQF8Gst9pyS`

