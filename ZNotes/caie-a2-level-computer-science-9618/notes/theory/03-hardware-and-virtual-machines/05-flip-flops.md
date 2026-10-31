## Flip-Flops

* Flip flops can store a single bit of data as 0 or 1
* Computers use bits to store data.
* Flip-flops can be used to store bits of data.
* Memory can be created from flip-flops.

### **SR Flip Flops**

- Can be made with NAND gates or NOR gates
- Error state exists

![](../../../assets/4d279d36cf1f-allimages88fb5fe0e36e85a8637ce976.png)


|**S**|**R**|**Q**|**Q Bar**|
|:---|:---|:---|:---|
|0|0|1|1|
|0|1|1|0|
|1|0|0|1|
|1|1|No Change|No Change|

* 00 causes an error as Q Bar is no longer the complement of Q

* 01 sets Q to 1

* 10 resets Q to 0

* 11 leads to no change; the initial value remains

![](../../../assets/d300b1195b23-allimagesd672871d6aa5cf17022e92ba.png)


|**S**|**R**|**Q**|**Q Bar**|
|:---|:---|:---|:---|
|0|0|No Change|No Change|
|0|1|0|1|
|1|0|1|0|
|1|1|0|0|

* 11 causes an error as Q Bar is no longer the complement of Q

* 10 sets Q to 1

* 01 resets Q to 0

* 00 leads to no change; the initial value remains

### **JK Flip Flops**

* JK flip flops are only active when the clock is high.
* JK flip flops use a clock pulse for synchronization to ensure proper functioning.
* Advantages of JK flip flops include the validity of all input combinations, avoidance of unstable states, and increased stability compared to SR flip flops.

![](../../../assets/71f9e2965472-allimages6c080486c1f1ec8ed3fdce22.png)


|**Clock**|**J**|**K**|**Q**|**Q Bar**|
|:---|:---|:---|:---|:---|
|0|0|0|-|-|
|0|0|1|-|-|
|0|1|0|-|-|
|0|1|0|1|1|
|1|0|0|No Change|No Change|
|1|0|1|0|1|
|1|1|0|1|0|
|1|1|1|1|1|
