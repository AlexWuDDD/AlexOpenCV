import numpy as np
import cv2
red = (0, 0, 255)
black = (0, 0, 0)

canvas = np.zeros((300, 300, 3), dtype='uint8')
color = red
for (row, y) in enumerate(range(0, 300, 10)):
    for (col, x) in enumerate(range(0, 300, 10)):
        color = (0, 0, 255)
        if row % 2 == col % 2:
            color = (0, 0, 0)
        cv2.rectangle(canvas, (x, y), (x+10, y+10), color, -1)
cv2.circle(canvas, (150, 150), 45, (0, 255, 0), -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
