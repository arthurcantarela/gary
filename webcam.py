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

def save_video():
    ''' Saves a video capture from the webcam
        (Not currently working probably due to
        codec problems) '''
    print("Teste")
    cap = cv2.VideoCapture(0)

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
    cap.release()
    out.release()
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


