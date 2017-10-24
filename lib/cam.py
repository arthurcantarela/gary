import numpy as np
import cv2
import time

class Cam(Object):
    def __init__(self, num=0, d_photos="photos")
        """ Initializes cam object. """
        self.cam_num = num
        self.d_photos = d_photos

    def init(self):
        """ Initializes the cam. """
        self.cap = cv2.VideoCapture(self.num)
        self.ret, self.frame = cap.read()

    def close(self):
        """ Closes the cam. """
        self.cap.release()

    def save_picture(self):
        """ Saves the current camera image by datetime. """
        if ret:
            cv2.imwrite(time.strftime("%Y-%m-%d-%H-%M-%S")+'.png', self.frame)
        else:
            print("error, couldn't find webcam")
            return 1

    def save_pictures(n, f):
        """ Saves n pictures with the frequency f."""
        for i in range(n):
            ret = self.save_picture()
            if ret:
                return ret
            time.sleep(f)

