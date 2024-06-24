import rclpy as rp
from rclpy.node import Node
from std_msgs.msg import Bool

class set_flag(Node) :
    def __init__(self) :
        super().__init__('turtlesim_publisher')
        self.publisher = self.create_publisher(Bool, 'flag', 10)
        timer_period = 5.0
        self.timer = self.create_timer(timer_period, self.set_flag)

    def set_flag(self) :
        msg = Bool()
        msg.data = True
        self.publisher.publish(msg)

def main(args=None):
    rp.init(args=args)
    turtlesim_publisher = set_flag()
    rp.spin(turtlesim_publisher)
    turtlesim_publisher.destroy_node()
    rp.shutdown()


if __name__ == '__main__' :
    main()