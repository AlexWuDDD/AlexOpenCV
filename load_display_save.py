import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels:{}".format(image.shape[2]))

cv2.imshow("Image", image)  # the first parameter is a string, the name of our window
# Using a parameter of 0
# indicates that any keypress will un-pause the execution.
cv2.waitKey(0)
cv2.imwrite("newimage.jpg", image)



