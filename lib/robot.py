import lib.locomotion as loc

class GarbageColectorRobot():
    def __init__(self, cam_num=0, d_photos="photos/"):
        """Initializes the robot with cam."""
        self.eyes = Cam(cam_num, d_photos)
        self.alive = False

        gary.trowel = loc.Locomotion()

        try:
            # Init camera
            gary.eyes.init()
        except:
            print("Problem opening input camera %s." % self.eyes.num)
            gary.eyes.close()
            sys.exit(1)

        self.is_alive = True

    def update(self):
        """Download JSON and update has_tasks and queue vars."""
        urllib.request.urlretrieve('#', 'status.json')

        with open('status.json') as data_file:
            data = json.load(data_file)

        self.has_tasks = data["status"]
        self.queue = data["queue"]


    def do(self, action):
        """Switch case that calls methods based on the actions in
        the queue."""
        if action == 'move_foward':
            self.trowel.move_foward()
        else if action == 'turn_cw':
            self.trowel.move_clockwise()
        else if action == 'turn_ccw':
            self.trowel.move_cclockwise()
        else if action == 'eat':
            self.trowel.eat()
        else if action == 'stop':
            self.trowel.stop()
        else if action == 'see':
            self.eyes.detect

    def move(self):
        """Simple movement in its own axis."""
        pass

    def kill(self):
        """Stop the loop and release the cam."""
        self.eyes.close()
        self.alive = False
