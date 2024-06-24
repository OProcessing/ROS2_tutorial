import rclpy as rp
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class OnedaySubscriber(Node) :
    def __init__(self) :
        super().__init__('turtlesim_subscriber')
        self.subscription = self.create_subscription(Bool, 'flag', self.timer_callback, 10)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription

    def timer_callback(self, msg):
        if msg.data :
            twist = Twist()
            twist.angular.z = 2.0
            self.publisher.publish(twist)


def main(args=None):
    rp.init(args=args)
    turtlesim_subscriber = OnedaySubscriber()
    rp.spin(turtlesim_subscriber)
    turtlesim_subscriber.destroy_node()
    rp.shutdown()


if __name__ == '__main__' :
    main()