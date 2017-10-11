import cv2
import numpy as np

drawing = False # if mouse is pressed change to True

def nothing(x):
    pass

# mouse callback function
def draw(event, x, y, flags, param):
    global r, g, b, w
    color = (r, g, b)
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),w,color, -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img,(x,y),w,color, -1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('W','image',1,50,nothing)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    w = cv2.getTrackbarPos('W','image')

    cv2.setMouseCallback('image',draw)


cv2.destroyAllWindows()
