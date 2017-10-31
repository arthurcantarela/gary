
import sys
import RPi.GPIO as G
from time import sleep
G.setmode(G.BCM)

# GPIOs controllers for left motors

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
pwm_sm = G.PWM(3,50)
pwm_m = G.PWM(18,100)

#Starts PWM cycle
pwm_sm.start(0)
pwm_m.start(0)

#Moves Gary for a direction
def MoveGary(direction):
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
def DriveGary(speed):

    #Stay
    if speed == 0:
        pwm_m.ChangeDutyCycle(0)

        #Low Speed
    if speed == 1:
        pwm_m.ChangeDutyCycle(30)

            #Regular Speed
    if speed == 2:
        pwm_m.ChangeDutyCycle(60)

                #High Speed
    if speed == 3:
        pwm_m.ChangeDutyCycle(100)


pwm_m.stop()

#Servomotor control
def ServoControl(angle):
    duty = angle/18 + 2
    GPIO.output(3, True)
    pwm_sm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3, False)

pwm_sm.stop()

G.cleanup()
