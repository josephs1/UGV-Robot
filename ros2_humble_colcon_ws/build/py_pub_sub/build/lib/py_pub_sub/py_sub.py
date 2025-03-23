#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotArmController(Node):
    def __init__(self):
        super().__init__('robot_arm_controller')
        self.subscriber_ = self.create_subscription(String, 'object_position', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = RobotArmController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()