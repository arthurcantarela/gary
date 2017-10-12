import cv2
import numpy as np

# Addition
x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x, y)) # 250+10=260 => 255
print(x+y)           # 250+10=260%256 => 4

# Blending
# g(x) = (1 - a).f0(x)+a.f1(x)

img1 = cv2.imread('horse.jpg')
img2 = cv2.imread('stone.jpe')

print(img1, img2)

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

