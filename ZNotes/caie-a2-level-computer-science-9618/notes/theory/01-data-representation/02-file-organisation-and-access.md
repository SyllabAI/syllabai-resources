## File Organization

### Serial

In serial files, records are stored one after another in chronological order. Records are appended to the next available spot.

* **Benefits:**

  * No need to sort the list.

  * Data can be appended easily.

### Sequential

In sequential files, records are stored one after another in the order of the key field. Records are inserted into the correct position. A new version of the file has to be created to update it.

* **Benefits:**

  * Allows for batch processing.

  * Allows the data to be stored and sorted in a specific order.

### Random

* In random files, records are stored in no particular order. Changes to the file are done directly. In random file organization, a unique key field is passed through a hash algorithm which produces the home location for the data. If that location is empty, the data is stored; otherwise, it relies on an overflow method to resolve the collision.

* A **collision** occurs when two different records produce the same hash value, meaning that the target location is already being used to store a different record.

* To handle collisions, random file organization uses one of two main hashing algorithms:

  * Open Hashing (Separate Chaining)

  * Mechanism: The records are not restricted to the primary positions available within the main file array. Instead, each slot (bucket) in the file contains a pointer to a separate, dynamically allocated linked list.

  * Handling Collisions: When a collision occurs, the new record is simply appended to the end of the linked list branching off from that specific home location. The record is stored outside the fixed limits of the main file array.

  * Finding a Record: The key is passed through the hash algorithm to locate the home bucket. The system then reads sequentially down the linked list attached to that bucket until the matching record is found.

  * Benefits: The file can handle an infinite number of collisions without ever running out of physical table slots, and deletions are cleaner because you only have to adjust linked list pointers.

  * Closed Hashing (Open Addressing)

    * Mechanism: All records must be stored directly inside the fixed boundaries of the main file structure itself. No external structures or auxiliary linked lists are allowed.

    * Handling Collisions: When saving a file, the algorithm searches for an alternative, empty slot (an open address) within the same file array using a specific mathematical probing routine:

      * Linear Probing: The system searches the file linearly ($+1, +2, +3...$) for the very next empty spot and saves the record there.

      * Quadratic Probing: The system searches intervals expanding quadratically ($+1^2, +2^2, +3^2...$) to find an empty spot and prevent data clustering.

    * Finding a Record: When finding a record, the system checks the home location. If it does not match, it starts from that current location and searches the array or the designated overflow area linearly step-by-step until the matching record is found or a completely empty slot is hit (signaling the record does not exist).

    * Benefits: Highly memory efficient since no extra pointer space or dynamic memory allocations are needed. It is fast as real-time processing is used.

## File Access

### Sequential Access

In sequential access, records are read in the exact order that they are stored in. It is read record by record until the target record is found or the key field value is exceeded.

* **Usage:** This is used for both **serial** and **sequential** file organization.

#### Direct / Random Access

In random access, you can directly access the specific data needed without reading the preceding records.

* **Usage:** This is used in both **sequential** and **random** file organization.

* **Implementation:** In sequential file organization, an index of all the key fields is used to jump to the data, while a hashing algorithm (using either open or closed hashing rules) is used in random file organization.