# Mark Schemes — Networks & the Internet
**2. Communication** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (82 questions)


### Q1
System A should be stored on a public cloud. **[1]**

The brochures are meant to be available to anyone on the internet, and a public cloud shares the provider's infrastructure between many customers, which makes it the cheaper way to serve a large number of downloads. **[1]**

System B should be stored on a private cloud. **[1]**

A private cloud is dedicated to the company, so access to the salary records can be restricted to selected employees and the company keeps control over the security of the data. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for System A on a public cloud
> 
> **1 mark** for a supporting reason, from: the brochures are intended to be available to anyone on the internet // the infrastructure is shared with other organisations, so it is cheaper // capacity can be increased when many people download at the same time
> 
> **1 mark** for System B on a private cloud
> 
> **1 mark** for a supporting reason, from: the service is dedicated to the company only // access can be restricted to selected employees rather than the general public // the company keeps control over the security of the salary records // the company controls how the records are backed up
> 
> Accept a reason for System B that names the confidential nature of salary data as the cause of the restriction
> 
> Do not award the reason mark in either half if the type of cloud named in that half is wrong, because the reason has to support the choice made
> 
> Do not accept "salary records are private so use a private cloud", because it repeats the name of the cloud instead of giving a reason

> **[exam-tip]**
> Two systems and four marks means one mark for each choice and one mark for each reason. Naming both clouds correctly and giving no reasons throws away half the question.
> 
> The reason for the public cloud is the part students miss. It is easy to explain why salary data must be locked down. The examiner also wants to know why the brochures do not need that, and why sharing a provider's infrastructure with other organisations is an advantage when the material is meant to be public anyway.

### Q2
Office: a star topology. **[1]**

Each computer has its own cable to a central switch, so a computer is added or removed without disconnecting any of the others, which suits an office where staff join and leave often. **[1]**

A fault on one cable stops only the computer on that cable, so the other twenty-nine computers keep working. **[1]**

Control room: a mesh topology. **[1]**

Every one of the four computers has a direct connection to each of the other three, so there is more than one route between any two of them and they still communicate if one connection fails. **[1]**

**[5 marks]**

> **[mark-scheme]**
> **1 mark** each, to a maximum of 5
> 
> **1 mark** for choosing a star topology for the office
> 
> **1 mark** for a computer being added or removed without disconnecting the other computers, because each has its own cable to the central switch
> 
> **1 mark** for a cable fault affecting only one computer, so the other twenty-nine keep working
> 
> **1 mark** for choosing a mesh topology for the control room
> 
> **1 mark** for every computer having a direct connection to every other, so there is more than one route between any two
> 
> **1 mark** for the four computers still being able to communicate when one connection fails, which is the requirement given in the stem
> 
> **1 mark** for a mesh being affordable for four computers, which need only 6 connections, whereas thirty computers would need 435
> 
> Accept "full mesh" in place of "mesh"
> 
> Accept a bus topology for the office only where you justify it by low cost and accept that a single cable fault stops the whole office
> 
> Do not accept a mesh for the office without a justification, because thirty computers would need 435 connections
> 
> Do not accept a star topology for the control room, because the central device would be a single point of failure and the stem requires communication to continue when a connection fails

> **[exam-tip]**
> "Justify" means give the choice and the reason together, and the reason has to come from the stem. Two details are placed there deliberately: staff join and leave often, and the control room must keep working if a connection fails. Each of those points to a different topology.
> 
> Do not choose the same topology for both areas. The question tells you the site uses a hybrid topology, which means the two areas are meant to be different. An answer that puts a star in both places has missed what the question is asking.

### Q3
A private cloud is dedicated to the bank alone, so the infrastructure holding the account records is not shared with other organisations. **[1]**

This gives the bank greater control over the security and privacy of the records, instead of relying on a provider that is serving many other customers at the same time. **[1]**

Access can be limited to the bank's own selected users rather than being open to anyone on the internet, which reduces the risk of unauthorised access to customer data. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** each, to a maximum of 3, from the following.
> 
> **1 mark** for the service is dedicated to the bank and is not shared with other organisations
> 
> **1 mark** for the bank keeps greater control over the security or the privacy of the records
> 
> **1 mark** for access is restricted to selected users rather than the general public, reducing unauthorised access
> 
> **1 mark** for the bank controls when and how backups are taken
> 
> **1 mark** for the storage can be tailored to the bank's own requirements
> 
> Accept "bespoke" for "tailored"
> 
> Do not accept "it is more secure" on its own, because the mark is for the control the bank keeps rather than for an unsupported claim
> 
> Do not accept "it is cheaper", because a private cloud is normally more expensive than a public cloud of the same capacity

> **[exam-tip]**
> Answers here usually say "a private cloud is safer" and stop. That is a conclusion, not an explanation. The marks are for the reasons behind it: the infrastructure is not shared, the bank sets the security, and only chosen users are let in.
> 
> Watch the direction of the cost argument. A private cloud usually costs more, because the bank is paying for infrastructure reserved for itself alone. Low cost is a reason to pick a public cloud, so it cannot be used to justify this choice.

### Q4
(i) Star topology **[1]**

(ii) Full mesh topology **[1]**

(iii) Hybrid topology **[1]**

**[3 marks]**

> **[mark-scheme]**
> (i) **1 mark** for star
> 
> (ii) **1 mark** for mesh
> 
> Accept full mesh for part (ii)
> 
> (iii) **1 mark** for hybrid
> 
> Do not accept star for part (ii). Every computer in Building B connects directly to every other computer and there is no central device
> 
> Do not accept star or mesh for part (iii), because the network as a whole combines two different topologies

> **[exam-tip]**
> Read the description of the connections, not the number of devices. "Each with its own cable to a single switch" is a star every time, and "a direct connection to every other computer" is a mesh every time.
> 
> Part (iii) is the one that is left blank. When one network is built from parts that use different topologies, the network as a whole is a hybrid topology. That word is on the syllabus and it is what the examiner is waiting for.

### Q5
| Description | Type of cloud |
|---|---|
| Computing services are offered by a third-party provider over the internet and are available to anyone with the appropriate equipment and credentials. | **Public cloud** **[1]** |
| Computing services are dedicated to one organisation, and only that organisation's users may access them. | **Private cloud** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `Public` in the first row
> 
> **1 mark** for `Private` in the second row
> 
> Accept "public cloud" and "private cloud" written in full
> 
> Do not accept "shared cloud" or "open cloud" for the first row, and do not accept "personal cloud" or "internal cloud" for the second row, because these are not the terms used in the syllabus

> **[exam-tip]**
> The word that decides the first answer is "anyone". A public cloud shares the provider's infrastructure between many customers, so anyone who pays for it can use it. A private cloud is dedicated to one organisation, so the answer turns on who is allowed in, not on where the servers stand.
> 
> Students often assume that a private cloud must sit inside the organisation's own building. It does not have to. A provider can run a private cloud over the internet and it is still private, because it is reserved for that one organisation.

### Q6
A hybrid topology is a network made by combining two or more different topologies. **[1]**

For example, a star network in one building joined to a mesh network in another building. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for a network that combines // joins together two or more different topologies
> 
> **1 mark** for a valid example that names two different topologies, for example star and bus, star and mesh, or bus and mesh
> 
> Do not accept an example that names only one topology, such as "several star networks joined together", because no second topology has been named
> 
> Do not accept "a mixture of wired and wireless connections", which is not a combination of topologies

> **[exam-tip]**
> The example must name two different topologies. Writing "a mixture of topologies" only repeats the definition and cannot earn the second mark.
> 
> The command word is "state", so one clear sentence is enough for the first mark. Listing the advantages of a hybrid topology earns nothing here.

### Q7
Drawback 1: the company loses direct control over its manuscripts. **[1]**

The files are held on a provider's remote infrastructure, so the company has to rely on that provider to keep them secure and to take backups, and cannot check those arrangements for itself. **[1]**

Drawback 2: the company has to keep paying for the service. **[1]**

The provider's charges recur for as long as the manuscripts are stored, while storage devices bought for the building are paid for once, so over several years the cloud can cost more. **[1]**

**[4 marks]**

> **[mark-scheme]**
> A maximum of 2 marks for each drawback, to a maximum of 4.
> 
> **1 mark** for loss of control over the data, and **1 mark** for the development that it is held on someone else's remote infrastructure and the company depends on the provider for security and backups
> 
> **1 mark** for increased recurring cost, and **1 mark** for the development that the provider's charges must be paid repeatedly while the company's own devices are paid for once
> 
> **1 mark** for a reliable internet connection is required, and **1 mark** for the development that the manuscripts cannot be reached at all if the connection or the provider's server fails
> 
> **1 mark** for uploading and downloading is slow for large files, and **1 mark** for the development that the transfer speed is limited by the company's internet connection rather than by its own devices
> 
> Accept "a third party" for "the provider"
> 
> Accept "the provider's security may be weaker" or "it may be less secure" as the first mark of a security drawback; the second mark needs the development that the company relies on the provider for its security and cannot check it
> 
> Do not accept two wordings of one drawback, for example "it needs the internet" and "it cannot be used offline", as two separate drawbacks

> **[exam-tip]**
> Four marks for two drawbacks means each one is worth two, so each needs a point and then a development. "It costs money" is the point; "and the charge is paid every month for as long as the files are stored" is the development that earns the second mark.
> 
> Do not turn this into an argument that cloud computing is simply worse. The examiner is testing whether you can state a real weakness, so keep to the ones the syllabus supports: dependence on an internet connection, charges that recur, and giving up direct control of the data.

### Q8
Each of the six computers has a direct connection to every other computer, so there is more than one route between any two of them. **[1]**

If one connection fails, the data takes an alternative route, and the computers act as relays to pass packets on towards the destination, so the monitoring keeps working. **[1]**

For twenty computers the number of connections rises from 15 to 190. **[1]**

That means far more cable and far more network ports on every computer, so the cost rises steeply and the network becomes difficult to install and to expand. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for every computer having a direct connection to every other computer, giving multiple routes between any two
> 
> **1 mark** for the data taking an alternative route if one connection fails, so the monitoring keeps working // for the devices acting as relays
> 
> **1 mark** for the number of connections growing very quickly, from 15 for six computers to 190 for twenty
> 
> **1 mark** for a consequence of that growth: much more cabling and hardware, a higher cost, or a network that is difficult to install and expand
> 
> Accept "there is no single point of failure" for the first point
> 
> Accept the third mark without the figures 15 and 190 if you state clearly that the number of connections grows far faster than the number of computers
> 
> Do not accept "the central switch would be overloaded", because a mesh topology has no central switch

> **[exam-tip]**
> When the stem gives you a requirement, such as "the monitoring must keep working even if part of the network fails", your answer has to use it. Marks for justifying a topology are given for linking a feature of that topology to the requirement in the stem, not for listing advantages you have memorised.
> 
> The second half of this question is where mesh answers usually lose marks. Do not write "it costs more" and stop. Say why it costs more: the number of connections grows much faster than the number of devices.

### Q9
**Final answer:** **28 connections**

Each server must be connected to the other 7 servers. **[1]**

8 servers x 7 connections each = 56 **[1]**

Each connection has been counted twice, once at each end, so 56 / 2 = 28 **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each server needing 7 connections // for stating that each server connects to every other server
> 
> **1 mark** for 8 x 7 = 56 // for using n(n - 1) / 2 with n = 8
> 
> **1 mark** for the final answer of 28
> 
> Accept 28 with correct working set out in any order
> 
> Accept a correct count taken from a labelled diagram
> 
> Do not accept 56, which counts every connection twice, once at each end
> 
> Do not accept 64, which comes from 8 x 8 and connects each server to itself

> **[exam-tip]**
> The trap here is doubling. Every connection has two ends, so multiplying the number of devices by the number of connections each device needs counts every connection twice. Always halve at the end.
> 
> This calculation is the reason a full mesh is rarely used for a large network. Eight servers need 28 connections, but sixteen servers need 120. The amount of cabling grows far faster than the number of devices.

### Q10
The documents are held on the provider's remote servers, so a volunteer in any of the five countries can open them from any device with an internet connection. **[1]**

Every volunteer works on the same stored copy, so an update made by one volunteer is seen by the others and the charity does not have to send files from country to country. **[1]**

The provider carries out the backups, so the charity does not have to buy backup hardware or pay someone to manage it. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** each, to a maximum of 3, from the following.
> 
> **1 mark** for the documents can be accessed from anywhere with an internet connection
> 
> **1 mark** for the volunteers share one stored copy, so several people can work on the same document and see each other's changes
> 
> **1 mark** for the provider performs the backups, so the charity needs no backup hardware or staff of its own
> 
> **1 mark** for the provider manages the security, so the charity does not have to install and maintain it
> 
> **1 mark** for storage capacity can be increased on demand as the number of documents grows, without buying storage devices
> 
> Accept "small amounts of storage are often free" as a cost benefit
> 
> Do not accept "it is faster", because the transfer speed depends on each volunteer's internet connection and may be slower than local storage
> 
> Do not accept two wordings of the same benefit, for example "accessible anywhere" and "accessible from any country", as two separate points

> **[exam-tip]**
> Three marks means three different benefits. The most common way to lose a mark here is to write one benefit twice, once as "it can be used anywhere" and once as "volunteers in other countries can use it". Those are one point, not two.
> 
> Tie each benefit to the charity in the question. An examiner reading "you can access it anywhere" learns nothing about five countries; "a volunteer in any of the five countries can open the same document" clearly answers what was asked.

### Q11
Every computer is connected directly to at least one other computer, and in a full mesh to every other computer. **[1]**

There is more than one route between any two computers. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** each, to a maximum of 2
> 
> **1 mark** for all devices being connected directly to at least one other device // for every device being connected to every other device in a full mesh
> 
> **1 mark** for there being multiple routes between any two devices
> 
> **1 mark** for the devices acting as relays, passing packets on towards the final destination
> 
> **1 mark** for there being no central device
> 
> Do not accept "all devices are connected to a central cable", which describes a bus topology
> 
> Do not accept "it is reliable" on its own, which is an advantage rather than a characteristic of the layout

> **[exam-tip]**
> A characteristic describes how the network is laid out or how data moves through it. An advantage says why that is useful. Questions on this topic ask for one or the other, and an advantage written where a characteristic is asked for scores nothing. Check which word the stem uses before you write.

### Q12
Benefit: the student can open the files from any computer that has an internet connection, so a memory stick left at home no longer matters. **[1]**

Drawback: the files cannot be opened at all when there is no internet connection. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for a correct benefit, from: can be accessed from anywhere with an internet connection // the provider carries out the backups so the student does not have to // storage capacity can be increased easily // files can be shared with other students // small amounts of storage are often free // no separate storage device has to be bought
> 
> **1 mark** for a correct drawback, from: cannot be accessed without an internet connection // the student has no control over the provider's security // the student has no control over whether backups are taken // access is lost if the provider's server fails // free storage is limited and extra capacity must be paid for // uploading and downloading large files can be slow
> 
> Accept "a third party" for "the provider"
> 
> Do not accept "it is cheaper" on its own as a benefit, because the cost depends on how much storage is used; "small amounts of storage are often free" is credited
> 
> Accept "the provider's security may be weaker / the files could be hacked on the provider's server" as a drawback

> **[exam-tip]**
> Read the number of marks and match it to the number of points asked for. This question wants one of each, so a page of benefits with no drawback still scores only one mark.
> 
> Answers such as "it is safer" or "it is faster" are too vague to credit. Name the thing that actually changes: where the files are held, who looks after the backups, or what happens when the connection drops.

### Q13
A new computer is added by running one new cable from it to the switch. **[1]**

The rest of the network keeps running while this is done, because no existing device shares that cable. **[1]**

A fault on one cable stops only the device on that cable, so the faulty cable is found quickly by seeing which computer has lost its connection. **[1]**

The problem to plan for is that the switch is a single point of failure. If it fails, all twenty-five computers lose their connection. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** each, to a maximum of 4
> 
> **1 mark** for a new device being added by connecting one new cable to the switch
> 
> **1 mark** for the existing devices being unaffected while the new device is added
> 
> **1 mark** for a fault affecting only the device on the faulty cable, which makes the fault quick to locate
> 
> **1 mark** for identifying the switch as a single point of failure // for the switch needing enough free ports for twenty-five devices
> 
> Accept "the whole network stops if the switch fails" for the fourth point
> 
> Do not accept "the network is faster" as an answer to either requirement, because speed is not one of the two requirements given in the stem

> **[exam-tip]**
> The command word is "explain", so every advantage needs a reason attached. "It is easy to add a computer" is half a marking point. "It is easy to add a computer, because only one new cable to the switch is needed and no other device is disconnected" is the whole of it.
> 
> The final sentence of the stem asks for a problem, so do not leave it out. A star topology answer that never mentions the central device as a single point of failure is incomplete, and that is the mark most often dropped on this topic.

### Q14
The saved progress is stored on the game provider's remote servers rather than on either of the two computers. **[1]**

When the player stops playing, the progress is transmitted over the internet from the first computer and stored on those servers. **[1]**

The player signs in on the second computer with the same credentials, so the servers can identify which player's saved progress to send. **[1]**

The second computer has an internet connection, so it can request that saved progress from the same servers and the game continues from the point that was saved. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the saved progress being held on the provider's remote server, not on the player's own computer
> 
> **1 mark** for the progress being uploaded over the internet from the first computer when the player stops
> 
> **1 mark** for the player signing in with the same account or credentials, so the correct saved data is identified
> 
> **1 mark** for the second computer downloading that saved progress over the internet, so play continues from the same point
> 
> Accept "the same user account" for credentials
> 
> Accept "any device with an internet connection can reach the same server" for the fourth mark
> 
> Do not accept "the progress is copied from the first computer to the second computer", because the two computers never communicate directly
> 
> Do not accept "the game saves automatically" on its own, because it does not say where the data is stored

> **[exam-tip]**
> The mistake to avoid is describing a transfer between the two computers. Nothing passes directly between them. Every step goes through the provider's remote server, and an answer that leaves the server out cannot reach full marks.
> 
> Do not overlook the sign-in step either. The remote server holds saved progress for very many players, so something has to tell it whose data to send back. Naming the account or the credentials is worth a mark on its own.

### Q15
If one cable is damaged, only the computer on that cable loses its connection. **[1]**

The other eleven computers can still communicate, because each of them has its own separate cable to the central device. **[1]**

If the central device fails, no computer can communicate with any other, because every packet on a star network has to pass through the central device. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** each, to a maximum of 3
> 
> **1 mark** for only the one computer being disconnected when its cable is damaged
> 
> **1 mark** for the rest of the network being unaffected, because each device has its own separate cable to the central device
> 
> **1 mark** for no device being able to communicate when the central device fails
> 
> **1 mark** for the reason that every packet has to pass through the central device // the central device is a single point of failure
> 
> Accept "the switch" or "the router" in place of "the central device"
> 
> Do not accept "the whole network stops working" as the effect of the damaged cable, which is the behaviour of a bus topology

> **[exam-tip]**
> Two failures, two different answers. That is exactly what this question tests, and students who have learned "a star topology is reliable" as one fixed sentence tend to give the same answer twice.
> 
> Say which devices are affected and give the reason. "The network still works" on its own earns one mark at most. The second mark comes from saying that each device has its own separate cable to the centre.

### Q16
When the file is opened, the laptop sends a request over the internet to the cloud provider's remote server. **[1]**

The server locates the file and transmits a copy of it back to the laptop, where the employee can work on it. **[1]**

When the file is saved, the changed version is transmitted back over the internet and stored on the remote server, so the copy held by the provider becomes the up-to-date one. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the laptop sends a request over the internet to the provider's remote server
> 
> **1 mark** for a copy of the file is transmitted from the remote server to the laptop
> 
> **1 mark** for the edited file is transmitted back and stored on the remote server // the version held on the remote server is updated
> 
> Accept "downloaded" for transmitted to the laptop and "uploaded" for transmitted back
> 
> Accept "the file is opened in a browser and edited there" for the second mark
> 
> Do not accept "the file is saved on the laptop's hard disk", because the stored copy is held on the provider's remote server
> 
> Do not accept "the file moves to the cloud", because it does not describe a transmission over the internet

> **[exam-tip]**
> The command word is "describe", so the marks are for the steps, not for a general statement that the file is "in the cloud". Write the journey: request out, copy back, edited copy returned.
> 
> Students often answer only the first half and lose the third mark. If a question names two actions, opening and saving, there is at least one mark attached to each of them.

### Q17
**Final answer:** **central, switch**

In a star topology, every device on the network has its own cable connecting it to one **central** device. **[1]**

On a modern local area network this device is usually a **switch**, which reads the destination address of a packet and sends the packet only to the device it is addressed to. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for central
> 
> **1 mark** for switch
> 
> Accept router for the second space
> 
> Do not accept hub for the second space. A hub sends every packet to every device on the network, so it does not match the description given in the sentence

> **[exam-tip]**
> Hub and switch are not interchangeable in this syllabus. A hub forwards a packet to every device and each device then decides whether to keep it. A switch reads the destination address and forwards the packet to that one device only. Any wording such as "only to the intended device" is describing a switch.

### Q18
Every machine loses the ability to communicate, not only machines 4 and 5. **[1]**

This is because all data has to travel along the one shared cable, and the cut has split that cable into two separate lengths. **[1]**

Neither length now has a terminator at the cut end, so signals reflect back along the cable. **[1]**

The reflected signals corrupt the data, so even two machines on the same side of the cut cannot communicate reliably. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** each, to a maximum of 4
> 
> **1 mark** for the whole network failing, rather than only the machines next to the break
> 
> **1 mark** for all data having to travel along the one shared cable, which is now in two separate parts
> 
> **1 mark** for the cut ends no longer being terminated, so signals reflect back along the cable
> 
> **1 mark** for the reflected signals corrupting data, so machines on the same side of the break are affected as well
> 
> **1 mark** for the fault being hard to locate, because every machine reports the same symptom
> 
> Accept "no machine can reach a machine on the other side of the break" for the first point
> 
> Do not accept "only machines 4 and 5 are affected"
> 
> Do not accept "the data is sent by another route", because a bus topology has only one route

> **[exam-tip]**
> Students often assume that the two halves of a cut bus network carry on working as two smaller networks. They do not. The cut ends are no longer terminated, so reflected signals corrupt the traffic on both halves.
> 
> The one shared cable is what defines this topology and it is also its weakness. When a question describes damage to a bus network, the examiner wants you to say that the whole network stops, and to give the reason, not just to name the machines closest to the damage.

### Q19
Cloud computing is the provision of computing services, such as data storage and software, by a provider on remote servers. **[1]**

The user accesses these services over the internet instead of holding the data or installing the software on their own computer. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for computing services provided on a remote server // on servers belonging to a provider // accessing files, software or a service on a remote server
> 
> **1 mark** for accessed over the internet // rather than being held or installed on the user's own computer
> 
> Accept "storage and/or software supplied by a third-party provider" for the first mark
> 
> Accept "reached online from any device with an internet connection" for the second mark
> 
> Award both marks for "accessing a service, files or software on a remote server". Accessing it on a remote server covers the first mark, and "remote" means it is not held on the user's own computer, which covers the second mark
> 
> "Saving files on the internet" on its own earns the second mark only, because it names neither the remote server nor the provider
> 
> Do not accept "a very large hard disk" or "a folder that backs up automatically", because both describe local storage rather than cloud computing

> **[exam-tip]**
> The mark scheme wants the words "remote server". Many students write that cloud computing means "saving files online", which describes the result rather than the arrangement, and it earns one mark at most. Say where the data or software actually sits, then say how the user reaches it.
> 
> A second common slip is to define cloud computing as storage only. The syllabus includes running applications as well, so mentioning software alongside data keeps you safe when the question is about a program rather than a file.

### Q20
Computer 1 places the packet onto the single shared cable and the signal travels along the cable. **[1]**

The packet therefore passes every computer on the network, not only computer 5. **[1]**

Each computer reads the destination address held in the packet. Computer 5 finds that the address matches its own and accepts the packet, and every other computer ignores it. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** each, to a maximum of 3
> 
> **1 mark** for the sending computer placing the packet onto the single shared cable // backbone
> 
> **1 mark** for the signal travelling along the cable so that it reaches all of the other devices
> 
> **1 mark** for each device reading the destination address held in the packet
> 
> **1 mark** for only the device whose address matches accepting the packet, and all other devices ignoring it
> 
> Accept "the packet is broadcast to every device on the cable" for the second point
> 
> Do not accept an answer in which a central device or a switch decides where the packet goes, because a bus topology has no central device

> **[exam-tip]**
> A common error is to describe the packet travelling only as far as computer 5 and then stopping. It does not. On a bus network the signal passes every device on the cable, and it is the devices, not the cable, that decide whether to accept it.
> 
> Read the topology named in the stem before you write. Students who have revised star topologies often answer "the switch forwards the packet to computer 5". There is no switch in a bus topology, so that answer earns nothing.

### Q21
All devices are connected to one central cable. **[1]**

There is no central device such as a switch. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for all devices being connected to one central cable // one single shared cable
> 
> **1 mark** for there being no central device such as a switch
> 
> Accept "every device is attached to the same cable" or "a backbone cable" for the first point
> 
> Accept the cable having a terminator at each end, to stop signals reflecting back, in place of either point
> 
> Do not accept "all devices are connected to each other", which describes a mesh topology
> 
> Do not accept "all devices are connected to a central device", which describes a star topology

> **[exam-tip]**
> The word "bus" has two different meanings in this syllabus, and they are easy to confuse. The address bus and data bus inside a processor are not the same thing as a bus network topology. In a network question, "bus" means the one shared cable that every device is attached to.
> 
> Watch the words "connected to". In a bus topology the devices are connected to the cable, not to one another. An answer that says "every computer is connected to every other computer" describes a mesh topology and scores nothing here.

### Q22
A and B are on the same network, so the data packet does not need to cross from one network to another. **[1]**

The switch reads the destination MAC address of B in the data packet and forwards the data packet straight to B, so the data packet never reaches the router. **[1]**

C is on a different network, and forwarding a data packet from one network to another network is a task that only the router can perform. **[1]**

The router reads the destination IP address in the header of the data packet and uses its routing table to decide which network to send the data packet to next. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for stating that A and B are on the same network, so no movement between networks is needed
> 
> **1 mark** for the switch using the MAC address to forward the data packet directly to B
> 
> **1 mark** for stating that C is on a different network, and that moving a data packet between networks is the router's task
> 
> **1 mark** for the router reading the destination IP address and using its routing table to choose where to send the data packet next
> 
> Accept "the switch sends it out of the port that B is connected to" for the second mark
> 
> Accept "the router chooses the next network, or the next router, on the route to C" for the fourth mark
> 
> Do not accept "the router is slower" or "the router is further away". Distance and speed are not the reason; the reason is that A and B are on the same network
> 
> Do not accept "the switch uses the IP address of B", because a switch identifies a device on the LAN by its MAC address

> **[exam-tip]**
> This question is really asking one thing: what makes a router necessary. A router is needed only when a data packet has to leave one network and enter another. If the sender and the receiver are on the same network, the switch alone can deliver the data packet, so the router is never involved.
> 
> Build every answer on this topic from the address type. Inside the LAN the device is found by MAC address, using the switch and its lookup table. Between networks the network is found by IP address, using the router and its routing table. Students who mix the two lose marks even when the rest of the answer is sound.

### Q23
Data is sent and received as radio signals, so no cable is needed between the laptop and the network. **[1]**

The device connects to the nearest cell tower, also called a base station, which serves the cell that the device is currently inside. **[1]**

As the researcher travels, her device automatically switches to the next nearest tower, so the connection continues as she moves from one cell into another. **[1]**

A drawback is that a remote site may be a long way from any tower, so the signal may be weak or missing. The connection may then be lost, or run at a low data transfer rate. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for wireless transmission: the data travels as radio signals, so no physical cable is required at the site
> 
> **1 mark** for the tower: the device connects to the nearest cell tower / base station, which serves the cell the device is in
> 
> **1 mark** for the switch between cells: as the user moves, the device automatically changes to the next nearest tower so that the connection is not lost
> 
> **1 mark** for a drawback tied to a remote site: the site may lie outside the coverage of any tower, or far from one, so the signal is weak or absent // there are fewer towers, so the data transfer rate is lower than a wired connection would give
> 
> Accept "mast" or "base station" in place of "cell tower"
> 
> Accept "the connection drops when she moves out of coverage" for the drawback
> 
> Do not accept "the laptop connects to a satellite". This is a cell phone network, and the link is made to a tower on the ground.
> 
> Do not accept "there is no internet at a remote site" as the drawback. The question states that she does connect, so the drawback has to be about the quality or the coverage of that connection.
> 
> **[4 marks]**

> **[exam-tip]**
> Students who have learned the generations 2G, 3G, 4G and 5G often write about them here and earn nothing, because the question asks how the connection is made, not how fast each generation is.
> 
> The three marks for the method are radio signals, the nearest tower, and the automatic switch between towers as the user moves. Save the point about speed for the drawback, and tie it to the remote site the question actually gives you.

### Q24
| Task | Performed by the switch | Performed by the router |
|---|---|---|
| Forwards a data packet to a device on a different network |   | **✔** |
| Uses a MAC address to send a data packet to one device on this LAN | **✔** |   |
| Assigns a private IP address to each device on this LAN |   | **✔** |

Row 1 **[1]** Row 2 **[1]** Row 3 **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for row 1 ticked as performed by the router
> 
> **1 mark** for row 2 ticked as performed by the switch
> 
> **1 mark** for row 3 ticked as performed by the router
> 
> Accept any clear mark in the correct box
> 
> Do not award a mark for a row with two boxes ticked
> 
> Do not award a mark for a row left blank

> **[exam-tip]**
> Confusing the switch with the router is the most common error in this whole topic, and the fix is one sentence for each. A switch moves data inside one network and uses MAC addresses. A router moves data between two networks and uses IP addresses.
> 
> Row 3 catches students out because the word "LAN" appears in it. Work from the address type instead of from the word: anything that involves an IP address is the router's job, even when the devices are all inside the LAN.

### Q25
A dedicated line is reserved for this company alone, so the connection is not shared with other users and the company does not have to compete with them for bandwidth. **[1]**

A dedicated line is permanently active, so a connection does not have to be set up through switching centres each time data is sent, as it is on the PSTN. **[1]**

Together these give a higher and more consistent data transfer rate, which matters here because the two offices send large files every day. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for exclusive use: the line is used only by this company // it is not shared with other users // there is no competition for the available bandwidth
> 
> **1 mark** for availability: the connection is always active / permanently open, instead of being routed through switching centres for each communication as it is on the PSTN
> 
> **1 mark** for the consequence for this company: a higher or more consistent bandwidth / data transfer rate, or a more reliable connection, which suits sending large files every day
> 
> Accept "guaranteed bandwidth" for the third marking point
> 
> Accept a reference to the dedicated line being fibre-optic and so offering a higher bandwidth than the copper telephone lines of the PSTN
> 
> Do not accept "it is faster" with no reason given. The reason has to be that the line is not shared, or that it is always available.
> 
> Do not accept "it is cheaper". A dedicated line costs the company more, which is the reason the company has to weigh it up at all.
> 
> Do not accept "the PSTN cannot send data". The PSTN carries the company's data now; the question is how well it does so.
> 
> **[3 marks]**

> **[exam-tip]**
> The trap in this question is answering it as a list of good things about fast connections. Every marking point has to come from one difference: a shared, switched network against a line that belongs to a single customer. If your sentence would be equally true of any internet connection, it is not a comparison and it will not earn a mark.
> 
> Watch the cost as well. Students often write that a dedicated line saves money, when the company is in fact paying extra for it.

### Q26
The connection between the two factories is a wide area network (WAN), because it covers a large geographical area. **[1]**

Data sent between the factories travels a far greater distance and passes through many more intermediate connections than data sent inside one factory, so it takes longer to arrive and the data transfer rate is lower. **[1]**

Inside one factory the company owns all of the cabling and equipment, so the LAN is private and protection is easier to implement. **[1]**

Between the countries the company does not own the transmission media. External or public infrastructure is used, such as lines leased from a telecommunications company or a satellite link, so the data passes through equipment the company cannot control. **[1]**

**[4 marks]**

> **[mark-scheme]**
> Maximum 2 marks for the data transfer rate and maximum 2 marks for protection.
> 
> **1 mark** for identifying the link between the factories as a WAN, or as a network covering a large geographical area
> 
> **1 mark** for the greater distance, or the greater number of intermediate connections, causing a lower data transfer rate than the LAN
> 
> **1 mark** for the LAN inside a factory being privately owned by the company, which makes protection easier to implement
> 
> **1 mark** for the WAN using external or public infrastructure the company does not own, so the data travels through equipment outside its control
> 
> Accept a named example of external infrastructure, such as leased telephone lines, fibre-optic cable owned by a telecommunications company, or satellite
> 
> Accept "the data passes through other organisations' equipment" for the fourth mark
> 
> Do not accept "a WAN is slower" with no reason given
> 
> Do not accept "WANs are not secure", because a WAN can be protected; the mark is for saying why protection is harder

> **[exam-tip]**
> Both halves of this answer come from the same two facts: a WAN covers a large geographical area, and a WAN runs on infrastructure the organisation does not own. Learn those two facts and you can build the speed answer and the protection answer from them.
> 
> The commonest error is writing that a WAN is slower and less secure without giving any cause. The mark is never for the label, it is for the reason attached to it.

### Q27
(i) The header of the data packet, which holds the destination IP address **[1]**

(ii) The routing table **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** in (i) for the header // the destination IP address in the header
> 
> **1 mark** in (ii) for the routing table
> 
> Accept "destination address" on its own in (i)
> 
> Do not accept "the payload" or "the data" in (i). The payload is the data being carried and the router does not read it
> 
> Do not accept "the lookup table of MAC addresses" in (ii), because that is what a switch stores, not a router

> **[exam-tip]**
> A data packet has two parts and the exam expects you to name them correctly. The header carries the addresses and the control information; the payload carries the data being sent. A router reads only the header.
> 
> Say "routing table" rather than "table of addresses". Cambridge uses the exact term in its mark schemes, and a vague answer such as "a list of routes" is not credited.

### Q28
The modem converts the digital signal produced by the computer into an analogue signal, so that the telephone line is able to carry it. **[1]**

The modem also converts the analogue signal that arrives from the telephone line back into a digital signal, so that the computer can use the data. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for modulation: converts the digital data / signal from the computer into an analogue signal that can be sent along the telephone line
> 
> **1 mark** for demodulation: converts the analogue signal received from the telephone line back into digital data / a digital signal for the computer
> 
> Accept "modulates" and "demodulates" in place of the two conversions, provided the direction of each one is stated
> 
> Do not accept "modem stands for modulator-demodulator" on its own. Expanding the name is not a description of the role.
> 
> Do not accept "it connects the computer to the internet" or "it gives the computer a signal". Neither one says what the modem changes.
> 
> Do not accept an answer that gives only one direction. Two marks require both conversions.
> 
> **[2 marks]**

> **[exam-tip]**
> Almost every lost mark here is a one-way answer. Students describe the digital to analogue conversion and then stop. The word modem holds both halves, modulator and demodulator, so a two-mark answer needs both directions, and each direction has to name the signal type it produces.
> 
> Naming the parts of the word is not a description. The examiner wants the conversion, not the abbreviation.

### Q29
| Characteristic | LAN | WAN |
|---|---|---|
| Geographical area covered | **Small, for example one building or one site** | **Large, for example a whole country or several countries** **[1]** |
| Ownership of the transmission media | **Owned by the organisation that uses the network** | **Not all owned by the organisation; external or public infrastructure is used, such as lines leased from a telecommunications company** **[1]** |
| Typical data transfer rate | **High** | **Low** **[1]** |

One mark is awarded for each fully correct row.

**[3 marks]**

> **[mark-scheme]**
> 1 mark per row. Both cells in a row must be correct for the mark.
> 
> **1 mark** for a small area, such as one building or one site, against a large area, such as a country or several countries
> 
> **1 mark** for the media being owned by the organisation using the LAN, against the WAN using media the organisation does not own, such as public or leased infrastructure
> 
> **1 mark** for a high data transfer rate against a low data transfer rate
> 
> Accept "private" for LAN ownership and "public or private" for WAN ownership
> 
> Accept "fast" and "slow" for the data transfer rate row
> 
> Do not accept a distance in miles or kilometres on its own as a description of the area covered
> 
> Do not accept "a WAN is bigger" in the ownership row, because it repeats the first row

> **[exam-tip]**
> Each row is marked as a pair, so a correct LAN cell beside a blank or wrong WAN cell earns nothing. Fill in both cells even when you are unsure of one, and make the two cells genuinely contrast.
> 
> The ownership row is the one most often lost. A WAN is not simply "owned by someone else": the organisation still owns the LAN at each end, and it is the connection between the sites that runs on infrastructure it does not own.

### Q30
**Fault 1:** the Network Interface Card (NIC) in that one computer has failed. **[1]**

Only that computer is affected, and the NIC is the only device in the LAN that serves that computer alone. The switch and the cables to it must still be working, because the other 23 computers can still communicate. **[1]**

**Fault 2:** the Wireless Access Point (WAP) has failed. **[1]**

The WAP is the only device that lets a wireless device join the wired LAN, so a failure there stops every laptop. The switch must still be working, because the wired computers can still reach each other and the server. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for identifying the Network Interface Card, or NIC, of that computer in Fault 1
> 
> **1 mark** for a valid reason in Fault 1: only that one computer is affected // the NIC is the only device used by that computer on its own // the switch must be working because the other computers still communicate
> 
> **1 mark** for identifying the Wireless Access Point, or WAP, in Fault 2
> 
> **1 mark** for a valid reason in Fault 2: the WAP is the only device that connects wireless devices to the wired LAN // every wireless device fails and every wired device works // the switch must be working because the wired computers still communicate
> 
> Accept "network card" for NIC
> 
> Accept "access point" for WAP
> 
> Do not accept "the switch" in Fault 1. A failed switch would stop all 24 computers, not one
> 
> Do not accept "the WNIC in the laptop" in Fault 2, because that would stop one laptop, not every laptop
> 
> Do not accept a reason that only restates the fault, for example "because that computer cannot connect"

> **[exam-tip]**
> Fault-finding questions are marked on the reason, not the guess. The reason always comes from what is still working. If one device out of 24 fails, the fault has to be in the part that belongs to that one device. If everything wireless fails while everything wired still works, the fault has to be in the one device that joins the wireless side to the wired side.
> 
> The common error in Fault 2 is to name the WNIC in a laptop. Read the fault again: no laptop can connect, so a single card in a single laptop cannot be the cause.

### Q31
| Stage | Order |
|---|---|
| The domain name is taken from the URL and sent to a DNS server. | **3** **[1]** |
| The web browser sends a request for the web page to the web server at that IP address. | **6** **[1]** |
| The user types the URL into the address bar of the web browser. | 1 |
| The IP address is sent back to the web browser. | **5** **[1]** |
| The DNS server does not hold the domain name, so it passes the request on to a higher-level DNS server. | **4** **[1]** |
| The web browser checks its cache to see whether it already holds the matching IP address. | **2** **[1]** |

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for `2` against the web browser checking its cache
> 
> **1 mark** for `3` against the domain name being sent to a DNS server
> 
> **1 mark** for `4` against the request being passed on to a higher-level DNS server
> 
> **1 mark** for `5` against the IP address being sent back to the web browser
> 
> **1 mark** for `6` against the web browser requesting the web page from the web server
> 
> Mark each row on its own. A student who gets one row wrong can still earn the other marks.
> 
> Do not accept an ordering in which the cache is checked after a DNS server is contacted.
> 
> Do not accept an ordering in which the web page is requested from the web server before the IP address is returned.
> 
> Do not accept a number used twice.

> **[exam-tip]**
> Two rows catch students out. The cache check comes second, before any DNS server is contacted, because if the browser already holds the address there is no need to ask anyone. The higher-level DNS server comes before the address is returned, because that is how the address is found in the first place.
> 
> A useful check is that the last stage is always the browser asking the web server for the page. Everything before it exists only to find out which address to ask.

### Q32
The internet is the infrastructure. It is the global network of interconnected networks, made up of the connections and devices that carry data between computers around the world. **[1]**

The World Wide Web is only one of the services that runs on that infrastructure. It is the collection of websites and web pages that are stored on web servers. **[1]**

Removing the World Wide Web would remove the web pages, but the networks underneath would still exist and would still carry data. The web depends on the internet; the internet does not depend on the web. **[1]**

Email would still work, because an email is delivered across the internet by an email application and does not need a web page. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the internet described as the underlying infrastructure // the global network of networks that carries the data
> 
> **1 mark** for the World Wide Web described as one service that uses the internet // a collection of websites / web pages held on web servers, rather than the network itself
> 
> **1 mark** for the consequence: losing the web pages would not remove the network connections, so data could still be transmitted // the dependency runs one way only, from the web to the internet
> 
> **1 mark** for a named service that does not use web pages: email sent through an email application // a messaging application // transferring a file directly between two computers
> 
> Accept "the World Wide Web depends on the internet but the internet does not depend on the World Wide Web" for the third marking point
> 
> Do not accept a website, an online shop, a search engine or a social media site as the example. Each of these is part of the World Wide Web, so each would stop working too.
> 
> Do not accept email that is read inside a web browser as the example, for the same reason.
> 
> Do not accept "the internet is bigger than the World Wide Web" on its own. The answer must say what each of the two is.

> **[exam-tip]**
> This question tests one idea only: which of the two depends on the other. The World Wide Web needs the internet. The internet does not need the World Wide Web.
> 
> The fourth mark is the one students throw away, by naming a website as their example. A website is the one kind of service that would stop. Pick something you use without opening a browser.

### Q33
A LAN covers a small geographical area, such as a single building or a single site. **[1]**

The hardware and the transmission media are owned by the organisation that uses the network. **[1]**

**[2 marks]**

> **[mark-scheme]**
> 1 mark per characteristic, to a maximum of 2
> 
> **1 mark** for covering a small geographical area, for example one building or one site
> 
> **1 mark** for the hardware and transmission media being owned by the organisation using the network, so ownership is private
> 
> **1 mark** for the connections between devices usually being physical, using cable owned by the organisation
> 
> **1 mark** for a high data transfer rate
> 
> **1 mark** for being easier to protect than a network that covers a large area
> 
> Accept "one site", "one building" or "one office" for a small geographical area
> 
> Do not accept "a network with only a few computers", because the number of devices is not what defines a LAN
> 
> Do not accept "it uses Wi-Fi", because wireless connections are not limited to a LAN

> **[exam-tip]**
> Characteristics of a LAN are about area, ownership and speed, not about how many computers are attached. A university LAN can have thousands of devices and is still a LAN, because it sits on one site.
> 
> Learn the LAN and WAN characteristics as matching pairs: small area against large area, private ownership against external infrastructure, high data transfer rate against low. Mark schemes are written in exactly those pairs.

### Q34
The sending computer transmits the data packet directly to the switch. **[1]**

The switch checks the destination address (the MAC address) that is stored in the data packet. **[1]**

It then forwards the data packet directly to that device only, out of the port that device is connected to, so the data packet reaches the destination computer and no other computer on the LAN receives it. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the sending computer transmitting the data packet directly to the switch // the switch receiving the data packet
> 
> **1 mark** for checking or reading the destination address of the data packet
> 
> **1 mark** for forwarding the data packet directly to that one device only
> 
> Accept "destination MAC address" for the second mark
> 
> Accept "sends it out of only the port that device is connected to" for the third mark
> 
> Do not accept "sends the data packet to every device attached to it", which describes the opposite behaviour
> 
> Do not accept "uses its routing table", because a routing table belongs to a router

> **[exam-tip]**
> Three marks means three separate steps: the switch receives the data packet, checks its destination address, then sends it to that one device. Students often write only "the switch sends the data to the right computer", which is the outcome, not the method, and earns one mark at most.
> 
> The single sentence that separates a switch from every other LAN device is that it sends the data packet to one device instead of copying it to every connection. Write that sentence and the third mark is safe. Also keep the switch and the router apart: a routing table belongs to the router, not to the switch.

### Q35
The domain name is taken from the URL and sent to a DNS server. **[1]**

The DNS server searches its index of domain names and their matching IP addresses. **[1]**

When the domain name is found, the matching IP address is sent back to the web browser. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the domain name being taken from the URL and sent to a DNS server
> 
> **1 mark** for the DNS server searching its index of domain names and their matching IP addresses
> 
> **1 mark** for the matching IP address being sent back to the web browser
> 
> Also accept, for one mark: if the DNS server does not hold the domain name, it passes the request on to a higher-level DNS server. Maximum 3 marks.
> 
> Accept list, table or database in place of index.
> 
> Do not accept that the DNS server sends the web page back to the browser. A DNS server returns an IP address only.
> 
> Do not accept that the browser checks its cache. The question states this has already happened and failed.

> **[exam-tip]**
> The commonest error on this question is writing that the DNS server sends back the web page. It sends back an address. The browser then makes a second, separate request to the web server at that address for the page itself.
> 
> Read the stem before you start writing. It tells you the cache has already been checked, so a first line about checking the cache earns nothing.

### Q36
Hana is using the internet only. **[1]**

She is using the internet because the message data is carried between her phone and her friend's phone over the global network of networks that joins the two countries. **[1]**

She is not using the World Wide Web because no web page held on a web server is being requested or displayed. The application sends the message itself; it does not fetch a page for a browser to show. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for identifying that she is using the internet only // that she is not using the World Wide Web
> 
> **1 mark** for justifying the internet: the message data travels over the internet infrastructure / the global network of networks that connects her phone to her friend's phone
> 
> **1 mark** for justifying the World Wide Web: no website / web page stored on a web server is requested or viewed
> 
> Accept "she is not using a browser to open a web page" for the third marking point
> 
> Do not accept "both". Sending a message through an application that is not a browser does not involve web pages.
> 
> Do not accept "she is using the World Wide Web because the message travels over the internet". That reverses the relationship. The World Wide Web runs on the internet; the internet does not need the World Wide Web.
> 
> Do not accept a justification that only repeats the word chosen, such as "she is using the internet because she is online".
> 
> **[3 marks]**

> **[exam-tip]**
> "Both" is the correct answer when the person opens something in a browser, and it is the wrong answer here. Read the stem for the give-away. If a website or a browser is mentioned, web pages are involved and the answer is both. If the data moves through an application of its own, only the internet is involved.
> 
> Give a separate reason for each of the two terms. A single sentence that mentions both usually earns only one of the two justification marks.

### Q37
Improvement: one network manager can set access rights centrally, **[1]** so each member of staff can only open the files their job requires, and files no longer travel on removable devices that can be lost or stolen. **[1]**

Greater risk: the computers are now connected, so malware that reaches one computer can spread across the network to the other 39. **[1]** Before the network was installed, an infection on one computer could only reach another computer if someone carried it there on a removable device. **[1]**

**[4 marks]**

> **[mark-scheme]**
> Maximum 2 marks for the improvement and maximum 2 marks for the risk.
> 
> **1 mark** for naming a security improvement: central control of access rights, or one central backup of all data, or removing the need to carry data on removable devices
> 
> **1 mark** for developing that improvement: only authorised staff can open a file, or every file is backed up to the same schedule, or a lost device no longer exposes company data
> 
> **1 mark** for naming a security risk: malware spreading from one computer to every other, or one stolen set of login details reaching data across the whole network, or the whole network being exposed through a single point of attack
> 
> **1 mark** for developing that risk by comparing it with the separate computers, for example that an infection or a stolen password previously reached one computer only
> 
> Accept the improvement and the risk in either order
> 
> Do not accept "hackers can get in" with no statement of what the network makes possible
> 
> Do not accept a benefit that is not about security, such as sharing a printer, even though it is correct

> **[exam-tip]**
> This question is marked in two halves, so an answer that gives four excellent points about risk can still only score 2. Split your writing before you start: two lines for the improvement, two lines for the risk.
> 
> The second mark in each half is the one students lose. Naming central backup earns one mark; saying why that is safer than 40 people each remembering to back up earns the second. Always add the "which means that" sentence.

### Q38
A DNS server stores an index of domain names and their matching IP addresses. **[1]**

It is used to translate the domain name taken from the URL into the IP address of the web server that holds the page. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for stating that a DNS server stores an index of domain names and their matching IP addresses
> 
> **1 mark** for stating that it translates a domain name into the matching IP address
> 
> Accept for the first mark: list, table, database, directory in place of index.
> 
> Accept for the second mark: converts, looks up, resolves in place of translates, and URL in place of domain name.
> 
> Do not accept that the DNS stores the web pages. The web pages are stored on the web server.
> 
> Do not accept that the DNS connects the user to the internet, or that it routes the data.

> **[exam-tip]**
> The error that costs marks here is describing the DNS as somewhere websites are kept. A DNS server holds no web pages at all. It holds pairs of domain names and addresses, and it hands back an address.
> 
> Two marks means two separate points, so do not write the same idea twice in different words. Say what a DNS server stores, then say what it does with it.

### Q39
(i) Wireless Network Interface Card (WNIC) **[1]**

(ii) Wireless Access Point (WAP) **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for Wireless Network Interface Card, or WNIC
> 
> **1 mark** for Wireless Access Point, or WAP
> 
> Accept "wireless NIC" in (i)
> 
> Accept "access point" in (ii)
> 
> Do not accept "NIC" or "Network Interface Card" on its own in (i), because that names the card used for a wired connection
> 
> Do not accept "router" in (ii). A router in a home or hotel often has a Wireless Access Point built into the same case, but the part that sends and receives the radio signals is the Wireless Access Point

> **[exam-tip]**
> Most students who lose the mark in (ii) write "router", because the single box they use at home does both jobs. Cambridge marks the two jobs separately, so always name the device that does the job described in the question. The Wireless Access Point provides the radio link into the wired network. The router forwards data packets between two networks.
> 
> Learn the two cards as a pair. A NIC gives a wired connection, a WNIC gives a wireless one, and each one gives its device a MAC address that identifies that device on the network.

### Q40
The internet is a global network of interconnected networks. It is the infrastructure that connects computers and networks all over the world. **[1]**

The World Wide Web is a collection of websites and web pages that are stored on web servers and accessed over the internet. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the internet described as a global network of networks // the worldwide infrastructure that connects separate networks together
> 
> **1 mark** for the World Wide Web described as a collection of websites / web pages / documents stored on web servers, which are accessed over the internet
> 
> Accept "a wide area network (WAN) that joins networks across the world" for the internet
> 
> Accept "the pages that a web browser requests from web servers" for the World Wide Web
> 
> Do not accept any answer that treats the two as the same thing, for example "the internet is the World Wide Web" or "both mean all of the websites in the world". The statement in the question is exactly what the answer has to contradict.
> 
> Do not accept "the internet is a web browser" or "the World Wide Web is a browser". A browser is the program used to view web pages; it is not the web and it is not the network.

> **[exam-tip]**
> Students lose a mark here by defining the internet using the word "web", or by describing both terms as "where you find information online". Keep the two definitions in different words. The internet is connections and hardware. The World Wide Web is pages and content.
> 
> A quick test before you move on: if your two sentences could be swapped over without changing the meaning, you have not stated a difference at all.

### Q41
The three films together need 3 x 8 = 24 megabits per second. **[1]**

This is more than the 20 megabits per second that the broadband connection can deliver, so the data arrives more slowly than it is played. **[1]**

Each buffer empties, so playback stops and restarts while each buffer refills. **[1]**

Reducing the bit rate of each film to 6 megabits per second would need only 18 megabits per second in total, which the connection can deliver. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for the total bit rate required, 3 x 8 = 24 megabits per second
> 
> **1 mark** for comparing it with the connection: 24 is greater than 20, so the data cannot arrive as fast as it is played
> 
> **1 mark** for the consequence: the buffer empties, so playback keeps pausing while the buffer refills
> 
> **1 mark** for one valid change:
> 
> - reduce the bit rate, resolution or quality of the films so that the total is 20 megabits per second or less
> - watch fewer films at the same time, so that at most two 8 megabits per second streams run together
> - change to a broadband connection with a download speed of at least 24 megabits per second
> 
> Accept any per-film bit rate for the fourth mark whose total is 20 megabits per second or less.
> 
> Accept "the stream buffers" or "the video freezes" for the third mark.
> 
> Do not accept "increase the size of the buffer". A larger buffer only covers a short dip in speed. Here the connection is 4 megabits per second short for as long as all three films are playing, so a larger buffer would empty as well; it would only take longer to do so.
> 
> Do not accept "the connection is too slow" on its own for the second mark, with no use of the figures 24 and 20.

> **[exam-tip]**
> Compare the total bit rate needed against the speed of the connection, not one stream against it. A single film at 8 megabits per second is comfortable on a 20 megabits per second line, and three at once are not. Whenever a question gives you a number of users and a bit rate each, multiply them before you say anything else.
> 
> "Make the buffer bigger" is a popular answer and it earns nothing here. A buffer helps when a connection is fast enough on average and dips for a moment. When the connection is too slow the whole time, the buffer empties whatever its size.

### Q42
One printer can be shared by all six computers, so the studio buys and maintains one printer instead of six. **[1]**

A single network licence for the photo editing software costs less than six separate single-user licences. **[1]**

One copy of each image file is kept for the whole studio instead of six copies, so less storage capacity has to be paid for. **[1]**

**[3 marks]**

> **[mark-scheme]**
> 1 mark per way, to a maximum of 3. The saving must be identified, not only the sharing.
> 
> **1 mark** for sharing one printer or other peripheral between the computers, so fewer devices are bought and maintained
> 
> **1 mark** for a network software licence costing less than a separate licence for each computer
> 
> **1 mark** for storing one copy of each file for the whole studio rather than a copy on every computer, reducing the storage that must be bought
> 
> **1 mark** for backing up the whole studio once rather than backing up six computers separately, saving staff time and backup media
> 
> **1 mark** for sending files over the network, so removable storage devices no longer have to be bought
> 
> Accept the shared item and the saving given in either order
> 
> Do not accept "sharing is cheaper" with nothing named as shared
> 
> Do not accept a benefit that does not save money, such as staff being able to send email

> **[exam-tip]**
> The command word is describe and the question names costs, so every point needs two halves: what is now shared, and what the studio therefore stops paying for. If you write "they can share a printer" and stop, you have given a benefit of networking but not answered a question about cost.
> 
> Software licensing is the point you are most likely to forget. Learn it as a benefit in its own right, because it appears in mark schemes far more often than you might expect.

### Q43
Both URLs contain the same domain name, `www.example.org`. **[1]**

The domain name names the server, so both web pages are stored on the same web server. **[1]**

The part of each URL after the domain name is different, `/courses/timetable.html` and `/library/opening-hours.html`. **[1]**

That part gives the location of the file on the server, so the two pages are separate files held in different folders on that one server. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for identifying that the domain name `www.example.org` is the same in both URLs
> 
> **1 mark** for concluding that both web pages are therefore stored on the same web server
> 
> **1 mark** for identifying that the path and file name after the domain name is different
> 
> **1 mark** for concluding that the two pages are separate files stored in different folders on that server
> 
> Accept for the second mark: the two pages belong to the same website, hosted by the same server.
> 
> Accept for the fourth mark: the two files have different names and are in different directories.
> 
> Do not accept that the two pages are stored on different servers. The domain name is identical, so it resolves to the same server.
> 
> Do not accept that the two pages have different domain names.

> **[exam-tip]**
> The mistake students make here is to see two different file names and conclude the pages are on two different servers. Work through the URL from left to right: the domain name tells you which server, and only what comes after it tells you where the file sits on that server.
> 
> This question uses the command word explain, so a list of the differences is not enough. Each time you point out something that is the same or different, say what it tells you about storage.

### Q44
| Link | Transmission medium | Reason |
|---|---|---|
| A | **fibre-optic cable** **[1]** | **It carries the data as pulses of light, so the electric motors cannot interfere with the signal.** **[1]** |
| B | **radio waves** **[1]** | **The unit is driven around the park, so no cable can be attached to it. The signal travels through the air instead.** **[1]** |

**[4 marks]**

> **[mark-scheme]**
> Link A: **1 mark** for the medium and **1 mark** for a reason that matches it
> 
> Medium: fibre-optic cable
> 
> Reason, any one of:
> 
> It carries the data as light, so electromagnetic interference from the motors does not affect it
> 
> Copper cable would pick up interference from the motors and the data would be corrupted
> 
> Accept "optical fibre" for the medium
> 
> Do not accept copper cable, twisted pair or coaxial cable for Link A. All of these carry electrical signals and all are affected by electromagnetic interference from the motors
> 
> Link B: **1 mark** for the medium and **1 mark** for a reason that matches it
> 
> Medium: radio waves, microwaves or satellite
> 
> Reason, any one of:
> 
> The unit moves, so no cable can be run to it or fixed to it
> 
> The data is carried through the air as electromagnetic waves, so the unit can move anywhere within range
> 
> Accept "Wi-Fi" for the medium only where the reason given is about movement
> 
> Do not accept any cable for Link B. A cable would have to be physically attached to a unit that is being driven around the park
> 
> Do not accept "Bluetooth", which is used for a direct connection between two devices that are close together

> **[exam-tip]**
> Two marks per row means the reason has to match the medium you have named. "Fibre optic is fast" is a true statement that earns nothing here, because it says nothing about the room full of electric motors.
> 
> Every detail in a scenario like this is a clue. A room containing large electric motors is telling you about electromagnetic interference, which rules out every cable that carries an electrical signal. A unit that is driven around is telling you that no cable can reach it at all, which rules out cable altogether.

### Q45
**Final answer:** **225 megabytes**

Time in seconds = 5 x 60 = 300 seconds **[1]**

Data transmitted = 6 x 300 = 1800 megabits **[1]**

Data in megabytes = 1800 / 8 = 225 megabytes **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for converting 5 minutes to 300 seconds
> 
> **1 mark** for 6 x 300 = 1800 megabits
> 
> **1 mark** for dividing by 8 to give 225 megabytes
> 
> Accept `225 MB`.
> 
> Accept the whole calculation in one line, 6 x 300 / 8 = 225, for all three marks.
> 
> Accept follow-through: if the time is converted wrongly but the method that follows is correct, award the second and third marks.
> 
> Do not accept 1800. That is the answer in megabits, not megabytes.
> 
> Do not accept 14400, which comes from multiplying by 8 instead of dividing.
> 
> Do not accept 28.125, which comes from dividing by 8 twice.
> 
> Do not accept 214.58, which comes from treating a megabyte as 1024 x 1024 bytes. The question asks for megabytes, which use a decimal prefix. The unit that uses a binary prefix is the mebibyte.

> **[exam-tip]**
> The one error that costs marks here is mixing bits and bytes. A bit rate given in megabits per second produces an answer in megabits, and there are 8 bits in a byte, so the last step is a division by 8. Multiplying by 8 gives 14400, which is 64 times the correct answer.
> 
> Watch the prefix as well. The question asks for megabytes, so a megabyte is 1000 kilobytes. Divide by 1024 only when the question asks for a kibibyte, mebibyte or gibibyte.
> 
> Always convert the time to seconds first, because bit rate is defined per second.

### Q46
Hardware such as a printer can be shared, so the company does not need one printer for every computer. **[1]**

Staff can share files and data directly with each other instead of copying them onto removable storage. **[1]**

**[2 marks]**

> **[mark-scheme]**
> 1 mark per benefit, to a maximum of 2
> 
> **1 mark** for sharing hardware or peripherals, for example one printer used by every computer
> 
> **1 mark** for sharing files or data between users
> 
> **1 mark** for users being able to communicate with each other, for example by email or messaging
> 
> **1 mark** for data being backed up centrally instead of separately on each computer
> 
> **1 mark** for one network manager being able to control the access rights of every user
> 
> **1 mark** for network software licences costing less than a separate licence for every computer
> 
> Accept "share resources" for sharing hardware
> 
> Do not accept "the computers can connect to the internet", which is not a benefit of joining these ten computers together
> 
> Do not accept "it is faster" or "it is easier" with no statement of what is faster or easier

> **[exam-tip]**
> A benefit has to say what is gained, not what a network is. "The computers can communicate with each other" is the definition of a network, so on its own it scores nothing. Turn it into a gain: what can staff now do that they could not do before?
> 
> Watch the number of marks. Two marks means two separate benefits, so do not spend both of them expanding one point about sharing files.

### Q47
| Part of the URL | Name of this part |
|---|---|
| `https` | **Protocol** **[1]** |
| `www.example.com` | **Domain name** **[1]** |
| `/exhibits/coins.html` | **Web page name / file name** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for `https` named as the protocol
> 
> **1 mark** for `www.example.com` named as the domain name
> 
> **1 mark** for `/exhibits/coins.html` named as the web page name or the file name
> 
> Accept for the first mark: transfer protocol, communication protocol.
> 
> Accept for the third mark: file name, web page name, path and file name.
> 
> Do not accept web address or URL for the domain name, because that names the whole thing.
> 
> Do not accept website for the domain name.
> 
> Do not accept IP address for any row. Every part shown here is text, not an IP address.

> **[exam-tip]**
> Students often write web address or URL in the domain name row. The URL is the whole line. The domain name is only the part that names the server the page is stored on.
> 
> Learn the three parts in the order they appear, because they always appear in that order: protocol, then domain name, then the web page or file name.

### Q48
A thick-client uses its own processor, so the video editing is carried out on the employee's own device. **[1]**

The speed of the editing therefore does not depend on how many other employees are using the server at the same time. **[1]**

A thick-client has its software installed on the device and can store the video files on the device, so it still works when there is no network connection. **[1]**

A thin-client cannot function without a permanent connection to a server, so an employee using one could not work while travelling. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** per marking point, to a maximum of 4
> 
> **1 mark** for a thick-client carries out the processing on its own processor
> 
> **1 mark** for the processing does not have to be shared with the other users of the server
> 
> **1 mark** for the software is installed on the thick-client device itself
> 
> **1 mark** for a thick-client can store the video files locally
> 
> **1 mark** for a thick-client can function offline / with no connection to a server
> 
> **1 mark** for a thin-client relies on a permanent connection to a server
> 
> **1 mark** for a thin-client would not work in a place with no network connection
> 
> **1 mark** for a thin-client sends all of its processing to the server, so the large video files would have to be sent across the network
> 
> Accept "the device does not need to reach the server to run the software" for the fifth marking point.
> 
> Do not accept "a thick-client is more powerful" on its own; the mark is for stating where the processing takes place.
> 
> Do not accept an answer about the cost of the devices, which is not a reason given in the question.

> **[exam-tip]**
> The difference Cambridge marks is where the processing happens, so make sure the words "own processor" or "processing on the device" appear somewhere in your answer.
> 
> Many students write only that a thick-client "works offline". That is one marking point, not four. The second half of your answer should say what a thin-client cannot do here, because the question asks why one choice is more suitable than the other.

### Q49
Fibre-optic cable has a higher bandwidth than copper cable. **[1]**

More of the video data therefore arrives each second, so the playback does not have to stop and wait. **[1]**

Fibre-optic cable carries the data as light, so it is not affected by electromagnetic interference and fewer errors occur. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each point, to a maximum of **3 marks**
> 
> Fibre-optic cable has a higher bandwidth / a higher transmission rate than copper cable
> 
> ... so more of the video data arrives each second and the playback does not stop
> 
> Fibre-optic cable carries the data as light and is not affected by electromagnetic interference
> 
> ... so fewer errors occur and less data has to be transmitted again
> 
> The signal weakens far less over the distance between the two offices than it does in copper cable
> 
> ... so the video data arrives at the second office without being corrupted
> 
> Accept "fibre optic is faster" for the transmission rate point
> 
> Do not accept "fibre optic is newer" or "fibre optic is better", neither of which names a property of the cable
> 
> Do not accept "fibre optic is cheaper". Fibre-optic cable is the most expensive of the cable types

> **[exam-tip]**
> An "explain" question is marked in two halves: the property of the cable, and what that property does to this video link. "Fibre optic is faster" is worth one mark at best. "Fibre optic has a higher bandwidth, so more video data arrives each second and the playback does not stop" is worth two.
> 
> Do not reach for cost as an advantage of fibre optic. It is the expensive option, and it is chosen in spite of that because of what it does for speed, for interference and for distance.

### Q50
Bit rate is the number of bits that are transmitted in one second. **[1]**

Bit rate is measured in bits per second. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the definition: the number of bits transmitted in one second // the amount of data transmitted in a given unit of time
> 
> **1 mark** for the unit: bits per second // `bit/s` // `bps` // kilobits per second // megabits per second
> 
> Accept "the speed at which bits are transmitted" for the definition mark.
> 
> Do not accept "the number of bytes transmitted per second" for either mark. Bit rate counts bits, not bytes.
> 
> Do not accept "hertz" or "bits" on its own for the unit mark, because neither states a rate.
> 
> Do not accept "how fast the video plays". Bit rate is a rate of data transfer, not a playback speed.

> **[exam-tip]**
> Bit rate is measured in bits, not bytes. Writing "megabytes per second" is the commonest way to lose this mark, and the same slip makes every later calculation eight times wrong. If you are not certain of the abbreviation, write the unit out in full.
> 
> The unit mark needs a rate, so "per second" has to be there. "Bits" alone is not a unit of bit rate.

### Q51
Protocol: `https` **[1]**

Domain name: `www.example.org` **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the protocol given as `https`
> 
> **1 mark** for the domain name given as `www.example.org`
> 
> Accept `https://` for the protocol.
> 
> Accept `example.org` for the domain name.
> 
> Do not accept `html` or `.html` for the protocol. That is the file type of the web page, not the method used to transfer it.
> 
> Do not accept `/courses/timetable.html` for the domain name. That is the path and file name, which gives the location of the file on the server.
> 
> Do not accept the whole URL for either mark.

> **[exam-tip]**
> A very common error is to copy out the whole URL twice. The question asks for two different parts of it, so write only the part that is asked for each time.
> 
> Students also confuse `https` with `html`. `html` is the language the web page is written in. `https` is the protocol, which is the method used to transfer the page between the client and the server.

### Q52
The till sends the scanned product code to the server as a request. **[1]**

The server carries out the processing: it looks up the price of the product and reduces the stock level by one. **[1]**

The server sends the price back to the till, and the till only displays it to the assistant. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** per marking point, to a maximum of 3
> 
> **1 mark** for the till sends a request / the scanned product code to the server
> 
> **1 mark** for the server carries out the processing
> 
> **1 mark** for the server looks up the price and updates the stock level
> 
> **1 mark** for the prices and stock levels are stored on the server, not on the till
> 
> **1 mark** for the server sends the result back to the till
> 
> **1 mark** for the till performs minimal processing and displays the returned result to the user
> 
> Accept "no data is stored on the till" for the fourth marking point.
> 
> Do not accept "the till processes the sale", which is what a thick-client would do.
> 
> Do not accept a description of the network connection itself; the marks are for where the processing is done and where the data is stored.

> **[exam-tip]**
> The examiner wants the split of work in three moves: a request from the till, the processing on the server, the result back to the till. Write those three moves and the marks follow.
> 
> A common mistake is to describe the shopping rather than the computing, with answers about the customer choosing clothes and paying. Every mark here is about where the processing happens and where the data is held.

### Q53
Copper cable carries the data as electrical signals. **[1]**

Fibre-optic cable carries the data as pulses of light. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for copper cable:
> 
> as an electrical signal / as electricity / as electrical pulses
> 
> **1 mark** for fibre-optic cable:
> 
> as light / as pulses of light / as a light signal
> 
> Accept "laser light" for the fibre-optic mark
> 
> Do not accept "as radio waves" for either cable. Radio waves are a wireless medium and are not carried along a cable
> 
> Do not accept "as data", "as bits" or "as a signal", none of which says what physically carries the data

> **[exam-tip]**
> A one-word answer is enough here, but it has to name the physical signal. "Light" and "electricity" both score. "It sends the data quickly" describes a benefit of the cable rather than how the data travels along it, and earns nothing.
> 
> Fix these two facts in your memory early, because almost every other difference between the two cables follows from them. Light does not respond to a magnetic field, which is exactly why fibre optic is free of electromagnetic interference.

### Q54
Both devices would wait for the same fixed length of time. **[1]**

They would therefore begin to transmit again at exactly the same moment, so a second collision would occur. **[1]**

The same thing would repeat every time, so the data would never be delivered. **[1]**

In CSMA/CD each device instead waits a random amount of time, called the back-off time, before it transmits again. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** each for any four of the following
> 
> **1 mark** for both devices wait the same fixed amount of time
> 
> **1 mark** for both devices would find the channel free and start to transmit at the same moment
> 
> **1 mark** for a second collision would occur
> 
> **1 mark** for this would repeat indefinitely, so the data is never delivered
> 
> **1 mark** for in CSMA/CD each device waits a random amount of time // a random back-off time
> 
> **1 mark** for the two devices are then very unlikely to restart at the same moment // one device finds the channel free and the other finds it busy
> 
> **1 mark** for the random wait time is increased if further collisions occur
> 
> Accept "back-off time" as an alternative to "random amount of time" throughout
> 
> Do not accept "5 milliseconds is too short", because the length of the wait is not the problem; the problem is that it is the same for both devices
> 
> Do not accept "the devices should wait a different amount of time" without the idea of randomness, unless the answer also explains how the different times are chosen

> **[exam-tip]**
> The random wait is the part of CSMA/CD that students leave out, and it is the part that makes the method work at all. If you can say why a fixed wait fails, you understand the protocol. Note also that the fault in the student's method is not the number 5. Any fixed value shared by both devices produces the same endless loop of collisions, so an answer that argues about the length of the delay scores nothing.

### Q55
For the real-time stream the data does not yet exist beyond the current moment, so the buffer can only be filled a short time ahead of the point being played. **[1]**

Holding only a few seconds of data keeps the delay small, so the user sees the concert close to the time it happens. **[1]**

For the on-demand stream the whole recording is already stored on the media server, so data can be sent to the buffer well ahead of the point being played. **[1]**

The buffer therefore holds much more of the stream, so a short fall in transmission speed does not interrupt playback. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each bullet point, to a maximum of 4.
> 
> **1 mark** for real-time: the data is only produced as the event happens, so the buffer can hold only a small amount of data ahead of playback
> 
> **1 mark** for real-time: a small amount of data in the buffer means a small delay, so the user sees the concert close to live
> 
> **1 mark** for real-time: if data arrives more slowly than it is played the buffer empties, so playback stops until the buffer refills
> 
> **1 mark** for on-demand: the whole file already exists on the media server, so data can be sent ahead of the point being played
> 
> **1 mark** for on-demand: the buffer can hold much more data, so a short fall in transmission speed does not interrupt playback
> 
> **1 mark** for on-demand: data already held in the buffer allows the user to rewind or skip back without waiting
> 
> Accept "cache" as an alternative word for buffer.
> 
> Do not accept "the buffer stores data temporarily" on its own. That is true of both streams, so it makes no difference and earns no mark.
> 
> Do not accept "real-time has no buffer". Both streams use a buffer; the difference is how far ahead it can be filled.

> **[exam-tip]**
> The mark here is for the difference, not for the definition of a buffer. You can write "the buffer stores data temporarily so playback is smooth" and still have said nothing about real-time or on-demand. Write about how far ahead of the playback point the buffer can be filled, and why.
> 
> The reason is worth remembering because it is the whole answer: an on-demand file is already finished, so the service can send you any part of it whenever it likes. A live event has not been recorded yet, so there is nothing further ahead to send.

### Q56
| Description | Type of client |
|---|---|
| The device sends its processing to a server and only displays the results that are returned. | **thin-client** **[1]** |
| The device uses its own processor to run software that is installed on the device. | **thick-client** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for thin-client in the first row
> 
> **1 mark** for thick-client in the second row
> 
> Accept "thin" and "thick" written on their own.
> 
> Do not accept "client" on its own, and do not accept "server", which is not a type of client.
> 
> Do not accept both rows filled in with the same answer.

> **[exam-tip]**
> Thin and thick describe how much work the device does, not how large, new or expensive it is. A thin-client can be a brand new device with a big screen and still be a thin-client, because the processing happens on the server.
> 
> Find the word "processing" in each description and ask where it happens. On the server means thin-client; on the device itself means thick-client.

### Q57
The desktop computers are fixed to the study desks and never move, so nothing is lost by tying them to a cable. **[1]**

A wired connection also gives them a faster and more reliable link to the shared catalogue. **[1]**

The visitors carry their devices around the building, so their connection must keep working as the device moves. **[1]**

The library cannot run a cable to every seat, and it cannot fit a cable to a device that it does not own. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for each point, to a maximum of **2 marks** for the desktop computers and **2 marks** for the visitors' devices
> 
> Desktop computers, wired:
> 
> The computers are in fixed positions and do not move, so freedom of movement is not needed
> 
> A wired connection has a faster transfer rate / a higher bandwidth for reaching the shared catalogue
> 
> A wired connection is more reliable / more stable
> 
> A wired connection is more secure, so the library's own records are harder to intercept
> 
> Visitors' devices, wireless:
> 
> The devices are carried around the building and must stay connected as they move
> 
> A cable cannot be run to every seat in the building
> 
> Visitors can join and leave the network without any change to the cabling
> 
> The library does not own the visitors' devices, but almost every such device already has a wireless adapter built in
> 
> Accept "the desktops are static" or "the desktops stay in one place" for the fixed position mark
> 
> Do not accept a bare statement of the choice, such as "the desktops use a cable". The choice is given in the question, so only the reason earns a mark
> 
> Do not accept the same reason offered for both groups

> **[exam-tip]**
> This question has two halves and four marks, so it wants two reasons about the desktop computers and two about the visitors' devices. The most common way to lose marks here is to write four good reasons for the cabled computers and nothing at all about the wireless ones, which caps you at two.
> 
> Repeating the choice earns nothing. The question already tells you which group gets which connection, so start every sentence with "because" and then check that what follows is a property of the connection rather than a restatement of it.

### Q58
Devices B and D are on the same subnet as device A. Device C is not. **[1]**

Devices A, B and D all have the network ID `192.168.10`, and every device on the same subnet has the same network ID. **[1]**

Device C has the network ID `192.168.25`, which is different, so device C is on a different subnet. **[1]**

The host IDs of A, B and D are 4, 37 and 9. They are all different, so each device is identified uniquely within the subnet. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for identifying B and D, and only B and D
> 
> **1 mark** for stating that A, B and D share the network ID `192.168.10`, and that devices on the same subnet have the same network ID
> 
> **1 mark** for stating that C has a different network ID, `192.168.25`, so it is on a different subnet
> 
> **1 mark** for stating that the host ID is different for every device within a subnet, so it identifies one device inside that subnet
> 
> Accept the network ID written as `192.168.10.0`, or described as the first three groups of the address
> 
> Accept `192.168.25.0` for device C's network ID
> 
> Do not accept device C. Device C has the same host ID as device A, `4`, but the host ID does not decide the subnet
> 
> Do not award the second, third or fourth mark for an answer that lists the devices without naming the network ID or the host ID

> **[exam-tip]**
> The trap in this question is device C. Its address ends in `.4`, exactly like device A, so a student who compares the last group picks C and loses three marks. The subnet is decided by the network ID at the front of the address. The host ID at the end only tells the devices inside one subnet apart.
> 
> Do not assume the split is always three groups to one either. The question tells you where the network ID ends, and a different question can put the boundary somewhere else, so read the stem before you split the address.

### Q59
| Step | What happens |
|---|---|
| 1 | A device with data to send monitors the communication channel. |
| 2 | **The device transmits the data only when the channel is free. If the channel is busy it waits.** **[1]** |
| 3 | Two devices begin to transmit at the same time, so a collision occurs. |
| 4 | **The devices detect the collision, abort the transmission and send a jamming signal.** **[1]** |
| 5 | **Each device waits a random amount of time, called the back-off time, and then tries to send the data again.** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for step 2: data is transmitted only when the channel is free // if the channel is busy the device waits
> 
> **1 mark** for step 4: the transmission is aborted // a jamming signal is transmitted (either alone is enough)
> 
> **1 mark** for step 5: each device waits a random amount of time / a random back-off time before trying to send again
> 
> Accept in step 5 the addition that the wait time is increased if further collisions occur
> 
> Do not accept "the devices wait and then try again" in step 5 without the word random or back-off, because a fixed wait would produce the same collision again
> 
> Do not accept steps written in a different order from the one shown

> **[exam-tip]**
> Step 5 is where most marks are lost. Students write "the devices wait and then resend", which is not enough. The wait has to be random, because two devices that wait for the same length of time will collide all over again. Learn the word "random", or the mark-scheme term "back-off time", and put it in every answer about what follows a collision.

### Q60
The real-time stream is sent from the source as the press conference happens, whereas the on-demand stream is sent from a file that is already stored in full on the media server. **[1]**

The real-time stream must be watched while the press conference is taking place, whereas the on-demand stream can be watched at a time chosen by the user. **[1]**

The real-time stream cannot be paused or rewound, whereas the on-demand stream can be paused, rewound and watched again. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each comparison, to a maximum of 3. Each comparison must state something about both streams.
> 
> **1 mark** for source of the data: real-time comes direct from the source as the event happens, on-demand comes from a file already stored on the media server
> 
> **1 mark** for timing: real-time is streamed and watched at the same time, on-demand is watched at a time the user chooses
> 
> **1 mark** for playback control: real-time cannot be paused or rewound, on-demand can be paused, rewound or skipped
> 
> **1 mark** for connection: real-time needs a steady connection and a low delay, on-demand can hold more data in the buffer ahead of the playback point so a short delay does not matter
> 
> Accept a comparison written as two separate sentences, one about each stream.
> 
> Do not accept a point about only one of the two streams, such as "on-demand can be paused", with no statement about the other.
> 
> Accept "real-time comes direct from the source, whereas on-demand is pre-recorded / downloaded to view later" for the source-of-data mark. Do not accept "on-demand is downloaded and real-time is streamed" with no statement of when the data is created, because both are bit streams

> **[exam-tip]**
> The command word is Compare, so every mark needs both sides. A list of three things on-demand streaming can do earns nothing, however correct each one is. Join the two halves with "whereas" and the mark is safe.
> 
> Do not write only "on-demand is a download". Say when the data was created: real-time comes direct from the source as it happens, whereas on-demand was pre-recorded and is downloaded to view later.

### Q61
In a peer-to-peer network each computer is responsible for its own backup, so there is no way to back up all the delivery records in one operation. **[1]**

In a client-server model the delivery records are stored on the server, so backing up the server backs up every record. **[1]**

A record held on one employee's computer can only be reached while that computer is switched on, but a server is always available, so all 150 employees can reach the shared records at any time. **[1]**

The server manages user accounts and access rights centrally, which is far easier than setting security separately on 150 computers. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** per marking point, to a maximum of 4
> 
> **1 mark** for peer-to-peer has no central management of backup / each computer backs up its own data
> 
> **1 mark** for storing the records on the server allows one central backup of all the records
> 
> **1 mark** for data on a peer is only available while that computer is switched on
> 
> **1 mark** for the server is always available, so the shared records can be accessed at any time
> 
> **1 mark** for peer-to-peer has no central management of security or access rights
> 
> **1 mark** for the server can control access rights for all users centrally
> 
> **1 mark** for the performance of an individual computer falls while other computers are accessing it
> 
> **1 mark** for peer-to-peer is not suitable for a large network, but a dedicated server is built to handle many requests
> 
> Accept "each computer is only as secure as the employee who uses it" for the fifth marking point.
> 
> Do not accept "client-server is better" with no reason given.
> 
> Do not accept an answer about network topology or cabling, which is not part of the choice of network model.

> **[exam-tip]**
> The question hands you two facts to use: the growth to 150 computers and the nightly backup. Each fact earns marks only if your answer says what peer-to-peer cannot do and what a client-server model does instead. Answers that list the good points of client-server without that contrast usually score about half the marks.
> 
> "Client-server is more secure" is not a marking point by itself. Say why: in peer-to-peer each user manages their own machine, so the network is only as secure as its weakest computer, while a server controls access rights for everyone from one place.

### Q62
A wired connection gives a faster transfer rate than a wireless connection. **[1]**

The very large image files are therefore uploaded to the server in less time. **[1]**

A wired connection is also more reliable, because the signal is not weakened by walls or by interference from other equipment. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each point, to a maximum of **3 marks**
> 
> A wired connection has a faster transfer rate / a higher bandwidth
> 
> ... so the very large image files take less time to upload / there is less waiting
> 
> A wired connection is more reliable / more stable
> 
> ... because it is not weakened by distance, by walls or by interference
> 
> A wired connection is more secure, because the data is not transmitted through the air where it could be intercepted
> 
> The computer is a desktop that stays in one place, so the freedom of movement that wireless gives is of no use here
> 
> Accept "less latency" or "fewer delays" for the transfer rate point
> 
> Do not accept "a cable is cheaper", which is not true here: adding a cable for a device costs more than using the wireless connection that is already there
> 
> Do not accept "wireless does not work", which states no property of either connection

> **[exam-tip]**
> The marks on an "explain" question come in pairs: the property and what it does for the studio. "Wired is faster" on its own is one mark. Adding "so the large image files upload in less time" earns the second, because it uses the detail given in the question.
> 
> The last point is the one you are most likely to miss. A desktop computer does not move, so the main advantage of wireless is worth nothing here. Saying why the alternative does not help this particular scenario is a valid way to earn a mark.

### Q63
A private IP address is used for communication inside the LAN only. **[1]**

Devices on the internet see only the public IP address, so a computer with a private IP address is not visible outside the LAN. **[1]**

A device outside the LAN therefore cannot send data straight to that computer, which reduces the chance of it being attacked. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each point, to a maximum of 3
> 
> **1 mark** for stating that a private IP address is used for internal LAN communication only
> 
> **1 mark** for stating that the computer is not visible, or is not directly accessible, from the internet
> 
> **1 mark** for stating that only the public IP address is seen by devices outside the LAN
> 
> **1 mark** for stating that an external device cannot send data directly to the computer
> 
> **1 mark** for stating that this reduces the chance of the computer being attacked or hacked
> 
> Accept `external network` or `WAN` in place of `the internet`
> 
> Do not accept `the data is encrypted`. A private IP address does not encrypt any data
> 
> Do not accept `a private IP address is unique on the internet`. A private IP address is unique only within its own LAN and may be reused on another LAN
> 
> Do not accept `the computer cannot access the internet`. The computer can still send and receive data

> **[exam-tip]**
> The command word is `explain`, so a definition on its own is not enough. Many students write only that a private IP address is used inside the LAN and stop there. That is one mark. The other two marks come from saying what this stops an outside device from doing.
> 
> Also be careful not to claim that a private IP address hides or protects the data itself. It hides the computer, not the contents of the messages.

### Q64
The device monitors the communication channel. **[1]**

The device transmits the data only when the channel is free. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for monitors / listens to / senses the communication channel
> 
> **1 mark** for transmits only when the channel is free // if the channel is busy the device waits and checks again
> 
> Accept "idle", "quiet" or "not in use" in place of "free"
> 
> Do not accept "the device sends a jamming signal", because that happens after a collision, not before transmission
> 
> Do not accept "the device waits a random amount of time", because the random back-off also happens after a collision, not before the first attempt

> **[exam-tip]**
> This question is about the two letters `CS` in `CSMA/CD`, which stand for Carrier Sense. A common mistake is to write out the collision part of the process instead, because that is the part most students revise. Jamming signals and random waiting come after a collision has already happened. Before transmitting, all the device does is listen and wait its turn.

### Q65
| Situation | Type of bit streaming |
|---|---|
| A user watches a football match while the match is being played. | **Real-time** **[1]** |
| A user watches a news programme that was recorded and stored last week. | **On-demand** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `Real-time` in the first row
> 
> **1 mark** for `On-demand` in the second row
> 
> Accept `real time` and `on demand`, with or without the hyphen.
> 
> Accept `live` for real-time.
> 
> Do not accept `streaming` or `bit streaming` on its own in either row, because it does not identify the type.
> 
> Do not accept both rows filled with the same answer.

> **[exam-tip]**
> Decide each row by asking one question: does the whole video already exist on the media server before the user presses play? If it does, the stream is on-demand. If the video is still being created while the user watches it, the stream is real-time.
> 
> Do not decide from the device or from the name of the website. The same website can offer both types, and it often does.

### Q66
In a peer-to-peer network all the computers have equal status, so no member's laptop has to act as a server for the others. **[1]**

No dedicated server has to be bought or maintained, which suits a club with a very small budget. **[1]**

Files are transferred directly between the laptops, which is exactly what the six members already do at their weekly meetings. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** per marking point, to a maximum of 3
> 
> **1 mark** for all the computers have equal status / there is no central server
> 
> **1 mark** for no dedicated server hardware has to be bought, so the network is cheap to set up
> 
> **1 mark** for no administrator or technical staff is needed, and no member works in computing
> 
> **1 mark** for the data is distributed, so each member stores and is responsible for their own photographs
> 
> **1 mark** for computers can share files directly with each other
> 
> **1 mark** for the network is very small, so the slow performance of a peer-to-peer network is not a problem
> 
> Accept "each member is responsible for the security and backup of their own laptop" for the fourth marking point.
> 
> Do not accept "it is cheap" or "it is easy to set up" on its own, with no reason given.
> 
> Do not accept a reason that applies to any network, such as "the members can share photographs", unless it is linked to there being no server.

> **[exam-tip]**
> Explain means give a reason, not just a fact. Naming a feature of peer-to-peer earns nothing on its own; you have to link it to something in the question, such as the very small budget, the six members, or the fact that nobody works in computing.
> 
> The most common way students lose marks here is by writing three general benefits of peer-to-peer networks and never mentioning the club at all.

### Q67
The tablet can be carried around the home and still stay connected to the network. **[1]**

No cable has to be bought or fitted for the tablet, so the connection is cheaper to set up. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for each advantage given, to a maximum of **2 marks**
> 
> Freedom of movement: the tablet stays connected while it is carried from room to room
> 
> No physical connection is needed for the tablet
> 
> Less cabling is needed, so the network costs less to set up
> 
> A new device is easy to add, because no extra cable has to be run to it
> 
> Most devices are made with a wireless adapter already built in
> 
> Accept "the tablet can be used in any room in the house" for the freedom of movement mark
> 
> Do not accept "wireless is faster", which is the reverse of the truth: a wired connection gives the higher transfer rate
> 
> Do not accept "wireless is more secure", which is also the reverse

> **[exam-tip]**
> The wired list and the wireless list are almost mirror images of each other, and this is where the marks are lost. Wireless wins on movement and on cost. Wired wins on speed, on reliability and on security. If you have written "wireless is faster and safer", you have copied down the wrong column.
> 
> Count your points as well. "Give two" means two different advantages. "You can move around with it" and "you can use it anywhere" are the same advantage written twice, so they earn one mark, not two.

### Q68
The data is divided into frames before it is transmitted. **[1]**

Each frame carries the destination address of the printer, so only the printer accepts that frame. **[1]**

Any other device that receives the frame compares the destination address with its own address and discards the frame, because the two do not match. **[1]**

Each frame also carries error checking data, so the printer can test whether the frame was damaged on the way. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** each for any four of the following
> 
> **1 mark** for the data is divided into frames before transmission
> 
> **1 mark** for each frame carries a destination address
> 
> **1 mark** for only the device whose address matches accepts the frame // every other device discards it // a switch forwards the frame only to the device with that destination address
> 
> **1 mark** for each frame carries a source address, so the printer knows which computer sent the data
> 
> **1 mark** for each frame carries error checking data
> 
> **1 mark** for the receiving device uses that data to test whether the frame was damaged during transmission
> 
> **1 mark** for a damaged frame is discarded and transmitted again
> 
> Accept `MAC address` or `IP address` wherever an address is named
> 
> Do not accept "Ethernet checks the data is correct" on its own, because it names no mechanism

> **[exam-tip]**
> The command word is "explain", so each point needs a consequence attached to it. "The frame has a destination address" is a statement; "the frame has a destination address, so only the printer accepts it" is an explanation and earns the mark. Whichever way the frame travels across the LAN, it is the destination address that decides which device keeps it, so always name the address and say what it is compared with.

### Q69
| Feature | IPv4 address | IPv6 address |
|---|---|---|
| Total number of bits in the address | **32** **[1]** | 128 |
| Number of groups in the address | 4 | **8** **[1]** |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `32` as the total number of bits in an IPv4 address
> 
> **1 mark** for `8` as the number of groups in an IPv6 address
> 
> Accept `4 bytes` for the IPv4 answer and `eight` written as a word for the IPv6 answer
> 
> Do not accept `8` for the IPv4 total. 8 is the number of bits in one group of an IPv4 address, not in the whole address
> 
> Do not accept `16` for the number of IPv6 groups. 16 is the number of bits in one group of an IPv6 address
> 
> Do not accept `128 bits` for IPv4 or `32 bits` for IPv6. The two totals must not be swapped

> **[exam-tip]**
> Learn the two numbers for each address as a pair. An IPv4 address is 4 groups of 8 bits, giving 32 bits in total. An IPv6 address is 8 groups of 16 bits, giving 128 bits in total.
> 
> The mark most often lost here is writing 8 for IPv4, because the student has remembered the size of a single group instead of the size of the whole address. Check whether the question is asking about one group or about the complete address before you write the number down.

### Q70
One or more dedicated servers control the network. **[1]**

The files and other resources are stored and managed centrally on the server. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for each characteristic, to a maximum of 2
> 
> **1 mark** for one or more dedicated servers control the network
> 
> **1 mark** for the files / resources are stored and managed centrally on the server
> 
> **1 mark** for the clients send requests to the server
> 
> **1 mark** for the server processes each request and returns the result to the client
> 
> **1 mark** for security, user accounts or backup are managed centrally on the server
> 
> **1 mark** for the computers do not have equal status
> 
> Accept "the server provides services to the clients" for the second marking point.
> 
> Do not accept "there is a server", which names a device rather than describing a characteristic of the model.
> 
> Do not accept a description of a network topology, which is a separate idea from the network model.

> **[exam-tip]**
> Two marks means two separate characteristics, not one characteristic written twice. "The server stores the files" and "all the files are in one place" are the same marking point, so together they earn one mark, not two.
> 
> Cambridge marks this model on who does what. Write one point about what the server does and one point about what the client does, and you will nearly always land both marks.

### Q71
| Part of the frame | Purpose |
|---|---|
| Destination address | **1 Identifies the device the frame is being sent to** **[1]** |
| **2 Source address** **[1]** | Identifies the device that sent the frame |
| Frame check sequence | **3 Allows the receiving device to check whether the data was damaged during transmission** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for row 1: identifies the device that the frame is being sent to // the address of the receiving device // where the frame must be delivered
> 
> **1 mark** for row 2: source address // sender address
> 
> **1 mark** for row 3: error checking // allows the receiving device to check the data has not been damaged // allows a damaged frame to be detected so it can be sent again
> 
> Accept "MAC address" or "IP address" as part of an answer in rows 1 and 2
> 
> Do not accept "the address" alone in row 2, because the frame carries two addresses and the answer must say which one
> 
> Do not accept "corrects any errors" in row 3, because the frame check sequence detects an error, it does not repair it

> **[exam-tip]**
> Read which column is empty before you write. Students often describe the purpose in a cell that asked for a name, or copy the words already printed in the other column. In row 3, "checks for errors" is enough for the mark, but "corrects errors" is wrong: a damaged frame is discarded and transmitted again, not repaired.

### Q72
Ethernet is a protocol, which is a set of rules for transmitting data. **[1]**

Data is transmitted in frames. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** each for any two of the following
> 
> **1 mark** for Ethernet is a protocol // a set of rules for transmitting data
> 
> **1 mark** for it is used for data transmission over wired / cabled network connections
> 
> **1 mark** for data is transmitted in frames
> 
> **1 mark** for each frame carries a source address and a destination address
> 
> **1 mark** for each frame carries error checking data
> 
> **1 mark** for it uses `CSMA/CD` to detect and avoid collisions
> 
> Accept "a wired networking standard used in a LAN" for the second marking point
> 
> Do not accept "Ethernet is a cable" or "Ethernet is a port", because those are hardware and Ethernet is the protocol that the hardware follows
> 
> Do not accept "Ethernet connects a computer to the internet", which describes the job of a router

> **[exam-tip]**
> Most students who drop marks here describe the cable instead of the protocol. The socket on the back of a computer is a connector; Ethernet itself is the set of rules that says how the bits travel along that cable and how they are packaged. Open your answer with the word "protocol" and the first mark is safe.

### Q73
> **[mark-scheme]**
> **One** mark per mark point (**Max 3**)
> 
> MP1 BitTorrent allows the sharing of files between thousands of users who are connected together over the **internet**.
> 
> MP2 It allows **more **users to share files with each other than would be the case with a peer-to-peer network.
> 
> MP3 Users share files **directly **with each other // the users’ computers are acting as peers
> 
> MP4 … no web server / central device is used // all users are of equal status.

### Q74
> **[mark-scheme]**
> (i)** 1 mark** for each bullet point (**max 2**).
> 
> - Courses must be available to anyone who wishes to follow them
> - Courses must be available on the internet
> - Company is willing to share infrastructure with other companies (public)
> - …which is more economic for the company
> 
> (ii) **1 mark** for each bullet point (**max 2** for each disadvantage).
> 
> - There could be a possible loss of control unlike the LAN
> - …because the data is stored on a remote infrastructure / someone else’s infrastructure
> - …reliance on external agency to complete tasks, e.g. backups, security
> - Requires reliable internet connection
> - …to ensure access to the remote data, more likely with LAN
> - Increased recurring costs
> - ...as cloud provider charges must be paid, costs for LAN once only

### Q75
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - Only has four groups of digits // IPv6 has eight groups
> - Uses dotted notation instead of colons
> - Because it is a 32 bit / 4 byte address // IPv6 is 128 bits / 16 bytes
> **[mark-scheme]**
> (i)** 1 mark** for server only connected to router
> 
> **1 mark** for two laptop computers connected only to router
> 
> ![Diagram shows a server connected to a router, which links to two laptops, labelled 'Laptop 1' and 'Laptop 2', forming a network hierarchy.](assets/001-diagram-shows-a-server-connected-to-a-router-whi.png)
> 
> (ii) **1 mark** for each bullet point (**max 2**)
> 
> - The data from the sending laptop is transmitted to the router
> - The data includes the address of the recipient
> - The router determines the recipient’s destination address
> - …by using a routing table
> - The router transmits the data directly / only to the recipient
> 
> (iii) **1 mark** for each use (**max 2**) and** 1 mark** for corresponding expansion (**max 2**)
> 
> - To improve the security of the LAN
> - …so that devices do not receive unintended data
> - …so that a compromised device does not expose the whole network
> - …so not all devices can access all segments
> - To make network management easier
> - …because faults can be isolated more efficiently
> - …by appropriate example
> - To make the network easier to expand // for better control of network growth
> - …by allowing for a greater range of IP addresses to be available
> - To improve network performance
> - To reduce network congestion
> - …by localising network communications // by dividing data between segments
> - …so that devices are not flooded with data
> - …because data sent between devices on the same subnet stays within the subnet
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 3**)
> 
> - To monitor the communications channel
> - To send data only when there is no data being transmitted / the line is quiet / idle
> - **To detect a collision** and then stop transmissions of further data // transmit a **jamming **signal
> - To calculate a **random **wait time / back-off time
> - ... then retransmit the data after that random wait time
> - Increase **random **time if multiple collisions
> **[mark-scheme]**
> **1 mark** for each highlighted area
> 
> | Type of IP address | Description |
> |---|---|
> | **public IP address** | an IP address that is assigned to a device to allow direct access on the internet |
> | static IP address | **an IP address that is fixed / doesn’t change each time a device re-joins a LAN / network** |
> | **private IP address** | an IP address used for internal LAN communication only |
> | dynamic IP address | **an IP address that may be refreshed / changed each time a **<u>**device re-joins**</u>** a LAN / network** |

### Q76
**1 mark** for each bullet point (**max 3**)

- Receives packets from internet / external network
- Implements a firewall
- Analyses the destination IP address of each packet
- Forwards the packet towards its destination // send packets onto local network or external network
- ...using the routing table
- Maintains / updates the routing
- Allocates <u>private </u>IP addresses
- Finds the most efficient route to the destination
- Changes the packet format for transmission over the next network //
- Network Address Translation (NAT): NAT is a technique used by routers to allow multiple devices in a private local area network (LAN) to share a single public IP address.
> **[mark-scheme]**
> Switch: **1 mark** for each bullet point (**max 1**)
> 
> - To allow two or more devices to communicate with one another
> - To connect individual devices to each other
> - To receive transmissions and **forward **them to their destination
> 
> Wireless Access Point (WAP): **1 mark** for each bullet point (**max 1**)
> 
> - To allow connection of devices (to the central device) **using radio signals** / Wi-Fi
> - To allow the central device to send / receive **radio signals** / Wi-Fi signals
> - To allow wireless enabled devices to connect to a wired network
> 
> Bridge:**1 mark** for each bullet point (**max 1**)
> 
> - To connect two LANs / segments with the **same protocol**
> - To transmit data between two networks with the** same protocol**
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - The students cannot access their files without a reliable internet connection
> - The amount of space for no payment may be limited so students will have to purchase more space if needed
> - The students do not have control over the backup (or security) of their work // the students are dependent on a third party for the (security and) backing up of their work
> **[mark-scheme]**
> **1 mark** for each advantage and **1 mark** for valid corresponding expansion
> 
> - Star topology is more resilient to faults
> - …because there is no single cable, leading to less disruption to teaching
> - Higher performance as there are fewer collisions
> - …because each device in the classroom is only connected to the switch
> - Easier to add new nodes
> - …because each device in the classroom connects directly to the switch
> - Easier to fault find compared to a bus topology

### Q77
> **[mark-scheme]**
> (i)** 1 mark** for:
> 
> Dedicated/bespoke services/storage on a remote server only available to company
> 
> (ii)** 1 mark** each to **max 3**:
> 
> e.g.
> 
> - Not reliant on a third party
> - … gives greater **control **over security/privacy
> - … gives greater **control **over backup
> - Storage can be tailored/scalable to company requirements// an example e.g. the amount of storage accessible/ facilitating the sharing of files
> **[mark-scheme]**
> **1 mark** each:
> 
> - Sending computer transmits packets directly to switch/router/central device
> - Switch/router/central device **checks destination address **of packet and forwards directly to that device
> **[mark-scheme]**
> (i)** 1 mark** each to **max 2**:
> 
> - Jamming signal is transmitted by the **sending device**
> - Transmission is aborted
> - The **sending device** waits a **random** time before trying to send data again ...
> - ... if further collisions occur the wait time is increased
> 
> (ii) **1 mark** each to **max 2**:
> 
> - Random time increased each time so can be infinite waiting
> - May be constant jamming signal so nothing ever sends
> - Certain nodes cannot be prioritised
> - High power consumption
> - Only suitable for short distance network // limited distance
> - Not scalable // more nodes means exponentially longer waiting times
**1 mark** for:

Static means the IP for that device does not change **and** Private means it can only be accessed/seen/used within the LAN

### Q78
> **[mark-scheme]**
> **1 mark** for characteristic
> 
> **1 mark** for description of application to examination software:
> 
> | Thin-client characteristic | Description of use in this software |
> |---|---|
> | Data is not stored on the client computer | Exam papers are stored on the server and not on the examiner’s computer // exam papers are not permanently stored on the examiners’ computers |
> | Client computer is reliant on access to server | Examiners cannot mark if their device cannot access the server / the server ‘goes down’ |
> | Client computer heavily reliant on network/internet connection | The marking software will not operate without network/internet access |
> | Client computer requires few local resources/memory | Examiners can use devices with low resources and the marking software will still function |
> | Client computer performs minimal functions/processes | The marking software transmits requests, the server responds and sends the response to the user |
> **[mark-scheme]**
> (i) **1 mark** each to **max 2**:
> 
> - Receives packets from internet
> - Analyses the destination IP address of each packet
> - Forwards the **packet **towards its destination
> - ... using the routing table
> - Maintains/updates the routing table
> - Finds the most efficient route to the destination
> 
> (ii) **1 mark** each to **max 2**:
> 
> - The PSTN consists of many different types of communication lines
> - … therefore the digital data may need to be converted into a different form/analogue signal
> - Data is transmitted in both directions at the same time // duplex data transmission
> - Using a PSTN the communication passes through different switching centres/ISPs

### Q79
**1 mark** for each correct row:

| Statement | Bus | Star | Mesh |
|---|---|---|---|
| all devices connect to one central device |   | ✔ |   |
| all devices connect to a central cable | ✔ |   |   |
| multiple paths for the packets to travel along |   |   | ✔ |
| robust against damage because if any line fails, the rest of the network retains full functionality |   | ✔ | ✔ |
| most likely to lose data through collisions | ✔ |   |   |
> **[mark-scheme]**
> (i)** 1 mark** for:
> 
> to **be visible** to and accessible by other devices on the internet
> 
> (ii) **1 mark** each:
> 
> - IPv4 has 4 groups of digits whilst IPv6 has 8 groups
> - IPv4 is usually represented in **denary** whilst IPv6 is usually represented in **hexadecimal **
> - IPv4 groups are between 0 and 255 whilst IPv6 is between 0 and FFFF
> - IPv4 is **32** bits whilst IPv6 is **128** bits

### Q80
> **[mark-scheme]**
> **1 mark **each:
> 
> - Identification of server in the bank scenario
> - Description e.g. Receives requests, processes the requests
> - Identification of client in bank scenario
> - Description e.g. Sends request to the server, waits and outputs the response

### Q81
> **[mark-scheme]**
> (i) **1 mark** for:
> 
> Continuous ordered flow of bits over a communication path
> 
> (ii) **1 mark** each to** max 2**:
> 
> - Real-time is direct from source whereas on-demand is prerecorded/downloaded to view later
> - Real-time cannot be re-watched, on-demand can be paused, re-watched etc.
> - Real-time plays continually, on-demand downloads sections/blocks and cannot play until next section is downloaded

### Q82
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - A WAN covers a large geographical area
> - External/public infrastructure is used
> - Non-dedicated hardware
> **[mark-scheme]**
> **1 mark **for correct media **1 mark** for matching description e.g.
> 
> - Fibre optic
> - Transmits data as pulses of light
> - Radio waves / microwaves
> - Transmits electromagnetic waves on different frequencies
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 4**)
> 
> - Data is compressed before transmitting
> - The video and audio are transmitted continuously as a series of bits
> - The video is uploaded to a media server
> - On download, the media server sends the data to a buffer
> - The buffer stores data from server until the receiving device can process it
> - The receiving device receives the bit stream from the buffer
> **[mark-scheme]**
> (i)** 1 mark** for public IP address and** 1 mark** for private IP address:
> 
> Public IP address:
> 
> - So that the router is visible to the Internet/external network/WAN
> 
> Private IP address:
> 
> - So that the router is identified to computers within the LAN
> 
> (ii) **1 mark** for each bullet point (**max 2**)
> 
> - It allows the network to be divided into smaller networks
> - … which reduces traffic in some parts of the network // reduces congestion
> - … because traffic only travels through the parts necessary
> - … which hides the complexity of network
> - … and allows for easier maintenance of the network
