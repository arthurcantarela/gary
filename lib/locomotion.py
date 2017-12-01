import sys, time
import RPi.GPIO as G
G.setmode(G.BCM)

class Locomotion():
    def __init__(self):
        """Set GPIOs controllers for motors"""

        # GPIOs controllers for left motors
        G.setup(5, G.OUT) # front
        G.setup(6, G.OUT) # back

        # GPIOs controllers for right motors

        G.setup(13,G.OUT) # front
        G.setup(19,G.OUT) # back

        # GPIOs controller for servomotor
        G.setup(3,G.OUT)

        # GPIO PWM setup

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

    def move(self, direction):
        pass

    def stop(self):
        G.output(5,False)
        G.output(6,False)
        G.output(13,False)
        G.output(19,False)

    def move_forward(self, seconds=None):
        G.output(5, True)
        G.output(6, True)
        G.output(13, True)
        G.output(19, True)

        if seconds != None:
            time.sleep(seconds)
            self.stop()

    def rotate_clockwise(self, degrees=None):
        G.output(5,True)
        G.output(6,False)
        G.output(13,False)
        G.output(19,False)

    def rotate_cclockwise(self, degrees=None):
        G.output(5,False)
        G.output(6,False)
        G.output(13,True)
        G.output(19,False)

    def set_velocity(self, speed):
        """Velocity control."""
        # M1
        speed = 0.67*speed
        self.pwm_m1.ChangeDutyCycle(speed)
        self.pwm_m1.stop()

        # M2
        speed = 0.77*speed
        self.pwm_m2.ChangeDutyCycle(speed)
        self.pwm_m2.stop()

        # M3
        speed = 0.92*speed
        self.pwm_m3.ChangeDutyCycle(speed)
        self.pwm_m3.stop()

        # M4
        self.pwm_m4.ChangeDutyCycle(speed)
        self.pwm_m4.stop()


    def turn_servo(self, degrees):
        """Set servos in the position degrees.
        Initial state: 90 degree"""
        duty = angle/18+2

        G.output(3, True)
        self.pwm_sm.ChangeDutyCycle(duty)

        time.sleep(1)

        G.output(3, False)
        self.pwm_sm.ChangeDutyCycle(0)



    def eat(self):
        """Anihilate the garbage."""
        # Open mouth
        self.turn_servo(180)
        # Go forward
        self.move_forward(8,50)
        time.sleep(1)
        self.move_forward(5,0)
        # Push gargabe
        self.turn_servo(60)
        # Close mouth
        self.turn_servo(90)


    def sleep(self):
        self.pwm_sm.stop()
        G.cleanup()
