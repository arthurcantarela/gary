import os
from lib import cam
import cv2

# run this script from / as python -m test.py

eyes = cam.Cam(0)
dir = os.getcwd()
filedir = os.path.join(dir, 'photos/positive/')
for filename in os.listdir(filedir):
    filename = os.path.join(filedir, filename)
    if filename.endswith(".png"):
        print()
        print(filename)
        print()
        inp = cv2.imread(filename)
        out = eyes.detect_garbage_picture(inp)
        for i,e in enumerate(out):
            # cv2.imwrite(filename+str(i), e)
            print("found 1 object in photo %s" % filename)
        print()
eyes.close()
