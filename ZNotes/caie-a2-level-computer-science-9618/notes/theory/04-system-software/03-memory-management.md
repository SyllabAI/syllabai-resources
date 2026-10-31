## Memory Management

### Virtual Memory

Temporarily using secondary storage to simulate additional main memory, as only part of a program needs to be in RAM. Data is swapped between the two.

Paging

A large process is divided into pages of equal sizes.

1. The RAM is divided into frames.

2. Virtual memory is divided into same-sized blocks called pages with fixed sizes.

3. Page table created to translate logical address to physical addresses and track all the free frames.

4. Pages are swapped between them as necessary.

5. When there is no empty space in the memory, a page gets replaced with the new one. The replacement algorithm is either first in first out, least used page and recently least used page.

**Page**

Virtual memory is divided into equal blocks called pages.

### Page Frame

Main memory is divided into parts equal in size to a page.

### Page Table

Contains the mappings of pages to page frames.

### Segmentation

A large process is divided to segments, the segments need not be the same size.

### Disk Thrashing

When pages are needed in the RAM as soon as they are moved to the disk leading to a continuous swapping of the same pages because the pages being swapped in and out are inter-dependent.