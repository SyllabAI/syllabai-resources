# Dijkstra’s Algorithm

Dijkstra’s algorithm can be used to find the shortest path between any 2 points on a diagram.

Steps for using Dijkstra’s algorithm:

![](../../../assets/e68ae68c2e11-dca3f33344fb9bb8d4b5de84.webp)

To solve the Djikstra’s algorithm problem, the following table will be given in the exam to carry out the given steps

The top left most box is used to write the vertex letter

The top middle box is used to write the the number of the arc used

The right most box is used to write weight of the arc at that arc

Finally the bottom row is to be used for calculation reasons

1. Start at source vertex, below labelling it 0 in the right most box, and 1 in the middle box

2. Look at all the vertices connected to the source vertex, select the least arc

3. Move to the selected vertex, labelling it 2 in the middle value since this is the second arc selected and the value of weight/distance moved to reach the vertex

4. Check the vertices connecting both the selected arcs, and check which arc is of the least weight amongst BOTH THE ARCS

5. Utilize the bottom row to use it as working space, to write the arc weights

6. Selecting the next arc label it the corresponding arc number and arc weight at the given vertex

7. Repeat the above steps until final destination has reached.