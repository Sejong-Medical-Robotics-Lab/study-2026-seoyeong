import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Driver(Node):
	def __init__(self):
		super().__init__("driver")
		self.pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
		self.timer = self.create_timer(1.0, self.tick)
		self.count = 0
	def tick(self):
		msg = Twist()
		msg.linear.x = 2.0
		msg.angular.z = 1.8
		self.pub.publish(msg)
		self.count += 1
def main():
		rclpy.init()
		rclpy.spin(Driver())
if __name__ == "__main__":
		main()
