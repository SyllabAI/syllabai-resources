# Prim’s algorithm with distance matrix

Prim’s algorithm can also be applied on a distance matrix in order to find the minimum spanning tree, it uses similar technique as for a diagram.

Steps for using the Prim’s algorithm on a distance matrix :

1. Choose a starting vertex, and mark it. for eg : 1. Make sure to draw a line across the row of the selected vertex

2. Look at the corresponding column of the marked vertex and select the least weighted arc, put a dotted line across the row of the selected vertex. Mark the second arc.

3. Look at both columns of the selected arcs and search for the least arc

4. Cancel the arc and mark it.

5. Continue this process until no arcs remain

6. To calculate total weight, simply add the weights of the selected arcs, if the question says to draw a graph you can do the following by adding the vertices on the graph.