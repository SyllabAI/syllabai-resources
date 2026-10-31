## Lossless and Lossy File Compression

### **Lossless File Compression**

* All the data bits from the original file are reconstructed again when the file is uncompressed.
* Important for files where the loss of data would be disastrous (spreadsheet)
* An algorithm is used to compress data
* No data is lost
* Repeated patterns/text are grouped together in indexes

### **Run-Length Encoding**

* It reduces the size of a string of adjacent, identical data (e.g. repeated colours in an image)
* A repeating string is encoded into two values: the first value represents the number of identical data items (e.g. characters), and the second value represents the code of the data item (such as ASCII code if it is a keyboard character), e.g. ‘aaaaabbbbccddddd’ becomes “05 97 04 98 02 99 05 100.”
* RLE is only effective where there is a long run of repeated units/bits
* One difficulty is that RLE compression isn't perfect for strings like "cdcdcdcdcd". We use a flag to solve this; e.g., 255 can be made as the flag. Now 255 will be put before every repeating value, e.g. our previous example becomes `255 05 97 255 04 98 255 02 99 255 05 100` where 255 now indicates that the next character/set of characters is approaching

### **Lossy File Compression**

* The file compression algorithm eliminates unnecessary data bits like in MP3 and JPEG formats.
* It is impossible to get the original file back once it is compressed
* Reduces file quality
  * In this, the image's size is reduced. 