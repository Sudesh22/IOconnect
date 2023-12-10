# IOconnect
Final Year Project on IIoT (Industry 4.0), developed using STM32. The motive of this project is to develop a safe and secure IoT network, thereby ensuring data integrity between the communication of IoT devices. We also aim to eliminate the need IoT Gateways by utilizing the technical advancements of the modern microcontrollers.

## Problem Statement
Design and implement a comprehensive Industrial Internet of Things (IIoT) 4.0 solution for optimizing manufacturing processes and enhancing operational efficiency in a smart factory environment.

## Limitations of the Existing system
Many existing IoT systems lack robust security measures, relying on basic encryption and authentication methods. This inadequacy leaves them vulnerable to sophisticated attacks, including intrusion, data breaches, and device manipulation. IoT networks consist of a wide array of devices, each with unique specifications and communication protocols. Existing solutions often struggle to provide uniform security across this diverse ecosystem, leading to vulnerabilities in certain devices or communication channels, that are prone to vulnerabilities such as hacking. Also to keep up with the upcoming trend of Machine Learning and use its potential for Growth estimation and to increase the efficiency of existing systems.

## Working
It sends sensor data to Raspberry Pi based Server by Encrypting
with AES-256 encryption algorithm. The Verifies data integrity with SHA-256 generated hash.
Real-time monitoring on dashboard and prediction of comapny
growth with Machine Learning.

## Block Diagram
<p align=center>
  <img src="Resources/blockm.png">
  <p align=center>Block Diagram</p>
</p>

## Snaps of the Project
<p align=center>
  <img src="Resources/IOconnect.svg">
  <p align=center>IOconnect</p>
</p>

## MCUs Used
- STM32F446RE - Gathers the data from the sensors, encrypts data using AES-256 Encryption algorithm and sends it to the ESP8266 module .
- ESP8266 - Receives the encrypted data and sends it to the Raspberry Pi based Server.

## Sensors Used
- TBD

## Project Status
- [x] Find Encryption Algorithms (Found: AES-256)
- [x] Find Hashing Algorithms (Found: SHA-256)
- [x] Try out the Algorithms using Python
- [x] Combine the Algorithms with Backend
- [x] Find research papers
- [x] Make PPT 
- [x] Find out about Port Forwarding DNS Port
- [x] Research hosting server on Raspberry-PI
- [x] Make the Raspberry-PI server online
- [x] Decide Online Database
- [x] Conduct Tests on Database
- [x] Implement Encrypted Login
- [ ] Decide Sensors and the MCU
- [ ] Add ML/AI to the project