import os
from lib import cam
import cv2

# run this script from / as python -m test.py

eyes = cam.Cam(0)
dir = os.getcwd()
filedir = os.path.join(dir, 'photos/positive/')
testdir = os.path.join(dir, 'test/')
for f in os.listdir(filedir):
    filename = os.path.join(filedir, f)
    if filename.endswith(".png"):
        print()
        print(filename)
        print()
        inp = cv2.imread(filename)
        out = eyes.detect_garbage_picture(inp)
        for i,e in enumerate(out):
            cv2.imwrite(os.path.join(testdir, f+str(i)), e)
            print("found 1 object in photo %s" % filename)
        print()
eyes.close()
