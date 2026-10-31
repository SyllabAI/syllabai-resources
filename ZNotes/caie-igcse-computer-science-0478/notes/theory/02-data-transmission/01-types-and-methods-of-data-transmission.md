# Data Transmission

## Types and Methods of Data Transmission

### **Data Packets**

* Packet Structure -
  * Header
    * Contains the IP address of the sender and the receiver
    * The sequence number of the packet
    * Size of the packet
    * Contains sequence number of packet 
  * Payload
    * Contains the actual data
  * Trailer
    * Includes a method of identifying the end of the packet
    * Error-Checking methods
* Packet Switching - Method of data transmission where the data is broken into multiple packets. Packets are then sent independently from start to end and reassembled at the receiver’s computer.


|Advantages|Disadvantages|
|:---|:---|
|There is no need to create a single line of communication|Packets may be lost|
|Possible to overcome failed or busy nodes|More prone to errors in real-time streaming|
|High data transmission speed|Delay at the receiver while the packets are being re-ordered|
|Easy to expand package usage||

### **Data Transmission**

* *Simplex data transmission* is in one direction only.
  * Examples: Broadcast television, broadcast radio. They are broadcasted from the tower to the receiver and not returned.
* Half-duplex data transmission is in both directions but not at the same time (e.g., walkie-talkie)
* *Full-duplex data transmission* is in both directions simultaneously (e.g. broadband connection on the phone line)
* *Serial data transmission* is when data is sent one bit at a time over a single wire
* *Parallel data transmission* is when data of several bits (1 byte) are sent down several wires at the same time.

### **Comparison of Serial and Parallel Data Transmission**


|Serial|Parallel|
|:---|:---|
|Better for longer distances (Telephone Lines)|Better for short distances (Internal circuits)|
|Cheaper Option|Expensive (More hardware required)|
|Used when the size of data transmitted is small|Used when speed is necessary|
|Easier to synchronise as there's only one data stream.|Difficult to synchronise due to skew between bits.|
