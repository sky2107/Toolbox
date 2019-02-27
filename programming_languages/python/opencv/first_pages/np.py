import cv2
import numpy as np
img = cv2.imread('../images/duffyDuck.jpg')
b,g,r = cv2.split(img)

# px = img[100,100]
# print(px)
# # accessing only blue pixel
# blue = img[100,100,0]
# print(blue)
# print(img.item(10,10,2))

# img.itemset((10,10,2),100)
# print(img.item(10,10,2))
# print(img.shape)##
# print(img.size)

cv2.imshow('imi', r)
cv2.waitKey(0)
cv2.destroyAllWindows()