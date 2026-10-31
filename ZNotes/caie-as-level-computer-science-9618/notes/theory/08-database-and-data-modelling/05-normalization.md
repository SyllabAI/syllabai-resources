## Normalization

**1<sup>st</sup> Normal Form (1NF):** contains no repeating attribute or
groups of attributes. Intersection of each tuple and attribute contains
only 1 value. Example:

 ![](../../../assets/50d036043056-image020.png)

**2<sup>nd</sup> Normal Form (2NF):** it is in 1NF and every non-primary
key attribute is fully dependent on the primary; all the incomplete
dependencies have been removed. Example:

 ![](../../../assets/43e03c7d8f2e-image021.png)

**3<sup>rd</sup>** **Normal Form (3NF):** it is in 1NF and 2NF and all
non-key elements are fully dependent on the primary key. No
inter-dependencies between attributes.

* MANY-TO-MANY functions cannot be directly normalized to 3NF, must
  use a 2 step process e.g.

 ![](../../../assets/b81035d18f53-image022.png)

becomes:

 ![](../../../assets/2887ddc88793-image023.png)