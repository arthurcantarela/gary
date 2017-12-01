import os
import cv2
from lib import cam

achados=0
temp=0

garbage_cascade = cv2.CascadeClassifier('photos/cascade/cascadeold.xml')

for filename in os.listdir("photos/positive/"):
    print("photos/positive/"+filename)
    img = cv2.imread("photos/positive/"+filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    garbage = garbage_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in garbage:
        temp=1
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    if temp == 1:
        achados+=1
        temp = 0
        cv2.imwrite("lixos_achados/"+filename, img)
print("Achei ", achados, " lixos")
