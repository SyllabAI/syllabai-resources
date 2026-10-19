# Mark Schemes — Encryption, Encryption Protocols & Digital Certificates
**17. Security** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (17 questions)


### Q1
With symmetric cryptography, the single key that encrypts and decrypts the data would have to be shared with every customer **[1]**

So any customer, or anyone who obtained that key, could decrypt the payment details of other customers **[1]**

With asymmetric cryptography, the shop shares only its public key, and each customer encrypts their payment details using the shop's public key **[1]**

Only the shop's matching private key, which is never transmitted, can decrypt the cipher text, so a customer who holds the public key still cannot read another customer's details **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> Symmetric (max 2)
> 
> - the same single key encrypts and decrypts, so it would have to be shared with every customer
> - any customer / anyone who obtains the key could decrypt every other customer's message // the risk of compromise is higher
> 
> Asymmetric (max 3)
> 
> - the shop generates a matching pair of keys, a public key and a private key
> - the shop's public key is shared with all customers
> - each customer encrypts their payment details using the shop's public key
> - the cipher text can only be decrypted using the shop's private key, which is kept secret / never transmitted
> - so holding the public key does not allow a customer to decrypt another customer's message
> 
> **[4 marks]**
> 
> Accept "recipient's public key" / "receiver's private key" for the shop's keys
> 
> Do not accept each customer encrypting with their own private key, because anyone with that customer's public key could then read the details
> 
> Do not accept "asymmetric cryptography is faster", because it is the slower process

> **[exam-tip]**
> The question says "rather than", so the examiner is looking for both sides. Many students describe the asymmetric process in full and never say what would go wrong with symmetric cryptography, which limits them to 3 marks.
> 
> Writing "asymmetric is more secure" is not enough by itself. Say why: with symmetric cryptography the one key has to be given to everyone, but with asymmetric cryptography only the public key is shared and the private key never leaves the shop.

### Q2
The sending office uses a key to encrypt the file (the plain text) into cipher text **[1]**

The same key must be shared with the receiving office **[1]**

The receiving office uses the same key to decrypt the cipher text back into plain text **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - a single key is used for both encryption and decryption
> - the file / plain text is encrypted using the key (and an encryption algorithm) to produce cipher text
> - the key has to be shared with / given to the receiving office
> - the receiving office decrypts the cipher text using the same key (to get the plain text back)
> 
> **[3 marks]**
> 
> Accept "secret key" for "key"
> 
> Do not accept the receiving office decrypting with a private key, or the sending office encrypting with a public key, because public and private keys are used in asymmetric cryptography

> **[exam-tip]**
> Weak answers say "the file is encrypted, sent, then decrypted" and never mention the key. Every mark here depends on naming the key and making clear it is the same key at both ends.
> 
> Notice the step that makes symmetric cryptography risky: the key itself has to reach the other office. Anyone who obtains that key can decrypt every file encrypted with it. This is why the risk of compromise is higher with symmetric cryptography than with asymmetric cryptography.

### Q3
| Statement | Symmetric | Asymmetric |
|---|---|---|
| Uses one key to both encrypt and decrypt the data | **✓** |   |
| Uses a matching pair of keys |   | **✓** |
| Only one of the keys is shared with others |   | **✓** |
| The same key must be shared with everyone who needs to read the data | **✓** |   |
| Is usually the faster process | **✓** |   |

All five rows correct **[2]**

**[2 marks]**

> **[mark-scheme]**
> **2 marks** for all five rows correct
> 
> **1 mark** for four rows correct
> 
> Do not accept a row with a tick in both columns

> **[exam-tip]**
> A common mistake is to think that in asymmetric cryptography the sender has one key and the receiver has the other. Both keys in a pair belong to the same owner. The owner shares the public key and keeps the private key.
> 
> Students also tick "faster" for asymmetric because it sounds more advanced. Symmetric cryptography is the simpler process, so it is usually faster. Asymmetric cryptography is more complex, so it is slower.

### Q4
The agency makes its public key available to everyone **[1]**

The agency encrypts the warning using its own private key **[1]**

A member of the public decrypts the warning using the agency's public key **[1]**

Only the agency holds the matching private key, and it is never transmitted, so a warning that decrypts correctly with the agency's public key must have come from the agency **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - the agency has / generates a matching pair of keys, a public key and a private key
> - the agency's public key is made available to everyone / the public
> - the warning is encrypted using the agency's (the sender's) private key
> - the public decrypt the warning using the agency's (the sender's) public key
> - only the agency has the private key / the private key is kept secret / is never transmitted
> - so a warning that can be decrypted with the agency's public key must have been encrypted by the agency / is authentic
> 
> **[4 marks]**
> 
> Accept "sender's private key" and "sender's public key"
> 
> Accept the same key steps applied to a digest of the warning (a digital signature)
> 
> Do not accept the warning being encrypted with the public's or the receiver's public key, because there is no single receiver and the agency would not be proving who sent it
> 
> Do not accept "the agency sends its private key to the public", because then anyone could pretend to be the agency

> **[exam-tip]**
> The most common error is to use the private-message method out of habit and encrypt with the receiver's public key. Ask two questions before you write. Who must be able to read it? Everyone, so the public key decrypts. Who must be the only one able to create it? The agency, so the agency's private key encrypts.
> 
> This method does not keep the warning secret, because anyone with the public key can decrypt it. That is not a weakness here: a public warning is not confidential, and the aim is to prove who sent it.

### Q5
The public key and the private key are generated together, by an algorithm, as a matching pair **[1]**

The private key is kept secret by its owner and is never transmitted **[1]**

Data encrypted with one key of the pair can only be decrypted with the matching key **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - the keys are a matching pair / are generated together (by an algorithm)
> - the public key is available to everyone / is shared / is published
> - the private key is kept secret / is unpublished / is never transmitted
> - data encrypted with one key can only be decrypted with the other, matching key (for example, encrypted with the public key and decrypted with the matching private key)
> 
> **[3 marks]**
> 
> Do not accept a description in which the same key both encrypts and decrypts the data, because that is symmetric cryptography
> 
> Do not accept "the private key is sent securely to the receiver", because the private key is never transmitted

> **[exam-tip]**
> Many students learn "public key encrypts, private key decrypts" as a fixed rule. It only describes sending a private message. The keys work in both directions: data encrypted with the private key can be decrypted with the matching public key. That is how a sender proves a message came from them. Describe the relationship as "one key encrypts, only the matching key decrypts" and you are right in both cases.

### Q6
The web server sends the browser its digital certificate, which contains the server's public key **[1]**

The browser checks that the certificate is valid and was issued by a trusted Certificate Authority (CA), so it knows the server is the genuine bank **[1]**

A symmetric key is exchanged securely: the browser encrypts it using the server's public key, and only the server's private key can decrypt it **[1]**

All data sent between the browser and the web server is then encrypted using the symmetric key **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - the browser requests a secure connection // asks the web server to identify itself
> - the web server sends its digital certificate to the browser
> - ... the certificate contains the web server's public key
> - the browser checks that the certificate is valid / was issued by a trusted Certificate Authority (CA) ... so the web server is authenticated / genuine
> - a symmetric key is agreed / exchanged securely // the browser encrypts a symmetric key with the server's public key ... which only the server's private key can decrypt
> - all data sent between the browser and the web server is then encrypted using the symmetric key
> 
> **[4 marks]**
> 
> Accept "session key" for "symmetric key"
> 
> Do not award the final point for "all the data is encrypted using the server's public key". SSL/TLS uses the public key to exchange the symmetric key, and the symmetric key encrypts the data
> 
> Do not accept "the web server sends its private key to the browser". A private key is never transmitted
> 
> No marks for describing how the bank obtained its digital certificate from the CA. The question asks how the certificate is used, not how it is acquired

> **[exam-tip]**
> A common mistake is to mix up the two keys. The server's private key never leaves the server. The browser uses the server's public key, taken from the certificate, so that only the server can read the symmetric key.
> 
> Another mistake is to say that all of the data is encrypted with the public key. Asymmetric encryption is slower, so SSL/TLS uses it only to exchange the symmetric key. The faster symmetric encryption then protects the rest of the communication.

### Q7
Plain text is the original data, before it is encrypted, which can be read and understood **[1]**

Cipher text is the data produced by encryption, which is meaningless and cannot be understood without the key to decrypt it **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for plain text: the original / unencrypted data, which can be understood
> 
> **1 mark** for cipher text: the encrypted / scrambled data, which cannot be understood without the (decryption) key
> 
> Accept "readable" for "can be understood", and "scrambled" or "encoded" for "encrypted"
> 
> Do not accept "text with no formatting" for plain text, because that is a word-processing meaning, not the encryption meaning

> **[exam-tip]**
> Students often write that cipher text "cannot be intercepted". Encryption does not stop anyone intercepting the data. It makes the intercepted data meaningless to anyone who does not have the key.
> 
> Plain text does not have to be text. A photo or a spreadsheet is also plain text before it is encrypted.

### Q8
The password, date of birth and symptoms are personal, confidential data **[1]**

SSL/TLS encrypts this data while it travels between the patient's browser and the hospital's web server, so if it is intercepted it cannot be understood **[1]**

SSL/TLS authenticates the hospital's web server, so the patient knows they are entering their details on the genuine hospital website **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - the data being sent (password / date of birth / symptoms) is personal / confidential / sensitive
> - the data is encrypted between the browser (client) and the web server ... so it cannot be understood if it is intercepted
> - the web server is authenticated (using its digital certificate) ... so the patient knows the website is genuine / belongs to the hospital
> - SSL/TLS ensures the data is not altered during transmission, for example the booking details are not changed
> 
> **[3 marks]**
> 
> Award the first point only if at least one item of data from the scenario is named
> 
> Accept "a hacker who intercepts the password cannot read it" for the encryption point
> 
> Do not accept "SSL/TLS stops hackers intercepting the data". Intercepted data is still intercepted; it is meaningless because it is encrypted
> 
> Do not accept "SSL/TLS keeps the patient records secure on the hospital's server". SSL/TLS protects data while it is transmitted between the client and the server, not data stored on the server

> **[exam-tip]**
> Students often write a general answer about encryption that could describe any system. The question says "in this situation", so name the data from the scenario, such as the password or the symptoms, and say why it needs protecting.
> 
> SSL/TLS only protects data while it travels between the browser and the web server. Do not claim that it keeps the records safe once they are stored in the hospital's database. That needs a different security measure.

### Q9
To encrypt the data sent between the client and the server, so that the data cannot be understood if it is intercepted **[1]**

To authenticate the server, so that the client knows it is communicating with the genuine website **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - to encrypt data sent between a client and a server // to provide an encrypted connection between the two computers ... so that intercepted data cannot be understood
> - to authenticate the server // to confirm the identity of the website or organisation // to show that the data comes from a trusted source
> - to ensure that the data is not altered during transmission
> 
> **[2 marks]**
> 
> Accept "so that only the intended receiver can understand the data" as part of the encryption point
> 
> Award only **one** mark if both answers describe encryption, for example "it encrypts the data" and "hackers cannot read the data". These are the same point
> 
> Do not accept "to stop data being intercepted". Encryption does not stop interception; it makes intercepted data meaningless
> 
> Do not accept "to protect the computer from viruses" or "to block hackers from the server". These describe anti-virus software and a firewall, not SSL/TLS

> **[exam-tip]**
> The most common mistake is to write that SSL/TLS stops data from being intercepted. It does not. Data travelling across the internet can still be intercepted, but because it is encrypted the interceptor cannot understand it. Write "cannot be understood if intercepted".
> 
> The syllabus writes SSL/TLS as one term. Answer about SSL/TLS as a whole, and do not spend time comparing SSL with TLS.

### Q10
**Using the digital certificate**

- The digital certificate is issued by a Certificate Authority (CA), so it proves the identity of the company **[1]**
- The certificate provides the company's public key, so the computer knows this public key belongs to the company **[1]**

**Checking the digital signature**

- The digital signature is decrypted using the company's public key to recover the message digest that the company sent **[1]**
- The update that was received is hashed with the same (agreed) hashing algorithm to produce a second message digest **[1]**
- The two message digests are compared **[1]**
- If they are the same, the update came from the company and has not been altered. If they are different, the update has been altered

**[5 marks]**

> **[mark-scheme]**
> **Role of the digital certificate (max 2):**
> 
> - the certificate is issued by a CA // authenticates / proves the identity of the company
> - the certificate provides the company's public key
> 
> **Checking the digital signature (max 3):**
> 
> - the digital signature is decrypted with the company's (sender's) public key to recover the message digest sent
> - the received update is hashed with the agreed / same hashing algorithm to produce a message digest of the update received
> - the two message digests are compared
> - if they are the same the update has not been altered / is authentic // if they are different the update has been altered
> 
> **[5 marks]**
> 
> Accept digest for message digest
> 
> Accept for the second certificate point: the public key from the certificate is used to verify / validate the digital signature
> 
> Do not accept the digital signature being decrypted with the company's private key. Only the company holds its private key

> **[exam-tip]**
> The most common error is using the wrong key. The signature was made with the company's private key, so the customer's computer needs the matching public key, and it gets that key from the digital certificate.
> 
> Many students also skip the second hash. The computer cannot compare anything until it has hashed the update it received. Say that it uses the same hashing algorithm, and say that the two message digests are compared, not the signature and the update.

### Q11
- The online shop sends a request for a digital certificate to a Certificate Authority (CA) **[1]**
- The shop gives the CA the information it needs to prove the shop's identity **[1]**
- The CA checks / verifies the identity of the shop **[1]**
- If the identity is verified, the CA creates and issues the digital certificate, which includes the shop's public key **[1]**

**[4 marks]**

> **[mark-scheme]**
> **One mark for each point (max 4):**
> 
> - the shop makes a request / enquiry for a certificate to a Certificate Authority (CA)
> - the shop gathers / sends the information the CA needs to prove the shop's identity
> - the shop sends its public key to the CA // the public key is agreed with the CA
> - the CA checks / verifies the shop's identity / details
> - the CA creates / issues the certificate that includes the shop's public key
> 
> **[4 marks]**
> 
> Accept: data sent to or from the CA is encrypted using the CA's public key / private key
> 
> Do not accept the CA sending the shop its private key. The private key belongs to the shop and is never transmitted

> **[exam-tip]**
> Many answers say the shop "buys a certificate" or "downloads one" and stop there. That earns nothing. The mark scheme rewards the checking step: the CA must verify the identity of the shop before it issues anything, otherwise anyone could pretend to be the shop.
> 
> Be careful with the keys. The certificate carries the shop's public key. Students often write that the CA gives the shop a private key, which is wrong.

### Q12
**Link A**

The designs are valuable secrets, and quantum cryptography is virtually unhackable because any eavesdropping on the key can be detected. **[1]**

The two offices are close together and are already joined by a dedicated fibre optic cable, which quantum cryptography needs. **[1]**

**Link B**

The customers are in many different countries, but quantum cryptography only works over relatively short distances. **[1]**

The customers connect over the internet, so each one would need a dedicated fibre optic line and specialist hardware, which would be far too expensive for thousands of customers. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Link A, max 2 from:**
> 
> - the designs are valuable (industrial) secrets, and quantum cryptography is virtually unhackable // eavesdropping can be detected // longer keys can be used
> - the offices are close together, so the link is within the limited range of quantum cryptography
> - the dedicated fibre optic line that quantum cryptography requires is already in place
> 
> **Link B, max 2 from:**
> 
> - the customers are far away // in many different countries, and quantum cryptography only works over relatively short distances // has a limited range
> - the customers connect over the internet and do not have a dedicated fibre optic line and specialist hardware
> - the cost of dedicated fibre optic lines and specialist hardware for thousands of customers is too high
> 
> **[4 marks]**
> 
> If benefits and drawbacks are only listed, with no reference to either link, award a maximum of 2 marks
> 
> Do not accept "the offices have a wired connection" on its own for Link A: the requirement is a dedicated fibre optic line, not any wired connection
> 
> Do not accept that Link B is unsuitable because customer data is not secret: the drawbacks are the distance and the equipment, not the value of the data

> **[exam-tip]**
> The most common mistake is to write down two benefits and two drawbacks of quantum cryptography from memory, without saying which link each one applies to. The question gives you the clues: the distance between the sites, the dedicated cable and the number and location of the customers. Use each clue in your answer.
> 
> Notice the word dedicated. The customers are connected by the internet, and the internet is not a dedicated fibre optic line between two points. That is why Link B would need new lines and specialist hardware for every customer.

### Q13
- The identity details of the owner, for example the name of the company or website owner **[1]**
- The owner's public key **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - information that identifies the owner of the certificate (the company / the website owner / the individual)
> - the owner's public key
> 
> **[2 marks]**
> 
> Accept the name of the Certificate Authority (CA) that issued the certificate, the date the certificate expires, or the digital signature of the CA, as one item each
> 
> Do not accept the owner's private key. A private key is kept secret by its owner and is never sent to anyone, so it cannot be inside a certificate that is shared with the public

> **[exam-tip]**
> The most common wrong answer is "the private key". A digital certificate is shared openly, so it can only hold the public key. If the private key were in the certificate, anyone could use it.
> 
> Write "public key" in full. The answer "a key" is not enough, because it does not say which key.

### Q14
The security of quantum cryptography is based on the laws of physics (the principles of quantum mechanics), not on mathematical algorithms. **[1]**

Any eavesdropping on the key can be detected... **[1]**

...because eavesdropping changes the properties of the photons, so the state of the key is changed. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - security is based on the laws of physics // principles of quantum mechanics // properties of photons, rather than on mathematical algorithms
> - it is virtually unbreakable // virtually unhackable
> - eavesdropping on the key can be detected...
> - ...because the state // properties of the photons will be changed
> - the integrity of the key once transferred can be guaranteed // the key cannot be copied and decrypted at a later date
> - longer // more secure keys can be exchanged
> 
> **[3 marks]**
> 
> Award the "because the state is changed" point only together with the point that eavesdropping can be detected
> 
> Do not accept "it uses a public key and a private key": that describes asymmetric cryptography, not quantum cryptography

> **[exam-tip]**
> Many students answer this by describing asymmetric encryption, with a public key and a private key. That is a different method and earns nothing here.
> 
> "Eavesdropping can be detected" is only one mark. On a 3-mark explain question, add the reason: the eavesdropping changes the properties of the photons. Then give a separate point, such as the security coming from the laws of physics rather than from mathematical algorithms.

### Q15
Quantum cryptography currently only works over relatively short distances. **[1]**

It needs a dedicated fibre optic line and specialist hardware. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - only works over relatively short distances // limited range
> - requires a dedicated fibre optic line and specialist hardware
> - high cost of buying // maintaining the equipment (the dedicated fibre optic line and specialist hardware)
> - the polarisation of light can change during transmission along the fibre optic cable
> - error rates are relatively high because the technology is still being developed
> - lacks features such as digital signatures // certified mail
> - allows criminals and terrorists to hide their communications
> 
> **[2 marks]**
> 
> Accept "the equipment is expensive" for the cost point
> 
> Do not accept a drawback of symmetric encryption, such as "the key has to be shared with the receiver"

> **[exam-tip]**
> Vague answers are the usual way to lose marks here. "It is new technology" does not match a marking point, so say what the newness causes: error rates are still relatively high. In the same way, "it is complicated" is too vague; name what it needs, which is a dedicated fibre optic line and specialist hardware.
> 
> Do not mix this topic up with symmetric and asymmetric encryption. Problems with sharing a key are a reason to use quantum cryptography, not a drawback of it.

### Q16
> **[mark-scheme]**
> **One **mark per mark point (**Max 4**)
> 
> MP1 Sheila’s computer uses an algorithm to generate a matching pair of keys private and public
> 
> MP2 Sheila’s computer sends Fred’s computer Sheila’s public key // Fred‘s computer acquires Sheila’s public key
> 
> MP3 Fred’s computer encrypts the document/plain text using Sheila’s public key to create cipher text
> 
> MP4 Fred’s computer sends the cipher text to Sheila’s computer The **cipher text** can only be decrypted using Sheila’s private key // Sheila’s computer uses Sheila’s private key to decrypt the cipher text.

### Q17
> **[mark-scheme]**
> **One **mark per point (**max 3**)
> 
> MP1 A digital certificate is an electronic/online document.
> 
> MP2 used to authenticate/prove the identity of a website/the online identity of an individual/organisation
> 
> MP3 typically issued by a CA
> 
> MP4 For example: it contains information identifying a website owner/individual and a public key
> **[mark-scheme]**
> **One **mark per point (**max 2**)
> 
> MP1 The digital certificate **provides the public key **
> 
> MP2 … that can be used to validate the private key associated with the organisation/website/digital signature
