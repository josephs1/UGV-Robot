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

- <pre><code></code></pre>

