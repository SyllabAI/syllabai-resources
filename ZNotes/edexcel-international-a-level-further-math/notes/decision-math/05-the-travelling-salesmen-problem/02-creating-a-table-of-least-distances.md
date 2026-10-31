# Table of least distances

To create a table of least distance you create a distance matrix, except instead of adding the direct weight between 2 vertices you calculate the smallest possible weight.

Example :

![](../../../assets/3b97f8a82029-d4c81ecf94f9d68be65b43c3.webp)

![](../../../assets/07dc4675911b-59c22870aeb772beec9d3e6a.webp)

The above image shows the table of least distances for the graph, notice that even though A-D had a direct connection of weight 10, reaching D through B is of weight 8 which is lesser than 10

Even for A-C, reaching C through B gave a value of 7 being lesser than 8.