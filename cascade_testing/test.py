
import numpy as np
import cv2

garbage_cascade = cv2.CascadeClassifier('cascade16-11-2017.xml')
garbage_cascade2 = cv2.CascadeClassifier('cascade15-11-2017.xml')

img = cv2.imread('img4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

garbage = garbage_cascade.detectMultiScale(gray, 1.3, 5)

garbage2 = garbage_cascade2.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in garbage:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

for (x,y,w,h) in garbage2:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

print("Cascade 16-11:")
print(garbage)
print("Cascade 15-11:")
print(garbage2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
