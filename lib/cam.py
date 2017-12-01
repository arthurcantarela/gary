import numpy as np
import cv2
import time

class Cam:
    def __init__(self, num=0, d_photos="../photos/"):
        """ Initializes cam object. """
        self.cam_num = num
        self.d_photos = d_photos
        self.cap = cv2.VideoCapture(self.cam_num)
        self.cascade = cv2.CascadeClassifier('photos/cascade/cascade.xml')
        ret, self.frame = self.cap.read()
        if not ret:
            print("Error: webcam not found")

    def init(self):
        """ Initializes the cam. """
        self.cap = cv2.VideoCapture(self.cam_num)
        ret, self.frame = self.cap.read()
        if not ret:
            return ret

    def close(self):
        """ Closes the cam. """
        self.cap.release()

    def save_picture(self, i=''):
        """ Saves the current camera image by datetime. """
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite(time.strftime(self.d_photos+"%Y-%m-%d-%H-%M-%S")+str(i)+'.png', frame)
            return 1
        else:
            print("error, couldn't find webcam")
            return ret

    def save_pictures(self, n, seconds):
        """ Saves n pictures with the time interval seconds."""
        for i in range(n):
            ret = self.save_picture(i)
            time.sleep(seconds)
            if not ret:
                return ret

    def open_picture(self,path):
        return cv2.imread(self.d_photos+path)

    def detect_garbage_picture(self,frame):
            ans = []
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            garbage = self.cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in garbage:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                # cv2.imshow('frame',frame)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                ans += frame
            return tuple(ans)

    def detect_garbage(self):
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            garbage = self.cascade.detectMultiScale(gray, 1.3, 5)
            print(garbage)
            for (x,y,w,h) in garbage:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.imshow('frame',frame)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        else:
            print("Error: Couldn't take picture")
            return 1
