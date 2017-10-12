import cv2
import time
import numpy as np

img1 = cv2.imread('horse.jpg')
img2 = cv2.imread('stone.jpe')
img3 = cv2.imread('python.png')

def slide_next(im1, im2):
    for i in range(10):
        dst = cv2.addWeighted(im1,(i+1)/10,im2,(1-(i+1)/10.0),0)
        cv2.imshow('image', dst)
        time.sleep(0.1)

cv2.imshow('image', img1)
time.sleep(1)
slide_next(img1, img2)
time.sleep(1)
slide_next(img2, img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
