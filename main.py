import urllib
import json
from pprint import pprint
from lib.cam import Cam
from lib.robot import GarbageColectorRobot

# Status Code:
# 0 - Dont have task to do
# 1 - Tasks in queue

def main():
    """Main program with the main loop for the robot."""

    # Create gary as GarbageColectorObject
    gary = GarbageColectorRobot()

    while gary.is_alive:
        # Download JSON
        gary.update()
        # Do tasks in order
        if gary.have_tasks:
            for e in gary.queue:
                gary.do(e)
        # Move
        gary.move()
        # Process images
        gary.eyes.process()

if __name__ == "__main__":
    main()
