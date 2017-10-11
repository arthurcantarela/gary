import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.uint8)
cv2.circle(img, (256,128),45,(0,0,255),45)
cv2.circle(img, (round(170.67),round(275.8)), 45, (0,255,0),45)
pts = [[256,128], [round(170,67),round(275.8)],[round(2*170.67),round(275.8)]]
pts = np.array(pts, np.int32 )
cv2.fillPoly(img,[pts],(0,0,0))
cv2.circle(img, (round(2*170.67),round(275.8)), 45, (255,0,0),45)
pts = [[299-5,210-10], [round(2*170.67),276], [384+5,210-10]]
pts = np.array(pts, np.int32 )
cv2.fillPoly(img,[pts],(0,0,0))

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,'OpenCV',(171-90,450), font, 3,(255,255,255),4,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
