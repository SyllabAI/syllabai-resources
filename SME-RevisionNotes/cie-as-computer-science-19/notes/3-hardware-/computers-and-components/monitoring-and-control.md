---
note_id: "rn_VFWSj88hpxFJBtcw"
title: "Monitoring & control"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/3-hardware-/computers-and-components/monitoring-and-control
path: 3-hardware-/computers-and-components/monitoring-and-control
updated_at: "2026-01-05T11:45:11.735Z"
spec_point_ids: ["spcpt_NXQkJSSGwbx4bdCc", "spcpt_5M3GQTQ5zXtyXGFG", "spcpt_PTxQ9BkNctX3djVm"]
spec_point_codes: []
guided_study: false
---

# Monitoring & control

## Monitoring vs control

> **Spec point** — `spcpt_NXQkJSSGwbx4bdCc`

## Monitoring vs control

### Monitoring systems

- A monitoring system is used to **collect data continuously** through observation
- It works by **passively gathering data**
- It **does not interact with or change** the environment
- The system **does not take action** based on the data collected
- Designed for **high accuracy** using **precise sensors and measurements**
- Examples of monitoring systems include:

  - **Weather stations**
  - **Patient monitoring in hospitals**

#### Weather stations

- Collect data like **temperature, wind speed, humidity, and rainfall**
- Used by **meteorologists** to observe and predict weather patterns
- Data is collected **24/7** but the system does **not react or change anything**

#### Patient monitoring

- Tracks **heart rate, oxygen levels, and blood pressure** in real-time
- Alerts medical staff if readings go outside safe ranges
- The system itself just **records and displays data**, it doesn’t directly treat the patient

### Control systems

- A control system is used to **automatically manage or adjust** a process based on data collected from sensors
- It works by **monitoring input**, then **taking action** if certain conditions are met
- Unlike monitoring systems, control systems **do interact with the environment**
- They are designed to keep systems **stable, safe, or working efficiently** without human input
- Examples of control systems include:

  - **Central heating system**
  - **Automatic irrigation system**

#### Central heating system

- **Monitors room temperature** using a thermostat
- If the temperature drops below the set level, the **boiler is switched on**
- Once the target temperature is reached, the system **turns the heating off** automatically
- The system constantly checks and **adjusts** to maintain the desired temperature

#### Automatic irrigation system

- **Monitors soil moisture levels** in farmland or gardens
- If moisture drops too low, it **activates sprinklers** to water the plants
- Once the soil reaches the correct level, the system **turns off the water supply**
- Ensures plants are **watered efficiently** without wasting resources

> **Exam Hint**
> - **Actuators **are output devices in a control system that carry out actions based on data from sensors
> - Examples include motors, heaters, valves, and pumps

## Use of sensors

> **Spec point** — `spcpt_5M3GQTQ5zXtyXGFG`

## Use of sensors

### What are sensors?

- Sensors are **input devices**
- They **measure a physical property of their environment** such as light levels, temperature or movement
- Sensors can be used for both **monitoring and control systems**
- A process where **outputs are recycled and used as inputs**, creating a continuous cycle is called a** feedback loop**

| **Sensor type** | **What it measures** | **Typical use** |
|---|---|---|
| **Acoustic** | Sound levels | To detect changes in sound levels of industrial machinery<br><br>To monitor noise pollution<br><br>In security system to detect suspicious sounds |
| **Accelerometer** | Acceleration rate, tilt, vibration | Detecting sudden changes in vehicle movement and deploy safety features if needed<br><br>In mobile phones to detect orientation of the device |
| **Flow** | Rate of gas, liquid or powder flow | Detect changes in the flow through pipes in water system |
| **Gas** | Presence of a gas e.g. carbon monoxide | Detect levels of gas in confined spaces<br><br>Detect gas levels when fixing gas leaks |
| **Humidity** | Levels of water vapour | Monitor humidity in greenhouses |
| **Infra-red** | Detecting motion or a heat source | Security systems detecting intruders who break the beam<br><br>Measures heat radiation of objects - used by emergency services to detect people |
| **Level** | Liquid levels | Detects levels of petrol in a car tank<br><br>Detect levels of water in a water tank<br><br>Detect a drop in water levels due to a leak |
| **Light** | Light levels | Automatically switching on lights when it gets dark (street lights, headlights) |
| **Magnetic field** | Presence and strength | Anti-lock braking system<br><br>Monitoring rotating machinery such as turbines |
| **Moisture** | Presence and levels of moisture | Monitoring moisture in the soil<br><br>Monitoring dampness in buildings |
| **pH** | Acidity or alkaline | Monitoring soil to ensure optimum growing conditions<br><br>Monitor ph levels in chemical processes |
| **Pressure** | Gas, liquid or physical pressure | Monitoring tyre pressure<br><br>Monitoring pressure in pipes during the manufacturing process |
| **Proximity** | Distance | Monitoring the position of objects in robotics<br><br>Used in safety systems to prevent objects from colliding |
| **Temperature** | Temperature in Celsius, Fahrenheit or Kelvin | Used to maintain temperature in swimming pools<br><br>Used to control temperature in chemical processes |

## Feedback loops

> **Spec point** — `spcpt_PTxQ9BkNctX3djVm`

## Feedback loops

### What is a feedback loop?

- A feedback loop is when a control system uses its **output to influence its next input**
- Allows the system to **automatically adjust** and stay within set conditions
- Feedback allows the system to** check if it’s working as expected**
- The **output affects the next input**, helping the system make adjustments
- This means the system can **automatically respond to changes** in its environment
- Helps the system **stay within set limits or target values** (e.g. temperature, moisture)
- Makes the system **more accurate and efficient** without needing human control

#### Example: Central heating system

- The system uses a **thermostat** to monitor the **room temperature**
- If the room gets **too cold**, the system **turns the heating on**
- Once the room reaches the **set temperature**, the system **turns the heating off**
- This process uses **feedback**:

  - The **output** (room temperature) affects the **input** (whether heating is needed)
- Feedback ensures the system **automatically adjusts** to keep the room at the right temperature
- No need for manual control as the system **self-corrects** using feedback
