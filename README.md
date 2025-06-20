# Senior Design Project - UGV with a Mobile Manipulator:
### Sponsored by Siemens
This repository contains the code for my group's senior design project: a UGV with a mobile manipulation. The code is written for the Arduino Due (microcontroller), the NVIDIA Jetson Orin Nano (microprocessor), and the client laptop.

<img src="https://github.com/josephs1/UGV-Robot/blob/main/Extras/Robot_photo.jpg?raw=true" width="30%" height="30%">

# Folder Contents:
## Main
The "Main" folder contains that code for connecting the client laptop to the NVIDIA Jetson Orin Nano through a web socket. The Jetson has a serial connection to an Arduino that will move the mechanical arm's servos and stepper motors along with the drivetrain's DC motors. An Xbox Controller is connected to the laptop for inputs to move the motors. Printed serial messages from both the Jetson and the laptop are outputted.

## ros_noetic_catkin_ws
This folder is a workspace for setting up and building a ROS 1 Noetic environment using Catkin. It currently has our robot arm's URDF package, the ROS MoveIt package for simulating our arm in Gazebo and ROS, and the "gazebo_ros_link_attacher" package for attaching blocks to our arm in Gazebo to show our arm "picking up" an object.

![ROS Arm Movement](https://github.com/josephs1/UGV-Robot/blob/main/Extras/ROS_arm_movement.gif)

*Figure 1: Testing Arm Movements in ROS with MoveIt.*

![ROS Hand Movement](https://github.com/josephs1/UGV-Robot/blob/main/Extras/ROS_hand_movement.gif)

*Figure 2: Testing Hand Movements in ROS with MoveIt.*

## Extras
The "Extras" folder contains old test code used in trial and errors for basic understanding and implementation of functions and libraries that are later used in the "Main" code. It also contains old ROS workspace trial and errors.

## Tests
The "Tests" folder contains code for testing purposes, such as scripts programming the Arduino, scripts for the laptop client, and scripts for the Jetson Orin Nano. The goal is to understand basic functionality of using new libraries, such as WebSocket, Pygame joystick controllers, Serial connections and commands, etc.

## ROS_Extras
Contains extra files that were used in editing other downloaded git repositories. Since saved files in those folders cannot be seen in this repository, they were put inside this folder.
