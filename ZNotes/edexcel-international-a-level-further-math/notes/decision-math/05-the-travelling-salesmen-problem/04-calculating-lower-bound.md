# Using M-S-T to calculate lower bounds

A minimum spanning tree can be used to calculate a lower bound.

Steps to calculate initial lower bound : 

1. Remove the vertex given from the table of distance matrix

2. Find a minimum spanning tree with the remaining vertices

3. Calculate the weight of the residual minimum spanning tree ( weight of spanning tree with removed vertex)

4. Add the 2 least weights possible from the vertex initially removed to the weight calculated before.

Example : 

Vertex asked to remove was A where the 2 least arcs by weight were 12 and 10

Weight of residual minimum spanning tree is 34

34+12+10= 56

Lower bound = 56

When upper bound= lower bound, solution is optimal.