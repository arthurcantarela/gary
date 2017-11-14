import sys
import RPi.GPIO as G
from time import sleep
G.setmode(G.BCM)

class Trowel():
    def __init__(self):
        """Set GPIOs controllers for motors"""

        # GPIOs controllers for right motors
        G.setup(5, G.OUT) # front
        G.setup(6, G.OUT) #back

        # GPIOs controllers for right motors

        G.setup(13,G.OUT) # front
        G.setup(19,G.OUT) # back

        # GPIOs controller for servomotor
        G.setup(3,G.OUT)

        # GPIO PWM setup

        G.setup(18,G.OUT) #PWM for motors
        G.setup(3,G.OUT) #PWM for servomotor

        #PWM frequency operation
        self.pwm_sm = G.PWM(3,50)
        self.pwm_m = G.PWM(18,100)

        #Starts PWM cycle
        self.pwm_sm.start(0)
        self.pwm_m.start(0)

    def move(self, direction):
        pass

    def move_foward(self):
        pass

    def rotate(self, degrees):
        pass

    def set_velocity(self, velocity):
        pass

    def turn_servo(self, degrees):
        pass

    def sleep(self):
        self.pwm_sm.stop()
        G.cleanup()
