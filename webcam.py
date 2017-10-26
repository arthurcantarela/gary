import numpy as np
import cv2
import time

def show_video():
    ''' Opens a new window and show what the webcam is recording '''

    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('frame',frame)
            cv2.waitKey(1)
        else:
            print("Error, couldn't find webcam")

    cap.release()
    cv2.destroyAllWindows()

def save_picture():
    ''' Saves an image capture from the webcam
        The name of the saved image is today's
        date.   '''

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        # The format below makes it easier to find most recent pictures after they're saved
        cv2.imwrite(time.strftime("%Y-%m-%d-%H-%M-%S")+'.png',frame)
    else:
        print("Error, couldn't find webcam")
    cap.release()


def save_pictures(times,frequency):
    ''' Saves an image capture from the webcam
        every (frequency) seconds (times) times
        The name of the saved image is today's
        date.   '''

    cap = cv2.VideoCapture(0)
    for i in range(times):
        ret, frame = cap.read()
        if not ret:
            print("Error, couldn't find webcam")
            exit(1)
        # The format below makes it easier to find most recent pictures after they're saved
        cv2.imwrite(time.strftime("%Y-%m-%d-%H-%M-%S")+i+'.png',frame)
        time.sleep(frequency)
    cap.release()


