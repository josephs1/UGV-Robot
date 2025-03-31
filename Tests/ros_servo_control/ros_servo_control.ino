#include <Servo.h>
#include <ros.h>
#include <std_msgs/Float64.h>

ros::NodeHandle nh;

// Define servos
Servo servo1, servo2;

// Callback functions for joint commands
void joint1_cb(const std_msgs::Float64& cmd) {
    servo1.write(map(cmd.data, -1.57, 1.57, 0, 180));  // Convert radians to degrees
}

void joint2_cb(const std_msgs::Float64& cmd) {
    servo2.write(map(cmd.data, -1.57, 1.57, 0, 180));
}

// ROS subscribers
ros::Subscriber<std_msgs::Float64> sub_joint1("joint1_position_controller/command", joint1_cb);
ros::Subscriber<std_msgs::Float64> sub_joint2("joint2_position_controller/command", joint2_cb);

void setup() {
    nh.initNode();
    nh.subscribe(sub_joint1);
    nh.subscribe(sub_joint2);

    servo1.attach(9);  // Connect servo1 to pin 9
    servo2.attach(10); // Connect servo2 to pin 10
}

void loop() {
    nh.spinOnce();
    delay(10);
}
