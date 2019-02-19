import argparse
import cv2
from FaceDetection.facedetector import FaceDetector


ap = argparse.ArgumentParser()
ap.add_argument('-f', '--face', required=True,
                help='Path to where the face cascade resides')
ap.add_argument('-i', '--image', required=True,
                help='Path to where the image file resides')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

fd = FaceDetector(args['face'])
faceRects = fd.detect(gray, scaleFactor=1.2,minNeighbors=5,
                      minSize=(30, 30))
print('I found {} face(s)'.format(len(faceRects)))

for (x,y, w, h) in faceRects:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Faces', image)
cv2.waitKey(0)
