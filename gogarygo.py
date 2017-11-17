import sys
import RPi.GPIO as G
from time import sleep
G.setmode(G.BCM)

class GarbageColectorRobot:

    def __init__(self):
    # GPIOs controllers for left motors

        G.setup(5, G.OUT) # front
        G.setup(6, G.OUT) # back

        # GPIOs controllers for right motors

        G.setup(13,G.OUT) # front
        G.setup(19,G.OUT) # back

        # GPIOs controller for servomotor
        G.setup(3,G.OUT)

        # GPIO PWM setup

        G.setup(18,G.OUT) # PWM for motors
        G.setup(3,G.OUT) # PWM for servomotor

        #PWM frequency operation
        self.pwm_sm = G.PWM(3,50)
        self.pwm_m = G.PWM(18,100)

        #Starts PWM cycle
        self.pwm_sm.start(0)
    	self.pwm_m.start(0)

	#Initial position for trowel
	self.trowel(90)

    #Moves Gary for a direction
    def move(self,direction,speed):
	
	crawl(speed)

        #Stop
        if direction == 5:
            G.output(5,False)
            G.output(6,False)
            G.output(13,False)
            G.output(19,False)

        # Move forward
        if direction == 8:
            G.output(5, True)
            G.output(6, False)
            G.output(13, True)
            G.output(19, False)

        # Move backward
        if direction == 2:
            G.output(5,False)
            G.output(6,True)
            G.output(13,False)
            G.output(19,True)

        #Move Right
        if direction == 6:
            G.output(5,True)
            G.output(6,False)
            G.output(13,False)
            G.output(19,False)

        #Move Left
        if direction == 4:
            G.output(5,False)
            G.output(6,False)
            G.output(13,True)
            G.output(19,False)

        sleep(1)


    #Velocity Control
    def crawl(self,speed):

        #Stay
        if speed == 0:
            self.pwm_m.ChangeDutyCycle(0)

        #Low Speed
        if speed == 1:
            self.pwm_m.ChangeDutyCycle(30)

        #Regular Speed
        if speed == 2:
            self.pwm_m.ChangeDutyCycle(60)

        #High Speed
        if speed == 3:
            self.pwm_m.ChangeDutyCycle(100)


    	self.pwm_m.stop()

    #Servomotor control
	
	#Reminder: Initial state - angle 90; Prepare trowel - angle 180; EAT - angle: 0; Next food - angle 90 (loop)
	#

    def trowel(self,angle):
        duty = angle/18 + 2
        G.output(3, True)
        self.pwm_sm.ChangeDutyCycle(duty)
	sleep(1)

        G.output(3, False)
	self.pwm_sm.ChangeDutyCycle(0) 

    def hungry(self):

	#Open
	self.trowel(180)
	sleep(1)
	
	#Eat
	self.trowel(0)
	sleep(1)

	#Close
	self.trowel(90)
	sleep(1)


    def sleep(self):
        self.pwm_sm.stop()
        G.cleanup()
