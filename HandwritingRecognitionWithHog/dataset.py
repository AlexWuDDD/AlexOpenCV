import sys
sys.path.append("..")

import imutils
import numpy as np
import mahotas
import cv2

def load_digits(datasetPath):
    data = np.genfromtxt(datasetPath, delimiter=",",
                         dtype="uint8")
    target = data[:,0]
    data = data[:, 1].reshape(data.shape[0], 28, 28)
    return (data, target)

