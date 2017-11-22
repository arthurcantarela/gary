import sys
import RPi.GPIO as G
from time import sleep
G.setmode(G.BCM)

class Trowel:

    def __init__(self):
    # GPIOs controllers for left motors

        G.setup(5, G.OUT) # front
        G.setup(6, G.OUT) # back

        # GPIOs controllers for right motors

        G.setup(13,G.OUT) # front
        G.setup(19,G.OUT) # back

        # GPIOs controller for servomotor
        G.setup(3,G.OUT)

        # GPIO with PWM setup for each motor

        G.setup(18,G.OUT) # PWM for front-left
        G.setup(23,G.OUT) # PWM for front-right
        G.setup(24,G.OUT) # PWM for back-left
        G.setup(25,G.OUT) # PWM for back-right

        #PWM frequency operation
        self.pwm_sm = G.PWM(3,50)
        self.pwm_m1 = G.PWM(18,100)
        self.pwm_m2 = G.PWM(23,100)
        self.pwm_m3 = G.PWM(24,100)
        self.pwm_m4 = G.PWM(25,100)

        #Starts PWM cycle
        self.pwm_sm.start(0)
    	self.pwm_m1.start(0)
        self.pwm_m2.start(0)
        self.pwm_m3.start(0)
        self.pwm_m4.start(0)

	#Initial position for trowel
	self.move_servo(90)

    #Moves Gary for a direction
    def move(self,direction,speed):

    ###########Test if its nececessary to change the velocitys according to the move of the robot
	self.vel_motor1(speed)
    self.vel_motor2(speed)
    self.vel_motor3(speed)
    self.vel_motor4(speed)

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
    def vel_motor1(self,speed):

        speed = 0.67*speed
        self.pwm_m.ChangeDutyCycle(speed)
    	self.pwm_m.stop()

    def vel_motor2(self,speed):

        speed = 0.77*speed
        self.pwm_m.ChangeDutyCycle(speed)
        self.pwm_m.stop()

    def vel_motor3(self,speed):

        speed = 0.92*speed
        self.pwm_m.ChangeDutyCycle(speed)
    	self.pwm_m.stop()

    def vel_motor4(self,speed):

        self.pwm_m.ChangeDutyCycle(speed)
    	self.pwm_m.stop()

    #Servomotor control

	########Reminder: Initial state - angle 90; Prepare trowel - angle 180; EAT - angle: 0; Next food - angle 90 (loop)
    def turn_servo(self,angle):
        duty = angle/18 + 2
        G.output(3, True)
        self.pwm_sm.ChangeDutyCycle(duty)
	sleep(1)

        G.output(3, False)
	self.pwm_sm.ChangeDutyCycle(0)

    def hungry(self):

	#Open
	self.turn_servo(180)

	#Eat
	self.turn_servo(0)

	#Close
	self.turn_servo(90)


    def sleep(self):
        self.pwm_sm.stop()
        G.cleanup()
