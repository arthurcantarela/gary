import cv2
import numpy as np

img = cv2.imread('chair.jpe')

px = img[100,100]
print(px)

img[100, 100] = [255,255,255]
print(img[100,100])

print(img.item(10,10,2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

print(img.shape)
print(img.size)
print(img.dtype)

random = img[100:300, 200:500]
img[0:200, 0:300] = random

cv2.imshow('image', img)
cv2.waitKey(0)
