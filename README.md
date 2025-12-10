CS407 AI For Robotics Final   
Image Used: https://github.com/slowrunner/ROS2-GoPiGo3  
Hardware Used: GoPiGo3 Raspberry Pi 4  
API Used: easygopigo3  
Distro Used: ROS2 Humble Hawksbill on Ubuntu 22.04 LTS Server (64-bit) for GoPiGo3 Robots  
Labeler: Yolo Label  

Goal:   
Build an AI model that has been trained to recognize left, right, forward, and back arrows. The output of this model will then be used aid a robot in navigating a maze.   



Modified Goal:   
Build an AI model that will reconize bad guys in Viruta Cop 2. 
Hardware used: Raspberry pi 5.     
Distro Used: Debian Linux 12 with Docker Container: ROS2 YOLO distro   
Labeler: Yolo Label    

Directory Map:   
- ~\Training Set  
    Contains Images used for training and validation. Contains label set as well.   
- ~\YOLOv8_Custom_Training  
    Contains Results from training. (vechical_badguys_run2) // First run failed after a few hours for some reason.  
- ~\ROS2CORRECTED 
    Contains publisher(camera) & subscriber(inference) nodes for proper ROS2 implementation
- ~\test1  
    Contains results from early inference run using main.py for testing prior to creating ROS2 nodes.  
