# Machine Learning Technique for Enhanced Situational Awareness With Fire Fighter Drones


# Table of Contents

## Chapter 1 — Introduction

1. [Overview](#11-overview)
2. [Problem Statement](#12-problem-statement)
3. [Objectives](#13-objectives)
4. [Significance](#14-significance)
5. [Scope](#15-scope)
6. [Motivation](#16-motivation)
7. [Contributions](#17-contributions)
8. [Organization](#18-organization)

## Chapter 2 — Background & Related Work

9. [Introduction](#21-introduction)
10. [Overview](#22-overview)
11. [Objectives](#23-objectives)
12. [System Description](#24-system-description)
13. [Core Concepts](#25-core-concepts)
14. [Related Work](#26-related-work)
15. [Technologies](#27-technologies)
16. [Implementation Scope](#28-implementation-scope)
17. [Challenges and Considerations](#29-challenges-and-considerations)

## Chapter 3 — Simulation Using ROS

18. [Overview](#31-overview)
19. [Objectives](#32-objectives)
20. [System Architecture](#33-system-architecture)
21. [Hardware Components](#34-hardware-components)
22. [AI / ML Pipeline](#35-ai-ml-pipeline)
23. [Simulation Setup](#36-simulation-setup)
24. [Communication FCU and Raspberry Pi](#37-communication-fcu-and-raspberry-pi)
25. [Distance Calculation](#38-distance-calculation)
26. [Technologies Used](#39-technologies-used)
27. [Results](#310-results)
28. [Challenges and Solutions](#311-challenges-and-solutions)
29. [Future Improvements](#312-future-improvements)

## Chapter 4 — Fire Drone System

30. [Overview](#41-overview)
31. [Objectives](#42-objectives)
32. [System Description](#43-system-description)
33. [Architecture & Design](#44-architecture--design)
34. [Bill of Materials](#45-bill-of-materials)
35. [Technologies Used](#46-technologies-used)
36. [Implementation Details](#47-implementation-details)
37. [Mathematical & Physical Models](#48-mathematical--physical-models)
38. [Results](#49-results)
39. [Challenges & Solutions](#410-challenges--solutions)
40. [Future Improvements](#411-future-improvements)

## Chapter 5 — Machine Learning Algorithms for Fire Detection

41. [Overview](#51-overview)
42. [Objectives](#52-objectives)
43. [System Description](#53-system-description)
44. [Data Pipeline](#54-data-pipeline)
45. [Model — YOLOv8](#55-model--yolov8)
46. [Development Environment](#56-development-environment)
47. [Technologies Used](#57-technologies-used)
48. [Implementation Details](#58-implementation-details)
49. [Distance Estimation](#59-distance-estimation)
50. [Results](#510-results)
51. [Challenges & Solutions](#511-challenges--solutions)
52. [Future Improvements](#512-future-improvements)

## Chapter 6 — FCU and Raspberry Pi Integration

53. [Overview](#61-overview)
54. [System Architecture](#62-system-architecture)
55. [Components](#63-components)
56. [UART Communication](#64-uart-communication)
57. [Software Stack](#65-software-stack)
58. [Telemetry and Control](#66-telemetry-and-control)
59. [Key MAVProxy Commands](#67-key-mavproxy-commands)
60. [Challenges & Solutions](#68-challenges--solutions)
61. [Results](#69-results)
62. [Future Improvements](#610-future-improvements)

## Chapter 7 — Conclusion & Future Work

63. [Conclusion](#71-conclusion)
64. [Limitations](#72-limitations)
65. [Future Work](#73-future-work)





## Project Description
This project presents the design and development of an intelligent firefighting drone system aimed at enhancing situational awareness during emergency response operations. The system integrates a custom-built UAV equipped with high-resolution and optional thermal cameras, combined with advanced machine learning techniques for real-time fire and smoke detection.

The drone utilizes computer vision algorithms based on YOLO models to analyze live video streams and identify fire-related patterns such as flames and smoke. Once a fire is detected, the system provides real-time alerts along with critical information including location, size, and spread estimation.

Additionally, the drone is integrated with GPS for autonomous navigation and a communication module to transmit data to a ground control station. The system is designed to support firefighters by improving response time, reducing risks, and enabling better decision-making in hazardous environments.

The project demonstrates the practical application of AI, embedded systems, and UAV technologies in modern firefighting scenarios, highlighting its potential for real-world deployment.


## Chapter 1 — Introduction

### 1.1 Overview

This chapter presents the motivation, problem definition, and key objectives of the autonomous firefighting drone system.

Wildfires have become increasingly frequent and severe, posing serious threats to lives, property, and ecosystems. While traditional firefighting methods remain effective, they often expose firefighters to hazardous conditions and are limited in operational reach.  
This project leverages artificial intelligence, robotics, and UAV technology to develop an autonomous fire detection and monitoring system.

---

### 1.2 Problem Statement

The primary challenge in firefighting is the rapid detection and suppression of fires, especially in inaccessible or high-risk environments.

Key problems addressed:

- Slow response time in detecting and reaching fire locations  
- High risk to human firefighters in hazardous conditions  
- Limited accessibility of traditional firefighting methods  
- Lack of real-time situational awareness during fire incidents  

---

### 1.3 Objectives

- Detect fire and smoke in real-time using YOLOv8  
- Enable autonomous navigation with obstacle avoidance  
- Transmit live video and telemetry to a ground control station  
- Estimate the distance to detected fire using the Triangle Similarity Method  
- Reduce human exposure to hazardous environments  

---

### 1.4 Significance

- Improve real-time situational awareness using aerial data  
- Enable faster detection and response through autonomous systems  
- Reduce direct human exposure to fire hazards  
- Provide a scalable and cost-effective emergency response solution  
- Support environmental protection through early fire detection  

---

### 1.5 Scope

The project includes the design, development, and testing of a prototype autonomous firefighting drone:

- **Fire Detection System:** YOLOv8-based real-time detection using an onboard camera, supported by additional sensing methods where applicable  
- **Navigation and Control:** GPS-based autonomous flight with LiDAR-based obstacle avoidance  
- **Fire Suppression (Optional):** Integration of a mechanism for dispensing water or fire-retardant materials  
- **Communication:** MAVLink/UART-based telemetry and data transmission  
- **Onboard Processing:** Raspberry Pi 4 for AI inference and data processing  
- **Simulation & Validation:** ROS Noetic and Gazebo 11 for simulation, with potential real-world testing and validation  

---

### 1.6 Motivation

- **Rising Fire Incidents:** Increasing global wildfire frequency demands advanced detection solutions  
- **Human Safety:** Autonomous drones reduce the need for human exposure in dangerous environments  
- **Technological Opportunity:** Advances in AI, robotics, and sensors enable intelligent UAV systems  
- **Environmental Impact:** Early detection helps reduce ecological damage  
- **Academic Alignment:** Practical application of AI and robotics in real-world disaster scenarios  

---

### 1.7 Contributions

1. Real-time fire detection system based on YOLOv8 with aerial deployment capability  
2. Autonomous navigation pipeline with LiDAR-based obstacle avoidance  
3. Distance estimation module using the Triangle Similarity Method  
4. Robust communication framework using MAVLink between the drone and ground station  
5. Fully validated simulation environment using ROS Noetic and Gazebo 11  
6. Potential integration of onboard fire suppression mechanisms for active response  
7. Open-source framework for future UAV-based emergency response systems  
8. Transferable methodology applicable to search and rescue and environmental monitoring  

---

### 1.8 Organization

The remainder of this document is organized as follows:

| Chapter | Title | Description |
|--------|------|-------------|
| 1 | Introduction | Overview, problem, objectives, scope, motivation, and contributions |
| 2 | Background & Related Work | Existing technologies, research, and challenges |
| 3 | Simulation Using ROS | Simulation setup, modeling, and obstacle avoidance |
| 4 | Fire Drone System | Hardware design and system architecture |
| 5 | Machine Learning Algorithms | YOLOv8 pipeline, dataset, training, and evaluation |
| 6 | FCU–Raspberry Pi Integration | UART communication and MAVLink implementation |
| 7 | Conclusion & Future Work | Summary, limitations, and future improvements |


## Chapter 2: Firefighter Drones Module – Background & Related Work

### 2.1 Introduction

This chapter presents the background and related work for the Firefighter Drones module, which is part of a larger integrated system. It outlines key concepts, technologies, and existing approaches relevant to drone-assisted firefighting.

---

### 2.2 Overview

Firefighter drones are unmanned aerial vehicles (UAVs) designed to support firefighting operations. They provide real-time data, enhance safety, and improve mission efficiency by operating in hazardous or inaccessible environments.

---

### 2.3 Objectives

- Improve firefighter safety  
- Provide real-time situational awareness  
- Enable access to hard-to-reach locations  
- Support search and rescue operations  
- Enhance fire monitoring and decision-making  

---

### 2.4 System Description

This module focuses on UAV-based support systems that integrate:

- **Robotics**: Autonomous or remote-controlled flight systems  
- **AI and Sensing**: Thermal imaging, object detection, and environmental analysis  
- **Communication Systems**: Real-time video streaming and telemetry transmission  

These drones function as preliminary responders by scanning fire scenes, detecting hazards, and assisting operational teams before direct human intervention.

---

### 2.5 Core Concepts

#### 2.5.1 Key Capabilities

- **Information Gathering**
  - Thermal cameras for detecting heat sources and victims  
  - Live video feeds for decision support  

- **Accessibility**
  - Ability to reach rooftops, high-rise structures, and confined areas  

- **Multi-Angle Observation**
  - Multiple viewpoints for comprehensive scene analysis  

- **Indoor Navigation**
  - Operation within buildings during structural fires  

---

#### 2.5.2 Technological Advancements

- Compact drone designs for rapid deployment  
- Increased payload capacity (sensors, cameras, extinguishers)  
- Autonomous navigation systems  
- Real-time data transmission  
- Extended battery performance  
- Obstacle detection and avoidance  

---

#### 2.5.3 Use Cases

| Scenario             | Application                                   |
|---------------------|-----------------------------------------------|
| Wildfires           | Fire spread monitoring and hotspot detection  |
| Urban Fires         | Real-time scene assessment                    |
| Search & Rescue     | Victim detection in complex environments      |
| Hazardous Materials | Gas detection and risk evaluation             |
| Inspection          | Structural and rooftop analysis               |
| Training            | Emergency simulation scenarios                |

---

### 2.6 Related Work

#### 2.6.1 Fire Suppression UAV Systems

- UAVs equipped with extinguisher payloads (e.g., CO₂ balls)  
- Integration of thermal sensors and GPS for fire detection and localization  
- Focus on reducing direct exposure of firefighters to hazards  

---

#### 2.6.2 First-Responder Drone Systems

- UAVs equipped with cameras and environmental sensors  
- Capabilities include human detection, scene reconstruction, and hazard analysis  
- Proposed enhancements include robotic manipulators and heat mapping  

---

#### 2.6.3 Drone Deployment Optimization

- Mathematical models for wildfire spread prediction and loss estimation  
- Use of metaheuristic algorithms (e.g., Water Wave Optimization)  
- Focus on improving scheduling efficiency and response times  

---

#### 2.6.4 Fire Extinguishing Quadcopter Designs

- Systems integrating flight controllers, servo mechanisms, and payload release units  
- Capable of targeted fire suppression through precision deployment  

---

#### 2.6.5 Operational Integration in Fire Services

- Use of drones across multiple emergency response phases  
- Integration of thermal and optical imaging with live data streaming  
- Highlights the need for regulatory compliance and standardized deployment  

---

### 2.7 Technologies

| Category           | Technologies                          |
|-------------------|--------------------------------------|
| UAV Platforms     | Quadcopters, Hexacopters             |
| Sensors           | Thermal cameras, gas sensors         |
| Navigation        | GPS, autonomous flight systems       |
| Control Systems   | Flight controllers, RC systems       |
| Communication     | Real-time video and telemetry        |
| Optimization      | Metaheuristic algorithms (e.g., WWO) |

---

### 2.8 Implementation Scope

This module includes:

- UAV-based aerial monitoring and inspection  
- Integration of:
  - Thermal imaging systems  
  - GPS modules  
  - Fire suppression payloads  

- Operational modes:
  - Autonomous navigation using predefined paths  
  - Manual control for precision tasks  

- Real-time data integration with command systems  
- Application of optimization techniques for efficient deployment  

---

### 2.9 Challenges and Considerations

| Challenge         | Description                          | Mitigation Approach                     |
|------------------|--------------------------------------|------------------------------------------|
| Regulations      | Airspace and legal restrictions      | Develop compliant operational frameworks |
| Interoperability | Integration across systems           | Standardize communication protocols      |
| Privacy          | Surveillance and data concerns       | Enforce strict data governance           |
| Limited Range    | Battery and endurance constraints    | Improve energy management systems        |

---

## Chapter 3: Simulation Using ROS

### Overview

This project designs and develops an autonomous fire detection and monitoring drone system. The drone uses computer vision to detect fires in real-time, transmits live data to a ground control station, and supports emergency response operations. The system is built on a custom hexacopter frame integrated with a Raspberry Pi, APM 2.8 flight controller, and YOLOv8-based fire detection model.

---

### Objectives

- Detect and locate fires autonomously using onboard cameras and computer vision
- Enable real-time data transmission to a ground control station
- Operate in environments too dangerous or inaccessible for human firefighters
- Reduce response time and minimize risk to human life
- Validate system performance through simulation and real-world testing

---

### System Architecture

The system is organized into four main layers:

```
┌─────────────────────────────────────┐
│          Ground Control Station      │
│     (Real-time data + alerts)        │
└────────────────┬────────────────────┘
                 │ Communication Module
┌────────────────▼────────────────────┐
│            Raspberry Pi 4           │
│   YOLOv8 Fire Detection | OpenCV    │
│   MAVLink | Distance Calculation    │
└────────────────┬────────────────────┘
                 │ UART Serial
┌────────────────▼────────────────────┐
│          APM 2.8 Flight Controller  │
│   GPS | IMU | Navigation | ESCs     │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│         Hardware Layer              │
│  Motors | ESCs | Props | Battery    │
└─────────────────────────────────────┘
```

---

### Hardware Components

| # | Component | Specification | Role |
|---|-----------|--------------|------|
| 1 | APM 2.8 | Arduino Mega-based IMU autopilot | Flight control, navigation |
| 2 | Raspberry Pi 4 | 4GB RAM | Onboard processing, AI inference |
| 3 | Camera | 5MP v1.3 | Live video feed for fire detection |
| 4 | ESC | 30A | Motor speed control |
| 5 | Brushless Motor | 2400KV | Propulsion |
| 6 | Propellers | 10x4.7 | Lift generation |
| 7 | Dual-side PCB | Prototype | Component integration |
| 8 | Buck Converter | 3A | Voltage regulation |
| 9 | LiPo Battery | 3S 5200mAh (11.1V) | Power source |
| 10 | Frame | 3D-printed F550 hexacopter | Structural base |
| 11 | Battery Connector | 3A | Power distribution |
| 12 | Wires | 2mm | Electrical connections |

---

### AI / ML Pipeline

#### Model: YOLOv8

- **Task:** Real-time fire and smoke detection
- **Architecture:** Single-stage CNN object detector
- **Training Platform:** Google Colab
- **Optimizer:** Adam
- **Dataset Source:** Google Images (Unsplash, iStock) + Roboflow datasets

#### Pipeline

```
Raw Images
    │
    ▼
Data Gathering (~3000 images)
    │
    ▼
Annotation (LabelImg / Roboflow)
    │
    ▼
Data Augmentation (Roboflow auto-annotation)
    │
    ▼
YOLOv8 Training (Google Colab + Ultralytics)
    │
    ▼
Model Validation & Testing
    │
    ▼
Inference on Live Drone Feed (Raspberry Pi)
```

#### Why YOLOv8?

- High accuracy on MS COCO and Roboflow 100 benchmarks
- Supports detection, segmentation, and classification
- Developer-friendly CLI and Python package
- Large active community and long-term support by Ultralytics

---

### Simulation Setup

#### Tools Used

| Tool | Purpose |
|------|---------|
| Gazebo 11 | 3D physics-based robot simulation |
| ROS Noetic | Robot operating system, sensor/topic communication |
| MAVROS | MAVLink to ROS bridge |
| MAVProxy | Ground control protocol |
| Darknet ROS | YOLO object detection in ROS |
| ArduPilot | Drone autopilot firmware |

#### ROS Packages

| Package | Function |
|---------|----------|
| `iq_sim` | Drone model + Gazebo world definition |
| `iq_gnc` | Flight control scripts (waypoints, obstacle avoidance) |
| `darknet_ros` | Real-time YOLO object detection |

#### Sensors Simulated

- **Camera** — 5MP, 640x480, 10Hz update rate
- **LiDAR (Hokuyo)** — 1024 samples, 30m range, used for obstacle avoidance

#### Key Setup Commands

```bash
# Launch Gazebo world
roslaunch iq_sim droneOnly.launch

# Run obstacle avoidance
rosrun iq_gnc obs_avoid.py

# Run square flight path
rosrun iq_gnc square.cpp

# Launch MAVROS
roslaunch iq_sim apm.launch

# Install CUDA for YOLO acceleration
sudo apt install nvidia-cuda-toolkit
```

---

### Communication: FCU and Raspberry Pi

#### Protocol: UART (Serial)

```
Raspberry Pi 4          APM 2.8
─────────────           ────────
TX  ──────────────────► RX
RX  ◄────────────────── TX
GND ─────────────────── GND
```

#### Setup Steps

1. Enable UART on Raspberry Pi via `sudo raspi-config`
2. Add `enable_uart=1` to `/boot/config.txt`
3. Identify serial port: `/dev/ttyAMA0`
4. Configure APM 2.8 serial port via Mission Planner
5. Use **Pymavlink** for MAVLink message handling

#### Key Libraries

| Library | Purpose |
|---------|---------|
| `pyserial` | Serial port communication |
| `pymavlink` | MAVLink message protocol |
| `OpenCV` | Computer vision processing |
| `MAVProxy` | Ground control station software |
| `matplotlib` | Data visualization |

---

### Distance Calculation

The system uses the **Triangle Similarity Method** to estimate distance from the camera to the detected fire.

```
d = (f x R) / r
```

| Variable | Value | Description |
|----------|-------|-------------|
| `f` | 3.60 mm | Focal length (Raspberry Pi Camera V1) |
| `r` | 10 cm | Marker radius in image plane (constant) |
| `R` | Calculated | Marker radius in object plane (live video) |
| `d` | Output | Distance from camera to fire |

---

### Technologies Used

| Category | Technology |
|----------|-----------|
| Detection Model | YOLOv8 (Ultralytics) |
| Vision Library | OpenCV |
| Programming Language | Python |
| Training IDE | Google Colab, Jupyter Notebook |
| Dataset Management | Roboflow |
| Simulation | Gazebo 11 + ROS Noetic |
| Communication | UART, MAVLink, MAVROS |
| Flight Controller | APM 2.8 (ArduPilot) |
| Companion Computer | Raspberry Pi 4 (4GB) |
| Hardware Platform | F550 Hexacopter |

---

### Results

- YOLOv8 model successfully detected fire in real-time video with **0.90 confidence score** on test images
- Obstacle avoidance validated in Gazebo simulation using LiDAR data
- Drone waypoint navigation tested using `square.cpp` flight script
- UART link established between Raspberry Pi 4 and APM 2.8 for telemetry and control
- Distance to fire estimated using triangle similarity method with fixed focal length

---

### Challenges and Solutions

| Challenge | Cause | Solution |
|-----------|-------|----------|
| Low detection accuracy | Insufficient training data | Used Roboflow datasets + automatic annotation |
| Slow YOLO inference | No GPU acceleration | Installed NVIDIA CUDA toolkit |
| Python version incompatibility | Library conflicts with ArduPilot | Used Python virtual environment v2.8.13 |
| APM 2.8 processing limitations | Outdated ATmega2560 MCU | Offloaded AI tasks to Raspberry Pi |
| Serial port conflict | Wrong port selected | Used `/dev/ttyAMA0` (primary UART only) |

---

### Future Improvements

- Extend battery life using solar power or fast-swap mechanisms
- Design weather-resistant drone body for smoke and high-wind environments
- Implement drone swarm coordination for large fire coverage
- Replace APM 2.8 with a modern ARM Cortex-based flight controller
- Integrate thermal camera for enhanced heat detection
- Add satellite or mesh network communication for remote area operations

---


## Chapter 4: Fire Drone System

### Overview

This chapter documents the full hardware architecture of the autonomous firefighting drone — a six-rotor UAV platform designed to detect, assess, and monitor fire events in environments hazardous to human responders. It covers component selection, system integration, power architecture, electrical design, and the physical rationale behind every hardware decision.

---

### Objectives

- Design and assemble a stable six-rotor UAV suitable for autonomous firefighting missions
- Select hardware based on payload capacity, power budget, weight, and compute requirements
- Integrate a companion computer with a dedicated flight controller over a serial communication bus
- Establish an isolated, regulated power delivery system for both high-current motor drive and sensitive digital electronics
- Provide a reproducible, documented hardware platform as the substrate for all software layers

---

### System Description

The drone is a hexacopter-class UAV combining three co-dependent subsystems:

| Subsystem | Function |
|---|---|
| Compute & Perception | Onboard AI inference, camera capture, sensor data processing |
| Flight Control | Low-level stabilization, motor mixing, GPS navigation, IMU fusion |
| Power & Actuation | Energy storage, voltage regulation, motor drive |

- **Robotics:** Sensors feed perception, perception informs control, control drives actuators — coordinated over a MAVLink communication bus
- **Physics:** Stable flight maintained by six independently controlled rotors generating differential thrust via PID control loop
- **Systems Engineering:** ArduPilot on ATmega2560 handles low-latency flight control; Python on Raspberry Pi 4 handles AI inference and mission logic via UART/MAVLink

---

### Architecture & Design

#### System Layers

```
┌──────────────────────────────────────────────────────┐
│                  MISSION / AI LAYER                   │
│   YOLOv8 Inference · Distance Estimation · OpenCV    │
│                  [ Raspberry Pi 4 ]                   │
├──────────────────────────────────────────────────────┤
│               COMMUNICATION LAYER                     │
│         MAVLink over UART · /dev/ttyAMA0             │
│              Pymavlink · MAVROS                       │
├──────────────────────────────────────────────────────┤
│              FLIGHT CONTROL LAYER                     │
│     PID Stabilization · IMU Fusion · GPS Nav         │
│              ArduPilot · [ APM 2.8 ]                 │
├──────────────────────────────────────────────────────┤
│                  HARDWARE LAYER                       │
│  6× ESC · 6× Motor · 6× Propeller · LiPo Battery   │
│  Buck Converter · PCB · F550 Hexacopter Frame        │
└──────────────────────────────────────────────────────┘
```

#### Power Architecture

```
[ 3S LiPo — 11.1V ]
        │
        ├──→ [ Power Distribution PCB ]──→ 6× ESC ──→ 6× Brushless Motor
        │
        └──→ [ Buck Converter (3A) ]──→ 5V regulated
                                              ├──→ Raspberry Pi 4
                                              └──→ Camera Module V1.3
```

#### Compute & Sensor Integration

```
[ 5MP Camera V1.3 ]──CSI──→ [ Raspberry Pi 4 ]
                                      │
                               UART / MAVLink
                                      │
                              [ APM 2.8 FCU ]
                                      │
                    ┌─────────────────┼─────────────────┐
                 [ GPS ]        [ ESC × 6 ]        [ Receiver ]
```

#### Motor Layout — Hexacopter X Configuration

```
        Motor 1 (CCW)
             │
Motor 6 ────┼──── Motor 2 (CW)
(CW)         │
Motor 5 ────┼──── Motor 3 (CCW)
(CCW)        │
        Motor 4 (CW)
```

> Alternating CW/CCW pairs cancel gyroscopic torque, providing natural yaw stability without constant FCU correction.

---

### Hardware Components

#### Bill of Materials

| # | Component | Specification | Qty | Role |
|---|---|---|---|---|
| 1 | APM 2.8 Flight Controller | ATmega2560, IMU, Barometer | 1 | Autopilot & stabilization |
| 2 | Raspberry Pi 4 | ARM Cortex-A72, 4GB LPDDR4 | 1 | Companion computer & AI inference |
| 3 | Camera Module | 5MP V1.3, f = 3.60 mm, CSI | 1 | Visual input for fire detection |
| 4 | ESC | 30A continuous, 3S compatible | 6 | Motor speed regulation |
| 5 | Brushless Motor | 2400KV, 3-phase outrunner | 6 | Thrust generation |
| 6 | Propellers | 10 × 4.7 in, CW + CCW pairs | 3 sets | Aerodynamic lift |
| 7 | Dual-Side PCB | Prototype FR4, dual-layer | 1 | Power distribution & interconnect |
| 8 | Buck Converter | Input: 7–35V · Output: 5V 3A | 1 | Regulated 5V supply |
| 9 | LiPo Battery | 3S, 11.1V, 5200mAh, XT60 | 1 | Primary energy source |
| 10 | Hexacopter Frame | F550, 3D-printed, 550mm span | 1 | Structural chassis |
| 11 | Battery Connector | 3A rated | 1 | Battery-to-PCB interface |
| 12 | Silicone Wire | 2mm gauge | — | Power transmission |

#### APM 2.8 — Flight Controller

Arduino Mega-based autopilot providing IMU fusion, PID stabilization, GPS navigation, and MAVLink telemetry. Handles all time-critical flight operations independently of the companion computer.

| Limitation | Impact |
|---|---|
| ATmega2560 processing power | Insufficient for onboard AI — mitigated by companion computer |
| Older IMU sensors | Lower update rate vs. modern FCUs |
| No onboard logging | Diagnostic data captured externally via MAVProxy |
| Higher power draw | Marginally reduces battery endurance |

#### Raspberry Pi 4 (4GB) — Companion Computer

Handles all high-level computation: YOLOv8 fire detection inference, OpenCV image processing, mission logic, and MAVLink command generation.

| Interface | Usage |
|---|---|
| CSI Ribbon | 5MP Camera V1.3 input |
| UART (`/dev/ttyAMA0`) | MAVLink link to APM 2.8 |
| USB / GPIO | Peripheral expansion |

#### 5MP Camera V1.3

- Fixed focal length: **f = 3.60 mm** — used in distance estimation formula
- Reliable under variable lighting including fire glow and partial smoke
- Native CSI integration with zero driver overhead

#### ESC 30A — Electronic Speed Controller

- One ESC per motor
- Converts PWM throttle signals from APM 2.8 into three-phase AC drive current
- 30A rating provides headroom above peak hover current (~4–5A per motor at 50% throttle)

#### Brushless Motor — 2400KV

| Metric | Value |
|---|---|
| KV Rating | 2400 RPM/V |
| No-load speed @ 11.1V | ~26,640 RPM |
| Advantage over brushed | Higher efficiency, lower heat, zero brush wear |

#### 3S LiPo — 5200mAh

| Parameter | Value |
|---|---|
| Nominal voltage | 11.1V (3 × 3.7V) |
| Capacity | 5200 mAh |
| Energy stored | ~57.7 Wh |
| Target hover endurance | 10–15 min under load |

#### F550 Frame — 3D Printed Hexacopter

- Lightweight construction preserves payload budget
- Arms positioned at equal 60° intervals for symmetric thrust
- Modular design accommodates future payload additions
- 3D printing enables rapid design iteration

#### Buck Converter (3A) & Dual-Side PCB

- Buck Converter steps 11.1V to stable 5V at >90% efficiency
- Prevents motor-generated EMI from reaching compute subsystem
- Dual-sided PCB consolidates all ESC power connections into compact vibration-resistant board

---

### Technologies Used

#### Hardware

| Category | Component |
|---|---|
| Flight Control | APM 2.8 (ArduPilot / ATmega2560) |
| Companion Compute | Raspberry Pi 4 — 4GB |
| Vision | 5MP Camera V1.3 (CSI) |
| Motor Drive | 6× ESC 30A |
| Actuation | 6× Brushless Motor 2400KV + 6× Propeller 10×4.7 |
| Power | 3S LiPo 5200mAh · Buck Converter 3A · Dual-Side PCB |
| Structure | 3D-Printed F550 Hexacopter Frame |

#### Firmware & Software

| Technology | Purpose |
|---|---|
| ArduPilot (ArduCopter) | Flight controller firmware |
| MAVLink Protocol | FCU ↔ Raspberry Pi communication |
| MAVProxy 1.5.2 | Ground control station interface |
| Mission Planner | APM 2.8 configuration & calibration |
| Pymavlink | Python MAVLink library |
| Raspberry Pi OS | Linux OS on companion computer |
| Python 3 | Application scripting |
| OpenCV | Image capture and preprocessing |
| Ultralytics YOLOv8 | Fire detection inference |
| ROS Noetic / MAVROS | Simulation & telemetry bridge |

---

### Implementation Details

#### Assembly Sequence

**Step 1 — Frame Assembly**

Six motor arms assembled on F550 frame at 60° intervals. All fasteners torqued consistently to prevent in-flight loosening from vibration.

**Step 2 — Motor & ESC Installation**

One 2400KV motor per arm. Each motor connected to a dedicated 30A ESC via three-phase bullet connectors. ESC signal leads routed to APM 2.8 output channels 1–6. CW/CCW orientation assigned per hexacopter X layout.

**Step 3 — PCB & Power Distribution**

Dual-sided PCB installed on center deck. All six ESC power leads soldered to PCB power bus. Buck Converter wired to bus input and 5V rail output.

**Step 4 — APM 2.8 Integration**

APM 2.8 mounted centrally on vibration-dampening foam standoffs. ESC signal wires, GPS, and UART Telem1 port connected.

**Step 5 — Raspberry Pi 4 Integration**

Raspberry Pi 4 mounted on upper deck. CSI ribbon routed to Camera V1.3. UART TX/RX cross-connected to APM 2.8 Telem1 at 57600 baud.

**Step 6 — Battery Placement**

3S LiPo secured to underside of center plate at calculated center of gravity to minimize roll/pitch trim offset.

#### APM 2.8 Configuration (Mission Planner)

```
Frame type       : Hexacopter X
Motor mapping    : ArduCopter 6-rotor X layout
Accelerometer    : Level calibration
Compass          : Rotating calibration procedure
ESC calibration  : All-at-once throttle range calibration
Serial (Telem1)  : MAVLink · 57600 baud · Raspberry Pi UART
```

#### UART Enablement on Raspberry Pi

```bash
# Enable hardware UART, disable serial console
sudo raspi-config
# → Interface Options → Serial → Disable login shell → Enable serial port hardware

# Add to /boot/config.txt
enable_uart=1

sudo reboot

# Serial port identifier for MAVLink
/dev/ttyAMA0
```

---

### Mathematical & Physical Models

#### Rotor Thrust & Torque

```
T = C_T · ρ · n² · D⁴

Q = C_Q · ρ · n² · D⁵
```

| Symbol | Description | Unit |
|---|---|---|
| `C_T` | Thrust coefficient (propeller geometry) | dimensionless |
| `C_Q` | Torque coefficient (propeller geometry) | dimensionless |
| `ρ` | Air density (~1.225 at sea level) | kg/m³ |
| `n` | Rotational speed | rev/s |
| `D` | Propeller diameter (10 in = 0.254 m) | m |

**Hover equilibrium condition:**

```
6 · T = m · g

T_required = (m · g) / 6
```

#### Power Budget & Hover Endurance

```
P_motor  ≈ 220–330 W   (6 motors at ~50% throttle, 11.1V)
P_compute ≈ 6–8 W       (Raspberry Pi 4 + camera under load)
P_FCU    ≈ 1 W          (APM 2.8)

I_total  ≈ 20–30 A      (system average at hover)

Endurance = Capacity / I_total
           = 5200 mAh / 25 A
           ≈ 0.208 h
           ≈ 12–13 minutes (theoretical hover)
```

#### Center of Gravity Constraint

```
x_CoG = Σ(mᵢ · xᵢ) / Σmᵢ = 0

y_CoG = Σ(mᵢ · yᵢ) / Σmᵢ = 0
```

#### Camera Distance Estimation (Triangle Similarity)

```
d = (f · R) / r
```

| Symbol | Description |
|---|---|
| `d` | Distance from camera to detected object |
| `f` | Camera focal length = **3.60 mm** (fixed, Camera V1.3) |
| `R` | Real-world radius of the detected marker/object |
| `r` | Pixel radius of the detected object in the image plane |

---

### Results

#### Flight System

| Outcome | Status |
|---|---|
| Stable autonomous hover with PID stabilization | ✅ Achieved |
| GPS-guided waypoint navigation via MAVLink | ✅ Achieved |
| ESC and motor calibration consistent across all 6 channels | ✅ Verified |
| Estimated hover endurance 10–15 min under payload | ✅ Within design target |

#### Integration & Communication

| Outcome | Status |
|---|---|
| Raspberry Pi ↔ APM 2.8 MAVLink link at 57600 baud | ✅ Operational |
| 5MP Camera streaming to YOLOv8 inference pipeline | ✅ Operational |
| 5V compute rail isolated from motor EMI | ✅ Verified |
| Power distribution PCB supplying all 6 ESCs without fault | ✅ Verified |

#### Validation

| Outcome | Status |
|---|---|
| Hardware validated in Gazebo/ROS simulation prior to build | ✅ Complete |
| Physical bench test: motor directions, ESC calibration, IMU sensors | ✅ Passed |
| YOLOv8 fire detection executed on Raspberry Pi 4 with live camera feed | ✅ Functional |
| MAVProxy: takeoff, land, waypoint, mode-change commands confirmed | ✅ Passed |

---

### Challenges & Solutions

| Challenge | Root Cause | Solution |
|---|---|---|
| APM 2.8 insufficient for AI workloads | ATmega2560 processing ceiling | Offloaded all ML inference to Raspberry Pi 4 |
| Motor EMI corrupting Raspberry Pi | Shared power rail, back-EMF noise | Dedicated regulated 5V rail via Buck Converter |
| IMU readings degraded by vibration | Motor/propeller vibration through frame | APM 2.8 mounted on vibration-dampening foam standoffs |
| CoG shift under full payload | Asymmetric component mass distribution | Battery centered on underside; electronics arranged symmetrically |
| UART voltage level concern | Raspberry Pi GPIO is 3.3V logic | APM 2.8 UART confirmed 5V-tolerant; baud rate verified |
| Limited flight endurance | High motor current vs. battery capacity | Selected 5200mAh 3S; minimized non-essential component mass |
| Frame stress at motor arm roots | 3D-printed PLA under dynamic motor load | Reprinted with higher infill; added reinforcing fasteners |
| ESC throttle range inconsistency | Factory ESC variation across 6 units | All-at-once ESC calibration via Mission Planner |

---

### Future Improvements

#### Hardware Generation 2

| Improvement | Rationale |
|---|---|
| Replace APM 2.8 with Pixhawk 4 or Cube Orange | ARM Cortex-M7; onboard logging; advanced sensor fusion |
| Add FLIR Lepton thermal camera | Fire detection through smoke and low-visibility conditions |
| Upgrade to 4S / 6S LiPo | Higher voltage reduces current draw, extends endurance |
| Custom PDB with integrated current sensing | Real-time power telemetry and better EMI suppression |

#### Platform Expansion

| Improvement | Rationale |
|---|---|
| Fire suppression payload | Transition from detection-only to active firefighting |
| LTE / 5G telemetry link | Enables BVLOS operations beyond RC control range |
| Replace Raspberry Pi 4 with NVIDIA Jetson Orin | GPU-accelerated inference, lower latency |
| Multi-drone swarm coordination | Wide-area awareness combined with targeted low-altitude response |


---


## Chapter 5: Machine Learning Algorithms for Fire Detection

### Overview

This chapter covers the complete machine learning pipeline developed to enable real-time fire detection from a drone-mounted camera. The system leverages **YOLOv8** to identify fire and smoke in live video feeds, and computes the **distance to the detected fire** using triangle similarity geometry. The pipeline spans dataset construction, annotation, augmentation, model training, evaluation, and on-device inference integration.

---

### Objectives

- Build a fire-specific image dataset through manual collection and automated annotation
- Train a high-accuracy, real-time fire detection model using YOLOv8
- Integrate the model with the drone's onboard Raspberry Pi camera
- Estimate the physical distance between the drone camera and the detected fire
- Validate the model's performance through testing and iterative refinement

---

### System Description

The detection subsystem operates as a perception layer within the broader drone architecture. The Raspberry Pi 4 captures live video, passes frames through the trained YOLOv8 model, and returns bounding boxes with class confidence scores.

```
Live Camera Feed
      │
      ▼
 Frame Capture (Raspberry Pi Camera V1.3 — 5MP)
      │
      ▼
 YOLOv8 Inference (Ultralytics)
      │
      ├── Bounding Box Coordinates
      ├── Class Label: "Fire" / "Smoke"
      └── Confidence Score
            │
            ▼
     Distance Estimation (Triangle Similarity)
            │
            ▼
     Alert / Telemetry Output → Ground Station
```

---

### Data Pipeline

#### Dataset Construction

**Collection**
- Approximately **3,000 fire images** gathered from open sources (Unsplash, iStock)
- Images cover varied environments: indoor fires, wildfires, candlelight, vehicle fires

**Annotation**
- Primary tool: **LabelImg** — manual bounding box drawing per image
- Annotation formats supported: **YOLO** and **PascalVOC**
- Each bounding box labeled with the class `fire`

**Data Augmentation & Expansion via Roboflow**

| Roboflow Capability | Purpose |
|---|---|
| Access to 500+ community datasets | Expanded training diversity |
| Automatic annotation | Eliminated manual labeling bottleneck |
| Built-in augmentation pipeline | Rotation, flip, zoom, shear, brightness shift |
| Export to YOLO format | Direct compatibility with YOLOv8 training |

Five to six Roboflow datasets were merged with the original collection, significantly improving model accuracy and generalization.

---

### Model — YOLOv8

#### Why YOLO over Other Pre-trained Models?

| Criterion | Pre-trained Models | YOLO |
|---|---|---|
| Purpose | Classification / Feature extraction | Real-time object detection |
| Speed | Varies | Optimized for high FPS |
| Bounding box output | Not always native | Core output |
| Deployment suitability | Requires adaptation | Production-ready |

YOLO frames detection as a **single regression problem** — one forward pass of the CNN simultaneously predicts bounding box coordinates and class probabilities across the entire image, making it inherently faster than region-proposal approaches such as Faster R-CNN.

#### YOLO Architecture

The backbone is a deep CNN with 24 convolutional layers:

- First 20 layers **pre-trained on ImageNet**
- Additional convolutional and fully connected layers appended for detection
- Final fully connected layer predicts:
  - Bounding box coordinates `(x, y, w, h)`
  - Objectness confidence score
  - Class probability vector
- Image divided into **S × S grid** — each cell predicts B bounding boxes and C class probabilities
- Final detections produced after Non-Maximum Suppression (NMS)

#### Why YOLOv8 Specifically?

- **Accuracy:** Benchmarked on Microsoft COCO and Roboflow 100 datasets
- **Developer Experience:** Clean CLI interface and well-structured Python API
- **Community Support:** Large active community for troubleshooting and guidance
- **Multi-task Capability:** Supports detection, segmentation, classification, and pose estimation
- **Long-term Support:** Ultralytics actively maintains and updates the model

---

### Development Environment

#### IDEs Used

| Tool | Role |
|---|---|
| **Jupyter Notebook** | Local prototyping, visualization, iterative testing |
| **Google Colab** | Cloud-based GPU training (Tesla T4 via CUDA) |

#### Programming Language

**Python** was the primary language due to:
- Native support for ML frameworks (PyTorch, OpenCV, Ultralytics)
- Object-oriented design enabling modular pipeline construction
- Cross-platform compatibility
- Extensive open-source ecosystem

#### Key Libraries

| Library | Purpose |
|---|---|
| **Ultralytics** | YOLOv8 model loading, training, inference |
| **OpenCV** | Frame capture, image preprocessing, bounding box rendering |
| **Roboflow SDK** | Dataset loading and management |
| **PyTorch** | Deep learning backend for YOLOv8 |
| **Matplotlib** | Training curve visualization |

---

### Technologies Used

| Technology | Details |
|---|---|
| YOLOv8 | Ultralytics YOLOv8 (latest at time of development) |
| Python | 3.x |
| Google Colab | GPU: Tesla T4, CUDA 11.x |
| Roboflow | Fire Detection dataset (multiple merged sources) |
| OpenCV | 4.x |
| LabelImg | Manual annotation |
| Raspberry Pi Camera | Module V1.3 — 5MP, focal length 3.60mm |

---

### Implementation Details

#### Step 1 — Environment Setup (Google Colab)

```python
pip install ultralytics
pip install roboflow
```

#### Step 2 — Dataset Loading from Roboflow

```python
from roboflow import Roboflow

rf = Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("your-workspace").project("fire-detection-vdmz")
dataset = project.version(1).download("yolov8")
```

#### Step 3 — Model Training

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Load pretrained YOLOv8 nano backbone

model.train(
    data=dataset.location + "/data.yaml",
    epochs=30,
    imgsz=640,
    batch=16,
    optimizer="Adam",
    patience=100,
    cache=True,
    save_period=1
)
```

- **Optimizer:** Adam
- **Epochs:** 30
- **Image Size:** 640 × 640
- **Pretrained Weights:** Transferred from ImageNet-trained backbone

#### Step 4 — Inference on Test Images

```python
from ultralytics import YOLO
from IPython.display import Image, display

model = YOLO("/runs/detect/train/weights/best.pt")
results = model.predict(source="test_image.jpg", imgsz=640)

for r in results:
    boxes = r.boxes     # Bounding box outputs
    masks = r.masks     # Segment masks (if applicable)
    probs = r.probs     # Classification probabilities
```

#### Step 5 — Batch Validation

```python
import glob
from IPython.display import Image, display

for image_path in glob.glob("/runs/detect/predict/*.jpg")[:1]:
    display(Image(filename=image_path, width=600))
    print("\n")
```

---

### Distance Estimation

The system estimates the **physical distance between the drone camera and the detected fire** using the **Triangle Similarity Method**.

#### Parameters

| Symbol | Description | Value |
|---|---|---|
| `f` | Focal length of camera | 3.60 mm (constant — Raspberry Pi Camera V1.3) |
| `r` | Radius of reference marker in image plane | 10 cm (constant) |
| `R` | Apparent size of object in image (computed per frame) | Varies |
| `d` | Distance from camera to fire object | Computed output |

#### Governing Equation

```
f / d = r / R
```

Solving for distance:

```
d = (f × R) / r
```

Where `R` is calculated dynamically from the bounding box dimensions during live video streaming. The focal length `f` and reference radius `r` remain constant for the Raspberry Pi Camera V1.3 module.

---

### Results

| Metric | Outcome |
|---|---|
| Fire detection confidence (candle image) | **0.90** (90%) |
| Fire detection confidence (vehicle fire) | **0.74** (74%) |
| Training convergence | Achieved within 30 epochs |
| Inference environment | Google Colab (Tesla T4 GPU) + Local Jupyter Notebook |
| Model output | Bounding box with class label "Fire" and confidence score |
| Validation | Visual inspection of prediction overlays on held-out images |

---

### Challenges & Solutions

| Problem | Cause | Solution |
|---|---|---|
| Low initial detection accuracy | Small and homogeneous dataset (~3,000 images) | Integrated Roboflow datasets (5–6 additional sources) |
| Manual annotation was time-consuming | Large volume of images requiring bounding boxes | Adopted Roboflow's automatic annotation feature |
| GPU memory constraints | YOLOv8 training on large batches | Used Google Colab with Tesla T4 GPU |
| Inference speed on Raspberry Pi | Limited onboard compute | Optimized model size; considered tiny-YOLO variant |
| Distance accuracy at varying angles | Camera projection assumptions | Applied Triangle Similarity with fixed reference constants |

---

### Future Improvements

- **Thermal Camera Integration:** Extend detection to infrared feeds for low-visibility and night-time scenarios
- **Multi-class Detection:** Add `smoke`, `person`, and `vehicle` classes to enrich situational awareness
- **Model Quantization:** Apply INT8 quantization or TensorRT optimization for faster Raspberry Pi inference
- **Tracking Module:** Integrate YOLOv8's built-in multi-object tracker to maintain fire identity across frames
- **Aerial Dataset Collection:** Build a drone-perspective fire dataset for improved aerial detection accuracy
- **Swarm Coordination:** Feed detection outputs into a multi-drone scheduling algorithm for optimized coverage

---



## Chapter 6: FCU and Raspberry Pi Integration

### Overview

This chapter documents the integration between the **APM 2.8 Flight Control Unit (FCU)** and a **Raspberry Pi 4** companion computer in the firefighting drone system.

The core design principle is a **clear functional separation**:

| Component | Responsibility |
|---|---|
| APM 2.8 FCU | Real-time flight control, stabilization, sensor fusion |
| Raspberry Pi 4 | AI inference, fire detection, high-level decision making |

Communication between them is established via **MAVLink over UART**.

---

### System Architecture

```
┌──────────────────────────────────────────────┐
│              Raspberry Pi 4                  │
│   ┌──────────────┐   ┌─────────────────┐    │
│   │  YOLOv8 Fire │   │  MAVLink Client │    │
│   │  Detection   │──▶│  (pymavlink)    │    │
│   └──────────────┘   └────────┬────────┘    │
└────────────────────────────── │ ────────────┘
                          UART  │  (TX/RX/GND)
┌──────────────────────────────────────────────┐
│              APM 2.8 FCU                     │
│   ┌──────────────┐   ┌─────────────────┐    │
│   │  Flight      │   │  MAVLink Server │    │
│   │  Controller  │◀──│  (ArduPilot)    │    │
│   └──────────────┘   └─────────────────┘    │
└──────────────────────────────────────────────┘
```

**Data Flow:**

```
Sensors → FCU → [MAVLink/UART] → Raspberry Pi → AI Processing → Commands → FCU → Motors
```

---

### Components

| Component | Specification | Role |
|---|---|---|
| Flight Controller | APM 2.8 (ATmega2560) | Low-level flight control |
| Companion Computer | Raspberry Pi 4 — 4GB | High-level processing and AI |
| Protocol | MAVLink over UART | Bidirectional communication |
| Interconnects | Jumper wires | Physical TX/RX/GND links |

#### Why APM 2.8 is a Limiting Factor

The APM 2.8 is functional but acknowledged as legacy hardware. This directly motivated the companion computer approach.

| Limitation | Impact on This Project |
|---|---|
| Weak ATmega2560 MCU | Cannot run AI models — offloaded entirely to Raspberry Pi |
| Low-accuracy IMU sensors | Compensated by GPS and software filtering |
| No onboard logging | Logging handled on Raspberry Pi side |
| High power consumption | Managed through buck converter and LiPo selection |

---

### UART Communication

#### Physical Wiring

| Raspberry Pi 4 | APM 2.8 |
|---|---|
| TX (GPIO 14) | RX |
| RX (GPIO 15) | TX |
| GND | GND |

> TX and RX must be cross-connected. A shared ground is mandatory for signal integrity.

#### Enabling UART on Raspberry Pi

```bash
# 1. Open configuration tool
sudo raspi-config
# Navigate to: Interface Options → Serial
# Disable: Login shell over serial
# Enable:  Serial port hardware

# 2. Edit boot config
sudo nano /boot/config.txt
# Add: enable_uart=1

# 3. Reboot
sudo reboot
```

The primary UART interface is exposed at `/dev/ttyAMA0`.

---

### Software Stack

| Library | Purpose |
|---|---|
| `pymavlink` | MAVLink message parsing and generation |
| `pyserial` | Low-level serial port access |
| `OpenCV` | Camera feed processing for fire detection |
| `MAVProxy` | Ground control station and command relay |
| `matplotlib` | Telemetry visualization |

#### Key Setup Commands

```bash
# Install MAVLink tools
sudo pip install pyserial pymavlink MAVProxy future

# Clone MAVLink library
git clone https://github.com/mavlink/mavlink.git --recursive
python3 -m pip install -r pymavlink/requirements.txt
```

> **Note on Python:** Use **Python 3.x** with a virtual environment (`venv`). Ensure library versions are compatible with the ArduPilot ecosystem before deployment.

---

### Telemetry and Control

#### Incoming Data (FCU to Raspberry Pi)

- GPS coordinates (latitude, longitude, altitude)
- Battery voltage and remaining capacity
- IMU data (roll, pitch, yaw rates)
- Current flight mode

#### Outgoing Commands (Raspberry Pi to FCU)

- Waypoint updates based on detected fire location
- Altitude and speed adjustments
- Mode switches: `GUIDED`, `AUTO`, `LAND`
- Return-to-home trigger

---

### Key MAVProxy Commands

| Command | Description |
|---|---|
| `arm throttle` | Arm motors |
| `takeoff <alt>` | Takeoff to altitude in meters |
| `mode GUIDED` | Enable autonomous guided mode |
| `land` | Initiate auto-land |
| `param fetch` | Sync parameters from FCU |

---

### Challenges & Solutions

| Problem | Cause | Solution |
|---|---|---|
| UART port conflict | Login shell occupying `/dev/ttyAMA0` | Disabled serial login via `raspi-config` |
| APM 2.8 cannot run AI | Limited MCU processing power | All inference offloaded to Raspberry Pi |
| MAVLink version mismatch | Library incompatibility | Pinned compatible library versions in virtual environment |
| Signal noise on UART | Long jumper wires without shielding | Kept wires short; verified shared GND |

---

### Results

- Stable bidirectional UART link established between Raspberry Pi 4 and APM 2.8
- Real-time MAVLink telemetry (GPS, altitude, battery) successfully streamed to companion computer
- High-level commands (waypoints, mode changes) relayed from Raspberry Pi to FCU reliably
- YOLOv8 fire detection pipeline running concurrently on Raspberry Pi without flight disruption

---

### Future Improvements

| Area | Proposed Enhancement |
|---|---|
| Flight Controller | Upgrade to Pixhawk 6C (ARM Cortex-M7, richer feature set) |
| Companion Computer | Upgrade to NVIDIA Jetson Nano for GPU-accelerated inference |
| Communication Link | Replace UART with higher-bandwidth CAN bus or Ethernet |
| Fault Tolerance | Implement watchdog and communication failsafe mechanisms |

---


## Chapter 7: Conclusion & Future Work

### Conclusion

The Fire Flight drone project demonstrates the potential of drone technology in wildfire management.

Key outcomes:

- Improved **safety** by reducing direct human exposure to fire zones
- Improved **efficiency** in fire detection and monitoring
- Cost-effective hardware design suitable for fire departments
- Cameras and sensors enable civilian detection in smoke-filled environments
- Fire Extinguisher Balls can reduce fire in targeted areas and create exit routes
- Gas sensors generate toxicity reports to help firefighters protect themselves

---

### Limitations

| Limitation | Description |
|---|---|
| Weather Conditions | High winds, heavy rain, or smoke can disrupt drone stability and control |
| Battery Life | Limited flight duration requires frequent battery changes or recharging |
| Operational Range | Drones cannot cover large wildfire areas without multiple units |
| Data Transmission | Remote or mountainous areas suffer poor connectivity and signal loss |

---

### Future Work

#### Extended Battery Life
- Develop more efficient battery technologies
- Explore alternative power sources such as solar power
- Implement rapid charging systems and battery swap mechanisms

#### Enhanced Weather Resistance
- Design drones capable of operating in high winds, rain, and smoke
- Implement advanced stabilization and navigation systems for adverse conditions

#### Increased Range and Coverage
- Develop long-range drones for larger area coverage
- Implement drone swarming technology to coordinate multiple UAVs simultaneously

#### Improved Communication
- Enhance communication systems for reliable data transmission in remote terrain
- Utilize satellite communication links or mesh networks for long-distance connectivity
