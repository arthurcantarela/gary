import os
from lib import cam

# run this script from / as python -m test.py

eyes = cam.Cam(0)
dir = os.getcwd()
filename = os.path.join(dir, '/photos/positive/')
for filename in os.listdir():
    if filename.endswith(".png"):
        inp = cv2.imread(filename, 3)
        out = eyes.detect_garbage_picture(inp)
        for i,e in enumerate(out):
            # cv2.imwrite(filename+str(i), e)
            print("found 1 object in photo %s" % filename)
eyes.close()
