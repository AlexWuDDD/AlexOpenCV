from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Path to the image')
ap.add_argument('-c', '--clusters', required=True, type=int, help='# of clusters')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure()
plt.axis('off')
plt.imshow(image)
plt.show()

image = image.reshape((image.shape[0]*image.shape[1], 3))
print(image)


# why do we change color spaces
# https://ppao.pyimagesearch.com/lessons/ppao-chapter-6-image-processing/
# https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/