import rclpy
from rclpy.node import Node
from rclpy import time

from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix

from vk_162_gps.gps import getGPS 

class MinimalPublisher(Node):

	def __init__(self):
		super().__init__('gps_publisher')
		self.gps_pub = self.create_publisher(NavSatFix,'/gps', 10)
		timer_period = 0.2  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.get_logger().info('GPS initialised')

	def timer_callback(self):
		data = getGPS('/dev/ttyACM0')
		gpsmsg = NavSatFix()
		gpsmsg.header.stamp = self.get_clock().now().to_msg()
		gpsmsg.header.frame_id = "gps"
		gpsmsg.latitude  = data[0]
		gpsmsg.longitude = data[1]
		gpsmsg.altitude  = data[2]
		self.gps_pub.publish(gpsmsg)

def main(args=None):
	rclpy.init(args=args)
	minimal_publisher = MinimalPublisher()
	rclpy.spin(minimal_publisher)
	minimal_publisher.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
    main()