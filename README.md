# Machine Learning Technique for Enhanced Situational Awareness With Fire Fighter Drones

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
