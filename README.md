# BlindEyes

This project was created at MakeHarvard 2018. It won first place for the design and practicality of the device. It was created to bring solutions to individuals who are blind or may have poor vision. Using lidars, ultrasonic sensors, haptic vibrating discs, Emic 2 Text to Speech Module,  microcontrollers(Arudino and Mbed) and the ARM Raspberry Pi, we developed a device that gives the user both object avoidance/detection information and object/scene recognition information.

## Hardware Components
Arduino Uno Board</br>
MBED (LPC 1768)</br>
Raspberry Pi 3</br>

#### Object Avoidance:
VL53L0X - Time of Flight Sensor (LIDAR)</br>
HC-SR04 - Ultrasonic Sensor

#### Haptic Feedback:
DRV2605 - Haptic Controller Breakout</br>
Vibrating Motor Discs 

#### Object Recognition and Audio
Raspberry Pi Camera</br>
Emic2 - Text to Speech Module</br>
VMA410 - Logic Level Converter - 3.3 to 5V



## Software Components
MBED (Head LIDAR/UltraSonic with Haptic Feedback) - C++ code </br>
Arduino (Modular LIDAR with Haptic Feedback, as shown on ankle) - C++ </br>
Google Cloud Vision - Python </br>
Serial Interface with Emic2 - Python </br>
Microsoft Azure Computer Vision (Experimental) - Python





