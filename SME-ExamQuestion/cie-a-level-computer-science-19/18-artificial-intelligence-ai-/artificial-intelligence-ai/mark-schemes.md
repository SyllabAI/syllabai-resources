# Mark Schemes — Artificial Intelligence (AI)
**18. Artificial Intelligence (AI)** · Cambridge (CIE) A-LEVEL computer-science (9618)


## Exam Questions (21 questions)


### Q1
| Start node | Destination node | Cost from start node (g) | Heuristic (h) | Total (f = g + h) |
|---|---|---|---|---|
| Dock | Dock | 0 | 13 | 13 |
| Dock | A | 6 | 9 | 15 |
| **Dock** | **B** | **4** | **10** | **14** |
| **Dock** | **C** | **8** | **5** | **13** |
| **C** | **Exit** | **8 + 8 = 16** | **0** | **16** |
| **C** | **D** | **8 + 3 = 11** | **5** | **16** |
| **B** | **D** | **4 + 5 = 9** | **5** | **14** |
| **D** | **Exit** | **4 + 5 + 5 = 14** | **0** | **14** |

| Final path | **Dock → B → D → Exit** |
|---|---|

From Dock: the row for B is g = 4, h = 10, f = 14 **[1]**

From Dock: the row for C is g = 8, h = 5, f = 13 **[1]**

C has the lowest total (13), so C is checked next, even though B has the lower cost from start node. The rows from C are Exit (f = 16) and D (f = 16). Dock is not given a row because it has already been checked **[1]**

B now has the lowest total (14). The route to D through B (g = 9, f = 14) is shorter than the route through C (g = 11), so D gets a new row. D is then checked, giving a new row for Exit (g = 14, f = 14) **[1]**

Exit now has the lowest total, so the search ends. Reading back from the last Exit row: Exit came from D, D (g = 9) came from B, and B came from Dock. The final path is Dock → B → D → Exit, taking 14 seconds **[1]**

**[5 marks]**

> **[mark-scheme]**
> **1 mark** for the row Dock, B, 4, 10, 14
> 
> **1 mark** for the row Dock, C, 8, 5, 13
> 
> **1 mark** for both rows from C: C, Exit, 16, 0, 16 and C, D, 11, 5, 16
> 
> **1 mark** for both the row B, D, 9, 5, 14 and the row D, Exit, 14, 0, 14
> 
> **1 mark** for the final path Dock → B → D → Exit
> 
> Accept rows from the same Start node in any order
> 
> Accept the cost from start node written as a sum, for example 4 + 5 = 9
> 
> Do not accept Dock → C → Exit or Dock → C → D → Exit as the final path: each takes 16 seconds

> **[exam-tip]**
> Always choose the node with the lowest total (f), not the lowest cost from start node (g). Students who check B first because its cost (4) is lowest get the order wrong. Checking C first is correct, even though C is not on the final path.
> 
> Do not stop when Exit first appears in the table. After checking C, Exit has a total of 16, but B has a lower total of 14. A cheaper route through B and D then gives Exit a second row with a total of 14. When a node appears twice, read the final path back from the row with the lower cost.

### Q2
| Start node | Destination node | Cost from start node (g) | Heuristic (h) | Total (f = g + h) |
|---|---|---|---|---|
| Home | Home | 0 | 7 | 7 |
| Home | P | 5 | 4 | 9 |
| Home | Q | 9 | 4 | 13 |
| Home | S | 6 | 2 | 8 |
| **S** | **Airport** | **6 + 4 = 10** | **0** | **10** |
| **S** | **Q** | **6 + 2 = 8** | **4** | **12** |

S has the lowest total (8) of the nodes in the table that have not been checked from, so the next two rows start from S. Home is not given a row because it has already been checked from.

S to Airport: g = 6 + 4 = 10, h = 0, f = 10 **[1]**

S to Q: g = 6 + 2 = 8, h = 4, f = 12. This route to Q is shorter than the route straight from Home (g = 9), so Q gets a new row **[1]**

The algorithm does not stop because Airport does not have the lowest total. P has a lower total (9) than Airport (10), so P must be checked first **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for the row S, Airport, 10, 0, 10
> 
> **1 mark** for the row S, Q, 8, 4, 12
> 
> **1 mark** for Airport does not have the lowest total // P has a lower total (9) than Airport (10) // P must be checked first
> 
> Accept the two rows in either order
> 
> Accept the cost from start node written as a sum, for example 6 + 4 = 10
> 
> Do not accept rows that start from P: P has the lowest cost from start node (5), but S has the lowest total (8)
> 
> Do not accept "a shorter route might exist" for the last mark unless it refers to the lower total of P

> **[exam-tip]**
> The most common error is choosing the node with the lowest cost from start node (g). The algorithm always chooses the lowest total (f = g + h). Here that is S with a total of 8, not P with a cost of 5.
> 
> Students also miss the row for Q. Q is already in the table, but the route through S (cost 8) is shorter than the route straight from Home (cost 9), so Q needs a new row. Give a node a new row only when its new cost from start node is lower than the one already in the table.

### Q3
| Start node | Destination node | Cost from start node (g) | Heuristic (h) | Total (f = g + h) |
|---|---|---|---|---|
| Gate | Gate | 0 | 9 | 9 |
| Gate | J | 3 | 9 | **12** |
| Gate | K | 5 | 5 | **10** |
| Gate | L | 2 | 10 | **12** |

J: 3 + 9 = 12, K: 5 + 5 = 10, L: 2 + 10 = 12 **[1]**

Gate has already been checked. Of the other nodes, K has the lowest total (10), so the next row starts from **K** **[1]**

**[2 marks]**

> **[mark-scheme]**
> **1 mark** for all three totals: J 12, K 10 and L 12
> 
> **1 mark** for K
> 
> Do not accept L: L has the lowest cost from start node (2), but K has the lowest total (10)
> 
> Do not accept Gate: the nodes joined to Gate have already been added to the table

> **[exam-tip]**
> The algorithm chooses the node with the lowest total (f), not the lowest cost from start node (g). Students who look only at the cost column choose L, because 2 is the smallest cost. Adding the heuristic can change which node has the lowest value.
> 
> Ignore the first row when you look for the lowest total. Gate has the smallest total of all (9), but its joined nodes are already in the table, so it is not chosen again.

### Q4
The character is the agent and the maze is the environment. The agent learns by performing actions, such as moving in one direction, and seeing the results of those actions. **[1]**

It learns by trial and error, using its own experiences. **[1]**

A good action, such as reaching the exit, receives positive feedback or a reward. A bad action, such as moving into a wall, receives negative feedback or a punishment. The program uses this feedback to improve its performance on later attempts. **[1]**

Supervised learning needs labelled data, with known inputs and their associated outputs. There is no data showing the correct moves, so supervised learning has nothing to learn from, whereas reinforcement learning can learn without labelled data or specific instructions. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Reinforcement learning (Max 3 from):**
> 
> - An agent (the character) learns to behave in an environment (the maze / the game)
> - ... by performing actions and seeing the results of the actions
> - It learns by trial and error using its own experiences
> - A good action receives positive feedback // a reward
> - A bad action receives negative feedback // a punishment
> - It uses the feedback to improve its performance at accomplishing similar tasks
> 
> **Supervised learning is not suitable (Max 2 from):**
> 
> - Supervised learning needs known inputs with associated outputs // labelled input data
> - ... there is no labelled data / no data showing the correct moves here, so it has no known outputs to learn from
> - Reinforcement learning learns without any labelled data // without specific instructions
> 
> **[4 marks]**
> 
> Accept "adjusts node weightings to achieve the correct outcome" as a reinforcement learning point
> 
> Award the second supervised learning point only when it is linked to the need for known outputs. Repeating "there is no data showing the correct moves" on its own is not enough, because the question already states it

> **[exam-tip]**
> Examiners report that answers specific to reinforcement learning score well, while generic statements about AI do not. Name the feedback: a reward for a good action and a punishment for a bad action.
> 
> Use the scenario. Say which part is the agent and which part is the environment, and give an example of a good action and a bad action in the maze. For the second half, the key idea is that supervised learning needs known outputs, and this game has none.

### Q5
Unsupervised learning only requires input data to be given, and the library has a very large amount of input data in its loan records. **[1]**

The loan records have no known outputs attached, so they are unlabelled data. Unsupervised learning is not trained on the right output, so it does not need known outputs to learn. **[1]**

Unsupervised learning discovers patterns on its own, so it can find patterns in the loans that were previously undetected by the staff. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for unsupervised learning only requires input data to be given (the loan records)
> 
> **1 mark** for it uses unlabelled input data // it is not trained on the right output (the loan records have no known outputs)
> 
> **1 mark** for it helps unknown patterns in data to be found // it discovers patterns on its own that were previously undetected (by the staff)
> 
> **Max 2 marks** if no point is linked to the library loan records
> 
> Do not accept "it uses the known outputs to make predictions". That describes supervised learning, and these records have no known outputs

> **[exam-tip]**
> Be careful not to describe supervised learning by mistake, for example by writing that the system is "trained on the correct answers". Unsupervised learning is the category that needs no correct answers at all, only input data.
> 
> Tie each point to the scenario. Saying "it finds patterns" earns more when you add that the patterns are ones the staff have not noticed, and that the loan records have no known outputs to learn from.

### Q6
| Description | Machine learning category |
|---|---|
| Learns from data in which each input is given together with its known output | **Supervised learning** |
| Learns by performing actions in an environment and receiving rewards or punishments | **Reinforcement learning** |
| Is given only input data and finds unknown patterns in it, without being trained on the right output | **Unsupervised learning** |
| Uses an artificial neural network with a large number of hidden layers | **Deep learning** |

**[2 marks]**

> **[mark-scheme]**
> **2 marks** for all four rows correct
> 
> **1 mark** for two rows correct
> 
> Each category is used once, so exactly three correct rows is not possible
> 
> Accept "supervised", "unsupervised", "reinforcement" and "deep" without the word "learning"

> **[exam-tip]**
> The two rows that are easiest to confuse are unsupervised learning and deep learning, because both can find patterns that people have not noticed. Use the clue that belongs to only one of them: deep learning is the category built on an artificial neural network with a large number of hidden layers.
> 
> Remember that deep learning counts as a machine learning category in its own right. If you are asked to state a category, any one of the four is accepted.

### Q7
An artificial neural network simulates the functioning of a biological brain, and it is a key component of machine learning. **[1]**

It has self-learning capabilities, so it produces better results as more data becomes available. This is why the system becomes more accurate each month. **[1]**

The network is organised into an input layer, hidden layers and an output layer, and weights are assigned to the connections between the nodes. **[1]**

Increasing the number of hidden layers gives the system more complex learning capabilities, so it can produce more accurate results. **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> - An artificial neural network simulates the functioning of a (biological / human) brain
> - Artificial neural networks are a key component of machine learning // allow the system to make intelligent decisions on its own
> - It has self-learning capabilities that produce better results as more data becomes available
> - It can solve problems that would be impossible or difficult for humans
> - It is layered (input, hidden and output layers) // it has many interconnected layers, some of which are hidden
> - Weights are assigned between nodes
> - Weights are adjusted through training to give a more accurate result
> - A larger number of hidden layers gives more complex learning capabilities // more accurate results
> - More layers progressively extract higher level features from the (raw) input
> 
> **[4 marks]**
> 
> **Max 3 marks** if no point is made about the effect of increasing the number of hidden layers
> 
> Do not accept "more hidden layers make the system faster". The credited effect of more hidden layers is more complex learning and more accurate results, not speed

> **[exam-tip]**
> A common mistake is to spend the whole answer describing, step by step, how the weights are corrected after an error. Only one point about adjusting weights is credited here. The question also asks how the network helps the system learn from more data, and what extra hidden layers do.
> 
> Make sure the second half of the question gets a point of its own. If you write "more layers means it is better", you do not score, because "better" is too vague. Say what improves: more complex learning, or more accurate results.

### Q8
Deep learning makes good use of unstructured data, such as these images. **[1]**

Deep learning outperforms other methods when the quantity of data is large, and the company has millions of images. **[1]**

Deep learning is effective at identifying hidden patterns, such as the features of a face, that would be too complex or too time consuming for humans to find. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - Deep learning makes good use of unstructured data (such as images)
> - Deep learning outperforms other methods when the data size is large
> - Deep learning can be trained using large quantities of unlabelled data
> - Deep learning is effective at identifying hidden patterns // patterns that humans might not be able to see // patterns that are too complex or time consuming for humans to find
> - Deep learning enables machines to process data with a nonlinear approach
> - Deep learning can give a more accurate outcome with higher numbers of hidden layers
> 
> **[3 marks]**
> 
> Do not accept a description of deep learning with no reason attached, for example "it uses an artificial neural network" on its own. That describes what deep learning is, not why it suits this system
> 
> Do not accept "it is more accurate" on its own, with no link to the number of hidden layers

> **[exam-tip]**
> Examiners report that the highest marks go to answers that are specific to deep learning, not generic statements that could describe any kind of AI. "It learns by itself" or "it is intelligent" is too general to earn a mark here.
> 
> Look back at the stem for the clues: a very large quantity of data, data in the form of images, and data that is not labelled. Each of these matches a reason examiners credit, because images are unstructured data. Accuracy is only credited when you link it to a higher number of hidden layers.

### Q9
An artificial neural network is modelled on the human **brain**.

The nodes in an artificial neural network are organised into an input layer, one or more **hidden** layers and an output layer.

**Weights** are assigned to the connections between the nodes.

Deep learning is a specialised form of **machine** learning.

**[2 marks]**

> **[mark-scheme]**
> **2 marks** for all four gaps correct
> 
> **1 mark** for two or three gaps correct
> 
> Accept "biological brain" for the first gap
> 
> Accept "weightings" for the third gap
> 
> Do not accept "input" or "output" for the second gap, because both of those layers are already named in the sentence

> **[exam-tip]**
> Mark schemes name the three layers of a network exactly: input, hidden and output. A description such as "the layers in the middle" is not the technical term, so learn the word hidden.
> 
> Do not treat deep learning as something separate from machine learning. Examiners credit it as a specialised form of machine learning, and they also accept it as one of the machine learning categories, alongside supervised, unsupervised and reinforcement learning.

### Q10
**Working**

Set the Depot to 0 and every shop to ∞ **[1]**

Visit Depot (0): A = 0 + 7 = 7, B = 0 + 12 = 12, C = 0 + 3 = 3

Visit C (3): E = 3 + 1 = 4, F = 3 + 4 = 7

Visit E (4): B = 4 + 5 = 9, which is less than 12, so B is updated. F = 4 + 2 = 6, which is less than 7, so F is updated **[1]**

Visit F (6): D = 6 + 12 = 18

Visit A (7): B through A = 7 + 11 = 18, which is more than 9, so B is not updated. D = 7 + 9 = 16, which is less than 18, so D is updated **[1]**

Visit B (9): D = 9 + 3 = 12, which is less than 16, so D is updated

Visit D (12): every node has now been visited

**Answers**

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| **7** | **9** | **3** | **12** | **4** | **6** |

**[2]**

**[5 marks]**

> **[mark-scheme]**
> **Working (Max 3)**
> 
> May be seen in a table or in the working lines
> 
> MP1 Initialisation: setting the Depot to 0
> 
> MP2 ... and the rest of the nodes to ∞
> 
> MP3 Evidence to show values at nodes being updated
> 
> MP4 Evidence to show visited node(s)
> 
> MP5 Evidence to show a correct calculation of at least one route
> 
> MP6 Evidence to show more than one route has been calculated for at least one node
> 
> **Correct answers (Max 2)**
> 
> **2 marks** for all six correct values
> 
> **1 mark** for four or five correct values
> 
> Accept infinity for ∞
> 
> Do not accept B = 12, D = 15, D = 16 or F = 7. Each is the time of a real route, but not the shortest one

> **[exam-tip]**
> The direct road is not always the shortest route. The road from the Depot to B takes 12 minutes, but going through C and E takes only 9. Keep checking until every node has been visited, because a value can change more than once: D here goes from ∞ to 18, then 16, then 12.
> 
> Three of the five marks are for working, so show it. Write the starting values (0 and ∞), show each addition, and make clear which nodes you have visited. A correct answer table with no working can score only 2 marks.

### Q11
B has the lowest distance (5) of the nodes not yet visited, so B is visited next **[1]**

Route to C through B: 5 + 2 = 7. This is less than 8, so C is updated to 7 **[1]**

Route to D through B: 5 + 6 = 11. This is more than 9, so D stays at 9 **[1]**

| Node | Shortest distance so far (km) | Visited |
|---|---|---|
| Start | 0 | Yes |
| A | 2 | Yes |
| B | 5 | **Yes** |
| C | **7** | No |
| D | **9** | No |
| E | ∞ | No |

**[3 marks]**

> **[mark-scheme]**
> **1 mark** for B shown as visited, with no other new node shown as visited
> 
> **1 mark** for C updated to 7
> 
> **1 mark** for D still 9 and E still ∞
> 
> Accept a tick, a cross or a crossed-out node to show visited
> 
> Accept infinity for ∞
> 
> Do not accept C visited next. C is the unvisited node nearest to A, but its distance so far (8) is not the lowest of the unvisited nodes
> 
> Do not accept D = 11. A new route only replaces the old value when it is shorter

> **[exam-tip]**
> The next node to visit is the unvisited node with the lowest distance in the whole table. It does not have to be joined to the node you visited last. Here A was visited last, but B is next because 5 is the lowest value left.
> 
> When you check a route through the node you are visiting, add its distance so far to the length of the road. Then compare with the value already in the table and keep the smaller one. Students often write the new value over the old one without comparing.

### Q12
Dijkstra's algorithm is used to find the shortest route from one town (node) to another town in the graph **[1]**

The shortest route is decided by the total of the distances along the roads **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - to find the shortest / optimal / most cost-effective route
> - between two nodes in a graph // from a start node to each of the other nodes
> - based on distance / cost / time (the values on the roads)
> 
> **[2 marks]**
> 
> Accept path for route
> 
> Do not award the first marking point for "finds a route" or "searches the graph" without the idea of shortest, optimal or lowest cost. Any search can find a route; Dijkstra's algorithm finds the best one.

> **[exam-tip]**
> Purpose means what the algorithm is for, not how it works. Many students use all their lines on the method (setting the start to 0, visiting nodes, updating values) and never write the one idea the question asks for: it finds the shortest route.
> 
> Always say what "shortest" is measured in. In this app it is distance, but in another question it could be time or cost.

### Q13
**System 1**

Each city is a node, and each flight is a connection between two nodes with the price of the flight as its value **[1]**

An algorithm such as A* or Dijkstra's algorithm analyses the graph to find the most cost-effective route between the two cities **[1]**

**System 2**

The artificial neural network can itself be represented as a graph, with nodes arranged in layers (input, hidden and output) and weights on the connections between the nodes **[1]**

The graph is used by a machine learning method, such as back propagation of errors, and the weights are adjusted through training to give more accurate predictions **[1]**

**[4 marks]**

> **[mark-scheme]**
> **Any four from:**
> 
> System 1 (max 2)
> 
> - each city is a node // each flight is a connection between two nodes // the graph shows the relationships between the cities
> - the price of each flight is the value on its connection
> - the problem is solved by finding a path in the graph between the two cities
> - the graph is analysed by an algorithm such as A* / Dijkstra's algorithm
> - ... to find the cheapest / most cost-effective / optimal route
> 
> System 2 (max 2)
> 
> - an artificial neural network can be represented using a graph
> - the nodes are arranged in layers // input, hidden and output layers
> - weights are assigned to the connections between nodes
> - the graph is used / analysed by algorithms used in machine learning ...
> - ... such as back propagation of errors / regression methods
> - the weights are adjusted through training to give a more accurate result
> 
> **[4 marks]**
> 
> Accept "vertex" for node, and "edge" / "arc" for connection
> 
> Do not accept, for System 2, a chart of past flight delays plotted against time, because that is a different meaning of the word "graph"

> **[exam-tip]**
> Most students answer System 1 well, because a map of cities looks like a graph. Many then write nothing about graphs for System 2 and are limited to 2 marks. An artificial neural network is a graph too: its nodes are joined by connections, and each connection carries a weight.
> 
> Watch the word "each" in the question. The marks are split between the two systems, so four points about route finding still only earn 2 marks.

### Q14
The network is given a handwritten number and produces an output. This output is compared with the correct outcome to find the errors. **[1]**

Information about the errors is transmitted back through the network, from the output layer through the hidden layers. **[1]**

The weights between the nodes are adjusted to reduce the errors, so the next result is more accurate. **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - the errors in the output are found // the output is compared with the correct / known output
> - information about the errors is transmitted / sent back through the network // through the hidden layers
> - the weights between the nodes are adjusted to reduce the errors // to give a more accurate result
> - this is repeated many times during training // the results become more accurate as more data is used
> 
> **[3 marks]**
> 
> Accept weightings for weights
> 
> Accept information about the errors being transmitted through the network without a direction being given
> 
> Credit the weights marking point once only, however many times weights are mentioned
> 
> Do not accept the input data being changed to reduce the errors. The data stays the same and the weights change
> 
> Do not accept a description of the structure of the network on its own, such as input, hidden and output layers, because it does not say what happens to the errors

> **[exam-tip]**
> Many students write down everything they know about neural networks, such as layers, nodes and deep learning, and score nothing. The question asks what happens to the errors. Build your answer around three steps: find the errors, send information about them back through the network, and adjust the weights.
> 
> A common wrong answer is that the network changes its input data. The data does not change. The weights between the nodes change. You do not need to show how much each weight changes.

### Q15
Each storage point is represented as a node, and each path is a connection between two nodes **[1]**

The time taken to travel along a path is stored as the value on that connection **[1]**

The graph can be analysed by an algorithm such as A* or Dijkstra's algorithm to find the route with the shortest total time between the start node and the destination node **[1]**

**[3 marks]**

> **[mark-scheme]**
> **Any three from:**
> 
> - each storage point is represented as a node
> - each path is a connection between two nodes // the graph shows the relationships between the storage points
> - the time for each path is the value on its connection
> - planning a route is solved as finding a path in the graph (from the start node to the destination node)
> - the graph can be analysed by an algorithm ...
> - ... such as A* / Dijkstra's algorithm
> - ... to find the optimal / shortest / quickest route
> 
> **[3 marks]**
> 
> Accept "vertex" for node, and "edge" / "arc" for connection
> 
> Do not accept distance as the value stored on a connection, because the values in this graph are travel times

> **[exam-tip]**
> This question does not ask you to carry out a search. Students who write out the steps of Dijkstra's algorithm, such as setting the start node to 0, spend a long time and still miss the marks for saying what the graph represents. Link every point to the warehouse: what is a node, what is a connection, and what the value on a connection means.
> 
> The values on a graph do not have to be distances. Here they are times, so the best route is the quickest one, which is not always the physically shortest one.

### Q16
Back propagation of errors **[1]**

**[1 mark]**

> **[mark-scheme]**
> **1 mark** for back propagation (of errors)
> 
> Accept backpropagation or back-propagation
> 
> Do not accept regression, which is a different method named separately in the syllabus
> 
> Do not accept deep learning, reinforcement learning, supervised learning or unsupervised learning, which are categories of machine learning and not this method

> **[exam-tip]**
> The syllabus names two methods side by side, back propagation of errors and regression, so students often swap them. Link the word "back" to the errors: information about the errors travels back through the network.
> 
> Some students write reinforcement learning because it also helps a system improve. Reinforcement learning is a category of machine learning in which an agent learns from rewards and punishments. Back propagation of errors is a method that sends information about errors through a neural network so that its weights can be adjusted.

### Q17
A graph is made up of nodes **[1]**

The nodes are joined by connections that show the relationships between the nodes **[1]**

**[2 marks]**

> **[mark-scheme]**
> **Any two from:**
> 
> - a graph is a set of nodes
> - nodes are joined / connected to other nodes // the connections show the relationships between nodes
> - a connection between two nodes can have a value, such as a distance / cost / time
> 
> **[2 marks]**
> 
> Accept "vertices" for nodes, and "edges" / "arcs" / "lines" for connections
> 
> Do not accept a description of a chart that plots data against x and y axes, such as a line graph or a bar chart, because that is a different meaning of the word "graph"

> **[exam-tip]**
> In AI, a graph is not a chart with axes. An answer about axes, plotted points or a line of best fit gains no marks. Picture a map of towns joined by roads instead: each town is a node and each road is a connection between two nodes.
> 
> Two marks need two different points. "A graph has nodes" earns one mark. For the second mark, say what joins the nodes, or what the value on a connection can represent.

### Q18
> **[mark-scheme]**
> **One **mark per mark point (**Max 3**)
> 
> MP1 Reinforcement learning is a machine learning technique based on feedback / rewards / punishment.
> 
> MP2 … in which an agent learns to behave in an environment by performing the actions and seeing the results of the actions.
> 
> MP3 … for each good action, the agent gets positive feedback / reward and each bad action receives negative feedback / punishment.
> 
> MP4 The agent learns automatically using feedback without any labelled data / specific instructions.
> 
> MP5 Adjust node weightings to achieve the correct outcome. // Using feedback to improve its performance at accomplishing similar tasks.

### Q19
> **[mark-scheme]**
> **One **mark per mark point (**Max 3**)
> 
> MP1 Deep learning learns by finding hidden patterns that are **undetectable to humans**.
> 
> MP2 It structures algorithms in layers: **input **layer, **hidden **layers and **output **layer.
> 
> MP3 … to create an artificial neural network to learn and make intelligent decisions on its own.
> 
> MP4 It is trained using large quantities of unlabelled data.
> 
> MP5 Deep learning requires/uses a **large number of** hidden layers.
> 
> MP6 … the larger the number of layers, the higher the level of success.

### Q20
> **[mark-scheme]**
> **One** mark per mark point **(Max 4) **
> 
> MP1 An artificial neural network is the component of artificial intelligence that is meant to simulate the functioning of a biological brain.
> 
> MP2 Artificial neural networks are a key component of machine learning.
> 
> MP3 They can solve problems that would prove impossible or difficult for humans // Artificial neural networks have self-learning capabilities that enable them to produce better results as more data becomes available
> 
> MP4 Artificial neural networks can be layered (input, hidden and output layers) // Artificial neural networks have many interconnected layers, some / many of which are hidden
> 
> MP5 Weights are assigned between nodes
> 
> MP6 Weights are adjusted through training to give a more accurate result
> 
> MP7 More complex learning capabilities / more accurate results are available with larger numbers of hidden layers

### Q21
> **[mark-scheme]**
> **One** mark per mark point - working **(Max 3) **
> May be seen on diagram or in working section
> 
> - MP1    Initialisation – setting Start to 0
> - MP2    …and the rest of the towns to
> - MP3    Evidence to show values at nodes being updated
> - MP4    Evidence to show ‘visited node(s)’
> - MP5    Evidence to show a correct calculation of at least one route
> - MP6    Evidence to show more than one route has been calculated for at least one town
> 
> Correct Answers **(Max 2)** 
> **Two **marks for all six correct values 
> **One** mark for four or five correct values.
> 
> | **A** | **B** | **C** | **D** | **E** | **F** |
> |---|---|---|---|---|---|
> | 8 | 12 | 19 | 14 | 16 | 10 |
