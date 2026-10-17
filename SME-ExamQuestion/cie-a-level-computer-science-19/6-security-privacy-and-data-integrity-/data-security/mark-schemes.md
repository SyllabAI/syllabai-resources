# Mark Schemes — Data Security
**6. Security, privacy & data integrity** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (20 questions)


### Q1
| Threat | Description | Measure that restricts the risk |
|---|---|---|
| **Hacker** **[1]** | **A person gains unauthorised access to the server over the internet in order to read, change or delete the customer records.** **[1]** | **A firewall** **[1]** |
| **Virus** **[1]** | **Malicious software replicates itself on the server and corrupts or deletes the customer records.** **[1]** | **Anti-virus software** **[1]** |

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for each correctly identified threat, to a maximum of 2
> 
> **1 mark** for each description that matches the threat identified, to a maximum of 2
> 
> **1 mark** for each measure that restricts the threat identified, to a maximum of 2
> 
> The two threats must be different and the two measures must be different.
> 
> Accept any two of the following rows.
> 
> Hacker: gains unauthorised access to the server over the internet // accesses the customer data without permission, with the intention of reading, changing or deleting it. Measure: firewall // strong password // biometric authentication // access rights
> 
> Virus: malicious software that replicates itself and can corrupt or delete the customer data. Measure: anti-virus software // anti-malware software // firewall
> 
> Spyware: malware installed without the user's knowledge that records the keystrokes of a member of staff, such as the server password, and sends them to a third party. Measure: anti-spyware software // anti-malware software // a virtual or on-screen keyboard
> 
> Do not accept a description that only repeats the name of the threat, such as "a hacker hacks the server" or "a virus infects the server"
> 
> Do not accept a description that gives only the consequence, such as "the customers lose money", with no statement of how the threat reaches the data
> 
> Do not accept encryption as the measure against a virus, because encryption does not stop a virus corrupting or deleting a file; it only stops the contents being understood

> **[exam-tip]**
> Two marks go missing here for the same two reasons. The first is giving the same threat twice. Hacker, virus and spyware are three different threats, so any two of them can score, as long as the two measures are also different.
> 
> The second is the description. Writing "a hacker hacks the server" repeats the name and earns nothing. The mark is for the mechanism, so say how the threat reaches the data: unauthorised access over the internet, or software that replicates itself. Finally, check that your measure would really stop your threat. Encryption, for example, does not stop a virus deleting a file, so it will not be credited against a virus.

### Q2
Customer A experienced pharming. **[1]**

Customer B experienced phishing. **[1]**

Difference: the malicious code redirected Customer A to the fake website automatically, even though the correct web address was typed, while Customer B had to take action by clicking a link in an email. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for pharming as the threat experienced by Customer A
> 
> **1 mark** for phishing as the threat experienced by Customer B
> 
> **1 mark** for one difference shown by the scenarios: pharming redirects the user automatically while phishing requires the user to act // pharming uses malicious code on the computer while phishing uses a fraudulent email
> 
> Accept "pharming attack" and "phishing email"
> 
> Do not accept phishing for Customer A. Customer A received no message and typed the correct web address, so nothing lured them to the fake site
> 
> Do not accept a difference in which Customer A clicks a link, because pharming redirects the browser without the user doing anything
> 
> Do not accept spyware or a virus for Customer A. Spyware records and sends what the user types and a virus replicates itself; neither redirects a browser to a fake website
> 
> Do not accept "both use a fake website" as the difference, because that is a similarity between the two threats, not a difference

> **[exam-tip]**
> Students describe pharming as "phishing but on a website", and lose the mark every time. Both threats end at a fake website, so the website is never the difference. Ask instead: **who acted?** If the victim had to open a message or click a link, it is phishing. If the browser reached the fake site on its own from a correct address, it is pharming.
> 
> The phrase "types the correct web address" is put in a stem deliberately. It rules out phishing, because a fraudulent message would have sent the user somewhere else. When you see it, write pharming.

### Q3
Feature of a virus: it replicates itself, so copies of it spread to other programs or files on the computer. **[1]**

Feature of spyware: it secretly records what the user does on the computer, such as the keys they press, and sends that record to a third party. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for a feature of a virus only: it replicates itself // it makes copies of itself // it spreads to other programs or files on the computer
> 
> **1 mark** for a feature of spyware only: it records the user's actions or keystrokes // it sends the data it has gathered to a third party
> 
> Accept "self-replicating" for replicates itself
> 
> Accept "records the keys the user presses" or "records keystrokes" for the recording
> 
> Accept "it can corrupt, damage or delete data" as the feature of a virus
> 
> Accept "it is downloaded without the user's knowledge" for spyware
> 
> Do not accept "it is malicious software" for either, because both are malware and the question asks what separates them

> **[exam-tip]**
> Students call every piece of malware a virus. Cambridge names only two types in this part of the syllabus, and the clearest way to separate them is one thing each: a virus **replicates**, spyware **records and reports**. Learn the pair that way and the mark is easy.
> 
> Be precise about what a virus does. "It can corrupt or delete data" is credited, but replication is the safest answer because it is the feature that makes a program a virus. For spyware, "it spies on you" is worth nothing on its own; say that it records what the user types, or that it sends the record to a third party.

### Q4
Once the computers have a connection to the internet, a person outside the school can try to reach any of the 20 computers, which was impossible while they were stand-alone. A firewall is needed. **[1]**

The firewall monitors all traffic entering and leaving the network and compares it against set criteria, such as a whitelist or a blacklist of addresses. **[1]**

It blocks any traffic that does not meet the criteria, and it can block the ports that the school does not use. **[1]**

Users can now download files from the internet, so anti-spyware software is needed to detect any software that is installed without the user's knowledge. **[1]**

Data sent from one computer to another can now be intercepted on the network, so it should be encrypted, which means it cannot be understood without the decryption key. **[1]**

**[5 marks]**

> **[mark-scheme]**
> **Any five from:**
> 
> - an attacker outside the school can now attempt to reach any computer through the internet connection, so a firewall is needed
> - the firewall monitors all incoming and outgoing traffic
> - ... and compares it against set criteria, a whitelist or a blacklist
> - the firewall blocks any traffic that does not meet the criteria, and can block unused ports
> - malware on one computer can now spread to the other computers across the network
> - ... so the anti-virus definitions on every computer must now be updated regularly
> - users can now download files from the internet, so anti-spyware software is needed to detect software installed without the user's knowledge
> - data sent between the computers can now be intercepted, so it should be encrypted
> - ... so that intercepted data cannot be understood without the decryption key
> 
> **[5 marks]**
> 
> Accept a proxy server in place of a firewall, if it is described: it stops devices reaching the school's computers directly, intercepts requests and screens the data that is returned.
> 
> Do not accept "the school should use stronger passwords" on its own. Each computer already has a user account and a password, so a mark needs a measure the network adds.
> 
> Do not accept "install anti-virus software" or "buy better anti-virus software". Anti-virus software is already installed on every computer, so it is not an additional measure. Only keeping its definitions up to date is credited.
> 
> Do not accept "the internet is dangerous" or any similar statement with no measure attached.

> **[exam-tip]**
> The syllabus asks you to describe security measures ranging from the stand-alone PC to a network of computers, and this is exactly that question. Do not simply list measures. For each one, say what changed when the computers were connected, because the marks are for the link between the new risk and the measure. A firewall on a machine with no network connection protects nothing, which is why the school did not need one before.

### Q5
A password can be guessed, or found by trying a very large number of combinations, but a fingerprint cannot be guessed in this way. **[1]**

A password can be written down, shared or seen by another person, who can then use it. A fingerprint cannot be handed to somebody else. **[1]**

The employee has to be physically present for the fingerprint to be scanned, so knowing a stolen detail is not enough to get in. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - a password can be guessed, or found by trying many combinations, while a fingerprint cannot be guessed
> - a password can be written down, shared or watched as it is typed, so another person can use it, while a fingerprint cannot be passed on in this way
> - the user must be physically present for the scan, so a stolen detail on its own does not give access
> - every user's fingerprint is different, so the system identifies the individual person rather than anybody who knows the password
> - a user cannot forget a fingerprint, so they do not need a short or reused password that is easier to break
> - spyware that records keystrokes cannot capture a fingerprint
> 
> **[3 marks]**
> 
> Accept "biometric data is unique to each user" for the uniqueness point.
> 
> Do not accept "a fingerprint cannot be copied" or "biometrics can never be broken". Both are too strong to credit.
> 
> Do not accept "it is faster to scan a finger than to type a password" or "the employee does not have to remember anything". Those are advantages of convenience, not of protection against unauthorised access.

> **[exam-tip]**
> Biometrics was added to this part of the syllabus, so it is worth having three separate points ready rather than one. The mark is lost most often by writing about convenience: "it is quicker" and "you cannot forget it" do not answer a question about protection unless you go on to say why that makes unauthorised access harder. Compare the fingerprint with the password at every point, because the question asks which gives better protection, not what a fingerprint scanner is.

### Q6
Access rights control which members of staff can open the customer records file and what they are allowed to do with it, such as read-only access or full access. **[1]**

This means each member of staff can reach only the data their job needs, and staff who do not need the customer records cannot open the file at all. **[1]**

Access rights on their own are not enough, because they are applied by the system to a user account. If a copy of the file is taken from the server, the customer records can still be read. **[1]**

Encryption turns the contents of the file into cipher text, so a copy of the file cannot be understood without the decryption key. **[1]**

Encryption on its own is not enough either, because it does not decide who is allowed to open the file. A member of staff who has the decryption key still sees the customer records in full. **[1]**

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for saying what access rights do: control which users can open the file, and which actions they may perform on it
> 
> **1 mark** for the effect of that: different users are given different permissions, so a user sees only what their job needs
> 
> **1 mark** for the limit of access rights: they are enforced on a user account, so a copy of the file taken from the server, or intercepted in transmission, can still be read
> 
> **1 mark** for saying what encryption does: the file contents are turned into cipher text, which cannot be understood without the decryption key
> 
> **1 mark** for the limit of encryption: it does not control who may open the file, so a user who holds the decryption key still reads the records
> 
> Accept "read/write, read only, full access" as the description of what access rights set.
> 
> Accept "encoded" or "scrambled" in place of "turned into cipher text".
> 
> Accept a stolen backup, a stolen hard disk or a copied file as the example that defeats access rights alone.
> 
> Do not accept an answer that only describes the two methods one after the other with no statement of what each one fails to protect against. Maximum 3 marks in that case.
> 
> Do not accept "encryption stops unauthorised people accessing the data". Encrypted data can still be accessed and copied; what it cannot be is understood.

> **[exam-tip]**
> The marks in this question are in the word "both". Many students describe access rights, then describe encryption, and stop. That answer earns about half the marks because it never says why one of them alone would leave the bookshop exposed.
> 
> Use a simple pairing as you write: one sentence for what the method does, one sentence for what it does not do. Access rights are checked when a user signs in, so they do nothing once a copy of the file has left the server. Encryption is undone by the key, so it does nothing about a member of staff who is entitled to hold that key. The two methods cover each other's gap, which is exactly why the consultant asked for both.

### Q7
The anti-virus software scans the files on the PC and compares them against a stored database of known viruses. **[1]**

Any file that matches is deleted or quarantined, so the virus cannot run on the PC. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - scans the files on the computer // checks files as they are downloaded or opened
> - compares the files against a stored database of known viruses
> - any virus found is deleted or quarantined // the download is stopped before it completes
> - the database of virus definitions must be updated regularly so that new viruses are recognised
> 
> **[2 marks]**
> 
> Accept anti-malware software in place of anti-virus software.
> 
> Do not accept "it removes all viruses from the PC". Anti-virus software only recognises viruses that are already in its database.
> 
> Do not accept "it stops hackers getting into the PC" or "it blocks traffic that does not meet set rules". That describes a firewall.

> **[exam-tip]**
> Two marks means two separate steps, so do not write one long sentence saying the software "protects the PC from viruses". Say what it looks at and say what it does when it finds something. Students also mix up the three measures: anti-virus scans files, anti-spyware looks for software that records what the user does, and a firewall checks traffic entering and leaving the computer.

### Q8
| User group | Access right |
|---|---|
| Sales assistants | **Read-only access** **[1]** |
| Pricing team | **Full access** **[1]** |
| Warehouse staff | **No access** **[1]** |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for sales assistants: read-only access
> 
> **1 mark** for pricing team: full access
> 
> **1 mark** for warehouse staff: no access
> 
> Accept "read only" or "view only" for the sales assistants.
> 
> Accept "read and write", "read/write" or "read, write and delete" for the pricing team.
> 
> Accept "access denied" for the warehouse staff.
> 
> Do not accept "restricted access" or "limited access" on their own in any row. They do not say which actions are allowed.
> 
> Do not accept "write only" for the pricing team. A user who edits a price must be able to read it first.

> **[exam-tip]**
> There are only three answers the mark scheme wants here: full access, read-only access and no access. Learn those three terms.
> 
> The row students lose is the last one. They write "restricted access" for the warehouse staff, which is true of the sales assistants as well, so it does not identify anything. If a group must not open the file at all, the answer is no access.

### Q9
Encryption protects the security of the data. If the records are copied or intercepted, they cannot be understood without the decryption key. **[1]**

Encryption does nothing to protect the integrity of the data, because it does not check that the values stored are accurate or complete. **[1]**

The part-written records are incomplete, so the value stored is not the value that should have been stored. This is a loss of data integrity, not a loss of data security. **[1]**

The incomplete records are still encrypted, so they will decrypt to incorrect delivery data and the company will use them as though they were correct. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - encryption protects the security of the data: data that is intercepted or copied cannot be understood without the decryption key
> - encryption does not check that the values stored are accurate or complete, so it does not protect integrity
> - the part-written records are incomplete, so this is a loss of data integrity, not a loss of data security
> - the incomplete records are still encrypted, so they decrypt normally and the wrong data is used as though it were correct
> - a separate measure is needed to protect integrity, for example restoring the affected records from a backup, or verifying the written records against the original data
> 
> **[4 marks]**
> 
> Accept "encoded" or "turned into cipher text" for encrypted.
> 
> Do not accept "encryption keeps the data safe so the manager is right". The question asks why the manager is wrong.
> 
> Do not accept "the data was not encrypted properly" or "the encryption key was lost in the power failure". Neither is stated in the question and neither is the reason the records are wrong.

> **[exam-tip]**
> This question is testing whether you can keep security and integrity apart under pressure. Encryption is an answer to the question "can someone else read this?", not to the question "is this the right value?". A record that is wrong and encrypted is still wrong. When a question describes data being lost, cut short or corrupted, reach for integrity measures such as backups and verification, not for encryption.

### Q10
Encryption has converted the customer records into cipher text. **[1]**

The thief cannot understand the records without the decryption key. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the records being encoded / scrambled / turned into cipher text
> 
> **1 mark** for the records being impossible to understand without the decryption key
> 
> Accept "scrambled", "encoded", "converted into an alternative form" and "ciphertext" written as one word for the first mark.
> 
> Accept "the key is needed to decode the data" or "the algorithm is needed to decode the data" for the second mark.
> 
> Do not accept "the thief cannot open the file". Encryption does not stop the file being opened, only understood.
> 
> Do not accept "the data is hidden" or "the data is deleted". Encrypted data is still there and is still readable as characters; it is the meaning that is protected.

> **[exam-tip]**
> Students very often write that encryption "stops the data being stolen". It does not. The thief still has the file. Encryption changes what the stolen file is worth, so always finish the sentence with what the thief cannot do: understand it without the key.
> 
> Two marks means two separate ideas here. Saying only "the data is encrypted so it is safe" repeats the question and scores nothing.

### Q11
Security of data means that the customer records are protected from loss, damage and unauthorised access, so they cannot be stolen, deleted or damaged. **[1]**

Privacy of data means that the shop controls who is allowed to see each customer record and what the data may be used for, so a customer's address and card details are only shown to people who are authorised to see them. **[1]**

Integrity of data means that the customer records are accurate, complete and up to date, and have not been changed by mistake during entry, processing or transfer. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for security: the data is protected from loss, damage or unauthorised access // the records cannot be stolen, deleted or damaged
> 
> **1 mark** for privacy: the shop decides who is allowed to see the data and how it may be used // only authorised people may see a customer's address or card details
> 
> **1 mark** for integrity: the data is accurate, complete, consistent and up to date // the data has not been changed by mistake during entry, processing or transfer
> 
> Accept "the data is not disclosed to unauthorised people" for privacy.
> 
> Accept "the data is not corrupted" for integrity.
> 
> Do not accept an answer that defines one of the three terms using another of them, for example "privacy means the data is kept secure", "security means the data has integrity" or "integrity means the data is safe". Each term must be described in its own words.
> 
> Do not accept "integrity means the data is protected from hackers", which describes security.
> 
> Do not accept "privacy means the data is encrypted". Encryption is a measure used to protect data, not a definition of privacy.

> **[exam-tip]**
> The commonest way to lose all three marks here is to answer with the other two words. "Privacy means keeping data secure and private" earns nothing, because it has not said anything the examiner did not already give you in the question. Write each one without using either of the other two words: who may see it is privacy, whether it is correct is integrity, and whether it is protected from loss or attack is security.

### Q12
Statement 1 describes the **privacy** of data. **[1]**

Statement 2 describes the **integrity** of data. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for Statement 1: privacy (of data)
> 
> **1 mark** for Statement 2: integrity (of data)
> 
> Accept "data privacy" for privacy and "data integrity" for integrity.
> 
> Do not accept security for either statement. Security of data is the protection of data from loss, damage and unauthorised access, which is the general idea behind both statements and so identifies neither of them.
> 
> Do not accept "accuracy" alone for Statement 2 unless the word integrity is given, because the question asks for one of the three named terms.

> **[exam-tip]**
> Most students who lose marks here write security for both statements, because both statements are about keeping data safe. Look at what each statement actually controls. If it controls who is allowed to see the data, the answer is privacy. If it controls whether the stored value is correct and complete, the answer is integrity.

### Q13
> **[mark-scheme]**
> **1 mark** for difference
> 
> **1 mark** for similarity
> 
> Difference:
> 
> - Pharming is malicious code that redirects to a** fake website**. Phishing uses an **email **to prompt user action.
> - Pharming is **automatic**. Phishing requires** user action**.
> 
> Similarity:
> 
> - Both try to obtain financial or personal information
> - Both are a false representation of an official organisation, e.g. a bank
> - Both make use of fake websites
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 3**).
> 
> - Download programs from reputable websites / sources
> - …as these are less likely to contain malware
> - Backup / archive computer systems
> - …so they can be restored in case of data loss from malware program installation
> - **Install and run** anti-malware program
> - …so that regular scans can be made for known malware
> - …and if malware is found it can be quarantined / removed
> - …and computer’s anti-malware definitions are regularly updated
> - Using a firewall to block unused ports
> - …so that malware cannot enter the computer system
> - Deny administrator privileges to everyday users
> - …so that malware cannot be downloaded by everyday users
> - Avoid the use of / access to removable devices
> - …so that malware cannot be installed from these devices

### Q14
> **[mark-scheme]**
> **1 mark **each for firewall, encryption and passwords.
> 
> Firewall:
> 
> - Monitors incoming and outgoing traffic and rejects any traffic that does not meet the set rules
> 
> Encryption:
> 
> - Ensures that if data is intercepted / obtained it cannot be understood without the decryption key
> 
> Passwords:
> 
> - Ensures only users with the correct password can access the resources // prevents unauthorised access

### Q15
> **[mark-scheme]**
> **1 mark** for:
> 
> Either
> 
> - Ensuring data can only be accessed by / disclosed to authorised persons
> 
> Or
> 
> - Ensuring data cannot be accessed by / disclosed to unauthorised persons
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 1**)
> 
> - Ensuring the accuracy / completeness / consistency of data (during / after processing) .
> - Ensuring the data is up to date
> **[mark-scheme]**
> **1 mark** for each bullet point.
> 
> Phishing email (**max 2**)
> 
> - The email pretends to be from an official body
> - ... persuading individuals to disclose private information // by example such as bank details
> - ... or requesting authentication by redirecting to an unofficial/unauthorised website // inviting a user to click a link
> 
> Spyware (**max 2**)
> 
> - Malware downloaded **without the user’s knowledge **
> - ... which secretly records the user’s actions / keystrokes on the computer
> - ... and sends logs of the actions to a third party

### Q16
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 4**)** **
> 
> **Max 2 **if no descriptions
> 
> - Backup / recovery procedures
> - … automatically takes copies of the database and store off site on a regular basis / weekly, etc.
> - ... so that the data can be recovered if lost
> - Use of access rights
> - … some users are given different access permissions to different tables
> - ... read/write, read only, full access, etc.
> - Views
> - … different users are able to see different parts of the database
> - ... only see what users need to see // by example
> - Record and table locking
> - … prevents simultaneous access to data
> - ... so updates are not lost // data is not overwritten
> - Encryption
> - ... the data is turned into ciphertext
> - ... so it cannot be understood without a decryption key

### Q17
> **[mark-scheme]**
> **1 mark** each to **max 2**:
> 
> - Encodes/scrambles data
> - ... so if it is intercepted it cannot be **understood**
> - Algorithm/**key** is required to decode the data

### Q18
> **[mark-scheme]**
> **1 mark** for security measure
> 
> **1 mark** each to max 2 for how the chosen measure works:
> 
> - Firewall
> - Checks incoming connections
> - ... against criteria
> - Blocks data from entering specific ports
> - Blocks data that does not meet whitelist that meets blacklist
> - Proxy server
> - Prevents devices accessing the web server directly
> - Intercepts any requests
> - Forwards the request using its own IP address
> - Screens returning data before sending it to the user

### Q19
> **[mark-scheme]**
> **1 mark** each to **max 3**:
> 
> - Compares all incoming and outgoing transmissions
> - ... against set criteria/whitelist/blacklist
> - Blocks all transmissions that do not meet rules
> - Blocks data entering from specific ports
> - Blocks unauthorised/unknown internal software transmitting data

### Q20
> **[mark-scheme]**
> **1 mark** for the security method. **2 marks** for explanation.
> 
> Security method:
> 
> Encryption
> 
> Explanation
> 
> - File contents are converted to cipher text
> - If intercepted the data cannot be understood without the decryption key
