## Operations Planning

Major operation decisions often involve major projects, such as relocation, expansion, and changes in operation methods.

### **Need for Planning Operations:**

* Ensures efficient use of resources and minimizes waste.

* Reduces time taken to complete projects.

* Helps manage costs by avoiding idle resources and unnecessary expenses.

### Examples of Business Projects:

* Setting up a new IT system.

* Relocating company operations.

* Installing new machinery.

* Expanding into international markets.

* Constructing new production facilities.

### **Resource Management in Operations Planning:**

* **Labor:** Workers should only be employed when needed to avoid unnecessary wage costs.

* **Materials:** Just-in-time (JIT) delivery prevents excess inventory storage costs and reduces risks like theft.

* **Machinery & Equipment:** Specialist tools should be rented only for the required duration to manage costs effectively.

* **Time Management:** Efficient scheduling ensures minimal downtime and maximizes productivity.

### **Importance of Efficient Resource Use:**

* Reduces costs and maximizes profitability.

* Prevents idle assets from increasing operational expenses.

* Ensures smooth workflow and timely project completion.

* Enhances cash flow management by avoiding unnecessary expenditures.

---

### **Critical Path Analysis (CPA)**

A planning technique that identifies all tasks in a project, puts them in the correct sequence and allows for the identification of the critical path.

* **Critical Path:** The sequence of activities that must be completed on time for the whole project to be completed by the agreed date.

* **Network Diagram:** The diagram used in critical path analysis that shows the logical sequence of activities and the logical dependencies between them, so the critical path can be identified.

### Key Aspects in CPA:

* **Identify Project Objective:** Define the goal, e.g., "Build a factory in six weeks."

* **Sequence Tasks & Draw Network Diagram:** Arrange activities logically.

* **Estimate Durations:** Assign time estimates to each task.

* **Identify the Critical Path:** Determine tasks that must be completed on time to meet the shortest project duration.

* **Use the Network as a Control Tool:** Monitor and adjust as needed.

### **Network Diagrams & Notation:**

* Arrows represent activities (tasks).

* Nodes (circles) indicate the completion of activities.

* Activity durations determine the project's timeline.

**Example:** **Building a House (3 Weeks Project)**

* **Critical Path Activities:** A, C, E, F, H.

* **Critical Path:** If these activities are delayed, the entire project is delayed.

* **Float Time:** Some tasks (e.g., ordering the new machine) can have delays without affecting the project timeline.

![](../../../assets/fc1e12b0f17f-allimages112a8c25972d20ab10e6257d.06)

### Benefits of CPA:

* Identifies the shortest completion time for a project.

* Helps allocate resources efficiently.

* Highlights critical activities requiring close monitoring.

* Provides flexibility through float time for non-critical activities.

### **How Critical Path Analysis is Determined:**

* **List all Activities:** Break down the project into key tasks (e.g., digging foundations, building walls, tiling the roof).

* **Establish Task Dependencies:** Identify which tasks must be completed before others can begin (e.g., walls must be built before the roof is tiled).

* **Draw the Network Diagram:** Represent activities with arrows and use numbered nodes to indicate task completion.

* **Assign Durations:** Estimate the time required for each activity.

* **Identify the Longest Path:** The critical path is the sequence of tasks that determines the shortest possible project completion time.

* **Calculate Float Time:** Tasks not on the critical path may have float time, allowing flexibility in scheduling without delaying the overall project.

### Order of Tasks:

#|
||

Activities

|

Preceding Activities

||
||

A

|

N/A

||
||

B

|

N/A

||
||

C

|

A

||
||

D

|

B & C

||
||

E

|

A

||
||

F

|

E

||
||

G

|

F & D

||
||

H

|

B & C

||
||

I

|

G & H

||
||

J

|

I

||
|#

* **Earliest Start Time:** An activity cannot begin before this time.

* **Latest Finish Time:** An activity cannot finish later than this time without delaying a project.

### Duration Time of The Tasks:

#|
||

Activities

|

Duration

||
||

A

|

8

||
||

B

|

6

||
||

C

|

12

||
||

D

|

6

||
||

E

|

14

||
||

F

|

10

||
||

G

|

3

||
||

H

|

14

||
||

I

|

3

||
||

J

|

4

||
|#

### **Main Stages of The Project:**

![](../../../assets/a340bbc22fd9-allimages50a385f11044edde0348aa39.06)

### **Inclusion of Activities & Durations of The Project:**

![](../../../assets/d98f706d1c65-allimagesd6efaff16fe180e590838f27.06)

### Key Aspects of Critical Path Analysis (CPA)

**Calculating the Earliest Start Time (EST):**

* The EST is the earliest time an activity can begin, considering the completion of preceding tasks.

* Example:

  * Activity E cannot start before day 8 because Activity A must be completed first.

  * Activity D cannot start before day 20 as Activities A and C must be completed first.

**Calculating the Latest Finish Time (LFT):**

* The LFT is the latest an activity can finish without delaying the entire project.

* Example:

  * Activity J (final activity) must finish by day 42.

  * The LFT for Activity I is day 38 (42 minus the duration of J).

  * If multiple paths lead to a node, the lowest LFT is chosen to ensure minimal project delay.

**Calculating Float Time for Non-Critical Activities:**

* Float time represents the spare time available for activities not on the critical path.

### **Types of Float:**

* **Total Float:** The maximum delay an activity can have without delaying the entire project.

* **Free Float:** The delay allowed without affecting the next task in the sequence.

By carefully calculating EST, LFT, and float times, project managers can optimize schedules, allocate resources efficiently, and prevent bottlenecks/slowdown of the production.

### **For the example above:**

**The critical path ensures that the house is completed in 42 days. Delays in any critical activity will extend the project duration.**

### Key Features of Float Time and Critical Path:

#|
||

Activity

|

Total Float

|

Free Float

||
||

B

|

15

|

14

||
||

C

|

1

|

0

||
||

D

|

6

|

6

||
||

H

|

1

|

1

||
|#

**Above is an example we will be using for the calculation.**

**Total Float:**

* **Formula:** LFT - Duration - EST

* Example (Activity D):

  * LFT: 32

  * Duration: 6

  * EST: 20

* **Total Float Calculation:** 32 - 6 - 20 = 6 days

* **Meaning:** Activity D can be delayed by up to 6 days without affecting the project completion time.

Free Float:

* **Formula:** EST (next activity) - Duration - EST (this activity)

* Example (Activity B):

  * EST of next activity (H or D): 20

  * Duration of B: 6

  * EST at the start of B: 0

* **Free Float Calculation:** 20 - 6 - 0 = 14 days

* Meaning: Activity B can be delayed by 14 days without delaying the next activities.

**Identifying the Critical Path:**

* The critical path consists of activities with no spare time (where EST = LFT).

* Example (Node 3):

  * EST of F = 22, LFT of E = 22 → No delay possible.

  * Therefore, Activity F must start on time or the project will be delayed.

  * Critical Path: A → E → F → G → I → J

* Total Project Duration: 42 days

### Importance of Float Times

* Total Float helps in resource allocation, allowing managers to adjust schedules without project delays.

* Free Float ensures that delays in one task don’t affect subsequent tasks.

* Understanding float times prevents bottlenecks and allows for better contingency planning.

### **Dummy Activities:**

A dummy activity is represented by a dotted line in a network diagram. It does not consume time or resources but shows logical dependencies between activities.

**Key Features:**

* It prevents the creation of illogical paths in network diagrams.

* It ensures accurate representation of dependencies between activities.

* It represents relationships, not actual tasks.

* It does not affect the project timeline or resources.

**Example:**

* Activities A and B start the project with no preceding activities.

* Activity C depends only on A.

* Activity D depends on both A and B.

**Incorrect Network:**

Below is an example, it incorrectly shows both C and D depending on A and B.

![](../../../assets/a72ae22b663f-allimages3f665b1c879543d32bd5ae26.18)

**Correct Network:**

* A dummy activity is used to indicate that:

* C starts after A is finished.

* D starts after both A and B are finished.

* The dotted line (dummy activity) links A to D to show this dependency.

![](../../../assets/65db44214d3e-allimages07ae4728668d5aaf58cff0a4.18)

### **Benefits of Critical Path Analysis (CPA):**

* **Accurate Project Duration:**

  * Helps calculate total project duration, allowing businesses to provide accurate delivery dates to customers.

  * Determines whether deadlines requested by customers can be met.

* **Efficient Resource Ordering:**

  * Early Start Times (EST) allow operations managers to order special equipment or materials at the right time.

  * Supports Just-In-Time (JIT) strategies and helps manage cash flow and working capital.

* **Effective Control Tool:**

  * Latest Finish Times (LFT) help monitor whether the project is on schedule by comparing actual completion times with network LFT.

* **Critical Path Awareness:**

  * Identifies activities with no float time where delays will impact the entire project.

  * Enables managers to speed up other activities to compensate for delays in critical tasks.

* **Resource Optimization:**

  * Resources from non-critical activities with float time can be allocated to critical ones to recover lost time.

  * Example: Delays in Activity E can be offset by reallocating resources from Activities D or H, which have spare time.

* **Supports Computer Applications:**

  * Logical and sequential structure of network diagrams is suitable for computer-based applications, enhancing efficiency and accuracy.

* **Improves Planning:**

  * Forces managers to carefully sequence activities and plan the project systematically.

* **Simultaneous Engineering:**

  * Highlights tasks that can be performed simultaneously during new product development.

  * Helps reduce the total time required for product development, benefiting fast-changing consumer markets.

### **Strengths, Drawbacks, and Requirements of CPA:**

#|
||

Strength

|

Drawbacks

|

Requirements

||
||

CPA aids in planning and controlling complex projects by visually identifying the sequence and duration of tasks.

|

CPA is less reliable for new projects with no prior data, as activity durations are often based on guesswork.

|

Successful implementation relies on skilled and experienced managers to use CPA effectively.

||
||

It provides a clear framework for identifying critical activities and float times.

|

Creating complex networks and calculating durations can take significant time and skilled labor.

|

Workers' commitment to the plan is critical. Involving employees in estimating activity durations can increase their buy-in and motivation.

||
||

It can help in optimizing resource allocation to improve efficiency and reduce delays.

|

N/A

|

Managers must identify cost-effective options to make up for delays in critical activities.

||
||

Useful for monitoring project progress and making adjustments when delays occur.

|

N/A

|

The cost and effort must be justified by the efficiency gains CPA provides.

||
||

N/A

|

N/A

|

A well-made CPA diagram cannot ensure project success without strong execution and management.

||
|#

