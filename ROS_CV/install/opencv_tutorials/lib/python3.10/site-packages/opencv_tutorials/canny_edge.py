import rclpy as rp
from sensor_msgs.msg import Image
import cv2
from rclpy.node import Node
from cv_bridge import CvBridge

class CannyEdge(Node) :
    def __init__(self) :
        super().__init__('img_subscriber')
        self.subscription = self.create_subscription(Image, '/camera', self.canny_edge, 10)
        self.publisher = self.create_publisher(Image, '/canny_edges', 10)
        self.cv_bridge = CvBridge()

    def canny_edge(self, img_msg):
        cv_image = self.cv_bridge.imgmsg_to_cv2(img_msg, 'bgr8')
        edges = cv2.Canny(cv_image, 100, 200)

        edge_msg = self.cv_bridge.cv2_to_imgmsg(edges, encoding='mono8')
        self.publisher.publish(edge_msg)

        cv2.waitKey(1)


def main(args=None):
    rp.init(args=args)
    img_subscriber = CannyEdge()
    rp.spin(img_subscriber)
    img_subscriber.destroy_node()
    rp.shutdown()


if __name__ == '__main__' :
    main()