import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Original', image)

eq = cv2.equalizeHist(image)

hist1 = cv2.calcHist([image], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([eq], [0], None, [256], [0, 256])

fig = plt.figure()
ax = fig.add_subplot(121)
ax.plot(hist1)
ax = fig.add_subplot(122)
ax.plot(hist2)
plt.show()

cv2.imshow('Histogram Equalization', np.hstack([image, eq]))
cv2.waitKey(0)
