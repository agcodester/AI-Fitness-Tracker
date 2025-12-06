import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
print("Choose the exercise: \n1:pull ups \n2:squats \n3:lunges \n4:push_ups \n5:bicep_curls \n6:crunches")
ar=int(input())
def exercise(argument):
    switcher={
        1:pull_ups,
        2:squats,
        3:lunges,
        4:push_ups,
        5:bicep_curls,
        6:crunches,
    }
    return switcher.get(argument,'default')

def pull_ups():
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()
    count = 0
    dir = 0
    total_rep = 5
    while count<total_rep:
        success, img = cap.read()
        img = cv2.resize(img, (1288, 720))
        # img = cv2.imread("new5.jpg")
        img = detector.findPose(img, False)
        lmlist = detector.findPosition(img, False)
        # print(lmlist)
        if len(lmlist) != 0:
            # Right Arm
            detector.finfAngle(img, 12, 14, 16)
            # Left Arm
            angle = detector.finfAngle(img, 11, 13, 15)
            per = np.interp(angle, (59, 128), (0, 100))
            # print(angle,per)

            # checj for the dumbell curl
            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0
            cv2.putText(img, f'{(int(per))}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            cv2.imshow("Image", img)
            if cv2.waitKey(1)==ord('e'):
                break

def squats():
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()
    count = 0
    dir = 0
    total_rep = 5
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1288, 720))
        # img = cv2.imread("new5.jpg")
        img = detector.findPose(img, False)
        lmlist = detector.findPosition(img, False)
        # print(lmlist)
        if len(lmlist) != 0:
            # Right Arm
            detector.finfAngle(img, 24, 26, 28)
            # Left Arm
            angle = detector.finfAngle(img, 23, 25, 27)
            per = np.interp(angle, (194, 275), (0, 100))
            print(angle,per)
            #bar=np.interp(angle,(220,310),(650,100))

            # checj for the dumbell curl
            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0
            cv2.putText(img, f'{(int(per))}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            #cv2.rectangle(img,(0,450),(250,720),(0,255),cv2.FILLED)
            cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            cv2.imshow("Image", img)
            if cv2.waitKey(1)==ord('e'):
                break

def lunges():
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()
    count = 0
    dir = 0
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1288, 720))
        # img = cv2.imread("new5.jpg")
        img = detector.findPose(img, False)
        lmlist = detector.findPosition(img, False)
        # print(lmlist)
        if len(lmlist) != 0:
            # Right Arm
            detector.finfAngle(img, 24, 26, 28)
            # Left Arm
            angle = detector.finfAngle(img, 23, 25, 27)
            per = np.interp(angle, (190, 82), (0, 100))
            print(angle,per)
            #bar=np.interp(angle,(220,310),(650,100))

            # checj for the dumbell curl
            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0
            cv2.putText(img, f'{(int(per))}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            #cv2.rectangle(img,(0,450),(250,720),(0,255),cv2.FILLED)
            cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            cv2.imshow("Image", img)
            if cv2.waitKey(1)==ord('e'):
                break

def push_ups():
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()
    count = 0
    dir = 0
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1288, 720))
        # img = cv2.imread("new5.jpg")
        img = detector.findPose(img, False)
        lmlist = detector.findPosition(img, False)
        # print(lmlist)
        if len(lmlist) != 0:
            # Right Arm
            detector.finfAngle(img, 12, 14, 16)
            # Left Arm
            angle = detector.finfAngle(img, 11, 13, 15)
            per = np.interp(angle, (185, 284), (0, 100))
            print(angle,per)
            #bar=np.interp(angle,(220,310),(650,100))

            # checj for the dumbell curl
            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0
            cv2.putText(img, f'{(int(per))}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            #cv2.rectangle(img,(0,450),(250,720),(0,255),cv2.FILLED)
            cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            cv2.imshow("Image", img)
            if cv2.waitKey(1) == ord('e'):
                break

def bicep_curls():
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()
    count1 = 0
    count2 = 0
    dir1 = 0
    dir2 = 0
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1288, 720))
        # img = cv2.imread("new5.jpg")
        img = detector.findPose(img, False)
        lmlist = detector.findPosition(img, False)
        # print(lmlist)
        if len(lmlist) != 0:
            # Right Arm
            angle1 = detector.finfAngle(img, 12, 14, 16)
            # Left Arm
            angle2 = detector.finfAngle(img, 11, 13, 15)
            per1 = np.interp(angle1, (191, 330), (0, 100))
            per2 = np.interp(angle2, (190, 330), (0, 100))
            # print(angle,per)

            # checj for the dumbell curl
            if per1 == 100:
                if dir1 == 0:
                    count1 += 0.5
                    dir1 = 1
            if per1 == 0:
                if dir1 == 1:
                    count1 += 0.5
                    dir1 = 0

            if per2 == 100:
                if dir2 == 0:
                    count2 += 0.5
                    dir2 = 1
            if per2 == 0:
                if dir2 == 1:
                    count2 += 0.5
                    dir2 = 0
            cv2.putText(img, f'R-{(int(per1))}%', (700, 100), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 3)
            cv2.putText(img, "L-"+str(int(count2)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 3)
            #cv2.putText(img, str(int(count1)), (200, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            cv2.putText(img, f'L-{(int(per2))}%', (1000, 100), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 3)
            #cv2.putText(img, str(int(count2)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            cv2.putText(img, "R-"+str(int(count1)), (300, 100), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 3)
            cv2.imshow("Image", img)
            if cv2.waitKey(1)==ord('e'):
                break

def crunches():
    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()
    count = 0
    dir = 0
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1288, 720))
        # img = cv2.imread("new5.jpg")
        img = detector.findPose(img, False)
        lmlist = detector.findPosition(img, False)
        # print(lmlist)
        if len(lmlist) != 0:
            # Right Arm
            detector.finfAngle(img, 12, 24, 26)
            # Left Arm
            angle = detector.finfAngle(img, 11, 23, 25)
            per = np.interp(angle, (59, 128), (0, 100))
            # print(angle,per)

            # checj for the dumbell curl
            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0
            cv2.putText(img, f'{(int(per))}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
            cv2.imshow("Image", img)
            if cv2.waitKey(1)==ord('e'):
                break

output=exercise(ar)
output()