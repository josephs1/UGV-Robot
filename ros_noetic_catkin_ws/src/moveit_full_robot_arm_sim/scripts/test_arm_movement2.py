#!/usr/bin/python3

from __future__ import print_function
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import actionlib
import pygame
import time

try:
    from math import pi, tau, dist, fabs, cos
except:
    from math import pi, fabs, cos, sqrt
    tau = 2.0 * pi
    def dist(p, q):
        return sqrt(sum((p_i - q_i) ** 2.0 for p_i, q_i in zip(p, q)))

from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

class MyRobot:
    def __init__(self, Group_Name):
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('node_set_predefined_pose', anonymous=True)

        self._robot = moveit_commander.RobotCommander()
        self._scene = moveit_commander.PlanningSceneInterface()
        self._planning_group = Group_Name
        self._group = moveit_commander.MoveGroupCommander(self._planning_group)

        self._display_trajectory_publisher = rospy.Publisher(
            '/move_group/display_planned_path',
            moveit_msgs.msg.DisplayTrajectory,
            queue_size=1
        )

        self._exectute_trajectory_client = actionlib.SimpleActionClient(
            'execute_trajectory',
            moveit_msgs.msg.ExecuteTrajectoryAction
        )
        self._exectute_trajectory_client.wait_for_server()

        self._planning_frame = self._group.get_planning_frame()
        self._eef_link = self._group.get_end_effector_link()
        self._group_names = self._robot.get_group_names()

        self._group.set_max_velocity_scaling_factor(0.1)
        self._group.set_max_acceleration_scaling_factor(0.1)

        rospy.loginfo('\033[95m' + "Planning Frame: {}".format(self._planning_frame) + '\033[0m')
        rospy.loginfo('\033[95m' + "End Effector Link: {}".format(self._eef_link) + '\033[0m')
        rospy.loginfo('\033[95m' + "Group Names: {}".format(self._group_names) + '\033[0m')
        rospy.loginfo('\033[95m' + " >>> MyRobot initialization is done." + '\033[0m')

    def move_relative(self, dx, dy, dz):
        """Plan a relative Cartesian movement but do not execute it immediately."""
        if dx == 0 and dy == 0 and dz == 0:
            return

        waypoints = []
        current_pose = self._group.get_current_pose().pose
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = current_pose.position.x + dx
        target_pose.position.y = current_pose.position.y + dy
        target_pose.position.z = current_pose.position.z + dz
        target_pose.orientation = current_pose.orientation

        waypoints.append(target_pose)

        (plan, fraction) = self._group.compute_cartesian_path(
            waypoints,
            0.02,           # eef_step
            False,            # jump_threshold set to 0.0 means no sudden joint jumps allowed
        )

        if fraction > 0.95:
            self._last_plan = plan
            rospy.loginfo('\033[36m' + f"Path planned successfully ({fraction*100:.1f}%). Waiting for execution..." + '\033[0m')
        else:
            self._last_plan = None
            rospy.logwarn('\033[91m' + f"Cartesian path planning failed or incomplete ({fraction*100:.2f}% achieved)." + '\033[0m')

    def execute_last_plan(self):
        if hasattr(self, '_last_plan') and self._last_plan:
            goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
            goal.trajectory = self._last_plan
            self._exectute_trajectory_client.send_goal(goal)
            self._exectute_trajectory_client.wait_for_result()
            rospy.loginfo('\033[32m' + "Motion executed." + '\033[0m')
        else:
            rospy.logwarn('\033[91m' + "No valid plan to execute." + '\033[0m')

    def joystick_listener(self):
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            print("No joystick detected.")
            return

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        rospy.loginfo('\033[92m' + "Controller connected: {}".format(joystick.get_name()) + '\033[0m')

        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            pygame.event.pump()

            dx = joystick.get_axis(0)
            dz = -joystick.get_axis(1)
            dy = joystick.get_axis(3)

            deadzone = 0.25
            if abs(dx) < deadzone:
                dx = 0
            if abs(dy) < deadzone:
                dy = 0
            if abs(dz) < deadzone:
                dz = 0

            scale = 0.1
            if dx != 0 or dy != 0 or dz != 0:
                self.move_relative(dx * scale, dy * scale, dz * scale)
                
            rospy.loginfo(f"Joystick: dx={dx}, dy={dy}, dz={dz}")

            # Button A (index 0) executes the latest plan
            if joystick.get_button(0):
                self.execute_last_plan()

            # Button B (index 1) exits
            if joystick.get_button(1):
                rospy.loginfo("B button pressed. Exiting...")
                break
            time.sleep(0.5)


    def __del__(self):
        moveit_commander.roscpp_shutdown()
        rospy.loginfo('\033[95m' + "Object of class MyRobot Deleted." + '\033[0m')


def main():
    arm = MyRobot("arm_group")
    arm.joystick_listener()

if __name__ == '__main__':
    main()

