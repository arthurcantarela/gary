import cv2
import time

class Cam:
    def __init__(self, num=0, d_photos="photos/"):
        """ Initializes cam object. """
        self.cam_num = num
        self.d_photos = d_photos
        self.cap = cv2.VideoCapture(self.cam_num)
        ret, self.frame = self.cap.read()
        if not ret:
            return ret

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

