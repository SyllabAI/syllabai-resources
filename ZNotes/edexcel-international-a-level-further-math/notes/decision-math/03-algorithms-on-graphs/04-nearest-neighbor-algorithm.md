# Nearest Neighbor Algorithm

Nearest neighbor algorithm can be used to find a short path that connect all vertices, this algorithm only works using a distance matrix

Steps for the nearest neighbor algorithm:

1. Choose a starting vertex, and delete the corresponding row by putting a dotted line across the row

2. Choose the lowest weighted arc of the row, delete the row

3. Move to the previously selected column and select the least weighted arc

4. Follow the steps, until no arcs remain

5. Finally add the total weight and draw the path