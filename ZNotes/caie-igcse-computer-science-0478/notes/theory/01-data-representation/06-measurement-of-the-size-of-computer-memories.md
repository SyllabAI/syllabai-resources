## Measurement of the Size of Computer Memories

* A binary digit is referred to as a **BIT**
* 8 bits is a **byte**
* 4 bits is a **nibble**
* Byte is used to measure memory size

### **IEC System / Binary Prefixes(Most Common)**


|Name of memory size|No. of Bytes|Equivalent Denary Value|
|:---|:---|:---|
|1 kibibyte (1KiB)|2<sup>10</sup>|1 024 bytes|
|1 mebibyte (1MiB)|2<sup>20</sup>|1 048 576 bytes|
|1 gibibyte (1GiB)|2<sup>30</sup>|1 073 741 824 bytes|
|1 tebibyte (1TiB)|2<sup>40</sup>|1 099 511 627 776 bytes|
|1 pebibyte (1PiB)|2<sup>50</sup>|1 125 899 906 842 624 bytes|

### **Conventional System ( SI units)**


|Name of memory size - SI units|No. of Bytes|Equivalent Denary Value|
|:---|:---|:---|
|1 kilobyte (1KB)|10<sup>3</sup>|1 000 bytes|
|1 megabyte (1MB)|10<sup>6</sup>|1 000 000 bytes|
|1 gigabyte (1GB)|10<sup>9</sup>|1 000 000 000 bytes|
|1 terabyte (1TB)|10<sup>12</sup>|1 000 000 000 000 bytes|
|1 petabyte (1PB)|10<sup>15</sup>|1 000 000 000 000 000 bytes|

### **Calculation of File Size**

* The file size of an image is calculated as image resolution (in pixels) × colour depth (in bits)
* The size of a mono sound file is calculated as sample rate (in Hz) × sample resolution (in bits) × length of sample (in seconds). `(For a stereo sound file, you would then multiply the result by two because the Left and Right channels are stored separately.)`

### Sample Question:

find the size of bitmap image with the width 500 and height 500. The color depth of this image is 24.

### working:

(500 x 500 x 24)

= 6,000,000 bits
(bit to bytes) /8 = 750,000 bytes

(bytes to KiB) /1024 = 732 KiB

### or:

24 bits = 3 bytes

(500 x 500 x 3)

= 750,000 bytes

(bytes to KiB) /1024 = 732 KiB