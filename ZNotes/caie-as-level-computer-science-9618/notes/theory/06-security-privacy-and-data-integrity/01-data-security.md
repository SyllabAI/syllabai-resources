# Security, Privacy and Data Integrity

## Data Security

* Data Security: ensuring data is protected against loss and unauthorized access.
* Data Integrity: making sure that data is valid and does not corrupt after transmission
* Data Privacy: ability to determine what data is shared with a third party
* Table below shows difference between Data Security and Computer System Security


|Data Security|System Security|
|:---|:---|
|Protection of data on a computer system|Protection of the computer system|
|To prevent corruption of data and prevent hackers from using data|To prevent access of viruses to the system and prevent hackers from entering  your computer system|
|E.g. encryption|E.g. ID & Password|

*Threats to Computer & Data Security*\*

* Malware
  * software intentionally designed to damage a computer or computer network
  * Includes Virus & Spyware
  * Virus: Software that replicates itself by inserting a copy of itself into another piece of software, which may cause the computer to crash and can lead to deletion or corruption of data
  * Spyware: software that gathers information about users' online and offline activity, including accessed sites, applications, and downloaded files.
  * Risk restriction: Ensure anti-virus and anti-spyware software is installed, regularly updated and run.
* Hacking
  * illegal access to a computer system
  * Hackers can obtain user’s confidential data which can cause identity theft
  * Can lead to the deletion or corruption of data
  * Risk restriction: Use strong passwords and ensure firewall
* Phishing
  * Attempt through emails to obtain user’s confidential data which can cause identity theft
  * Risk restriction: Ignore suspicious mails and ensure firewall criteria include SPAM filters, blacklist, etc.
* Pharming
  * Redirects user to a fake website that appears legitimate to gain confidential data
  * Risk restriction: use a reliable ISP; check that links are genuine and ensure https is present in the URL

**Computer System Security Measures**

* User Accounts and Passwords
  * Usernames & passwords to deny access to unauthorized users
  * User-assigned privilege, which accesses to only the user’s workplace, preventing the user to have admin rights.
  * Can assign privileges to files so users with low privileges do not have access.
* Firewalls
  * Hardware or software that filters information travelling between the computer system and the internet
  * (software) firewall can make decisions about what to allow and block by detecting illegal attempts by specific software to connect to the internet
* Authentication
  * Process of determining whether someone is who they claim to be.
  * Helps prevent unauthorized access
  * Log-on using digital signatures, passwords and biometric scans.
* Digital Signatures
  * The data is hashed using a agreed hashing algorithm, to produce a digest. The sender encrypts the digest using the sender’s private key to create the digital signature. The message and the signature are sent to the receiver. The receiver uses the sender's public key to decrypt the signature to reproduce the orignal digest. The receiver then applies the same hashing algorithm on the received message to produce a second digest. The receiver compares the second digest with the one from the digital signature. If both are the same, the document is authentic and this proves the integrity of the message and the identity of the sender.
* Anti-virus software
  * Runs in the background to detect & remove viruses.
  * Checks files for known malicious patterns
* Anti-spyware software: detects & removes spyware.
* Encryption:
  * Conversion of data to code by encoding it
  * It doesn’t stop illegal access but appears meaningless
  * Necessary to use decryption software to decode data
* Data Security Measures
  * Encryption
  * Access Rights to data (authorization): different users assigned different authorization levels which prevent them from accessing all data ∴ increases security
* Data Backup
  * An exact copy of an original piece of data in case the original is lost or corrupted
  * Within the same computer system or at different site
* Disk-mirroring strategy
  * Real-time strategy that writes data to two or more disks at the same time.
  * If one fails, the other is still there to be read off of