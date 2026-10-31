# Data Representation

## Data Types

**Integer:**

* Positive or negative number; no fractional part
* Held in pure binary for processing and storage
* Some languages differentiate short/long integers (more bytes used to
  store long integers)

**Real:**

* Number that contains a decimal point
* Referred to as singles and doubles depending upon the number of bytes used to store

**Character:**

* A character is any letter, number, punctuation or space
* Takes up a single unit of storage (usually a byte).

**String:**

* Combination of alphanumeric characters enclosed in “ ”
* Each character is stored in one byte using ASCII code
* Each character is stored in two bytes using Unicode
* The maximum length of a string is limited by available memory.
* Incorrect to store dates or numbers as strings
* Phone no. must be stored as a string; otherwise, the initial 0 is lost

**Boolean:**

* It can store one of only two values; “True” or “False.”
* Stored in 1 byte: True = 11111111, False = 00000000

**Date:**

* Dates are stored as a ‘serial’ number
* Equates to the number of seconds elapsed since 1st January 1970 00:00:00 UTC, excluding leap seconds.
* Usually takes 8 bytes of storage
* Displayed as dd/mm/yyyy or mm/dd/yyyy

**Array:**

* Data structure consisting of a collection of elements
* Identified by at least one array index (or key)

**File:**

* An object that stores data, information, settings or commands
* Can be opened, saved, deleted & moved
* Transferrable across network connections



