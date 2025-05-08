#! /usr/bin/python3

# Python 2/3 compatibility imports
from __future__ import print_function
from six.moves import input

# Include the necessary libraries 
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import actionlib
from pynput import keyboard  # Importing pynput for keyboard listening
import pygame
import time

try:
    from math import pi, tau, dist, fabs, cos
except:  # For Python 2 compatibility
    from math import pi, fabs, cos, sqrt

    tau = 2.0 * pi
    
    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))


from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

class MyRobot:

    # Default Constructor
    def __init__(self, Group_Name):
        # Initialize the moveit_commander and rospy node
        self._commander = moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('node_set_predefined_pose', anonymous=True)
        
        # Instantiate a RobotCommander object. This object is the outer-level interface to the robot
        self._robot = moveit_commander.RobotCommander()
        # Instantiate a PlanningSceneInterface object. This object is an interface to the world surrounding the robot.
        self._scene = moveit_commander.PlanningSceneInterface()
        
        # Define the move group for the robotic arm
        self._planning_group = Group_Name
        # Instantiate a MoveGroupCommander Object. This interface can be used to plan and execute motions on the robotic arm
        self._group = moveit_commander.MoveGroupCommander(self._planning_group)
        
        # Create a DisplayTrajectory ROS publisher which is used to display trajectories in Rviz
        self._display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

        # Create action client for the "Execute Trajectory" action server
        self._exectute_trajectory_client = actionlib.SimpleActionClient('execute_trajectory', moveit_msgs.msg.ExecuteTrajectoryAction)
        self._exectute_trajectory_client.wait_for_server()

        # Get the planning frame, end effector link, and the robot group names
        self._planning_frame = self._group.get_planning_frame()
        self._eef_link = self._group.get_end_effector_link()
        self._group_names = self._robot.get_group_names()

        rospy.loginfo('\033[95m' + "Planning Group: {}".format(self._planning_frame) + '\033[0m')
        rospy.loginfo('\033[95m' + "End Effector Link: {}".format(self._eef_link) + '\033[0m')
        rospy.loginfo('\033[95m' + "Group Names: {}".format(self._group_names) + '\033[0m')
        rospy.loginfo('\033[95m' + " >>> MyRobot initialization is done." + '\033[0m')

    def move_relative(self, dx, dy, dz):
        """Move the end effector relatively by dx, dy, dz in the current frame."""
        current_pose = self._group.get_current_pose().pose
        target_pose = geometry_msgs.msg.Pose()
        
        # Set new target pose relative to the current pose
        target_pose.position.x = current_pose.position.x + dx
        target_pose.position.y = current_pose.position.y + dy
        target_pose.position.z = current_pose.position.z + dz
        target_pose.orientation = current_pose.orientation  # Keep the same orientation
        
        #----------------------
        constraints = moveit_msgs.msg.Constraints()
        orientation_constraint = moveit_msgs.msg.OrientationConstraint()

        orientation_constraint.link_name = self._eef_link
        orientation_constraint.header.frame_id = self._planning_frame
        orientation_constraint.orientation = current_pose.orientation
        orientation_constraint.absolute_x_axis_tolerance = 0.1
        orientation_constraint.absolute_y_axis_tolerance = 0.1
        orientation_constraint.absolute_z_axis_tolerance = 0.1
        orientation_constraint.weight = 1.0

        constraints.orientation_constraints.append(orientation_constraint)
        self._group.set_path_constraints(constraints)
        #----------------------
        
        self._group.set_pose_target(target_pose)
        plan_success, plan, planning_time, error_code = self._group.plan()

        if plan_success:
            self._last_plan = plan
            goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
            goal.trajectory = plan
            self._exectute_trajectory_client.send_goal(goal)
            self._exectute_trajectory_client.wait_for_result()
            rospy.loginfo('\033[32m' + "Movement complete." + '\033[0m')
        else:
            rospy.logwarn('\033[93m' + "Planning failed." + '\033[0m')
            self._last_plan = None

    def on_press(self, key):
        """Listen for key press and move the robot end effector accordingly."""
        try:
            if key == keyboard.Key.esc:
                # Stop the listener when Escape is pressed
                return False
            elif key.char == 'w':
                self.move_relative(0, 0, 0.05)  # Move up by 0.01 in Z
            elif key.char == 's':
                self.move_relative(0, 0, -0.05)  # Move down by 0.01 in Z
            elif key.char == 'a':
                self.move_relative(-0.05, 0, 0)  # Move left by 0.01 in X
            elif key.char == 'd':
                self.move_relative(0.05, 0, 0)  # Move right by 0.01 in X
            elif key.char == 'e':
                self.move_relative(0, 0.05, 0)  # Move forward by 0.01 in Y
            elif key.char == 'q':
                self.move_relative(0, -0.05, 0)  # Move backward by 0.01 in Y
        except AttributeError:
            pass  # Handle special keys like shift, ctrl, etc.

    def start_keyboard_listener(self):
        """Start listening for keyboard inputs."""
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
            
    def execute_last_plan(self):
        if hasattr(self, '_last_plan') and self._last_plan:
            goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
            goal.trajectory = self._last_plan
            self._exectute_trajectory_client.send_goal(goal)
            self._exectute_trajectory_client.wait_for_result()
            rospy.loginfo('\033[32m' + "Motion executed." + '\033[0m')
        else:
            rospy.logwarn('\033[91m' + "No valid plan to execute." + '\033[0m')

    # Class Destructor
    def __del__(self):
        # Shut down the moveit commander
        moveit_commander.roscpp_shutdown()
        rospy.loginfo('\033[95m' + "Object of class MyRobot Deleted." + '\033[0m')
    
    def start_joystick(self):
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            print("No joystick detected.")
            return

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    
        while True:
            pygame.event.pump()
	
            dx = joystick.get_axis(1)
            dz = -joystick.get_axis(3)
            dy = joystick.get_axis(0)
	
            deadzone = 0.25
            if abs(dx) < deadzone:
                dx = 0
            if abs(dy) < deadzone:
                dy = 0
            if abs(dz) < deadzone:
                dz = 0
	    
            if dx < 0:
                self.move_relative(0, 0, 0.05)
            elif dx > 0:
                self.move_relative(0, 0, -0.05)
            if dy < 0:
                self.move_relative(-0.05, 0, 0)
            elif dy > 0:
                self.move_relative(0.05, 0, 0)
            if dz < 0:
                self.move_relative(0, 0.05, 0)
            elif dz > 0:
                self.move_relative(0, -0.05, 0)
                
            # Button A (index 0) executes the latest plan
            if joystick.get_button(0):
                self.execute_last_plan()

            # Button B (index 1) exits
            if joystick.get_button(1):
                rospy.loginfo("B button pressed. Exiting...")
                break
	    
            time.sleep(0.02)
        
def main():
    # Create a new arm object from the MyRobot class
    arm = MyRobot("arm_group")
    
    # Start the keyboard listener in a separate thread
    # arm.start_keyboard_listener()
    
    arm.start_joystick()


if __name__ == '__main__':
    main()
        
        

