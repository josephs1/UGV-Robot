# Main Code Process:
This is the main code given for the Arduino, the Jetson, and the client's laptop. The code can be fully started from the client laptop given that both computers are connected to the same network and IP addresses are known.

Connect a remote controller to the laptop and use the following command to be able to control the drivetrain and arm for the robot:
- <code>python laptop_client_controller_no_log.py</code>

# Arm Movement:
Use the right joystick to move a joint forwards or backwards. Press the X button to switch to the next joint's motor. Seqeunce is: servo1 (end effector's joint), servo2 (joint 4), servo3 (joint 3), nema (joint 2).

# Drivetrain Movement:
Hold right trigger to switch from arm movement to drivetrain movement. While held, use the left joystick to move the robot's left wheels forwards or backwards and use the right joystick to move the robot's right wheels forwards or backwards.
