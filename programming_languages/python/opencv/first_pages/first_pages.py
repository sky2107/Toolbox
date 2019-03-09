import cv2
import numpy as np
from matplotlib import pyplot as plt

print(cv2.__version__)

img = cv2.imread('images/duffyDuck.jpg', 0)


plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()


# cv2.imwrite('images/messigray.png', img)
