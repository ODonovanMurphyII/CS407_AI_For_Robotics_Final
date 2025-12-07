import easygopigo3 as easy
from ultralytics import YOLO
import cv2 as cv 
import time
import os


## Creating Camera Object
cameraIndex = 0
cam = cv.VideoCapture(cameraIndex)
if(not cam.isOpened()):
    print("Could not open the camera")
else:
    print("Camera Connected")
    ## Waking the camera up
    for i in range(25):
        cam.read()
        time.sleep(0.1)


## need to move this somewhere better but for now
myModel = YOLO("best.pt")
VEHICALS = 0
BAD_GUYS = 1
THRESHOLD = 0.30

def explore():
    i = 0
    while(i < 360):
        print("Taking image")
        allClearFileName = os.path.join("./clear", "image" + str(i) + ".jpeg")
        badGuysFileName = os.path.join("./notclear", "image" + str(i) + ".jpeg")
        ret, image = cam.read()
        result = myModel.predict(source=image, save=True, classes=[BAD_GUYS])
        confidence = result[0].boxes.conf[0].item() if result[0].boxes else 0
        if(confidence > THRESHOLD):
            print("BAD GUY!\n")
            cv.imwrite(badGuysFileName, image)
            print("Image saved: " + badGuysFileName + "\n")
        else:
            print("ALL CLEAR!\n")
            cv.imwrite(allClearFileName, image)
            print("Image saved: " + allClearFileName + "\n")
        i += 1
        #robot.turn_degrees(i)

def main():
    # Objects
    #robot = easy.EasyGoPiGo3()
    #proxSensor = robot.init_distance_sensor()
    #frontServo = robot.init_servo("SERV01")

    #inits 
    #robot.stop()
    #robot.set_speed(200)

    print("Bad Guy Identifier!\n")
    print(myModel.names)
    #while(1):
    explore()
        


    




# Bringing up the robot
if __name__ == "__main__":
    main()