import cv2
import serial
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)
# mySerial = serial.Serial('COM5', 9600, 8)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands :
        hand1 = hands[0]
        fingers= detector.fingersUp(hand1)
        nfingers = ''.join(str(fingers).split(','))
        
        sfingers = str(nfingers)
        sfingers = sfingers.replace(' ', '')
        print(sfingers)
        
        # mySerial.write(sfingers.encode())

    cv2.imshow("Image", img)
    cv2.waitKey(1)


