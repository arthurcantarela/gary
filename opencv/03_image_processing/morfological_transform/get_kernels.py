import numpy as np
import cv2

# Rectangular Kernel
print(cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)))

# Elliptical Kernel
print(cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))

# Cross-shaped Kernel
print(cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)))
