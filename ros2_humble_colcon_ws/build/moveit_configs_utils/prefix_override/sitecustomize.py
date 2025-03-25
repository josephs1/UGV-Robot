import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ugv-c7/CodeWorkspace/UGV-Robot/ros2_humble_colcon_ws/install/moveit_configs_utils'
