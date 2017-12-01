import numpy as np
import cv2
import urllib
import json
from pprint import pprint
from lib.cam import Cam
from lib.robot import GarbageColectorRobot

def main():
    """Main program with the main loop for the robot."""

    # Create gary as GarbageColectorObject
    gary = GarbageColectorRobot()

    while gary.is_alive:
        # Download JSON
        gary.update()
        # Do tasks in order
        if gary.have_tasks:
            for task in gary.queue:
                gary.do(task)
        # Move
        gary.move()
        # Process images
        action = gary.eyes.process()
        # Go foward, rotate or keep waiting
        gary.do(action)

if __name__ == "__main__":
    main()
