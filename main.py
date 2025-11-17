import easygopigo3 as easy
from ultralytics import YOLO

## need to move this somewhere better but for now
upModel = YOLO('Insert Model Here')
downModel = YOLO('Insert Model Here')
leftModel = YOLO('Insert Model Here')
rightModel = YOLO('Insert Model Here')

def explore(EasyGoPiGo3: robot):
    i = 0
    headingListUp = []
    headingListDown = []
    headingListLeft = []
    headingListRight = []
    while(i < 360):
        robot.turn_degrees(i)
        #take an image
        #predict using the model
        headingListUp[i] = upModel.predict(source='my image', save=True)
        headingListDown[i] = downModel.predict(source='my image', save=True)
        headingListLeft[i] = leftModel.predict(source='my image', save=True)
        headingListRight[i] = rightModel.predict(source='my image', save=True)
        i += 1
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
        take_action(explore(robot), robot)


    




# Bringing up the robot
if __name__ == "__main__":
    main()