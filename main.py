import easygopigo3 as easy
from ultralytics import YOLO
import cv2 as cv 
import time

## Creating Camera Object
cam = cv2.VideoCapture(0)

## Waking the camera up
for i in range(25):
    cam.read()
    time.sleep(0.1)

## need to move this somewhere better but for now
myModel = YOLO("yolov8n.pt")
vehicles = 0
bad_guys = 1

def explore(EasyGoPiGo3: robot):
    i = 0
    headingList[i]
    while(i < 360):
        ret, image = cam.read()
        if not ret:
            ret, image = cam.read()
        else:
            headingList[i] = myModel.predict(source=image, save=True, classes=[] )
        i += 1
        robot.turn_degrees(i)
    return headingListUp, headingListDown, headingListLeft, headingListRight

# must be run IMMEDIATELY after explore
def take_action(upResults, downResults, leftResults, rightResults, EasyGoPiGo3: robot):
    upMax = max(upResults)
    upHeading = upResults.index(upMax)

    downMax = max(downResults)
    downHeading = downResults.index(downMax)

    leftMax = max(leftResults)
    leftHeading = leftResults.index(leftMax)

    rightMax = max(rightResults)
    rightHeading = rightResults.index(rightMax)

    largest = max(upMax, downMax, leftMax, rightMax)
    if largest == upMax:
        robot.turn_degrees(upHeading)
    elif largest == downMax:
        robot.turn_degrees(downHeading)
    elif largest == leftMax:
        robot.turn_degrees(leftHeading)
    elif largest == rightMax:
        robot.turn_degrees(rightHeading)

def main():
    # Objects
    robot = easy.EasyGoPiGo3()
    proxSensor = robot.init_distance_sensor()
    frontServo = robot.init_servo("SERV01")

    #inits 
    robot.stop()
    robot.set_speed(200)

    #Starting our maze solving loop
    # TODO this is crude but gets the basic idea
    while(1):
        


    




# Bringing up the robot
if __name__ == "__main__":
    main()