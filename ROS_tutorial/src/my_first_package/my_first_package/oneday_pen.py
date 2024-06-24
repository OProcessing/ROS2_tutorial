import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import SetPen

class OnedayPen(Node) :
    def __init__(self) :
        super().__init__('turtlesim_subscriber')
        self.subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.pen_callback, 10)
        self.subscription
        self.cli = self.create_client(SetPen, '/turtle1/set_pen')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.pen_state = None

    def pen_callback(self, msg):
        if msg.x < 5 :
            if self.pen_state != 'red':
                self.pen_state = 'red'
                print(f"X is below 5: {msg.x}")
                self.set_pen(255, 0, 0)

        if msg.x > 5 :
            if self.pen_state != 'black':
                self.pen_state = 'black'
                print(f"X is above 5: {msg.x}")
                self.set_pen(0, 0, 0)

    def set_pen(self, red, green, blue) :
        pen = SetPen.Request()
        pen.r = red
        pen.g = green
        pen.b = blue
        pen.width = 3

        self.cli.call_async(pen)

def main(args=None):
    rp.init(args=args)
    oneday_pen = OnedayPen()
    rp.spin(oneday_pen)

    oneday_pen.destroy_node()
    rp.shutdown()


if __name__ == '__main__' :
    main()