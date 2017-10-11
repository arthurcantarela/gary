import cv2
import numpy as np

img = cv2.imread('chair.jpe')
b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))

img[:,:,2] = 0

cv2.imshow('image', img)
cv2.waitKey(0)
