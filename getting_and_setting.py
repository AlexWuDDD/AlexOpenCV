import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# OpenCV represents images as NumPy arrays.
# Conceptually, we can think of this representation as a matrix
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# it’s important to note that OpenCV stores RGB channels in reverse order
# B  G   R
(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

corner = image[0:100, 0:100] # image[y, x]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Even though we specify pixels in terms of (x, y)-coordinates,
# when it comes to writing code, we access the individual pixel values as image[y, x] .
# Why does the y-coordinate come first?
# Well, keep in mind that an image is defined as a matrix.
# We define a matrix in terms of number of rows and number of columns.
# Therefore, to access an individual pixel located at (x, y),
# we first supply y, the row number, followed by x, the column number
# this is by far the most common mistake I see when first getting started with OpenCV,
# so be sure to keep this in mind.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


