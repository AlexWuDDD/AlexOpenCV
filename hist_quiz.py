import matplotlib.pyplot as plt
import numpy as np
import cv2

image = cv2.imread('images/wave_test.png')
cv2.imshow('Original', image)


imageG = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', imageG)

hist = cv2.calcHist([imageG], [0], None, [256], [0, 256])
plt.figure()
plt.plot(hist)
plt.show()

chans = cv2.split(image) # B G R
hist2D = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [8, 8], [0, 256, 0, 256])
plt.figure()
p = plt.imshow(hist2D, interpolation='nearest')
plt.title('2D Color Histogram for R and G')
plt.colorbar(p)
plt.show()


cv2.waitKey(0)