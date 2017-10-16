import numpy as np
import cv2
import time

def main():

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

main()

