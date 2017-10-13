import cv2
import numpy as np

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)