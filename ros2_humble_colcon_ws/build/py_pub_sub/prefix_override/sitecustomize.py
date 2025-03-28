import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jstefan1/CodeWorkspace/UGV-Robot/ros2_humble_colcon_ws/install/py_pub_sub'
