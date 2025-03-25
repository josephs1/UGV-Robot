from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	ld = LaunchDescription()

	publisher_node = Node(
		package = "py_pub_sub",
		executable = "py_pub"
	)

	subscriber_node = Node(
		package = "py_pub_sub",
		executable = "py_sub"
	)

	ld.add_action(publisher_node)
	ld.add_action(subscriber_node)
	
	return ld
