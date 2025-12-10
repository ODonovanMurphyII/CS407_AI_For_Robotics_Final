# camera_publisher.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import time

class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')
        
        # Create publisher on topic 'camera/image_raw'
        self.publisher_ = self.create_publisher(Image, 'camera/image_raw', 1)
        
        # Set a timer to capture frames (e.g., 0.1 seconds = 1Hz)
        timer_period = 1  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Initialize OpenCV Bridge
        self.bridge = CvBridge()
        
        # Camera Setup
        self.camera_index = 0
        self.cam = cv2.VideoCapture(self.camera_index)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
        
        if not self.cam.isOpened():
            self.get_logger().error("Could not open the camera")
        else:
            self.get_logger().info("Camera Connected. Warming up...")
            # Waking the camera up (from your original script)
            for i in range(25):
                self.cam.read()
                time.sleep(0.1)
            self.get_logger().info("Camera Warmup Complete.")

    def timer_callback(self):
        ret, frame = self.cam.read()
        
        if ret:
            # Convert OpenCV image (BGR) to ROS Image message
            msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing video frame')
        else:
            self.get_logger().warn("Failed to capture frame")

    def __del__(self):
        # Release camera on shutdown
        if self.cam.isOpened():
            self.cam.release()

def main(args=None):
    rclpy.init(args=args)
    camera_publisher = CameraPublisher()
    
    try:
        rclpy.spin(camera_publisher)
    except KeyboardInterrupt:
        pass
    
    camera_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()