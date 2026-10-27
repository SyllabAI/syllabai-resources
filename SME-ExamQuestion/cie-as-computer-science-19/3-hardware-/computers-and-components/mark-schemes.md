# Mark Schemes — Computers & Components
**3. Hardware** · Cambridge (CIE) AS computer-science (9618)


## Exam Questions (16 questions)


### Q1
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**).
> 
> - Static RAM has faster access time
> - …because it does not need to be refreshed
> - …used on the CPU for improvement of CPU cache speed
> - Static RAM has lower
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - EEPROM allows frequent / multiple read / write / erase operations
> - …which means that the contents of the firmware in the headset can be changed easily
> - …without fully erasing the contents of the firmware in the headset first
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 4**)
> 
> - The print instructions and data are sent by the laptop to a buffer (at laptop speed)
> - The data is transferred from the buffer to the printer (at printer speed)
> - …allowing user to continue using the laptop // and allowing processor to continue processing
> - …instead of waiting for relatively slower printer
> - When the buffer is empty an interrupt is sent to the laptop
> - …requesting more data

### Q2
> **[mark-scheme]**
> **1 mark **for each bullet point (**max 3**).
> 
> - Disk needs to be prepared for initial use
> - Disk needs to be checked for errors
> - A new file system needs to be generated on the disk
> - The file allocation table needs to be set up

### Q3
> **[mark-scheme]**
> **1 mark **for each component (**max 3**)
> 
> Buffers
> 
> - A buffer temporarily holds data until it is ready to be transmitted **to the device**
> 
> Address Bus
> 
> - The address of the **data to be written to** **the device** (in RAM) is carried on the address bus
> 
> Data Bus
> 
> - All data to be **written to the device / buffer** is carried on the data bus

### Q4
> **[mark-scheme]**
> **1 mark** for:
> 
> - infra-red / proximity (sensor)
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - Actuator generates a signal / causes an action / converts electrical energy into a mechanical force
> - ... to push an arm // to open a trap door // to pick up the chocolate bar with the incorrect weight
> **[mark-scheme]**
> (i) **1 mark** for each feature (**max 2**)
> 
> - Dedicated to a single task // limited number of functions
> - Built into a larger system // integrated into a larger system
> - An embedded system must contain a processor, memory and an I/O capability // Dedicated hardware
> 
> (ii) **1 mark** for each bullet point (**max 1**)
> 
> - Difficult to change / update the firmware by the user // Difficult to upgrade devices to take advantage of new technology
> - Cannot be easily **adapted **for task
> - Troubleshooting faults/upgrading is a specialist task
> - Devices are often thrown away rather than repaired as difficult to upgrade or repair

### Q5
> **[mark-scheme]**
> **One mark** for each bullet point (**max 2**)
> 
> - Feedback ensures that a system operates within set criteria / constraints
> - ...by enabling system output to affect (subsequent) system input
> - ...thus allowing conditions to be <u>automatically </u>adjusted
> **[mark-scheme]**
> **One mark** for each reason to **max 3 **to match the example given
> 
> • Dedicated to one task **applied to example**
> • Does not require much processing power **applied to example**
> • Built into a larger system **applied to example**
> • Contains firmware that cannot be easily updated **applied to example**
> • The system does not have its own operating system
> • An embedded system must contain a processor, memory and an I/O capability // Dedicated hardware

### Q6
**1 mark **for each bullet point (**max 3**)

Generic mark points:

- Additive manufacturing
- Uses a digital 3D model or a Computer-Aided Design (CAD) file
- Builds up the model one layer at a time
- ...starting from the bottom
- ...using x, y, and z coordinates
- The material is fused or cured together layer by layer

Specific mark points:

**Fused Deposition Modelling (FDM)**

- Material is heated and pushed through nozzle / extruder

**Stereolithography (SLA) **

- Photosensitive liquid resin is exposed to a UV-laser beam

**Digital Light Processing (DLP) **

- Uses liquid plastic resin melted with arc lamps

**Selective Laser Sintering (SLS) **

- Uses a laser to form objects from powdered material
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - To prevent overheating // ensure material is hot enough
> - ...by identifying the temperature of the object (being printed)
> - ...by identifying the temperature of the material being used
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - Dynamic RAM has lower cost per unit
> - A fast access speed is not needed
> - Higher bit density // more data can be stored per chip

### Q7
> **[mark-scheme]**
> **1 mark **for each bullet point (**max 2**)
> 
> - Immediate Access Store holds all the data / instructions / programs currently in use
> - Immediate Access Store is volatile memory
> - Immediate Access Store has fast access times

### Q8
**1 mark** for sensor and matching purpose to **max 2**:

| Sensor | Purpose of sensor in navigation system |
|---|---|
| Pressure | To detect if a table or other obstacle has been hit // to detect when food is put on/taken off the tray so it can move on |
| Infra-red | To detect if there is an obstacle in the way // to indicate that it has reached the desired table |
| Sound | To detect if someone is speaking so that it can use AI to decipher the speech and whether the robot is required to stop |
> **[mark-scheme]**
> **1 mark **each to **max 2**:
> 
> - Feedback ensures that a system operates within set criteria / constraints
> - ... by enabling system output to affect subsequent system input
> - ... thus allowing conditions to be automatically adjusted
> **[mark-scheme]**
> **1 mark** each to **max 4**:
> 
> - Resistive: The space between the conductive layers is removed/the layers touch and a circuit is completed
> - Capacitive: The electrical charge changes where the user pressed
> - The point of contact is identified
> - ... from the change in electrical field
> - The software/microprocessor **calculates **the coordinates

### Q9
> **[mark-scheme]**
> **1 mark** for each correctly completed statement:
> 
> - (LCD) displays/screens/lenses
> - gyroscope/accelerometer
> - direction/speed
> - digital cameras
> 
> A headset can have one or **two (LCD) displays/screens/lenses** that output the image to the user. The headset has speakers that output surround sound to give a realistic experience. The user's head movements are detected using a sensor. This sensor is a **gyroscope/accelerometer**. The data is transmitted to a microprocessor that analyses the data to identify the **direction/speed** of movement. Some headsets use **digital cameras** that record the user's eye movements for analysis.
**1 mark **each to **max 3**:

- The buffer is used as a **temporary **store for data going to the headset
- Data is **transferred **into the buffer by the computer
- Data is **retrieved **from the buffer by the headset
- When the buffer is empty or full, an interrupt is sent to the computer requesting more data or stopping further data being sent
- When the headset has enough data or needs more data, an interrupt is sent by the headset to the computer to stop sending data from the buffer
**1 mark** each to **max 3**:

- EEPROM allows** frequent or multiple** read, write, and erase operations
- … so the headset can take advantage of new features
- … without fully erasing the contents of the firmware in the headset first // can erase a particular byte or the whole EEPROM
- … without removing the chip(s) or firmware from the headset
- … the contents of the firmware in the headset can be changed by the user without technical expertise
- Cheaper to manufacture, so the headset will be cheaper to purchase

### Q10
> **[mark-scheme]**
> **1 mark** each to **max 2**:
> 
> - The doorbell only performs the specific tasks of motion detection/video recording/doorbell ringing
> - The motion sensor and digital camera are built into the doorbell
> - The CPU/memory/storage/software are all dedicated to this task only
> - Only a dedicated microprocessor is required due to the limited processing requirements
> **[mark-scheme]**
> No mark for identification of monitoring or control **1 mark** each to **max 2** for justification:
> 
> Monitoring:
> 
> - The turning on of the digital camera does not affect the input to the sensor/button
> - The transmission of the data/video does not affect the input to the sensor/button
> - The ringing of the doorbell does not affect the input to the button
> 
> Control:
> 
> - Video doorbell does not only store the values from the motion sensor
> - The data is processed, generating a signal to start the digital camera recording
> - Button pressed/motion detected causes a signal to be sent over a network to the smartphone
> **[mark-scheme]**
> (i)** 1 mark** each to **max 2**:
> 
> - Current reading or data from motion sensor
> - Current or recent video
> - Instructions being executed
> - Start-up, BIOS, or boot-up instructions
> 
> (ii)** 1 mark** for each row:
> 
> | Statement | Answer |
> |---|---|
> | the **two **types of logic gate that can be used to create solid state devices | **NAND NOR** |
> | the number of transistors contained in each cell | **2** |
> | the type of gate that can retain electrons without power | **floating** |
> | the type of gate that allows or stops current from passing through | **control** |
> 
> (iii)** 1 mark **each to **max 2**:
> 
> - Captured video is transmitted to buffer
> - … video is transmitted from buffer to smartphone
> - Store recent data in a buffer for the user to rewind
> - … instead of storing everything in secondary storage
> - Store readings from motion sensor
> - … until the microprocessor can process them
> - Store video from digital camera
> - … before moving it to secondary storage

### Q11
**1 mark** for each bullet point (**max 3**)

- The system uses feedback
- The system acts independently
- Input data causes the car to brake
- … braking decreases or changes the distance to the object
- … this new distance is used to determine whether or how hard the car needs to brake

### Q12
> **[mark-scheme]**
> **1 mark** for each difference
> 
> e.g.
> 
> - DRAM requires constant refreshing, but SRAM does not need to be constantly refreshed
> - DRAM generally has greater capacities per chip, but SRAM generally has lower capacities per chip
> - DRAM has slower access times than SRAM
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 4**)
> 
> - The computer and the hard disk drive transmit and receive at different speeds // The computer transfers data faster than the HDD can receive
> - The buffer is used for temporary storage
> - … so that the computer can transfer data to the buffer at the higher speed
> - ... and is not held up waiting for data to transfer
> - … and so that data is transferred to the hard disk drive from the buffer at the slower rate

### Q13
> **[mark-scheme]**
> **1 mark** for sensor **and** its use in this system
> 
> - Infra-red sensor
> - Measure / check the height of the vehicle
> - Pressure sensor
> - Measure / check the weight of the vehicle
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**) for a correct justification
> 
> No marks for the identification of the system
> 
> Monitoring system
> 
> - Because there is no use of feedback // the warning sign is only an indicator
> - ... the output of the turning on of the sign does not affect the input of data from the sensors
> - The system does not have any actuators

### Q14
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 3**)
> 
> e.g.
> 
> - It is difficult to change / update the firmware by the user
> - Errors cannot be fixed easily // Troubleshooting / fault-finding / repairing is a specialist task / expensive
> - Functionality cannot be changed/extended easily // Cannot be easily adapted for another task
> - Faulty / outdated devices are often thrown away rather than repaired
> - … leading to e-waste
> **[mark-scheme]**
> **1 mark** from:
> 
> - DRAM is less expensive to manufacture/purchase than SRAM in the embedded system
> - DRAM has a higher bit density per chip // more data can be stored per chip
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - EPROM uses ultraviolet light to erase data whilst EEPROM uses an electrical signal to do this
> - EPROM has to be removed from the circuit board when changing the data whilst EEPROM remains in the circuit when the data is changed
> - EPROM erases all the data, EEPROM can erase parts of the data

### Q15
> **[mark-scheme]**
> **1 mark** for all 3 appropriate sensors
> 
> | Scenario | Type of sensor |
> |---|---|
> | A door is open. | Pressure sensor // Infra-red |
> | The external daylight level is below a set amount. | Light sensor |
> | A person is detected within 2 metres. | Infra-red |
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 3**) for a correct justification No marks for the identification of the system
> 
> **Monitoring system**
> 
> - There is no use of feedback // The light and the alarm are just warnings
> - The output of the floodlight or the audio alarm does not affect the input of data from the sensors
> - The system does not have any actuators

### Q16
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> e.g.
> 
> - DRAM requires constant refresh cycles unlike SRAM
> - DRAM has lower access speed than SRAM
> **[mark-scheme]**
> (i) **1 mark** for each bullet point (**max 4**)
> 
> - The disc is spun at high speed
> - A laser is shone onto the disc to read or write
> - … using an optical head to move it into position
> - … it follows the spiral track from the centre outwards
> - When writing, the laser burns pits to represent the data
> - When reading, the laser reflects from pits and lands
> - The reflection from a pit and a land is different
> - … the differences are interpreted as 1s or 0s
> 
> (ii)** 1 mark** for each bullet point (**max 3**)
> 
> - The computer and optical disc reader/writer send and receive at different speeds
> - A buffer allows temporary storage of the data
> - … so that the computer can transfer data to the buffer at the higher speed
> - … and is not held up waiting for data to transfer // so the computer can carry on with other tasks
> - … so the optical disc reader/writer is not overloaded
> - … and so that data is transferred to the optical disc reader/writer from the buffer at the slower rate
