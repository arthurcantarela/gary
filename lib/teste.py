import cam
import cv2

a = cam.Cam()

frame = a.open_picture("positive/2017-10-26-15-33-005.png")

a.detect_garbage_picture(frame)

