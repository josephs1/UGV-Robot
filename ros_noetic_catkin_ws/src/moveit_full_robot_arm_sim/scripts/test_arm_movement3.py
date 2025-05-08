#!/usr/bin/python3
import rospy
import moveit_commander
import geometry_msgs.msg
import pygame
import sys

class MyRobot:
    def __init__(self, group_name):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('move_arm_xyz_controller', anonymous=True)
        
        self._group = moveit_commander.MoveGroupCommander(group_name)
        self._group.set_planning_time(5.0)  # Increase planning time for complex motions

        # Initialize pygame for joystick input
        pygame.init()
        pygame.joystick.init()

        # Ensure a joystick is connected
        if pygame.joystick.get_count() < 1:
            rospy.logerr("No joystick detected. Please connect one.")
            return

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        rospy.loginfo("Joystick initialized: {}".format(self.joystick.get_name()))

    def get_joystick_input(self):
        pygame.event.pump()  # Process events

        x = self.joystick.get_axis(0)
        y = self.joystick.get_axis(1)
        z = self.joystick.get_axis(4)

        # Apply dead zone filtering
        x = 0.0 if abs(x) < 0.25 else x * 0.05
        y = 0.0 if abs(y) < 0.25 else y * 0.05
        z = 0.0 if abs(z) < 0.25 else z * 0.05

        return x, y, z

    def move_to_xyz(self):
        # Get current pose
        current_pose = self._group.get_current_pose().pose

        # Get joystick input
        x_move, y_move, z_move = self.get_joystick_input()

        # Modify current pose
        new_pose = geometry_msgs.msg.Pose()
        new_pose.position.x = current_pose.position.x + x_move
        new_pose.position.y = current_pose.position.y + y_move
        new_pose.position.z = current_pose.position.z + z_move
        new_pose.orientation = current_pose.orientation  # Preserve orientation

        rospy.loginfo(f"Moving to: X={new_pose.position.x}, Y={new_pose.position.y}, Z={new_pose.position.z}")

        # Set the new target pose and plan movement
        self._group.set_pose_target(new_pose)
        plan = self._group.plan()
        if plan:
            self._group.go(wait=True)
        else:
            rospy.logwarn("Motion planning failed!")

if __name__ == '__main__':
    arm_controller = MyRobot("arm_group")

    rate = rospy.Rate(10)  # Run at 10 Hz
    while not rospy.is_shutdown():
        arm_controller.move_to_xyz()
        rate.sleep()

