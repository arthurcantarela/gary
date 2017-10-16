import numpy as np
import cv2
import time

def mostrar_video():

    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('frame',frame)
            cv2.waitKey(1)
        else:
            print("Erro, webcam nao reconhecida")

    cap.release()
    cv2.destroyAllWindows()

def gravar_video():
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
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

