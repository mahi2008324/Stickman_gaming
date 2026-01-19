import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector

# Initialize the hand detector
detector = HandDetector(detectionCon=0.5, maxHands=2)

# Initialize the webcam
cam = cv2.VideoCapture(0)

cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

while True:
    success, frame = cam.read()
    img = cv2.flip(frame, 1)  # Flip the frame horizontally
    hands, img = detector.findHands(img)  # Find hands in the frame
    if hands and hands[0]['type'] == "Left":
        fingers = detector.fingersUp(hands[0])
        totalFingers = fingers.count(1)
        cv2.putText(img, f'Fingers: {totalFingers}',(50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0,255, 0), 2)
        if totalFingers == 1:
            pyautogui.keyDown('right')
            pyautogui.keyUp('left')
        if totalFingers == 0:
            pyautogui.keyDown('left')
            pyautogui.keyUp('right')
    cv2.imshow("Livefeed", img)

    cv2.waitKey(1)
