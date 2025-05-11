# Building for Ubuntu 20.04 Linux:
Start in this directory: .../UGV-Robot/ros_noetic_catkin_ws/src/

## Installing ROS Noetic:
- <pre><code>sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'</code></pre>
- <pre><code>sudo apt install curl</code></pre>
- <pre><code>curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -</code></pre>
- <pre><code>sudo apt update</code></pre>
- <pre><code>sudo apt install ros-noetic-desktop-full</code></pre>

## Catkin Setup:
- <pre><code>sudo apt install python3-catkin-tools</code></pre>
- <pre><code>git clone https://github.com/ros/catkin.git</code></pre>
- <pre><code>export CMAKE_PREFIX_PATH="/opt/ros/noetic:$CMAKE_PREFIX_PATH"</code></pre>
- <pre><code>catkin clean</code></pre>
- <pre><code>catkin build</code></pre>

## Installing MoveIt:
- <pre><code>sudo apt install ros-noetic-ros-controllers</code></pre>
- <pre><code>sudo apt install ros-noetic-moveit</code></pre>
- <pre><code>sudo apt-get install ros-noetic-ros-control</code></pre>
- <pre><code>sudo apt install rospack-tools</code></pre>
- <pre><code>sudo apt install ros-noetic-teleop-twist-keyboard</code></pre>
- <pre><code>sudo apt update</code></pre>

## Installing Livox-SDK2:
Instructions from repo: https://github.com/Livox-SDK/Livox-SDK2
- <pre><code>sudo apt install cmake</code></pre>
- <pre><code>git clone https://github.com/Livox-SDK/Livox-SDK2.git</code></pre>
- <pre><code>cd ./Livox-SDK2/</code></pre>
- <pre><code>mkdir build</code></pre>
- <pre><code>cd build</code></pre>
- <pre><code>cmake .. && make -j</code></pre>
- <pre><code>sudo make install</code></pre>

## Installing livox_ros_driver2:
Instruction from repo: https://github.com/Livox-SDK/livox_ros_driver2
- <pre><code>git clone https://github.com/Livox-SDK/livox_ros_driver2.git</code></pre>
- <pre><code>source /opt/ros/noetic/setup.sh</code></pre>
- <pre><code>cd livox_ros_driver2</code></pre>
- <pre><code>./build.sh ROS1</code></pre>

# Launching ROS Files
Always source before roslaunching at directory: .../UGV-Robot/ros_noetic_catkin_ws/

## Moving drivetrain in Gazebo:
- <pre><code>roslaunch full_ugv_robot_urdf full_ugv_robot_urdf.launch</code></pre>
  - Use the 'I' key to move forwards, 'J' & 'L' for left and right, and ',' for backwards.

## Moving drivetrain and arm in Rviz and Gazebo w/ MoveIt:
- <pre><code>roslaunch full_ugv_robot_moveit_config full_ugv_robot_sim.launch</code></pre>

## Moving end effector in XYZ axes with a remote controller:
- rosrun full_ugv_robot_moveit_config test_arm_movement.py

## Livox LiDAR quick start sample:
- Make the livox_lidar_quick_start.lidar file in this directory: .../UGV-Robot/ros_noetic_catkin_ws/src/Livox-SDK2/build/samples/livox_lidar_quick_start/ using the file given in .../UGV-Robot/ROS_Extras/
- ./livox_lidar_quick_start livox_lidar_quick_start.lidar

## Livox LiDAR Rviz example:
- roslaunch livox_ros_driver2 rviz_MID360.launch

## Livox LiDAR Transmitter & Receiver:
- For transmitting LiDAR data from computer 1 to computer 2 where computer 2 displays the point cloud data in Rviz.
- Computer 1:
  - roslaunch livox_ros_driver2 rviz_sender_MID360.launch
- Computer 2:
  - roslaunch livox_ros_driver2 rviz_receiver_MID360.launch
