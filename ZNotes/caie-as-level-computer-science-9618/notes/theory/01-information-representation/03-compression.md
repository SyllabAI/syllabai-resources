## Compression

* **Definition:** Compression is the process of reducing file size without significant loss in quality, resulting in:
  * Reduced time needed to search for data.
  * Faster transfer of compressed files, using less bandwidth than uncompressed files.

  
---
* **Lossless Compression**
  * *Definition:* A type of compression that allows original data to be perfectly reconstructed from a compressed file by utilizing some form of replacement.
  * *Examples:* Bitmap (.bmp), vector graphic (.svg), .png images, text file compression, database records.
  * *Run-Length Encoding (RLE):*
    * `Definition:` A form of lossless compression used for compressing text files and bitmap images.
    * `Mechanism:` Reduces file size by encoding sequences of adjacent, identical elements (characters in text files and pixels in bitmap images) into two values: run count and run value.
    * `Example:` RLE of a bitmap image.

  
---
* **Lossy Compression**
  * *Definition:* A type of compression that irreversibly eliminates unnecessary data.
  * *Effect:* File accuracy/quality is lower than with lossless compression, but file size is significantly reduced (often to about 10% of the lossless size).
  * *Examples:* Sound files (.mp3), .jpeg images.
  * *Mechanism in Sound Files:*
    * `Perceptual Coding:` Removes parts of the sound that are less audible or discernible to human hearing, as used in .mp3 compression.



