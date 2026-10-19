# Mark Schemes — Compression
**1. Information representation** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (21 questions)


### Q1
(i)

`11C 14E 190 122 1FD 107 1B3 16A` **[1]**

(ii)

Before compression = 8 pixels × 1 byte = **8 bytes** **[1]**

After compression = 8 pairs × 2 bytes = **16 bytes** **[1]**

(iii)

No two pixels that are next to each other have the same colour, so every run has a length of 1. **[1]**

Each pixel is now stored as a count and a colour value, which needs 2 bytes instead of 1, so RLE has made the row twice as large instead of smaller. **[1]**

**[5 marks]**

> **[mark-scheme]**
> (i)
> 
> **1 mark** for all eight pairs correct, each with a count of 1: `11C 14E 190 122 1FD 107 1B3 16A`
> 
> (ii)
> 
> **1 mark** for `8 bytes` before compression
> 
> **1 mark** for `16 bytes` after compression
> 
> (iii)
> 
> **1 mark** for there are no runs of identical consecutive pixels // every run length is 1 // no colour repeats next to itself
> 
> **1 mark** for each pixel now needs 2 bytes instead of 1 // the compressed row is larger than the original // the size has doubled, so there is no saving
> 
> Accept a follow-through mark in part (iii) for a correct comparison of the two sizes you gave in part (ii)
> 
> Do not accept "RLE does not work on photographs" on its own, because it does not say why
> 
> Do not accept "data is lost", because RLE is lossless and nothing is lost here
> 
> Do not accept "the image has too many colours" on its own; the marking point is that the colours do not repeat in consecutive pixels

> **[exam-tip]**
> RLE only saves space when the same colour repeats in consecutive pixels. Where there is a lot of colour detail, as in a photograph, RLE can make the file larger, and this is exactly the case examiners use to check whether you have understood the method or only memorised it.
> 
> Do the arithmetic before you write the explanation. Count the pairs, multiply by 2, and compare that with the number of pixels. If you assume compression must always reduce a file size, you can calculate 16 bytes correctly and then still write that the file has got smaller, contradicting your own working.

### Q2
(i)

`D2 D2 D2 D2 A7 A7 D2 D2 D2 D2 D2 D2 FF` **[1]**

(ii)

Uncompressed row = 13 pixels × 1 byte = 13 bytes

Compressed row = 4 pairs × 2 bytes = 8 bytes **[1]**

Bytes saved = 13 - 8 = **5 bytes** **[1]**

**[3 marks]**

> **[mark-scheme]**
> (i)
> 
> **1 mark** for all 13 colour values in the correct order: `D2 D2 D2 D2 A7 A7 D2 D2 D2 D2 D2 D2 FF`
> 
> (ii)
> 
> **1 mark** for both sizes correct: 13 bytes uncompressed and 8 bytes compressed
> 
> **1 mark** for a saving of `5 bytes`
> 
> Accept the saving expressed as `40 bits`
> 
> Accept a follow-through mark for a saving correctly calculated from an incorrect row in part (i)
> 
> Do not accept `9 bytes`, which counts each RLE pair as 1 byte instead of 2
> 
> Do not accept `4 bytes` as the compressed size, which counts the number of pairs rather than the number of bytes they occupy

> **[exam-tip]**
> An RLE pair costs two bytes, not one: one byte holds the count and one byte holds the colour value. Counting the four pairs as four bytes gives a saving of 9 bytes and loses both calculation marks.
> 
> Notice that colour `D2` appears in two separate pairs. RLE only merges pixels that are next to each other, so a colour that comes back later in the row starts a new pair. Do not add the two runs of `D2` together.

### Q3
| Uncompressed image data | RLE compressed image data |
|---|---|
| `3A 3A 3A B7 B7` | `33A 2B7` |
| `C4 C4 09 09 09 09 5E` | `2C4 409 15E` [1] |
| `FF FF A0 FF FF FF` [1] | `2FF 1A0 3FF` |

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for `2C4 409 15E`
> 
> **1 mark** for `FF FF A0 FF FF FF`
> 
> Accept a space between the count and the colour value, for example `2 C4 4 09 1 5E`
> 
> Do not accept `2C4 409 5E`, which leaves the count of 1 off the single pixel
> 
> Do not accept `C42 094 5E1` or any form that puts the colour value before the count
> 
> Do not accept `FF FF A0 FF FF` or `FF FF A0 FF FF FF FF`, which decode the last pair with the wrong count

> **[exam-tip]**
> The count is always written first and the colour value second. Reversing them to `C42` is the most common error here, and it makes the data impossible to decode because you cannot tell where one pair ends and the next begins.
> 
> A pixel that appears only once still needs a count of `1` in front of it. Writing `5E` on its own breaks the pattern of pairs, so the row cannot be read back correctly.

### Q4
| File | Description of how the file can be compressed |
|---|---|
| Text file | **A lossless method such as run-length encoding is used.** **[1]** **A sequence of identical consecutive characters is replaced by that character and a count of the number of repeats.** **[1]** |
| Bitmap photograph | **A lossy method is used.** **[1]** **Similar colours are grouped together so that fewer colours have to be stored, and the change is not noticed by the human eye.** **[1]** |
| Vector graphic | **The drawing list is stored as text, so a lossless text compression method is applied to it.** **[1]** **Repeated sequences of characters in the list of drawing objects and their properties are replaced by a shorter code.** **[1]** |

**[6 marks]**

> **[mark-scheme]**
> **1 mark** for a correct method and **1 mark** for a matching description, in each row, to a maximum of 2 marks per row
> 
> Text file
> 
> **1 mark** for run-length encoding // a lossless method
> 
> **1 mark** for a sequence of identical consecutive characters is replaced by that character and a count of the repeats
> 
> **1 mark** for the method must be lossless so that no characters are lost and the text still makes sense
> 
> Bitmap photograph
> 
> **1 mark** for a lossy method
> 
> **1 mark** for similar colours are grouped together so fewer colours are stored
> 
> **1 mark** for the colour depth is reduced so fewer bits are used for each pixel
> 
> **1 mark** for the image resolution is reduced so fewer pixels are stored
> 
> Vector graphic
> 
> **1 mark** for the file is a drawing list stored as text, so a lossless text compression method can be applied
> 
> **1 mark** for repeated sequences of characters in the drawing objects and their properties are replaced by a shorter code
> 
> **1 mark** for the method must be lossless, because losing a property or a coordinate would change the shape that is drawn
> 
> Do not accept "it is compressed" or "the file size is reduced" in any row, because neither describes a method
> 
> Do not accept a lossy method for the text file or for the vector graphic
> 
> Do not accept a file format name on its own, for example "JPEG" or "MP3", with no description of what the compression does

> **[exam-tip]**
> Each row is worth 2 marks, so each row needs two separate statements: what kind of compression is used, and what that compression actually does to the data. A single word such as "lossless" answers half the row and earns half the marks.
> 
> The vector graphic row catches students out. A vector graphic is not a grid of pixels, so there is nothing to group or average. It is a drawing list of objects and their properties held as text, so it is compressed the way text is compressed, and it must stay lossless because dropping one property changes the picture.

### Q5
(i)

Working: (2400 × 1800 × 24) / 8 = 12 960 000 bytes **[1]**

12 960 000 / 1000 / 1000 = 12.96

Answer: **12.96 MB** **[1]**

(ii)

Reduction in size = 12.96 - 3.24 = 9.72 MB

9.72 / 12.96 × 100 = **75%** **[1]**

**[3 marks]**

> **[mark-scheme]**
> (i)
> 
> **1 mark** for correct working: `(2400 × 1800 × 24) / 8 / 1000 / 1000`
> 
> **1 mark** for the answer `12.96 MB`
> 
> Accept `12 960 000 bytes` as an intermediate step, but the final answer must be given in MB
> 
> Do not accept `12.36`, which comes from dividing by 1024 twice. On this syllabus a megabyte uses a decimal prefix, so 1 MB is 1 000 000 bytes; dividing by 1024 twice gives mebibytes
> 
> Do not accept `103 680 000`, which is the size in bits
> 
> (ii)
> 
> **1 mark** for `75%`
> 
> Accept a follow-through mark for a percentage correctly calculated from an incorrect answer to part (i)
> 
> Do not accept `300%`, which divides the saving by the compressed size instead of by the original size
> 
> Do not accept `25%`, which is the compressed size as a percentage of the original rather than the reduction

> **[exam-tip]**
> Watch the units. On 9618, kilo, mega and giga are decimal prefixes (1000), while kibi, mebi and gibi are binary prefixes (1024). Dividing by 1024 twice gives 12.36 and loses the mark, even though the working looks sensible.
> 
> A percentage reduction is always measured against the original size. Dividing the 9.72 MB saving by the 3.24 MB compressed size gives 300%, which is impossible: a file cannot shrink by more than 100%. If your percentage comes out above 100, you have divided by the wrong number.

### Q6
The sampling rate can be reduced, so fewer samples are stored for each second of sound. **[1]**

Sounds that the listener will not notice can be removed, for example frequencies that are outside the range of human hearing. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for each of two different ways, to a maximum of 2
> 
> **1 mark** for reduce the sampling rate // take fewer samples of the sound each second
> 
> **1 mark** for reduce the sampling resolution // use fewer bits to store each sample
> 
> **1 mark** for remove frequencies that are outside the range of human hearing
> 
> **1 mark** for remove quieter sounds that are masked by louder sounds
> 
> Do not accept "make the file smaller" or "remove some of the data", because neither states what is removed
> 
> Do not accept two versions of the same idea, for example "lower the sampling rate" and "take fewer samples per second", which together earn 1 mark only
> 
> Do not accept naming a file format on its own, for example "save it as an MP3"

> **[exam-tip]**
> Two ways means two different mechanisms. "Reduce the sampling rate" and "take fewer samples each second" are the same statement written twice, so they earn one mark, not two.
> 
> Naming a format is not a description. "It is saved as an MP3" says nothing about what the compression removes from the file, so it scores zero. Always say what is taken out and why the listener does not notice.

### Q7
**File A: lossless compression** **[1]**

An installation program only runs if every byte of the file is restored exactly. Lossless compression is reversible, so the decompressed file is identical to the original. If any data were removed, the program would be corrupted and would not install. **[1]**

**File B: lossy compression** **[1]**

A photograph on a website can lose some detail without the change being noticeable to the human eye. Lossy compression gives a much greater reduction in file size than lossless, so the pages load faster and less bandwidth is used. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for identifying lossless compression for File A
> 
> **1 mark** for a justification for File A: an executable file must be restored exactly, bit for bit // removing any data would corrupt the program so it would not run or install // lossless is reversible so the original file is recovered
> 
> **1 mark** for identifying lossy compression for File B
> 
> **1 mark** for a justification for File B: the loss of detail is not noticeable to the human eye // lossy gives a greater reduction in file size than lossless, so the photographs download faster and use less bandwidth
> 
> Accept "the program would be corrupted", "the program would not install" and "the program would not run" for the File A justification
> 
> A response that chooses lossless for File B can earn both File B marks, but only if it is justified by a stated need for the photographs to keep their exact original detail, for example accurate product colours
> 
> Do not accept lossy compression for File A under any justification. Removing data from an executable file makes it unusable, however large the saving in file size
> 
> Do not accept a bare "lossless" and "lossy" with no reasons. The identification marks are awarded, but the two justification marks are not

> **[exam-tip]**
> Half of the marks here are for the justification, not for the choice, so naming the two types of compression and stopping gets you two marks out of four. For each file, say what would go wrong if the other method were used.
> 
> The error to avoid is choosing lossy for anything that has to work exactly as it was written. An installation program, a spreadsheet and a text document all break if data is removed, however small the file becomes. Lossy is only ever suitable where a small loss of detail does not matter, which in practice means images, video and sound.

### Q8
Lossy compression permanently removes data from a file, so some of the characters in the report would be lost. **[1]**

Lossy compression cannot be reversed, so those characters could not be put back when the file is decompressed and the report would no longer make sense. **[1]**

Lossless compression is reversible, so the file is returned to its exact original state when it is decompressed and every character of the report is still present. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each point, to a maximum of 3:
> 
> **1 mark** for lossy permanently removing data // characters from the file
> 
> **1 mark** for lossy not being reversible, so the removed characters cannot be restored
> 
> **1 mark** for the loss of characters changing the meaning of the report // making the report inaccurate or unreadable
> 
> **1 mark** for lossless being reversible // the original file being restored exactly when it is decompressed
> 
> **1 mark** for lossless removing no data, so every character of the report is kept
> 
> Accept "text", "words" or "letters" in place of "characters"
> 
> Do not accept "lossy would reduce the quality of the text". A text file has no quality setting to reduce; the problem is that missing characters cannot be recovered
> 
> Do not accept "lossless makes the file smaller", because both methods make the file smaller and that is not a reason to choose one of them

> **[exam-tip]**
> Students often answer this question by describing image compression, writing about pixels, colours and blurring. This file is text, so the answer must be about characters and about the meaning of the report being lost.
> 
> A second common error is to say that lossy "compresses too much". The size of the reduction is not the problem. The problem is that the removal is permanent, so a text file compressed with a lossy method can never be returned to its original state.

### Q9
Lossy compression permanently removes some of the data from the file, while lossless compression removes none of the original data. **[1]**

Lossy compression cannot be reversed, so the original file cannot be restored, while lossless compression can be reversed and returns the file to its exact original state. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for each difference, to a maximum of 2. Each answer must say something about both types of compression:
> 
> **1 mark** for lossy permanently removing data while lossless removes none of the original data
> 
> **1 mark** for lossy not being reversible while lossless is reversible // the original file can be restored exactly with lossless but not with lossy
> 
> **1 mark** for lossy usually producing a smaller file than lossless
> 
> **1 mark** for lossy reducing the quality of the file while lossless does not change the quality
> 
> Accept "irreversible" for lossy and "reversible" for lossless
> 
> Do not accept a statement about only one type, such as "lossy removes data". That is a fact, not a difference
> 
> Do not accept "lossy loses more data than lossless", because lossless loses no data at all

> **[exam-tip]**
> The command word is "state two differences", so every point must mention lossy and lossless. "Lossy removes data" describes one method only and earns nothing, however true it is. Write each point as a single sentence with the word "while" or "whereas" in the middle and you cannot get this wrong.
> 
> The other frequent error is writing that lossless "only loses a little data". Lossless loses none. If even one bit were lost, the file could not be returned to its exact original state, and that is the whole purpose of lossless compression.

### Q10
Uncompressed file size in bits: 900 × 8 = 7200 Mb **[1]**

Uncompressed download time: 7200 ÷ 12 = 600 seconds **[1]**

Compressed file size: 30% of 900 MB = 270 MB, which is 270 × 8 = 2160 Mb, so the compressed download time is 2160 ÷ 12 = 180 seconds **[1]**

Time saved: 600 - 180 = 420 seconds **[1]**

**[4 marks]**

> **[mark-scheme]**
> **1 mark** for converting the uncompressed file size to bits: 900 × 8 = 7200 Mb // 7 200 000 000 bits
> 
> **1 mark** for the uncompressed download time of 600 seconds
> 
> **1 mark** for the compressed file size of 270 MB and its download time of 180 seconds
> 
> **1 mark** for the time saved of 420 seconds
> 
> Accept 420 seconds written as 7 minutes
> 
> Accept working carried out entirely in bits, for example 7 200 000 000 ÷ 12 000 000 = 600
> 
> Award the method marks for correct working even when the final subtraction is wrong
> 
> Do not accept 52.5 seconds. That answer treats the transfer rate as 12 megabytes per second and ignores the 8 bits in a byte
> 
> Do not accept 180 seconds or 600 seconds on their own, because the question asks for the difference between the two times

> **[exam-tip]**
> The single most common error in this type of question is mixing bits and bytes. File sizes are given in bytes and transfer rates are given in bits per second, so multiply the file size by 8 before you divide by the rate. Read the units in the question twice before you start.
> 
> The second error is stopping too early. You are asked for the time saved, not for the two download times, so you must subtract. Write both times down clearly and then subtract, so that the method marks are still available if one step of the arithmetic goes wrong.

### Q11
The compressed file contains fewer bits than the original file, so there are fewer bits to send across the satellite link. **[1]**

This reduces the transmission time, so the readings reach the central server sooner. **[1]**

Less bandwidth is used on the satellite link, so the owner pays for less data. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for each point, to a maximum of 3:
> 
> **1 mark** for there being fewer bits // a smaller file to transmit
> 
> **1 mark** for the transmission time being reduced // the readings arriving sooner
> 
> **1 mark** for less bandwidth being used // other transmissions on the link not being affected
> 
> **1 mark** for less of the paid data allowance being used // the cost of sending the data being lower
> 
> **1 mark** for less storage space being used on the central server when the file arrives
> 
> Accept "the file uploads faster" for the transmission time point
> 
> Do not accept the same idea written three times, for example "it is smaller", "it takes up less space" and "it is not as big". Those are one marking point, not three
> 
> Do not accept "the satellite link becomes faster", because compression does not change the data transfer rate of the link

> **[exam-tip]**
> The most common way to lose marks here is to write one idea three times in three different ways. Three bullet points that all say the file is smaller earn one mark. Give three different consequences instead: transmission time, bandwidth or cost, and storage space.
> 
> Watch the second trap too. The transfer rate of the link is fixed by the satellite connection. Compression reduces the amount of data you send over that link, it does not speed the link up.

### Q12
Compression is the process of reducing the number of bits used to store a file, so the file uses less space in secondary storage. **[1]**

A compressed file also has fewer bits to send across a network, so it takes less time to transmit. **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for the reduction: reducing the size of a file // reducing the number of bits or bytes used to store the file
> 
> **1 mark** for a consequence of that reduction: less secondary storage space is used, or the transmission time across a network is reduced, or less bandwidth is used
> 
> Accept "encoding a file so that it uses fewer bits" for the first mark
> 
> Do not accept "deleting files to make space", because compression changes how one file is stored and does not remove files
> 
> Do not accept "the file opens faster" or "the computer runs faster", because compression changes the size of a file and not the processing speed of the computer

> **[exam-tip]**
> An answer that only says "it makes the file smaller" repeats the question and earns one mark at most. Say what is made smaller, which is the number of bits used to store the file, and then say why that matters, which is storage space or transmission time.
> 
> Be careful with the word "delete". Compression does not delete a file. Even lossy compression keeps the file, it just stores less detail inside it.

### Q13
(i) A (very) large **file **is created // redundant zeroes are stored in the file

(ii) One mark for:

- Values are delimited by a special character / a separator character
- First character indicates **sample **length

**Max 1 mark**

(iii) The **algorithm **to **store **/ **extract / separate **the individual values is more complex / takes longer to execute / run / process

NE Algorithm is more complicated

### Q14
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**).
> 
> - To reduce the time it takes to download the program files from the web server // to upload them to the server in the first place
> - To reduce the amount of storage space used on the web server // user’s device

### Q15
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 3**)
> 
> Lossy compression (ticked)
> 
> - Loss of quality will not be noticed
> - Needs to be viewed in real time so less bandwidth needed if file size smaller
> - Smaller file sizes will reduce buffering so the video will play more smoothly
> - Viewers may watch on different devices, so may not need high quality resolution
> 
> Lossless compression (ticked)
> 
> - Original recording may not have been made in high resolution
> - Could be streaming to high bandwidth devices
> - The reduction in the file size is sufficient for the receiving device
> - Viewers do not want any loss of quality

### Q16
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> - Reduced bandwidth usage when transmitting the message
> - Reduced transmission time from email client to email server
> - Reduced storage space **on the email**
> - Email accounts often have a maximum size for an attachment

### Q17
> **[mark-scheme]**
> (i)** 1 mark** each to **max 3**:
> 
> - The file takes less storage space on the web server than if lossless compression was used
> - The file is faster to upload/download to/from the server than if lossless compression was used
> - The file uses less bandwidth to transmit than if lossless compression was used
> - The file consumes less data allowance than if lossless compression was used
> 
> (ii) **1 mark **each:
> 
> - Identifies **consecutive **repeating **pixels **of the same colour
> - Stores the colour /pattern and the number of times it repeats

### Q18
> **[mark-scheme]**
> **1 mark** each to **max 2**:
> 
> - Dedicated connection to the headset // not sharing bandwidth
> - Already fast connection that can transmit the data without slowing
> - Video may already be a small file size and does not need further reduction
> - Video is not saved so storage is not an issue in the headset

### Q19
> **[mark-scheme]**
> **1 mark** for each bullet point (**max 2**)
> 
> e.g.
> 
> - The change may not be noticeable // Data removed is usually not noticed by the human eye
> - … for example, changes in shade/detail
> - It produces a larger decrease in file size compared to lossless // Lossy decreases file size considerably

### Q20
> **[mark-scheme]**
> **1 mark **for correct method
> 
> For example:
> 
> - Run-Length Encoding

### Q21
> **[mark-scheme]**
> (i)** 1 mark **for each bullet point (**max 3**)
> 
> e.g.
> 
> - Less of the teacher’s storage space is used
> - ... so more student work can be stored
> - Transmission time is reduced
> - … so the teacher does not have to wait as long for it to arrive
> - Bandwidth usage is reduced
> - … so other transmissions are not adversely affected
> - Less data allowance is used on the teacher’s email system
> 
> (ii) **1 mark** for each bullet point (**max 3**)
> 
> - Run-Length Encoding // RLE
> - Repeated sequences of the same characters are replaced by
> - ... a single copy of the character
> - ... and a count of the number of characters
