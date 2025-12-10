# inference_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
from ultralytics import YOLO

class InferenceSubscriber(Node):
    def __init__(self):
        super().__init__('inference_subscriber')
        
        
        # Subscribe to the camera topic
        self.subscription = self.create_subscription(
            Image, 
            'camera/image_raw', 
            self.listener_callback, 
            10
        )
        
        self.bridge = CvBridge()
        self.save_folder = "/images"
        
        # Configuration from your original script
        self.my_model = YOLO("best.pt")
        self.VEHICALS = 0
        self.BAD_GUYS = 1
        self.THRESHOLD = 0.30
        
        # Setup directories
        #os.makedirs("./clear", exist_ok=True)
        #os.makedirs("./notclear", exist_ok=True)
        
        # Counter for filenames (replacing the loop iterator)
        self.image_count = 0
        
        self.get_logger().info("Inference Node Started. Waiting for images...")
        self.get_logger().info(f"Classes: {self.my_model.names}")

    def listener_callback(self, data):
        try:
            # Convert ROS Image message back to OpenCV image
            current_frame = self.bridge.imgmsg_to_cv2(data)
            rgb_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2RGB)
            
            # Run Inference
            # Note: verbose=False reduces console spam
            result = self.my_model.predict(source=rgb_frame, classes=[self.BAD_GUYS], verbose=False)
            
            # Extract confidence (handle case where no boxes are found)
            confidence = result[0].boxes.conf[0].item() if result[0].boxes and len(result[0].boxes) > 0 else 0
            
            # Define filenames
            #all_clear_filename = os.path.join("./clear", f"image{self.image_count}.jpeg")
            #bad_guys_filename = os.path.join("./notclear", f"image{self.image_count}.jpeg")
            
            # Logic Check
            if confidence > self.THRESHOLD:
                self.image_count += 1
                self.get_logger().warn(f"BAD GUY DETECTED! (Conf: {confidence:.2f})")
                boundingBox = result[0].plot()
                self.filename = f"box_{self.image_count:04d}.jpg"
                self.fullpath = os.path.join(self.save_folder, self.filename)
                cv2.imwrite(self.fullpath,boundingBox)
                #self.get_logger().info(f"Image saved: {bad_guys_filename}")

                
                # --- ROBOT ACTION HERE ---
                # If you re-integrate EasyGoPiGo3, this is where you would 
                # call robot.stop() or take evasive action.
                
            else:
                # Optional: Uncomment if you want to log 'Clear' status every frame
                # self.get_logger().info("ALL CLEAR")
                #cv2.imwrite(all_clear_filename, current_frame)
                self.get_logger().warn(f"All Clear! (Conf: {confidence:.2f})")
                
            
        except Exception as e:
            self.get_logger().error(f"Error processing image: {e}")

def main(args=None):
    rclpy.init(args=args)
    inference_subscriber = InferenceSubscriber()
    
    try:
        rclpy.spin(inference_subscriber)
    except KeyboardInterrupt:
        pass
        
    inference_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()