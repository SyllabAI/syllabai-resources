# Prim’s Algorithm

Prim’s algorithm is another method to find a minimum spanning tree, it starts with a single vertex and repeatedly adds edges already in the MST to a vertex.

Steps for using Prim’s algorithm:

1. Start by choosing any vertex from the diagram

2. Choose the arc of least weight that joins the chosen vertex, if there are multiple arc of the same weight you can choose any one

3. Follow the vertex of the chosen arc and repeat step 2 until a tree is formed

4. List the arc in the correct order

Example of using Prim’s algorithm

![](../../../assets/1fbc92bbc426-117e0892b97db5d2457f3c83.webp)

Select a starting vertex, we’ll start with D

![](../../../assets/4c03641ed389-c708611692fe592d8c0dbad1.webp)

Choose the least weight of arc connecting to D, in this case it’s F-D

![](../../../assets/c7fe728829b2-4c06150000a962b84696f8d7.webp)

Following the same order, next least arc is F-C

![](../../../assets/837a52c3fe0e-8402554771c57a7461eabae4.webp)

Next least arc added is B-C

![](../../../assets/aef1c227e578-964624777d4fc3d9ebfc8bb9.webp)

Next arc added is B-A

![](../../../assets/c7c89eaf5850-d6951f52bc6aaf13ef1e0d9b.webp)

Next arc is D-E, it will not be A-E, since D-E (19) is of lesser weight than 21 any other arc such as 23,25,20 would create a cycle.

![](../../../assets/776ad57546e1-f01816b1ad7bf94f38df8094.webp)

Final spanning tree.