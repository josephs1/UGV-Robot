import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ObjectPositionPublisher(Node):
    def __init__(self):
        super().__init__('object_position_publisher')
        self.publisher_ = self.create_publisher(String, 'object_position', 10)
        self.timer_ = self.create_timer(1.0, self.publish_position) # Publishing Frequency
        self.count = 0

    def publish_position(self):
        msg = String()
        msg.data = f"Object Position: x={self.count}, Y={self.count + 1}, Z={self.count + 2}"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = ObjectPositionPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()