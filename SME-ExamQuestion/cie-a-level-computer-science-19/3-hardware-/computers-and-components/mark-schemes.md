# Mark Schemes — Computers & Components
**3. Hardware** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (58 questions)


### Q1
The pressure sensor sends its reading to the microprocessor, which compares it with the stored limits of 3 bar and 4 bar. **[1]**

When the pressure falls below 3 bar, the microprocessor sends a signal to the actuator and the pump is switched on. **[1]**

Running the pump raises the water pressure in the pipes, so the action of the system changes the quantity that the sensor is measuring. **[1]**

The sensor's next reading is therefore higher because of the system's own action, and the microprocessor uses that new reading to switch the pump off once the pressure reaches 4 bar, keeping the pressure inside the set limits without a person acting. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the reading being sent to the microprocessor and compared with the stored limits
> 
> **1 mark** for the microprocessor signalling the actuator to switch the pump on when the pressure is below 3 bar
> 
> **1 mark** for stating that running the pump raises the pressure, so the system's own output changes the quantity the sensor measures
> 
> **1 mark** for stating that the next reading is used to switch the pump off at 4 bar, so the pressure is kept within the set limits automatically
> 
> The third and fourth marking points are the feedback marks. An answer that describes only sensor, then microprocessor, then actuator has described the input path that any system has, and has not closed the loop. Award the first two marking points only.
> 
> Accept "the output of the system affects the subsequent input" in place of the third marking point.
> 
> Accept "conditions are adjusted automatically" or "the system operates within the set criteria" in place of the fourth marking point.
> 
> Do not accept "the system sends feedback to the user" or "the pressure is shown on a display". Feedback is not information sent to a person.
> 
> Do not accept "the pump keeps running until someone switches it off". The system switches the pump off itself, using the new reading.

> **[exam-tip]**
> Most answers to this question stop at the actuator. Describing the sensor, the microprocessor and the pump earns you two marks and no more, because that chain is present in any system that acts on a reading. The feedback marks are for saying that the pump's action changes the pressure, and that the pressure is what the sensor measures next.
> 
> A quick check before you finish: does your answer contain a sentence in which the system's output changes its own next input? If not, you have not written about feedback yet.

### Q2
Without feedback the system could not use the effect of its own cooling when it made its next decision. **[1]**

The cooling unit would run for a fixed length of time, or stay on all the time, instead of stopping when the office reached 22 °C. **[1]**

The temperature of the office would move outside the required value, and the system could no longer adjust the conditions automatically. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for stating that the system would not use the change made by its own output when deciding what to do next
> 
> **1 mark** for stating that the cooling unit would run for a fixed time, or run continuously, instead of switching off at the correct point
> 
> **1 mark** for stating that the temperature would not be kept at or near the required value, so the conditions could not be adjusted automatically
> 
> Accept "the office would become too cold" or "the office would stay too warm" for the third marking point.
> 
> Accept "a person would have to switch the cooling unit off" for the third marking point.
> 
> Do not accept "the system would not work" or "the system would break". Say what changes about the temperature.
> 
> Do not accept "the sensor would stop working". Removing feedback does not stop readings being taken; it stops the system using the effect its own action has on those readings.

> **[exam-tip]**
> This question is testing feedback from the other direction, so plan your answer around the loop being broken. A system without feedback is working blind: it acts once, on a timer or on a single reading, and never checks what its action did.
> 
> Answers that only say "it would be less accurate" score nothing, because that is a judgement rather than an explanation. Say what the cooling unit does and what happens to the temperature in the room.

### Q3
When the system switches the heater on, the temperature of the water rises. **[1]**

The temperature sensor then measures this new, higher temperature, so the action taken by the system changes the value that the system reads next. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for stating that the action of the system, switching the heater on, changes the temperature of the water
> 
> **1 mark** for stating that this changed temperature is what the sensor measures next, so the output of the system affects its own next input
> 
> Accept "the output of the system affects the subsequent input" for the second marking point.
> 
> Accept "the new reading is used to decide whether the heater stays on" for the second marking point.
> 
> Do not accept "the sensor sends its reading to the microprocessor" on its own. That is the input path and it happens in a monitoring system too.
> 
> Do not accept "the system gives feedback to the user" or "the system displays a message". Feedback here is not information sent to a person.

> **[exam-tip]**
> In everyday English, feedback means telling someone how they did. In this topic it means something different, so do not write about messages, displays or reports.
> 
> A two-mark feedback answer needs both halves of the loop: what the system's action changes, and the fact that the sensor then reads that changed value. Write one sentence for each half.

### Q4
The temperature sensor measures the temperature of the liquid at regular intervals. **[1]**

Each reading is sent to the microprocessor. **[1]**

The microprocessor compares the reading with the stored limits of 4 °C and 8 °C. **[1]**

If the reading is above 8 °C, the microprocessor sends a signal to the actuator, which switches the cooling unit on. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the sensor measuring the temperature continuously or at regular intervals
> 
> **1 mark** for the reading being sent to the microprocessor
> 
> **1 mark** for the microprocessor comparing the reading with a stored value or stored range
> 
> **1 mark** for a signal being sent to the actuator to switch the cooling unit on when the reading is above the upper limit
> 
> Accept `processor`, `microcontroller` or `computer` in place of `microprocessor`.
> 
> Accept "stored preset value", "set range" or "the values programmed into the system" in place of the stored limits.
> 
> Do not accept "the sensor decides that the liquid is too warm" or "the sensor switches on the cooling unit". The sensor only supplies a value; the comparison and the decision are made by the microprocessor.
> 
> Do not accept "the reading is sent to the actuator". The reading goes to the microprocessor, and the microprocessor signals the actuator.
> 
> Do not accept "the reading is stored in a file" on its own. Storing a reading is monitoring, not deciding.

> **[exam-tip]**
> The mark that is missed most often is the comparison. Students write sensor, then microprocessor, then cooling unit, and never say what the microprocessor actually does with the number. Always include the step where the reading is compared with a value already stored in the system.
> 
> Use the limits given in the question. Writing "if it is too hot" is vague; writing "if the reading is above 8 °C" shows the examiner you know where the decision comes from.

### Q5
The infra-red sensor detects whether a person is standing in front of the doors. **[1]**

It sends this reading to the microprocessor, which compares the reading with the condition that opens the doors. **[1]**

The actuator receives a signal from the microprocessor and converts it into a mechanical movement that slides the doors open. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the sensor detecting or measuring a physical quantity, here the presence of a person in front of the doors
> 
> **1 mark** for the sensor sending the reading to the microprocessor
> 
> **1 mark** for the actuator converting the signal from the microprocessor into a physical action or movement that opens the doors
> 
> Accept `processor`, `microcontroller` or `computer` in place of `microprocessor`.
> 
> Accept "converts electrical energy into a mechanical force" or "generates a signal that causes an action" for the actuator mark.
> 
> Accept a motor named as the actuator.
> 
> Do not accept "the sensor opens the doors". A sensor only takes readings; it never carries out the action.
> 
> Do not accept "the actuator decides when the doors open". The decision is made by the microprocessor.
> 
> Do not accept "the sensor sends a signal to the actuator". The reading goes to the microprocessor first.

> **[exam-tip]**
> The commonest error here is merging the two devices into one, writing that the sensor "sees the person and opens the door". Keep them separate: the sensor supplies a value, the microprocessor makes the decision, and the actuator carries out the movement.
> 
> Notice that the question puts sensor and actuator in bold. That is the examiner telling you the answer needs both, so split your answer into a sentence about each before you start writing.

### Q6
Chip A should be a PROM. **[1]**

A PROM can be programmed once only and its contents cannot then be erased, so the serial number written during manufacture can never be changed. **[1]**

Chip B should be an EEPROM. **[1]**

An EEPROM is erased by an electrical signal while it stays in the circuit, so the firmware can be erased and rewritten many times without the receiver being opened or the chip being removed. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for identifying PROM for Chip A
> 
> **1 mark** for a justification of PROM: it can be programmed once only // its contents cannot be erased or changed afterwards
> 
> **1 mark** for identifying EEPROM for Chip B
> 
> **1 mark** for a justification of EEPROM: it allows frequent read, write and erase operations // it is erased by an electrical signal // it can be erased while it remains in the circuit, so the chip does not have to be removed // part of the contents can be erased rather than all of it
> 
> Accept, for the EEPROM justification, a comparison that rules EPROM out: an EPROM would have to be removed from the circuit board and erased with ultraviolet light, which cannot be done by an update sent over the internet
> 
> Do not accept EPROM for Chip B
> 
> Do not accept EEPROM for Chip A. An EEPROM can be rewritten, so the serial number would not be protected
> 
> Do not accept a justification that only repeats the question, for example "because it must never be changed"

> **[exam-tip]**
> Two marks here are for naming a chip and two are for saying why, so never leave the justification out. A bare answer of PROM and EEPROM scores half of the available marks.
> 
> The wording of each bullet in the question tells you which property to reach for. "Written once during manufacture" points at PROM, and "sent over the internet several times each year" points at the one type that can be erased electrically without being taken out of the device.

### Q7
| System | Type of sensor |
|---|---|
| The system checks that the air inside a greenhouse does not become too hot. | **Temperature** **[1]** |
| The system detects that a heavy crate has been placed on a loading platform. | **Pressure** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `Temperature` (sensor) in the first row
> 
> **1 mark** for `Pressure` (sensor) in the second row
> 
> Accept `weight sensor` for the second row.
> 
> Do not accept `heat sensor` for the first row. The syllabus names the device a temperature sensor.
> 
> Do not accept `infra-red` for the second row. Infra-red detects that an object is present, not how heavy it is.
> 
> Do not accept a brand name or a named component such as `thermistor` or `strain gauge`. Name the type of sensor.

> **[exam-tip]**
> Write the type of sensor and nothing else. Adding a sentence about what the sensor does costs you time and cannot earn a second mark, because the mark is for the sensor type alone.
> 
> Learn the four sensor types the syllabus names: temperature, pressure, infra-red and sound. Almost every sensor question on this paper is answered from that short list.

### Q8
| Type of ROM | How the contents can be erased |
|---|---|
| PROM | **The contents cannot be erased. A PROM is programmed once only and keeps those contents for the life of the chip.** **[1]** |
| EPROM | **The chip is removed from the circuit board and exposed to ultraviolet (UV) light, which erases all of the contents at once.** **[1]** |
| EEPROM | **An electrical signal is applied while the chip stays in the circuit, and either a single byte or the whole chip can be erased.** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for PROM: the contents cannot be erased // it can be programmed once only
> 
> **1 mark** for EPROM: erased using ultraviolet light // the whole chip is erased // the chip must be removed from the circuit board first
> 
> **1 mark** for EEPROM: erased using an electrical signal or voltage // the chip stays in the circuit // part of the contents can be erased rather than all of it
> 
> Accept UV for ultraviolet, and voltage or electrical charge for electrical signal
> 
> Accept "in situ" for staying in the circuit
> 
> Do not accept "erased by deleting the files". These chips are not erased a file at a time
> 
> Do not accept an answer for PROM that says it is erased slowly or with difficulty. A PROM cannot be erased at all

> **[exam-tip]**
> Read the row label before you write. The PROM row catches students out because they assume every type of ROM must have some way of being erased, and they invent one. Stating plainly that a PROM cannot be erased is the answer that earns the mark.
> 
> For the EPROM and EEPROM rows, name the method and the place. UV light with the chip removed for EPROM, an electrical signal with the chip left in the circuit for EEPROM.

### Q9
(i) The system only records the noise level in a log file and switches on a lamp; it does not change anything inside the production hall. **[1]**

The lamp warns the supervisor but does not reduce the noise, so the output of the system does not affect the next reading taken by the sound sensor. **[1]**

(ii) Connect the microprocessor to an actuator that acts on the source of the noise, for example one that slows the noisy machine down or closes a soundproof shutter around it. **[1]**

When a reading is above the safe limit the microprocessor sends a signal to that actuator. The action lowers the noise level, so the next reading taken by the sound sensor is changed by the system's own action and the system now uses feedback. **[1]**

**[4 marks]**

> **[mark-scheme]**
> (i)
> 
> **1 mark** for stating that the system only records or displays the readings and does not change the noise level
> 
> **1 mark** for stating that the lamp is only a warning to a person, so the output does not affect the next reading or there is no feedback
> 
> (ii)
> 
> **1 mark** for naming an actuator that acts on the source of the noise, for example slowing or stopping the machine, or closing a shutter, door or cover
> 
> **1 mark** for explaining that the action changes the noise level, so the sensor's next reading is changed by the system's own action
> 
> Accept any actuator that reduces the noise at source for the third marking point.
> 
> Do not accept a louder alarm, a message sent to a phone, a larger display or an entry written to a second log file. These warn a person; they do not change the noise level, so the system is still a monitoring system.
> 
> Do not accept "add more sound sensors" or "take readings more often". More input does not create an output that acts on the process.
> 
> Do not accept "make the supervisor switch the machine off". If a person takes the action, the system is still only monitoring.

> **[exam-tip]**
> Part (ii) is where marks are lost. Students suggest a bigger alarm or an automatic text message, because both feel like the system "doing something". Neither changes the noise level, which is the quantity the sensor is measuring, so the system stays a monitoring system.
> 
> Whatever change you suggest, check that it acts on the same quantity the sensor measures. If your new output cannot change the sensor's next reading, it is not a control system.

### Q10
A PROM can be programmed once only, whereas an EPROM can be erased and reprogrammed many times. **[1]**

The contents of a PROM cannot be erased, whereas the contents of an EPROM are erased by exposing the chip to ultraviolet (UV) light. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for PROM being programmed once only **and** EPROM being erased and reprogrammed many times
> 
> **1 mark** for the contents of a PROM not being erasable **and** the contents of an EPROM being erased using ultraviolet light
> 
> Accept UV for ultraviolet
> 
> Accept "written once" or "set once" for programmed once only
> 
> Do not accept a statement about only one of the two chips, for example "PROM can be written to once". A difference must name what each chip does
> 
> Do not accept "EPROM is erased using an electrical signal". That is EEPROM

> **[exam-tip]**
> The word difference is doing the marking here. Each mark needs both halves of the contrast in the same sentence, so use whereas or but to join them. Writing two separate facts, one about PROM and one about EPROM, in different places on the page often loses a mark.
> 
> The other frequent slip is mixing up the two erasing methods. EPROM uses ultraviolet light, EEPROM uses electricity. The extra E at the front stands for electrically, which is the clue.

### Q11
The sensors only report the temperature: the readings are stored in a log file and shown on a screen, and nothing is done to the freezing equipment. **[1]**

The system has no actuator, so it has no way of changing the temperature inside the warehouse. **[1]**

Turning on the red lamp only warns the manager. It does not change the temperature, so the output of the system does not affect the next reading that the sensor takes and there is no feedback. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - The system only stores or displays the readings and does not change the process
> - The system has no actuator, so it cannot change the temperature
> - Turning on the red lamp is only a warning to a person
> - The output of the system does not affect the next reading taken by the sensor
> - The system does not use feedback
> - A person has to take the action to correct the temperature, not the system
> 
> **[3 marks]**
> 
> Accept "the warning lamp is only an indicator" for the third bullet.
> 
> Do not accept "the system controls the temperature when it gets too warm" or "the system turns the freezer back on". Nothing in the question gives the system any means of changing the temperature.
> 
> Do not accept the red lamp offered as an actuator. A lamp that warns a person is an indicator; an actuator acts on the process being measured.
> 
> Do not accept "it is a monitoring system because it monitors the temperature". That repeats the question and earns nothing.

> **[exam-tip]**
> Students lose these marks by writing that the system "keeps the food below -18 °C". Read the question again: the only things the system does are write to a log file, update a screen and switch on a lamp. None of those makes the warehouse colder.
> 
> A reliable test in the exam is to ask what would happen if nobody was in the office. If the temperature would stay wrong, it is a monitoring system. If the system would correct it on its own, it is a control system.

### Q12
SRAM has a faster access time than DRAM because it does not have to be refreshed. **[1]**

The cache must supply the processor with data as quickly as possible, so the faster type of RAM is used there. **[1]**

DRAM has a greater capacity per chip than SRAM, so 16 GB of main memory fits into far fewer chips and takes up less space. **[1]**

DRAM is less expensive to manufacture than SRAM, so building all 16 GB from SRAM would make the laptop much more expensive. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - SRAM has a faster access time than DRAM
> - ... because SRAM does not need to be refreshed
> - ... so SRAM suits the cache, which has to keep the processor supplied with data
> - DRAM has a greater capacity per chip than SRAM // DRAM has a higher bit density
> - ... so 16 GB of main memory needs fewer chips / less space if DRAM is used
> - DRAM is less expensive to manufacture than SRAM
> - ... so making all 16 GB from SRAM would make the laptop much more expensive
> - The main memory does not need the very fast access time that the cache needs
> 
> **[4 marks]**
> 
> Accept "cheaper" for less expensive, and "more data per chip" for greater capacity per chip
> 
> Do not accept "SRAM is better than DRAM". The question asks why each type is used where it is, so an answer must say what makes each type suitable for its own job
> 
> Do not accept "SRAM is static and DRAM is dynamic". Expanding the abbreviations is not an explanation

> **[exam-tip]**
> There are two separate arguments to make here and weaker answers only make one. Say why SRAM belongs in the cache, then say why DRAM belongs in the main memory. Four marks means roughly two points on each side.
> 
> The size figures in the question are a hint. 4 MB against 16 GB tells you that capacity per chip and cost per chip matter for the main memory, which is exactly where DRAM wins.

### Q13
A monitoring system only records or displays the sensor data, but a control system uses the sensor data to change the process it is measuring. **[1]**

A monitoring system takes no action of its own, but a control system sends a signal to an actuator so that an action is carried out. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - A monitoring system records or displays the sensor data, whereas a control system uses the sensor data to change the process
> - A monitoring system takes no action on the process, whereas a control system carries out an action on the process
> - A monitoring system has no actuators, whereas a control system uses actuators
> - A monitoring system does not use feedback, whereas a control system uses feedback
> - The output of a monitoring system does not affect the next input, whereas the output of a control system affects the next input
> 
> **[2 marks]**
> 
> Accept a warning lamp, a display, an alarm or a log file named as the output of a monitoring system, provided the answer also says that the process itself is not changed.
> 
> Do not accept "a monitoring system checks the conditions and corrects them" or "a monitoring system adjusts the process". A monitoring system never acts on the process it is watching.
> 
> Do not accept "a control system is faster" or "a control system is more accurate". Speed and accuracy are not the difference between the two.

> **[exam-tip]**
> Each of your two answers must be written as a comparison. Writing only "a control system uses actuators" leaves the examiner to guess what a monitoring system does, and half a comparison scores nothing. Use the word "whereas" or "but" in every line.
> 
> The word "monitoring" makes students write that the system "checks and then corrects" the conditions. It does not correct anything. The moment your answer has a monitoring system changing something, you have described a control system and lost the mark.

### Q14
The data is stored in cells. Each cell contains two transistor gates, a control gate and a floating gate. **[1]**

To write a bit, a high voltage is applied that pushes electrons onto the floating gate. **[1]**

The floating gate is surrounded by an insulating layer, so it holds those electrons even when there is no power supply. This is why the video is still there after the drone is switched off. **[1]**

The control gate allows or stops the current passing through the cell, and whether the current passes depends on whether the floating gate is holding electrons, so the cell is read back as a 1 or a 0. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for data being stored in cells, each containing a control gate and a floating gate
> 
> **1 mark** for a high voltage pushing electrons onto the floating gate in order to write
> 
> **1 mark** for the floating gate retaining the electrons without power, so the memory is non-volatile
> 
> **1 mark** for the control gate allowing or stopping the current, so that the state of the cell is read as a 1 or a 0
> 
> Accept "the cells are built using NAND or NOR gates" as an alternative to the first marking point
> 
> Accept "erasing applies the voltage in reverse to pull the electrons off the floating gate" as an alternative to the second marking point
> 
> Accept "the floating gate is insulated by oxide layers above and below it" for the third marking point
> 
> Do not accept "the data is stored magnetically" or "the data is stored as pits and lands", which describe a magnetic hard disk and an optical disc
> 
> Do not accept "solid state memory has no moving parts" on its own. That is a consequence of the design, not an account of how a bit is stored

> **[exam-tip]**
> The usual answer to this question lists the benefits of solid state storage, that it is fast, small and has no moving parts, and scores nothing, because the question asks how the data is held. Learn the two gates and which job each one does: the floating gate stores the charge, and the control gate switches the current so the stored value can be read. Non-volatile is the term to reach for when you explain why the data survives the power being removed.

### Q15
| Feature | Static RAM (SRAM) | Dynamic RAM (DRAM) |
|---|---|---|
| How one memory cell is built | **Transistors arranged as flip-flops** **[1]** | **Transistors and capacitors** |
| Need for refreshing | **Does not need to be refreshed** **[1]** | **Must be refreshed constantly** |
| Relative access time | **Faster access time** **[1]** | **Slower access time** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each fully correct row (**max 3**). Both cells in a row must be correct for the mark
> 
> **1 mark** for SRAM using transistors arranged as flip-flops **and** DRAM using transistors and capacitors
> 
> **1 mark** for SRAM not needing to be refreshed **and** DRAM requiring constant refreshing
> 
> **1 mark** for SRAM having a faster access time **and** DRAM having a slower access time
> 
> Accept latches for flip-flops
> 
> Accept "refresh cycles" for refreshing
> 
> Do not accept a row where only one of the two cells is completed, or where the same answer is written in both cells

> **[exam-tip]**
> Every row here is a comparison, so each answer only means something next to the other one. Writing "fast" against SRAM and leaving the DRAM cell blank scores nothing. Use the words faster and slower so the examiner can see the contrast.
> 
> The refreshing row is the one worth memorising, because the other two follow from it. DRAM stores each bit as a charge in a capacitor and that charge leaks away, so it has to be topped up, and that is what makes DRAM slower.

### Q16
The platters are rotated at high speed. **[1]**

The read/write head is mounted on an arm, which moves the head over the correct track on the surface of the platter. **[1]**

A variation in the current in the head produces a variation in the magnetic field on the surface, so the data is stored as a magnetic pattern. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the platters or disks being rotated at high speed
> 
> **1 mark** for a read/write head on an arm being moved into position over the correct track
> 
> **1 mark** for a variation in the current in the head producing a variation in the magnetic field on the surface
> 
> Accept "the surface is coated with a material that can be magnetised" as an alternative to the third marking point
> 
> Accept "electronic circuits, or an actuator, control the movement of the arm" as part of the second marking point
> 
> Do not accept "the head burns the data onto the surface", which is the operation of an optical disc writer, not a magnetic hard disk
> 
> Do not accept "the head touches the surface". The head is positioned just above the surface

> **[exam-tip]**
> The mark scheme wants the direction of the conversion stated correctly, and it is easy to write the reading process by mistake. When writing, the current in the head is varied and this changes the magnetic field on the disk. When reading, it is the other way round: the changing magnetic field produces a varying current in the head. Say which way round yours is going. Also avoid the word "burns" anywhere near a magnetic hard disk, because that belongs to the laser of an optical disc writer.

### Q17
Cache memory: Static RAM (SRAM) **[1]**

Main memory: Dynamic RAM (DRAM) **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for SRAM as the type of RAM used for cache memory
> 
> **1 mark** for DRAM as the type of RAM used for main memory
> 
> Accept Static RAM and Dynamic RAM written in full, and accept the abbreviations on their own
> 
> Do not accept SDRAM for either answer. SDRAM is not a term used in this syllabus, and the two types named in the syllabus are Static RAM and Dynamic RAM
> 
> Do not accept ROM or cache as a type of RAM

> **[exam-tip]**
> The two abbreviations differ by one letter, so read the question and your own answer carefully. SRAM is Static, DRAM is Dynamic. Writing SDRAM, which you may have seen printed on a memory module, will not be credited here.
> 
> Link each one to a use as you learn it: SRAM sits in the cache because speed matters most there, DRAM is the main memory because capacity matters most there.

### Q18
The surface of each platter is divided into concentric circles called **tracks**. **[1]**

Each of these circles is divided into **sectors**, which are wedge-shaped sections of the surface. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for tracks
> 
> **1 mark** for sectors
> 
> Accept "concentric tracks" for the first answer
> 
> Do not accept "blocks" for either answer. A block is one track within one sector, which is the basic unit of storage, not the division of the surface itself
> 
> Do not accept "platters" for either answer, because the question has already named the platter

> **[exam-tip]**
> Tracks and sectors are swapped over in answers more often than any other pair of terms on this topic. Fix the shapes in your mind: a track is a ring, so it is a circle, and a sector is a wedge, like a slice cut out of the whole disk. The two together give a block, which is where a piece of data is actually written.

### Q19
Primary memory is needed because the processor works directly on the data and instructions held there. **[1]**

Its fast access times let the video being edited be processed at a speed the editor can work with. **[1]**

Secondary storage is needed because the video data held in primary memory while the computer is running is lost when the power is switched off, so finished files must be written somewhere that keeps them. **[1]**

Secondary storage also offers a far larger capacity at a much lower cost per gigabyte, so 4 TB of video can be stored affordably. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for: the processor can work directly only on data and instructions held in primary memory
> 
> **1 mark** for: primary memory has fast access times, so the video is processed at a usable speed
> 
> **1 mark** for: the data held in primary memory while the computer is running is lost when the power is switched off, so finished files must be written to secondary storage to be kept
> 
> **1 mark** for: secondary storage offers a much larger capacity, and a much lower cost per gigabyte, than primary memory
> 
> Accept "non-volatile" in place of a description of data being kept when the power is off.
> 
> Do not accept a comparison of Random Access Memory with Read Only Memory. This question is about the roles of primary memory and secondary storage in the system, not about types of memory chip.

> **[exam-tip]**
> This is the question where students empty out everything they know about RAM and ROM, and none of it is being asked for. The examiner wants two reasons for each of the two stores. For primary memory, think about how the processor reaches it and how fast. For secondary storage, think about what survives the power being switched off, and about how much you get for the money. Four sentences, four marks.

### Q20
RAM is volatile, so everything held in RAM is lost when the tablet is switched off. **[1]**

The start-up instructions would therefore no longer be present the next time the tablet was switched on, so the tablet could not start. **[1]**

ROM is non-volatile, so it keeps the start-up instructions without any power being supplied. **[1]**

ROM is read only, so the start-up instructions cannot be overwritten by the user or by a program that is running, whereas anything in RAM can be written over at any time. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - RAM is volatile
> - ... so the contents of RAM are lost when the tablet is switched off
> - ... so the start-up / boot-up instructions would not be there when the tablet was next switched on
> - ... so the tablet would have no instructions to load the operating system
> - ROM is non-volatile, so it keeps its contents when there is no power
> - ROM is read only, so its contents cannot be changed or deleted
> - ... so the start-up instructions cannot be overwritten by the user or by other software
> 
> **[4 marks]**
> 
> Accept "the tablet would not boot" or "the tablet would not know how to start" for the consequence point
> 
> Do not accept "ROM is cheaper than RAM". Cost is not the reason the two cannot be swapped
> 
> Do not accept "there would not be enough memory". The question replaces ROM with more RAM, so the total amount of memory increases

> **[exam-tip]**
> This question is really asking about two properties at once, and most answers only reach for one. Volatility explains why the instructions would disappear, and read only explains why they could be damaged even while the power is on. Give both and the four marks come easily.
> 
> Watch the direction of the argument. You are explaining why ROM is needed, so each point must end with something the tablet could no longer do.

### Q21
The printing drum is given an electrical charge across its whole surface. **[1]**

A laser beam is scanned across the drum and draws the image of the page, changing the charge on the parts of the drum that the laser strikes. **[1]**

Toner is attracted to the parts of the drum that the laser has written on, so the toner takes the shape of the text and images. **[1]**

The paper is passed against the drum and the toner is transferred from the drum onto the paper. **[1]**

The paper then passes through heated rollers, which melt the toner so that it is fixed permanently to the paper. **[1]**

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for the drum being charged
> 
> **1 mark** for a laser scanning across the drum and changing the charge to draw the image of the page
> 
> **1 mark** for toner being attracted to the areas of the drum written by the laser
> 
> **1 mark** for the toner being transferred from the drum onto the paper
> 
> **1 mark** for heated rollers melting the toner so that it is fixed to the paper
> 
> Accept "photosensitive drum" or "photoreceptor drum" for the drum
> 
> Accept "the fuser" for the heated rollers
> 
> Accept "the laser reverses the charge where it strikes the drum" for the second marking point
> 
> Do not accept "ink is sprayed onto the paper", which is the operation of an inkjet printer
> 
> Do not accept "the printer stores the page in a buffer first", which describes the use of a buffer rather than the printing operation

> **[exam-tip]**
> This is a sequence, and the marks follow the order of the sequence, so write it as numbered steps rather than as one long sentence. The two steps students most often leave out are the first and the last: charging the drum before the laser writes on it, and fusing the toner with heated rollers at the end. Without the heated rollers the toner would simply be loose powder sitting on the page. Do not drift into describing an inkjet printer; a laser printer uses dry toner powder, never liquid ink.

### Q22
The storage is non-volatile, so the data is still there after the device has been disconnected and carried to the office. **[1]**

The device can be physically disconnected from one computer and connected to another, so data can be moved between two machines that are not linked by a network. **[1]**

It has a large enough capacity, at a low cost per gigabyte, to hold a whole week of research data. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - The storage is non-volatile, so data is retained with no power supply while it is being carried
> - The device can be disconnected from one computer and connected to another
> - ... so data can be transferred with no network connection between the two sites
> - Capacity is large enough to hold a week of data // cost per gigabyte is low enough for the amount of data involved
> - The device is small and light enough to be carried by a person
> - The copy also acts as a backup held away from the original site
> 
> **[3 marks]**
> 
> Accept a named example of removable secondary storage, such as a USB flash drive, an external hard disk drive or an optical disc, provided a reason is also given
> 
> Do not accept "it is faster than sending the data over the network". The stem states that there is no network connection at the site

> **[exam-tip]**
> Read the scenario for the constraint before you start writing. The words "no network connection" are there to tell you which property matters, and answers that suggest uploading to the cloud have ignored them. The mark for portability is the one most often missed: say that the device can be unplugged and carried, not just that it is small.

### Q23
ROM is non-volatile, so the instructions that start the machine are still present each time it is switched on. **[1]**

ROM is read only, so those start-up instructions cannot be overwritten while the machine is in use. **[1]**

RAM can be written to as well as read, so it can hold the journey and payment details entered by the customer while the sale is taking place. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - ROM is non-volatile, so its contents remain when the machine has no power
> - ... so the start-up / boot-up instructions are available every time the machine is switched on
> - ROM is read only, so its contents cannot be changed or overwritten by the running program
> - RAM is read and write, so data can be written into it while the machine is being used
> - RAM holds the data and instructions currently in use, for example the journey selected or the payment being processed
> - RAM is volatile, so the customer's details are cleared when the machine is switched off
> 
> **[3 marks]**
> 
> Accept "temporary" for volatile and "permanent" for non-volatile only where you also state that the contents are lost or kept when the power is removed
> 
> Do not accept "RAM is faster than ROM" on its own. Speed is a difference between the two, but it does not explain why the machine needs both

> **[exam-tip]**
> The command word is explain, so every point needs a because. Writing "ROM is non-volatile and RAM is volatile" lists two facts and earns very little. Turn each fact into a consequence for this machine: non-volatile means the start-up instructions survive being switched off overnight.
> 
> You can also lose marks by describing what RAM and ROM are in general instead of saying what each one does in the ticket machine. Tie every point back to the device in the question.

### Q24
Secondary storage keeps data when the computer is switched off, so saved files are not lost. **[1]**

Secondary storage provides a much larger capacity than primary memory, so far more data can be kept. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - Data is retained when the power is switched off // it is non-volatile // it stores data permanently
> - It has a much larger capacity than primary memory
> - It costs much less per gigabyte, so large amounts of data can be stored affordably
> - Removable secondary storage allows data to be carried between computers or taken off site
> - It holds programs and files that are not currently in use, ready to be loaded when they are needed
> 
> **[2 marks]**
> 
> Accept "long-term storage" or "permanent storage" for the first bullet
> 
> Do not accept "it is faster than primary memory". Secondary storage is very much slower

> **[exam-tip]**
> Two reasons means two different reasons. "It saves your files" and "it stores your work permanently" are the same reason written twice, and they score one mark between them. Pick one point about keeping data without power and one about capacity or cost, and you have two clearly separate marks.

### Q25
A sensor in the headset, such as a gyroscope or an accelerometer, detects the movement of the trainee's head. **[1]**

The sensor data is transmitted to a microprocessor, which analyses it to identify the direction and the speed of the movement. **[1]**

The images shown on the headset's two displays are updated to match the new position of the head, so the view of the cockpit changes. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for a sensor detecting the head movement, named as a gyroscope or an accelerometer
> 
> **1 mark** for the data being transmitted to a microprocessor that analyses it to identify the direction or speed of movement
> 
> **1 mark** for the images on the displays, screens or lenses being updated to match
> 
> Accept "digital cameras record the user's eye movements for analysis" as an additional operation, but only in place of the first marking point, not as well as it
> 
> Do not accept "the headset knows where the trainee is looking" with no sensor or processing named
> 
> Do not accept "the headset outputs surround sound through its speakers", which is a different output of the headset and does not change the view

> **[exam-tip]**
> Explain questions on a virtual reality headset need the full chain: sensor, then microprocessor, then display. Most lost marks come from stopping after the sensor. Name the sensor as a gyroscope or an accelerometer rather than writing "a movement sensor", because the mark scheme lists the specific components, and remember that the headset has two displays or lenses, one for each eye, which is what creates the three-dimensional effect.

### Q26
| Statement | RAM or ROM |
|---|---|
| The contents are lost when the power to the computer is switched off. | **RAM** **[1]** |
| This memory holds the instructions that the computer needs in order to start up. | **ROM** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for RAM against the first statement
> 
> **1 mark** for ROM against the second statement
> 
> Accept the names written in full: Random Access Memory for RAM, Read Only Memory for ROM
> 
> Do not accept ROM for the first statement. ROM is non-volatile, so its contents are still there after the power is switched off
> 
> Do not accept RAM for the second statement. RAM is volatile, so start-up instructions held there would be lost every time the computer was switched off

> **[exam-tip]**
> The word volatile is worth learning precisely. Volatile means the contents are lost when the power is removed, so RAM is volatile and ROM is non-volatile. A very common error is to swap these two round because ROM sounds like the smaller and weaker chip.
> 
> Also be careful not to describe RAM as "permanent storage". RAM is fast working memory, not storage that survives a power cut.

### Q27
Only a limited amount of data and instructions can be held in primary memory at any one time. **[1]**

Anything that does not fit has to remain in secondary storage. **[1]**

Before the processor can use it, it must be transferred into primary memory, and other data must be transferred out again to make room. **[1]**

Secondary storage has much slower access times than primary memory, so the tablet spends a large part of its time moving data instead of processing it. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for: primary memory can hold only a limited amount of data and instructions at any one time
> 
> **1 mark** for: the data and instructions that do not fit stay in, or are written back to, secondary storage
> 
> **1 mark** for: data must be transferred into primary memory before the processor can use it, and transferred out again to free space
> 
> **1 mark** for: secondary storage has much slower access times, so the repeated transfers slow the whole system down
> 
> Accept a correct reference to virtual memory or to paging, but neither term is needed for full marks.
> 
> Do not accept "the processor is too slow" or "the tablet needs a better processor". The stem states that the processor has not changed.

> **[exam-tip]**
> The stem rules out two of the three obvious answers on purpose: the processor and the secondary storage are both unchanged, so neither can be the cause. That leaves you to build a chain, and a chain is what the four marks are for. Not enough room, so data stays on the drive, so it has to be shuffled in and out, so the slow drive sets the pace. Write the chain in that order and each link earns a mark.

### Q28
The speaker is sent an electrical signal by the computer. **[1]**

The speaker converts that electrical signal into sound waves that travel through the air to the listener. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the speaker receiving an electrical signal // an analogue signal from the computer
> 
> **1 mark** for converting the electrical signal into sound waves
> 
> Accept "the signal makes part of the speaker vibrate and the vibration produces the sound waves" for the second mark
> 
> Accept a reference to the digital data being converted to an analogue signal before it reaches the speaker, for the first mark
> 
> Do not accept "the speaker plays the sound", which repeats the question instead of describing the operation

> **[exam-tip]**
> A speaker is the exact reverse of a microphone, so learn the two as a pair: a microphone turns sound waves into an electrical signal, and a speaker turns an electrical signal back into sound waves. The common mistake is writing only about what the guest hears. Marks are given for the conversion the device performs, so both the electrical signal and the sound waves have to be named.

### Q29
The processor fetches each instruction from an address in primary memory, so a program can only be executed once its instructions are held there. **[1]**

The processor cannot fetch instructions directly from secondary storage. **[1]**

Primary memory also has much faster access times than secondary storage, so the program runs at a speed the user will accept. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for: the processor fetches instructions directly from primary memory // an instruction has to be in primary memory before it can be fetched and executed
> 
> **1 mark** for: the processor cannot access secondary storage directly // secondary storage is not directly addressable by the processor
> 
> **1 mark** for: primary memory has much faster access times, so the program runs at a usable speed // running straight from secondary storage would be far too slow
> 
> Accept a correct reference to the fetch stage of the fetch-execute cycle for the first mark.
> 
> Do not accept "primary memory is bigger than secondary storage". It is normally very much smaller.

> **[exam-tip]**
> Speed is the answer students reach for first, and it is worth only one of the three marks. The other two are about access: the processor can only reach primary memory directly, so an instruction sitting on a hard disk simply cannot be fetched. Make that point before you write anything about speed.

### Q30
A capacitive touchscreen works by detecting a change in the electrical charge in its top layer when the screen is touched. **[1]**

The object touching the screen has to be conductive, so a thick glove would not change the charge and the touch would not be registered. **[1]**

A resistive touchscreen has two conductive layers separated by a small gap. Pressing the screen pushes the layers together and completes a circuit at that point. **[1]**

Any object can apply that pressure, including a gloved finger, so the resistive touchscreen should be chosen. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for stating that a capacitive screen detects a change in electrical charge or current
> 
> **1 mark** for stating that a capacitive screen needs a conductive object, so a gloved finger would not be detected
> 
> **1 mark** for stating that a resistive screen has two layers that are pushed together by pressure to complete a circuit
> 
> **1 mark** for choosing the resistive screen because pressure can be applied through a glove
> 
> Accept "the layers touch and the space between them is removed" for the third mark
> 
> Accept a correct answer written the other way round, for example ruling the capacitive screen out first and then recommending the resistive screen
> 
> Do not accept "resistive screens are cheaper" or "resistive screens are more durable", which are not based on the principal operation of the device and are not asked for here
> 
> Do not award the fourth mark if the capacitive screen is recommended, however good the reasoning

> **[exam-tip]**
> A question like this gives marks for the mechanism, not for the choice on its own, so writing "resistive" and stopping scores zero. Work through the operation of each screen and then let the operation decide the answer. The detail examiners look for is that a capacitive screen relies on the conductivity of a bare finger, which is exactly what a glove removes, while a resistive screen only needs pressure and does not care what is doing the pressing.

### Q31
Primary memory holds the data and the instructions that are currently in use while the computer is running. **[1]**

The processor can read from it and write to it directly, and its access times are much faster than those of secondary storage. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - Holds the data and instructions currently in use // holds the program that is running
> - Is directly accessible by the processor // the processor reads from it and writes to it directly
> - Has much faster access times than secondary storage
> - Acts as the short-term or working store while the computer is switched on
> 
> **[2 marks]**
> 
> Accept "Immediate Access Store" as another name for primary memory
> 
> Do not accept "stores data permanently" or "stores files the user has saved". That is the role of secondary storage

> **[exam-tip]**
> The word that earns the mark is "directly". Plenty of answers say primary memory is fast, which is true but is only half the point. What makes it primary is that the processor reaches it without going through anything else. Say that, and the speed mark usually follows.

### Q32
The top layer of a capacitive touchscreen holds an electrical charge. **[1]**

A finger is conductive, so touching the screen changes the electrical charge, or current, at the point of contact. **[1]**

A microprocessor uses that change to calculate the horizontal and vertical coordinates of the point of contact, and passes them to the software. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the screen holding an electrical charge // having an electric field across it
> 
> **1 mark** for the touch of a conductive object changing the charge or the current at that point
> 
> **1 mark** for a microprocessor calculating the coordinates of the point of contact from that change
> 
> Accept "increase in current" or "decrease in current" for the second mark
> 
> Accept "the coordinates are sent to the software as an input" as the third mark
> 
> Do not accept "the two layers touch and complete a circuit", which is the operation of a resistive touchscreen, not a capacitive one

> **[exam-tip]**
> The two types of touchscreen are marked separately, so decide which one the question names before you start writing. Layers touching and a circuit being completed belongs to a resistive screen; a change in electrical charge belongs to a capacitive screen. Mixing them loses the mark even though both sentences are true of some touchscreen. Also remember the final step: something has to work out where on the screen the touch happened, and that is the microprocessor calculating the coordinates.

### Q33
The kiosk needs an input device so that the guest can enter their booking details into the system. **[1]**

Without one, the processor would have no data to work on and the system could not identify which booking to check in. **[1]**

The kiosk needs an output device so that the results of that processing can leave the system. **[1]**

Without one, the guest could not be told the room number and could not be given the printed room card, so the check-in could never be completed. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for stating that an input device lets the guest supply data to the kiosk, for example a booking reference, a name or payment details
> 
> **1 mark** for the consequence of having no input: the processor has no data to process // the system cannot identify which booking belongs to this guest
> 
> **1 mark** for stating that an output device lets the results of processing leave the system and reach the guest
> 
> **1 mark** for the consequence of having no output: the guest is never told the room number, or never receives the room card, so the check-in cannot be completed
> 
> Accept "the kiosk could not confirm the booking to the guest" for the fourth mark.
> 
> Do not accept a description of how a touchscreen or a printer works internally. This question asks why the kiosk needs input and output at all, not how a named device operates.

> **[exam-tip]**
> The four marks here are two pairs, and the second mark of each pair is the one students miss. Naming an input and an output only gets you halfway. Each time you name one, add "so that ..." or "without it ..." and say what the system would be unable to do. Notice also that a touchscreen counts as both an input device and an output device, so it can earn a mark on either side, but not on both for the same point.

### Q34
The microphone detects sound waves travelling through the air. **[1]**

It converts those sound waves into an electrical signal that the computer can process. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the microphone detecting sound waves // vibrations in the air
> 
> **1 mark** for converting the sound waves into an electrical signal // an analogue signal
> 
> Accept "the electrical signal is then sampled and stored as digital data" for the second mark
> 
> Do not accept "the microphone records the user's voice", which states what the device is used for rather than the operation it carries out

> **[exam-tip]**
> The command word is describe, so the answer has to say what the device physically does, not what it is for. "It lets the user talk to the computer" earns nothing. For a microphone, always name both ends of the conversion: sound waves in, electrical signal out. Students who only write "it turns sound into data" miss the mark because they have skipped the electrical signal.

### Q35
Without an input device there is no way for data or instructions to enter the system, so the processor has nothing to process. **[1]**

Without an output device the results of processing stay inside the computer, so nobody can use them. **[1]**

Input and output are what connect the computer to the world outside it, so a machine with only a processor and memory cannot carry out a useful task. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - Without an input device, no data or instructions can enter the system
> - ... so the processor has nothing to process // the user cannot tell the system what to do
> - Without an output device, the results of processing cannot leave the system
> - ... so the user cannot see or use those results
> - Input and output are how the computer communicates with the world outside it
> - A system with no input and no output cannot perform a useful task for a user
> 
> **[3 marks]**
> 
> Accept "the computer would be useless" only when it is joined to a reason, for example "useless because the user could never see the result"
> 
> Do not accept "the computer would not switch on" or "the computer would break". Both are untrue, and neither answers the question

> **[exam-tip]**
> When a question quotes a wrong statement and asks you to explain why it is wrong, you must attack the statement itself. Answers that simply describe what a keyboard and a monitor do never engage with the claim that they are optional. Deal with input and output separately, and in each case say what the system would be unable to do without it.

### Q36
An input device allows data or instructions from outside the computer to be entered into the system, so that the processor has something to work on. **[1]**

An output device takes the results the computer has produced and presents them in a form a person can understand or use. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the input role: allows data or instructions to be entered into the computer system // converts data from outside the system into a form the computer can process
> 
> **1 mark** for the output role: presents or communicates the results of processing to the user // converts processed data into a form a person can understand or use
> 
> Accept "sends data to the processor" for the input mark and "receives data from the processor" for the output mark.
> 
> Do not accept a list of device names such as "keyboard" or "monitor" on its own. The question asks for the role a device plays, not for an example of one.

> **[exam-tip]**
> Most students lose this mark by naming devices instead of describing what they are for. A list of five input devices scores nothing here. Write one sentence that says what the device lets the system do, then add an example only if you have room.

### Q37
**Benefits of Design A**

- The machine only ever has to run the ticket selling program, so a small processor and a small amount of memory are enough, which makes each machine cheaper to manufacture. **[1]**

- A customer cannot install or run any other software on the machine, so it cannot be used for anything except selling tickets. **[1]**

**Drawbacks of Design A**

- The firmware is difficult to change, so adding a new function such as selling a new type of ticket is far harder than installing new software on a general purpose computer. **[1]**

- Fault finding and repair are specialist tasks, so the company cannot use an ordinary technician and repairs cost more. **[1]**

**[4 marks]**

> **[mark-scheme]**
> Two marks for benefits and two marks for drawbacks. A third correct benefit does not earn a drawback mark.
> 
> Each point must be applied to the ticket machine.
> 
> **Benefits, any two from:**
> 
> - Only the ticket selling program has to run, so a smaller processor and less memory are needed and each machine is cheaper to manufacture
> - The machine starts up and responds faster, because there is no general purpose operating system to load
> - The machine is more reliable, because no other program can be installed that could interfere with or crash the ticket selling program
> - A customer cannot install or run other software on the machine, so it cannot be misused
> - Lower power consumption, so the running cost of a station full of machines is lower
> 
> **[2 marks]**
> 
> **Drawbacks, any two from:**
> 
> - The firmware is difficult to update, so adding a new function such as a new ticket type is much harder than installing software on a general purpose computer
> - Fault finding, repair and upgrading are specialist tasks, so repairs cost the company more
> - The machine cannot be adapted to a different task, so it has no other use if the company stops selling tickets this way
> - An out of date machine is likely to be replaced and thrown away rather than upgraded, which adds to e-waste
> 
> **[2 marks]**
> 
> Accept "cheaper" only where the reason is given.
> 
> Do not accept "it is smaller" as a benefit. A ticket machine is a large cabinet and has room for either design.
> 
> Do not accept "it is dedicated to one task" as a benefit without saying what that gains the company here. Accept "it cannot be adapted for another task" as a drawback when applied to the ticket machine.

> **[exam-tip]**
> Read the tariff split before you write. Four marks for two benefits and two drawbacks means exactly one mark each, so four sentences about embedded systems in general will not reach four marks. Two of them have to be drawbacks.
> 
> Every point has to touch this ticket machine. "It is cheaper" scores nothing on its own. "It is cheaper because the machine only ever runs the ticket program, so a small processor is enough" scores the mark. The words after "because" are what the examiner is looking for.

### Q38
- A smartphone is not dedicated to a single task. It performs many different tasks that are not related to each other. **[1]**

- The user can install and remove any software they choose, so the set of functions a smartphone performs is not fixed when it is manufactured. **[1]**

- A smartphone runs a full general purpose operating system, rather than firmware written to control one device. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - A smartphone is not dedicated to one task // it carries out many unrelated tasks // it is a general purpose computer
> - The user can install, remove and change the software, so the functions are not fixed
> - A smartphone runs a full operating system rather than firmware written for one function
> - A smartphone is not built into a larger device // it is not integrated into a larger system
> 
> **[3 marks]**
> 
> Accept "apps" for software.
> 
> Accept a comparison with a named embedded system, for example a washing machine controller, provided the point being made is one credited in this mark scheme.
> 
> Do not accept "a smartphone is too big" or "a smartphone is too small". Physical size does not decide whether a system is embedded. A large industrial machine controller is an embedded system.
> 
> Accept "a smartphone needs a powerful general purpose processor to run many apps, whereas an embedded system needs only limited processing power". Do not accept "a smartphone has too much memory" on its own.
> 
> Accept "a smartphone is not built into / integrated into a larger system". Do not accept "a smartphone is not built into anything" with no reference to a larger system or device.

> **[exam-tip]**
> Size is the trap in this question. Students often decide whether something is an embedded system by how small it is, and a smartphone is small, so they say yes. The controller inside a factory machine is an embedded system and it is not small.
> 
> The test Cambridge marks is whether the system is dedicated to one fixed task set by the manufacturer, or whether the user can choose what software it runs. Write about the task and the software, not the size.

### Q39
The computer sends the model data into the buffer at high speed, while the 3D printer takes data out of the buffer at the much slower speed at which it prints. **[1]**

The buffer stores that data temporarily until the 3D printer is ready to use it. **[1]**

The computer is therefore not held up waiting for the 3D printer, so the processor can carry on with other tasks. **[1]**

When the buffer is full, an interrupt is sent to the computer so that it stops sending any more data. **[1]**

When the buffer is empty, or nearly empty, an interrupt is sent to the computer to request more data, and the computer then sends the next block of data into the buffer. **[1]**

**[5 marks]**

> **[mark-scheme]**
> **Any five from:**
> 
> - The computer sends data much faster than the 3D printer can print it, so the two work at different speeds
> - The buffer stores the data temporarily until the 3D printer is ready to use it
> - Data is transferred out of the buffer to the 3D printer at the slower printing speed
> - The computer is not held up waiting for the 3D printer, so the processor can carry on with other tasks
> - When the buffer is full, an interrupt is sent to the computer to stop it sending more data
> - When the buffer is empty, or nearly empty, an interrupt is sent to the computer to request more data
> - The computer responds by sending the next block of data into the buffer
> - This repeats until all of the data for the model has been sent
> 
> **[5 marks]**
> 
> Accept "the interrupt is sent by the 3D printer" or "the interrupt is sent by the device" for either interrupt mark.
> 
> Do not accept an answer that says the computer sends an interrupt to the 3D printer to ask for more data. The interrupt travels from the device that owns the buffer to the computer.
> 
> Do not accept "the buffer stores the whole model file". The buffer is small, which is the reason the interrupts are needed at all.
> 
> Do not accept a description of the fetch-execute cycle. No marks are available for how the processor handles the interrupt once it arrives.

> **[exam-tip]**
> The direction of the interrupt is the mark most often thrown away. The interrupt is a signal from the printer to the computer saying that its buffer needs more data, or that its buffer is full and the computer should stop. Students who write that the computer interrupts the printer have it backwards.
> 
> You do not need to explain what the processor does after it receives the interrupt. The marks here are for what the state of the buffer is signalling, so keep every sentence about the buffer filling and emptying.

### Q40
- The embedded system runs only the coffee making program, so a low power processor and a small amount of memory are enough, which makes the coffee machine cheaper to manufacture. **[1]**

- The embedded system uses very little electricity, so the coffee machine costs less to run. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - Cheaper to manufacture, because only a small dedicated processor and a small amount of memory are needed
> - Uses less electricity // lower power consumption
> - Small enough to fit inside the coffee machine
> - Starts up and responds quickly, because there is no general purpose operating system to load and only one program to run
> - More reliable, because no other software is running that could interfere with the coffee making program
> 
> **[2 marks]**
> 
> Accept a benefit written from the manufacturer's point of view or the user's point of view.
> 
> Accept "faster response" or "real time response" for the fourth point.
> 
> Do not accept "it is dedicated to one task" or "it is built into the machine" on their own. Those are features of an embedded system, not benefits of using one.
> 
> Do not accept "it is small" with no link to fitting inside the coffee machine.
> 
> Do not accept "it is easy to upgrade". The opposite is true, and this is a standard drawback.

> **[exam-tip]**
> Benefits and features are not the same thing, and this is where most marks are lost. "Dedicated to one task" and "built into the device" describe what an embedded system is. Neither of them earns a benefit mark by itself.
> 
> Turn each feature into what it gains. Because the system runs only one program, it needs a smaller processor, so the machine costs less to build. That second half of the sentence is the mark.

### Q41
The microphone and the processor work at different speeds, because the microphone produces sound data continuously while the processor accepts that data only when it is free. **[1]**

The sound data is written into the buffer as it is captured, and the buffer holds it temporarily. **[1]**

The processor reads the sound data out of the buffer when it is ready, so the microphone is not held up and no sound data is lost. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for identifying that the microphone and the computer, or processor, work at different speeds
> 
> **1 mark** for stating that the captured sound data is written into the buffer and held there temporarily
> 
> **1 mark** for stating that the processor reads the data out of the buffer when it is ready, so that no data is lost, or so that the microphone is not held up
> 
> Accept "the microphone sends data faster than the processor can accept it" or "the processor is busy with other tasks" for the first mark.
> 
> Accept "the buffer fills while the processor is busy and empties when the processor reads it" for the third mark.
> 
> Do not accept "the buffer speeds up the microphone" or "the buffer makes the transfer faster". A buffer does not change the speed of either device.
> 
> Do not accept "the buffer stores the whole recording", because a buffer holds only a small amount of data at a time.

> **[exam-tip]**
> Most textbook buffer examples send data out of the computer to a printer, so students who have learned only that example often describe the flow the wrong way round here. Decide which device is producing the data and which one is consuming it before you write anything.
> 
> The marks are for the mechanism, not for the benefit. Writing "it stops the sound from lagging" gives a result without saying what the buffer actually does with the data.

### Q42
A buffer is an area of memory that is used for the temporary storage of data. **[1]**

It holds the data while the data is being transferred between two devices, or two processes, that work at different speeds. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for stating that a buffer is temporary storage, or an area of memory that holds data temporarily
> 
> **1 mark** for stating that it holds data being transferred between two devices, or two processes, that work at different speeds
> 
> Accept "temporary store", "temporary memory", or "holds data until the receiving device is ready" for the first mark.
> 
> Accept "so that the faster device does not have to wait for the slower device" for the second mark.
> 
> Do not accept "permanent storage" or "secondary storage". A buffer is volatile temporary storage, not a place where data is kept.
> 
> Do not accept "a buffer stores data" on its own, because it does not say that the storage is temporary.

> **[exam-tip]**
> The word "temporary" is doing most of the work in this definition and it is the word most often left out. Writing that a buffer "stores data" is true of every kind of memory, so it earns nothing.
> 
> The second mark is for the reason the buffer exists, so always name the difference in speed between the two devices. A definition that stops at "an area of memory" is only half an answer.

### Q43
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

### Q44
> **[mark-scheme]**
> **1 mark **for each bullet point (**max 3**).
> 
> - Disk needs to be prepared for initial use
> - Disk needs to be checked for errors
> - A new file system needs to be generated on the disk
> - The file allocation table needs to be set up

### Q45
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

### Q46
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

### Q47
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

### Q48
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

### Q49
> **[mark-scheme]**
> **1 mark **for each bullet point (**max 2**)
> 
> - Immediate Access Store holds all the data / instructions / programs currently in use
> - Immediate Access Store is volatile memory
> - Immediate Access Store has fast access times

### Q50
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

### Q51
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

### Q52
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

### Q53
**1 mark** for each bullet point (**max 3**)

- The system uses feedback
- The system acts independently
- Input data causes the car to brake
- … braking decreases or changes the distance to the object
- … this new distance is used to determine whether or how hard the car needs to brake

### Q54
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

### Q55
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

### Q56
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

### Q57
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

### Q58
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
