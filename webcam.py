import numpy as np
import cv2
import time

def init_cam():
    ''' Returns the cv2.VideoCapture(), which is used
        in the other functions in this file '''
    cap = cv2.VideoCapture(0)
    return cap

def release_cam(cam):
    cam.release

def show_video(cap):
    ''' Opens a new window and show what the webcam is recording '''

    print("Press 'q' to quit")
    while(True):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error, couldn't find webcam")

    cv2.destroyAllWindows()

def save_video(cap):
    ''' Saves a video capture from the webcam
        (Not currently working probably due to
        codec problems) '''
    print("Teste")

    # Define the codec and create VideoWriter object
    out_name = input("Please enter the name of the output file: ")
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame,0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()

def save_picture(cap):
    ''' Saves an image capture from the webcam
        The name of the saved image is today's
        date.   '''

    ret, frame = cap.read()
    if ret:
        # The format below makes it easier to find most recent pictures after they're saved
        cv2.imwrite(time.strftime("%Y-%m-%d-%H-%M-%S")+'.png',frame)
    else:
        print("Error, couldn't find webcam" +
                "Please make sure it has been initialized with cv2.VideoCapture()")


def save_pictures(times,frequency,cap):
    ''' Saves an image capture from the webcam
        every (frequency) seconds (times) times
        The name of the saved image is today's
        date.   '''

    for i in range(times):
        ret, frame = cap.read()
        if not ret:
            print("Error, couldn't find webcam" +
                "Please make sure it has been initialized with cv2.VideoCapture()")
            exit(1)
        # The format below makes it easier to find most recent pictures after they're saved
        cv2.imwrite(time.strftime("%Y-%m-%d-%H-%M-%S")+i+'.png',frame)
        time.sleep(frequency)


