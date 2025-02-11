2/7/25:

Arm Assembly is based on the Arm Assembly file from Arm – replacement in the Solidworks folder. Labeled Axes and a global point with coordinate system was added for use in exporting to URDF.

underactuated_hand_rev2.4 is mostly the same as the previous one in the Hand folder, but with a few extra axes added (not important, but makes it different than the other).

Arm Assembly contains both assemblies put together (may not have properly attached them).

NOTE: need to convert the arm assembly to URDF, (Hand is already able to convert to URDF), in order to use in ROS Gazebo.

2/9/25:
Arm Exportation to URDF fully working.

2/10/25:
Begun implementing the URDF into a catkin workspace to use in ROS Gazebo.
