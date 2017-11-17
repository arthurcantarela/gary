import numpy as np
import cv2
import lib.cam

# run this script from / as python -m test.py

eyes = cam.Cam(0)
dir = os.path.dirname(__file__)
filename = os.path.join(dir, '/photos/positive/')
for filename in os.listdir():
    inp = cv2.imread(filename)
    out = eyes.detect_garbage_picture(inp)
    for i,e in enumerate(out):
        cv2.imwrite(filename+i, e)
eyes.close()
