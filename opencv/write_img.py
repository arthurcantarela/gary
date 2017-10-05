import numpy as np
import cv2

img = cv2.imread('pineapple.jpe', 0)
cv2.imwrite('gray.png', img)


