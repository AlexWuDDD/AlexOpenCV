import cv2
import numpy as np
from FaceDetection.facedetector import FaceDetector

cap = cv2.VideoCapture(0)
while (1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    # cv2.imshow("capture", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fd = FaceDetector('.\FaceDetection\haarcascade_frontalface_default.xml')
    faceRects = fd.detect(gray, scaleFactor=1.3,
                          minNeighbors=5,
                          minSize=(30, 30))

    for (x, y, w, h) in faceRects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Faces', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()