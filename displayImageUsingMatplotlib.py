import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

# image =mpimg.imread("chelsea-the-cat.png")
image = cv2.imread("chelsea-the-cat.png")
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()


# Summary
# In this blog post I showed you how to display matplotlib RGB images.
#
# We made use of matplotlib, pyplot and mpimg to load and display our images.
#
# To remove the axes of the figure, make a call to plt.axis("off").
#
# Just remember that if you are using OpenCV that your images are stored in BGR order rather than RGB!
#
# As long as you remember that, you won’t have any issues!